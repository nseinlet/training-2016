# -*- coding: utf-8 -*-
from openerp import models, fields, api

class Partner(models.Model):
    _name = 'res.partner'
    _inherit = 'res.partner'
    
    instructor = fields.Boolean(string="Is instructor")
    session_ids = fields.Many2many('openacademy.session', 'attendees_m2m_link', 'partner_id', 'session_id', string="Attending sessions")
    instructing_session_ids = fields.One2many('openacademy.session', 'instructor_id', string="Instructing sessions")
    
