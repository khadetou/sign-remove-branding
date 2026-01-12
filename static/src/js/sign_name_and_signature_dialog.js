/** @odoo-module **/

import { SignNameAndSignature } from "@sign/dialogs/sign_name_and_signature_dialog";
import { patch } from "@web/core/utils/patch";

/**
 * Patch the SignNameAndSignature component to use our custom template
 * that has the branding text removed.
 */
patch(SignNameAndSignature.prototype, {
    // Override the template getter to use our custom template
});

// Override the static template property
SignNameAndSignature.template = "sign_remove_branding.NameAndSignature";

