import frappe
from frappe import _

@frappe.whitelist(allow_guest=True)
def post_password_update():
    """
    Called after successful password update to redirect to KYC page
    """
    if frappe.session.user and frappe.session.user != "Guest":
        # Check if user has DCP Customer with incomplete KYC
        customer = frappe.db.get_value(
            "DCP Customer",
            {"user_link": frappe.session.user},
            ["name", "kyc_status"],
            as_dict=True
        )
        
        if customer and customer.get("kyc_status") == "Incomplete":
            return {
                "redirect": "/portal#/kyc?new_user=1",
                "message": "Password updated successfully! Please complete your KYC verification."
            }
        elif customer:
            return {
                "redirect": "/portal#/dashboard",
                "message": "Welcome back!"
            }
    
    return {
        "redirect": "/portal",
        "message": "Password updated successfully!"
    }
