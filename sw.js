// =====================================================
//  MDS SERVICE WORKER — Cache first pour les assets statiques
// =====================================================

const CACHE_NAME = 'mds-cache-v3';
const STATIC_ASSETS = [
    '/',
    '/index.html',
    '/css/style.css',
    '/js/main.js',
    '/manifest.json',
    '/mds_icon_classique.webp',
    '/assets/favicon.svg',
    '/assets/icon-192.svg',
    '/assets/icon-512.svg',
    '/404.html'
];

// Installation : mise en cache des assets statiques
self.addEventListener('install', (event) => {
    event.waitUntil(
        caches.open(CACHE_NAME).then((cache) => {
            return cache.addAll(STATIC_ASSETS);
        })
    );
    self.skipWaiting();
});

// Activation : suppression des anciens caches
self.addEventListener('activate', (event) => {
    event.waitUntil(
        caches.keys().then((keys) =>
            Promise.all(
                keys.filter((key) => key !== CACHE_NAME).map((key) => caches.delete(key))
            )
        )
    );
    self.clients.claim();
});

// Fetch : stratégie Network First, fallback cache
self.addEventListener('fetch', (event) => {
    // 1. Ignorer les requêtes vers des domaines externes (CSP + Erreurs de cache)
    if (!event.request.url.startsWith(self.location.origin)) {
        return; // Ne fait rien, laisse le navigateur gérer la requête normalement
    }

    // 2. Ignorer les requêtes non-GET
    if (event.request.method !== 'GET') return;

    event.respondWith(
        fetch(event.request)
            .then((response) => {
                // Mettre en cache la réponse si valide
                if (response && response.status === 200) {
                    const clone = response.clone();
                    caches.open(CACHE_NAME).then((cache) => cache.put(event.request, clone));
                }
                return response;
            })
            .catch(() => {
                // En cas d'échec réseau, servir depuis le cache
                return caches.match(event.request).then((cached) => {
                    if (cached) return cached;
                    // Fallback vers la page 404 pour les pages HTML
                    if (event.request.headers.get('accept').includes('text/html')) {
                        return caches.match('/404.html');
                    }
                });
            })
    );
});
