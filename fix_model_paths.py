#!/usr/bin/env python3
"""
Fix QGIS Model Style Paths
Replaces hardcoded style paths with user-specific paths
"""

import os
import sys
import re

def get_qgis_profile_path():
    """Get the QGIS profile path for the current OS and user"""
    if sys.platform == 'win32':
        # Windows
        appdata = os.environ.get('APPDATA')
        if appdata:
            return os.path.join(appdata, 'QGIS', 'QGIS3', 'profiles', 'default')
    elif sys.platform == 'darwin':
        # macOS
        home = os.path.expanduser('~')
        return os.path.join(home, 'Library', 'Application Support', 'QGIS', 'QGIS3', 'profiles', 'default')
    else:
        # Linux
        home = os.path.expanduser('~')
        return os.path.join(home, '.local', 'share', 'QGIS', 'QGIS3', 'profiles', 'default')
    
    return None

def fix_model_paths(model_file, styles_dir='styles/tactile-maps'):
    """
    Replace hardcoded style paths in QGIS model with user-specific paths
    
    Args:
        model_file: Path to the .model or .model3 file
        styles_dir: Relative path to styles directory from QGIS profile
    """
    
    # Get QGIS profile path
    profile_path = get_qgis_profile_path()
    if not profile_path:
        print(f"[ERROR] Could not determine QGIS profile path for platform: {sys.platform}")
        return False
    
    # Convert to forward slashes for cross-platform compatibility
    profile_path = profile_path.replace('\\', '/')
    
    # Read the model file
    try:
        with open(model_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"[ERROR] Could not read {model_file}: {e}")
        return False
    
    # Find all .qml style references
    # Pattern matches: C:\Users\mauri\OneDrive - UGent\Masterproef\Stijlen\filename.qml
    # or any path ending in .qml
    pattern = r'value="[^"]*\\Stijlen\\([^"]+\.qml)"'
    
    # Count replacements
    matches = re.findall(pattern, content)
    if not matches:
        print(f"[WARNING] No style paths found in {model_file}")
        return True
    
    print(f"[INFO] Found {len(matches)} style references:")
    for match in set(matches):
        print(f"  - {match}")
    
    # Replace with new path
    def replace_path(match):
        filename = match.group(1)
        # Use forward slashes for cross-platform compatibility
        new_path = f'{profile_path}/{styles_dir}/{filename}'
        # For Windows compatibility in XML, use forward slashes (QGIS handles this)
        return f'value="{new_path}"'
    
    new_content = re.sub(pattern, replace_path, content)
    
    # Write back
    try:
        with open(model_file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"[OK] Updated {model_file}")
        print(f"[OK] Style paths now point to: {profile_path}/{styles_dir}/")
        return True
    except Exception as e:
        print(f"[ERROR] Could not write {model_file}: {e}")
        return False

def main():
    """Main function"""
    
    # Determine script directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Model files to fix
    models_dir = os.path.join(script_dir, 'models')
    model_files = []
    
    if os.path.exists(models_dir):
        for filename in ['Model.model', 'Model.model3']:
            filepath = os.path.join(models_dir, filename)
            if os.path.exists(filepath):
                model_files.append(filepath)
    
    if not model_files:
        print("[ERROR] No model files found in models/ directory")
        return 1
    
    print("=" * 60)
    print("  QGIS Model Style Paths Fixer")
    print("=" * 60)
    print()
    
    success = True
    for model_file in model_files:
        print(f"Processing: {os.path.basename(model_file)}")
        if not fix_model_paths(model_file):
            success = False
        print()
    
    if success:
        print("=" * 60)
        print("  ✓ All model files updated successfully!")
        print("=" * 60)
        return 0
    else:
        print("=" * 60)
        print("  ✗ Some errors occurred")
        print("=" * 60)
        return 1

if __name__ == '__main__':
    sys.exit(main())
