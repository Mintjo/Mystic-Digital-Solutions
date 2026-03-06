import os
import re

base_dir = r"c:\Users\ADMIN\Desktop\Mystic Digital Solutions"

# We must update both nav-links and mobile-nav in secteurs/*.html and 404.html.
# In secteurs, the href values start with ../index.html. For portfolio.html, it should be ../portfolio.html
# In 404, the href values start with index.html. For portfolio.html, it should be portfolio.html

def update_nav(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        changed = False

        # Desktop nav: Look for Secteurs link and insert Portfolio after it.
        # It usually is <a href="../index.html#secteurs">Secteurs</a>
        if 'secteurs/' in filepath.replace('\\', '/'):
            prefix = '../'
        else:
            prefix = ''

        search_desktop = f'<a href="{prefix}index.html#secteurs">Secteurs</a>'
        replace_desktop = f'{search_desktop}<a href="{prefix}portfolio.html">Portfolio</a>'

        search_desktop2 = f'<a href="{prefix}index.html#secteurs" class="mobile-link">Secteurs</a>'
        replace_desktop2 = f'{search_desktop2}<a href="{prefix}portfolio.html" class="mobile-link">Portfolio</a>'
        
        search_mobile = f'<nav class="mobile-nav" id="mobileNav"><a href="{prefix}index.html#secteurs">Secteurs</a>'
        replace_mobile = f'<nav class="mobile-nav" id="mobileNav"><a href="{prefix}index.html#secteurs">Secteurs</a><a href="{prefix}portfolio.html">Portfolio</a>'
        
        if search_desktop in content and replace_desktop not in content:
            content = content.replace(search_desktop, replace_desktop)
            changed = True
            
        if search_desktop2 in content and replace_desktop2 not in content:
            content = content.replace(search_desktop2, replace_desktop2)
            changed = True

        if search_mobile in content and replace_mobile not in content:
            content = content.replace(search_mobile, replace_mobile)
            changed = True

        if changed:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated {os.path.basename(filepath)}")
        else:
            print(f"No update for {os.path.basename(filepath)}")
            
    except Exception as e:
        print(f"Error on {filepath}: {e}")

# Process 404
update_nav(os.path.join(base_dir, "404.html"))

# Process secteurs
secteurs_dir = os.path.join(base_dir, "secteurs")
if os.path.exists(secteurs_dir):
    for f in os.listdir(secteurs_dir):
        if f.endswith(".html"):
            update_nav(os.path.join(secteurs_dir, f))

print("Update termine.")
