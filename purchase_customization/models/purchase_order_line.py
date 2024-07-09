from odoo import api, fields, models

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'
    weight = fields.Float('Weight', digits='Stock Weight', related = 'product_id.weight')
