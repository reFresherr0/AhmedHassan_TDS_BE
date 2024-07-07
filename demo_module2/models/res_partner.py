from odoo import fields,api,_, models

class ResPartner(models.Model):
    _inherit = "res.partner"

    ext_reg_no = fields.Integer(string="External Registration Number")
    po_box = fields.Integer(string="Po Box")
    partner_type= fields.Selection(selection=[
        ("customer", "Customer"),
        ("vendor", "Vendor"),
        ("employee", "Employee")],string="Partner Type")
    
    port_ids=fields.Many2many('res.port')


    