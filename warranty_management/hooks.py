# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "warranty_management"
app_title = "Warranty Management"
app_publisher = "DigiThinkIT, Inc."
app_description = "Warranty Management process"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "natalia@digithinkit.com"
app_version = "0.0.1"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/warranty_management/css/warranty_management.css"
# app_include_js = "/assets/warranty_management/js/warranty_management.js"

# include js, css files in header of web template
# web_include_css = "/assets/warranty_management/css/warranty_management.css"
# web_include_js = "/assets/warranty_management/js/warranty_management.js"

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#   "Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "warranty_management.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]
fixtures = [
    {
        "doctype": "Custom Field",
        "filters": [
            ["name", "in", (
               "Stock Entry-warranty_claim",
"Material Request-warranty_claim","Delivery Note-warranty_claim", "Sales Invoice-warranty_claim","Warranty Claim-is_paid"
            )]
        ]
    }
]
# Installation
# ------------

# before_install = "warranty_management.install.before_install"
# after_install = "warranty_management.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "warranty_management.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#   "Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#   "Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
    "Warranty Claim": {
        "before_save": "warranty_management.warranty_claim.before_save",
    },
}
# doc_events = {
#   "*": {
#       "on_update": "method",
#       "on_cancel": "method",
#       "on_trash": "method"
#   }
# }

# Scheduled Tasks
# ---------------

scheduler_events = {
    # "all": [
    #     "warranty_management.tasks.all"
    # ],
    "daily": [
        "warranty_management.tasks.daily"
    ],
    #   "hourly": [
    #       "warranty_management.tasks.hourly"
    # ],
    # "weekly": [
    #    "warranty_management.tasks.weekly"
    # ]
    # "monthly": [
    #    "warranty_management.tasks.monthly"
    # ]
}

# Testing
# -------

# before_tests = "warranty_management.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
#   "frappe.desk.doctype.event.event.get_events": "warranty_management.event.get_events"
# }

doctype_js = {
    "Warranty Claim": ["custom_scripts/warranty_claim.js"]
}
