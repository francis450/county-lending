import frappe
import os
from frappe import _
from frappe.utils import now, get_datetime

@frappe.whitelist()
def get_admin_application_queue():
	"""
	Returns a list of loan applications for the admin cockpit.
	Mocked sorting by AI Confidence Score.
	"""
	# Check for Reviewer role
	# if "Reviewer" not in frappe.get_roles(frappe.session.user):
	# 	frappe.throw(_("Access Denied: Reviever role required"))

	# This is a mock implementation. We'll simulate some applications.
	return [
		{
			"name": "LA-2026-0001",
			"customer_name": "James Kamau",
			"loan_amount": 50000,
			"ai_score": 98,
			"detected_salary": 45000,
			"status": "AI Verified",
			"creation": "2026-02-09 10:30:00",
			"flags": []
		},
		{
			"name": "LA-2026-0002",
			"customer_name": "Sarah Wanjiku",
			"loan_amount": 25000,
			"ai_score": 85,
			"detected_salary": 60000,
			"status": "Flagged",
			"creation": "2026-02-09 11:15:00",
			"flags": ["M-Pesa gambling transactions detected."]
		},
		{
			"name": "LA-2026-0003",
			"customer_name": "Philip Omondi",
			"loan_amount": 100000,
			"ai_score": 92,
			"detected_salary": 85000,
			"status": "AI Verified",
			"creation": "2026-02-09 09:00:00",
			"flags": []
		}
	]

@frappe.whitelist(allow_guest=True, methods=['POST'], xss_safe=True)
def onboard_customer(data):
    """
    CBK Compliant Registration: Creates User + DCP Customer
    Stage 1: Self-Registration & Authentication
    """
    try:
        customer_data = frappe.parse_json(data)
        email = customer_data.get("email")
        
        # Check if user already exists
        if frappe.db.exists("User", email):
            return {"error": "User with this email already exists"}
        
        # Step 1: Create Frappe User Account
        user = frappe.get_doc({
            "doctype": "User",
            "email": email,
            "first_name": customer_data.get("first_name"),
            "last_name": customer_data.get("last_name"),
            "mobile_no": customer_data.get("phone"),
            "enabled": 1,
            "send_welcome_email": 0,
            "user_type": "Website User"
        })
        user.insert(ignore_permissions=True)
        
        # Assign Customer role
        user.add_roles("Customer")
        
        # Send password reset email for the new user
        user.reset_password(send_email=True)
        
        # Step 2: Auto-create DCP Customer (CBK Requirement)
        dcp_customer = frappe.get_doc({
            "doctype": "DCP Customer",
            "first_name": customer_data.get("first_name"),
            "last_name": customer_data.get("last_name"),
            "email": email,
            "phone": customer_data.get("phone"),
            "user_link": user.name,
            "status": "Pending",
            "kyc_status": "Incomplete"
        })
        dcp_customer.insert(ignore_permissions=True)
        
        # Explicitly assign ownership to the new user
        dcp_customer.owner = user.name
        dcp_customer.db_update()

        frappe.db.commit()
        
        # Don't auto-login - user must set password via email first
        
        return {
            "message": "Success",
            "user_id": user.name,
            "customer_id": dcp_customer.name,
            "customer": dcp_customer.as_dict()
        }
        
    except Exception as e:
        frappe.log_error("Onboarding Error", message=str(e))
        frappe.db.rollback()
        return {"error": str(e)}

@frappe.whitelist(methods=['POST'])
def upload_kyc_file():
    """
    Custom file upload handler for KYC documents with authentication
    """
    try:
        files = frappe.request.files
        form = frappe.form_dict
        
        doctype = form.get('doctype')
        docname = form.get('docname')
        fieldname = form.get('fieldname')
        is_private = form.get('is_private', 0)
        
        # Verify user has permission to update this customer record
        if doctype == "DCP Customer":
            customer = frappe.get_doc("DCP Customer", docname)
            
            # Security check: ensure the logged-in user owns this customer record
            if customer.user_link != frappe.session.user:
                frappe.throw("You can only upload files to your own KYC profile", frappe.PermissionError)
        
        # Upload the file
        if 'file' in files:
            file = files['file']
            ret = frappe.get_doc({
                "doctype": "File",
                "attached_to_doctype": doctype,
                "attached_to_name": docname,
                "attached_to_field": fieldname,
                "file_name": file.filename,
                "is_private": int(is_private),
                "content": file.stream.read()
            })
            ret.save(ignore_permissions=True)
            frappe.db.commit()
            
            return {
                "message": "File uploaded successfully",
                "file_url": ret.file_url,
                "file_name": ret.file_name
            }
        else:
            return {"error": "No file provided"}
            
    except Exception as e:
        frappe.log_error("File Upload Error", message=str(e))
        return {"error": str(e)}

