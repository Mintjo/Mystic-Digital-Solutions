import shutil
import os

print("Starting custom hero replace...")

src = r"C:\Users\ADMIN\.gemini\antigravity\brain\f5c3b357-cea7-4d7c-8664-dc9b3a857b71\hero_professional_1774095651681.png"
dst = r"images/hero/hero-main-new.png"

# Ensure dir exists although it should already
os.makedirs(os.path.dirname(dst), exist_ok=True)
shutil.copy(src, dst)

for filepath in ['index.html', 'css/style.css', 'css/style.min.css']:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        content = content.replace("hero-main.webp", "hero-main-new.png")
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {filepath}")
    except Exception as e:
        print(f"Failed to update {filepath}: {e}")

print("Hero updated and references changed.")
