import os

css_content = """
/* =====================================================
   PORTFOLIO (NOS REALISATIONS)
   ===================================================== */
.portfolio-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 32px;
  margin-top: 48px;
}

@media (max-width: 992px) {
  .portfolio-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

@media (max-width: 768px) {
  .portfolio-grid {
    grid-template-columns: 1fr;
  }
}

.portfolio-card {
  background: var(--white);
  border: 1px solid var(--border);
  border-radius: 12px;
  overflow: hidden;
  transition: all 0.3s ease;
  display: flex;
  flex-direction: column;
}

.portfolio-card:hover {
  transform: translateY(-4px);
  box-shadow: 0 8px 24px rgba(0, 0, 0, 0.1);
}

.portfolio-image-wrapper {
  position: relative;
  width: 100%;
  height: 200px;
}

.portfolio-image-wrapper img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.portfolio-sector-tag {
  position: absolute;
  top: 16px;
  left: 16px;
  background: var(--blue);
  color: var(--white);
  font-size: 11px;
  padding: 4px 12px;
  border-radius: 4px;
  font-weight: 600;
  text-transform: uppercase;
}

.portfolio-content {
  padding: 24px;
  flex: 1;
  display: flex;
  flex-direction: column;
}

.portfolio-content h3 {
  font-size: 18px;
  font-weight: 700;
  color: var(--text-dark);
  margin: 0 0 12px 0;
  line-height: 1.3;
}

.portfolio-description {
  font-size: 14px;
  color: var(--text-muted);
  line-height: 1.6;
  margin-bottom: 20px;
  display: -webkit-box;
  -webkit-line-clamp: 3;
  -webkit-box-orient: vertical;
  overflow: hidden;
  flex: 1;
}

.portfolio-results {
  background: #F0FDF4;
  border: 1px solid #BBF7D0;
  border-radius: 8px;
  padding: 12px;
  margin-bottom: 20px;
}

.portfolio-result-item {
  color: #166534;
  font-size: 13px;
  font-weight: 500;
  margin-bottom: 4px;
  display: flex;
  align-items: flex-start;
  gap: 8px;
}

.portfolio-result-item:last-child {
  margin-bottom: 0;
}

.portfolio-tags {
  display: flex;
  flex-wrap: wrap;
  gap: 6px;
}

.portfolio-tag {
  background: #EEF2FF;
  color: var(--blue);
  font-size: 11px;
  font-weight: 600;
  padding: 4px 8px;
  border-radius: 4px;
}

/* Portfolio Page specific */
.portfolio-filters {
  display: flex;
  justify-content: center;
  flex-wrap: wrap;
  gap: 12px;
  margin-bottom: 40px;
}

.portfolio-filter-btn {
  background: var(--white);
  border: 1px solid var(--border);
  color: var(--text-dark);
  font-size: 14px;
  font-weight: 500;
  padding: 8px 20px;
  border-radius: var(--radius-pill);
  cursor: pointer;
  transition: all 0.2s;
}

.portfolio-filter-btn:hover {
  background: var(--gray-light);
}

.portfolio-filter-btn.active {
  background: var(--blue);
  color: var(--white);
  border-color: var(--blue);
}

.portfolio-hero {
  background-color: var(--hero-bg);
  padding: 120px 0 60px 0;
  text-align: center;
}

.portfolio-hero h1 {
  color: var(--white);
  font-size: 40px;
  margin-bottom: 16px;
}

.portfolio-hero p {
  color: var(--text-hero);
  font-size: 18px;
  max-width: 600px;
  margin: 0 auto;
}

.portfolio-grid-page {
  grid-template-columns: repeat(2, 1fr);
}

@media (max-width: 768px) {
  .portfolio-grid-page {
    grid-template-columns: 1fr;
  }
}

"""

css_path = r"c:\Users\ADMIN\Desktop\Mystic Digital Solutions\css\style.css"

with open(css_path, "a", encoding="utf-8") as f:
    f.write(css_content)

print(f"Added classes to style.css")
