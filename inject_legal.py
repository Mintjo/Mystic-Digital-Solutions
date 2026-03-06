import os
import re

base_dir = r"c:\Users\ADMIN\Desktop\Mystic Digital Solutions"

new_html = r'''<div class="footer-bottom-info" style="display: flex; flex-direction: column; align-items: center;">
          <p class="footer-bottom-text" style="margin: 0;">\1</p>
          <div style="font-size: 11px; color: #64748B; font-weight: normal; margin-top: 8px; text-align: center;">RCCM : RB/NAT/22 A 2010 | IFU : 0202213876129</div>
        </div>'''

# Match either the full text or the short text, but don't re-wrap if already wrapped
pattern = re.compile(r'<p class="footer-bottom-text"(?: style="margin:\s*0;")?>(© 2025 MDS Digital Solutions(?:[^<]*))</p>')

def inject_legal(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # If it's already got the RCCM, skip
        if "RCCM : RB/NAT/22 A 2010" in content:
            print(f"Skipped (already done): {os.path.basename(filepath)}")
            return

        # Replace using regex, keeping the original inner text (\1)
        if pattern.search(content):
            new_content = pattern.sub(new_html, content)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Update: {os.path.basename(filepath)}")
        else:
            print(f"Skipped (pattern not found): {os.path.basename(filepath)}")
    except Exception as e:
        print(f"Error on {filepath}: {e}")

# Process files in root
for f in os.listdir(base_dir):
    if f.endswith(".html"):
        inject_legal(os.path.join(base_dir, f))

# Process files in secteurs
secteurs_dir = os.path.join(base_dir, "secteurs")
if os.path.exists(secteurs_dir):
    for f in os.listdir(secteurs_dir):
        if f.endswith(".html"):
            inject_legal(os.path.join(secteurs_dir, f))

print("Modification termine via regex.")
