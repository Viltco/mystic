# -*- coding: utf-8 -*-
{
    'name': "branch_customization",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "M.Rizwan",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'branch', 'account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/inherited_branch_view.xml',
        'views/inherited_account_tag_view.xml',
        'views/inherited_account_invoice.xml',
        'views/inherited_account_payment_wizard_view.xml',
        'views/inherited_account_journal.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
