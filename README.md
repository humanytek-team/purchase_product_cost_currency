# purchase_product_cost_currency
Extension of addons purchase and product for add the following features:

* Add field cost_currency_id to model product.template that allow set the currency for the cost of the product.
* Extend the form view of product for add the new field cost_currency_id.
* Add field product_cost_currency_id to model purchase.order.line, this field is related to product_id.cost_currency_id.
* Extend the form view of purchase order to add the field product_cost_currency_id to the lines of the order.
