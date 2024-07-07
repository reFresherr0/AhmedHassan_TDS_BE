from odoo import fields,api,_, models

class Port(models.Model):
    _name = "res.port"
    
    name = fields.Char(string="name")