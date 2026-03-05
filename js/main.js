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
document.getElementById('stat-iocs').textContent = '1,204';
document.getElementById('stat-ttps').textContent = '23';

document.addEventListener('DOMContentLoaded', async () => {
  // Apply saved theme before anything renders (prevents flash)
  initTheme();

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
