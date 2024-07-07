from odoo import models, fields, api
import requests
import json


class Package(models.Model):
    _name = "demo.package"
    
    name = fields.Char(string="Name")
    price = fields.Integer(string="Unit Price")
    allowed_users= fields.Integer(string="Allowed Users")
    is_active = fields.Boolean(string="Is Active")
    is_over = fields.Boolean(string="Is Over")
    django_id=fields.Integer(string="django_id")



    def prepare_request_headers(self):
        return {'content-Type': 'application/json'}


    @api.model
    def create(self, values):
        res= super().create(values)
        url= self.env.company.test_url + 'packages/'
        response=requests.post(url, headers=self.prepare_request_headers(),data=json.dumps(values),auth="")
        if response.status_code == 201:  
            data = response.json()
            django_id = data.get('id')  
            if django_id:
                res.write({'django_id': django_id})
        print(url)
        print(json.dumps(values))
        print(response.content)

        return res
    
    def update(self, values):
        for rec in self:
            url= self.env.company.test_url + 'packages/generic/'+str(rec.django_id)
            response=requests.put(url, headers=self.prepare_request_headers(),data=json.dumps(values),auth="")
            print(url)
            print(json.dumps(values))
            print(response.content)
        return super(Package, self).write(values)


    def unlink(self):
        for rec in self:
            url= self.env.company.test_url + 'packages/generic/'+str(rec.django_id)
            response=requests.delete(url, headers=self.prepare_request_headers(),auth="")
            print(url)
            print(response)
        return super(Package, self).unlink()

    
    