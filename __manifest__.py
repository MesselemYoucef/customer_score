# -*- coding: utf-8 -*-
{
    'name': 'Customer Score',
    'version': '1.0',
    'summary': 'Calculate the customer score based on his activity with the company',
    'sequence': -102,
    'description': """Calculate the customer score based on his activity with the company""",
    'category': 'Productivity',
    'website': 'https://www.odoo.com',
    'Licence': 'LGPL-3',
    'images': [],
    'depends': [
        'base',
        'sale',
        'product'
    ],
    'data': [
        "views/product_view.xml",
        "views/customer_view.xml"
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
