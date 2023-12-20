# -*- coding: utf-8 -*-

{
    'name': 'Display Sale order date in invoice report',
    'version': '1.0.1.1',
    'author':'Soft-integration',
    'category': 'Accounting',
    'description': "",
    'depends': [
        'sale','account'
    ],
    'data': [
        'views/report_invoice.xml',
        'views/res_config_settings_view.xml'
    ],
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}
