{
    'name': 'To-Do Application',
    'version': '1.0',
    'category': 'Tools',
    'description': 'Manage personal To-Do tasks',
    'author': 'Melinda Lim',
    'depends': ['base'],
    'application': True,
    'data': [
            'security/ir.model.access.csv',
            'security/todo_security_access_rules.xml',
            'views/todo_menu.xml',
            'views/todo_view.xml',
            'views/res_partner_view.xml',
            'views/index_template.xml',
            ],
    'installable': True,
}
