from odoo import api, fields, models
from odoo.addons.base.res.res_request import referenceable_models

class TodoTask(models.Model):
    _inherit = 'todo.task'

    effort_estimate = fields.Integer()
    name = fields.Char(help="What needs to be done?")
    stage_id = fields.Many2one('todo.task.stage', 'Stage')
    tag_ids = fields.Many2many('todo.task.tag', string='Tags')

    #refers_to = fields.Reference([('res.user', 'User'), ('res.partner', 'Partner')], 'Refers to')
    #refers_to = fields.Reference(referenceable_models, 'Refers to')

    #state = fields.Selection(related = 'stage_id.state', string = 'Stage State')
    #stage_fold = fields.Boolean(string = 'Stage Folded?', related = 'stage_id.fold')
    # stage_fold = fields.Boolean('Stage Folded?',
    #                 compute = '_compute_stage_fold',
    #                 search = '_search_stage_fold',
    #                 inverse = '_write_stage_fold')
    #
    # @api.depends('stage_id.fold')
    # def _compute_stage_fold(self):
    #     for todo in self:
    #         todo.stage_fold = todo.stage_id.fold
    #
    # def _search_stage_fold(self, operator, value):
    #     return [('stage_id.fold', operator, value)]
    #
    # def _write_stage_fold(self):
    #     for todo in self:
    #         todo.stage_id.fold = todo.stage_fold
