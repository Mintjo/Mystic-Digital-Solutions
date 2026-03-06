import os

base_dir = r"c:\Users\ADMIN\Desktop\Mystic Digital Solutions"

def update_year(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        if "2025" in content:
            new_content = content.replace("2025", "2026")
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Update: {os.path.basename(filepath)}")
        else:
            print(f"Skipped: {os.path.basename(filepath)} (2025 not found)")
    except Exception as e:
        print(f"Error on {filepath}: {e}")

# Root HTML files
for f in os.listdir(base_dir):
    if f.endswith(".html"):
        update_year(os.path.join(base_dir, f))

# Secteurs HTML files
secteurs_dir = os.path.join(base_dir, "secteurs")
if os.path.exists(secteurs_dir):
    for f in os.listdir(secteurs_dir):
        if f.endswith(".html"):
            update_year(os.path.join(secteurs_dir, f))

print("Mise a jour de l'annee terminee.")
