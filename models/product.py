# -*- coding: utf-8 -*-

from openerp import fields, models


class ProductTemplate(models.Model):
    _inherit = 'product.template'

    cost_currency_id = fields.Many2one(
        'res.currency', 'Currency', help='Currency used in cost of the product.')
