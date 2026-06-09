import frappe
import requests
import re

GST_STATE_MAP = {
    "01": "Jammu & Kashmir", "02": "Himachal Pradesh",
    "03": "Punjab", "04": "Chandigarh", "05": "Uttarakhand",
    "06": "Haryana", "07": "Delhi", "08": "Rajasthan",
    "09": "Uttar Pradesh", "10": "Bihar", "11": "Sikkim",
    "12": "Arunachal Pradesh", "13": "Nagaland", "14": "Manipur",
    "15": "Mizoram", "16": "Tripura", "17": "Meghalaya",
    "18": "Assam", "19": "West Bengal", "20": "Jharkhand",
    "21": "Odisha", "22": "Chhattisgarh", "23": "Madhya Pradesh",
    "24": "Gujarat", "27": "Maharashtra", "29": "Karnataka",
    "32": "Kerala", "33": "Tamil Nadu", "36": "Telangana",
    "37": "Andhra Pradesh",
}

GSTIN_PATTERN = r'^\d{2}[A-Z]{5}\d{4}[A-Z]{1}[A-Z\d]{1}Z[A-Z\d]{1}$'

def validate_and_fetch_gst(doc, method):
    """
    Triggered on Supplier before_save.
    Validates GSTIN format and fetches details from GST API.
    """

    gstin = doc.get("gstin")

    if not gstin:
        return

    gstin = gstin.strip().upper()
    if not re.match(GSTIN_PATTERN, gstin):
        frappe.throw("Invalid GSTIN format. Example: 33AAPFU0939F1ZV")

    # Get state from first 2 digits
    state_code = gstin[:2]
    doc.gst_state = GST_STATE_MAP.get(state_code, "Unknown")

    # Get API key from GST Settings DocType
    api_key = frappe.db.get_single_value("GST Settings", "gst_api_key")
    if not api_key:
        frappe.throw("GST API key not configured. Go to GST Settings.")

    try:
        response = requests.get(
            f"https://gst-verification-api-get-profile-returns-data.p.rapidapi.com/v1/gstin/{gstin}/details",
            headers={
                "x-rapidapi-key": api_key,
                "x-rapidapi-host": "gst-verification-api-get-profile-returns-data.p.rapidapi.com",
                "Content-Type": "application/json"
            },
            timeout=10
        )

        if response.status_code == 200:
            # ✅ data is nested inside "data" key
            data = response.json().get("data", {})

            # ✅ Correct field names from actual API response
            doc.gst_legal_name = data.get("legal_name", "")
            doc.gst_status = data.get("status", "")
            doc.gst_business_type = data.get("business_constitution", "")

            frappe.msgprint(
                f"✅ GST Verified: {doc.gst_legal_name} | {doc.gst_status}",
                alert=True
            )
        else:
            frappe.msgprint(
                f"⚠️ Could not verify GST. Status: {response.status_code}",
                alert=True
            )

    except requests.exceptions.Timeout:
        frappe.msgprint("GST API timeout. Saved without verification.")
    except Exception as e:
        frappe.log_error(f"GST Verify Error: {str(e)}", "GST Verification")
        frappe.msgprint("GST API error. Check error log.")