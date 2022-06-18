# -*- coding: utf-8 -*-
{
    'name': 'Calculadora',
    'version': '1',
    'summary': 'Ejercicios',
    'sequence': -100,
    'description': """Calculadora (Curso-Pyhon-Odoo-2022)""",
    'author': 'Nelson Ivan Tontarelli',
    'maintainer': 'Nelson',
    'license': 'AGPL-3',
    'depends': [
        'sale',
        'mail',
            ],
    'data': [
        'views/calculadora.xml',
        'report/calculadora_report.xml',
        'report/report.xml',
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}