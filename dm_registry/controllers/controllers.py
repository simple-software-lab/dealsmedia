# -*- coding: utf-8 -*-
# from odoo import http


# class DmRegistry(http.Controller):
#     @http.route('/dm_registry/dm_registry/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/dm_registry/dm_registry/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('dm_registry.listing', {
#             'root': '/dm_registry/dm_registry',
#             'objects': http.request.env['dm_registry.dm_registry'].search([]),
#         })

#     @http.route('/dm_registry/dm_registry/objects/<model("dm_registry.dm_registry"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('dm_registry.object', {
#             'object': obj
#         })
