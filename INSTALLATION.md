# Installation Guide - Sign Remove Branding Module

## Prerequisites

- Odoo 19.0 installed
- `sign` module installed and activated
- Access to Odoo server filesystem
- Administrator access to Odoo

## Installation Steps

### Step 1: Verify Module Location

The module should be located at:
```
/data/workspace/odoo/19/odoo-19/custom/addons/sign_remove_branding/
```

### Step 2: Update Odoo Configuration (if needed)

Make sure your `odoo.conf` includes the custom addons path:

```ini
[options]
addons_path = /path/to/odoo/addons,/path/to/odoo/custom/addons
```

### Step 3: Restart Odoo Server

Restart the Odoo service to recognize the new module:

```bash
# If using systemd
sudo systemctl restart odoo

# Or if running manually
./odoo-bin -c /path/to/odoo.conf
```

### Step 4: Update Apps List

1. Log in to Odoo as Administrator
2. Go to **Apps** menu
3. Click on the **⋮** (three dots) menu
4. Select **Update Apps List**
5. Click **Update** in the confirmation dialog

### Step 5: Install the Module

1. In the **Apps** menu, remove the "Apps" filter
2. Search for "Sign - Remove Branding"
3. Click **Install** button

### Step 6: Clear Browser Cache

After installation, clear your browser cache or do a hard refresh:
- **Chrome/Edge**: Ctrl + Shift + R (Windows) or Cmd + Shift + R (Mac)
- **Firefox**: Ctrl + F5 (Windows) or Cmd + Shift + R (Mac)

### Step 7: Verify Installation

1. Go to any signature request
2. Click to adopt/create a signature
3. Enable the "Frame" checkbox
4. Verify that "Signed with Odoo Sign" text is no longer visible

## Troubleshooting

### Module Not Appearing in Apps List

**Problem**: Module doesn't show up after updating apps list

**Solution**:
1. Check file permissions: `sudo chown -R odoo:odoo custom/addons/sign_remove_branding`
2. Verify module structure: `ls -la custom/addons/sign_remove_branding/`
3. Check Odoo logs for errors: `tail -f /var/log/odoo/odoo.log`

### Branding Still Visible

**Problem**: "Signed with Odoo Sign" text still appears

**Solution**:
1. Clear browser cache completely
2. Restart Odoo server: `sudo systemctl restart odoo`
3. Update assets: Go to Settings > Technical > User Interface > Views, search for "sign.NameAndSignature" and verify the override is loaded
4. Check browser console for JavaScript errors (F12)

### Assets Not Loading

**Problem**: CSS/XML changes not applied

**Solution**:
1. Enable developer mode: Settings > Activate Developer Mode
2. Go to Settings > Technical > User Interface > Assets
3. Search for "sign_remove_branding"
4. Verify assets are listed
5. Click "Regenerate Assets" if needed

## Uninstallation

To remove the module:

1. Go to **Apps** menu
2. Search for "Sign - Remove Branding"
3. Click **Uninstall**
4. Restart Odoo server
5. Clear browser cache

## Advanced Configuration

### Remove Hash as Well

If you want to also remove the hash from the signature frame:

1. Edit `custom/addons/sign_remove_branding/static/src/scss/sign_remove_branding.scss`
2. Uncomment lines 14-18:
```scss
:after {
    content: '' !important;
    display: none !important;
}
```
3. Restart Odoo and clear browser cache

### Completely Remove Frame

To completely hide the signature frame:

1. Edit `custom/addons/sign_remove_branding/static/src/scss/sign_remove_branding.scss`
2. Uncomment lines 25-30:
```scss
.modal {
    .o_sign_frame {
        display: none !important;
        visibility: hidden !important;
    }
}
```
3. Restart Odoo and clear browser cache

## Support

For issues or questions:
1. Check Odoo logs: `/var/log/odoo/odoo.log`
2. Enable debug mode and check browser console
3. Verify module dependencies are installed
4. Contact your system administrator

## Version History

- **1.0.0** (2026-01-12): Initial release
  - Removes "Signed with Odoo Sign" branding
  - Compatible with Odoo 19.0

