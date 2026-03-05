// =============================================
// data.js — THIR Static Data & Mutable Stores
// All static reference data and live-data arrays
// that other modules read from and write to.
// =============================================

// --------------------------------------------------
// MITRE ATT&CK matrix structure
// --------------------------------------------------
const ATTCK_DATA = {
  tactics: [
    { id: 'TA0043', name: 'Recon' },
    { id: 'TA0042', name: 'Resource Dev' },
    { id: 'TA0001', name: 'Initial Access' },
    { id: 'TA0002', name: 'Execution' },
    { id: 'TA0003', name: 'Persistence' },
    { id: 'TA0004', name: 'Priv Escal' },
    { id: 'TA0005', name: 'Def Evasion' },
    { id: 'TA0006', name: 'Cred Access' },
    { id: 'TA0007', name: 'Discovery' },
    { id: 'TA0008', name: 'Lateral Move' },
    { id: 'TA0011', name: 'C2' },
  ],
  techniques: [
    ['T1595','T1585','T1190','T1059','T1078','T1068','T1055','T1003','T1087','T1021','T1071'],
    ['T1596','T1583','T1566','T1203','T1098','T1134','T1027','T1558','T1018','T1570','T1095'],
    ['T1597','T1584','T1133','T1047','T1547','T1548','T1070','T1552','T1069','T1210','T1105'],
    ['T1598','T1587','T1199','T1053','T1037','T1078','T1562','T1110','T1083','T1550','T1572'],
  ],
  detected:  ['T1059','T1078','T1003','T1087','T1021','T1071','T1566','T1110','T1547','T1027','T1055','T1133'],
  monitored: ['T1190','T1068','T1558','T1018','T1570','T1095','T1053','T1134','T1562','T1552'],
};

// --------------------------------------------------
// Country code → [lon, lat] for threat map plotting
// --------------------------------------------------
const COUNTRY_COORDS = {
  AF:[67.7,33.9],AL:[20.2,41.2],DZ:[2.6,28.0],AO:[17.9,-11.2],AR:[-63.6,-38.4],
  AU:[133.8,-25.3],AT:[14.6,47.5],AZ:[47.4,40.1],BD:[90.4,23.7],BE:[4.5,50.5],
  BG:[25.5,42.7],BR:[-51.9,-14.2],BY:[28.0,53.7],CA:[-96.8,56.1],CH:[8.2,46.8],
  CL:[-71.5,-35.7],CN:[104.2,35.9],CO:[-74.3,4.6],CZ:[15.5,49.8],DE:[10.5,51.2],
  DK:[10.0,56.3],EG:[30.8,26.8],ES:[-3.7,40.5],ET:[40.5,9.1],
  FI:[26.0,64.0],FR:[2.2,46.2],GB:[-3.4,55.4],GH:[-1.0,7.9],GR:[21.8,39.1],
  HK:[114.2,22.3],HR:[16.5,45.1],HU:[19.5,47.2],ID:[113.9,-0.8],IN:[78.7,20.6],
  IQ:[43.7,33.2],IR:[53.7,32.4],IT:[12.6,42.8],JP:[138.3,36.2],KE:[37.9,-0.0],
  KR:[127.8,36.6],KZ:[66.9,48.0],LB:[35.9,33.9],LT:[23.9,56.0],LV:[24.6,56.9],
  LY:[17.2,26.3],MA:[-7.1,31.8],MD:[28.4,47.4],MK:[21.7,41.6],MM:[96.7,17.1],
  MX:[-102.6,23.6],MY:[109.7,4.2],NG:[8.7,9.1],NL:[5.3,52.1],NO:[8.5,60.5],
  NZ:[172.0,-41.5],PA:[-80.8,8.5],PE:[-75.0,-9.2],PH:[122.9,12.9],PK:[69.4,30.4],
  PL:[19.1,52.1],PT:[-8.2,39.4],RO:[25.0,46.0],RS:[21.0,44.0],RU:[99.0,61.5],
  SA:[45.1,23.9],SD:[30.2,12.9],SE:[18.6,60.1],SG:[103.8,1.4],SI:[14.9,46.1],
  SK:[19.7,48.7],SY:[38.3,34.8],TH:[100.9,15.9],TN:[9.5,33.9],TR:[35.2,39.0],
  TW:[121.0,23.7],TZ:[34.9,-6.4],UA:[31.2,48.4],UG:[32.3,1.4],US:[-95.7,37.1],
  UZ:[63.9,41.4],VE:[-66.6,6.4],VN:[108.3,14.1],ZA:[25.1,-29.0],ZW:[30.0,-20.0],
};

