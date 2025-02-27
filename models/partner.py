from odoo import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def send_message_to_contact(self, message_content, partner_id):
        recipient = self.env['res.partner'].browse(partner_id)
        if recipient:
            self.env['mail.message'].create({
                'body': message_content,
                'model': 'res.partner',
                'res_id': partner_id,
                'message_type': 'comment',
                'subtype_id': self.env.ref('mail.mt_comment').id,
                'author_id': self.env.user.partner_id.id,
            })
