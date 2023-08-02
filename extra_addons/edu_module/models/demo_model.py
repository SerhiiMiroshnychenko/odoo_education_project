from odoo import fields, models


class DemoModel(models.Model):
    _name = 'demo.model'
    _description = 'Model for demo object'

    name = fields.Char(string='Name', required=True)
    quantity = fields.Float(string='Quantity', default=0.0)
