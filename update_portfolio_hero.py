import os
import re

print("Updating portfolio hero and filters...")

html_path = 'portfolio.html'
with open(html_path, 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Hero section in HTML
old_hero = re.search(r'<!-- ===================== PORTFOLIO HERO ===================== -->(.*?)<!-- ===================== PORTFOLIO FILTERS & GRID ===================== -->', html, re.DOTALL)

new_hero = '''<!-- ===================== PORTFOLIO HERO ===================== -->
  <section class="portfolio-hero">
    <div class="hero-pattern-overlay"></div>
    <div class="container" style="position: relative; z-index: 2;">
      <a href="index.html" class="portfolio-back-btn fade-in">
        <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" style="width:16px;height:16px;">
          <path stroke-linecap="round" stroke-linejoin="round" d="M10 19l-7-7m0 0l7-7m-7 7h18" />
        </svg>
        Retour à l'accueil
      </a>
      <h1 class="fade-in">Nos Réalisations</h1>
      <p class="fade-in fade-delay-1">Chaque projet est une histoire de transformation. Découvrez comment nous aidons les organisations africaines à atteindre l'excellence numérique.</p>
    </div>
  </section>

  <!-- ===================== PORTFOLIO FILTERS & GRID ===================== -->'''

if old_hero:
    html = html.replace(old_hero.group(0), new_hero)
else:
    print("Warning: Could not find exact hero block to replace.")

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html)

css_path = 'css/style.css'
with open(css_path, 'r', encoding='utf-8') as f:
    css = f.read()

# Replace CSS for portfolio-hero
old_css_hero = re.search(r'\.portfolio-hero \{.*?(?=\.portfolio-grid-page \{)', css, re.DOTALL)

new_css_hero = '''.portfolio-hero {
  background-color: #1B1F3B;
  min-height: 350px;
  position: relative;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 80px 0;
  overflow: hidden;
}

.hero-pattern-overlay {
  position: absolute;
  inset: 0;
  background-image: 
    linear-gradient(rgba(255,255,255,0.05) 1px, transparent 1px),
    linear-gradient(90deg, rgba(255,255,255,0.05) 1px, transparent 1px);
  background-size: 40px 40px;
  background-position: center;
  z-index: 1;
}

.portfolio-hero h1 {
  color: var(--white);
  font-size: 42px;
  font-weight: 700;
  margin-bottom: 16px;
  position: relative;
}

.portfolio-hero p {
  color: #C5C9D6;
  font-size: 16px;
  max-width: 650px;
  margin: 0 auto;
  position: relative;
  line-height: 1.6;
}

.portfolio-back-btn {
  position: absolute;
  top: -60px;
  left: 0;
  display: inline-flex;
  align-items: center;
  gap: 8px;
  color: var(--white);
  border: 1px solid rgba(255,255,255,0.3);
  padding: 8px 18px;
  border-radius: 30px;
  font-size: 14px;
  font-weight: 600;
  transition: all 0.2s ease;
  text-decoration: none;
}

.portfolio-back-btn:hover {
  background: rgba(255,255,255,0.1);
  border-color: var(--white);
}

@media (max-width: 768px) {
  .portfolio-back-btn {
    position: relative;
    top: 0;
    margin-bottom: 32px;
  }
  .portfolio-hero {
    padding: 100px 0 60px;
  }
  .portfolio-hero h1 {
    font-size: 32px;
  }
}

.portfolio-filters {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 12px;
  margin-bottom: 48px;
}

.portfolio-filter-btn {
  background: var(--white);
  border: none;
  color: var(--text-muted);
  font-size: 14px;
  font-weight: 600;
  padding: 10px 24px;
  border-radius: 30px;
  cursor: pointer;
  box-shadow: 0 2px 8px rgba(0,0,0,0.06);
  transition: all 0.3s ease;
}

.portfolio-filter-btn:hover {
  color: var(--blue);
  box-shadow: 0 4px 12px rgba(37,99,235,0.1);
  transform: translateY(-2px);
}

.portfolio-filter-btn.active {
  background: var(--blue);
  color: var(--white);
  box-shadow: 0 6px 16px rgba(37,99,235,0.25);
  transform: translateY(-2px);
}

'''

if old_css_hero:
    css = css.replace(old_css_hero.group(0), new_css_hero)
else:
    print("Warning: Could not find exact css hero block to replace.")
    css += "\\n" + new_css_hero

with open(css_path, 'w', encoding='utf-8') as f:
    f.write(css)

# Generate minified CSS easily (just removing newlines/spaces mostly for the updated part)
# or since this is just a single file update, let's keep it simple and clean.
css_min_path = 'css/style.min.css'
try:
    with open(css_path, 'r', encoding='utf-8') as f:
        full_css = f.read()
    
    # very rudimentary minifier for our changes, since it's just CSS
    minified = full_css.replace('\\n', '').replace(' {', '{').replace(': ', ':')
    with open(css_min_path, 'w', encoding='utf-8') as f:
        f.write(minified)
except Exception as e:
    print(f"Failed to minify: {e}")

print("Update completed.")