// --------------------------------------------------
// Hardcoded fallback IP feed (used when pipeline offline)
// --------------------------------------------------
let THREAT_IPS = [
  { ip: '185.220.101.42', type: 'TOR Exit · SSH Brute Force',      score: 97, country: 'DE' },
  { ip: '91.134.209.12',  type: 'RDP Brute Force',                  score: 89, country: 'FR' },
  { ip: '45.33.32.156',   type: 'Network Scanner',                  score: 74, country: 'US' },
  { ip: '203.0.113.88',   type: 'C2 Beacon Attempt',                score: 96, country: 'RU' },
  { ip: '198.199.67.49',  type: 'Credential Stuffing',              score: 81, country: 'NL' },
  { ip: '103.75.188.44',  type: 'Web App Scanner',                  score: 62, country: 'HK' },
  { ip: '62.102.148.68',  type: 'TOR · Malware Host',               score: 99, country: 'SE' },
  { ip: '5.188.206.78',   type: 'SSH Dictionary Attack',            score: 91, country: 'RU' },
  { ip: '167.248.133.122',type: 'Mass Scanner (Shodan)',             score: 55, country: 'US' },
  { ip: '178.128.23.90',  type: 'Exploit Attempt CVE-2021-44228',   score: 94, country: 'SG' },
];

// --------------------------------------------------
// Hardcoded fallback IOC feed (used when pipeline offline)
// --------------------------------------------------
let IOC_FEED = [
  { type: 'DOMAIN', indicator: 'update-checker[.]ru',           threat: 'C2 / RAT Dropper',       confidence: 'HIGH' },
  { type: 'HASH',   indicator: 'e3b0c44298fc...',               threat: 'Ryuk Ransomware Variant', confidence: 'HIGH' },
  { type: 'URL',    indicator: 'hxxp://185.220[.]101/payload',  threat: 'Malware Delivery',        confidence: 'HIGH' },
  { type: 'IP',     indicator: '91.108.56.130',                 threat: 'Cobalt Strike C2',        confidence: 'MED'  },
  { type: 'DOMAIN', indicator: 'cdn-delivery[.]xyz',            threat: 'Phishing Kit Host',       confidence: 'HIGH' },
  { type: 'HASH',   indicator: 'aabbcc1122...',                 threat: 'Mimikatz Variant',        confidence: 'HIGH' },
  { type: 'URL',    indicator: 'hxxps://login.micros0ft[.]com', threat: 'Credential Phishing',     confidence: 'MED'  },
  { type: 'IP',     indicator: '203.0.113.254',                 threat: 'APT Infrastructure',      confidence: 'MED'  },
  { type: 'DOMAIN', indicator: 'sys-update[.]net',              threat: 'Persistence Mechanism',   confidence: 'LOW'  },
  { type: 'HASH',   indicator: 'deadbeef9f...',                 threat: 'Emotet Loader',           confidence: 'HIGH' },
];

