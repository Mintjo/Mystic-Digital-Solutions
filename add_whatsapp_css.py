import os

css_content = """
/* =====================================================
   WHATSAPP FLOATING BUTTON
   ===================================================== */
.whatsapp-float {
  position: fixed;
  bottom: 24px;
  right: 24px;
  background-color: #25D366;
  color: #FFF;
  width: 60px;
  height: 60px;
  border-radius: 50%;
  display: flex;
  justify-content: center;
  align-items: center;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
  z-index: 9999;
  transition: all 0.3s ease;
  text-decoration: none;
}

.whatsapp-float:hover {
  transform: translateY(-4px) scale(1.05);
  box-shadow: 0 6px 16px rgba(0, 0, 0, 0.2);
  color: #FFF;
}

.whatsapp-float svg {
  width: 35px;
  height: 35px;
  fill: currentColor;
}

@media (max-width: 768px) {
  .whatsapp-float {
    width: 50px;
    height: 50px;
    bottom: 20px;
    right: 20px;
  }
  
  .whatsapp-float svg {
    width: 30px;
    height: 30px;
  }
}
"""

css_path = r"c:\Users\ADMIN\Desktop\Mystic Digital Solutions\css\style.css"

with open(css_path, "a", encoding="utf-8") as f:
    f.write(css_content)

print("Styles WhatsApp ajoutes a style.css")
