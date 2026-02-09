import frappe
import time
import random

def analyze_documents(loan_application_name):
	"""
	Simulates the DeepSeek AI Analysis.
	In a real scenario, this would call an OCR service and run business logic.
	"""
	loan_app = frappe.get_doc("Loan Application", loan_application_name)
	
	# Simulate processing time
	# Note: In production, this should be an asynchronous task (frappe.enqueue)
	
	results = {
		"status": "Success",
		"analysis": [
			{"task": "Analyzing income consistency...", "result": "Consistent"},
			{"task": "Verifying employer details...", "result": "Verified"},
			{"task": "Cross-referencing M-Pesa turnover...", "result": "Matched"},
			{"task": "DETECTING: Salary detected.", "result": "KSh 45,000"}
		],
		"confidence_score": 98,
		"risk_flags": []
	}
	
	# Mock some logic
	if random.random() < 0.1: # 10% chance of a flag
		results["risk_flags"].append("M-Pesa gambling transactions detected.")
		results["confidence_score"] = 85
		
	# Update the Loan Application with AI results (assuming fields exist or using custom fields)
	# For now, we'll just return the results. 
	# In Frappe, we might store this in a 'DeepSeek AI Result' JSON field or similar.
	
	return results

@frappe.whitelist()
def trigger_ai_analysis(loan_application):
	# This would be called from the frontend
	# For the purpose of the "DeepSeek screen", we might just wait or use a background job
	time.sleep(2) # Simulate work
	return analyze_documents(loan_application)
