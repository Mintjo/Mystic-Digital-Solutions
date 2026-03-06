import os

base_dir = r"c:\Users\ADMIN\Desktop\Mystic Digital Solutions"

def rename_portfolio(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # We want to replace "Portfolio" with "Nos Réalisations"
        # However, we must be careful not to replace "portfolio.html" filename or slugs if they should stay.
        # The user specifically mentioned navigation links and labels.
        
        # Replace ">Portfolio<" to catch menu items and footer links
        changed = False
        if ">Portfolio<" in content:
            content = content.replace(">Portfolio<", ">Nos Réalisations<")
            changed = True
        
        # Also replace "Portfolio" in nav links if it doesn't have tags around it (sometimes happens in scripts or attributes)
        # But we want to be safe. Let's look for common patterns in this site.
        
        # Link label in <a> tags
        # Search for >Portfolio</a> and replace with >Nos Réalisations</a>
        if ">Portfolio</a>" in content:
            content = content.replace(">Portfolio</a>", ">Nos Réalisations</a>")
            changed = True

        # Header of the portfolio page or sections
        if "<h1>Portfolio</h1>" in content:
            content = content.replace("<h1>Portfolio</h1>", "<h1>Nos Réalisations</h1>")
            changed = True
            
        # Specific search for the section label in index.html or other places
        if "Portfolio" in content:
            # Check specifically for label text in span or similar
            # But avoid replacing portfolio.html in href
            # The safest is to target the specific text nodes.
            pass

        if changed:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"Updated: {os.path.basename(filepath)}")
        else:
            print(f"No match in: {os.path.basename(filepath)}")
            
    except Exception as e:
        print(f"Error on {filepath}: {e}")

# Process files in root
for f in os.listdir(base_dir):
    if f.endswith(".html") or f == "README.md":
        rename_portfolio(os.path.join(base_dir, f))

# Process files in secteurs
secteurs_dir = os.path.join(base_dir, "secteurs")
if os.path.exists(secteurs_dir):
    for f in os.listdir(secteurs_dir):
        if f.endswith(".html"):
            rename_portfolio(os.path.join(secteurs_dir, f))

print("Renommage termine.")
