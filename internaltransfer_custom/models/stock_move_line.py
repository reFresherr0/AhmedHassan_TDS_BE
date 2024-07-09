from odoo import api, fields, models,_
from odoo.exceptions import UserError, ValidationError


class StockMoveLine(models.Model):
    _inherit = 'stock.move.line'
    
    yds_quantity = fields.Float(compute="ahmed_compute")
    
    @api.depends('product_uom_id')
    def ahmed_compute(self):
        for line in self:
            quant = self.env['stock.quant'].search([('product_id', '=', line.product_id.id), ('location_id', '=', line.location_id.id)]).available_quantity
            qty = line.product_id.uom_id._compute_quantity(quant, line.product_uom_id, )
            line.yds_quantity = qty
            
   

