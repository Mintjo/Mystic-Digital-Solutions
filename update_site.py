import os
import re

print("Starting update script...")

# 1. Update CSS
css_path = 'css/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Make sure we don't duplicate
if 'translateY(-8px) scale(1.02)' not in css:
    css = css.replace(
    """.portfolio-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
}""", 
    """.portfolio-card:hover {
  transform: translateY(-8px) scale(1.02);
  box-shadow: 0 16px 32px rgba(37, 99, 235, 0.15);
  border-color: var(--blue);
}"""
    )

if '.btn-outline-blue' not in css:
    css += """
.btn-outline-blue {
  background: transparent;
  color: var(--blue);
  border: 1px solid var(--blue);
}
.btn-outline-blue:hover {
  background: var(--blue);
  color: var(--white);
}
"""
with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

css_min_path = 'css/style.min.css'
try:
    with open(css_min_path, 'r', encoding='utf-8') as f:
        min_css = f.read()
    min_css = min_css.replace('transform:translateY(-4px);box-shadow:0 8px 24px rgba(0,0,0,0.1)', 'transform:translateY(-8px) scale(1.02);box-shadow:0 16px 32px rgba(37,99,235,0.15);border-color:var(--blue)')
    if '.btn-outline-blue' not in min_css:
        min_css += '.btn-outline-blue{background:transparent;color:var(--blue);border:1px solid var(--blue)}.btn-outline-blue:hover{background:var(--blue);color:var(--white)}'
    with open(css_min_path, 'w', encoding='utf-8') as f:
        f.write(min_css)
except Exception as e:
    print(f"Failed to update min css: {e}")

# 2. HTML Text Replacements
def apply_replacements(content):
    # CliniPro
    content = content.replace("CliniPro : Digitalisation d'une clinique à Cotonou", "Clinique Mahougnon : Digitalisation des services")
    content = content.replace("CliniPro Benin", "Clinique Mahougnon")
    content = content.replace("CliniPro", "Clinique Mahougnon")
    content = content.replace("clinipro.svg", "clinique-mahougnon.svg")
    
    # BatiGroup
    content = content.replace("BatiGroup : Suivi de chantier en temps réel", "AGETEP : Suivi de chantier en temps réel")
    content = content.replace("BatiGroup Cotonou", "AGETEP")
    content = content.replace("BatiGroup", "AGETEP")
    content = content.replace("batigroup.svg", "agetep.svg")
    
    # UniSavoir
    content = content.replace("UniSavoir : Plateforme e-learning universitaire", "African School of Science : Plateforme e-learning")
    content = content.replace("UniSavoir Afrique", "African School of Science")
    content = content.replace("UniSavoir", "African School of Science")
    content = content.replace("unisavoir.svg", "african-school-of-science.svg")
    
    # LexAfrica
    content = content.replace("LexAfrica : Portail client pour cabinet juridique", "Cabinet ASL : Portail client pour cabinet d'avocats")
    content = content.replace("LexAfrica Conseil", "Cabinet ASL")
    content = content.replace("LexAfrica", "Cabinet ASL")
    content = content.replace("lexafrica.svg", "cabinet-asL.svg")
    
    # PaySafe
    content = content.replace("PaySafe : Intégration Mobile Money", "Sofishop : Intégration Paiement Mobile & E-commerce")
    content = content.replace("PaySafe Mobile", "Sofishop")
    content = content.replace("PaySafe", "Sofishop")
    content = content.replace("paysafe.svg", "sofishop.svg")
    
    # ImpactPlus
    content = content.replace("ImpactPlus : Plateforme de suivi pour une ONG", "ONG Africa For Data Impact : Plateforme de suivi")
    content = content.replace("ImpactPlus Foundation", "ONG Africa For Data Impact")
    content = content.replace("ImpactPlus", "ONG Africa For Data Impact")
    content = content.replace("impactplus.svg", "africa-for-data-impact.svg")
    
    return content

for filepath in ['portfolio.html', 'index.html']:
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    html = apply_replacements(html)
    
    # Add Brochure Button in index.html
    if filepath == 'index.html':
        btn_html = '''<div style="display: flex; flex-direction: column; gap: 12px; width: 100%;">
            <a href="documents/brochure-mds.pdf" class="btn btn-outline-blue" download style="justify-content:center;">
              <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" style="width:18px;height:18px;margin-right:8px;">
                <path stroke-linecap="round" stroke-linejoin="round" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4" />
              </svg>
              Télécharger notre brochure
            </a>
            <a href="#contact" class="btn btn-outline-white" style="justify-content:center;">En savoir plus sur nous</a>
          </div>'''
        
        # Replace the old button with the new grouped buttons
        old_btn = '<a href="#contact" class="btn btn-outline-white" style="width:100%;justify-content:center;">En savoir plus sur nous</a>'
        if old_btn in html:
            html = html.replace(old_btn, btn_html)
        else:
            print(f"Warning: Old btn not found exactly in {filepath}")
            # regex approach
            if "Télécharger notre brochure" not in html:
                html = re.sub(r'<a href="#contact" class="btn btn-outline-white"[^>]*>En savoir plus sur nous</a>', btn_html, html)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)

print("HTML and CSS modified.")

# 3. Generating new SVG Logos
os.makedirs('images/logos', exist_ok=True)
logos_to_create = {
    'clinique-mahougnon.svg': 'Clinique Mahougnon',
    'agetep.svg': 'AGETEP',
    'african-school-of-science.svg': 'African School of Sci.',
    'cabinet-asL.svg': 'Cabinet ASL',
    'sofishop.svg': 'Sofishop',
    'africa-for-data-impact.svg': 'Africa Data Impact'
}

for filename, text in logos_to_create.items():
    svg_content = f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 200 60" width="200" height="60">
  <text x="50%" y="50%" dominant-baseline="middle" text-anchor="middle" font-family="Inter, sans-serif" font-weight="700" font-size="16" fill="#94A3B8">{text}</text>
</svg>'''
    with open(f"images/logos/{filename}", 'w', encoding='utf-8') as f:
        f.write(svg_content)

print("SVGs created.")

# 4. Generate dummy PDF
os.makedirs('documents', exist_ok=True)
pdf_content = b"%PDF-1.4\n1 0 obj\n<< /Type /Catalog /Pages 2 0 R >>\nendobj\n2 0 obj\n<< /Type /Pages /Kids [3 0 R] /Count 1 >>\nendobj\n3 0 obj\n<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] >>\nendobj\nxref\n0 4\n0000000000 65535 f \n0000000009 00000 n \n0000000056 00000 n \n0000000111 00000 n \ntrailer\n<< /Size 4 /Root 1 0 R >>\nstartxref\n190\n%%EOF"
with open('documents/brochure-mds.pdf', 'wb') as f:
    f.write(pdf_content)

print("PDF created.")
print("Script finished natively.")
