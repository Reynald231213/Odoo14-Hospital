# -*- coding: utf-8 -*-
{
    'name': "hospital",

    'summary': """
        Hospital
        """,

    'description': """
        Hospital Apps 
    """,

    'author': "Reynald S B",
    'website': "http://www.youtube.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'mail'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/patient.xml',
        'views/kids.xml',
        'views/appointment.xml',
        'wizard/create_appointment_view.xml',
        'wizard/search_appointment_view.xml',
        

    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}