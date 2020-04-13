# -*- coding: utf-8 -*-

from odoo import api, fields, models
from bigoyster import Bigoyster

class Partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    dashboard = fields.Char(string='Dashboard')
    location_handle = fields.Char(string='Handle')
    registry_status = fields.Char(string='Status')
    active_campaigns = fields.Integer("Active Campaigns")
    follower_count = fields.Integer("Follower Count")
    credit_balance = fields.Integer("Credit Balance")

    def isa_brand(self):
        return True

    def approve_brand(self):
        self.env.user.id
        api_url = 'https://stageapi.bigoyster.com/'
        user = 'test'
        password = 'me'
        token=''
        client = Bigoyster(base_url=api_url, token=token, username=user, password=password)
        
