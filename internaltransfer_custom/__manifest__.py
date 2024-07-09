{
    'name': 'InternalTransfer Custom',
    'summary':'',
    'author':"Ahmed Hassan",
    'version':'16.0',
    'category':'Hidden',
    'sequence':1,
    'depends':[
        'base',
        'contacts',
        'stock',
        
    ],
    'data':[
        'views/stock_picking_views.xml'
        # 'security/ir.model.access.csv',
        # 'views/packages_views.xml',
        # 'views/sale_order_views.xml',
        # 'views/res_partner_views.xml',
        # 'views/res_port_views.xml',
        # 'reports/sale_order.xml',
        # 'views/demo_menus.xml',

    ],
    'installable':True,
    'application':True,
    'auto_install':False,
}