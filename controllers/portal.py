from odoo import http
from odoo.http import request

class CompanyContactsPortal(http.Controller):

    @http.route(['/my/company_contacts'], type='http', auth='user', website=True)
    def company_contacts(self, **kw):
        user = request.env.user
        contacts = request.env['res.partner'].sudo().search([
            ('company_id', '=', user.company_id.id),
            ('id', '!=', user.partner_id.id)
        ])
        return request.render('company_contacts_portal.portal_company_contacts', {
            'contacts': contacts,
        })

    @http.route(['/my/send_message'], type='json', auth='user')
    def send_message(self):
        data = request.httprequest.json
        contact_id = data.get('contact_id')
        message = data.get('message')
        contact = request.env['res.partner'].sudo().browse(int(contact_id))
        if contact and contact.company_id == request.env.user.company_id:
            contact.send_message_to_contact(message, contact.id)
            return True
        return False
