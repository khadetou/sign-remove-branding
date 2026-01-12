# Complete Guide - Sign Remove Branding Module

## 🎯 Executive Summary

This module removes the "Signed with Odoo Sign" branding from signature frames in Odoo 19's Sign module. The branding appears as text above signatures when users enable the security frame feature.

**Installation Time**: ~5 minutes  
**Difficulty**: Easy  
**Impact**: Visual only - no functional changes  

---

## 📖 Table of Contents

1. [Understanding the Problem](#understanding-the-problem)
2. [How the Module Works](#how-the-module-works)
3. [Installation](#installation)
4. [Verification](#verification)
5. [Customization](#customization)
6. [Troubleshooting](#troubleshooting)
7. [Technical Details](#technical-details)

---

## 🔍 Understanding the Problem

### What is the Branding?

When users sign documents in Odoo Sign with the "Frame" option enabled, a security frame appears around the signature with:
- **Text**: "Signed with Odoo Sign" (the branding we want to remove)
- **Border**: Teal-colored curved border on the left
- **Hash**: Security hash at the bottom

### Where Does It Appear?

1. **Signature Dialog**: When adopting/creating a signature
2. **PDF Documents**: Embedded as an image in the final signed PDF
3. **All Interfaces**: Backend, frontend, and public signing pages

### Why Remove It?

- White-label requirements
- Custom branding needs
- Client preferences
- Professional appearance

---

## ⚙️ How the Module Works

### The Original Flow

```
User Signs → Frame Rendered with "Signed with Odoo Sign" 
→ Captured as PNG Image → Stored in Database → Embedded in PDF
```

### With This Module

```
User Signs → Frame Rendered WITHOUT Branding 
→ Captured as Clean PNG → Stored in Database → Embedded in PDF
```

### Technical Approach

1. **XML Inheritance**: Overrides the template to remove branding attribute
2. **CSS Override**: Hides the pseudo-element that displays the text
3. **Asset Loading**: Ensures overrides load in all contexts

**Key Point**: Original Odoo files are NOT modified. Uses Odoo's inheritance system.

---

## 🚀 Installation

### Prerequisites

- ✅ Odoo 19.0 installed
- ✅ Sign module installed
- ✅ Administrator access
- ✅ SSH/terminal access to server

### Step-by-Step Installation

#### Step 1: Verify Module Location
```bash
ls -la custom/addons/sign_remove_branding/
```

Expected output: Module files listed

#### Step 2: Set Permissions (if needed)
```bash
sudo chown -R odoo:odoo custom/addons/sign_remove_branding
```

#### Step 3: Restart Odoo
```bash
# Using systemd
sudo systemctl restart odoo

# Or manually
./odoo-bin -c /path/to/odoo.conf
```

#### Step 4: Update Apps List
1. Login as Administrator
2. Go to **Apps** menu
3. Click **⋮** (three dots)
4. Select **Update Apps List**
5. Click **Update**

#### Step 5: Install Module
1. Remove "Apps" filter in Apps menu
2. Search: "Sign - Remove Branding"
3. Click **Install**
4. Wait for installation to complete

#### Step 6: Clear Browser Cache
- **Chrome/Edge**: `Ctrl + Shift + R` (Windows) or `Cmd + Shift + R` (Mac)
- **Firefox**: `Ctrl + F5` (Windows) or `Cmd + Shift + R` (Mac)
- **Safari**: `Cmd + Option + R` (Mac)

---

## ✅ Verification

### Automated Verification
```bash
cd custom/addons/sign_remove_branding
python3 verify_module.py
```

### Manual Verification

1. **Create Test Signature**:
   - Go to any signature request
   - Click to adopt/create signature
   - Enable "Frame" checkbox
   - **Verify**: No "Signed with Odoo Sign" text appears

2. **Test PDF Generation**:
   - Complete the signature
   - Download the signed PDF
   - **Verify**: Frame in PDF has no branding text

3. **Check All Interfaces**:
   - Test in backend (logged in as user)
   - Test in frontend (portal user)
   - Test in public signing (no login)

---

## 🎨 Customization

### Option 1: Remove Hash Too

The security hash at the bottom can also be removed:

1. Edit: `static/src/scss/sign_remove_branding.scss`
2. Find lines 13-18 (commented out)
3. Uncomment:
```scss
:after {
    content: '' !important;
    display: none !important;
}
```
4. Restart Odoo and clear cache

### Option 2: Remove Entire Frame

To completely hide the frame:

1. Edit: `static/src/scss/sign_remove_branding.scss`
2. Find lines 24-31 (commented out)
3. Uncomment:
```scss
.modal {
    .o_sign_frame {
        display: none !important;
        visibility: hidden !important;
    }
}
```
4. Restart Odoo and clear cache

### Option 3: Custom Branding

To replace with your own text:

1. Edit: `static/src/xml/sign_name_and_signature_dialog.xml`
2. Change line 7 from:
```xml
<attribute name="sign_label"></attribute>
```
to:
```xml
<attribute name="sign_label">Your Company Name</attribute>
```
3. Restart Odoo and clear cache

---

## 🐛 Troubleshooting

### Problem: Module Not Appearing

**Symptoms**: Can't find module in Apps list

**Solutions**:
```bash
# Check file permissions
ls -la custom/addons/sign_remove_branding/

# Check Odoo logs
tail -f /var/log/odoo/odoo.log

# Verify addons path in odoo.conf
grep addons_path /etc/odoo/odoo.conf
```

### Problem: Branding Still Visible

**Symptoms**: "Signed with Odoo Sign" text still appears

**Solutions**:
1. Hard refresh browser: `Ctrl + Shift + R`
2. Clear all browser data
3. Restart Odoo: `sudo systemctl restart odoo`
4. Check module is installed: Apps > Installed > Search "Sign - Remove Branding"
5. Regenerate assets: Settings > Technical > Assets > Regenerate

### Problem: Assets Not Loading

**Symptoms**: CSS/XML changes not applied

**Solutions**:
1. Enable debug mode: Add `?debug=1` to URL
2. Check browser console (F12) for errors
3. Verify assets in: Settings > Technical > User Interface > Assets
4. Search for "sign_remove_branding"
5. Click "Regenerate Assets" button

---

## 🔧 Technical Details

### Module Structure

