# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-26 |
| **Generated At** | 2026-03-26T10:52:01Z |
| **Shift Time** | 10:52 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **99** |
| Confirmed Threats | **76** |
| False Positives Filtered | **23** (23.2%) |
| Unique Attacker IPs | **53** |
| Countries of Origin | **19** |
| High Severity Cases | **4** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **95** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **58** |
| Unique Credential Pairs | **48** |
| Unique Usernames | **43** |
| Unique Passwords | **43** |
| Successful Auth Pairs | **4** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 4 |
| `gbase` | 3 |
| `gns3` | 3 |
| `mohammad` | 3 |
| `unknown` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `12345678` | 4 |
| `123456` | 3 |
| `123` | 3 |
| `gns3123` | 3 |
| `Mohammad123!` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `gbase` | `123` | 3 |
| `gns3` | `gns3123` | 3 |
| `mohammad` | `Mohammad123!` | 3 |
| `userdeploy` | `Userdeploy123` | 2 |
| `345gs5662d34` | `345gs5662d34` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `qwe123..` | `34.91.0.68` | 2026-03-26T09:55:59 |
| `root` | `3245gs5662d34` | `34.91.0.68` | 2026-03-26T09:56:03 |
| `root` | `Server@123` | `121.196.193.211` | 2026-03-26T10:09:09 |
| `root` | `3245gs5662d34` | `121.196.193.211` | 2026-03-26T10:09:13 |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **1** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `34.91.0.68`, `121.196.193.211`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **53** |
| Unique ASNs | **38** |
| High-Risk ASNs | **26** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4837` | CHINA UNICOM China169 Backbone | 6 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 4 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 3 | HIGH |
| `AS22773` | Cox Communications Inc. | 3 | MEDIUM |
| `AS3786` | LG DACOM Corporation | 2 | HIGH |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 2 | HIGH |
| `AS396982` | Google LLC | 2 | HIGH |
| `AS56041` | China Mobile communications corporation | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (4)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-8312cebc4358

| Field | Detail |
|---|---|
| **Source IP** | `34.91.0[.]68` |
| **First Seen** | 2026-03-26 09:55 |
| **Last Seen** | 2026-03-26 09:56 |
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
| `2026-03-26 09:55:58` | `cowrie.session.connect` |
| `2026-03-26 09:55:58` | `cowrie.client.version` |
| `2026-03-26 09:55:58` | `cowrie.client.kex` |
| `2026-03-26 09:55:59` | `cowrie.login.success` |
| `2026-03-26 09:55:59` | `cowrie.session.params` |
| `2026-03-26 09:55:59` | `cowrie.command.input` |
| `2026-03-26 09:55:59` | `cowrie.command.failed` |
| `2026-03-26 09:55:59` | `cowrie.log.closed` |
| `2026-03-26 09:56:00` | `cowrie.session.params` |
| `2026-03-26 09:56:00` | `cowrie.command.input` |
| `2026-03-26 09:56:00` | `cowrie.session.file_download` |
| `2026-03-26 09:56:00` | `cowrie.log.closed` |
| `2026-03-26 09:56:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.91.0[.]68` to AbuseIPDB if not already reported
- [ ] Block `34.91.0[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-923c8535d11a

| Field | Detail |
|---|---|
| **Source IP** | `34.91.0[.]68` |
| **First Seen** | 2026-03-26 09:56 |
| **Last Seen** | 2026-03-26 09:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-26 09:56:02` | `cowrie.session.connect` |
| `2026-03-26 09:56:02` | `cowrie.client.version` |
| `2026-03-26 09:56:02` | `cowrie.client.kex` |
| `2026-03-26 09:56:03` | `cowrie.login.success` |
| `2026-03-26 09:56:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.91.0[.]68` to AbuseIPDB if not already reported
- [ ] Block `34.91.0[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-675851325167

| Field | Detail |
|---|---|
| **Source IP** | `121.196.193[.]211` |
| **First Seen** | 2026-03-26 10:09 |
| **Last Seen** | 2026-03-26 10:09 |
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
| `2026-03-26 10:09:08` | `cowrie.session.connect` |
| `2026-03-26 10:09:08` | `cowrie.client.version` |
| `2026-03-26 10:09:08` | `cowrie.client.kex` |
| `2026-03-26 10:09:09` | `cowrie.login.success` |
| `2026-03-26 10:09:09` | `cowrie.session.params` |
| `2026-03-26 10:09:09` | `cowrie.command.input` |
| `2026-03-26 10:09:09` | `cowrie.command.failed` |
| `2026-03-26 10:09:09` | `cowrie.log.closed` |
| `2026-03-26 10:09:10` | `cowrie.session.params` |
| `2026-03-26 10:09:10` | `cowrie.command.input` |
| `2026-03-26 10:09:10` | `cowrie.session.file_download` |
| `2026-03-26 10:09:10` | `cowrie.log.closed` |
| `2026-03-26 10:09:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.196.193[.]211` to AbuseIPDB if not already reported
- [ ] Block `121.196.193[.]211` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-374d8e52cedc

| Field | Detail |
|---|---|
| **Source IP** | `121.196.193[.]211` |
| **First Seen** | 2026-03-26 10:09 |
| **Last Seen** | 2026-03-26 10:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-26 10:09:12` | `cowrie.session.connect` |
| `2026-03-26 10:09:12` | `cowrie.client.version` |
| `2026-03-26 10:09:12` | `cowrie.client.kex` |
| `2026-03-26 10:09:13` | `cowrie.login.success` |
| `2026-03-26 10:09:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.196.193[.]211` to AbuseIPDB if not already reported
- [ ] Block `121.196.193[.]211` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `103.56.30[.]33` | **5** | 2026-03-26 09:34 | 2026-03-26 09:46 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `112.132.249[.]164` | **5** | 2026-03-26 09:51 | 2026-03-26 09:58 | 7m | 0 | `T1592` | 🟢 LOW |
| `113.193.234[.]210` | **5** | 2026-03-26 09:55 | 2026-03-26 10:07 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `113.31.103[.]129` | **5** | 2026-03-26 09:53 | 2026-03-26 10:03 | 4m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `179.183.196[.]198` | **5** | 2026-03-26 09:49 | 2026-03-26 10:02 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `186.80.18[.]158` | **5** | 2026-03-26 09:48 | 2026-03-26 10:00 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `187.154.126[.]94` | **5** | 2026-03-26 09:55 | 2026-03-26 10:06 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `217.92.170[.]18` | **5** | 2026-03-26 09:38 | 2026-03-26 09:45 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `34.91.0[.]68` | **5** | 2026-03-26 09:47 | 2026-03-26 09:57 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.11[.]36` | **4** | 2026-03-26 09:50 | 2026-03-26 09:57 | 3m | 0 | `T1592` | 🟢 LOW |
| `47.103.157[.]194` | **2** | 2026-03-26 09:22 | 2026-03-26 09:23 | 0m | 0 | `T1592` | 🟢 LOW |
| `106.248.238[.]187` | 1 | 2026-03-26 09:04 | 2026-03-26 09:05 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.66.128[.]10` | 1 | 2026-03-26 09:35 | 2026-03-26 09:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `122.187.229[.]220` | 1 | 2026-03-26 09:30 | 2026-03-26 09:30 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `128.185.209[.]162` | 1 | 2026-03-26 09:08 | 2026-03-26 09:08 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.224.215[.]237` | 1 | 2026-03-26 10:11 | 2026-03-26 10:11 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `167.99.234[.]119` | 1 | 2026-03-26 08:55 | 2026-03-26 08:55 | 2s | 0 | `T1592` | 🟢 LOW |
| `176.65.148[.]214` | 1 | 2026-03-26 10:46 | 2026-03-26 10:46 | 30s | 0 | `T1592` | 🟢 LOW |
| `182.60.128[.]241` | 1 | 2026-03-26 09:27 | 2026-03-26 09:27 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `182.95.48[.]154` | 1 | 2026-03-26 09:25 | 2026-03-26 09:25 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.247.171[.]186` | 1 | 2026-03-26 08:54 | 2026-03-26 08:56 | 106s | 0 | `T1592` | 🟢 LOW |
| `186.23.209[.]47` | 1 | 2026-03-26 10:06 | 2026-03-26 10:06 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `203.219.162[.]18` | 1 | 2026-03-26 10:23 | 2026-03-26 10:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `207.254.29[.]22` | 1 | 2026-03-26 10:05 | 2026-03-26 10:05 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `210.182.73[.]132` | 1 | 2026-03-26 10:27 | 2026-03-26 10:27 | 9s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `222.100.159[.]2` | 1 | 2026-03-26 10:47 | 2026-03-26 10:47 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `35.202.9[.]133` | 1 | 2026-03-26 10:06 | 2026-03-26 10:07 | 40s | 0 | `T1592` | 🟢 LOW |
| `69.112.28[.]181` | 1 | 2026-03-26 10:27 | 2026-03-26 10:27 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `90.173.78[.]90` | 1 | 2026-03-26 10:32 | 2026-03-26 10:32 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `91.144.158[.]62` | 1 | 2026-03-26 10:48 | 2026-03-26 10:48 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `92.119.96[.]55` | 1 | 2026-03-26 09:46 | 2026-03-26 09:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `95.53.200[.]223` | 1 | 2026-03-26 09:46 | 2026-03-26 09:46 | 11s | 0 | `T1592` | 🟢 LOW |

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
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 10/100 | 🟢 LOW | **27/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `92.119.96[.]55` | ES | ASPWIFI S.L. | **100** ⚠️ | 3 |
| `182.60.128[.]241` | IN | Mahanagar Telephone Nigam Limited | **100** ⚠️ | 1 |
| `103.56.30[.]33` | IN | Balaji Online | **100** ⚠️ | 50 |
| `187.154.126[.]94` | MX | UNINET | **100** ⚠️ | 21 |
| `179.183.196[.]198` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 6 |
| `167.99.234[.]119` | US | DigitalOcean, LLC | **100** ⚠️ | 23 |
| `113.31.103[.]129` | CN | Shanghai UCloud Information Technology Company Limited | **100** ⚠️ | 50 |
| `47.103.157[.]194` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 50 |
| `186.80.18[.]158` | CO | Telmex Colombia S.A. | **100** ⚠️ | 50 |
| `122.187.229[.]220` | IN | BHARTI TELENET LTD. NEW DELHI | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 74 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 53 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 4 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 2 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |

---

## 🔕 False Positive Summary (23 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 4 |
| AbuseIPDB score 7 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 14 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 99 cases |
| Tool 34  | Credential Extractor        | ✅ 58 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 53 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 23 filtered (23.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 38 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 4 priority case(s) shown individually · 32 recon entry/entries in table (11 group(s) consolidating 51 session(s)).

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
_Report time: 2026-03-26T10:52:01Z_
