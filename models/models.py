# -*- coding: utf-8 -*-

from odoo import models, fields, api

class sales_jeff(models.Model):
    # _name = 'sales_jeff.sales_jeff'
    _inherit= 'sale.order'

    clientname = fields.Char('Client Name', required=True)
   

