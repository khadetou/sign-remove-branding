# -*- coding: utf-8 -*-
{
    'name': 'Sign - Remove Branding',
    'version': '19.0.1.0.0',
    'category': 'Sales/Sign',
    'summary': 'Remove "Signed with Odoo Sign" branding from signatures',
    'description': """
        This module removes the "Signed with Odoo Sign" branding from:
        - Signature dialog frame
        - PDF documents
        - All signature-related interfaces
    """,
    'author': 'Custom',
    'website': '',
    'depends': ['sign'],
    'data': [],
    'assets': {
        'web.assets_backend': [
            'sign_remove_branding/static/src/scss/sign_remove_branding.scss',
            'sign_remove_branding/static/src/xml/sign_name_and_signature_dialog.xml',
            'sign_remove_branding/static/src/js/sign_name_and_signature_dialog.js',
            'sign_remove_branding/static/src/dialog/thank_you_dialog.xml',
        ],
        'sign.assets_public_sign': [
            'sign_remove_branding/static/src/scss/sign_remove_branding.scss',
            'sign_remove_branding/static/src/xml/sign_name_and_signature_dialog.xml',
            'sign_remove_branding/static/src/js/sign_name_and_signature_dialog.js',
        ],
        'web.assets_frontend': [
            'sign_remove_branding/static/src/scss/sign_remove_branding.scss',
            'sign_remove_branding/static/src/xml/sign_name_and_signature_dialog.xml',
            'sign_remove_branding/static/src/js/sign_name_and_signature_dialog.js',
        ],
    },
    'installable': True,
    'application': False,
    'auto_install': False,
    'license': 'LGPL-3',
}

