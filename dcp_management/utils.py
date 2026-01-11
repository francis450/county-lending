import frappe

def after_request():
    """
    Hook executed after each request.
    Handles redirection to KYC page after password reset for new DCP customers.
    """
    pass  # This hook is kept for future use

def before_request():
    """
    Hook executed before every request.
    Redirects Customers from /me to /portal.
    """
    path = frappe.request.path

    if path.rstrip("/") == "/me":
        if "Customer" in frappe.get_roles():
            target = get_customer_home_page(frappe.session.user) or "/portal"
            frappe.local.response["type"] = "redirect"
            frappe.local.response["location"] = target
            raise frappe.Redirect

def get_customer_home_page(user):
    """
    Returns the home page for the authenticated user based on their role and KYC status.
    Used by the get_website_user_home_page hook.
    """
    if "Customer" in frappe.get_roles(user):
        customer = frappe.db.get_value("DCP Customer", {"user_link": user}, ["name", "kyc_status"], as_dict=True)
        
        if customer:
            if customer.kyc_status == "Incomplete":
                # Redirect to KYC page if incomplete
                # Using Hash routing for the SPA
                return "/portal#/kyc"
            # Default customer portal
            return "/portal"
            
    return None

