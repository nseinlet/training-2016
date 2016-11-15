# -*- coding: utf-8 -*-
from odoo import models, fields, api

class Course(models.Model):
    _name = 'openacademy.course'

    name = fields.Char(string="Title", required=True)
    description = fields.Text()
    responsible_id = fields.Many2one('res.users', string='Responsible')
    session_ids = fields.One2many('openacademy.session', 'course_id', string="Sessions")
    entity_id = fields.Many2one('openacademy.entity', string='Entity')
    average_fill = fields.Float(string='Average fill', compute='_compute_avg_session_fill')
    average_attendees = fields.Float(string='Average attendee count', compute='_compute_avg_session_fill')
    
    @api.depends('session_ids', 'session_ids.taken_seats', 'session_ids.attendee_ids')
    def _compute_avg_session_fill(self):
        for rec in self:
            rec.average_fill = sum([sess.taken_seats for sess in rec.session_ids]) / len(rec.session_ids) if rec.session_ids else 0
            rec.average_attendees = sum([len(sess.attendee_ids) for sess in rec.session_ids]) / len(rec.session_ids) if rec.session_ids else 0
