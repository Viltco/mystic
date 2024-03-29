# -*- coding: utf-8 -*-
{
    'name': "res_partner_customization",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base' , 'hr','contacts' , 'select_multiple_models' ,'de_shift_attendance' , 'mystic_fuel_integration'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/views.xml',
        'views/hr_employee.xml',
        'views/contracts.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
