// =============================================
// pipeline.js — THIR Live Data Pipeline
// Fetches real data from data/ JSON files written
// by GitHub Actions every hour. Falls back to
// hardcoded demo data (data.js) if offline.
// Depends on: data.js, render.js
//
// PATCHES:
//   FIX-2: Added threatIPsLoaded flag — tracks whether threat_ips.json
//          loaded successfully, independently of pipelineOnline.
//          main.js uses this to decide whether liveSimulate() runs,
//          preventing the IP feed going silently static when only
//          stats.json or ir_cases.json loads but threat_ips.json fails.
//   FIX-3: ATTCK_DATA.detected merge now wrapped in new Set() to
//          deduplicate. Without this, re-renders (e.g. future auto-
//          refresh) double the array on every call.
//   FIX-5: IR_CASES now replaced (not prepended) with live cases when
//          available. Demo cases (SIM-001/002/003) were always appended
//          below real honeypot events — they are fallback data only.
//   FIX-6: buildLiveTicker() — c.ttps || fallback only fires when ttps
//          is falsy. Tool 26 writes ttps:[] on LOW sessions (empty array
//          is truthy), so [][0] returned undefined, producing
//          "TTP · undefined detected" in the ticker. Fixed by checking
//          array length before falling back to ['T1110.001'].
//          Also added minimum repeat logic so the ticker scrolls
//          smoothly even when only 1-2 live cases are present.
// =============================================

let pipelineOnline  = false;
let threatIPsLoaded = false;   // FIX-2: per-source load flag
let liveMapPoints   = null;

// --------------------------------------------------
// Entry point — fetch all three sources in parallel
// --------------------------------------------------
async function loadLiveData() {
  const results = await Promise.allSettled([
    fetch('data/stats.json').then(r => r.ok ? r.json() : Promise.reject(r.status)),
    fetch('data/ir_cases.json').then(r => r.ok ? r.json() : Promise.reject(r.status)),
    fetch('data/threat_ips.json').then(r => r.ok ? r.json() : Promise.reject(r.status)),
    fetch('data/assets.json').then(r => r.ok ? r.json() : Promise.reject(r.status)),
  ]);

  const [statsResult, irResult, threatResult, assetsResult] = results;

  if (statsResult.status === 'fulfilled') {
    bindStats(statsResult.value);
    pipelineOnline = true;
  } else {
    console.warn('[THIR] stats.json unavailable — using hardcoded metrics');
  }

  if (irResult.status === 'fulfilled') {
    bindIRCases(irResult.value);
    pipelineOnline = true;
  } else {
    console.warn('[THIR] ir_cases.json unavailable — using demo cases');
  }

  if (threatResult.status === 'fulfilled') {
    bindThreatIPs(threatResult.value);
    pipelineOnline  = true;
    threatIPsLoaded = true;   // FIX-2: mark threat feed as loaded
  } else {
    console.warn('[THIR] threat_ips.json unavailable — using demo IPs');
  if (assetsResult.status === 'fulfilled') {
    bindAssets(assetsResult.value);
  } else {
    console.warn('[THIR] assets.json unavailable — ID.AM-1 showing static label');
  }
    // threatIPsLoaded stays false → main.js will start liveSimulate()
  }

  updateNavStatus();
}

