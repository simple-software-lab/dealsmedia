# -*- coding: utf-8 -*-

from odoo import api, fields, models
from bigoyster import Bigoyster
import requests
import os

class Partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    dashboard = fields.Char(string='Dashboard')
    location_handle = fields.Char(string='Handle')
    registry_status = fields.Char(string='Status')
    active_campaigns = fields.Integer("Active Campaigns")
    follower_count = fields.Integer("Follower Count")
    credit_balance = fields.Integer("Credit Balance")

    def write(self, vals):
        res = super(Partner, self).write(vals)
        for rec in self:
            rec.call_event_api('MFG018', {'odoo_id': rec.id})
        return res
                                     
    @api.model
    def call_event_api(self, event_type, addl_info):
        if os.environ.get('ODOO_STAGE') == 'staging':
            url = 'https://stageapi.dealsmedia.com'
            headers = {
                'Authorization': "Token b4d38894b61f54b46de2239d9604446506772a69",
            }
        elif os.environ.get('ODOO_STAGE') == 'production':
            url = 'https://api.dealsmedia.com/event/create'
            headers = {
                'Authorization': "Token f7a95eceaef62d1c5338dc20c54a0514c8c0070b",
            }
        params = {
            'event_type': 'CO003',
            'addl_info': addl_info
        }
        response = requests.post(url, json=params, headers=headers, timeout=5, verify=False)
        
    def isa_brand(self):
        return True

    def approve_brand(self):
        self.env.user.id
        api_url = 'https://stageapi.bigoyster.com/'
        user = 'test'
        password = 'me'
        token=''
        client = Bigoyster(base_url=api_url, token=token, username=user, password=password)
        
