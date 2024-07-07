from odoo import fields,api,_, models
from odoo.exceptions import ValidationError


READONLY_FIELD_STATES = {
    state: [('readonly', True)]
    for state in {'sale', 'done', 'cancel'}
}

class SaleOrder(models.Model):
    _inherit = "sale.order"
    
    test_field = fields.Char(string="Test") 
    test2_field=fields.Char(string="Test2")
    x=fields.Integer()
    y=fields.Integer()
    z=fields.Integer(compute="ahmed_compute",store=True,readonly=False)
    ext_reg_no = fields.Integer(string="External Registration Number")
    partner_id = fields.Many2one(
        comodel_name='res.partner',
        string="Customer",
        readonly=False, change_default=True, index=True,
        tracking=1,
        store=True,
        compute="compute_customer",
        states=READONLY_FIELD_STATES,
        domain="[('type', '!=', 'private'), ('company_id', 'in', (False, company_id))]")

    

    def compute_customer(self):
        for record in self:
            if record.ext_reg_no:
                record.partner_id = self.env['res.partner'].search([('ext_reg_no', '=', record.ext_reg_no)], limit=1)
            else:
                record.partner_id=False

    @api.onchange('ext_reg_no')
    def onchange_ext_reg(self):
        for record in self:
            if record.ext_reg_no:
                record.partner_id = self.env['res.partner'].search([('ext_reg_no', '=', record.ext_reg_no)], limit=1)
            else:
                record.partner_id=False


    @api.depends('x','y')
    def ahmed_compute(self):
        for record in self:
            if record.x and record.y:
                record.z= record.x * record.y
            else:
                record.z=0


    @api.onchange('test_field')
    def onchange_test_field(self):
        for record in self:
            if record.test_field:
                record.test2_field = record.test_field +record.test_field +"hello world"
    
    @api.constrains('z')
    def check_if_z_less100(self):
        for record in self:
            if record.z < 100:
                raise ValidationError("z field must be greater than 100")
