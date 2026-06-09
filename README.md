# GST Verify — Frappe/ERPNext App

Auto-verifies GSTIN when a new Supplier is created in ERPNext.

## 🔧 What It Does
- Validates GSTIN format using regex
- Calls GST Verification REST API
- Auto-fills Legal Name, GST Status, Business Type, State
- Secure API key storage via custom GST Settings DocType

## 📸 Demo
<img width="1536" height="1024" alt="image" src="https://github.com/user-attachments/assets/00598519-69ec-4929-9873-0fa8352d3679" />


## 🛠️ Tech Stack
Python | Frappe Framework | ERPNext | REST API | MySQL

## ⚙️ Installation
1. bench get-app https://github.com/Kowsi2211/gst-verify-frappe
2. bench --site your-site install-app gst_verify
3. Go to GST Settings → enter your RapidAPI key
