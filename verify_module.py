#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Verification script for sign_remove_branding module
Run this script to verify the module structure is correct
"""

import os
import sys
from pathlib import Path

def check_file_exists(filepath, description):
    """Check if a file exists and print result"""
    if os.path.exists(filepath):
        print(f"✓ {description}: {filepath}")
        return True
    else:
        print(f"✗ {description} MISSING: {filepath}")
        return False

def check_file_content(filepath, search_string, description):
    """Check if a file contains specific content"""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            if search_string in content:
                print(f"✓ {description}")
                return True
            else:
                print(f"✗ {description} - Content not found")
                return False
    except Exception as e:
        print(f"✗ Error reading {filepath}: {e}")
        return False

def main():
    print("=" * 60)
    print("Sign Remove Branding Module - Verification Script")
    print("=" * 60)
    print()
    
    # Get module path
    module_path = Path(__file__).parent
    print(f"Module path: {module_path}")
    print()
    
    all_checks_passed = True
    
    # Check required files
    print("Checking required files...")
    print("-" * 60)
    
    required_files = [
        ('__manifest__.py', 'Manifest file'),
        ('__init__.py', 'Init file'),
        ('README.md', 'README file'),
        ('INSTALLATION.md', 'Installation guide'),
        ('static/src/xml/sign_name_and_signature_dialog.xml', 'XML override'),
        ('static/src/scss/sign_remove_branding.scss', 'SCSS override'),
        ('static/description/index.html', 'Description HTML'),
    ]
    
    for filename, description in required_files:
        filepath = module_path / filename
        if not check_file_exists(filepath, description):
            all_checks_passed = False
    
    print()
    
    # Check manifest content
    print("Checking manifest content...")
    print("-" * 60)
    
    manifest_path = module_path / '__manifest__.py'
    manifest_checks = [
        ("'name': 'Sign - Remove Branding'", "Module name"),
        ("'depends': ['sign']", "Dependency on sign module"),
        ("'installable': True", "Module is installable"),
        ("'assets':", "Assets defined"),
    ]
    
    for search_string, description in manifest_checks:
        if not check_file_content(manifest_path, search_string, description):
            all_checks_passed = False
    
    print()
    
    # Check XML override
    print("Checking XML override...")
    print("-" * 60)
    
    xml_path = module_path / 'static/src/xml/sign_name_and_signature_dialog.xml'
    xml_checks = [
        ('t-inherit="sign.NameAndSignature"', "Template inheritance"),
        ('sign_label', "Sign label attribute override"),
    ]
    
    for search_string, description in xml_checks:
        if not check_file_content(xml_path, search_string, description):
            all_checks_passed = False
    
    print()
    
    # Check SCSS override
    print("Checking SCSS override...")
    print("-" * 60)
    
    scss_path = module_path / 'static/src/scss/sign_remove_branding.scss'
    scss_checks = [
        ('.o_sign_frame.active', "Frame selector"),
        (':before', "Before pseudo-element"),
        ('display: none !important', "Display none rule"),
    ]
    
    for search_string, description in scss_checks:
        if not check_file_content(scss_path, search_string, description):
            all_checks_passed = False
    
    print()
    print("=" * 60)
    
    if all_checks_passed:
        print("✓ All checks passed! Module structure is correct.")
        print()
        print("Next steps:")
        print("1. Restart Odoo server")
        print("2. Update Apps List in Odoo")
        print("3. Install 'Sign - Remove Branding' module")
        print("4. Clear browser cache")
        return 0
    else:
        print("✗ Some checks failed. Please review the errors above.")
        return 1

if __name__ == '__main__':
    sys.exit(main())

