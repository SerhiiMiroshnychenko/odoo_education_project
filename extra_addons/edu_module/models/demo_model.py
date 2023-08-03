from odoo import api, fields, models


class DemoModel(models.Model):
    _name = 'demo.model'
    _description = 'Model for demo object'

    name = fields.Char(string='Name', required=True, size=15)
    price = fields.Monetary(string='Price', currency_field='currency_id')
    quantity = fields.Float(string='Quantity')
    total_bill = fields.Monetary(string='Total bill',
                                 currency_field='currency_id',
                                 compute='_compute_total_bill')
    currency_id = fields.Many2one('res.currency')

    @api.depends("price", "quantity")
    def _compute_total_bill(self):
        for product in self:
            product.total_bill = product.price * product.quantity
