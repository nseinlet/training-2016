# -*- coding: utf-8 -*-
from openerp import http

# class OpenacademySubject(http.Controller):
#     @http.route('/openacademy_subject/openacademy_subject/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/openacademy_subject/openacademy_subject/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('openacademy_subject.listing', {
#             'root': '/openacademy_subject/openacademy_subject',
#             'objects': http.request.env['openacademy_subject.openacademy_subject'].search([]),
#         })

#     @http.route('/openacademy_subject/openacademy_subject/objects/<model("openacademy_subject.openacademy_subject"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('openacademy_subject.object', {
#             'object': obj
#         })