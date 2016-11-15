# -*- coding: utf-8 -*-

from odoo import models, fields, api

class OpenAcademySubject(models.Model):
    _name = 'openacademy.subject'

    name = fields.Char()
    
class OpenAcademyCourse(models.Model):
    _inherit = 'openacademy.course'
    
    subject_id = fields.Many2one('openacademy.subject', string='subject')
    available = fields.Boolean('Course available')
    
class OpenAcademySession(models.Model):
    _inherit = 'openacademy.session'
    
    subject_id = fields.Many2one('openacademy.subject', string='subject', related='course_id.subject_id')
    course_available = fields.Boolean('Course available', related='course_id.available')
    
