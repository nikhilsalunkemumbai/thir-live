// =============================================
// render.js — THIR DOM Render Functions
// All functions that write data into the page.
// Depends on: data.js
// =============================================

// --------------------------------------------------
// Utility: set element text by id
// --------------------------------------------------
function setEl(id, val) {
  const el = document.getElementById(id);
  if (el) el.textContent = val;
}

// --------------------------------------------------
// Utility: map abuse score to CSS class
// --------------------------------------------------
function scoreClass(s) {
  if (s >= 85) return 'score-high';
  if (s >= 60) return 'score-med';
  return 'score-low';
}

// --------------------------------------------------
// Render: IP threat feed
// --------------------------------------------------
function renderIPFeed() {
  const ul = document.getElementById('ip-feed');
  ul.innerHTML = '';
  THREAT_IPS.forEach(item => {
    const li = document.createElement('li');
    li.className = 'feed-item';
    li.innerHTML = `
      <span class="feed-ip">${item.ip}</span>
      <span class="feed-type">${item.type} <span style="color:var(--text-dim);font-size:10px">[${item.country}]</span></span>
      <span class="feed-score ${scoreClass(item.score)}">${item.score}</span>
    `;
    ul.appendChild(li);
  });
}

// --------------------------------------------------
// Render: IOC feed
// --------------------------------------------------
function renderIOCFeed() {
  const ul = document.getElementById('ioc-feed');
  ul.innerHTML = '';
  IOC_FEED.forEach(item => {
    const li        = document.createElement('li');
    li.className    = 'feed-item';
    const confClass = item.confidence === 'HIGH' ? 'score-high' : item.confidence === 'MED' ? 'score-med' : 'score-low';
    const truncated = item.indicator.substring(0, 28) + (item.indicator.length > 28 ? '…' : '');
    li.innerHTML = `
      <span class="feed-ip" style="font-size:9px;color:var(--text-dim)">[${item.type}]</span>
      <span class="feed-type" style="font-size:11px">${truncated}<br><span style="color:var(--text-dim);font-size:10px">${item.threat}</span></span>
      <span class="feed-score ${confClass}">${item.confidence}</span>
    `;
    ul.appendChild(li);
  });
}

// --------------------------------------------------
// Render: MITRE ATT&CK heatmap
// --------------------------------------------------
function renderATTCK() {
  const grid = document.getElementById('attck-grid');
  grid.innerHTML = '';

  ATTCK_DATA.tactics.forEach(t => {
    const div = document.createElement('div');
    div.className = 'attck-tactic';
    div.innerHTML = `<div>${t.name}</div><div style="color:var(--text-dim);font-size:8px;margin-top:2px">${t.id}</div>`;
    grid.appendChild(div);
  });

  ATTCK_DATA.techniques.forEach(row => {
    row.forEach(tid => {
      const div        = document.createElement('div');
      const isDetected = ATTCK_DATA.detected.includes(tid);
      const isMonitored= ATTCK_DATA.monitored.includes(tid);
      div.className    = `attck-technique ${isDetected ? 'detected' : isMonitored ? 'monitored' : ''}`;
      div.textContent  = tid;
      div.title        = tid;
      grid.appendChild(div);
    });
  });
}

// --------------------------------------------------
// Render: IR case timeline
// --------------------------------------------------
function renderIRCases() {
  const container = document.getElementById('ir-cases');
  container.innerHTML = '';
  IR_CASES.forEach(c => {
    const statusClass = c.status === 'contained' ? 'tag-contained' : c.status === 'monitoring' ? 'tag-monitoring' : 'tag-active';
    const phasesHtml  = c.phases.map(p => `
      <div class="ir-phase ${p.done ? 'done' : ''} ${p.active ? 'active' : ''}">
        <div class="ir-phase-label">${p.name}</div>
        <div class="ir-phase-val">${p.val}</div>
      </div>
    `).join('');
    const ttpHtml = c.ttps.map(t => `<span class="ttp-tag">${t}</span>`).join('');
    const div = document.createElement('div');
    div.className = 'ir-case';
    div.innerHTML = `
      <div class="ir-case-head">
        <div>
          <div class="ir-title">${c.title}</div>
          <div style="font-family:var(--mono);font-size:10px;color:var(--text-dim);margin-top:4px">${c.id} · ${c.date} · SEV: ${c.severity}</div>
        </div>
        <div class="ir-meta">
          <span class="ir-tag ${statusClass}">${c.status.toUpperCase()}</span>
        </div>
      </div>
      <div style="font-size:13px;color:var(--text-dim);margin-bottom:1rem;line-height:1.5">${c.summary}</div>
      <div class="ir-phases">${phasesHtml}</div>
      <div class="ir-ttp">TTPs: ${ttpHtml}</div>
    `;
    container.appendChild(div);
  });
}

// --------------------------------------------------
// Render: tool portfolio grid
// --------------------------------------------------
function renderTools() {
  const grid = document.getElementById('tools-grid');
  grid.innerHTML = '';
  TOOLS_DATA.forEach(t => {
    const langHtml = t.langs.map(l => `<span class="lang-badge lang-${l}">${l.toUpperCase()}</span>`).join('');
    const div = document.createElement('div');
    div.className = 'tool-card';
    div.innerHTML = `
      <div class="tool-lang">${langHtml}</div>
      <div class="tool-name">${t.name}</div>
      <div class="tool-desc">${t.desc}</div>
      <div class="tool-meta">
        <span>${t.domain}</span>
        <span>~${t.lines} lines</span>
      </div>
    `;
    grid.appendChild(div);
  });
}

// --------------------------------------------------
// Render: security posture dashboard
// --------------------------------------------------
function renderPosture() {
  const grid = document.getElementById('posture-grid');
  grid.innerHTML = '';
  POSTURE_CONTROLS.forEach(c => {
    const statusLabel = c.status === 'active' ? 'Active' : c.status === 'monitoring' ? 'Monitoring' : 'Planned';
    const div = document.createElement('div');
    div.className = 'control-card';
    div.innerHTML = `
      <div class="control-id">${c.id}</div>
      <div class="control-name">${c.name}</div>
      <div class="control-status status-${c.status}">
        <div class="status-dot"></div>
        <span class="status-text">${statusLabel}</span>
      </div>
      <div style="font-family:var(--mono);font-size:9px;color:var(--text-dim);margin-top:6px;letter-spacing:0.05em">${c.tool}</div>
    `;
    grid.appendChild(div);
  });
}
