import os
import re
from datetime import datetime

base_dir = r"c:\Users\ADMIN\Desktop\Mystic Digital Solutions"
secteurs_dir = os.path.join(base_dir, "secteurs")
services_dir = os.path.join(base_dir, "services")
base_url = "https://mysticdigitalsolutions.com"

# 1. Generate robots.txt
robots_content = f"""User-agent: *
Allow: /
Sitemap: {base_url}/sitemap.xml
"""
with open(os.path.join(base_dir, "robots.txt"), "w", encoding="utf-8") as f:
    f.write(robots_content)
print("robots.txt généré.")

# 2. Get list of HTML files
html_files = []
# main pages
if os.path.exists(os.path.join(base_dir, "index.html")):
    html_files.append(("index.html", ""))
if os.path.exists(os.path.join(base_dir, "portfolio.html")):
    html_files.append(("portfolio.html", ""))

# secteurs
if os.path.exists(secteurs_dir):
    for f in os.listdir(secteurs_dir):
        if f.endswith(".html"):
            html_files.append((f, "secteurs/"))

# services
if os.path.exists(services_dir):
    for f in os.listdir(services_dir):
        if f.endswith(".html"):
            html_files.append((f, "services/"))

# 3. Generate sitemap.xml
today = datetime.now().strftime("%Y-%m-%d")
sitemap_content = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']

for filename, folder in html_files:
    url = f"{base_url}/{folder}{filename}"
    if filename == "index.html":
        priority = "1.0"
    elif filename == "portfolio.html":
        priority = "0.9"
    elif folder == "services/":
        priority = "0.9"
    else:
        priority = "0.8"
        
    sitemap_content.append("  <url>")
    sitemap_content.append(f"    <loc>{url}</loc>")
    sitemap_content.append(f"    <lastmod>{today}</lastmod>")
    sitemap_content.append(f"    <priority>{priority}</priority>")
    sitemap_content.append("  </url>")

sitemap_content.append("</urlset>")

with open(os.path.join(base_dir, "sitemap.xml"), "w", encoding="utf-8") as f:
    f.write("\n".join(sitemap_content))
print("sitemap.xml généré.")

# 4. Inject Missing OG Meta tags correctly
def inject_og_tags(filepath, rel_url):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract Title & Description to reuse
    title_match = re.search(r'<title>(.*?)</title>', content, re.IGNORECASE)
    desc_match = re.search(r'<meta\s+name=["\']description["\']\s+content=["\'](.*?)["\']', content, re.IGNORECASE)
    
    title = title_match.group(1).strip() if title_match else "Mystic Digital Solutions"
    desc = desc_match.group(1).strip() if desc_match else "Agence digitale — Data, Web, Automatisation"
    
    # Check if OG tags already exist, if so replace them to maintain consistency
    og_pattern = re.compile(r'<!-- Open Graph & SocialMeta -->.*?<meta name="twitter:description" content=".*?" />', re.DOTALL)
    
    og_tags = f"""<!-- Open Graph & SocialMeta -->
    <meta property="og:title" content="{title}" />
    <meta property="og:description" content="{desc}" />
    <meta property="og:type" content="website" />
    <meta property="og:url" content="{base_url}/{rel_url}" />
    <meta property="og:image" content="{base_url}/images/og_banner_dark.png" />
    <meta name="twitter:card" content="summary_large_image" />
    <meta name="twitter:title" content="{title}" />
    <meta name="twitter:description" content="{desc}" />
    <meta name="twitter:image" content="{base_url}/images/og_banner_dark.png" />"""
    
    if '<!-- Open Graph & SocialMeta -->' in content:
        new_content = og_pattern.sub(og_tags, content)
    else:
        # Inject before </head>
        new_content = re.sub(r'(</head>)', f'    {og_tags}\n\\1', content, flags=re.IGNORECASE)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"Mis à jour: {rel_url}")

# Batch process subpages
directories_to_scan = [("secteurs", "secteurs/"), ("services", "services/")]
for dir_name, prefix in directories_to_scan:
    d = os.path.join(base_dir, dir_name)
    if os.path.exists(d):
        for f in os.listdir(d):
            if f.endswith(".html"):
                inject_og_tags(os.path.join(d, f), f"{prefix}{f}")

print("Opération SEO terminée.")
