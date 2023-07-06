# -*- coding: utf-8 -*-
{
    'name': "Gestión de Garajes",

    'summary': """
        Gestión de colecciones de coches en aparcamientosm""",

    'description': """
        Modulo de pruebas
    """,

    'author': "Pau Gallego",
    'website': "paugallego",

    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/garaje_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    # Indicamos que es una aplicacion
    'application': True,
}