// --------------------------------------------------
// BIND: stats.json → metrics bar + hero stats
// --------------------------------------------------
function bindStats(stats) {
  setEl('m-blocked',  stats.total_attacks    ?? '--');
  setEl('m-iocs',     stats.unique_ips        ?? '--');
  setEl('m-ttps',     stats.total_ttps        ?? '--');
  setEl('m-cases',    stats.confirmed_threats ?? '--');

  const status   = (stats.honeypot_status || 'UNKNOWN').toUpperCase();
  const uptimeEl = document.getElementById('m-uptime');
  if (uptimeEl) {
    if (status === 'HEALTHY' || status === 'UP') {
      uptimeEl.textContent = 'ONLINE';
      uptimeEl.className   = 'metric-val green';
    } else if (status === 'DOWN' || status === 'DEGRADED') {
      uptimeEl.textContent = 'OFFLINE';
      uptimeEl.className   = 'metric-val red';
    } else {
      uptimeEl.textContent = status;
      uptimeEl.className   = 'metric-val yellow';
    }
  }

  setEl('stat-iocs',      stats.unique_ips        ?? '--');
  setEl('stat-ttps',      stats.total_ttps        ?? '--');
  setEl('stat-attacks',   stats.total_attacks     ?? '--');
  setEl('stat-ips',       stats.unique_ips        ?? '--');
  setEl('stat-countries', stats.unique_countries  ?? '--');

  if (stats.generated_at) {
    const d   = new Date(stats.generated_at);
    const fmt = d.toUTCString().replace('GMT', 'UTC');
    setEl('last-updated', 'Pipeline: ' + fmt);
  }

  if (stats.integrity_status === 'MODIFIED') {
    const badge = document.querySelector('#posture .section-header');
    if (badge) {
      const warn = document.createElement('span');
      warn.style.cssText = 'font-family:var(--mono);font-size:10px;color:var(--accent2);letter-spacing:0.1em;margin-left:1rem';
      warn.textContent   = '⚠ INTEGRITY ALERT';
      badge.appendChild(warn);
    }
  }
}

// --------------------------------------------------
// BIND: ir_cases.json → IR timeline + ATT&CK + ticker
// --------------------------------------------------
function bindIRCases(data) {
  const cases = data.cases || [];
  if (!cases.length) return;

  const liveCases = cases.slice(0, 10).map(c => ({
    id:       c.case_id,
    title:    buildCaseTitle(c),
    status:   c.login_success ? 'active' : 'contained',
    severity: c.severity || 'LOW',
    date:     (c.first_seen || '').slice(0, 10),
    phases: [
      { name: 'Detection', val: 'Cowrie honeypot SSH',                                       done: true },
      { name: 'Triage',    val: severityTriage(c),                                           done: true },
      { name: 'Contain',   val: c.login_success ? 'Isolated' : 'Blocked at auth',            done: true },
      { name: 'RCA',       val: c.commands.length ? 'Commands logged' : 'Brute force only',  done: true },
      { name: 'TTPs',      val: (c.ttps || []).slice(0, 2).join(', ') || 'T1110.001',        done: true },
    ],
    ttps:    c.ttps && c.ttps.length ? c.ttps : ['T1110.001'],
    summary: buildCaseSummary(c),
    live:    true,
  }));

  // FIX-5: Replace IR_CASES with live data when available.
  //        Demo cases (SIM-001/002/003) are fallback only — they should
  //        not appear alongside real honeypot events on a live pipeline.
  IR_CASES = liveCases;

  // FIX-3: Deduplicate ATT&CK detected array with new Set() to prevent
  //        array growth if bindIRCases() is ever called more than once.
  const allTTPs = new Set(cases.flatMap(c => c.ttps || []));
  if (allTTPs.size > 0) {
    ATTCK_DATA.detected = [...new Set([...allTTPs, ...ATTCK_DATA.detected])];
  }

  buildLiveTicker(cases);
  renderIRCases();
  renderATTCK();
}

// --------------------------------------------------
// BIND: threat_ips.json → IP feed + threat map
// --------------------------------------------------
function bindThreatIPs(data) {
  const ips = data.ips || [];
  if (!ips.length) return;

  THREAT_IPS = ips.map(ip => ({
    ip:      ip.indicator,
    type:    classifyIP(ip),
    score:   ip.abuse_score || 0,
    country: ip.country || '??',
  }));

  IOC_FEED = ips
    .filter(ip => ip.abuse_score >= 50)
    .slice(0, 10)
    .map(ip => ({
      type:       'IP',
      indicator:  ip.indicator,
      threat:     classifyIP(ip),
      confidence: ip.abuse_score >= 80 ? 'HIGH' : 'MED',
    }));

  if (!IOC_FEED.length) {
    IOC_FEED = ips.slice(0, 5).map(ip => ({
      type:       'IP',
      indicator:  ip.indicator,
      threat:     classifyIP(ip),
      confidence: 'LOW',
    }));
  }

  updateThreatMapPoints(ips);
  renderIPFeed();
  renderIOCFeed();
}

