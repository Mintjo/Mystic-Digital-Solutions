import os
import re

base_dir = r"c:\Users\ADMIN\Desktop\Mystic Digital Solutions"
secteurs_dir = os.path.join(base_dir, "secteurs")

html_files = [os.path.join(base_dir, "index.html"), os.path.join(base_dir, "404.html")]
for f in os.listdir(secteurs_dir):
    if f.endswith('.html'):
        html_files.append(os.path.join(secteurs_dir, f))

for filepath in html_files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        old_content = content
        
        # Determine prefix
        prefix = "../" if "secteurs" in filepath else ""
        
        # 1. Update Favicons
        # Remove old icon links
        content = re.sub(r'<link rel="icon"[^>]*>\s*', '', content)
        content = re.sub(r'<link rel="apple-touch-icon"[^>]*>\s*', '', content)
        
        # Insert new icon link after <link rel="manifest" />
        # Wait, manifest.json matching
        new_icons = f'<link rel="icon" href="{prefix}mds_icon_classique.webp" type="image/webp" />\n  <link rel="apple-touch-icon" href="{prefix}mds_icon_classique.webp" />\n  '
        content = re.sub(r'<link rel="manifest".*?>\s*', lambda m: m.group(0) + new_icons, content, flags=re.IGNORECASE)
        
        # 2. Update Header Logo (mds_base_transparent.webp)
        content = re.sub(
            r'<a href="[^"]*" class="logo">\s*<img src="[^"]*"\s*alt="[^"]*"\s*class="logo-img"\s*/>\s*</a>',
            f'<a href="#" class="logo"><img src="{prefix}mds_base_transparent.webp" alt="MDS - Mystic Digital Solutions" class="logo-img" /></a>',
            content,
            flags=re.DOTALL
        )
        
        # 3. Update Footer Logo (mds_navbar_dark.webp)
        content = re.sub(
            r'<div class="footer-brand">\s*<img src="[^"]*"\s*alt="[^"]*"\s*class="logo-img"\s*/>',
            f'<div class="footer-brand">\n          <img src="{prefix}mds_navbar_dark.webp" alt="MDS - Mystic Digital Solutions" class="logo-img" />',
            content,
            flags=re.DOTALL
        )
            
        if content != old_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated logos in {os.path.basename(filepath)}")

print("Logo replacements complete.")
