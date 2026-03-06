# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-06 |
| **Generated At** | 2026-03-06T22:35:49Z |
| **Shift Time** | 22:35 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **47** |
| Confirmed Threats | **17** |
| False Positives Filtered | **30** (63.8%) |
| Unique Attacker IPs | **35** |
| Countries of Origin | **7** |
| High Severity Cases | **3** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **44** |

---

## 🚨 Confirmed Threats (17)

### 🟢 LOW · IR-e0434e05033d

| Field | Detail |
|---|---|
| **Source IP** | `120.157.18.252` |
| **First Seen** | 2026-03-06T01:07:38.558770Z |
| **Last Seen** | 2026-03-06T01:07:38.559804Z |
| **Session Duration** | 0s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-06 01:07:38` | `cowrie.session.connect` |
| `2026-03-06 01:07:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `120.157.18.252`
- [ ] No immediate escalation required

### 🟢 LOW · IR-7a6c27757e89

| Field | Detail |
|---|---|
| **Source IP** | `192.109.200.213` |
| **First Seen** | 2026-03-06T03:57:13.565431Z |
| **Last Seen** | 2026-03-06T03:57:13.703522Z |
| **Session Duration** | 0s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-06 03:57:13` | `cowrie.session.connect` |
| `2026-03-06 03:57:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `192.109.200.213`
- [ ] No immediate escalation required

### 🟢 LOW · IR-ee0d6e0cf144

| Field | Detail |
|---|---|
| **Source IP** | `192.109.200.213` |
| **First Seen** | 2026-03-06T03:57:13.837636Z |
| **Last Seen** | 2026-03-06T03:57:15.388797Z |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ❌ No |
| **TTPs (MITRE)** | T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-06 03:57:13` | `cowrie.session.connect` |
| `2026-03-06 03:57:13` | `cowrie.client.version` |
| `2026-03-06 03:57:13` | `cowrie.client.kex` |
| `2026-03-06 03:57:14` | `cowrie.login.failed` |
| `2026-03-06 03:57:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `192.109.200.213`
- [ ] No immediate escalation required

### 🔴 HIGH · IR-2094c68caa5b

| Field | Detail |
|---|---|
| **Source IP** | `192.109.200.213` |
| **First Seen** | 2026-03-06T03:57:16.034465Z |
| **Last Seen** | 2026-03-06T03:57:16.857478Z |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt detected |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-06 03:57:16` | `cowrie.session.connect` |
| `2026-03-06 03:57:16` | `cowrie.client.version` |
| `2026-03-06 03:57:16` | `cowrie.client.kex` |
| `2026-03-06 03:57:16` | `cowrie.login.success` |
| `2026-03-06 03:57:16` | `cowrie.direct-tcpip.request` |
| `2026-03-06 03:57:16` | `cowrie.direct-tcpip.data` |
| `2026-03-06 03:57:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.109.200.213` to AbuseIPDB if not already reported
- [ ] Block `192.109.200.213` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — attacker attempted port forwarding via honeypot
- [ ] Check if target host/port in tunnel data is internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc5231cd802a

| Field | Detail |
|---|---|
| **Source IP** | `192.109.200.213` |
| **First Seen** | 2026-03-06T03:57:17.864570Z |
| **Last Seen** | 2026-03-06T03:57:18.707550Z |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt detected |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-06 03:57:17` | `cowrie.session.connect` |
| `2026-03-06 03:57:17` | `cowrie.client.version` |
| `2026-03-06 03:57:18` | `cowrie.client.kex` |
| `2026-03-06 03:57:18` | `cowrie.login.success` |
| `2026-03-06 03:57:18` | `cowrie.direct-tcpip.request` |
| `2026-03-06 03:57:18` | `cowrie.direct-tcpip.data` |
| `2026-03-06 03:57:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.109.200.213` to AbuseIPDB if not already reported
- [ ] Block `192.109.200.213` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — attacker attempted port forwarding via honeypot
- [ ] Check if target host/port in tunnel data is internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🟢 LOW · IR-9d01ff7cdbe1

| Field | Detail |
|---|---|
| **Source IP** | `192.109.200.213` |
| **First Seen** | 2026-03-06T03:57:19.497116Z |
| **Last Seen** | 2026-03-06T03:57:21.045745Z |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ❌ No |
| **TTPs (MITRE)** | T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-06 03:57:19` | `cowrie.session.connect` |
| `2026-03-06 03:57:19` | `cowrie.client.version` |
| `2026-03-06 03:57:19` | `cowrie.client.kex` |
| `2026-03-06 03:57:19` | `cowrie.login.failed` |
| `2026-03-06 03:57:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `192.109.200.213`
- [ ] No immediate escalation required

