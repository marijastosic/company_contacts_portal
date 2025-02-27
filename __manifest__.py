{
    'name': 'Company Contacts Portal',
    'version': '18.0.0.0',
    'summary': 'View and message company contacts in the portal.',
    'author': 'Marija Misic',
    'category': 'Portal',
    'depends': ['base', 'portal', 'mail', 'web'],
    'data': [
        'views/portal_templates.xml'
    ],
    'assets': {
        'web.assets_frontend': [
            'company_contacts_portal/static/src/js/messaging.js'
        ]
    },
    'installable': True,
}