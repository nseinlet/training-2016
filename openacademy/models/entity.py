# -*- coding: utf-8 -*-
from openerp import models, fields, api

class Entity(models.Model):
    _name = 'openacademy.entity'
    _inherit = 'mail.thread'
    _rec_name = 'full_name'
    
    name = fields.Char(required=True, track_visibility='on_change')
    full_name = fields.Char(compute='_compute_full_name')
    parent_id = fields.Many2one('openacademy.entity', ondelete='restrict')
    parent_left = fields.Integer(index=True)
    parent_right = fields.Integer(index=True)
    
    _parent_name = "parent_id"
    _parent_store = True
    _parent_order = 'name'
    _order = 'parent_left'

    @api.depends('name', 'parent_id', 'parent_id.name')
    def _compute_full_name(self):
        for r in self:
            if r.parent_id.full_name:
                r.full_name = "%s | %s" % (r.parent_id.full_name, r.name)
            else:
                r.full_name = r.name
