import frappe
import os
from frappe import _
from frappe.utils import now, get_datetime

@frappe.whitelist(allow_guest=True)
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
        frappe.db.commit()
        
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

@frappe.whitelist()
def upload_kyc_documents(customer_id, national_id, files_data):
    """
    CBK Stage 2: KYC Document Upload
    Stores private files as per Data Protection Act
    """
    try:
        customer = frappe.get_doc("DCP Customer", customer_id)
        files = frappe.parse_json(files_data) if isinstance(files_data, str) else files_data
        
        # Update National ID
        customer.national_id = national_id
        
        # File uploads are handled separately via upload_file API
        # This method just updates the KYC status
        
        if customer.national_id_front and customer.national_id_back and customer.passport_photo:
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
def apply_for_loan(customer_id, amount, tenure, loan_product, consent_data):
    """
    CBK Stage 3: Loan Request Interface
    - Checks KYC status before proceeding
    - Logs consent for CRB check
    - Creates loan application
    """
    try:
        # Validate KYC status
        customer = frappe.get_doc("DCP Customer", customer_id)
        
        if customer.kyc_status != "Verified":
            return {
                "error": "KYC not completed",
                "kyc_required": True,
                "message": "Please complete your KYC verification before applying for a loan"
            }
        
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
        
        # Create loan application (mock - will integrate with Lending module)
        loan_app = {
            "customer_id": customer_id,
            "loan_amount": amount,
            "tenure": tenure,
            "loan_product": loan_product,
            "status": "Pending",
            "application_date": now()
        }
        
        frappe.log_error("Loan Application", message=str(loan_app))
        
        return {
            "status": "Submitted",
            "name": f"LOAN-{get_datetime().strftime('%Y%m%d%H%M%S')}",
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
