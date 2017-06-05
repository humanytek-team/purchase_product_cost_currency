# -*- coding: utf-8 -*-

from openerp import fields, models

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    product_cost_currency_id = fields.Many2one(
        'res.currency', 'Currency', related='product_id.cost_currency_id')
