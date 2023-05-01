{
    'name': "Medical Shop",
    'version': '1.0',
    'depends': ['base'],
    'author': "Vishal Verma",
    'category': 'Category',
    'description': """
    Description text
    """,
    # data files always loaded at installation
    'data': [
        'security/ir.model.access.csv',
        'views/drugs_property_view.xml',
        'views/drugs_order_lines_view.xml',
        'views/drugs_property_tag_view.xml',
        'views/drugs_order_view.xml',
        'views/drugs_customer_view.xml',
        'views/drugs_menu.xml',

    ],
    # data files containing optionally loaded demonstration data
    'demo': [
      
    ],
    'application':True,
    'instalation':True,
}