{
    'name': 'Edu Module',
    'version': '1.0',
    'summary': 'Educational Odoo module',
    'description': """
    A simple module was created for educational purposes
    """,
    'depends': ['base'],
    'author': 'Serhii Miroshnychenko',
    'license': 'LGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'views/demo_model_views.xml',
        'views/edu_menus.xml',
        'views/demo_model_tree.xml',
        'views/demo_model_kanban.xml',
        'views/demo_model_form.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}