from odoo import http
from odoo.http import request
import json


class SalesOrderController(http.Controller):
    
    @http.route('/get_sales_orders', type='http', auth='public', methods=['GET'])
    def get_sales_orders(self, **kwargs):
        sales_orders = request.env['sale.order'].sudo().search([])

        orders_data = []
        for order in sales_orders:
            order_data = {
                'id': order.id,
                'name': order.name,
                'partner_id': order.partner_id.name,
                'total_amount': order.amount_total,
                'test_field': order.test_field,
                'x': order.x,
                'y': order.y,
                'z': order.z,
            }
            orders_data.append(order_data)

        return request.make_response(
            data=json.dumps(orders_data),
            headers=[('Content-Type', 'application/json')],
        )
