import frappe

def execute():
    """
    Fixes ownership of DCP Customer documents.
    Sets the 'owner' field to match the 'user_link' field for all DCP Customers.
    """
    customers = frappe.get_all("DCP Customer", fields=["name", "user_link", "owner"])
    
    count = 0
    for customer in customers:
        if customer.user_link and customer.owner != customer.user_link:
            frappe.db.set_value("DCP Customer", customer.name, "owner", customer.user_link)
            count += 1
            
    print(f"Fixed ownership for {count} DCP Customers")