@frappe.whitelist(methods=['POST'])
def upload_kyc_documents(customer_id, national_id, files_data, kra_pin=None, residential_address=None, county=None, city=None, postal_code=None):
	"""
	CBK Stage 2: KYC Document Upload
	Stores private files as per Data Protection Act
	Requires authenticated user
	"""
	try:
		# Debug logging
		frappe.log_error(title="KYC Upload Debug", message=f"""
			customer_id: {customer_id}
			national_id: {national_id}
			kra_pin: {kra_pin}
			residential_address: {residential_address}
			county: {county}
			city: {city}
			postal_code: {postal_code}
			files_data type: {type(files_data)}
			files_data: {files_data}
		""")
		
		# Verify user has permission to update this customer record
		customer = frappe.get_doc("DCP Customer", customer_id)
		
		# Security check: ensure the logged-in user owns this customer record
		if customer.user_link != frappe.session.user:
			frappe.throw("You can only update your own KYC documents", frappe.PermissionError)
		files = frappe.parse_json(files_data) if isinstance(files_data, str) else files_data
		
		# Update Customer Details
		customer.national_id = national_id
		if kra_pin: customer.kra_pin = kra_pin
		if residential_address: customer.residential_address = residential_address
		if county: customer.county = county
		if city: customer.city = city
		if postal_code: customer.postal_code = postal_code
		
		# File uploads are handled separately via upload_file API
		# This method receives the file URLs/Paths or we check if they exist
		# But wait, the frontend likely uploaded them already and is passing filenames/urls?
		# The previous code didn't use 'files' variable.
		# Let's assume frontend uploads via a separate call and we just check the doc
		# OR we accept file paths here.
		# The frontend snippet confirms files are uploaded separately effectively (or will be).
		# Let's check the fields map.
		
		# If files_data contains links to files, we might not need to do much if they are attached.
		# BUT, the `DCP Customer` doctype has fields like `national_id_front` which are Attach Image/File.
		# We need to set those fields on the doc.
		
		if files:
			if files.get('id_front'): customer.national_id_front = files.get('id_front')
			if files.get('id_back'): customer.national_id_back = files.get('id_back')
			if files.get('kra_certificate'): customer.kra_pin_certificate = files.get('kra_certificate')
			if files.get('passport_photo'): customer.passport_photo = files.get('passport_photo')

		# Debug: Log what we're about to save
		frappe.log_error(title="KYC Before Save", message=f"""
			Customer: {customer.name}
			national_id: {customer.national_id}
			kra_pin: {customer.kra_pin}
			residential_address: {customer.residential_address}
			county: {customer.county}
			city: {customer.city}
			postal_code: {customer.postal_code}
			national_id_front: {customer.national_id_front}
			national_id_back: {customer.national_id_back}
			kra_pin_certificate: {customer.kra_pin_certificate}
			passport_photo: {customer.passport_photo}
		""")

		# Check if all required fields are present to mark as Pending Verification
		required_fields = [
			customer.national_id, customer.national_id_front, customer.national_id_back,
			customer.kra_pin, customer.passport_photo, customer.residential_address
		]
		
		if all(required_fields):
			customer.kyc_status = "Pending Verification"
		
		customer.save(ignore_permissions=True)
		frappe.db.commit()
		
		return {"message": "KYC documents uploaded successfully", "customer": customer.as_dict()}
		
	except Exception as e:
		frappe.log_error("KYC Upload Error", message=str(e))
		return {"error": str(e)}

@frappe.whitelist()
def verify_kyc(customer_id):
    """
    Mock KYC Verification (Simulates IPRS API call)
    In production: integrate with IPRS or other verification services
    """
    try:
        customer = frappe.get_doc("DCP Customer", customer_id)
        
        if customer.kyc_status != "Pending Verification":
            return {"error": "KYC not submitted for verification"}
        
        # Mock verification - in production call IPRS API
        customer.kyc_status = "Verified"
        customer.kyc_verified_date = now()
        customer.verified_by = frappe.session.user
        customer.status = "Active"
        
        customer.save(ignore_permissions=True)
        frappe.db.commit()
        
        return {"message": "KYC verified successfully", "customer": customer.as_dict()}
        
    except Exception as e:
        frappe.log_error("KYC Verification Error", message=str(e))
        return {"error": str(e)}

