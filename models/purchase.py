# -*- coding: utf-8 -*-

from openerp import fields, models
from openerp.exceptions import ValidationError
from openerp.tools.translate import _


class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    def wkf_confirm_order(self):
        purchase_order_currency_id = self.currency_id.id
        purchase_order_lines = self.order_line
        currencies_order_lines = [
            order_line.product_id.cost_currency_id.id for
            order_line in purchase_order_lines if
            order_line.product_id.cost_currency_id]

        if currencies_order_lines:
            currencies_order_lines = list(set(currencies_order_lines))

            if [purchase_order_currency_id] != currencies_order_lines:
                raise ValidationError(
                    _('The currency of the cost price of any of products'
                    ' in lines does not match with the currency of the purchase order')
                    )

        return super(PurchaseOrder, self).wkf_confirm_order()


class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    product_cost_currency_id = fields.Many2one(
        'res.currency', 'Currency', related='product_id.cost_currency_id')
