import os
import re

base_dir = r"c:\Users\ADMIN\Desktop\Mystic Digital Solutions"
target_id = "G-8LZMS2YV5X"
placeholder = "G-XXXXXXXXXX"

def update_ga_in_file(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        if placeholder in content:
            new_content = content.replace(placeholder, target_id)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"MAJ Google Analytics: {os.path.basename(filepath)}")
    except Exception as e:
        print(f"Erreur sur {filepath}: {e}")

# Process files in root
for f in os.listdir(base_dir):
    if f.endswith(".html"):
        update_ga_in_file(os.path.join(base_dir, f))

# Process files in secteurs directory
secteurs_dir = os.path.join(base_dir, "secteurs")
if os.path.exists(secteurs_dir):
    for f in os.listdir(secteurs_dir):
        if f.endswith(".html"):
            update_ga_in_file(os.path.join(secteurs_dir, f))

print("Mise à jour de l'ID Google Analytics terminée sur tout le site.")
