app_name = "gst_verify"
app_title = "Gst Verify"
app_publisher = "kowsalya"
app_description = "gst verfication on supplier creation"
app_email = "kowsalya.craftinteractive@gmail.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "gst_verify",
# 		"logo": "/assets/gst_verify/logo.png",
# 		"title": "Gst Verify",
# 		"route": "/gst_verify",
# 		"has_permission": "gst_verify.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/gst_verify/css/gst_verify.css"
# app_include_js = "/assets/gst_verify/js/gst_verify.js"

# include js, css files in header of web template
# web_include_css = "/assets/gst_verify/css/gst_verify.css"
# web_include_js = "/assets/gst_verify/js/gst_verify.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "gst_verify/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}
doctype_js = {
    "Supplier": "public/js/supplier_gst.js"
}
# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "gst_verify/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
# 	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "gst_verify.utils.jinja_methods",
# 	"filters": "gst_verify.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "gst_verify.install.before_install"
# after_install = "gst_verify.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "gst_verify.uninstall.before_uninstall"
# after_uninstall = "gst_verify.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "gst_verify.utils.before_app_install"
# after_app_install = "gst_verify.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "gst_verify.utils.before_app_uninstall"
# after_app_uninstall = "gst_verify.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "gst_verify.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
# 	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
# 	}
# }
doc_events = {
    'Supplier': {
        "before_save": "gst_verify.events.supplier_gst.validate_and_fetch_gst"
    }
}
fixtures = [
    {
        "dt": "Custom Field",
        "filters": [
            ["module", "=", "GST Verify"],
        ]

    },
    {
        "dt": "Property Setter",
        "filters": [
            ["module", "=", "GST Verify"],
        ]
    }
]

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"gst_verify.tasks.all"
# 	],
# 	"daily": [
# 		"gst_verify.tasks.daily"
# 	],
# 	"hourly": [
# 		"gst_verify.tasks.hourly"
# 	],
# 	"weekly": [
# 		"gst_verify.tasks.weekly"
# 	],
# 	"monthly": [
# 		"gst_verify.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "gst_verify.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "gst_verify.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "gst_verify.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["gst_verify.utils.before_request"]
# after_request = ["gst_verify.utils.after_request"]

# Job Events
# ----------
# before_job = ["gst_verify.utils.before_job"]
# after_job = ["gst_verify.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
# 	{
# 		"doctype": "{doctype_1}",
# 		"filter_by": "{filter_by}",
# 		"redact_fields": ["{field_1}", "{field_2}"],
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_2}",
# 		"filter_by": "{filter_by}",
# 		"partial": 1,
# 	},
# 	{
# 		"doctype": "{doctype_3}",
# 		"strict": False,
# 	},
# 	{
# 		"doctype": "{doctype_4}"
# 	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
# 	"gst_verify.auth.validate"
# ]

# Automatically update python controller files with type annotations for this app.
# export_python_type_annotations = True

# default_log_clearing_doctypes = {
# 	"Logging DocType Name": 30  # days to retain logs
# }

# Translation
# ------------
# List of apps whose translatable strings should be excluded from this app's translations.
# ignore_translatable_strings_from = []

