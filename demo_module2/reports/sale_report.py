from odoo import fields,api,_, models
from odoo.exceptions import ValidationError


class SaleReport(models.Model):
    _inherit = "sale.report"



    y=fields.Integer()



    def _select_additional_fields(self):
        res = super(SaleReport,self)._select_additional_fields()
        return{
            'y':'s.y',
        }
    
