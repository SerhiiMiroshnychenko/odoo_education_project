from odoo import fields, models, api
from datetime import timedelta


class CinemaCinemaMovie(models.Model):
    _name = "cinema.cinema.movie"
    _description = "A model representing movies"
    _order = "name"
    _sql_constraints = [('name_uniq', 'unique (name)', "Movie name already exists !")]

    name = fields.Char(required=True)
    premiere_date = fields.Date(default=lambda self: fields.Date.today())
    deadline_date = fields.Date()
    color = fields.Integer()

    # This field will contain all the cinemas where this movie is playing.
    cinema_ids = fields.Many2many('cinema.cinema')

    @api.onchange("premiere_date")
    def _onchange_premiere_date(self):
        for movies in self:
            if not movies.deadline_date:
                movies.deadline_date = movies.premiere_date + timedelta(days=14)
