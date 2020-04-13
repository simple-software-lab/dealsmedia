# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    dashboard = fields.Char(string='Dashboard')
    location_handle = fields.Char(string='Handle')
    active_campaigns = fields.Integer("Active Campaigns")
    follower_count = fields.Integer("Follower Count")
    credit_balance = fields.Integer("Credit Balance")
    