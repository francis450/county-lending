# Copyright (c) 2026, Frappe and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document
from dcp_management.services.deepseek_service import analyze_document_with_vision

class DCPCustomer(Document):
	@frappe.whitelist()
	def run_ai_verification(self):
		"""
		Triggered by the 'Run AI Verification' button.
		This method orchestrates the analysis of all relevant KYC documents.
		"""
		if not self.national_id_front:
			frappe.throw("National ID (Front) is missing.")

		# Use the raw file path so the service can read private files directly from disk
		file_url = self.national_id_front

		prompt = """
		Analyze the provided Kenyan National ID. Extract the following information:
		- Full Names
		- ID Number
		- Date of Birth
		- Gender
		- District of Birth
		Also, check for any signs of tampering or if it looks like a forgery.
		Summarize your findings clearly.
		"""

		frappe.msgprint("Starting AI analysis of National ID. This may take a moment...", title="AI Verification")

		# Run in background
		frappe.enqueue(
			run_document_analysis,
			doc_name=self.name,
			file_url=file_url,
			prompt=prompt,
			result_field="ai_verification_summary"
		)

@frappe.whitelist()
def run_document_analysis(doc_name, file_url, prompt, result_field):
	"""
	Background job to call the DeepSeek API and update the document.
	"""
	try:
		# Call the service
		result = analyze_document_with_vision(
			file_url, prompt,
			reference_doctype="DCP Customer",
			reference_name=doc_name,
		)

		# Update the document
		frappe.db.set_value("DCP Customer", doc_name, result_field, result, update_modified=False)
		frappe.db.commit()

		# Notify user via socket
		frappe.publish_realtime(
			"dcp_customer_ai_update",
			{"doc_name": doc_name, "field": result_field, "result": result},
			user=frappe.session.user
		)

	except Exception as e:
		frappe.log_error(f"AI analysis failed: {e}", "DCP Customer AI Error")
		frappe.db.set_value("DCP Customer", doc_name, result_field, f"An error occurred during analysis: {e}", update_modified=False)
		frappe.db.commit()


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
