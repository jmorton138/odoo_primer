# -*- coding: utf-8 -*-

from odoo import models, fields, api

class sales_jeff(models.Model):
    # _name = 'sales_jeff.sales_jeff'
    _inherit= 'sale.order'

    clientname = fields.Char('Client Name', required=True)
   
    # sudo docker run -v /home/jeff/Desktop/custom_modules:/mnt/extra-addons -p 8069:8069 --name odoo --link db:db -t odoo

