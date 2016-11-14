# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Session(models.Model):
    _name = 'openacademy.session'

    name = fields.Char(required=True)
    course_id = fields.Many2one('openacademy.course', string="Course", required="1")
    start_date = fields.Date()
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    seats = fields.Integer(string="Number of seats")
    
