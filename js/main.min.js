// =====================================================
//   MYSTIC DIGITAL SOLUTIONS — MAIN JS
// =====================================================

// === FORMULAIRE — Les envois passent par /api/contact (serverless) ===

document.addEventListener('DOMContentLoaded', () => {

  // === COOKIE BANNER LOGIC ===
  const cookieBanner = document.getElementById('cookie-banner');
  const acceptBtn = document.getElementById('cookie-accept');
  const declineBtn = document.getElementById('cookie-decline');

  if (cookieBanner) {
    // Vérifier si un choix a déjà été fait
    const cookieConsent = localStorage.getItem('mds_cookie_consent');
    if (!cookieConsent) {
      // Si aucun choix, afficher la bannière avec un petit délai
      setTimeout(() => {
        cookieBanner.style.display = 'flex';
        cookieBanner.style.transform = 'translateY(0)';
      }, 1000);
    } else {
      // Sinon on cache
      cookieBanner.style.display = 'none';
      if (cookieConsent === 'accepted') {
        // Consentement déjà donné : activer GA immédiatement
        if (typeof gtag !== 'undefined') {
          gtag('consent', 'update', { 'analytics_storage': 'granted', 'ad_storage': 'granted' });
        }
      } else if (cookieConsent === 'declined') {
        // Refus confirmé : désactiver le suivi GA
        window['ga-disable-G-8LZMS2YV5X'] = true;
      }
    }

    // Gestion du clic Accepter
    acceptBtn?.addEventListener('click', () => {
      localStorage.setItem('mds_cookie_consent', 'accepted');
      // Activer Google Analytics après consentement explicite
      if (typeof gtag !== 'undefined') {
        gtag('consent', 'update', { 'analytics_storage': 'granted', 'ad_storage': 'granted' });
      }
      cookieBanner.style.transform = 'translateY(100%)';
      setTimeout(() => cookieBanner.style.display = 'none', 400);
    });

    // Gestion du clic Refuser
    declineBtn?.addEventListener('click', () => {
      localStorage.setItem('mds_cookie_consent', 'declined');
      window['ga-disable-G-8LZMS2YV5X'] = true; // Désactiver le suivi GA côté client
      cookieBanner.style.transform = 'translateY(100%)';
      setTimeout(() => cookieBanner.style.display = 'none', 400);
    });
  }

  // === HAMBURGER MENU ===
  const hamburger = document.getElementById('hamburger');
  const mobileNav = document.getElementById('mobileNav');

  if (hamburger && mobileNav) {
    hamburger.addEventListener('click', () => {
      hamburger.classList.toggle('open');
      mobileNav.classList.toggle('open');
    });

    // Close mobile nav on link click
    mobileNav.querySelectorAll('a').forEach(link => {
      link.addEventListener('click', () => {
        hamburger.classList.remove('open');
        mobileNav.classList.remove('open');
      });
    });
  }

  // Close mobile nav on outside click
  document.addEventListener('click', (e) => {
    if (mobileNav && mobileNav.classList.contains('open')) {
      if (!mobileNav.contains(e.target) && !hamburger.contains(e.target)) {
        hamburger.classList.remove('open');
        mobileNav.classList.remove('open');
      }
    }
  });

  // === ACTIVE NAV LINK ON SCROLL ===
  const sections = document.querySelectorAll('section[id]');
  const navLinks = document.querySelectorAll('.nav-links a');

  const updateActiveNav = () => {
    let current = '';
    sections.forEach(section => {
      const sectionTop = section.offsetTop - 100;
      if (window.scrollY >= sectionTop) {
        current = section.getAttribute('id');
      }
    });
    navLinks.forEach(link => {
      link.style.color = '';
      if (link.getAttribute('href') === `#${current}`) {
        link.style.color = '#fff';
        link.style.background = 'rgba(255,255,255,0.12)';
      } else {
        link.style.background = '';
      }
    });
  };
  window.addEventListener('scroll', updateActiveNav, { passive: true });

  // === FADE-IN ON SCROLL ===
  const fadeEls = document.querySelectorAll('.fade-in');

  const observerOptions = {
    threshold: 0.12,
    rootMargin: '0px 0px -40px 0px'
  };

  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, observerOptions);

  fadeEls.forEach(el => observer.observe(el));

  // === SMOOTH SCROLL for anchor links ===
  document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
      const target = document.querySelector(this.getAttribute('href'));
      if (target) {
        e.preventDefault();
        const headerOffset = 96; // top-bar + header height
        const elementPosition = target.getBoundingClientRect().top;
        const offsetPosition = elementPosition + window.scrollY - headerOffset;
        window.scrollTo({ top: offsetPosition, behavior: 'smooth' });
      }
    });
  });

  // === HEADER shadow on scroll ===
  const header = document.getElementById('header');
  if (header) {
    window.addEventListener('scroll', () => {
      if (window.scrollY > 10) {
        header.style.boxShadow = '0 4px 24px rgba(0,0,0,0.35)';
      } else {
        header.style.boxShadow = '0 2px 12px rgba(0,0,0,0.2)';
      }
    }, { passive: true });
  }

  // === COMPTEURS ANIMÉS (Hero stats) ===
  function animateCounter(el) {
    const target = parseInt(el.dataset.target, 10);
    const suffix = el.dataset.suffix || '';
    const duration = 2500; // ms (augmenté pour un meilleur rendu visuel)
    let start = null;

    function step(timestamp) {
      if (!start) start = timestamp;
      const elapsed = timestamp - start;
      const progress = Math.min(elapsed / duration, 1);
      // Easing ease-out cubique
      const eased = 1 - Math.pow(1 - progress, 3);
      const current = Math.round(eased * target);
      el.textContent = current + suffix;
      if (progress < 1) {
        requestAnimationFrame(step);
      } else {
        el.textContent = target + suffix; // Assurer la valeur finale
      }
    }
    requestAnimationFrame(step);
  }

  const counterEls = document.querySelectorAll('.counter[data-target]');
  if (counterEls.length > 0) {
    const counterObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if (entry.isIntersecting) {
          animateCounter(entry.target);
          counterObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.1 });

    counterEls.forEach(el => counterObserver.observe(el));
  }

  // === FAQ ACCORDÉON ===
  document.querySelectorAll('.faq-question').forEach(btn => {
    btn.addEventListener('click', () => {
      const item = btn.closest('.faq-item');
      const isOpen = item.classList.contains('open');

      // Fermer tous les items de la même colonne
      const col = btn.closest('.faq-col');
      if (col) {
        col.querySelectorAll('.faq-item.open').forEach(openItem => {
          openItem.classList.remove('open');
          openItem.querySelector('.faq-question').setAttribute('aria-expanded', 'false');
        });
      }

      // Ouvrir celui cliqué (si ce n'était pas déjà ouvert)
      if (!isOpen) {
        item.classList.add('open');
        btn.setAttribute('aria-expanded', 'true');
      }
    });
  });


  // === FORMULAIRE DE CONTACT ===
  const form = document.getElementById('contactForm');
  const formSuccess = document.getElementById('formSuccess');
  const submitBtn = document.getElementById('formSubmitBtn');

  function showError(inputId, errId, show) {
    const input = document.getElementById(inputId);
    const err = document.getElementById(errId);
    if (!input || !err) return;
    if (show) {
      input.classList.add('error');
      err.classList.add('visible');
    } else {
      input.classList.remove('error');
      err.classList.remove('visible');
    }
  }

  function validateForm() {
    let valid = true;
    const nom = document.getElementById('cf-nom');
    const email = document.getElementById('cf-email');
    const secteur = document.getElementById('cf-secteur');
    const message = document.getElementById('cf-message');

    // Nom
    if (!nom || nom.value.trim().length < 2) {
      showError('cf-nom', 'err-nom', true); valid = false;
    } else { showError('cf-nom', 'err-nom', false); }

    // Email
    const emailRe = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!email || !emailRe.test(email.value.trim())) {
      showError('cf-email', 'err-email', true); valid = false;
    } else { showError('cf-email', 'err-email', false); }

    // Secteur
    if (!secteur || !secteur.value) {
      showError('cf-secteur', 'err-secteur', true); valid = false;
    } else { showError('cf-secteur', 'err-secteur', false); }

    // Message
    if (!message || message.value.trim().length < 20) {
      showError('cf-message', 'err-message', true); valid = false;
    } else { showError('cf-message', 'err-message', false); }

    return valid;
  }

  if (form) {
    // Validation en temps réel sur chaque champ
    ['cf-nom', 'cf-email', 'cf-secteur', 'cf-message'].forEach(id => {
      const el = document.getElementById(id);
      if (el) el.addEventListener('input', validateForm);
    });

    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      if (!validateForm()) return;

      // Animation chargement
      submitBtn.classList.add('loading');
      submitBtn.textContent = 'Envoi en cours...';

      // Récupération des données
      const nom = document.getElementById('cf-nom').value.trim();
      const email = document.getElementById('cf-email').value.trim();
      const secteur = document.getElementById('cf-secteur').value;
      const message = document.getElementById('cf-message').value.trim();
      const besoin = form.querySelector('input[name="besoin"]:checked');
      const besoinVal = besoin ? besoin.value : 'Renseignement';

      const svgEnvoyer = '<svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2" style="width:18px;height:18px;"><path stroke-linecap="round" stroke-linejoin="round" d="M12 19l9 2-9-18-9 18 9-2zm0 0v-8" /></svg> Envoyer mon message';

      try {
        const response = await fetch('/.netlify/functions/contact', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ nom, email, secteur, besoin: besoinVal, message })
        });

        const data = await response.json();
        submitBtn.classList.remove('loading');
        submitBtn.innerHTML = svgEnvoyer;

        if (!response.ok) {
          let errMsg = document.getElementById('form-error-msg');
          if (!errMsg) {
            errMsg = document.createElement('p');
            errMsg.id = 'form-error-msg';
            errMsg.style.cssText = 'color:#ef4444;font-size:14px;margin-top:12px;text-align:center;';
            form.parentNode.insertBefore(errMsg, form.nextSibling);
          }
          errMsg.textContent = data.error || "Une erreur s'est produite. Veuillez réessayer ou nous écrire directement à contact@mysticdigitalsolutions.com";
        } else {
          form.style.display = 'none';
          if (formSuccess) formSuccess.classList.add('visible');
        }
      } catch (err) {
        console.error('[MDS] Erreur envoi formulaire :', err);
        submitBtn.classList.remove('loading');
        submitBtn.innerHTML = svgEnvoyer;
        // Fallback mailto si l'API n'est pas disponible
        const sujet = encodeURIComponent(`[MDS] Demande – ${secteur} – ${besoinVal}`);
        const corps = encodeURIComponent(`Nom : ${nom}\nEmail : ${email}\nSecteur : ${secteur}\nBesoin : ${besoinVal}\n\nMessage :\n${message}`);
        window.location.href = `mailto:contact@mysticdigitalsolutions.com?subject=${sujet}&body=${corps}`;
      }
    });
  }

});

// Réinitialiser le formulaire (appelé depuis le bouton succès)
function resetForm() {
  const form = document.getElementById('contactForm');
  const formSuccess = document.getElementById('formSuccess');
  if (form) { form.reset(); form.style.display = ''; }
  if (formSuccess) formSuccess.classList.remove('visible');
}

// =====================================================
//   ENREGISTREMENT DU SERVICE WORKER (PWA)
// =====================================================
if ('serviceWorker' in navigator) {
  window.addEventListener('load', () => {
    navigator.serviceWorker.register('/sw.js')
      .then(() => console.log('[MDS] Service Worker enregistré ✓'))
      .catch(err => console.warn('[MDS] Service Worker non enregistré :', err));
  });
}

// =====================================================
//   BACK TO TOP BUTTON
// =====================================================
const backToTop = document.getElementById('backToTop');
if (backToTop) {
  window.addEventListener('scroll', () => {
    if (window.scrollY > 400) {
      backToTop.classList.add('visible');
    } else {
      backToTop.classList.remove('visible');
    }
  }, { passive: true });
}