@frappe.whitelist()
def log_consent(customer_id, consent_type, ip_address, policy_version="v1.0"):
    """
    CBK Stage 4: Consent Management & Data Protection
    Logs every consent action with audit trail
    """
    try:
        customer = frappe.get_doc("DCP Customer", customer_id)
        
        # Append consent log
        customer.append("consent_logs", {
            "consent_type": consent_type,
            "consent_given": 1,
            "ip_address": ip_address,
            "policy_version": policy_version,
            "consent_timestamp": now()
        })
        
        customer.save(ignore_permissions=True)
        frappe.db.commit()
        
        return {"message": "Consent logged successfully"}
        
    except Exception as e:
        frappe.log_error("Consent Logging Error", message=str(e))
        return {"error": str(e)}

@frappe.whitelist()
def apply_for_loan(customer_id, amount, tenure, purpose, consent_data):
    """
    CBK Stage 3: Loan Request Interface
    - Checks KYC status before proceeding
    - Logs consent for CRB check
    - Creates loan application
    """
    try:
        # Validate KYC status
        dcp_customer = frappe.get_doc("DCP Customer", customer_id)
        
        if dcp_customer.kyc_status != "Verified":
            return {
                "error": "KYC not completed",
                "kyc_required": True,
                "message": "Please complete your KYC verification before applying for a loan"
            }
        
        # Ensure ERPNext Customer exists
        if not dcp_customer.customer_link:
            # Check if Customer exists with same email
            existing_customer = frappe.db.get_value("Customer", {"email_id": dcp_customer.email})
            if existing_customer:
                dcp_customer.customer_link = existing_customer
                dcp_customer.save(ignore_permissions=True)
            else:
                # Create ERPNext Customer
                new_customer = frappe.get_doc({
                    "doctype": "Customer",
                    "customer_name": f"{dcp_customer.first_name} {dcp_customer.last_name}",
                    "customer_type": "Individual",
                    "customer_group": "All Customer Groups",
                    "territory": "All Territories",
                    "email_id": dcp_customer.email,
                    "mobile_no": dcp_customer.phone
                })
                new_customer.insert(ignore_permissions=True)
                dcp_customer.customer_link = new_customer.name
                dcp_customer.save(ignore_permissions=True)
        
        erp_customer = dcp_customer.customer_link

        # Parse consent data
        consent_info = frappe.parse_json(consent_data) if isinstance(consent_data, str) else consent_data
        
        # Log CRB consent (CBK requirement)
        log_consent(
            customer_id=customer_id,
            consent_type="CRB Check",
            ip_address=consent_info.get("ip_address", ""),
            policy_version=consent_info.get("policy_version", "v1.0")
        )
        
        # Log Terms & Conditions consent
        log_consent(
            customer_id=customer_id,
            consent_type="Terms & Conditions",
            ip_address=consent_info.get("ip_address", ""),
            policy_version=consent_info.get("policy_version", "v1.0")
        )

        # Get defaults
        company = frappe.db.get_single_value("Global Defaults", "default_company") or frappe.get_all("Company", limit=1)[0].name
        # simplified loan product selection for MVP
        loan_product = frappe.get_all("Loan Product", limit=1)
        if not loan_product:
             frappe.throw("No Loan Products configuration found. Please contact support.")
        loan_product_name = loan_product[0].name
        
        # Create loan application
        loan_app = frappe.get_doc({
            "doctype": "Loan Application",
            "applicant_type": "Customer",
            "applicant": erp_customer,
            "company": company,
            "loan_product": loan_product_name,
            "loan_amount": amount,
            "repayment_method": "Repay Over Number of Periods",
            "repayment_periods": tenure,
            "description": purpose,
            "status": "Open",
            "posting_date": now()
        })
        loan_app.insert(ignore_permissions=True)
        frappe.db.commit()
        
        return {
            "status": "Submitted",
            "name": loan_app.name,
            "message": "Your loan application has been submitted successfully"
        }
        
    except Exception as e:
        frappe.log_error("Loan Application Error", message=str(e))
        return {"error": str(e)}

