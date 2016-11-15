# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Session(models.Model):
    _name = 'openacademy.session'

    name = fields.Char(required=True)
    course_id = fields.Many2one('openacademy.course', string="Course", required="1")
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    start_date = fields.Date(default=fields.Date.today)
    seats = fields.Integer(string="Number of seats")
    instructor_id = fields.Many2one('res.partner', string="Instructor", domain="['|', ('instructor', '=', True), ('category_id', 'ilike', 'teacher')]")
    instructor_name = fields.Char(string='Instructor name', related='instructor_id.name')
    active = fields.Boolean(default=True)
    attendee_ids = fields.Many2many('res.partner', 'attendees_m2m_link', 'session_id', 'partner_id')
    taken_seats = fields.Float(string="Taken seats", compute='_taken_seats')
    entity_id = fields.Many2one('openacademy.entity', string='Entity')
    course_entity_id = fields.Many2one('openacademy.entity', string='Course entity', related="course_id.entity_id")

    @api.depends('seats', 'attendee_ids')
    def _taken_seats(self):
        for r in self:
            if not r.seats:
                r.taken_seats = 0.0
            else:
                r.taken_seats = 100.0 * len(r.attendee_ids) / r.seats
    