### 🔴 HIGH · IR-3a7b2196c267

| Field | Detail |
|---|---|
| **Source IP** | `192.109.200.213` |
| **First Seen** | 2026-03-06T03:57:21.362863Z |
| **Last Seen** | 2026-03-06T03:57:22.351302Z |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt detected |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-06 03:57:21` | `cowrie.session.connect` |
| `2026-03-06 03:57:21` | `cowrie.client.version` |
| `2026-03-06 03:57:21` | `cowrie.client.kex` |
| `2026-03-06 03:57:21` | `cowrie.login.success` |
| `2026-03-06 03:57:22` | `cowrie.direct-tcpip.request` |
| `2026-03-06 03:57:22` | `cowrie.direct-tcpip.data` |
| `2026-03-06 03:57:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.109.200.213` to AbuseIPDB if not already reported
- [ ] Block `192.109.200.213` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — attacker attempted port forwarding via honeypot
- [ ] Check if target host/port in tunnel data is internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🟢 LOW · IR-47e0502e29e7

| Field | Detail |
|---|---|
| **Source IP** | `192.109.200.213` |
| **First Seen** | 2026-03-06T03:57:23.011019Z |
| **Last Seen** | 2026-03-06T03:57:24.552782Z |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ❌ No |
| **TTPs (MITRE)** | T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-06 03:57:23` | `cowrie.session.connect` |
| `2026-03-06 03:57:23` | `cowrie.client.version` |
| `2026-03-06 03:57:23` | `cowrie.client.kex` |
| `2026-03-06 03:57:23` | `cowrie.login.failed` |
| `2026-03-06 03:57:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `192.109.200.213`
- [ ] No immediate escalation required

### 🟢 LOW · IR-442e4e2ab7f1

| Field | Detail |
|---|---|
| **Source IP** | `192.109.200.213` |
| **First Seen** | 2026-03-06T03:57:25.597814Z |
| **Last Seen** | 2026-03-06T03:57:27.146625Z |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ❌ No |
| **TTPs (MITRE)** | T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-06 03:57:25` | `cowrie.session.connect` |
| `2026-03-06 03:57:25` | `cowrie.client.version` |
| `2026-03-06 03:57:25` | `cowrie.client.kex` |
| `2026-03-06 03:57:26` | `cowrie.login.failed` |
| `2026-03-06 03:57:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `192.109.200.213`
- [ ] No immediate escalation required

### 🟢 LOW · IR-579d150d9b3a

| Field | Detail |
|---|---|
| **Source IP** | `192.109.200.213` |
| **First Seen** | 2026-03-06T03:57:27.731009Z |
| **Last Seen** | 2026-03-06T03:57:29.472055Z |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ❌ No |
| **TTPs (MITRE)** | T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-06 03:57:27` | `cowrie.session.connect` |
| `2026-03-06 03:57:27` | `cowrie.client.version` |
| `2026-03-06 03:57:27` | `cowrie.client.kex` |
| `2026-03-06 03:57:28` | `cowrie.login.failed` |
| `2026-03-06 03:57:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `192.109.200.213`
- [ ] No immediate escalation required

### 🟢 LOW · IR-4adfa24ea5a5

| Field | Detail |
|---|---|
| **Source IP** | `20.124.87.15` |
| **First Seen** | 2026-03-06T04:16:52.356634Z |
| **Last Seen** | 2026-03-06T04:17:02.559035Z |
| **Session Duration** | 10s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-06 04:16:52` | `cowrie.session.connect` |
| `2026-03-06 04:17:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `20.124.87.15`
- [ ] No immediate escalation required

### 🟢 LOW · IR-25f980d9fff9

| Field | Detail |
|---|---|
| **Source IP** | `20.124.87.15` |
| **First Seen** | 2026-03-06T04:17:02.768459Z |
| **Last Seen** | 2026-03-06T04:17:02.769781Z |
| **Session Duration** | 0s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |
| **TTPs (MITRE)** | T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-06 04:17:02` | `cowrie.session.connect` |
| `2026-03-06 04:17:02` | `cowrie.client.version` |
| `2026-03-06 04:17:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `20.124.87.15`
- [ ] No immediate escalation required

### 🟢 LOW · IR-1496a7723839

| Field | Detail |
|---|---|
| **Source IP** | `172.212.201.77` |
| **First Seen** | 2026-03-06T11:43:32.442711Z |
| **Last Seen** | 2026-03-06T11:43:42.442882Z |
| **Session Duration** | 10s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |
| **TTPs (MITRE)** | T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-06 11:43:32` | `cowrie.session.connect` |
| `2026-03-06 11:43:32` | `cowrie.client.version` |
| `2026-03-06 11:43:32` | `cowrie.client.kex` |
| `2026-03-06 11:43:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `172.212.201.77`
- [ ] No immediate escalation required

### 🟢 LOW · IR-9c5df0a4965c

| Field | Detail |
|---|---|
| **Source IP** | `172.212.201.77` |
| **First Seen** | 2026-03-06T11:43:33.166407Z |
| **Last Seen** | 2026-03-06T11:43:33.167809Z |
| **Session Duration** | 0s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |
| **TTPs (MITRE)** | T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-06 11:43:33` | `cowrie.session.connect` |
| `2026-03-06 11:43:33` | `cowrie.client.version` |
| `2026-03-06 11:43:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `172.212.201.77`
- [ ] No immediate escalation required

### 🟢 LOW · IR-f0022df7bcfd

| Field | Detail |
|---|---|
| **Source IP** | `3.141.168.125` |
| **First Seen** | 2026-03-06T14:02:56.256818Z |
| **Last Seen** | 2026-03-06T14:02:56.481952Z |
| **Session Duration** | 0s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-06 14:02:56` | `cowrie.session.connect` |
| `2026-03-06 14:02:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `3.141.168.125`
- [ ] No immediate escalation required

### 🟢 LOW · IR-b49028c64e3b

| Field | Detail |
|---|---|
| **Source IP** | `118.196.78.37` |
| **First Seen** | 2026-03-06T14:27:44.644937Z |
| **Last Seen** | 2026-03-06T14:29:44.706882Z |
| **Session Duration** | 120s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |
| **TTPs (MITRE)** | T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-06 14:27:44` | `cowrie.session.connect` |
| `2026-03-06 14:27:44` | `cowrie.client.version` |
| `2026-03-06 14:29:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `118.196.78.37`
- [ ] No immediate escalation required

### 🟢 LOW · IR-bdc51a28ba8f

| Field | Detail |
|---|---|
| **Source IP** | `57.151.129.39` |
| **First Seen** | 2026-03-06T17:40:38.698326Z |
| **Last Seen** | 2026-03-06T17:40:38.699189Z |
| **Session Duration** | 0s |
| **Login Attempts** | 0 |
| **Auth Success** | ❌ No |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-06 17:40:38` | `cowrie.session.connect` |
| `2026-03-06 17:40:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Monitor for repeat activity from `57.151.129.39`
- [ ] No immediate escalation required

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `120.157.18.252` | AU | Telstra Limited | **100** ⚠️ | 1 |
| `172.212.201.77` | US | Microsoft Limited | **100** ⚠️ | 50 |
| `20.124.87.15` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `118.196.78.37` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 30 |
| `192.109.200.213` | DE | Telco power Ltd | **100** ⚠️ | 0 |
| `57.151.129.39` | US | Microsoft Limited | **99** ⚠️ | 2 |
| `3.141.168.125` | US | Amazon Technologies Inc. | **99** ⚠️ | 9 |
| `64.236.193.16` | US | Microsoft Limited | **64** | 50 |
| `172.184.213.240` | US | Microsoft Limited | **38** | 0 |
| `93.123.109.222` | NL | TECHOFF_SRV_LIMITED | **32** | 7 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | — |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | — |
| [T1078](https://attack.mitre.org/techniques/T1078) | — |

---

## 🔕 False Positive Summary (30 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 22 |
| AbuseIPDB score 13 below threshold 25 | 1 |
| AbuseIPDB score 2 below threshold 25 | 2 |
| AbuseIPDB score 7 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05 | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26 | Incident Timeline Generator | ✅ 47 cases |
| Tool 27 | Threat Intel Feeder         | ✅ 35 IPs enriched |
| Tool 29 | False Positive Tracker      | ✅ 30 filtered (63.8%) |
| Tool 30 | Metric Exporter             | ✅ stats.json written |
| Tool 28 | SOC Handover Report         | ✅ This report |

---

## 📋 Standing Orders for Next Shift

- [ ] Verify honeypot is HEALTHY (Tool 05 green)
- [ ] Review any new HIGH/CRITICAL IR cases in `data/ir_cases.json`
- [ ] Check AbuseIPDB for newly reported IPs from this shift
- [ ] If Cowrie captures a download, run Tool 31 malware analyzer
- [ ] Integrity baseline auto-recreates every 2 hours via pipeline

---

_Generated by THIR · Tool 28 · SOC Handover Report Generator_  
_Pipeline: `nikhilsalunkemumbai/thir-live` · Cowrie SSH Honeypot · AWS EC2_  
_Report time: 2026-03-06T22:35:49Z_
