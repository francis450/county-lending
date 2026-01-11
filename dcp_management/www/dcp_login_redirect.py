import frappe

def get_context(context):
    """
    Redirects /login to the Custom Portal Login
    """
    frappe.local.response["type"] = "redirect"
    frappe.local.response["location"] = "/portal#/login"
    raise frappe.Redirect
