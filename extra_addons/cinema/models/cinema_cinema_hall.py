from odoo import api, fields, models


class CinemaCinemaHall(models.Model):
    _name = 'cinema.cinema.hall'

    name = fields.Char(
        string="Cinema hall name",
        required=True,
    )

    seats = fields.Integer(required=True)

    cinema_id = fields.Many2one(
        'cinema.cinema',
        required=True,
        ondelete='cascade',
        inverse_name='hall_ids'
    )


