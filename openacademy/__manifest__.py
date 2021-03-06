# -*- coding: utf-8 -*-
{
    'name': "openacademy",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/openerp/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['mail', 'website'],

    # always loaded
    'data': [
        'security/groups.xml',
        'security/ir.model.access.csv',
        'security/irrules.xml',
        'views/course.xml',
        'views/session.xml',
        'views/partner.xml',
        'views/entity.xml',
        'views/menu.xml',
        'views/wizard.xml',
        'views/templates.xml',
        'views/sessionanalysis.xml',
        'views/reports.xml',
        'datas/category.xml',
        'datas/entity.xml',
        'datas/session_workflow.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
