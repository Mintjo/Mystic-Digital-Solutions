import os

css_content = """
/* Project Card Footer (Duration & Link) */
.portfolio-footer {
  margin-top: 16px;
  padding-top: 16px;
  border-top: 1px solid #E5E7EB;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.portfolio-duration {
  font-size: 13px;
  color: var(--text-muted);
  display: flex;
  align-items: center;
  gap: 6px;
}

.portfolio-duration svg {
  width: 14px;
  height: 14px;
  color: var(--text-muted);
}

.portfolio-link {
  font-size: 14px;
  font-weight: 600;
  color: var(--blue);
  text-decoration: none;
  transition: color 0.2s;
}

.portfolio-link:hover {
  color: #1d4ed8;
}
"""

css_path = r"c:\Users\ADMIN\Desktop\Mystic Digital Solutions\css\style.css"

with open(css_path, "a", encoding="utf-8") as f:
    f.write(css_content)

print("Styles portfolio footer ajoutes.")
