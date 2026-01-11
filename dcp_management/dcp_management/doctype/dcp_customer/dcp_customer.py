# Copyright (c) 2026, Frappe and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class DCPCustomer(Document):
	pass

def has_permission(doc, ptype, user):
	"""
	Custom permission check: Customers can only access their own DCP Customer records
	System Managers can access all records
	"""
	if "System Manager" in frappe.get_roles(user):
		return True
	
	# Customer role: can only access their own record
	if "Customer" in frappe.get_roles(user):
		if doc.user_link == user:
			return True
	
	return False
