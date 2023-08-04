from odoo import api, fields, models


class CinemaCinema(models.Model):
    _name = 'cinema.cinema'
    _inherit = ['mail.thread']

    name = fields.Char(
        string="Cinema name",
        required=True,
        tracking=1
    )

    description = fields.Text()

    user_id = fields.Many2one(
        comodel_name="res.users",
        required=True,
        string="Administrator",
        default=lambda self: self.env.uid
    )
    number_of_stuff = fields.Integer()

    hall_ids = fields.One2many(
        "cinema.cinema.hall",
        "cinema_id",
        string='Halls'
    )

    square_space = fields.Float()
    state = fields.Selection(
        selection=[('open', 'Open'),
                   ('close', 'Close')],
        required=True,
        default='open',
        tracking=1
    )

    restaurant = fields.Boolean(string='Restaurant')

    total_seats = fields.Integer(compute='_compute_total_seats')

    @api.depends('hall_ids')
    def _compute_total_seats(self):
        for theater in self:
            theater.total_seats = sum(theater.hall_ids.mapped('seats'))

    movie_ids = fields.Many2many(
        'cinema.cinema.movie',
        states={'close': [('invisible', True)]})




