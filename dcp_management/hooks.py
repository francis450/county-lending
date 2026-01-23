app_name = "dcp_management"
app_title = "DCP Management"
app_publisher = "Frappe"
app_description = "DCP LOS"
app_email = "dev@example.com"
app_license = "mit"

# Apps
# ------------------

# required_apps = []

# Each item in the list will be shown as an app in the apps page
# add_to_apps_screen = [
# 	{
# 		"name": "dcp_management",
# 		"logo": "/assets/dcp_management/logo.png",
# 		"title": "DCP Management",
# 		"route": "/dcp_management",
# 		"has_permission": "dcp_management.api.permission.has_app_permission"
# 	}
# ]

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/dcp_management/css/dcp_management.css"
# app_include_js = "/assets/dcp_management/js/dcp_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/dcp_management/css/dcp_management.css"
# web_include_js = "/assets/dcp_management/js/dcp_management.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "dcp_management/public/scss/website"

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

# Website Route Rules - Using www/portal.py instead
# ------------------
website_route_rules = [
	{"from_route": "/portal", "to_route": "portal"},
]


# Svg Icons
# ------------------
# include app icons in desk
# app_include_icons = "dcp_management/public/icons.svg"

# Home Pages
# ----------

# application home page (will override Website Settings)
home_page = "portal"

# website user home page (by Role)
role_home_page = {
	"Customer": "/portal"
}

# Website user home page (computed)
get_website_user_home_page = "dcp_management.utils.get_customer_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
# 	"methods": "dcp_management.utils.jinja_methods",
# 	"filters": "dcp_management.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "dcp_management.install.before_install"
# after_install = "dcp_management.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "dcp_management.uninstall.before_uninstall"
# after_uninstall = "dcp_management.uninstall.after_uninstall"

# Integration Setup
# ------------------
# To set up dependencies/integrations with other apps
# Name of the app being installed is passed as an argument

# before_app_install = "dcp_management.utils.before_app_install"
# after_app_install = "dcp_management.utils.after_app_install"

# Integration Cleanup
# -------------------
# To clean up dependencies/integrations with other apps
# Name of the app being uninstalled is passed as an argument

# before_app_uninstall = "dcp_management.utils.before_app_uninstall"
# after_app_uninstall = "dcp_management.utils.after_app_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "dcp_management.notifications.get_notification_config"

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

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"dcp_management.tasks.all"
# 	],
# 	"daily": [
# 		"dcp_management.tasks.daily"
# 	],
# 	"hourly": [
# 		"dcp_management.tasks.hourly"
# 	],
# 	"weekly": [
# 		"dcp_management.tasks.weekly"
# 	],
# 	"monthly": [
# 		"dcp_management.tasks.monthly"
# 	],
# }

# Testing
# -------

# before_tests = "dcp_management.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "dcp_management.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
# 	"Task": "dcp_management.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
before_request = ["dcp_management.utils.before_request"]
# after_request = ["dcp_management.utils.after_request"]

# Job Events
# ----------
# before_job = ["dcp_management.utils.before_job"]
# after_job = ["dcp_management.utils.after_job"]

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
# 	"dcp_management.auth.validate"
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

