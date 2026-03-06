import os
import glob
from PIL import Image

brain_dir = r"C:\Users\ADMIN\.gemini\antigravity\brain\02636933-3fe8-4ac9-8b85-84e9d898b807"
target_dir = r"c:\Users\ADMIN\Desktop\Mystic Digital Solutions\images\secteurs"
html_dir = r"c:\Users\ADMIN\Desktop\Mystic Digital Solutions\secteurs"

images_map = {
    "ong_content_": ("ong-services", "ong.html", "ONG africaine en réunion avec des bénéficiaires", False, True),
    "agritech_context_": ("agritech-context", "agritech.html", "Agriculteurs africains utilisant une application mobile", True, False),
    "agritech_services_": ("agritech-services", "agritech.html", "Tableau de bord agritech dans un champ", False, True),
    "fintech_context_": ("fintech-context", "fintech.html", "Paiement mobile en Afrique", True, False),
    "fintech_services_": ("fintech-services", "fintech.html", "Dashboard financier moderne tenu par des mains africaines", False, True),
    "logistique_context_": ("logistique-context", "logistique.html", "Superviseur logistique africain devant une flotte de camions", True, False),
    "logistique_services_": ("logistique-services", "logistique.html", "Tableau de bord logistique avec carte dynamique", False, True),
    "tourisme_context_": ("tourisme-context", "tourisme.html", "Guide touristique montrant un paysage sur tablette", True, False),
    "tourisme_services_": ("tourisme-services", "tourisme.html", "Interface de réservation hôtelière", False, True),
}

for img_prefix, (out_name, html_file, alt_text, is_context, is_services) in images_map.items():
    # Find newest matching png
    matches = glob.glob(os.path.join(brain_dir, f"{img_prefix}*.png"))
    if not matches:
        print(f"Skipping {img_prefix}, no PNG found.")
        continue
    
    # Sort by modification time, newest first
    matches.sort(key=os.path.getmtime, reverse=True)
    latest_img = matches[0]
    
    # Convert to JPG
    out_path = os.path.join(target_dir, f"{out_name}.jpg")
    img = Image.open(latest_img).convert("RGB")
    img.save(out_path, "JPEG", quality=85)
    print(f"Converted {latest_img} -> {out_path}")
    
    # Edit HTML
    html_path = os.path.join(html_dir, html_file)
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    img_tag = f'\n            <img src="../images/secteurs/{out_name}.jpg" alt="{alt_text}" class="about-team-img fade-in" loading="lazy">'
    
    if is_context and f"{out_name}.jpg" not in content:
        # Insert before <p class="fade-in fade-delay-1 sector-context-desc">
        target_str = '<p class="fade-in fade-delay-1 sector-context-desc">'
        if target_str in content:
            content = content.replace(target_str, img_tag + '\n            ' + target_str)
            print(f"Inserted context image in {html_file}")
            
    if is_services and f"{out_name}.jpg" not in content:
        # Insert before <div class="sector-services-grid">
        target_str = '<div class="sector-services-grid">'
        if target_str in content:
            content = content.replace(target_str, img_tag + '\n            ' + target_str)
            print(f"Inserted services image in {html_file}")
            
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(content)

print("Insertion process complete.")
