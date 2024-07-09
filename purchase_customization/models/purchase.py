from odoo import api, fields, models


class PurchaseOrder(models.Model):
    _inherit = "purchase.order"
    phone = fields.Char(unaccent=False, related='partner_id.phone')
    Total_weight = fields.Float('Total Weight', compute="compute_totalweight",readonly=True)
    

    def compute_totalweight(self):
        for record in self:
            for line in record.order_line:
                record.Total_weight += line.weight