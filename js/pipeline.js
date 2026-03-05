// =============================================
// pipeline.js — THIR Live Data Pipeline
// Fetches real data from data/ JSON files written
// by GitHub Actions every hour. Falls back to
// hardcoded demo data (data.js) if offline.
// Depends on: data.js, render.js
// =============================================

let pipelineOnline  = false;
let liveMapPoints   = null;

// --------------------------------------------------
// Entry point — fetch all three sources in parallel
// --------------------------------------------------
async function loadLiveData() {
  const results = await Promise.allSettled([
    fetch('data/stats.json').then(r => r.ok ? r.json() : Promise.reject(r.status)),
    fetch('data/ir_cases.json').then(r => r.ok ? r.json() : Promise.reject(r.status)),
    fetch('data/threat_ips.json').then(r => r.ok ? r.json() : Promise.reject(r.status)),
  ]);

  const [statsResult, irResult, threatResult] = results;

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
    pipelineOnline = true;
  } else {
    console.warn('[THIR] threat_ips.json unavailable — using demo IPs');
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
    ttps:    c.ttps || ['T1110.001'],
    summary: buildCaseSummary(c),
    live:    true,
  }));

  IR_CASES = [...liveCases, ...IR_CASES];

  const allTTPs = new Set(cases.flatMap(c => c.ttps || []));
  if (allTTPs.size > 0) {
    ATTCK_DATA.detected = [...allTTPs, ...ATTCK_DATA.detected];
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
  if (isp.includes('tor') || isp.includes('exit'))                        return 'TOR Exit · SSH Attack';
  if (isp.includes('shodan'))                                              return 'Mass Scanner (Shodan)';
  if (isp.includes('censys'))                                              return 'Mass Scanner (Censys)';
  if (isp.includes('digitalocean') || isp.includes('linode') || isp.includes('vultr')) return 'VPS · Brute Force';
  if (ip.otx_pulses > 5)                                                  return 'Known Threat Actor';
  if (ip.abuse_score >= 90)                                               return 'High-Confidence Attacker';
  if (ip.abuse_score >= 50)                                               return 'SSH Brute Force';
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
  parts.push(`TTPs: ${(c.ttps || ['T1110.001']).join(', ')}.`);
  return parts.join(' ');
}

// --------------------------------------------------
// Helper: rebuild the ticker from live case data
// --------------------------------------------------
function buildLiveTicker(cases) {
  const items = cases.slice(0, 8).map(c => {
    const ttp    = (c.ttps || ['T1110.001'])[0];
    const action = c.login_success ? 'BREACH' : 'BLOCK';
    return `<span>${action}</span> · SSH from ${c.src_ip} (${c.severity}) · <span>TTP</span> · ${ttp} detected`;
  });
  const ticker = document.getElementById('ticker-content');
  if (ticker && items.length) {
    const text = items.join(' · ') + ' · ' + items.join(' · ') + ' ·&nbsp;';
    ticker.innerHTML = text;
  }
}

// --------------------------------------------------
// Nav status indicator
// --------------------------------------------------
function updateNavStatus() {
  const label = document.getElementById('threat-label');
  const dot   = document.getElementById('tl-dot');
  if (!label) return;

  if (!pipelineOnline) {
    label.textContent  = 'OFFLINE';
    label.style.color  = 'var(--text-dim)';
    if (dot) dot.style.background = 'var(--text-dim)';
    return;
  }

  const hasHigh = IR_CASES.some(c => c.live && (c.severity === 'HIGH' || c.severity === 'CRITICAL'));
  if (hasHigh) {
    label.textContent = 'ELEVATED';
    label.style.color = 'var(--accent2)';
    if (dot) { dot.style.background = 'var(--accent2)'; dot.style.animation = 'pulse-green 1s infinite'; }
  } else {
    label.textContent = 'MONITORING';
    label.style.color = 'var(--accent3)';
    if (dot) dot.style.background = 'var(--accent3)';
  }
}
