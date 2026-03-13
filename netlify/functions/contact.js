// =====================================================
//   MYSTIC DIGITAL SOLUTIONS — Netlify Function Contact
//   Enregistrement Supabase + Notification Email
// =====================================================

exports.handler = async (event) => {
  const headers = {
    'Access-Control-Allow-Origin': '*',
    'Access-Control-Allow-Methods': 'POST, OPTIONS',
    'Access-Control-Allow-Headers': 'Content-Type',
    'Content-Type': 'application/json'
  };

  if (event.httpMethod === 'OPTIONS') {
    return { statusCode: 200, headers, body: '' };
  }

  if (event.httpMethod !== 'POST') {
    return { statusCode: 405, headers, body: JSON.stringify({ error: 'Méthode non autorisée' }) };
  }

  let body;
  try {
    body = JSON.parse(event.body || '{}');
  } catch {
    return { statusCode: 400, headers, body: JSON.stringify({ error: 'Corps de requête invalide' }) };
  }

  const { nom, email, secteur, besoin, message } = body;

  // Validation basique
  if (!nom || !email || !secteur || !message) {
    return { statusCode: 400, headers, body: JSON.stringify({ error: 'Champs requis manquants' }) };
  }

  // === INSERTION SUPABASE ===
  const supabaseUrl = process.env.SUPABASE_URL;
  const supabaseServiceKey = process.env.SUPABASE_SERVICE_KEY;

  if (supabaseUrl && supabaseServiceKey) {
    try {
      const { createClient } = require('@supabase/supabase-js');
      const supabase = createClient(supabaseUrl, supabaseServiceKey);

      const { error: dbError } = await supabase
        .from('contact_messages')
        .insert([{ nom, email, secteur, besoin: besoin || 'Renseignement', message }]);

      if (dbError) {
        console.error('[MDS] Erreur Supabase :', dbError);
        return { statusCode: 500, headers, body: JSON.stringify({ error: "Erreur d'enregistrement. Veuillez réessayer." }) };
      }
    } catch (dbErr) {
      console.error('[MDS] Erreur Supabase :', dbErr);
      return { statusCode: 500, headers, body: JSON.stringify({ error: 'Erreur serveur' }) };
    }
  }

  // === ENVOI EMAIL VIA EMAILJS REST API ===
  const emailjsServiceId = process.env.EMAILJS_SERVICE_ID;
  const emailjsTemplateId = process.env.EMAILJS_TEMPLATE_ID;
  const emailjsPublicKey = process.env.EMAILJS_PUBLIC_KEY;
  const emailjsPrivateKey = process.env.EMAILJS_PRIVATE_KEY;

  if (emailjsServiceId && emailjsTemplateId && emailjsPublicKey && emailjsPrivateKey) {
    try {
      await fetch('https://api.emailjs.com/api/v1.0/email/send', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          service_id: emailjsServiceId,
          template_id: emailjsTemplateId,
          user_id: emailjsPublicKey,
          accessToken: emailjsPrivateKey,
          template_params: {
            from_name: nom,
            from_email: email,
            secteur,
            besoin: besoin || 'Renseignement',
            message,
            to_email: 'contact@mysticdigitalsolutions.com'
          }
        })
      });
    } catch (emailErr) {
      console.warn('[MDS] Avertissement envoi email :', emailErr);
      // Optionnel : ne bloque pas l'enregistrement
    }
  }

  return { statusCode: 200, headers, body: JSON.stringify({ success: true }) };
};
