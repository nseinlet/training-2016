# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Course(models.Model):
    _name = 'openacademy.course'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    responsible_id = fields.Many2one('res.users', string='Responsible')
    session_ids = fields.One2many('openacademy.session', 'course_id', string="Sessions")
    
