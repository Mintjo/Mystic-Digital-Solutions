const puppeteer = require('puppeteer');
const path = require('path');

async function generatePDF() {
  console.log('Lancement de Puppeteer pour générer la brochure PDF...');
  const browser = await puppeteer.launch({
    headless: "new"
  });
  const page = await browser.newPage();
  
  const htmlPath = `file://${path.join(__dirname, 'brochure-mds.html')}`;
  
  await page.goto(htmlPath, { waitUntil: 'networkidle0' });
  
  // Générer le PDF
  await page.pdf({
    path: path.join(__dirname, 'brochure-mds.pdf'),
    format: 'A4',
    printBackground: true,
    margin: {
      top: '0',
      bottom: '0',
      left: '0',
      right: '0'
    }
  });

  console.log('PDF généré avec succès dans documents/brochure-mds.pdf !');
  await browser.close();
}

generatePDF().catch(console.error);
