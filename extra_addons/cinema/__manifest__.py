{
    'name': "Cinema module",
    'version': '16.1.1',
    'depends': [
        'base',
        'mail'
    ],
    'author': "Author Name",
    'category': '',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/cinema_cinema_views.xml',
        'views/cinema_cinema_hall_views.xml',
        'views/cinema_cinema_movie_views.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