// --------------------------------------------------
// Hardcoded fallback IR cases (simulation / demo)
// --------------------------------------------------
let IR_CASES = [
  {
    id: 'SIM-001', title: 'SSH Brute Force + Shell Access — Cowrie Honeypot',
    status: 'contained', severity: 'HIGH', date: '2025-01-15', live: false,
    phases: [
      { name: 'Detection', val: 'Cowrie logged auth success', done: true },
      { name: 'Triage',    val: '12 attempts, 1 success',     done: true },
      { name: 'Contain',   val: 'Honeypot isolated session',  done: true },
      { name: 'RCA',       val: 'Default creds reused',       done: true },
      { name: 'TTPs',      val: 'T1110.001 · T1078',          done: true },
    ],
    ttps: ['T1110.001','T1078','T1059.004'],
    summary: 'Attacker authenticated via SSH credential brute force. Executed whoami, uname -a, attempted wget. Session fully logged by Cowrie. IP submitted to AbuseIPDB.',
  },
  {
    id: 'SIM-002', title: 'Malware Download Attempt via Honeypot',
    status: 'contained', severity: 'HIGH', date: '2025-01-10', live: false,
    phases: [
      { name: 'Detection', val: 'Cowrie logged wget command', done: true },
      { name: 'Triage',    val: 'ELF binary download attempt',done: true },
      { name: 'Contain',   val: 'Honeypot filesystem only',   done: true },
      { name: 'RCA',       val: 'Bot framework deployment',   done: true },
      { name: 'TTPs',      val: 'T1105 · T1059.004',          done: true },
    ],
    ttps: ['T1105','T1059.004','T1222.002'],
    summary: 'Post-auth attacker issued wget to retrieve ELF binary from external host. Cowrie simulated filesystem, download captured. Binary hash submitted to VirusTotal. Confirmed Mirai variant dropper.',
  },
  {
    id: 'SIM-003', title: 'Credential Reconnaissance — Mass Scanner',
    status: 'contained', severity: 'LOW', date: '2025-01-08', live: false,
    phases: [
      { name: 'Detection', val: 'High-volume failed auth',    done: true },
      { name: 'Triage',    val: 'AbuseIPDB score: 0 (Shodan)',done: true },
      { name: 'Contain',   val: 'Auto-filtered as FP',        done: true },
      { name: 'RCA',       val: 'Internet-wide scanner',      done: true },
      { name: 'TTPs',      val: 'T1110.001 only',             done: true },
    ],
    ttps: ['T1110.001'],
    summary: 'Mass credential scan from known Shodan scanner IP. 847 login attempts, zero success. AbuseIPDB score 0. Automatically filtered as false positive by Tool 29.',
  },
];

// --------------------------------------------------
// Tool portfolio static data
// --------------------------------------------------
const TOOLS_DATA = [
  { name: 'Incident Timeline Generator', langs: ['py'], desc: 'Parses Cowrie NDJSON logs into structured IR cases. Groups events by session, maps TTPs to MITRE ATT&CK, scores severity. Output: data/ir_cases.json.', domain: 'Incident Response', lines: 375 },
  { name: 'Threat Intel Feeder',         langs: ['go'], desc: 'Enriches attacker IPs via AbuseIPDB and AlienVault OTX concurrently. Deduplicates across sessions, maps country codes for visualisation. Output: data/threat_ips.json.', domain: 'Threat Intelligence', lines: 411 },
  { name: 'False Positive Tracker',      langs: ['py'], desc: 'Three-signal FP detection: AbuseIPDB score threshold, known scanner ISP matching (Shodan/Censys/Rapid7), mass-scanner behaviour pattern. Output: data/fp_filter.json.', domain: 'Alert Triage', lines: 407 },
  { name: 'Metric Dashboard Exporter',   langs: ['go'], desc: 'Aggregates all pipeline outputs into a single stats object. Derives severity breakdown, top TTPs by frequency, unique country count, honeypot status. Output: data/stats.json.', domain: 'Metrics & Reporting', lines: 459 },
  { name: 'Network Service Monitor',     langs: ['go'], desc: 'Concurrent TCP port checker. Verifies Cowrie honeypot liveness on Oracle VPS port 2222. Writes structured JSON posture report. Runs before each pipeline cycle.', domain: 'Infrastructure', lines: 220 },
  { name: 'File Integrity Monitor',      langs: ['go'], desc: 'SHA-256 baseline verification for all data/ pipeline outputs. Detects unauthorised modification between pipeline runs. Alerts via GitHub Actions annotation.', domain: 'Data Integrity', lines: 198 },
];

