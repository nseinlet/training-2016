# -*- coding: utf-8 -*-
from odoo import http

class Openacademy(http.Controller):
    @http.route('/openacademy/openacademy/', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('openacademy.index', {
            'courses': http.request.env['openacademy.course'].search([]),
        })

    @http.route('/session/<model("openacademy.session"):session>/', auth='public', website=True)
    def session(self, session):
        return http.request.render('openacademy.session', {
            'session': session
        })
        
#     @http.route('/openacademy/openacademy/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('openacademy.listing', {
#             'root': '/openacademy/openacademy',
#             'objects': http.request.env['openacademy.openacademy'].search([]),
#         })

#     @http.route('/openacademy/openacademy/objects/<model("openacademy.openacademy"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openacademy.object', {
#             'object': obj
#         })
