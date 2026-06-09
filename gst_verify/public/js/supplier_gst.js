frappe.ui.form.on("Supplier", {
    gstin: function(frm) {
        if (!frm.doc.gstin) {
            frm.set_value("gst_legal_name", null);
            frm.set_value("gst_status", null);
            frm.set_value("gst_state", null);
        }
    }
});