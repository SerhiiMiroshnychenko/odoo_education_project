from odoo import api, fields, models
from odoo.exceptions import UserError


class CinemaCinemaHall(models.Model):
    _name = 'cinema.cinema.hall'

    name = fields.Char(string="Cinema hall name", required=True)
    seats = fields.Integer(required=True)
    cinema_id = fields.Many2one('cinema.cinema', required=True, ondelete='cascade')

    movie_ids = fields.Many2many('cinema.cinema.movie')
