from odoo import api, fields, models


class CinemaCinema(models.Model):
    _name = 'cinema.cinema'
    _inherit = ['mail.thread']

    name = fields.Char(
        string="Cinema name",
        required=True,
        tracking=1
    )
    user_id = fields.Many2one(
        comodel_name="res.users",
        required=True,
        string="Administrator",
        default=lambda self: self.env.uid
    )
    number_of_stuff = fields.Integer()
    square_space = fields.Float()
    state = fields.Selection(
        selection=[('open', 'Open'),
                   ('close', 'Close')],
        required=True,
        default='open',
        tracking=1
    )
