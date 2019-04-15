from odoo import api, fields, models, api

class TodoTask(models.Model):
    _name = 'todo.task'
    _description = 'To-do Task'

    name = fields.Char('Description', required=True)
    is_done = fields.Boolean('Done?')
    active = fields.Boolean('Active?', default=True)
    user_id = fields.Many2one('res.users', string='Resonsible', default=lambda self: self.env.user)
    team_ids = fields.Many2one('res.partners', string='Team')
    date_deadline = fields.Char('Deadline')

    @api.multi
    def do_clear_done(self):
        for task in self:
            task.active = False
        return True

    @api.multi
    def write(self, values):
        if 'active' not in values:
            values['active'] = True
        super().write(values)
