# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

## [Unreleased]
### Changed
- Extension of method that process confirmation of purchase order to validate that the currency of lines of order is the same currency of purchase order.

## [0.2.0] - 2017-06-06
### Changed
- Adds domain to field product_id to filter products by currency of order in lines of purchase order.

## [0.1.0] - 2017-06-05
### Added
- Adds field cost_currency_id to model product.template that allow set the currency for the cost of the product.
- Extends the form view of product for add the new field cost_currency_id.
- Adds field product_cost_currency_id to model purchase.order.line, this field is related to product_id.cost_currency_id.
- Extends the form view of purchase order to add the field product_cost_currency_id to the lines of the order.
