
from odoo import api,fields, models, _
import requests
import urllib3
from xml.etree import ElementTree as ET
import logging





class ResCompany(models.Model):
    _inherit = 'res.company'

    test_url = fields.Char(string='Testing URL')

    def prepare_environment_url(self):
            return self.test_url
    
    def prepare_request_headers(self):
        return {'content-Type': 'application/json'}
    
    def get_data(self):
        url = self.env.company.test_url + 'packages/'
        headers = self.prepare_request_headers()
        response = requests.get(url, headers=headers)
        print(url)
        print(response.content)
        if response.status_code == 200:
            data = response.json()
            for d in data:
                values = {
                'name': d.get('name'),
                'price': d.get('price'),
                'allowed_users': d.get('allowed_users'),
                'is_active': d.get('is_active'),
                'is_over': d.get('is_over'),
                'django_id': d.get('id')
            }
                if(not(self.env['demo.package'].search([('django_id', '=', d['id'])], limit=1))):
                    self.env['demo.package'].create(values)


   