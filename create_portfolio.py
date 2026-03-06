import os

# Create images/portfolio/ dir if doesn't exist
os.makedirs(r"c:\Users\ADMIN\Desktop\Mystic Digital Solutions\images\portfolio", exist_ok=True)

# Generate portfolio.html
index_path = r"c:\Users\ADMIN\Desktop\Mystic Digital Solutions\index.html"
portfolio_path = r"c:\Users\ADMIN\Desktop\Mystic Digital Solutions\portfolio.html"

with open(index_path, 'r', encoding='utf-8') as f:
    index_content = f.read()

# Extract head, header, footer
head_end = index_content.find("</head>") + len("</head>")
head_content = index_content[:head_end].replace("<title>Mystic Digital Solutions | Agence Digitale en Afrique de l'Ouest</title>", "<title>Nos Réalisations | Mystic Digital Solutions</title>")
# Update active state if any, though none currently in static HTML
header_start = index_content.find('<body>')
header_end = index_content.find('<!-- ===================== HERO ===================== -->')
if header_end == -1:
    header_end = index_content.find('<section class="hero"')

header_content = index_content[header_start:header_end]

footer_start = index_content.find('<!-- ===================== CTA FINAL ===================== -->')
if footer_start == -1:
    footer_start = index_content.find('<section class="cta-final"')
footer_content = index_content[footer_start:]

