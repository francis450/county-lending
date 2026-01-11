import frappe

def get_context(context):
    """
    Serve the Vue SPA at /portal route without Frappe website wrapper.
    """
    context.no_cache = 1
    context.no_breadcrumbs = True
    
    # Tell Frappe to skip the standard website template
    frappe.response['type'] = 'page'
    
    return context
