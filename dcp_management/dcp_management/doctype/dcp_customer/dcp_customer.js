// Copyright (c) 2026, Frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('DCP Customer', {
	refresh: function(frm) {
        // Add the button if the document is saved
        if (!frm.is_new()) {
            frm.add_custom_button(__('Run AI Verification'), function() {
                frappe.call({
                    method: 'run_ai_verification',
                    doc: frm.doc,
                    callback: function(r) {
                        if (r.message) {
                            frappe.msgprint(r.message);
                        }
                    }
                });
            }).addClass('btn-primary');
        }

        // Real-time updates
        frappe.realtime.on("dcp_customer_ai_update", function(data) {
            if (data.doc_name === frm.doc.name) {
                frm.set_value(data.field, data.result);
                frappe.show_alert({
                    message: __("AI Verification Complete"),
                    indicator: 'green'
                }, 5);
            }
        });
	},

    run_ai_verification: function(frm) {
        frappe.call({
            method: "dcp_management.dcp_management.doctype.dcp_customer.dcp_customer.DCPCustomer.run_ai_verification",
            args: {
                doc_name: frm.doc.name
            },
            callback: function(r) {
                // The backend will show the initial message
            }
        });
    }
});