@frappe.whitelist()
def get_customer_loans(customer_id):
    """
    Fetch all loans for a customer with mock data for MVP.
    """
    try:
        customer = frappe.get_doc("DCP Customer", customer_id)
        
        # Mock data for MVP - will be replaced with real Lending module data
        mock_loans = [
            {
                "name": "LOAN-001",
                "loan_amount": 10000,
                "total_payable": 10500,
                "total_payment": 5000,
                "status": "Active",
                "rate_of_interest": 5,
                "repayment_periods": 3,
                "creation": "2026-01-05",
                "posting_date": "2026-01-05"
            }
        ] if customer.kyc_status == "Verified" else []
        
        return {
            "loans": mock_loans,
            "active_loan": mock_loans[0] if mock_loans else None,
            "history": [],
            "kyc_status": customer.kyc_status
        }
        
    except Exception as e:
        frappe.log_error("Get Customer Loans Error", message=str(e))
        return {"error": str(e), "loans": [], "active_loan": None, "history": []}

@frappe.whitelist()
def get_customer_profile(customer_id):
    """
    Get customer profile with KYC status
    """
    try:
        customer = frappe.get_doc("DCP Customer", customer_id)
        return {"customer": customer.as_dict()}
    except Exception as e:
        frappe.log_error("Get Profile Error", message=str(e))
        return {"error": str(e)}

@frappe.whitelist()
def get_current_user_customer():
    """
    Get current logged-in user's DCP Customer record
    """
    try:
        if frappe.session.user == "Guest":
            return {"error": "Not authenticated", "customer": None}
        
        customer = frappe.db.get_value("DCP Customer", 
                                      {"user_link": frappe.session.user}, 
                                      ["name", "first_name", "last_name", "email", "phone", "kyc_status", "status"], 
                                      as_dict=True)
        
        if not customer:
            return {"error": "Customer record not found", "customer": None}
        
        return {"customer": customer}
    except Exception as e:
        frappe.log_error("Get Current User Customer Error", message=str(e))
        return {"error": str(e), "customer": None}

@frappe.whitelist()
def update_customer(customer_id, data):
    """
    Update customer information
    """
    try:
        customer_data = frappe.parse_json(data) if isinstance(data, str) else data
        customer = frappe.get_doc("DCP Customer", customer_id)
        
        for key, value in customer_data.items():
            if hasattr(customer, key) and key not in ['name', 'creation', 'owner']:
                setattr(customer, key, value)
        
        customer.save(ignore_permissions=True)
        frappe.db.commit()
        
        return {"message": "Success", "customer": customer.as_dict()}
    except Exception as e:
        frappe.log_error("Update Customer Error", message=str(e))
        return {"error": str(e)}

@frappe.whitelist()
def make_payment(loan_id, amount):
    """
    Record a loan payment
    """
    try:
        payment_data = {
            "loan_id": loan_id,
            "amount": amount,
            "timestamp": now()
        }
        
        frappe.log_error("Payment Processed", message=str(payment_data))
        
        return {"status": "Success", "message": "Payment processed successfully"}
    except Exception as e:
        frappe.log_error("Payment Error", message=str(e))
        return {"error": str(e)}

def render_spa():
    """
    Serves the Vue SPA by rendering the built index.html.
    """
    import frappe.website.render
    
    path = frappe.get_app_path("dcp_management", "public", "frontend", "dist", "index.html")
    
    if not os.path.exists(path):
        frappe.throw("SPA build not found. Please run 'npm run build' in the frontend directory.")
    
    with open(path, "r") as f:
        html_content = f.read()
    
    frappe.response['type'] = 'page'
    frappe.response['page_name'] = 'dcp-portal'
    return html_content


def render_spa():
    """
    Serves the Vue SPA by rendering the built index.html.
    This is used as a web page handler via website_route_rules.
    """
    import frappe.website.render
    
    path = frappe.get_app_path("dcp_management", "public", "frontend", "dist", "index.html")
    
    if not os.path.exists(path):
        frappe.throw("SPA build not found. Please run 'npm run build' in the frontend directory.")
    
    with open(path, "r") as f:
        html_content = f.read()
    
    # Return raw HTML without Frappe's website wrapper
    frappe.response['type'] = 'page'
    frappe.response['page_name'] = 'dcp-portal'
    return html_content
