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
    state = fields.Selection([('1', 'step 1'), ('2', 'step 2')], default='1')
    monchamp1 = fields.Char()
    monchamp2 = fields.Char()
    monchamp3 = fields.Char()
    
    @api.multi
    def _to_step(self, step):
        self.write({
            state: step,
            'monchamp1': 'a',
            'monchamp2': 'b',
            'monchamp3': 'c',
        })
        
        return {
            'type': 'ir.actions.act_window',
            'name': 'Register attendees',
            'res_model': 'openacademy.wizard.multi',
            'res_id': self.id,
            'view_mode': 'form',
            'target': 'new',
        }
        
    @api.multi
    def to_step1(self):
        return self._to_step('1')
        
    @api.multi
    def to_step2(self):
        return self._to_step('2')
        
    @api.multi
    def subscribe(self):
        for session in self.session_ids:
            session.attendee_ids |= self.attendee_ids
