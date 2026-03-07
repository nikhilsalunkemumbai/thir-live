// =============================================
// main.js — THIR Entry Point & Utilities
// Wires up DOMContentLoaded, live simulation
// fallback, animated counters, and the footer clock.
// Depends on: data.js, pipeline.js, render.js, map.js
// =============================================

// --------------------------------------------------
// Theme: dark / light toggle with localStorage persistence
// --------------------------------------------------
const THEME_KEY = 'thir-theme';

function applyTheme(theme) {
  const html  = document.documentElement;
  const icon  = document.getElementById('theme-icon');
  const label = document.getElementById('theme-label');

  if (theme === 'light') {
    html.setAttribute('data-theme', 'light');
    if (icon)  icon.textContent  = '\u263D';  // crescent moon = click to go dark
    if (label) label.textContent = 'DARK';
  } else {
    html.removeAttribute('data-theme');
    if (icon)  icon.textContent  = '\u2600';  // sun = click to go light
    if (label) label.textContent = 'LIGHT';
  }
}

function initTheme() {
  // Respect saved preference; default to dark
  const saved = localStorage.getItem(THEME_KEY) || 'dark';
  applyTheme(saved);

  document.getElementById('theme-toggle').addEventListener('click', () => {
    const current = document.documentElement.getAttribute('data-theme') === 'light' ? 'light' : 'dark';
    const next    = current === 'light' ? 'dark' : 'light';
    applyTheme(next);
    localStorage.setItem(THEME_KEY, next);
  });
}

// --------------------------------------------------
// Mobile nav: hamburger toggle for .nav-drawer
// --------------------------------------------------
function initMobileNav() {
  const btn    = document.getElementById('nav-menu-btn');
  const drawer = document.getElementById('nav-drawer');
  if (!btn || !drawer) return;

  function openDrawer() {
    drawer.classList.add('open');
    btn.setAttribute('aria-expanded', 'true');
    drawer.setAttribute('aria-hidden', 'false');
  }

  function closeDrawer() {
    drawer.classList.remove('open');
    btn.setAttribute('aria-expanded', 'false');
    drawer.setAttribute('aria-hidden', 'true');
  }

  btn.addEventListener('click', function (e) {
    e.stopPropagation();
    drawer.classList.contains('open') ? closeDrawer() : openDrawer();
  });

  // Close when any drawer link is tapped
  drawer.querySelectorAll('.nav-drawer-link').forEach(link => {
    link.addEventListener('click', closeDrawer);
  });

  // Close on outside click
  document.addEventListener('click', function (e) {
    if (!drawer.contains(e.target) && !btn.contains(e.target)) closeDrawer();
  });

  // Close on Escape
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') closeDrawer();
  });
}

// --------------------------------------------------
// Simulation: rotate feed entries when pipeline offline
// --------------------------------------------------
function liveSimulate() {
  let ipIdx = 0;
  setInterval(() => {
    const entry   = { ...THREAT_IPS[ipIdx % THREAT_IPS.length] };
    entry.score   = Math.floor(50 + Math.random() * 50);
    THREAT_IPS.unshift(entry);
    if (THREAT_IPS.length > 12) THREAT_IPS.pop();
    renderIPFeed();
    ipIdx++;
  }, 4000);

  let iocIdx = 0;
  setInterval(() => {
    const entry = { ...IOC_FEED[iocIdx % IOC_FEED.length] };
    IOC_FEED.unshift(entry);
    if (IOC_FEED.length > 12) IOC_FEED.pop();
    renderIOCFeed();
    iocIdx++;
  }, 6000);
}

// --------------------------------------------------
// Utility: animated number counter
// --------------------------------------------------
function animateCounter(el, target, duration = 1500) {
  let current = 0;
  const step  = target / (duration / 16);
  const timer = setInterval(() => {
    current += step;
    if (current >= target) {
      el.textContent = target.toLocaleString();
      clearInterval(timer);
    } else {
      el.textContent = Math.floor(current).toLocaleString();
    }
  }, 16);
}

// --------------------------------------------------
// Utility: footer UTC clock
// --------------------------------------------------
function updateClock() {
  const el = document.getElementById('footer-time');
  if (el) el.textContent = new Date().toUTCString().replace('GMT', 'UTC');
}

// --------------------------------------------------
// Bootstrap
// --------------------------------------------------
document.addEventListener('DOMContentLoaded', async () => {
  const statIocs = document.getElementById('stat-iocs');
  const statTtps = document.getElementById('stat-ttps');
  if (statIocs) statIocs.textContent = '1,204';
  if (statTtps) statTtps.textContent = '23';

  // Apply saved theme before anything renders (prevents flash)
  initTheme();

  // Wire mobile nav drawer
  initMobileNav();

  // Render static sections immediately (no fetch needed)
  renderTools();
  renderPosture();

  // Render feed sections with fallback data so page is never blank
  renderIPFeed();
  renderIOCFeed();
  renderATTCK();
  renderIRCases();

  // Start clock
  updateClock();
  setInterval(updateClock, 1000);

  // Init threat map with hardcoded points
  initThreatMap();

  // Attempt to fetch live pipeline data
  await loadLiveData();

  if (pipelineOnline) {
    renderIPFeed();
    renderIOCFeed();
    if (liveMapPoints) initThreatMap();
  } else {
    liveSimulate();
  }

  // Animate metric counters once numbers are in the DOM
  setTimeout(() => {
    const blocked = document.getElementById('m-blocked');
    const iocs    = document.getElementById('m-iocs');
    if (blocked && !isNaN(parseInt(blocked.textContent)))
      animateCounter(blocked, parseInt(blocked.textContent));
    if (iocs && !isNaN(parseInt(iocs.textContent)))
      animateCounter(iocs, parseInt(iocs.textContent));
  }, 300);
});
