# -*- coding: utf-8 -*-
from odoo import models, fields, api
from odoo.exceptions import ValidationError

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
                
    # onchange handler
    @api.onchange('seats', 'attendee_ids')
    def _onchange_seats(self):
        def raise_warning(title, msg):
            return {
                'warning': {
                    'title': title or "",
                    'message': msg or "",
                }
            }
        if self.seats < 0:
            return raise_warning("No negative seats",
                     "The seats number must be a positive number")
        elif self.seats < len(self.attendee_ids):
            return raise_warning("Not enough seats",
                    "Too much attendees for the number of seats")
                    
    @api.constrains('instructor_id', 'attendee_ids')
    def _check_not_teaching_himself(self):
        for record in self:
            if record.instructor_id and record.instructor_id.id in record.attendee_ids.ids:
                raise ValidationError("Instructor cannot teach himself")
                
    

    
