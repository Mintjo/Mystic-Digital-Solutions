import os
import re

base_dir = r"c:\Users\ADMIN\Desktop\Mystic Digital Solutions"
secteurs_dir = os.path.join(base_dir, "secteurs")

bad_sectors = ["agritech.html", "fintech.html", "logistique.html", "tourisme.html"]

texts = {
       "agritech.html": "Au cœur du continent, la grande agriculture performante de demain a vitalement, grandement et activement enfin commencé une forte et très bienvenue importante mutation profonde grandement favorisée et propulsée en grande échelle par les spectaculaires essors du révolutionnaire secteur digital très moderne indispensable aujourd'hui aux cultivateurs, producteurs ou regroupements coopératifs du monde rural moderne et de ses nombreux agro-industriels très investis. En associant judicieusement les plus fortes analyses fines de la très précieuse donnée concrète captée directement du terrain fertile, de l'irrigation aux moissons, l'expertise pointue et logicielle complète proposée et mise habilement en place techniquement par le cabinet MDS vient véritablement aider et supporter sereinement toute la chaîne vitale des immenses récoltes vivrières ou d'exportations modernes.",
       "fintech.html": "Le très passionnant grand et rigide univers très réglementé résolument international de la finance classique tout comme celui bancaire institutionnel ont très indubitablement, totalement, profondément et irrémédiablement vu naître et évoluer des prodigieuses merveilles telles les incontournables innovations et toutes récentes créatives révolutions purement, incontestablement purement numériques : le prolifique fabuleux secteur foisonnant si puissant des tout nouveaux systèmes intelligents de multiples et diversifiés paiements tous sans exception mobiles. MDS vous apporte avec certitude de la haute valeur technologique de conformité avec les portefeuilles ou logiciels pour vous garantir pleinement d'opérer confortablement dans toute cette immense arène technofinancière à tous vos formidables et multiples partenaires et si nombreux clients en ligne connectés avec l'application web ou mobile conçue par nous.",
       "logistique.html": "Le monde trépidant de la complexe et constante logistique du continent, tout comme l'univers très lié à lui du colossal transport physique des denses biens, implique obligatoirement par toute définition basique ou de haute performance, le plus fort niveau nécessaire hautement crucial de toute la visibilité d'ensemble continue sans faille et une extrême minutieuse coordination sans aucun équivoque à chaque étape précise charnière du grand réseau d'acheminement, d'entreposage temporaire et d'ultime livraisons. MDS accompagne la modernité impressionnante de tous les impressionnants et multiples défis ardus inhérents aux flottes de routiers avec la géolocalisation ou au maritime afin que l'ensemble entier fluide du maillon ne comporte absolument jamais de failles.",
       "tourisme.html": "À l'ère d'un engouement formidable de l'hôtellerie mondiale, ce beau secteur prestigieux du lointain inoubliable voyage a plus que jamais un irrépréhensible fort besoin d'excellentissimes, douces et attractives somptueuses superbes et conviviales nombreuses riches luxueuses attractives lumineuses formidables séjours d'expériences particulièrement uniques adaptées singulièrement à ses hôtes raffinés ou routards enthousiastes. Que ce grand hôtel magnifique, belle belle modeste ou fière chaleureuse grande et digne auberge rurale soit totalement aidée pour capter sa nouvelle superbe exigeante clientèle : voici toute la passionnante de MDS. Nous mettons joyeusement une fierté totale exceptionnelle à déployer sans pareils d'exceptionnels de grands complets de gestion intégrés parfaitement digitaux (exemples: PMS, réservations hôtelières directes etc.)."
}

alts = {
       "agritech.html": "Agriculteurs africains utilisant une application mobile",
       "fintech.html": "Paiement mobile en Afrique",
       "logistique.html": "Superviseur logistique africain devant une flotte de camions",
       "tourisme.html": "Guide touristique montrant un paysage sur tablette"
}

imgs = {
       "agritech.html": "agritech-context.jpg",
       "fintech.html": "fintech-context.jpg",
       "logistique.html": "logistique-context.jpg",
       "tourisme.html": "tourisme-context.jpg"
}

for sector in bad_sectors:
    filepath = os.path.join(secteurs_dir, sector)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Restore footer description
    content = re.sub(r'<p class="footer-desc sector-context-desc">.*?</p>', '<p class="footer-desc">Mystic Digital Solutions.</p>', content, flags=re.DOTALL)
    
    # If the image was injected in the footer, let's remove it if any (e.g. <img src="../images/secteurs/tourisme-context.jpg" ...>)
    # But wait, inject_images.py might have skipped it or added it. Just to be safe:
    content = re.sub(rf'\n\s*<img src="../images/secteurs/{imgs[sector]}".*?>', '', content, flags=re.DOTALL)

    # Fix the sector-context
    # Replace the whole <section class="sector-context"> bloc
    pattern = r'<section class="sector-context">\s*<div class="container">\s*<p>.*?</p>\s*</div>\s*</section>'
    
    img_tag = f'<img src="../images/secteurs/{imgs[sector]}" alt="{alts[sector]}" class="about-team-img fade-in" loading="lazy">'
    p_tag = f'<p class="fade-in fade-delay-1 sector-context-desc">{texts[sector]}</p>'
    replacement = f'<section class="sector-context">\n        <div class="container">\n            {img_tag}\n            {p_tag}\n        </div>\n    </section>'
    
    content = re.sub(pattern, replacement, content, flags=re.DOTALL)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        print(f"Fixed sector context and footer for {sector}")

# Fix logos in index.html, 404.html, and all secteurs
html_files = [os.path.join(base_dir, "index.html"), os.path.join(base_dir, "404.html")]
for f in os.listdir(secteurs_dir):
    if f.endswith('.html'):
        html_files.append(os.path.join(secteurs_dir, f))

for filepath in html_files:
    if os.path.exists(filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
            
        old_content = content
        if "secteurs" in filepath:
            content = content.replace('src="../assets/logo-mds.png"', 'src="../logo.webp"')
            content = content.replace('src="../images/logo-mds.png"', 'src="../logo.webp"')
            content = content.replace('src="../assets/logo-mds.webp"', 'src="../logo.webp"')
        else:
            content = content.replace('src="assets/logo-mds.png"', 'src="logo.webp"')
            content = content.replace('src="images/logo-mds.png"', 'src="logo.webp"')
            content = content.replace('src="assets/logo-mds.webp"', 'src="logo.webp"')
            
        if content != old_content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Fixed logo in {os.path.basename(filepath)}")

print("Fixes complete.")
