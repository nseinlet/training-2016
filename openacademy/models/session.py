# -*- coding: utf-8 -*-
from datetime import timedelta

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class Session(models.Model):
    _name = 'openacademy.session'
    _order = 'sequence'
    
    name = fields.Char(required=True)
    course_id = fields.Many2one('openacademy.course', string="Course", required="1")
    duration = fields.Float(digits=(6, 2), help="Duration in days")
    start_date = fields.Date(default=fields.Date.today)
    end_date = fields.Date(string="End Date", store=True, compute='_get_end_date', inverse='_set_end_date')
    hours = fields.Float(string="Duration in hours", compute='_get_hours', inverse='_set_hours')
    seats = fields.Integer(string="Number of seats")
    instructor_id = fields.Many2one('res.partner', string="Instructor", domain="['|', ('instructor', '=', True), ('category_id', 'ilike', 'teacher')]")
    instructor_name = fields.Char(string='Instructor name', related='instructor_id.name')
    active = fields.Boolean(default=True)
    attendee_ids = fields.Many2many('res.partner', 'attendees_m2m_link', 'session_id', 'partner_id')
    taken_seats = fields.Float(string="Taken seats", compute='_taken_seats')
    attendees_count = fields.Integer(string="Attendees count", compute='_get_attendees_count', store=True)
    entity_id = fields.Many2one('openacademy.entity', string='Entity')
    course_entity_id = fields.Many2one('openacademy.entity', string='Course entity', related="course_id.entity_id", store=True)
    sequence = fields.Integer('Order')
    color = fields.Integer()
    state = fields.Selection([
        ('draft', "Draft"),
        ('confirmed', "Confirmed"),
        ('done', "Done"),
    ], default='draft')

    @api.multi
    def action_draft(self):
        self.state = 'draft'

    @api.multi
    def action_confirm(self):
        self.state = 'confirmed'

    @api.multi
    def action_done(self):
        self.state = 'done'

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
                
    @api.depends('start_date', 'duration')
    def _get_end_date(self):
        for r in self:
            if not (r.start_date and r.duration):
                r.end_date = r.start_date
                continue

            # Add duration to start_date, but: Monday + 5 days = Saturday, so
            # subtract one second to get on Friday instead
            start = fields.Datetime.from_string(r.start_date)
            duration = timedelta(days=r.duration, seconds=-1)
            r.end_date = start + duration

    def _set_end_date(self):
        for r in self:
            if not (r.start_date and r.end_date):
                continue

            # Compute the difference between dates, but: Friday - Monday = 4 days,
            # so add one day to get 5 days instead
            start_date = fields.Datetime.from_string(r.start_date)
            end_date = fields.Datetime.from_string(r.end_date)
            r.duration = (end_date - start_date).days + 1
            
    @api.depends('duration')
    def _get_hours(self):
        for r in self:
            r.hours = r.duration * 24

    def _set_hours(self):
        for r in self:
            r.duration = r.hours / 24
            
    @api.depends('attendee_ids')
    def _get_attendees_count(self):
        for r in self:
            r.attendees_count = len(r.attendee_ids)
            
    @api.multi
    def launch_wizard(self):
        my_wiz = self.env['openacademy.wizard'].create(
            {'session_id': self.id}
        )
        return {
            'type': 'ir.actions.act_window',
            'name': 'Register attendees',
            'res_model': 'openacademy.wizard',
            'res_id': my_wiz.id,
            'view_mode': 'form',
            'target': 'new',
        }
    

    
