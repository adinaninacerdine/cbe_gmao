# -*- coding: utf-8 -*-
{
    'name': "cbe_gmao",

    'summary': """
        Ectension du module maintenance""",

    'description': """
        Ce module permet d'automatiser la sortie de stock des pieces de rechange lors de chaque opération de maintenance
    """,

    'author': "Green Relaods",
    'website': "http://www.greenreloads.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','maintenance', 'stock'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/maintenance_views.xml',
        'data/ir_cron_data.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}