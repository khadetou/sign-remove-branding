# Quick Start Guide

## Installation (3 Simple Steps)

### 1. Restart Odoo
```bash
sudo systemctl restart odoo
# or
./odoo-bin -c odoo.conf
```

### 2. Update Apps List
- Login as Administrator
- Go to **Apps** → **⋮** → **Update Apps List**

### 3. Install Module
- Search for "**Sign - Remove Branding**"
- Click **Install**
- Clear browser cache (Ctrl+Shift+R)

## What This Module Does

✅ **Removes** "Signed with Odoo Sign" text from signature frames  
✅ **Works** in backend, frontend, and public sign interfaces  
✅ **Keeps** the security hash (optional to remove)  
✅ **No configuration** needed - works automatically  

## Before & After

### Before Installation
```
┌─────────────────────────┐
│ Signed with Odoo Sign   │  ← This text appears
│  ┌──────────────────┐   │
│  │   [Signature]    │   │
│  └──────────────────┘   │
│ 742ae500e2...           │
└─────────────────────────┘
```

### After Installation
```
┌─────────────────────────┐
│                         │  ← Text removed!
│  ┌──────────────────┐   │
│  │   [Signature]    │   │
│  └──────────────────┘   │
│ 742ae500e2...           │
└─────────────────────────┘
```

## Optional Customizations

### Remove Hash Too
Edit `static/src/scss/sign_remove_branding.scss` and uncomment:
```scss
:after {
    content: '' !important;
    display: none !important;
}
```

### Remove Entire Frame
Edit `static/src/scss/sign_remove_branding.scss` and uncomment:
```scss
.modal {
    .o_sign_frame {
        display: none !important;
        visibility: hidden !important;
    }
}
```

## Verification

Run the verification script:
```bash
cd custom/addons/sign_remove_branding
python3 verify_module.py
```

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Module not visible | Update Apps List, check file permissions |
| Branding still shows | Clear browser cache, restart Odoo |
| Assets not loading | Regenerate assets in Settings > Technical |

## Files Modified (via Inheritance)

- ✏️ `sign/static/src/dialogs/sign_name_and_signature_dialog.xml`
- ✏️ `sign/static/src/scss/sign_common.scss`

**Note**: Original files are NOT modified. This module uses Odoo's inheritance system.

## Support

📖 See `INSTALLATION.md` for detailed instructions  
📖 See `README.md` for full documentation  

## License

LGPL-3

