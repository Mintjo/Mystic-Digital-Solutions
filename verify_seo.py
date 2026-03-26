import os
import re

base_dir = r"c:\Users\ADMIN\Desktop\Mystic Digital Solutions"
errors = []

for root, dirs, files in os.walk(base_dir):
    if "node_modules" in dirs:
        dirs.remove("node_modules")
    for file in files:
        if file.endswith(".html"):
            file_path = os.path.join(root, file)
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Check for img without alt
            # Regex to find <img ... > and ensure it contains alt="..."
            imgs = re.findall(r'<img[^>]*>', content, re.IGNORECASE)
            for img in imgs:
                if 'alt=' not in img.lower():
                    errors.append(f"Missing alt tag in {file_path}: {img}")
            
            # Check for www.mysticdigitalsolutions.com
            if 'www.mysticdigitalsolutions.com' in content:
                errors.append(f"Found 'www' domain in {file_path}")

if not errors:
    print("All checks passed!")
else:
    for err in errors:
        print(err)
