// =============================================
// main.js — THIR Entry Point & Utilities
// Wires up DOMContentLoaded, live simulation
// fallback, animated counters, and the footer clock.
// Depends on: data.js, pipeline.js, render.js, map.js
// =============================================

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
  let current  = 0;
  const step   = target / (duration / 16);
  const timer  = setInterval(() => {
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
    // Re-render feeds with live data
    renderIPFeed();
    renderIOCFeed();
    // Re-init map with live geo points if available
    if (liveMapPoints) initThreatMap();
  } else {
    // Fall back to rotating simulation
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
