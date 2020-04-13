# -*- coding: utf-8 -*-

from odoo import api, fields, models


class Partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'

    dashboard = fields.Many2one('crm.team', string='Sales Team')
    location_handle = fields.One2many('crm.lead', 'partner_id', string='Opportunities', domain=[('type', '=', 'opportunity')])
    active_campaigns = fields.Integer("Active Campaigns")
    follower_count = fields.Integer("Follower Count")
    credit_balance = fields.Integer("Credit Balance")
    