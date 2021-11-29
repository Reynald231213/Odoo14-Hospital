# -*- coding: utf-8 -*-
# from odoo import http


# class Ujicoba(http.Controller):
#     @http.route('/ujicoba/ujicoba/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/ujicoba/ujicoba/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('ujicoba.listing', {
#             'root': '/ujicoba/ujicoba',
#             'objects': http.request.env['ujicoba.ujicoba'].search([]),
#         })

#     @http.route('/ujicoba/ujicoba/objects/<model("ujicoba.ujicoba"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('ujicoba.object', {
#             'object': obj
#         })
