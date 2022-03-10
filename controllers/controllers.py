# -*- coding: utf-8 -*-
from odoo import http

# class SalesJeff(http.Controller):
#     @http.route('/sales_jeff/sales_jeff/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sales_jeff/sales_jeff/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sales_jeff.listing', {
#             'root': '/sales_jeff/sales_jeff',
#             'objects': http.request.env['sales_jeff.sales_jeff'].search([]),
#         })

#     @http.route('/sales_jeff/sales_jeff/objects/<model("sales_jeff.sales_jeff"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sales_jeff.object', {
#             'object': obj
#         })