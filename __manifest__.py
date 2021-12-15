# -*- coding: utf-8 -*-
{
    'name': "validations_app",

    'summary': """
            Validation app
        """,

    'description': """
        An app that validates
    """,

    'author': "Josep",
    'website': "https://www.youtube.com/watch?v=uSX1eakWCiE&t=235s",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'security/ir.model.access.csv',
        'views/student_view.xml',
        'views/module_view.xml',
        'views/course_view.xml',
        'views/validation_view.xml',
        'views/menu.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],

    'application' : True,
    'installable' : True
}
