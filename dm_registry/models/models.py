# -*- coding: utf-8 -*-

# from odoo import models, fields, api


# class dm_registry(models.Model):
#     _name = 'dm_registry.dm_registry'
#     _description = 'dm_registry.dm_registry'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100