// --------------------------------------------------
// Helper: classify an IP record into a human label
// --------------------------------------------------
function classifyIP(ip) {
  const isp = (ip.isp || '').toLowerCase();
  if (isp.includes('tor') || isp.includes('exit'))                                            return 'TOR Exit · SSH Attack';
  if (isp.includes('shodan'))                                                                  return 'Mass Scanner (Shodan)';
  if (isp.includes('censys'))                                                                  return 'Mass Scanner (Censys)';
  if (isp.includes('digitalocean') || isp.includes('linode') || isp.includes('vultr'))        return 'VPS · Brute Force';
  if (ip.otx_pulses > 5)                                                                       return 'Known Threat Actor';
  if (ip.abuse_score >= 90)                                                                    return 'High-Confidence Attacker';
  if (ip.abuse_score >= 50)                                                                    return 'SSH Brute Force';
  return 'Credential Scanning';
}

// --------------------------------------------------
// Helper: build liveMapPoints from real country codes
// --------------------------------------------------
function updateThreatMapPoints(ips) {
  const mumbai = [72.87, 19.07];
  liveMapPoints = ips
    .filter(ip => ip.country && COUNTRY_COORDS[ip.country])
    .slice(0, 15)
    .map(ip => ({
      name:   ip.country,
      coords: COUNTRY_COORDS[ip.country],
      type:   ip.abuse_score >= 80 ? 'brute' : ip.abuse_score >= 50 ? 'c2' : 'scan',
      label:  ip.indicator,
    }));
  liveMapPoints.push({ name: 'Honeypot', coords: mumbai, type: 'defender', label: 'HONEYPOT' });
}

// --------------------------------------------------
// Helpers: IR case builder utilities
// --------------------------------------------------
function buildCaseTitle(c) {
  if ((c.downloads || []).length > 0)                         return `Malware Download — ${c.src_ip}`;
  if (c.login_success && (c.commands || []).length > 0)       return `Shell Access — ${c.src_ip}`;
  if (c.login_success)                                        return `Successful Login — ${c.src_ip}`;
  return `SSH Brute Force — ${c.src_ip}`;
}

function severityTriage(c) {
  if (c.severity === 'HIGH')   return 'Successful auth + commands';
  if (c.severity === 'MEDIUM') return 'Interactive session';
  return 'Credential scanning';
}

function buildCaseSummary(c) {
  const parts = [];
  parts.push(`Attacker ${c.src_ip} made ${c.login_attempts} login attempt(s).`);
  if (c.login_success)              parts.push(`Authentication succeeded.`);
  if ((c.commands  || []).length)   parts.push(`Executed ${c.commands.length} command(s): ${c.commands.slice(0, 3).join(', ')}.`);
  if ((c.downloads || []).length)   parts.push(`Attempted ${c.downloads.length} file download(s).`);
  parts.push(`TTPs: ${(c.ttps && c.ttps.length ? c.ttps : ['T1110.001']).join(', ')}.`);
  return parts.join(' ');
}

