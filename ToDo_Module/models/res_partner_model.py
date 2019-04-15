from odoo import fields, models, api

class ResPartner(models.Model):
    _inherit = 'res.partner'
    todo_ids = fields.Many2many(
        'todo.task',
        string = "To-do Teams"
    )