portfolio_body = """
  <!-- ===================== PORTFOLIO HERO ===================== -->
  <section class="portfolio-hero">
    <div class="container">
      <h1 class="fade-in">Nos Réalisations</h1>
      <p class="fade-in fade-delay-1">Découvrez comment nous transformons les organisations africaines grâce au numérique.</p>
      <div style="margin-top: 24px;" class="fade-in fade-delay-2">
        <a href="index.html" style="color: var(--white); text-decoration: none; opacity: 0.8; font-size: 14px;">&larr; Retour à l'accueil</a>
      </div>
    </div>
  </section>

  <!-- ===================== PORTFOLIO FILTERS & GRID ===================== -->
  <section class="portfolio-page-content" style="padding: 80px 0; background: var(--bg-light);">
    <div class="container">
      
      <div class="portfolio-filters fade-in">
        <button class="portfolio-filter-btn" data-filter="tous">Tous</button>
        <button class="portfolio-filter-btn" data-filter="sante">Santé</button>
        <button class="portfolio-filter-btn" data-filter="btp">BTP</button>
        <button class="portfolio-filter-btn" data-filter="ong">ONG</button>
        <button class="portfolio-filter-btn" data-filter="education">Éducation</button>
        <button class="portfolio-filter-btn" data-filter="juridique">Juridique</button>
        <button class="portfolio-filter-btn" data-filter="fintech">Fintech</button>
      </div>

      <div class="portfolio-grid portfolio-grid-page">
        <!-- Projet 1 -->
        <div class="portfolio-card fade-in" data-category="sante">
          <div class="portfolio-image-wrapper">
            <img src="images/portfolio/clinipro.png" alt="Médecin africain utilisant une tablette dans une clinique moderne" loading="lazy">
            <span class="portfolio-sector-tag">Santé</span>
          </div>
          <div class="portfolio-content">
            <h3>CliniPro : Digitalisation d'une clinique à Cotonou</h3>
            <p class="portfolio-description">Développement d'un dossier patient numérique complet et d'un tableau de bord de gestion pour une clinique de 45 lits à Cotonou.</p>
            <div class="portfolio-results">
              <div class="portfolio-result-item">✅ -60% temps de recherche patient</div>
              <div class="portfolio-result-item">✅ +35% nouveaux patients</div>
              <div class="portfolio-result-item">✅ -70% erreurs facturation</div>
            </div>
            <div class="portfolio-tags">
              <span class="portfolio-tag">React</span><span class="portfolio-tag">PostgreSQL</span><span class="portfolio-tag">Node.js</span><span class="portfolio-tag">Power BI</span>
            </div>
          </div>
        </div>

        <!-- Projet 2 -->
        <div class="portfolio-card fade-in" data-category="btp">
          <div class="portfolio-image-wrapper">
            <img src="images/portfolio/batigroup.png" alt="Chef de chantier africain avec tablette" loading="lazy">
            <span class="portfolio-sector-tag">BTP</span>
          </div>
          <div class="portfolio-content">
            <h3>BatiGroup : Suivi de chantier en temps réel</h3>
            <p class="portfolio-description">Application mobile de suivi de 5 chantiers simultanés avec pointage ouvriers, consommation matériaux, photos géolocalisées.</p>
            <div class="portfolio-results">
              <div class="portfolio-result-item">✅ -25% dépassements budgétaires</div>
              <div class="portfolio-result-item">✅ 2h récupérées/semaine</div>
              <div class="portfolio-result-item">✅ Visibilité totale 5 chantiers</div>
            </div>
            <div class="portfolio-tags">
              <span class="portfolio-tag">PWA</span><span class="portfolio-tag">React</span><span class="portfolio-tag">N8N</span><span class="portfolio-tag">GPS</span><span class="portfolio-tag">PDF auto</span>
            </div>
          </div>
        </div>

        <!-- Projet 3 -->
        <div class="portfolio-card fade-in" data-category="ong">
          <div class="portfolio-image-wrapper">
            <img src="images/portfolio/impactplus.png" alt="Agent de terrain africain" loading="lazy">
            <span class="portfolio-sector-tag">ONG</span>
          </div>
          <div class="portfolio-content">
            <h3>ImpactPlus : Plateforme de suivi pour une ONG</h3>
            <p class="portfolio-description">Système de mesure d'impact et collecte de données terrain hors connexion pour une ONG opérant dans 12 communes rurales du Bénin.</p>
            <div class="portfolio-results">
              <div class="portfolio-result-item">✅ Reporting en 1 jour vs 2 sem.</div>
              <div class="portfolio-result-item">✅ 100% données capturées</div>
            </div>
            <div class="portfolio-tags">
              <span class="portfolio-tag">PWA offline</span><span class="portfolio-tag">KoboToolbox</span><span class="portfolio-tag">LaTeX</span><span class="portfolio-tag">Dashboard</span>
            </div>
          </div>
        </div>

        <!-- Projet 4 -->
        <div class="portfolio-card fade-in" data-category="education">
          <div class="portfolio-image-wrapper">
            <img src="images/portfolio/unisavoir.png" alt="Étudiant africain utilisant un ordinateur" loading="lazy">
            <span class="portfolio-sector-tag">Éducation</span>
          </div>
          <div class="portfolio-content">
            <h3>UniSavoir : Plateforme e-learning universitaire</h3>
            <p class="portfolio-description">Plateforme d'apprentissage en ligne pour une université de 3000 étudiants avec cours vidéo, quiz interactifs, suivi de progression.</p>
            <div class="portfolio-results">
              <div class="portfolio-result-item">✅ +25% taux de réussite</div>
              <div class="portfolio-result-item">✅ -80% temps traitement admin</div>
              <div class="portfolio-result-item">✅ 100% accès flexible</div>
            </div>
            <div class="portfolio-tags">
              <span class="portfolio-tag">React</span><span class="portfolio-tag">Node.js</span><span class="portfolio-tag">PostgreSQL</span><span class="portfolio-tag">Video streaming</span><span class="portfolio-tag">LaTeX</span>
            </div>
          </div>
        </div>

        <!-- Projet 5 -->
        <div class="portfolio-card fade-in" data-category="juridique">
          <div class="portfolio-image-wrapper">
            <img src="images/portfolio/lexafrica.png" alt="Avocat africain dans un bureau en bois moderne" loading="lazy">
            <span class="portfolio-sector-tag">Juridique</span>
          </div>
          <div class="portfolio-content">
            <h3>LexAfrica : Portail client pour cabinet juridique</h3>
            <p class="portfolio-description">Système de gestion numérique des dossiers clients avec portail sécurisé, génération automatique de documents en LaTeX et facturation.</p>
            <div class="portfolio-results">
              <div class="portfolio-result-item">✅ -65% temps recherche dossiers</div>
              <div class="portfolio-result-item">✅ +45% satisfaction client</div>
              <div class="portfolio-result-item">✅ Gain 3h/document</div>
            </div>
            <div class="portfolio-tags">
              <span class="portfolio-tag">React</span><span class="portfolio-tag">AES-256</span><span class="portfolio-tag">2FA</span><span class="portfolio-tag">LaTeX</span><span class="portfolio-tag">Node.js</span>
            </div>
          </div>
        </div>

        <!-- Projet 6 -->
        <div class="portfolio-card fade-in" data-category="fintech">
          <div class="portfolio-image-wrapper">
            <img src="images/portfolio/paysafe.png" alt="Africain payant avec téléphone Mobile Money" loading="lazy">
            <span class="portfolio-sector-tag">Fintech</span>
          </div>
          <div class="portfolio-content">
            <h3>PaySafe : Intégration Mobile Money</h3>
            <p class="portfolio-description">Intégration complète des API MTN MoMo, Moov Money et Celtiis pour une plateforme de microfinance servant 2000 clients.</p>
            <div class="portfolio-results">
              <div class="portfolio-result-item">✅ -40% taux de défaut</div>
              <div class="portfolio-result-item">✅ Productivité agent x2</div>
              <div class="portfolio-result-item">✅ Conformité BCEAO garantie</div>
            </div>
            <div class="portfolio-tags">
              <span class="portfolio-tag">Node.js</span><span class="portfolio-tag">API Mobile Money</span><span class="portfolio-tag">PostgreSQL</span><span class="portfolio-tag">Power BI</span>
            </div>
          </div>
        </div>
      </div>

      <div class="text-center fade-in" style="margin-top: 64px;">
        <h3 style="font-size:24px; color:var(--text-dark); margin-bottom:24px;">Vous avez un projet similaire ? Parlons-en &rarr;</h3>
        <a href="index.html#contact" class="btn btn-primary">Nous contacter</a>
      </div>
    </div>
  </section>

  <script>
    // Portfolio filtering script
    document.addEventListener('DOMContentLoaded', () => {
      const filterBtns = document.querySelectorAll('.portfolio-filter-btn');
      const cards = document.querySelectorAll('.portfolio-card');
      
      filterBtns.forEach(btn => {
        btn.addEventListener('click', () => {
          // Remove active class from all
          filterBtns.forEach(b => b.classList.remove('active'));
          // Add active class to clicked
          btn.classList.add('active');
          
          const filter = btn.getAttribute('data-filter');
          
          cards.forEach(card => {
            if (filter === 'tous' || card.getAttribute('data-category') === filter) {
              card.style.display = 'flex';
            } else {
              card.style.display = 'none';
            }
          });
        });
      });
      // Set active default
      const defaultBtn = document.querySelector('[data-filter="tous"]');
      if(defaultBtn) defaultBtn.classList.add('active');
    });
  </script>
"""

final_portfolio = head_content + header_content + portfolio_body + footer_content

with open(portfolio_path, 'w', encoding='utf-8') as f:
    f.write(final_portfolio)

print("portfolio.html cree.")
