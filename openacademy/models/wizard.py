# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Wizard(models.TransientModel):
    _name = 'openacademy.wizard'

    session_id = fields.Many2one('openacademy.session', string="Session", required=True)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    @api.multi
    def subscribe(self):
        self.session_id.attendee_ids |= self.attendee_ids
        
class WizardMulti(models.TransientModel):
    _name = 'openacademy.wizard.multi'

    def _default_session(self):
        ids = list(set([self._context.get('active_id', False), ] + self._context.get('active_ids', [])))
        return self.env['openacademy.session'].browse(ids)
        
    session_ids = fields.Many2many('openacademy.session', string="Session", required=True, default=_default_session)
    attendee_ids = fields.Many2many('res.partner', string="Attendees")

    @api.multi
    def subscribe(self):
        for session in self.session_ids:
            session.attendee_ids |= self.attendee_ids
