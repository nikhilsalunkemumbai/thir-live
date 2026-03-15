// =============================================
// main.js — THIR Entry Point & Utilities
// Wires up DOMContentLoaded, live simulation
// fallback, animated counters, and the footer clock.
// Depends on: data.js, pipeline.js, render.js, map.js
//
// PATCHES:
//   FIX-1: Removed hardcoded stat-iocs / stat-ttps overrides —
//          bindStats() in pipeline.js sets these correctly from
//          live data; the hardcoded values were silently masking
//          real honeypot numbers on every page load.
//   FIX-7: animateCounter target now strips commas before parseInt
//          so "2,847" → 2847 rather than 2 (parseInt stops at comma).
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

  drawer.querySelectorAll('.nav-drawer-link').forEach(link => {
    link.addEventListener('click', closeDrawer);
  });

  document.addEventListener('click', function (e) {
    if (!drawer.contains(e.target) && !btn.contains(e.target)) closeDrawer();
  });

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
// FIX-7: strip commas before parseInt so "2,847" → 2847
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
  // FIX-1: Removed hardcoded stat-iocs / stat-ttps lines that were here.
  //        bindStats() in pipeline.js sets these from live data correctly.
  //        Hardcoding them here was overwriting real honeypot numbers.

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

  // Init threat map — deferred so flex layout has fully painted
  // and getBoundingClientRect() returns accurate panel dimensions
  requestAnimationFrame(() => initThreatMap());

  // Attempt to fetch live pipeline data
  await loadLiveData();

  if (pipelineOnline) {
    // renderIPFeed / renderIOCFeed already called inside bindThreatIPs
    // only re-init map if live points were loaded
    if (liveMapPoints) initThreatMap();
  }

  // FIX-2 (partial): if threat IPs failed to load, simulate the feed
  if (!threatIPsLoaded) {
    liveSimulate();
  }

  // Animate metric counters once live numbers are in the DOM
  // FIX-7: strip commas before parseInt
  setTimeout(() => {
    const blocked = document.getElementById('m-blocked');
    const iocs    = document.getElementById('m-iocs');
    if (blocked) {
      const val = parseInt((blocked.textContent || '').replace(/,/g, ''));
      if (!isNaN(val)) animateCounter(blocked, val);
    }
    if (iocs) {
      const val = parseInt((iocs.textContent || '').replace(/,/g, ''));
      if (!isNaN(val)) animateCounter(iocs, val);
    }
  }, 300);
});