// --------------------------------------------------
// Helper: rebuild the ticker from live case data
//
// FIX-6: c.ttps || ['T1110.001'] only fires when ttps is falsy.
//        Tool 26 writes ttps:[] on LOW sessions — empty array is truthy,
//        so [][0] returned undefined → "TTP · undefined detected".
//        Fixed: check array length before falling back.
//
//        Also repeats items to fill the CSS scroll animation smoothly
//        when only 1-2 live cases are available.
// --------------------------------------------------
function buildLiveTicker(cases) {
  const items = cases.slice(0, 8).map(c => {
    // FIX-6: length check — empty array is truthy so || never fired
    const ttp    = (c.ttps && c.ttps.length ? c.ttps : ['T1110.001'])[0];
    const action = c.login_success ? 'BREACH' : 'BLOCK';
    return `<span>${action}</span> · SSH from ${c.src_ip} (${c.severity}) · <span>TTP</span> · ${ttp} detected`;
  });

  const ticker = document.getElementById('ticker-content');
  if (!ticker || !items.length) return;

  // Repeat enough times to keep the ticker full regardless of case count.
  // CSS animation scrolls -50% so we need content duplicated at minimum.
  // With few items, pad to at least 8 entries before duplicating.
  const minItems  = 8;
  const repeated  = Array(Math.ceil(minItems / items.length)).fill(items).flat().slice(0, 16);
  const text      = repeated.join(' · ') + ' · ' + repeated.join(' · ') + ' ·&nbsp;';
  ticker.innerHTML = text;
}

// --------------------------------------------------
// Helper: update nav threat label based on pipeline state
// --------------------------------------------------
function updateNavStatus() {
  const label = document.getElementById('threat-label');
  const dot   = document.getElementById('tl-dot');
  if (!label) return;

  if (!pipelineOnline) {
    label.textContent = 'OFFLINE';
    label.style.color = 'var(--warn)';
    if (dot) {
      dot.style.background = 'var(--warn)';
      dot.style.animation  = 'none';
    }
    return;
  }

  // Count live cases by severity
  const liveCases    = IR_CASES.filter(c => c.live);
  const hasCritical  = liveCases.some(c => c.severity === 'CRITICAL');
  const hasHigh      = liveCases.some(c => c.severity === 'HIGH');
  const hasMedium    = liveCases.some(c => c.severity === 'MEDIUM');
  const highScoreIPs = THREAT_IPS.filter(ip => (ip.score ?? 0) >= 90).length;

  if (hasCritical || (hasHigh && highScoreIPs >= 3)) {
    // Active high-confidence threat in pipeline
    label.textContent = 'ELEVATED';
    label.style.color = 'var(--accent2)';
    if (dot) {
      dot.style.background = 'var(--accent2)';
      dot.style.animation  = 'pulse-green 1s infinite';
    }
  } else if (hasHigh || hasMedium || highScoreIPs >= 1) {
    // Live data, threats present but contained
    label.textContent = 'MONITORING';
    label.style.color = 'var(--warn)';
    if (dot) {
      dot.style.background = 'var(--warn)';
      dot.style.animation  = 'pulse-green 2s infinite';
    }
  } else if (liveCases.length > 0) {
    // Pipeline live, only low severity / brute force noise
    label.textContent = 'LIVE';
    label.style.color = 'var(--accent3)';
    if (dot) {
      dot.style.background = 'var(--accent3)';
      dot.style.animation  = 'pulse-green 2s infinite';
    }
  } else {
    // Pipeline fetched OK but no sessions yet (honeypot just restarted)
    label.textContent = 'STANDBY';
    label.style.color = 'var(--text-dim)';
    if (dot) {
      dot.style.background = 'var(--text-dim)';
      dot.style.animation  = 'none';
    }
  }
}
// --------------------------------------------------
// Helper: update Asset Inventory
// --------------------------------------------------
function bindAssets(data) {
  const total  = data.total_assets  ?? 0;
  const online = data.assets_online ?? 0;
  // Update ID.AM-1 control name to show live count
  const cards = document.querySelectorAll('.control-card');
  cards.forEach(card => {
    const idEl = card.querySelector('.control-id');
    if (idEl && idEl.textContent.trim() === 'ID.AM-1') {
      const nameEl = card.querySelector('.control-name');
      if (nameEl) nameEl.textContent = `Asset Inventory (${online}/${total} online)`;
    }
  });
}