// --------------------------------------------------
// Security posture controls (NIST CSF mapping)
// Only controls that THIR genuinely implements are listed.
// Each maps directly to one or more pipeline tools.
// --------------------------------------------------
const POSTURE_CONTROLS = [
  // Tool 05 — network_monitor_live.go: TCP checks Cowrie port 2222 every hour
  { id: 'DE.CM-1',  name: 'Honeypot Liveness Monitoring',   status: 'active',     tool: 'Tool 05' },

  // Tool 26 — incident_timeline_live.py: groups Cowrie sessions into IR cases, maps TTPs
  { id: 'DE.AE-2',  name: 'Attack Session Detection',       status: 'active',     tool: 'Tool 26' },
  { id: 'RS.AN-1',  name: 'Session Investigation & Triage', status: 'active',     tool: 'Tool 26' },

  // Tool 27 — threat_intel_feeder_live.go: enriches IPs via AbuseIPDB + OTX
  { id: 'DE.CM-7',  name: 'Attacker IP Enrichment (OSINT)', status: 'active',     tool: 'Tool 27' },
  { id: 'DE.AE-5',  name: 'Threat Intel Correlation',       status: 'active',     tool: 'Tool 27' },

  // Tool 29 — false_positive_live.py: 3-signal FP filter (score + ISP + behaviour)
  { id: 'DE.AE-3',  name: 'False Positive Suppression',     status: 'active',     tool: 'Tool 29' },

  // Tool 30 — metric_exporter_live.go: aggregates all outputs into stats.json
  { id: 'DE.AE-4',  name: 'Pipeline Metrics Aggregation',   status: 'active',     tool: 'Tool 30' },

  // Tool 07 — file_integrity_live.go: SHA-256 baseline check on all data/ outputs
  { id: 'PR.DS-6',  name: 'Pipeline Output Integrity',      status: 'active',     tool: 'Tool 07' },

  // GitHub Actions: structured Cowrie NDJSON → IR case archive with TTP tags
  { id: 'RS.AN-2',  name: 'TTP Mapping (MITRE ATT&CK)',     status: 'active',     tool: 'Tool 26' },

  // Planned: SOC handover report (Tool 28) not yet built
  { id: 'RS.CO-3',  name: 'Automated Handover Reporting',   status: 'planned',    tool: 'Tool 28' },

  // Planned: malware analyzer for ELF binaries downloaded via Cowrie
  { id: 'DE.CM-4',  name: 'Malware Sample Analysis',        status: 'planned',    tool: 'Planned' },
];

// --------------------------------------------------
// Hardcoded geo points for threat map fallback
// --------------------------------------------------
const THREAT_LOCS = [
  { name: 'Frankfurt', coords: [8.68,   50.11], type: 'brute',    label: '185.220.101.42' },
  { name: 'Paris',     coords: [2.35,   48.85], type: 'brute',    label: 'RDP Attack' },
  { name: 'Moscow',    coords: [37.62,  55.75], type: 'c2',       label: 'C2 Beacon' },
  { name: 'Amsterdam', coords: [4.90,   52.37], type: 'scan',     label: 'Credential Stuff' },
  { name: 'Stockholm', coords: [18.06,  59.33], type: 'c2',       label: 'TOR / Malware' },
  { name: 'Singapore', coords: [103.82,  1.35], type: 'exploit',  label: 'Log4j Attempt' },
  { name: 'Hong Kong', coords: [114.17, 22.32], type: 'scan',     label: 'Web Scanner' },
  { name: 'Honeypot',  coords: [72.87,  19.07], type: 'defender', label: 'HONEYPOT' },
  { name: 'New York',  coords: [-74.00, 40.71], type: 'scan',     label: 'Mass Scanner' },
];
