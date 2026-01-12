# Sign - Remove Branding

## Description

This module removes the "Signed with Odoo Sign" branding from signature frames in the Odoo Sign module.

## Features

- Removes "Signed with Odoo Sign" text from signature dialog
- Removes branding from signature frames in PDF documents
- Keeps the security hash (optional - can be removed via CSS)
- Works in backend, frontend, and public sign interfaces

## Installation

1. Copy this module to your `custom/addons` directory
2. Update the apps list: `Settings > Apps > Update Apps List`
3. Search for "Sign - Remove Branding"
4. Click Install

## Configuration

No configuration needed. The module works automatically after installation.

### Optional Customizations

If you want to also remove the hash or completely hide the frame:

1. Edit `static/src/scss/sign_remove_branding.scss`
2. Uncomment the relevant sections as indicated in the comments

## Technical Details

### What it does:

1. **XML Override**: Removes the `sign_label` attribute from the signature frame template
2. **CSS Override**: Hides the `:before` pseudo-element that displays the branding text
3. **Asset Loading**: Loads the overrides in all relevant asset bundles (backend, frontend, public)

### Files Modified (via inheritance):

- `sign/static/src/dialogs/sign_name_and_signature_dialog.xml`
- `sign/static/src/scss/sign_common.scss`

## Compatibility

- Odoo Version: 19.0
- Depends on: `sign` module

## License

LGPL-3

## Author

Custom Development

## Support

For issues or questions, please contact your system administrator.

