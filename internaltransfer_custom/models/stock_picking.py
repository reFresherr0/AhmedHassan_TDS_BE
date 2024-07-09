from odoo import api, fields, models,_
from odoo.exceptions import UserError, ValidationError


class StockPicking(models.Model):
    _inherit = 'stock.picking'  # inheriting from stock.picking
    
    
    @api.constrains('move_line_ids_without_package')
    def check_avail(self):
        for record in self:
            for line in record.move_line_ids_without_package:
                if line.qty_done > line.yds_quantity:   
                    raise ValidationError(_('There is not enough stock in the inventory'))