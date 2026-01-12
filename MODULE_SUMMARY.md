# Sign Remove Branding - Module Summary

## 📦 Module Information

- **Name**: Sign - Remove Branding
- **Technical Name**: `sign_remove_branding`
- **Version**: 19.0.1.0.0
- **Category**: Sales/Sign
- **License**: LGPL-3
- **Depends**: sign
- **Auto Install**: No

## 📁 Module Structure

```
sign_remove_branding/
├── __init__.py                          # Module initialization
├── __manifest__.py                      # Module manifest
├── README.md                            # Full documentation
├── INSTALLATION.md                      # Detailed installation guide
├── QUICK_START.md                       # Quick reference
├── MODULE_SUMMARY.md                    # This file
├── verify_module.py                     # Verification script
│
├── static/
│   ├── description/
│   │   ├── index.html                   # Module description page
│   │   ├── icon.svg                     # Module icon (SVG)
│   │   └── icon.png                     # Module icon (PNG)
│   │
│   └── src/
│       ├── scss/
│       │   └── sign_remove_branding.scss    # CSS overrides
│       │
│       └── xml/
│           └── sign_name_and_signature_dialog.xml  # Template overrides
```

## 🎯 What It Does

### Primary Function
Removes the "Signed with Odoo Sign" branding text from signature frames throughout the Odoo Sign module.

### Technical Implementation

1. **XML Override** (`sign_name_and_signature_dialog.xml`)
   - Inherits from `sign.NameAndSignature` template
   - Removes the `sign_label` attribute containing "Signed with Odoo Sign"

2. **CSS Override** (`sign_remove_branding.scss`)
   - Hides the `:before` pseudo-element that displays the branding
   - Uses `!important` to ensure override priority
   - Optionally can hide hash and entire frame

3. **Asset Loading** (`__manifest__.py`)
   - Loads overrides in `web.assets_backend`
   - Loads overrides in `sign.assets_public_sign`
   - Loads overrides in `web.assets_frontend`

## 🔧 How It Works

### The Branding Flow (Original)

1. User enables "Frame" checkbox in signature dialog
2. HTML/CSS renders frame with "Signed with Odoo Sign" text
3. `html2canvas` library captures frame as PNG image
4. Image is base64-encoded and stored in database
5. When PDF is generated, frame image is embedded

### The Override Flow (With This Module)

1. XML override removes `sign_label` attribute
2. CSS override hides `:before` pseudo-element
3. Frame is captured WITHOUT branding text
4. Clean frame image is stored and embedded in PDF

## 📋 Installation Checklist

- [ ] Module files copied to `custom/addons/sign_remove_branding/`
- [ ] File permissions set correctly (`chown -R odoo:odoo`)
- [ ] Odoo server restarted
- [ ] Apps list updated in Odoo
- [ ] Module installed from Apps menu
- [ ] Browser cache cleared
- [ ] Signature dialog tested

## ✅ Verification

Run the verification script:
```bash
cd custom/addons/sign_remove_branding
python3 verify_module.py
```

Expected output: "✓ All checks passed!"

## 🎨 Customization Options

### Option 1: Remove Hash Too
Edit `static/src/scss/sign_remove_branding.scss`, uncomment lines 14-18

### Option 2: Remove Entire Frame
Edit `static/src/scss/sign_remove_branding.scss`, uncomment lines 25-30

### Option 3: Custom Branding
Edit `static/src/xml/sign_name_and_signature_dialog.xml`, change:
```xml
<attribute name="sign_label"></attribute>
```
to:
```xml
<attribute name="sign_label">Your Custom Text</attribute>
```

## 🔍 Files Modified (via Inheritance)

This module does NOT modify original Odoo files. It uses Odoo's inheritance system:

| Original File | Override Method |
|---------------|-----------------|
| `sign/static/src/dialogs/sign_name_and_signature_dialog.xml` | XML inheritance |
| `sign/static/src/scss/sign_common.scss` | CSS override with `!important` |

## 🐛 Troubleshooting

### Module Not Visible
```bash
# Check permissions
ls -la custom/addons/sign_remove_branding/

# Check Odoo logs
tail -f /var/log/odoo/odoo.log
```

### Branding Still Shows
```bash
# Restart Odoo
sudo systemctl restart odoo

# Clear browser cache
Ctrl + Shift + R (or Cmd + Shift + R on Mac)
```

### Assets Not Loading
1. Enable Developer Mode
2. Settings > Technical > User Interface > Assets
3. Search for "sign_remove_branding"
4. Click "Regenerate Assets"

## 📊 Impact Analysis

### What Changes
- ✅ Signature dialog frame (no branding text)
- ✅ PDF embedded signatures (no branding in image)
- ✅ All signature interfaces (backend, frontend, public)

### What Stays the Same
- ✅ Signature functionality
- ✅ Security hash (unless manually removed)
- ✅ Frame border (unless manually removed)
- ✅ All other Sign module features

## 🔐 Security Considerations

- Module only affects visual presentation
- Does not modify signature validation
- Does not affect document integrity
- Security hash remains intact (by default)

## 📝 Maintenance

### Updates
- Compatible with Odoo 19.0
- May need updates for future Odoo versions
- Monitor Odoo release notes for Sign module changes

### Backup
Before installation, backup:
- Database
- Custom modules
- Configuration files

## 📞 Support Resources

- `README.md` - Full documentation
- `INSTALLATION.md` - Detailed installation steps
- `QUICK_START.md` - Quick reference guide
- `verify_module.py` - Automated verification

## 📜 License

LGPL-3 - See LICENSE file for details

## 👨‍💻 Development

### Testing
1. Create signature request
2. Adopt signature with Frame enabled
3. Verify no "Signed with Odoo Sign" text
4. Complete signature
5. Download PDF and verify branding removed

### Debugging
Enable Odoo debug mode:
```
?debug=1
```

Check browser console (F12) for JavaScript errors

---

**Created**: 2026-01-12  
**Version**: 1.0.0  
**Odoo Version**: 19.0

