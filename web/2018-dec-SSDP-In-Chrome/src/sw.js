//importScripts('/cache-polyfill.js');

self.addEventListener('install', function(e) {
 e.waitUntil(
   caches.open('airhorner').then(function(cache) {
     return cache.addAll([
       './',
       './index.html'/*,
       './images/j2i-32.jpeg',
       './images/j2i-64.jpeg',
       './images/j2i-128.jpeg',
       './scripts/app.js',
       './scripts/background.js',
       './scripts/jquery-3.3.1.min.js',
       './scripts/MulticastSocket.js',
       './styles/style.css',
       './manifest.json'*/
     ]);
   })
 );
});