# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Entity(models.Model):
    _name = 'openacademy.entity'
    
    name = fields.Char(required=True)
    parent_id = fields.Many2one('openacademy.entity', ondelete='restrict')
    parent_left = fields.Integer(index=True)
    parent_right = fields.Integer(index=True)
    
    _parent_name = "parent_id"
    _parent_store = True
    _parent_order = 'name'
    _order = 'parent_left'
