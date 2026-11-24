// Offline cache for Saratoga Springs Utah Crossroads Stake Emergency Operations Plan
// Keeps the plan, icons, and member illustrations available on phones even if cell networks fail.
const CACHE_NAME = 'crossroads-stake-eop-v4.2';
const ASSETS_TO_CACHE = [
  './',
  './index.html',
  './stake_leadership_presentationV4.html',
  './stake_leadership_presentation.html',
  './manifest.webmanifest',
  './assets/favicon.svg',
  './assets/apple-touch-icon.png',
  './assets/app-icon-192.png',
  './assets/app-icon-512.png',
  './assets/prep_01_family_peace.jpg',
  './assets/prep_02_aux_power_medical.jpg',
  './assets/prep_03_water_food_storage.jpg',
  './assets/prep_04_72hr_kit.jpg',
  './assets/prep_05_home_shutoffs_gathering.jpg'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => cache.addAll(ASSETS_TO_CACHE))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE_NAME).map((k) => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  if (event.request.method !== 'GET') return;
  event.respondWith(
    caches.match(event.request).then((cached) => {
      const networkFetch = fetch(event.request)
        .then((response) => {
          if (response && response.status === 200 && response.type === 'basic') {
            const copy = response.clone();
            caches.open(CACHE_NAME).then((cache) => cache.put(event.request, copy));
          }
          return response;
        })
        .catch(() => cached);
      return cached || networkFetch;
    })
  );
});
