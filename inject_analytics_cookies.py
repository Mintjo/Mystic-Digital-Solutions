import os
import re

base_dir = r"c:\Users\ADMIN\Desktop\Mystic Digital Solutions"

# Identifiant Google Analytics (Gtag) - Remplacez G-XXXXXXXXXX par votre propre ID.
# On utilise un ID générique pour le moment, documenté pour le client.
GTAG_ID = "G-XXXXXXXXXX"

# Script Google Analytics
analytics_script = f"""
    <!-- Google tag (gtag.js) -->
    <script async src="https://www.googletagmanager.com/gtag/js?id={GTAG_ID}"></script>
    <script>
      window.dataLayer = window.dataLayer || [];
      function gtag(){{dataLayer.push(arguments);}}
      gtag('js', new Date());

      gtag('config', '{GTAG_ID}');
    </script>
"""

# Bannière Cookies (HTML à ajouter juste après <body>)
cookie_banner_html = """
    <!-- Cookie Banner -->
    <div id="cookie-banner" class="cookie-banner">
        <div class="container cookie-container">
            <p>Nous utilisons des cookies pour améliorer votre expérience, analyser notre trafic et personnaliser le contenu. En continuant à naviguer sur ce site, vous acceptez notre utilisation des cookies.</p>
            <div class="cookie-btns">
                <button id="cookie-accept" class="btn btn-primary">Accepter</button>
                <button id="cookie-decline" class="btn btn-outline-white" style="color:#1B1F3B; border-color:#1B1F3B;">Refuser</button>
            </div>
        </div>
    </div>
"""

def inject_in_files(directory):
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".html"):
                filepath = os.path.join(root, file)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()

                modified = False

                # 1. Inject Analytics before </head>
                if "googletagmanager.com/gtag/js" not in content and "</head>" in content:
                    content = content.replace("</head>", analytics_script + "</head>")
                    modified = True

                # 2. Inject Cookie banner just after <body>
                if "cookie-banner" not in content and "<body" in content:
                    # Find body opening tag precisely since it can have classes
                    body_match = re.search(r'<body[^>]*>', content)
                    if body_match:
                        body_tag = body_match.group(0)
                        content = content.replace(body_tag, body_tag + "\n" + cookie_banner_html)
                        modified = True

                if modified:
                    with open(filepath, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Injected Analytics & Cookies in: {filepath}")

inject_in_files(base_dir)
print("Injection done.")
