# -*- coding: utf-8 -*-
{
    'name': "vehicle_reservation",

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
    'images': ['static/description/icon.png'],

    # any module necessary for this one to work correctly
    'depends': ['base','mail' , 'fleet' , 'material_purchase_requisitions','branch' , 'product' , 'account'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/vehicle_reservation.xml',
        'views/rental_in_progress.xml',
        'views/service_type_product.xml',
        'views/rental_invoice_lines.xml',
        'wizard/booking_wizard.xml',
        'wizard/chauffeur_out_wizard.xml',
        'wizard/chauffeur_in_wizard.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
    ],
}
