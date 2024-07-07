{
    'name': 'Demo Module',
    'summary':'',
    'author':"Aya Abdelmageed Abdelfattah",
    'version':'16.0',
    'category':'Hidden',
    'sequence':1,
    'depends':[
        'base',
        'contacts',
        'sale',
    ],
    'data':[
        'security/ir.model.access.csv',
        #'report/',
        'views/res_company_views.xml',
        'views/packages_views.xml',
        'views/sale_order_views.xml',
        'views/res_partner_views.xml',
        'views/res_port_views.xml',
        'reports/sale_order.xml',
        
        
        'views/demo_menus.xml',

    ],
    'installable':True,
    'application':True,
    'auto_install':False,
}